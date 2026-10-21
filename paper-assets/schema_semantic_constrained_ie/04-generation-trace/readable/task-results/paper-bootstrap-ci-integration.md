# paper bootstrap ci integration

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bootstrap-ci-integration_20260522T084539_result.json`
- **Structured JSON:** [`051938d51e12309ef770.json`](../../sessions/05/051938d51e12309ef770.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成：

1. **Line 106-107**（composability 段落）：插入一句 bootstrap 结论，带 `% exp_ids` 注释标注数据来源
2. **Line 143**（Table 2 caption）：替换旧的 `p>0.05` 统计描述为 Bonferroni 校正后的精确结果

关键数据：4 对比较均未通过 Bonferroni 校正（α/4=0.0125），最小 p=0.014（Qwen-DocRED），所有 95% CI ⊆ [-0.76, +0.22]pp。

---
