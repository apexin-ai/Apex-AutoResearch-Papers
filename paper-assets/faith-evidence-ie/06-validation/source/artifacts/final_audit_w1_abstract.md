# Final Audit W1: Abstract + 正文数字交叉验证

审计日期: 2026-05-23

---

## ✅ 已核对一致

### Abstract 数字

| 数字 | 来源 | 验证 |
|------|------|------|
| -5.63pp (1.7B evidence tax) | abstract.tex:5, introduction.tex:17,22, experiments.tex:59, appendix.tex:188 (tab:training_tax: 42.75-48.38=-5.63) | ✅ 全部一致 |
| +0.25±0.47pp (4B tax) | abstract.tex:5, introduction.tex:17,22, experiments.tex:59, appendix.tex:189 | ✅ 全部一致 |
| Cohen's d=2.58 (LLaMA) | abstract.tex:7, experiments.tex:65, appendix.tex:135 (tab:variance_ci) | ✅ 全部一致 |
| 51.19 Ign-F1 (1.7B RSFT) | abstract.tex:7, introduction.tex:26, experiments.tex:81 (tab:scaling) | ✅ 全部一致 |
| std 0.09pp (1.7B RSFT) | abstract.tex:7, introduction.tex:26, experiments.tex:63,81, appendix.tex:132 | ✅ 全部一致 |
| 50.19 (8B SFT) | abstract.tex:7, introduction.tex:26, experiments.tex:83 (tab:scaling) | ✅ 全部一致 |
| std 3.23pp (8B SFT) | abstract.tex:7, introduction.tex:26, experiments.tex:63,83, appendix.tex:134 | ✅ 全部一致 |
| 4.7× fewer params | abstract.tex:7, introduction.tex:26, conclusion.tex:5, experiments.tex:63 — 8/1.7=4.706≈4.7 | ✅ 全部一致 |
| ρ=1.0 (test ranking) | abstract.tex:7, experiments.tex:110, appendix.tex:218 — 手动验证 tab:test_results 排名: 14B>LLaMA>8B>1.7B>4B dev/test 相同 | ✅ 全部一致 |
| non-overlapping χ² CIs at 1.7B | abstract.tex:7, appendix.tex:132 (SFT CI [1.45,17.55], RSFT CI [0.04,0.54], 1.45>0.54) | ✅ 不重叠确认 |

### Introduction 数字

| 数字 | 来源 | 验证 |
|------|------|------|
| -5.63pp (1.7B) | introduction.tex:17,22 → 与 abstract、experiments、appendix 一致 | ✅ |
| +0.25±0.47pp (4B) | introduction.tex:17,22 → 同上 | ✅ |
| ρ=-0.79, n=76, p<0.001 (per-relation EDCR) | introduction.tex:24, method.tex:72, experiments.tex:116, appendix.tex:394 | ✅ 四处一致 |
| +1.2 to +6.6pp (RSFT range) | introduction.tex:26 → tab:scaling gains: +1.24, +1.24→1.2(1dp); +6.55→6.6(1dp) | ✅ 四舍五入正确 |
| 51.19, std 0.09pp | introduction.tex:26 → 同 abstract 验证 | ✅ |
| 50.19, std 3.23pp | introduction.tex:26 → 同 abstract 验证 | ✅ |
| 4.7× | introduction.tex:26 → 同 abstract 验证 | ✅ |
| Cohen's d=2.58 | introduction.tex:24 → 同 abstract 验证 | ✅ |

### Method 数字

| 数字 | 来源 | 验证 |
|------|------|------|
| EDCR 0.6797 (SFT baseline) | method.tex:72 → tab:main (experiments.tex:27): 0.6797 | ✅ |
| EDCR 0.6487 (RSFT) | method.tex:72 → tab:main (experiments.tex:29): 0.6487; 手动验证 (0.6569+0.6542+0.6350)/3=0.6487 | ✅ |
| EDCR 0.9876 (GRPO QLoRA) | method.tex:72 → tab:spectrum (appendix.tex:330): 0.9876 | ✅ |
| ρ=-0.89, n=7, p=0.007 (cross-method) | method.tex:72, experiments.tex:116 | ✅ |
| ρ=-0.06, p=0.58 (EDCR vs Evi-F1) | method.tex:72, experiments.tex:116, appendix.tex:394 | ✅ |

### Experiments 数字 (除不一致项外)

| 数字 | 来源 | 验证 |
|------|------|------|
| SFT mean 43.58±3.80, range 39.74--47.34 | experiments.tex:13, tab:main:27; 手动验证: seeds 39.74/43.66/47.34, mean=43.58, std=3.80 | ✅ |
| SFT no-evidence 47.21 | tab:main:28, tab:ablation_full:61 | ✅ |
| RSFT CED 44.82±0.51 (3-seed) | tab:main:29; 手动验证 (44.23+45.12+45.11)/3=44.82, std=0.511≈0.51 | ✅ |
| Evi-F1 80.96 vs 79.61 | experiments.tex:15, tab:main:27,29 | ✅ |
| RSFT Rel-F1 45.80 | tab:main:29, experiments.tex:46, appendix.tex:100 | ✅ |
| GRPO QLoRA: Rel-F1 1.38, Evi-F1 85.04, EDCR 0.9876 | experiments.tex:43, tab:spectrum:330 | ✅ |
| GRPO bf16: Rel-F1 45.49, EDCR 0.6318 | experiments.tex:43, tab:spectrum:331 | ✅ |
| DPO 1ep→3ep: Rel-F1 33.37→31.45, Evi-F1 80.90→84.84, EDCR 0.8123→0.7503 | experiments.tex:46, tab:spectrum:332-333 | ✅ |
| Duplication 60.5%→33.0% | experiments.tex:59, tab:mechanistic:162 | ✅ |
| Training-time tax: +0.04pp (8B), +0.03pp (14B) | experiments.tex:59, tab:training_tax:190-191; 验证: 50.19-50.15=0.04, 55.10-55.07=0.03 | ✅ |
| RSFT gains: +6.55/+1.24/+4.14/+3.79 | experiments.tex:61, tab:scaling; 验证: 51.19-44.64/44.82-43.58/54.33-50.19/58.86-55.07 | ✅ |
| LLaMA RSFT gain +5.45 | tab:scaling:85; 56.54-51.09=5.45 | ✅ |
| LLaMA seeds RSFT 55.87--57.14, SFT 48.02--53.84 | experiments.tex:65, appendix.tex:212 | ✅ |
| Variance compression 7.5× (4B), 6.5× (8B), 4.6× (LLaMA) | experiments.tex:63,65, tab:variance_ci:133-135 | ✅ |
| SFT seed stds: 2.79/3.80/3.23 (1.7B/4B/8B), RSFT: 0.09/0.51/0.50 | experiments.tex:63, tab:scaling, tab:variance_ci | ✅ |
| 36× more predictable (3.23/0.09) | experiments.tex:63; 3.23/0.09=35.89≈36 | ✅ |
| Re-DocRED: RSFT 41.45 (+4.86pp over SFT 36.59) | experiments.tex:110, appendix.tex:215; 41.45-36.59=4.86 | ✅ |
| DocRED RSFT gain +5.08pp | experiments.tex:110, appendix.tex:215; 44.82-39.74=5.08 (3-seed mean minus SFT s42) | ✅ |
| Test Ign-F1 drops ~20pp | tab:test_results: range 19.81--21.86pp across all models | ✅ |
| Annotation density 34.7 vs 12.3, 2.82× | experiments.tex:110; 34.7/12.3=2.821 | ✅ |
| Partial correlations ρ=-0.8541 vs -0.8554 | experiments.tex:116, appendix.tex:397-398 | ✅ |
| CED vs flat-NLI: Rel-F1 45.63 vs 45.61 (diff 0.02pp) | experiments.tex:116, method.tex:55, appendix.tex:44 | ✅ |
| k=1 vs k=3: +1.02 Ign-F1 | experiments.tex:116; 44.66-43.64=1.02 | ✅ |
| Error reduction 6--22% | experiments.tex:116, tab:error_analysis: trunc FN -16~-22%, halluc FP -6~-12%, dup -11~-20% | ✅ |
| Evidence unchanged <0.4pp | experiments.tex:116, tab:error_analysis | ✅ |
| SFT evidence variance compression 25× (4B), 1.4× (8B) | experiments.tex:59, appendix.tex:199; 0.50/0.02=25, 0.48/0.35=1.37≈1.4 | ✅ |

### Conclusion 数字

| 数字 | 来源 | 验证 |
|------|------|------|
| 1.7B, 4B, 8B + 14B validation | conclusion.tex:4 → 与 abstract/intro 一致 | ✅ |
| two model families, two datasets | conclusion.tex:4 → Qwen3+LLaMA, DocRED+Re-DocRED | ✅ |
| 4.7× fewer params | conclusion.tex:5 → 与 abstract/intro/experiments 一致 | ✅ |

---

## ⚠️ 发现不一致

### 1. 1.7B 方差压缩倍数: 31× vs 32.6×

- **experiments.tex:63**: "variance compression is 31× at 1.7B"
- **appendix.tex tab:variance_ci (line 132)**: Compression = 32.6×
- **原因**: experiments 用 rounded std 计算 (2.79/0.09=31.0)；appendix 表声明 "ratio of SFT to RSFT point estimates (unrounded)"，用未四舍五入的 std 得到 32.6×
- **建议**: 统一为 32.6×（使用精确值）或两处都写 31×（使用 rounded 值），不应两处不同

### 2. DREEAM joint Evi-F1: 54.01% vs 54.15

- **experiments.tex:110**: "supervised DREEAM (54.01\%~\citep{ma2023dreeam})"
- **appendix.tex tab:encoder_comparison (line 306)**: DREEAM Evi-F1 (joint) = 54.15
- **差异**: 0.14pp
- **建议**: 核对 DREEAM 原论文的 exact value，统一两处

### 3. Evidence Strategy 段 EDCR 0.654 vs Table 1 EDCR 0.6487

- **experiments.tex:104 (§5.5)**: "RSFT CED reaches 36.1 (EDCR 0.654)"
- **experiments.tex tab:main (line 29)**: RSFT CED EDCR = 0.6487
- **个别 seed EDCR**: s42=0.6569, s43=0.6542, s44=0.6350, s45=0.6550 — 均不等于 0.654
- **3-seed mean**: (0.6569+0.6542+0.6350)/3 = 0.6487; **4-seed mean**: 0.6503
- **最接近**: s43=0.6542 四舍五入到 3dp 为 0.654，但其他 EDCR 均用 4dp
- **建议**: 统一为 0.6487（3-seed mean）或明确标注哪个 seed/计算方式

---

## ❌ 待确认疑点

### 1. RSFT Method B: 51.52 Ign-F1 at 4B (+4.18pp)

- **experiments.tex:61**: "RSFT from an independent SFT base (s44, Method B) achieves 51.52 Ign-F1 at 4B (+4.18pp over that base)"
- 推算 base = 51.52 - 4.18 = 47.34 (即 SFT 4B 最强 seed s44)
- 内部逻辑自洽，但 **51.52 未出现在任何表格中**，无法从已有表格交叉验证

### 2. CED reranking: Rel-F1 48.64, Evi-F1 81.88

- **experiments.tex:104**: "CED reranking at inference (best-of-N=8 by CED score) achieves Rel-F1 48.64 and Evi-F1 81.88 (TP-only)"
- **未出现在任何表格中**，无法交叉验证

### 3. Post-hoc BM25: Evi-F1 (joint) 34.7, EDCR 0.766

- **experiments.tex:104**: "Post-hoc retrieval achieves higher Rel-F1 (48.76) ... lower Evi-F1 (joint) of 34.7 (EDCR 0.766)"
- Rel-F1 48.76 与 SFT no-evidence 的 Rel-F1 匹配（tab:main:28），✅
- 但 **Evi-F1 34.7 和 EDCR 0.766 未出现在任何表格中**

### 4. Evidence Strategy 段精度不统一

- §5.5 使用 3dp EDCR (0.766, 0.654)，全文其他位置均用 4dp
- §5.5 Evi-F1 36.1 用 1dp，tab:encoder_comparison 也用 36.1（一致但与其他 Evi-F1 的 2dp 不同）
- 不影响正确性，但 reviewer 可能注意到

---

## 四舍五入一致性检查

| 指标 | 精度 | 状态 |
|------|------|------|
| Ign-F1 | 2dp (43.58, 44.82, 51.19 等) | ✅ 全篇一致 |
| Ign-F1 增量 | 2dp 正文 (e.g., +6.55, +1.24)；1dp 用于 intro 范围摘要 (+1.2 to +6.6) | ✅ 可接受 |
| Rel-F1 | 2dp | ✅ 全篇一致 |
| Evi-F1 | 2dp（除 §5.5 的 36.1 和 34.7 为 1dp） | ⚠️ 轻微不统一 |
| EDCR | 4dp（除 §5.5 为 3dp） | ⚠️ 轻微不统一 |
| Std | 2dp (0.09, 0.51, 3.80 等) | ✅ 全篇一致 |
| 方差压缩倍数 | 1dp (4.7×, 4.6×, 7.5× 等) | ✅ 一致（但 32.6× 在 appendix 表中） |
| Evidence tax | pp 单位，2dp | ✅ 全篇一致 |
| 相关系数 ρ | 2dp (0.79, 0.89, 0.06) | ✅ 一致 |
| p 值 | 3dp 或不等式 (0.007, <0.001) | ✅ 一致 |
| Cohen's d | 2dp | ✅ 一致 |

---

## 总结

- **已验证一致**: 50+ 个数字/统计量
- **发现 3 个不一致**（需修正）:
  1. 方差压缩 31× vs 32.6×
  2. DREEAM Evi-F1 54.01% vs 54.15
  3. EDCR 0.654 vs 0.6487
- **4 个待确认疑点**（数字无对应表格，无法交叉验证）
- **精度基本统一**，仅 §5.5 (Evidence Strategy Comparison) 存在轻微精度不统一
