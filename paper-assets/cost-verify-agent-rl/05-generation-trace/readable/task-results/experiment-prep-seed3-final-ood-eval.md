# experiment prep seed3 final ood eval

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_prep-seed3-final-ood-eval_20260520T211127_result.json`
- **Structured JSON:** [`34e5d15f01f0d208fc37.json`](../../sessions/34/34e5d15f01f0d208fc37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

配置验证通过。

---

**配置文件**: `/root/autodl-tmp/cost-verify-agent-rl/RAGEN/config/_alfworld_exp029_seed3_ood_final.yaml`（与 `/root/cost-verify-agent-rl/RAGEN/config/` 是同一文件）

**预期 checkpoint 路径**: `/root/autodl-tmp/checkpoints/exp029-seed3/global_step_15`
- save_freq=5, total_steps=15, 当前已有 step_5 和 step_10

**提交命令**（训练完成后直接执行）:
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/cost-verify-agent-rl/RAGEN && CUDA_VISIBLE_DEVICES=0,1 WANDB_PROJECT=cost-verify-agent-rl python train.py --config-name _alfworld_exp029_seed3_ood_final"
```

**关键参数确认**:
| 参数 | 值 |
|------|-----|
| resume_from_path | `exp029-seed3/global_step_15` |
| n_gpus_per_node | 2（匹配训练 FSDP） |
| val_env_groups | 134（全部 OOD 任务） |
| val_tags | AlfworldSG_OOD |
| val temperature | 0.4 |
| seed.train | 42（匹配 seed3） |
| total_training_steps | 1（只 eval） |
| val_before_train | true |

**潜在问题**: 如果 seed3_v2 训练异常终止（未走到 step 15），`global_step_15` 不存在。启动前需先确认 `ls /root/autodl-tmp/checkpoints/exp029-seed3/global_step_15/`。

---
