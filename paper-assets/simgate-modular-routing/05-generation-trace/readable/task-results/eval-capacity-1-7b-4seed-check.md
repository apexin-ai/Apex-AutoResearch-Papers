# eval capacity 1 7b 4seed check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_capacity-1_7b-4seed-check_20260517T003136_result.json`
- **Structured JSON:** [`1456e6521478be63b02e.json`](../../sessions/14/1456e6521478be63b02e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练+eval 已完成。结果如下：

```
=== Capacity Scaling 1.7B (4-seed) Results ===

Status: COMPLETED

Per-seed episode-level balanced_acc:
  seed42: 44.37%
  seed43: 43.54%
  seed44: 42.71%
  seed45: 41.67%
  Mean: 43.07% (std: 1.00%)

Comparison:
  0.6B (4 seeds): 50.7%
  1.7B (4 seeds, new): 43.1%
  1.7B (8 seeds, old): 47.1%
  4B (4 seeds): 58.96%

Non-monotonicity: REAL (worse than both 0.6B and old 1.7B run)
```

结果文件：`/root/autodl-tmp/simgate-modular-routing/results/capacity_episode_eval/1_7b_4seed_summary.json`

问题严重：1.7B 新跑的 4-seed 结果 (43.1%) 不仅低于 0.6B (50.7%)，还低于之前 1.7B 8-seed 的 47.1%。det_recall 在 seed45 上跳到 73.3% 但 int_recall 只有 10%，说明模型严重偏向某一类。这可能指向训练配置问题（learning rate、epochs、data split）而非真实的 capacity scaling 失败。

---
