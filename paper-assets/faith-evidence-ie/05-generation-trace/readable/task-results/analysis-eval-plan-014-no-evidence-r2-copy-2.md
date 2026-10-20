# analysis eval plan 014 no evidence r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_plan_014_no_evidence_r2_20260516T041450_result.json`
- **Structured JSON:** [`28d34486ef5cdd9fc04a.json`](../../sessions/28/28d34486ef5cdd9fc04a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**rel_f1 = 0.4876**, Ign-F1 = 0.4721

与 evidence-SFT baseline (rel_f1=0.4106) 对比，**evidence tax = +7.7 个 F1 点（+18.8%）**。去掉 evidence 生成后关系抽取显著提升，与之前中间 eval 的 0.4893 高度一致（差 0.17%），结果可复现。

其他要点：
- No-evidence 模式确认生效：raw_output 只含 head/relation/tail，evi_pred_total=0
- 格式合规率 99.3%，precision/recall 基本平衡（0.490/0.485）
- 截断率 31.2%（307/985），即使不生成 evidence 也有不少截断
- 无 W&B run ID
- 结论：**Positive result**

分析已写入 `artifacts/eval_plan_014_no_evidence_r2_analysis.md`。

---
