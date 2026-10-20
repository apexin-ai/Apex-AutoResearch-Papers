# monitor grpo v2 step5 reward

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_grpo-v2-step5-reward_20260514T115958_result.json`
- **Structured JSON:** [`e7c6d374e48032eb4250.json`](../../sessions/e7/e7c6d374e48032eb4250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### GRPO v2 (PID 30171, cuda:0)
- **当前 step**: 6/73（1:03:12 elapsed，~10 min/step）
- **reward/mean**: **无法确认** — metrics 被 Python stdout 全缓冲卡住了。日志里 step 5 完成时有一行空白（TRL 清除进度条后应打印 metrics 的位置），但 `PrinterCallback` 的 `print()` 走 stdout，nohup 重定向下全缓冲，metrics 还在内存 buffer 中没 flush 到文件。
  - 日志中 grep "reward"/"loss" 零匹配
  - 没有 WandB（启动时没传 `--wandb-run-name`）
  - 没有 tensorboard runs 目录
  - 唯一的 hope 是等到 step 10（下一个 logging 点）看缓冲是否填满 flush，或者等 step 50 的 checkpoint 时读 `trainer_state.json`

### eval-sft-v2-ckpt (PID 32728, cuda:1)
- **已完成** (202/202)
- 结果保存在 `results/eval_sft_v2_ckpt.json`

| Metric | Mean | 90% CI |
|--------|------|--------|
| debug_accuracy | **0.762** | [0.713, 0.812] |
| probe_executed | **0.584** | [0.525, 0.644] |
| probe_diagnostic | **0.134** | [0.094, 0.173] |
| probe_dependent | **0.144** | [0.104, 0.183] |
| probe_generation_rate | 0.985 | — |

### 建议
GRPO v2 的 metrics 暂时看不到。两个选项：
1. **等** — step 10（~40 min 后）或之后某步时 stdout buffer 填满会自动 flush
2. **主动干预** — 如果你想现在就看到 metrics，可以 kill 再用 `python -u`（unbuffered）或 `PYTHONUNBUFFERED=1` 重新启动。不过这需要从头训练。

---
