# ssh exp062 status check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp062-status-check_20260521T172440_result.json`
- **Structured JSON:** [`74c5d431b7f32e65de86.json`](../../sessions/74/74c5d431b7f32e65de86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp062 Decoding Strategy Status

### GPU Utilization

| GPU | Util | Mem Used / Total |
|-----|------|-----------------|
| 0 | 77% | 16.1 / 31.8 GB |
| 1 | 77% | 16.1 / 31.8 GB |
| 2 | 0% | 0 / 31.8 GB |
| 3 | 33% | 1.8 / 31.8 GB |

### Generation Progress

Output files are in `data/&lt;model>-&lt;strategy>/generations_shard0.jsonl`, not `chains_decoding/`.

| Combo | PID | Status | Lines | Est % (~4980 target) | ETA |
|-------|-----|--------|-------|------|-----|
| **qwen3-8b greedy** | 369104 | ALIVE (2h) | 2,159 | **43%** | ~2.6h remaining (~18s/it) |
| **qwen3-8b topk** | 375795 | ALIVE (5min) | 106 | **2%** | just started |
| **qwen3-0.6b greedy** | 357811 | ALIVE (5h) | 4,872 | **~98%** (done) | greedy finished, now running topk |
| **qwen3-0.6b topk** | 357811 | (same PID) | 2,420 | **49%** | in progress |

PID 357811 runs `--strategies greedy topk` sequentially — greedy is essentially complete (4872 lines), now working through topk (2420 lines, ~49%).

PID 369104 also runs `--strategies greedy topk` — still on greedy phase (458/996 seeds per log). PID 375795 is a separate topk-only process (106 lines, just started).

### Feature CSVs

| Combo | Exists? |
|-------|---------|
| qwen3-0.6b-greedy | **YES** (already extracted) |
| qwen3-0.6b-topk | No |
| qwen3-8b-greedy | No |
| qwen3-8b-topk | No |
| mistral-7b-v0.3-topk | **YES** (just extracted by watcher) |

### Watchers

- **PID 372588** (feature watcher): ALIVE (1.1h). Just finished extracting `mistral-7b-v0.3-topk` features. Now waiting on PID 357811 (Qwen3-0.6B) to finish.
- **PID 376120** (anti-duplicate watcher): ALIVE (4min). Monitoring for `[greedy] Done` in qwen8b log — will kill PID 369104 when greedy completes to prevent duplicate topk (since 375795 already handles topk separately).

### Summary

Everything is alive and progressing. Qwen3-0.6B greedy is done (features extracted); its topk is ~49%. Qwen3-8B greedy is at ~43% with ~2.6h remaining; topk just started. The watcher pipeline is healthy and will auto-extract features as each chain completes. GPU 2 is idle/available.

---
