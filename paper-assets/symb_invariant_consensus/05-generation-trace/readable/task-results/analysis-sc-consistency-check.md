# analysis sc consistency check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sc-consistency-check_20260518T171756_result.json`
- **Structured JSON:** [`23ae310a263c1e8927c0.json`](../../sessions/23/23ae310a263c1e8927c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认完毕。

---

## SC 一致性检查结果

### 1. Tie-breaking 逻辑差异

唯一差异在 **folio_123**，vote 分布 `Unknown: 6, False: 6`（K=12 完美 tie），gold = `False`。

| | Oracle 脚本 | 主 pipeline (SelfConsistency) |
|---|---|---|
| 实现 | `max(sorted(keys), key=count)` | `max(groups_dict, key=len)` |
| tie-break | `sorted()` → `['False','Unknown']`，`max()` 保留首个 → **False** | dict 按插入序迭代，trace 中 `Unknown` 先出现 → **Unknown** |
| SC 正确? | ✓ (False == gold) | ✗ (Unknown ≠ gold) |

**根因**：Python `max()` 遇到相等 key 时返回**第一个**遇到的元素。Oracle 脚本先 `sorted()` 使字母序确定性，`False` < `Unknown` 所以 `False` 胜出。主 pipeline 用 dict 插入序（即 trace 出现顺序），`Unknown` 先出现所以 `Unknown` 胜出。

### 2. Divergent 题目

**folio_123**，仅此 1 题。

### 3. 影响

**不影响论文结论。** 这是一个 tie（6:6 完美平票）的非确定性 tie-breaking 差异，不是算法逻辑 bug。两个 SC 数字（75.00% vs 75.49%）差 0.49pp，在论文中报哪个都合理。建议统一 tie-breaking 策略（如都用 `sorted` 后取首个），然后用统一后的数字。

---
