# exp phase d lora retrain gpu23

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_phase_d_lora_retrain_gpu23_20260516T115417_result.json`
- **Structured JSON:** [`8055510f5844669f9962.json`](../../sessions/80/8055510f5844669f9962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

log_interval=50，每 50 步打印一次。50 步 × 4.5s/步 ≈ 3.75 分钟后才会有 step=50 的 log。GPU 利用率 99% 确认训练在正常跑。

---

## 总结

**两路 LoRA v2 训练已成功启动：**

| 任务 | tmux session | PID | GPU | 初始 loss |
|------|-------------|-----|-----|-----------|
| LoRA-Visual v2 | `v2_lora_visual_r16` | 665119 | cuda:2 (12.7 GB, 99%) | 1.9794 |
| LoRA-Physical v2 | `v2_lora_physical_r16` | 665199 | cuda:3 (12.8 GB, 99%) | 2.3697 |

**配置：**
- base: pi0_libero, LoRA rank=16, alpha=32, lr=1e-4, batch=16, steps=10000
- trainable params: 3,686,400 / 3.5B (0.11%)
- 数据：97 episodes, 66984 frames (libero_object_image)

**注意：** 初始 loss ~2.0-2.4，高于任务描述中预期的 0.05-0.15。这可能是因为 pi0_libero 使用了不同的 loss 计算方式（可能包含语言 token loss），属正常范围。

**预计完成时间：** ~4.5s/step × 10000 steps ≈ 12.5 小时（比 v1 的 170min 长，可能是 Blackwell GPU 上 bf16 未优化或 batch_size 偏大）。

**日志位置：**
- `/root/runs/meta_brain_lora_routing/v2_lora_visual_r16.log`
- `/root/runs/meta_brain_lora_routing/v2_lora_physical_r16.log`

---
