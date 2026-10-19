# eval prep 30k eval command

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_prep_30k_eval_command_20260527T083459_result.json`
- **Structured JSON:** [`db646ad3ec3581a450ca.json`](../../sessions/db/db646ad3ec3581a450ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练状态汇总：

**s0 (cuda:1)**: step 29585/30000 (99%), 剩余 ~32 min，预计 ~09:55 UTC 完成
- 速度 4.62s/it，loss 稳定 0.012-0.025
- Checkpoint 目录目前有 26000, 28000, best — 30000 尚未生成

**s1 (cuda:2)**: step 29035/30000 (97%), 剩余 ~1h15min，预计 ~10:37 UTC 完成
- 速度 4.63s/it，loss 稳定

训练均未完成，不启动 eval。Agent 可通过 cron 监控 s0 完成后立即在 cuda:0 启动 30K eval，命令已确认（含 --pi05）。

---
