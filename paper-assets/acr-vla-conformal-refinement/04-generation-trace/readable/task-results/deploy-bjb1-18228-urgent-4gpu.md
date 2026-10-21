# deploy bjb1 18228 urgent 4gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-urgent-4gpu_20260519T200908_result.json`
- **Structured JSON:** [`983af40b0e8f38d7d56b.json`](../../sessions/98/983af40b0e8f38d7d56b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb1-18228 全部部署完成。4 个 GPU 全部占用：

| GPU | 实验 ID | 模式 | Benchmark | Seed | tmux session |
|-----|---------|------|-----------|------|-------------|
| 0 | eval-crm-goal-seed42 | crm_obs_only | goal | 42 | eval-crm-goal-seed42 |
| 2 | eval-crm-goal-seed43 | crm_obs_only | goal | 43 | eval-crm-goal-seed43 |
| 3 | eval-crm-long-seed45 | crm_obs_only | long | 45 | eval-crm-long-seed45 |
| 1 | eval-vla-only-object-seed48 | vla_only | object | 48 | eval-vla-only-object-seed48 |

所有实验已验证启动无报错，registry 已推进到 RUNNING。CRM checkpoint 本地已存在，无需 scp。

---
