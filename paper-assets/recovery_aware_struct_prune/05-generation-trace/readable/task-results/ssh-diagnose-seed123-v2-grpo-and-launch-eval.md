# ssh diagnose seed123 v2 grpo and launch eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_diagnose_seed123_v2_grpo_and_launch_eval_20260522T145733_result.json`
- **Structured JSON:** [`4ac4221a373adfb409c8.json`](../../sessions/4a/4ac4221a373adfb409c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

1. **GRPO 训练**：成功完成 100/100 steps（18:42），checkpoint-100 model.safetensors **12GB** ✓
2. **W&B run**：`j1ut733l`（run name: grpo_sft_random_20）
3. **Eval PID**：56283（bash wrapper 56278）
4. **GPU:0 显存**：目前 0 MiB — 模型仍在 CPU 加载阶段（RSS ~13.5GB，CPU 500%），尚未迁移到 GPU。这个 12GB 非均匀结构模型的 CPU 加载预计还需 1-2 分钟

其他 eval 同时在跑：GPU:2 = sft_depth_first_20 (PID 54882)，GPU:3 = grpo_depth_first_20 (PID 51986)，均 29GB 显存 / 99% 利用率。

GPU:0 显存上涨后即进入推理阶段，无需额外操作。

---
