# ops gradient analysis checkpoint prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gradient-analysis-checkpoint-prep_20260527T022019_result.json`
- **Structured JSON:** [`6545e593e45a88d61e32.json`](../../sessions/65/6545e593e45a88d61e32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 五个 checkpoint 路径（全部确认存在）

| # | 条件 | 服务器 | 路径 |
|---|------|--------|------|
| 1 | Cell 1 (Full OCC BN) | **10894** | `/root/autodl-tmp/checkpoints/mvp_occ_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s3_v2--50000_chkpt` |
| 2 | Cell 2 (Full OCC LN) | **10894** | `/root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt` |
| 3 | Cell 3 (Detach BN) | **10894** | `/root/autodl-tmp/checkpoints/ablation_occ_detach_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3_v2--50000_chkpt` |
| 4 | Cell 4 (Detach LN) | **34685** | `/root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt` |
| 5 | Vanilla | **34685** | `/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt` |

**注意**：Cell 1 和 Cell 3 的已完成 checkpoint 在 **10894** 上（`mvp_occ_s3_v2` 和 `ablation_occ_detach_s3_v2`），不在 34685。34685 上的 s4 版本正在训练中，尚无 50k checkpoint。

### 2. 分布

- **10894**: Cell 1, Cell 2, Cell 3（3 个）
- **34685**: Cell 4, Vanilla（2 个）

### 3. 34685 训练进度

| 实验 | 当前 step | 进度 | tqdm 剩余时间 | 速度 |
|------|----------|------|-------------|------|
| detach_ln_v2_s1 | ~10,427 / 50,005 | 21% | ~10h 08m | ~1.05 it/s |
| detach_ln_s4 | ~10,490 / 50,005 | 21% | ~10h 26m | ~1.05 it/s |
| ablation_occ_detach_s4 | ~7,679 / 50,005 | 15% | ~11h 00m | ~1.05 it/s |
| mvp_occ_s4 | ~7,659 / 50,005 | 15% | ~10h 55m | ~1.05 it/s |

4 GPU 全部满载（82-99% util，~62GB VRAM）。按当前速度，全部 4 个实验预计在 **~11h 内完成**，应在 DDL (05-28 12:00 UTC) 前完成。

### 4. 缺失情况

无缺失。原始任务中查找的 `mvp_occ_s{0,1,2}` 和 `ablation_occ_detach_s{0,1,2}` 在 34685 上不存在，但 10894 上有对应的 `s3_v2` 版本且已完成 50k checkpoint，可作为代表。

---
