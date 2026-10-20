# ops redocred rsft eval r2 cuda1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_redocred_rsft_eval_r2_cuda1_20260516T162430_result.json`
- **Structured JSON:** [`5cbf884cef3bdcccedc0.json`](../../sessions/5c/5cbf884cef3bdcccedc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 正常运行：

- **PID**: 363322 (子进程)，cuda:1 占用 10230 MiB
- **状态**: 模型加载成功，SFT adapter 已合并，推理进行中 (1/124 batches, ~33s/batch)
- **数据**: 493 eval docs, 7473 gold triples
- **预计耗时**: ~68 分钟 (124 batches × 33s)

修正了原指令中的模型路径错误（`models/Qwen/Qwen3-4B` → `models/Qwen3-4B`）。Registry 已更新为正确命令和 PID。

---
