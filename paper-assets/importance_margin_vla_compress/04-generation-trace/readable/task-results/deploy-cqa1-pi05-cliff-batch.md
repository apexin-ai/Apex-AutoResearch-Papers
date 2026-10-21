# deploy cqa1 pi05 cliff batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_pi05_cliff_batch_20260525T053430_result.json`
- **Structured JSON:** [`389074f63160343bc9e7.json`](../../sessions/38/389074f63160343bc9e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部成功启动，日志确认配置正确且已开始加载模型：

| GPU | exp_id | suite | prune_mode | 状态 |
|-----|--------|-------|------------|------|
| 0 | eval_pi05_random_k085_goal_seed42_postfix_v3 | libero_goal | random | ✅ 加载模型中 |
| 1 | eval_pi05_l2norm_k085_object_seed42_postfix_v2 | libero_object | l2norm | ✅ 加载模型中 |
| 2 | eval_pi05_random_k085_long_seed42_postfix_v3 | libero_10 | random | ✅ 加载模型中 |
| 3 | eval_pi05_l2norm_k085_long_seed42_postfix_v3 | libero_10 | l2norm | ✅ 加载模型中 |

所有实验已正常启动，正在加载 π0.5 模型权重。

---
