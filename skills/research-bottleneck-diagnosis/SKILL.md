---
name: research-bottleneck-diagnosis
description: "Diagnose a quantified research bottleneck by comparing candidate explanations and designing discriminating controls, interventions and ablations. Use for attribution before mechanism design; distinguish contribution evidence from causal identification."
---

# Diagnose the bottleneck

Distinguish credible explanations at low cost rather than prove a favorite guess. If the problem is not quantified, obtain the necessary measurement first; a cause list cannot substitute for a real problem.

## Procedure

1. Use the actual structure, logs, and relevant knowledge to identify candidate causes and alternatives: measurement/data, representation/mechanism, optimization/implementation, or evaluation factors as applicable. Do not impose an idea quota.
2. For each candidate, specify predictions that differ from alternatives, falsifying outcomes, the test operation, controlled conditions, and cost. Prioritize tests that change the decision; exhaustive elimination is unnecessary.
3. Design controls, interventions, or ablations. Distinguish changing a component with the remaining system fixed from retraining or retuning. Record simultaneous changes in parameters, compute, training, data, and optimization; consider budget matching, simple replacements, and factor interactions when necessary.
4. Separate intervention delivery, predicted mediator change, and final outcome change. A failed intervention does not refute its mechanism. A delivered intervention contradicting a reliable mechanism prediction is relevant counterevidence. A better final score with an unknown mediator does not establish the mechanism.
   For “no mediator change,” assess expected effect size, sensitivity, timing, strata/aggregation, and uncertainty. Non-detection is not proof of zero. Use a known-change control if needed. If valid measurement rules out the prediction, accept counterevidence rather than indefinitely protecting the hypothesis as “unmeasurable.”
5. Mark explanations supported, weakened, unresolved, or untested, with scope. An ablation supports contribution in its configuration/protocol. Causal claims need intervention, confounding, identification assumptions, and limits; association alone is not a root cause.

## Deliverable and exit

Provide competing hypotheses, prioritized tests, failure interpretations, and the next decision. Adapt the [diagnosis matrix](assets/diagnosis-matrix.md) when saving output. Sufficient evidence yields mechanism-targeted design constraints; insufficient evidence yields an informative test or a narrower conclusion, not automatic module stacking.

Design and execution are separate. An attribution request does not authorize implementation, training, or paid calls. Actual runs follow current authorization and resource limits; retain negative results. Do not introduce competition award rhetoric.
