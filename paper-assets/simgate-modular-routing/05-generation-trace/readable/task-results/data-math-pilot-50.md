# data math pilot 50

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_math-pilot-50_20260514T134137_result.json`
- **Structured JSON:** [`2c84a943d350838e920e.json`](../../sessions/2c/2c84a943d350838e920e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered as `art_20260514_c3a7ec`.

---

```
代码执行率: 41/50 (82%)
Internal acc: 40/50 (80%)
CodeInterp acc: 36/50 (72%)
Labels (raw): det=1, int=5, no-pref=44
Labels (filtered): det=1, int=5, no-pref=44
Gate: PASS (82% >= 80%)
```

**关键发现：**

| 指标 | 值 |
|------|-----|
| 代码执行率 | 41/50 (82%) — 刚过 80% 门槛 |
| Internal acc | 40/50 (80%) |
| CodeInterp acc | 36/50 (72%) |
| Filtered (0 code rounds) | 9/50 (18%) |
| 代码轮次分布 | 0轮:9, 1轮:36, 2轮:5 |
| 平均耗时 | 12.0s/题，总计 599s |

**意外结果：Internal reasoning (80%) 反超 Code Interpreter (72%)。** 这导致 label 分布严重偏向 internal-preferred（5 vs 1 det-preferred），大量 no-preference（44/50）。

Filtering 对 label 分布无影响——9 个被过滤的题本来就是 no-preference（两端同对或同错）。

**需要 Director 决策的点：**
- 代码执行率 82% 刚过门槛，18% 仍绕过强制 prompt
- 代码不但没帮忙反而降低了准确率（72% < 80%），可能需要重新评估 MATH 环境下 code interpreter 的价值

---
