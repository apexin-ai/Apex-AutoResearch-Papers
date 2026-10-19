# code implement mse loss

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_implement_mse_loss_20260520T022931_result.json`
- **Structured JSON:** [`eca02dd41f6bb8bee606.json`](../../sessions/ec/eca02dd41f6bb8bee606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**Dry-run（3 steps, batch_size=4, seq_len=2048, sparsity_target=0.3, cuda:0）：**

| Metric | Step 1 | Step 2 | Step 3 |
|--------|--------|--------|--------|
| MSE loss | 0.007992 | 0.008175 | 0.010398 |
| Constraint loss | 0.005005 | 0.001526 | 0.000656 |
| Total loss | 0.012997 | 0.009701 | 0.011054 |
| Sparsity | 0.391 | 0.375 | 0.371 |
| Lambda | 1.0→0.5 | 0.5→0.25 | 0.25→0.12 |
| Step time | 1.3s | 0.9s | 0.9s |

- **显存**：~34.6 GB / 97.9 GB（cuda:0），batch_size=4 无 OOM 风险
- **Sparsity 收敛**：初始 0.391，向 0.3 target 逐步收敛，lambda 自适应下调
- **Loss 量级**：MSE ~0.008-0.01，合理范围
- **Checkpoint**：保存为 `predictor_mse.pt`，格式与 KL/BCE 一致（`{"predictors": ..., "args": ...}`），可直接用 `benchmark_eval.py` 评估

**创建的文件：**
1. `src/train_perlayer_mse.py` — 完整训练脚本（~200 行）
2. `src/losses.py` 末尾追加 `PerLayerMSELoss` 类（~10 行）

---
