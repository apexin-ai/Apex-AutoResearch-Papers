# code refactor plot scripts

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_refactor_plot_scripts_20260516T082238_result.json`
- **Structured JSON:** [`4db10c139f45c9fac71b.json`](../../sessions/4d/4db10c139f45c9fac71b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。PDF 文件非空（27KB 和 18KB）。

---

## 汇报

### 1. 脚本修改摘要

**`artifacts/scripts/plot_summary_auc_decay.py`**：
- 移除 hardcoded data dict，改为 `discover_auc_files()` 自动扫描 `results_*/`, `results/*/`, `data_*/` 下的 `pairwise_auc.json`
- `infer_label()` 从目录名自动推断模型名和分组（model/decode）
- 颜色/marker 从 Tableau-10 colormap 循环分配
- 支持 `--results-dir`, `--output`, `--filter` 命令行参数
- 输出到 `artifacts/figures/fig2_auc_decay.pdf`

**`scripts/draw_kstar_theta.py`**：
- 移除 hardcoded `AUC_DATA` 和 `STYLES`，改为 `discover_ci_files()` 扫描 `artifacts/*bootstrap*ci*.json` 和 `results_*/*bootstrap*ci*.json`
- 从 JSON 的 `pairs.{pair}.ci_lower` 自动提取 CI 下界
- `infer_label()` 优先从 JSON metadata 中的 `experiment` 字段推断，fallback 到文件名
- 支持 `--results-dir`, `--output`, `--filter`

### 2. 自动发现的实验数据
- `results_exp016_qwen_base/pairwise_auc.json` → 标签 "Qwen-base"
- `results/exp_021_length_128/pairwise_auc.json` → 标签 "exp_021_length_128"
- `artifacts/exp016_bootstrap_ci.json` → 标签 "Qwen-base"（from metadata）

### 3. Tab kstar_ci 溢出处理
- 主表（`tab:kstar_ci`）保持 5 模型不变（已满 `table*` 宽度），caption 加了引用扩展表
- 新增 appendix 表 `tab:kstar_ci_extended`：7 模型（含 Qwen-base 实际数据 + LLaMA-8B placeholder `--`），放在 Table S2 之后

### 4. 验证结果
- `plot_summary_auc_decay.py`: OK，PDF 27KB
- `draw_kstar_theta.py`: OK，PDF 18KB
- LaTeX 扩展表已加入 `docs/paper/appendix.tex`

### 5. 兼容性
- 当 `results_exp019_mistral7b/` 和 `results_exp020_pythia_*` 产出 `pairwise_auc.json` 后，脚本会自动发现并绘制，无需改代码
- 同理 bootstrap CI JSON 产出后 `draw_kstar_theta.py` 会自动纳入

---
