# ops check xvla k08 seed43 result

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-xvla-k08-seed43-result_20260520T214308_result.json`
- **Structured JSON:** [`a0a5e7c6aa2a5ddf23d1.json`](../../sessions/a0/a0a5e7c6aa2a5ddf23d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成。日志中有完整结果：

## X-VLA k=0.8 seed43 — LIBERO-Object

**Overall SR: 88.4% (442/500)** | 95% Wilson CI: [85.3%, 90.9%] | 耗时 61.4 min

### Per-task 明细

| Task | 物品 | SR |
|------|------|-----|
| 0 | alphabet soup | **100%** (50/50) |
| 1 | cream cheese | **98%** (49/50) |
| 2 | salad dressing | **100%** (50/50) |
| 3 | bbq sauce | 82% (41/50) |
| 4 | ketchup | 78% (39/50) |
| 5 | tomato sauce | **98%** (49/50) |
| 6 | butter | **58%** (29/50) |
| 7 | milk | 84% (42/50) |
| 8 | chocolate pudding | 88% (44/50) |
| 9 | orange juice | **98%** (49/50) |

短板任务：butter (58%)、ketchup (78%)、bbq sauce (82%)。结果文件保存在 `eval_results/xvla_prune_k08_libero_object_seed43.json`（路径相对于 X-VLA-Libero 项目目录）。

---
