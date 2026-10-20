# experiment disambiguation prompting

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_disambiguation_prompting_20260522T221751_result.json`
- **Structured JSON:** [`4fe33448d31a7d63f2ac.json`](../../sessions/4f/4fe33448d31a7d63f2ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both episode and judge API calls failed with `Insufficient balance`. The experiment data is invalid — all 900 episodes are empty error traces, and all 900 judgments defaulted to "none" because the judge calls also failed.

**To proceed**, the OpenRouter account needs credits recharged. Once funded:

```bash
# Clean failed data, then re-run
rm disambiguation_intervention/episodes/episodes.jsonl
rm disambiguation_intervention/judgments/judgments.jsonl
rm disambiguation_intervention/results.json

# Re-run
source .venv/bin/activate
python disambiguation_intervention/run_disambiguation.py --phase episodes
python disambiguation_intervention/run_disambiguation.py --phase judge
python disambiguation_intervention/analyze_disambiguation.py
```

The scripts themselves are complete and correct — resume logic will skip already-completed episodes, so you can also just delete the bad data and re-run without changes. Want me to do anything else while waiting for credits?

---
