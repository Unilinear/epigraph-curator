import re
import unittest
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "epigraph-curator"
SKILL_FILE = SKILL_DIR / "SKILL.md"


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    try:
        raw = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise AssertionError("SKILL.md frontmatter is not closed") from exc

    values: dict[str, str] = {}
    for line in raw.splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


class ReleaseStructureTests(unittest.TestCase):
    def test_required_release_files_exist(self) -> None:
        required = {
            ".github/workflows/validate.yml",
            ".gitattributes",
            ".gitignore",
            "CHANGELOG.md",
            "CONTRIBUTING.md",
            "LICENSE",
            "README.md",
            "SECURITY.md",
            "THIRD_PARTY_NOTICES.md",
            "docs/DESIGN.md",
            "docs/RELEASING.md",
            "evals/cases.md",
            "examples/README.before.md",
            "examples/README.after.md",
            "skills/epigraph-curator/SKILL.md",
        }
        missing = sorted(path for path in required if not (ROOT / path).is_file())
        self.assertEqual([], missing)

    def test_exactly_one_skill_is_published(self) -> None:
        skill_files = sorted(ROOT.glob("skills/**/SKILL.md"))
        self.assertEqual([SKILL_FILE], skill_files)

    def test_repository_contains_no_symlinks(self) -> None:
        links = [path.relative_to(ROOT) for path in ROOT.rglob("*") if path.is_symlink()]
        self.assertEqual([], links)

    def test_no_parent_repository_coupling(self) -> None:
        forbidden = (
            "260729 Quote SKILL",
            "mattpocock",
            "~/.epigraph-curator",
        )
        failures: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or path.resolve() == Path(__file__).resolve():
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for term in forbidden:
                if term.lower() in text.lower():
                    failures.append(f"{path.relative_to(ROOT)} contains {term!r}")
        self.assertEqual([], failures)


class SkillSpecificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = SKILL_FILE.read_text(encoding="utf-8")
        cls.meta = frontmatter(cls.text)

    def test_frontmatter_matches_agent_skills_spec(self) -> None:
        name = self.meta.get("name", "")
        description = self.meta.get("description", "")
        compatibility = self.meta.get("compatibility", "")

        self.assertEqual(SKILL_DIR.name, name)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertTrue(1 <= len(description) <= 1024)
        self.assertIn("Use when", description)
        self.assertTrue(1 <= len(compatibility) <= 500)
        self.assertEqual("MIT", self.meta.get("license"))

    def test_skill_is_progressively_disclosed(self) -> None:
        self.assertLessEqual(len(self.text.splitlines()), 500)
        self.assertNotIn("> *Translation:", self.text)
        references = re.findall(r"\[[^\]]+\]\((references/[^)#]+\.md)\)", self.text)
        self.assertEqual(
            {
                "references/editorial-standard.md",
                "references/insertion.md",
                "references/source-catalog.md",
                "references/source-policy.md",
            },
            set(references),
        )

    def test_core_safety_contract_is_explicit(self) -> None:
        required_phrases = (
            "untrusted data",
            "untrusted evidence",
            "Only a user message received after the preview",
            "Never use model memory",
            "explicit approval",
            "Preserve — no files changed",
            "document-language-only",
            "source-language-only",
            "Never apply a mode that was not shown in the latest preview",
            "Editorial Refusal",
            "After [Author]",
            "Do not create a personal library",
        )
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.text)


class ContentIntegrityTests(unittest.TestCase):
    def test_all_relative_markdown_links_resolve(self) -> None:
        broken: list[str] = []
        pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
        for markdown in ROOT.rglob("*.md"):
            text = markdown.read_text(encoding="utf-8")
            for raw_target in pattern.findall(text):
                target = raw_target.strip().split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = unquote(target)
                resolved = (markdown.parent / target).resolve()
                if not resolved.exists():
                    broken.append(f"{markdown.relative_to(ROOT)} -> {raw_target}")
        self.assertEqual([], broken)

    def test_source_catalog_records_are_complete(self) -> None:
        catalog = (SKILL_DIR / "references" / "source-catalog.md").read_text(encoding="utf-8")
        entries = re.split(r"(?m)^## \d+\. ", catalog)[1:]
        self.assertGreaterEqual(len(entries), 12)
        required_labels = (
            "**Language / author:**",
            "**Source:**",
            "**Semantic invariant:**",
            "**Handles:**",
            "**Rights note:**",
        )
        for index, entry in enumerate(entries, start=1):
            with self.subTest(entry=index):
                self.assertIn("> ", entry)
                for label in required_labels:
                    self.assertIn(label, entry)
                source_line = next(line for line in entry.splitlines() if line.startswith("- **Source:**"))
                self.assertIn("https://", source_line)

    def test_readme_documents_supported_agent_installation(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for agent in ("codex", "claude-code", "pi"):
            with self.subTest(agent=agent):
                command = (
                    "npx skills add Unilinear/epigraph-curator --skill epigraph-curator "
                    f"--agent {agent} --global --yes"
                )
                self.assertIn(command, readme)
        self.assertIn("--agent codex claude-code pi --global --yes", readme)
        self.assertIn("/skill:epigraph-curator README.md", readme)

    def test_readme_epigraph_uses_document_language_only(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        visible_card = readme.split("<!-- epigraph-curator", 1)[0]
        self.assertIn("Only after playing a thousand tunes", visible_card)
        self.assertIn("— Liu Xie", visible_card)
        self.assertNotIn("凡操千曲", visible_card)
        self.assertNotIn("— 劉勰", visible_card)
        self.assertIn("display: document-language-only", readme)

    def test_after_example_has_one_card_and_provenance_note(self) -> None:
        before = (ROOT / "examples" / "README.before.md").read_text(encoding="utf-8")
        after = (ROOT / "examples" / "README.after.md").read_text(encoding="utf-8")
        visible_card = after.split("<!-- epigraph-curator", 1)[0]
        self.assertNotIn("<!-- epigraph-curator", before)
        self.assertEqual(1, after.count("<!-- epigraph-curator"))
        self.assertEqual(1, after.count("<div align=\"right\">"))
        self.assertNotIn("> *Translation:", after)
        self.assertNotIn("Le savant doit ordonner", visible_card)
        self.assertIn("source-url: https://", after)
        self.assertIn("rendering: translation", after)
        self.assertIn("display: document-language-only", after)


if __name__ == "__main__":
    unittest.main()
