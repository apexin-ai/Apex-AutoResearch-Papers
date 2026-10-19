# ssh unified eval v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_unified-eval-v2_20260515T161753_result.json`
- **Structured JSON:** [`2a1923548d0a80c98d54.json`](../../sessions/2a/2a1923548d0a80c98d54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 checkpoint 全部评估完毕。

```
evaluate.py md5 (真实 v2): 4f2faa315b3e45b0781c1c07c47515eb

BCE s42:  Dense PPL=27.96, Sparse PPL=44.54, Δ%=+59.3%, Model Sparsity=0.496
BCE s123: Dense PPL=28.38, Sparse PPL=44.59, Δ%=+57.1%, Model Sparsity=0.496
BCE s456: Dense PPL=28.14, Sparse PPL=43.03, Δ%=+52.9%, Model Sparsity=0.496

Dense PPL 与 KL eval 一致性: 否 (KL Dense=9.21 vs BCE Dense≈28)
```

**关键发现：Dense PPL 仍然是 ~28，不是 9.21。** 同一个 evaluate.py（同一个 md5）跑出来 Dense PPL 差 3 倍，说明问题不在 evaluate.py 版本差异——而是 KL eval 和 BCE eval 的**运行参数或环境**不同。可能的原因：

1. KL eval 当时用了不同的 `--calibration_samples` 或 `--seq_len`
2. 模型权重路径不同（不同的 llama-3.1-8b 副本）
3. WikiText-2 数据集缓存版本不同

需要查 KL eval 的实际运行日志来确认参数差异。

---
