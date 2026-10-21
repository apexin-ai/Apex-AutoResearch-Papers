# code exp008 nregime fix

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp008_nregime_fix_20260514T041734_result.json`
- **Structured JSON:** [`923b934d8486da8e36ec.json`](../../sessions/92/923b934d8486da8e36ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。三个文件已更新并通过验证：

**修改总结：**

| 文件 | 改动 |
|------|------|
| `run_signal_survival.py` | 新增 `--regime-dirs NAME=PATH` 和 `--regime-names`；保留 `--sft-signals-dir`/`--rl-signals-dir` legacy 兼容；`generate_mock_data` 支持 N regime 链式衰减（N=2 时随机序列与原版一致） |
| `signal_survival_analysis.py` | 新增 `compute_single_regime_metrics` 和 `_extract_signal_vectors`；`run_survival_analysis` 接收 `OrderedDict[regime_name, signals]`，输出 `auc_matrix`(signal×regime) + `pairwise_tests`(相邻对) + `per_signal`(N=2 向后兼容)；`print_summary_table` N=2 走 legacy 表格，N>2 走 AUC 矩阵表格 |
| `plot_survival.py` | bar chart 改为 seaborn heatmap (signal×regime AUC)；新增 Δ AUC heatmap (相邻 regime 对)；移除 scatter plot 和对 raw signal data 的依赖，只需 report JSON |

**验证结果：**
- N=2 dry-run：legacy 表格正常输出，4 signal 全部 surviving
- N=4 dry-run（base→SFT→RL→DPO）：AUC 矩阵 + 3 对 pairwise test 正确，AUC 逐级衰减符合预期
- PDF 输出：`survival_auc_heatmap.pdf` (19KB) + `survival_delta_auc.pdf` (21KB) 正常生成

---
