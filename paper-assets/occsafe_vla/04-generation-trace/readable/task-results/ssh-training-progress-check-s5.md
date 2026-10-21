# ssh training progress check s5

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_training-progress-check-s5_20260526T104045_result.json`
- **Structured JSON:** [`d958bae1629017508d5b.json`](../../sessions/d9/d958bae1629017508d5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the summary:

## 训练实验状态汇总 (2026-05-26 ~19:00 UTC)

### westd-10894

| 实验 | PID | GPU | 步数 | 进度 | 速度 | 剩余时间 | 预计完成 | 备注 |
|------|-----|-----|------|------|------|----------|----------|------|
| mvp_occ_s3_v2 | 33897 | cuda:1 | 48775/50005 | 97.5% | 1.05 it/s | ~20 min | May 26 ~19:20 UTC | 正常，ckpt 30K/40K 已保存 |
| full_occ_ln_s3_v2 | 34102 | cuda:2 | 48634/50005 | 97.3% | 1.07 it/s | ~21 min | May 26 ~19:22 UTC | 正常，ckpt 30K/40K 已保存 |
| ablation_occ_detach_s3_v2 | 34443 | cuda:3 | 48500/50005 | 97.0% | 1.05 it/s | ~24 min | May 26 ~19:25 UTC | 正常，ckpt 30K/40K 已保存 |
| reverse_cutoff_s2_v2 | 170605 | cuda:0 | 5853/50005 | 11.7% | 1.05 it/s | ~11.7h | May 27 ~06:40 UTC | 正常 |

### westd-34685

| 实验 | PID | GPU | 步数 | 进度 | 速度 | 剩余时间 | 预计完成 | 备注 |
|------|-----|-----|------|------|------|----------|----------|------|
| vanilla_v2_s1 | 419107 | cuda:0 | 6925/50005 | 13.8% | 1.07 it/s | ~11.2h | May 27 ~06:10 UTC | ⚠️ 尾部有 IO 抖动(8-16 s/it) |
| vanilla_v2_s2 | 419342 | cuda:1 | 6950/50005 | 13.9% | 1.07 it/s | ~11.2h | May 27 ~06:10 UTC | ⚠️ 尾部有 IO 抖动(8-16 s/it) |
| detach_ln_s3 | 419641 | cuda:2 | 6908/50005 | 13.8% | 1.07 it/s | ~11.2h | May 27 ~06:10 UTC | ⚠️ 尾部严重 IO 抖动(8-13 s/it) |
| cutoff_25k_s1_v2 | 453581 | cuda:3 | 5510/50005 | 11.0% | 1.08 it/s | ~11.4h | May 27 ~06:25 UTC | ⚠️ 尾部有 IO 抖动 |

### 关键发现

- **8/8 进程全部存活**
- westd-10894 的 3 个老实验（mvp_occ/full_occ_ln/detach）将在 **~20-25 分钟内完成**
- westd-34685 上 4 个实验日志尾部都出现严重 IO 抖动（正常 ~1.07 it/s 骤降到 5-16 s/it），4 个实验同时出现说明是 **磁盘 IO 竞争**，可能影响整体完成时间。如果抖动持续，实际完成时间可能比预估晚 1-3 小时

---
