# analysis p0 bootstrap ci

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p0_bootstrap_ci_20260516T051544_result.json`
- **Structured JSON:** [`9a42a7e92721ba13356b.json`](../../sessions/9a/9a42a7e92721ba13356b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
Random Tiebreak Baseline:
- Tied problems: 5/60
- SC (current tiebreak): 42/60 = 70.0%
- SC (random tiebreak, expected): 42.5/60 = 70.8%
- SICA: 44/60 = 73.3%
- SICA vs SC_random gap: +2.5 pp

Paired Bootstrap 95% CI:
- Paired diff breakdown: SICA_only_correct=3, SC_only_correct=1, both_same=56
- Mean accuracy difference (SICA - SC): +3.3pp
- 95% CI: [-3.3, 10.0] pp
- p-value (proportion of bootstrap samples <= 0): 0.2261
```

关键发现：

1. **5 个平票题**，全部 gt 都在 tied candidates 中，random tiebreak 期望正确 2.5 题（SC 实际答对了 2 题）。SC_random = 70.8%，SICA 仍领先 **+2.5pp**。

2. **Bootstrap CI 跨零**：[-3.3, 10.0]pp，p=0.23。60 题样本量下，3.3pp 的差距统计上不显著——只有 4 题 discordant（3 题 SICA 赢、1 题 SC 赢），信号太稀疏。这在论文里需要诚实报告，同时可以用更大数据集（D012 扩展到 200+ 题）来增强统计效力。

---
