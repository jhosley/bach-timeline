# Content Schema

Every content item is a markdown file with YAML frontmatter. The frontmatter carries the structured fields the timeline app will consume; the markdown body carries the museum-placard narrative. This document is the single source of truth for the content model.

## Shared conventions

- **Filenames** are the item's `id` plus `.md` (e.g. `bwv-1046.md`).
- **Dates** use ISO form (`1721-03-24`) at whatever precision is known, with `date_precision` declaring how much to trust the digits: `day` | `month` | `year` | `circa`.
- **`provenance`** (required on events; on works it qualifies the *dating*): 
  - `documented` — surviving primary records (council minutes, letters, receipts, autograph dates)
  - `tradition` — from early secondary accounts (the 1750 Obituary, Forkel) that may be embellished
  - `disputed` — scholarship actively disagrees; the body must explain the disagreement
- **Cross-links** use item ids. A referenced id that doesn't exist yet is allowed — it marks planned content.
- **`sources`** are short human-readable citations (author, title, chapter). Precise page/document numbers are added during the R6 verification pass.

## `type: event` — a moment on the timeline

```yaml
---
id: brandenburg-dedication-1721
type: event
arc: life                  # life | eclipse-rediscovery | living-bach
era: cothen                # eisenach ohrdruf lueneburg arnstadt muehlhausen weimar
                           # cothen leipzig-1 leipzig-2 leipzig-3
                           # eclipse revival living-bach
date: 1721-03-24
date_precision: day
date_end:                  # optional, for spans
tracks: [works]            # positions | family | works | craft | world
title: "Bach dedicates the Brandenburg Concertos"
place: cothen
provenance: documented
people: [christian-ludwig-brandenburg]
related_works: [brandenburg-concertos]
related_events: [berlin-harpsichord-1719]
sources:
  - "Wolff, The Learned Musician, ch. 7"
summary: >
  One or two sentences shown on the timeline hover/preview.
---

Body: the full museum-placard narrative, 150–400 words.
End with a **Why it matters** paragraph when the study relevance isn't obvious.
```

## `type: work` — a featured composition (or set)

```yaml
---
id: bwv-1046
type: work
bwv: "1046"                # string; ranges allowed for sets ("1046–1051")
title: "Brandenburg Concerto No. 1 in F major"
genre: orchestral          # cantata-sacred | cantata-secular | motet | passion-oratorio
                           # mass | keyboard | organ | orchestral | chamber
                           # contrapuntal | pedagogical
key: "F major"
forces: "2 horns, 3 oboes, bassoon, violino piccolo, strings, continuo"
era: cothen
place: cothen
date_composed: 1721
date_precision: circa
dating_note: ""            # required when dating is disputed/revised
occasion: ""               # liturgical date, court event, pedagogy, etc.
tier: full                 # full = own card | set = umbrella card for a collection
                           # listed = named in a set's roster, no own file
set: brandenburg-concertos # id of the umbrella card this belongs to, if any
provenance: documented
craft_tags: [ritornello, concerto-grosso]
recording:
  performer: "..."
  album: "..."
  year: 2009
  url: null                # curated & verified in R6
score_imslp: null          # verified in R6
related_events: [brandenburg-dedication-1721]
sources:
  - "..."
---

Body sections, in order (omit any that don't apply):
**What it is** — one paragraph.
**Listen for** — the study-companion heart of the card.
**Craft** — contrapuntal/structural notes, cross-linking craft essays.
**Dating** — only when `dating_note` is set; explain the scholarship.
```

## `type: person`

```yaml
---
id: anna-magdalena-bach
type: person
name: "Anna Magdalena Bach, née Wilcke"
born: 1701
died: 1760
relationship: "Second wife"
related_events: [...]
sources: [...]
---
Body: a short portrait, 150–350 words.
```

## `type: place`

```yaml
---
id: cothen
type: place
name: "Cöthen (Köthen), Anhalt-Cöthen"
coordinates: [51.75, 11.97]
bach_years: "1717–1723"
role: "Kapellmeister to Prince Leopold of Anhalt-Cöthen"
related_events: [...]
sources: [...]
---
Body: the town then, the court/church, what survives today, journeys from here.
```

## `type: era` — the "room introduction" essay

```yaml
---
id: cothen
type: era
arc: life
title: "Cöthen: the instrumental golden age"
years: "1717–1723"
---
Body: 500–900 words, warmer essayistic voice. Sets the scene, names the tension
of the period, and tells the reader what to go look at.
```
