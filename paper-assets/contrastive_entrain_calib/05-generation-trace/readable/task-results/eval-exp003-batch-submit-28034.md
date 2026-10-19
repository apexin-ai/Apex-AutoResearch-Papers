# eval exp003 batch submit 28034

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_exp003-batch-submit-28034_20260521T071737_result.json`
- **Structured JSON:** [`7e6d10d170d577b07315.json`](../../sessions/7e/7e6d10d170d577b07315.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

| 实验 | GPU | 显存占用 | PID | 状态 |
|------|-----|---------|-----|------|
| `exp-003-eval-ckpt5000-v2` | cuda:0 | 16764 MiB | 495833 | RUNNING |
| `exp-003-eval-ckpt6000` | cuda:1 | 16764 MiB | 495906 | RUNNING |
| `exp-003-eval-ckpt6500` | cuda:2 | 16152 MiB | 496116 | RUNNING |
| `exp-003-eval-ckpt7000` | cuda:3 | 14944 MiB | 496266 | RUNNING |

4 张 RTX 5090 全部占用，tmux session 和 torch compile workers 均已启动。每次 eval 约 1-1.5 小时，timeout 设为 4 小时。

---
