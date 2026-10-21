# analysis rho06 mechanism data

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rho06_mechanism_data_20260518T040915_result.json`
- **Structured JSON:** [`faef05002ae993867648.json`](../../sessions/fa/faef05002ae993867648.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成。

## 关键发现

### ρ=0.6 adaptive (τ=0.8 fixed)
- **b\* 分布**：mean=1.37 ± 1.90, median=0.86, 右偏分布 (p5=0.28, p95=3.86)
- **α_eff binding rate**：33.4% — 约 1/3 的 batch 触及 τ=0.8 上界
- **ESS/B**：mean=0.576 ± 0.13 — 有效样本量约为 batch size 的 58%
- **b\* 趋势平稳**：训练期间无明显 drift (step 0-500: 1.375 → step 6000+: 1.301)
- **mean_q**：0.624（ρ=0.6 数据中合成样本的高 q-score 拉高了均值）

### vs ρ=0.2 对比
| 指标 | ρ=0.6 | ρ=0.2 |
|---|---|---|
| b\* mean | 1.37 | 1.73 |
| α_eff binding rate | 33.4% | 60.0% |
| ESS/B mean | 0.576 | 0.734 |
| mean_q | 0.624 | 0.393 |

ρ=0.6 下 b\* 更小（更温和的下加权）、binding rate 更低（α_eff 约束更少触顶）、ESS/B 更低（更激进地丢弃有效样本）。这符合预期：高污染率下 batch 中 synthetic 样本占比高，mean_q 大，需要更大的差异化权重。

### 文件位置
- 完整 JSON：`westd-30476:/root/provenance_weight_training/analysis/rho06_mechanism_data.json` (85KB，含 histogram、per-window trend、全部分布数据)
- 摘要：`artifacts/rho06_mechanism_summary.json`
- 分析脚本：`westd-30476:/root/provenance_weight_training/analysis/analyze_rho06_mechanism.py`

---
