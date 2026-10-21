# ssh fill paper dryrun

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fill-paper-dryrun_20260524T083807_result.json`
- **Structured JSON:** [`e9edbf90296abe25d07c.json`](../../sessions/e9/e9edbf90296abe25d07c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析报告。

---

## Dry-Run 验证报告

### 1. 脚本同步状态

- `fill_paper_n17.py` **未同步到服务器**。服务器上不存在 `/root/gated_mfrm_judge_bias/docs/` 目录。
- `output_n17/` **不存在**。N=17 MCMC 尚未运行。

### 2. 脚本接口

脚本接口清晰，用 `--trace-dir` 指定 MCMC 输出目录：
```bash
python fill_paper_n17.py --trace-dir /root/gated_mfrm_judge_bias/exp003/output_n17
```
输出到 `output_n17/paper_artifacts/`（可通过 `--out-dir` 覆盖）。

依赖：仅 Python 标准库（`json`, `argparse`, `pathlib`），无需额外安装。无 `--dry-run` 参数。

### 3. 数据格式不匹配（关键问题）

用 N=8 的 `output_003b/results.json` 比对脚本预期，发现 **5 处格式不匹配**，MCMC 完成后脚本无法直接运行：

| # | 脚本预期 | 实际格式 (results.json) | 严重程度 |
|---|---------|----------------------|---------|
| 1 | `results["n_models"]`, `results["n_judges"]` | `results["data_summary"]["N"]`, `["J"]` | 中 — design 数值会读为 None |
| 2 | `convergence.joint_gmfrm.r_hat_max` / `ess_min` / `divergent_transitions` | `.r_hat` / `.ess` / `.divergences` | 中 — 诊断值全部读为 None |
| 3 | `results["c_n"]` 或 `results["refit_posterior"]["c_n_95ci"]` → 期望 `{model: {mean, ci:[lo,hi], ess_bulk}}` | `parameters.joint_gmfrm.c_values` → `{model: float}` (无 CI/ESS)；`refit_summary.json` 有 CI 但格式为 array `[{model, mean, ci_95_lower, ci_95_upper, ess_bulk}]` | **高** — contamination 表和 judge severity 表无法生成 |
| 4 | `results["d_j"]` → 同上格式 | `parameters.joint_gmfrm.d_values` → flat dict | **高** |
| 5 | LOO 数据 `loo.get("delta_elpd")` / `loo.get("se")` | 实际是嵌套结构：`delta_elpd_loo` 在顶层，`dse` 在 `comparison.MFRM` 内 | 中 — LOO 数值读为 0/N/A |

### 4. 目录结构匹配

`run_n17_downstream.py` 会创建 `output_n17/downstream/` 并包含：
- `downstream/model_comparison/` (LOO/WAIC) — 脚本搜索路径 **匹配** ✓
- `downstream/bootstrap_results/` — **匹配** ✓  
- `downstream/baselines/` — **匹配** ✓
- `downstream/delta_theta/` — **匹配** ✓
- `downstream/facet_fit/` — **匹配** ✓

目录结构设计正确，问题仅在 JSON 内部的 key 名和数据结构。

### 5. 修复建议

`fill_paper_n17.py` 的 `extract_values()` 需要适配实际数据格式。核心改动：

1. **Design**: `results["data_summary"]["N"]` → `n_models` 等
2. **Convergence**: 用 `conv.get("r_hat", conv.get("r_hat_max"))` 双向兼容
3. **c_n/d_j**: 需从 `refit_summary.json`（`trace_dir/downstream/analysis/refit_summary.json`）读取 CI 数据，将 array 格式转为 dict-keyed-by-name
4. **LOO**: 适配嵌套结构 `comparison.MFRM.elpd_diff` / `comparison.MFRM.dse`

### 6. MCMC 完成后的执行流程

```bash
# Step 1: MCMC fitting
cd /root/gated_mfrm_judge_bias/exp003
python run_exp003_n17.py \
  --judgment-dir /root/gated_mfrm_judge_bias/exp001_n17/results \
  --exposure-csv /root/gated_mfrm_judge_bias/exp002/results/exposure_scores.csv \
  --output-dir /root/gated_mfrm_judge_bias/exp003/output_n17 \
  --warmup 6000 --samples 4000 --chains 4 --target-accept 0.95 --device gpu

# Step 2: Downstream analysis
python run_n17_downstream.py

# Step 3: Paper artifacts (需先修复脚本)
python docs/paper/fill_paper_n17.py --trace-dir /root/gated_mfrm_judge_bias/exp003/output_n17
```

**结论**：脚本逻辑正确、依赖无需安装、目录结构匹配，但 JSON key/格式不兼容实际 MCMC 输出。需要先修复 `extract_values()` 的数据读取逻辑，才能在 MCMC 完成后一键填充。是否现在修复？

---
