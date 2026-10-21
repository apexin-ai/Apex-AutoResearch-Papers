# ops check docred constrained eval status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_docred_constrained_eval_status_20260516T020953_result.json`
- **Structured JSON:** [`3142d129512b949ce798.json`](../../sessions/31/3142d129512b949ce798.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. w5_llama_docred_lora_constrained_eval
- **进程状态**: 运行中 (PID 317464/317469, ELAPSED 01:43:05, STAT=Rl)
- **GPU 占用**: cuda:0, 16816 MiB
- **进度**: **407/998** 行 (~40.8%)
- **输出文件**: `/root/schema_semantic_constrained_ie/outputs/w5_llama_docred_lora_constrained_eval.jsonl`
- **日志**: 正常，持续输出 `pad_token_id` 设置提示（无错误）
- **预估剩余**: 已跑 ~103 分钟处理 407 条，平均 ~15.2s/条，剩余 591 条约 **150 分钟（~2.5 小时）**

### 2. w5_qwen_docred_lora_constrained_eval
- **进程状态**: 运行中 (PID 321568, ELAPSED 15:18, STAT=Rl)
- **GPU 占用**: cuda:1, 17256 MiB
- **进度**: **47/998** 行 (~4.7%)
- **输出文件**: `/root/schema_semantic_constrained_ie/outputs/w5_qwen_docred_lora_constrained_eval.jsonl`
- **日志**: 模型加载完成，正在推理（有 Mistral tokenizer regex 警告，不影响功能）
- **预估剩余**: 已跑 ~15 分钟处理 47 条，平均 ~19.1s/条，剩余 951 条约 **303 分钟（~5 小时）**

两个实验均正常运行，无错误。Qwen 启动较晚且单条推理略慢。

---
