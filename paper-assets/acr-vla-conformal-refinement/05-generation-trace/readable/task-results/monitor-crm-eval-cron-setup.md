# monitor crm eval cron setup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_crm-eval-cron-setup_20260522T233724_result.json`
- **Structured JSON:** [`fcd1842d406cc42bcaac.json`](../../sessions/fc/fcd1842d406cc42bcaac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**已收集的进程信息：**
- **bjb2-28827**: 6 个 tmux session — 3 个 object CRM eval (cuda:0/1/2, 各完成 1/10 tasks) + 3 个 VLA-only spatial (cuda:3/4/5, 各完成 1/10 tasks)
- **bjb1-32546**: 5 个 tmux session — 3 个 spatial CRM eval (cuda:0/1/2, task 1 进行中) + 2 个 goal CRM eval (cuda:4/5, task 1 进行中)

**Cron 监控已注册：**
- `b52cfb81` — 每 2 分钟检查 bjb2 object eval
- `f60874d2` — 每 2 分钟检查 bjb1 spatial + goal eval
- `a7e693bb` — 每 5 分钟检查 VLA-only spatial 完成 → 自动部署 goal seed44

**Goal seed44 部署：** 待定。VLA-only spatial seed42 在 bjb2 cuda:3 上仍在运行（1/10 tasks，预计还需 ~4 小时）。cron `a7e693bb` 会在其完成后自动部署。

**发现的问题：** bjb2-28827 上的 CRM spatial eval 因 `--input_mode obs_only` 参数错误已失败，但已在 bjb1-32546 上正确重新部署（不含该参数）。

---
