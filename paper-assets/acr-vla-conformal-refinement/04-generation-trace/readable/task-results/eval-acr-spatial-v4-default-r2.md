# eval acr spatial v4 default r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acr-spatial-v4-default-r2_20260514T202900_result.json`
- **Structured JSON:** [`a6f7b81224130c9747c0.json`](../../sessions/a6/a6f7b81224130c9747c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`eval-acr-spatial-v4-default` 已启动并注册。

**状态汇总：**
- **服务器**: bjb1-18228, cuda:0
- **tmux session**: `eval-acr-spatial-v4-default`
- **进程已确认运行**: SmolVLA + CRM v3-norm 已加载，正在载入 LIBERO spatial 环境（10 tasks x 10 rollouts）
- **参数**: `--mode acr_vla --benchmark spatial --n_rollouts 10 --seed 42 --K 10`，使用默认 max_correction_norm（checkpoint 内置值 1.42）
- **Registry**: RUNNING，spec 已填充

注意：tee 日志写入失败（目录已补建），stdout 仍在 tmux 内可用。后续查状态用 `tmux capture-pane -t eval-acr-spatial-v4-default -p`。

---
