# code plan001 collider mbias iv

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan001-collider-mbias-iv_20260520T092800_result.json`
- **Structured JSON:** [`25fc5bebb8940a7d44c6.json`](../../sessions/25/25fc5bebb8940a7d44c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，总耗时 609.8s。验证结果：

### DAG 1: Collider — 6/6 Y
| C | Th t_ctrl | MC t_ctrl | OK | Bias_ctrl |
|---|---|---|---|---|
| C1 | 0.9494 | 0.9493 | Y | -0.0506 |
| C2 | 0.9676 | 0.9675 | Y | -0.0324 |
| C3 | 0.9167 | 0.9169 | Y | -0.0833 |
| C4 | 1.0005 | 1.0005 | Y | +0.0005 |
| C5 | 0.9221 | 0.9220 | Y | -0.0779 |
| C6 | 0.9494 | 0.9493 | Y | -0.0506 |

No-control plim=1.0005≈τ=1.0. Random search: 85.4% of random C have |bias_ctrl|>|bias_nc|.

### DAG 2: M-bias — 6/6 Y
| C | Th t_ctrl | MC t_ctrl | OK | Bias_ctrl |
|---|---|---|---|---|
| C1 | 1.0064 | 1.0066 | Y | +0.0064 |
| C2 | 1.0127 | 1.0129 | Y | +0.0127 |
| C3 | 0.9948 | 0.9948 | Y | -0.0052 |
| C4 | 1.0014 | 1.0018 | Y | +0.0014 |
| C5 | 1.0089 | 1.0095 | Y | +0.0089 |
| C6 | 1.0064 | 1.0066 | Y | +0.0064 |

No-control plim=1.0003≈τ=1.0. Random search: 62.7% worse with control.

### DAG 3: IV BETA_MIXED — Wald: 4/6 Y (C3 W2 marginal, C4 unstable), OLS: 12/12 Y
### DAG 3: IV BETA_SAME — Wald: 4/6 Y (C4 unstable), OLS: 12/12 Y

C4_weak_diag 的 Wald N 是预期行为：近均匀 C 使 FS* 接近 0，Wald=RF/FS* 爆炸。OLS 列全部通过，theory-MC 一致性已确认。

---
