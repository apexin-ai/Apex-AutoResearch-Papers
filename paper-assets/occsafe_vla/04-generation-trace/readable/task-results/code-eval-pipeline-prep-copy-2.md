# code eval pipeline prep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_eval-pipeline-prep_20260527T032119_result.json`
- **Structured JSON:** [`a0719edd8a387e27762f.json`](../../sessions/a0/a0719edd8a387e27762f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。以下是完整结果。

---

## Eval 脚本验证

两台服务器 `evaluate_safelibero.py` 均存在且一致。使用 `draccus` dataclass 配置，关键参数：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--pretrained_checkpoint` | (必填) | checkpoint 路径 |
| `--num_rollouts` | 20 | 每任务 rollout 数 |
| `--seed` | 42 | 随机种子 |
| `--task_suite_name` | libero_spatial | 任务集 |
| `--collision_threshold` | 0.001 | 碰撞检测阈值 |

## GPU → 实验映射（从运行进程确认）

**注意**: 用户提到的 `_r2`/`_35` 后缀是口头简称，实际 `--run_id_note` 和 checkpoint 目录名如下：

### westd-34685 (4 GPU, RTX PRO 6000 Blackwell)

| 物理 GPU | PID | 实际实验名 | 用户简称 |
|----------|-----|-----------|---------|
| 0 | 681204 | `detach_ln_v2_s1` | detach_ln_v2_s1_35 |
| 1 | 677648 | `detach_ln_s4` | detach_ln_s4 |
| 2 | 735982 | `ablation_occ_detach_s4` | ablation_occ_detach_s4 |
| 3 | 736344 | `mvp_occ_s4` | mvp_occ_s4 |

### westd-10894 (4 GPU, RTX PRO 6000 Blackwell)

| 物理 GPU | PID | 实际实验名 | 用户简称 |
|----------|-----|-----------|---------|
| 0 | 481426 | `full_occ_ln_v2_s1c` | full_occ_ln_v2_s1c_r2 |
| 1 | 481643 | `full_occ_ln_v2_s2` | full_occ_ln_v2_s2_r2 |
| 2 | 481988 | `detach_ln_v2_s0c` | detach_ln_v2_s0c_r2 |
| 3 | 490883 | `full_occ_ln_v2_s0d` | full_occ_ln_v2_s0d |

## Eval 命令（训练完成后直接执行）

Checkpoint 路径模式: `/root/autodl-tmp/checkpoints/&lt;exp>/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--&lt;exp>`

### westd-34685 — 4 条命令

**GPU 0 — detach_ln_v2_s1 (Cell 4 v2)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 CUDA_VISIBLE_DEVICES=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s1 --num_rollouts 50 --seed 42
```

**GPU 1 — detach_ln_s4 (Cell 4 n=5)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 CUDA_VISIBLE_DEVICES=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s4 --num_rollouts 50 --seed 42
```

**GPU 2 — ablation_occ_detach_s4 (Cell 3 n=5)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 CUDA_VISIBLE_DEVICES=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s4 --num_rollouts 50 --seed 42
```

**GPU 3 — mvp_occ_s4 (Cell 1 n=5)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 CUDA_VISIBLE_DEVICES=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s4 --num_rollouts 50 --seed 42
```

### westd-10894 — 4 条命令

**GPU 0 — full_occ_ln_v2_s1c (Cell 2 v2)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 CUDA_VISIBLE_DEVICES=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c --num_rollouts 50 --seed 42
```

**GPU 1 — full_occ_ln_v2_s2 (Cell 2 v2)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 CUDA_VISIBLE_DEVICES=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2 --num_rollouts 50 --seed 42
```

**GPU 2 — detach_ln_v2_s0c (Cell 4 v2)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 CUDA_VISIBLE_DEVICES=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s0c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c --num_rollouts 50 --seed 42
```

**GPU 3 — full_occ_ln_v2_s0d (Cell 2 v2)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 CUDA_VISIBLE_DEVICES=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0d/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0d --num_rollouts 50 --seed 42
```

## 时间估计

- 8 个 eval 全部并行（每 GPU 1 个），总耗时 ~50 min
- 34685 训练 ~12:30 UTC 完成 → eval ~13:20 UTC 完成
- 10894 训练 ~14:21 UTC 最晚完成 → eval ~15:11 UTC 完成
- **全部在 DDL 2026-05-28 12:00 UTC 之前完成**

## 注意事项

1. **Checkpoint 尚不存在**: `detach_ln_v2_s0c` (10894) 和几个实验的 checkpoint 目录存在但训练未完成，最终 checkpoint 在训练结束时写入。启动 eval 前用 `ls` 确认最终 checkpoint 目录已生成。
2. **训练后 GPU 释放不需要手动操作**: 训练进程退出后 GPU 自动释放，可直接启动 eval。
3. **每个 eval 进程独占 1 GPU**: 使用 `CUDA_VISIBLE_DEVICES` 限定单卡，`MUJOCO_EGL_DEVICE_ID` 匹配同一物理编号。

---
