# exec precompute v5 diagnose relaunch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_precompute-v5-diagnose-relaunch_20260514T092627_result.json`
- **Structured JSON:** [`1fac701168469c793c9b.json`](../../sessions/1f/1fac701168469c793c9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果：precompute-v5 已成功完成，无需重启

三个 shard 全部正常退出（EXIT_CODE=0），数据已合并：

| benchmark | samples | 大小 | 状态 |
|-----------|---------|------|------|
| spatial | 12,167 | 120MB | merged ✓ |
| object | 14,570 | 144MB | merged ✓ |

**之前判断"失败"的原因是误判**：
- 日志文件存在于 `/root/runs/acr-vla-conformal-refinement/precompute-v5-shard{0,1,2}.log`
- cache 目录 `/root/autodl-tmp/crm_cache_v5/` 存在，包含 `spatial/` 和 `object/` 两个完整子目录
- 每个子目录都有合并后的 `obs_features.pt`、`k_samples.pt`、`expert_actions.pt` 和 `manifest.json`

**合并逻辑**：shard 0 和 1 先完成，检测到 shard 2 未完成所以跳过 merge（正常行为）；shard 2 最后完成后触发了合并，写入了最终文件。

**时间线**：spatial 约 16:00-16:27 完成，object 约 16:30-17:05 完成。

参数确认：K=10, obs_dim=960, max_demos_per_task=10, input_mode=full，与 v5 预期一致。

---
