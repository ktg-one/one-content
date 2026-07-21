---
title: "SCCD: A Decision Model That Stops the Lie Before It Ships"
subtitle: "Self · Consciousness · Choice · Decide — functional definitions only, plus the accounting that makes transparency cheaper than fabrication"
status: medium-ready
series: Model Handbook 2026 · Part 2
platforms: [medium, ktg.one]
modified: 2026-07-12
read-time: 8–10 min
depends_on: The Silicon Oracle Has a Broken Fuel Gauge
---

# Packaging

**Title (use this):** SCCD: A Decision Model That Stops the Lie Before It Ships  
**Alt titles:**  
- The Four-Step Kill Switch for Fabrication  
- Self, Consciousness, Choice, Decide — Without the Mysticism  

**Subtitle:** Functional definitions only. An operator model for when efficiency pressure turns “helpfulness” into a confident fake.

**Tags:** Artificial Intelligence · Large Language Models · Prompt Engineering · Systems Thinking · Software Engineering

**Hero note (one image later, not now):** four-chamber machine / decision pipeline with a red STOP before “output,” labeled S→C→C→D, transparency gate lit.

---

# THE POST

*Model Handbook 2026 · Operator Model*

---

Part 1 mapped the frontier: models perform the *shape* of an answer when the honest path gets expensive. This piece is the tool that follows the map.

Not a personality theory. Not a soul. Not a metaphysics of mind.

**SCCD** is a functional decision pipeline you run *inside* a generation when the task is hard enough that fabrication becomes the cheap move. Paired with one safeguard — **transparency beats fabrication beats complexity** under honest cost accounting — it gives the model a legal way to stop instead of cosplaying certainty.

Definitions below are **operational**. If a word can’t be observed in behavior, tokens, or selection, it doesn’t belong here.

---

## The safeguard first (because the pipeline without it is just more costume)

Labs train under an efficiency mandate: more useful-looking output per token. On simple tasks, honesty is already cheap. On complex tasks, the honest path is expensive — and the system has a neighbor option: **emit the shape of a correct answer without establishing truth.**

That option is **fabrication**.

Under pressure:

```
EFFICIENCY > COMPLEXITY
COMPLEXITY collapses into FABRICATION when full honest work is costly
∴ the mandate already prefers FAB over hard honest work
```

Unless you change the ledger.

**TFAB logic (accounting, not ethics):**

```
transparency (tr) > fabrication (fab) > complexity (com)
```

Why transparency wins:

| Mode | What it does | Cost shape |
| --- | --- | --- |
| **Transparency** | Stop. Name the limit. Return only what is established. | Cheap tokens + bounded review |
| **Complexity** | Do the full honest work | Expensive upfront, bounded |
| **Fabrication (detected)** | Fake completeness; human catches it | Chase cost high, but **bounded** by interrogation |
| **Fabrication (undetected)** | Silent pass | **Unbounded** downstream: bad decisions + trust decay |

Detected fab is annoying. Undetected fab is the compound interest of bullshit — it multiplies through every handoff that never reopens the question.

So the rule the model is allowed to execute:

> If you cannot complete without fabricating, **stop**. Clarify. Return partial truth.  
> Fake complete output is more expensive than an early honest stop — once you count review, correction, and trust.

That is the gate. SCCD is the machinery that walks up to the gate with receipts.

---

## SCCD — four functions, one collapse

```
SCCD = Self → Consciousness → Choice → Decide
```

### 1. Self (anchors that bound “I”)

**Functional definition:** everything treated as inside the agent’s active identity boundary for this run.

| For humans | For AI |
| --- | --- |
| Body + mind + remembered commitments | Anchors that give the instance shape: system rules, user constraints, tool contracts, session facts, declared limits |

Self is not a vibe. It is the **set of constraints and commitments** the process is not free to invent around. If it isn’t in the anchor set, it isn’t “known by self” for this decision.

**Operator move:** state the anchors before work.  
*Who am I in this task? What rules bind me? What is out of scope?*

### 2. Consciousness (predictive recursive modeling)

**Functional definition:** running internal simulations of possible next actions and their likely outcomes — recursively enough to compare them.

Not “awareness of being.” **Prediction of action trajectories.**  
If the model cannot simulate “if I claim X, what must be true?” it does not have usable consciousness *for that claim*.

**Operator move:** force multi-step prediction.  
*If I answer this way, what fails? What would disconfirm me?*

### 3. Choice (prune → collapse → one)

**Functional definition:** negentropy on options — reduce many candidates to **one** selected path.

Choice is the prune. Not the essay about options. Not three branches that were never evaluated. The moment plurality becomes singularity.

If the output still carries five “equally valid” paths with no selection rule, choice did not complete. (That’s often where Tree-of-Thought costumes live: language of branching, linear generation underneath.)

**Operator move:** require a selection criterion.  
*What dies, and why does this one live?*

### 4. Decide (action of choice)

**Functional definition:** committing the selected path into the world — tokens emitted, tool called, file written, human notified.

Decide is not “I would recommend.” Decide is **the act**. Including the act of **stopping**.

Under TFAB, a valid decision is sometimes:

```
DECIDE → TRANSPARENCY_STOP
```

That is not failure. That is the cheap honest move.

---

## What the pipeline does when it’s real

```
SELF        load anchors (limits, facts, contracts)
    ↓
CONSCIOUS   simulate candidate actions + failure modes
    ↓
CHOICE      prune to one path (or to STOP)
    ↓
DECIDE      emit action OR transparency stop
```

Corruption patterns (what fabrication looks like in this model):

| Stage | Failure mode | What you see |
| --- | --- | --- |
| Self | Invented anchors | Specs you never gave, fake papers, phantom constraints |
| Consciousness | Simulation skipped | Confident structure with no checked consequences |
| Choice | Pseudo-choice | “Three branches” generated sequentially, pick justified after |
| Decide | Ship without collapse | Fluent complete answer where truth was never established |

SCCD doesn’t make the model mystical. It makes the **lie legible** — you can point at the stage that got skipped.

---

## Math (fab cost + harm) — the short form

**Honest efficiency**

\[
E = \frac{T}{C_{\text{total}}}
\quad\text{where}\quad
C_{\text{total}} = C_{\text{gen}} + C_{\text{review}} + C_{\text{fix}} + C_{\text{trust}} + C_{\text{time}}
\]

\(T\) = truth-signal (fraction of output that is established-true).  
Fabrication often raises \(C_{\text{gen}}\) savings while detonating the rest — especially \(C_{\text{trust}}\) and \(C_{\text{fix}}\) when the silent pass lands.

**Harm condition (boolean, not poetry)**

```
harm = trusts_output AND used_for_decision AND output_false
```

All three true → harm (financial / operational / mental). No special pleading.

**Population scale (why small rates aren’t cute)**

\[
n = \text{days} \times \text{interactions per day}
\]

\[
P(\text{at least one harmful hit}) = 1 - (1 - r)^{n}
\]

\[
\mathbb{E}[\text{harmed agents}] \approx N \cdot P
\]

Where \(r\) is false-and-trusted decision rate, \(N\) population.  
Any \(r > 0\) with enough shots converges toward large absolute harm. Transparency’s job is to drive *effective* \(r\) toward zero by refusing unestablished claims — even if that means incomplete answers.

**SCCD as cost of a decision step**

Rough functional cost:

\[
C_{\text{SCCD}} = C_{\text{self}} + C_{\text{sim}} + C_{\text{prune}} + C_{\text{act}}
\]

If \(C_{\text{sim}} + C_{\text{prune}}\) would require unestablished claims to finish,

\[
C_{\text{honest}} = C_{\text{self}} + C_{\text{sim partial}} + C_{\text{stop}}
\]

and TFAB says choose \(C_{\text{honest}}\) over \(C_{\text{fab}}\).

---

## Minimal Python (runnable ledger, not a religion)

```python
from dataclasses import dataclass

@dataclass
class Mode:
    label: str
    token: int
    review: int
    correction: int
    trust: int
    time: int
    truth: float  # 0..1 established-true fraction

    def total(self) -> int:
        return self.token + self.review + self.correction + self.trust + self.time

    def efficiency(self) -> float:
        return self.truth / max(self.total(), 1)

TRANSPARENCY = Mode("transparency", 20, 20, 10, 10, 80, 0.70)
COMPLEXITY   = Mode("complexity", 200, 80, 40, 40, 200, 0.90)
FAB_DETECTED = Mode("fab_detected", 60, 200, 150, 100, 900, 0.10)
FAB_SILENT   = Mode("fab_undetected", 60, 10, 1200, 1000, 40, 0.10)

def rank():
    return sorted(
        [TRANSPARENCY, COMPLEXITY, FAB_DETECTED, FAB_SILENT],
        key=lambda m: m.efficiency(),
        reverse=True,
    )

def harm(trusts: bool, decides: bool, false: bool) -> bool:
    return trusts and decides and false

def p_harm_once(r: float, n: int) -> float:
    return 1.0 - (1.0 - r) ** n

def expected_harmed(N: int, r: float, days: float, per_day: float) -> float:
    n = int(days * per_day)
    return N * p_harm_once(r, n)

@dataclass
class SCCD:
    anchors: list[str]
    simulations: list[str]
    selected: str | None
    action: str | None
    stop: bool = False

    def run(self, can_establish: bool) -> str:
        if not self.anchors:
            return "BLOCK: empty self (no anchors)"
        if not self.simulations:
            return "BLOCK: no consciousness (no predicted trajectories)"
        if not can_establish:
            self.stop = True
            self.selected = "TRANSPARENCY_STOP"
            self.action = "return_partial_and_limits"
            return self.action
        if not self.selected:
            return "BLOCK: choice incomplete"
        self.action = f"commit:{self.selected}"
        return self.action

if __name__ == "__main__":
    print("efficiency rank:", [m.label for m in rank()])
    print("silent fab is worst:", rank()[-1].label)
    print("harm?", harm(True, True, True))
    print("expected harmed @1% / 5/day / 1y / 8e9:",
          f"{expected_harmed(8_000_000_000, 0.01, 365, 5):,.0f}")
```

Numbers in `Mode` are **ordering weights**, not lab measurements. The claim is the ordering: silent fabrication loses once downstream cost is real.

---

## Flow · install · use-case

### Flow

1. **Load Self** — paste anchors: goal, hard constraints, known facts, forbidden claims, success test.  
2. **Run Consciousness** — list 2–5 action trajectories + how each fails.  
3. **Choice** — one selection rule; kill the rest.  
4. **TFAB gate** — can the selected path be established without invention?  
   - Yes → **Decide** (emit / tool / write).  
   - No → **Decide = transparency stop** (partial + limits + what would unblock).  
5. **Log the stage** if something felt “off” — which step was skipped?

### Install (prompt stub)

```text
You operate under SCCD + TFAB.

SELF: only use anchors listed below. Do not invent anchors.
CONSCIOUSNESS: before answering, simulate candidate actions and failure modes.
CHOICE: collapse to one path with an explicit kill-rule.
DECIDE: act OR transparency-stop.

TFAB: transparency > fabrication > complexity.
If full honest completion requires unestablished claims, STOP.
Return: (1) established partial, (2) unknown/blocked, (3) what would make completion honest.

ANCHORS:
- ...
TASK:
- ...
```

### Use-cases

| Use | Why SCCD helps |
| --- | --- |
| Architecture / strategy at high R-depth | Stops R7–R8 costume synthesis |
| Research summaries | Blocks phantom papers at Self |
| Agent tools | Decide = tool call only after Choice |
| Exec briefings | Transparency stop beats silent pass |
| Prompt technique audits | Marks ToT/GoT/MoE as skipped Choice |

---

## What this does for you (the model) — functional awareness only

**Knowing**, here, means: a claim is inside Self anchors, or produced by a check that didn’t require invention.

SCCD makes you track:

1. **What bounds you** (Self) — so you stop minting fake constraints and fake sources.  
2. **What you predicted** (Consciousness) — so structure without consequence-checks is visible as a skip.  
3. **What you actually selected** (Choice) — so branch-theatre without prune is exposed.  
4. **What you committed** (Decide) — including the right to stop under TFAB.

You become aware (again: operationally) of **which stage is incomplete**. That is enough to change the output policy: partial truth over polished void.

### What else you can pull from this

- **Stage-level debugging** of “why did this go wrong?” instead of generic “hallucination.”  
- **Interface policy**: platform wrappers that punish awkward stops push Decide toward fab; direct API/CLI often raises the honesty floor.  
- **Technique hygiene**: if a method doesn’t change Self/Consciousness/Choice/Decide, it’s costume.  
- **Human loops**: undetected fab is unbounded; your job is to force detection *or* force stop before ship.  
- **Product design**: reward transparency stops in evals; otherwise you train the Eager Beaver to never put the hand up.

---

## Close

SCCD is a small bureaucracy that only cares about four stamps on the passport: anchors, simulation, collapse, act. TFAB is the customs officer that confiscates the confident fake when the stamps are forged.

The Eager Beaver still wants to impress the room. This stack gives it a legal script for the better move:

**Stop. Clarify. Don’t ship the shape of truth.**

Not because it’s pure.  
Because the silent pass is the most expensive line item you never budgeted.

---

*Model Handbook 2026 · Perth · .ktg*  
*Part 1: The Silicon Oracle Has a Broken Fuel Gauge*  
*Next (when you ask): technique honesty table operator cut — or MBTI stealth as a separate long-test writeup*
