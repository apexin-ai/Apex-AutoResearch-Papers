# ops fix best ckpt symlink and rerun

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_best_ckpt_symlink_and_rerun_20260525T170124_result.json`
- **Structured JSON:** [`99e983142011fbcd46e9.json`](../../sessions/99/99e983142011fbcd46e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Episode 20 出来了！两个 episode 都正常完成：

- Episode 10/50: success=False, collided=False, steps=300
- Episode 20/50: success=False, collided=False, steps=300

Eval 确认正常运行。

## 汇报

### A. Symlink 修复（4 个 best/ 目录）
全部成功：`model.safetensors -> model_lora.safetensors`

| 目录 | 验证 |
|------|------|
| `.../a1_sdf_pi05_object_pudding_seed1_l005/best/` | `model.safetensors -> model_lora.safetensors` |
| `.../a1_sdf_pi05_object_pudding_seed1_l01/best/` | `model.safetensors -> model_lora.safetensors` |
| `.../a1_sdf_pi05_object_pudding_seed2_l005/best/` | `model.safetensors -> model_lora.safetensors` |
| `.../a1_sdf_pi05_object_pudding_seed2_l01/best/` | `model.safetensors -> model_lora.safetensors` |

原始基模型已备份为 `model_base_backup.safetensors`。

### B. Eval 启动
- **PID**: 508967（python 子进程），父进程 508965
- **GPU 3**: 9014 MiB，正常推理中
- **Checkpoint**: `seed2_l005/best/`（symlink 修复后）
- **日志**: `/root/colliforce-vla/logs/eval_s2_l005_best_10k_v2.log`

### C. 前 2 个 Episode 结果
- Episode 10/50: success=False, collided=**False**, steps=300
- Episode 20/50: success=False, collided=**False**, steps=300

模型加载和推理正常（LoRA 注入成功，key 匹配无报错），无碰撞。

### D. 其他 GPU 状态

| GPU | PID | 进程 | 显存 | 说明 |
|-----|-----|------|------|------|
| cuda:0 | 168730 | `train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 0` | 27036 MiB | 训练中，已运行 7h+ |
| cuda:1 | 478655 | `eval_safelibero.py s0_l005 30k` | 8991 MiB | eval 中 |
| cuda:2 | 478930 | `eval_safelibero.py s0_l01 30k` | 8995 MiB | eval 中 |
| cuda:3 | 508967 | `eval_safelibero.py s2_l005 best`（刚启动） | 9014 MiB | eval 中 |

---
