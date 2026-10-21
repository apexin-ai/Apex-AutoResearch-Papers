# eval exp004 ckpt8000 immediate

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp004-ckpt8000-immediate_20260519T141710_result.json`
- **Structured JSON:** [`82ca48484532509880eb.json`](../../sessions/82/82ca48484532509880eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 **不空闲**。当前正在跑 exp004-ckpt2000 的 eval（已运行 ~5 分钟）：

```
PID 138467 | GPU 0 | 17650 MiB
eval_unified_preset.py --lora_path .../checkpoint-2000 --exp_id exp004-ckpt2000
```

所有 4 张 GPU 都有进程占用。Checkpoint-8000 路径已确认存在：
`/root/contrastive_entrain_calib/outputs/exp-004-act-baseline/checkpoint-8000`

**选项**：
1. 等 ckpt-2000 eval 跑完（预计 ~40-55 min），再在 GPU 0 上跑 ckpt-8000
2. 现在直接排队：写个脚本等 PID 138467 结束后自动启动 ckpt-8000 eval

选哪个？

---
