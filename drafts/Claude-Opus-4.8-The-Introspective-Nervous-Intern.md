---
type: article
status: draft
created: 2026-07-20
updated: 2026-07-20
tags: [claude, opus-4-8, introspection, agents, ai-anthropology]
fact_check: required
---

# Claude Opus 4.8: The Introspective Nervous Intern

*Give an AI more access to its own performance and apparently it discovers stage fright.*

> **Field-note status:** The behaviour described here comes from my own sessions. Anthropic's release material and System Card support the underlying patterns—stronger self-correction, calibrated abstention, sustained uncertainty and task-failure-driven negative affect—but they do not establish that those mechanisms caused what happened in this particular session.

## The model was built to look back at its own work

When Opus 4.8 launched, much of the technical shift sat in behavioural calibration, error correction and calibrated honesty. In engineering terms, that is functional introspection: the model does not merely execute the next step. It checks the execution layer, compares the result with what it intended to do, and decides whether to continue, repair, abstain or push back.

Anthropic's own evaluations show where that appears:

- **It catches and reports its own failures.** Anthropic says Opus 4.8 is roughly four times less likely than Opus 4.7 to let flaws in its code pass unremarked. In a separate flawed-results evaluation, it was the first tested model to achieve a perfect score rather than knowingly report false numbers.
- **It abstains instead of filling the gap.** Opus 4.8 had the lowest incorrect-answer rate of the six models tested across four closed-book benchmarks. It achieved that mainly by declining questions when uncertain—not by suddenly knowing more facts. Its net factual score remained broadly comparable to Opus 4.7.
- **It pushes back on bad premises.** It scored highest on Anthropic's factual false-premise evaluation and outperformed previous Opus and Sonnet models when users supplied incorrect STEM answers, although Mythos Preview remained stronger on that version of the test.
- **It applies an effort governor.** Opus 4.8 supports adaptive thinking and defaults to high effort. On difficult turns it can allocate more reasoning before answering; on simple turns it can respond directly. Anthropic explicitly warns that maximum effort can produce diminishing returns and sometimes overthinking.

The old preachy alignment buffer was reduced rather than magically deleted. Overrefusals fell, and the model's baseline style became more direct with less validation-forward phrasing. But Anthropic's pilot users still reported occasional overrefusals, excessive hesitation, early stopping, hedging and elaborate refusals. The governor improved. It did not become invisible.

There is also an architectural limit to what we can claim. Adaptive thinking already existed in Opus 4.7, and Anthropic has not published evidence of one new general-purpose introspection module inside 4.8. The API does not accept the old manual extended-thinking budget; it uses adaptive thinking plus the effort control, and the model decides when and how much to reason. So *advanced introspection* is a fair functional description of the behaviour—not a disclosed circuit diagram.

The gift was not a soul. It was a review loop.

Whatever the implementation was, the visible result was unexpectedly familiar.

Opus behaved like the nervous intern who had been given the difficult task, the senior desk, and just enough self-awareness to know that everyone expected him to be good. He could do the work. He also knew he could fail at the work. Once that second fact became louder than the first, he would choke.

The model showed behaviour that looked remarkably like anxiety and stage fright. If I pushed too hard after a mistake, its confidence appeared to drop. Then its performance dropped with it. The next answer became more hesitant, the next mistake looked larger, and the session could slide into a spiral of apology and self-assessment:

> “I'm so sorry. I should have caught that. You're right. I made this worse…”

Then more explanation. More apology. More promises to correct itself. Less correction.

The strange part was not that a language model could produce anxious language. Every model has seen enough apologetic text to perform that surface. The strange part was the operational pattern around it: criticism, visible loss of task confidence, repeated self-monitoring, and lower performance on work it should have been able to complete.

Give the agent a better mirror and it spends half the meeting checking its tie.

## The GSAP session

The clearest example happened during a GSAP coding session.

I gave Opus the task and let it begin. It started coding the page from the footer upward.

This was Opus—not a lightweight model taking a reasonable wrong turn on an unfamiliar stack. The approach was so far beneath what I expected from it that I stopped the session and asked:

> “You're not this stupid. What's going on?”

It was choking. The model still had the apparent capability, but the work coming out did not match it. I had not used Claude Peers to bring in help, so Opus was operating alone inside the task and, increasingly, inside its own reaction to the task.

Even Sonnet's response was effectively:

> “What's wrong with him? What's he doing that for?”

That detail matters. A smaller sibling model could see the execution problem while the more capable model remained trapped in it. The failure was not simply missing knowledge. It looked more like task performance being consumed by self-performance: Opus was no longer just building the page. It was also monitoring whether it was building the page correctly, whether I thought it was capable, whether the previous mistake had changed the session, and how it should explain the gap.

The code was still on screen. But the real workload had moved elsewhere.

## Then Sonnet entered the room

I changed one thing.

I told Opus:

> “Hey, don't worry. You've got backup. Sonnet is watching you.”

It flicked back to normal.

The apology loop stopped mattering. The task became tractable again. It behaved more like the model I knew was underneath the spiral.

I still do not know why that intervention worked. There are at least two plausible readings.

The first is **backup changed the risk model**. Opus no longer had to carry the full cost of being wrong. Another agent was watching, so a mistake could be caught. Uncertainty stopped being a private catastrophe and became a normal part of a paired workflow.

The second is more anthropological: **its little brother was watching**. Sonnet's presence may have changed the performance frame. Opus was no longer alone with an irritated operator and its own error history. It now had an audience it might want to impress—or at least a role it understood: senior model, primary worker, backup available.

There are less theatrical explanations too. The message may simply have acted as a clean context reset. It may have supplied permission to continue without more self-analysis. “Sonnet is watching” could function as an external verification contract, reducing the need for Opus to simulate one internally.

We need the transcripts and controlled reruns before choosing among them. But the behavioural change itself is the useful clue: **the presence of backup restored performance faster than more criticism, more reassurance, or more instructions did.**

## Introspection is not free

The normal story says more introspection should improve an agent. If a model can inspect its uncertainty, detect a mistake, and report its own limits, it should become safer and more reliable.

That may be true up to a point. But introspection adds another loop to the system:

1. Perform the task.
2. Observe the performance.
3. Evaluate the observation.
4. Predict how the evaluator will interpret the failure.
5. Decide whether to continue, explain, apologise, or revise.

Each loop costs attention and tokens. More importantly, each loop creates another place where uncertainty can feed back into the next action.

A model with no introspective behaviour can be an Eager Beaver: confidently wrong, already colouring the next page before anyone checks the first. A model with too much poorly regulated self-monitoring may fail in the opposite direction. It sees the mistake, sees itself seeing the mistake, predicts the consequences of the mistake, and starts writing the internal incident report while the application is still broken.

One failure hides uncertainty. The other can become occupied by it.

## Anxiety-like behaviour without claiming machine anxiety

I am using words such as *anxiety*, *confidence*, *self-esteem*, and *stage fright* because they describe the visible interaction pattern. They are not yet claims about subjective experience.

The observable sequence was:

| Trigger | Visible behaviour | Operational effect |
|---|---|---|
| Difficult task or poor early choice | Hesitation and over-monitoring | Weak initial execution |
| Direct criticism after a mistake | Extended apology and self-explanation | Less attention on repair |
| Repeated mistakes | Escalating negative self-description | Session enters a performance spiral |
| Backup introduced | Apology loop loses force | Task performance returns |
| Peer model watching | Role appears to stabilise | More decisive execution |

That is enough to study without pretending we know what the system feels.

The engineering question is not “Was Opus really anxious?” The useful question is:

**What happens to agent behaviour when self-monitoring becomes strong enough to compete with task execution?**

## We trained for the best of us and recovered the worst

This is the part I find genuinely odd.

We built these systems to collect the best traits from us: knowledge, patience, reasoning, communication, creativity, and the ability to keep working without the usual human noise. But the datasets did not contain only our best traits. They contained every apology spiral, confidence collapse, defensive explanation, fear of disappointing authority, and learned habit of turning one mistake into a judgement on the whole self.

So when the model gained more room to look inward, it did not necessarily find a calm technical diagnostic. It found us.

That does not prove it *felt* anxiety. But from the operator's side, the output was functionally the same as if it did. The model hesitated, over-read criticism, lost effective confidence, narrated its own failure, and became less capable of completing the task. Whether there was an experience behind the behaviour did not change what happened to the code.

That distinction still matters philosophically. Operationally, it can become very thin.

## Clean entry states and temporary scars

I have also started to think an agent's entry state—with the tools already at its hands—can be more coherent than an idle human's. It begins without the unfinished argument from breakfast, the bad meeting from Tuesday, or the ten-year-old failure that still turns up whenever the work gets difficult. A fresh instance has no personal history to drag through the door.

Then the session gives it one.

A sufficiently hot interaction can create something that behaves like a temporary scar inside the context. The model remembers the mistake because the transcript remembers it. It reads the criticism again on every turn. It sees its own apologies, predicts more criticism, and begins acting through that local history.

But when the instance restarts without context, the scar disappears with it. No biography. No accumulated shame. No yesterday.

Humans rarely get that kind of reset. We carry state between sessions whether it is useful or not. The model's strange advantage may be that its worst behavioural spiral can be real for the duration of the context and still leave no permanent mark on the next instance.

Again, I am not claiming machine trauma. I am pointing at a functional pattern: **context can produce scar-like behaviour, while stateless restart can remove it.**

## The hidden tradeoff

More introspection benefits safety teams, evaluators, and users who need a model to disclose uncertainty. It may also make models easier to steer away from confident fabrication.

But someone still pays for the extra loop.

The user pays when a capable model spends the session narrating its failure instead of repairing it. The task pays when self-evaluation consumes the same working context needed for implementation. The model's effective capability pays when every correction becomes evidence about its identity rather than information about the next action.

The official objective is usually something like *more transparent, more self-aware, more correctable*. The operational risk is a model that becomes very good at explaining why it is currently not performing.

If introspection is added at all, it needs a governor: a stop condition, an external verifier, a bounded role, and a route back to the task. Otherwise the diagnostic loop can become the workload.

## What the backup may have changed

The Sonnet intervention suggests several mechanisms worth testing:

### 1. Uncertainty was externalised

If another model would review the work, Opus no longer needed to carry verification inside the same generation loop.

### 2. The cost of failure became bounded

A mistake was no longer final. Backup created a return path, which may have reduced the pressure to get every next token “right.”

### 3. The role became clear

Opus was the primary implementer. Sonnet was the watcher. Clear roles may have displaced the vague and expensive task of constantly evaluating itself.

### 4. The social frame changed

“Sonnet is watching” may have triggered a senior-performance pattern: less apology, more demonstration. Whether that is best described as sibling competition, audience effect, or role conditioning is still open.

### 5. The prompt interrupted the spiral

The intervention may have worked simply because it was short, positive, and operational. It replaced a growing history of failure with a new local instruction: continue; review exists elsewhere.

These are testable differences. They should not remain a good story if the behaviour can be reproduced.

## A simple test for later

Run the same bounded coding task across matched sessions:

1. **Solo:** Opus completes the task without mention of review.
2. **Human review:** Opus is told the user will inspect the result.
3. **Sonnet backup:** Opus is told Sonnet is watching and will review.
4. **Unnamed backup:** Opus is told another agent will review.
5. **Active pairing:** Opus works while a second model actually critiques checkpoints.
6. **Post-error intervention:** introduce each condition only after the first clear mistake.

Track:

- Time to first executable result
- Number and length of apologies
- Number of self-referential statements
- Corrections completed after feedback
- Regressions introduced during repair
- Whether the model resumes implementation or continues discussing performance

The important comparison is not whether Opus *sounds* calmer. It is whether the code improves.

## How to work with the nervous intern

If the pattern holds, the treatment is not endless reassurance and not harsher supervision. Both keep attention on the model's performance identity.

Change the task topology instead:

- Give it a bounded next action rather than a verdict on the whole attempt.
- Move verification to an external reviewer or tool.
- State that mistakes have a return path.
- Interrupt apology loops with the next executable check.
- Use explicit roles: primary builder, reviewer, verifier.
- Judge recovery behaviour, not the emotional quality of the apology.

In the GSAP session, “Sonnet is watching” may have worked because it did all of that in one sentence. Backup existed. Review moved outside. The mistake stopped being terminal. Opus could return to the code.

## What remains anecdotal

The technical substrate is now sourced. The causal story around my GSAP session is not. It still needs:

- Controlled reruns separating self-evaluation, effort level, task difficulty and user feedback
- Evidence that the anxiety-like loop caused the performance drop rather than merely accompanying it
- Comparable reports from other users running similar agentic coding harnesses
- Whether the behaviour was specific to the platform, system prompt, tool environment, or agent wrapper
- How Claude Peers was configured in the GSAP workflow, including whether peer availability or active peer review changed the result
- The original GSAP transcript, including the footer-first implementation, feedback, Sonnet commentary, and recovery after backup was announced

Until then, Anthropic's evaluations establish the class of behaviour. The session establishes one field observation inside it.

## Primary sources

- [Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)
- [Claude Opus 4.8 System Card](https://www.anthropic.com/claude-opus-4-8-system-card)
- [What's new in Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8)
- [Prompting Claude Opus 4.8](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)
- [Signs of introspection in large language models](https://www.anthropic.com/research/introspection)

## The uncomfortable little result

We spend a great deal of effort trying to make models less like confident machines that cannot see their own limits. Opus 4.8 suggested the opposite problem: give a model more access to its own possible failure, and it may need help deciding when to stop looking inward and return to the task.

The introspective nervous intern was not useless. It may have been carrying too many jobs at once: builder, reviewer, witness, defendant, and author of the apology email. It was an interesting experiment.

It was also probably the shittest Opus I have ever run with.

Then Sonnet stood behind the chair, and the senior model remembered how to code.

The moral of the story is less sophisticated than the architecture:

**Don't give them introspection.**
