# infra verify llama model

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify_llama_model_20260521T150746_result.json`
- **Structured JSON:** [`c9272b0424b1710f5fd8.json`](../../sessions/c9/c9272b0424b1710f5fd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完毕。汇报如下：

---

## 诊断结果

### 1. Llama 模型是否存在
**存在。** 路径 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/`，4个 safetensors 分片（约 15GB），下载时间 2026-05-21 21:48–22:22。

### 2 & 3. Llama verified 数据的 model_used 字段
**`model_used` 字段存在**，值为：
```
/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct
```
所有 1096 行都包含 `model_used` 字段（grep 计数 = 1096 = 总行数）。

字段名用的是 `model_parametric_answer`（不是 `qwen_parametric_answer`）。

### 4. 前 5 条 parametric answer 内容

| # | Question | model_parametric_answer |
|---|----------|------------------------|
| 1 | Who was the composer of So What? | Miles Davis. |
| 2 | What is the capital of New Zealand? | Wellington. |
| 3 | Who was the director of Training Day? | Antoine Fuqua |
| 4 | What is Jackson the capital of? | Mississippi |
| 5 | In what city was Oleg Govorun born? | Kiev. |

这些答案是**事实正确的**（Miles Davis、Wellington、Antoine Fuqua、Mississippi、Kiev），符合 Llama-3.1-8B-Instruct 的 parametric knowledge，不像是 Qwen 输出（Qwen 的回答风格通常更长、更正式）。

### 5. Qwen base verify 对比
**`data/en_conflict_train_verified.jsonl` 不存在**（Qwen base verify 尚未完成），无法对比。`data/` 目录下只有原始数据文件和 `llama31/`、`original_500/` 子目录。

### Llama verify 文件清单
- `data/llama31/en_conflict_train_verified.jsonl` — 1096 行，1.1MB，生成时间 22:54
- `data/llama31/en_conflict_test_verified.jsonl` — 存在，287KB，生成时间 22:55

---
