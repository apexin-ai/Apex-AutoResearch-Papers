# diagnosis decoding strategy check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_decoding_strategy_check_20260521T063730_result.json`
- **Structured JSON:** [`330abd544886b00de11b.json`](../../sessions/33/330abd544886b00de11b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**STATUS: PARTIAL** — 实验正在运行，无错误。

| 组合 | 状态 |
|------|------|
| pythia-2.8b × greedy | 运行中 38/995 (~3.8%), ETA ~3.8h |
| pythia-2.8b × topk | 待 greedy 完成后自动运行 |
| olmo-2-1b × greedy | 运行中 59/995 (~5.9%), ETA ~2.25h |
| olmo-2-1b × topk | 待 greedy 完成后自动运行 |
| qwen3-1.7b × greedy | **未启动** |
| qwen3-1.7b × topk | **未启动** |

GPU 2、3 空闲。Qwen3-1.7B 需要手动启动。诊断已写入 `artifacts/_project/analysis/decoding_strategy_diagnosis.txt`。

---
