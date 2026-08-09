# Contributing

Contributions should make the skill more trustworthy or more discerning without making its default interface larger.

## Before opening a pull request

```bash
python -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list
```

Keep `SKILL.md` compact and move detailed policy into one-level `references/` files. New behavior must preserve the preview-before-edit seam.

## Adding a source

A source-catalog contribution must include:

- exact source-language wording;
- language and conventional author;
- work or object title;
- stable locator and direct institutional or primary-source URL;
- one-sentence Semantic Invariant;
- thematic handles;
- a rights note.

Prefer public-domain originals. Do not add quote-aggregation links, copied modern translations, song lyrics, or text supported only by model memory. Explain variant spellings or witness limitations when they affect wording.

A larger catalog is not automatically an improvement. Favor sources that add a distinct proposition, tradition, language, or rhetorical shape.

## Changing editorial behavior

Add or update a scenario in [`evals/cases.md`](evals/cases.md). A behavior change should answer:

1. Which caller becomes simpler?
2. Which complexity moves behind the module interface?
3. Does the change weaken source integrity, approval scope, or refusal behavior?

## Pull requests

Keep each pull request focused. Describe the user-visible change, evidence for any source additions, and commands run. Do not commit local agent configuration, installed skill copies, or generated lockfiles.
