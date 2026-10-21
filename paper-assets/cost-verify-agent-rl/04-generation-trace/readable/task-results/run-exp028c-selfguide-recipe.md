# run exp028c selfguide recipe

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp028c_selfguide_recipe_20260515T213342_result.json`
- **Structured JSON:** [`4470be33552c8c951fbe.json`](../../sessions/44/4470be33552c8c951fbe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行，双卡满载（41GB VRAM, GPU 利用率 45%/100%）。

## 产出汇总

| 项目 | 状态 |
|------|------|
| **参数冲突检查** | `ppo_mini_batch_size` 从计划的 256 降至 **128**。原因：`train.py:159` 断言检查 trajectory 级别（`env_groups*group_size*effective_ratio >= ppo_mini_batch_size`），不考虑 step_independent 展开。实际训练样本 ~3200，128 的 mini-batch 分成 ~25 个 mini-batches |
| **Config 文件** | `/root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp028c_selfguide_recipe.yaml` |
| **启动脚本** | `/root/cost-verify-agent-rl/scripts/run_exp028c_selfguide_recipe.sh` |
| **训练状态** | PID=824675, W&B run=`4yu6qz1m`, 双卡 cuda:0+1 |
| **Registry** | exp028c_selfguide_recipe → RUNNING, notes 已记录 9 项改动 + 冲突结论 |

**9 项实际改动**：mini_batch 32→128, steps 50→100, LR 5e-7→1e-6, KL 0.005→0.01, env_groups 8→16, group_size 16→8, entropy 0.01→0.001, history_length 5→2, loss_agg seq-mean-token-mean→token-mean。model_path 保持 SFT checkpoint 不变。

---
