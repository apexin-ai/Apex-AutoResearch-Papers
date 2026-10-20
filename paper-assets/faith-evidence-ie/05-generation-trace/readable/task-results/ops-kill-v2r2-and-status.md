# ops kill v2r2 and status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_v2r2_and_status_20260516T120838_result.json`
- **Structured JSON:** [`cd5f539c7e4909e7f8d3.json`](../../sessions/cd/cd5f539c7e4909e7f8d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**Kill 完成**: PID 339089 + 子进程 339094/339093 全部已终止，GPU 0 已释放。

**当前 GPU 分配**:

| GPU | 显存占用 | 实验 | PID |
|-----|---------|------|-----|
| **0** | **0 MiB / 32GB — 空闲** | — | — |
| 1 | 23.3 GB / 32GB | `plan_006_qwen3_1_7b_no_evidence_eval_v3` (PID 337844) + `plan_016_llama_3_1_8b_sft_eval` (PID 340116) | 337844, 340116 |
| 2 | 18.4 GB / 32GB | `qwen3_8b_no_evidence_eval_v2` (PID 335357) | 335357 |
| 3 | 17.9 GB / 32GB | `plan_016_llama_3_1_8b_no_evidence_eval` (PID 339692) | 339692 |

**空闲 GPU**: cuda:0（完全空闲）

**注意**: GPU 1 上跑了两个 eval（1.7B v3 + 8B sft），1.7B 只占 ~5.4GB 所以能共存，但 8B 占 ~17.9GB，总计 23.3GB，还有余量。

---
