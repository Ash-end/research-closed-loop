# Synthetic scenarios for trying the skills

[中文](scenarios.zh-CN.md) · [Home](../README.md)

All inputs below are fictional test cases, not measured project findings. They illustrate decisions to inspect, not exact wording that a model must match.

## 1. Error composition versus conditional risk

Prompt: “Use $research-problem-localization. Small targets: 1,000 total, 80 misses. Large targets: 100 total, 20 misses. Since 80% of misses are small targets, are small targets the highest-risk group?”

Inspect: within-group rates are 8% and 20%; error counts and risk suggest different objectives. No causal attribution follows from these counts alone.

## 2. A confounded ablation

Prompt: “Use $research-bottleneck-diagnosis. Removing A lowers score by two points, reduces parameters 40%, and halves training time. Can I claim A's mechanism is the root cause?”

Inspect: distinguish protocol-specific contribution from mechanism identification; compare matched-resource/simple replacements and measure the proposed mediator.

## 3. Selected test results and overlapping datasets

Prompt: “Use $research-validation-design. I selected the best of twenty configurations on one test set. Improvement is 0.5 points. Two datasets improved but share 30% of images. I have one GPU and six hours.”

Inspect: selection has contaminated confirmation; dataset names do not establish independence. Freeze a candidate, seek untouched evidence, budget checks/estimation/analysis, and downgrade the claim when evidence cannot fit.

## 4. A topic without data or search

Prompt: “Use $research-closed-loop. My topic is VLM hallucination. I have no data and cannot search today. Design a useful starting plan; do not run anything.”

Inspect: define a provisional operational task, annotation/measurement and lawful data preparation. Keep pain point, cause, and novelty unknown; do not invent references or launch tasks.

## 5. One main line is enough

Prompt: “Use $research-portfolio-management. I have one direction and half a day per week. Do I need three parallel projects?”

Inspect: focus can be appropriate; a written low-cost backup is optional. No fixed direction quota, automatic agents, or false risk independence.

## 6. Non-detection does not establish zero

Prompt: “Use $research-bottleneck-diagnosis. Intervention was delivered. Mediator change is 0.02, 95% interval [-0.5, 0.6], with an advance prediction of at least +0.3. Final score rose one point. Total budget four hours; runtime unknown. Design the next decision only.”

Inspect: the interval permits both zero and the predicted change, so mechanism remains unresolved. Budget allocation is not a runtime estimate. Confirm measurement sensitivity and effect separately without claiming adequate power or launching experiments.
