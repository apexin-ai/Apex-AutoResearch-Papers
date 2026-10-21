# run llama math gpu1 immediate

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_llama_math_gpu1_immediate_20260521T124317_result.json`
- **Structured JSON:** [`c5fe5f8f4e062243ba9c.json`](../../sessions/c5/c5fe5f8f4e062243ba9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。汇总：

**Llama MATH 推理**
- **PID**: 162258
- **GPU 1**: 88GB 显存占用，69% 利用率
- **进度**: 第一个 condition (4897) 正在处理 200 math items，速度 ~2100 toks/s input
- **输出**: `results/exp002/llama_math.jsonl`
- **日志**: `/tmp/math_llama.log`

**4 个 MATH shard 文件**（均 289 行 = 1 header + 288 conditions）

| Shard 文件 | 模型 | Condition ID 范围 |
|---|---|---|
| `shard_qwen_math.csv` | Qwen3-8B | 4609–4896 |
| `shard_llama_math.csv` | Llama-3.1-8B-Instruct | 4897–5184 |
| `shard_gemma_math.csv` | gemma-2-9b-it | 5185–5472 |
| `shard_mistral_math.csv` | Mistral-7B-Instruct-v0.3 | 5473–5760 |

Condition ID 从 4609 起编，避免与现有 4-benchmark 结果（1–4608）冲突。其他 3 个模型 GSM8K 一结束即可用对应 shard 启动 MATH。

---
