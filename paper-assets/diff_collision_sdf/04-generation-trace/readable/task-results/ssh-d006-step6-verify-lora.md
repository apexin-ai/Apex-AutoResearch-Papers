# ssh d006 step6 verify lora

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d006_step6_verify_lora_20260520T210247_result.json`
- **Structured JSON:** [`2d07d87ebe43bd1a5bb8.json`](../../sessions/2d/2d07d87ebe43bd1a5bb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D006 Step 6 验证结果

### 两个 LoRA 实验都启动失败

**错误**：启动命令使用了脚本不支持的参数 `--gpu` 和 `--max_steps`。

```
train_baseline.py: error: unrecognized arguments: --gpu 1 --max_steps 30000
train_baseline.py: error: unrecognized arguments: --gpu 3 --max_steps 30000
```

**正确用法**（脚本文档注释和 argparse 定义）：
- GPU 选择：`CUDA_VISIBLE_DEVICES=X` 环境变量，不是 `--gpu`
- 训练步数：`--num_train_steps`，不是 `--max_steps`

### 当前 GPU 状态（只有 2/4 在用，非 6/6）

| GPU | 利用率 | 显存 | 进程 |
|-----|--------|------|------|
| 0 | 80% | 35747/97887 MiB | PID 222903 (原 baseline_spatial_bowl_s0_v2) |
| 1 | **0%** | **0 MiB** | **空闲 — LoRA spatial 失败** |
| 2 | 100% | 35747/97887 MiB | PID 222982 (原 baseline_object_pudding_s0_v2) |
| 3 | **0%** | **0 MiB** | **空闲 — LoRA pudding 失败** |

### 需要重新启动的正确命令

```bash
# spatial_bowl on cuda:1
CUDA_VISIBLE_DEVICES=1 nohup python scripts/train_baseline.py \
  --scene spatial_bowl --seed 0 \
  --exp_name baseline_lora_spatial_bowl_s0 \
  --num_train_steps 30000 \
  > ~/runs/diff_collision_sdf/baseline_lora_spatial_bowl_s0.log 2>&1 &

# object_pudding on cuda:3
CUDA_VISIBLE_DEVICES=3 nohup python scripts/train_baseline.py \
  --scene object_pudding --seed 0 \
  --exp_name baseline_lora_object_pudding_s0 \
  --num_train_steps 30000 \
  > ~/runs/diff_collision_sdf/baseline_lora_object_pudding_s0.log 2>&1 &
```

是否要我重新启动这两个实验？

---
