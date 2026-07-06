# The Bach Timeline

An interactive, visual timeline of Johann Sebastian Bach's life, works, craft, and afterlife (1685 → present) — a personal study companion.

**Owner:** James Edmund Hosley II
**Status:** Content phase R1 (Cöthen pilot era) — see [PRD.md](PRD.md) for the full plan.

## Repository layout

```
PRD.md                  The approved product requirements document
content/
  SCHEMA.md             Content model — read this before adding/editing content
  eras/                 One overview essay per era (the "room introduction" text)
  events/<era>/         One file per timeline event
  works/<era>/          One file per featured work (or work-set)
  people/               One file per person in Bach's orbit
  places/               One file per principal town
```

All content is plain markdown with YAML frontmatter — reviewable in any editor, tool-agnostic, and consumed later by the static-site build (GitHub Pages).

## Content principles

1. **Provenance honesty** — every item is flagged `documented`, `tradition`, or `disputed`.
2. **Context first** — every work links to the life events that explain it, and vice versa.
3. **Voice** — museum-placard voice for cards; warmer essayistic voice for era introductions and craft essays.
4. **Links** — recording/score URLs are curated and verified in phase R6; until then they are named but `url: null`.
