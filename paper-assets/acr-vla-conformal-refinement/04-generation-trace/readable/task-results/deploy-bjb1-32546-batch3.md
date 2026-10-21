# deploy bjb1 32546 batch3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-batch3_20260519T202911_result.json`
- **Structured JSON:** [`3451a1298b689b655d4f.json`](../../sessions/34/3451a1298b689b655d4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部部署完成，registry 已注册为 RUNNING。

| GPU | exp_id | 模式 | Benchmark | Seed | PID |
|-----|--------|------|-----------|------|-----|
| cuda:1 | eval-crm-goal-seed44 | crm_obs_only | Goal (OOD) | 44 | 83909 |
| cuda:3 | eval-crm-goal-seed45 | crm_obs_only | Goal (OOD) | 45 | 85315 |
| cuda:4 | eval-vla-only-long-seed47 | vla_only | Long | 47 | 86796 |
| cuda:5 | eval-vla-only-spatial-seed48 | vla_only | Spatial | 48 | 88042 |

GPU 显存已分配（5.6-7.3 GB），日志显示模型和环境加载正常，无报错。

---
