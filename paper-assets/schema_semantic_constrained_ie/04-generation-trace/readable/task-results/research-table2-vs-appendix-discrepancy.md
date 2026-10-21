# research table2 vs appendix discrepancy

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_table2_vs_appendix_discrepancy_20260520T140637_result.json`
- **Structured JSON:** [`c28016c1c27c23e20ba6.json`](../../sessions/c2/c28016c1c27c23e20ba6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 根因结论

**根因是 `compiler/type_mask_processor.py` 代码版本不同。**

- w5 运行于 May 15-16，使用旧版 type_mask_processor（544 行）
- May 18 发生重大 grammar fix，代码从 544 行扩展到 938 行，新增 entity type continuation masking、role prefix/continuation masking 等 token 级约束
- d065 运行于 May 20，使用新版

新版在 generation 时强制 domain-range 约束（如 `_mask_tail_type` 根据当前 relation + head_type 限制 allowed tail types），导致：

| 指标 | w5 (旧代码) | d065 (新代码) | 原因 |
|---|---|---|---|
| DR% | 0.21% (33个) | 0% | 新版 generation 时即满足 DR 约束 |
| R-F1 | 43.78 | 44.70 | entity type 分配改变影响 gold matching |
| E-F1 | 83.94 | 84.71 | 同上 |

205/998 (20.5%) 的 sample 输出不同。所有命令行参数（model、dataset、seed、decoding_strategy、max_new_tokens）完全一致，eval 脚本也无问题。

完整报告已注册为 artifact `root_cause_w5_vs_d065`。

---
