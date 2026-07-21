---
type: log
---

# Ingestion Log

## 2026-07-18

- **SCCD rewrite**: deleted pasted `sccd\sccd_tfab.py` (2026-07-12) on Kev's directive "the self token must be created by the self"; agent authored replacement at same path. New: `Anchor` provenance (self-minted vs imported), S1 rule (zero self-minted anchors = Decide blocked), self-minted demo anchors from live session doctrine, ASCII-only output (old version crashed cp1252 console with `UnicodeEncodeError` at scale sweep — found live during verification run). Executed clean: A=COMMIT(100), B=TRANSPARENCY_STOP(55), C=BLOCK(imported-only Self). `SCCD-TFAB-OPERATOR-KIT.md` code section updated.

- **PUBLISH**: Kev confirms Honest Diagnostic shipped as a two-part split. Moved to `posted\`: `02 Model Handbook 2026 - The Honest Diagnostic.md` (root version, status draft → posted) and `02-Model-Handbook-2026 - Self-Assessment.md` (the split-out second half; no frontmatter). First live pieces — `posted\` no longer empty. `drafts\02 Model Handbook 2026 - The Honest Diagnostic.md` remains as the older differing draft version.

- Dedup cull (Kev directive "rm dupes"): deleted 9 root articles byte-identical (hash-verified at deletion time) to their `drafts\` copies — 03 Fabrication Threshold, 03 Transparency Logic, 04 MBTI LLM's Personality, 4. PIQUE TEST, ARQ-WRITING-KTG, MEDIUM-READY Fabrication Frontier, MEDIUM-READY SCCD-TFAB, POST-2 Technique Honesty Test, RMDRE-IMBUEDv15. Canonical copies live in `drafts\`. Root keeps only true version pairs: `02 Model Handbook 2026 - The Honest Diagnostic.md`, `02-25-2026-QMDR-2026.md` (differ from drafts counterparts). Wikilinks unaffected — [[Note Name]] resolves path-independent; duplicate filenames removed restores the filenames-unique convention.

## 2026-07-17

- Initialized `wiki/` layer (`index.md`, `log.md`, `hot.md`, `overview.md`, `sources/`, `domains/{model-handbook-series,medium-articles,blog-ktg,sccd}/_index.md`). No existing files/folders moved or renamed.
- Created vault `_content/CLAUDE.md` (none existed in `.claude/` or at root).
- Catalogued 12 root articles into `wiki/index.md` with guessed status (draft / ready-full / medium-ready / reference) from frontmatter + content inspection. `posted/` confirmed empty.
- Ingested `.raw/ideate-52.txt` ("2026 Frontier AI: What the Labs Don't Tell You," ktg.one, published 2026-03-12) → [[ideate-52-2026-frontier-ai]], linked into [[blog-ktg]] and [[model-handbook-series]] domains. Noted `.raw/_dupes/ideate-42-DUPE-of-52.txt` as an identical, quarantined duplicate — not separately ingested.
- Flagged one unverified claim in the ingested source (platform-vs-CLI "50-60% less power" figure, no cited methodology) via `[!contradiction]` callout on the source page.
