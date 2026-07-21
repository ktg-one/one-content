# Content Refactoring & Multi-Channel Distribution Architecture

The **Content Refactoring Engine** automates the transition from raw NotebookLM research drops into SEO-optimized master posts and multi-channel persona outputs (Reddit, LinkedIn, X, Meta) ready for distribution via Composio MCP.

---

## Directory Architecture

```
_content/
├── inbox/                # Incoming raw drops from NotebookLM (.md / .txt)
├── outbox/               # Processed outbox directories
│   ├── master/           # SEO-refactored master articles & metadata JSON
│   ├── assets/           # Generated image assets (image_1_<slug>.png, image_2_<slug>.png)
│   ├── reddit/           # Reddit persona posts (250-500 words, discussion starter)
│   ├── linkedin/         # LinkedIn persona posts (150-300 words, single-line spacing)
│   ├── x/                # X (Twitter) thread posts (numbered tweets < 280 chars)
│   └── meta/             # Meta (Facebook/Instagram) visual story posts
├── sccd/
│   ├── seo_refactor.py           # Core SEO analysis & refactoring script
│   └── image_prompt_templates.py # GitHub notebooklm-prompt-styles templates
├── .agents/
│   ├── personas/                 # Channel persona specifications
│   │   ├── reddit_persona.md
│   │   ├── linkedin_persona.md
│   │   ├── x_persona.md
│   │   └── meta_persona.md
│   ├── skills/
│   │   └── content-refactoring-engine/SKILL.md # One-Shot Skill runner
│   └── mcp_config.json           # Composio MCP configuration
└── docs/                         # Workspace documentation
    ├── architecture.md
    ├── workflows.md
    └── personas.md
```

---

## Core Pipeline Components

### 1. Ingest & Refactoring (`sccd/seo_refactor.py`)
- Reads drops from `inbox/`.
- Validates heading structure, keyphrase density, meta descriptions, and readability.
- Identifies 2 optimal image anchor points.
- Applies GitHub `notebooklm-prompt-styles` templates (*Silicon Refined*, *Strategic Blue*, *Executive Report*, *Liquid Executive*, *Prestige Gold*, *Cyber AI*) to construct rich image prompts.
- Outputs `outbox/master/<name>_refactored.md` and `outbox/master/<name>_meta.json`.

### 2. Visual Asset Generation (`generate_image`)
- Invokes `generate_image` using the prompt templates in metadata JSON.
- Saves high-res assets to `outbox/assets/image_1_<slug>.png` and `outbox/assets/image_2_<slug>.png`.
- Attaches alt tags, captions, and descriptions in the master markdown file.

### 3. Channel Persona Outboxes (`.agents/personas/`)
- **Author Voice Rule:** Author's authentic voice, vocabulary, and phrasing are preserved **verbatim**. No synthetic AI rewriting.
- Repurposes and formats content for prime character/word counts for each channel.

### 4. Composio MCP Integration
- Registered in `.agents/mcp_config.json` via `npx -y composio-core mcp`.
- Connects outbox posts directly to Reddit, LinkedIn, X, and Meta APIs.
