---
name: research-validation-design
description: "Design claim-specific empirical validation with fair baselines, independent datasets or splits, component and interaction tests, uncertainty, reproducibility and explicit limits. Use after a pilot or to audit evidence; no universal proof from benchmark wins."
---

# Validate claims and audit evidence

Start from what each claim needs, not from accumulating datasets and tables. Use this stage to design validation or audit existing results; without actual data, deliver a plan only.

## Procedure

1. Specify central claims, scope, competing explanations, and minimum necessary evidence. Separate performance, mechanism, generalization, efficiency, and real-world causal claims.
2. Select independent data/settings and splits covering relevant boundaries. Check shared entities, common sources, temporal leakage, near-duplicates, and preprocessing leakage. Split by appropriate groups/time; correlated frames are not independent samples. Use development data for selection and untouched evaluation after freezing. A test set used for tuning requires disclosure and new confirmatory evidence.
3. Include credible simple baselines, closest prior work, and relevant strong baselines. Match data, splits, metrics, training/search budgets, backbones, and external resources. Report incomparable published scores separately; they do not directly establish a SOTA win. Explain benefit and cost when resources differ.
4. Deletions, replacements, design alternatives, and factor interactions answer specified questions. State whether other parts are fixed or retrained/retuned. Do not assume every module is necessary. Remove unhelpful components; test interactions for complementary components. Explain how an extra loss/branch targets a supported residual bottleneck before adding it.
5. Where randomness matters, use budget-appropriate repetitions and report actual counts, effect sizes, dispersion/appropriate intervals, and error-bar meaning. Match statistical methods, resampling units, and independence assumptions to the problem. Address selective multiple comparisons; no universal “three seeds are sufficient.”
6. Retain protocol, code/dependency versions, configurations, data licenses/splits, runs, and negative results. Map claims to evidence, failure settings, costs, and limitations. Unsupported claims require revision, narrowing, or stopping—not cherry-picking the best dataset/seed.

## Deliverable

Adapt the [validation protocol](assets/validation-protocol.md): must-have/optional experiments, dependencies, resource limits, and stopping conditions. For existing results, audit each claim as supported, partial, unsupported, or unknown. Multiple datasets strengthen tested scopes, not universal generalization; ablations are not automatic causal identification.

With unknown runtime, separate budget caps from evidence-based duration estimates. Once execution is authorized, estimate cost with small batches and reserve data checks, analysis, and recovery time. Mark insufficient evidence incomplete/pilot; reduced repetitions or truncated evaluation do not magically become sufficient confirmation.

Planning/auditing does not authorize code changes, training, external submissions, paid calls, or extra parallel jobs. Execution follows the current scope and budget. Do not inherit competition abstracts, scores, or award rules.
