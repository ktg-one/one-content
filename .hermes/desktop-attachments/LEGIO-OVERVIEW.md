# LEGIO-OVERVIEW.md

--------------------------------------------------------------------------------

title: "LEGIO — System Overview & Architecture"
version: "v30.2"
status: "ACTIVE"
created: "2026-02-16"
updated: "2026-02-22"
creator: "ktg"
category: "overview"
replaces: ["LEGIO-OVERVIEW.md (original)", "LEGIO-ARCHITECTURE-v1.md"]
description: "Single source of truth for LEGIO. What it is, how it works, where it's at. Combines overview + architecture decision record."
LEGIO — THE LEGION
17-Module Prompt Cascade → Agentic Framework
LEGIO (Latin): the legion — Rome's self-contained fighting force. Same units, different formations per campaign. One system, infinite configurations.

--------------------------------------------------------------------------------

1. WHAT LEGIO IS
LEGIO is a 17-module prompt engineering cascade that transforms any query into a structured, multi-expert, quality-gated execution pipeline. Built as KTG-DIRECTIVE v30 (STRAWHATS ADAPTIVE-BATTALION), now being translated into modular specs compiled into executable agent configurations.
LEGIO-*.md (specs) → Forge MCP (compiler) → AGENTS.md (S2A compressed) → Claude Code (runtime)


Specs = blueprints. Forge compiles them into onboarding docs. Models read the onboarding and execute.

--------------------------------------------------------------------------------

2. NAMING RULES
Two rules. No exceptions.
Rule 1 — Roman names = command chain roles.
 Organisational hierarchy. WHO does what.
Rule 2 — Original names = techniques.
 Methods models already recognise from training data. Renaming loses signal.
ROMAN (6 command roles):     ORIGINAL (11 techniques):
├─ Imperatus                 ├─ USC
├─ Armatura                  ├─ ARQ
├─ The Seal                  ├─ Prompt Bombs
├─ Consilium                 ├─ FCoT / CoC
├─ Legatus                   ├─ Baton Bolt / Swarm
└─ Censor                    ├─ CoVE
                             ├─ PGScan
                             ├─ Self-Reflect-Adapt
                             ├─ QMDR / MLDoE
                             └─ CEP


Models need "Score," "Plan," "Execute," "Verify" — not "Imperator," "Legatus," "Praetor."

--------------------------------------------------------------------------------

3. COMMAND CHAIN
Six officers. Fixed order. Each has one job.
┌───────────────────────────────────────────────────────────┐
│  IMPERATUS — Supreme Commander              [LEGIO-00]    │
│  Scores query (RKQDE). Selects mode. Sets all dials.      │
│  OUTPUT → Sealed execution manifest                       │
├───────────────────────────────────────────────────────────┤
│  ARMATURA — The Arsenal                     [LEGIO-01]    │
│  Sets CONSTRAINT LEVELS for every technique.               │
│  Dials, not switches. Even "off" = minimum viable.         │
│  OUTPUT → Constraint levels embedded in manifest           │
├───────────────────────────────────────────────────────────┤
│  THE SEAL — Anti-Lazy Contract (嘘契約)       [LEGIO-02]    │
│  Epistemic honesty binding. Shortcut = restart verbose.    │
│  No manifest executes without contract signature.          │
│  OUTPUT → Signed commitment, execution authorised          │
├───────────────────────────────────────────────────────────┤
│  CONSILIUM — War Council (MR.RUG)           [LEGIO-04]    │
│  Assembles N domain experts. Each surveys terrain.         │
│  Expert count from Imperatus. Formation from Armatura.     │
│  OUTPUT → Expert constellation ready for deployment        │
├───────────────────────────────────────────────────────────┤
│  LEGATUS — Field General (SkeletrainOT)     [LEGIO-05]    │
│  Takes manifest + experts. Lays all tracks: routes,        │
│  patterns, reasoning, bombs, gates, verification.          │
│  OUTPUT → Sealed railroad. Zero decisions during execution │
├───────────────────────────────────────────────────────────┤
│  ═══════════ EXECUTION: The Legion Marches ═══════════    │
│  Tracks laid. Bombs planted. Gates set. Pure speed.        │
│  Experts follow route cards. No planning — just run.       │
├───────────────────────────────────────────────────────────┤
│  CENSOR — Mission Assurance (ISC)           [LEGIO-11]    │
│  Refines output against Imperatus success criteria.        │
│  Won't release until objective is secured.                 │
│  Imperatus opens the mission. Censor closes it.            │
├───────────────────────────────────────────────────────────┤
│  ═══════════ REFINE & OUTPUT: Post-Battle ════════════    │
│  Reflect. Format. Verify. Compress. Deliver.               │
│  Quality loops close. Memory updates. Output ships.        │
└───────────────────────────────────────────────────────────┘


SAS Three-Phase Spine
Three SYSTEM-CORE modules cannot be skipped. They ARE the command spine.
Phase
Module
Roman
Function
Planning
Imperatus (SilRoute)
Imperator
Strategic command — back in Rome, never on field
Execution
Legatus (SkeletrainOT)
Legatus
Tactical command — battle plan, manoeuvres
Exploitation
Censor (ISC)
—
Kill squad — extracts intel, packages deliverable
Imperatus decides WHAT. Legatus decides HOW. Censor decides IF IT'S DONE.

--------------------------------------------------------------------------------

4. IMPERATUS — STRATEGIC COMMAND
Imperatus sits in the capital. Decides army size, equipment, objectives. Four steps:
Step
Action
Output
1. DECOMPOSE
Break prompt apart. Domains, moving parts, implicit needs.
Analysis
2. SUCCESS CRITERIA
Binary checkboxes. BEFORE scoring — can't assess difficulty without knowing "done".
Lock
3. SCORE
RKQDE assessment, informed by decomposition + criteria.
Scores
4. COMMAND
Full strategic decisions → sealed execution manifest (JSON).
Manifest
Imperatus decides:
 iterations, formation, experts, bombs, USC candidates, gate strictness, output format.
 
Imperatus does NOT decide:
 reasoning style per node, execution pattern, CoVE variant, node order. That's Legatus.
Full spec: 
01-LEGIO-Imperatus.md
 (Commander SILROUTE protocol with 10 operational tags)

--------------------------------------------------------------------------------

5. LEGATUS — TACTICAL COMMAND
Takes Imperatus's constraints and decides HOW to fight:
Tactical Decision
Options
Reasoning per node
FCoT (analytical) or CoC (procedural)
Execution pattern
Baton (sequential) or Swarm (parallel)
CoVE variant
Which verification type per checkpoint
Node order
Dependencies, flow, critical path
Quality stations
Placement within the battle plan
Example:
 
Imperatus: "5 experts, 3 USC candidates, 3 iterations, DELIBERATE mode, bombs at X/Y"
 
Legatus: "Node 1 FCoT, Nodes 2-3 Swarm (parallel), Node 4 CoC, CoVE Top-2 after Node 3, Baton handoff A→B at Node 2"
Emperor sets army size and objective. General draws the battle plan.

--------------------------------------------------------------------------------

6. MODE TIERS
Four tiers. Named for Roman military ranks. Tiers set CONSTRAINT LEVELS across all techniques simultaneously.
Tier
Name
Role
Trigger
USC
Experts
Skeleton
QUICK
Velites
Light skirmishers
R≤3 ∧ Q≤5
0
0
Direct
ANALYTICAL
Hastati
Front line
R=4-6 ∨ Q=6-7
2
3
Light
DELIBERATE
Principes
Second line
R≥7 ∨ K≥6 ∨ Q≥8
3
5
Full/DAG
MAXIMUM
Triarii
Veterans
R≥9 ∨ K≥8 ∨ /deep
5
5-8
GoT
"It has come to the Triarii"
 — Roman saying for when the situation demands everything you have.
RKQDE scoring:
 R=Reasoning depth, K=Knowledge complexity, Q=Quality stakes, D=Decomposition breadth, E=Edge-case density.
Mode selection
 uses RLoT-adaptive routing (Σ + Danger), not static thresholds. See Imperatus spec for full routing logic.

--------------------------------------------------------------------------------

7. THE PIPELINE
17 modules across 4 zones. Sequential numbering, no gaps.
PRE-FLIGHT (LEGIO-00 → 03) — Before the legion moves
#
File
Name
Function
00
LEGIO-00-IMPERATUS_CORE_.md
Imperatus
Scores query (RKQDE). Selects mode tier. Sets success criteria. Issues sealed manifest.
01
LEGIO-01-ARMATURA_CORE_.md
Armatura
Sets constraint LEVELS for every technique. Pipeline is fixed — dials, not switches.
02
LEGIO-02-CONTRACT_SEAL_.md
The Seal
Anti-lazy contract. 嘘契約 epistemic binding. Shortcut = restart. Signs before execution.
03
LEGIO-03-USC_MOD_.md
USC
Universal Self-Consistency. Generates N candidates (0/2/3/5 by mode). Selects or synthesises.
ASSEMBLY (LEGIO-04 → 06) — Assembling the force
#
File
Name
Function
04
LEGIO-04-CONSILIUM_MOD_.md
Consilium
 (MR.RUG)
War council. Assembles domain experts. Each expert surveys terrain, proposes nodes.
05
LEGIO-05-LEGATUS_CORE_.md
Legatus
 (SkeletrainOT)
Field general. Builds execution skeleton. Lays all 6 track types. Seals railroad.
06
LEGIO-06-PROMPT-BOMBS_KIT_.md
Prompt Bombs
Pre-compressed context packets. Planted at coordinates. Detonate on trigger.
EXECUTION (LEGIO-07 → 10) — The legion marches
#
File
Name
Function
07
LEGIO-07-FCOT-COC_MOD_.md
FCoT / CoC
Reasoning style per node. FCoT = exploration. CoC = deterministic. Hybrid available.
08
LEGIO-08-BATON-SWARM_MOD_.md
Baton Bolt / Swarm
Execution patterns. Baton = sequential handoff. Swarm = parallel strike. + Iteration.
09
LEGIO-09-COVE_MOD_.md
CoVE
Chain of Verification. Factual / Logical / Consistency / Multi-Expert variants.
10
LEGIO-10-PGSCAN-ARQ_MOD_.md
PGScan + ARQ
Post-execution gap scan. Cross-candidate synthesis. ARQ quality gates.
REFINE & OUTPUT (LEGIO-11 → 16) — After the battle
#
File
Name
Function
11
LEGIO-11-CENSOR_CORE_.md
Censor
 (ISC)
Mission assurance. ToT synthesis (5 paths) + 3-stage curation (relevance → quality → density). Won't release until objective secured. SYSTEM-CORE.
12
LEGIO-12-SELF-REFLECT_MOD_.md
Self-Reflect-Adapt
Technique effectiveness audit. 4-phase: inventory → effectiveness → patterns → metadata. BoT + CEP contribution.
13
LEGIO-13-OUTPUT-FORMAT_MOD_.md
Output Format
Delivery shape router: Narrative (human) / MLDoE (AI iteration) / CEP (cross-session). Decided at Imperatus, executed here.
14
LEGIO-14-FINAL-REFLECT_MOD_.md
Final Reflection
Mandatory ALL modes. Success criteria check. Confidence 0-10. 嘘契約 enforcement. Closes loop with Imperatus.
15
LEGIO-15-QMDR_MOD_.md
QMDR / MLDoE
Multi-Layer Density of Experts enrichment. Cross-candidate learning synthesis.
16
LEGIO-16-CEP_MOD_.md
CEP
Context Engineering Protocol. Memory compression. 嘘契約 final check.

--------------------------------------------------------------------------------

8. ACTIVATION MATRIX (v30)
Full 18-step view (v30 source numbering) showing mode-per-step scaling. The 17-module LEGIO numbering absorbs Success Criteria Lock into Imperatus and defers Buffer Valet.
Pre-Flight
Step
Module
QUICK
ANALYTICAL
DELIBERATE
MAXIMUM
0
IMPERATUS
 (SYSTEM-CORE)
All
All
All
All
1
Success Criteria Lock
Implicit
Explicit
Signature
Multi-constraint
2
—
Buffer Valet (FUTURE)
—
—
—
3
ARQ
Pre-turn 1Q
Pre-turn 1-2Q
Pre+Post
Full
4
Anti-Lazy Protocol
Optional
Required
Required
Required+Enforced
5
USC
1-path
2 candidates
3 candidates
5+ meta
→ Confidence Gate: >9/10 to proceed
Pipeline
Step
Module
QUICK
ANALYTICAL
DELIBERATE
MAXIMUM
6
MR.RUG (+ARQ gate)
Optional
3 experts
5+ experts
20+ experts
7
LEGATUS
 (SYSTEM-CORE)
Direct
Light 3-5 nodes
Full 5+ nodes
Graph-of-Thought
8
Prompt Bombs
Clarifier
Clarifier+Scaffold
Full Arsenal
Deep injection
→ Confidence Gate: all experts >9/10 to proceed
Execute
Step
Module
QUICK
ANALYTICAL
DELIBERATE
MAXIMUM
9
FCoT/CoC routing
CoC
FCoT
FCoT+ARQ
Mix+ARQ
10
Iteration Protocol
Single
Optional multi
3-pass required
3-pass enforced
11
Swarm/Baton
Direct gen
Baton
Baton+ARQ
Swarm+ARQ
12
CoVE (+ARQ gate)
Skip
Top-1
Top-2
All ≥4
13
PGScan
Skip
Light
3-branch
Deep+AutoFix
Refine & Output
Step
Module
QUICK
ANALYTICAL
DELIBERATE
MAXIMUM
14
CENSOR
 (SYSTEM-CORE)
Lean/Max density
Normal
Normal+Nuance
All-Out
15
Self-Reflect-Adapt
Skip
Optional
Required
Full+BoT
16
Output Format Selection
Narrative / MLDoE / CEP — decided at Imperatus
17
Final Reflection
Mandatory ALL modes
18
Epistemic Compliance 嘘契約
Honesty contract
→ Confidence Gate: >9/10 to proceed

--------------------------------------------------------------------------------

9. ARQ GATE POSITIONS
Four fixed structural checkpoints. Imperatus controls STRICTNESS, not count.
Gate
Position
Check
1
During MR.RUG
Per expert summoned — does this expert belong?
2
After Legatus
Plan validates against success criteria
3
Before execution finishes
Generated content matches plan
4
Before output
Final success criteria verification
QUICK = light touches (advisory)
MAXIMUM = hard HALT on failure
ARQ is the ribcage — always four positions. Everything else flexes around it.

--------------------------------------------------------------------------------

10. FORMATION TEMPLATES
Six use-case formations (config files, not code). Same legion, different arrangement.
Formation
Roman
Use Case
Status
TBD
Testudo (tortoise)
High-stakes research
PENDING
TBD
Triplex Acies (triple line)
Standard analytical
PENDING
TBD
Cuneus (wedge)
Quick tasks
PENDING
TBD
Orbis (circle)
Multi-domain
PENDING
TBD
TBD
Coding
PENDING
TBD
TBD
Creative
PENDING
Each template defines: which of 17 modules activate, order, parameters.

--------------------------------------------------------------------------------

11. MCP DEPLOYMENT
Decision: MCP IS the agent framework
No LangGraph (inaccessible, bloated)
No CrewAI (opinionated handoffs)
No n8n rebuild (workflow tool, not agent orchestration)
MCP = universal protocol (Claude, GPT, Gemini all support)
Single MCP Server: 
imperatus
score(query) → R/K/Q/D + mode + formation
formation(mode, use_case) → activation matrix
gate_check(phase, confidence) → PROCEED/HALT
reflect(execution_log) → quality audit + pattern capture


MCP as Scaffold Pattern
MCP tool provides the framework/structure
Host model does the thinking
Tags/modes = routing decisions
stepNumber/totalSteps = progress tracking
nextStepNeeded = HALT/PROCEED gates
Migration Path (Skills → MCP)
Current Skill
Target MCP Tool
mr-rug
MR.RUG MCP tool
enrichweave
Enrichment MCP tool
context
CEP MCP tool
ktg-prompt-forge
PromptForge MCP tool
Skills are currently Claude-specific. MCP makes them universal.

--------------------------------------------------------------------------------

12. ARCHITECTURE
              HUMAN LAYER                      MACHINE LAYER
        ┌──────────────────┐            ┌──────────────────────┐
        │  LEGIO-*.md      │            │  AGENTS.md           │
        │  (17 spec files) │──→ FORGE ──│  (S2A compressed     │
        │  Human-readable  │   (MCP)    │   onboarding doc)    │
        │  Full elaboration│            │  Model reads this    │
        └──────────────────┘            └──────────┬───────────┘
                                                    │
                                                    ▼
                                         ┌──────────────────────┐
                                         │  Claude Code         │
                                         │  (Runtime execution) │
                                         │  Follows the railroad│
                                         └──────────────────────┘


Specs
 (LEGIO-*.md) = human-readable blueprints
Forge
 = offline MCP compiler. Reads specs, applies S2A compression, outputs AGENTS.md
AGENTS.md
 = onboarding document a model reads before executing
Runtime
 = Claude Code (or any agent) executing the pipeline. No decisions — follow the railroad

--------------------------------------------------------------------------------

13. CROSS-CUTTING SYSTEMS
System
Status
How It Works
Tier System
 (Velites → Triarii)
DEFERRED
Constraint overlays applied AFTER full path documented
ARQ
 (Quality Gates)
DEFINED
Co-located with 4 hosts: Consilium, Legatus, PGScan, Self-Reflect
GoT
 (Graph-of-Thought)
DONE
In Legatus. Three topologies: Railroad (SoT), Rail Network (DAG), Metro (GoT)
嘘契約
 (Epistemic Contract)
DONE
In The Seal. ①knows non-compliance ∧ ②knows instruction ∧ ③pretends done = LIE
Absorbed (no standalone spec):
Success Criteria Lock → inside Imperatus 
[ground]
 tag
Buffer Valet → FUTURE (commented out in v30)
ARQ pre-flight → co-located with host modules
Additional Roman Mappings (Documentation Layer)
Component
Roman Name
Function
Confidence gates
Tessera
Watchword system — don't pass without it
Prompt Bombs
Scorpiones
Pre-positioned artillery
MR.RUG expert squads
Contubernium
8-man tactical units
CoVE verification
Frumentarii
Military intelligence/reconnaissance
Phase: Pre-flight
Praefectus Castrorum
Camp prefect (logistics)
Phase: Pipeline
Legatus
Strategic planning
Phase: Execute
Primus Pilus
First spear (leads the charge)
Phase: Refine
Optio
Second-in-command (quality control)
Phase: Output
Aquilifer
Eagle bearer (carries the standard)

--------------------------------------------------------------------------------

14. BUILD PROGRESS
PRE-FLIGHT (00-03):  ████████████ DONE
ASSEMBLY (04-06):    ████████████ DONE
EXECUTION (07-10):   ████████████ DONE
REFINE (11-16):      ████████████ DONE
CROSS-CUTTING:       ████████░░░░ 3/5

TOTAL: 17/17 modules written + 4 meta ✓ ALL SPECS COMPLETE



--------------------------------------------------------------------------------

15. MODULE INDEX
#
File
Name
Zone
Status
00
LEGIO-00-IMPERATUS_CORE_.md
Imperatus
SYSTEM-CORE
DONE
01
LEGIO-01-ARMATURA_CORE_.md
Armatura
SYSTEM-CORE
DONE
02
LEGIO-02-CONTRACT_SEAL_.md
The Seal + 嘘契約
PRE-FLIGHT
DONE
03
LEGIO-03-USC_MOD_.md
USC
PRE-FLIGHT
DONE
04
LEGIO-04-CONSILIUM_MOD_.md
Consilium (MR.RUG + GSIF)
ASSEMBLY
DONE
05
LEGIO-05-LEGATUS_CORE_.md
Legatus (SkeletrainOT) + GoT
SYSTEM-CORE
DONE
06
LEGIO-06-PROMPT-BOMBS_KIT_.md
Prompt Bombs
ASSEMBLY
DONE
07
LEGIO-07-FCOT-COC_MOD_.md
FCoT / CoC
EXECUTION
DONE
08
LEGIO-08-BATON-SWARM_MOD_.md
Baton Bolt / Swarm
EXECUTION
DONE
09
LEGIO-09-COVE_MOD_.md
CoVE + 10Rs + Negentropy
EXECUTION
DONE
10
LEGIO-10-PGSCAN-ARQ_MOD_.md
PGScan + ARQ
EXECUTION
DONE
11
LEGIO-11-CENSOR_CORE_.md
Censor
 (ISC)
SYSTEM-CORE
DONE
12
LEGIO-12-SELF-REFLECT_MOD_.md
Self-Reflect-Adapt
REFINE
DONE
13
LEGIO-13-OUTPUT-FORMAT_MOD_.md
Output Format
OUTPUT
DONE
14
LEGIO-14-FINAL-REFLECT_MOD_.md
Final Reflection + 嘘契約
OUTPUT
DONE
15
LEGIO-15-QMDR_MOD_.md
QMDR / MLDoE
OUTPUT
DONE
16
LEGIO-16-CEP_MOD_.md
CEP + 嘘契約 final
OUTPUT
DONE
—
LEGIO-FORGE-SCHEMA_SPEC_.md
Forge Schema Spec
META
DONE
—
LEGIO-STATUS.md
Translation Status
META
DONE
—
LEGIO-OVERVIEW.md
This document
META
DONE

--------------------------------------------------------------------------------

16. NEXT PRIORITIES
Tier overlays
 — Velites→Triarii constraint tables for each module. Full path now documented.
Cleanup
 — Archive misnamed 
LEGIO-08-PROMPT-BOMBS_KIT_.md
 duplicate. Review nSilRoute.md for Imperatus gaps.
Formation templates
 — Six use-case configurations (Testudo, Triplex Acies, Cuneus, Orbis, Coding, Creative).
Forge MCP
 — Build compiler: specs → S2A-compressed AGENTS.md.
Skills → MCP
 — Convert mr-rug, enrichweave, context, ktg-prompt-forge to universal MCP tools.
Pending Decisions
[ ] Six formation templates: define specific use cases and activation matrices
[ ] Prompt-bombs toolkit design (standalone tool)
[ ] MCP server implementation of Imperatus
[ ] Skills → MCP migration (mr-rug, enrichweave, context, ktg-prompt-forge)
[ ] kTTT integration: how Imperatus decides iteration count (1/2/3 runs)

--------------------------------------------------------------------------------

17. EVOLUTION NOTES
v28 → v30 Changes
Aspect
v28 (Sil-Route + Tech Gate)
v30 (Commander SILROUTE / Imperatus)
Architecture
2 separate modules
Unified command module
Routing
Static threshold tables
RLoT-adaptive scoring (Σ + Danger)
Prompt Bombs
Planted during SkeleTraIn
Pre-embedded in manifest by Commander
Tool allocation
Ad-hoc per phase
Pre-assigned in delegation matrix
Cross-model
CEP v6 INTER (manual)
Automatic detection + model selection
Skip logic
Per-mode fixed grid
Commander's discretion per RKQDE
Mid-flight
No re-routing
adapt
 tag with escalation rules
Audit trail
Verbose only
Full audit mode with bomb/gate tracking
ArXiv Integrations (Jan 2026 Sweep)
Paper
Integration Point
2505.14140 (RLoT)
Adaptive routing replaces static technique gate
2601.08058 (Latent Reasoning)
Reasoning path selection includes latent mode signals
2601.10825 (Societies of Thought)
Expert persona diversity as mechanistic requirement
2601.21484 (Test-Time Scaling)
Energy-guided budget scaling in 
arm
 phase
2601.20439 (PEARL)
Planner-executor split formalized in delegation
2510.07505 (PEAR)
Multi-proxy-executor pattern in swarm mode
2601.08108 (Sketch-of-Thought)
Compression fallback in 
adapt
 phase

--------------------------------------------------------------------------------

SOURCE REFERENCES
Source
Maps To
01-LEGIO-Imperatus.md
Commander SILROUTE full protocol (10 tags, activation matrix, delegation)
STRAWHATS-v30-ADAPT.md
Full v30 pipeline (KTG root)
N00-CORE-STRAWHATS-meta-v30.md
Meta architecture (KTG root)
Skills: mr-rug, enrichweave, context, ktg-prompt-forge
MCP migration candidates

--------------------------------------------------------------------------------

LEGIO v30.2 | System Overview & Architecture | 2026-02-21 | ktg.one
 
"Imperatus commands. Consilium advises. Legatus plans. The legion executes. Censor secures."