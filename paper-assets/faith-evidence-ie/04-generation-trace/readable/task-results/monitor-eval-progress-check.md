# monitor eval progress check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_eval_progress_check_20260516T021737_result.json`
- **Structured JSON:** [`6b1b90272541ecc72619.json`](../../sessions/6b/6b1b90272541ecc72619.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

| 实验 | GPU | 进度 | ETA (UTC) | 状态 |
|------|-----|------|-----------|------|
| eval_flat_nli_s44 | cuda:0 | **238/247 (96%)** | ~02:25 (~7min) | 即将完成 |
| eval_flat_nli_seed45 | cuda:3 | **196/247 (79%)** | ~03:03 (~45min) | 正常 |
| eval_rsft_ced_s45 | cuda:2 | **69/247 (28%)** | ~04:18 (~2h) | 正常 |
| eval_rsft_ced_s43 | cuda:1 | **5/247 (2%)** | ~05:19 (~3h) | 刚启动 |

4 个 GPU 利用率 39-51%，显存各占 ~11GB/32GB，全部正常。实际每个 eval 总耗时约 3h（~40-50s/batch × 247 batches），比预估的 1h 慢——`--no-quantize` 全精度推理 + batch_size=4 是主因。无异常，无卡死。

---
