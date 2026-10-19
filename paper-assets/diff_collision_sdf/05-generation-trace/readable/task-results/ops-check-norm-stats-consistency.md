# ops check norm stats consistency

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_norm_stats_consistency_20260522T061218_result.json`
- **Structured JSON:** [`64092c62aded904ed17e.json`](../../sessions/64/64092c62aded904ed17e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

1. **两个文件完全一致。** baseline_object_pudding_eval 和 pi0_base 的 norm_stats.json 内容相同（文件大小均为 1126 bytes，所有 key/value 完全匹配）。

2. **无差异。** 两者的 `state`（8 维 mean/std）和 `actions`（7 维 mean/std）数值完全相同，q01/q99 均为 null。

3. **A3 checkpoint 目录下没有自己的 norm_stats.json**（路径 `/root/autodl-tmp/checkpoints/a3_grad_refine_object_pudding/a3_grad_refine_object_pudding_seed0/best/assets/physical-intelligence/libero/norm_stats.json` 不存在）。

---
