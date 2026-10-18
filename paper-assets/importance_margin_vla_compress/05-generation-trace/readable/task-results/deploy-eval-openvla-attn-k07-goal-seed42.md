# deploy eval openvla attn k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_eval_openvla_attn_k07_goal_seed42_20260526T132022_result.json`
- **Structured JSON:** [`13af96ddb88eabf1099e.json`](../../sessions/13/13af96ddb88eabf1099e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:0 和 cuda:1 均被占用，无法部署。**

当前占用情况：

| GPU | PID | 运行时间 | 实验 |
|-----|-----|---------|------|
| cuda:1 | 246725 | 2h06m | `random_prune k=0.7 goal seed42` |
| cuda:0 | 307307 | 8m25s | `l2norm_prune k=0.7 goal seed42` |

两个都是 Goal k=0.7 的 eval 实验，cuda:0 上的 l2norm 刚启动 8 分钟，cuda:1 上的 random 已跑 2 小时。需要等其中一个完成后再部署 Attention k=0.7 实验。

---
