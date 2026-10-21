# deploy long seed42 r4 rerun

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_long-seed42-r4-rerun_20260522T171932_result.json`
- **Structured JSON:** [`95654973244b40e21148.json`](../../sessions/95/95654973244b40e21148.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

**汇总：**
- **实验**: `eval-pi05-vla-only-long-seed42-r4-rerun`
- **服务器**: bjb1-18228, **cuda:1**（cuda:0 被 CRM precompute 占用，改用 cuda:1）
- **PID**: 89827
- **状态**: RUNNING，模型已开始加载
- **日志**: `/root/acr-vla-conformal-refinement/logs/eval_long_vla_only_seed42_r4_rerun.log`
- **注意**: 参数 K 被解析为 1（非 10），log 显示 `'K': 1`——检查 evaluate.py 的 `--K` 参数是否被正确传入。其余参数（n_action_steps=10, max_steps=520, n_rollouts=20, seed=42）均正确。

---
