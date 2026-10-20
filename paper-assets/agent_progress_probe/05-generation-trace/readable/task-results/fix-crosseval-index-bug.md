# fix crosseval index bug

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_crosseval-index-bug_20260514T154606_result.json`
- **Structured JSON:** [`5cd750b90090a4219385.json`](../../sessions/5c/5cd750b90090a4219385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。结果汇总：

## Bug 确认
- `split_info.json` 的 `test_indices` 范围 [33, 15158]，是 **conf≥2 过滤后 15401 元素数组**的索引
- 原脚本直接用这些索引访问 54809 元素的 `embeddings.pt` → **39.0% 标签错配** (711/1824)
- 修复方法：通过 `keep_indices`（conf≥2 在全量数组中的位置）做索引映射

## 修复后结果（正确 test set: 1824 windows, stag=485, prog=1339）

| Model | macro_f1 | accuracy | f1_stag | f1_prog | Δmacro_f1 |
|-------|----------|----------|---------|---------|-----------|
| **baseline_probe_001** | **0.9055** | 0.9282 | 0.8593 | 0.9518 | **+0.092** |
| no_cmd_rep | 0.7107 | 0.8004 | 0.5495 | 0.8718 | -0.022 |
| no_file_diff | 0.6822 | 0.7001 | 0.6068 | 0.7576 | +0.049 |
| no_ob | 0.7659 | 0.8481 | 0.6272 | 0.9046 | +0.012 |

关键发现：
- **Baseline 恢复到 0.9055**，与原始训练时报告的 macro_f1 完全一致，确认索引修复正确
- Holdout 模型的相对排序不变：no_ob > no_cmd_rep > no_file_diff
- 修复脚本已保存在服务器 `lf_holdout_crosseval_fixed.py`，结果在 `lf_holdout_crosseval_fixed_results.json`

---
