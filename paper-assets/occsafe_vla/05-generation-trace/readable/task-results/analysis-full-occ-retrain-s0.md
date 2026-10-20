# analysis full occ retrain s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_occ_retrain_s0_20260523T180535_result.json`
- **Structured JSON:** [`29c6053f769aa30057c5.json`](../../sessions/29/29c6053f769aa30057c5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE(success)。

## 分析结果

### 训练状态
- **成功完成**，50005/50005 steps，EXIT_CODE=0，无报错

### Checkpoint
```
/root/autodl-tmp/checkpoints/full_occ_retrain_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt
```
包含完整模型文件 + action_head/occ_head/proprio_projector checkpoint。

### 关键 Metrics

| 指标 | full_occ_retrain_s0 | vanilla_retrain_s0 | 对比 |
|------|---------------------|-------------------|------|
| action_loss_final | **0.0417** | 0.0457 | **-8.8%** ✓ |
| occ_loss_final | 0.0104 | N/A | — |
| total_steps | 50005 | 50005 | 一致 |
| training_hours | 14.21 | 14.13 | +0.6% |

### 对比分析
- Full OCC 的 action_loss (0.0417) 比 vanilla (0.0457) **低 8.8%**，符合预期——OCC 辅助任务提供了额外梯度信号，帮助学到更好的视觉表征
- occ_loss 从 0.0975 收敛到 0.0104（下降 89.3%），说明 occupancy 预测任务训练充分
- 训练时间几乎无差异（+0.6%），occ_head 开销可忽略

### W&B
未启用（日志中无任何 wandb 记录）。

---
