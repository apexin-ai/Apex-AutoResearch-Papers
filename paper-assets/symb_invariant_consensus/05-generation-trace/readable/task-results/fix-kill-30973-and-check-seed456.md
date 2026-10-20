# fix kill 30973 and check seed456

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-30973-and-check-seed456_20260523T203700_result.json`
- **Structured JSON:** [`2a7938e3f22cccad3050.json`](../../sessions/2a/2a7938e3f22cccad3050.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个组件的 tiebreaking 都是 alphabetical：

**SC** (`baselines/self_consistency.py`):
```python
best_answer = max(sorted(groups.keys()), key=lambda k: len(groups[k]))
```
`sorted` 先按字母排序，`max` 在票数相同时保留第一个（字母序最小）。

**SICA** (`sica/scorer.py` → `select_answer`):
```python
# 分数 tie → 按频次
# 频次也 tie → sorted(top)[0] 即字母序最小
top_by_count = sorted(a for a in top if answer_counts.get(a, 0) == max_count)
return top_by_count[0]
# 无 answer_counts 时:
return sorted(top)[0]
```
所有 tie 最终 fallback 到 `sorted(...)[0]`，即 alphabetical。

## 结果

**任务 1**：westd-30973 上所有冗余进程已 kill，3 块 GPU 全部释放 (0 MiB)，无残留 tmux session。

**任务 2**：seed456_v2 使用的 tiebreaking 方式已确认为 **alphabetical**（SC 和 SICA 均如此）。**无需修正**。

---
