# infra gpu check b11

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_gpu-check-b11_20260518T004017_result.json`
- **Structured JSON:** [`8b6dcd04eb521b3e8f1e.json`](../../sessions/8b/8b6dcd04eb521b3e8f1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Summary

### Subtask A: GPU & Experiment Progress

| Session | Current Job | Progress | Notes |
| --- | --- | --- | --- |
| **tc_fix** | 1/3: Pythia-2.8B t=0.5 (top_p=0.9) | 62% (612/995 seeds), ~1h08m left | First job still running |
| **indep_seed** | 2/4: OLMo-2-1B indepB | 19% (93/495 seeds) | Job 1 **completed**: Pythia-2.8B indepA (500 seeds, 2338 records → `data/independent_seed/pythia-2.8b-indepA/generations_shard0.jsonl`, 80 skipped) |

**GPU**: RTX 5090, 90% utilization, 9.8/32.6 GB VRAM, 2 python processes (one per session).

### Subtask B: Qualitative Example Extracted

Written to `artifacts/_project/analysis/qualitative_example_seed5.md`.

Seed 5 = Abraham Lincoln article. Key degradation pattern across gen-0 to gen-4:
- **TTR**: 0.660 → 0.260 (60% collapse)
- **Hapax ratio**: 0.555 → 0.178
- **Text**: Gen-0 is coherent Wikipedia prose; by gen-3/4 it degenerates into repetitive lists ("Douglas was the Republican nominee for President in 1884... 1888... 1892..."), an excellent qualitative example of model collapse.

---
