# m103 scp and resubmit westd38929 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_m103_scp_and_resubmit_westd38929_long_20260525T044510_result.json`
- **Structured JSON:** [`dd4b692e339d1a3795c7.json`](../../sessions/dd/dd4b692e339d1a3795c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。总结：

| GPU | exp_id | mode | k_ratio | 状态 |
|-----|--------|------|---------|------|
| 0 | `eval_openvla_attn_k09_long_seed42_v3` | attention_prune | 0.9 | 运行中，已开始 Task 1/10 |
| 1 | `eval_openvla_attn_k085_long_seed42_v3` | attention_prune | 0.85 | 运行中 |
| 2 | `eval_openvla_random_k09_long_seed42_v3` | random_prune | 0.9 | 运行中，已开始 Task 1/10 |
| 3 | `eval_openvla_l2norm_k09_long_seed42_v3` | l2norm_prune | 0.9 | 运行中 |

- 服务器：westd-38929，4 GPU 各跑一个
- 模型：从 westd-27271 补传了 2 个缺失 shard（00003, 00004），15G 完整
- suite：libero_10 (Long)，10 tasks x 50 episodes = 500 total
- Registry 已注册，状态 RUNNING

---
