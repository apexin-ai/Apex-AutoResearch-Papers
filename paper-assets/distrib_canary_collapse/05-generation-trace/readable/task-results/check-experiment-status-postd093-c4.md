# check experiment status postd093 c4

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_experiment_status_postd093_c4_20260520T030356_result.json`
- **Structured JSON:** [`bc41287bb1aa091da029.json`](../../sessions/bc/bc41287bb1aa091da029.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部查清。

## 结果

### 实验 1: alpha_sweep_a050_postd093_s42_fp32 (westd-17855)
- **状态: COMPLETED (训练完成，分析未运行)**
- EXIT_CODE = 0
- gen_0 ~ gen_10 全部完成，`all_metrics.json` 已写入
- 最后一代指标：ppl=32.62, entropy=2.6206, eff_rank=59.7, mauve=0.0245
- **缺失：没有 `analysis/` 目录，`5method_leadlag.json` 不存在** — 需要单独跑 analysis 步骤
- 结果路径：`/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_postd093_s42_fp32/`

### 实验 2: c4_a075_s43_fp32 (westd-19828)
- **状态: COMPLETED**
- `analysis/5method_leadlag.json` 存在
- 结果路径：`/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a075_s43/analysis/`

### 实验 3: c4_a050_s43_fp32 (westd-19828)
- **状态: COMPLETED**
- `analysis/5method_leadlag.json` 存在
- 结果路径：`/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s43/analysis/`

---

**需要操作**: 实验 1 训练已成功完成但 analysis 管道未执行，需要对 `a050_postd093_s42_fp32` 补跑 analysis 生成 `5method_leadlag.json`。

---
