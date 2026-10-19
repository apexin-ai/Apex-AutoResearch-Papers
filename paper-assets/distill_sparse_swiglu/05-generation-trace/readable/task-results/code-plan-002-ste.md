# code plan 002 ste

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_002_ste_20260515T183953_result.json`
- **Structured JSON:** [`5c8b6bef99af04d89628.json`](../../sessions/5c/5c8b6bef99af04d89628.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行：

- **KL-STE Lagrangian** 正确启动（relaxation=STE）
- **Step 1**: loss=6.97, sparsity=0.539
- **Step 10**: loss=3.375, sparsity=0.539
- 无 NaN/inf，数值合理，lambda 在正常调整

实验 `ste_kl_s42` 已在 cuda:1 上运行（1000 步），代码改动总结：

- **predictor.py**: 新增 `STEMask` 类 — 前向用 hard threshold (`sigmoid > 0.5 → 1/0`)，反向通过 `hard - sigmoid.detach() + sigmoid` 让梯度流过 sigmoid
- **train.py**: 新增 `kl_ste` loss_type 和 `train_kl_ste()` 函数 — 与 `train_kl_normalized` 相同的 KL loss + Lagrangian 约束，仅将 GumbelSigmoidMask 替换为 STEMask，无 tau annealing

---
