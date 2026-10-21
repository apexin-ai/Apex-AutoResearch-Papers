# code train bce comp script

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train_bce_comp_script_20260515T173032_result.json`
- **Structured JSON:** [`a89e6d3b6b0a3f8d101a.json`](../../sessions/a8/a89e6d3b6b0a3f8d101a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Import 和参数解析均通过。

`src/train_bce_comp.py` 已写入服务器，`--help` 验证通过。关键设计：

- **Phase 1** (step 1..`comp_warmup_steps`): BCE + SparsityReg，仅训练 predictor；CompensationHead 通过 `requires_grad_(False)` 冻结
- **Phase 2** (step `comp_warmup_steps+1`..`num_steps`): BCE + comp_loss_weight × CompMSE + SparsityReg，predictor + CompensationHead 联合训练
- **Optimizer**: 单个 AdamW 含两个 param group（predictor_lr / comp_lr），Phase 1 期间 comp params 无梯度自动跳过，Phase 2 解冻后无缝衔接
- **Checkpoint**: 保存 `predictor_bce_comp.pt`（predictors + comp_network + args）

---
