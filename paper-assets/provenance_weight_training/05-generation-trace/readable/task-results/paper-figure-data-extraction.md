# paper figure data extraction

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_figure-data-extraction_20260515T221834_result.json`
- **Structured JSON:** [`f971ad5bb75295bb0f43.json`](../../sessions/f9/f971ad5bb75295bb0f43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出全部注册完成。

## 提取结果汇总

### 产出文件（服务器 `/root/provenance_weight_training/artifacts/figure_data/`）

| 文件 | 内容 |
|------|------|
| `bstar_trajectory_seed42.csv` | 24412 行 per-batch 数据（step, b_star, alpha_eff, ess, regime） |
| `binding_stats_seed42.json` | binding regime 汇总统计 |
| `tau_sweep_summary.json` + `.csv` | 6 个 tau 值的 mean b* 和 mean α_eff |

### adaptive_fix_seed42 binding 分布（去重后 24412 micro-batches）

| Regime | Count | Pct | Mean b* | Mean α_eff | Mean ESS |
|--------|-------|-----|---------|------------|----------|
| clean | 467 | 1.91% | 0.0 | 0.860 | 4.069 |
| alpha_eff_binding | 9351 | 38.3% | 1.111 | 0.800 | 2.796 |
| ess_binding | 14594 | 59.8% | 1.626 | 0.551 | 2.017 |

### tau sweep

| τ | mean b* | mean α_eff |
|---|---------|------------|
| 0.5 | 0.39 | 0.50 |
| 0.6 | 0.59 | 0.55 |
| 0.7 | 0.89 | 0.61 |
| 0.8 | 1.40 | 0.65 |
| 0.9 | 2.36 | 0.68 |
| 0.95 | 3.08 | 0.69 |

### 关于与预期数据的偏差

原始 `step_metrics.jsonl` 有 51913 行，包含多次重启的重复数据（checkpoint step 500/1000/1500 各有 ~8000+ 条 dump entries）。任务中给出的参考统计（49.9% clean）是基于未去重的原始数据。去重后的 24412 行是实际的 unique micro-batch 观测值，binding 分布是准确的：ESS binding 占主导（59.8%），因为 batch_size=4 + contamination_ratio=0.4 下，大多数 batch 的 ESS 在 b* 达到 τ 阈值前就触底了。

---
