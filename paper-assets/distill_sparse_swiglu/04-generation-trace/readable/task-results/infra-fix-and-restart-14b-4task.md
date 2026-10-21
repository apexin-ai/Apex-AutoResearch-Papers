# infra fix and restart 14b 4task

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix_and_restart_14b_4task_20260518T005234_result.json`
- **Structured JSON:** [`8b4209829305b827cf20.json`](../../sessions/8b/8b4209829305b827cf20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 已正常运行：

- **cuda:0** (KL): PID 87149, 63.9GB VRAM, WikiText-2 已完成，正在跑 lm-eval tasks
- **cuda:1** (TEAL): PID 87288, 34.6GB VRAM, 同上（VRAM 较低因为 TEAL vanilla 不需要 predictor）

HF 缓存路径 `/root/autodl-tmp/.hf_cache` 正确，所有需要的数据集（ai2_arc, winogrande, cais/mmlu, wikitext, gsm8k）都已缓存。离线模式已启用。无需重新提交。

---
