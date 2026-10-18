# inspect westd41074 deploy long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_inspect_westd41074_deploy_long_20260526T013109_result.json`
- **Structured JSON:** [`d8a7114334fc0d0dc3d5.json`](../../sessions/d8/d8a7114334fc0d0dc3d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 巡检结果

| GPU | PID | 命令 | 显存 | 运行时间 | 状态 |
|-----|-----|------|------|----------|------|
| **GPU0** | — | — | 1 MiB | — | **空闲** |
| **GPU1** | 76492 | `l2norm_prune --k_ratio 0.5 --suite libero_object` | 15961 MiB | ~5.2h | 运行中 |
| **GPU2** | 259181 | `attention_prune --k_ratio 0.7 --suite libero_object` | 15961 MiB | ~1.2h | 运行中 |
| **GPU3** | 259256 | `random_prune --k_ratio 0.7 --suite libero_object` | 15961 MiB | ~1.2h | 运行中 |

### 结论

**GPU2/3 不空闲**，正在跑 Object suite 的 k=0.7 实验（attention_prune 和 random_prune），约 1.2 小时前启动。无法立即部署 Long 实验。

**GPU0 空闲**，按指示不部署，等 Agent 协调。

GPU1 的 l2norm_k05_object 已跑 5.2 小时，可能接近完成。GPU2/3 的 Object k=0.7 实验跑了 1.2 小时，Object suite 通常需要几个小时，预计还需等待。

建议：等 GPU2/3 的 Object k=0.7 实验完成后再部署 Long 实验。

---
