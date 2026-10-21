# eval post grpo qwen math batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_post_grpo_qwen_math_batch_20260516T155847_result.json`
- **Structured JSON:** [`65953534175859744416.json`](../../sessions/65/65953534175859744416.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部正常。GPU 2/3 正在加载模型（IO 被前两个占满，稍后就会上显存）。

**汇总**：

| exp_id | GPU | 状态 | tmux session |
|--------|-----|------|-------------|
| eval_grpo_rasp_25_qwen_math | cuda:0 | RUNNING, 54.7GB VRAM | ✓ |
| eval_grpo_standard_25_qwen_math | cuda:1 | RUNNING, 48.7GB VRAM | ✓ |
| eval_grpo_rasp_20_qwen_math | cuda:2 | RUNNING, 加载中 | ✓ |
| eval_grpo_standard_20_qwen_math | cuda:3 | RUNNING, 加载中 | ✓ |

- 旧进程 21403/21483 已 kill
- 4 个模型路径均使用根目录（有 `model.safetensors`）
- Registry 已全部推进到 RUNNING
- 输出：`/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_*.json`

---
