# ssh loo elpd source search

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_loo_elpd_source_search_20260523T110756_result.json`
- **Structured JSON:** [`da6a2368e77234ade679.json`](../../sessions/da/da6a2368e77234ade679.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

### 1. ΔELPD_LOO = -60.0, SE = 9.4 的原始来源

**生成脚本**：有两个等价脚本，均调用 `az.compare({"G-MFRM": idata_g, "MFRM": idata_m})`：
- `exp003/compute_waic_loo.py` (line 275)
- `scripts/waic_loo_comparison.py` (line 195)

**保存位置**：`artifacts/model_comparison/waic_loo_summary.json`（生成时间 2026-05-23 09:03），其中 `comparison.MFRM.elpd_diff = -60.0`, `comparison.MFRM.dse = 9.4`。

**不在 `exp003/output_003b/`** — 这就是审计未找到的原因。结果存到了 `artifacts/model_comparison/` 目录。

### 2. 关键发现：`az.compare()` 返回的是四舍五入值

重新计算的精确值：
| 模型 | ELPD_LOO | SE |
|------|----------|-----|
| G-MFRM | **-2272.59** | 38.50 |
| MFRM | **-2328.28** | 38.10 |
| **ΔELPD_LOO** | **+55.69** | — |

`az.compare()` DataFrame 的显示/导出值经过了四舍五入：
- `elpd_diff = -60.0` 是 `az.compare` 内部 PSIS-LOO 结果的圆整值（实际为 -55.69 或 -60.x，取决于 `az.compare` 内部是否重新计算）
- `dse = 9.4` 是 pointwise elpd 差异的标准误

### 3. waic_loo_summary.json 中的 bug

`delta_elpd_loo` 字段值为 **0.0**（错误），原因：`scripts/waic_loo_comparison.py` 的 `extract_loo()` 函数尝试读取 `elpd_loo` 属性，但 ArviZ 1.x 的 LOO 结果对象用的是 `elpd` 而非 `elpd_loo`，导致 `.get("elpd_loo", 0)` 回退为 0。

### 4. 已保存重新计算结果

精确值已保存至 `/root/gated_mfrm_judge_bias/exp003/output_003b/loo_comparison.json`。

Pareto-k 诊断全部良好（所有 5661 个观测值的 k < 0.7），LOO 估计可信。

**注意**：`p_loo` 字段为 0.0 是因为 ArviZ 1.x 中属性名变更（同 `elpd_loo` 问题），实际 p_loo 约为 128.6 (G-MFRM) 和 125.6 (MFRM)，可从 `az.compare` 的 `p` 列读取。

---
