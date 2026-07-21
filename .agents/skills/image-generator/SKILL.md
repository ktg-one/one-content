---
name: "image-generator"
description: "Image Generation Skill for Content Pipeline. Constructs high-impact visual prompts pulling from GitHub notebooklm-prompt-styles repository templates and executes generate_image to create PNG assets in outbox/assets/ with alt tags and captions."
---

# Image Generator Skill

This skill generates high-fidelity visual assets for blog posts and social content using curated prompt templates and the built-in image generator tool.

---

## Prompt Archetypes (`sccd/image_prompt_templates.py`)
- **`silicon_refined`**: Bento-grid minimalist visual design, Matte Charcoal (`#1D1D1F`) & Tech Blue (`#0071E3`).
- **`strategic_blue`**: Architectural hexagonal pattern overlay, Slate Blue (`#264653`) & Ice Blue (`#E9F5F8`).
- **`executive_report`**: Consulting-grade data visualization, Deep Navy (`#051C2C`) & Muted Blue (`#007DBB`).
- **`liquid_executive`**: Dark-mode fluid blue smoke and silk textures, Executive Blue (`#0056B3`) & Pure Black (`#000000`).
- **`prestige_gold`**: Dark luxury golden-hour lighting curves, Old Gold (`#E2B670`) & Midnight Blue (`#0F172A`).
- **`cyber_ai`**: Holographic 3D neural network, Cyber Cyan (`#00F0FF`) & Neon Violet (`#7B2CBF`).

---

## Execution Workflow
1. Read prompt strings from `outbox/master/<name>_meta.json`.
2. Invoke `generate_image(Prompt=..., ImageName=...)`.
3. Save generated `.png` assets to `outbox/assets/image_1_<slug>.png` and `outbox/assets/image_2_<slug>.png`.
