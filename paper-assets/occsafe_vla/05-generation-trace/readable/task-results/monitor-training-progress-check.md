# monitor training progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-check_20260527T044230_result.json`
- **Structured JSON:** [`5f7345873cff111f5cd1.json`](../../sessions/5f/5f7345873cff111f5cd1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

8/8 实验全部正常运行，无异常。

| exp_id | Step | 进度 | ETA (UTC) | action_loss |
|--------|------|------|-----------|-------------|
| full_occ_ln_v2_s1c_r2 | ~14868 | 29.7% | 5/27 ~14:00 | 0.117 |
| full_occ_ln_v2_s2_r2 | ~14856 | 29.7% | 5/27 ~14:00 | 0.124 |
| detach_ln_v2_s0c_r2 | ~14845 | 29.7% | 5/27 ~13:50 | 0.122 |
| full_occ_ln_v2_s0d | ~12272 | 24.5% | 5/27 ~16:30 | 0.150 |
| detach_ln_v2_s1_35 | ~19184 | 38.4% | 5/27 ~12:40 | 0.091 |
| detach_ln_s4 | ~19205 | 38.4% | 5/27 ~12:40 | 0.129 |
| ablation_occ_detach_s4 | ~16400 | 32.8% | 5/27 ~13:30 | 0.135 |
| mvp_occ_s4 | ~16356 | 32.7% | 5/27 ~13:30 | 0.115 |

最晚的 full_occ_ln_v2_s0d 预计 5/27 16:30 UTC 完成，距 DDL (5/28 12:00 UTC) 有 ~19h 余量。GPU 利用率 84-99%，磁盘 10894 剩 38G、34685 剩 92G，均充足。

报告已写入 `artifacts/training_status_20260527_0446.md`。

---
