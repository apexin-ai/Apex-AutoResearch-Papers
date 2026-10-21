# ops check 34685 progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_34685_progress_20260524T174911_result.json`
- **Structured JSON:** [`1362e1a7e06ccdd94511.json`](../../sessions/13/1362e1a7e06ccdd94511.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | exp_id | PID | Step/Total | Progress | Speed | ETA (UTC) |
|-----|--------|-----|-----------|----------|-------|-----------|
| 0 | cutoff_45k_s1 | 882188 | 17332/50005 | 34.7% | 1.07 it/s | May 25 ~10:24 |
| 1 | cutoff_15k_s1 | 861222 | 19699/50005 | 39.4% | 1.07 it/s | May 25 ~09:47 |
| 2 | cutoff_25k_s2 | 998127 | 2791/50005 | 5.6% | 1.08 it/s | May 25 ~14:04 |
| 3 | reverse_cutoff_s2 | 998624 | 2764/50005 | 5.5% | 1.07 it/s | May 25 ~14:11 |

全部 4 GPU 利用率 99%，显存 ~62G/97G，状态正常。

备注：
- cutoff_15k_s1 的日志在 `/root/occsafe_vla/logs/cutoff_15k_s1.log`（非 `/root/runs/` 路径）
- 最新 loss：cutoff_45k_s1 @ 17300 → occ=0.0138, action=0.1201；reverse_cutoff_s2 @ 2700 → occ=0.1301, action=0.1855

---
