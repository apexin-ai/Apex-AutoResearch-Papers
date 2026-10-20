# code download 72b server b

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_download_72b_server_b_20260519T064000_result.json`
- **Structured JSON:** [`70dba193dc06ee1da8cd.json`](../../sessions/70/70dba193dc06ee1da8cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 显存已完全释放 (4x 2MiB/32607MiB)。

---

## 最终汇报

### 1. 模型下载状态和路径
- **状态**: 完成 (21/21 files, 33 分钟)
- **路径**: `/root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-72B-Instruct-AWQ/snapshots/698703eae6604af048a3d2f509995dc302088217`
- **大小**: 40GB on disk (AWQ 4-bit, 11 safetensor shards)

### 2. 磁盘使用
- `/root/autodl-tmp`: 350GB total, 105GB used (30%), 246GB available
- `.hf_cache` 目录: 56GB（含之前已有模型）

### 3. Prompt 模板内容 (`code/zeroshot_prompts.py`)

| Dataset | Entity Types |
|---------|-------------|
| CoNLL2003 | PER, ORG, LOC, MISC |
| FewNERD | person, organization, location, building, art, product, event, other |
| SciERC | Generic, Material, Method, Metric, OtherScientificTerm, Task |

- 输出格式: `{"entities": [{"text": "...", "type": "...", "start": &lt;int>, "end": &lt;int>}], "relations": [], "events": []}`
- 两种 prompt 变体: `build_zeroshot_prompt` (类型列表) / `build_zeroshot_prompt_with_descriptions` (含类型定义)
- `format_chat_messages()` 直接生成 vLLM chat completion 格式

### 4. vLLM 加载测试结果
- **Tokenizer**: vocab_size=151643, chat_template 可用 (`<|im_start|>/<|im_end|>`)
- **vLLM 加载**: 成功，配置 `tensor_parallel_size=4, quantization='awq', max_model_len=4096, gpu_memory_utilization=0.85`
- **每 GPU 显存**: model 9.79 GiB + CUDA graph 1.52 GiB ≈ 11.3 GiB / 32 GiB
- **KV cache**: 207,408 tokens, max concurrency 50.64x (4096 tokens/request)
- **测试生成**: 通过，输出正常文本
- **注意**: 需要用本地 snapshot 完整路径加载（`HF_ENDPOINT` 下载时生效，但 vLLM 加载时 huggingface.co 不可达）

### 5. 阻塞问题
- **无阻塞问题**。唯一注意事项：vLLM 加载时需设 `TRANSFORMERS_OFFLINE=1` + `HF_HUB_OFFLINE=1` 并用本地 snapshot 路径，或确保 `HF_ENDPOINT=https://hf-mirror.com` 在运行时也生效。

---
