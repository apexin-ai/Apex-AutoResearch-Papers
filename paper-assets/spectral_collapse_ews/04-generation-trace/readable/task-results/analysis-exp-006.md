# analysis exp 006

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_006_20260518T084811_result.json`
- **Structured JSON:** [`3cd69dd1b87eca0b6424.json`](../../sessions/3c/3cd69dd1b87eca0b6424.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. exp_006 marked DONE (negative).

## exp_006 完整结果

| Gen | eff_rank | log_det | ppl | distinct4 | mix_ratio | triggered | train_loss |
|-----|----------|---------|------|-----------|-----------|-----------|------------|
| 0 | 417.55 | 2366.68 | 9.554 | 0.7414 | — | — | — |
| 1 | 477.31 | 2365.10 | 10.089 | 0.7099 | 0.5 | false | 1.984 |
| 2 | 487.08 | 2394.01 | 10.416 | 0.5995 | 0.5 | false | 1.934 |
| 3 | 496.03 | 2423.83 | 10.760 | 0.4898 | 0.5 | false | 1.752 |
| 4 | 501.19 | 2448.26 | 11.135 | 0.4304 | 0.5 | false | 1.572 |
| 5 | 512.50 | 2488.08 | 11.643 | 0.3730 | 0.5 | false | 1.467 |
| 6 | 518.89 | 2507.62 | 12.144 | 0.3556 | 0.5 | false | 1.325 |
| 7 | 526.89 | 2526.19 | 12.723 | 0.2905 | 0.5 | false | 1.251 |
| 8 | 535.30 | 2542.89 | 13.397 | 0.2558 | 0.5 | false | 1.149 |
| 9 | 544.50 | 2560.14 | 14.159 | 0.2260 | 0.5 | false | 1.062 |
| 10 | 553.76 | 2572.22 | 15.100 | 0.2388 | 0.5 | false | 0.991 |

### Controller 分析

- **从未触发**。mix_ratio 全程锁定 0.5（默认值），controller_ratio = 0.5 × 10 gen。
- log_det per-gen delta 趋势：
  - Gen 0→1: **-1.58**（微降）, 1→2: +28.9, 2→3: +29.8, 3→4: +24.4, 4→5: +39.8, 5→6: +19.5, 6→7: +18.6, 7→8: +16.7, 8→9: +17.3, 9→10: +12.1
  - Delta 单调递减（从 ~30 降到 ~12），始终不够触发 tau=0.002 阈值。无拐点。

### 结论：**NEGATIVE**

假设被证伪：k=10 + tau=0.002 + per_gen mode 未能产生预期的 0.55-0.65 mix ratio 调节。原因是 per-gen log_det delta 归一化后远低于阈值，controller 形同虚设。

这是一个 **有价值的 negative result**：与 exp_005（k=20，过早耗尽 budget）形成两极，共同说明 per_gen mode 下 log_det signal 的 delta 要么太小不触发（k=10），要么一旦触发就因高 gain 快速耗尽（k=20）。支持论文的 signal-decay paradox / r_crit claim。

### Checkpoints

所有 11 个 generation（gen_0 到 gen_10）checkpoint 完整存在。

---
