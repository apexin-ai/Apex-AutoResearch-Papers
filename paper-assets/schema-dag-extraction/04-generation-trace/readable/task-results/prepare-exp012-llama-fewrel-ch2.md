# prepare exp012 llama fewrel ch2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prepare_exp012_llama_fewrel_ch2_20260515T211826_result.json`
- **Structured JSON:** [`c0dbf30b3a71434711d7.json`](../../sessions/c0/c0dbf30b3a71434711d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部就绪。总结：

## 完成情况

### 脚本路径
`/root/schema-dag-extraction/scripts/run_llama_fewrel_ch2.sh`

### 代码修改（`src/run_fewrel_formal.py`）
两处关键改动，不影响 Qwen3 现有逻辑：
1. **Chat template 支持** — `run_re_extraction()` 中检测模型名，LLaMA/Mistral/Gemma/Phi 自动包装 `tokenizer.apply_chat_template()`（L92-96, L132-141）
2. **`gpu_memory_utilization` 参数化** — 新增 CLI arg `--gpu_memory_utilization`，从硬编码 0.95 改为可配置，通过 preprocess config 传递到 extract 阶段（L81, L90, L272, L327, L367）

### 启动命令
```bash
nohup bash /root/schema-dag-extraction/scripts/run_llama_fewrel_ch2.sh > /root/schema-dag-extraction/artifacts/llama_fewrel_ch2/run.log 2>&1 &
```

### 预计运行时间
- exp2: 54 batches（count 8 × 27 + count 16 × 27），约 7.8k inferences
- LLaMA-8B + vLLM @ 0.80 GPU util：~55-65 min

### 潜在风险
1. **Chat template + structured output 兼容性** — vLLM 的 constrained JSON decoding 需要和 chat template tokens 兼容。NER 上已验证可行，RE 应无问题
2. **Floor effect** — LLaMA-8B 在 80-rel RE 上如果 accuracy < 20%，BCS effect 可能被地板效应掩盖。但 RE 用 accuracy metric（非 span F1），且 Qwen3 在 80-rel 有 -31.2pp 的巨大效应，即使 LLaMA 只有 ~10pp gap 也有价值
3. **Batch 一致性** — 使用相同 seed=42 + 相同 80 relations + MiniLM embeddings（模型无关），batch 配置与 Qwen3 完全一致，可直接对比

---
