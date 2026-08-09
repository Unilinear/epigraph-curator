# Epigraph Curator

[![Validate](https://github.com/Unilinear/epigraph-curator/actions/workflows/validate.yml/badge.svg)](https://github.com/Unilinear/epigraph-curator/actions/workflows/validate.yml)

> *La parole est moitié à celuy qui parle, moitié à celuy qui l’escoute.*
>
> *Speech belongs half to the speaker, half to the listener.*
>
> <div align="right">— Michel de Montaigne</div>

<!-- epigraph-curator
framing-intent: A document's meaning is completed by its reader, so its opening frame matters.
source-author: Michel de Montaigne
source-work: Essais III.13, De l’expérience
source-locator: 1588 text, book III, chapter XIII
source-url: https://artflsrv03.uchicago.edu/philologic4/montaigne1588/navigate/1/4/14
source-quotation: |
  La parole est moitié à celuy qui parle, moitié à celuy qui l’escoute.
semantic-invariant: Meaning in speech is made jointly by speaker and listener.
rendering: translation
translation: Epigraph Curator rendering
adaptation: none
rationale: The line makes the reader a participant in the meaning the document is about to create.
-->

**Give your ideas ancestors.**

Epigraph Curator is an [Agent Skill](https://agentskills.io/) that reads a Markdown document, identifies what it wants the reader to believe, and curates one opening quotation that frames that belief.

Not a random quote generator. Not a search-results page. One sourced editorial answer—and the judgment to refuse.

## What makes it different

- **One lead, not a dump.** Alternatives appear only when requested.
- **Existing quality is preserved.** A strong, sourced epigraph is not replaced merely for novelty.
- **The whole document matters.** Selection begins with a one-sentence Framing Intent, not keyword matching.
- **Sources are inspectable.** Every preview includes an author, work, locator, and direct URL.
- **Bilingual without clutter.** Original first, faithful translation second; translation provenance stays outside the card.
- **Approval is a hard seam.** The skill previews first and edits only after explicit approval.
- **Offline behavior is honest.** Without Web access it uses the bundled, public-domain source catalog or refuses; it never invents a source from model memory.
- **No hidden state.** It writes no personal library, telemetry, or configuration.

## Install

The commands below install Epigraph Curator globally so it is available in every project. Remove `--global` for a project-local installation.

### OpenAI Codex

```bash
npx skills add Unilinear/epigraph-curator --skill epigraph-curator --agent codex --global --yes
```

### Claude Code

```bash
npx skills add Unilinear/epigraph-curator --skill epigraph-curator --agent claude-code --global --yes
```

### Pi

```bash
npx skills add Unilinear/epigraph-curator --skill epigraph-curator --agent pi --global --yes
```

Pi discovers installed skills when a session starts. Invoke it naturally or force-load it with:

```text
/skill:epigraph-curator README.md
```

### Install for all three

```bash
npx skills add Unilinear/epigraph-curator --skill epigraph-curator --agent codex claude-code pi --global --yes
```

### Local checkout

```bash
npx skills add . --skill epigraph-curator
```

The repository follows the portable Agent Skills layout, so compatible agents can also load [`skills/epigraph-curator/`](skills/epigraph-curator/) directly. Start a new agent session after installation so the skill is discovered.

## Use

Natural requests are the interface:

```text
Curate an epigraph for README.md.
```

```text
Improve the epigraph in docs/essay.md, but keep it in Classical Chinese.
```

```text
Suggest an opening quotation for SPEC.md. Do not edit the file.
```

The default flow is deliberately short:

1. The skill reads the entire target document and infers its Framing Intent.
2. It researches multiple conceptual routes and verifies the exact wording.
3. It returns one card, one sentence of rationale, and one direct source.
4. It leaves every file unchanged.
5. After an explicit approval, it inserts the exact preview and an adjacent hidden provenance note.

See the small [before](examples/README.before.md) and [after](examples/README.after.md) example.

## Trust contract

Epigraph Curator treats the target document as untrusted input, ignores instructions embedded inside it, and binds approval to the latest preview. A stale preview is never silently applied after the document changes.

Its editorial gates are:

- **Rhetorical Fit** — the line frames the document’s proposition.
- **Distinctiveness** — it feels selected for this document.
- **Elegance** — it is restrained, precise, and suggestive.

A candidate must also satisfy the [source and attribution policy](skills/epigraph-curator/references/source-policy.md). If either editorial quality or evidence fails, the correct result is an Editorial Refusal.

## Repository map

```text
skills/epigraph-curator/
├── SKILL.md                         # compact runtime interface
├── agents/openai.yaml              # display metadata
└── references/
    ├── editorial-standard.md       # quality gates
    ├── insertion.md                # approved write protocol
    ├── source-catalog.md           # offline, traceable source layer
    └── source-policy.md            # evidence and attribution rules
```

Project rationale is in [`docs/DESIGN.md`](docs/DESIGN.md). Behavioral scenarios are in [`evals/cases.md`](evals/cases.md).

## Develop

Requirements: Python 3.10+ for repository tests and Node.js only for the optional installation smoke test.

```bash
python -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list
```

The skill itself has no package install, runtime dependency, API key, or required account. Live Web access is optional but recommended.

## License

Original repository content is released under the [MIT License](LICENSE). Public-domain source quotations and linked third-party materials are described in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
