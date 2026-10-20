# experiment llama folio multiseed cuda1

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llama-folio-multiseed-cuda1_20260522T105851_result.json`
- **Structured JSON:** [`bbad6aa17efbe5e34d78.json`](../../sessions/bb/bbad6aa17efbe5e34d78.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。3 个 seed 均已跑完：

- `SENTINEL_LLAMA8B_FOLIO_SEED123_DONE`
- `SENTINEL_LLAMA8B_FOLIO_SEED456_DONE`
- `SENTINEL_LLAMA8B_FOLIO_SEED789_DONE`
- `SENTINEL_LLAMA8B_FOLIO_MULTISEED_DONE`

LLaMA-3.1-8B 模型较小，3 个 seed × 204 FOLIO 跑得很快（总共约 1 分钟内完成）。结果已保存在：
- `results/multi_seed/llama8b_folio_seed123/`
- `results/multi_seed/llama8b_folio_seed456/`
- `results/multi_seed/llama8b_folio_seed789/`

注意日志显示 SICA=0.0%, SC=0.0%——指标全零，可能需要检查 LLaMA-3.1-8B 在 FOLIO 上的输出质量是否正常。

---
