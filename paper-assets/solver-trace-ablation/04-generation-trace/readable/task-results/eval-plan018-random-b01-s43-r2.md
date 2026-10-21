# eval plan018 random b01 s43 r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan018-random-b01-s43-r2_20260514T164553_result.json`
- **Structured JSON:** [`8474bfdb8e85ba4ef7ce.json`](../../sessions/84/8474bfdb8e85ba4ef7ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。结果汇总：

## plan018-additive-random-b01-s43-r2 Eval 结果

### 训练 metrics (step 500)
| 指标 | 值 |
|------|-----|
| train_loss | 0.009 |
| final loss | 0.004 |
| prove_rate (train log) | 0.593 |
| mean_isr (train log) | 0.099 |
| epoch | 2.0 |
| train_runtime | 4692s (~78min) |

### eval_sta.py 结果 (proofwriter_fol_100, Prover9)
| 指标 | 值 |
|------|-----|
| **prove_rate** | **0.88** |
| **mean_isr** | **0.0506** |
| isr_std | 0.0668 |
| median_isr | 0.0 |
| proved_only_mean_isr | 0.0575 |
| isr_pr_ratio | 0.0575 |
| min_isr / max_isr | 0.0 / 0.222 |
| n_proved / n_problems | 88 / 100 |
| elapsed_seconds | 517.0 |

### By answer type
| Type | Count | Proved | PR | Mean ISR |
|------|-------|--------|----|----------|
| false | 25 | 22 | 0.88 | 0.033 |
| unknown | 41 | 37 | 0.90 | 0.045 |
| true | 34 | 29 | 0.85 | 0.071 |

### 同系列对比
| Seed | PR | ISR |
|------|----|-----|
| s42 | 0.79 | 0.104 |
| **s43** | **0.88** | **0.051** |
| s44 | 0.89 | 0.062 |

s43 的 PR 与 s44 接近（0.88 vs 0.89），ISR 最低（0.051），显示最佳的 random baseline 压制效果。

---
