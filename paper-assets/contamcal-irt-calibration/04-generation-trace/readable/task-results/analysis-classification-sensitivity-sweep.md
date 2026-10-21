# analysis classification sensitivity sweep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_classification-sensitivity-sweep_20260519T185355_result.json`
- **Structured JSON:** [`b36b0d920f96709146fa.json`](../../sessions/b3/b36b0d920f96709146fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报结果：

## Classification Sensitivity Sweep 结果

**30 个 (τ, σ) 组合的分类结果：**

| Model | 稳定性 | 详情 |
|-------|--------|------|
| **Phi-4** | ROBUST | 30/30 = Immune |
| **Qwen2.5-14B** | ROBUST | 30/30 = U-collapse |
| **Qwen2.5-7B** | SENSITIVE | 25/30 V-recovery, 5/30 Immune |
| **Gemma-2-9B** | ROBUST | 30/30 = Benefit |
| **OLMo-2-7B** | ROBUST | 30/30 = Benefit-sat |

**关键发现：**

- **4/5 family 完全稳定**——在所有 30 种阈值组合下分类不变
- **Qwen2.5-7B 是唯一 sensitive case**，仅在 τ=2.0（最宽松 noise band）时从 V-recovery 翻转为 Immune。这符合预期：其 delta = -1.78pp，恰好在 noise/recovery 边界附近
- σ 的变化对所有 model 的分类**零影响**（因为没有 model 的 delta 在 -3pp ~ -7pp 范围内翻转）
- **25/30 组合 5 个 model 全部一致，30/30 组合至少 4/5 一致**

这个结果对审稿人很有说服力——分类对阈值选择高度 robust。

**输出文件：**
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_agreement_heatmap.pdf` — 总体一致性热力图
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_permodel_heatmap.pdf` — 5 个 model 分别的分类热力图
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_matrix.json` — 完整分类数据
- `/root/contamcal-irt-calibration/analysis/results/sensitivity/sensitivity_summary.txt` — 文本摘要

---
