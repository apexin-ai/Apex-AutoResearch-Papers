# deploy bjb2 28827 freed gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-freed-gpus_20260526T175153_result.json`
- **Structured JSON:** [`1da138d954813b4216eb.json`](../../sessions/1d/1da138d954813b4216eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 部署完成

bjb2-28827 GPU 0/1（空闲）部署优先级 1：pi05 tau-sweep Object 补充 seed。

| GPU | exp_id | tau | PID | 显存 |
|---|---|---|---|---|
| cuda:0 | pi05-object-tau015-s42-bjb2 | 0.15 | 548972 | 10030 MiB |
| cuda:1 | pi05-object-tau035-s42-bjb2 | 0.35 | 549421 | 9545 MiB |

- 命令: `evaluate.py --model pi05 --mode adaptive_conformal_crm --K 2 --max_correction_norm 0.2 --benchmark object --seed 42 --n_rollouts 20`
- CRM checkpoint: `crm_pi05_unified_3suite/crm_best.pt`
- 输出: `logs/eval_object_adaptive_pi05_tau{015,035}_seed42.json`
- registry 已 RUNNING（含 hypothesis + spec）

GPU 2-5 仍在跑（10-12 GB 占用，util 20-50%），未触碰。

---
