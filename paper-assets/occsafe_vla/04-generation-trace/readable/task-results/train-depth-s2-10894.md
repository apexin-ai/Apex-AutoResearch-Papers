# train depth s2 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_depth-s2-10894_20260522T064147_result.json`
- **Structured JSON:** [`ad1673d16bc4ff64a36e.json`](../../sessions/ad/ad1673d16bc4ff64a36e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

磁盘空间不足。westd-10894 只有 **36G 可用**，远低于 100GB 阈值。

**磁盘占用明细（westd-10894 /root/autodl-tmp/checkpoints/）**：
- ablation_random_occ_s0 — 45G（DONE ✓）
- ablation_random_occ_s1 — 45G（DONE ✓）
- ablation_occ_detach_s0 — 45G（DONE ✓）
- ablation_occ_detach_s1 — 45G（DONE ✓）
- ablation_random_occ_s2 — 4K（刚开始训练）
- ablation_occ_detach_s2 — 4K（刚开始训练）
- 合计 ~180G 被已完成实验的 checkpoint 占用

**单个 depth checkpoint 约 15G**（westd-34685 数据：75G / 5 个 checkpoint）。depth_s2 训练到 50005 步：
- save_freq=2500 → 20 个 checkpoint → ~300G（不可能）
- save_freq=10000 → 5 个 checkpoint → ~75G（需要先清理出空间）

**可行方案**：
如果删除 4 个已完成的 ablation s0/s1 checkpoint（已经 DONE 且有 eval 结果），可释放 180G，总可用 ~216G，足够 depth_s2 甚至 depth_s3。

每个已完成实验都保留了 3 个 checkpoint（30000/40000/50000）和 eval 结果。如果评估已完成且结论已记录，这些 checkpoint 可以安全删除。

**需要你确认**：是否可以删除 westd-10894 上这 4 个已完成 ablation 实验的 checkpoint 目录来腾出空间？还是你想换其他方案？

---
