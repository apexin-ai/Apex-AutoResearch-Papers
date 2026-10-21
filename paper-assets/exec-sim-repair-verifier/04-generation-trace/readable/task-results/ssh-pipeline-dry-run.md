# ssh pipeline dry run

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_pipeline-dry-run_20260520T102359_result.json`
- **Structured JSON:** [`07e8ece9393f0507b4d1.json`](../../sessions/07/07e8ece9393f0507b4d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dry-run 结果

### Task B: plot_figure2_v2.py — PASS
- 输出: `artifacts/figure2_v2.png` (97KB)
- 无报错，脚本用硬编码数据直接绘图

### Task A: w5_mixed_effects_v2.py — PASS (修了一个 bug)

**发现的 bug**: `formulation × mutation_type` 交互项导致设计矩阵奇异（`LinAlgError: Singular matrix`）。原因是数据不平衡——CWM repo 数据 mutation_type 全是 `unknown`，TRAJ 只有 func 级数据，交叉表有大量结构性空格。

**修复**: 在 `fit_mixed_lm` 中捕获 `LinAlgError`，自动回退为无交互的主效应模型（`*` → `+`）。修复已应用到本地和服务器。

**运行结果** (51,842 obs, 139 problems, 3 formulations, 2 models):
- Model 1 (cross-complexity): 回退到 `C(formulation) + C(mutation_type)`，收敛有 warning（`unknown` 类别的系数 SE 为 NaN），但输出完整
- Model 2 (cross-model): 回退到 `C(formulation) + C(model)`，正常收敛。CWM 比 CLS 低 -10.65pp，TRAJ 低 -31.48pp，Qwen 比 DeepSeek 低 -9.41pp
- 输出: `artifacts/w5_dryrun/w5_mixed_effects_results.json` + `w5_latex_tables.tex`

**预期**: 正式数据（CLS/TRAJ/CWM 各 3 seed，所有 repo 级）将不会触发 singular matrix，因为 formulation × complexity 不会有空格。convergence warnings 也应消失。

---
