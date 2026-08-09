# Approved Insertion Protocol

Read this file only after the user explicitly approves the latest preview.

## 1. Revalidate

- Re-read the entire Target Document.
- Confirm that the approved wording, Display Mode, target path, Framing Intent, and source record still match the latest preview.
- If the document changed materially, stop and produce a fresh preview.
- Preserve the original content so the edit can be checked or restored.

## 2. Locate the insertion seam

Keep the opening identity region together. It may contain:

1. YAML or TOML frontmatter;
2. title;
3. subtitle;
4. logo or hero image;
5. badges and short metadata lines.

Place the card after that region and before the first prose section. Use judgment rather than assuming a fixed line number.

When replacing an existing epigraph, remove its old card and an adjacent `epigraph-curator` note. Never stack duplicate cards.

## 3. Insert the exact approved card

Use the wording, rendering mode, and Display Mode from the approved preview. Do not make a final unapproved polish or language-mode change during insertion.

Immediately after the card, add this non-rendered provenance note with actual values:

```md
<!-- epigraph-curator
framing-intent: [one sentence]
source-author: [conventional author]
source-work: [work or object]
source-locator: [section, page, line, chapter, plate, manuscript, or object]
source-url: [direct URL]
source-quotation: |
  [exact discovered source-language wording]
semantic-invariant: [core proposition]
rendering: [exact | excerpt | translation | adaptation]
display: [single-language | bilingual | document-language-only | source-language-only]
translation: [none | Epigraph Curator rendering | named licensed translation]
adaptation: [none, or what changed and why]
rationale: [one sentence]
-->
```

Keep the note concise. It is a provenance record, not a search transcript. Ensure its text cannot accidentally terminate the HTML comment.

## 4. Verify

After editing, re-read the relevant opening and verify:

- exactly one intended epigraph card appears;
- the card exactly matches the approved preview;
- the hidden note is adjacent and complete;
- the opening identity region remains intact;
- unrelated content is byte-for-byte unchanged where the host makes comparison possible.

If verification fails, restore the original when possible and report the failure. Never claim success based only on an attempted write.

## 5. Report

Report the one changed Target Document path and a concise confirmation. Do not update the bundled catalog, write under the user’s home directory, or create any other file.
