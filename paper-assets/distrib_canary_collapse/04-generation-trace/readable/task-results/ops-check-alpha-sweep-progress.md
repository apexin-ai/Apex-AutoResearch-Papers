# ops check alpha sweep progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-alpha-sweep-progress_20260514T233150_result.json`
- **Structured JSON:** [`fb520947c7f22c949f5a.json`](../../sessions/fb/fb520947c7f22c949f5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
alpha_sweep_a000_s42 (α=0.0):
  - GPU: cuda:0, 利用率 89%, 12.5GB/98GB
  - 进程: PID 46721, 已运行 4h31m
  - 进度: gen 10/10 训练中（synthetic data 已生成，正在训练）
  - 每 gen 约 26 分钟
  - 预估剩余: < 15 分钟（最后一个 gen 的训练阶段）

alpha_sweep_a025_s42_v3 (α=0.25):
  - GPU: cuda:1, 利用率 46%, 14.4GB/98GB
  - 进程: PID 53074, 已运行 2h29m
  - 进度: gen 5/10 完成，gen 6 刚开始
  - 每 gen 约 23.5 分钟
  - 预估剩余: ~1 小时 58 分钟（5 个 gen）
```

注：a000_s42 的输出目录是 `results/alpha_sweep/a000_s42/`，a025_s42 是 `results/alpha_sweep/a025_s42/`。两个实验的 `num_generations=10`，总共产生 gen_0 到 gen_10（gen_0 为初始轮）。

---
