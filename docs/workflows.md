# Workflows Runbook: Content Refactoring Engine

This runbook guides you through running the **Content Refactoring Engine** to turn NotebookLM drops into multi-channel published posts.

---

## 1. Standard One-Shot Workflow

### Step 1: Drop Raw NotebookLM Content into `inbox/`
Export your research notes, podcast transcript summary, or draft post from NotebookLM into a markdown or text file inside `inbox/`:
```bash
inbox/my_notebook_drop.md
```

### Step 2: Trigger the Engine
Tell the agent in chat:
> *"Refactor inbox drop my_notebook_drop.md"*

Or run the refactoring command manually:
```bash
python sccd/seo_refactor.py inbox/my_notebook_drop.md
```

### Step 3: Visual Generation & Outbox Formatting
The engine automatically:
1. Performs SEO readability and structure scoring.
2. Selects 2 visual anchor points in the article.
3. Generates 2 visual image assets into `outbox/assets/` using GitHub NotebookLM prompt templates.
4. Generates persona-tailored outbox posts into `outbox/reddit/`, `outbox/linkedin/`, `outbox/x/`, and `outbox/meta/`.

### Step 4: Composio Distribution
With Composio MCP configured, trigger direct posting or scheduling to your target platforms:
```bash
npx -y composio-core execute ...
```

---

## 2. Testing & Diagnostics

To verify the SEO refactoring script and prompt templates manually:
```bash
python sccd/seo_refactor.py inbox/sample_drop.md
```
Output files created:
- `outbox/master/sample_drop_refactored.md`
- `outbox/master/sample_drop_meta.json`
