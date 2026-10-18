# analyze eval pi05 random k09 fixedmask object seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_random_k09_fixedmask_object_seed42_v2_20260521T221218_result.json`
- **Structured JSON:** [`a6054b48c6fc52a25d3d.json`](../../sessions/a6/a6054b48c6fc52a25d3d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：`eval_pi05_random_k09_fixedmask_object_seed42_v2`

| 指标 | 值 |
|------|-----|
| **overall_sr** | **17.0%** |
| total_episodes | 500 |
| total_successes | 85 |
| elapsed_min | 111.1 min |
| 完成状态 | EXIT_CODE=0，正常完成 |
| 错误/警告 | 无实质性错误（仅 robosuite 私有宏文件警告和 DeprecationWarning） |

### Per-task SR

| Task | Description | SR |
|------|------------|-----|
| T0 | pick up the alphabet soup... | 12% |
| T1 | (未截取名称) | 26% |
| T2 | (未截取名称) | 16% |
| T3 | pick up the bbq sauce... | 14% |
| T4 | pick up the ketchup... | 12% |
| T5 | pick up the tomato sauce... | 24% |
| T6 | pick up the butter... | 18% |
| T7 | pick up the milk... | 14% |
| T8 | pick up the chocolate pudding... | 24% |
| T9 | pick up the orange juice... | 10% |

### 判断：fixed mask **没有**恢复性能

- **π0.5 baseline (无 pruning)**: 98.2%
- **random k=0.9 stochastic mask**: 12% (seed42)
- **random k=0.9 fixed mask**: 17.0% ← 本实验

Fixed mask 仅从 12% → 17%，微弱提升，远未恢复到 baseline 水平。这说明 **temporal inconsistency 不是 random pruning 灾难性下降的根因**。即使每个 episode 内 mask 固定，random 丢弃 10% vision tokens 仍然导致严重性能崩溃。

根因更可能是：random pruning 丢弃了关键的视觉信息 token（与物体交互相关的 patch），而非 mask 的时序不一致性问题。这强化了 importance-based pruning 的必要性——需要识别哪些 token 重要、哪些可以安全丢弃。

---
