# eval openvla random pruning sweep

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_random_pruning_sweep_20260519T212747_result.json`
- **Structured JSON:** [`877db74c72f9c11db7ca.json`](../../sessions/87/877db74c72f9c11db7ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有数据点已存在，无需重跑。**

主服务器 (westd-27271) 上已有完整的 OpenVLA random pruning eval 结果，全部 n=500, seed=7（互相一致）：

| k_ratio | SR | successes/total | seed | timestamp |
|---------|------|-----------------|------|-----------|
| 0.95 | **69.4%** | 347/500 | 7 | 2026-05-19 08:26 |
| 0.90 | **62.0%** | 310/500 | 7 | 2026-05-19 08:33 |
| 0.70 | **49.0%** | 245/500 | 7 | 2026-05-18 12:26 |
| 0.50 | **37.4%** | 187/500 | 7 | 2026-05-18 07:57 |
| 0.30 | **20.6%** | 103/500 | 7 | 2026-05-18 18:19 |

加上 baseline k=1.0 (74%)，6-point 曲线数据齐全。所有点 seed 一致（seed=7），n_episodes 均为 500。k=0.90 和 k=0.95 刚于今天在 westd-27271 上跑完。

结果路径：`/root/autodl-tmp/importance_margin_vla_compress/eval_results/openvla_random_prune_k{ratio}_object.json`（在 westd-27271 上）。

不需要在 westd-41074 上启动新的 eval。

---
