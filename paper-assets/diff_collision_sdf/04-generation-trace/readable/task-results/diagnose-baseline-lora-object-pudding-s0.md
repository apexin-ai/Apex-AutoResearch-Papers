# diagnose baseline lora object pudding s0

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_baseline_lora_object_pudding_s0_20260522T115824_result.json`
- **Structured JSON:** [`35a6290325b3d294c086.json`](../../sessions/35/35a6290325b3d294c086.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志中无任何 save/checkpoint 记录。**两个训练虽然跑完 30K steps 但没保存 checkpoint。** 这是关键问题。

## 诊断结果

### baseline_lora_object_pudding_s0 (cuda:3, PID 281629)
- **状态：训练已完成，Cron 误报**
- Steps: 30000/30000 ✓
- Final loss: 0.0124
- Wall time: 33h43m21s (~4.05s/step)
- 无 error/traceback
- LoRA params: 33,472,512 (一致到结束)

### baseline_lora_spatial_bowl_s0 (cuda:1, PID 281554)
- **状态：训练已完成，Cron 误报**
- Steps: 30000/30000 ✓
- Final loss: 0.0088
- Wall time: 33h39m36s (~4.04s/step)
- 无 error/traceback
- LoRA params: 33,472,512 (一致到结束)

### ⚠️ 严重问题：两个实验均无 checkpoint 文件

输出目录 (`baseline_lora_obj_s0/` 和 `baseline_lora_spa_s0/`) 只包含 log 文件，无 `.safetensors`、`.pt` 或任何 checkpoint 目录。日志中也没有任何 "save"/"checkpoint" 相关记录。

整个 `/root/autodl-tmp/` 下唯一的 `.safetensors` 是原始预训练权重 (`openpi_weights/pi0_base/model.safetensors`)。

**训练脚本可能未配置 checkpoint 保存，或保存路径有误。33+ 小时的训练结果丢失。需要检查训练脚本的 checkpoint 保存逻辑后决定是否重跑。**

---
