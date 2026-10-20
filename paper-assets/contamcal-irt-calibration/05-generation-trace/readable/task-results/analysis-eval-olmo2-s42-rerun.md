# analysis eval olmo2 s42 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_olmo2_s42_rerun_20260521T154505_result.json`
- **Structured JSON:** [`9a7c67513c78282206c1.json`](../../sessions/9a/9a7c67513c78282206c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/eval_olmo2_s42_rerun_analysis.md`。

## 结果摘要

**d000 MMLU 基线验证通过**：53.79% 精确匹配，确认不是 58.60%。

**ARC**：5 个 dosage 全部与论文值精确匹配（0.00pp 偏差）。

**MMLU 偏差**：

| Dosage | Paper | Rerun | Δ |
|--------|-------|-------|---|
| d000 | 53.79 | 53.79 | 0.00 ✅ |
| d005 | 55.89 | 56.14 | +0.25 ✅ |
| d025 | 57.73 | 56.17 | **-1.56** ⚠️ |
| d050 | 57.44 | 57.25 | -0.19 ✅ |
| d100 | 58.60 | 57.00 | **-1.60** ⚠️ |

d025 和 d100 的 MMLU 偏低 ~1.6pp，可能原因是 evaluate.py 版本差异（rerun 37775 bytes vs reference 37591 bytes），mc_suffix 处理差异只影响 MMLU 不影响 ARC。

**Pattern 分类**：OLMo-2 仍为 **Benefit**，无需修改。rerun MMLU 增幅 3.21pp（paper 4.81pp），ARC 增幅 3.92pp 完全一致。

**建议下一步**：用 37591-byte reference evaluate.py 对 d025/d100 做验证 eval，确认偏差来源。

---
