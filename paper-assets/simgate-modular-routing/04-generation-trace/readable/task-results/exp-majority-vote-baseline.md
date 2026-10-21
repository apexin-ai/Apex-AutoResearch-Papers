# exp majority vote baseline

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_majority-vote-baseline_20260516T013857_result.json`
- **Structured JSON:** [`e749edcd7cd36e2caaa8.json`](../../sessions/e7/e749edcd7cd36e2caaa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果完整。核心发现：

## 结果

### Task-type majority vote baseline

| Split Seed | TT-MajVote bal_acc | Global-Maj bal_acc | Val label dist |
|:---:|:---:|:---:|:---:|
| 42 | **0.5000** | 0.5000 | 240 det / 60 int |
| 123 | 1.0000* | 1.0000* | 330 det / 0 int |
| 456 | 1.0000* | 1.0000* | 330 det / 0 int |

*\*val set 100% deterministic，balanced_acc 退化为 trivial 1.0*

### vs Router (split seed=42)
- **TT majority vote: 0.5000** (= always predict "deterministic")
- **Router 8-seed mean: 0.4711±0.0221**
- Delta: +0.0289 → 朴素 baseline 优于 router

### 关键洞察

1. **所有 11 个 task_type 的 majority label 都是 "deterministic"**。TT-majority vote ≡ global majority vote ≡ "always predict det"。Task-type 级别不提供额外区分力。

2. **数据集极度不平衡**：train set 91.4% deterministic。"internal" label 只出现在 4 个 task_type（chemistry-mix, find-non-living-thing, grow-fruit, lifespan-longest-lived-then-shortest-lived）中，且都是少数。

3. **Episode-level split 无 stratify 导致 val set 不稳定**：seed 123/456 的 val set 完全没有 internal 样本。

4. **Router 低于 50% balanced_acc 的含义**：router 不是在"学习 task-type signal"——它在 unseen episodes 上表现比"永远猜 deterministic"还差，说明它过拟合到了训练 episode 的 step-level pattern，在 held-out episodes 上反而预测出更多错误的 "internal"。

结果已保存到 `results/majority_vote_baseline/results.json`，脚本在 `scripts/majority_vote_baseline.py`。

---
