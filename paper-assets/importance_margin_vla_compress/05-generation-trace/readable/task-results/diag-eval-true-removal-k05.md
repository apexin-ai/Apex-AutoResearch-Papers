# diag eval true removal k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_true_removal_k05_20260517T094307_result.json`
- **Structured JSON:** [`7b04387a2a442c9c0228.json`](../../sessions/7b/7b04387a2a442c9c0228.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：实验 **completed**，结果为全零

| 项目 | 状态 |
|---|---|
| 进程 | 已死，无 tmux session |
| 结果文件 | `eval_true_removal_k05_object.json` 存在，17:21 写入 |
| 完成度 | 10 tasks × 50 episodes = 500 episodes 全部跑完 |

### 结果

**Overall SR: 0/500 (0.0%)**，所有 10 个 task 全部 0%，每个 episode 都跑满 280 步 timeout。

Sanity check（`sanity_true_removal.json`，仅 2 episodes）也是 0%。

### 解读

True token removal（k=0.5，即移除 50% tokens 缩短序列）彻底破坏了模型行为——机器人完全不动/无意义动作直到超时。和 zero-masking 的效果一致（都是 0%），说明问题不在 "置零引入噪声" vs "真正缩短序列"，而是 pruning 50% vision tokens 本身对 stage1-only checkpoint 就是致命的。

---
