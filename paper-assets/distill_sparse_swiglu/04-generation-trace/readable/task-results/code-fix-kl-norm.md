# code fix kl norm

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-kl-norm_20260515T135636_result.json`
- **Structured JSON:** [`6d568790d1c0780d0cb4.json`](../../sessions/6d/6d568790d1c0780d0cb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

200 步训练完成。汇报如下：

---

## losses.py 修改 diff

```diff
- seq_len, vocab_size = dense_logits.shape[-2], dense_logits.shape[-1]
- return kl / (seq_len * vocab_size)
+ seq_len = dense_logits.shape[-2]
+ return kl / seq_len
```

`F.kl_div(reduction='batchmean')` 已除以 batch_size，额外只除以 seq_len 得到 per-token KL。之前多除了 vocab_size (128256)，导致 KL ≈ 1e-8。

## train.py Lagrangian 参数（无需修改）

| 参数 | 值 |
|------|-----|
| lambda_init | 1.0 |
| 更新倍率 | ×2.0 (上) / ×0.5 (下) |
| 更新间隔 | 每 25 步 |
| lambda cap | [0.1, 1000] |
| 容忍带 | ±0.02 |

## 每 25 步轨迹

| Step | KL | Sparsity | Constraint | Lambda |
|------|------|----------|-----------|--------|
| 1 | 1.180 | 0.406 | 0.094 | 1.00 |
| 25 | — | 0.398 | — | 1→2 |
| 30 | 0.617 | 0.398 | 0.203 | 2.00 |
| 50 | 0.469 | 0.398 | 0.203 | 2→4 |
| 75 | — | 0.457 | — | 4→8 |
| 80 | 0.586 | 0.520 | 0.000 | 8.00 |
| 100 | 0.582 | 0.506 | 0.000 | 8.00 |
| 125 | — | (in band) | — | 不变 |
| 150 | 0.539 | 0.504 | 0.000 | 8.00 |
| 175 | — | (in band) | — | 不变 |
| 200 | 0.641 | 0.504 | 0.000 | 8.00 |

## 结论

- **KL 量级正确**：step 1 KL = 1.18（预期 ~0.1-0.5 范围略高，但合理——修复前除以 vocab_size 是 ~9e-6）
- **Sparsity 收敛到目标**：step 80+ 稳定在 0.50-0.52，在 ±0.02 容忍带内
- **Lagrangian 工作正常**：3 次 lambda 翻倍（1→2→4→8），step 75 后 sparsity 进入容忍带，lambda 停止更新
- **KL 没有收敛到很低值**（~0.5-0.6），但 200 步 quicktest 目的是验证归一化量级和 Lagrangian 行为，不是完整训练

Checkpoint 已保存到 `/root/distill_sparse_swiglu/checkpoints/kl_normalized_quicktest/predictor_kl.pt`。

---
