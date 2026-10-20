# write composability table update

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_composability_table_update_20260515T230519_result.json`
- **Structured JSON:** [`f2add6306feaa07b9d9e.json`](../../sessions/f2/f2add6306feaa07b9d9e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。变更摘要：

**section5_scierc_draft.tex:**
- **Table 5** 扩展为 4 blocks (Qwen ZS/FT + Llama ZS/FT)，新增 Model/Setting 列，用 `\multirow` + `\cmidrule` 分组，`\resizebox` 适配列宽
- **段落文字** 分 Qwen/Llama 两段描述 FT 结果，新增跨模型一致性总结（DR ≤ 0.09%, R-F1 ±0.1pp），Claim 3 结论升级为 "across two model families"
- **Secondary observations** 更新为双模型 CF 对比（Qwen 9.82→1.18pp, Llama 6.32→0.46pp）和双模型 ZS F1 中性验证（含 Llama -0.14pp 如实报告）
- 所有数值附 exp_id 注释，保留 "one dataset and one fine-tuning method (LoRA)" 限定语

**main.tex Limitations:**
- Line 70 从单模型 "DR=0%" 更新为 "both Qwen3-8B and Llama-3.1-8B (DR ≤ 0.09%, R-F1 loss <0.1pp)"，CF 拆分为 Qwen 1.18% / Llama 0.46%

---
