# check r7n2 r3 final

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_r7n2-r3-final_20260516T050600_result.json`
- **Structured JSON:** [`737519bfa8f5b18b8bf1.json`](../../sessions/73/737519bfa8f5b18b8bf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终结果

### 完成状态
7/21 runs 完成（脚本在确认趋势后跳过中间 scales）。进程已正常退出。

### 结果汇总

**Step-level Balanced Accuracy:**

| Scale | n_train | Seed 42 | Seed 43 | Seed 44 | Mean ± Std |
|-------|---------|---------|---------|---------|------------|
| 25% | 433 | 0.498 | 0.508 | 0.486 | **0.497 ± 0.009** |
| 50% | 867 | 0.493 | — | — | 0.493 |
| 800% | 13,880 | 0.515 | 0.517 | 0.500 | **0.511 ± 0.007** |

**Episode-level Balanced Accuracy:**

| Scale | n_train | Seed 42 | Seed 43 | Seed 44 | Mean ± Std |
|-------|---------|---------|---------|---------|------------|
| 25% | 433 | 0.498 | 0.496 | 0.492 | **0.495 ± 0.003** |
| 50% | 867 | 0.515 | — | — | 0.515 |
| 800% | 13,880 | 0.498 | 0.525 | 0.508 | **0.510 ± 0.011** |

**Internal-class recall (episode-level):** 0.0% – 8.3% across all scales. Model predicts almost exclusively "deterministic".

### 结论：Negative (Outcome B 确认)

32x 数据扩增（433 → 13,880）对 episode-level balanced accuracy 无改善，始终 ≈ 50%（随机水平）。根本原因：极端类别不平衡（800% scale 下 deterministic:internal = 97.7%:2.3%），监督分类在此信号密度下必然 collapse 到多数类预测。

**Registry 已更新为 DONE/negative，cron 已删除。**

---
