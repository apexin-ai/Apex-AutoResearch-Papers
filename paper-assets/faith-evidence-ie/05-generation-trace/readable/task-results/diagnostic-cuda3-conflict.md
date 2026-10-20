# diagnostic cuda3 conflict

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnostic_cuda3_conflict_20260515T162018_result.json`
- **Structured JSON:** [`2c6b8ae04023a0824250.json`](../../sessions/2c/2c6b8ae04023a0824250.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。报告已写入 `artifacts/cuda3_diagnostic.md`。

**结论**：两个进程都活着，GPU 3 显存 87.5% (28548/32607 MiB)，确实存在争用——eval 推理速度从 ~50s/batch 退化到 ~90s/batch（train 启动后）。但没有 OOM，建议不杀进程，让 eval 自然跑完（预计 ~1-1.5h），之后训练速度会恢复。

额外信息：ckpt-80 评估已出结果，F1=0.4456, Evi-F1=0.8034, EDCR=0.6409。

---
