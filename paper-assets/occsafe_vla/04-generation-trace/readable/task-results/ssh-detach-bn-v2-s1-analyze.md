# ssh detach bn v2 s1 analyze

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_detach_bn_v2_s1_analyze_20260526T073124_result.json`
- **Structured JSON:** [`1e7128fe1c835534e452.json`](../../sessions/1e/1e7128fe1c835534e452.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D051 v2 实验状态汇总

### detach_bn_v2_s1 (cuda:1) — ✅ 完成
- 正常完成 50005 steps，EXIT_CODE=0
- **Step 50000 loss**: occ=0.0089, action=0.0513
- **Checkpoint**: `/root/autodl-tmp/checkpoints/detach_bn_v2_s1/openvla-7b+...--detach_bn_v2_s1--50000_chkpt`
- GPU 1 已释放 (0 MiB)

### detach_bn_v2_s0 (cuda:0) — ✅ 完成（正在写最后几步）
- 50000 checkpoint 已保存，step 50004/50005
- **Step 50000 loss**: occ=0.0095, action=0.0449
- **Checkpoint**: `detach_bn_v2_s0/...--50000_chkpt`

### detach_bn_v2_s2 (cuda:2) — ⏳ 即将完成
- 正在保存 50000 checkpoint（merge model shards 中）
- **Step 50000 loss**: occ=0.0094, action=0.0481
- 预计 1-2 分钟内完成

### full_occ_bn_v2_s1 (cuda:3) — 🔄 训练中
- Step **48533**/50005 (97%)，~1.07 it/s
- **Step 48500 loss**: occ=0.0110, action=0.0557
- **ETA**: ~23 min

### GPU 空闲情况
| GPU | 显存 | 状态 |
|-----|------|------|
| 0 | 62203/97887 MiB | s0 秒级释放 |
| 1 | 0 MiB | **空闲** |
| 2 | 62203/97887 MiB | s2 分钟级释放 |
| 3 | 62203/97887 MiB | full_occ 在跑，~23min |

3 个 detach_bn 实验 loss 一致性好（occ: 0.0089-0.0095, action: 0.0449-0.0513），全部即将/已完成。full_occ_bn_v2_s1 ~23 分钟后完成，之后 4 张卡全部空闲。

---
