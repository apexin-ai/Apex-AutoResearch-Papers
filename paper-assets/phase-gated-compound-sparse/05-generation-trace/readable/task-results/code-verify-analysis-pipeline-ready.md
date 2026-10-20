# code verify analysis pipeline ready

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-analysis-pipeline-ready_20260514T192745_result.json`
- **Structured JSON:** [`c52a7a05ca4aa14c5f62.json`](../../sessions/c5/c52a7a05ca4aa14c5f62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**Pipeline 状态**: 基本就绪，1 个问题需修复。

**通过项**:
- D054 (median + median bootstrap CI): ✓
- Wilcoxon + Bonferroni: ✓
- 16 条件全覆盖（8/model），缺失条件优雅降级
- s015 数据格式与脚本输入完全匹配（500 problems, `per_problem_ii` 结构正确）

**需修复**:
- **D059 违规**: `paired_imp_vs_rand()` 和 `paired_imp_vs_rand_gradient_test()` 报告了 imp vs rand 的 d_z，应移除。涉及 `scripts/analyze_c2_n500.py` 中两个函数的返回值和 `format_report()` 中两个表格的 d_z 列。

**注意事项**:
- 现有 s015 分析用了 `B_BOOTSTRAP=2000`，全量跑应用默认 10000
- 始终使用 `scripts/analyze_c2_n500.py`，根目录版本已过时
- 一键命令: `cd /root/autodl-tmp/pacs && /root/miniconda3/bin/python scripts/analyze_c2_n500.py`

---
