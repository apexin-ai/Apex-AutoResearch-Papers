# ops spatial bowl a1 prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial_bowl_a1_prep_20260524T122346_result.json`
- **Structured JSON:** [`7cedb2d543b5c5d08f41.json`](../../sessions/7c/7cedb2d543b5c5d08f41.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**昨天（2026-05-23）已完成过一轮完整的准备验证。** 以下是汇报：

---

### 1. SDF GT 数据：已就绪

- 路径：`/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz`
- 两台服务器（westd-35807、westd-45947）均已有，114,658 bytes，4076 个查询点
- **无需预计算**

### 2. 训练脚本适配：直接可用

`scripts/train_a1_sdf_aux_pi05.py` 的 `SCENE_CONFIG` 已包含 `spatial_bowl`，`--scene spatial_bowl` 直接工作，无需修改。

### 3. 训练数据：已就绪

- 路径：`/root/autodl-tmp/colliforce_data/safelibero_spatial/`
- 50 episodes，~434MB，两台服务器均有

### 4. Checkpoint 路径

不会与现有 object_pudding checkpoints 冲突（按 scene 名区分目录）。

### 5. 双 lambda 启动命令

```bash
# λ=0.005, GPU 0
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/colliforce-vla && \
WANDB_MODE=offline PYTHONUNBUFFERED=1 python scripts/train_a1_sdf_aux_pi05.py \
  --scene spatial_bowl --seed 0 --gpu 0 --batch_size 32 \
  --num_train_steps 30000 --lambda_sdf 0.005 --lambda_ee 0.01 \
  --lr 2.5e-5 --save_interval 2000

# λ=0.01, GPU 1
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/colliforce-vla && \
WANDB_MODE=offline PYTHONUNBUFFERED=1 python scripts/train_a1_sdf_aux_pi05.py \
  --scene spatial_bowl --seed 0 --gpu 1 --batch_size 32 \
  --num_train_steps 30000 --lambda_sdf 0.01 --lambda_ee 0.01 \
  --lr 2.5e-5 --save_interval 2000
```

### 6. 阻塞项

**两台服务器当前都 SSH 认证失败**。AutoDL 实例可能重启导致端口变了，需要去 AutoDL 控制台查看新端口并更新 `resources.yaml` 中 westd-35807（当前 port: 35807）和 westd-45947（当前 port: 45947）的配置。

其余（代码、数据、SDF GT、配置）全部就绪，端口更新后即可启动。

---
