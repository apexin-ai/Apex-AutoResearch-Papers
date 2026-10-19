# experiment eval 4runs v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_eval_4runs_v2_20260512T170825_result.json`
- **Structured JSON:** [`a5ea805d439dbed68608.json`](../../sessions/a5/a5ea805d439dbed68608.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 eval 已实际运行完成。pool_size = 26（1 positive + 25 negatives），所有 127 个样本一致。

## 结果汇总

| strategy | seed | ckpt | recall@1 | recall@5 | recall@10 | pool_size |
|----------|------|------|----------|----------|-----------|-----------|
| random   | 42   | final | 0.9449   | 0.9843   | 0.9843    | 26        |
| random   | 123  | final | 0.9449   | 0.9921   | 0.9921    | 26        |
| random   | 456  | final | 0.9291   | 0.9921   | 0.9921    | 26        |
| emb_dist | 42   | final | 0.6693   | 0.8898   | 0.9291    | 26        |

**关键发现**：
- **random 策略**三个 seed 的 recall@1 均在 92.9%–94.5%，recall@5/10 在 98.4%–99.2%，非常稳定
- **embedding_distance 策略**显著差于 random：recall@1 仅 66.9%（下降 ~27pp），recall@5 降到 89.0%，recall@10 降到 92.9%
- embedding_distance 的负采样让模型面对更难的 negatives，但 final checkpoint 的表现明显退化，可能是训练不够充分或 hard negative 策略需要调整

---
