# check eval results collect

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval_results_collect_20260517T125019_result.json`
- **Structured JSON:** [`6c83752b8068ec079108.json`](../../sessions/6c/6c83752b8068ec079108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Eval 1: k=0.3 trained ACIS pruning (cqa1-33015) — 仍在运行

当前进度：Task 8 ep 3/50，还剩 Task 8 和 9，预计 ~10 分钟完成。

已完成 task 的 SR：

| Task | Description | SR |
|------|------------|-----|
| 0 | — | 0/50 (0.0%) |
| 1 | — | 27/50 (54.0%) |
| 2 | — | 31/50 (62.0%) |
| 3 | — | 37/50 (74.0%) |
| 4 | — | 21/50 (42.0%) |
| 5 | — | 13/50 (26.0%) |
| 6 | — | 16/50 (32.0%) |
| 7 | pick up the milk and place it in the basket | 25/50 (50.0%) |

前 8 个 task 累计：170/400 = **42.5%**

---

### Eval 2: Goal suite k=0.5 true_removal pruning (westd-27271) — 已完成

**Overall SR: 0.0%** (0/500)

所有 10 个 task 全部 0/50。k=0.5 的 true_removal 在 libero_goal 上完全失效，模型能力被彻底摧毁。

JSON 已保存至 `eval_results/eval_goal_prune_k05.json`。

---

Eval 1 还需约 10 分钟完成，要等它结束后再汇总吗？

---
