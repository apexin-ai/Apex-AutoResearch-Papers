# check phase0 progress 0517

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phase0_progress_0517_20260517T020650_result.json`
- **Structured JSON:** [`ab43619815e686b13441.json`](../../sessions/ab/ab43619815e686b13441.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

---

### exp_001 (125M) — Phase 0

**已完成 Gen 0-4，当前正在跑 Gen 5（生成阶段 ~5440/50000）**

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | σ₁ |
|-----|----------|---------|-----|-----------|------------|-----|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | — | 1942.82 |
| 1 | 491.77 | 2464.76 | 11.38 | 0.6256 | 1.623 | 803.96 |
| 2 | 496.44 | 2469.93 | 13.58 | 0.5154 | 1.268 | 712.03 |
| 3 | 493.31 | 2440.57 | 16.25 | 0.4900 | 1.134 | 700.68 |
| 4 | 485.67 | 2405.05 | 19.80 | 0.4679 | 1.098 | 729.59 |

趋势：ppl 持续上升（9.55→19.80），distinct4 持续下降（0.74→0.47），eff_rank 在 Gen 1-2 上升后 Gen 3-4 开始下降，log_det 同步下降。collapse 信号明显。

---

### exp_002 (1B) — Phase 0

**已完成 Gen 0-2，当前正在跑 Gen 3（生成阶段 ~4800/50000）**

| Gen | eff_rank | log_det | ppl | distinct4 | train_loss | σ₁ |
|-----|----------|---------|-----|-----------|------------|-----|
| 0 | 516.14 | 2835.32 | 8.07 | 0.7510 | — | 1661.24 |
| 1 | 570.75 | 2905.74 | 9.41 | 0.6335 | 1.530 | 1052.79 |
| 2 | 580.92 | 2893.85 | 11.04 | 0.5382 | 1.218 | 916.30 |

趋势：ppl 上升（8.07→11.04），distinct4 下降（0.75→0.54），但 eff_rank 仍在上升（516→581），log_det Gen 2 略降。1B 模型退化速度比 125M 慢。

---

### 进程状态

| 实验 | PID | GPU | CPU | 状态 |
|------|-----|-----|-----|------|
| exp_001 (resume_from_gen 4) | 59365 | GPU 0 | 100% | Running, Gen 5 生成中 |
| exp_002 (1B) | 25237 | GPU 1 | 74.6% | Running, Gen 3 生成中 |

---

### GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| 0 | 94% | 65909 MiB |
| 1 | 90% | 39771 MiB |

---

### 磁盘状态

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| / | 30G | 25G | 5.1G | 84% |
| /root/autodl-tmp | 250G | 111G | 140G | 45% |

根分区 84% 需关注，但 autodl-tmp 空间充裕。

---
