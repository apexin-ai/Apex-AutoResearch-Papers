# code analysis heatmap

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis_heatmap_20260512T172509_result.json`
- **Structured JSON:** [`6c0cf6d732c05e6b07e5.json`](../../sessions/6c/6c0cf6d732c05e6b07e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部任务完成。结果汇总：

---

### a. Per-layer EMA score 统计摘要

| gamma | 全局 mean | 层间 std | min score | max score |
|-------|----------|---------|-----------|-----------|
| 0.5   | 0.5991   | 0.0534  | -0.1962   | 1.0000    |
| 0.7   | 0.5961   | 0.0501  | -0.1962   | 1.0000    |
| 0.9   | 0.5765   | 0.0381  | -0.1962   | 1.0000    |

gamma 越大，层间方差越小（0.0534→0.0381），符合 EMA 平滑效应。

### b. Per-layer 差异观察

**EMA 信号最强层（mean 最高）**: layers [31, 18, 19, 30, 35] — 集中在中间偏上层，三个 gamma 值一致。

**EMA 信号最弱层（mean 最低）**: layers [4, 3, 2, 1, 5/11] — 浅层 EMA 信号弱，说明浅层 KV representation 变化大、centroid 不稳定。

关键发现：
- 浅层 (0-5) EMA mean ~0.45-0.55，std 小，range 窄 → KV 表示不太冗余
- 中层 (16-35) EMA mean ~0.60-0.66，std 大，range 宽（甚至出现负值）→ 冗余信号最强但也最不稳定
- 深层 (40-47) EMA mean 回落到 ~0.54-0.57 → 中等冗余

### c. Heatmap 文件路径

| 文件 | 路径 |
|------|------|
| gamma=0.5 heatmap | `/root/carc/results/ema_heatmap_gamma05.pdf` |
| gamma=0.7 heatmap | `/root/carc/results/ema_heatmap_gamma07.pdf` |
| gamma=0.9 heatmap | `/root/carc/results/ema_heatmap_gamma09.pdf` |
| 三 gamma 对比图 | `/root/carc/results/ema_heatmap_comparison.pdf` |
| 原始数据 | `/root/carc/results/heatmap_data.pt` |

### d. composite_signal_test.py dry-run

通过。输出 shape `torch.Size([1024])`，score range `[0.0016, 0.9690]`。

文件位于 `/root/carc/composite_signal_test.py`。

---
