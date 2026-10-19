# experiment p2b eval 4runs pool50

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_p2b_eval_4runs_pool50_20260512T195326_result.json`
- **Structured JSON:** [`74062224b7900cd618c6.json`](../../sessions/74/74062224b7900cd618c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 checkpoint 评估完成。汇总结果：

| strategy | seed | ckpt | recall@1 | recall@5 | recall@10 | pool_size |
|---|---|---|---|---|---|---|
| random | 42 | final | 0.496 | 0.843 | 0.945 | 50 |
| random | 123 | final | 0.535 | 0.850 | 0.921 | 50 |
| random | 456 | final | 0.543 | 0.843 | 0.953 | 50 |
| emb_dist | 42 | final | 0.488 | 0.835 | 0.874 | 50 |

**Random 策略均值**: R@1=0.525, R@5=0.845, R@10=0.940

**关键发现**:
- Random 三个 seed 之间差异不大（R@1: 0.496-0.543）
- **emb_dist 在 R@10 上明显低于 random**（0.874 vs 0.940 均值），说明 embedding distance 负采样策略生成的 harder negatives 反而让模型更难区分 top-10
- pool_size 从 25→50 后，所有指标均有所下降（符合预期，更大 pool 更难）

---
