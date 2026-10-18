# data alt diversity extract

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_alt-diversity-extract_20260523T131153_result.json`
- **Structured JSON:** [`c9bbc4f3c6e12f498469.json`](../../sessions/c9/c9bbc4f3c6e12f498469.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/docs/paper/data/alt_diversity_measures.txt`。

关键数据：

| Measure | D\_fdr\_sig | sig+/sig- | mean \|β\_std\| | corr w/ K\_eff (ρ) |
|---|---|---|---|---|
| Q-statistic | 2/12 | 1/1 | 0.080 | 0.674 / 0.708 |
| Disagreement | 8/12 | 7/1 | 0.186 | 0.861 / 0.860 |
| κ-diversity | 7/12 | 7/0 | 0.194 | 0.942 / 0.947 |

注意：alt\_diversity\_effect\_size.json 中 12 个条件是 2 benchmarks × 6 manipulations **pooled across K**，没有 K=3/K=5 拆分。K\_eff 的 K=3/K=5 参考数据从 k5\_aggregation\_analysis.json 补充（majority\_vote: K=3 keff 8/12, K=5 keff 12/12）。

---
