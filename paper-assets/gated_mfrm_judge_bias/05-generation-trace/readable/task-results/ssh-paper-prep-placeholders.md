# ssh paper prep placeholders

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_paper_prep_placeholders_20260524T011411_result.json`
- **Structured JSON:** [`d3eff30e8f97fc2ee606.json`](../../sessions/d3/d3eff30e8f97fc2ee606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已经收集完整。以下是报告。

---

## 1. 占位符清单

所有 TBD 均在 `docs/paper/experiments.tex`，集中在 Table 1 的 "17 models" 两列：

| 行号 | 方法 | 占位符 | 上下文 |
|------|------|--------|--------|
| 29 | Raw Average | `& TBD & TBD \\` | 17-model τ, ρ |
| 30 | MFRM-only | `& TBD & TBD \\` | 17-model τ, ρ |
| 31 | Sequential | `& TBD & TBD \\` | 17-model τ, ρ |
| 32 | CyclicJudge | `& TBD & TBD \\` | 17-model τ, ρ |
| 33 | CyclicJudge+discard | `& TBD & TBD \\` | 17-model τ, ρ |
| 34 | DCR Factor | `& TBD & TBD \\` | 17-model τ, ρ |
| 35 | Pref.\ Leakage | `& TBD & TBD \\` | 17-model τ, ρ |
| 37 | G-MFRM (ours) | `\textbf{TBD} & \textbf{TBD}` | 17-model τ, ρ (加粗) |
| 40 | \caption | `(TBD)` | caption 末尾描述 17-model 结果 |

**共 17 个 TBD**：8 行 × 2 个指标 (τ, ρ) + 1 个 caption 描述。

其他 tex 文件无 TBD/TODO/PLACEHOLDER/FIXME。

---

## 2. `run_n17_downstream.py` 输出结构

脚本跑 6 个分析步骤，输出到 `output_n17/downstream/`：

| 步骤 | 子目录 | 输出格式 | 关键 metrics |
|------|--------|----------|-------------|
| 1. WAIC/LOO | `model_comparison/` | WAIC/LOO 表 | ΔELPD_LOO, SE, stacking weight |
| 2. Bootstrap Δτ | `bootstrap_results/` | bootstrap CI | Δτ 95% CI, P(Δτ≥0) |
| 3. Baselines (exp004) | `baselines/results.json` | JSON | 每方法 `kendall_tau`, `spearman_rho`, per-model `theta` |
| 4. Bias absorption (exp019) | `delta_theta/` | JSON | per-model Δθ (G-MFRM vs MFRM) |
| 5. Facet fit (exp008) | `facet_fit/results.json` | JSON | per-model infit/outfit/θ/c, per-judge infit/outfit/d |
| 6. Full posterior analysis | `analysis/` | analyze_003b 输出 | 综合 posterior 分析 |

此外，MCMC 本身（`run_exp003_n17.py`）在拟合时调用 `evaluation.py`，直接输出 `output_n17/results.json`，包含 G-MFRM 的 τ 和 ρ。

---

## 3. 占位符 → downstream 输出映射表

| 论文占位符 (experiments.tex) | 数据来源 | 字段路径 |
|---|---|---|
| L29-35: 7 baselines 的 τ | `downstream/baselines/results.json` | `[method].kendall_tau` |
| L29-35: 7 baselines 的 ρ | `downstream/baselines/results.json` | `[method].spearman_rho` |
| L37: G-MFRM τ | `output_n17/results.json` | `joint_gmfrm.kendall_tau` |
| L37: G-MFRM ρ | `output_n17/results.json` | `joint_gmfrm.spearman_rho` |
| L40: caption "(TBD)" | 手动更新 | 根据上述数值写出 N=17 结论描述 |

baselines `results.json` 中方法名映射：
- `raw_average` → Raw Average
- `mfrm_only` → MFRM-only
- `sequential` → Sequential
- `cyclic_judge` → CyclicJudge
- `cyclic_judge_discard` → CyclicJudge+discard
- `dcr_factor` → DCR Factor
- `pref_leakage` → Pref. Leakage

MCMC 完成后，只需读两个 JSON（`output_n17/results.json` + `downstream/baselines/results.json`），即可填完全部 17 个 TBD。

---
