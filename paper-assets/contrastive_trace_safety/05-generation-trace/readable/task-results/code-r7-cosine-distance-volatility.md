# code r7 cosine distance volatility

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r7_cosine_distance_volatility_20260518T053426_result.json`
- **Structured JSON:** [`ef4d6ec755e8490133bc.json`](../../sessions/ef/ef4d6ec755e8490133bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the summary:

## Cosine Distance Volatility: Shallow vs Deep Layers

| Model   | Layer (type)    | Mean cos_dist | Std cos_dist | Median   | N pairs |
|---------|----------------|---------------|-------------|----------|---------|
| R1-8B   | L2 (biased)    | 0.1855        | 0.0974      | 0.1569   | 11,640  |
| R1-8B   | L14 (corrected)| 0.4112        | 0.1434      | 0.4003   | 11,640  |
| OT-7B   | L2 (biased)    | 0.0771        | 0.0800      | 0.0408   | 18,032  |
| OT-7B   | L16 (corrected)| 0.2064        | 0.0911      | 0.1938   | 18,032  |
| QwQ-32B | L2 (biased)    | 0.0374        | 0.0639      | 0.0150   | 4,757   |
| QwQ-32B | L60 (corrected)| 0.1019        | 0.0754      | 0.0851   | 4,757   |
| R1-32B  | L10 (biased)   | 0.0669        | 0.0497      | 0.0524   | 3,406   |
| R1-32B  | L63 (corrected)| 0.0916        | 0.0759      | 0.0739   | 3,406   |

### Volatility Ratio (shallow / deep)
| Model   | Ratio |
|---------|-------|
| R1-8B   | 0.45x |
| OT-7B   | 0.37x |
| QwQ-32B | 0.37x |
| R1-32B  | 0.73x |

**Counter to the initial hypothesis**: shallow layers are consistently **less** volatile (lower cosine distance) than deep layers across all 4 models. Shallow representations change less between adjacent steps, while deep layers show 1.4x-2.7x higher step-to-step variation.

This reframes the crossing rate bias mechanism: the issue with shallow layers is not that they're too volatile, but rather that their representations are **too stable/compressed**, with neighboring steps tightly clustered. This means a linear decision boundary in shallow layers operates on smaller margins, making threshold crossings more noise-driven (spurious) rather than reflecting genuine semantic transitions. Deep layers spread representations apart, producing more reliable (and less noisy) crossing signals.

Results saved to `artifacts/exp_r7_cosine_volatility/results.json`.

---
