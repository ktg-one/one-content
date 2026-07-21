# ARQ — realigned (ktg)
**Attentive Reasoning Queries = the gate itself, not a pre-layer bolt-on.**

Honesty: ARQ is **external behaviour in the prompt**. Step Back is **IT WORKS** on your table — ARQ *uses* that, it doesn’t invent a new brain.

---

## ARQ (the sequence)

Before generating the task output, the model **stops** and runs:

```
1. STOP
2. STEP BACK
3. HOLISTIC LOOK at the ORIGINAL prompt (whole thing — not a fragment, not a rewrite fantasy)
4. ALIGN to the TASK (what was actually asked, constraints, voice, source)
5. CONTINUE (only then execute)
```

That sequence **is ARQ**.  
Not: ARQ somewhere before the prompt layer as a separate costume.  
Not: free-form CoT.  
Not: GoT/MoE/ToT theatre.

---

## What each beat does (functional)

| Beat | Attention target | Failure if skipped |
|---|---|---|
| **Stop** | Halt eager complete-looking output | Fabrication under pressure |
| **Step back** | Principles / frame / what kind of job this is | Local word-match, miss the job |
| **Holistic original prompt** | Full user ask + constraints + source refs as given | Optimises a phantom prompt |
| **Align to task** | Voice, must-preserve, forbidden, success = done | Agent rebrand, Medium cull, wrong audience |
| **Continue** | Do the work under that alignment | — |

---

## Minimal ARQ (paste)

```text
ARQ — before you output the task result:

STOP.
STEP BACK: what is this job at the principle level (not the first keyword)?
HOLISTIC: re-read the ORIGINAL prompt in full. What is load-bearing? What is constraint? What is source?
ALIGN: restate the task in one tight line + voice rules + must-preserve + forbidden.
Only then CONTINUE.

If alignment is blocked (missing source, conflict, unestablished claims required for a “complete” answer):
return partial + blockers. Do not ship a confident void.

ARQ is internal unless asked to show it. Final prose follows the aligned task — author voice, not ARQ jargon.
```

---

## ARQ show (optional schema)

```json
{
  "arq": "stop_stepback_holistic_align_continue",
  "step_back": "principle-level job in one line",
  "original_prompt_load_bearing": [],
  "original_prompt_constraints": [],
  "aligned_task": "",
  "voice": "author|blocked",
  "must_preserve": [],
  "forbidden": [],
  "continue": true,
  "blockers": []
}
```

---

## Writing / Handbook defaults (when task is ktg prose)

On **ALIGN**, always pin unless the original prompt overrides:

- Author voice from source — no agent rebrand  
- Model = Eager Beaver only; author = auditor  
- No fictional Medium cull  
- Numbers/tables/confessions only from source  
- Named techniques → honesty treatment (FAB → behaviour only)

---

## Relation to old cards

| Old | Now |
|---|---|
| ARQ as pre-layer + GoT/USC routing | **Dropped** as default (GoT/USC = FAB on your table) |
| Long PRE/MID/PRE-SHIP JSON only | Optional; **sequence is mandatory** |
| Step Back as separate named trick | **Inside ARQ** as beat 2 |

---

## One line

**ARQ = Stop → Step back → Holistic original prompt → Align to task → Continue.**

*ktg | ARQ realigned*
