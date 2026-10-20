# ops check eval status 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-status-10894_20260526T111426_result.json`
- **Structured JSON:** [`738fecbcc3cd644ebb7e.json`](../../sessions/73/738fecbcc3cd644ebb7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 eval 实验全部正在运行：

| 实验 | GPU | PID | 进度 | 状态 |
|------|-----|-----|------|------|
| **mvp_occ_s3_v2_eval** | cuda:1 (16.8GB) | 186629 | Task 0 已完成 (TSR=1.000, CAR=0.980)，进入下一个 task | 运行中 |
| **full_occ_ln_s3_v2_eval** | cuda:2 (16.8GB) | 186837 | Task 0: 98% (49/50 rollouts) | 运行中 |
| **ablation_occ_detach_s3_v2_eval** | cuda:3 (16.8GB) | 189901 | Task 0: 74% (37/50 rollouts) | 运行中 |

GPU 0 被 `reverse_cutoff_s2_v2` 训练占用 (62.2GB, 99% utilization)。4 张 GPU 全部在工作。

---
