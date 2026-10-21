# check exp008d checkpoints

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp008d-checkpoints_20260524T205048_result.json`
- **Structured JSON:** [`75938e8b7c247317d754.json`](../../sessions/75/75938e8b7c247317d754.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

```
exp_008d_subsample_on_h8:  无中间 checkpoint，仅 latest.pt (221MB)
exp_008d_civo_trigger_s1:  有 1 个中间 checkpoint: checkpoint_25000.pt + latest.pt
exp_008d_civo_trigger_s3:  有 2 个中间 checkpoint: checkpoint_25000.pt, checkpoint_75000.pt + latest.pt
exp_008d_civo_trigger_s4:  有 2 个中间 checkpoint: checkpoint_25000.pt, checkpoint_75000.pt + latest.pt
exp_006:                   不存在（bjb1-45299 无此目录）

bjb1-40020:                无任何 exp_008d 或 exp_006 目录

覆盖范围: 15K-55K 区间 — 只有 checkpoint_25000.pt 落在此范围
           checkpoint 间距太大（25K → 75K → latest），≥5 个 checkpoint: 不满足
```

**总结**: collapse 过程的中间 checkpoint 极度稀疏。整个 008d 系列只保存了 step 25000 和 75000 两个 checkpoint，15K-55K 区间仅有 25K 一个点，远达不到 ≥5 个 checkpoint 的要求。原始 exp_008d_subsample_on_h8 甚至没有任何中间 checkpoint。

---
