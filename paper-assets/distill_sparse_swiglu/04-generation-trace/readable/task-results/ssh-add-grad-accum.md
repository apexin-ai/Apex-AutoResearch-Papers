# ssh add grad accum

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_add-grad-accum_20260515T121326_result.json`
- **Structured JSON:** [`367669d3fbadf8440518.json`](../../sessions/36/367669d3fbadf8440518.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

dry-run 通过。结果确认：

1. **已有 gradient_accumulation_steps 参数** — 但原实现有 bug（loss 未 scale、step 计数错误）
2. **修改内容**：
   - `train_kl` 和 `train_bce` 改为 nested loop：外层 `opt_step`（optimizer step），内层 micro-batch
   - loss 除以 `gradient_accumulation_steps` 再 backward
   - tau 退火、logging、wandb.log 全部基于 optimizer step
   - `num_steps` 语义 = optimizer step 数（总 forward = num_steps × ga）
3. **dry-run 验证**：
   - 3 个 optimizer step（Step 1/3 → 3/3），每步 2 次 forward（共 6 次 forward）
   - loss 正常下降/变化，无 OOM，checkpoint 正常保存
   - batch_size=2 + ga=2 → effective batch=4

---
