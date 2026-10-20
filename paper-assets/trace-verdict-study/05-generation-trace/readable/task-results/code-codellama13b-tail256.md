# code codellama13b tail256

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_codellama13b_tail256_20260518T013828_result.json`
- **Structured JSON:** [`93a73f34080f417ab71c.json`](../../sessions/93/93a73f34080f417ab71c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，正在 cuda:0 上运行。

- **Condition**: `full_trace_tail_256`
- **模型**: CodeLlama-13b-Instruct-hf
- **Steps**: 444 total, ~5s/it（比 tail-512 的 ~13s/it 快约 2.5x）
- **预计训练时间**: ~37 分钟
- **日志**: `~/runs/trace-verdict-study/codellama13b_full_trace_tail256_seed42.log`
- 训练完成后自动执行 eval

---
