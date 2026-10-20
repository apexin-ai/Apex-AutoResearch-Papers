# audit trace dpo 3ep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_trace-dpo-3ep_20260524T053134_result.json`
- **Structured JSON:** [`eef0bc9983f34b5f3e5f.json`](../../sessions/ee/eef0bc9983f34b5f3e5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**源文件确认**：`/root/autodl-tmp/eval_results/dpo_rebuilt_3ep_eval/metrics.json`（2026-05-23 21:37 修改）
- `f1` = 0.31446 → **31.45**（paper 值正确）

**完整 metrics**：

| 指标 | 值 |
|------|-----|
| Rel-F1 | 31.45 |
| Ign-F1 | 30.76 |
| Evi-F1 (TP) | 84.84 |
| Evi-F1 (Joint) | 24.51 |
| EDCR | 75.03 |
| Precision | 29.39 |
| Recall | 33.81 |

**Registry 补录**：已在 `dpo_rebuilt_3ep_eval` 的 metrics 中添加 `rel_f1: 0.3145`。

---
