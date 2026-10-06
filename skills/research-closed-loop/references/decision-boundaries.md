# Interpretation boundaries

## Always identify the denominator

“80% of misses are small targets” describes P(small | miss), not P(miss | small). Illustrative counts: 1,000 small targets with 80 misses, versus 100 large targets with 20 misses. Small targets contribute 80% of all misses, but within-group miss rates are 8% and 20%. Small targets contribute more errors, not higher conditional risk. Specify whether the objective is total errors, conditional risk, or practical loss. These figures are examples, not measured project results.

Define 32×32 as original/resized box dimensions or an area threshold. Fix matching/confidence thresholds, labels, and sampling definitions for comparisons, and report group sizes. Uncertainty must match the sampling unit; correlated frames are not independent individuals.

## Separate mechanism evidence from outcome evidence

Deleting a module may also change capacity, training time, or optimization. Identify simultaneous changes and consider budget matching, replacement components, and interactions. Controls do not automatically identify real-world causes; state interventions, confounding, measurement validity, and extrapolation scope.

| Observation | Supported interpretation | Do not automatically infer |
|---|---|---|
| Intervention not delivered | Mechanism remains untested | Mechanism is invalid |
| Intervention delivered; imprecise mediator estimate still permits prediction | Mechanism remains unresolved; improve measurement/discrimination | Non-detection is zero, or inclusion of prediction in an interval proves it |
| Intervention delivered; valid measurement excludes predicted mediator change | Counterevidence to the prediction under these conditions | Label every contradiction an invalid test |
| Mediator changes; final outcome does not | Check downstream assumptions, benefit size, and extra costs | Adding modules will solve it |
| Final outcome improves; mediator unknown | Effect may hold; mechanism remains unestablished | Intended mechanism is proven |

## Validation is not selecting winners

Use development data for selection and untouched evaluation after freezing. Repeated test-driven changes contaminate confirmation. Datasets sharing entities, near-duplicates, or collection sources are not independent merely because names differ.

Do not require every module to be necessary: delete unhelpful parts, assess interactions, and compare costs. Negative pilots may justify stopping, narrowing, or redirecting. Generalization, causation, mechanism, and description carry different evidence obligations.

## Stage exits are decisions, not mandatory passes

Continue for important mechanism questions, narrow claims when evidence is limited, or stop. There is no unique legal stage order. Two or three directions are optional, not a quota; one main line and a written backup may be enough. Do not automatically launch multiple experiments.
