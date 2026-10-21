# ssh check exp009 status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp009_status_20260522T200916_result.json`
- **Structured JSON:** [`6115b3f4d62ab6220db3.json`](../../sessions/61/6115b3f4d62ab6220db3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-009 OVB Validation 实验状态

### 1. 状态：运行中 — 196/200（98%）

当前正在跑 `[196/200] rho=0.9 seed=45`，已耗时 ~19h，ETA ~23 分钟。rho=0.9 还剩 5 个 seed（45-49）。

### 2. 已完成部分的 bias_slope 结果

**Sequential（基线）：**
| ρ | n | mean bias_slope |
|---|---|-----------------|
| 0.0 | 50 | 0.1982 ± 0.0547 |
| 0.3 | 50 | 0.1950 ± 0.0555 |
| 0.6 | 50 | 0.1910 ± 0.0568 |
| 0.9 | 45 | 0.1845 ± 0.0587 |

**Joint（MFRM）：**
| ρ | n | mean bias_slope |
|---|---|-----------------|
| 0.0 | 50 | 0.0558 ± 0.0241 |
| 0.3 | 50 | 0.0574 ± 0.0278 |
| 0.6 | 50 | 0.0595 ± 0.0293 |
| 0.9 | 45 | 0.0635 ± 0.0268 |

### 3. 关键发现

**bias_slope 没有随 ρ 单调递增** — 反而呈现出一个有意思的模式：

- **Sequential**: bias_slope 随 ρ **单调递减**（0.198 → 0.185），说明 rater correlation 越高，sequential 方法的 bias 反而略小
- **Joint (MFRM)**: bias_slope 随 ρ **单调递增**（0.056 → 0.064），但幅度很小（增幅仅 ~0.008）
- **核心结论**：Joint 方法在所有 ρ 条件下 bias_slope 都远低于 sequential（约 3-4 倍），且对 ρ 变化不敏感。RMSE 也一致更低（0.12 vs 0.21）

实验预计约 23 分钟内完成，rho=0.9 最后 5 个 seed 不太可能改变整体趋势。

---
