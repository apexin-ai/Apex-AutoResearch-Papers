# Eval 失败诊断报告

**日期**: 2026-05-23  
**服务器**: westd-34685  
**状态**: 已自动修复，eval 正在运行中

## 失败概要

| 实验 | EXIT_CODE | 失败时间 (UTC) | 重提交后状态 |
|------|-----------|---------------|-------------|
| cutoff_25k_s0_eval | 2 | 2026-05-23T20:34:18Z | 运行中 (PID 502810, GPU 3) |
| reverse_cutoff_s0_eval | 2 | 2026-05-23T20:34:20Z | 运行中 (PID 503993, GPU 2) |

## 根因分析

**错误类型**: 命令行参数错误（argparse unrecognized argument）

**错误信息**（两个实验完全相同）:
```
evaluate_safelibero.py: error: unrecognized arguments: --num_trials_per_task 50
```

**原因**: 第一次提交的 eval 命令使用了 `--num_trials_per_task 50`，但 `evaluate_safelibero.py` 不接受此参数。正确参数为 `--num_rollouts 50`。argparse 对无法识别的参数返回 exit code 2。

## 修复情况

已通过 nohup 方式重新提交，使用正确参数 `--num_rollouts 50`。当前进度：
- **cutoff_25k_s0_eval**: Task 0, 41/50 rollouts (82%)
- **reverse_cutoff_s0_eval**: Task 0, 32/50 rollouts (64%)

重提交命令（已在运行）:
```bash
# cutoff_25k_s0_eval (GPU 3)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
CUDA_VISIBLE_DEVICES=3 MUJOCO_EGL_DEVICE_ID=3 MUJOCO_GL=egl WANDB_MODE=disabled \
nohup python /root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note cutoff_25k_s0_eval \
  --seed 42 > /tmp/cutoff_25k_s0_eval.log 2>&1 &

# reverse_cutoff_s0_eval (GPU 2)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
CUDA_VISIBLE_DEVICES=2 MUJOCO_EGL_DEVICE_ID=2 MUJOCO_GL=egl WANDB_MODE=disabled \
nohup python /root/occsafe_vla/openvla-oft/vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note reverse_cutoff_s0_eval \
  --seed 42 > /tmp/reverse_cutoff_s0_eval.log 2>&1 &
```

## 注意事项

- exit file (`/tmp/agent-ml-exit/*.exit`) 仍为旧的失败记录，不反映当前运行状态
- 当前 eval 通过 nohup 启动，不在 tmux session 中，无 EXIT trap 写 exit file
- 日志输出在 `/tmp/*.log`，不在 `~/runs/occsafe_vla/`
