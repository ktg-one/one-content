# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# _content: LLM Wiki

Mode: Content pipeline (reference library)
Purpose: Good AI / KTG publication pipeline — Medium, ktg.one blog, LinkedIn drafts through to posted.
Owner: Kev
Created: 2026-07-17

## Session start (do this first)

1. Read `wiki\hot.md` — recent context cache (~500 words).
2. Then `wiki\index.md` — root articles cataloged with status (draft / ready / medium-ready).

## Structure

```
_content/
├── .raw/          # source clips, immutable ingest inbox (dupes quarantined in .raw/_dupes/)
├── drafts/        # work in progress
├── posted/        # published pieces (first 2 live 2026-07-18; draft → posted moves logged in wiki/log.md)
├── sccd/          # SCCD framework material + sccd_tfab.py
├── Tags/          # tag pages
└── wiki/
    ├── index.md   # master catalog
    ├── log.md     # append-only, new entries at TOP
    ├── hot.md     # ~500-word recent context cache
    ├── overview.md
    ├── canvases/  # content-overview.canvas dashboard
    ├── sources/   # one page per raw source
    └── domains/   # model-handbook-series, medium-articles, blog-ktg, sccd
```

Not a git repo. `.env` sits in root — never read into output or copy elsewhere.

## Root vs drafts (deduped 2026-07-18)

9 byte-identical root duplicates of `drafts\` articles deleted on Kev's directive (logged in wiki/log.md). Canonical article copies live in `drafts\`. Root keeps only `02-25-2026-QMDR-2026.md` (differs from drafts copy). Don't scatter new files in root — new material goes to `.raw\` then ingest.

## Published (2026-07-18)

Honest Diagnostic shipped as a two-part split — both in `posted\`: `02 Model Handbook 2026 - The Honest Diagnostic.md` (status: posted) + `02-Model-Handbook-2026 - Self-Assessment.md` (split-out second half). `drafts\` still holds an older differing Honest Diagnostic version.

## Canvas frontend

Canvases render in the Obsidian app — open `_content` as vault, click `.canvas` files in `wiki\canvases\`. No web UI. `advanced-canvas` community plugin is installed but disabled; enable for presentation mode + PNG/SVG/PDF export.

## Writing rules (from drafts\AGENTS.md)

- Author voice from source drafts — repurpose/package, don't rewrite voice unless asked.
- No Medium length culls.
- ARQ discipline: stop → step back → holistic original prompt → align → continue (`ARQ-WRITING-KTG.md`).

## Conventions

- All notes use YAML frontmatter: type, status, created, updated, tags (minimum)
- Wikilinks use [[Note Name]] format — filenames unique, no paths
- .raw/ never modified
- wiki/index.md updated on every ingest
- wiki/log.md append-only, new entries at TOP
- Publish-status changes (draft → posted) get logged in wiki/log.md

## Operations

- Ingest: drop source in .raw/, say "ingest [filename]"
- Query: ask — Claude reads hot.md then index first
- Lint: "lint the wiki"
- SCCD ledger: `python sccd\sccd_tfab.py` (stdlib only)
- Routing for other domains: see C:\Users\kevin\Documents\LIFE-MAP.md
- Related folder: `..\content-hub\` — agent-orchestrated publishing runtime (WordPress-first, review-gated). Consolidation with this vault is an open decision on the life board.

## Lint policy — dupes get culled (Kev directive 2026-07-17)

Every wiki-lint run includes a dedup cull:
1. Hash pass: byte-identical .raw sources → quarantine in `.raw/_dupes/`, log it.
2. Semantic pass (if ollama running): `python C:\Users\kevin\.claude\skills\wiki-tiling-py\tiling_check_win.py --vault C:\Users\kevin\Documents\_content` — wiki-page pairs ≥0.90 = merge candidates.
3. Merge: keep canonical page, fold unique content in, add loser's title to canonical `aliases:` frontmatter, delete loser, log the merge (aliases keep old wikilinks resolving).
4. 0.80–0.90 band: report for Kev, never auto-merge.
5. Every cull is a log entry. No silent deletions. Special case here: article drafts in `drafts/` vs `posted/` may legitimately be near-identical (versions) — version pairs are NOT dupes, skip them.
