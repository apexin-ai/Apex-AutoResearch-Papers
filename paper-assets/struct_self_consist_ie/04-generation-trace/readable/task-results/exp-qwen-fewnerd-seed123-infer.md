# exp qwen fewnerd seed123 infer

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen_fewnerd_seed123_infer_20260518T082904_result.json`
- **Structured JSON:** [`9043b2bb28fe33e25585.json`](../../sessions/90/9043b2bb28fe33e25585.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inference is running on bjb1-21071, PID 133509. Progress: 552/301,184 prompts (~0.2%). Output directory exists but is still empty (results written at end). At ~10 it/s average, estimated ~8 hours remaining for stochastic sampling, plus ~1 hour for greedy decoding.

The job is running via `merge_and_infer_seed123.sh` which will automatically run `analyze_fewnerd_results.py` after inference completes. Check back with:

```
tail -5 /root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log
```

Once done, I'll read `output/exp_021_fewnerd_n8_seed123/results.json` and produce the seed=123 vs seed=42 comparison summary.

---
