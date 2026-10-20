# monitor exp 003 gen2

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_003_gen2_20260517T113921_result.json`
- **Structured JSON:** [`765b44804abcba3f8f2f.json`](../../sessions/76/765b44804abcba3f8f2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_003 (Phase 1 Adaptive) 状态报告

### 当前进度
- **Gen 2 未完成**，正在生成合成样本：**48,640 / 50,000** (97.3%)
- 生成完成后还需要 training + evaluation 两个阶段
- PID 88156 正常运行

### 已有结果

| Gen | eff_rank | log_det | ppl | distinct4 | mix_ratio | train_loss |
|-----|----------|---------|-----|-----------|-----------|------------|
| 0 | 417.55 | 2366.68 | 9.55 | 0.7414 | — | — |
| 1 | 479.49 | 2356.68 | 10.01 | 0.7108 | **0.5** | 1.983 |

### Controller 分析

**Gen 0→1 delta:**
- `(2366.68 - 2356.68) / 2366.68 = 0.00423`
- **0.00423 < τ=0.005 → 未触发**
- Gen 1 mix_ratio = 0.5（默认值，未干预）

**Gen 2 的 mix_ratio：** 由于 Gen 0→1 delta 未达阈值，Gen 2 应仍以 **mix_ratio=0.5** 训练（controller 未触发调整）。日志中无 controller 状态输出，代码可能没有显式 log 决策过程。

### 预警

连续两代 delta 未达 τ=0.005 的趋势值得关注。log_det 从 2366.68 降到 2356.68，衰减速率缓慢。可能原因：
1. τ=0.005 阈值设得偏高，导致 controller 迟迟不触发
2. Pythia-410m 在 mix_ratio=0.5 下 spectral collapse 进展缓慢，需要更多 generation 才能累积到阈值

Gen 2 结果出来后才能判断 Gen 1→2 delta 是否加速。如果 Gen 2 的 log_det 继续缓慢下降（delta 仍 < 0.005），controller 可能到很晚的 generation 才触发，影响实验效率。

### 预估完成时间
生成阶段约 5 分钟内完成，加上 training + evaluation，Gen 2 整体预计 **30-60 分钟**后完成。

---
