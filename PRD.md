# The Bach Timeline — Product Requirements Document

**Project:** An interactive, visual timeline of Johann Sebastian Bach's life, works, craft, and afterlife
**Owner & Author:** James Edmund Hosley II (study companion to Juilliard studies of Bach's music)
**Status:** APPROVED — 2026-07-06
**Date:** 2026-07-06
**Home:** GitHub repository, deployed as a static site (GitHub Pages)

---

## 1. Vision

A single, beautiful place to answer the question every Bach student eventually asks about every piece: **"Why does this music exist?"**

The app presents Bach's story as a timeline floating in space — suspended among flowing, never-ending streams of music — signifying that what he set in motion in a 200-mile circle of central Germany never stopped sounding. Zooming into any moment opens a clean, museum-quality presentation: what happened, who was paying him, what the job demanded, what was happening at home, what he wrote, and why it matters to a musician studying it today.

This is a **study companion**, not a course and not an encyclopedia. It is optimized for the moment when you are working on a Bach piece and want its full context within two clicks.

### Goals

1. **Context engine** — connect every featured work to its biographical, professional, and theological circumstances.
2. **The full arc, not just the life** — Bach's story includes his eclipse after death and his rediscovery. The timeline runs from 1685 to the present.
3. **Counterpoint as the through-line** — Bach's lifelong deepening of contrapuntal craft is treated as its own narrative, not a footnote.
4. **A listening and score guide** — 200–300 featured works, each linked to a recording and a free score.
5. **Satisfying to look at** — the ethereal outer view should be something you *want* to open; the inner views should read like museum placards: calm, authoritative, uncluttered.

### Non-goals

- Not a public product; no accounts, no backend, no database.
- Not a complete BWV catalog (1,000+ works); depth over exhaustiveness, with grouped coverage where sets belong together.
- Not a performance-practice tutorial — we link to and summarize the interpreters; we don't teach technique.

---

## 2. The Three Grand Arcs

The timeline is organized as three eras, visually distinct but continuous:

### Arc I — The Life (1685–1750)

The core biography, told through parallel tracks (see §3). Ten periods anchor it:

1. **Eisenach (1685–1695)** — birth into the vast Bach musical clan; orphaned at 9.
2. **Ohrdruf (1695–1700)** — raised by his organist brother Johann Christoph; the (legendary) moonlight copying of forbidden scores; keyboard foundation.
3. **Lüneburg (1700–1702)** — choral scholarship at St. Michael's; exposure to the French style; formative organ influences (Böhm; trips to hear Reincken in Hamburg).
4. **Arnstadt (1703–1707)** — first organist post at 18; the 250-mile walk to Lübeck to hear Buxtehude (and the unauthorized four-month absence); the sword scuffle with the bassoonist Geyersbach; console complaints about his "strange harmonies" confusing the congregation.
5. **Mühlhausen (1707–1708)** — marriage to Maria Barbara; first cantata masterpieces (*Gott ist mein König*, BWV 71 — his only work printed in his lifetime as a cantata); caught between orthodox and Pietist factions.
6. **Weimar (1708–1717)** — court organist to the Duke; the great organ works; discovery of Vivaldi and the Italian concerto (transcriptions that rewired his sense of form); promotion to Konzertmeister with a monthly cantata duty; passed over for Kapellmeister; **one month in the Duke's jail** for insisting on his resignation.
7. **Cöthen (1717–1723)** — Kapellmeister to Prince Leopold, a Calvinist court needing no elaborate church music: hence the instrumental golden age — Brandenburgs, cello suites, violin sonatas & partitas, Well-Tempered Clavier I, the Inventions & Sinfonias for his students and children. Maria Barbara's sudden death (1720, while Bach was away); marriage to Anna Magdalena (1721); the court's musical decline after Leopold's marriage.
8. **Leipzig I — the cantata years (1723–1729)** — Thomaskantor (the town's third choice, after Telemann and Graupner declined). The staggering production rhythm: roughly a cantata *every week* for years — composed, copied, rehearsed, and performed in seven-day cycles. St. John Passion (1724), St. Matthew Passion (1727/29). Working conditions: teaching duties, four churches, an underfunded and under-strength ensemble (his famous 1730 memo to the council itemizing what proper church music actually requires).
9. **Leipzig II — Collegium and consolidation (1729–1741)** — direction of the Collegium Musicum (coffee-house concerts; the secular side of Bach); the harpsichord concertos; Clavier-Übung series; the Scheibe controversy (a public critic calling his style turgid and outdated — the era's taste shifting under his feet); the prefect dispute with Rector Ernesti; family losses and the sons leaving for their own careers.
10. **The summing-up (1741–1750)** — the late encyclopedic works: Goldberg Variations, WTC II, the visit to Frederick the Great at Potsdam (1747) and the *Musical Offering*, the B minor Mass assembled as a summa, *The Art of Fugue* left with its final fugue unfinished. Failing eyesight, the disastrous eye surgeries by the traveling oculist John Taylor, death on 28 July 1750.

**The family layer runs through all of this:** 7 children with Maria Barbara, 13 with Anna Magdalena — 10 of the 20 surviving to adulthood; the composer sons (Wilhelm Friedemann, Carl Philipp Emanuel, Johann Christoph Friedrich, Johann Christian) and what Bach's household teaching looked like (the Clavierbüchlein notebooks as documents of a father teaching).

### Arc II — Eclipse and Rediscovery (1750–1850)

The part most timelines skip, and one of the great stories in music history:

- **The estate scattered (1750s)** — manuscripts divided among heirs; Anna Magdalena dies in poverty (1760); Wilhelm Friedemann sells off cantata manuscripts; significant works lost forever.
- **"Old Bach," the learned relic** — for decades Bach is remembered mainly as a keyboard virtuoso and pedagogue; his style considered old-fashioned; his sons (especially C.P.E. and the "London Bach," Johann Christian) are the famous Bachs. Yet the WTC circulates in manuscript among connoisseurs like samizdat.
- **The keepers of the flame** — Baron van Swieten's Vienna salon feeding Bach manuscripts to Mozart and Haydn; **Mozart hearing the motet *Singet dem Herrn* at the Thomaskirche in 1789** ("Now, there is something one can learn from!") and studying the counterpoint; Beethoven raised on the WTC, punning that Bach ("brook") should have been named *Meer* ("sea"); Forkel's first biography (1802), openly nationalist in motive.
- **The 1829 resurrection** — 20-year-old **Felix Mendelssohn** conducts the St. Matthew Passion at the Berlin Singakademie, the first performance since Bach's death — cut, re-orchestrated, and a sensation ("it took an actor's son and a young Jew to restore the greatest Christian music to the world," as Mendelssohn wryly noted). The event that relaunches Bach into the public canon.
- **The monument built (1850)** — founding of the Bach-Gesellschaft on the centenary of his death; the 46-volume complete edition begins; Schumann and Brahms among the subscribers.

### Arc III — The Living Bach (1850–present)

How each era remakes Bach in its own image — presented as a gallery of interpreters and moments rather than a dense event stream:

- **The Romantic Bach** — massed choirs, piano transcriptions (Liszt, Busoni), Bach as cathedral.
- **Schweitzer and Casals** — Albert Schweitzer's 1905 study reading the cantatas as pictorial theology; Pablo Casals discovering the cello suites in a Barcelona junk shop and making them central repertoire.
- **The modernists' Bach** — Bach as pure structure; Webern's orchestration of the six-part ricercar; Glenn Gould's 1955 Goldberg Variations.
- **The historically informed performance (HIP) revolution** — Harnoncourt and Leonhardt's complete cantata cycle on period instruments (1971–1989); the debate over one-voice-per-part (Rifkin, Parrott).
- **The modern voices** *(per your request, treated in depth)* — **John Eliot Gardiner**: the Bach Cantata Pilgrimage (2000) performing all the sacred cantatas on their liturgical dates across Europe, and his book *Music in the Castle of Heaven* (2013), which the app will draw on for its humanizing, sometimes irreverent portrait of Bach (the unruly schoolboy, the fractious employee, the visceral theologian); **Masaaki Suzuki** and Bach Collegium Japan's complete cantata recordings; **Ton Koopman**; **Angela Hewitt**, **András Schiff** on the keyboard works.
- **Bach beyond the concert hall** — the Voyager Golden Record carrying three Bach works into interstellar space (a literal version of the app's "music flowing into forever" theme — worth featuring prominently).

---

## 3. Timeline Tracks (Arc I structure)

Within the Life arc, parallel horizontal tracks share one time axis. Toggleable:

| Track | Content |
|---|---|
| **Positions** | Colored era bands: employer, title, salary (with modern purchasing-power context), duties, working conditions, disputes |
| **Family** | Births, marriages, deaths, the sons' departures; the emotional weather of the household |
| **Works** | Featured works plotted at composition date, color-coded by genre; sets shown as clustered groups (e.g., the 1724–25 chorale cantata cycle as one shimmering band, not 52 dots) |
| **Craft** | Milestones in his contrapuntal development (see §4) |
| **World** | Context: births/deaths of Handel, Scarlatti, Telemann, Vivaldi; wars, rulers, the coffee craze, the state of "Germany" as 300 statelets |

The insight the design must deliver: **vertical reading**. Click 1723 and see, aligned in one glance, the new Leipzig job, its brutal weekly cantata cycle, the family moving into the Thomasschule, and the works pouring out.

---

## 4. The Craft Section — Counterpoint as Bach's Engine

A dedicated section (also woven into the timeline as the Craft track), treating what you asked for: the contrapuntal theory Bach embraced, developed, and encoded into his teaching works. Written to be readable by a musically literate non-specialist — every term defined the first time it's used.

**Essays planned (each ~1,000–1,500 words, with linked musical examples):**

1. **What counterpoint is and why it mattered** — independent melodic lines that also make harmony; the inheritance from Palestrina through the German organ tradition; why Bach's contemporaries were abandoning it for lighter *galant* textures while he doubled down.
2. **The Inventions & Sinfonias as a method** — Bach's own title page (1723) is a mission statement: to teach "a cantabile style of playing" and "a strong foretaste of composition." Two-part and three-part thinking as the foundation; how each invention grows from a single idea (the *inventio* of classical rhetoric).
3. **Fugue: the discipline** — subject, answer, countersubject, episode, stretto — defined and illustrated; why the WTC's traversal of all 24 keys was both a technical demonstration (new tuning systems) and an encyclopedia of what fugue could be.
4. **Canon: the strictest game** — from the Goldberg canons (every third variation, at successively wider intervals) to the riddle canons of the Musical Offering.
5. **The chorale as classroom** — four-part chorale harmonization as the distilled core of his teaching (and still the core of harmony pedagogy today, including in your own studies); how the 371 chorales became the universal textbook.
6. **Counterpoint as theology** — the view (Gardiner is eloquent here) that for Bach, ordered independent voices cohering into harmony was a picture of divine order; *Soli Deo Gloria* on the scores.
7. **The late summa** — Art of Fugue, Musical Offering, the Canonic Variations: Bach systematically writing the complete book on his own craft as the world moved on.

Each essay cross-links to the featured works that embody it, and each relevant work card links back.

---

## 5. The Works Catalog (~250–300 featured works)

Organized by genre, each work getting a **work card**: BWV number, date & place, occasion/purpose, a "what to listen for" paragraph, craft notes where relevant, one recommended recording link, one score link (IMSLP), and cross-links to timeline events.

**Coverage plan by genre** (counts are targets, refined during research):

| Genre | Featured | Approach |
|---|---|---|
| **Sacred cantatas** | ~60–70 individually + all ~200 listed | The masterpieces and study-essential cantatas get full cards (BWV 4, 21, 82, 106, 140, 147…); the annual cycles presented as navigable groups with the full surviving list, so nothing is invisible even if not all get essays |
| **Secular cantatas** | ~10 | Coffee Cantata, Peasant Cantata, Hunt Cantata, the Leipzig homage works |
| **Motets** | all 6–7 | Including *Singet dem Herrn* (the one Mozart heard) |
| **Passions & oratorios** | all | St. Matthew, St. John (with its multiple versions), the lost St. Mark; Christmas, Easter, Ascension oratorios |
| **Masses & Magnificat** | all | B minor Mass (with its assembly history — a career-spanning anthology), the 4 Lutheran (Kyrie–Gloria) masses, Magnificat in both versions |
| **Inventions & Sinfonias** | all 30 | Per your request: each of the 15+15 gets a short card (key, core idea, craft point); the set gets a collective essay |
| **WTC I & II** | all 48 | Each prelude–fugue pair gets a short card; landmark pairs get full treatment |
| **Other keyboard** | ~35 | Goldbergs (with variation-by-variation guide), partitas, English & French suites, Italian Concerto, toccatas, Chromatic Fantasy |
| **Organ** | ~30 | The great preludes/toccatas/fantasias & fugues, Orgelbüchlein (as a group with highlights), the "Great Eighteen," Passacaglia in C minor, trio sonatas, Schübler chorales |
| **Orchestral** | all | 6 Brandenburgs, 4 orchestral suites, violin & keyboard concertos |
| **Chamber & solo strings** | all major | 6 cello suites, 6 violin sonatas & partitas (Chaconne featured), flute sonatas, gamba sonatas, trio sonatas |
| **Late contrapuntal** | all | Art of Fugue, Musical Offering, Canonic Variations, 14 canons |

**Listening links policy:** one carefully chosen recommendation per work (favoring the interpreters from Arc III — Gardiner, Suzuki, Gould, Casals, Hewitt — so the catalog and the reception story reinforce each other), linking to YouTube where stable official uploads exist. Score links to IMSLP. These are curated pointers, not embedded media — keeps the site static, fast, and free of licensing issues.

---

## 6. Places — the Geography Section

- Every write-up names its place, and each of the ~10 principal towns (Eisenach, Ohrdruf, Lüneburg, Arnstadt, Mühlhausen, Weimar, Cöthen, Leipzig, plus Lübeck and Potsdam as pilgrimage/visit sites) gets a **place page**: the town then, the church/court, the organ he played, what survives today.
- A dedicated **map section**: Bach's whole life within a ~200-mile circle of central Germany (the striking fact that the most cosmopolitan mind in music never left it), with journey lines for the famous trips (Lübeck on foot, Hamburg, Dresden, Potsdam) — rendered in the same ethereal visual language.

---

## 7. Experience & Design

### The outer view — "the timeline hung in space"

- A dark, deep-space canvas; the timeline as a luminous horizontal ribbon floating in the void.
- **Flowing music imagery**: slow-moving streams of light — suggesting staff lines, voice leading, endless melody — drifting from the ribbon outward "into the forever." Subtle, continuous, satisfying motion (CSS/canvas animation; must stay smooth and battery-friendly, with a reduced-motion mode).
- The three arcs visible as one continuous ribbon with distinct luminosity/character: the Life bright and dense; the Eclipse dimming; the Rediscovery reigniting and streaming to the present — the design itself tells the reception story.
- Zoom: from the full 340-year sweep down to a single year; tracks fade in as you approach Arc I.

### The inner view — "the museum"

- Clicking any event, work, era, or person transitions to a clean, light, gallery-like presentation: generous whitespace, museum-placard typography, one image or musical example per screen where warranted, footnoted sources.
- Every fact card carries a **provenance flag**: *Documented* (surviving records, letters, council minutes) vs. *Tradition* (stories from the 1750 Obituary or Forkel that may be embellished — e.g., the moonlight copying). Scholarly honesty as a design feature.
- Navigation: timeline ⇄ works catalog ⇄ craft essays ⇄ places ⇄ people, all cross-linked; global search.

### Design references to gather during build

- Museum sites (Rijksmuseum, MoMA) for the inner view; space-visualization work for the outer view. We'll assemble a small mood board for your approval before UI work begins.

---

## 8. Technical Approach

- **Static site in a GitHub repository**, deployed via **GitHub Pages** — no server, no accounts, no cost; a single URL you can open anywhere.
- **All content lives as reviewable files**: markdown for essays and event narratives, structured JSON/YAML for events, works, people, places. You review content in VSCode exactly like any other document; the site is regenerated from it.
- Build tooling: a lightweight static-site setup (recommendation at build time: likely **Astro** or a hand-rolled vite build — decision deferred to the build phase and will be presented with reasoning; the content format is designed to be tool-agnostic so nothing done in the research phase is ever thrown away).
- The outer-space timeline is custom canvas/SVG work; the museum pages are plain, fast HTML.
- Repository proposal: `~/bach-timeline` locally → GitHub repo `bach-timeline` under your account.

---

## 9. Content Research Plan (the real work — happens BEFORE any app code)

Per your direction: research and content first. Every phase produces markdown/JSON files in the repo that you review before we proceed.

**Primary sources & references:**

- Christoph Wolff, *Johann Sebastian Bach: The Learned Musician* (the scholarly standard biography)
- *The New Bach Reader* (David/Mendel/Wolff) — the actual surviving documents in translation
- **John Eliot Gardiner, *Bach: Music in the Castle of Heaven*** — the modern humanizing portrait; also his Cantata Pilgrimage notes
- Peter Williams's revisionist biographies (a skeptical counterweight — useful for the provenance flags)
- Bach Digital (bach-digital.de) — the manuscript database; bach-cantatas.com — cantata details, texts, occasions; IMSLP for scores
- For Arc II: Celia Applegate, *Bach in Berlin* (the 1829 revival); standard reception-history literature

**Research phases (each ends with a review pause):**

| Phase | Deliverable | Scale |
|---|---|---|
| **R1** | Content schema (the JSON/markdown shapes for events, works, people, places) + one fully-written pilot era — **Cöthen** — so you can judge voice, depth, and format on the era most relevant to instrumental study | ~15 events, ~25 work cards, 1 place page |
| **R2** | Arc I complete: all ten periods' events, family layer, world track | ~120–150 events |
| **R3** | Works catalog: full 250–300 cards + set essays (Inventions, WTC, cantata cycles, Goldbergs) | the largest phase — will be split into genre batches for review |
| **R4** | Craft section: the 7 counterpoint essays | ~10k words |
| **R5** | Arc II & III: eclipse, rediscovery, interpreters (Gardiner et al.), Voyager | ~60 events + interpreter profiles |
| **R6** | Places & maps content; listening-link curation pass | 10 place pages, ~300 links verified |

Research will be done with live web verification (dates, BWV attributions, quotes) — every narrative carries its sources. I'll flag anywhere scholarship disagrees (e.g., cello suite dating, cantata chronology revisions by Dürr/Dadelsen) rather than presenting one view as settled fact.

**After content approval:** Build phase — schema-driven static site, outer view, museum pages, deploy to GitHub Pages. (Own plan, presented separately.)

---

## 10. Open Questions for Review

1. **Repo/name:** happy with `bach-timeline` as the repo and working title? (We can name the *app* something better later — e.g., *The Forever Stream*, *Castle of Heaven* is taken.)
2. **Pilot era:** I propose Cöthen for R1 (instrumental works, dramatic biography, manageable size). Prefer Leipzig I instead, if cantatas are closer to your current studies?
3. **Voice:** essays written like museum wall text (concise, elegant) or like Gardiner (opinionated, vivid, longer)? My proposal: museum voice for cards, a warmer essayistic voice for the Craft essays and era introductions.
4. **Your studies:** anything you're working on at Juilliard right now that should jump the queue in R3, so the catalog is useful to you immediately?

---

*End of PRD — awaiting review.*
