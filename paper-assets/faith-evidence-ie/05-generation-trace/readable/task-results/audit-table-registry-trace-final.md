# audit table registry trace final

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table-registry-trace-final_20260523T191624_result.json`
- **Structured JSON:** [`91367ad384116199261c.json`](../../sessions/91/91367ad384116199261c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计已完成。最终结果写入 `artifacts/final_audit_w2_tables.md`。

**汇总：212 cells，200 ✅ (94.3%)，12 ⚠️ (5.7%)，0 ❌**

12 个 ⚠️ 按优先级：

1. **LLaMA test 行混用 v1/v3 评估**（2 cells）— truncation 和 evi_f1_joint 来自 v1，Ign-F1 来自 v3。建议统一用 v3 值。
2. **Flat-NLI 消融混源**（4 cells）— Rel-F1 用 D076-compliant reeval，Evi-F1/EDCR 用旧 eval。建议用单一协议重跑或标注。
3. **8B RSFT 跨表不一致**（3 cells）— Table 2 用 d102 checkpoint 的 Ign-F1，tab:cross_detail 用 plan_006 的 Evi-F1/EDCR。不同 checkpoint。
4. **8B/LLaMA inference-time tax 无法精确复现**（2 cells）— 使用 registry 预计算值，原始 metrics 计算略有偏差。
5. **1.7B RSFT Rel-F1 四舍五入 & variance 压缩比**（1 cell each）— 微小舍入差异。

需要我处理其中某项，还是这份审计报告直接归档？

---
