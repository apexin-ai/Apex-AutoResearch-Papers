# code fix sft eos restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-sft-eos-restart_20260514T235437_result.json`
- **Structured JSON:** [`6122bcfbf1173db57ad7.json`](../../sessions/61/6122bcfbf1173db57ad7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**两个 SFT 训练已经在运行，无需修复。**

诊断结果：
- `sft_rasp_20` 和 `sft_standard_20` 均已启动，tmux session 活跃
- EOS 断言**通过**了：`Dataset prepared: 7473 samples. EOS verified (token='<｜end▁of▁sentence｜>', id=151643)`
- `apply_chat_template()` 对 DeepSeek-R1-Distill-Qwen-7B 的 tokenizer（包括 pruned 版本）会正确追加 `<｜end▁of▁sentence｜>` EOS token
- 当前进度：两个 job 均在 step ~365/1870（epoch 1 约 19%），约 1.07s/step

loss 值暂未在日志文件中直接可见（HuggingFace Trainer 的 loss 通过 `\r` 覆盖式进度条输出，重定向到文件后会被截断）。第 10 步（`logging_steps=10`）后的 loss 应出现在 trainer 内部记录中。可以等到 epoch 1 结束时查看 checkpoint 的 `trainer_state.json` 获取完整 loss 曲线。

---
