# Signal Garden

[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#)

> *The scientist must put things in order; science is built with facts as a house is built with stones, but an accumulation of facts is no more a science than a heap of stones is a house.*
>
> <div align="right">— Henri Poincaré</div>

<!-- epigraph-curator
framing-intent: Useful observability comes from structuring evidence into decisions, not accumulating more events.
source-author: Henri Poincaré
source-work: La Science et l’Hypothèse
source-locator: part IV, chapter IX
source-url: https://fr.wikisource.org/wiki/La_Science_et_l%E2%80%99Hypoth%C3%A8se/Chapitre_9
source-quotation: |
  Le savant doit ordonner ; on fait la science avec des faits comme une maison avec des pierres ; mais une accumulation de faits n’est pas plus une science qu’un tas de pierres n’est une maison.
semantic-invariant: Information becomes knowledge through ordered relations, not accumulation alone.
rendering: translation
display: document-language-only
translation: Epigraph Curator rendering
adaptation: none
rationale: Poincaré turns the project's preference for structured signals over event volume into an architectural image.
-->

Signal Garden turns a noisy event stream into a small set of decisions that operators can trust.

It treats observability as an information-design problem: collect less, relate signals explicitly, and preserve the path from evidence to action.

## Principles

- Relationships matter more than event counts.
- Every alert should suggest a decision.
- Silence is useful only when it is explainable.
