# code model download dryrun

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_model_download_dryrun_20260512T200536_result.json`
- **Structured JSON:** [`d98ba4975d058cf18a17.json`](../../sessions/d9/d98ba4975d058cf18a17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 模型缓存路径
| 模型 | 路径 |
|------|------|
| Pythia-1.4B | `/root/autodl-tmp/.hf_cache/EleutherAI/pythia-1.4b` |
| OLMo-1B-hf | `/root/autodl-tmp/.hf_cache/allenai/OLMo-1B-hf` |

### 2. 模型 & Tokenizer 信息

| | Pythia-1.4B | OLMo-1B-hf |
|---|---|---|
| 架构 | GPTNeoXForCausalLM | OlmoForCausalLM |
| 参数量 | ~1.4B (24 layers, hidden=2048) | ~1.2B (16 layers, hidden=2048, tie_word_embeddings) |
| vocab_size | 50304 | 50304 |
| tokenizer_class | GPTNeoXTokenizer | GPTNeoXTokenizer |
| eos_token | `<\|endoftext\|>` | `<\|endoftext\|>` (id=50279) |
| pad_token | 无原生 → pipeline fallback 到 eos_token | `<\|padding\|>` (id=1) |

### 3. Dry-run 结果（10 docs, depth 0-2）
两个模型均通过，无报错。

| | Pythia-1.4B | OLMo-1B-hf |
|---|---|---|
| AUC(0v1) | 0.50 | 0.50 |
| AUC(1v2) | 0.50 | 0.50 |
| JSD(0v1) | 0.813 | 0.716 |
| JSD(1v2) | 0.670 | 0.740 |
| K* | 0 | 0 |
| 总耗时 | ~33s | ~27s |

（AUC=0.5 / feature importance 全零是预期的 — 10 docs 不具统计意义）

### 4. VRAM 使用
两个模型在 4090D (24GB) 上以 fp16 加载，`device_map="auto"` 使用 90% 预留策略。实际模型占用：
- Pythia-1.4B fp16: ~2.8GB（safetensors 2.73GB）
- OLMo-1B fp16: ~2.2GB（safetensors 4.38GB fp32 → 加载为 fp16 约 2.2GB）
- 推理含 KV cache 峰值估计 < 5GB，4090D 24GB 完全无压力

### 5. 遇到的问题及解决
- **下载方式**：ModelScope 成功覆盖了 Pythia 和 OLMo（不需要回退 HF 镜像），下载速度 6-25MB/s 波动
- **Pythia pad_token**：原始 tokenizer 无 pad_token，pipeline 中 `tokenizer.pad_token = tokenizer.eos_token` 的 fallback 正常工作
- **OLMo pad_token**：自带 `<|padding|>` (id=1)，无需额外处理
- **无异常错误**：仅有 sklearn 的 feature name warning（不影响结果），`torch_dtype` deprecated warning（cosmetic）

dryrun 临时数据已清理。

---
