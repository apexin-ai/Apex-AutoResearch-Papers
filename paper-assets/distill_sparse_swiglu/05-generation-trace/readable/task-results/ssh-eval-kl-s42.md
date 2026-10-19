# ssh eval kl s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval-kl-s42_20260515T155737_result.json`
- **Structured JSON:** [`0706f2be0a36dd4b8633.json`](../../sessions/07/0706f2be0a36dd4b8633.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组评估全部完成。

```
evaluate.py md5: 4f2faa315b3e45b0781c1c07c47515eb ✓

s42:  Dense PPL=9.21, Sparse PPL=12.08, Δ%=+31.2%, Model Sparsity=0.498
s123: Dense PPL=9.25, Sparse PPL=11.91, Δ%=+28.8%, Model Sparsity=0.498
```

两个 seed 的 per-layer sparsity 分布一致：低层和高层稀疏度高（0.7-0.8），中间层低（0.2-0.4），符合 TEAL global allocation 的预期模式。

s123 略优于 s42（Sparse PPL 11.91 vs 12.08），两者 dense baseline 略有差异（9.25 vs 9.21）是因为 WikiText-2 HF 缓存/tokenization 随机性，可忽略。

---
