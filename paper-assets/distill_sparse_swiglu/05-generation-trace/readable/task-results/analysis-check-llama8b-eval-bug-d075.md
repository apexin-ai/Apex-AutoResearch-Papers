# analysis check llama8b eval bug d075

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_llama8b_eval_bug_d075_20260519T135252_result.json`
- **Structured JSON:** [`09919f7a01c626c70bd7.json`](../../sessions/09/09919f7a01c626c70bd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。结论如下：

---

## 结果

### 1. LLaMA-8B 是否使用了相同的 buggy score 代码

**是。** LLaMA-8B 所有 uniform eval 都走 `benchmark_eval.py` → `teal_global_masks()` （`evaluate.py:81`）:
```python
hard_mask = (logits > 0).float()
mag = intermediates[layer_idx].abs().float()
scores = (mag * hard_mask).mean(dim=(0, 1))
```
与 Qwen-14B 完全相同的代码路径。

### 2. Per-layer sparsity 是否存在 sparsity=0

**不存在。** 两台服务器共检查了 10 个 LLaMA-8B uniform eval 日志，覆盖 5 个 sparsity 水平（25/30/35/45/50%）和 3 个 seed（42/123/456），**32 层全部精确命中目标 sparsity**，无任何异常：

| 实验 | 目标 | 实际 per-layer |
|---|---|---|
| kl30 s42/s123/s456 | 30% | 0.301 × 32 |
| kl50 s42/s123/s456 | 50% | 0.500 × 32 |
| kl25 s42 | 25% | 0.250 × 32 |
| kl35 s42 | 35% | 0.352 × 32 |
| kl45 s42 | 45% | 0.449 × 32 |

对比 Qwen-14B（Layer 1-4 sparsity=0.000）明确不同。

### 3. 结论：LLaMA-8B uniform eval 不需要重跑

Bug 不在 LLaMA-8B 上触发。原因：LLaMA-8B 的 predictor 在每层都有足够多非零 `mag * hard_mask` score（predictor 在 calibration data 上对每个 neuron 至少部分时间 logit>0），因此 `_uniform_topk_masks` 的 top-k threshold 始终 >0，sparsity 分配正确。

Qwen-14B 的问题出在 Layer 1-4，这些层的 predictor 在 calibration 期间几乎对所有 neuron 输出 logit≤0，导致大多数 score=0 → threshold=0 → `s >= 0` 全 True → mask 全 1 → sparsity=0。

### 4. 受影响实验

**无。** 所有 LLaMA-8B uniform eval 实验结果有效，无需重跑。

---
