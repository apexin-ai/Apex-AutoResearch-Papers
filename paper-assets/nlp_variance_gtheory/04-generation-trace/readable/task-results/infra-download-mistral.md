# infra download mistral

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_download_mistral_20260521T005229_result.json`
- **Structured JSON:** [`c8b6b3908fe2469212d1.json`](../../sessions/c8/c8b6b3908fe2469212d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Mistral-7B-Instruct-v0.3 下载已完成，无需恢复。

```
Mistral-7B-Instruct-v0.3: 完成 (14GB, /root/autodl-tmp/.hf_cache/LLM-Research/Mistral-7B-Instruct-v0___3/, 3个safetensors文件)
```

文件清单：
- 3 个 safetensors (4.7G + 4.7G + 4.3G)
- config.json, tokenizer.json, tokenizer.model 等全部就绪
- 0 个 .incomplete 文件

注意：路径是 ModelScope 格式 (`LLM-Research/Mistral-7B-Instruct-v0___3`)，不是 HuggingFace 格式 (`mistralai/Mistral-7B-Instruct-v0.3`)。项目代码加载模型时需用实际路径。

---
