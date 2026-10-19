# ops p0 final harvest v2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p0-final-harvest-v2_20260516T121238_result.json`
- **Structured JSON:** [`3dcface089fa768bf29e.json`](../../sessions/3d/3dcface089fa768bf29e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== P0 FINAL RESULT ===
obs_only seed44: RUNNING (8/10 tasks done, partial 10/80 successes = 12.5%)
argmin seed44:   RUNNING (7/10 tasks done, partial 5/70 successes = 7.1%)

Fisher test: BLOCKED — 等两个实验完成

=== P0 PARTIAL (seed44 interim) ===
| task                  | obs_only | argmin |
|-----------------------|----------|--------|
| alphabet_soup         | 0/10     | 0/10   |
| cream_cheese          | 1/10     | 0/10   |
| salad_dressing        | 2/10     | 1/10   |
| bbq_sauce             | 2/10     | 2/10   |
| ketchup               | 1/10     | 1/10   |
| tomato_sauce          | 1/10     | 1/10   |
| butter                | 2/10     | 0/10   |
| milk                  | 1/10     | —      |
| subtotal (completed)  | 10/80    | 5/70   |

估计剩余时间:
- obs_only: ~2 tasks → ~2.5h
- argmin: ~3 tasks → ~4.5h

=== 3-SEED PARTIAL TABLE ===
| seed | obs_only | argmin | Δ      |
|------|----------|--------|--------|
| 42   | 22/100   | 12/100 | +10pp  |
| 43   | 16/100   | 17/100 | -1pp   |
| 44   | ~12-13%? | ~7%?   | TBD    |

=== SERVER STATUS ===
bjb1-18228: 2 GPUs — P0 obs_only_norm02_seed44 + argmin_seed44 (both ~10.5h elapsed)
bjb1-32546: 6 GPUs — vla_mean_s44, obs_only_norm03_s44, scalar_s44, obs_only_norm01_s44, obs_only_default_s44, obs_only_norm02_s45
bjb2-28827: 6 GPUs — argmin_s45, vla_only_s45, perdof_norm02_s45, scalar_s45, obs_only_default_s45, vla_mean_s45 (4 new JSONs completed)
bjb2-40593: 1 GPU  — perdof_default_seed44
```

P0 两个实验都在正常推进，没有 error/hang。argmin 比 obs_only 慢一个 task（7 vs 8/10）。预计 argmin 最后完成约 4-5 小时后可跑 Fisher test。

---
