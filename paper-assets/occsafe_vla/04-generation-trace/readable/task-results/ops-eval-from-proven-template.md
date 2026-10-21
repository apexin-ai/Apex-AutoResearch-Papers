# ops eval from proven template

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_from_proven_template_20260523T205150_result.json`
- **Structured JSON:** [`459bb1269f7b03c46624.json`](../../sessions/45/459bb1269f7b03c46624.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 eval 进程已经在正常运行中，不需要重启。**

当前状态：

| Eval | PID | GPU | 进度 | 状态 |
|------|-----|-----|------|------|
| reverse_cutoff_s0 | 518746 | GPU 2/3 | T0: 98% (49/50) | 正在运行 |
| cutoff_25k_s0 | 519021 | GPU 2/3 | T0 完成 (TSR=1.000 CAR=0.980), T1 开始 | 正在运行 |

日志文件正在实时更新（最后修改时间 04:54:38/04:54:40），进度条在推进。

---

**产出汇总：**

**1. 完整命令模板**（从运行中进程的 /proc/PID/cmdline 提取）：
```bash
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint &lt;CHECKPOINT_PATH> \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note &lt;RUN_NAME> \
  --seed 42
```

**2. Checkpoint 路径**：
- reverse_cutoff_s0: `/root/autodl-tmp/checkpoints/reverse_cutoff_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`
- cutoff_25k_s0: `/root/autodl-tmp/checkpoints/cutoff_25k_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt`

**3. 步骤 3 跳过** — 进程已在运行，杀掉重启会浪费已完成的进度。

**4. 验证**：
- 两个进程存活，日志实时更新
- 之前的 v2 失败（EXIT_CODE=143 = SIGTERM）已被新一轮 eval 替代
- cutoff_25k_s0 Task 0 已完成，预计 10 个 task 全部完成约需 ~5 小时
- 日志位置：`/tmp/reverse_cutoff_s0_eval.log`、`/tmp/cutoff_25k_s0_eval.log`

---
