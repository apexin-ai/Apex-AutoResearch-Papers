# exp plan001 step1 api scoring

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_plan001-step1-api-scoring_20260522T072241_result.json`
- **Structured JSON:** [`eb29d649ebfb66771e0f.json`](../../sessions/eb/eb29d649ebfb66771e0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job is running stably. Here's the status summary:

**Plan 001 Step 1 — Running on `seetacloud-rtx6000`**

| Item | Status |
|------|--------|
| Progress | 1/126 conditions done |
| Last completed | claude-3-haiku / mmlu / clean — acc=0.767, 0 errors, 237s |
| Currently scoring | claude-3-haiku / mmlu / prompt_injection (~3 min in) |
| Process | PID 87042, healthy, 6:47 elapsed |
| 502 retries | 2 observed, handled by exponential backoff |
| Estimated total | ~9 hours (126 conditions × ~4 min avg) |
| Timeout | 14h — plenty of headroom |

The job is running fine with checkpointing. Each completed condition writes a JSON file immediately to `artifacts/results/plan001/individual_scores/`, so progress is crash-safe. You can monitor with:

```bash
# Checkpoint count
ls /root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores/ | wc -l

# Latest log
tail -10 /root/runs/cert_manip_resist_eval/plan001_step1_full_v4.log
```

Want me to check back periodically, or wait until you ask?

---
