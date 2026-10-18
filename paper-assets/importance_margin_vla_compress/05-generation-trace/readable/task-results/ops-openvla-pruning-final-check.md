# ops openvla pruning final check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_openvla_pruning_final_check_20260517T194718_result.json`
- **Structured JSON:** [`5d5822dd0ee661c7e07b.json`](../../sessions/5d/5d5822dd0ee661c7e07b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态总结

**进程 697608：活跃运行中**（GPU 0, 71% util, ~16GB VRAM）

### 已完成：Baseline eval (libero_object)
| Task | SR |
|---|---|
| alphabet soup | 0.78 |
| cream cheese | 0.80 |
| salad dressing | 0.82 |
| bbq sauce | 0.46 |
| ketchup | **0.96** |
| tomato sauce | 0.78 |
| butter | 0.58 |
| milk | 0.72 |
| chocolate pudding | 0.68 |
| orange juice | 0.82 |
| **Overall** | **0.74 (370/500)** |

耗时 226 min。

### 进行中：Random Prune k=0.5 eval
当前在 Task 1/10，Ep 30/50（256→128 tokens）。按 baseline 速度估算，整个 pruning eval 还需约 3.5 小时完成。

**Pruning 结果尚未产出。** 进程正在跑 random_prune_k05 的第一个 task，预计全部完成时间约 07:15 CST。

---
