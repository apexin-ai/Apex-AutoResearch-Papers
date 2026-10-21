# ops westd34685 status and next

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd34685_status_and_next_20260523T165523_result.json`
- **Structured JSON:** [`88c37a7cf8e96b3f97b1.json`](../../sessions/88/88c37a7cf8e96b3f97b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 各实验状态

| 实验 | GPU | 当前 Step | 进度 | 预计剩余 | 状态 |
|------|-----|-----------|------|----------|------|
| vanilla_retrain_s0 | GPU 0 | 46795/50005 | 93% | ~50 min | 运行中 |
| full_occ_retrain_s0 | GPU 1 | 46573/50005 | 93% | ~53 min | 运行中 |
| reverse_cutoff_s0 | GPU 2 | 39954/50005 | 80% | ~2.6h | 运行中 |
| cutoff_25k_s0 | GPU 3 | 40023/50005 | 80% | ~2.6h | 运行中 |

### 2. Checkpoint 路径

| 实验 | 最新 Checkpoint |
|------|----------------|
| vanilla_retrain_s0 | `/root/autodl-tmp/checkpoints/vanilla_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--40000_chkpt` |
| full_occ_retrain_s0 | `/root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--40000_chkpt` |
| reverse_cutoff_s0 | `/root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--30000_chkpt` |
| cutoff_25k_s0 | `/root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--40000_chkpt` (刚保存) |

### 3. 后续行动

- **Eval**: 无——4 个实验均未完成（无 50000/50005_chkpt）
- **梯度分析**: 未启动——等 vanilla + full_occ 完成。`run_full_analysis.sh` 已存在（11KB, May 23 18:23）
- **空闲 GPU**: 无——4 张卡全部占用

### 4. 预计时间线

- **~1h 后**: vanilla_retrain_s0 + full_occ_retrain_s0 完成 → GPU 0/1 释放 → 可启动梯度分析（1 张卡）+ 报告空闲卡（1 张）
- **~2.6h 后**: reverse_cutoff_s0 + cutoff_25k_s0 完成 → 需提交 eval

建议 ~1h 后再次检查状态。

---
