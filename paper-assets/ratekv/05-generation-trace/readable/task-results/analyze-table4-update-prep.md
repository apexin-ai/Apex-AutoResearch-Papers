# analyze table4 update prep

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_table4_update_prep_20260515T181250_result.json`
- **Structured JSON:** [`29e1af08445fb2e7b134.json`](../../sessions/29/29e1af08445fb2e7b134.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模板已产出并注册 (`art_20260515_ba2ca9`)。

关键发现：

- **Llama k=2 行已填入**：avg delta 从 -1.0 改善到 -0.1，所有 4 个 task 都大幅改善（ARC-C 改善最大，+1.9 pts）
- **Yi/Mistral 行留占位符**（`__YI_*__`, `__MI_*__`），等实验结果到位后替换
- **Caption 更新建议**：加注 "each model evaluated at its profiling-derived optimal k"
- **Provenance 更新清单**：C168-C172 五条 claim 的具体更新动作已列出

模板路径：`artifacts/table4_k2_update_template.md`

---
