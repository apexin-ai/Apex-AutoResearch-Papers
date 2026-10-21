# ops collect reconvla bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect-reconvla-bjb2-40593_20260515T043904_result.json`
- **Structured JSON:** [`b2e04860e7e395c8dacf.json`](../../sessions/b2/b2e04860e7e395c8dacf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The log is being buffered - printing every 5 rollouts. Here's the current state:

```
exp_id: reconvla-object-n20 (bjb2-40593)
Status: RUNNING (PID 211962, uptime ~3h, started 09:48 CST)
Tasks: 0/10 completed (still on T1)
Per-task (partial):
  T1 pick_up_the_alphabet_soup_and_place_it_in_the_basket: rollout 10/20 done, 0% (0/10 so far)
  T2-T10: not started
Overall: N/A — too early

ETA: ~15 min/rollout × 200 total = ~50h. ~47h remaining.
```

**Notes:**
- Process started ~3h ago (09:48 CST), not 12+ hours as stated. Either the previous run was a different process, or the estimate was off.
- No results file written yet (`artifacts/reconvla_object.json` only created on completion).
- Registry has `eval-reconvla-object` on bjb1-32546 (different server, n=10). This bjb2-40593 n=20 run has **no independent registry entry**.
- T1 alphabet_soup is 0/10 success so far — consistent with other experiments where this task scores 0%.

Want me to create a registry entry for this experiment (e.g. `eval-reconvla-object-n20-bjb2`)?

---
