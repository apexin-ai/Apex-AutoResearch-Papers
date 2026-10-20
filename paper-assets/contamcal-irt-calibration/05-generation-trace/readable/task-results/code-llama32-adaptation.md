# code llama32 adaptation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama32_adaptation_20260516T073038_result.json`
- **Structured JSON:** [`1e40eaad47ae27020079.json`](../../sessions/1e/1e40eaad47ae27020079.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 完成总结

### 模型下载
- **路径**: `/root/autodl-tmp/models/LLM-Research/Llama-3___2-3B/`
- **大小**: ~6 GB (2 个 safetensors shards)
- **参数**: 3.21B, LlamaForCausalLM, 28 layers, vocab 128K

### 修改的文件

| 文件 | 改动 |
|------|------|
| `exp001/train_sft.py` | 1) 新增 `LLAMA3_CHAT_TEMPLATE` 常量&lt;br>2) `formatting_func` → `make_formatting_func(tokenizer)` (用 `apply_chat_template` 替代硬编码 Qwen 模板)&lt;br>3) tokenizer 加载后自动检测设置 chat template |
| `exp001/evaluate.py` | 1) 新增 `LLAMA3_CHAT_TEMPLATE` 常量&lt;br>2) `load_model_and_tokenizer` 中加入 chat template 自动设置 + pad_token fallback |

### 不需要修改
- `exp002/compute_signals.py` — orchestrator
- `exp002/signal_minkpp.py` — forward pass only
- `exp002/signal_embedding.py` — frozen sentence-transformer encoder
- `exp002/signal_selfcritique.py` — plain text prompts + YES/NO logprob
- SFT 数据 — 标准 messages 格式
- LoRA target modules — Llama 3.2 和 Qwen 2.5 命名一致

### Dry-run 结果
- 模型加载 ✓
- Tokenizer + chat template ✓
- `make_formatting_func` 对 Llama 和 Qwen 都正确 ✓
- LoRA targets (q/k/v/o_proj + gate/up/down_proj) 全部存在 ✓
- Tokenization 正常 (252 tokens for sample) ✓

### 无未解决兼容性问题
代码完全向后兼容 Qwen，可以直接用 `--model-name /root/autodl-tmp/models/LLM-Research/Llama-3___2-3B` 启动 Llama SFT 训练。

---
