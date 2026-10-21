# deploy bjb1 32546 full saturation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-32546-full-saturation_20260526T154426_result.json`
- **Structured JSON:** [`8c77160a73fa1f732d0a.json`](../../sessions/8c/8c77160a73fa1f732d0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 部署完成 — 全 6 卡运行中

| GPU | 实验 ID | PID | 显存 | Util |
|-----|---------|-----|------|------|
| 0 | pi05-adaptive-long-s43-bjb1 | 903949 | 14741 MiB | 25% |
| 1 | pi05-adaptive-long-s44-bjb1 | 904304 | 14741 MiB | 22% |
| 2 | eval-crm-spatial-s48-d149-bjb1 | 908783 | 6306 MiB | 25% |
| 3 | eval-crm-object-s42-d149-bjb1 | 909918 | 5731 MiB | 26% |
| 4 | eval-crm-object-s43-d149-bjb1 | 911462 | 5731 MiB | 34% |
| 5 | eval-crm-goal-s43-d149-bjb1 | 912825 | 5609 MiB | 37% |

所有进程已通过 environment loading 阶段，进入 rollout。注册表 6 个实验状态均为 RUNNING。

**注**：D149 SmolVLA 实验首次启动因任务模板缺 `--checkpoint` 而失败，已补 `--crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` 后重启成功。

---
