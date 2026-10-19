# ops spatial bowl train prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial_bowl_train_prep_20260525T062515_result.json`
- **Structured JSON:** [`24993887a68fd97e5ec9.json`](../../sessions/24/24993887a68fd97e5ec9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有依赖项齐全。以下是汇总：

---

## spatial_bowl A1 训练确认

### 完整启动命令

```bash
cd /root/colliforce-vla && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
CUDA_VISIBLE_DEVICES=0 python scripts/train_a1_sdf_aux_pi05.py \
  --scene spatial_bowl \
  --lambda_sdf 0.005 \
  --seed 0 \
  --gpu 0 \
  --batch_size 32 \
  --num_train_steps 30000 \
  --save_interval 2000 \
  --log_interval 100
```

输出 checkpoint 目录将是：`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_spatial_bowl_seed0_l005/`

### 数据状态

| 资源 | 路径 | 状态 |
|------|------|------|
| SafeLIBERO spatial BDDL | `vlsa-aegis/safelibero/.../safelibero_spatial/` | ✓ 4 个 task 文件 |
| 训练数据 (LeRobot) | `/root/autodl-tmp/colliforce_data/safelibero_spatial/` | ✓ 存在 (data/images/meta) |
| HDF5 原始数据 | `/root/autodl-tmp/colliforce_data/spatial_bowl_train.hdf5` | ✓ 存在 |
| SDF GT | `/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz` | ✓ 112KB |
| Baseline assets (norm_stats) | `assets/baseline_spatial_bowl/safelibero_spatial/norm_stats.json` | ✓ 存在 |
| Pi0.5 权重 | `/root/autodl-tmp/openpi_weights/pi05_libero/` | ✓ config.json + model.safetensors |

### 参考：object_pudding 已完成的训练

checkpoints 下已有 6 个 object_pudding 实验（seed 0/1/2 × λ 0.005/0.1），格式为 `a1_sdf_pi05_object_pudding_seed{N}_l{lambda}`。

### 预估训练时长

基于 object_pudding 经验，30K steps 在单张 RTX PRO 6000 上约 **8-12 小时**。

### 阻塞问题

**无阻塞**。所有数据、权重、配置文件均已就绪，可直接提交。

---
