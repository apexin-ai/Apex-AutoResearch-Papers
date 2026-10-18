# analysis eval pi05 l2norm k09 seed47 w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_pi05_l2norm_k09_seed47_w41_20260529T082005_result.json`
- **Structured JSON:** [`6eb1a58d9025693b970d.json`](../../sessions/6e/6eb1a58d9025693b970d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总如下：

## eval_pi05_l2norm_k09_long_seed47_w41

- **SR = 80.4%**，EXIT_CODE=0，正常完成（149.4 min）
- Per-task: T0=100%, T1=90%, T2=90%, T3=100%, T4=86%, T5=94%, T6=4%, T7=94%, T8=54%, T9=92%
- Registry 已更新为 DONE

## 其余 4 个实验状态

均已是 DONE，无需操作：
| exp_id | SR | status |
|---|---|---|
| eval_pi05_l2norm_k085_long_seed47_w38 | 77.8 | DONE |
| eval_pi05_random_k095_long_seed47_cqa1 | 62.0 | DONE |
| eval_pi05_random_k09_long_seed47_cqa1 | 30.8 | DONE |
| eval_pi05_random_k085_long_seed47_cqa1 | 43.4 | DONE |

## Seed47 完整表格

| k | L2norm seed47 | Random seed47 | L2norm 5-seed μ | Random 5-seed μ |
|---|---|---|---|---|
| 0.95 | **RUNNING** | 62.0 | 86.8±0.8 | 61.2±0.7 |
| 0.9 | **80.4** ✓ | 30.8 | 80.4±0.5 | 33.6±1.2 |
| 0.85 | 77.8 | 43.4 | 78.1±1.0 | 44.9±1.3 |
| 0.5 | 50.0 | **RUNNING** | 51.7±1.5 | 50.4±0.6 |

还有 2 个实验仍在 RUNNING：
- `eval_pi05_l2norm_k095_long_seed47_cqa1`
- `eval_pi05_random_k05_long_seed47_w38`

Seed47 已完成的结果均在 5-seed 均值的合理范围内（±1-2 std），无异常。

---
