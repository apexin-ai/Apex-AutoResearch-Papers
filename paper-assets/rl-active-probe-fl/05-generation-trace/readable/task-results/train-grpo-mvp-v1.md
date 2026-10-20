# train grpo mvp v1

**rl active probe fl** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_grpo-mvp-v1_20260514T064405_result.json`
- **Structured JSON:** [`6d8ff85ceaa674116243.json`](../../sessions/6d/6d8ff85ceaa674116243.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动。状态：

- **模型加载**：检测到 LoRA adapter，正在加载 base model (Qwen3-8B) + SFT adapter，5/5 shards 已加载完成
- **GPU**：使用 device 0，分配 90% 显存
- **警告**：vLLM 版本兼容性警告（非致命，不影响训练）和 `torch_dtype` deprecation 提示（无影响）
- **tmux session**：`grpo-mvp-v1`
- **日志文件**：`~/runs/rl-active-probe-fl/grpo-mvp-v1.log`

模型加载顺利，接下来会进入 adapter merge 和 GRPO trainer 初始化阶段。可用 `tail` 日志持续跟踪进度。

---
