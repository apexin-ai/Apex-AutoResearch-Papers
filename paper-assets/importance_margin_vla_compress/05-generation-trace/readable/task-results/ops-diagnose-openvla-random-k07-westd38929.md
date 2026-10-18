# ops diagnose openvla random k07 westd38929

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-openvla-random-k07-westd38929_20260521T115805_result.json`
- **Structured JSON:** [`745b0d58c1bbef114f88.json`](../../sessions/74/745b0d58c1bbef114f88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能之前已清除或在另一个 session 中创建）。

---

## 诊断结果

**实验状态: 完成 (SUCCESS)**

**Overall SR: 44.4%** (222/500, 10 tasks × 50 episodes)

Per-task breakdown:

| Task | SR |
|------|-----|
| alphabet soup | 72% |
| ketchup | 64% |
| orange juice | 64% |
| salad dressing | 56% |
| tomato sauce | 52% |
| bbq sauce | 38% |
| chocolate pudding | 34% |
| milk | 24% |
| cream cheese | 20% |
| butter | 20% |

结果文件: `eval_results/openvla_random_k07_seed42_v2.json` (12:07) 和 `eval_results/openvla_random_prune_k07_object.json` (19:56)，两份内容一致（SR 均为 44.4%）。

**GPU2 状态: 空闲** (1 MiB / 97887 MiB)。GPU0、GPU1、GPU3 各有进程占用 ~16GB。

Registry 已更新为 DONE/success，metrics 已写入。

---
