# ops model download westd

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_model-download-westd_20260513T062348_result.json`
- **Structured JSON:** [`2646bdf529d320f730e1.json`](../../sessions/26/2646bdf529d320f730e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both models downloaded and verified. Summary:

---

### GPT-2 Small
- **Path**: `/root/autodl-tmp/.hf_cache/openai-community/gpt2/`
- **Size**: 1.1GB (包含 pytorch_model.bin + model.safetensors 各 523MB)
- **TransformerLens 验证**: 加载至 CUDA 成功
  - Layers: 12, Heads: 12, d_model: 768
  - Vocab: 50257
  - GPU 显存占用: 635.5 MB
- **加载方式**: 需要用本地路径加载 HF model 后传入 TransformerLens（直接 `from_pretrained('gpt2-small')` 会尝试从 HF 下载，在 AutoDL 环境下容易失败）
  ```python
  hf_model = AutoModelForCausalLM.from_pretrained('/root/autodl-tmp/.hf_cache/openai-community/gpt2')
  tokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/.hf_cache/openai-community/gpt2')
  model = HookedTransformer.from_pretrained('gpt2-small', hf_model=hf_model, tokenizer=tokenizer, device='cuda')
  ```

### Qwen-2.5 0.5B
- **Path**: `/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B/`
- **Size**: 1.4GB (model.safetensors 942MB)
- **Tokenizer 验证**: Qwen2TokenizerFast, vocab_size = 151643

---
