# ops gpu status and 1 7b rsft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_and_1_7b_rsft_20260517T025818_result.json`
- **Structured JSON:** [`1452715510fda6efa681.json`](../../sessions/14/1452715510fda6efa681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

**总结：**

- **1.7B CED scoring**: 完成，9,042 samples 已就绪，等待 RSFT training
- **s43 test eval**: cuda:1 仍在运行，尚无输出
- **1.7B RSFT training**: 4 卡全满，无法提交。最早可用的 GPU 预计是 cuda:0 或 cuda:1（eval 完成后释放，~11GB 任务应在 1-2h 内结束），或 cuda:2（llama scoring 结束后）

---
