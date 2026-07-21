# Workflows Runbook: Content & Cloud Infrastructure Engine

This runbook guides you through operating the **Content Refactoring Engine** and setting up cloud infrastructure (Railway, n8n, Composio).

---

## 🔒 Master Skill Rule

> **CRITICAL RULE:** A workflow is ONLY packaged into a `SKILL.md` AFTER it has been executed and empirically verified as a 100% success. Premature or unverified skills are strictly forbidden.

---

## 1. Content Refactoring Workflow (Verified)

### Step 1: Drop Raw NotebookLM Content into `inbox/`
Export your research notes, podcast transcript summary, or draft post from NotebookLM into a markdown or text file inside `inbox/`:
```bash
inbox/my_notebook_drop.md
```

### Step 2: Trigger the Engine
Run the refactoring command:
```bash
python sccd/seo_refactor.py inbox/my_notebook_drop.md
```

### Step 3: Visual Generation & Outbox Formatting
The engine automatically:
1. Performs SEO readability and structure scoring.
2. Selects 2 visual anchor points in the article.
3. Generates 2 visual image assets into `outbox/assets/` using GitHub NotebookLM prompt templates (*Silicon Refined*, *Strategic Blue*).
4. Generates persona-tailored outbox posts into `outbox/reddit/`, `outbox/linkedin/`, `outbox/x/`, and `outbox/meta/` preserving author voice verbatim.

---

## 2. Cloud Setup Workflows (In Progress)

### A. Railway CLI Login & Deployment
```bash
# 1. Login to Railway
railway login

# 2. Link or initialize project
railway init

# 3. Deploy n8n instance
railway up
```

### B. n8n Instance & Google OAuth Setup
1. Deploy n8n on Railway or start local instance (`http://localhost:5678`).
2. Generate API key in n8n (Settings $\rightarrow$ API).
3. Update `.env` with `N8N_API_URL` and `N8N_API_KEY`.
4. Configure Google OAuth credential inside n8n dashboard for Drive, Docs, Gmail, and Calendar.

### C. Composio MCP Integration
- Configuration active in [`.agents/mcp_config.json`](file:///C:/Users/kevin/Documents/_content/.agents/mcp_config.json) using `@composio/mcp@latest`.
- Connects outbox posts directly to Reddit, LinkedIn, X, and Meta APIs.

---

## 3. Verification & Skill Packaging

- Once Railway deployment or n8n workflow runs successfully, verify the live endpoint/execution.
- **Packaging:** Author the corresponding `SKILL.md` in `.agents/skills/` ONLY after empirical verification.
