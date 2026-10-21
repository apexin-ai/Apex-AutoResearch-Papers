# exp mse lr sweep 30 s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mse_lr_sweep_30_s42_20260524T100212_result.json`
- **Structured JSON:** [`e1aad49dd7e3a3a8d586.json`](../../sessions/e1/e1aad49dd7e3a3a8d586.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已提交并在运行中：

| Exp ID | LR | GPU | Status |
|--------|-----|------|--------|
| `mse30_lr2e4_s42` | 2e-4 | cuda:0 | RUNNING |
| `mse30_lr1e4_s42` | 1e-4 | cuda:1 | RUNNING |

**配置确认：**
- 模型：LLaMA-3.1-8B (`/root/autodl-tmp/models/llama-3.1-8b`)
- Loss：Per-layer MSE (FFN output)
- Sparsity：30%, uniform, Lagrangian constraint
- Seed：42, num_steps=1000, batch_size=4, seq_len=2048, warmup=100
- 训练后自动链式执行 WikiText-2 eval（`benchmark_eval.py --tasks wikitext2`）
- wandb 已禁用（服务器无 API key）
- 日志：`~/runs/distill_sparse_swiglu/mse30_lr{2e4,1e4}_s42.log`

**早期训练信号（~step 40）：**
- LR=2e-4: mse=0.00697, sparsity=0.402
- LR=1e-4: mse 略高（符合预期，学习更慢），sparsity=0.406

每步 ~0.9s，预估 1000 步约 15 分钟完成训练 + eval。

---
