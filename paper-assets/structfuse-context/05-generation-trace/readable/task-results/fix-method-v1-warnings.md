# fix method v1 warnings

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_method-v1-warnings_20260514T230021_result.json`
- **Structured JSON:** [`01c51df84591d088362c.json`](../../sessions/01/01c51df84591d088362c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 处修改完成：

| # | 修改 | 内容 |
|---|------|------|
| W1 | Projection head | "linear projection head" → "two-layer MLP projection head (Linear→GELU→Linear)" |
| W2 | Pooling 策略 | 补充 "mean pooling over non-padding positions of the last hidden layer"，位于 encoder architecture 段 |
| W3 | pos-weight | **查证结果**：`pos_weight_alpha=1.0`，但所有策略的 `pos_dataflow_distance` 均为 1（含 dataflow_aware 和 embedding_distance）。weight = exp(-1) ≈ 0.368 为常数，等效于 unweighted InfoNCE。已在公式后说明此机制存在但实际未生效 |
| W4 | Epoch | "3 epochs" → "2 epochs with early stopping (patience=2)；s42 用 3 epochs 提供完整 overfitting curve，后续 seeds 用 2 epochs" |
| I1 | L2 norm | 在 pooling 描述后补充 "followed by L2 normalization" |
| I2 | FusionHead | 确认 method_v1.md 中无提及，无需改动 |

---
