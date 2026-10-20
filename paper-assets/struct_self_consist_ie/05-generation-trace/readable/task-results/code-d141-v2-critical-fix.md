# code d141 v2 critical fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d141_v2_critical_fix_20260518T135557_result.json`
- **Structured JSON:** [`15fa80fe83f27f4464a4.json`](../../sessions/15/15fa80fe83f27f4464a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**修复了 4 个问题：**
- **CRITICAL 1**: `evaluation.py`、`conditional_decomp`、`scatter_plot` 三个文件的 entity matching 从 `(start, end, type)` 改为 `(text, type)`
- **CRITICAL 2**: `conditional_decomp` 和 `scatter_plot` 的 CoNLL/FewNERD 数据源统一到 `exp_002_conll_n16_r1024` / `exp_027_fewnerd_n16`
- **Gold filter**: entity merge 加了空 gold 跳过
- **N=8**: CoNLL/FewNERD 从 N=16 截断到 N=8

**关键结果变化（Entity Merge Gap Recovery）：**

| Dataset | Greedy | Oracle | Best Merge | Gap Recovery |
|---------|--------|--------|------------|--------------|
| SciERC  | 0.6441 | 0.7758 | 0.6610 (k=3) | **12.8%** |
| CoNLL   | 0.9077 | 0.9497 | 0.9063 (k=3) | **-3.3%** |
| FewNERD | 0.7493 | 0.8701 | 0.7521 (k=2) | **2.3%** |

Merge 在 text matching 下对 CoNLL 反而略低于 greedy，FewNERD 收益极小。所有 merge vs oracle 差异在三个数据集上均显著为负。

完整报告已注册到 `artifacts/d141_v2_fix/d141_v2_fix_report.md`。

---
