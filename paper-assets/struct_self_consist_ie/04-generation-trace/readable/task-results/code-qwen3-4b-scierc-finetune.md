# code qwen3 4b scierc finetune

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen3_4b_scierc_finetune_20260515T185817_result.json`
- **Structured JSON:** [`38160692571299f42c04.json`](../../sessions/38/38160692571299f42c04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，模型正在加载数据并开始 tokenization。

总结：
1. `train_config_scierc_4b.yaml` 已创建，LoRA 配置与 CoNLL 4B 完全一致（rank=32, alpha=64, lr=2e-4, 5 epochs, enable_thinking=false）
2. dataset_info.json 已有 `scierc_uie_train` / `scierc_uie_dev` 条目，无需修改
3. 训练已通过 `submit_training_job` 提交到 cuda:3，tmux session `exp_qwen3_4b_scierc_finetune`
4. Registry 已更新为 RUNNING
5. 日志确认模型加载和数据 tokenization 正常进行中

---
