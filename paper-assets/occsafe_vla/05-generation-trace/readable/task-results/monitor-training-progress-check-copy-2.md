# monitor training progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260528T063420_result.json`
- **Structured JSON:** [`21be70588951e2e49210.json`](../../sessions/21/21be70588951e2e49210.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Current server time: **2026-05-28 14:38 +0800 = 06:38 UTC**. DDL in **5h22m**.

## Training Progress Summary

| # | Experiment | Cell | Server | Step | Speed | Remaining | Train ETA (UTC) | +Eval | DDL? |
|---|-----------|------|--------|------|-------|-----------|----------------|-------|------|
| 1 | vanilla_object_s1 | obj | 10894:0 | 47815/50005 | 1.08/s | **34m** | 07:12 | 07:52 | **OK** |
| 2 | detach_ln_v2_s4 | **Cell4** | 10894:1 | 29183/50005 | 1.08/s | **5h21m** | 11:59 | 12:39 | **TIGHT** |
| 3 | full_occ_bn_v2_s3 | Cell1 | 10894:2 | 5267/50005 | 1.08/s | 11h30m | 18:08 | 18:48 | MISS |
| 4 | vanilla_object_s2 | obj | 10894:3 | 5254/50005 | 1.08/s | 11h30m | 18:08 | 18:48 | MISS |
| 5 | full_occ_bn_v2_s2 | Cell1 | 34685:1 | 6631/50005 | 1.09/s | 11h03m | 17:41 | 18:21 | MISS |

### Resumed experiments (two possible outcomes)

These three use `--resume True`, and tqdm shows batch_idx from 0. Key question: does training stop when **global_step** (= resume_step + batch_idx) hits 50005, or when **batch_idx** hits 50005?

| Experiment | Cell | Resume | batch_idx | Global Step | If global_step termination | If batch_idx termination |
|-----------|------|--------|-----------|-------------|---------------------------|--------------------------|
| **detach_ln_v2_s3** | **Cell4** | 40000 | 9756 | 49756 | **~4min left → 06:42+eval 07:22 OK** | 10h15m → 16:53 MISS |
| **full_occ_ln_v2_s3** | Cell2 | 40000 | 9742 | 49742 | **~4min left → 06:42+eval 07:22 OK** | 10h15m → 16:53 MISS |
| **detach_ln_v2_s2** | **Cell4** | 25000 | 16091 | 41091 | **2h16m → 08:54+eval 09:34 OK** | 8h39m → 15:17 MISS |

## Cell 4 ANOVA Verdict (need n>=3; s0, s1 already done)

**Best case** (global_step termination):
- s3 finishes in ~4min, s2 at ~08:54, s4 at ~11:59 UTC
- n=3 achievable by ~07:22 (s3 eval done), n=4 by ~09:34 (s2 eval done)
- s4 training ends at 11:59 + 40min eval = 12:39 → slightly past DDL

**Worst case** (batch_idx termination):
- Only s4 (from scratch, no resume ambiguity) could finish training at 11:59 UTC
- But eval takes 40min → 12:39 UTC → MISS
- n=3 not achievable before DDL

**Recommendation**: Check in ~5-10 minutes whether detach_ln_v2_s3 and full_occ_ln_v2_s3 terminate (they're at 97.5%+ global progress if the code uses global_step). That will resolve the ambiguity immediately.

---
