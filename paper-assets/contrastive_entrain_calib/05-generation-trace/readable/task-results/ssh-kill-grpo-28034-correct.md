# ssh kill grpo 28034 correct

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-grpo-28034-correct_20260522T170251_result.json`
- **Structured JSON:** [`c88250c6a59786946144.json`](../../sessions/c8/c88250c6a59786946144.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
Server: westd-28034 confirmed (4x RTX 5090)
exp-003-s3 (PID 24760): KILLED (SIGTERM)
exp-003-len512 (PID 29337): KILLED (SIGKILL)
exp-003-len512-r3only (PID 29342, 残留): KILLED (SIGTERM)
tmux sessions: exp003_len512, exp-003-s3 已清除

Remaining active tasks:
- GPU 1: exp-004-reduced-lora (PID 30011, 21.8GB VRAM) — tmux session exp-004-reduced-lora
- GPU 3: eval_r3s2_ckpt8000 (PID 22138, 16.9GB VRAM) — tmux session eval_r3s2_ckpt8000
- GPU 0, 2: 空闲 (GPU-Util 100% 但无进程，应为刚 kill 后的残留状态，会很快降下来)
- 其余为 tensorboard / jupyter 等基础服务
```

---
