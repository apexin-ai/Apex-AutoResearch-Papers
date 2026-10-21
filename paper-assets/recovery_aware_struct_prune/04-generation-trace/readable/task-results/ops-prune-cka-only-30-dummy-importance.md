# ops prune cka only 30 dummy importance

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prune_cka_only_30_dummy_importance_20260517T215102_result.json`
- **Structured JSON:** [`31c2160d2df29e8080f7.json`](../../sessions/31/31c2160d2df29e8080f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正常运行，正在加载模型。检测到非均匀 MLP 结构（intermediate_size range [8128, 18944]），说明剪枝生效。

## 产出汇总

| 项目 | 结果 |
|---|---|
| Dummy importance | `results/importance_scores_dummy_ones.pt` — 28层 attn+mlp 全 1，已验证 |
| 剪枝 | 成功。MLP 303/784 groups pruned, 0 attn pruned, 实际 sparsity 28.92%。产出 11G @ `/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30/` |
| Eval | PID **58841**, cuda:2, tmux session `eval_postprune_cka_only_30`, log: `~/runs/recovery_aware_struct_prune/eval_postprune_cka_only_30.log` |

---
