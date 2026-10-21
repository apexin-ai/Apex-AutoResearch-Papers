# analysis harvest codellama seed42 final

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_codellama_seed42_final_20260519T022955_result.json`
- **Structured JSON:** [`b2960a926fb00ddf4e8f.json`](../../sessions/b2/b2960a926fb00ddf4e8f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。

```
GPU STATUS: 双卡空闲（0%利用率，无进程）
codellama13b_seed42: accuracy=98.24% [97.5%, 99.0%] — DONE (success)

三 seed 完全一致：seed42=98.24%, seed123=98.24%, seed456=98.24%
```

值得注意：原假设预期 93-96%，实际 98.24% 远超预期，且三个 seed 结果完全相同（0.9824），方差为零。CodeLlama-13B 在 full_trace_tail_512 条件下表现极其稳定。

---
