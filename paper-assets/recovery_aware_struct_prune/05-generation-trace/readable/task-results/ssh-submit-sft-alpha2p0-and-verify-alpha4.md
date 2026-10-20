# ssh submit sft alpha2p0 and verify alpha4

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_sft_alpha2p0_and_verify_alpha4_20260523T221212_result.json`
- **Structured JSON:** [`0185b9259460a9bfc26f.json`](../../sessions/01/0185b9259460a9bfc26f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总结果：

### 输出

**1. GPU 验证**：GPU 2 已确认空闲（0% util, 0MiB），符合提交条件。

**2. sft_rasp_alpha2p0_20_fixed**：已提交，tmux session `eval_math500_sft_rasp_alpha2p0_20_fixed` 运行中，PID **171964**（CUDA_VISIBLE_DEVICES=2），模型正在加载中。

**3. grpo_alpha4_20 身份确认**：README 显示是 GRPO 训练的模型（`model_name: grpo_alpha4_20`，tags 包含 `grpo` 和 `trl`），base model 显示为 `None`（未记录 base model 路径），W&B run ID `cvbwau6d`。从命名和 GRPO tag 看，**是 alpha=4.0 剪枝模型经 GRPO 训练的结果**，但 README 未显式记录 alpha 值，需要通过 W&B run 或训练脚本确认具体 base model。config.json 架构为 `Qwen2ForCausalLM`。

**4. grpo_standard_20_fixed 结果**：**accuracy = 27.0%**（135/500），stderr = 0.0199。EOS stats: 278 natural EOS, 222 truncated, avg response length 1127.8。

---
