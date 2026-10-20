# ops check plan014 noevi completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_plan014_noevi_completion_20260516T162119_result.json`
- **Structured JSON:** [`e87d36c195bdea54d110.json`](../../sessions/e8/e87d36c195bdea54d110.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新为 DONE，cron 已删除。

**结果摘要：**

| 指标 | 值 |
|------|-----|
| ign_f1 | **0.4721** |
| ign_precision / recall | 0.4654 / 0.4791 |
| format_compliance | 99.3% |
| n_truncated | 307/985 (31.2%) |
| inference_time | 6904s (~115min) |

**4B Evidence Tax：-7.5pp ign_f1**（with-evidence 0.3974 vs no-evidence 0.4721）。要求模型输出 evidence 使关系抽取性能显著下降。

---
