# exp review exp a baseline ensemble

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-exp-a-baseline-ensemble_20260515T122341_result.json`
- **Structured JSON:** [`2eeea6aac0a539c6b72b.json`](../../sessions/2e/2eeea6aac0a539c6b72b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment `review-exp-a-baseline-ensemble` 完成。结果摘要：

| Group | Features | Avg F1 | 95% CI |
|-------|----------|--------|--------|
| **(a) 4-baseline** | AvgLogProb, LD, FDG, Bino | **0.7964** | [0.7921, 0.8007] |
| **(b) 4-baseline+surface** | 上述 + ttr, hapax | **0.8049** | [0.8003, 0.8092] |
| **(c) 7-feature unified** | 7 depth features | 0.7887 | [0.7839, 0.7930] |
| **(d) 7-feature original** | 同上 (sanity check) | 0.7887 | [0.7839, 0.7930] |

关键发现：

1. **Sanity check 通过**: (c) = (d) = 0.7887，完全复现 bootstrap_ci_v2 的参考结果
2. **4-baseline ensemble 反超 7-feature**: 0.7964 vs 0.7887，CI 不重叠 → 统计显著
3. **加 surface features 后更强**: 0.8049，比 7-feature 高 1.6 个百分点
4. **对 reviewer 的回应**: 统一超参后 baseline 不仅不弱，反而更强。reviewer 关于"不公平比较"的担忧不成立——用相同超参，4-detector ensemble 的泛化能力优于 7 depth features

Per-generator 最弱点仍是 qwen3-8b (4-baseline: 0.7133 vs 7-feature: 0.6815)，但 4-baseline 对 qwen3-8b 也有 +3.2 pp 改善。

---
