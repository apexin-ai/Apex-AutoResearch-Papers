# ssh verify 10894 experiments

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_10894_experiments_20260525T183123_result.json`
- **Structured JSON:** [`e727fddd3f324e49f562.json`](../../sessions/e7/e727fddd3f324e49f562.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10894 实验状态报告

| exp_id | 状态 | GPU | 当前 step | 进度 | action_loss | occ_loss | 速度 | 剩余时间 |
|--------|------|-----|-----------|------|-------------|----------|------|----------|
| cutoff_45k_s2_v2 | RUNNING | cuda:0 (99%, 62G) | 3400/50005 | 7% | 0.2061 | 0.0126 | ~1.08 it/s | ~12.0h |
| mvp_occ_s3_v2 | RUNNING | cuda:1 (99%, 62G) | 3000/50005 | 6% | 0.1123 | 0.0086 | ~1.08 it/s | ~12.1h |
| full_occ_ln_s3_v2 | RUNNING | cuda:2 (99%, 63G) | 3200/50005 | 6% | 0.0947 | 0.0099 | ~1.08 it/s | ~12.0h |
| ablation_occ_detach_s3_v2 | RUNNING | cuda:3 (99%, 62G) | 3200/50005 | 6% | 0.0879 | 0.0095 | ~1.08 it/s | ~12.0h |

## 详细信息

**进程存活确认**：4 个 PID 全部存活，uptime 48-55 分钟（非 6h，可能有排队/启动延迟）。

**注意事项**：
- 3 个 resume 实验的进度条从 0 开始计数（已知 M052 bug：batch_idx 从 0 重新计数）。如果代码用 global_step 判断终止（20000 + batch_idx ≥ 50005），实际只需训练 30005 步，剩余 ~7h。如果用 batch_idx 判断，则跑满 50005 步，剩余 ~12h。
- cutoff_45k_s2_v2 从头训练，step=0 初始 action_loss=0.6133 → step=3400 降到 0.2061，收敛正常。
- resume 实验初始 action_loss 较低（0.08-0.10）符合预期（20K checkpoint），但 3000 步后略有上升（0.09-0.11），可能是 lr scheduler 重置导致，需持续观察。

---
