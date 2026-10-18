# ops check running experiments p1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-running-experiments-p1_20260520T231412_result.json`
- **Structured JSON:** [`a9ea4fc12cb83cda387b.json`](../../sessions/a9/a9ea4fc12cb83cda387b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

| # | 实验 | 服务器 | 状态 | 进度 |
|---|------|--------|------|------|
| 1 | `eval_openvla_prune_random_k05_seed42` | westd-41074 | **ALIVE** | Task 2/10, Ep 10/50 (~12% total) |
| 2 | `eval_openvla_prune_l2norm_k07_seed43_v2` | westd-27271 | **ALIVE** | Task 2/10, Ep 40/50 (~14% total) |
| 3 | `eval_xvla_prune_k085_seed44` | cqa1-33015 | **DEAD** | 未启动——无 k085 日志文件，GPU 2 空闲 (0%, 1 MiB) |

**cqa1-33015 补充**：`/tmp` 下存在的 xvla 日志为 k=0.2/0.3/0.5/0.7/0.9，均非 k=0.85。其中 k=0.5 seed44 已完成（Overall SR 44.4%）。k=0.85 seed44 实验从未启动或日志路径不同。

---
