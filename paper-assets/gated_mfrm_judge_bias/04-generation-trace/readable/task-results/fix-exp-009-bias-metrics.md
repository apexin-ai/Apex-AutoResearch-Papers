# fix exp 009 bias metrics

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_009_bias_metrics_20260521T230843_result.json`
- **Structured JSON:** [`833f5173d439f38dec86.json`](../../sessions/83/833f5173d439f38dec86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。报告如下：

---

## 修改摘要

**文件**: `/root/gated_mfrm_judge_bias/exp009/run_exp009.py`

### 修改 1 — 提取 `c_true`（~line 186）
```python
# 新增一行
c_true = data["true_params"]["c"]
```

### 修改 2 — 计算 bias_slope/bias_corr（~line 192-193）
```python
# 在 tau 计算后新增
bias_slope = float(np.polyfit(c_true, diff, 1)[0])
bias_corr = float(np.corrcoef(diff, c_true)[0, 1])
```
并在 `buf.append` dict 中加入 `"bias_slope": bias_slope, "bias_corr": bias_corr`。

### 修改 3 — 可视化更新
`plot_bias_vs_rho()` 从 2 面板改为 3 面板：
- Panel 1: **Bias Slope vs ρ**（替代旧 mean_bias 面板）— sequential 预期正斜率随 ρ 增大，joint ≈ 0
- Panel 2: RMSE vs ρ（保留）
- Panel 3: Kendall τ vs ρ（新增）

### CSV columns
`bias_vs_rho.csv`: `rho, seed, method, rmse, mean_bias, kendall_tau, bias_slope, bias_corr`

---

## 运行状态
| 项目 | 状态 |
|------|------|
| 旧进程 (PID 54679) | ✓ killed |
| 旧 CSV | ✓ 已删除 |
| tmux session `exp-009` | ✓ 运行中 (created 07:10:19) |
| 语法检查 | ✓ SYNTAX_OK |
| 首个 MCMC seed | JAX JIT 编译中（正常） |

---
