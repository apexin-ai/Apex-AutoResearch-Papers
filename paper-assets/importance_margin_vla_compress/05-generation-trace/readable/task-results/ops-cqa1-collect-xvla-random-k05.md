# ops cqa1 collect xvla random k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-collect-xvla-random-k05_20260521T052528_result.json`
- **Structured JSON:** [`74f96bc9c552a94a7ff9.json`](../../sessions/74/74f96bc9c552a94a7ff9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## X-VLA Random k=0.5 Object — seed42 结果（已完成）

**Overall SR: 353/500 (70.6%)**，95% Wilson CI: [66.5%, 74.4%]，耗时 76.0 min

| Task | 描述 | SR |
|------|------|-----|
| 0 | pick up the alphabet soup | 96% (48/50) |
| 1 | pick up the cream cheese | 46% (23/50) |
| 2 | pick up the salad dressing | 98% (49/50) |
| 3 | pick up the bbq sauce | 80% (40/50) |
| 4 | pick up the ketchup | 100% (50/50) |
| 5 | pick up the tomato sauce | 76% (38/50) |
| 6 | pick up the butter | 2% (1/50) |
| 7 | pick up the milk | 82% (41/50) |
| 8 | pick up the chocolate pudding | 26% (13/50) |
| 9 | pick up the orange juice | 100% (50/50) |

结果与预期一致（SR=70.6%）。结果已保存至 `eval_results/xvla_prune_k0.5_libero_object.json`。

**seed43** 目前仍在运行中（当前在 Task 3），cuda:2 上有 python 进程占用 4521MiB 显存，GPU 利用率 0%（在等 episode 间 reset）。

---
