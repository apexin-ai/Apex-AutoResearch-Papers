# analysis process eval update csv

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_process_eval_update_csv_20260525T062014_result.json`
- **Structured JSON:** [`ab79a25a28a28f24aed2.json`](../../sessions/ab/ab79a25a28a28f24aed2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CSV 更新完成。

**full_occ_retrain_s0 eval 结果**：TSR=0.802, CAR=0.746, 127 collisions, 500 episodes。CAR=0.746 略低于其他 Full OCC seeds（0.765-0.832）。

**CSV 更新汇总**（共 10 行）：
- `full_occ_retrain_s0`: eval_pending → 实际结果
- 9 行从 200-episode 更新为 500-episode 50-rollout 数据：mvp_vanilla_s0/s1/s2, mvp_occ_s0/s2, ablation_occ_detach_s0/s1, ablation_random_occ_s0/s1

注意：`mvp_occ_s1`（line 7）仍为 200 episodes，任务中未提供 50-rollout 数据。

---
