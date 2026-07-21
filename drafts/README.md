# drop/ — the intake folder

Drop a blog post here (`.md`). That's the whole interface.

The marketing runtime picks it up and runs **DROP → REFACTOR → IMAGE+ALT → PUBLISH (WordPress first)**, stopping at the review gate before any public social fire. Full loop: `../Runtime.md`.

Notes:
- Blogs usually arrive already written in your voice (NotebookLM). The runtime **repurposes + packages** — it does NOT rewrite your voice unless you ask.
- Filename becomes the slug. A `POST`-prefix means ready (your existing `blog/` convention).
- Image gen is spec-driven — drop an image brief alongside the post (`<slug>.image.md`) if you know exactly what you want.
- **Nothing posts to socials without your per-post `YES`.** A WordPress draft is the safe first step.
