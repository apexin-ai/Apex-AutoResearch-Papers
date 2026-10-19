# ops spatial bowl prep and analysis scripts

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_spatial_bowl_prep_and_analysis_scripts_20260525T151925_result.json`
- **Structured JSON:** [`602697d8086c874d84a7.json`](../../sessions/60/602697d8086c874d84a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

信息收集完毕。以下是结果：

---

## Part A: spatial_bowl 训练

**训练已在运行，无需额外准备。**

`train_pi05_a1_spatial_bowl_s0_l005` 就是 PID 168730：

| 项目 | 值 |
|------|-----|
| 进程 | PID 168730, tmux session `train_pi05_a1_spatial_bowl_s0_l005` |
| 命令 | `python scripts/train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 0 --gpu 0` |
| lambda_sdf | 0.005（脚本默认值，与目标一致） |
| 进度 | **7063/30000 (24%)**, 已跑 ~5h17m |
| 速度 | ~4.63 s/it |
| 预估剩余 | **~29.5h** |
| Checkpoint | `/root/autodl-tmp/checkpoints/a1_sdf_pi05_spatial_bowl/a1_sdf_pi05_spatial_bowl_seed0_l005/` |
| Conda env | `libero` |
| WANDB | disabled |

**SDF 数据**：就位（`/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz`，脚本 SCENE_CONFIG 已配置）。

**GPU 状态**：
- cuda:0 — 训练中 (27GB/98GB, 100% util)
- cuda:1-3 — 空闲 (~9GB/98GB)

如果需要额外启动另一个训练（不同 seed 或不同参数），可用模板：
```bash
tmux new-session -d -s train_spatial_bowl_s1_l005 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && cd /root/colliforce-vla && export WANDB_MODE=disabled && python scripts/train_a1_sdf_aux_pi05.py --scene spatial_bowl --seed 1 --gpu &lt;GPU_ID> --lambda_sdf 0.005 --batch_size 32 --num_train_steps 30000 --save_interval 2000 --log_interval 100 2>&1 | tee logs/train_spatial_bowl_s1_l005.log'
```

---

## Part B: 30K Displacement-Filtered CAR 分析脚本

**状态：不存在，需要编写。**

现有情况：
- `eval_pi05_safelibero.py` 已在 JSON 中保存 per-episode 粒度的数据：
  - `max_displacement`, `collided`, `collision_step`, `collision_obstacle`
  - `per_obstacle_displacement` (每障碍物独立)
  - `per_obstacle_min_ee_distance`, `all_collided_obstacles`
- JSON 格式示例（来自 `pi05_safelibero_object_v11_s1.json`）：每 task 下 `episodes` 数组，每个 episode 有 `max_displacement` 和 `collided`
- **没有** 独立的 displacement-filtered CAR 分析脚本

**需要编写的内容**：一个 post-processing 脚本，读取 eval JSON，计算 displacement-filtered CAR（即：只把 displacement > threshold 的碰撞计为 "真碰撞"，排除微小 displacement 的 false positive）。大约 50-80 行 Python。

输入：eval JSON 路径 + displacement threshold（默认 0.001 是当前 `COLLISION_THRESHOLD`，可设更高阈值如 0.005/0.01 做 sensitivity 分析）

输出：不同 threshold 下的 filtered CAR + per-task breakdown

需要我现在写这个分析脚本吗？

---
