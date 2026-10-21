# verify final partB C retry

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_final_partB_C_retry_20260523T193820_result.json`
- **Structured JSON:** [`7ead3b698865abe218c1.json`](../../sessions/7e/7ead3b698865abe218c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed to compile the full verification report.

---

## Part B: Figure 数据源验证

### 1. delta_vs_rho 图

**数据点 vs 正文一致性检查：**

| ρ | 图中 Δ | 正文来源 | 一致？ |
|---|--------|----------|--------|
| 0.2 | +0.046 | appendix.tex:392 "+0.046 PPL" | ✅ |
| 0.3 | +0.002 | appendix.tex:471 "Δ=+0.002" | ✅ |
| 0.4 | -0.020 | results.tex:7, intro:24 "Δ=-0.020" | ✅ |
| 0.6 | -0.032 | results.tex:94 "Δ=-0.032" | ✅ |

✅ **一致。** 所有四个数据点在正文（results.tex, discussion.tex, introduction.tex, appendix.tex）中多处引用均一致。图由 worker_figure_delta_vs_rho_v3 (May 23 09:47) 生成，使用正确数据。

### 2. constraint_regime_decomposition 图

⚠️ **generate_paper_figures.py 仍含 tau=0.8 旧数据，但最终图已正确。**

| | generate_paper_figures.py (May 19, 旧) | worker v3 (May 23, 最终) | 正文 (results.tex:126, appendix.tex:143-146) |
|---|---|---|---|
| ρ=0.4 α_eff | 38.2% | **50.9%** | **50.9%** |
| ρ=0.4 ESS | 59.8% | **43.3%** | **43.3%** |
| ρ=0.4 clean | 2.0% | **5.8%** | **5.8%** |
| ρ=0.6 α_eff | 33.4% | **46.8%** | **46.8%** |
| ρ=0.6 ESS | 66.0% | **48.7%** | **48.7%** |
| ρ=0.6 clean | 0.6% | **4.5%** | **4.5%** |

实际的 PDF/PNG 文件时间戳为 May 23 12:01，晚于 generate_paper_figures.py (May 19 13:39)，由 worker v3 用正确的 tau=0.7 数据覆盖生成。

✅ **最终图数据正确** — 与正文所有引用一致。

⚠️ **generate_paper_figures.py 需更新** — 脚本中 fig2_constraint_regime() 仍硬编码 tau=0.8 旧数据，若重新运行会生成错误图表。

### 3. Figure caption 数字一致性

| 图 | Caption 中数字 | 正文一致？ |
|----|---------------|-----------|
| fig:grid_b_trend (results.tex:84-87) | ESS-only b* 3.5-5.9, adaptive b* 1.4 | ✅ 与 results.tex:10-17 一致 |
| fig:regime_decomp (appendix.tex:143-146) | ρ=0.4: 50.9/43.3/5.8; ρ=0.6: 46.8/48.7/4.5 | ✅ 与 results.tex:126 一致 |
| fig:tau_rho_rank (appendix.tex:157-159) | τ=0.7 paired t=-4.70, p<0.05 | ✅ 与 results.tex:116 一致 |
| fig:dr_dual_curve (appendix.tex:220-222) | 描述性，无具体数值 | ✅ 无冲突 |
| fig:delta_vs_rho (appendix.tex:484-488) | 描述 transition zone [0.3, 0.4] | ✅ 与 appendix.tex:479 一致 |
| fig:overview (introduction.tex:44) | Δ=-0.020 | ✅ 与 results.tex:7 一致 |

✅ **所有 caption 数字与正文一致。**

---

## Part C: Appendix 交叉引用一致性

### 1. ρ sensitivity tables

**ρ=0.6 table (tab:rho06, appendix:269-285) vs 主文 (results.tex:94-96):**

| 数据项 | Appendix tab:rho06 | results.tex | 一致？ |
|--------|---------------------|-------------|--------|
| Adaptive mean | 17.731 ± .004 | 17.731 ± 0.004 | ✅ |
| Uniform mean | 17.763 ± .008 | 17.763 ± 0.008 | ✅ |
| Δ | -0.032 | -0.032 | ✅ |
| Grid b=0.3 (seed 42) | 17.634 | 17.634 | ✅ |
| ESS-only mean | 17.763 ± .006 | 17.763 | ✅ |
| Random mean | 17.861 ± .025 | 17.861 | ✅ |
| t-stat (3dp) | t=-9.95 | t=-9.95 | ✅ |
| p-value (3dp) | p=0.010 | p=0.010 | ✅ |

✅ **完全一致。**

**ρ=0.3 table (tab:rho03, appendix:456-477) vs 主文：**
- appendix:471 "Δ=+0.002" ✅ 与 discussion.tex:11 一致

**ρ=0.2 (appendix:390-397) vs 主文：**
- appendix:392 "Δ=+0.046" ✅ 与 discussion.tex:11 一致

### 2. Detector comparison table

**tab:detector (appendix:358-372) vs results.tex:108-109:**

| Detector | Appendix AUC/ECE/Δ | results.tex | 一致？ |
|----------|---------------------|-------------|--------|
| GPT-2 | AUC 0.91, ECE 0.131, Δ=+0.098 | AUC 0.91, ECE 0.131, Δ=+0.098 | ✅ |
| N-gram | AUC 0.73, ECE 0.069, Δ=+0.129 | AUC 0.73, ECE 0.069, Δ=+0.129 | ✅ |
| TF-IDF+LR | AUC 0.94, ECE 0.048 | experiments.tex:8 "AUC=0.94, ECE=0.05" | ⚠️ |

⚠️ **TF-IDF ECE: 0.048 (detector table) vs 0.05 (experiments.tex).** 仅为四舍五入差异 (0.048→0.05)，不影响结论。

❌ **TF-IDF+LR Holdout PPL 不一致:**
- tab:detector (appendix:362): τ=0.8, 3 seeds → PPL **17.650** ± .010, Δ=**-0.044**
- tab:tau (appendix:115): τ=0.8, 3 from-scratch seeds → PPL **17.683** ± .006, Δ=**-0.011**

两个表理应记录同一实验（TF-IDF+LR, τ=0.8, 3 seeds），但 PPL 差异 0.033，Δ 差异 0.033。最可能原因：detector table 包含了 checkpoint-resumed seed 42 数据（resume artifact 使 Δ 膨胀至 -0.041），而 tau sweep table 明确使用 from-scratch seeds。**建议：detector table 应改用 from-scratch 数据 (17.683)，或注明包含 checkpoint-resumed run。**

### 3. Grid search table

**tab:grid_full (appendix:78-98) vs 主文:**

| 数据项 | Appendix | 主文 | 一致？ |
|--------|----------|------|--------|
| b=0.3 PPL (seed 42) | 17.640 (best) | results.tex:59 seed 42 = 17.640 | ✅ |
| Grid 3-seed mean | — (seed 42 only) | results.tex:7 "17.620 for grid b=0.3 (3-seed mean)" | ✅ (不矛盾) |
| b=0.3 is post-hoc best | caption 确认 | results.tex:9 "grid-best b=0.3" | ✅ |
| b=0.1 三种子均值 | caption "17.655 ± 0.009" | — (主文未直接引用此数) | ✅ |

✅ **一致。**

### 4. Batch-size results

主文 (results.tex:121) 引用的 batch-size 数据：
- B=4: Δ=-0.020±0.008 (3 seeds) → 1.0×
- B=8: Δ=-0.050 (2-seed mean) → 2.5×
- B=16: Δ=-0.068±0.005 (3 seeds) → 3.4×

与 appendix.tex:71 一致: "B=16 the adaptive advantage amplifies 3.4× (Δ=-0.068±0.005)" ✅
与 discussion.tex:74 一致: "1.0× at B=4, 2.5× at B=8 2-seed mean, 3.4× at B=16 3 seeds" ✅
与 conclusion.tex:2 一致: "1.0× to 3.4×" ✅

✅ **一致。** 但 appendix 中没有 B=8/B=16 的 per-seed 详细表格（主文直接给出数字，无对应附录表可交叉验证）。

### 5. 交叉引用

逐项检查 appendix.tex 中所有 `\ref{}` 引用：

| 引用 | 目标 label | 存在？ |
|------|-----------|--------|
| Proposition~\ref{prop:monotone} | appendix.tex:5 | ✅ |
| \S\ref{sec:sensitivity} | results.tex:113 | ✅ |
| Table~\ref{tab:grid_full} | appendix.tex:98 | ✅ |
| Appendix~\ref{app:resume_artifact} | appendix.tex:424 | ✅ |
| Figure~\ref{fig:regime_decomp} | appendix.tex:146 | ✅ |
| Figure~\ref{fig:tau_rho_rank} | appendix.tex:160 | ✅ |
| Table~\ref{tab:hybrid}/\ref{tab:dr_threshold} | appendix.tex:188/213 | ✅ |
| Figure~\ref{fig:dr_dual_curve} | appendix.tex:223 | ✅ |
| Table~\ref{tab:downstream} | appendix.tex:256 | ✅ |
| Table~\ref{tab:rho06} | appendix.tex:285 | ✅ |
| Table~\ref{tab:alpha_corr}/\ref{tab:alpha_corr_perseed} | appendix.tex:314/342 | ✅ |
| Table~\ref{tab:detector} | appendix.tex:372 | ✅ |
| Table~\ref{tab:cross_model} | appendix.tex:420 | ✅ |
| Table~\ref{tab:main} | results.tex:78 | ✅ |
| Table~\ref{tab:tau} | appendix.tex:125 | ✅ |
| Figure~\ref{fig:delta_vs_rho} | appendix.tex:489 | ✅ |
| \S\ref{sec:robustness}, \S\ref{sec:limitations} | results.tex:92, main.tex:71 | ✅ |
| Eq~\ref{eq:bstar} (via Algorithm) | method.tex:25 | ✅ |

✅ **所有交叉引用的 label 均存在，无断链。**

⚠️ **tab:hybrid (appendix:172-188) 未注明使用 τ=0.8.** Adaptive ρ=0.4 = 17.689 匹配 τ=0.8 from-scratch (17.694-0.005)，而非主表 τ=0.7 的 17.680。读者交叉引用时可能混淆。建议在 caption 中注明 "τ=0.8"。

### 6. 统计量一致性

| 统计量 | 主文 | Appendix | 一致？ |
|--------|------|----------|--------|
| ρ=0.4 paired t | t=-7.1 (results.tex:8) | — (未重复) | ✅ |
| ρ=0.4 p | p=0.019 (results.tex:8) | — (未重复) | ✅ |
| ρ=0.4 p_BH | p=0.078 (results.tex:8) | — | ✅ |
| ρ=0.6 t (3dp) | t=-9.95 (results.tex:94) | t=-9.95 (appendix:283) | ✅ |
| ρ=0.6 p (3dp) | **p=0.010** (results.tex:94) | **p=0.010** (appendix:283) | ✅ |
| ρ=0.6 t (full precision) | — | t=-15.4 (appendix:283) | ✅ |
| ρ=0.6 p (full precision) | — | p=0.004 (appendix:283) | ✅ |
| ρ=0.6 p_BH | p=0.064 (results.tex:94 footnote) | — | ✅ |
| 95% BCa CI | [-0.028, -0.012] (results.tex:8) | — | ✅ |

✅ **已知问题 (p=0.009 vs p=0.010) 已修复** — 主文和 appendix 现在均为 p=0.010。

---

## 汇总

| 级别 | 项目 | 详情 |
|------|------|------|
| ❌ | Detector table PPL 不一致 | tab:detector TF-IDF PPL 17.650 vs tab:tau τ=0.8 PPL 17.683，差 0.033。疑为 checkpoint-resumed 数据混入。**需修复其一。** |
| ⚠️ | generate_paper_figures.py 过时 | fig2 仍用 tau=0.8 数据。最终 PDF 已正确，但脚本重新运行会生成错图。**建议更新脚本。** |
| ⚠️ | tab:hybrid 未注明 τ | Adaptive 值匹配 τ=0.8，但 caption 未说明，与主表 τ=0.7 可能造成混淆。**建议 caption 加 "τ=0.8"。** |
| ⚠️ | ECE 四舍五入 | experiments.tex "0.05" vs detector table "0.048"。不影响结论。 |
| ✅ | delta_vs_rho 图数据 | 全部四个数据点与正文一致 |
| ✅ | constraint_regime 图数据 | 最终图使用正确 tau=0.7 数据 |
| ✅ | 所有 caption 数字 | 与正文一致 |
| ✅ | ρ sensitivity tables | 与主文完全一致 |
| ✅ | Grid search table | b=0.3 best，数据一致 |
| ✅ | Batch-size results | 所有引用一致 |
| ✅ | 交叉引用 | 无断链 |
| ✅ | p=0.009 vs 0.010 | 已修复，现均为 0.010 |

---
