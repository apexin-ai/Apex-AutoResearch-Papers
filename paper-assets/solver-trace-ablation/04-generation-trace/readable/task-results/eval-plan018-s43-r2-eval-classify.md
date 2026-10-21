# eval plan018 s43 r2 eval classify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan018-s43-r2-eval-classify_20260514T164803_result.json`
- **Structured JSON:** [`89fdc43aece5cc9308f7.json`](../../sessions/89/89fdc43aece5cc9308f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Results summary:

```
eval_prove_rate: 0.88
eval_mean_isr: 0.0506
eval_proved_only_isr: 0.0575
n_proved: 88
h7_count: 0 / h7_rate: 0.0%
h1_count: 82 / h1_rate: 93.2%
genuine_count: 6 / genuine_rate: 6.8%
```

Conclusion: **negative** — as expected for Random condition. H1 dominant (93.2%), near-zero genuine reasoning (6.8%). High prove rate (88%) achieved almost entirely via conclusion-in-premise hacking. ISR extremely low (0.0575). Status kept at ANALYZING for main agent.

---
