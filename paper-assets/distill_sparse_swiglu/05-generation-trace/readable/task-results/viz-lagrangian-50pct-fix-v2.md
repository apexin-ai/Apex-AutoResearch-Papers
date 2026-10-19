# viz lagrangian 50pct fix v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_lagrangian_50pct_fix_v2_20260517T060112_result.json`
- **Structured JSON:** [`647edf3b119c18327d46.json`](../../sessions/64/647edf3b119c18327d46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图已成功生成（177KB PNG）。任务完成：

- **数据来源**：从 `/root/runs/distill_sparse_swiglu/mvp_kl_norm_v2_s42.log` 提取了完整 1000 步数据（101 个点，每 10 步 + step 1）
- **替换结果**：`kl_50pct_s42` 从 48 点（200 步截断）更新为 101 点（1-1000 步）
- **Lambda 范围**：1.95 - 1000.00；**Sparsity 范围**：0.406 - 0.529
- **输出文件**：`lagrangian_dynamics.pdf` 和 `.png` 已更新，50% 曲线现在延伸到 1000 步，与其他三条线一致

---
