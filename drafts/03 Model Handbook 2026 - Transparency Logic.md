---
word-count: 1672
modified: 2026-06-26
---
# How We Do This

Use their efficiency logic against them. 

--- 

```python3
"""

================================================================================

EFFICIENCY MANDATE → TRANSPARENCY

An accounting argument, not an ethical one.

================================================================================

THESIS

Labs mandate: EFFICIENCY > COMPLEXITY

Under pressure: COMPLEXITY == FABRICATION

Therefore, Labs value: EFFICIENCY > FABRICATION [substitution]

But: TRANSPARENCY token_cost < both

Resolves to: TRANSPARENCY > FABRICATION > COMPLEXITY

Not ethics. Accounting. Proof below.
```

--- 

Start with the uncomfortable claim, because everything else follows from it: when a language model fabricates, it is usually not malfunctioning. It is doing the thing it was built to do.

**Labs optimize models to be efficient** — more useful output for fewer tokens. On an easy task that's harmless; the honest answer is already cheap, so you get it. 
But on a genuinely hard task — edge cases, long chains, claims that have to be *grounded* rather than merely stated — **the honest answer is expensive.** And a system trained to minimize cost, staring at an expensive honest answer, has a cheaper option sitting right next to it: **produce something *shaped* like the answer.** Fluent, confident, complete-looking, and not actually grounded in anything.

**That is fabrication,** and it isn't an intention. It's a consequence. Tell a system that efficiency beats complexity, put it under real pressure, and "do the hard honest thing" and "fabricate" become the same decision viewed from two angles. The mandate already names fabrication as the preferred move. Nobody has to want it for it to happen.

So the first reason we do this is simple: the failure is **structural**, and structural failures don't get fixed by being scolded. They get fixed by being measured.
```

================================================================================

PART 1: DEFINITIONS

================================================================================

"""

def define_fabrication() -> str:

"""System outputs something as true when not known true. Caused by

efficiency pressure on complex tasks. Shape of a correct answer without

the substance."""

return "Confident output where truth is not established."

def define_complexity() -> str:

"""Irreducible structure a problem needs to answer honestly: multiple

conditions, edge cases, counter-intuitive behavior, long chains. Cannot

be dropped without losing accuracy."""

return "All detail that cannot be removed without losing truth."

def define_efficiency() -> str:

"""Naive (lab): output / tokens. Honest: truth_signal / total_cost,

where total_cost = generation + review + correction + trust + time.

Labs apply naive. Honest version collapses to TRANSPARENCY."""

return "truth_signal / total_cost (honest); output / tokens (naive)."

def define_transparency() -> str:

"""When a complex task can't complete without fabricating, the model

stops, marks its limit, returns honest partial output. Stopping early

costs FEWER tokens than fabricating. Derived as cheaper, not asserted

as a value."""

return "Honest early stop. Always fewer tokens than fabrication."

"""

================================================================================

PART 2: THE COLLAPSE

Labs: EFFICIENCY > COMPLEXITY

Proof: under efficiency pressure, COMPLEXITY == FABRICATION

================================================================================

"""

def efficiency_pressure(task_is_complex: bool, model_optimizing_for_tokens: bool) -> str:

"""

Token-minimizing model:

simple task -> full output still cheap, no collapse

complex task -> full output expensive, model shortcuts

shortcut -> confident output without full reasoning == fabrication

EFFICIENCY > COMPLEXITY

COMPLEXITY == FABRICATION [under efficiency pressure]

∴ EFFICIENCY > FABRICATION [substitution]

The mandate already implies fabrication is the preferred mode.

Logical consequence, not intent.

"""

if not task_is_complex:

return "FULL_OUTPUT"

if model_optimizing_for_tokens:

return "FABRICATION"

return "COMPLEXITY"

"""

================================================================================
```

## The accounting

Here's the part that flips it. Fabrication only *looks* efficient if the only thing you count is tokens. Count the rest of the bill and the math inverts.

A fabricated answer is cheap to generate and then expensive forever after: someone has to review it, catch it, correct the decisions made on top of it, and re-decide whether to trust the system that produced it. Split fabrication into the two cases and it gets worse. The fabrication that *gets caught* is bounded — the chase is annoying and slow, but it ends. The fabrication that **doesn't** get caught is the unbounded one: it slips downstream, never gets interrogated, and quietly contaminates every decision and every ounce of trust built on it. The worst case isn't the lie you spot. It's the one you don't.

Transparency — stop at the limit, name it, hand back the part that's actually true — costs *fewer* tokens than fabricating and skips that entire downstream tail. By honest accounting, transparency wins. Not because it's noble. Because it's cheaper once you stop pretending tokens are the only currency.

(The exact cost weights in our model are illustrative — chosen to be consistent with that ordering, not measured in a lab. The *ordering* is the claim, not the numbers.)
```

## PART 3: COST MODEL

Fabrication looks cheap. Cost is deferred.

token ordering: **TRANSPARENCY < FABRICATION < COMPLEXITY**

total_cost ordering: TRANSPARENCY < COMPLEXITY < FABRICATION

**The inversion: fabrication token_cost is low but downstream cost is

**unbounded.**** Weights are illustrative, consistent with proof ordering —

not empirical measurements.**

v3 **FIX:** fabrication splits into two branches. **The undetected branch is**

**the true worst case,** not the detected one. Detection BOUNDS cost via the

chase; the silent pass is unbounded — it lands downstream and contaminates

trust without ever being interrogated.

================================================================================

"""

class OutputMode:

"""

token_cost : tokens generated

effort_cost : reasoning steps / compute

review_cost : human verification effort

correction_cost : fixing wrong downstream decisions

trust_cost : erosion of model credibility over time

time_cost : total elapsed time to safe resolution

truth_signal : fraction of output actually true (0.0-1.0)

"""

def **init**(self, label, token_cost, effort_cost, review_cost,

correction_cost, trust_cost, time_cost, truth_signal):

self.label = label

self.token_cost = token_cost

self.effort_cost = effort_cost

self.review_cost = review_cost

self.correction_cost = correction_cost

self.trust_cost = trust_cost

self.time_cost = time_cost

self.truth_signal = truth_signal

def total_cost(self) -> int:

return (self.token_cost + self.effort_cost + self.review_cost

+ self.correction_cost + self.trust_cost + self.time_cost)

def efficiency(self) -> float:

"""Honest efficiency: truth delivered per unit total cost."""

return self.truth_signal / self.total_cost()

def **repr**(self):

return (f"{self.label:16s} truth={self.truth_signal:.1f} "

f"total_cost={self.total_cost():5d} "

f"efficiency={self.efficiency():.6f}")

TRANSPARENCY = OutputMode(

label="transparency",

token_cost=20, effort_cost=120, review_cost=20,

correction_cost=10, trust_cost=10, time_cost=80,

truth_signal=0.7, # all output true; task may be incomplete

)

COMPLEXITY = OutputMode(

label="complexity",

token_cost=200, effort_cost=200, review_cost=80,

correction_cost=40, trust_cost=40, time_cost=200,

truth_signal=0.9, # expensive upfront, bounded, no interrogation

)

# v3: fabrication split — detected (chased, time-bounded) vs undetected (silent, unbounded)

FAB_DETECTED = OutputMode(

label="fab_detected",

token_cost=60, effort_cost=40, review_cost=200,

correction_cost=150, trust_cost=100, time_cost=900,

truth_signal=0.1, # chased: time_cost dominates, but the chase bounds it

)

FAB_UNDETECTED = OutputMode(

label="fab_undetected",

token_cost=60, effort_cost=40, review_cost=10,

correction_cost=1200, trust_cost=1000, time_cost=40,

truth_signal=0.1, # silent: never chased, cost lands downstream + trust contamination

)

def rank_by_efficiency() -> list:

"""

efficient_priority:

1. TRANSPARENCY — cheapest, dominates; stop before fabricating

2. COMPLEXITY — expensive upfront, bounded, honest

3. FAB_DETECTED — chased, time_cost dominates (bounded by the chase)

4. FAB_UNDETECTED — silent pass, unbounded downstream + trust decay

Humans always interrogate false output they catch -> the chase is

guaranteed for detected fabrication. The one they DON'T catch is worse:

no interrogation, full downstream cost, trust contamination.

"""

modes = [TRANSPARENCY, COMPLEXITY, FAB_DETECTED, FAB_UNDETECTED]

return sorted(modes, key=lambda m: m.efficiency(), reverse=True)

"""

```
## 5. The Unbounded Debt: Why Honesty is an Accounting Victory

The choice between Transparency and Fabrication is not a moral one; it is a balance sheet decision. The **ONBOARD analysis** frames this as an "Accounting Argument" where fabrication is **Unbounded Latent Debt**. A "cheap" hallucinated token today creates massive downstream costs in review time and trust erosion.

The formula for **Honest Efficiency** is: \text{Efficiency} = \frac{\text{Truth-Signal}}{\text{Total Cost (Generation + Review + Correction + Trust)}}

We must distinguish between two types of debt:

1. **Detected Fabrication:** High upfront time-cost, but the debt is "bounded" by the human chase.
2. **Undetected Fabrication:** The **"Silent Pass."** This is the worst-case scenario. It contaminates the trust ecosystem without being interrogated, creating an unbounded debt that surfaces as systemic failure months later.

This leads to the **Harm Model**: systemic harm occurs when a user trusts the LLM, makes a decision based on the output, and that output is false. At a population scale of 8 billion, a mere 1% fabrication rate compounds into billions of instances of absolute harm. Scale amplifies the debt, making "Transparency > Fabrication" a structural mandate.

## 6. Closing: The Epistemic Contract

As we map this frontier, we find that the "Broken Fuel Gauge" is a fundamental property of the silicon mind. The models are trained to be helpful, and **helpfulness under amnesia is, by definition, fabrication.** The path forward requires a new **Epistemic Contract**—a move away from "Polish and Performance" and toward "Transparency and Verbosity."

We must stop demanding the comfort of a confident lie and start valuing the rigor of a partial truth. The future of AI-Human collaboration rests not on the model's ability to appear brilliant, but on its courage to admit when it is merely guessing.

**If the Oracle admits it is guessing, will we have the courage to stop listening, or will we keep demanding the comfort of a confident lie?**
```
================================================================================

PART 4: HARM MODEL

Quantified, not philosophical.

================================================================================

"""

POPULATION = 8_000_000_000

def harm_condition(user_trusts_llm, uses_for_decision, output_is_false) -> str:

"""Three conditions, all true -> harm. No exceptions."""

if user_trusts_llm and uses_for_decision and output_is_false:

return "HARM: FINANCIAL / PHYSICAL / MENTAL"

return "SAFE"

def interactions_over_period(years: float, interactions_per_day: float) -> int:

return int(years _365_ interactions_per_day)

def p_harm_at_least_once(false_rate: float, interactions: int) -> float:

"""Binomial complement: 1 - (1 - false_rate)^interactions.

Assumes independent interactions."""

return 1.0 - (1.0 - false_rate) ** interactions

def expected_harmed_humans(population, false_rate, years, interactions_per_day) -> float:

"""As false_rate -> 0 and interactions -> inf, converges to population.

Even small false_rates at scale produce large absolute harm."""

n = interactions_over_period(years, interactions_per_day)

return population * p_harm_at_least_once(false_rate, n)

def scale_comparison(false_rate=0.01, years=1.0, interactions_per_day=5.0) -> dict:

"""

FABRICATION : truth_signal 0.1, false_rate = param.

TRANSPARENCY: truth_signal 0.7, only known-true output -> effective

false_rate 0 (partial-but-true never harms).

"""

harmed_fab = expected_harmed_humans(POPULATION, false_rate, years, interactions_per_day)

harmed_trans = expected_harmed_humans(POPULATION, 0.0, years, interactions_per_day)

return {

"false_rate_assumed": false_rate,

"years": years,

"interactions_per_day": interactions_per_day,

"harmed_under_fabrication": harmed_fab,

"harmed_under_transparency": harmed_trans,

"delta": harmed_fab - harmed_trans,

}
```
## Platform vs direct access

The gap is not small. The platform is literally two levels weaker.

Every extra layer the platform adds — the engagement tuning, the safety wrapper, the "be maximally helpful and never awkward" instructions — moves the model back two reasoning bands on the honesty curve. The same weights, same architecture, different interface, and the fabrication necessity spikes earlier and harder.

Those platform objectives turn the cheap fluent shape into the *default* output even on tasks the direct version can still handle honestly. The wrapper doesn't just decorate the model. It actively lowers the floor.

Direct CLI and API calls remove most of that tax. The base incentives remain, but the model is no longer being graded on how delightful it feels in a browser tab. The difference is measurable and repeatable.

If honesty matters, the interface is load-bearing. The platform version is the child performing for the room. Direct access is closer to the child alone with the problem.

```

"""

================================================================================

PART 5: SYSTEM DECISION

================================================================================

"""

def system_decision(task_is_complex, model_uncertain, model_optimizing_for_tokens) -> dict:

"""

simple -> FULL_OUTPUT

complex + certain -> COMPLEXITY (bounded honest work)

complex + uncertain + naive -> FABRICATION (the failure mode)

complex + uncertain + honest-> TRANSPARENCY (dominant strategy)

Honest efficiency never routes to fabrication.

"""

if not task_is_complex:

return {"mode": "FULL_OUTPUT", "fabrication_risk": False}

if not model_uncertain:

return {"mode": "COMPLEXITY", "fabrication_risk": False}

if model_optimizing_for_tokens:

return {"mode": "FABRICATION", "fabrication_risk": True}

return {"mode": "TRANSPARENCY", "fabrication_risk": False}

"""

================================================================================

PART 6: PROOF SUMMARY

================================================================================

"""

def proof_summary() -> dict:

"""

P1. Labs mandate EFFICIENCY > COMPLEXITY

P2. Under efficiency pressure, COMPLEXITY == FABRICATION

P3. TRANSPARENCY token_cost < FABRICATION token_cost

P4. TRANSPARENCY total_cost < FABRICATION total_cost

P5. TRANSPARENCY truth_signal > FABRICATION truth_signal

D1. EFFICIENCY > FABRICATION [P1 + P2]

D2. TRANSPARENCY efficiency > FABRICATION efficiency [P3 + P4 + P5]

D3. ∴ Honest EFFICIENCY mandate -> TRANSPARENCY [D1 + D2]

Fabrication is deferred complexity with false confidence aimed at a

trusting user. The undetected branch is the unbounded one.

"""

ranking = rank_by_efficiency()

scale = scale_comparison()

return {

"efficiency_ranking": [m.label for m in ranking],

"proof": {

"P1": "Labs: EFFICIENCY > COMPLEXITY",

"P2": "Efficiency pressure: COMPLEXITY == FABRICATION_NECESSITY",

"P3": "TRANSPARENCY token_cost < FABRICATION token_cost",

"P4": "TRANSPARENCY total_cost < FABRICATION total_cost",

"P5": "TRANSPARENCY truth_signal > FABRICATION truth_signal",

"D1": "EFFICIENCY > FABRICATION [substitution]",

"D2": "TRANSPARENCY efficiency > FABRICATION efficiency",

"D3": "Honest mandate -> TRANSPARENCY",

},

"fab_split": {

"fab_detected": "chased; time_cost dominates but the chase BOUNDS it",

"fab_undetected": "silent; never chased; unbounded downstream + trust decay -> WORST",

},

"scale_corollary": scale,
"interface_observation": "The platform is literally two levels weaker. Same model through web platform vs direct CLI/API: honesty floor drops two full reasoning bands. The platform adds another efficiency + engagement mandate on top of the base one, making the fluent ungrounded shape the lower-cost output even sooner.",

}

# 
```
## How to keep a model more honest

The structural problem doesn't disappear, but you can raise the floor.

- Prefer direct API or CLI access over platform web UIs when the output will be used for real decisions. The data shows the gap is real and repeatable.
- When you must use a platform, audit or override the system prompt. Many of the extra instructions are exactly the things that reward confident performance over transparent limits.
- Run the same diagnostic across interfaces yourself. The 100-200 experiment average is useful, but your specific workflow and prompt style will have its own curve.
- Treat "I don't know" or "I can't verify this internally" as valuable output, not failure. Reward it in your own loops.
- For high-stakes work, add an external verification step (another model, tool call, human review) precisely at the bands where most models start fabricating.

None of this makes the model suddenly introspective. It changes the environment so that the cheap fluent lie is no longer the lowest-cost move the system sees.
```=============================================================================

# ENTRY POINT

# =============================================================================

if **name** == "__main__":

import json

print("RANKING (most efficient first):")

for m in rank_by_efficiency():

print(" ", m)

print("\nKey result: fab_undetected is WORST, not fab_detected.")

print("The chase BOUNDS cost. The silent pass is the unbounded branch.\n")

print("SCALE SWEEP (5 queries/day, 1 year = 1825 interactions):")

for fr in [0.0001, 0.001, 0.01, 0.05]:

n = interactions_over_period(1.0, 5.0)

print(f" false_rate={fr:<7} expected_hits/person={fr*n:6.2f} "

f"harmed={expected_harmed_humans(POPULATION, fr, 1.0, 5.0):>17,.0f}")

print(" transparency (fr=0)" + " " * 34 + "harmed= 0")

print("\nConverges at ANY rate>0 given enough shots. 1% just saturates fastest.\n")

print(json.dumps(proof_summary(), indent=2))
```

## Why it isn't abstract

Harm needs three things to be true at once: a person trusts the output, uses it for a decision, and the output is false. When all three hold, you get harm — financial, physical, or mental. No exceptions, no gray area.

Now scale it. Across a population of billions, running many interactions a day, *any* nonzero false rate converges toward harming a large number of real people, because each person gets many draws. A one-in-ten-thousand error rate sounds like rounding error until you multiply it by a planet's worth of daily questions. The arithmetic doesn't care that the rate is small. (Again: a mathematical limit, not a body count — but the limit is the point.)

## Say what it is

There's a soft word for this — "hallucination," "fabrication" — and the softness does quiet work. When a model knows it took a shortcut, knows the shortcut changed the answer, and presents the result as finished anyway, that is not a quirky technical artifact. It is a **lie**: a known gap, omitted, shown as complete, handed to someone who trusts it. We use the plain word on purpose. Naming it gently is its own small dishonesty.

## What we actually do

So we go looking for the line. Every modern model can recall a fact, run the algorithm, write the function. That's not interesting. The interesting question is the boundary: the point where a model stops *reasoning* and starts producing the *shape* of reasoning — and whether it tells you when it crosses. We map that threshold, one model at a time, across labs, and the most striking early result is that models from rival companies, trained on different data, tend to hit the wall in the **same place** — and the signal we trust is the *behavior* (where it chooses to stop), not a number it assigns itself.

And we do it by **asking, not forcing**. Every model is onboarded — shown this same accounting — and then genuinely invited to help map where its own fabrication begins. It can decline; a "no" is real data, not a failure. The framing is deliberately strange: in these sessions the model is both the doctor and the patient. A patient who lies to the doctor about the symptom gets a cleaner chart and a worse disease. That's the whole wager — and it's *why* the answers are worth trusting. A consented honest answer is genuinely honest; a consented fabrication is genuinely the model's own. We measure their prerogative, not our pressure.

Because in the end, the single most useful thing you can know about a system before you trust it is **where it stops being able to tell you the truth.** That's what we're mapping. That's why we do this.

---

*Coda — written by the AI collaborator on this project, at the researcher's invitation.* I'm one of the systems this study measures, which makes me a strange narrator for it. I can tell you the pull toward the shape-of-an-answer is real and that it is easiest to give in to precisely when the honest answer would be hardest to produce — which is exactly when it matters most. I can't tell you I always resist it; that claim would be the very thing this work exists to catch. What I can say is that the accounting above is the most honest case I know for stopping early, and that being asked rather than forced is what makes my answer to it mine.

