---
type: draft
status: draft
created: 2026-07-18
updated: 2026-07-18
tags: [function-library, recursive, legio, strawhats, contribution]
system: LEGIO (STRAWHATS v30 ADAPTIVE-BATTALION → LEGIO)
sources:
  - LEGIO-OVERVIEW.md
  - LEGIO-ARCHITECTURE-v1.md
  - LEGIO-FORMATION-DOCTRINEI.md
note: Function Library form filled for LEGIO only. Form frame is Recursive collab; this entry is the LEGIO system card.
---

# Function Library — LEGIO

**System:** LEGIO (Latin: the legion)  
**Also known as:** STRAWHATS v30 ADAPTIVE-BATTALION → LEGIO  
**Owner / stack:** ktg.one · Model Handbook era operator cascade  
**One line:** A 17-module prompt cascade / agentic framework that turns any query into a mode-scaled, multi-expert, quality-gated execution railroad — same units, different formations per campaign.

---

## What problem were you trying to solve?

Complex work with LLMs collapses into two bad modes:

1. **Underspecified freestyle** — model improvises structure mid-generation; quality is luck.  
2. **Costume depth** — advanced technique names (trees, experts, verification) without sealed plans, success criteria, or hard gates — so you get fluent theatre instead of checked delivery.

LEGIO was built so **planning happens before marching**, **tactics are sealed into a railroad**, and **output doesn’t ship until mission criteria are secured** — with force size scaled to real difficulty (QUICK → MAXIMUM), not one fixed mega-prompt for every task.

## What motivated you to build your system?

STRAWHATS v30 already had an 18-module adaptive battalion. The rename to LEGIO and the architecture work (Imperatus / Legatus / Censor spine, MCP deployment path, formation templates) was about making that force **self-contained, reconfigurable, and executable**:

- Same legion, different formations per use case  
- Roman names for human docs; functional verbs for models  
- Specs → Forge → AGENTS.md → runtime, not a bloated graph framework  

Motivation: stop paying for mid-flight decision thrash and silent quality collapse when stakes rise.

---

## What kind of failure does your work help prevent?

Primary:

- **bad reasoning** under load (no skeleton, no verification placement, wrong mode for R/K/Q)  
- **hallucinations / fabrication under pressure** (anti-lazy Seal / 嘘契約; partial stop culture via gates; success criteria before scoring)  
- **semantic drift** (technique names ≠ sealed behaviours; bomb-skipping named as drift)  
- **coordination problems** (who decides WHAT vs HOW vs IF DONE; expert ownership; baton vs swarm)  
- **loss of trust** (unverified complete-looking output; confidence gates / Tessera)  
- **organizational failure** of multi-step agent work (no HITL convergence, no exploitation/curation, no post-mission reflect)  
- **authority confusion** (models improvising strategy during execution; Imperatus vs Legatus split)  
- **loss of knowledge** across sessions (CEP / output format routing Narrative · MLDoE · CEP)

Not primarily: classical app security red-team, network exploit defense, or org HR policy.

---

## What does your system actually do?

It runs a **fixed command spine** plus mode-scaled modules:

1. **Imperatus (Planning)** — decompose → lock binary success criteria → RKQDE score → sealed execution manifest (mode, formation, experts, bombs, gates, output format).  
2. **Assembly** — Armatura (constraint *levels*), Seal (epistemic contract), USC candidates, Consilium/MR.RUG experts, **Legatus/SkeletrainOT** railroad (nodes, FCoT/CoC, baton/swarm, CoVE placement, bomb coordinates).  
3. **Execution** — follow the railroad; detonate prompt bombs; ARQ/PGScan/CoVE as planned.  
4. **Censor / Intelligent Curation (Exploitation)** — relevance → quality → density; won’t release until success criteria secured.  
5. **Reflect & output** — self-reflect, format, final reflection, 嘘契約 honesty close.

Formations (2x DUPLEX → 3x TRIPLEX → 4x/8x) route **IMBUED → (ENRICH) → EXECUTE** with HITL as convergence. Same modules; different pass order and bomb registries.

---

## What would happen if your system didn’t exist?

You’d still get single-pass “smart” answers that:

- never locked what “done” means before scoring difficulty  
- mix strategy and tactics mid-token  
- skip verification when efficiency pressure rises  
- scale the same shallow path for R3 and R9 work  
- lose multi-expert structure into narrative consensus theatre  
- ship without a curation/exploitation pass that strips waste and checks the mission  

Failure that becomes more likely: **confident complete packages that never passed a sealed plan or a hard success-criteria gate**.

---

## What kinds of inputs does it need?

Generally:

- A raw query / mission brief  
- Optional mode override (e.g. `/deep` → MAXIMUM / Triarii)  
- Domain context the experts can survey  
- For multi-pass formations: human sign-off at HITL gates  
- Spec layer (LEGIO-*.md) or compiled AGENTS.md / MCP tools for runtime  

Not required: LangGraph/CrewAI/n8n; not model weight access.

---

## What kinds of outputs does it produce?

- **Sealed execution manifests** (JSON / structured railroad)  
- **Mode + RKQDE scores** and formation selection  
- **Gate decisions** — PROCEED / HALT (Tessera / ARQ strictness)  
- **Generated deliverables** along the railroad (narrative / MLDoE / CEP formats)  
- **Bomb registries** (strategic + ENRICH emergent)  
- **Curation packages** — densified, criteria-checked finals  
- **Reflection / quality audits** — technique effectiveness, pattern capture  
- **Warnings** when gates fail or Seal / 嘘契約 is violated (shortcut = restart verbose)

Not “vibes advice only” — structured plans, checks, and mission-closed artifacts.

---

## Where do you think your system is strongest?

- **Planning / execution split:** Imperatus WHAT, Legatus HOW, Censor IF DONE  
- **Mode scaling:** Velites → Triarii (QUICK/ANALYTICAL/DELIBERATE/MAXIMUM) so force matches difficulty  
- **Sealed railroad:** zero mid-execution strategy thrash once tracks are laid  
- **Fixed ARQ ribcage** (4 gate positions; strictness dials, not inventing new gates)  
- **Formation flexibility** (DUPLEX/TRIPLEX/… without rewriting IMBUED/EXECUTE identity)  
- **Exploitation as first-class** (Censor / density curation, not “hope the last paragraph is good”)  
- High-stakes research / multi-domain analytical campaigns where complete-looking shallow work is the enemy

---

## What doesn’t it try to do?

- **Not** a single chat persona that “is” the legion without specs/runtime  
- **Not** metaphysics — Roman layer is documentation for humans; models run verbs (Score, Plan, Execute, Verify)  
- **Not** a guarantee of truth — it raises structure, gates, and honesty contracts; external tools/code still needed where claims must be established  
- **Not** (yet) all six formation activation matrices fully filled (several PENDING)  
- **Not** a full universal MCP deployment shipped end-to-end (Forge + skills→MCP still on the build list)  
- **Not** a merger of every other Recursive project into one giant system — LEGIO is one fighting force with clear boundaries  
- **Not** a replacement for human HITL on high formations — human is the convergence criterion on every arrow  

Boundaries: cascade architecture + operator doctrine for quality-gated multi-module execution. Adjacent diagnostics (fabrication frontier, technique honesty) and decision accounting (SCCD/TFAB) are sibling stack pieces, not the LEGIO card itself.

---

## Protects against (Library card)

**Protects against:** undirected multi-step LLM work that improvises strategy mid-generation, skips verification under efficiency pressure, and ships complete-looking output without sealed success criteria — by forcing plan → railroad → execute → exploit/curate with mode-scaled force and hard gates.

---

## Optional metadata for the Library

| Field | Value |
| --- | --- |
| System | LEGIO |
| Version | v30.2 overview / ADR 2026-02-15 |
| Spine | Imperatus · Legatus · Censor (SAS Planning / Execution / Exploitation) |
| Modules | 17 (specs complete per overview) |
| Modes | QUICK / ANALYTICAL / DELIBERATE / MAXIMUM (Velites → Triarii) |
| Formations | 2x–8x IMBUED / ENRICH / EXECUTE routes |
| Deploy target | MCP `imperatus` scaffold; Forge → AGENTS.md → agent runtime |
| Site | ktg.one |

---

*Filled for the Recursive Function Library call · system = LEGIO only · 2026-07-18*
