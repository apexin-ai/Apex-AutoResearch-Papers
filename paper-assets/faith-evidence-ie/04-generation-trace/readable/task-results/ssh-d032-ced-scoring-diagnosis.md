# ssh d032 ced scoring diagnosis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d032-ced-scoring-diagnosis_20260515T010820_result.json`
- **Structured JSON:** [`cce3b98560fddc55d096.json`](../../sessions/cc/cce3b98560fddc55d096.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 246 个文档的 CED 诊断已完成。

---

```
== D032 CED Scoring 诊断结果 ==
分析 doc 数: 246
每 doc 候选数: 8

CED Score 分布:
- 全局 mean: 0.5667
- 全局 std: 0.3071
- 跨文档 std 均值 (mean_std): 0.1425
- 跨文档 std 中位数: 0.1245
- top1-bottom1 gap 均值: 0.4203
- top2-bottom2 gap 均值: 0.3354

Evidence 多样性:
- sentence_ids Jaccard overlap rate: 0.7405 (mean), 0.7352 (median)

CED Score 分位数:
  P  0: 0.0000
  P 10: 0.0105
  P 25: 0.3581
  P 50: 0.5911
  P 75: 0.8088
  P 90: 0.9823
  P100: 0.9977

结论: 可行
原因: mean_std=0.1425>0.05 且 top2-bottom2 gap=0.3354>0.1，CED 方差足够支撑 rejection sampling
```

**关键发现**：

1. **CED 方差充足**：每个文档 8 个候选的 CED std 均值 = 0.1425（远超 0.05 阈值），top2-bottom2 gap = 0.3354（远超 0.1 阈值）。Rejection sampling 有足够的信号区分好坏候选。

2. **Triple-set 虽然几乎相同（之前观测 diversity=0.9/8），但 evidence 引用确实有差异**：sentence_ids Jaccard overlap ~0.74，约 26% 的 evidence 差异来自不同的 sentence 引用组合，这正是 CED 奖励可以区分的维度。

3. **CED 分布呈现良好的区分度**：P10=0.01 vs P90=0.98，说明最差和最好的候选之间有接近满分的差距。top-25% 筛选策略可以有效选出高质量 evidence。

---
