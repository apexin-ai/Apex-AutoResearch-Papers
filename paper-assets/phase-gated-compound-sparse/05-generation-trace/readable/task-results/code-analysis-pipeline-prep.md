# code analysis pipeline prep

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_analysis-pipeline-prep_20260514T223013_result.json`
- **Structured JSON:** [`5cb0b7cb79f3b7981368.json`](../../sessions/5c/5cb0b7cb79f3b7981368.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析 pipeline 已就绪。

**脚本**: `/root/autodl-tmp/pacs/analyze_n500_unified.py`

**5 项分析全部覆盖**:
1. Median II + bootstrap 95% CI (B=10000) — D054
2. Cohen's d_z within-importance only — D059
3. Per-phase effective n (high/mid/low)
4. Spearman ρ + permutation 单调性检验

**唯一修改**: 给 `permutation_monotonicity_test` 函数添加了 Spearman ρ（`scipy.stats.spearmanr`）。

**Dry-run 验证通过**:
- n=500 部分数据 (DS 3/8, QW 3/8)：正常运行，缺失条件报 missing data
- n=50 全量数据：d_z 输出正常（−0.52 ~ −0.80），Spearman ρ=1.0，permutation p=0.085

实验全部完成后运行 `/root/miniconda3/bin/python analyze_n500_unified.py --csv --latex` 即可获得完整结果。

---
