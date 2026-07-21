---
type: overview
created: 2026-07-17
---

# Vault Overview

This is the **Good AI / KTG** content-production vault. It is a working pipeline for essays, threads, and technique breakdowns about LLM behavior (fabrication, context handling, prompting technique honesty) that get packaged for **ktg.one (blog)**, **Medium**, and **LinkedIn**.

## Physical layout (unchanged by this wiki layer)

- Root (`_content/`) — loose in-progress articles, the current "Model Handbook 2026" series, MEDIUM-READY packages, prompt/tool templates (RMDRE, QMDR).
- `drafts/` — mirror snapshot of the same root article set (appears to be a working-copy duplicate, same filenames, timestamps ~Jul 13).
- `posted/` — currently empty. Intended destination once something goes live.
- `sccd/` — the SCCD-TFAB (Self · Consciousness · Choice · Decide) operator kit: a decision-model writeup plus a Python implementation (`sccd_tfab.py`).
- `Tags/` — empty at time of ingest.
- `README.md` — describes the `drop/` intake convention: drop a `.md` blog post, the marketing runtime runs DROP → REFACTOR → IMAGE+ALT → PUBLISH (WordPress first), gated by manual `YES` before social fire.
- `.raw/` — clipped source material staged for wiki ingestion (see [[wiki/sources/_index|Sources]]).

## Wiki layer (new, this layer only)

- `wiki/index.md` — master catalog of every page + the root-article status table.
- `wiki/log.md` — ingestion log (orchestrator-maintained).
- `wiki/hot.md` — recent/active context.
- `wiki/sources/` — one page per ingested raw source (from `.raw/`).
- `wiki/domains/` — one subfolder per content domain, each with an `_index.md`:
  - [[wiki/domains/model-handbook-series/_index|model-handbook-series]]
  - [[wiki/domains/medium-articles/_index|medium-articles]]
  - [[wiki/domains/blog-ktg/_index|blog-ktg]]
  - [[wiki/domains/sccd/_index|sccd]]

## Status vocabulary observed in frontmatter

- `draft` — active work, not yet packaged.
- `medium-ready` — packaged for Medium specifically.
- `ready-full` — packaged, ready to post (platform-agnostic within `platforms:`).
- `posted` — live (none observed yet; `posted/` is empty).
- No frontmatter / no `status:` field — treated as **draft** by default unless content clearly reads as a reusable tool/prompt template, in which case treated as **reference**.

See `_content/CLAUDE.md` (vault root) for pipeline conventions.
