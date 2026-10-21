# ops extract k07 results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_k07_results_20260518T045802_result.json`
- **Structured JSON:** [`73fda903a9ca6bca4376.json`](../../sessions/73/73fda903a9ca6bca4376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated to DONE, cron deleted.

## OpenVLA k=0.7 Random Pruning Results (256→179 tokens)

**Overall SR: 49.0% (245/500)**

| Task | SR | Successes |
|---|---|---|
| alphabet soup | 74% | 37/50 |
| orange juice | 76% | 38/50 |
| ketchup | 68% | 34/50 |
| salad dressing | 64% | 32/50 |
| tomato sauce | 62% | 31/50 |
| bbq sauce | 46% | 23/50 |
| milk | 40% | 20/50 |
| chocolate pudding | 32% | 16/50 |
| cream cheese | 18% | 9/50 |
| butter | 10% | 5/50 |

**Degradation curve so far:**
- k=1.0 (baseline, 256 tokens): **74.0%**
- k=0.7 (179 tokens): **49.0%** (−25.0 pp, −33.8%)
- k=0.5 (128 tokens): **37.4%** (−36.6 pp, −49.5%)

Degradation is non-linear — removing 30% of tokens already costs 25 pp. The curve is steeper than linear, confirming significant redundancy is limited. Tasks with small/hard-to-distinguish objects (butter, cream cheese) are hit hardest.

---
