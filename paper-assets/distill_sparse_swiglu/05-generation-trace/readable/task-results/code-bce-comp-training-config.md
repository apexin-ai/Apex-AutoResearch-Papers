# code bce comp training config

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bce-comp-training-config_20260515T172020_result.json`
- **Structured JSON:** [`52032ed25b0266fd76fa.json`](../../sessions/52/52032ed25b0266fd76fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 交付物

**`src/train_compensation.py`** — sequential compensation 训练脚本
- 加载冻结的 predictor checkpoint → 训练 CompensationNetwork（per-layer bottleneck MLP: hidden_size → 256 → hidden_size）
- End-to-end KL distillation: `KL(dense_logits, sparse_with_comp_logits)`
- 67.2M 可训练参数（0.84% of model），与 predictor training 同量级
- 已完成 dry-run 验证（batch_size=1, seq_len=128, 2 steps）—— GPU 0/1 当前各被占 ~67.5GB，full-size dry-run 需等 GPU 释放

**`scripts/run_plan001_remaining.sh`** — 8 个 run 的批量调度脚本
- `bce_comp`: 5 seeds（s42/s123/s456 复用现有 predictor，s0/s1 先训 predictor 再训 comp）
- `kl_comp`: 3 seeds（s42/s123/s456 复用 kl_norm_v2 predictor）
- 支持分阶段执行：`bash scripts/run_plan001_remaining.sh bce_comp|kl_comp|bce_pred_new|all`
- BCE+comp 用 cuda:0，KL+comp 用 cuda:1（可并行）

### 关键设计决策

基于 FastForward 论文调研和现有 `train_spon.py` 模板：
- **Sequential 训练**（非 joint）：predictor 冻结 + hard mask，只优化 compensation 参数
- **End-to-end KL loss**（非 per-layer MSE）：直接优化最终输出质量，无需修改 wrapper 捕获逻辑
- **lr=1e-4**（比 predictor 的 1e-3 低一个量级）：compensation 是精修，不需要大 lr
- CompensationNetwork 已集成在 `PredictorWrapper._patch_single_mlp` 中（`result + comp_network.forward_layer(layer_idx, x)`），无需新建 patcher

---
