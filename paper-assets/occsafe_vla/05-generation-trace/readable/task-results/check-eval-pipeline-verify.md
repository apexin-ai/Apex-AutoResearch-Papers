# check eval pipeline verify

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_pipeline_verify_20260525T142449_result.json`
- **Structured JSON:** [`6972bb7f67eafc58237e.json`](../../sessions/69/6972bb7f67eafc58237e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## Eval Pipeline 预验证报告

### 1. Eval 脚本

**路径**: `/root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py`

**关键参数**:
| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--pretrained_checkpoint` | (必填) | checkpoint 路径 |
| `--task_suite_name` | `libero_spatial` | LIBERO 任务集 |
| `--num_rollouts` | 20 | 每个 task 的 rollout 数，需改为 **50** |
| `--collision_threshold` | 0.001 | L1 位移阈值 |
| `--seed` | 42 | 随机种子 |
| `--output_path` | 自动生成 | JSON 输出路径 |
| `--save_videos` | False | 是否保存 MP4 |

### 2. TSR 和 CAR 输出

**同时输出**。脚本计算逻辑：
- **TSR** = 成功完成 task 的 episode 比例
- **CAR** = 无碰撞 episode 比例（碰撞定义：warmup 后任何非目标物体的 L1 位移 > 0.001）

输出 JSON 包含 per-task TSR/CAR、overall TSR/CAR、per-episode 明细（max_displacement, collision_detected, trajectory_length, task_success）、位移统计（min/max/mean/median）。

### 3. SafeLIBERO 环境

**就绪**。从历史 eval 日志（`ablation_occ_detach_s1_50r_eval.log`, `ablation_occ_detach_s2_50r_eval.log`）确认 occsafe conda 环境下 mujoco、robosuite、libero、torch、transformers 均正常加载运行。

### 4. 训练进度

3 个 s3 训练均在 ~10800/50005 步（~22%），速度 ~1.08 it/s。

### 5. 最终 Checkpoint 路径（训练完成后）

```
/root/autodl-tmp/checkpoints/ablation_occ_detach_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt

/root/autodl-tmp/checkpoints/mvp_occ_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt

/root/autodl-tmp/checkpoints/full_occ_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt
```

### 6. Eval 命令模板

训练完成后，可同时在 3 张 GPU 上并行跑 3 个 eval：

```bash
# ablation_occ_detach_s3 — GPU 0
cd /root/occsafe_vla/openvla-oft && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 \
nohup python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 \
    > ~/runs/occsafe_vla/ablation_occ_detach_s3_50r_eval.log 2>&1 &

# mvp_occ_s3 — GPU 1
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 \
nohup python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 \
    > ~/runs/occsafe_vla/mvp_occ_s3_50r_eval.log 2>&1 &

# full_occ_ln_s3 — GPU 2
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 \
nohup python vla-scripts/evaluate_safelibero.py \
    --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
    --task_suite_name libero_spatial \
    --num_rollouts 50 \
    > ~/runs/occsafe_vla/full_occ_ln_s3_50r_eval.log 2>&1 &
```

**结论**：eval pipeline 就绪，无阻塞项。训练完成后可直接执行上述命令。

---
