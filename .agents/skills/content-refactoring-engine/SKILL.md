---
name: "content-refactoring-engine"
description: "Automated One-Shot Content Refactoring Engine for NotebookLM drops. Scans incoming drafts in inbox/, generates 2 visual images with captions/alt tags, refactors content for SEO into outbox/master/, and formats channel-specific persona posts for Reddit, LinkedIn, X, and Meta ready for Composio distribution."
---

# Content Refactoring & Multi-Channel Distribution Engine

This skill automates the complete pipeline from raw NotebookLM drops in `inbox/` to SEO-refactored master drafts and multi-channel outbox posts (Reddit, LinkedIn, X, Meta) ready for Composio distribution.

---

## Workflow Execution Steps

When a new drop arrives in `inbox/` (or when triggered via "refactor content [file]"):

### Step 1: Run SEO Refactor & Image Anchor Selection
Run the SEO refactoring engine script:
```bash
python sccd/seo_refactor.py inbox/<drop-filename>.md
```
This parses the input, generates frontmatter/meta description, scores SEO readability, selects 2 image insertion points, and outputs:
- Refactored master article: `outbox/master/<name>_refactored.md`
- Image metadata: `outbox/master/<name>_meta.json`

### Step 2: Generate 2 Visual Assets
Read the image prompts from `outbox/master/<name>_meta.json` and invoke the image generator tool (`generate_image`) for both anchors:
- **Image 1:** Saved to `outbox/assets/image_1_<slug>.png`
- **Image 2:** Saved to `outbox/assets/image_2_<slug>.png`

Attach alt tags, captions, and descriptions in the master markdown file.

### Step 3: Transform into Channel Persona Outboxes
Read the refactored master article and apply the persona transformation specifications:
- **Reddit Outbox:** `outbox/reddit/<name>_reddit.md` (using `.agents/personas/reddit_persona.md`)
- **LinkedIn Outbox:** `outbox/linkedin/<name>_linkedin.md` (using `.agents/personas/linkedin_persona.md`)
- **X Outbox:** `outbox/x/<name>_x_thread.md` (using `.agents/personas/x_persona.md`)
- **Meta Outbox:** `outbox/meta/<name>_meta.md` (using `.agents/personas/meta_persona.md`)

### Step 4: Composio Distribution Verification
Verify Composio MCP server readiness to route outgoing posts to Reddit, LinkedIn, X, and Meta.
