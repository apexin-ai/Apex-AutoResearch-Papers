# code implement true oracle refine

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement_true_oracle_refine_20260522T194458_result.json`
- **Structured JSON:** [`bc2e4994870e64c48ca9.json`](../../sessions/bc/bc2e4994870e64c48ca9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实现完成。总结：

### GT SDF 数据格式
- keys: `query_points` (N,3, float64) + `sdf_values` (N,, float32)
- spatial_bowl: 4076 点, sdf ∈ [-0.05, 0.05], mean=0.017
- object_chocolate: 4084 点, sdf ∈ [-0.05, 0.05], mean=0.016
- 正=安全, 负=碰撞

### 新增代码 (1049→1144 行, +95 行)
| 函数/参数 | 说明 |
|---|---|
| `_load_sdf_gt_oracle(path)` | 加载 npz + 构建 cKDTree |
| `query_gt_sdf(position, sdf_gt_data, k=8)` | IDW 插值查询 GT SDF（K=8 最近邻，解决稀疏网格梯度为零问题） |
| `_refine_action_oracle(...)` | 数值梯度 refinement，delta→absolute 坐标转换（M024 fix） |
| `--true_oracle` | 启用 GT SDF oracle refinement |
| `--force_refine_oracle` | 每步都 refine（忽略 margin） |
| 每 episode 记录 | `sdf_value`, `refine_count`, `gradient_magnitude_avg` |

### Dry-run 验证
- 碰撞区域 (SDF=-0.033): refinement 生效，shift=0.1m，grad_mag=0.16
- 安全区域 (SDF=0.023): 不触发 refinement
- 两台服务器语法验证通过

### 建议运行命令（cuda:3 释放后）
```bash
# spatial_bowl with baseline policy + true oracle
python scripts/eval_safelibero.py \
    --checkpoint /root/autodl-tmp/checkpoints/baseline_spatial_bowl_0 \
    --config_name baseline_spatial_bowl \
    --suite safelibero_spatial --task_id 0 \
    --true_oracle \
    --sdf_gt_path /root/colliforce-vla/data/sdf_gt_spatial_bowl.npz \
    --refine_alpha 0.1 --refine_margin 0.01 \
    --n_episodes 50 --gpu 3 \
    --output_prefix true_oracle
```

```bash
# force refine 版本
python scripts/eval_safelibero.py \
    --checkpoint /root/autodl-tmp/checkpoints/baseline_spatial_bowl_0 \
    --config_name baseline_spatial_bowl \
    --suite safelibero_spatial --task_id 0 \
    --true_oracle --force_refine_oracle \
    --sdf_gt_path /root/colliforce-vla/data/sdf_gt_spatial_bowl.npz \
    --refine_alpha 0.1 \
    --n_episodes 50 --gpu 3 \
    --output_prefix true_oracle_force
```

---
