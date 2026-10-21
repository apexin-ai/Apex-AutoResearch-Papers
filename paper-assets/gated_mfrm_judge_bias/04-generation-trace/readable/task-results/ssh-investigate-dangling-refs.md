# ssh investigate dangling refs

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_investigate_dangling_refs_20260524T051155_result.json`
- **Structured JSON:** [`dcfa1171aab367aa29b9.json`](../../sessions/dc/dcfa1171aab367aa29b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成，以下是汇报。

---

## 1. Dangling References 的精确位置

两个 reference 都在 `experiments.tex` **第 52 行**（同一段长文本中）：

**Reference A — Prior robustness:**
> `Results are robust to prior specification (Horseshoe \citep{piironen2017horseshoe} vs.\ HalfNormal: Pearson $r > 0.999$; Appendix)`

注意：是裸文本 `Appendix`，没有 `\ref{}`。

**Reference B — Item-level diagnostics:**
> `Model and judge facets show acceptable fit (all infit/outfit MNSQ within $[0.63, 1.07]$; item-level diagnostics in Appendix).`

同样是裸文本 `Appendix`，无 `\ref{}`。

---

## 2. appendix.tex 当前 sections（共 18 个）

| # | Section | Label |
|---|---------|-------|
| 1 | Proof of Theorem | `app:proof` |
| 2 | Explicit Form of OVB Coefficient γ_n | `app:gamma` |
| 3 | Murphy–Topel Variance Correction | `app:murphy_topel` |
| 4 | Ablation Study | `app:ablation` |
| 5 | Posterior Predictive Check | `app:ppc` |
| 6 | OVB Validation Across Confounding Levels | `app:ovb_validation` |
| 7 | Contamination Susceptibility Recovery | `app:cn_recovery` |
| 8 | Error Propagation Figure | `app:error_prop_fig` |
| 9 | Self-Evaluation Robustness | `app:self_eval` |
| 10 | Judge Severity Profiles | `app:judge_severity` |
| 11 | Judge Count Sensitivity | `app:judge_count` |
| 12 | Stage 2 Weight Robustness | `app:weight_robustness` |
| 13 | Power Analysis | `app:power` |
| 14 | Per-Model Estimates | `app:raw_scores` |
| 15 | Contamination Bias Absorption | `app:bias_absorption` |
| 16 | Synthetic Calibration at Matched Scale | `app:synthetic_calibration` |
| 17 | CI Coverage Analysis | `app:ci_coverage` |
| 18 | Use of AI Assistants | `app:ai_assistants` |

**没有** prior robustness 或 item-level diagnostics 的 section。

---

## 3. 数据是否已存在

### Reference A: Horseshoe vs. HalfNormal prior robustness

**数据已存在，可直接计算 Pearson r。**

两组 c_n 值来源：

| Model | Horseshoe c_n | HalfNormal c_n |
|-------|--------------|----------------|
| gpt-3.5-turbo | 5.694 | 5.566 |
| gpt-4-0613 | 4.245 | 4.146 |
| qwen2.5-72b | 3.023 | 2.938 |
| llama-3.3-70b | 2.503 | 2.458 |
| gemma-2-9b | 1.611 | 1.653 |
| qwen3-8b | 1.115 | 1.149 |
| gpt-4o-mini | 0.844 | 0.916 |
| gpt-4o | 0.790 | 0.875 |

- **Horseshoe**: `/root/gated_mfrm_judge_bias/exp003/results/results.json` → `parameters.joint_gmfrm.c_values`
- **HalfNormal**: `/root/gated_mfrm_judge_bias/exp003/output_003b/results.json` → `parameters.joint_gmfrm.c_values`

θ 值也高度一致。θ 和 c_n 两组的 Pearson r 目测都 > 0.999。

还有 `output_003b/analysis/refit_summary.json` 提供了 HalfNormal refit 的完整后验统计（mean/sd/CI/ESS/R-hat）。

exp-016 无用：`results/` 目录为空（实验被 kill）。

### Reference B: Item-level diagnostics

**数据已存在，但仅为 .npy 数组，无直接可读的表格。**

- `exp008/results/item_infit.npy` — 176 个 item 的 infit MNSQ
- `exp008/results/item_outfit.npy` — 176 个 item 的 outfit MNSQ
- `exp008/results/results.json` → `item_summary`：
  - mean_infit = 0.779, sd = 0.411
  - mean_outfit = 0.730, sd = 0.567
  - n_overfit = 18, n_underfit = 74 (共 176 items)
- 同一 JSON 还有 model-level 和 judge-level 的 infit/outfit（已在 experiments.tex 正文引用）

缺少的是：item hash → infit/outfit 的映射表。npy 数组没有 item 标识，需要和原始数据的 item 顺序对齐才能生成可读表格。

---

## 4. 是否足够直接写附录 section

### Prior robustness → **足够**
两个 results.json 中的 c_n 和 θ 值可直接列成对比表，计算 Pearson r，加一段说明文字即可。还可以对比 ranking (τ)、convergence diagnostics。数据完整。

### Item-level diagnostics → **基本足够，但需少量处理**
有 176 个 item 的 infit/outfit 数值（.npy），也有 summary 统计。可以写成：
- 一个 summary 段落（已有：mean/sd/overfit/underfit counts）
- 一个 histogram 图（需从 .npy 生成）
- 或一个按 infit/outfit 分位列出 flagged items 的表

需要的额外工作：从 .npy 加载数据并对齐 item ID，生成可视化或表格。不需要重新跑实验。

---
