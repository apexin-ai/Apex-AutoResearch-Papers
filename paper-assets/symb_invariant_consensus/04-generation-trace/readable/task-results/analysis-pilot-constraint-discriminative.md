# analysis pilot constraint discriminative

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pilot-constraint-discriminative_20260517T053102_result.json`
- **Structured JSON:** [`2d42655e952b5bdd560a.json`](../../sessions/2d/2d42655e952b5bdd560a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已经很清楚了。让我输出最终总结。

```
========================================================================
CONSTRAINT DISCRIMINATIVE ANALYSIS - FINAL SUMMARY
========================================================================

Total problems: 43
  - Unanimous (1 answer candidate): 20/43 (46.5%)
  - Multi-answer (≥2 candidates):   23/43 (53.5%)

Among multi-answer problems:
  Total unique constraints: 3614
  Discriminative (by count): 414/3614 = 11.5%
  Discriminative (by weight): 1903/5114 = 37.2%
  Problems with ≥1 discriminative constraint: 23/23 (100%)
  
  Problems where disc. constraints favor different answer than SC: 4/23

========================================================================
CONCLUSION
========================================================================
```

**Discriminative constraints DO exist, but are structurally weak:**

1. **satisfied_ratio=1.0 的原因**：所有约束都是中间推理步骤（domain facts/rules），Z3 可以同时满足所有约束，没有逻辑矛盾。MaxSAT excluded=0。

2. **Discriminative power 有限的原因**：
   - 88.5% 的 unique 约束出现在给出不同答案的 trace 中（non-discriminative）
   - 这些 "共享" 约束的权重与 trace 数量成正比 → SICA 退化为加权 majority vote ≈ SC
   - 仅 37.2% 的权重提供差异化信号
   - 只有 4/23 问题中 discriminative 信号指向不同于 SC 的答案

3. **根本原因**：提取的约束是 `kind_charlie == True`、`Implies(rough_charlie, cold_charlie)` 这类 domain facts — 无论最终答案是 True/False/Unknown，这些中间推理步骤大部分是共通的。约束系统没有提取"答案级别"的判别谓词。

**D030 Pivot 决策输入**: `discriminative_ratio = 37.2%` (by weight)，但有效 flip 率仅 4/23 = 17.4%，最终只贡献 +2.33pp。这证实 constraint filtering 路线的天花板极低 — 不是因为 discriminative constraints "不存在"，而是因为约束的语义层次错误（中间步骤 vs 答案判别）。

---
