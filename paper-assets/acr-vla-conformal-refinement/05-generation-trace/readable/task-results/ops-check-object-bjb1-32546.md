# ops check object bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-object-bjb1-32546_20260515T032854_result.json`
- **Structured JSON:** [`36cc7047fbbc8d679710.json`](../../sessions/36/36cc7047fbbc8d679710.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the summary:

## 6 Object Eval Experiments on bjb1-32546

| GPU | Exp ID | PID | Progress | Status |
|-----|--------|-----|----------|--------|
| cuda:0 | eval-reconvla-object | 9659 | 0/10 (T1 rollout 5/10, 0 success) | Running |
| cuda:1 | eval-acr-object-v4-perdof | 11116 | 0/10 (T1 rollout 5/10, 0 success) | Running |
| cuda:2 | eval-acr-object-v4-obs-only | 13806 | 0/10 (model loaded, no rollouts yet) | Running |
| cuda:3 | eval-acr-object-v4-scalar | 14012 | 0/10 (model loaded, no rollouts yet) | Running |
| cuda:4 | **eval-vla-only-object** | 17222 | **3/10** — T1=0%, T2=10%, T3=20% (avg 10.0%) | Running |
| cuda:5 | **eval-vla-mean-object** | 18814 | 0/10 (model loaded, no rollouts yet) | Running |

### Actions taken
1. **Registry**: Created entries for eval-vla-only-object and eval-vla-mean-object with hypotheses, specs, and metrics
2. **Metrics**: Updated all 6 experiments with latest progress from logs
3. **Cron**: Created hourly monitoring (`:23`) for all 6 experiments — checks logs, updates registry, marks DONE when finished

### Notes
- eval-vla-only-object (cuda:4) is the furthest ahead at 3/10 tasks, showing very low success (10% avg) — expected for K=1 single sample baseline
- cuda:0/1 are both on T1 (alphabet_soup), which appears difficult (0% so far for both reconvla and perdof)
- cuda:2/3/5 just started — model loaded but no rollout output yet
- ETA: ~8-10h for all experiments to finish (200 rollouts per experiment at ~3 min/rollout)

---
