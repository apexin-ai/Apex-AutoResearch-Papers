# 服务器原始数据审计报告

**服务器**: gpu-6000pro-2  
**提取日期**: 2026-05-25  
**项目路径**: `/root/autodl-tmp/recursive_gen_depth_est/`

---

## 目录结构

```
recursive_gen_depth_est/
├── data/           # 生成数据 (pythia, olmo, gpt2xl × nucleus/temp09/topk50, qwen, wild, etc.)
├── results/        # 实验结果
├── results_filtered/ # 过滤后结果 (pairwise_auc, feature_importance)
├── checkpoints/    # LoRA adapters (pythia, gpt2xl, olmo × depth 0-4)
├── artifacts/      # Atlas 分析产物
├── scripts/        # 训练和评估脚本
├── src/            # 核心代码
├── paper/          # 论文 LaTeX
├── figures/        # 图表
├── logs/           # 日志
├── models/         # 预训练模型缓存
└── runs/           # 训练 runs
```

---

## 结果文件清单

### 核心结果
- `artifacts/atlas_v2/atlas_v2_results.json` — 9-cell atlas 主结果
- `artifacts/atlas_v2/edd_analysis_9cell.json` — EDD 分析 + pairwise AUC (含 std)
- `artifacts/atlas_v2/feature_trajectory.json` — Feature trajectory per cell
- `artifacts/atlas_v2/cross_model_comparison.json` — Cross-model rank correlation
- `artifacts/atlas_v2/atlas_summary.json` — Atlas 汇总 (含 monotonicity, feature importance per cell)
- `results/bootstrap_ci_table1.json` — Bootstrap CI (10000 resample)
- `results/reviewer_metrics/bootstrap_ci_table1_v2.json` — Bootstrap CI v2 (含 d1d3 balanced acc)
- `results_filtered/pairwise_auc.json` — Pairwise AUC (Pythia nucleus, filtered data)
- `results_filtered/feature_importance.json` — RF feature importance (filtered)

### Baselines
- `results/detection_baselines_ordinal/results.json` — Binoculars + Fast-DetectGPT ordinal
- `results/reviewer_metrics/ppl_threshold_baseline.json` — PPL threshold vs RF

### Cross-model / Cross-scale
- `results/14b_cross_ref/14b_cross_ref_results.json` — Pythia→Qwen-14B cross-ref
- `results/qwen25_14b_temp09/summary.json` — Qwen-14B self-ref (temp09)
- `results/qwen25_7b_selfref/summary.json` — Qwen-7B self-ref
- `results/reviewer_metrics/d1d3_balanced_acc.json` — d1-d3 balanced acc + cross-model transfer

### Accumulation
- `results/accumulation_pairwise_auc.json` — Mix25/50 pairwise AUC
- `results/accum_mix50_pairwise_auc_verified.json` — Verified (500 tree) AUC
- `results/accumulation_v3/pythia_nucleus/mix50/summary.json`
- `results/accumulation_v3/olmo_temp09/mix50/summary.json`
- `results/accumulation_edd/edd_comparison.json` — Full-rep vs accum25 EDD comparison

### Wild Data / Calibration
- `results/wild_data_calibration_comprehensive/comprehensive_results.json`
- `results/fpr_coverage/summary.json` — FPR-coverage tradeoff

### Conditional PI
- `results/conditional_pi/summary.json` — Permutation importance (30 repeats × 1000 bootstrap)

---

## 关键指标提取

### Table 1 源数据: 9-Cell RF 4-Class Accuracy + d1-d3 Balanced Accuracy

源文件: `results/reviewer_metrics/bootstrap_ci_table1_v2.json` (n_bootstrap=1000, 95% CI)

| Cell | RF 4-Class Acc | 95% CI | d1-d3 Bal Acc | 95% CI | n_samples |
|------|---------------|--------|---------------|--------|-----------|
| pythia_nucleus | 0.7869 | [0.7808, 0.7923] | 0.7177 | [0.7101, 0.7248] | 20000 |
| pythia_temp09 | 0.7674 | [0.7615, 0.7736] | 0.6927 | [0.6851, 0.7001] | 20000 |
| pythia_topk50 | 0.6884 | [0.6815, 0.6941] | 0.5886 | [0.5812, 0.5963] | 20000 |
| olmo_nucleus | 0.7893 | [0.7839, 0.7946] | 0.7263 | [0.7195, 0.7333] | 20000 |
| olmo_temp09 | 0.8212 | [0.8158, 0.8268] | 0.7637 | [0.7571, 0.7704] | 20000 |
| olmo_topk50 | 0.7449 | [0.7390, 0.7508] | 0.6624 | [0.6553, 0.6700] | 20000 |
| gpt2xl_nucleus | 0.8411 | [0.8361, 0.8462] | 0.7936 | [0.7871, 0.8002] | 20000 |
| gpt2xl_temp09 | **0.8586** | [0.8543, 0.8631] | **0.8143** | [0.8083, 0.8205] | 20000 |
| gpt2xl_topk50 | 0.7593 | [0.7534, 0.7652] | 0.6836 | [0.6760, 0.6908] | 20000 |

**Summary**: mean RF acc = 0.7841, range [0.6884, 0.8586]; mean d1-d3 BA = 0.7159

### Per-Class Recall (d1/d2/d3)

源文件: `results/reviewer_metrics/d1d3_balanced_acc.json`

| Cell | d1 recall | d2 recall | d3 recall |
|------|-----------|-----------|-----------|
| pythia_nucleus | 0.8187 | 0.5867 | 0.7227 |
| pythia_temp09 | 0.8133 | 0.5387 | 0.7213 |
| pythia_topk50 | 0.7227 | 0.4560 | 0.5747 |
| olmo_nucleus | 0.8053 | 0.6147 | 0.7427 |
| olmo_temp09 | 0.8773 | 0.6613 | 0.7720 |
| olmo_topk50 | 0.7853 | 0.5120 | 0.6560 |
| gpt2xl_nucleus | 0.8587 | 0.7333 | 0.7747 |
| gpt2xl_temp09 | 0.9093 | 0.6880 | 0.8187 |
| gpt2xl_topk50 | 0.7947 | 0.5253 | 0.7107 |

---

### AUC Decay 源数据 (Pairwise AUC per 9-cell)

源文件: `artifacts/atlas_v2/edd_analysis_9cell.json`

| Cell | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD@T=0.70 |
|------|----------|----------|----------|------------|
| pythia_nucleus095 | 0.9995 ± 0.0005 | 0.9302 ± 0.0021 | 0.8130 ± 0.0054 | 3 |
| pythia_temp09 | 0.9997 ± 0.0003 | 0.9098 ± 0.0017 | 0.7953 ± 0.0043 | 3 |
| pythia_topk50 | 0.9990 ± 0.0004 | 0.8363 ± 0.0070 | 0.6865 ± 0.0038 | 2 |
| gpt2xl_nucleus095 | 0.9989 ± 0.0004 | 0.9584 ± 0.0027 | 0.8921 ± 0.0066 | 3 |
| gpt2xl_temp09 | 0.9996 ± 0.0001 | 0.9792 ± 0.0013 | 0.8861 ± 0.0021 | 3 |
| gpt2xl_topk50 | 0.9987 ± 0.0006 | 0.9140 ± 0.0017 | 0.7566 ± 0.0027 | 3 |
| olmo_nucleus095 | 0.9966 ± 0.0008 | 0.9341 ± 0.0032 | 0.8189 ± 0.0086 | 3 |
| olmo_temp09 | 0.9998 ± 0.0001 | 0.9558 ± 0.0029 | 0.8341 ± 0.0068 | 3 |
| olmo_topk50 | 0.9996 ± 0.0003 | 0.9042 ± 0.0050 | 0.7339 ± 0.0077 | 3 |

**EDD Summary**: 8/9 cells achieve EDD=3 at T=0.70; 1 cell (pythia_topk50, d2v3 AUC=0.6865 < 0.70) has EDD=2

Additional AUC from `results_filtered/pairwise_auc.json` (Pythia nucleus filtered, LR & RF):
| Pair | LR AUC | RF AUC |
|------|--------|--------|
| d0v1 | 0.9953 | 0.9977 |
| d0v2 | 0.9993 | 0.9988 |
| d0v3 | 0.9997 | 0.9995 |
| d1v2 | 0.8108 | 0.8782 |
| d1v3 | 0.9588 | 0.9774 |
| d2v3 | 0.7884 | 0.8323 |

---

### Cross-Model Rank Correlation (Spearman ρ)

源文件: `artifacts/atlas_v2/cross_model_comparison.json`

| Strategy | Pythia↔OLMo | Pythia↔GPT2XL | OLMo↔GPT2XL | Mean ρ |
|----------|-------------|---------------|--------------|--------|
| nucleus_p095 | 0.6459 (p=0.003) | 0.9035 (p<1e-6) | 0.8521 (p<1e-5) | 0.8005 |
| temperature_09 | 0.6263 (p=0.004) | 0.6529 (p=0.002) | 0.9592 (p<1e-6) | 0.7461 |
| topk_k50 | 0.7363 (p<0.001) | 0.7152 (p<0.001) | 0.9807 (p<1e-6) | 0.8107 |

---

### Cross-Model Transfer (Leave-One-Out)

源文件: `results/reviewer_metrics/d1d3_balanced_acc.json`

| Holdout Model | d1 recall | d2 recall | d3 recall | Bal Acc |
|---------------|-----------|-----------|-----------|---------|
| Pythia | 0.4930 | 0.2677 | 0.7363 | 0.4990 |
| OLMo | 0.7549 | 0.4327 | 0.5883 | 0.5920 |
| GPT-2 XL | 0.7465 | 0.5255 | 0.4450 | 0.5723 |

**Mean cross-model transfer**: 0.5544 (vs within-dist: 0.7109)

---

### 14B Scale Results

源文件: `results/14b_cross_ref/14b_cross_ref_results.json`

#### Qwen2.5-14B with Pythia-1.4B features (cross-reference)

| Strategy | 4-class Acc | d1-d3 Bal Acc | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD@T=0.70 |
|----------|-------------|---------------|----------|----------|----------|------------|
| nucleus | 0.4497 | 0.3947 | 0.7016 | 0.7308 | 0.5987 | 2 |
| temp09 | 0.4633 | 0.4029 | 0.7392 | 0.7238 | 0.6145 | 2 |
| topk50 | 0.4085 | 0.3527 | 0.6990 | 0.6810 | 0.5415 | 0 |

#### Self-Reference Comparison

| Strategy | Cross-ref (Pythia feat) | Self-ref (Qwen feat) | Delta |
|----------|------------------------|---------------------|-------|
| nucleus | 0.4497 | 0.5405 | -0.0908 |
| temp09 | 0.4633 | 0.5050 | -0.0417 |
| topk50 | 0.4085 | 0.4793 | -0.0708 |

#### Qwen2.5-14B Self-Reference (temp09)

源文件: `results/qwen25_14b_temp09/summary.json`

- RF 4-class acc: 0.505 [0.4976, 0.5124]
- Top5 features: p90_ppl, skew_ppl, kurt_ppl, p90_surprisal, var_surprisal

#### Qwen2.5-7B Self-Reference

源文件: `results/qwen25_7b_selfref/summary.json`

- RF 4-class acc: 0.5205 [0.5135, 0.5271]
- Top5 features: p90_ppl, skew_ppl, p90_surprisal, kurt_ppl, var_surprisal

---

### Baseline Comparison (Detection Baselines Ordinal)

源文件: `results/detection_baselines_ordinal/results.json`

| Cell | Binoculars LR 4-class | Fast-DetectGPT LR 4-class | Combined LR 4-class | RF (Ours) |
|------|----------------------|--------------------------|---------------------|-----------|
| pythia_nucleus | 0.3761 | 0.3950 | 0.5132 | 0.7869 |
| pythia_temp09 | 0.3863 | 0.3865 | — | 0.7674 |
| pythia_topk50 | — | — | — | 0.6884 |
| gpt2xl_nucleus | 0.5002 | 0.6136 | 0.6213 | 0.8411 |
| gpt2xl_temp09 | — | — | — | 0.8586 |
| gpt2xl_topk50 | 0.4808 | 0.5467 | 0.5632 | 0.7593 |

#### PPL Threshold vs RF (Binary d0/d1+)

源文件: `results/reviewer_metrics/ppl_threshold_baseline.json`

| Method | Precision | Recall | F1 | AUC |
|--------|-----------|--------|-----|-----|
| PPL threshold (Youden) | 0.9893 | 0.7366 | 0.8445 | 0.8521 |
| RF depth filter (19 feat) | 0.9988 | 0.9951 | 0.9970 | 0.9998 |

**Gap**: RF outperforms PPL threshold by +0.1525 F1, +0.1477 AUC

---

### Feature Importance (Universal Ranking across 9 cells)

源文件: `results_filtered/feature_importance.json` + `artifacts/atlas_v2/feature_trajectory.json`

| Rank | Feature | Mean Importance | CV (consistency) |
|------|---------|-----------------|------------------|
| 1 | p90_ppl | 0.1946 | 0.2075 |
| 2 | var_surprisal | 0.1612 | 0.1932 |
| 3 | p75_ppl | 0.1025 | 0.2852 |
| 4 | mean_surprisal | 0.0969 | 0.2284 |
| 5 | mean_ppl | 0.0510 | 0.9763 |
| 6 | p50_ppl | 0.0429 | 0.1544 |
| 7 | type_token_ratio | 0.0418 | 0.2081 |
| 8 | p25_ppl | 0.0353 | 0.1607 |
| 9 | hapax_ratio | 0.0348 | 0.1835 |
| 10 | entropy_of_surprisal | 0.0329 | 0.1228 |

**Top-2 consistency**: p90_ppl appears in top-2 of 9/9 cells; var_surprisal in 7/9 cells.

#### Conditional Permutation Importance (Rank-based)

源文件: `results/conditional_pi/summary.json`

| Family | Mean PI | Avg Rank |
|--------|---------|----------|
| surprisal (var + mean + entropy) | 0.0890 | 7.33 |
| perplexity (9 features) | 0.0388 | 7.52 |
| lexical (TTR + hapax) | 0.0043 | 9.72 |
| ngram_entropy | 0.0013 | 15.67 |
| repetition (2/3/4-gram) | 0.0007 | 16.52 |

---

### Accumulation (Mixed-Depth Corpus)

源文件: `results/accumulation_pairwise_auc.json`, `results/accum_mix50_pairwise_auc_verified.json`

#### Mix25 (25% accumulation in each depth)

| Cell | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD@0.70 |
|------|----------|----------|----------|----------|
| gpt2xl_nuc | 0.9995 | 0.8168 | 0.7258 | 3 |
| pythia_nuc | 0.9998 | 0.8090 | 0.7486 | 3 |
| olmo_temp | 1.0000 | 0.8481 | 0.7585 | 3 |

#### Mix50 (50% accumulation) — Verified with 500 trees

| Cell | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD@0.70 |
|------|----------|----------|----------|----------|
| gpt2xl_nuc | 0.9996 | 0.8305 | 0.6945 | 2 |
| pythia_nuc | 0.9999 | 0.7925 | 0.7159 | 3 |
| olmo_temp | 0.9999 | 0.8166 | 0.7262 | 3 |

#### Full-Rep vs Accum25 EDD Comparison

源文件: `results/accumulation_edd/edd_comparison.json`

| Cell | Type | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD@0.70 |
|------|------|----------|----------|----------|----------|
| GPT-2 XL nucleus | full-rep | 0.9941 | 0.9131 | 0.8829 | 3 |
| GPT-2 XL nucleus | accum25 | 0.9995 | 0.8168 | 0.7258 | 3 |
| OLMo temp09 | full-rep | 0.9960 | 0.9010 | 0.8214 | 3 |
| OLMo temp09 | accum25 | 1.0000 | 0.8481 | 0.7585 | 3 |
| Pythia nucleus | full-rep | 0.9975 | 0.8607 | 0.8005 | 3 |
| Pythia nucleus | accum25 | 0.9998 | 0.8090 | 0.7486 | 3 |

#### Accumulation v3 — Mix50 Detailed

**Pythia nucleus mix50** (源: `results/accumulation_v3/pythia_nucleus/mix50/summary.json`)
- Overall acc: 0.6865, d1-d3 bal acc: 0.5834
- Per-class: d0=0.996, d1=0.692, d2=0.417, d3=0.641
- Full-rep baseline: 0.8428; delta: -0.1563

**OLMo temp09 mix50** (源: `results/accumulation_v3/olmo_temp09/mix50/summary.json`)
- Overall acc: 0.7023, d1-d3 bal acc: 0.6039
- Per-class: d0=0.997, d1=0.725, d2=0.412, d3=0.674

---

### Wild Data Calibration / FPR

源文件: `results/wild_data_calibration_comprehensive/comprehensive_results.json`

#### Base FPR (argmax prediction on known-human corpora)

| Corpus | d0 Rate | FPR (d1+) |
|--------|---------|-----------|
| C4 (10k) | 65.98% | **34.02%** |
| FineWeb (10k) | 82.85% | 17.15% |
| RedPajama (10k) | 84.47% | 15.53% |

**注意 (C004)**: 这些 FPR 是 OOD 假阳性率，不反映真实 AI 内容占比。

#### Threshold Sweep — C4

| P(d0) threshold | FPR | Coverage |
|-----------------|-----|----------|
| 0.05 | 0.23% | 99.77% |
| 0.10 | 0.89% | 99.11% |
| 0.15 | 6.71% | 93.29% |
| 0.20 | 22.38% | 77.62% |

#### FPR-Coverage Tradeoff (Controlled CV)

源文件: `results/fpr_coverage/summary.json`

| Confidence Threshold | d1-d3 Bal Acc | Coverage |
|---------------------|---------------|----------|
| 0.50 | 0.7695 | 88.16% |
| 0.60 | 0.8205 | 73.91% |
| 0.70 | 0.8575 | 61.33% |
| 0.80 | 0.8806 | 49.50% |
| 0.90 | 0.8927 | 38.92% |

---

### LoRA 训练配置

源文件: `checkpoints/lora_depth_0/adapter_config.json` + `scripts/lora_finetune.py` + `checkpoints/lora_depth_0/checkpoint-939/trainer_state.json`

| 参数 | 值 |
|------|-----|
| Base Model | Pythia-1.4B (`/root/autodl-tmp/models/pythia-1.4b`) |
| LoRA rank (r) | 16 |
| LoRA alpha | 32 |
| LoRA dropout | 0.05 |
| Target modules | `query_key_value` |
| Task type | CAUSAL_LM |
| Bias | none |
| Learning rate | 2e-4 (linear decay) |
| Batch size | 8 |
| Gradient accumulation | 2 (effective batch = 16) |
| Epochs | 3 |
| Max sequence length | 512 |
| Precision | bf16 |
| Optimizer | AdamW (default) |
| Scheduler | linear (default) |
| Total steps | 939 |
| Seed | 42 |
| Save strategy | epoch |
| Dataloader workers | 4 |

**Training loss**: Start ~2.32, End ~2.21 (depth_0)

---

### 附加数据

#### Single-Feature AUC (Binary d0/d1+)

源文件: `results/reviewer_metrics/ppl_threshold_baseline.json`

| Feature | AUC |
|---------|-----|
| p90_ppl | 0.986 |
| var_surprisal | 0.976 |
| mean_surprisal | 0.930 |
| p75_ppl | 0.916 |
| type_token_ratio | 0.891 |

#### PCA Variance Explained

源文件: `artifacts/atlas_v2/atlas_summary.json`

- PC1: 67.67%
- PC2: 15.29%
- Cumulative (PC1+PC2): 82.96%

#### Monotonicity (Spearman τ with depth for key features)

GPT-2 XL temp09 shows perfect -1.0 monotonicity for: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl, p25-p90_ppl, mean_surprisal, var_surprisal, entropy_of_surprisal, type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy; +1.0 for rep_2/3/4gram.

---

## 数据完整性说明

1. 所有 9 cells 均有 20000 samples (5000 per depth × 4 depths)
2. Bootstrap CI 使用 n=1000 (v2) 或 n=10000 (v1) resamples
3. RF 使用 200 trees, 5-fold stratified CV (除 baseline_battery 使用 100 trees single split)
4. Conditional PI 使用 200 trees main, 30 repeats; 100 trees boot, 10 repeats, 1000 bootstrap
5. Feature extraction 基于 Pythia-1.4B perplexity (self-reference model)
6. LoRA checkpoints 存在于 pythia depth 0-2, gpt2xl depth 0-4, olmo depth 0-4
