# gpu xnli pipeline 110

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_xnli-pipeline-110_20260522T044346_result.json`
- **Structured JSON:** [`5a5196b0c1cbe15b3a83.json`](../../sessions/5a/5a5196b0c1cbe15b3a83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

XNLI baseline experiment complete. Results summary:

**Asymmetry comparison (ZH→EN − EN→ZH balanced accuracy):**

| Model | XNLI | Conflict | XNLI CI | Conflict CI |
|-------|------|----------|---------|-------------|
| Qwen3-8B | +6.72pp | +5.95pp | [+2.36, +11.73] | [−3.67, +14.81] |
| Llama-3.1-8B | +5.97pp | +11.76pp | [+0.92, +11.33] | [+4.29, +19.57] |

**Core finding**: The ~6pp ZH→EN > EN→ZH asymmetry is **not conflict-specific** — it persists with comparable magnitude on XNLI (a non-conflict NLI task). For Qwen, the XNLI asymmetry is actually larger than the conflict asymmetry. This is a general cross-lingual representation property of these models, likely driven by English-dominant pretraining.

Report registered as `art_20260522_1150c6`.

---
