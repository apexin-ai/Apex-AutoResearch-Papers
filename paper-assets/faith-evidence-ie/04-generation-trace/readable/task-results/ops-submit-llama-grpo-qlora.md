# ops submit llama grpo qlora

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_llama_grpo_qlora_20260516T130835_result.json`
- **Structured JSON:** [`b7acc70fce65537fb1a6.json`](../../sessions/b7/b7acc70fce65537fb1a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。总结：

**plan_016_llama_grpo_qlora** 已在 cuda:2 上运行（PID 346621）

| 参数 | 值 |
|------|-----|
| base_model | Meta-Llama-3.1-8B |
| sft_adapter | sft_output_llama_3_1_8b (with-evidence) |
| quantize | 4-bit QLoRA |
| stage | 3 (CED reward) |
| num_generations | 4 |
| lora_rank | 64 |
| kl_coef | 0 |
| total_steps | 757 |
| GPU mem | 8039 MiB |

**修复的问题**：
1. base LLaMA-3.1-8B 的 tokenizer 没有 `chat_template` → 改为从 SFT adapter 目录加载 tokenizer
2. NLI 模型（DeBERTa）网络不通 → 传本地缓存路径 + `TRANSFORMERS_OFFLINE=1`

日志：`/root/autodl-tmp/grpo_output_llama_3_1_8b_qlora.log`

---
