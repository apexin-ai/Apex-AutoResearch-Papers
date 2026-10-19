# deploy smolvla baseline v3 spatial goal

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_smolvla-baseline-v3-spatial-goal_20260522T204846_result.json`
- **Structured JSON:** [`86187108cf29eced4adc.json`](../../sessions/86/86187108cf29eced4adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，总结：

**Registry 更新：**
- `eval-smolvla-lerobot-object-seed43-v2` → DONE (SR=66.5%)
- `eval-smolvla-lerobot-object-seed44-v2` → DONE (SR=65.0%)
- `eval-smolvla-lerobot-spatial-seed43-v2` → DONE/failed (killed on bjb1-18228)
- `eval-smolvla-lerobot-goal-seed43-v2` → DONE/failed (killed on bjb1-18228)

**已部署 (bjb1-32546)：**
- cuda:2 — `eval-smolvla-lerobot-spatial-seed43-v3` (RUNNING, 13GB VRAM)
- cuda:4 — `eval-smolvla-lerobot-goal-seed43-v3` (RUNNING, 10GB VRAM)

**待部署：**
- `goal_seed44` — 等 goal_seed43 完成后在 cuda:4 串行跑（已写入 cron 自动部署）

**监控：** 每 8 分钟 cron 检查日志，完成后自动更新 registry 并串行部署 goal_seed44。

---
