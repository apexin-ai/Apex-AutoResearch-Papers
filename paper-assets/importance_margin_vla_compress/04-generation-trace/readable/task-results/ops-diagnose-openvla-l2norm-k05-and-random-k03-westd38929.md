# ops diagnose openvla l2norm k05 and random k03 westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-openvla-l2norm-k05-and-random-k03-westd38929_20260521T120834_result.json`
- **Structured JSON:** [`932bd2fd4d582bbd45e9.json`](../../sessions/93/932bd2fd4d582bbd45e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总：

## 实验 1: eval_openvla_l2norm_k05_object_seed42_v2 — **完成 ✓**

**Overall SR: 39.2% (196/500)** — 确认与先前崩溃恢复结果一致。

Per-task SR:
| Task | SR |
|---|---|
| ketchup | 70% |
| alphabet_soup | 56% |
| milk | 50% |
| chocolate_pudding | 44% |
| orange_juice | 44% |
| salad_dressing | 38% |
| bbq_sauce | 32% |
| tomato_sauce | 32% |
| cream_cheese | 14% |
| butter | 12% |

Registry: DONE/success, v3 duplicate 标记为 killed。

## 实验 2: eval_openvla_random_k03_object_seed42_v2 — **仍在运行**

PID 2478, GPU 1, 已运行 4h42m。当前进度: task 10/10, ep 10/50。预计 ~25 分钟内完成。

## westd-38929 GPU 状态

| GPU | 状态 | PID | 任务 |
|---|---|---|---|
| 0 | 占用 | 181687 | random k=0.5 seed42 (15h28m) |
| 1 | 占用 | 2478 | random k=0.3 seed42 (~25min剩余) |
| 2 | 占用 | 186986 | baseline seed42 (6h41m) |
| **3** | **空闲** | — | l2norm k=0.5 已完成 |

无活跃 cron 需要删除。GPU 3 现在可用。

---
