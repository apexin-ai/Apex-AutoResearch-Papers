# diag bjb1 18228 recovery

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb1-18228-recovery_20260526T031747_result.json`
- **Structured JSON:** [`39f7342ddf54145c7332.json`](../../sessions/39/39f7342ddf54145c7332.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。现在整理完整报告。

---

## 状态检查报告

### bjb1-18228
**连接状态**: 成功  
**GPU**: 4x RTX 4090，全部空闲（0% 利用率，0MiB 显存）  
**进程**: 无 evaluate.py 进程运行，无 tmux session（重启后全部被杀死）

#### 实验结果

| 实验 | 状态 | 结果 |
|------|------|------|
| **pi05-crm-k2-long-s44** | **完成** | overall_success_rate=**80%** (160/200)。Registry 已更新为 success |
| **pi05-crm-k2-long-s42** | **被杀死，需重跑** | 日志显示跑到第10个task (KITCHEN_SCENE6) 的 rollout 15/20 时被杀。距完成仅差5个rollout，无JSON输出 |
| **pi05-crm-k2-long-s43** | **被杀死，需重跑** | 日志显示跑到第10个task (KITCHEN_SCENE6) 的 rollout 5/20 时被杀。差15个rollout，无JSON输出 |
| **eval-mechanism-goal-adapt-s42** | **已失败（非重启导致）** | 启动即 crash：`FileNotFoundError: '/root/acr-vla-conformal-refinement/checkpoints/crm_smolvla_3suite_v1/crm_best.pt'`。checkpoint 路径应为 `/root/autodl-tmp/checkpoints/...`。Registry 已标记 failed |

### bjb2-40593
**连接状态**: **失败** — `Unable to connect to port 40593 on 106.38.204.136`  
需要用户去控制台查新端口并更新 SSH 配置。

### 需要重新部署的实验清单

1. **pi05-crm-k2-long-s42** — π0.5 CRM Long seed42，原命令：
   ```
   CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 42 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed42_pi05_K2.json
   ```

2. **pi05-crm-k2-long-s43** — π0.5 CRM Long seed43，原命令：
   ```
   CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py --model pi05 --mode crm_obs_only --K 2 --max_correction_norm 0.05 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_pi05_unified_3suite/crm_best.pt --obs_dim 2048 --unified_obs_dim 2088 --benchmark long --seed 43 --n_rollouts 20 --output_file logs/eval_long_crm_obs_only_norm0.05_seed43_pi05_K2.json
   ```

3. **eval-mechanism-goal-adapt-s42** — 需修正 checkpoint 路径为 `/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt` 后重跑

bjb1-18228 有 4 块空闲 4090，可立即部署以上 3 个实验。等主 Agent 安排。

---
