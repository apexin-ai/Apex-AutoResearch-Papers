# analysis temperature cost estimate

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_temperature-cost-estimate_20260523T080404_result.json`
- **Structured JSON:** [`9c9977e5b7a79933c837.json`](../../sessions/9c/9c9977e5b7a79933c837.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. The validation file has real per-model token counts from actual API calls. Let me compile the estimate.

Key findings from the codebase:

**Prompt structure** (pairwise judge scoring):
- System prompt: ~80 tokens (fixed)
- User message: question + response_a + response_b (~180-210 tokens, varies by question)

**Empirical token counts** (from `api_adapter_validation.json`):

| Model | Input tokens | Output tokens |
|-------|-------------|---------------|
| claude-opus-4 | 290 | 134 |
| gpt-5.5 | 262 | 195 |
| gemini-pro | 263 | 1020 (verbose/truncated) |
| gpt-4.1 | 263 | 101 |
| claude-sonnet-4 | 290 | 106 |
| gemini-flash | 263 | 88 |
| claude-3-haiku | 290 | 109 |
| gpt-4o-mini equiv | 263 | 60 |

---

```
=== Temperature Experiment Cost Estimate ===
Per-call avg tokens: input=275, output=~130 (median, excl. gemini-pro outlier)

Calls per model: 4 temps × 1000 questions × 3 repeats = 12,000

Full experiment (9 models × 108K calls):

  Model               | In tok | Out tok | $/call   | Subtotal
  ---------------------|--------|---------|----------|----------
  claude-opus-4-6      |  290   |  160    | $0.0164  | $196.20
  gpt-5.5              |  265   |  235    | $0.0060  |  $72.30
  claude-sonnet-4-6    |  290   |  130    | $0.0028  |  $33.84
  gemini-3.1-pro-prev  |  265   |  300    | $0.0018  |  $21.33
  gpt-4.1              |  265   |  120    | $0.0015  |  $17.88
  claude-3-haiku       |  290   |  130    | $0.0002  |   $2.82
  gpt-4.1-mini         |  265   |   75    | $0.0002  |   $2.71
  gpt-4.1-nano         |  265   |   80    | $0.0001  |   $0.70
  gemini-3.5-flash     |  265   |  105    | $0.0001  |   $0.62
  ---------------------------------------------------------
  Total cost: ~$348                    (≈$350 conservative)

  Cost dominated by:
    claude-opus-4-6: $196 (56%)
    gpt-5.5:          $72 (21%)
    top-2 = 77% of total cost

Pilot (3 cheapest × 36K calls):
  Models: gpt-4.1-nano ($0.70) + gemini-3.5-flash ($0.62) + claude-3-haiku ($2.82)
  Total cost: ~$4.14

Timeline estimate:
  Parallel (all 9 models, 25 workers each):
    Bottleneck = claude-opus-4-6 (~14.5s/call × 480 batches ≈ 2 hours)
  Sequential: ~8-10 hours
  Pilot (3 cheap, parallel): ~20 min

Recommendation: pilot first ($4, 20 min)
  → validate temperature actually affects scores before spending $350
  → if opus needed, consider dropping repeats from 3→1 first (saves $131)
  → without opus: full experiment = ~$152 (remove opus saves 56%)
```

**Notes**:
- Output tokens buffered +20% for higher-temperature verbosity
- gemini-pro output tokens estimated at 300 (validation showed 1020 due to verbose/truncated JSON — real cost could be higher)
- Prices are direct API rates; OpenRouter pass-through may add small markup
- `gpt-5.5` doesn't support `temperature=0` (code already has `_NO_TEMP_ZERO` set), will need `{0.01, 0.3, 0.7, 1.0}` or skip temp=0 for that model

---
