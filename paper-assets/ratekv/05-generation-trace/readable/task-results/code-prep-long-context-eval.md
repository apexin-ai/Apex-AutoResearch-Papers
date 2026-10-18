# code prep long context eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_long_context_eval_20260516T023901_result.json`
- **Structured JSON:** [`e1927a6501f306b240b1.json`](../../sessions/e1/e1927a6501f306b240b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本已写好：

- **`run_llama_8k_eval.py`** — Llama-3.1-8B, Spike 分布, 模型路径 `/root/autodl-tmp/models/LLM-Research/Meta-Llama-3.1-8B`, 输出 `artifacts/llama_8k_eval_results.json`
- **`run_mistral_8k_eval.py`** — Mistral-7B-v0.3, Flat 分布, 模型路径 `/root/autodl-tmp/models/Mistral-7B-v0.3`, 输出 `artifacts/mistral_8k_eval_results.json`

两个脚本共同特点：
- 支持 `--gpu N` 参数（默认 0）
- 使用 merged profiles（hires 2-bit + standard 4/8-bit）
- 评估三个条件：BF16 baseline / constrained MCKP (k=2) / uniform 4-bit，stride=8192
- 包含 concentration 分析和 2K reference 数据
- 输出格式与现有 Qwen 8K spotcheck 一致

---
