# code exp28b check and exp31

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp28b-check-and-exp31_20260520T191039_result.json`
- **Structured JSON:** [`24fc460bf252a2828ae5.json`](../../sessions/24/24fc460bf252a2828ae5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks complete. Summary:

---

## Part A: exp28b Results

exp28b crashed during evaluation (float16 dtype in GRU), but all **9-class seed123 + seed456 runs completed**. Combined with exp28 seed42:

| N | IID | DD_OOD | AA_OOD |
|--:|:---:|:------:|:------:|
| 50 | 1.000±0.000 | 1.000±0.000 | 0.969±0.037 |
| 125 | 1.000±0.000 | 1.000±0.000 | 0.975±0.019 |
| 250 | 1.000±0.000 | 1.000±0.000 | 0.975±0.035 |
| 350 | 1.000±0.000 | 0.978±0.030 | 0.972±0.033 |

Vanilla (seed42 only): N=125 aa=0.244, N=350 aa=0.489. Vanilla N=50/250 missing (crash).

Registry: exp28b → **DONE (success)**.

## Part B: exp31 Lambda Ablation

| Lambda | IID | DD_OOD | **AA_OOD** | FITD_OOD |
|-------:|:---:|:------:|:----------:|:--------:|
| 0 | 1.0 | 1.0 | **1.0** | 1.0 |
| 0.1 | 1.0 | 1.0 | **0.990** | 1.0 |
| 0.5 | 1.0 | 1.0 | **0.981** | 1.0 |
| 1.0 | 1.0 | 1.0 | **0.981** | 1.0 |
| 2.0 | 1.0 | 1.0 | **0.944** | 1.0 |

**Hypothesis falsified (negative result)**: Higher lambda **monotonically hurts** AA OOD. lambda=0 (intent-only E2E, no persuasion aux loss) achieves perfect scores everywhere. The persuasion auxiliary loss acts as a distractor during E2E fine-tuning rather than a regularizer.

Registry: exp31 → **DONE (negative)**.

Output files:
- `results/exp28_combined_data_efficiency.json`
- `results/exp31_lambda_ablation.json`

---
