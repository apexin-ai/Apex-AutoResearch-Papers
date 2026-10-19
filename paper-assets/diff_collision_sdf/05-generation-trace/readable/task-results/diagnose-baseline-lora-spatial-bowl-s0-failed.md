# diagnose baseline lora spatial bowl s0 failed

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_baseline_lora_spatial_bowl_s0_failed_20260522T115454_result.json`
- **Structured JSON:** [`ecb184d3988597bb6e3f.json`](../../sessions/ec/ecb184d3988597bb6e3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：SUCCESS — W&B 误报（假阳性），训练已正常完成。**

诊断结果：

| 项目 | 值 |
|------|-----|
| **conclusion** | **SUCCESS** |
| **最终 step** | 30000/30000 (100%) |
| **最终 loss** | 0.0088 (best: 0.00876 @ step 30000) |
| **训练时长** | 33h 39m 36s (~4.04s/it) |
| **checkpoint 路径** | `/root/autodl-tmp/checkpoints/baseline_spatial_bowl/baseline_lora_spatial_bowl_seed0/` |
| **checkpoint 内容** | step 29999, step 30000, best (均含 model.safetensors ~6.7GB + optimizer.pt ~249MB) |
| **失败原因** | 无。Cron 误报原因：WANDB_MODE=disabled，无 W&B metrics 可查 |
| **磁盘** | /root/autodl-tmp 260G/350G used (75%), 91G 可用 |

LoRA 参数量 33,472,512（~33.5M），loss 从 ~0.22 平稳下降到 ~0.009，训练正常收敛。无 Error/Exception/OOM。

**建议下一步**：可直接进入 evaluation 阶段，使用 step 30000 或 best checkpoint。

---
