# diagnose critical path eta check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_critical_path_eta_check_20260527T174936_result.json`
- **Structured JSON:** [`b148236259eb2fdd8649.json`](../../sessions/b1/b148236259eb2fdd8649.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总 (2026-05-27 18:10 UTC)

**DDL: 2026-05-28 12:00 UTC (剩余 ~17h 50m)**

### westd-34685 (4 experiments)

| Experiment | Step | Progress | Speed | Remaining | ETA (UTC) | DDL? |
|---|---|---|---|---|---|---|
| **detach_ln_v2_s2** | 10204/50005 | 20% | 1.09 it/s | ~10h 8m | **May 28 ~04:18** | OK |
| detach_ln_v2_s3 | 5432/50005 | 11% | 1.08 it/s | ~11h 28m | May 28 ~05:38 | OK |
| full_occ_ln_v2_s3 | 5445/50005 | 11% | 1.08 it/s | ~11h 27m | May 28 ~05:37 | OK |
| vanilla_object_s0 | 5041/50005 | 10% | 1.10 it/s | ~11h 21m | May 28 ~05:31 | OK |

### westd-10894 (3 experiments)

| Experiment | Step | Progress | Speed | Remaining | ETA (UTC) | DDL? |
|---|---|---|---|---|---|---|
| detach_ln_v2_s0c_r3 | 32384/50005 | 65% | 1.08 it/s | ~4h 31m | May 27 ~22:41 | OK |
| full_occ_ln_s4 | 30586/50005 | 61% | 1.08 it/s | ~4h 59m | May 27 ~23:09 | OK |
| vanilla_object_s1 | 1150/50005 | 2% | 1.10 it/s | ~12h 20m | May 28 ~06:30 | OK |

### 关键结论

**所有 7 个实验均在 DDL 前完成，无需干预。**

**detach_ln_v2_s2** 的 ETA 是 ~04:18 UTC，比 DDL 早近 8 小时。之前 Reviewer 报告的 ~12:15 UTC 估计有误——当前稳定速度 1.09 it/s，tqdm 自身估算也是 ~10h 8m 剩余，两者一致。Cell 4 可以拿到 n=3。

---
