# code prep seed46 and reeval commands

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-seed46-and-reeval-commands_20260515T220754_result.json`
- **Structured JSON:** [`e152f8bbd35bbacd7cae.json`](../../sessions/e1/e152f8bbd35bbacd7cae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕，汇总结果：

### 1. seed46 准备状态：✅ 可以提交
- 输出目录 `/root/autodl-tmp/rsft_output_flat_nli_s46` **不存在**，无冲突
- 训练数据 `rsft_train.jsonl` 存在，**2691 行**
- 磁盘空间：250G 总量，已用 184G，**剩余 67G (26%)**，足够一次训练（adapter ~500MB + checkpoints）

训练命令已准备好，确认无误可直接执行。

### 2. reeval_flat_nli_s43 checkpoint：✅ 存在
- `/root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507/adapter_model.safetensors` — 504MB，时间戳 May 16 03:56

### 3. reeval_rsft_topk3 checkpoint：✅ 存在
- `/root/autodl-tmp/rsft_topk3_output/adapter_model.safetensors` — 504MB，时间戳 May 16 05:05

### 4. 问题
无。三项检查全部通过。提交 reeval 前记得按 C001 约束先 `nvidia-smi` 确认目标 GPU 显存占用 < 2GB。

---
