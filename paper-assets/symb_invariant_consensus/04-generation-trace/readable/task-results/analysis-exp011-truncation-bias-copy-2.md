# analysis exp011 truncation bias

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp011-truncation-bias_20260517T105204_result.json`
- **Structured JSON:** [`93926360df4f33c1451b.json`](../../sessions/93/93926360df4f33c1451b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键发现：

**Truncation 不解释 SICA 的优势。**

交叉表：
```
                Truncated   Not-trunc   Total
  sica_wins          1          4        5
    sc_wins          0          1        1
 concordant         15         39       54
      Total         16         44       60
```

- 5 个 SICA wins 中只有 1 个涉及 truncation（idx=24, 3/12 traces truncated），其余 4 个完全没有截断
- 唯一的 SC win 也无截断
- Fisher exact test p=1.0，无统计显著关联

额外发现：
- 实际只有 16/60 问题有 any truncated trace（不是任务描述中的 44 条——44 可能是 trace 级别计数，不是 problem 级别）
- 仅 1/60 问题的 majority traces 被截断
- 截断问题的 constraint extraction rate (0.865) 低于非截断问题 (1.000)，但 SICA 的 discordant wins 几乎全部来自非截断问题

**结论：SICA +6.67pp 的增益不是 truncation artifact，而是真实的方法效果。**

---
