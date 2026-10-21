# ops cqa1 collect l2norm results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-collect-l2norm-results_20260521T080536_result.json`
- **Structured JSON:** [`74369bcc45d21bb0bfe8.json`](../../sessions/74/74369bcc45d21bb0bfe8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## 结果

### eval_xvla_l2norm_k07_object_seed42_v2 — DONE ✓
- **SR = 58.2%** (291/500), 95% CI [53.8%, 62.4%]
- mode = `l2_norm` 已确认
- D132 crossover 确认：**random k=0.7 (65.2%) > L2norm k=0.7 (58.2%)，差距 +7.0pp**
- 与 seed44 (56.4%) 一致，seed42 稍高但在 CI 范围内

### eval_xvla_l2norm_k05_object_seed42 — 仍在运行
- mode = `l2_norm` 已确认
- 当前进度：Task 4 开头（10 tasks 中完成了 4 个）
- 预计还需 ~50-60 分钟

## GPU 状态 (cqa1-33015)

| GPU | 显存 | 利用率 | 状态 |
|-----|------|--------|------|
| 0 | 4537/24564 MiB | 58% | 占用 (l2norm k=0.5 seed42 + 可能其他 eval) |
| 1 | 4537/24564 MiB | 62% | 占用 (eval_xvla_random_k05_object_seed44) |
| **2** | **1/24564 MiB** | **0%** | **空闲** |
| 3 | 4540/24564 MiB | 27% | 占用 (eval_xvla_random_k07_object_seed43_v2，接近完成) |

**GPU 2 现在空闲**，GPU 3 上的 random k=0.7 seed43 v2 接近完成（Task 9 ep 48-49），很快也会释放。

---
