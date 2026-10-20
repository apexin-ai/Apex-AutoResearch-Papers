# ops eval tail2048 v3

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_tail2048_v3_20260518T113943_result.json`
- **Structured JSON:** [`7f8a48e1250e389c0d52.json`](../../sessions/7f/7f8a48e1250e389c0d52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Epoch 3 eval 正在 GPU 1 上运行（PID 430637，1190 samples）。2 分钟后回来检查结果。

**进展总结：**
- Checkpoint 目录正常：checkpoint-148 / checkpoint-296 / checkpoint-444 / final
- eval_loss=nan 原因：label_only_loss 训练模式下，HF Trainer 内置 eval 计算 loss 时 label masking 导致无有效 token，这是正常的，不影响生成式评估
- eval 脚本需要额外参数：`--model_path /root/autodl-tmp/models/CodeLlama-13b-Instruct-hf`（默认加载 Qwen-7B 会尺寸不匹配）和 `--truncation_side left`（tail 模型需要保留尾部）
- Epoch 3 eval 已在运行，完成后继续 epoch 1

---
