# ops check 10894 full occ ln

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_10894_full_occ_ln_20260524T143430_result.json`
- **Structured JSON:** [`a8bd9760ca046b4fe370.json`](../../sessions/a8/a8bd9760ca046b4fe370.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个训练全部正常运行。

| GPU | exp_id | PID | Step/Total | Speed | Remaining |
|-----|--------|-----|------------|-------|-----------|
| 0 | ablation_occ_detach_s0_retrain | 746696 | 19161/50005 (38%) | ~1.08 it/s | ~7h 56m |
| 1 | full_occ_ln_s0 | 742821 | 19579/50005 (39%) | ~1.08 it/s | ~7h 49m |
| 2 | full_occ_ln_s1 | 743031 | 19549/50005 (39%) | ~1.08 it/s | ~7h 49m |
| 3 | full_occ_ln_s2 | 743375 | 19513/50005 (39%) | ~1.07 it/s | ~7h 53m |

GPU 显存使用：4 卡均 ~62GB/98GB，利用率 44-99%。

最新 loss（每 500 步打印）：

| exp_id | step | occ_loss | action_loss |
|--------|------|----------|-------------|
| full_occ_ln_s1 | 19500 | 0.0122 | 0.0864 |
| full_occ_ln_s2 | 19500 | 0.0079 | 0.0942 |
| ablation_occ_detach_s0_retrain | 19100 | 0.0118 | 0.1133 |

全部约 8 小时后完成（预计 UTC 5/24 ~21:30 左右）。ablation 比 ln 组慢约 400 步，因其晚启动。

---
