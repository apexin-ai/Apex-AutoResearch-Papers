# ops detach ln s3 eval launch

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_detach-ln-s3-eval-launch_20260526T230813_result.json`
- **Structured JSON:** [`4c2b67156a4ab39c9ea3.json`](../../sessions/4c/4c2b67156a4ab39c9ea3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已成功启动并在正常运行：

| 任务 | GPU | PID | 状态 |
|------|-----|-----|------|
| detach_ln_s3_eval | cuda:2 (57%, 16.8GB) | 565722 | T0: 24% (12/50) |
| cutoff_25k_s1_v2_eval | cuda:3 (43%, 16.8GB) | 567676 | T0: 8% (4/50) |

**使用的脚本**：`vla-scripts/evaluate_safelibero.py`

**完整命令**：
```bash
# detach_ln_s3_eval (cuda:2)
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt \
  --num_rollouts 50 --seed 42 --task_suite_name libero_spatial

# cutoff_25k_s1_v2_eval (cuda:3)
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt \
  --num_rollouts 50 --seed 42 --task_suite_name libero_spatial
```

日志位置：`/tmp/detach_ln_s3_eval.log`、`/tmp/cutoff_25k_s1_v2_eval.log`。westd-34685 四张卡现在全部在跑 eval。

---
