# ssh harvest newly completed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest-newly-completed_20260520T045334_result.json`
- **Structured JSON:** [`e4a8117b89e7e5b77dff.json`](../../sessions/e4/e4a8117b89e7e5b77dff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。以下是最近 30 分钟内新生成的 JSON 结果：

| 服务器 | 文件 | mode | benchmark | SR | avg_K | fast_path | 备注 |
|--------|------|------|-----------|-----|-------|-----------|------|
| bjb2-28827 | eval_goal_obs_only_norm02_seed48.json | crm_obs_only | goal | **0.68** | — | — | 12:21 生成 |
| bjb2-28827 | eval_spatial_obs_only_norm02_seed49.json | crm_obs_only | spatial | **0.32** | — | — | 12:37 生成 |
| bjb1-32546 | eval_object_vla_only_seed51.json | vla_only | object | **0.15** | — | — | 12:28 生成 |
| bjb1-32546 | eval_long_obs_only_norm02_seed48.json | crm_obs_only | long | **0.15** | — | — | 12:33 生成 |
| bjb1-32546 | eval_long_obs_only_norm02_seed49.json | crm_obs_only | long | **0.14** | — | — | 12:32 生成 |
| bjb1-32546 | eval_spatial_vla_only_seed51.json | vla_only | spatial | **0.33** | — | — | 12:47 生成 |
| bjb2-40593 | — | — | — | — | — | — | 无新文件 |

这些都是 baseline 实验（obs_only / vla_only），无 avg_K 和 fast_path 字段。

**重点关注项状态：**

1. **crm-goal-48** (bjb2-28827) — SR=0.68，已完成
2. **crm-spatial-49** (bjb2-28827) — SR=0.32，已完成
3. **vla-object-51** (bjb1-32546) — SR=0.15，已完成
4. **crm-long-48/49** (bjb1-32546) — SR=0.15/0.14，两个 seed 均已完成
5. **P25-seed44** (bjb2-40593) — **未生成**。logs 目录下无任何 `eval_*adaptive*` 或 `eval_*p25*` 文件，可能仍在运行或未启动

另：只查了 3 台服务器（bjb2-40593 / bjb2-28827 / bjb1-32546），第 4 台服务器名称未知，请确认。

---
