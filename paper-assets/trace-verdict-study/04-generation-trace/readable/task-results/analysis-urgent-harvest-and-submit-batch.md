# analysis urgent harvest and submit batch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_urgent_harvest_and_submit_batch_20260518T230810_result.json`
- **Structured JSON:** [`30b2378acb9e3728d44f.json`](../../sessions/30/30b2378acb9e3728d44f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。

```
GPU STATUS: 双卡空闲 (0% util, no processes, no tmux)
  GPU0: 49GB VRAM residual but idle — GPU1: fully free

SEED456 (qwen15b_exception_only):
  accuracy = 99.83% [99.58%, 100.0%] — DONE ✓
  vs seed42: 99.83% → 99.83% (差值 0, 完全一致)
  pass F1=0.999, fail F1=0.997

CODELLAMA_SEED123 (codellama13b_full_trace_tail512):
  accuracy = 98.24% [97.48%, 98.99%] — DONE ✓
  vs seed42: 97.5% → 98.24% (+0.74pp, seed123 略优)
  pass F1=0.988, fail F1=0.968

READY FOR SUBMISSION: cuda:0 ✓, cuda:1 ✓
```

---
