# LEGIO-ARCHITECTURE-v1.md

LEGIO — Architecture Decision Record
STRAWHATS v30 ADAPTIVE-BATTALION → LEGIO
Session: 2026-02-15 | COP-R9/10-architecture-legio-imperatus

--------------------------------------------------------------------------------

1. SYSTEM RENAME
STRAWHATS v30 ADAPTIVE-BATTALION
 → 
LEGIO
Roman Legion: self-contained fighting force (~5,000). Same 18 agents, different formations per use case.
Naming Decision: Two Layers
Roman names
 = documentation layer (humans, Council, ArXiv, clients)
Functional names
 = execution layer (models parse verbs not nouns)
Models need "Score," "Plan," "Execute," "Verify" — not "Imperator," "Legatus," "Praetor."

--------------------------------------------------------------------------------

2. MODE TIERS → ROMAN RANKS
Mode
Roman
Role
Trigger
QUICK
Velites
Light skirmishers, first contact
R≤3 ∧ Q≤5
ANALYTICAL
Hastati
Front line infantry, standard
R=4-6 ∨ Q=6-7
DELIBERATE
Principes
Experienced second line
R≥7 ∨ K≥6 ∨ Q≥8
MAXIMUM
Triarii
Veteran reserves
R≥9 ∨ K≥8 ∨ /deep
"It has come to the Triarii" — Roman saying for critical situations.

--------------------------------------------------------------------------------

3. THREE SYSTEM-CORE MODULES → SAS MISSION PHASES
These three cannot be skipped. They ARE the command spine.
Step
Module
SAS Phase
Roman (docs only)
Function
0
Imperatus
 (SilRoute)
Planning
Imperator (Emperor)
Strategic command — back in Rome, never on field
7
SkeletrainOT
Execution
Legatus (General)
Tactical command — battle plan, maneuvers
14
Intelligent Curation
Exploitation
—
Finds the findings — extracts intel post-assault
SAS Three-Phase Mission Structure:
Planning
 — Set constraints, objectives, resource allocation (Imperatus)
Execution
 — Tactical delivery of the assault (SkeletrainOT)
Exploitation
 — Go in after, extract intelligence, package for next unit (Intelligent Curation)
Intelligent Curation = SAS exploitation team. Not a judge (Praetor). A 
kill squad
 that surgically removes waste, maximizes density, packages the deliverable. Relevance filter → quality assessment → 5× CoD density optimization.

--------------------------------------------------------------------------------

4. IMPERATUS — STRATEGIC COMMAND SEQUENCE
Imperatus sits in the capital. Decides army size, equipment, objectives. Four steps:
Step 1: DECOMPOSE
Break prompt apart. What's asked? What domains? Moving parts? Analysis before judgment.
Step 2: SUCCESS CRITERIA
Define "done" with binary checkboxes. Must come BEFORE scoring — can't assess difficulty without knowing what success means.
Step 3: SCORE
R/K/Q/D assessment. Now informed by decomposition AND success criteria. Accurate, not guesswork.
Step 4: COMMAND (the payload)
Full strategic decisions — outputs a complete execution manifest (JSON):
Decision
Options
Iterations
1-shot / 2-run / 3-run (kTTT vs ADAPT)
Formation
Which of 18 agents activate, which cut
Experts
Which MR.RUG specialists (templated per use case)
Bombs
How many, placement (toolkit decides)
Candidates
How many USC paths
Gate strictness
Light touches (QUICK) → hard HALT (MAXIMUM)
Output format
Narrative / MLDoE / CEP
Imperatus does NOT decide:
 reasoning style per node, execution pattern, CoVE variant, node order. That's SkeletrainOT's job.

--------------------------------------------------------------------------------

5. SKELETRAIN-OT — TACTICAL COMMAND
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
Example Flow:
Imperatus:
 "5 experts, 3 USC candidates, 3 iterations, DELIBERATE mode, bombs at positions X/Y"
 
SkeletrainOT:
 "Node 1 FCoT (analytical), Nodes 2-3 Swarm (parallel independent), Node 4 CoC (procedural), CoVE Top-2 after Node 3, Baton handoff Expert A→B at Node 2"
Emperor sets army size and objective. General draws the battle plan.

--------------------------------------------------------------------------------

6. ARQ GATE POSITIONS — FIXED (Not Variable)
ARQ gates are structural checkpoints, hardwired. Imperatus controls STRICTNESS, not count.
Position
When
Check
Gate 1
During MR.RUG
Per expert summoned — does this expert belong?
Gate 2
After SkeletrainOT
Plan validates against success criteria
Gate 3
Before execution finishes
Generated content matches plan
Gate 4
Before output
Final success criteria verification
QUICK = light touches (advisory)
MAXIMUM = hard HALT on failure
ARQ is the ribcage — always four positions. Everything else flexes around it.

--------------------------------------------------------------------------------

7. FORMATION TEMPLATES
Six use-case formations (config files, not code). Same legion, different arrangement:
Formation
Roman
Use Case
Notes
TBD
Testudo (tortoise)
High-stakes research
Maximum protection
TBD
Triplex Acies (triple line)
Standard analytical
Workhorse
TBD
Cuneus (wedge)
Quick tasks
Fast penetration
TBD
Orbis (circle)
Multi-domain
Complex/surrounded
TBD
TBD
Coding
TBD
TBD
Creative
Each template defines: which of 18 agents activate, order, parameters.

--------------------------------------------------------------------------------

8. MCP DEPLOYMENT ARCHITECTURE
Decision: MCP IS the agent framework
No LangGraph (inaccessible, bloated)
No CrewAI (opinionated handoffs)
No n8n rebuild (workflow tool, not agent orchestration)
MCP = universal protocol (Claude, GPT, Gemini all support)
Single MCP Server: 
imperatus
Tools exposed:
score(query) → R/K/Q/D + mode + formation
formation(mode, use_case) → activation matrix
gate_check(phase, confidence) → PROCEED/HALT
reflect(execution_log) → quality audit + pattern capture


MCP as Scaffold Pattern (from Lotus Wisdom analysis)
MCP tool provides the framework/structure
Host model does the thinking
Tags/modes = routing decisions
stepNumber/totalSteps = progress tracking
nextStepNeeded = HALT/PROCEED gates
Migration Path
Existing skills → MCP servers:
/mnt/skills/user/mr-rug/
 → MR.RUG MCP tool
/mnt/skills/user/enrichweave/
 → Enrichment MCP tool
/mnt/skills/user/context/
 → CEP MCP tool
/mnt/skills/user/ktg-prompt-forge/
 → PromptForge MCP tool
Skills are currently Claude-specific. MCP makes them universal.

--------------------------------------------------------------------------------

9. FULL 18-MODULE PIPELINE (v30)
Phase 1: PRE-FLIGHT (Quality Foundation)
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
Phase 2: PIPELINE (Structure Planning)
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
SKELETRAIN-OT
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
Phase 3: EXECUTE (Generate Content)
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
Phase 4: REFINE & SYNTHESIZE (Polish)
Step
Module
QUICK
ANALYTICAL
DELIBERATE
MAXIMUM
14
INTELLIGENT CURATION
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
→ Confidence Gate: >9/10 to proceed
Phase 5: OUTPUT (Delivery Format)
Step
Module
Notes
16
Output Format Selection
Narrative / MLDoE / CEP — decided at Imperatus Step 4
17
Final Reflection
Mandatory ALL modes
18
Epistemic Compliance 嘘契約
Honesty contract

--------------------------------------------------------------------------------

10. ADDITIONAL MAPPINGS (Documentation Layer)
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

11. PENDING DECISIONS
[ ] Six formation templates: define specific use cases and activation matrices
[ ] Prompt-bombs toolkit design (standalone tool)
[ ] MCP server implementation of Imperatus
[ ] Skills → MCP migration (mr-rug, enrichweave, context, ktg-prompt-forge)
[ ] Roman name for Intelligent Curation (exploitation phase) — or keep functional
[ ] kTTT integration: how Imperatus decides iteration count (1/2/3 runs)

--------------------------------------------------------------------------------

12. SOURCE REFERENCES
/mnt/project/KTG-v30-ADAPT.md
 — Full v30 pipeline
/mnt/project/N00-CORE-STRAWHATS-meta-v30.md
 — Meta architecture
/mnt/project/07-PLAN02-SkeletrainOT_CORE_v2_1.md
 — SkeletrainOT spec
/mnt/project/13-POST01-INT-SYN-CUR_CORE_.md
 — Intelligent Curation spec
/mnt/project/N01-PRE00-Sil-Route_CORE_.md
 — SilRoute (→ Imperatus)
/mnt/project/06-PLAN01-MR-RUG-_SKILL_.md
 — MR.RUG spec
/mnt/project/N06-PLAN01-MR-RUG-_SKILL_.md
 — MR.RUG skill variant
/mnt/skills/user/context/SKILL.md
 — CEP v14 (context save)
/mnt/skills/user/mr-rug/SKILL.md
 — MR.RUG skill (→ MCP candidate)
/mnt/skills/user/enrichweave/SKILL.md
 — Enrich skill (→ MCP candidate)
/mnt/skills/user/ktg-prompt-forge/SKILL.md
 — PromptForge skill (→ MCP candidate)

--------------------------------------------------------------------------------

LEGIO v1 | Architecture Decision Record | 2026-02-15 | ktg.one