# code prep yi gemma multiseed

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_yi_gemma_multiseed_20260516T053010_result.json`
- **Structured JSON:** [`9e1208f76c8584f98682.json`](../../sessions/9e/9e1208f76c8584f98682.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks complete. Here's the report:

---

## 就绪性报告

### Yi-1.5-9B: **就绪 ✓**

| 项目 | 状态 |
|------|------|
| 脚本支持 | `--model yi` 已配置 |
| 模型路径 | `/root/autodl-tmp/.hf_cache/01ai/Yi-1___5-9B` |
| 模型文件 | config.json + 4 safetensors shards ✓ |
| Tokenizer | tokenizer_config.json 存在 ✓ |
| 架构 | LlamaForCausalLM（标准 patch_attention 兼容）|
| GQA | 32 attention heads / 4 KV heads = **GQA ratio 8:1**，48 layers |
| BOS 问题 | 不适用（`gemma2: False`，走标准 eval_ppl 路径）|
| max_2bit | 2 |

### Gemma-2-9B: **就绪 ✓**

| 项目 | 状态 |
|------|------|
| 脚本支持 | `--model gemma2` 已配置 |
| 模型路径 | `/root/autodl-tmp/.hf_cache/google/gemma-2-9b` |
| 模型文件 | config.json + 8 safetensors shards ✓ |
| 架构 | Gemma2ForCausalLM |
| GQA | 16 attention heads / 8 KV heads = **GQA ratio 2:1**，42 layers |
| BOS fix | **已处理** — `evaluate_perplexity_gemma2()` 内置 BOS prepend 逻辑（L189-213），每个 chunk 检测首 token 是否为 BOS，缺则 prepend |
| Gemma2 专用 patch | 使用 `patch_attention_gemma2`（从 `run_gemma2_full_pipeline.py` 导入），处理 sliding window attention |
| max_2bit | 8（允许更多 2-bit heads，适应 Gemma-2 的 head 敏感度分布）|

### 推荐命令

```bash
# Yi-1.5-9B
python run_multi_seed_ppl.py --model yi --gpu 0 --batch-size 4

# Gemma-2-9B
python run_multi_seed_ppl.py --model gemma2 --gpu 0 --batch-size 4
```

### 预估运行时间

| 模型 | KV heads × Layers | 总 profiling 点 | 预估时间（3 seeds） |
|------|--------------------|-----------------|---------------------|
| Yi-1.5-9B | 4 × 48 = 192 heads | 192 × 3 bits × 3 seeds | ~3.5-4.5h |
| Gemma-2-9B | 8 × 42 = 336 heads | 336 × 3 bits × 3 seeds | ~5-7h |

Yi 的 KV head 数少（4），profiling 快于 Gemma-2（8 KV heads）。两者都建议 `--batch-size 4`（9B 模型 + profiling overhead，防 OOM）。如果 GPU 是 80GB A100 可以试 `--batch-size 8`。

---
