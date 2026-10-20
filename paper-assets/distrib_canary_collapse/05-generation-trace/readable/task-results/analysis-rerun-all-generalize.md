# analysis rerun all generalize

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rerun_all_generalize_20260518T002423_result.json`
- **Structured JSON:** [`1bc1081f3753653d9eca.json`](../../sessions/1b/1bc1081f3753653d9eca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 JSON 数据完整获取。以下是最终汇报。

---

## 统一参数 (n_perm=5000, xcorr lag=5, granger lag=1, BH q=0.05) 结果

### 对比表：Table 7 旧值 vs 新结果

| Row | Metric | Table7_OLD | Raw_p | FDR_permethod | FDR_pooled |
|---|---|---|---|---|---|
| C4 Domain | PG_fwd | 8/8 | **8/8** | **8/8** | **8/8** |
| C4 Domain | K≥4 | 8/8 | **7/8** | **7/8** | **7/8** |
| OPT-1.3B | PG_fwd | 6/8 | **6/8** | **6/8** | **6/8** |
| OPT-1.3B | K≥4 | 6/8 | **6/8** | **6/8** | **6/8** |
| Scale 1.4B | PG_fwd | 5/8 | **5/8** | **2/8** | **3/8** |
| Scale 1.4B | K≥4 | 5/8 | **5/8** | **2/8** | **3/8** |

### 全方法总结

| Experiment | Method | Raw | FDR_pm | FDR_pool |
|---|---|---|---|---|
| C4 Domain | naive_pearson | 8/8 | 8/8 | 8/8 |
| C4 Domain | differenced_xcorr | 8/8 | 8/8 | 8/8 |
| C4 Domain | threshold_onset | 6/8 | 6/8 | 6/8 |
| C4 Domain | toda_yamamoto | 4/8 | 4/8 | 4/8 |
| C4 Domain | permutation_granger | 8/8 | 8/8 | 8/8 |
| C4 Domain | K≥3 | 8/8 | 8/8 | 8/8 |
| C4 Domain | K≥4 | 7/8 | 7/8 | 7/8 |
| | | | | |
| OPT-1.3B | naive_pearson | 8/8 | 8/8 | 8/8 |
| OPT-1.3B | differenced_xcorr | 8/8 | 8/8 | 8/8 |
| OPT-1.3B | threshold_onset | 8/8 | 8/8 | 8/8 |
| OPT-1.3B | toda_yamamoto | 6/8 | 6/8 | 6/8 |
| OPT-1.3B | permutation_granger | 6/8 | 6/8 | 6/8 |
| OPT-1.3B | K≥3 | 8/8 | 8/8 | 8/8 |
| OPT-1.3B | K≥4 | 6/8 | 6/8 | 6/8 |
| | | | | |
| Scale 1.4B | naive_pearson | 7/8 | 7/8 | 7/8 |
| Scale 1.4B | differenced_xcorr | 6/8 | 6/8 | 6/8 |
| Scale 1.4B | threshold_onset | 8/8 | 8/8 | 8/8 |
| Scale 1.4B | toda_yamamoto | 0/8 | 0/8 | 0/8 |
| Scale 1.4B | permutation_granger | 5/8 | **2/8** | **3/8** |
| Scale 1.4B | K≥3 | 6/8 | 6/8 | 6/8 |
| Scale 1.4B | K≥4 | 5/8 | **2/8** | **3/8** |

### Per-pair PG raw p-values

**C4 Domain** (all 8/8 significant):
| Pair | PG p_raw | PG p_fdr_pm | PG p_fdr_pool | K_raw |
|---|---|---|---|---|
| token_entropy→mauve | 0.0212 | 0.0242 | 0.0251 | 3/5 |
| token_entropy→distinct_1 | 0.0082 | 0.0164 | 0.0161 | 4/5 |
| token_entropy→distinct_2 | 0.0126 | 0.0202 | 0.0166 | 4/5 |
| token_entropy→distinct_3 | 0.0262 | 0.0262 | 0.0299 | 4/5 |
| ece→mauve | 0.0178 | 0.0237 | 0.0219 | 4/5 |
| ece→distinct_1 | 0.0012 | 0.0096 | 0.0021 | 5/5 |
| ece→distinct_2 | 0.0036 | 0.0144 | 0.0055 | 5/5 |
| ece→distinct_3 | 0.0078 | 0.0164 | 0.0108 | 5/5 |

**OPT-1.3B** (6/8 significant, perplexity pairs fail):
| Pair | PG p_raw | PG p_fdr_pm | PG p_fdr_pool | K_raw |
|---|---|---|---|---|
| token_entropy→perplexity | 0.8540 | 0.8540 | 0.8540 | 3/5 |
| token_entropy→distinct_1 | 0.0012 | 0.0048 | 0.0024 | 5/5 |
| token_entropy→distinct_2 | 0.0034 | 0.0091 | 0.0060 | 5/5 |
| token_entropy→distinct_3 | 0.0128 | 0.0171 | 0.0164 | 5/5 |
| ece→perplexity | 0.6275 | 0.7171 | 0.6693 | 3/5 |
| ece→distinct_1 | 0.0012 | 0.0048 | 0.0024 | 5/5 |
| ece→distinct_2 | 0.0046 | 0.0092 | 0.0074 | 5/5 |
| ece→distinct_3 | 0.0126 | 0.0171 | 0.0164 | 5/5 |

**Scale 1.4B** (5/8 raw sig, FDR drops to 2-3/8):
| Pair | PG p_raw | PG p_fdr_pm | PG p_fdr_pool | K_raw |
|---|---|---|---|---|
| token_entropy→perplexity | 0.7163 | 0.7163 | 0.7640 | 1/5 |
| token_entropy→distinct_1 | 0.0274* | 0.0548 | 0.0516 | 4/5 |
| token_entropy→distinct_2 | 0.0346* | 0.0553 | 0.0615 | 4/5 |
| token_entropy→distinct_3 | 0.0532 | 0.0709 | 0.0867 | 3/5 |
| ece→perplexity | 0.5739 | 0.6559 | 0.7346 | 2/5 |
| ece→distinct_1 | 0.0042* | 0.0336* | 0.0112* | 4/5 |
| ece→distinct_2 | 0.0086* | 0.0344* | 0.0212* | 4/5 |
| ece→distinct_3 | 0.0216* | **0.0548** | 0.0432* | 4/5 |

### 关键发现

1. **C4 和 OPT：FDR 无影响**。C4 PG 8/8 全保留，OPT PG 6/8 全保留。三种 FDR scope 完全一致。

2. **C4 K≥4 从 8/8 降到 7/8**。`token_entropy→mauve` 只有 3/5 票（threshold_onset 因 downstream mauve 未检测到 onset 而 n.s.，TY 因 d_max=1 导致 df_resid=4 而 n.s.）。

3. **Scale 1.4B 是唯一 FDR 敏感的实验**。PG raw 5/8 → FDR_pm 2/8 / FDR_pool 3/8。根因：token_entropy 的 3 个 distinct pair p-values 边缘（0.0274/0.0346/0.0532），BH 校正后全部失去显著性。ece→distinct_3 也从 0.0216 → 0.0548（FDR_pm 刚好越界）。

4. **TY 在 Scale 1.4B 全军覆没 (0/8)**，因为 d_max=1-2 导致 df_resid 极低（1-4），符合 C003 约束预期。

5. **threshold_onset 无 p-value**，使用 lead_time>0 的布尔判定，不参与 FDR 校正。其在 Scale 1.4B 反而表现最强 (8/8)，因为它只检测时序先后不做统计检验。

JSON 结果保存在各实验的 `analysis/unified_5method.json` 和汇总 `results/generalize/analysis/unified_generalize_all.json`。

---
