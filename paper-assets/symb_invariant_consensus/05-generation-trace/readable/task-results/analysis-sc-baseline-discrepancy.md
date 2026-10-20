# analysis sc baseline discrepancy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sc-baseline-discrepancy_20260520T135659_result.json`
- **Structured JSON:** [`fc92555d00a3364bda98.json`](../../sessions/fc/fc92555d00a3364bda98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因完全确认。以下是完整调查结果：

---

## 调查结果

### 差异根因：Tiebreaking 策略不同

7 个问题（不是 3 个）的 SC 判定不同，**全部是投票 tie**（票数完全相等）。净差异 = 5 - 2 = 3 题。

| 问题 | Gold | 票数分布 | exp033 选择 | exp089 选择 | 谁对 |
|------|------|---------|------------|------------|------|
| folio_42 | True | Unknown:5, True:5 | Unknown | True | exp089 |
| folio_65 | True | True:5, False:5, Unknown:2 | True | False | exp033 |
| folio_83 | False | Unknown:5, False:5, +1噪声 | Unknown | False | exp089 |
| folio_99 | Unknown | Unknown:5, True:5, +1噪声 | Unknown | True | exp033 |
| folio_100 | True | Unknown:4, True:4, +2噪声 | Unknown | True | exp089 |
| folio_157 | False | Unknown:5, False:5 | Unknown | False | exp089 |
| folio_163 | False | Unknown:5, False:5 | Unknown | False | exp089 |

### 两种 Tiebreaking 机制

**exp033** (`SelfConsistency` class, 旧版本): `max(groups.keys(), key=count)` — **dict 插入顺序** 决定 tie。由于 traces 中 "Unknown" 通常出现在前面的 trace 中，ties 倾向于选 "Unknown"。

**exp089** (独立脚本): `max(sorted(candidates), key=count)` — **字母序** 决定 tie。"False" < "True" < "Unknown"。

### Normalization 完全一致

两边都使用相同的 `normalize_logic_answer()`，映射表一致：
```python
{"true": "True", "false": "False", "unknown": "Unknown", "uncertain": "Unknown", ...}
```

`is_equiv()` vs `==` 的差异**不影响**结果——对 "True"/"False"/"Unknown" 这些简单字符串，两者等价。

### 建议

1. **论文用 exp089 的值 (SC = 55.88%, 114/204)**。字母序 tiebreaking 是确定性的、可复现的，而 dict 插入顺序依赖 trace 生成顺序。
2. **统一 normalization**：当前 `SelfConsistency` class 已更新为 `max(sorted(...))` 版本，与 exp089 一致。无需再改代码。
3. **论文注脚建议**：可以提到 204 题中 7 题存在 exact majority-vote tie（3.4%），SC baseline 对 tiebreaking convention 敏感。这也说明 SICA 在 tie 区域提供额外信号的价值。

---
