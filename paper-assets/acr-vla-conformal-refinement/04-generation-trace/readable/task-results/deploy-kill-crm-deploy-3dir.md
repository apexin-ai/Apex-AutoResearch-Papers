# deploy kill crm deploy 3dir

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_kill-crm-deploy-3dir_20260523T011208_result.json`
- **Structured JSON:** [`e3919738f5c4bbf5eeda.json`](../../sessions/e3/e3919738f5c4bbf5eeda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

### 产出

**1. Partial results 已保存** → `artifacts/crm_eval_partial_results.md` (已注册 art_20260523_bd0dfb)

**2. 意外情况**: `pkill -f 'evaluate.py'` 误杀了 tmux server（PID 218130 的命令行包含 `evaluate.py`），导致 cuda:3 上的 train_crm 也被终止。已从 `checkpoint_epoch0032.pt` 恢复训练，确认 resume 成功（epoch 33 继续中，val_loss=0.006075）。

**3. 5 个实验全部启动成功，无 argparse error：**

| Session | GPU | Mode | max_correction_norm |
|---------|-----|------|---------------------|
| dirA_norm03 | cuda:0 | crm_obs_only | 0.3 |
| dirA_norm01 | cuda:1 | crm_obs_only | 0.1 |
| dirA_norm005 | cuda:2 | crm_obs_only | 0.05 |
| dirB_adaptive | cuda:4 | adaptive_conformal_crm | tau=0.074855 |
| dirC_reconvla | cuda:5 | reconvla | K=10 |

**4. train_crm (resumed)**: cuda:3, epoch 33/50 from checkpoint_epoch0032

**PID 列表** (从进程输出):
- train_crm: 548658/548664
- dirA_norm03: 548888
- dirA_norm01: 549157
- dirA_norm005: 549426
- dirB_adaptive: 550037
- dirC_reconvla: 550634

---
