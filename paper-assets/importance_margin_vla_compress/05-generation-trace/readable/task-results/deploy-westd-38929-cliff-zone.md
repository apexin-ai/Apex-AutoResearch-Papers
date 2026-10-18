# deploy westd 38929 cliff zone

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd-38929-cliff-zone_20260525T180918_result.json`
- **Structured JSON:** [`91fea3f1a100344f05c0.json`](../../sessions/91/91fea3f1a100344f05c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部正常运行，已开始评估 Task 1/10：

| GPU | exp_id | mode | k | token 裁剪 | 状态 |
|-----|--------|------|---|-----------|------|
| cuda:0 | `eval_openvla_attn_k07_long_seed42_v2` | attention_prune | 0.7 | 256→179 | running |
| cuda:1 | `eval_openvla_l2norm_k07_long_seed42_v2` | l2norm_prune | 0.7 | 256→179 | running |
| cuda:2 | `eval_openvla_random_k07_long_seed42_v2` | random_prune | 0.7 | 256→179 | running |
| cuda:3 | `eval_openvla_l2norm_k085_long_seed42_v2` | l2norm_prune | 0.85 | 256→217 | running |

每个实验 500 episodes（10 tasks × 50），libero_10 suite，timeout 12h。

---
