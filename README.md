# _content — Publication Pipeline & One-Shot Content Engine

Content-creation vault & automated **One-Shot Content Refactoring Engine** for Good AI / KTG: NotebookLM drops, Model Handbook article series, Medium-ready pieces, ktg.one blog material, and multi-channel social distribution.

---

## ⚡ Quick Start: Content Refactoring Engine

1. **Drop NotebookLM Content**: Place raw markdown or text notes in [`inbox/`](file:///C:/Users/kevin/Documents/_content/inbox/).
2. **Run Refactor Engine**:
   ```bash
   python sccd/seo_refactor.py inbox/<drop-filename>.md
   ```
3. **Outputs Generated Automatically**:
   - **SEO Master Draft:** [`outbox/master/<filename>_refactored.md`](file:///C:/Users/kevin/Documents/_content/outbox/master/)
   - **Awesome Prompts & Metadata:** [`outbox/master/<filename>_meta.json`](file:///C:/Users/kevin/Documents/_content/outbox/master/)
   - **Generated Visuals:** [`outbox/assets/`](file:///C:/Users/kevin/Documents/_content/outbox/assets/)
   - **Channel Personas:** [`outbox/reddit/`](file:///C:/Users/kevin/Documents/_content/outbox/reddit/), [`outbox/linkedin/`](file:///C:/Users/kevin/Documents/_content/outbox/linkedin/), [`outbox/x/`](file:///C:/Users/kevin/Documents/_content/outbox/x/), [`outbox/meta/`](file:///C:/Users/kevin/Documents/_content/outbox/meta/)

---

## 📁 Repository Structure

```
_content/
├── inbox/                # Raw drops from NotebookLM (.md / .txt)
├── outbox/               # Channel-specific outboxes (master, assets, reddit, linkedin, x, meta)
├── .raw/                 # Ingest inbox for wiki reference sources
├── drafts/               # Articles in progress
├── posted/               # Published articles
├── sccd/                 # SEO refactor engine & GitHub NotebookLM prompt templates
│   ├── seo_refactor.py
│   └── image_prompt_templates.py
├── .agents/
│   ├── personas/         # Channel persona specifications (author voice preserved)
│   ├── skills/           # One-Shot Skill modules
│   └── mcp_config.json   # Composio MCP configuration
├── docs/                 # Workspace documentation
│   ├── architecture.md
│   ├── workflows.md
│   └── personas.md
└── wiki/                 # Knowledge layer & catalog
```

---

## 📚 Documentation

Detailed documentation is available in the [`docs/`](file:///C:/Users/kevin/Documents/_content/docs/) directory:
- 🏗️ [docs/architecture.md](file:///C:/Users/kevin/Documents/_content/docs/architecture.md) — System architecture & folder breakdown.
- ⚡ [docs/workflows.md](file:///C:/Users/kevin/Documents/_content/docs/workflows.md) — Step-by-step operational runbook.
- 🎭 [docs/personas.md](file:///C:/Users/kevin/Documents/_content/docs/personas.md) — Voice preservation & word-count specs.

---

## 🔒 Rules & Guidelines

- **Author Voice:** Repurpose & package — **never rewrite the author's voice**.
- **SEO & Image Prompts:** Driven by GitHub `notebooklm-prompt-styles` templates (*Silicon Refined*, *Strategic Blue*, *Executive Report*, *Liquid Executive*, *Prestige Gold*, *Cyber AI*).
- **Composio MCP:** Connected via `npx -y composio-core mcp` for multi-platform distribution.
