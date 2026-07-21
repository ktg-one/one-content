---
type: index
created: 2026-07-17
---

# Wiki Index

Master catalog for the Good AI / KTG content vault. See [[wiki/overview|Overview]] for layout, [[wiki/hot|Hot]] for recent context, [[wiki/log|Log]] for ingestion history.

## Domains

- [[wiki/domains/model-handbook-series/_index|model-handbook-series]]
- [[wiki/domains/medium-articles/_index|medium-articles]]
- [[wiki/domains/blog-ktg/_index|blog-ktg]]
- [[wiki/domains/sccd/_index|sccd]]

## Sources

- [[wiki/sources/ideate-52-2026-frontier-ai|2026 Frontier AI: What the Labs Don't Tell You]] — ktg.one, published 2026-03-12, ingested 2026-07-17. Dupe quarantined at `.raw/_dupes/ideate-42-DUPE-of-52.txt`.

## Root article catalog

Status is a **guess** derived from frontmatter `status:` field where present, else inferred from polish level / presence of packaging metadata. Canonical copies live under `drafts/` — 9 byte-identical root mirrors deleted in the 2026-07-18 dedup cull (see [[wiki/log|Log]]); only `02 Model Handbook 2026 - The Honest Diagnostic.md` and `02-25-2026-QMDR-2026.md` still have a differing root version.

| File | Domain | Status (guess) | Basis |
|---|---|---|---|
| `posted/02 Model Handbook 2026 - The Honest Diagnostic.md` | model-handbook-series | **posted** | Kev confirmed shipped 2026-07-18 (two-part split, part 1); older draft version remains in `drafts/` |
| `posted/02-Model-Handbook-2026 - Self-Assessment.md` | model-handbook-series | **posted** | Kev confirmed shipped 2026-07-18 (split-out part 2) |
| `03 Model Handbook 2026 - The Fabrication Threshold.md` | model-handbook-series | **draft** | frontmatter has `word-count`/`modified` only, no `status`; starts mid-sequence ("## 2.") suggesting an excerpt/fragment |
| `03 Model Handbook 2026 - Transparency Logic.md` | model-handbook-series | **draft** | frontmatter has `word-count`/`modified` only, no `status`; contains raw python scratch block |
| `04 Model Handbook 2026 - The MBTI LLM's Personality.md` | model-handbook-series | **draft** | no frontmatter, test-list format, unfinished feel |
| `4. THE PIQUE TEST — 10 Tests That Expose How Well You Understand Your Model.md` | model-handbook-series | **draft** | no frontmatter; terse companion/appendix to MBTI doc |
| `POST-2-Technique-Honesty-Test.md` | model-handbook-series | **ready-full** | frontmatter `status: ready-full` |
| `MEDIUM-READY-Model-Handbook-2026-The-Fabrication-Frontier.md` | medium-articles (repackages model-handbook-series) | **medium-ready** | frontmatter `status: medium-ready` |
| `MEDIUM-READY-SCCD-TFAB-Operator-Model.md` | medium-articles (repackages sccd) | **medium-ready** | frontmatter `status: medium-ready` |
| `ARQ-WRITING-KTG.md` | blog-ktg | **draft / notes** | no frontmatter; internal framework notes, terse |
| `RMDRE-IMBUEDv15-2026.md` | tool/prompt (no content domain) | **reference** | no frontmatter; persona/system-prompt template ("Recursive Master Deep Research Engine"), not a publishable article |
| `02-25-2026-QMDR-2026.md` | tool/prompt (no content domain) | **reference** | no frontmatter; system-prompt template ("Search-Augmented Strategic Inquiry Engine"), not a publishable article |

Not deep-catalogued this pass (flagged for future ingestion): `blog-LEGIO_Sovereign_Command.pdf`, `blog-LEGIO_Tactical_Execution.pdf` (see [[wiki/domains/blog-ktg/_index|blog-ktg]]).

`posted/` folder: **2 live** (2026-07-18) — Honest Diagnostic two-part split. Rest of series pre-publish.

## Counts

- Root/drafts articles catalogued: 12 (7 model-handbook-series, 2 medium-articles, 1 blog-ktg, 2 tool/reference)
- Domains created: 4
- Sources ingested: 1 (1 dupe quarantined, not separately ingested)
