# analysis verify ap implementation

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify_ap_implementation_20260513T073738_result.json`
- **Structured JSON:** [`88cbc56917828993b6ed.json`](../../sessions/88/88cbc56917828993b6ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整代码已获取。结论如下：

---

**AP 实现**（L106-110）：`compute_attribution_precision` 签名只接收 `pred_rels`，不接收 `gold_rels`。逻辑 = `有 evidence 字段且非空的预测关系数 / 总预测关系数`。**不比对 gold evidence，只检查 evidence 字段是否非空。**

**Reviewer 判断：正确。** AP 就是格式完整率（predicted relation 是否附带了任何 evidence 文本），不验证 evidence 内容是否与 gold 一致。

**Evi-F1 实现**（L56-103）：`compute_evi_f1` 接收 `pred_rels` + `gold_rels` + `sentences`。将预测/gold evidence 文本都映射回 sentence index，构建 `(relation_key, sid)` 元组集合，计算集合交集的 precision/recall/F1。**真正比对 gold evidence。**

**结论：AP 不是 evidence 质量指标，只是 evidence 覆盖率/格式完整率。** 衡量 evidence 质量应看 Evi-F1。论文中如果将 AP 表述为 evidence accuracy 或 quality metric，措辞需要修正。

---
