# ops kill ghost bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-ghost-bjb2-40593_20260515T054611_result.json`
- **Structured JSON:** [`20b169b614df6c8ae206.json`](../../sessions/20/20b169b614df6c8ae206.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。结果汇报：

**PID 211962 (ghost 进程)** — 已 kill，确认 DEAD。

**PID 227434 (eval-mag-obsonly-norm003-b2)** — ALIVE，运行正常。
- 状态: `Rl+`，已运行 15 分 14 秒
- 命令: `python -u src/evaluate.py --mode crm_obs_only --benchmark spatial --n_rollouts 10 --seed 42 --K 10 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt --max_correction_norm 0.03 --output_file logs/eval_mag_obsonly_norm003.json`
- 日志显示模型和环境已加载完成，正在执行 eval

**GPU 状态** — RTX 4090D，PID 227434 占用 6185MiB / 24564MiB，GPU 利用率 12%，温度 35°C，正常运行。

无需重新部署，eval 任务已恢复运行。

---
