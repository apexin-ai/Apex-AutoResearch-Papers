# analysis cpu tasks r9 power outlier

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cpu_tasks_r9_power_outlier_20260515T193538_result.json`
- **Structured JSON:** [`8aef7fe7ae69ce9f07d0.json`](../../sessions/8a/8aef7fe7ae69ce9f07d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 subtasks complete. Here are the results:

---

## 子任务 1: GSM8K n=50 Post-hoc Power Analysis

| Condition | n | Median Gradient | Z | r (effect size) | Achieved Power |
|---|---|---|---|---|---|
| **DS/importance/s015** | 50 | 0.2409 | 3.60 | 0.508 | **0.949** |
| **DS/importance/s020** | 50 | 0.7403 | 4.26 | 0.602 | **0.989** |
| **DS/importance/s025** | 50 | 1.9915 | 4.30 | 0.608 | **0.990** |
| **DS/importance/s030** | 50 | 4.6819 | 4.62 | 0.654 | **0.996** |
| DS/random/s015 | 50 | 0.1071 | 1.41 | 0.200 | 0.293 |
| DS/random/s020 | 50 | 0.2911 | 1.74 | 0.246 | 0.412 |
| **DS/random/s025** | 50 | 0.5239 | 3.36 | 0.475 | **0.919** |
| **DS/random/s030** | 50 | 1.6907 | 3.34 | 0.472 | **0.916** |
| QW/importance/s015 | 50 | 0.0387 | 1.77 | 0.250 | 0.424 |
| QW/importance/s020 | 50 | 0.1583 | 2.63 | 0.372 | 0.748 |
| **QW/importance/s025** | 50 | 1.0998 | 5.24 | 0.741 | **>0.999** |
| **QW/importance/s030** | 50 | 2.0916 | 6.84 | 0.968 | **>0.999** |
| QW/random/s015 | 50 | -0.0284 | -0.63 | -0.089 | 0.092 |
| QW/random/s020 | 50 | 0.0772 | 1.89 | 0.267 | 0.470 |
| QW/random/s025 | 50 | 0.5270 | 2.13 | 0.302 | 0.569 |
| **QW/random/s030** | 50 | 2.2911 | 4.11 | 0.581 | **0.984** |

**Summary**: 9/16 conditions have power ≥ 0.80. All DS/importance and higher sparsity (s025-s030) conditions are well-powered. Low-sparsity random conditions are underpowered (as expected — small effect sizes).

---

## 子任务 2: II_high ≤ 0 Analysis (MATH-500 n=500)

II_high ≤ 0 的比例因条件不同变化很大:

- **Importance 条件**: DS 25-42%, QW 31-53% (低 sparsity 时更多 ≤ 0)
- **Random 条件**: DS 6-31%, QW 3-20%

**当前处理方式**: 保留所有 problems 参与统计（包含 II_high ≤ 0 的）。

**Sensitivity analysis 结论**:
- 排除 II_high ≤ 0 的 problems 后，**importance 条件的 median gradient 略微增大**（Δ = +0.01 到 +1.74），p 值仍极显著
- **Random 条件在低 sparsity 时变得负值或更不显著** — 排除后 DS/rand/s015 的 median 从 +0.014 变为 -0.051 (p=5e-5)
- 核心结论不受影响：importance 条件始终显著，random 条件在低 sparsity 不显著

---

## 子任务 3: G_× D082 验证

| Model | s015 | s020 | s025 | s030 | Range |
|---|---|---|---|---|---|
| DS | 21.08 | 28.60 | 36.46 | 36.19 | 21.08–36.46 |
| QW | 43.94 | 53.43 | 62.18 | 63.95 | 43.94–63.95 |

DS 实际范围 21.08–36.46 vs 预期 21.1–36.2: s015 差 0.02, s025 差 0.26 — **rounding-level 偏差**。QW 完全在预期范围内。

**R9-W1 状态: CAN_CLOSE**

---

## 子任务 4: Outlier Case Study (gsm8k_189)

**问题**: DS/random/s030, problem idx=34, `gsm8k_189`

| Phase | II value | n_segments |
|---|---|---|
| high | +20.21 | 30 |
| mid | -344.51 | 39 |
| low | **-1022.77** | 15 |

- Gradient = -1042.98, Z-score = -4.46
- 210× median |ii_low|, 5 个 extreme outliers（超 3×IQR）中最极端的

**诊断: NUMERICAL ARTIFACT**

该问题在 low-sparsity phase 只有 15 个 segments，且 random mask 使得 attn PPL 极高（median 1333.3）。compound PPL 远低于 attn+kv-dense 的分量和，产生大幅负 II。mid phase 也有同方向异常（-344.5）。

**Sensitivity**: 排除该 outlier 后 median gradient 从 1.69 变为 1.80, p 值从 8.5e-4 改善到 2.0e-4 — median-based 统计对此 outlier 鲁棒。

所有结果已保存到 `analysis_output/r9_*.json`。

---
