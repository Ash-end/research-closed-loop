# The complete research loop

[中文](workflow.zh-CN.md) · [Home](../README.md)

## The logical contract

The goal is a traceable chain: **observed problem → competing explanation → intervention or method → predicted mechanism → empirical evidence → bounded conclusion → next decision**.

The chain is not a requirement to prove every cause before thinking, nor a universal model of theoretical research. Its purpose is to prevent a solution looking for a problem, unsupported mechanism stories, and unbounded experimentation. Planning remains distinct from execution authorization.

Start where the evidence places you. If there is only a topic, define an operational task, prepare lawful data and measurement, and keep the purported pain point unknown. If strong results already exist, audit them rather than re-run the earlier stages by ritual.

## 1. Localize a real, measurable problem

**Input:** a reproduction discrepancy, deployment failure, experimental anomaly, qualitative observation, or topic requiring initial measurement.

**Work:** define the task, metric, units, threshold, numerator/denominator, sampling unit, system version, and practical cost. Stratify by relevant boundaries while retaining the overall picture. Verify labels, measurement code, missingness, preprocessing, and pipeline behavior before calling a pattern an algorithmic weakness.

**Output:** a problem card stating where the discrepancy occurs, where it does not, its size and uncertainty, source evidence, and what remains unmeasured.

**Decision:** proceed to diagnosis if the discrepancy is sufficiently credible and consequential for the current question. Otherwise repair measurement, acquire missing evidence, redefine the task, or stop.

**Example:** 80 misses among 1,000 small objects versus 20 among 100 large objects means 8% versus 20% miss rates. Small objects contribute 80% of all misses, but have lower conditional risk. Total errors, worst-group risk, and business loss are different optimization objectives. These are illustrative numbers, not project findings.

## 2. Diagnose causes and bottlenecks

**Input:** a quantified problem and its boundaries, plus the relevant system structure and logs.

**Work:** propose credible competing explanations, observable predictions, and outcomes that would weaken each explanation. Select a cheap test that differentiates them: a controlled comparison, intervention, ablation, replacement, or interaction design. Track factors changing together, including capacity, compute, training exposure, and optimization.

**Output:** a hypothesis matrix and prioritized tests, with controls, cost, interpretation limits, and falsifying outcomes.

**Decision:** if evidence isolates a useful bottleneck, derive constraints for a mechanism-targeted design. If explanations remain entangled, perform the most informative next check or narrow the conclusion. Exhaustively listing every imaginable cause is unnecessary.

**Failure interpretation:** distinguish intervention not delivered; delivered but mediator prediction contradicted; mediator changed but downstream benefit absent; and final outcome improved without the mediator being established. A wide interval containing both zero and a predicted effect is unresolved evidence, not proof of either zero or the mechanism. A reliable measurement excluding the prediction is counterevidence.

**Example:** deleting module A reduces score by two points but also halves training time and reduces parameters by 40%. This suggests contribution under that protocol, not proof of A's unique mechanism. Compare compute/capacity-matched alternatives and measure the claimed mediator.

## 3. Map literature and formulate a bounded gap

**Input:** the task, bottleneck hypothesis, practical constraints, and the candidate operation.

**Work:** search primary papers and official supplements with task, mechanism, constraints, synonyms, and contrary-result terms. Prioritize recent work while retaining foundational and closest prior work. Record search date, coverage, and access limits. For each relevant claim, identify source location, assumptions, data/protocol, result, and cost; separate author reports from your inference.

**Output:** a claim–source–conditions matrix; what prior methods already solve; demonstrated limits versus unevaluated dimensions; a bounded gap; and the proposed method's substantive distinction.

**Decision:** if existing methods already meet the need, reproduce or use them. Otherwise turn the proposed difference into a testable operation and explicitly name its assumptions, costs, and counterexamples. If access is insufficient, keep novelty provisional rather than inventing citations.

**Gap form:** “Under X, existing approaches impose Y or leave Z unsupported. Operation M differs from closest approach N by D and predicts observation O, at cost R.” Novelty need not overturn the field; addressing a neglected dimension can be substantive if evidence supports it.

## 4. Test the smallest informative prototype

**Input:** a concrete operation, mechanism prediction, competing explanation, available development data, and resource constraints.

**Work:** select the least expensive way to distinguish the hypothesis: derivation, counterexample, measurement check, toy study, or small implementation. Preserve bottleneck-triggering conditions. Include a credible simple/existing baseline and relevant measures of bottleneck, mediator, final effect, and cost. Define continue/revise/stop conditions before examining outcomes.

**Output:** a pilot plan with inputs, protocol, budget/estimation basis, iteration bounds, outcome interpretations, and an independent confirmation route.

**Decision:** a promising signal may justify stronger validation; an important mechanism question may justify further focused tests. A valid negative result can justify stopping or changing direction. A toy improvement alone does not warrant superiority claims.

**Budget rule:** unknown runtime is not a license to fabricate an estimate. Use existing logs or, only after execution is authorized, a bounded small run. Include preparation, analysis, and recovery in the total budget. If the necessary test does not fit, label a reduced pilot, seek cheaper evidence, or stop—not an artificially “complete” truncated experiment.

**Example:** a VLM prompt reduces unsupported object assertions. Also check correct-object coverage and abstention; producing less content can reduce errors without resolving the proposed visual-grounding bottleneck.

## 5. Build complete, claim-specific validation

**Input:** the current method, provisional findings, intended claims, failure boundaries, and budget.

**Work:** choose experiments that address each claim and its strongest alternative explanation. Use credible simple baselines, closest prior work, and relevant strong baselines with matched data, splits, metrics, backbones, and training/search resources. Separate incomparable public scores. Evaluate appropriate independent datasets/settings, checking shared entities, temporal leakage, near-duplicates, and common data sources.

Preserve development/confirmation separation. State whether ablations hold the rest fixed or retrain/retune. Test meaningful replacements/interactions rather than assuming every module is necessary. Report actual repetitions, uncertainty, statistical assumptions, meaningful effect sizes, costs, negative results, and reproducibility details. The [scikit-learn pitfalls guide](https://scikit-learn.org/stable/common_pitfalls.html) explains preprocessing and test-data leakage; the [NeurIPS checklist](https://neurips.cc/public/guides/PaperChecklist) provides a domain-specific disclosure reference, not a universal acceptance standard.

**Output:** a validation protocol or evidence audit mapping every claim to a result, support status, limitations, and next decision.

**Decision:** retain supported claims within tested scope; narrow partial claims; revise or stop unsupported ones. Do not cherry-pick seeds/datasets or assume an extra loss/branch fixes the residual problem. Multiple datasets strengthen bounded evidence, not universal generalization; components can legitimately be unnecessary.

**Example:** two datasets sharing 30% of images are not two independent confirmations. A test set used to select among twenty configurations is development evidence, even if the best score increased.

## 6. Manage directions, resource limits, and correlated risk

**Input:** current directions, actual resources, deadlines, dependencies, evidence, and known failure modes.

**Work:** maintain a main direction and affordable alternatives when useful. Compare practical value, next informative action, cost, evidence, and shared risk. Two candidates built on the same unavailable dataset or unsupported mechanism do not automatically diversify risk. Decide what to prioritize, defer, revise, or stop.

**Output:** a small portfolio board with allocation, backup maintenance cost, common risks, and evidence-based switch/stop conditions.

**Decision:** switch when a central prediction is refuted, needed data remain unavailable, benefit fails to justify cost, or the budget/deadline is reached. A temporary implementation fault is not itself a reason to abandon the idea. One main line can be appropriate; two or three directions are not a quota.

This stage is cross-cutting rather than a final checkpoint. Revisit it when resource/evidence changes. It does not launch agents, parallel GPU jobs, background schedules, or unlimited retries.

## Records, resumption, and output sizing

Use existing notes when possible. For a brief diagnosis, a short explanation and next test may be sufficient. For a full project, optional templates retain problem definitions, hypothesis status, source support, run IDs, costs, negative outcomes, and decisions.

To resume, supply the most recent state and new evidence. Ask the router to update the decision; do not restart by default. An artifact is persistent context, not an autonomous scheduler.

The [project state template](../skills/research-closed-loop/assets/research-state.md) is a starting point. All templates can be shortened; a missing field is preferable to a fabricated value.

## Boundaries

Empirical effects, mechanism explanations, causal identification, and external validity are different claims. Read [interpretation boundaries](../skills/research-closed-loop/references/decision-boundaries.md) for worked distinctions. These skills assist reasoning; appropriate data, tooling, statistics, ethics, and human judgment remain necessary. They never guarantee publication, awards, generalization, or successful experimentation.
