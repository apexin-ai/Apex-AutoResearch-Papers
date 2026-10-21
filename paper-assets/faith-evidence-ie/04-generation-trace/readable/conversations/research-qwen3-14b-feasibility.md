# research qwen3 14b feasibility

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_research_qwen3_14b_feasibility_20260518T100058.jsonl`
- **Structured JSON:** [`e4edf075cba8be2388c3.json`](../../sessions/e4/e4edf075cba8be2388c3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-18T10:03:51.894471+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T10:03:51.894844+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T10:03:51.895012+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B HuggingFace model parameters hidden_size layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B HuggingFace model parameters hidden_size layers"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T10:03:51.895148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B safetensors file size VRAM LoRA training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B safetensors file size VRAM LoRA training"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T10:03:51.895351+00:00_

Web search results for query: "Qwen3-14B HuggingFace model parameters hidden_size layers"

Links: [{"title":"Qwen3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/qwen3"},{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen3","url":"https://huggingface.co/docs/transformers/v4.53.0/model_doc/qwen3"},{"title":"nvidia/Qwen3-14B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4"},{"title":"Qwen3-VL","url":"https://huggingface.co/docs/transformers/main/en/model_doc/qwen3_vl"},{"title":"Qwen3-VL · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/qwen3_vl"},{"title":"Qwen/Qwen3.5-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-4B"},{"title":"transformers/src/transformers/models/qwen3/configuration_qwen3.py at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/src/transformers/models/qwen3/configuration_qwen3.py"},{"title":"Qwen3-VL-Moe","url":"https://huggingface.co/docs/transformers/main/model_doc/qwen3_vl_moe"},{"title":"Qwen3.5 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/qwen3_5"}]

Based on the search results, here's what I found regarding the Qwen3-14B model parameters:

## Qwen3-14B Model Parameters

**Number of Layers:**
Qwen3-14B has 40 layers.

**Hidden Size:**
The search results show default configuration parameters for Qwen3 models. The default hidden_size is 4096 for the standard Qwen3 configuration. However, this appears to be a base configuration value, and the actual hidden_size for the Qwen3-14B model specifically would need to be confirmed from the model's config.json file on the HuggingFace Hub.

**Other Key Parameters:**
Qwen3-14B has 40 attention heads for Q and 8 for KV, and a context length of 32,768 tokens natively and 131,072 tokens with YaRN.

For the exact hidden_size value specific to the Qwen3-14B model, you can check the model's co
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T10:03:51.895567+00:00_

Web search results for query: "Qwen3-14B safetensors file size VRAM LoRA training"

Links: [{"title":"Qwen3.5 Fine-tuning Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.5/fine-tune"},{"title":"Qwen3 - How to Run & Fine-tune | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3-how-to-run-and-fine-tune"},{"title":"Will This LLM Fit My GPU? VRAM Requirements for Every Model Size — ai.rs","url":"https://ai.rs/ai-developer/will-llm-fit-my-gpu-vram-requirements"},{"title":"Fine-Tuning Qwen/Qwen3-VL-30B-A3B MoE Architecture with LoRA | by Shaaf Salman | Medium","url":"https://medium.com/@ishaafsalman/fine-tuning-qwen-qwen3-vl-30b-a3b-moe-architecture-with-lora-2365359e870f"},{"title":"Fine-Tuning Qwen3-VL 8B: A Step-by-Step Guide | DataCamp","url":"https://www.datacamp.com/tutorial/fine-tuning-qwen3-vl-8b"},{"title":"Qwen3-14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-14b"},{"title":"How to Fine-Tune Qwen3.5 0.8B Locally?","url":"https://sonusahani.com/blogs/fine-tune-qwen3-5-8b-locally"},{"title":"GPU System Requirement Guide for Qwen 3.5","url":"https://apxml.com/posts/qwen-3-5-system-requirement-vram-guide"},{"title":"Running Qwen3.6 Locally: VRAM Requirements for 27B and 35B-A3B Quantized Models","url":"https://www.knightli.com/en/2026/05/01/qwen3-6-local-vram-quantization-table/"},{"title":"Qwen3.5 9B, 4B, 2B & 0.8B: GPU Requirements, VRAM Usage & KV Cache Breakdown (262K Context)","url":"https://kaitchup.substack.com/p/qwen35-9b-4b-2b-and-08b-gpu-requirements"}]

Based on the search results, here's information about Qwen3-14B safetensors file size, VRAM requirements, and LoRA training:

## Safetensors File Size
Qwen3-14B has 14.8 billion total parameters. While a specific safetensors file size wasn't explicitly mentioned in the results, you can estimate it using standard calculations: BF16 (16-bit) precision typically requires approximately 28-30GB for a 14B model.

## VRAM Requirement
…[truncated 952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T10:03:51.895793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B config.json hidden_size vocab_size num_hidden_layers intermediate_size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B config.json hidden_size vocab_size num_hidden_layers intermediate_size"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T10:03:51.895960+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B QLoRA 4-bit training VRAM 32GB GPU batch_size gradient checkpointing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B QLoRA 4-bit training VRAM 32GB GPU batch_size gradient checkpointing"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T10:03:51.896116+00:00_

Web search results for query: "Qwen3-14B config.json hidden_size vocab_size num_hidden_layers intermediate_size"

Links: [{"title":"config.json · Qwen/Qwen3-4B at main","url":"https://huggingface.co/Qwen/Qwen3-4B/blob/main/config.json"},{"title":"Qwen3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/qwen3"},{"title":"config.json · TIGER-Lab/General-Reasoner-Qwen3-14B at main","url":"https://huggingface.co/TIGER-Lab/General-Reasoner-Qwen3-14B/blob/main/config.json"},{"title":"config.json · nvidia/Qwen3-14B-NVFP4 at main","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-32B at main","url":"https://huggingface.co/Qwen/Qwen3-32B/blob/main/config.json"},{"title":"Qwen/Qwen2.5-VL-3B-Instruct · Update config.json","url":"https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct/discussions/39/files"},{"title":"config.json · Qwen/Qwen3-8B at main","url":"https://huggingface.co/Qwen/Qwen3-8B/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-14B at 7d3da9c56f02b22d31dc1ca97c7ee628d1e2e237","url":"https://huggingface.co/Qwen/Qwen3-14B/blame/7d3da9c56f02b22d31dc1ca97c7ee628d1e2e237/config.json"},{"title":"config.json · Qwen/Qwen3-4B-Instruct-2507 at main","url":"https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json"},{"title":"qwen3_next - vLLM","url":"https://docs.vllm.ai/en/v0.10.2/api/vllm/transformers_utils/configs/qwen3_next.html"}]

Based on the search results, I found documentation for the Qwen3 model configuration. The hidden_size defaults to 4096, vocab_size defaults to 151936, num_hidden_layers defaults to 32, and intermediate_size defaults to 22016 for Qwen3 models according to the Hugging Face documentation.

However, the search results show documentation for the general Qwen3 model architecture rather than the specific configuration values for the Qwen3-14B model. The actual config.json files from Hugging Face (such as the one for Qwen/Qwen3-14B) did not
…[truncated 411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T10:03:51.896344+00:00_

Web search results for query: "Qwen3-14B QLoRA 4-bit training VRAM 32GB GPU batch_size gradient checkpointing"

Links: [{"title":"Qwen3-14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-14b"},{"title":"Qwen3.5 Fine-tuning Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.5/fine-tune"},{"title":"QLoRA Explained - How 4 Bit Quantization Unlocks Frontier Models","url":"https://theneuralmaze.substack.com/p/qlora-explained-how-4-bit-quantization"},{"title":"Qwen 3 GPU Requirements — Original Family (0.6B–235B) VRAM Guide (2026) | Will It Run AI Blog","url":"https://willitrunai.com/blog/qwen-3-gpu-requirements"},{"title":"Qwen3 - How to Run & Fine-tune | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3-how-to-run-and-fine-tune"},{"title":"Deploy Qwen 3 on GPU Cloud: Hardware Requirements and Setup Guide | Spheron Blog","url":"https://www.spheron.network/blog/deploy-qwen3-gpu-cloud/"},{"title":"VRAM Calculator for AI & ML | GPU Memory Sizing | Skorppio","url":"https://skorppio.com/tools/vram-calculator-for-ai-ml"},{"title":"How to Run Qwen3 Locally - A Practical Guide for AI Enthusiasts","url":"https://onedollarvps.com/blogs/how-to-run-qwen3-locally"},{"title":"QLoRA Fine-Tuning with Unsloth: A Complete Guide","url":"https://medium.com/@matteo28/qlora-fine-tuning-with-unsloth-a-complete-guide-8652c9c7edb3"},{"title":"GPU System Requirement Guide for Qwen 3.5","url":"https://apxml.com/posts/qwen-3-5-system-requirement-vram-guide"}]

I've found search results related to your query about Qwen3-14B QLoRA training with a 32GB GPU. Here are the key findings:

## QLoRA Training Considerations

It is not recommended to do QLoRA (4-bit) training on the Qwen3.5 models, no matter MoE or dense, due to higher than normal quantization differences. However, information specific to Qwen3 (not 3.5) dense models like the 14B appears more feasible.

## Gradient Checkpointing for VRAM Optimization

Gradient checkpoi
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T10:03:51.896512+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:huggingface.co \"Qwen/Qwen3-14B\" config.json hidden_size 5120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:huggingface.co \"Qwen/Qwen3-14B\" config.json hidden_size 5120"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T10:03:51.896640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B architecture hidden_size 5120 num_attention_heads 40 layers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B architecture hidden_size 5120 num_attention_heads 40 layers"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T10:03:51.896836+00:00_

Web search results for query: "Qwen3-14B architecture hidden_size 5120 num_attention_heads 40 layers"

Links: [{"title":"Qwen3 14B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-14b/"},{"title":"unknown model architecture: 'qwen3' · Issue #10454 · ollama/ollama","url":"https://github.com/ollama/ollama/issues/10454"},{"title":"Qwen3-14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-14b"},{"title":"Qwen3.6–35B-A3B: The Tiny-Active Open Model That Thinks, Codes, and Agents Like a Much Bigger One | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Apr, 2026 | Medium","url":"https://medium.com/data-science-in-your-pocket/qwen3-6-35b-a3b-the-tiny-active-open-model-that-thinks-codes-and-agents-like-a-much-bigger-one-486d535e372e"},{"title":"Qwen3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/qwen3"},{"title":"Unpacking Qwen 3: Architecture, Capabilities, and Performance | by Erik Milošević | Towards AGI | Medium","url":"https://medium.com/towards-agi/unpacking-qwen-3-architecture-capabilities-and-performance-a87f6b317f72"},{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen/Qwen3-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-4B"},{"title":"Qwen/Qwen3.5-4B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-4B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"}]

Based on the search results, I found detailed information about the Qwen3-14B architecture parameters you asked about.

Qwen3-14B has a hidden_size (embedding_length) of 5120, with 40 attention heads and 40 layers (block_count). More specifically, the model uses grouped query attention (GQA), with 40 heads for queries and 8 for keys/values.

Additional architectural details include:
- The total parameter count reaches approximately 14.8 billion, of which 13.2 billion are non-embedding parameters
- The model f
…[truncated 266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T10:03:51.897029+00:00_

Web search results for query: "site:huggingface.co "Qwen/Qwen3-14B" config.json hidden_size 5120"

Links: [{"title":"config.json · TIGER-Lab/General-Reasoner-Qwen3-14B at main","url":"https://huggingface.co/TIGER-Lab/General-Reasoner-Qwen3-14B/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-4B at main","url":"https://huggingface.co/Qwen/Qwen3-4B/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-14B at d17b97ca036704c156b50686b3f4551e224bbe03","url":"https://huggingface.co/Qwen/Qwen3-14B/blob/d17b97ca036704c156b50686b3f4551e224bbe03/config.json"},{"title":"config.json · nvidia/Qwen3-14B-NVFP4 at main","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-14B at 7d3da9c56f02b22d31dc1ca97c7ee628d1e2e237","url":"https://huggingface.co/Qwen/Qwen3-14B/blame/7d3da9c56f02b22d31dc1ca97c7ee628d1e2e237/config.json"},{"title":"config.json · dnotitia/Smoothie-Qwen3-14B at main","url":"https://huggingface.co/dnotitia/Smoothie-Qwen3-14B/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-14B-MLX-4bit at be2785af0328eca1c896d8445c97b4a2a69c2457","url":"https://huggingface.co/Qwen/Qwen3-14B-MLX-4bit/blob/be2785af0328eca1c896d8445c97b4a2a69c2457/config.json"},{"title":"config.json · aifeifei798/QiMing-Pantheon-Qwen3-14B at ce81e4d6216cc952149847d4636464a0a9bf195a","url":"https://huggingface.co/aifeifei798/QiMing-Pantheon-Qwen3-14B/blame/ce81e4d6216cc952149847d4636464a0a9bf195a/config.json"},{"title":"config.json · Qwen/Qwen3-4B-Instruct-2507 at main","url":"https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507/blob/main/config.json"},{"title":"config.json · Qwen/Qwen3-14B-MLX-bf16 at 56195040ec43ec47daf0b013d351784dc56504cf","url":"https://huggingface.co/Qwen/Qwen3-14B-MLX-bf16/blame/56195040ec43ec47daf0b013d351784dc56504cf/config.json"}]

The search results show multiple Hugging Face links related to Qwen3-14B config.json files. I found several relevant sources, including:

1. **Direct match**: https:/
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T10:03:51.897193+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Qwen/Qwen3-14B\" safetensors total size GB huggingface files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Qwen/Qwen3-14B\" safetensors total size GB huggingface files"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T10:03:51.897340+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B bf16 LoRA fine-tuning VRAM usage single GPU 32GB RTX benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B bf16 LoRA fine-tuning VRAM usage single GPU 32GB RTX benchmark"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T10:03:51.897503+00:00_

Web search results for query: "Qwen3-14B bf16 LoRA fine-tuning VRAM usage single GPU 32GB RTX benchmark"

Links: [{"title":"Qwen3-Coder-Next: How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3-coder-next"},{"title":"Speed Benchmark - Qwen","url":"https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html"},{"title":"Medina 14B: Multi-GPU LoRA Hot-Swap Inference Benchmark · GitHub","url":"https://gist.github.com/synchronic1/22ad2e229fe760f0ccd5313f53adea59"},{"title":"GPU Requirements 2026: Llama 4 = 1× H100 ($2.50/hr), DeepSeek V3.2 = 8× H200 ($36/hr), Qwen 3.5 27B = 1× H100 | Spheron Blog","url":"https://www.spheron.network/blog/gpu-requirements-cheat-sheet-2026/"},{"title":"Running Qwen3.6 Locally: VRAM Requirements for 27B and 35B-A3B Quantized Models","url":"https://www.knightli.com/en/2026/05/01/qwen3-6-local-vram-quantization-table/"},{"title":"Qwen 3 GPU Requirements — Original Family (0.6B–235B) VRAM Guide (2026) | Will It Run AI Blog","url":"https://willitrunai.com/blog/qwen-3-gpu-requirements"},{"title":"Qwen3 Coder: Fine Tune Qwen3 with LoRA | A Step-by-Step Guide","url":"https://qwen3lm.com/fine-tune-qwen3-with-lora/"},{"title":"Qwen3.5 9B, 4B, 2B & 0.8B: GPU Requirements, VRAM Usage & KV Cache Breakdown (262K Context)","url":"https://kaitchup.substack.com/p/qwen35-9b-4b-2b-and-08b-gpu-requirements"},{"title":"Evaluating LLM Fine-tuning Efficiency on NVIDIA RTX 6000 Blackwell Max-Q - Fixstars Corporation Tech Blog","url":"https://blog.us.fixstars.com/evaluating-llm-fine-tuning-efficiency-on-nvidia-rtx-6000-blackwell-max-q/"},{"title":"Qwen3.6 - How to Run Locally | Unsloth Documentation","url":"https://unsloth.ai/docs/models/qwen3.6"}]

Based on the search results, I found relevant information about Qwen3-14B fine-tuning, though specific benchmarks for bf16 LoRA on a single 32GB RTX GPU are limited in the results.

Here's what I found:

## General LoRA Fine-tuning Requirements

Qwen3 models support par
…[truncated 1202 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T10:03:51.897785+00:00_

Web search results for query: ""Qwen/Qwen3-14B" safetensors total size GB huggingface files"

Links: [{"title":"Download Qwen-3 Models - MoE, Dense & Quantized Versions","url":"https://qwen-3.com/en/download"},{"title":"model.safetensors · Qwen/Qwen3-4B-Instruct-2507-FP8 at main","url":"https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507-FP8/blob/main/model.safetensors"},{"title":"Qwen/Qwen3.5-4B at main","url":"https://huggingface.co/Qwen/Qwen3.5-4B/tree/main"},{"title":"nvidia/Qwen3-14B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4"},{"title":"model-00003-of-00005.safetensors · Qwen/Qwen3-8B at 895c8d171bc03c30e113cd7a28c02494b5e068b7","url":"https://huggingface.co/Qwen/Qwen3-8B/blob/895c8d171bc03c30e113cd7a28c02494b5e068b7/model-00003-of-00005.safetensors"},{"title":"model.safetensors-00001-of-00002.safetensors · Qwen/Qwen3.5-4B at main","url":"https://huggingface.co/Qwen/Qwen3.5-4B/blob/main/model.safetensors-00001-of-00002.safetensors"},{"title":"model.safetensors · Qwen/Qwen3-4B-MLX-8bit at main","url":"https://huggingface.co/Qwen/Qwen3-4B-MLX-8bit/blob/main/model.safetensors"},{"title":"model.safetensors · Qwen/Qwen3-8B-MLX-4bit at main","url":"https://huggingface.co/Qwen/Qwen3-8B-MLX-4bit/blob/main/model.safetensors"},{"title":"Unsloth Model Catalog | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/unsloth-model-catalog"},{"title":"Qwen/Qwen3-8B at main","url":"https://huggingface.co/Qwen/Qwen3-8B/tree/main"}]

I need to search more specifically for the Qwen3-14B model files:

Links: [{"title":"Qwen/Qwen3-14B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-GGUF"},{"title":"bartowski/Qwen_Qwen3-14B-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/Qwen_Qwen3-14B-GGUF"},{"title":"Qwen/Qwen3-14B-MLX-4bit · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-MLX-4bit"},{"title":"lm-kit/qwen-3-14b-instruct-gguf · Hugging Face","url":"https://huggingface.co/lm-kit/qwen-3-14b-instruct
…[truncated 6344 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T10:03:51.897987+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T10:03:51.898119+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T10:03:51.898254+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*config*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*config*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T10:03:51.898390+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T10:03:51.898507+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*train*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*train*.py",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T10:03:51.898622+00:00_

artifacts/freige/training/sft_trainer.py
artifacts/freige/training/rsft_trainer.py
artifacts/freige/training/grpo_trainer.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T10:03:51.898733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts/freige/training/sft_trainer.py",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-18T10:03:51.898891+00:00_

1	"""SFT 训练脚本: Qwen3-4B + QLoRA 在 DocRED 上微调。
2	
3	支持单卡和多卡（DeepSpeed ZeRO-2/3）训练。
4	默认启用 4-bit QLoRA 量化，适配 RTX 5090 32GB x4。
5	
6	单卡:   python -m freige.training.sft_trainer --output_dir ./sft_output
7	多卡:   accelerate launch --config_file configs/accelerate_4gpu.yaml \
8	            -m freige.training.sft_trainer --deepspeed configs/deepspeed_zero2.json
9	不量化: 加 --no_quantize
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import os
16	from dataclasses import dataclass, field
17	from pathlib import Path
18	from typing import Optional
19	
20	import torch
21	from datasets import Dataset
22	from peft import LoraConfig, TaskType, get_peft_model
23	from transformers import (
24	    AutoModelForCausalLM,
25	    AutoTokenizer,
26	    BitsAndBytesConfig,
27	    TrainingArguments,
28	)
29	from trl import SFTTrainer, SFTConfig
30	
31	from freige.training import LLAMA3_CHAT_TEMPLATE
32	
33	logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
34	logger = logging.getLogger(__name__)
35	
36	SYSTEM_PROMPT = (
37	    "You are an information extraction model. Given a document with numbered sentences "
38	    "and a list of entities, extract all relation triples. For each triple, provide the "
39	    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
40	    "Output as a JSON list."
41	)
42	
43	DEFAULT_MODEL = "/root/autodl-tmp/models/Qwen3-4B"
44	
45	
46	def build_chat_messages(instruction: str, input_text: str, output_text: str = None):
47	    """构建 Qwen3 chat 格式的消息列表。"""
48	    messages = [
49	        {"role": "system", "content": SYSTEM_PROMPT},
50	        {"role": "user", "content": f"{instruction}\n\n{input_text}"},
51	    ]
52	    if output_text is not None:
53	        messages.append({"role": "assistant", "content": output_text})
54	    return messages
55	
56	
57	def prepare_dataset(
58	    data_dir: str = None,
59	    split: str = "train",
60	    tokenizer=None,
61	    max_length: int 
…[truncated 699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-18T10:03:51.899044+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "lora_r|lora_rank|rank|alpha|target_modules|per_device_train_batch|gradient_checkpointing|max_seq_length|model_name",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts",
  "output_mode": "content",
  "glob": "*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Grep",
  "tool_args": {
    "pattern": "lora_r|lora_rank|rank|alpha|target_modules|per_device_train_batch|gradient_checkpointing|max_seq_length|model_name",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/artifacts",
    "output_mode": "content",
    "glob": "*.py"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T10:03:51.899225+00:00_

artifacts/freige/analysis/ced_signal_validation.py:72:    reward_model = CEDRewardModel(model_name=nli_model)
artifacts/freige/analysis/ced_signal_validation.py:245:    axes[0, 0].hist(margins, bins=50, edgecolor="black", alpha=0.7, color="#4C72B0")
artifacts/freige/analysis/ced_signal_validation.py:253:    axes[0, 1].hist(p_pos, bins=50, edgecolor="black", alpha=0.7, color="#55A868", label="p_pos")
artifacts/freige/analysis/ced_signal_validation.py:254:    axes[0, 1].hist(p_neg, bins=50, edgecolor="black", alpha=0.5, color="#C44E52", label="p_neg")
artifacts/freige/analysis/ced_signal_validation.py:260:    axes[1, 0].scatter(p_neg, p_pos, alpha=0.15, s=8, color="#4C72B0")
artifacts/freige/analysis/ced_signal_validation.py:271:    axes[1, 1].scatter(jaccard_diff, margins, alpha=0.15, s=8, color="#DD8452")
artifacts/freige/training/rsft_score_filter.py:419:    ced_model = CEDRewardModel(model_name=args.nli_model_path, device=args.nli_device)
artifacts/freige/training/rsft_trainer.py:169:        if hasattr(model, "gradient_checkpointing_disable"):
artifacts/freige/training/rsft_trainer.py:170:            model.gradient_checkpointing_disable()
artifacts/freige/training/rsft_trainer.py:216:        if hasattr(model, "gradient_checkpointing_enable"):
artifacts/freige/training/rsft_trainer.py:217:            model.gradient_checkpointing_enable()
artifacts/freige/training/rsft_trainer.py:267:    parser.add_argument("--lora_rank", type=int, default=64)
artifacts/freige/training/rsft_trainer.py:268:    parser.add_argument("--lora_alpha", type=int, default=128)
artifacts/freige/training/rsft_trainer.py:306:    local_rank = int(os.environ.get("LOCAL_RANK", 0))
artifacts/freige/training/rsft_trainer.py:310:        device_map={"": local_rank},
artifacts/freige/training/rsft_trainer.py:331:    model.gradient_checkpointing_enable()
artifacts/freige/training/rsft_trainer.py:336:        r=args.lora_rank,
artifacts/freige/training/rsft_trainer.py:337:        lora_alpha=args.lora_alpha
…[truncated 5701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-18T10:03:51.899496+00:00_

```
=== Qwen3-14B 可行性报告 ===

模型: Qwen/Qwen3-14B / 14.8B params (13.2B non-embedding) / bf16 ~29.5GB

架构:
  hidden_size: 5120
  num_layers: 40
  num_attention_heads: 40 (Q), 8 (KV, GQA)
  intermediate_size: 17408
  vocab_size: 151936
  head_dim: 128

─────────────────────────────────────────────

LoRA 参数量估算 (rank=64, 7 target modules per layer):
  q_proj:    (5120+5120)×64  = 655K
  k_proj:    (5120+1024)×64  = 393K
  v_proj:    (5120+1024)×64  = 393K
  o_proj:    (5120+5120)×64  = 655K
  gate_proj: (5120+17408)×64 = 1442K
  up_proj:   (5120+17408)×64 = 1442K
  down_proj: (17408+5120)×64 = 1442K
  ──────────────────────────────
  Per layer: 6.42M → 40 layers → ~257M LoRA params

─────────────────────────────────────────────

显存估算 1: bf16 LoRA (不量化)
  Base model (bf16):     14.8B × 2B = 29.6 GB
  LoRA adapters (bf16):  257M × 2B  = 0.5 GB
  Optimizer (fp32, AdamW): 257M × 12B = 3.1 GB
  Gradients (bf16):      257M × 2B  = 0.5 GB
  Activations (GC, bs=1, seq=4096): ~3-5 GB
  CUDA overhead:         ~1 GB
  ──────────────────────────────
  总计: ~38-40 GB
  32GB 单卡: ❌ 不可行 (模型权重本身已 29.6GB，几乎填满显存)

─────────────────────────────────────────────

显存估算 2: QLoRA 4-bit (NF4)
  Base model (4-bit):    14.8B × 0.5B = 7.4 GB
  量化 overhead:         ~0.5 GB
  LoRA adapters (bf16):  257M × 2B   = 0.5 GB
  Optimizer (fp32, AdamW): 257M × 12B = 3.1 GB
  Gradients (bf16):      257M × 2B   = 0.5 GB
  Activations (GC, bs=1, seq=4096): ~3-5 GB
  CUDA overhead:         ~1 GB
  ──────────────────────────────
  总计: ~16-18 GB
  32GB 单卡: ✅ 可行，余量充足 (~14GB headroom)

  可尝试 bs=2: 额外 ~3-4 GB activations → ~20-22 GB，仍可行

─────────────────────────────────────────────

Gradient Checkpointing 影响:
  关闭: activations 可达 10-15 GB (bs=1, seq=4096, 40 layers)
  开启: 降至 ~3-5 GB (只存层边界 activations，重算中间值)
  代价: 训练速度慢 ~30%
  QLoRA 场景下必须开启（已是项目默认配置）

─────────────────────────────────────────────

推荐配置:
  量化: QLoRA 4-bit (NF4, double_quant=True)
  batch_size: 1-2 (per_device)
  gradient_accumulation: 8 (有效 bs=8-16)
  gradient_checkpointing: True
  LoRA: rank=64, alpha=128 (与现有配置一致)
  precision: bf16 compute dtype
  flash_attention: 开启 (attn_implementation="flash_attention_2")

─────────────────────────────────────────────

预估训练时间:
  参考: Qwen3-8B bf16 LoRA, 3018 samples, 3 epochs, 1134 steps
  14B vs 8B: ~1.8x FLOPs (层数 40 vs 36, hidden 5120 vs 4096)
  QLoRA 额外开销: dequant ~10-15%, GC recompute ~30%
  综合: 每 step 约 2-2.5x 慢于 8B bf16 LoRA

  SFT (3000 samples, 3 epochs, ~1125 steps):  ~3-5h
  RSFT (3000 samples, 3 epochs, ~1125 steps): ~3-5h
  (实际取决于 seq_len 分布，DocRED 样本较短则更快)

─────────────────────────────────────────────

与现有 pipeline 兼容性:
  ✅ TRL SFTTrainer + PEFT LoRA: 完全兼容，同架构家族
  ✅ target_modules 名称一致: q/k/v/o_proj, gate/up/down_proj
  ✅ BitsAndBytesConfig 4-bit: 直接可用
  ✅ tokenizer/chat_template: Qwen3 系列通用
  ✅ 单卡训练: QLoRA 无需 model parallelism
  ✅ 代码改动: 只需改 model_name 路径
  ⚠️ 建议加 attn_implementation="flash_attention_2" 省显存+加速

─────────────────────────────────────────────

风险/注意事项:
  1. bf16 LoRA 不可行，必须用 QLoRA 4-bit
  2. 4-bit 量化会引入精度损失，可能影响 IE 任务细粒度输出质量
     → 需要实验验证 14B-QLoRA vs 8B-bf16 的质量权衡
  3. 推理/eval 同样需要 QLoRA 加载，单卡 ~8-9GB
     → eval 不会有显存压力 (C001 约束仍应遵守)
  4. 模型下载: bf16 safetensors ~29.5GB，需确认服务器磁盘空间
  5. Qwen3-14B 的 thinking mode (&lt;/think> tokens) 需在训练数据中处理
     → 建议用 chat_template 的 enable_thinking=False
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_qwen3_14b_feasibility_20260518T100058"
}
```

</details>

---
