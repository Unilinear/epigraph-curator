# Releasing

## Prepare

1. Run `git rev-parse --show-toplevel` and confirm that it resolves to this repository—not a parent checkout.
2. Update `metadata.version` in `skills/epigraph-curator/SKILL.md`.
3. Add the release date and changes to `CHANGELOG.md`.
4. Check every new source record against the source and attribution policy.
5. Run:

   ```bash
   python -m unittest discover -s tests -v
   PYTHONUTF8=1 uvx --from 'git+https://github.com/agentskills/agentskills#subdirectory=skills-ref' skills-ref validate skills/epigraph-curator
   npx --yes skills@1.5.22 add . --list
   ```

6. Inspect `git status` and confirm there are no caches, local settings, credentials, symlinks, or parent-repository files.

## Publish the repository

For the first public release:

```bash
gh repo create Unilinear/epigraph-curator --public --source=. --remote=origin --push
git tag -a v1.0.0 -m "Epigraph Curator v1.0.0"
git push origin v1.0.0
```

For later releases, create the version tag after the release commit and push it.

## Verify distribution

From outside the checkout:

```bash
npx skills add Unilinear/epigraph-curator --list
npx skills add Unilinear/epigraph-curator --skill epigraph-curator
```

Confirm that exactly one skill is discovered and that its bundled references are installed with it.

## Release notes

Describe user-visible behavior, source-policy changes, and any compatibility changes. Never market a larger catalog as better curation by itself.
