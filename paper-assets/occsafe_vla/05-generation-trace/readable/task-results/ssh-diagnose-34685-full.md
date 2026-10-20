# ssh diagnose 34685 full

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_34685_full_20260525T193131_result.json`
- **Structured JSON:** [`ea843f38429296f885ac.json`](../../sessions/ea/ea843f38429296f885ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 34685 诊断结果

| 实验 | 状态 | 当前 step | 进度 | 速度 | 预计完成(UTC) | checkpoint | 备注 |
|------|------|-----------|------|------|--------------|------------|------|
| detach_bn_v2_s0 | **运行中** | 6984/50005 | 14% | 1.08 it/s | ~14:30 May 26 | 无（首次存档在 step 10000） | GPU0, 正常 |
| detach_bn_v2_s1 | **运行中** | 7030/50005 | 14% | 1.08 it/s | ~14:30 May 26 | 无 | GPU1, 正常 |
| detach_bn_v2_s2 | **运行中** | 7020/50005 | 14% | 1.09 it/s | ~14:30 May 26 | 无 | GPU2, 正常 |
| full_occ_bn_v2_s1 | **运行中** | 5488/50005 | 11% | 1.09 it/s | ~14:50 May 26 | 无 | GPU3, 晚启动约25min |

**GPU 使用率**: 4×RTX PRO 6000 (98GB), 全部 99%/99%/99%/47% util, 各占 ~62GB VRAM
**磁盘**: /root 30G, 已用 13G (41%), 无独立 autodl-tmp 分区（overlay 根分区）

### 关键判断
- 所有 4 个实验**健康运行中**，从头训练，当前 ~14% 进度
- save_freq=10000，尚未产生任何 checkpoint（最早 step-010000 预计 ~2h 后出现）
- step-050000 checkpoint 预计 **May 26 14:30-15:00 UTC** 完成
- **距 CoRL deadline 3.5 天，训练将在 ~11h 后完成——时间充足**
- Registry 无需更新（状态仍为 RUNNING，与实际一致）

---
