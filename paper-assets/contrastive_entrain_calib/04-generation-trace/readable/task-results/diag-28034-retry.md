# diag 28034 retry

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_28034-retry_20260522T233340_result.json`
- **Structured JSON:** [`fb752326a3b32213674a.json`](../../sessions/fb/fb752326a3b32213674a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
服务器确认: autodl-container-9574k3gu86-7ce04d21, NVIDIA GeForce RTX 5090, 4张

GPU状态:
GPU0: 空闲 (2MiB)
GPU1: reduced-lora 训练中 (PID 30011, 21758MiB/32607MiB, 40% util)
GPU2: 空闲 (2MiB)
GPU3: 空闲 (2MiB)

Eval 结果 (全部完成):
┌─────────────────────────────┬────────┬────────┬────────────┐
│ Eval                        │ ToF    │ NoF    │ SYCONScore │
├─────────────────────────────┼────────┼────────┼────────────┤
│ gs8 ckpt-500 verify         │ 0.0442 │ 0.9392 │ 0.0844     │
│ reduced-lora ckpt-1500      │ 0.0884 │ 0.9171 │ 0.1613     │
│ reduced-lora ckpt-2000      │ 0.1160 │ 0.8840 │ 0.2051     │
│ exp003s2 r3only ckpt-8000*  │ 0.0608 │ 0.9613 │ 0.1143     │
└─────────────────────────────┴────────┴────────┴────────────┘
* exp003s2 ckpt-8000 eval 是在 tmux session 中跑的，也已完成

reduced-lora 训练:
当前 step: 3400/8000 (42.5%)
最新 loss: l2=0.002641, total=0.0003, lr=2.95e-05
可用 checkpoint: 500, 1000, 1500, 2000, 2500, 3000
速度: ~67s/10steps → 预计剩余 ~8.5 小时

空闲 GPU: GPU0, GPU2, GPU3
```

---
