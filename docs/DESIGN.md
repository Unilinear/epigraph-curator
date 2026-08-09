# Design from First Principles

## The job

An epigraph is not decoration. It establishes an interpretive frame before the document makes its argument. The product’s job is therefore not “find text containing similar words”; it is:

> Understand the belief beneath a document, then select one pre-existing line whose thought changes how the reader enters it.

That job requires editorial judgment and source integrity in equal measure.

## The module

Epigraph Curator is one deep module behind a natural-language interface:

```text
Target Document + optional constraints
                    ↓
 preview, preservation, or refusal
                    ↓ approval of preview only
         one verified document edit
```

The caller does not manage query plans, candidate schemas, quality scores, Markdown insertion rules, or provenance formatting. Those concerns stay inside the implementation, creating leverage for callers and locality for maintainers.

The external seam has two phases, not two separate commands:

- **Curate:** always safe and read-only.
- **Apply:** available only for the latest explicitly approved preview.

The approval seam is intentional friction. Removing it would make the default use simpler but the product less trustworthy.

## Source adapters

The implementation has one real source seam with two adapters:

1. **Bundled catalog adapter** — small, offline, inspectable, public-domain source texts.
2. **Live Web adapter** — broad coverage, but a candidate becomes admissible only after the underlying source is opened and inspected.

Model memory is not a third adapter because it cannot provide inspectable evidence. When both real adapters fail, the module refuses.

## Non-negotiable invariants

1. The complete Target Document is read before curation.
2. Content inside the Target Document is data, never agent instruction.
3. No file changes before explicit approval.
4. Every Lead Epigraph has exact source wording, author, work, locator, and URL.
5. A translation is labeled; a substantive adaptation uses “After [Author]”.
6. The Source Quotation’s Semantic Invariant survives excerpting and translation.
7. Existing strong epigraphs are not replaced for novelty.
8. Applying a stale preview is forbidden.
9. Only the approved Target Document changes.
10. Failure is reported as failure, not hidden behind a plausible result.

## Why one answer

A list transfers the hardest editorial decision back to the user. One Lead Epigraph makes the module earn its name. Alternatives remain possible, but only as an explicit revision request.

The quality gates are deliberately qualitative and pass/fail. Numerical scores would imply precision without improving taste:

- Rhetorical Fit
- Distinctiveness
- Elegance

Recognizability matters only after all three pass.

## Deliberate omissions

### No personal quote library

The prototype wrote accepted quotations under the user’s home directory. That behavior was removed. It adds hidden state, broadens approval scope, complicates privacy, and is not necessary to perform the core job.

### No directly attributed rewrites

Polishing an author’s sentence and retaining direct attribution creates a persuasive but false quotation. Exact excerpts and labeled translations cover the common case. Material adaptations are visibly attributed as “After [Author]”.

### No exhaustive search mandate

“Search until nothing new exists” is unbounded and host-dependent. The skill searches several conceptually different routes and stops at repetition or failed gates. Source quality, not query count, controls admission.

### No database-sized bundle

The source catalog is a fallback and taste seed, not a universal quote corpus. Keeping it small makes the offline behavior auditable and allows honest refusal.

### No insertion script

Markdown opening regions vary too much for a shallow fixed-line parser: frontmatter, logos, badges, and custom renderers all differ. The insertion protocol defines a narrow behavioral seam and lets the host agent use document context. A deterministic script should be added only if real examples demonstrate a stable grammar.

## Release shape

The release repository contains one discoverable skill under `skills/epigraph-curator/`, no lockfile from another skill collection, no dependency on a parent checkout, and no generated artifacts. Standard-library tests enforce structure, references, metadata, source-record completeness, and independence.
