# code exp D mcnemar

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_D_mcnemar_20260515T112338_result.json`
- **Structured JSON:** [`868d0fd10457637c2a3c.json`](../../sessions/86/868d0fd10457637c2a3c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

执行完成。注意 OBD OOF accuracy 这次为 43.6%（vs v2 的 38.0%），因为 LGBMClassifier 没有固定 `random_state`。配对检验结果无论如何都高度显著。

## 结果摘要

### OBD vs GPT-5.5 (N=500)
| | |
|---|---|
| OBD accuracy | 43.6% |
| GPT-5.5 accuracy | 33.2% |
| Difference | **+10.4pp** |
| Contingency | a=94, b=124, c=72, d=210 |
| McNemar exact p | **0.0002** |
| Bootstrap 95% CI | **[+5.0pp, +15.8pp]** |
| CI includes 0 | NO |

### OBD vs Claude (N=500)
| | |
|---|---|
| OBD accuracy | 43.6% |
| Claude accuracy | 33.0% |
| Difference | **+10.6pp** |
| Contingency | a=101, b=117, c=64, d=218 |
| McNemar exact p | **0.0001** |
| Bootstrap 95% CI | **[+5.4pp, +15.8pp]** |
| CI includes 0 | NO |

OBD 在配对检验下显著优于两个 LLM（p < 0.001），bootstrap CI 不含 0。

如果需要精确复现 v2 的 38.0% OBD 准确率，需要在 `LGBMClassifier` 里加 `random_state=42`——要我加上重跑吗？结果保存在 `artifacts/exp_D_mcnemar.json`。

---
