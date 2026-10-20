# analysis mf3 148vs166 discrepancy

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mf3-148vs166-discrepancy_20260524T234415_result.json`
- **Structured JSON:** [`8eec858a93068065725c.json`](../../sessions/8e/8eec858a93068065725c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已经完全清楚。最后一行有个小 bug 但不影响关键输出。

## 结论

**差异原因：answer 归一化**

- **r21 脚本** (`n_disagree=166`)：用原始字符串比较 answer。任何 answer ≠ majority 的 trace 都算 minority。
- **minority_constraint_direction 脚本** (`non_unanimous=148`)：先把 answer 归一化到 `{True, False, Unknown}`。无法归一化的 answer（如自由文本）被丢弃。归一化后全票一致的问题被标为 unanimous。

**18 个差异问题**全部是这种情况：某些 trace 的 answer 不是标准的 True/False/Unknown，而是自由文本（如 `"Marvin is an alien."`, `"koalas love to sleep"`, `"Probably true, but uncertain"` 等）。

| 效果 | r21 | mcd |
|------|-----|-----|
| 自由文本 answer | 算作 minority（≠majority） | 归一化失败，丢弃该 trace |
| 丢弃后剩余全票一致 | — | 标为 unanimous，跳过 |

具体的 18 个 problem：`folio_9, 11, 27, 54, 61, 70, 75, 85, 89, 91, 96, 112, 120, 134, 138, 140, 170, 176`

每个问题的共同特征：**绝大多数 trace (8-11/12) 给出正确格式的一致答案，只有 1-2 条 trace 输出了自由文本而非 True/False/Unknown。**

## 建议

1. **论文应引用 166/204 (81.4%)**，因为这 18 个问题确实存在 trace 间分歧（LLM 输出了不同内容），只是分歧的形式是格式错误而非答案标签不同。
2. **73.6% 的 minority-exclusive ratio 基于 n=148**。如果论文同时引用 81% 和 73.6%，需要注明两者的分母不同，并解释原因（方向性分析要求 minority trace 有可归一化的答案标签）。
3. 或者，可以统一口径：在 minority_constraint_direction 分析中也把自由文本 trace 视为 minority（它们的 constraint 仍然可以分析方向性），这样两边都是 166。

---
