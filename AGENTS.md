# AGENTS.md

This file provides guidance to Codex / Antigravity when working with code and content in this repository.

# _content: LLM Wiki & One-Shot Content Engine

Mode: Content pipeline & One-Shot Refactoring Engine
Purpose: Good AI / KTG publication pipeline — NotebookLM drops, Medium, ktg.one blog, and multi-channel social distribution (Reddit, LinkedIn, X, Meta) via Composio.
Owner: Kev
Created: 2026-07-17
Updated: 2026-07-21

---

## Session start (do this first)

1. Read `wiki\hot.md` — recent context cache (~500 words).
2. Then `wiki\index.md` — root articles cataloged with status (draft / ready / medium-ready).
3. Read [`docs/architecture.md`](file:///C:/Users/kevin/Documents/_content/docs/architecture.md) & [`docs/workflows.md`](file:///C:/Users/kevin/Documents/_content/docs/workflows.md) for Content Engine operations.

---

## Structure

```
_content/
├── inbox/         # NotebookLM raw drops (.md / .txt)
├── outbox/        # Channel outboxes (master, assets, reddit, linkedin, x, meta)
├── .raw/          # source clips, immutable ingest inbox (dupes quarantined in .raw/_dupes/)
├── drafts/        # work in progress
├── posted/        # published pieces
├── sccd/          # SCCD framework + seo_refactor.py + image_prompt_templates.py
├── .agents/       # Personas, One-Shot Skills, and Composio mcp_config.json
├── docs/          # Architecture, Workflows, and Persona specifications
└── wiki/          # Knowledge layer & catalog
```

Not a git repo. `.env` sits in root — never read into output or copy elsewhere.

---

## Content Refactoring Operations

1. **Inbox Drops**: Place raw NotebookLM notes or drafts in `inbox/`.
2. **Refactor Execution**:
   ```bash
   python sccd/seo_refactor.py inbox/<drop-filename>.md
   ```
3. **Image Prompts**: Generated using GitHub `notebooklm-prompt-styles` templates (`sccd/image_prompt_templates.py`).
4. **Outbox Transformations**:
   - `outbox/master/`: Refactored master article & metadata.
   - `outbox/assets/`: Generated images (`image_1_<slug>.png`, `image_2_<slug>.png`).
   - `outbox/reddit/`: 250-500 words, authentic community starter.
   - `outbox/linkedin/`: 150-300 words, single-line spacing, bulleted key takeaways.
   - `outbox/x/`: Numbered thread (<280 chars per tweet).
   - `outbox/meta/`: 150-300 words visual story.

---

## Writing Rules

- **Author Voice:** PRESERVE AUTHOR VOICE VERBATIM. Repurpose and package — **never rewrite the author's voice**.
- **No Medium length culls.**
- **ARQ discipline:** stop → step back → holistic original prompt → align → continue (`ARQ-WRITING-KTG.md`).

---

## Conventions

- All notes use YAML frontmatter: type, status, created, updated, tags (minimum)
- Wikilinks use `[[Note Name]]` format — filenames unique, no paths
- `.raw/` never modified
- `wiki/index.md` updated on every ingest
- `wiki/log.md` append-only, new entries at TOP
- Publish-status changes (draft → posted) get logged in `wiki/log.md`

---

## Operations & Lint Policy

- Ingest: drop source in `.raw/`, say "ingest [filename]"
- Refactor: drop NotebookLM draft in `inbox/`, say "refactor inbox drop [filename]"
- Lint: "lint the wiki"
- Dedup cull: byte-identical `.raw` sources quarantined in `.raw/_dupes/`
