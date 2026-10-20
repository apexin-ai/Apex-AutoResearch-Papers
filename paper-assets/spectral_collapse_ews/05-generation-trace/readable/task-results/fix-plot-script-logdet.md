# fix plot script logdet

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plot_script_logdet_20260516T223634_result.json`
- **Structured JSON:** [`ced46c962f8147690e14.json`](../../sessions/ce/ced46c962f8147690e14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**修改摘要：**
1. `results/phase0_results.json` — 回填了 Gen 0-2 的 `log_det` 字段（2366.68, 2464.76, 2469.93），Gen 3 已有值保持不变
2. `scripts/plot_spectral_trajectory.py` — 阈值从 `len(records) > 4` 改为 `len(records) >= 1`

**验证结果：**
- 绘图脚本正常执行，PDF/PNG 已生成
- log_det panel Gen 0-3 数据完整：2366.68 → 2464.76 → 2469.93 → 2440.57（Gen 2 峰值后回落，与 effective_rank 趋势一致）

---
