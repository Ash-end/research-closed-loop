---
name: research-minimal-prototype
description: "Design a low-cost prototype or falsification test for a research mechanism, with a credible baseline, informative measurements and bounded continue/revise/stop criteria. Use before expensive engineering; a positive pilot is not confirmatory proof."
---

# Build the smallest discriminating test

Minimize the cost of answering the research question, not merely code size. Choose derivation, counterexample, existing-result checks, toy experiments, or a small prototype as appropriate; not every idea needs a new trained network.

## Procedure

1. State the operation, mechanism, assumptions, expected observables, and competing explanation. A list of module names is not a method.
2. Select representative small development data retaining the bottleneck-triggering conditions and a reasonable reference. Check the pipeline, metric, and basic implementation. Toy-only evidence has explicit extrapolation limits.
3. Include a credible simple or existing baseline and control key resources. As relevant, measure bottleneck, mediator, overall outcome, and important costs. Overall improvement alone does not establish resolution of the target pain point.
4. Before observing outcomes, define continue/revise/stop conditions, resource limits, iteration bounds, and reasons. Do not invent power, thresholds, or GPU cost. Separate exploratory selection from confirmation; never repeatedly select on the final test set.
   If runtime is unknown, allocate budget rather than invent duration. After execution is authorized, use existing logs or a tightly bounded small run to estimate cost, including preparation, analysis, and failure buffer. If an informative test exceeds remaining resources, label a reduced pilot, seek cheaper evidence, or stop. A time cap does not imply adequate sample size.
5. Interpret failures separately: implementation/measurement fault, undelivered intervention, failed mechanism prediction, mediator success without downstream benefit, or benefit below cost. Check then revise; valid counterevidence can justify stopping. Do not assume the first version must fail or keep adding modules.

## Deliverable and exit

Provide the minimal test, required inputs, resource estimates and their basis, discriminating outcomes, and decision. Adapt the [pilot plan](assets/pilot-plan.md) for saved output. A positive signal motivates independent validation, not proof of superiority. An important unresolved mechanism may also justify further tests, with an explicit reason.

Implement and verify only when requested, in the authorized project and budget. The skill itself does not authorize training, paid calls, or remote execution. Retain negative results; do not fabricate experiments or apply competition award criteria.
