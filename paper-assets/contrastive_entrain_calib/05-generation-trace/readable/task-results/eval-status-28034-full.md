# eval status 28034 full

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_status-28034-full_20260522T185202_result.json`
- **Structured JSON:** [`f47a7afe14dd8fbbaa50.json`](../../sessions/f4/f47a7afe14dd8fbbaa50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== westd-28034 Status ===
GPU0: 占用 | PID 37266 | eval_unified_preset.py exp-004-s2-eval-ckpt5000 (17638MiB/32607MiB)
GPU1: 占用 | PID 30011 | exp-004-reduced-lora 训练 (21758MiB/32607MiB, 45% util)
GPU2: 空闲 | 2MiB
GPU3: 空闲 | 2MiB

exp-004-reduced-lora: step 1130/8000, total_loss=0.0009 (sft=0.0002, l2=0.0071), step_time≈6.9s/step, lr=4.40e-05
  预计剩余: ~(8000-1130)×6.9s ≈ 13.2h

空闲 GPU: cuda:2, cuda:3
残留进程: PID 22131 (eval_r3s2_ckpt8000 的 tmux 壳进程残留，但 tmux session 已不存在，未占用 GPU)

eval_results 最新文件:
  - exp-003-s2-ckpt7500 (May 22 21:36) ← 有结果
  - exp-002v3-ckpt1000/1500/500 (May 22 21:25-21:26)
  - exp-002v3-ckpt2000 (May 22 20:43)
  - exp-004-s2-ckpt2000 (May 22 19:57) ← 空目录

已 SCP 的 checkpoints:
  - exp-004-s2-v2-ckpt-4500
  - exp-004-s2-v2-ckpt-5000

注意: GPU0 正在跑 exp-004-s2-eval-ckpt5000 的 eval（用的是 eval_checkpoints 里的 ckpt-5000）。
```

---
