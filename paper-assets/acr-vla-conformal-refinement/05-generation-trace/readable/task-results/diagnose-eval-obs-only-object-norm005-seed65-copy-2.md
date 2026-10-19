# diagnose eval obs only object norm005 seed65

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval-obs-only-object-norm005-seed65_20260521T023851_result.json`
- **Structured JSON:** [`f5bc82e722a8f378d9e0.json`](../../sessions/f5/f5bc82e722a8f378d9e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**实验未失败，已成功完成。** 监控系统误判。

**根因**：实验正常跑完，输出文件写到了相对路径 `logs/eval_obs_only_object_norm005_seed65.json`，实际位置是 `/root/acr-vla-conformal-refinement/logs/eval_obs_only_object_norm005_seed65.json`。监控系统在 `/root/autodl-tmp/...` 路径下找不到输出文件，也没有 W&B sentinel，因此 5 次探测后判定为 failed。

**实验结果**：
- Overall success rate (crm_obs_only, object, norm=0.05, seed=65): **14.0% (14/100)**
- 10 个 task 全部完成，结果已写入 JSON

**同服务器其他实验**：3 个 seed66 实验正常运行中（GPU 0/2/3，norm=0.03/0.05/0.1），GPU 1 已空闲。磁盘 61% 使用，无问题。

**不需要重跑。** 需要做的是：
1. 将结果文件从 `/root/acr-vla-conformal-refinement/logs/` 拷贝到监控系统期望的路径（如果需要）
2. 修正监控系统对该实验的状态标记为 completed

---
