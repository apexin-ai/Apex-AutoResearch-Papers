# eval check 29046 status

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_check-29046-status_20260522T124804_result.json`
- **Structured JSON:** [`3e9b90097918cb954ce9.json`](../../sessions/3e/3e9b90097918cb954ce9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了 exp-003 的实际存储路径。汇总如下：

---

## westd-29046 状态汇总 (2026-05-22 20:48 UTC+8)

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU0 (exp-003-s2) | 95% | 38GB / 96GB |
| GPU1 (exp-004-s2-v2) | 94% | 46GB / 96GB |

两卡都在满负载训练。

### exp-003-s2 (R3-only seed2)
- **当前进度**: step **7623/8000** (95.3%)
- **速度**: ~25s/step
- **剩余**: ~377 steps → **约 2.6 小时**完成（预计 ~23:20）
- **checkpoint-8000**: **尚未产出**
- checkpoint 保存在 `/root/autodl-tmp/checkpoints/exp003_r3only_seed2/`，目前最新到 **checkpoint-7500**
- 注意：之前给的 `exp-003-r3only-s2` 目录名不对，实际目录是 `exp003_r3only_seed2`（下划线命名）
- seed1 的 checkpoint-8000 已存在

### exp-004-s2-v2 (ACT seed2 第三次重启)
- **当前进度**: step **2150/8000** (26.9%)，从 ckpt-2000 resume
- **速度**: ~90s/10 steps → ~9s/step（比 exp-003 快很多，因为是 LoRA SFT）
- **loss 趋势**: sft_loss 在 0.001~0.018 波动，l2_loss ~0.0026，正常范围
- 输出路径: `/root/autodl-tmp/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/`
- 启动时间: 20:25，运行约 23 分钟
- **预估完成**: ~5850 steps 剩余 × 9s ≈ **14.6 小时**（明天上午 ~11:00）

### 磁盘
| 分区 | 用量 | 剩余 | 状态 |
|------|------|------|------|
| / (根) | 28G/30G (93%) | **2.4G** | **危险** |
| /root/autodl-tmp (数据盘) | 59G/250G (24%) | 192G | 正常 |

**根分区只剩 2.4G，需要关注。** 如果训练过程中有任何日志/临时文件写入根分区，可能会撑满导致训练中断。建议清理根分区或确保新文件都写入 autodl-tmp。

---
