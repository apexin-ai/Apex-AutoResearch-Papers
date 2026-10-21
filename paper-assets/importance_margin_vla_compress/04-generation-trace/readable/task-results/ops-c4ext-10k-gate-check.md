# ops c4ext 10k gate check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c4ext_10k_gate_check_20260519T231700_result.json`
- **Structured JSON:** [`ed3053256c5d0bd3757e.json`](../../sessions/ed/ed3053256c5d0bd3757e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
C4-ext 10K Gate 数据
====================
当前 step: 9900 / 100000
当前 loss: 3.1055
LR: 9.81e-05
SPS: 0.6

最近 100 步统计 (step 4950-9900, 每步=50 iter):
- 平均 loss: 3.0245
- 趋势: 微弱下降 (前50步均值 3.0473 → 后50步均值 3.0016, Δ=-0.046)
- 后50步内部: 前半 2.9809 → 后半 3.0223 (近期略有回升但在噪声范围内)
- 范围: [2.2867, 3.5496]
- NaN/OOM: 无 (grep 0 匹配)

Eval checkpoint:
- step 5000 eval/action_loss: 3.1565

健康检查:
- 进程: 活 (PID 26118, uptime 4:43:54, CPU 428%, RSS 5.2GB)
- GPU: NVIDIA RTX PRO 6000 Black, 39°C, 159W/600W
- GPU 显存: 30.1GB / 97.9GB (30.8%)
- SPS 稳定: 是 (全程恒定 0.6)

ETA 10K: ~07:21 UTC (距最新日志 ~2.7 min)

Gate 建议数据:
- 平均 loss 3.02, 处于 > 3.0 区间 → 建议调查
- 但趋势缓慢下降, 且从 warmup 后 (step 1000, loss ~3.6) 持续降至 3.0 附近
- 方差较大 (2.29-3.55), 单步 loss 波动明显
- 无任何异常 (无 NaN/OOM/error, SPS 稳定, GPU 健康)
- 综合判断: 处于 3.0 边界, 仍在缓慢收敛中, 建议继续训练但密切监控
```

---
