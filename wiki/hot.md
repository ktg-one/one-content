---
type: hot
updated: 2026-07-17
---

# Hot

Recent / active context for this vault.

## Just happened (2026-07-18)

- **First publish confirmed**: Honest Diagnostic shipped as two-part split. `posted\` now holds `02 Model Handbook 2026 - The Honest Diagnostic.md` (posted) + `02-Model-Handbook-2026 - Self-Assessment.md`. Series has its live anchor.
- Dedup cull: 9 byte-identical root mirrors of `drafts\` articles deleted; canonical copies in `drafts\`. Canvas file nodes repointed to `drafts\` paths.
- `.raw\.manifest.json` created (delta tracker backfilled for ideate-52).

## Just happened (2026-07-17)

- `wiki/` layer stood up for the first time on this vault (no prior wiki). See [[wiki/index|Index]] and [[wiki/overview|Overview]].
- New source ingested: [[wiki/sources/ideate-52-2026-frontier-ai|2026 Frontier AI: What the Labs Don't Tell You]] (ktg.one, 2026-03-12) — external corroboration for the fabrication-threshold and keyword-hierarchy claims in [[wiki/domains/model-handbook-series/_index|model-handbook-series]]. Contains one unverified stat (platform-vs-CLI power gap) flagged for fact-check before reuse.

## Where the pipeline actually stands right now

- Most active domain: **model-handbook-series** — 6 of 7 pieces still `draft`, only `POST-2-Technique-Honesty-Test.md` is `ready-full`.
- Packaging is running ahead of drafting in one place: two `medium-ready` pieces already exist (Fabrication Frontier, SCCD Operator Model) while several of their source drafts are still rough.
- `posted/` is empty — **nothing from this series has actually shipped yet**. Everything cataloged is pre-publish.
- `sccd/` (the mitigation/decision-model counterpart to the fabrication essays) has a working Python implementation (`sccd_tfab.py`) already, ahead of its own writeup's packaging state.

## Open questions worth resolving next session

- Is the Qwen Max "linear autoregressive transformer" quote in `02-Model-Handbook-2026 - Self-Assessment.md` the same primary quote reused in the newly-ingested ktg.one source, or an independent second citation? Affects whether the source counts as true corroboration.
- Reconcile the two different "reliability cliff" framings: this vault's own R7–R8 / Fab% 26%→67% vs. the ingested source's "8 Tower-of-Hanoi disks" / generic P_r^n formula — same phenomenon, not yet mapped to one number.
- `blog-LEGIO_Sovereign_Command.pdf` / `blog-LEGIO_Tactical_Execution.pdf` (root, large PDFs) not yet catalogued — candidate for next ingestion pass, possible new domain.
- `RMDRE-IMBUEDv15-2026.md` and `02-25-2026-QMDR-2026.md` are reusable tool/prompt templates, not articles — consider a `tools/` or `prompts/` domain if more of these show up.
