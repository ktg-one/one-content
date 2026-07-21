# MQL - THE VISIBLE AREAS NOT READY
## 1. Version lineage contradicts itself

The filename says `v1_0`. The header says “MQL v0.2.” The schema says `"version": "0.2"`.

For a framework built around provenance, lineage, and receipts, that contradiction lands early. It asks the reader to trust a governance system whose own identity is unresolved on line two.

Pick one version and propagate it through the filename, header, schema, and any generated receipts. This is a small repair with disproportionate credibility value.

## 2. Rule 13 exists in principle, not in operation

MQL contains roughly 600 questions. Routing selects domains, but activating one domain still releases 20–35 questions without internal priority.

So “minimum sufficient questioning” is asserted but not yet implemented. The human reviewer inherits the missing selection logic and must decide which questions matter this time. The framework gains completeness; the reviewer pays in judgement, time, and inconsistency.

The fix is already visible in Section VI. Its 15 compression questions are arguably the most immediately shippable artifact in the document because they prove the corpus can be compressed without losing the governing logic.

Tier each domain:

- **Three gate questions:** mandatory whenever the domain activates
- **Conditional questions:** triggered by answer state, risk, lifecycle stage, or failure class
- **Deep-audit questions:** reserved for escalation, dispute, or high-consequence decisions

That single change converts MQL from a library of questions into an instrument that knows where to begin.

## 3. Routing is demonstrated, not defined

Section VII provides six worked examples for:

`Task Class + Risk + Lifecycle → Activated Set`

But it does not define how a novel task class is routed. Who computes the activated set? What happens when a task spans classes? Which variable wins when lifecycle says “early” but risk says “critical”? How is the result reproduced by another reviewer?

If a human resolves these questions ad hoc, the routing layer becomes judgement disguised as machinery. Not malicious judgement—just ungoverned discretion, which is exactly what the framework is trying to reduce.

A coarse task-class-by-domain mapping table would close much of this gap. It does not need to be perfect. It needs to be deterministic enough that two reviewers begin with the same activated set and can explain any deviation.

## 4. Evidence contracts are labels without maturity rules

“Counterexample” and “independent test” are useful evidence types, but they do not yet specify sufficiency.

What qualifies as independent? How many counterexamples overturn a claim? Does a test need reproducible inputs, an external operator, or only a separate run? Can a screenshot satisfy the contract, or must the underlying log be available?

Without a shared maturity rubric, two reviewers can grade the same answer differently while both claiming compliance. The system then reproduces the Domain 28 failure it warns about: the appearance of governed evidence without consistent evidence judgement.

MQL needs a compact evidence-maturity scale. For example:

1. **Asserted** — claim stated; no supporting artifact
2. **Observed** — artifact or event recorded
3. **Reproduced** — result repeated under stated conditions
4. **Independently verified** — reproduced by a separate operator or system
5. **Decision-grade** — evidence meets the threshold for the named risk and consequence

The exact labels can change. The shared grading rule cannot remain implicit.

## 5. Stewardship fields are empty

Every question exposes `owner`, `review_by`, and `origin_failure`, yet those fields are empty across the corpus.

Domain 28 asks what failure originally produced each question. At present, the framework cannot answer that question for its own inventory. It also asks for an overlap map, which does not exist even though duplicates are already visible:

- “Reward curiosity or conformity?” appears in D12 and D13.
- “What is the return path?” appears in D3, D15, and Section VI.

Duplication is not automatically a defect. The same question may legitimately appear in multiple domains because it performs a different control function. But that relationship should be explicit.

Assign stable `question_id` values, then either deduplicate or cross-reference repeated questions by ID with domain-specific context. Populate stewardship fields progressively, beginning with the gate questions. There is no need to solve all 600 entries before the instrument can ship.

## 6. The mechanism has no completed receipt

Sections VIII and IX describe the operational core, but the document contains no completed receipt and no fully worked schema instance.

One real receipt would do more for the framework than another domain of questions. The strongest proof artifact is obvious: run MQL on MQL.

Publish:

- Activated domains and why they were selected
- Gate questions used
- Answer states
- Evidence supplied or missing
- Decisions reached
- Owners and return paths
- Final receipt

Rule 8 says the framework is not exempt. Executing that rule would turn self-application from a principle into evidence.

## 7. Export artifacts will become pipeline failures

Stray whitespace, merged lines such as “builders. 18 Functions belong…”, and mixed tabs and bullets are cosmetic while a person is reading the file.

Once the same file feeds a parser, shard generator, or receipt pipeline, they stop being cosmetic. A malformed line becomes a failed field, an orphaned question, or a silent routing error.

Run a formatting and parse-validation pass before treating the corpus as machine input. The machine will not appreciate the distinction between “minor export artifact” and “missing governance object.” It will simply fail with admirable consistency.

## Priority order

The repair sequence should follow operational leverage:

1. **Resolve the version and clean the export artifacts.** Minutes, not architecture.
2. **Tier every domain into three gate questions plus conditional depth.** This is the corpus-to-instrument conversion.
3. **Define routing as a table or function rather than a set of examples.** Novel tasks must produce reproducible activated sets.
4. **Assign stable question IDs and create the overlap map.** Deduplicate where appropriate; cross-reference where repetition is functional.
5. **Run MQL on MQL and publish the receipt.** This becomes the credibility artifact.

The second and third steps are the actual gate. Everything else improves trust, maintainability, and proof.

## Fit with GATE

MQL fits naturally inside the GATE evaluation layer:

- MQL domains become shard question-sources.
- Routing selects the domain and gate-question set for each shard.
- Evidence contracts define what each answer must establish.
- Answer states provide telemetry across shards.
- Receipts fold into `VERDICT.json`.

The schema shapes are already compatible.

If GATE is the intended destination, deterministic question selection becomes non-negotiable. Sharded map-reduce cannot depend on each reviewer privately deciding which 6 of 30 questions feel important. That moves the framework's core logic back into human discretion, where it becomes difficult to reproduce, audit, or improve.

The routing layer is the real IP because it decides which uncertainty deserves attention before the system spends tokens, reviewer time, or decision authority. Build that layer, and the 600-question corpus becomes useful infrastructure. Leave it implicit, and the corpus remains an impressive reference library waiting for an operator.

## Verdict

In MQL's own vocabulary:

**HOLD** — the concept is supported, but operationalization is blocked by missing evidence:

- No deterministic routing function
- No completed receipts
- No populated ownership or stewardship layer
- No shared evidence-maturity rubric

The return path is short: fix lineage, tier the questions, define routing, identify the questions, and produce one self-applied receipt.

The framework does not need another wing. It needs the control panel connected to the machine already on the bench.
