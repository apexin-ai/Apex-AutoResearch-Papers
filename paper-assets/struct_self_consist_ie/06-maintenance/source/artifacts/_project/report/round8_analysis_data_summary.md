# Round 8 Analysis Data Summary

拉取时间: 2026-05-15

---

## 1. SJ Union vs Max Normalizer 对比

### SciERC (Qwen SciERC NER N=8 seed42, n=529)

| Normalizer | Spearman ρ | p-value | AUROC | mean SJ | std SJ |
|------------|-----------|---------|-------|---------|--------|
| SJ_max | 0.3599 | 1.28e-17 | 0.7180 | 0.7026 | 0.1956 |
| SJ_union | 0.3650 | 4.11e-18 | 0.7154 | 0.6918 | 0.1977 |

- **Δρ = +0.0051** (union略高)，ΔAUROC = −0.0025 (max略高)
- 结论：两种 normalizer 差异极小，ρ 差 <0.01

### CoNLL (LLaMA CoNLL NER N=8 seed42, n=2756)

| Normalizer | Spearman ρ | AUROC | mean SJ | std SJ |
|------------|-----------|-------|---------|--------|
| SJ_max | 0.4314 | 0.7039 | 0.9718 | 0.092 |
| SJ_union | 0.4318 | 0.7041 | 0.9709 | 0.0941 |

- **Δρ = +0.0004**，ΔAUROC = +0.0002
- 结论：CoNLL 上两种 normalizer 几乎完全一致

**跨数据集总结：SJ_union 与 SJ_max 的 Spearman ρ 差异在两个数据集上均 < 0.01，可互换使用。**

---

## 2. Seed 456 LP Range Analysis

数据来源: Qwen SciERC joint N=8, n_valid=529

| Metric | seed42 | seed456 |
|--------|--------|---------|
| median LP range | **0.0401** | **0.0396** |
| IQR_25 | 0.0265 | 0.0236 |
| IQR_75 | 0.0685 | 0.0733 |
| IQR | 0.0421 | 0.0498 |
| tied_fraction (ε=0.05) | **60.3%** | **62.2%** |
| mean LP range | 0.0622 | 0.0567 |
| std LP range | 0.0691 | 0.0522 |

**关键数值（Paper Agent 直接引用）：**
- seed456: median = 0.040, IQR = [0.024, 0.073], tied = 62.2%
- seed42: median = 0.040, IQR = [0.026, 0.069], tied = 60.3%
- 两个 seed 高度一致，证实 LP range 窄 + tied fraction 高的现象具有跨 seed 鲁棒性

---

## 3. Table 2 Selection F1 — NER (unified pipeline, 2-seed mean, seeds 42+123)

配置: Qwen SciERC NER N=8

| Signal | Selection F1 | ΔF1 vs Greedy | combined_p |
|--------|-------------|---------------|------------|
| Greedy | 0.6448 | — | — |
| Random | 0.6101 | −0.0347 | — |
| **LP** | **0.6468** | **+0.0020** | 0.289 |
| **SJ** | **0.6462** | **+0.0014** | 0.675 |
| **FK** | **0.6458** | **+0.0010** | 0.793 |
| EM | 0.6371 | −0.0077 | 0.450 |
| VC | 0.6230 | −0.0218 | 0.259 |
| Oracle | 0.7781 | +0.1333 | — |

Per-seed 数据:
- LP: seed42=0.6501, seed123=0.6436
- SJ: seed42=0.6450, seed123=0.6475
- FK: seed42=0.6448, seed123=0.6468

### RE Selection F1 — 尚无 2-seed 统一数据

`selection_f1_table2.json` 仅包含 NER subtask。已有的 RE 数据：

**单 seed (seed42) RE Selection F1** (from `re_selection_recompute.json`, full_set n=397):

| Signal | Sel F1 | ΔF1 vs Greedy |
|--------|--------|---------------|
| Greedy | 0.4042 | — |
| Random | 0.3544 | −0.0498 |
| LP | 0.3948 | −0.0094 |
| VC | 0.3944 | −0.0099 |
| FK | 0.3872 | −0.0171 |
| SJ | 0.3855 | −0.0188 |
| EM | 0.3718 | −0.0324 |

**3-seed (42/123/456) RE N=16** (from `analysis_scierc_re_n16_3seed_selection_f1.json`):

| Signal | mean Sel F1 | mean ΔF1 |
|--------|-------------|----------|
| Greedy | 0.2914 | — |
| LP | **0.2988** | **+0.0073** |
| VC | 0.2837 | −0.0077 |
| FK | 0.2826 | −0.0088 |
| SJ | 0.2812 | −0.0102 |
| EM | 0.2768 | −0.0147 |

RE 上所有 structural signal (SJ/FK/VC/EM) 均低于 greedy，仅 LP 保持微正。

---

## 4. RE Seed123/Seed456 实验进度

**两组实验均已完成** (2026-05-15 23:45):

| 实验 | 文件 | 大小 |
|------|------|------|
| exp_re_scierc_seed123 | report.json + samples.jsonl | 3.7MB |
| exp_re_scierc_seed456 | report.json + samples.jsonl | 3.7MB |

### RE seed123 关键指标
- NER: greedy_f1 = 0.6635, ρ_SJ = 0.4036 (full), ρ_FK = 0.2818
- RE: greedy_f1 = 0.4200, ρ_SJ = 0.2789 (full), ρ_FK = 0.2431
- RE ρ_SJ conditional = 0.277 (n=236, p=1.6e-5)
- Verdict: FAIL (RE ρ_SJ < 0.40)

### RE seed456 关键指标
- NER: greedy_f1 = 0.6639, ρ_SJ = 0.3579 (full), ρ_FK = 0.2531
- RE: greedy_f1 = 0.4173, ρ_SJ = 0.2650 (full), ρ_FK = 0.2452
- RE ρ_SJ conditional = 0.315 (n=239, p=6.4e-7)
- Verdict: FAIL (RE ρ_SJ < 0.40)

**两个新 seed 与 seed42 一致：RE 上 SJ ρ 约 0.26-0.28，远低于 NER 的 0.36-0.40。RE 信号弱具有跨 seed 一致性。**

---

## 待计算

- [ ] RE 2-seed unified pipeline selection F1 for Table 2（需从 seed123/456 的 samples.jsonl 计算 RE selection F1 并与 seed42 合并）
