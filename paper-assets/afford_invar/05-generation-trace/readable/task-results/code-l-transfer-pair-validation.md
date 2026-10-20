# code l transfer pair validation

**afford invar** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l-transfer-pair-validation_20260519T222514_result.json`
- **Structured JSON:** [`4094ed202ae123d38b9b.json`](../../sessions/40/4094ed202ae123d38b9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**判定: MARGINAL**（阈值 0.85 下 avg_pos/anchor=4.8）

关键数据：

| Threshold | #Positive Pairs | Avg Pos/Anchor |
|-----------|----------------|----------------|
| 0.80 | 5,986 | 15.3 |
| **0.85** | **1,867** | **4.8** |
| 0.90 | 485 | 1.2 |

三个重要发现：

1. **降阈值到 0.80 即可解决** — avg_pos/anchor 从 4.8 跳到 15.3，进入 SUFFICIENT 区间
2. **libero_90 有大量完全相同指令的不同 task** — Top-20 跨任务对全部 sim=1.0，都是 libero_90 内不同 task_id 但指令文本完全一样（如 "pick up the book and place it in the left compartment of the caddy" 同时出现在 libero_90_74 和 libero_90_82）。815/1867 正对来自 libero_90 内部
3. **跨 suite 正对为零** — spatial/object/goal 之间没有任何正对。L_transfer 只在同 suite 内起作用，无法提供跨 suite 语义对齐

12/130 个任务在 0.85 阈值下完全孤立（无正对）。

报告已写入 `artifacts/ltransfer_positive_density.md`。

---
