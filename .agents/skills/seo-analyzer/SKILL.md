---
name: "seo-analyzer"
description: "SEO Analysis and Refactoring Skill for NotebookLM drops. Evaluates heading structure, keyphrase density, meta descriptions, readability scores, and selects 2 optimal image placement points using GitHub notebooklm-prompt-styles templates."
---

# SEO Analyzer Skill

This skill performs comprehensive SEO analysis, readability scoring, and refactoring on incoming markdown drops.

---

## Capabilities & Operation

### 1. Execute SEO Refactoring
```bash
python sccd/seo_refactor.py inbox/<drop-filename>.md
```

### 2. Output Specification
- **Master Refactored Draft:** `outbox/master/<name>_refactored.md`
- **SEO Metadata JSON:** `outbox/master/<name>_meta.json` (Includes word count, H1/H2 checks, SEO score 0-100, and 2 image prompts built from GitHub `notebooklm-prompt-styles`).

---

## Pre-Conditions & Requirements
- Input drop must be located in `inbox/`.
- `sccd/seo_refactor.py` and `sccd/image_prompt_templates.py` must be present.
