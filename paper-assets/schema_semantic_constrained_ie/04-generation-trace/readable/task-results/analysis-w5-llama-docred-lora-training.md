# analysis w5 llama docred lora training

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_llama_docred_lora_training_20260515T195603_result.json`
- **Structured JSON:** [`d76f8ee14a3cbb1fc407.json`](../../sessions/d7/d76f8ee14a3cbb1fc407.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练成功完成。核心结论：

**Metrics**: train_loss=0.0572, eval_loss=0.0624, eval_token_acc=**98.06%**, 训练耗时 **89.3 分钟** (573 steps)

**关键发现**: eval_loss 在 **epoch 2 最优** (0.0596)，epoch 3 回升至 0.0624，轻微过拟合。推荐推理评测时同时测 **checkpoint-382** (epoch 2) 和最终 checkpoint。

**与 SciERC 对比**: 训练时间 8.2× (654s→5357s)，token_acc 略低 0.11pp (98.17%→98.06%)，均在合理范围。

**Checkpoints 完整**: adapter 1.2GB + merged model 15GB，磁盘余量充足 (根分区 46%, 数据盘 42%)。

报告已注册: `art_20260515_cfa2be`

---
