# ops deploy bjb1 32546 cuda4 vla only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy-bjb1-32546-cuda4-vla-only_20260515T051026_result.json`
- **Structured JSON:** [`2e838d25a7b50abe8e87.json`](../../sessions/2e/2e838d25a7b50abe8e87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成，进程正常启动。

| 项目 | 值 |
|------|-----|
| **exp_id** | `eval-vla-only-object-k1` |
| **PID** | 39397 |
| **GPU** | bjb1-32546 cuda:4 |
| **参数** | `--mode vla_only --baseline_mode single --K 1 --benchmark object --n_rollouts 10` |
| **日志** | `~/runs/acr-vla-conformal-refinement/eval-vla-only-object-k1.log` |
| **预计运行时间** | ~8-10 小时（参考同服务器其他 object eval，1 task 约 1h，共 10 tasks；K=1 比 K=10 快，但 rollout 仍受仿真速度限制） |

模型已加载，正在加载 LIBERO object 环境，即将开始 rollout。

---
