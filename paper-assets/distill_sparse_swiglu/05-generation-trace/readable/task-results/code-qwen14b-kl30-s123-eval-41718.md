# code qwen14b kl30 s123 eval 41718

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen14b_kl30_s123_eval_41718_20260519T150546_result.json`
- **Structured JSON:** [`40ec86456ad4668c8ac2.json`](../../sessions/40/40ec86456ad4668c8ac2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。总结：

- **exp_id**: `qwen14b_kl30_s123_eval_v5`（v4 已在 registry 中存在为 DONE）
- **服务器**: westd-41718 cuda:1，PID 154366
- **checkpoint**: 从 westd-34887 复制了 `qwen14b_kl30_s123/predictor_kl_normalized.pt`（234MB，14B predictor）到 westd-41718（westd-41718 原来只有 8B 的 `kl_30pct_s123`）
- **D075 修复**: 已确认 evaluate.py line 78 使用 `torch.sigmoid(logits)`
- **tasks**: wikitext2, arc_challenge, winogrande, hellaswag, piqa, mmlu（6 tasks，与 v3/v4 对齐）
- **模型级稀疏率**: 0.296（日志已开始输出）
- **cuda:0 未受影响**: PID 152255 (`qwen14b_teal30_uniform_hspiqa_v2`) 仍在运行
- **日志**: `~/runs/distill_sparse_swiglu/qwen14b_kl30_s123_eval_v5.log`
- **临时 SSH key 已清理**

注意：`submit_training_job` 工具不在当前可用工具列表中，使用了 nohup 方式（符合 C002 约束）。

---
