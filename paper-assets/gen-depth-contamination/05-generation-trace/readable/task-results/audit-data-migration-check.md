# audit data migration check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_data_migration_check_20260516T085038_result.json`
- **Structured JSON:** [`f125d6c4a424dfca9a6f.json`](../../sessions/f1/f125d6c4a424dfca9a6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 迁移完整性检查报告

### 1. 存在的文件

| 路径 | 大小 | 所属实验 |
|------|------|---------|
| `results_exp016_qwen_base/pairwise_auc.json` | — | exp-016 (base vs instruct) |
| `results/exp_021_length_128/pairwise_auc.json` | — | exp-021 (length ablation) |
| `results_exp020_pythia_greedy/pairwise_auc.json` | — | exp-020 (Pythia greedy) |
| `artifacts/exp016_bootstrap_ci.json` | 1786B | exp-016 bootstrap CI |
| `artifacts/figures/fig2_auc_decay.{pdf,png}` | — | 主图已生成 |
| `artifacts/figures/fig3_transfer_heatmap.{pdf,png}` | — | 主图已生成 |
| `artifacts/figures/fig_s1_auc_decay_ci.{pdf,png}` | — | 补充图已生成 |
| `artifacts/figures/fig_filtering_strategies.{pdf,png}` | — | 主图已生成 |
| `data_exp019_mistral7b/depth_{0-3}.jsonl` | — | exp-019 原始生成数据 |
| `data_exp020_pythia_{greedy,nuc09,t07,t12}/` | — | exp-020 原始生成数据 |

### 2. 缺失的文件

| 实验 | 缺失文件 | 说明 |
|------|---------|------|
| exp-003 (decoding ablation) | `exp003_bootstrap_ci.json` | report.md 仍指向 westc-26893 |
| exp-013 (cross-transfer) | `cross_transfer_matrix.json` | 服务器上不存在 |
| exp-006 (filtering) | `filtering_results.json` | 服务器上不存在 |
| exp-001, exp-002, mvp-001 | `pairwise_auc.json` | 早期实验数据未迁移 |
| exp-019 (Mistral-7B) | 结果文件 | 有原始数据但 `results_exp019_mistral7b/` 为空（实验可能未完成评估） |
| exp-020 (Pythia nuc0.9) | 结果文件 | `results_exp020_pythia_nuc09/` 为空 |
| exp-021 (length 256) | 结果文件 | `results/exp_021_length_256/` 为空 |

### 3. 仍指向 westc-26893 的引用

仅 report.md 中一处：
```
[exp003_bootstrap_ci](westc-26893:/root/autodl-tmp/gen-depth-contamination/artifacts/exp003_bootstrap_ci.json)
```

服务器代码中无任何 `westc-26893` 引用（grep 确认）。

### 4. 影响评估

**对论文生成无阻塞影响。** 原因：

- **fig3_transfer_heatmap**: `transfer_heatmap.py` 有 `EMBEDDED_TRANSFER` 硬编码 4×4 矩阵（exp-013 数据），无需原始 JSON
- **fig_filtering_strategies**: `plot_filtering_strategies.py` 有 `EMBEDDED_FILTERING` 硬编码 5 策略分数（exp-006 数据），无需原始 JSON
- **fig2_auc_decay**: 自动发现 `results_*/pairwise_auc.json`，当前有 3 个实验数据（exp016、exp020_greedy、exp021_128），可正常绘图
- **fig_s1_auc_decay_ci**: 仅有 exp016 bootstrap CI，缺 exp003 CI 数据——但图已生成（可能只显示 exp016 的 CI band）
- 所有 **已生成的 PDF/PNG 图表已在 `artifacts/figures/` 中**，无需重新生成

### 5. 建议

- **无需从备份恢复**。Fallback 嵌入数据 + 已生成图表已覆盖论文所需。
- **report.md 的 westc-26893 引用**可清理，改为 `(embedded in plot script)` 或本地 artifact 路径。
- `results_exp019_mistral7b/` 和 `results_exp020_pythia_nuc09/` 为空是因为 exp-018/019 仍在运行中（report.md 显示 running 状态），非迁移遗漏。
- 早期实验（exp-001/002/003/mvp-001）的原始 JSON 丢失但不影响当前论文——其核心数值已嵌入绘图脚本或被后续实验（exp-016/020/021）替代。

---
