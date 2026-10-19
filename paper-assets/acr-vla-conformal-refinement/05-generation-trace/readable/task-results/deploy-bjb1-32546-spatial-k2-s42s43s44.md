# deploy bjb1 32546 spatial k2 s42s43s44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-spatial-k2-s42s43s44_20260525T053939_result.json`
- **Structured JSON:** [`7b9e0a430b22fca40fa5.json`](../../sessions/7b/7b9e0a430b22fca40fa5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个实验全部部署完成，registry 已注册为 RUNNING。

**部署摘要**:

| GPU | exp_id | mode | seed | 状态 |
|-----|--------|------|------|------|
| cuda:0 | eval-k2-spatial-adapt-s42-paired-r2 | adaptive_conformal_crm | 42 | RUNNING, rollout 5/20 进行中 |
| cuda:1 | eval-k2-spatial-vla-only-s42-paired-r2 | vla_only | 42 | RUNNING, rollout 5/20 进行中 |
| cuda:2 | eval-k2-spatial-adapt-s43-paired-r2 | adaptive_conformal_crm | 43 | RUNNING, tasks loaded |
| cuda:3 | eval-k2-spatial-vla-only-s43-paired-r2 | vla_only | 43 | RUNNING, tasks loaded |
| cuda:4 | eval-k2-spatial-adapt-s44-paired-r2 | adaptive_conformal_crm | 44 | RUNNING, tasks loaded |
| cuda:5 | eval-k2-spatial-vla-only-s44-paired-r2 | vla_only | 44 | RUNNING, tasks loaded |

所有 GPU 显存已占用（5.5-6.2 GiB），6 个进程均正常运行。CRM checkpoint 使用默认路径 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt`。

---
