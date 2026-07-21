# STATE.md — Current Workspace Execution & Infrastructure State

*Last Updated: 2026-07-21 17:55*

---

## 🔒 Master Skill Rule
> **CRITICAL RULE:** A workflow is ONLY packaged into a `SKILL.md` AFTER it has been executed and empirically verified as a 100% success. Premature or unverified skills are strictly forbidden.

---

## 🚦 System Execution State

### 1. Local Content Pipeline (100% Operational)
- **Ingest:** `inbox/` drops scanned automatically.
- **SEO Refactor Engine:** `sccd/seo_refactor.py` calculates SEO score (0-100), word count, and image anchor placement.
- **Image Prompts:** `sccd/image_prompt_templates.py` pulls GitHub `notebooklm-prompt-styles` visual archetypes (*Silicon Refined*, *Strategic Blue*).
- **Asset Generation:** `generate_image` tool outputs PNGs to `outbox/assets/`.
- **Persona Outboxes:** Verbatim Author Voice posts formatted for `outbox/reddit/`, `outbox/linkedin/`, `outbox/x/`, and `outbox/meta/`.
- **Test Suite:** 7/7 unit tests passing (`python -m unittest discover tests`).

### 2. Connectors & MCP Infrastructure
- **Codebase Memory MCP:** `codebase-memory-mcp` v0.9.0 globally installed (`codebase-memory-mcp --ui=true --port=9749`).
- **Memory MCP:** `@modelcontextprotocol/server-memory` configured.
- **Composio MCP:** Authenticated & live with key `ak_wx...`. (Pending OAuth link for social accounts at `app.composio.dev/apps`).
- **n8n API MCP:** Configured with 40+ tool API server. (Pending live Railway n8n instance URL).
- **Google Workspace CLI:** `gws` v0.22.5 installed.
- **Railway CLI:** `railway` v5.27.1 installed.

---

## 📌 Active Next Tasks for Fresh Session
1. **n8n Railway Instance Link:** Obtain live Railway n8n instance URL and update `.env` / `mcp_config.json`.
2. **Composio Social OAuth:** Link social channels (LinkedIn, Reddit, X, Meta) in `app.composio.dev/apps`.
3. **Live Social Distribution Test:** Execute first live post via Composio / n8n once authenticated.
