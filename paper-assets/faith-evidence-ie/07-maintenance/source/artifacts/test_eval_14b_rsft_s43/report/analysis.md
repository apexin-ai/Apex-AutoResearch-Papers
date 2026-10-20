# 14B RSFT s43 Test Eval Analysis

## 1. Experiment Results

### test_eval_14b_rsft_s43_with_evi

| Metric | Value |
|--------|-------|
| Ign-F1 | 0.3767 |
| F1 | 0.3767 |
| Precision | 0.4252 |
| Recall | 0.3382 |
| Evi-F1 (DREEAM) | 0.2468 |
| Evi-F1 (TP) | 0.5836 |
| EDCR | 0.8340 |
| Documents | 500 |
| Predictions | 22861 |
| Format OK | 498/500 |
| Truncated | 271/500 (54.2%) |
| Inference Time | 6583.2s (13.17 s/doc) |
| CodaLab Converted | 13323 |

### test_eval_14b_rsft_s43_no_evi

| Metric | Value |
|--------|-------|
| Ign-F1 | 0.3775 |
| F1 | 0.3775 |
| Precision | 0.4138 |
| Recall | 0.3470 |
| Documents | 500 |
| Predictions | 31216 |
| Format OK | 499/500 |
| Truncated | 292/500 (58.4%) |
| Inference Time | 6554.6s (13.11 s/doc) |
| CodaLab Converted | 14066 |

## 2. Evidence Tax (s43)

- with-evi Ign-F1: 0.3767
- no-evi Ign-F1: 0.3775
- **Evidence tax: +0.08pp** (no-evi marginally better)

s43 evidence tax 接近零，远小于 s42 的 +0.77pp。

## 3. 14B 2-Seed Reproducibility (s42 vs s43)

### with-evi Ign-F1

| Seed | Ign-F1 |
|------|--------|
| s42 | 0.3849 |
| s43 | 0.3767 |
| **Mean** | **0.3808** |
| **Std** | **0.0058** |

s43 比 s42 低 0.82pp，seed 间方差偏大。

### no-evi Ign-F1

| Seed | Ign-F1 |
|------|--------|
| s42 | 0.3926 |
| s43 | 0.3775 |
| **Mean** | **0.3851** |
| **Std** | **0.0107** |

no-evi seed 间差异更大（1.51pp），s43 显著低于 s42。

### Evidence Tax

| Seed | Tax (pp) |
|------|----------|
| s42 | +0.77 |
| s43 | +0.08 |
| **Mean** | **+0.42** |
| **Std** | **0.49** |

14B evidence tax = **+0.42 +/- 0.49pp (n=2)**，正方向但置信区间跨零。

## 4. Full-Scale Evidence Tax Summary (Test Set)

| Scale | Tax Mean (pp) | Tax Std | n | Direction | Individual Seeds |
|-------|--------------|---------|---|-----------|-----------------|
| 4B (Qwen3) | +1.65 | 0.29 | 3 | positive (no-evi better) | — |
| 8B (Qwen3) | -0.91 | 0.74 | 3 | negative (with-evi better) | — |
| **14B (Qwen3)** | **+0.42** | **0.49** | **2** | **ambiguous** | s42=+0.77, s43=+0.08 |
| LLaMA-8B | -1.46 | 0.40 | 2 | negative (with-evi better) | — |

## 5. Key Observations

1. **14B evidence tax 不显著**：+0.42pp mean，但 std=0.49pp，置信区间 [-0.07, +0.91] 跨零。2 个 seed 结果差异大（+0.77 vs +0.08），无法确定方向。

2. **14B seed 方差偏大**：with-evi std=0.58pp, no-evi std=1.07pp，均高于同 scale 的预期。s43 整体表现低于 s42（with-evi 低 0.82pp，no-evi 低 1.51pp）。

3. **Scale 趋势**：4B 有明确正 tax（evidence 是负担），8B 和 LLaMA 有明确负 tax（evidence 有帮助），14B 处于中间位置。这与"更大模型更能利用 evidence"的假设部分一致——从 4B 到 8B tax 从正变负——但 14B 又回弹到接近零，可能表明 14B 的 evidence 利用能力不如 8B。

4. **CodaLab 文件已生成**：两个实验均已生成 `codalab_submission.json`，可提交官方评测。
