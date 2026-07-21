# AGENTS.md

This file provides guidance to Codex / Antigravity when working with code and content in this repository.

# _content: LLM Wiki & One-Shot Content Engine

Mode: Content pipeline & One-Shot Refactoring Engine
Purpose: Good AI / KTG publication pipeline — NotebookLM drops, Medium, ktg.one blog, and multi-channel social distribution (Reddit, LinkedIn, X, Meta) via Composio & n8n.
Owner: Kev
Created: 2026-07-17
Updated: 2026-07-21

---

## 🔒 Master Skill Rule

> **CRITICAL RULE:** A workflow is ONLY packaged into a `SKILL.md` AFTER it has been executed and empirically verified as a 100% success. Premature or unverified skills are strictly forbidden.

---

## Session start (do this first on every fresh session)

1. Read `wiki\hot.md` — recent context cache & active draft status.
2. Read `wiki\index.md` — root cataloged articles with status.
3. Read [`docs/architecture.md`](file:///C:/Users/kevin/Documents/_content/docs/architecture.md), [`docs/workflows.md`](file:///C:/Users/kevin/Documents/_content/docs/workflows.md), [`docs/personas.md`](file:///C:/Users/kevin/Documents/_content/docs/personas.md), and [`docs/ideation_roadmap.md`](file:///C:/Users/kevin/Documents/_content/docs/ideation_roadmap.md).

---

## Workspace Subsystems & Active Connectors

1. **Codebase Memory & Intelligence:** Powered by `codebase-memory-mcp` (DeusData - `codebase-memory-mcp --ui=true --port=9749`) and `@modelcontextprotocol/server-memory`.
2. **SEO Analysis & Refactoring:** Executed via `sccd/seo_refactor.py` and `.agents/skills/seo-analyzer/SKILL.md`.
3. **AI Image Generator:** GitHub `notebooklm-prompt-styles` templates (`sccd/image_prompt_templates.py`) + `generate_image` tool $\rightarrow$ `outbox/assets/`.
4. **Persona Outboxes:** Strict **Author Voice Preservation** for Reddit (`outbox/reddit/`), LinkedIn (`outbox/linkedin/`), X Thread (`outbox/x/`), and Meta (`outbox/meta/`).
5. **Google Workspace Automation:** CLI tool `gws` (v0.22.5) installed; skill located in `.agents/skills/google-workspace-cli/SKILL.md`. *(Strictly isolated to personal account workflows; never run against work accounts)*.
6. **Composio MCP Server:** Configured in `.agents/mcp_config.json` via `@composio/mcp@latest` with key `ak_wx...`.
7. **n8n Automation Engine:** Configured in `.agents/mcp_config.json` via `n8n-mcp` (40+ tools API server).
8. **Cloud Deployment CLI:** Railway CLI (v5.27.1) installed.

---

## Repository Structure

```
_content/
├── inbox/         # NotebookLM raw drops (.md / .txt)
├── outbox/        # Channel outboxes (master, assets, reddit, linkedin, x, meta)
├── .raw/          # source clips, immutable ingest inbox (dupes quarantined in .raw/_dupes/)
├── drafts/        # work in progress
├── posted/        # published pieces
├── sccd/          # SCCD framework + seo_refactor.py + image_prompt_templates.py + retrieve_details.py
├── .agents/       # Personas, Skills (seo-analyzer, image-generator, content-refactoring-engine, find-skills, google-workspace-cli), and mcp_config.json
├── docs/          # Architecture, Workflows, Personas, and Ideation Roadmap
├── tests/         # Python unittest suite (python -m unittest discover tests)
└── wiki/          # Knowledge layer & catalog (index.md, hot.md)
```

`.env` sits in workspace root — never read into output or copy elsewhere.

---

## Writing & Execution Rules

- **Author Voice:** PRESERVE AUTHOR VOICE VERBATIM. Repurpose and package — **never rewrite the author's voice**.
- **No Medium length culls.**
- **No Guessing:** Never guess code logic, schemas, or CLI flags. Always look them up first.
- **YOLO / Autonomous Mode:** When given a post or command, execute end-to-end without mid-process pauses or confirmation prompts.
