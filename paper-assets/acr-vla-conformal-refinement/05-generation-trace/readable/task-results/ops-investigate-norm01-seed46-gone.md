# ops investigate norm01 seed46 gone

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate-norm01-seed46-gone_20260518T000653_result.json`
- **Structured JSON:** [`49388fd5980bd1418fdc.json`](../../sessions/49/49388fd5980bd1418fdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry already has `conclusion: "killed"` which is correct.

**Summary:**

| Field | Value |
|-------|-------|
| Server | bjb1-18228 (cuda:3) |
| Status | Process killed mid-run (task 5/10, ~May 17 20:53) |
| Cause | Unknown — no OOM, no kernel kill. Likely external termination or server restart |
| Output JSON | Does not exist |
| Registry | Set back to QUEUED for retry |

**Partial results before death** (not authoritative — incomplete):
- alphabet_soup: 0%, cream_cheese: 10%, salad_dressing: 30%, bbq_sauce: 20%

**Action needed:** Retry this experiment on next available GPU slot on bjb1-18228 (or elsewhere). Same command:
```
python evaluate.py --benchmark object --mode crm_obs_only \
  --crm_checkpoint /root/autodl-tmp/checkpoints/crm_v3_norm/obs_only/crm_best.pt \
  --max_correction_norm 0.1 --seed 46 \
  --output_file logs/eval_object_obs_only_norm01_seed46.json
```

---
