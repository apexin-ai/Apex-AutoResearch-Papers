# analyze batch analyzing 6exp

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_batch-analyzing-6exp_20260523T070454_result.json`
- **Structured JSON:** [`733c076696d935a60b19.json`](../../sessions/73/733c076696d935a60b19.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 6 experiments updated to DONE. Note: the registry auto-set eval-supp-obj-adapt-s42-r2 conclusion to "negative" because adaptive CRM (77.5%) didn't improve over VLA-only (79%).

```
exp_id                              | conclusion | SR     | notes
------------------------------------|------------|--------|------
eval-object-vla-only-wrapper-s42-r2 | success    | 79.0%  | VLA-only baseline, 158/200
eval-object-vla-only-wrapper-s43-r2 | success    | 77.0%  | VLA-only baseline, 154/200
eval-object-vla-only-wrapper-s44-r2 | success    | 77.5%  | VLA-only baseline, 155/200
eval-supp-obj-reconvla-s42          | success    | 79.0%  | reconvla K=10, 158/200
eval-supp-obj-adapt-s42-r2          | negative   | 77.5%  | adaptive CRM tau=0.074855, 155/200; trigger_rate=70.2%, no gain over VLA-only
eval-supp-goal-crm005-s42           | success    | 85.5%  | crm_obs_only norm=0.05 on Goal suite, 171/200
```

VLA-only Object baseline 3-seed mean: **77.8% ± 1.1%**. Reconvla matches at 79%. Adaptive CRM on Object doesn't improve (77.5% = within noise). Goal suite CRM at 85.5% is the strongest result.

---
