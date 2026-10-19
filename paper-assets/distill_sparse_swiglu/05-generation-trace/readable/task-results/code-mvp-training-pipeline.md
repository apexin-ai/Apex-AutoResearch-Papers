# code mvp training pipeline

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mvp-training-pipeline_20260515T103054_result.json`
- **Structured JSON:** [`281a8a8d1e62e6fe9374.json`](../../sessions/28/281a8a8d1e62e6fe9374.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两项验证均通过：

- `train.py --help`：参数解析正确，所有参数均可用
- `SparsityPredictor` forward：输出 shape `(2, 16, 14336)` 正确，参数量 2,373,760（~2.37M）符合预期

### 写入的文件总结

| 文件 | 功能 |
|------|------|
| `src/predictor.py` | `SparsityPredictor`（rank-128 bottleneck）、`GumbelSigmoidMask`（τ 退火 + hard threshold）、`PredictorWrapper`（monkey-patch 每层 MLP 注入 mask） |
| `src/losses.py` | `KLDistillLoss`（T²-scaled KL div）、`BCESparsityLoss`（top-k binary target）、`SparsityRegularizer`（L1 density penalty） |
| `src/data_utils.py` | SlimPajama streaming loader + WikiText-2/C4 eval dataset packing |
| `src/train.py` | 完整训练循环：KL 模式（双前向 dense+sparse）、BCE 模式（分层计算）、cosine schedule、W&B logging、checkpoint 保存 |
| `src/evaluate.py` | TEAL greedy allocation 实现 model-level 50% sparsity、WikiText-2/C4 perplexity 评估、dense baseline 对比 |

---
