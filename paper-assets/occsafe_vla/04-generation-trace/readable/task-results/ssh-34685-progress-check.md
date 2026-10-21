# ssh 34685 progress check

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_34685_progress_check_20260526T054909_result.json`
- **Structured JSON:** [`cce82b28361b7dec4185.json`](../../sessions/cc/cce82b28361b7dec4185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-34685 训练进度 (2026-05-26)

| exp_id | GPU | step/50K | 进度% | occ_loss | action_loss | speed | ETA |
|--------|-----|----------|-------|----------|-------------|-------|-----|
| detach_bn_v2_s0 | cuda:0 | 43785/50005 | 87.6% | 0.0112 | 0.0728 | 1.07 it/s | ~1h37m |
| detach_bn_v2_s1 | cuda:1 | 43870/50005 | 87.7% | 0.0080 | 0.0625 | 1.07 it/s | ~1h36m |
| detach_bn_v2_s2 | cuda:2 | 43746/50005 | 87.5% | 0.0086 | 0.0566 | 1.06 it/s | ~1h39m |
| full_occ_bn_v2_s1 | cuda:3 | 42305/50005 | 84.6% | 0.0089 | 0.0845 | 1.08 it/s | ~1h59m |

**GPU 利用率**:
| GPU | util | VRAM |
|-----|------|------|
| 0 | 99% | 62.2/97.9 GB |
| 1 | 99% | 62.2/97.9 GB |
| 2 | 86% | 62.2/97.9 GB |
| 3 | 50% | 62.2/97.9 GB |

**磁盘**: 40% (12G/30G)

**进程**: 4 个全部存活，运行时长均 ~12h。Loss 均已收敛至平稳区间，detach 三个 seed 的 action_loss 在 0.05-0.07 区间，full_occ_bn_v2_s1 的 action_loss 略高 (0.0845)。

---
