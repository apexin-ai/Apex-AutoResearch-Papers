# fix n2 roberta finetune 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_n2_roberta_finetune_001_20260515T122400_result.json`
- **Structured JSON:** [`72b6ca59bcace1709ff2.json`](../../sessions/72/72b6ca59bcace1709ff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中，loss 在下降 (1.4434 → 1.3990)。

**诊断总结：**
- **失败原因**：模型文件 `model.safetensors` 损坏（上一个 Worker 用 ModelScope 下载时截断），safetensors 反序列化失败
- **修复**：从 hf-mirror.com 用 aria2c 重新下载 `pytorch_model.bin`（safetensors 版本有 xet storage 兼容性问题，data_offsets 与实际文件大小不匹配）
- **脚本代码无需修改**：`n2_deberta_finetune.py` 使用 Auto 类，兼容 RoBERTa
- **已重新提交**：`n2_roberta_finetune_001`，GPU cuda:1，训练已正常进行

---
