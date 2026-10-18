# check iv exclusion restriction

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_iv-exclusion-restriction_20260523T082512_result.json`
- **Structured JSON:** [`d26f7a95407fc0917906.json`](../../sessions/d2/d26f7a95407fc0917906.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== IV Exclusion Restriction Check ===
Models found: 9

Model                        | MMLU acc |  ARC acc | MMLU rank | ARC rank
------------------------------------------------------------------------------
claude-3-haiku               |   0.7667 |   0.4500 |       2.0 |      1.0
claude-opus-4-6              |   0.8900 |   0.9867 |       6.0 |      8.0
claude-sonnet-4-6            |   0.8100 |   0.9533 |       4.0 |      3.0
gemini-3.1-pro-preview       |   0.9547 |   0.9865 |       7.0 |      7.0
gemini-3.5-flash             |   0.9683 |   1.0000 |       9.0 |      9.0
gpt-4.1-mini                 |   0.8000 |   0.9633 |       3.0 |      4.0
gpt-4.1-nano                 |   0.6333 |   0.8533 |       1.0 |      2.0
gpt-4.1                      |   0.8367 |   0.9667 |       5.0 |      5.0
gpt-5.5                      |   0.9567 |   0.9832 |       8.0 |      6.0

Spearman rank correlation: r = 0.9000, p = 0.0009
```

**Verdict: r = 0.900 > 0.8 → IV INVALID，只能用 reduced-form。**

MMLU 和 ARC 的 clean accuracy rank 高度相关（ρ = 0.90, p < 0.001），排除性限制（exclusion restriction）不成立——一个 benchmark 上的 capability 几乎完全预测另一个 benchmark 上的 capability，无法将其作为有效工具变量。

注意：数据中只有 9 个模型（非预期的 15 个），但 9 个模型已足够得出明确结论。

---
