# eval contamination 60 uniform seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_contamination_60_uniform_seed42_20260516T010553_result.json`
- **Structured JSON:** [`da009b955b5f4c78c570.json`](../../sessions/da/da009b955b5f4c78c570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 完成。

```json
{"eval_perplexity": 17.766, "eval_loss": 2.8773, "checkpoint_path": "output/models/contamination_60_uniform_seed42/final", "eval_method": "eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl", "eval_samples": 5000, "eval_tokens": 4077068}
```

对比 ρ=0.4 uniform baseline PPL=17.694，ρ=0.6 uniform PPL=17.766，差异仅 +0.072（+0.41%）。污染比例从 0.4 升到 0.6 对 uniform weighting 的影响很小。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "data": {
    "eval_perplexity": 17.766,
    "eval_loss": 2.8773,
    "checkpoint_path": "output/models/contamination_60_uniform_seed42/final",
    "eval_method": "eval_perplexity.py sliding-window (stride=1024, max_length=2048, fp16) on data/human/eval_holdout.jsonl",
    "eval_samples": 5000,
    "eval_tokens": 4077068
  }
}
```

</details>

---
