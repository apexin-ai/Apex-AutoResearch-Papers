# diagnose train phase2 lambda0 extra seed

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_train_phase2_lambda0_extra_seed_20260527T141518_result.json`
- **Structured JSON:** [`d1e59dc160ab403ec4a7.json`](../../sessions/d1/d1e59dc160ab403ec4a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

memory.md 已有记录：`wandb 未配置：训练命令需加 export WANDB_MODE=disabled`。这次的失败正是因为训练命令没加这个。无需新增 memory 条目。

---

```
失败原因: wandb.init() 因无 API key 报错退出。训练命令缺少 `export WANDB_MODE=disabled`，
         而服务器上无 .netrc、无 WANDB_API_KEY 环境变量、无 wandb config 目录。
         
         Traceback 关键行:
         train_pytorch.py:403 → init_wandb → wandb.init → 
         UsageError: No API key configured. Use `wandb login` to log in.

修复建议: 在训练命令中加 `export WANDB_MODE=disabled`，即：
         bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && 
         cd /root/colliforce-vla && export WANDB_MODE=disabled && 
         python scripts/train_a1_sdf_aux_pi05.py --scene object_pudding --seed 0 
         --lambda_sdf 0.005 --gpu 1 --num_train_steps 10000 
         --exp_name phase2_stage1_seed0_l005"

是否可立即重试: 是。cuda:1 当前空闲（0MiB），磁盘 6GB 可用，conda 环境完好。
               只需在命令中补上 export WANDB_MODE=disabled 即可重试。
```

**补充信息**：`/tmp/phase2_stage1_s0.log` 是另一个实验的日志（正在 step 1768/10000 正常训练中），不是本次失败实验的日志。本次失败的完整 traceback 在 `~/runs/diff_collision_sdf/train_phase2_lambda0_extra_seed.log`。

---
