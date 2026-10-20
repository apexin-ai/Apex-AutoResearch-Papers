# exp llama fewnerd train v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama_fewnerd_train_v2_20260518T092917_result.json`
- **Structured JSON:** [`01a6f7366cf3fdc3b911.json`](../../sessions/01/01a6f7366cf3fdc3b911.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，监控已设置。

**总结：**
- LLaMA 3.1-8B Few-NERD LoRA 训练在 `autodl-5090` GPU 1 上运行中
- 使用已有配置 `train_config_llama_fewnerd.yaml`（单 GPU，无 accelerate/torchrun）
- 131,767 条训练数据，24,708 步，~1.65s/step，预计约 11 小时完成
- 日志: `logs/llama_fewnerd_train.log`
- Checkpoint 输出: `checkpoints/llama3.1-8b-fewnerd-lora/`
- Cron 每 30 分钟自动检查进度（job ID: `bedeb783`）

---
