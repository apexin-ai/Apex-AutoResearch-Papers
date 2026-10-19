# ops p0 seed44 harvest and full scan

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-seed44-harvest-and-full-scan_20260516T112507_result.json`
- **Structured JSON:** [`a794d67580f993ff78ac.json`](../../sessions/a7/a794d67580f993ff78ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the report:

```
=== P0 RESULT ===
obs_only seed44: RUNNING — 7/10 tasks done, ~3h remaining
  Partial: 9/70 so far (12.9%)
  [alphabet_soup 0/10, cream_cheese 1/10, salad_dressing 2/10,
   bbq_sauce 2/10, ketchup 1/10, tomato_sauce 1/10, butter 2/10]
  Currently: milk (task 8/10)

argmin seed44: RUNNING — 6/10 tasks done, ~4h remaining
  Partial: 5/60 so far (8.3%)
  [alphabet_soup 0/10, cream_cheese 0/10, salad_dressing 1/10,
   bbq_sauce 2/10, ketchup 1/10, tomato_sauce 1/10]
  Currently: butter (task 7/10)

=== 3-SEED FISHER DATA (incomplete) ===
| seed | obs_only 0.2 | argmin    |
|------|-------------|-----------|
| 42   | 22%         | 12%       |
| 43   | 16%         | 17%       |
| 44   | ~13% (7/10) | ~8% (6/10)| ← RUNNING, ETA ~3-4h

=== bjb1-18228: 4/6 GPU active ===
- cuda:0  PID 474319  obs_only norm01 seed45    2.4h  task 1/10
- cuda:1  PID 452987  perdof seed44             6.5h  4/10 tasks done
- cuda:2  PID 428411  P0 obs_only norm02 seed44 10h   7/10 tasks done
- cuda:3  PID 428122  P0 argmin seed44          10h   6/10 tasks done

=== bjb1-32546: 6/6 GPU active ===
- cuda:0  PID 226878  scalar seed44 r2           4.3h
- cuda:1  PID 212665  vla_mean seed44            6.4h
- cuda:2  PID 220786  obs_only norm03 seed44     5.4h
- cuda:3  PID 233553  obs_only norm02 seed45     3.7h
- cuda:4  PID 227086  obs_only norm01 seed44     4.3h
- cuda:5  PID 229751  obs_only default seed44    4.2h

=== bjb2-28827: 6/6 GPU active, cuda:3 conflict RESOLVED ===
- cuda:0  PID 224628  scalar seed45              2.8h
- cuda:1  PID 222830  perdof norm02 seed45       2.9h
- cuda:2  PID 248661  vla_mean seed45            0.2h
- cuda:3  PID 242264  obs_only default seed45    0.7h  ← conflict resolved
- cuda:4  PID 221413  vla_only K=1 seed45        2.9h
- cuda:5  PID 215941  argmin seed45              3.5h

=== bjb2-40593: 1/1 GPU active ===
- cuda:0  PID 316387  perdof default seed44      4.1h  task 2/10

=== NEWLY COMPLETED (bjb2-28827) ===
- eval_object_perdof_norm03_r3.json  (19:02)
- eval_object_perdof_norm02_seed43_r3.json (18:38)
```

All 19 GPUs across 4 servers fully utilized. P0 seed44 experiments are ~70% and ~60% done respectively — expect results in 3-4 hours.

---
