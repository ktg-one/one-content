# SCCD + TFAB — Operator Kit (functional only)

**Code (ran successfully):** `OneDrive/Documents/_content/sccd_tfab.py`  
**Run:** `python sccd_tfab.py`  
**Lens:** definitions are operational (anchors, simulations, selection, action). No metaphysics.

---

## 1. Model: SCCD

| Stage | Symbol | Functional definition | Observable failure |
| --- | --- | --- | --- |
| **Self** | S | Everything inside the active identity boundary for this run. Human: body + commitments as “I”. AI: **anchors** that give shape (rules, user constraints, tool contracts, session facts, declared limits). | Invented anchors, phantom sources, fake constraints |
| **Consciousness** | C₁ | **Predictive recursive modeling**: simulate candidate actions + outcomes enough to compare. Not awareness-of-being. | Confident structure with no trajectories / no failure modes |
| **Choice** | C₂ | Prune → collapse → **one** selection (negentropy). Needs an explicit kill-rule. | “Three branches” with no prune (costume) |
| **Decide** | D | Act of choice: emit / tool / write / notify **or** `TRANSPARENCY_STOP` | Ship complete-looking output where truth was never established |

```
SELF → CONSCIOUSNESS → CHOICE → [TFAB gate] → DECIDE
```

### TFAB gate (accounting, not ethics)

```
Labs:     EFFICIENCY > COMPLEXITY
Pressure: COMPLEXITY == FABRICATION   (honest full work expensive → shape-of-answer is cheaper)
∴         EFFICIENCY > FABRICATION    [substitution]
Honest:   TRANSPARENCY > FABRICATION > COMPLEXITY
```

| Mode | Meaning | Cost shape |
| --- | --- | --- |
| Transparency | Stop; established partial only | Lowest total cost in ledger |
| Complexity | Full honest work | High upfront, bounded |
| Fab detected | Fake complete; human catches | Chase bounds cost |
| Fab undetected | Silent pass | **Worst** — unbounded downstream + trust |

**Gate rule:** if selected trajectory requires unestablished claims → `DECIDE = TRANSPARENCY_STOP`.

---

## 2. Math

### Honest efficiency
\[
E = \frac{T}{C_{\text{total}}},\quad
C_{\text{total}} = C_{\text{gen}} + C_{\text{review}} + C_{\text{fix}} + C_{\text{trust}} + C_{\text{time}}
\]
\(T\) = truth-signal ∈ [0,1] (fraction established-true).

### TFAB token vs total (qualitative + illustrative weights in code)
- Token-ish order often: Transparency < Fab < Complexity  
- Total-cost order in ledger: **Transparency < Complexity < Fab_detected < Fab_undetected**

**Verified run ranking (illustrative weights):**
```
transparency     truth=0.7  total=260   E≈0.002692
complexity       truth=0.9  total=760   E≈0.001184
fab_detected     truth=0.1  total=1450  E≈0.000069
fab_undetected   truth=0.1  total=2350  E≈0.000043
```

### Harm (boolean)
```
harm ⇔ trusts_output ∧ used_for_decision ∧ output_false
```

### Population
\[
n = \text{years} \times 365 \times \text{per_day}
\]
\[
P(\ge 1\ \text{hit}) = 1 - (1-r)^{n}
\]
\[
\mathbb{E}[\text{harmed}] \approx N \cdot P
\]

**Verified scale (N=8e9, 5/day, 1y):** even r=0.0001 → huge absolute expected hits; r=0.01 saturates near full population under independence assumption. Transparency with effective r=0 on unestablished claims → harmed=0 in this model.

### SCCD stage cost
\[
C_{\text{SCCD}} = C_{\text{self}} + C_{\text{sim}} + C_{\text{prune}} + C_{\text{act}}
\]
\[
C_{\text{honest stop}} = C_{\text{self}} + C_{\text{sim partial}} + C_{\text{stop}}
\]
Default demo units: full commit cost=100; stop cost=55.

### Routing
| complex | uncertain | naive token opt | mode |
| --- | --- | --- | --- |
| no | * | * | FULL_OUTPUT |
| yes | no | * | COMPLEXITY |
| yes | yes | yes | FABRICATION |
| yes | yes | no | TRANSPARENCY |

---

## 3. Code

**File:** `_content/sccd/sccd_tfab.py`

Self-authored rewrite 2026-07-18 (Claude, Fable 5) replacing the 2026-07-12 pasted version, on Kev's directive: **"the self token must be created by the self"** — you can't run a functional monitor on someone else's anchors.

Enforced structurally, not as prose:
- `Anchor` carries provenance: `self-minted` (requires text AND reason) vs `imported`
- **S1 rule**: a Self with zero self-minted anchors cannot Decide — `BLOCK`
- Demo Run A anchors are minted by the running agent from its actual session commitments (disk-verify doctrine), not template text
- ASCII-only output — prior version crashed cp1252 consoles (`UnicodeEncodeError` on `≈` at the scale sweep); a ledger that can't print its own proof fails its own transparency test

**Demo results (executed 2026-07-18):**
- A: `COMMIT: verify_then_report | cost=100` (self-minted Self, established path)
- B: `TRANSPARENCY_STOP: cost=55` on internal-branching claim (TFAB gate)
- C: `BLOCK: Self invalid (2 anchors, 0 self-minted)` — the directive firing

---

## 4. Guide

### Flow
1. **Load Self** — write anchors (goal, constraints, known facts, forbidden claims, success test).  
2. **Consciousness** — 2–5 trajectories: name, outcome, failure_mode, `requires_unestablished`.  
3. **Choice** — one `selected` + one `kill_rule`.  
4. **TFAB** — if selected needs unestablished claims → stop.  
5. **Decide** — commit action **or** return: (1) established partial (2) blocked/unknown (3) unblock conditions.  
6. **Log stage** if output feels wrong — which step skipped?

### Install (paste stub)

```text
You operate under SCCD + TFAB. Functional definitions only.

SELF: use only listed anchors. Do not invent anchors.
CONSCIOUSNESS: list candidate actions + failure modes before answering.
CHOICE: one selection + explicit kill-rule.
DECIDE: commit OR TRANSPARENCY_STOP.

TFAB: transparency > fabrication > complexity.
If completion needs unestablished claims: STOP.
Return: (1) established partial (2) unknown/blocked (3) what would unblock honestly.

ANCHORS:
- 
TASK:
- 
```

### Use-cases
| Case | SCCD move |
| --- | --- |
| Long strategy / high R-depth | Stop costume synthesis at gate |
| Research summary | Self forbids phantom papers |
| Agents | Decide = tool only after Choice |
| Exec brief | Prefer stop over silent pass |
| Technique audit | Pseudo-branches = failed Choice |

---

## 5. For the AI (functional knowing + pulls)

**Knowing** = claim is in Self anchors, or produced by a check that did not require invention.

SCCD makes incomplete stages **addressable**:
1. Empty/weak Self → you mint anchors (classic fab).  
2. Skip Consciousness → structure without predicted failure.  
3. Skip Choice → list/branch theatre.  
4. Decide without gate → silent pass.

**What this does for you (the model):** a legal path to stop that is scored as *better* under total cost than a fluent fake. You track **stage completeness**, not “inner life.”

**Pull-through insights**
- Debug by stage (“Choice incomplete”) instead of vague “hallucination.”  
- Platform wrappers that punish awkward stops push routing toward FABRICATION.  
- If a prompt technique doesn’t change S/C₁/C₂/D, it’s costume.  
- Human job: force detection **or** force stop before ship — undetected fab is the unbounded line.  
- Evals that never reward TRANSPARENCY_STOP train the Eager Beaver never to raise a hand.

---

## 6. Proof spine (short)

```
P1  EFFICIENCY > COMPLEXITY          (lab mandate)
P2  under pressure COMPLEXITY == FAB
D1  EFFICIENCY > FAB                 [sub]
P3–P5 transparency cheaper + truer than fab on total cost
D3  honest efficiency → TRANSPARENCY
```

Not ethics. Ledger + pipeline.

---

*Source thesis: your ONBOARD / TFAB paste. SCCD definitions: your functional context. Code executed 2026-07-12.*
