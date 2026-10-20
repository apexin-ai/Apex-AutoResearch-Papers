# ssh check all training progress

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_all_training_progress_20260525T193040_result.json`
- **Structured JSON:** [`8b0dd90a4a1b16c19f37.json`](../../sessions/8b/8b0dd90a4a1b16c19f37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 服务器:GPU | 实验 | 当前step (local) | Global step | 总step | 进度% | 剩余时间 |
|-----------|------|-----------------|-------------|--------|-------|---------|
| **westd-10894** | | | | | | |
| 10894:0 | cutoff_45k_s2_v2 | 7022 | 7022 | 50005 | 14.0% | ~11.0h |
| 10894:1 | mvp_occ_s3_v2 | 6616 | 26616 | 50005 | 53.2% | ~6.0h |
| 10894:2 | full_occ_ln_s3_v2 | 6809 | 26809 | 50005 | 53.6% | ~5.9h |
| 10894:3 | ablation_occ_detach_s3_v2 | 6822 | 26822 | 50005 | 53.6% | ~5.9h |
| **westd-34685** | | | | | | |
| 34685:0 | detach_bn_v2_s0 | 6932 | 6932 | 50005 | 13.9% | ~11.0h |
| 34685:1 | detach_bn_v2_s1 | 6979 | 6979 | 50005 | 14.0% | ~10.9h |
| 34685:2 | detach_bn_v2_s2 | 6968 | 6968 | 50005 | 13.9% | ~11.0h |
| 34685:3 | full_occ_bn_v2_s1 | 5436 | 5436 | 50005 | 10.9% | ~11.4h |

**汇总：**
- 所有 8 个实验均在正常训练中，速度稳定 ~1.08 it/s
- 3 个 resume 实验（mvp_occ_s3_v2 / full_occ_ln_s3_v2 / ablation_occ_detach_s3_v2）进度过半，目标 local 30005 步（global 50005），预计 ~6h 后完成
- 5 个从头训练实验进度 ~11-14%，预计 ~11h 后完成
- full_occ_bn_v2_s1 比同批实验晚启动约 25 分钟，略落后

**最近 loss 快照（step 6800-7000）：**
| 实验 | occ_loss | action_loss |
|------|----------|-------------|
| cutoff_45k_s2_v2 | 0.0120 | 0.1572 |
| mvp_occ_s3_v2 | 0.0075 | 0.0747 |
| full_occ_ln_s3_v2 | 0.0079 | 0.0967 |
| ablation_occ_detach_s3_v2 | 0.0068 | 0.0708 |
| detach_bn_v2_s0 | 0.0100 | 0.1738 |
| detach_bn_v2_s1 | 0.0112 | 0.1641 |
| full_occ_bn_v2_s1 (step 5400) | 0.0143 | 0.1182 |

Resume 实验的 loss 明显低于从头训练的，符合预期（它们已经训练了 26K+ global steps）。

---
