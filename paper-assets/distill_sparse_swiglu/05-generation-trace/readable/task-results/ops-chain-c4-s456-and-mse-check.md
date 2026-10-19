# ops chain c4 s456 and mse check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_chain_c4_s456_and_mse_check_20260520T030912_result.json`
- **Structured JSON:** [`0d7670f5697b3b245f0d.json`](../../sessions/0d/0d7670f5697b3b245f0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s456 已完成。汇总：

```
C4 s123: 完成 PPL=16.3686
C4 s456: 完成 PPL=16.3551
s456 checkpoint: 存在
MSE 训练: step 480/1000, loss=0.0035, sparsity=0.297, checkpoint: 无（训练中）
```

两个 seed 的 C4 PPL 非常接近（16.37 vs 16.36），方差极小。MSE 训练约 48% 进度，在 cuda:0 上正常推进。

---
