# research 2025 2026 base models

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 187
- **Recorded user turns:** 0
- **Tool calls:** 93
- **Original source:** `logs/chats/worker_research_2025-2026-base-models_20260518T070717.jsonl`
- **Structured JSON:** [`cc5cf513634d2ab1797f.json`](../../sessions/cc/cc5cf513634d2ab1797f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

187 recorded events

### Tool call

_source line 1 · 2026-05-18T07:12:29.413433+00:00_

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
  "session": "worker_research_2025-2026-base-models_20260518T070717",
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

_source line 2 · 2026-05-18T07:12:29.413809+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T07:12:29.414025+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search batch 1: general + HF",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "tool_args": {
    "description": "Search batch 1: general + HF",
    "subagent_type": "general-purpose",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"best open source LLM 2025 2026 base model\"\nSearch 2: \"latest base models huggingface 2025\"\nSearch 3: \"new open source LLM families 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T07:12:29.414195+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search batch 2: Llama + Qwen + Mistral",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "tool_args": {
    "description": "Search batch 2: Llama + Qwen + Mistral",
    "subagent_type": "general-purpose",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Llama 4 base model release\"\nSearch 2: \"Qwen 3 base model\"\nSearch 3: \"Mistral latest base model 2025\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T07:12:29.414401+00:00_

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
  "session": "worker_research_2025-2026-base-models_20260518T070717",
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

_source line 6 · 2026-05-18T07:12:29.414557+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T07:12:29.414683+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search batch 3: Gemma + OLMo",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "tool_args": {
    "description": "Search batch 3: Gemma + OLMo",
    "subagent_type": "general-purpose",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"Gemma 3 base model\"\nSearch 2: \"OLMo 2 base model\"\nSearch 3: \"Gemma 3 pretrained model huggingface 2025\"\n\nReturn ALL findings in a structured format. Be thorough."
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T07:12:29.414916+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "best open source LLM 2025 2026 base model 7B 14B parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "best open source LLM 2025 2026 base model 7B 14B parameters"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T07:12:29.415053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "latest base models huggingface 2025 2026 open source LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "latest base models huggingface 2025 2026 open source LLM"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T07:12:29.415184+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "new open source LLM families 2025 2026 base model release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "new open source LLM families 2025 2026 base model release"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T07:12:29.415305+00:00_

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
  "session": "worker_research_2025-2026-base-models_20260518T070717",
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

_source line 12 · 2026-05-18T07:12:29.415484+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T07:12:29.415609+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search batch 4: DeepSeek + Phi",
  "subagent_type": "general-purpose",
  "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "tool_args": {
    "description": "Search batch 4: DeepSeek + Phi",
    "subagent_type": "general-purpose",
    "prompt": "You are researching the latest open-source base LLMs (7B-14B parameters) released in 2025-2026 for an academic paper. Run the following 3 web searches and compile ALL results with as much detail as possible. For each model found, note: full name, HuggingFace repo ID, parameter count, release date, whether it's gated, whether a base (non-instruct) version exists, training data size if mentioned, and benchmark performance if mentioned.\n\nSearch 1: \"DeepSeek V3 base model\"\nSearch 2: \"Phi-4 base model\"\nSearch 3: \"DeepSeek R2 base model 2025 2026\"\n\nReturn ALL findings in a structured format. Be thorough - list every model you find in the 7B-14B range. Also note if any of these models use MoE architecture (mixture of experts) and what the active parameter count is."
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T07:12:29.415769+00:00_

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
  "session": "worker_research_2025-2026-base-models_20260518T070717",
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

_source line 15 · 2026-05-18T07:12:29.415885+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T07:12:29.416009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 4 base model release 2025 2026 7B 8B parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 4 base model release 2025 2026 7B 8B parameters"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T07:12:29.416202+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen 3 base model 2025 2026 HuggingFace 7B 8B 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen 3 base model 2025 2026 HuggingFace 7B 8B 14B"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T07:12:29.416388+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mistral latest base model 2025 2026 7B parameters release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mistral latest base model 2025 2026 7B parameters release"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-18T07:12:29.416567+00:00_

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
  "session": "worker_research_2025-2026-base-models_20260518T070717",
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

_source line 20 · 2026-05-18T07:12:29.416695+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-18T07:12:29.416822+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 base model 2025 huggingface parameters release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 base model 2025 huggingface parameters release"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T07:12:29.416948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 2 base model 2025 huggingface parameters release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 2 base model 2025 huggingface parameters release"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-18T07:12:29.417070+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 pretrained model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 pretrained model huggingface 2025"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T07:12:29.417203+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-18T07:12:29.417346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phi-4 base model HuggingFace parameters 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phi-4 base model HuggingFace parameters 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T07:12:29.417475+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek R2 base model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek R2 base model 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T07:12:29.417611+00:00_

Web search results for query: "Llama 4 base model release 2025 2026 7B 8B parameters"

Links: [{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"Meta AI All Models Available: Llama‑4, Llama‑3, and Deployment Options","url":"https://www.datastudios.org/post/meta-ai-all-models-available-llama-4-llama-3-and-deployment-options"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Meta's Llama 4 models now available on AWS","url":"https://www.aboutamazon.com/news/aws/aws-meta-llama-4-models-available"},{"title":"Meta Llama 4 explained: Everything you need to know","url":"https://www.techtarget.com/whatis/feature/Meta-Llama-4-explained-Everything-you-need-to-know"},{"title":"Unmatched Performance and Efficiency | Llama 4","url":"https://www.llama.com/models/llama-4/"},{"title":"Llama 4: Did Meta just push the panic button?","url":"https://www.interconnects.ai/p/llama-4"},{"title":"Meta releases Llama 4, a new crop of flagship AI models | TechCrunch","url":"https://techcrunch.com/2025/04/05/meta-releases-llama-4-a-new-crop-of-flagship-ai-models/"},{"title":"Meta Llama: Everything you need to know about the open generative AI model | TechCrunch","url":"https://techcrunch.com/2025/10/06/meta-llama-everything-you-need-to-know-about-the-open-generative-ai-model/"}]

Based on the search results, here's what I found about Llama 4 base model releases:

## Llama 4 Release Information

On April 5, 2025, Meta released the Llama 4 model family, which includes the following base models:

### Model Specifications

Scout: 17 billion active parameter model with 16 experts, context window of 10M, with 109B parameters in total

Maverick: 17 billion active parameter model with 128 experts, context wind
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T07:12:29.417773+00:00_

Web search results for query: "latest base models huggingface 2025 2026 open source LLM"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"State of Open Source on Hugging Face: Spring 2026","url":"https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Top 10 Downloaded Open-Source Models on HuggingFace","url":"https://www.analyticsvidhya.com/blog/2025/11/top-open-source-models-on-huggingface/"},{"title":"Top 10 LLM Models on Hugging Face | Cloudsmith","url":"https://cloudsmith.com/blog/top-10-most-popular-llm-models-on-hugging-face"},{"title":"Top 7 Platforms to Fine-Tune Open Source LLMs in 2026 | Second Talent","url":"https://www.secondtalent.com/resources/top-platforms-to-fine-tune-open-source-llms/"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"}]

Based on the search results, here's a comprehensive overview of the latest base models on Hugging Face for 2025-2026 open source LLMs:

## Key Latest Models (2025-2026)

### Flagship Models

Kimi K2.6 is one of the strongest open-weight models for developers in 2026. The Hugging Face model card lists it under a Modified MIT license and shows a model size of about 1.1T parameters.

Qwen3 is the model family that quietly became
…[truncated 1215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T07:12:29.417947+00:00_

Web search results for query: "Qwen 3 base model 2025 2026 HuggingFace 7B 8B 14B"

Links: [{"title":"Qwen3 - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen/collections"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Download Qwen-3 Models - MoE, Dense & Quantized Versions","url":"https://qwen-3.com/en/download"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"},{"title":"Qwen/Qwen3-8B-GGUF · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-GGUF"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3-1.7B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-1.7B-Base"},{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"}]

Based on the web search results, here's what I found about Qwen 3 base models:

## Qwen3 Overview

Qwen3 is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models.

## Available Base Models

Six dense models are open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, with both pre-trained and post-trained versions available on platforms like Hugging Face, ModelScope, and Kaggle.

Notably, the specific models you asked about (7B, 8B, 14B) include the **Qwen3-8B** and **Qwen3-14B** base models. There is no 7B model in the Qwen3 lineup, but the 8B serves a similar purpose.

## Key Improvements

Qwen3 is pre-trained on 36 trillion tokens across 119 languages — tripling the language coverage of Qwen2.5 — with a much richer mix of high-quality data, including coding, STEM, reasonin
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T07:12:29.418104+00:00_

Web search results for query: "best open source LLM 2025 2026 base model 7B 14B parameters"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"Open LLM Leaderboard best models ❤️‍🔥 - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/open-llm-leaderboard-best-models"},{"title":"The Best Open Source and Open-Weight LLM Models to Run Locally in 2026","url":"https://huggingface.co/blog/daya-shankar/open-source-llm-models-to-run-locally"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Best Open-Source LLMs in 2026: A Practical Guide by Use Case - ML Journey","url":"https://mljourney.com/best-open-source-llms-in-2026-a-practical-guide-by-use-case/"},{"title":"Best Local LLM Models 2026 | Developer Comparison","url":"https://www.sitepoint.com/best-local-llm-models-2026/"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"}]

Based on the search results, here's a comprehensive overview of the best open-source LLM base models in the 7B-14B parameter range for 2025-2026:

## Top Base Models in 7B-14B Range

### 7B Models

**Qwen2.5-Coder 7B** - Fits on 8GB VRAM and outperforms general-purpose models twice its size on code generation, debugging, and refactoring.

**Qwen 3 7B** - Posts the highest HumanEval score (76.0) of any model under 8B parameters in t
…[truncated 1350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T07:12:29.418268+00:00_

Web search results for query: "Mistral latest base model 2025 2026 7B parameters release"

Links: [{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/models/overview"},{"title":"Mistral 7B | Mistral AI","url":"https://legal.mistral.ai/ai-governance/models/mistral-7-b"},{"title":"Mistral 7B LLM | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/models/mistral-7b"},{"title":"Mistral 7B - Mistral AI | Mistral Docs","url":"https://docs.mistral.ai/models/mistral-7b-0-1"},{"title":"Mistral 3 AI Explained - Open-Source Models Guide 2026 — Shawn Kanungo","url":"https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026"},{"title":"mistral","url":"https://ollama.com/library/mistral"},{"title":"mistral-7b-instruct-v0.2 Model by Mistral AI","url":"https://build.nvidia.com/mistralai/mistral-7b-instruct-v2/modelcard"},{"title":"Models - from cloud to edge | Mistral AI","url":"https://mistral.ai/models"},{"title":"Mistral AI Models 2026: Small 4, Large 3, Voxtral TTS, Forge — Complete Guide | Serenities AI","url":"https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide"}]

Based on the search results, here's information about Mistral's latest base models in 2025-2026:

## Mistral 3 Family (December 2025)

Mistral 3 AI is a family of 10 artificial intelligence models that launched in December 2025. The Ministral 3 family includes dense models at 14B, 8B, and 3B parameters. 

The base model lineup includes:
- 3B, 8B, and 14B models for different use cases

Key features of Mistral 3 base models:
- Every single model in the family can process both text and images, with vision baked into the core training
- Trained natively on over 40 languages with particular strength in European languages
- Mistral 3 extends context windows up to 256K tokens
- Released under the Apache 2.0 license, allowing free commercial use and modification

## Mistral Small
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T07:12:29.418460+00:00_

Web search results for query: "new open source LLM families 2025 2026 base model release"

Links: [{"title":"Open-Source LLM Landscape 2026, 15+ Model Families Mapped | Presenc AI","url":"https://presenc.ai/research/open-source-llm-landscape-2026"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source Self-Hosted LLMs for Coding in 2026 - Pinggy","url":"https://pinggy.io/blog/best_open_source_self_hosted_llms_for_coding/"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Open-Source LLMs 2026: Llama 4, Mistral, Qwen, Falcon & More | AI Moments","url":"https://www.singularitymoments.com/open-source-llms-2026/"},{"title":"Open Source LLM Releases 2026: Every Major Model So Far - Fazm Blog","url":"https://fazm.ai/blog/open-source-llm-releases-2026"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"}]

Based on the search results, here's a comprehensive overview of new open-source LLM families released in 2025-2026:

## Major Model Families Released

### Meta Llama 4 (April 2025)
Llama 4 includes Scout (109B total, 17B active, 10M context window), Maverick (400B total, 17B active, 1M context), and the announced but unreleased Behemoth (~2T total, 288B active). Llama 4 is the most widely deployed open source model family, with over 650 million total downloads and roughly 9% of enterprise production workloads running on Llama variant
…[truncated 1820 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T07:12:29.418622+00:00_

Web search results for query: "DeepSeek V3 base model HuggingFace 7B 14B parameters 2025 2026"

Links: [{"title":"deepseek-ai/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3"},{"title":"DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/deepseek_v3"},{"title":"deepseek-ai/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3-Base"},{"title":"DeepSeek-V3","url":"https://huggingface.co/docs/transformers/main/en/model_doc/deepseek_v3"},{"title":"deepseek-ai/DeepSeek-V3.1-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Base"},{"title":"anchovy/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/anchovy/DeepSeek-V3-Base"},{"title":"README_WEIGHTS.md · deepseek-ai/DeepSeek-V3 at main","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/README_WEIGHTS.md"},{"title":"deepseek-ai/DeepSeek-V3.2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3.2"},{"title":"unsloth/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-V3"},{"title":"deepseek-ai/DeepSeek-V3 - Demo - DeepInfra","url":"https://deepinfra.com/deepseek-ai/DeepSeek-V3"}]

Based on the search results, I found information about DeepSeek V3. However, I should clarify that the specific 7B and 14B parameter versions you mentioned in your query don't appear to exist for DeepSeek V3.

## DeepSeek V3 Model Specifications

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. The total size of DeepSeek-V3 models on HuggingFace is 685B, which includes 671B of the Main Model weights and 14B of the Multi-Token Prediction (MTP) Module weights.

The DeepSeek V3 base model is available on HuggingFace under the repository `deepseek-ai/DeepSeek-V3-Base`. This is the primary base model available, and it does not come in 7B or 14B variants - it is a 671B parameter model
…[truncated 461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-18T07:12:29.418778+00:00_

Web search results for query: "OLMo 2 base model 2025 huggingface parameters release"

Links: [{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"allenai/OLMo-2-0325-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/OLMo-2-0425-1B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B"},{"title":"OLMo2 · Hugging Face","url":"https://huggingface.co/docs/transformers/main/en/model_doc/olmo2"},{"title":"allenai/OLMo-2-0425-1B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-DPO"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"OLMo2","url":"https://huggingface.co/docs/transformers/v4.56.2/en/model_doc/olmo2"}]

Based on the search results, here's what I found about OLMo 2 base models released in 2025:

## OLMo 2 Model Releases

OLMo 2 is a new family of 7B and 13B models featuring a 9-point increase in MMLU, among other evaluation improvements, compared to the original OLMo 7B model.

### Available Model Sizes

The OLMo 2 family includes multiple model sizes:

1. **7B Model** - The 7B model was trained on OLMo-mix-1124 and Dolmino-mix-1124 datasets using a staged training approach.

2. **13B Model** - A 13B model trained on up to 5T tokens.

3. **1B Model** - OLMo 2 1B is the smallest model in the OLMo 2 family.

4. **32B Model** - Available as of March 2025

### Key Details

- **Training**: Models were trained on up to 5T tokens.
- **Release**: This model was released on 2024-12-31 and added to Hugging Face Transformers on 2024
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-18T07:12:29.418934+00:00_

Web search results for query: "Gemma 3 base model 2025 huggingface parameters release"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Gemma 3","url":"https://huggingface.co/docs/transformers/v4.57.3/en/model_doc/gemma3"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"google/gemma-3n-E4B-it-litert-preview · Hugging Face","url":"https://huggingface.co/google/gemma-3n-E4B-it-litert-preview"},{"title":"Gemma 3 - a unsloth Collection","url":"https://huggingface.co/collections/unsloth/gemma-3"},{"title":"Gemma 3n fully available in the open-source ecosystem!","url":"https://huggingface.co/blog/gemma3n"},{"title":"Gemma3n","url":"https://huggingface.co/docs/transformers/en/model_doc/gemma3n"},{"title":"Gemma 3 - How to Run Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/tutorials/gemma-3-how-to-run-and-fine-tune"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"}]

Based on the search results, here's what I found about Gemma 3 base models released in 2025 on Hugging Face:

## Model Sizes and Parameters

Gemma 3 comes in four sizes: 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions. Additionally, Google released Gemma 3 with a new 270M model, so the complete lineup includes five different sizes.

## Multimodal Capabilities

The 4, 12, and 27 billion parameter models can process both images and text, while the 1B variant is text only. The 270M model is also text-only.

## Context Window

The input context window length has been increased from Gemma 2's 8k to 32k for the 1B variants, and 128k for all others.

## Release Timeline

Gemma 3 is Google's latest 
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-18T07:12:29.419122+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-8B-Base Qwen3-14B-Base HuggingFace release date benchmark performance training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-8B-Base Qwen3-14B-Base HuggingFace release date benchmark performance training data"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-18T07:12:29.419263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mistral 3 base model 8B 14B HuggingFace release date December 2025 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mistral 3 base model 8B 14B HuggingFace release date December 2025 benchmark"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T07:12:29.419418+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 4 Scout Maverick base pretrained model HuggingFace gated download"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 4 Scout Maverick base pretrained model HuggingFace gated download"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T07:12:29.419558+00:00_

Web search results for query: "Phi-4 base model HuggingFace parameters 2025 2026"

Links: [{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"microsoft/Phi-4-reasoning-vision-15B · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"nvidia/Phi-4-multimodal-instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Phi-4-multimodal-instruct-NVFP4"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"nvidia/Phi-4-reasoning-plus-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Phi-4-reasoning-plus-NVFP4"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"}]

Based on the web search results, here's information about Phi-4 base model parameters available on HuggingFace:

## Phi-4 Model Variants and Parameters

The Phi-4 family includes several models with different parameter sizes:

1. **Phi-4-mini models**: The model with only 3.8B-param achieves a similar level of multilingual language understanding and reasoning ability as much larger models. This includes variants like Phi-4-mini-instruct and Phi-4-mini-reasoning.

2. **Phi-4 Base Model**: While the search results don't explicitly state the base model's parameter count, they reference a standard Phi-4 model.

3. **Phi-4-Reasoning**: Phi-4-reasoning, with only 14B parameters, performs we
…[truncated 720 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-18T07:12:29.419720+00:00_

Web search results for query: "Gemma 3 pretrained model huggingface 2025"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"transformers/docs/source/en/model_doc/gemma3.md at main · huggingface/transformers","url":"https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/gemma3.md"},{"title":"Gemma 3","url":"https://huggingface.co/docs/transformers/v5.0.0rc2/model_doc/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"Run Gemma with Hugging Face Transformers | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_inference"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"google/gemma-3-1b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-it"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"Gemma3n","url":"https://huggingface.co/docs/transformers/main/en/model_doc/gemma3n"}]

Based on the search results, here's comprehensive information about Gemma 3 pretrained models on Hugging Face:

## Overview

Google released Gemma 3, which ranges from 1B to 27B parameters, has a context window up to 128k tokens, can accept images and text, and supports 140+ languages. This model was released on 2025-03-25 and added to Hugging Face Transformers on 2025-03-12.

## Model Variants

Gemma 3 comes in four sizes: 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions. The 4, 12, and 27 billion parameter models can process both images and text, while the 1B variant is text only.

## Key Features

- **Context Window**: The input context window lengt
…[truncated 787 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-18T07:12:29.419879+00:00_

Web search results for query: "DeepSeek R2 base model 2025 2026"

Links: [{"title":"The Ultimate DeepSeek Guide 2026 | Master AI with DeepSeek-V3.2 & R2","url":"https://deepseek.ai/blog/deepseek-guide-2026"},{"title":"Will DeepSeek’s new model spark another global AI shake-up in 2026?","url":"https://restofworld.org/2025/deepseek-china-r2-ai-model-us-rivalry/"},{"title":"DeepSeek V4 and R2 Deep Dive | Meta Intelligence","url":"https://www.meta-intelligence.tech/en/insight-deepseek-v4-r2"},{"title":"DeepSeek's Next Move: What V4 Will Look Like","url":"https://recodechinaai.substack.com/p/deepseeks-next-move-what-v4-will"},{"title":"What is DeepSeek R2: The Best Upcoming AI Model In 2025? | AI Hub","url":"https://overchat.ai/ai-hub/what-is-deepseek-r2"},{"title":"Deepseek R2 Release Timeline & Updates 2025","url":"https://www.byteplus.com/en/topic/384181"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"},{"title":"DeepSeek Plans AI Agent Rollout in Late 2025 - Techstrong.ai","url":"https://techstrong.ai/features/deepseek-plans-ai-agent-rollout-in-late-2025/"},{"title":"DeepSeek Roadmap, Rumors & Confirmed Releases: What Is Official and What Is Not - Chat-Deep.ai","url":"https://chat-deep.ai/guide/deepseek-roadmap-rumors/"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"}]

Based on the search results, here's what I found regarding DeepSeek R2 base model in 2025-2026:

## DeepSeek R2 Status

In late February 2026, multiple sources confirmed that DeepSeek was preparing to release two new models: DeepSeek V4 (the fourth generation of its general-purpose foundation model) and DeepSeek R2 (the second generation of its reasoning model).

However, as of May 7, 2026, R2 is not listed among the current model IDs in the official DeepSeek API model list, and no official R2 release was found in the checked DeepSeek model list or release pages.

## Dev
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-18T07:12:29.420037+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 7B 8B base model huggingface repo release date benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 7B 8B base model huggingface repo release date benchmark"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T07:12:29.420172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 12B base model huggingface repo benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 12B base model huggingface repo benchmark 2026"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-18T07:12:29.420299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 4 8B base model huggingface 2025 release"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 4 8B base model huggingface 2025 release"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-18T07:12:29.420466+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phi-4 14B base model huggingface repo release date training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phi-4 14B base model huggingface repo release date training data"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-18T07:12:29.420624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "google/gemma-3-12b-pt huggingface model card gated benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "google/gemma-3-12b-pt huggingface model card gated benchmark"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-18T07:12:29.420753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "microsoft phi-4 14B base model HuggingFace parameters release date gated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "microsoft phi-4 14B base model HuggingFace parameters release date gated"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-18T07:12:29.420879+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "allenai/OLMo-2-1124-7B huggingface model card benchmark training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "allenai/OLMo-2-1124-7B huggingface model card benchmark training tokens"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-18T07:12:29.421014+00:00_

Web search results for query: "Llama 4 Scout Maverick base pretrained model HuggingFace gated download"

Links: [{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Original · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Original"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"},{"title":"unsloth/Llama-4-Maverick-17B-128E · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"}]

Based on the search results, here's what I found about Llama 4 Scout and Maverick base pretrained models on HuggingFace:

## Model Overview

Llama 4 Maverick (~400B) and Llama 4 Scout (~109B) were released on the Hugging Face Hub, and both are Mixture of Experts (MoE) models with 17B active parameters.

## Base Pretrained Models

Llama 4 Scout was pretrained on ~40 trillion tokens and Llama 4 Maverick was pretrained on ~22 trillion tokens of multimodal data. The Llama 4 models were pre-trained with a context length of 256K.

## Model Weights and Formats

The Ll
…[truncated 636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-18T07:12:29.421172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "allenai/OLMo-2-1124-13B huggingface model card benchmark training data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "allenai/OLMo-2-1124-13B huggingface model card benchmark training data"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-18T07:12:29.421304+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-18T07:12:29.421457+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "google/gemma-3-4b-pt huggingface pretrained base model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "google/gemma-3-4b-pt huggingface pretrained base model"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-18T07:12:29.421596+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T07:12:29.421732+00:00_

Web search results for query: "Qwen3-8B-Base Qwen3-14B-Base HuggingFace release date benchmark performance training data"

Links: [{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Speed Benchmark - Qwen","url":"https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen 3 Benchmarks, Comparisons, Model Specifications, and More - DEV Community","url":"https://dev.to/best_codes/qwen-3-benchmarks-comparisons-model-specifications-and-more-4hoa"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"}]

Based on the search results, here's comprehensive information about Qwen3-8B-Base and Qwen3-14B-Base:

## Release Date
Qwen3 was released on April 29, 2025, with both the 8B and 14B base models included in this release.

## Model Specifications

**Qwen3-8B-Base:**
- Dense model architecture with 8B parameters

**Qwen3-14B-Base:**
The model has 14.8B parameters, 13.2B non-embedding parameters, 40 layers, 40 attention heads (GQA) for Q and 8 for KV, and a context length of 32,768 tokens.

## Training Data
Qwen3 is pre-trained on 36 trillion tokens across 119 languages with a much richer mix of high-quality data, including coding, STEM, reasoning, book, multilingual, and synthetic data.

## Benchmark P
…[truncated 678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-18T07:12:29.421891+00:00_

Web search results for query: "Mistral 3 base model 8B 14B HuggingFace release date December 2025 benchmark"

Links: [{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Mistral 3 AI Explained - Open-Source Models Guide 2026 — Shawn Kanungo","url":"https://shawnkanungo.com/blog/what-is-mistral-3-ai-open-source-models-guide-2026"},{"title":"NVIDIA Partners With Mistral AI to Accelerate New Family of Open Models | NVIDIA Blog","url":"https://blogs.nvidia.com/blog/mistral-frontier-open-models/"},{"title":"Mistral Large 3: An Open-Source MoE LLM Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mistral-large-3-moe-llm-explained"},{"title":"Mistral Large 3: First Look and Testing","url":"https://www.analyticsvidhya.com/blog/2025/12/mistral-large-3/"},{"title":"Mistral 3 Arrives With Large 3 and Ministral Models for Enterprise and Edge AI","url":"https://www.reworked.co/ai-platforms/mistral-3-arrives-with-large-3-and-ministral-models-for-enterprise-and-edge-ai/"},{"title":"Mistral Large 3 by Mistral AI on Vercel AI Gateway, Specs, Pricing & API","url":"https://vercel.com/ai-gateway/models/mistral-large-3"},{"title":"Ministral 3 - 8B | Mistral AI","url":"https://legal.mistral.ai/ai-governance/models/ministral-3-8b"},{"title":"Mistral 3 Models on DigitalOcean | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/mistral-3-models"},{"title":"Mistral Large 3 and Ministral 3 family now available first on Amazon Bedrock - AWS","url":"https://aws.amazon.com/about-aws/whats-new/2025/12/mistral-large-3-ministral-3-family-available-amazon-bedrock/"}]

Based on the web search results, here's the information about Mistral 3 base models:

## Release Date

Mistral 3 AI is a family of 10 artificial intelligence models that launched in December 2025. More specifically, Mistral 3 launched on December 2, 2025.

## Model Sizes

For edge and local use cases, the Ministral 3 series is available in three model s
…[truncated 698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-18T07:12:29.422043+00:00_

Web search results for query: "Qwen3 7B 8B base model huggingface repo release date benchmark"

Links: [{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3-8B-FP8 · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-FP8"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen3.6-27B: 27B Model Beats 397B on Coding (2026)","url":"https://www.buildfastwithai.com/blogs/qwen3-6-27b-review-2026"},{"title":"Qwen3 - a Qwen Collection","url":"https://huggingface.co/collections/Qwen/qwen3"},{"title":"Qwen/Qwen3-Embedding-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Embedding-8B"},{"title":"Qwen (Qwen)","url":"https://huggingface.co/Qwen"}]

Based on the search results, here's what I found about Qwen3 7B/8B base models:

## Release Date

Qwen3 was released in 2025, with the technical report available on arXiv (2505.09388). More specifically, Qwen3 was announced as the latest addition to the Qwen family of large language models.

## Hugging Face Repository

Six dense models are open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, with pre-trained counterparts available on Hugging Face, ModelScope, and Kaggle.

## Base Model Performance Benchmarks

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-8B-Base performs as well as Qwen2.5-14B-Base. Additionally, in areas like STEM, coding, 
…[truncated 617 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T07:12:29.422223+00:00_

Web search results for query: "Llama 4 8B base model huggingface 2025 release"

Links: [{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"nvidia/Llama-4-Scout-17B-16E-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-4-Scout-17B-16E-Instruct-FP8"},{"title":"aviol/Meta-Llama-4-8B · Hugging Face","url":"https://huggingface.co/aviol/Meta-Llama-4-8B"},{"title":"nvidia/Llama-3.1-8B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/llama4"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"Meta Llama 4 explained: Everything you need to know","url":"https://www.techtarget.com/whatis/feature/Meta-Llama-4-explained-Everything-you-need-to-know"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Llama (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Llama_(language_model)"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's what I found about Llama 4 and the 8B base model:

## Llama 4 Release Information

Llama 4 was released on April 5, 2025. However, it's important to note that the Llama 4 family of models comes in two flavors: 109B and 402B parameters, along with smaller efficient models.

## Llama 4 Model Sizes

Rather than an 8B base model, Meta is launching two efficient models in the Llama 4 series: Llama 4 Scout, a 17 billion parameter model with 16 experts, and Llama 4 Maverick, a 17 billion parameter model with 128 experts.

The Llama 4 collection of models are natively multimodal AI models that enable text and multimodal experiences, leveraging a mixture-of-experts architecture to offer
…[truncated 588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-18T07:12:29.422482+00:00_

Web search results for query: "Phi-4 14B base model huggingface repo release date training data"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"OpenMeditron/Meditron3-Phi4-14B · Hugging Face","url":"https://huggingface.co/OpenMeditron/Meditron3-Phi4-14B"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/phi"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"}]

Based on the web search results, here's the information about Phi-4 14B base model:

## Release Date

Phi-4 is Microsoft's December 2024 release of their efficient-LLM family — a 14.7B-parameter model.

## Training Data

The training data is an extension of the data used for Phi-3 and includes a wide variety of sources from: Publicly available documents filtered rigorously for quality, selected high-quality educational data, and code. Newly created synthetic, "textbook-like" data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world. Acquired academic books and Q&A datasets. High quality chat format supervised data covering various topics to reflect human preferences on different 
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-18T07:12:29.422669+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ministral 3 8B base model HuggingFace repo \"mistralai\" parameters context length"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ministral 3 8B base model HuggingFace repo \"mistralai\" parameters context length"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T07:12:29.422816+00:00_

Web search results for query: "microsoft phi-4 14B base model HuggingFace parameters release date gated"

Links: [{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Introducing Phi-4: Microsoft’s Newest Small Language Model Specializing in Complex Reasoning | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090"},{"title":"Microsoft Launches Two Powerful Phi-4 Reasoning Models","url":"https://www.analyticsvidhya.com/blog/2025/05/phi-4-reasoning-models/"},{"title":"microsoft/Phi-4-reasoning-vision-15B · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/phi-4 · Base model","url":"https://huggingface.co/microsoft/phi-4/discussions/4"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"}]

Based on the web search results, here's what I found about Microsoft Phi-4 14B base model on HuggingFace:

## Key Information

**Parameters:** Phi-4 has 14.7B parameters

**Release Date:** Phi-4 is the December 2024 release of Microsoft's Phi family

**Model Status:** Phi-4 is available on Azure AI Foundry and on Hugging Face

**Architecture:** It's a standard decoder-only transformer with 16K context and ChatML chat template

**License:** The license is MIT — most permissive of recent major release
…[truncated 643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-18T07:12:29.422970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-8B-Base parameters layers context length gated apache license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-8B-Base parameters layers context length gated apache license"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-18T07:12:29.423114+00:00_

Web search results for query: "google/gemma-3-12b-pt huggingface model card gated benchmark"

Links: [{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"google/gemma-3-12b-it-qat-q4_0-gguf · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-gguf"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"google/gemma-3-12b-pt at main","url":"https://huggingface.co/google/gemma-3-12b-pt/tree/main"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3: Google’s new open model based on Gemini 2.0","url":"https://blog.google/technology/developers/gemma-3/"},{"title":"google/gemma-3-27b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-pt"},{"title":"google/gemma-3-12b-it-qat-q4_0-unquantized · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-unquantized"}]

Based on the search results, I found information about the **google/gemma-3-12b-pt** model on Hugging Face:

## Key Information

**Model Access:** To access Gemma on Hugging Face, you're required to review and agree to Google's usage license. This is a gated model.

**Model Description:** Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

**Model Capabilities:** Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-18T07:12:29.423268+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 4 Scout base pretrained non-instruct HuggingFace \"meta-llama\" gated license"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 4 Scout base pretrained non-instruct HuggingFace \"meta-llama\" gated license"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-18T07:12:29.423472+00:00_

Web search results for query: "google/gemma-3-4b-pt huggingface pretrained base model"

Links: [{"title":"google/gemma-3-4b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-4b-pt"},{"title":"google/gemma-3-4b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-4b-it"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-1b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-pt"},{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"RedHatAI/gemma-3-4b-it-quantized.w4a16 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-3-4b-it-quantized.w4a16"},{"title":"Run Gemma with Hugging Face Transformers | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_inference"},{"title":"Full Model Fine-Tune using Hugging Face Transformers | Gemma | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_text_full_finetune"},{"title":"Fine-Tune Gemma for Vision Tasks using Hugging Face Transformers and QLoRA | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_vision_finetune_qlora"},{"title":"google/gemma-3-1b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-it"}]

Based on the web search results, here's what I found about the **google/gemma-3-4b-pt** model on Hugging Face:

## Model Overview

Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. The "pt" suffix indicates this is the **pre-trained (base) version** rather than an instruction-tuned variant.

## Key Characteristics

Gemma 3 comes in four sizes, 1 billion, 4 billion, 12 billion, and 27 billion parameters with base (pre-trained) and instruction-tuned versions. The 4B variant has 4 billion parameters.

G
…[truncated 876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-18T07:12:29.423645+00:00_

Web search results for query: "Gemma 3 12B base model huggingface repo benchmark 2026"

Links: [{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"tensorblock/gemma-3-12b-it-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/gemma-3-12b-it-GGUF"},{"title":"google/gemma-3-12b-it-qat-q4_0-gguf · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it-qat-q4_0-gguf"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"RedHatAI/gemma-3-12b-it-quantized.w8a8 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-3-12b-it-quantized.w8a8"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"nocturne23/gemma-3-12b-it-Q4_K_M-GGUF · Hugging Face","url":"https://huggingface.co/nocturne23/gemma-3-12b-it-Q4_K_M-GGUF"},{"title":"lmstudio-community/gemma-3-12b-it-GGUF · Hugging Face","url":"https://huggingface.co/lmstudio-community/gemma-3-12b-it-GGUF"},{"title":"Quantized Models for google/gemma-3-12b-it – Hugging Face","url":"https://huggingface.co/models?other=base_model%3Aquantized%3Agoogle%2Fgemma-3-12b-it"}]

Based on the web search results, I found information about the Gemma 3 12B model on Hugging Face. Here's what I found:

## Gemma 3 12B Base Model Overview

Gemma 3 is a family of lightweight, state-of-the-art open models from Google, and Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants.

Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

## Benchmark Performance

Using the benchmark evaluation metrics described in this
…[truncated 884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-18T07:12:29.423802+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen 3 base model benchmark MMLU GSM8K HumanEval scores 8B 14B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen 3 base model benchmark MMLU GSM8K HumanEval scores 8B 14B"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-18T07:12:29.423940+00:00_

Web search results for query: "allenai/OLMo-2-1124-13B huggingface model card benchmark training data"

Links: [{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"allenai/OLMo-2-1124-13B-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-GGUF"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"allenai/OLMo-2-1124-13B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct"},{"title":"allenai/OLMo-2-1124-13B-DPO-Preview · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-DPO-Preview"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-2-1124-13B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-RM"},{"title":"allenai/OLMo-2-1124-13B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-SFT"},{"title":"allenai/OLMo-2-1124-13B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-DPO"},{"title":"allenai/OLMo-2-1124-13B · What Instruct Template? Recommended Temperature?","url":"https://huggingface.co/allenai/OLMo-2-1124-13B/discussions/3"}]

Based on the search results, I found comprehensive information about the allenai/OLMo-2-1124-13B model card from Hugging Face. Here's what I found:

## Model Overview
OLMo is a series of Open Language Models designed to enable the science of language models. These models are trained on the Dolma dataset.

## Training Data
OLMo 2 is a new family of 7B and 13B models featuring a 9-point increase in MMLU, among other evaluation improvements, compared to the original OLMo 7B model. These gains come from training on OLMo-mix-1124 and Dolmino-mix-1124 datasets and staged training approach.

## Benchmark Results
Core model results for OLMo 2 7B and 13B models are found below
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-18T07:12:29.424098+00:00_

Web search results for query: "Phi-4 base pretrained model not instruct HuggingFace microsoft 14B"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"Introducing Phi-4: Microsoft’s Newest Small Language Model Specializing in Complex Reasoning | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Welcome to the new Phi-4 models - Microsoft Phi-4-mini & Phi-4-multimodal","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/welcome-to-the-new-phi-4-models---microsoft-phi-4-mini--phi-4-multimodal/4386037"},{"title":"NyxKrage/Microsoft_Phi-4 · Hugging Face","url":"https://huggingface.co/NyxKrage/Microsoft_Phi-4"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"Phi-4 - a microsoft Collection","url":"https://huggingface.co/collections/microsoft/phi-4-677e9380e514feb5577a40e4"},{"title":"Microsoft makes powerful Phi-4 model fully open-source on Hugging Face | VentureBeat","url":"https://venturebeat.com/ai/microsoft-makes-powerful-phi-4-model-fully-open-source-on-hugging-face"}]

Based on the search results, here's what I found about the Phi-4 base pretrained model:

## Phi-4 Base Model Overview

Phi-4 is a 14B parameters, dense decoder-only transformer model. Phi-4 is available on Azure AI Foundry and on Hugging Face.

### Model Details

The training data is an extension of the data used for Phi-3 and inc
…[truncated 1088 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-18T07:12:29.424256+00:00_

Web search results for query: "DeepSeek V3 V2 small model 7B 14B 16B lite base 2025 2026 HuggingFace"

Links: [{"title":"DeepSeek Official Models List 2026 (V4, Flash, Pro) | DeepSeek V4 Network","url":"https://deepseekv4.network/models"},{"title":"DeepSeek Models Guide: R1, V3, and Coder | InsiderLLM","url":"https://insiderllm.com/guides/deepseek-models-guide/"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"GitHub - deepseek-ai/DeepSeek-V3 · GitHub","url":"https://github.com/deepseek-ai/deepseek-v3"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"Ultimate Guide - The Best DeepSeek-AI Models in 2026","url":"https://www.siliconflow.com/articles/en/the-best-deepseek-ai-models-in-2025"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"DeepSeek Models: V3.2, R1, Distills, and Production Caveats","url":"https://fireworks.ai/blog/deepseek-models"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek - Wikipedia","url":"https://en.wikipedia.org/wiki/DeepSeek"}]

Based on the search results, here's a comprehensive overview of DeepSeek models including the versions and sizes you asked about:

## DeepSeek Model Family Overview

### V1 Series
V1 has a dense stack of 7B and 67B models with 4K context and ~2T tokens.

### V2 Series
V2 uses MoE architecture with 236B total parameters, ~21B active, 128K context, ~8T tokens. V2-Lite trims to ~16B total and ~2.4B active for smaller clusters.

### V3 Series
V3 MoE has 671B total parameters, ~37B active, 256 experts, ~14T tokens. In March 2025, DeepSeek released DeepSeek-V3-0324, which uses the same 
…[truncated 1006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-18T07:12:29.424528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-18T07:12:29.424720+00:00_

Web search results for query: "allenai/OLMo-2-1124-7B huggingface model card benchmark training tokens"

Links: [{"title":"allenai/OLMo-2-1124-7B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-2-1124-7B-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-GGUF"},{"title":"allenai/OLMo-2-1124-7B-RM-Preview · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM-Preview"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"allenai/OLMo-2-1124-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-Instruct"},{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/OLMo-2-1124-7B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-DPO"},{"title":"README.md · allenai/OLMo-2-1124-7B at 22fbf33a789d28264eb2f5511cda7dbc8338e976","url":"https://huggingface.co/allenai/OLMo-2-1124-7B/blame/22fbf33a789d28264eb2f5511cda7dbc8338e976/README.md"},{"title":"allenai/OLMo-2-1124-7B-DPO-Preview · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-DPO-Preview"}]

Now let me search for more specific information about training tokens for this model:

Links: [{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"OLMo-2-1124-7B","url":"https://www.promptlayer.com/models/olmo-2-1124-7b"},{"title":"GitHub - allenai/OLMo: Modeling, training, eval, and inference code for OLMo · GitHub","url":"https://github.com/allenai/OLMo"},{"title":"allenai/OLMo-2-1124-7B-Instruct Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/allenai-olmo-2-1124-7b-instruct-free-chat-online-skywork-ai/"},{"title":"Papers Explain
…[truncated 2179 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-18T07:12:29.424888+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"
  }
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-18T07:12:29.425024+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-18T07:12:29.425162+00:00_

Web search results for query: "Ministral 3 8B base model HuggingFace repo "mistralai" parameters context length"

Links: [{"title":"mistralai/Ministral-3-8B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Base-2512"},{"title":"mistralai/Ministral-3-8B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512"},{"title":"mistralai/Ministral-3-8B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512"},{"title":"mistralai/Ministral-3-8B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-BF16"},{"title":"mistralai/Ministral-8B-Instruct-2410 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-8B-Instruct-2410"},{"title":"mistralai/Ministral-3-8B-Instruct-2512-GGUF · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-GGUF"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Mistral · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/mistral"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Mistral 3 Models on DigitalOcean | DigitalOcean","url":"https://www.digitalocean.com/community/tutorials/mistral-3-models"}]

Based on the search results, here is the information about the Ministral 3 8B base model from the mistralai HuggingFace repository:

## Model: mistralai/Ministral-3-8B-Base-2512

**Context Length:** The model supports a 256k context window.

**Model Size:** The Ministral 3 series is available in three model sizes: 3B, 8B, and 14B parameters.

**Architecture and Capabilities:** For each model size, base, instruct, and reasoning variants are released to the community, each with image understanding capabilities, all under the Apache 2.0 license.

**Hardware Requirements:** Due to their size an
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-18T07:12:29.425348+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-18T07:12:29.425531+00:00_

Web search results for query: "Qwen3-8B-Base parameters layers context length gated apache license"

Links: [{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"Qwen3.5-0.8B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen3.5-0.8b"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"LICENSE · Qwen/Qwen3-8B at main","url":"https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE"},{"title":"Qwen Models Guide: 600M to 1 Trillion Parameters","url":"https://www.digitalapplied.com/blog/qwen-models-complete-guide"},{"title":"dengcao/Qwen3-8B","url":"https://ollama.com/dengcao/Qwen3-8B"},{"title":"Qwen/Qwen3-Next-80B-A3B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"},{"title":"Qwen3-8B-Base: Open 8B LLM Overview","url":"https://www.emergentmind.com/topics/qwen3-8b-base"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"}]

Based on the search results, here's the information about Qwen3-8B-Base:

## Parameters and Architecture

Qwen3-8B is a dense transformer-based model with 8.2 billion parameters—6.95 billion of which are non-embedding parameters—spanning 36 layers.

The model has 32 attention heads for Query and 8 for Key/Value (GQA), with a context length of 32,768 tokens natively and 131,072 tokens with YaRN.

## Gated Attention

While the search results mention gated attention in a related model, Qwen3-Next-80B-A3B replaces standard attention with the combination of Gated DeltaNet and Gated Attention, enabling efficient context modeling for ultra-long context length. However, specific information about whether Qwen3-8B-Base itself uses gated attention mechanisms is not explicitly stated in these resul
…[truncated 343 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-18T07:12:29.425715+00:00_

Web search results for query: "Llama 4 Scout base pretrained non-instruct HuggingFace "meta-llama" gated license"

Links: [{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"unsloth/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Scout-17B-16E-Instruct"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct at main","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct/tree/main"},{"title":"LLaMA 4 Explained - Everything You Need to Know","url":"https://www.labellerr.com/blog/llama-4/"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/llama4"},{"title":"future-technologies/FineTuned-Meta-Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/future-technologies/FineTuned-Meta-Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's what I found about Llama 4 Scout:

## Model Overview

Llama 4, developed by Meta, introduces a new auto-regressive Mixture-of-Experts (MoE) architecture, with Llama 4 Scout having 17B active parameters out of ~109B total, using just 16 experts.

## Base (Non-Instruct) Model

The base pretrained variant is available at `meta-llama/Llama-4-Scout-17B-16E` on HuggingFace. Pretrained models can be adapted for natural language generation.

## Gated License

You need to accept the license terms on the model card before accessing the weights. These models a
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-18T07:12:29.425880+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-18T07:12:29.426018+00:00_

Web search results for query: "Qwen 3 base model benchmark MMLU GSM8K HumanEval scores 8B 14B"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"AngelSlim/Qwen3-14B_eagle3 · Hugging Face","url":"https://huggingface.co/AngelSlim/Qwen3-14B_eagle3"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"AngelSlim/Qwen3-4B_eagle3 · Hugging Face","url":"https://huggingface.co/AngelSlim/Qwen3-4B_eagle3"},{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"Swallow LLM Leaderboard","url":"https://swallow-llm.github.io/leaderboard/about.en.html"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen Latest Model | Most Recent Release","url":"https://qwen.co.com/latest-model.html"},{"title":"Qwen2.5-LLM: Extending the boundary of LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-llm/"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"}]

I found comprehensive benchmark results for Qwen 3 base models. Here are the key scores you're looking for:

## Qwen3-8B Base Model Scores

For general tasks, Qwen3-8B achieves MMLU: 79.66. For math & STEM tasks, it scores GSM8K: 90.22. For coding tasks, it achieves EvalPlus: 60.70.

## Qwen3-14B Base Model Scores

Qwen3-14B-Base achieves MMLU: 81.05, GSM8K: 92.49, and for coding tasks achieves EvalPlus: 72.23.

## Additional Context

For comparison with smaller models, Qwen3-4B-Base achieves MMLU: 74.16, GSM8K: 85.36.

The search results from the official Qwen3 Technical Report show comprehensive benchmark evaluations, though HumanEval scores were not explicitly listed in the comparison tables. The models demonstrate strong performance, particularly in STEM, coding, and reasoning benchmarks, where Qwen3 dense base models surpass Qwen2.5 bas
…[truncated 139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-18T07:12:29.426167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"
  }
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-18T07:12:29.426297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"
  }
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-18T07:12:29.426489+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 2 7B 13B benchmark MMLU HellaSwag ARC results comparison 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 2 7B 13B benchmark MMLU HellaSwag ARC results comparison 2025"
  }
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-18T07:12:29.426622+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 benchmark results MMLU HellaSwag 1B 4B 12B 27B training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 benchmark results MMLU HellaSwag 1B 4B 12B 27B training tokens"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-18T07:12:29.426755+00:00_

Web search results for query: "Mistral Small 3 7B base model huggingface release date 2025 benchmark MMLU"

Links: [{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"Mistral Small 3 | Mistral AI","url":"https://mistral.ai/news/mistral-small-3"},{"title":"unsloth/Mistral-Small-24B-Base-2501-bnb-4bit · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501-bnb-4bit"},{"title":"mistralai/Mistral-7B-v0.1 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-v0.1"},{"title":"Mistral Small 3.1 | Mistral AI","url":"https://mistral.ai/news/mistral-small-3-1"},{"title":"unsloth/Mistral-Small-24B-Base-2501 · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"mistralai/Mistral-Small-24B-Instruct-2501 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501"},{"title":"mistralai/Mistral-Small-3.1-24B-Instruct-2503 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/getting-started/models/benchmark/"}]

Based on the search results, here's what I found about Mistral Small 3:

**Model Details:**
Mistral Small 3 boasts 24B parameters and achieves state-of-the-art capabilities comparable to larger models. Note that the search results do not show a 7B version of Mistral Small 3 - the model has 24 billion parameters, not 7 billion.

**Release Date:**
The model was released in January 2025. The version labeled "2501" (indicating January 2025) is referenced in the HuggingFace documentation.

**MMLU Benchmark:**
Mistral Small 3 achieves over 81% accuracy on MMLU and 150 tokens/s latency, making it currently the most efficient model of its category.

**HuggingFace Availability:**
Mistral Small 3.1 is available to download on the HuggingFace website in both Base 
…[truncated 345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-18T07:12:29.426911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 2 0325 32B base model huggingface release date 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 2 0325 32B base model huggingface release date 2025"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-18T07:12:29.427041+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "google/gemma-3-27b-pt pretrained base model training data tokens gated"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "google/gemma-3-27b-pt pretrained base model training data tokens gated"
  }
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-18T07:12:29.427168+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ministral 3 14B base model HuggingFace \"mistralai/Ministral-3-14B\" benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ministral 3 14B base model HuggingFace \"mistralai/Ministral-3-14B\" benchmark MMLU"
  }
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-18T07:12:29.427292+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3-14B-Base architecture layers attention heads non-embedding parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3-14B-Base architecture layers attention heads non-embedding parameters"
  }
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-18T07:12:29.427519+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 4 Maverick base pretrained HuggingFace \"meta-llama/Llama-4-Maverick\" non-instruct"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 4 Maverick base pretrained HuggingFace \"meta-llama/Llama-4-Maverick\" non-instruct"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-18T07:12:29.427671+00:00_

Web search results for query: "Qwen2.5 7B 14B base model huggingface benchmark training tokens 2024 2025"

Links: [{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen/Qwen2.5-7B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen/Qwen2.5-7B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B"},{"title":"Qwen/Qwen2.5-Coder-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-14B"},{"title":"Qwen/Qwen2.5-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B"},{"title":"Qwen/Qwen2.5-Coder-14B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct"},{"title":"Qwen/Qwen2.5-14B-Instruct-1M · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B-Instruct-1M"},{"title":"Qwen/Qwen2.5-7B-Instruct-1M · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-1M"},{"title":"Qwen/Qwen2.5-14B-Instruct · Hugging Face","url":"https://huggingface.co/Qwen/Qwen2.5-14B-Instruct"}]

Based on the search results, here's information about Qwen2.5 7B and 14B base models:

## Model Overview

Qwen2.5 includes pre-trained and instruction-tuned models of 7 sizes, including 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B.

## Training Tokens

The pre-training data increased from 7 trillion tokens to 18 trillion tokens, with focus on knowledge, coding, and mathematics. For the Qwen2.5-Coder variant, the training tokens were scaled up into 5.5 trillion including source code, text-code grounding, Synthetic data, etc.

## Benchmark Performance

For the 7B model, Qwen2.5-7B demonstrates significant improvements achieving 74.2 on MMLU, 49.8 on MATH, and 57.9 on coding tasks like HumanEval.

The Qwen2.5-7B model surpasses its predecessors and counterparts in numerous b
…[truncated 516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-18T07:12:29.427836+00:00_

Web search results for query: "DeepSeek V2 V3 7B 14B base model huggingface distilled 2025"

Links: [{"title":"deepseek-ai/DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond","url":"https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond"},{"title":"DeepSeek-V2 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/deepseek_v2"},{"title":"DeepSeek-V3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/deepseek_v3"},{"title":"DeepSeek-V3.2 Release | DeepSeek API Docs","url":"https://api-docs.deepseek.com/news/news251201"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"deepseek-ai/DeepSeek-V3-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V3-Base"}]

Based on the search results, here's what I found about DeepSeek models and their distilled variants on Hugging Face:

## DeepSeek-V3 Base Model

DeepSeek-V3 is a strong Mixture-of-Experts (MoE) language model with 671B total parameters with 37B activated for each token. To achieve efficient inference and cost-effective training, DeepSeek-V3 adopts Multi-head Latent Attention (MLA) and DeepSeekMoE architectures, which were thoroughly validated in DeepSeek-V2.

## Distilled Models (2025)

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series to the community. 

Specifically, DeepSeek-R1-Distill-Qwen-1.5B, Deep
…[truncated 609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-18T07:12:29.427995+00:00_

Web search results for query: "OLMo 2 7B 13B base model huggingface 2025 release Allen AI"

Links: [{"title":"OLMo 2 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-2"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"allenai/OLMo-2-1124-13B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-Instruct-GGUF"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"allenai/OLMo-2-1124-7B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B-RM"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"}]

Based on the search results, here's what I found about OLMo 2:

## OLMo 2 Release Overview

OLMo 2 is a new family of 7B and 13B models trained on up to 5T tokens. These models are on par with or better than equivalently-sized fully-open models, and competitive with open-weight models from Meta and Mistral on English academic benchmarks.

## Base Models on Hugging Face

The base models are available on Hugging Face:
- OLMo 2 7B base version is available for use as foundation for post-training.
- OLMo 2 13B base version is available for use as foundation for post-training.

## Training Details

OLMo 2 features a 9-point increase in MMLU compared to the original OLMo 7B model, with these gains coming from training on OLMo-mix-1124 and Dolmino-mix-1124 datasets and staged training approach.

## Performance

OLMo 2 7B outperforms LLama-
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 93 · 2026-05-18T07:12:29.428146+00:00_

Web search results for query: "microsoft/phi-4 HuggingFace benchmark MMLU training data size tokens gated access"

Links: [{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"phi-4 | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/phi-4-microsoft"},{"title":"GitHub - microsoft/MMLU-CF: A Contamination-free Multi-task Language Understanding Benchmark [Official, ACL 2025] · GitHub","url":"https://github.com/microsoft/MMLU-CF"},{"title":"microsoft/Phi-4-multimodal-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-multimodal-instruct"},{"title":"Microsoft AI Just Released Phi-4: A Small Language Model Available on Hugging Face Under the MIT License - MarkTechPost","url":"https://www.marktechpost.com/2025/01/08/microsoft-ai-just-fully-open-sourced-phi-4-a-small-language-model-available-on-hugging-face-under-the-mit-license/"},{"title":"Phi-4: Small Language Models That Pack a Punch | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/phi-4-small-language-models-that-pack-a-punch/4464167"},{"title":"microsoft/phi-4-gguf · Hugging Face","url":"https://huggingface.co/microsoft/phi-4-gguf"}]

Based on the search results, here's what I found about microsoft/phi-4 on HuggingFace:

## MMLU Benchmark Performance
Phi-4 scores 84.8% on MMLU (a broad test of knowledge across 57 subjects), and achieved 84.8% on MMLU, 80.4% on MATH, and 82.6% on HumanEval.

## Training Data Size
Microsoft trained it on 9.8 trillion tokens over three weeks, using a mix of synthetic data (generated by larger models like GPT-4o) a
…[truncated 925 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-18T07:12:29.428300+00:00_

Web search results for query: "DeepSeek-R1-Distill-Qwen-14B DeepSeek-R1-Distill-Qwen-7B HuggingFace base model benchmark"

Links: [{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B"},{"title":"litert-community/DeepSeek-R1-Distill-Qwen-1.5B · Hugging Face","url":"https://huggingface.co/litert-community/DeepSeek-R1-Distill-Qwen-1.5B"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-14B"},{"title":"Mungert/DeepSeek-R1-Distill-Qwen-14B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/DeepSeek-R1-Distill-Qwen-14B-GGUF"},{"title":"stelterlab/DeepSeek-R1-Distill-Qwen-14B-AWQ · Hugging Face","url":"https://huggingface.co/stelterlab/DeepSeek-R1-Distill-Qwen-14B-AWQ"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"unsloth/DeepSeek-R1-Distill-Qwen-32B · Hugging Face","url":"https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B"}]

Based on the search results, here's what I found about the DeepSeek-R1-Distill-Qwen models on HuggingFace:

## Model Overview

DeepSeek has open-sourced distilled 1.5B, 7B, 8B, 14B, 32B, and 70B checkpoints based on Qwen2.5 and Llama3 series.

## Benchmark Performance

The evaluation results demonstrate that the distilled smaller dense models perform exceptionally well on benchmarks. DeepSeek-R1-Distill-Qwen-32B outperforms OpenAI-o1-mini across various benchmarks, achieving new state-of-the-
…[truncated 724 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-18T07:12:29.428547+00:00_

Web search results for query: "DeepSeek-Coder-V2-Lite-Base 16B HuggingFace parameters MoE active benchmark"

Links: [{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"},{"title":"DeepSeek-Coder V2 Lite Instruct","url":"https://www.emergentmind.com/topics/deepseek-coder-v2-lite-instruct"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"deepseek-ai/DeepSeek-V2-Lite · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite"},{"title":"deepseek-ai/deepseek-coder-v2-lite-instruct | Run with an API on Replicate","url":"https://replicate.com/deepseek-ai/deepseek-coder-v2-lite-instruct"},{"title":"deepseek-coder-v2:16b-lite-instruct-fp16","url":"https://ollama.com/library/deepseek-coder-v2:16b-lite-instruct-fp16"},{"title":"DeepSeek-Coder-V2: An Open-Source Marvel in Code Intelligence | by givkashi | Medium","url":"https://medium.com/@givkashi/deepseek-coder-v2-an-open-source-marvel-in-code-intelligence-e8572f7741e0"},{"title":"Model Variants | deepseek-ai/DeepSeek-Coder-V2 | DeepWiki","url":"https://deepwiki.com/deepseek-ai/DeepSeek-Coder-V2/2.1-model-variants"},{"title":"deepseek-coder-v2:16b","url":"https://ollama.com/library/deepseek-coder-v2:16b"}]

Based on the search results, here's the information about DeepSeek-Coder-V2-Lite-Base 16B parameters and MoE active parameters:

## Parameters and MoE Configuration

DeepSeek-Coder-V2-Lite-Base has 16B parameters based on the DeepSeekMoE framework, with only 2.4B active parameters. 

This means that for any given input, the model routes the computation through only about 15% of its total parameters (for Lite variants)
…[truncated 883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-18T07:12:29.428723+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-18T07:12:29.428864+00:00_

Web search results for query: "OLMo 2 0325 32B base model huggingface release date 2025"

Links: [{"title":"allenai/OLMo-2-0325-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct"},{"title":"allenai/OLMo-2-0325-32B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-SFT"},{"title":"allenai/OLMo-2-0325-32B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B"},{"title":"allenai/OLMo-2-0325-32B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-DPO"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"allenai/OLMo-2-0325-32B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct-GGUF"},{"title":"OLMo-2-0325-32B huggingface.co api & allenai OLMo-2-0325-32B github AI Model - Toolify","url":"https://www.toolify.ai/ai-model/allenai-olmo-2-0325-32b"},{"title":"unsloth/OLMo-2-0325-32B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/OLMo-2-0325-32B-Instruct-GGUF"}]

Based on the search results, here's what I found about the OLMo 2 0325 32B base model on Hugging Face:

The OLMo-2-0325-32B base model was released on November 26, 2024. However, the model was last updated on March 26, 2025.

The search results show that OLMo 2 32B is the largest model in the OLMo 2 family, scaling up the OLMo 2 training recipe used for the 7B and 13B models released in November. Trained up to 6T tokens and post-trained using Tulu 3.1, it is the first fully-open model to outperform GPT3.5-Turbo and GPT-4o mini on a suite of popular, multi-skill academic benchmarks.

The model is available on Hugging Face under the repository name `allenai/OLMo-2-0325-32B`.


REMINDER: You MUST includ
…[truncated 75 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-18T07:12:29.429015+00:00_

Web search results for query: "Qwen3-14B-Base architecture layers attention heads non-embedding parameters"

Links: [{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen3 14B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-14b/"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-14B-Base Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/qwen-qwen3-14b-base-free-chat-online-skywork-ai/"},{"title":"unsloth/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-14B-Base"},{"title":"Qwen3 14B Base API | Together AI","url":"https://www.together.ai/models/qwen3-14b-base"},{"title":"Qwen3-14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-14b"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Unpacking Qwen 3: Architecture, Capabilities, and Performance | by Erik Milošević | Towards AGI | Medium","url":"https://medium.com/towards-agi/unpacking-qwen-3-architecture-capabilities-and-performance-a87f6b317f72"},{"title":"Qwen/Qwen3-14B - Demo - DeepInfra","url":"https://deepinfra.com/Qwen/Qwen3-14B"}]

Based on the search results, here are the architecture specifications for **Qwen3-14B-Base**:

**Architecture Layers & Attention:**
- Number of Layers: 40
- Number of Attention Heads (GQA): 40 for Q and 8 for KV

**Parameter Details:**
- Total Number of Parameters: 14.8B
- Non-Embedding Parameters: 13.2B

**Additional Architectural Features:**
- The model employs a dense, causal transformer architecture with grouped query attention (GQA)
- The model employs SwiGLU activation functions and RMSNorm with pre-normalization for enhanced training stability
- Context Length: 32,768


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-18T07:12:29.429172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 12B base pretrained benchmark scores MMLU 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 12B base pretrained benchmark scores MMLU 2025"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-18T07:12:29.429332+00:00_

Web search results for query: "Gemma 3 benchmark results MMLU HellaSwag 1B 4B 12B 27B training tokens"

Links: [{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 Model: Multimodal & Efficient LLM","url":"https://www.emergentmind.com/topics/gemma-3-model"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"GitHub - heilcheng/openevals: Benchmarking suite for open-weight language models · GitHub","url":"https://github.com/heilcheng/gemma-benchmark"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 27B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-27b"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"}]

Based on the search results, here's comprehensive information about Gemma 3 benchmark results:

## Training Tokens

The 27B model was trained with 14 trillion tokens, the 12B model was trained with 12 trillion tokens, 4B model was trained with 4 trillion tokens, the 1B with 2 trillion tokens, and the 270M with 6 trillion tokens.

## HellaSwag Benchmark Results

For HellaSwag, the Gemma 3 models achieved the following scores: 1B: 62.3, 4B: 77.2, 12B: 84.2, and 27B: 85.6

## MMLU Benchmark Results

For MMLU-Pro specifically, Gemma 3-27B-IT yields 67.5% versus Gemini 2.0-Pro's 79.1% and Gemma 2-27B-IT's 56.9%

## Overall Performance

The Gemma 3 models are traine
…[truncated 471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-18T07:12:29.429499+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 3.3 8B base model huggingface release 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 3.3 8B base model huggingface release 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-18T07:12:29.429636+00:00_

Web search results for query: "Ministral 3 14B base model HuggingFace "mistralai/Ministral-3-14B" benchmark MMLU"

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"mistralai/Ministral-3-14B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512"},{"title":"mistralai / ministral-14b-instruct-2512","url":"https://docs.api.nvidia.com/nim/reference/mistralai-ministral-14b-instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"unsloth/Ministral-3-14B-Reasoning-2512-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Ministral-3-14B-Reasoning-2512-GGUF"},{"title":"README.md · mistralai/Ministral-3-14B-Base-2512 at main","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512/blob/main/README.md"},{"title":"RedHatAI/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/RedHatAI/Ministral-3-14B-Instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-BF16"},{"title":"unsloth/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/unsloth/Ministral-3-14B-Base-2512"},{"title":"mistralai/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512"}]

Based on the web search results, here's information about the Ministral 3 14B base model and its MMLU benchmark performance:

## Model Overview
The largest model in the Ministral 3 family, Ministral 3 14B offers frontier capabilities and performance comparable to its larger Mistral Small 3.2 24B counterpart, and is a powerful and efficient language model with vision capabilities.

## MMLU Benchmark
The model was evaluated on MMLU and MMLU-Redux benchmarks as part of comprehensive evaluation efforts. The research paper indicates that res
…[truncated 768 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-18T07:12:29.429788+00:00_

Web search results for query: "google/gemma-3-27b-pt pretrained base model training data tokens gated"

Links: [{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-27b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-pt"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"eramax/gemma-3-27b-it-qat:q4_0","url":"https://ollama.com/eramax/gemma-3-27b-it-qat:q4_0"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"eramax/gemma-3-27b-it-qat","url":"https://ollama.com/eramax/gemma-3-27b-it-qat"},{"title":"Full Model Fine-Tune using Hugging Face Transformers | Gemma | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/huggingface_text_full_finetune"},{"title":"google/gemma-3-1b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-1b-pt"},{"title":"google/gemma-3-27b • LM Studio","url":"https://lmstudio.ai/models/google/gemma-3-27b"}]

Based on the search results, here's the information about the google/gemma-3-27b-pt pretrained base model:

## Training Data Tokens

The 27B model was trained with 14 trillion tokens.

## Gated Access

To access Gemma on Hugging Face, you're required to review and agree to Google's usage license. To do this, please ensure you're logged in to Hugging Face and click below. Requests are processed immediately.

## Model Details

Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

The model was trained on a div
…[truncated 335 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-18T07:12:29.429944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Falcon 3 7B 10B base model huggingface 2024 2025 TII"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Falcon 3 7B 10B base model huggingface 2024 2025 TII"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-18T07:12:29.430082+00:00_

Web search results for query: "OLMo 2 7B 13B benchmark MMLU HellaSwag ARC results comparison 2025"

Links: [{"title":"OLMo 2: Advancing True Open-Source Language Models – The AI Observer","url":"https://www.theaiobserver.com/olmo-2-advancing-true-open-source-language-models/"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"Comparative Analysis of Mistral 7B and OLMo2 7B on the Ollama Platform","url":"https://matasoft.hr/qtrendcontrol/index.php/un-perplexed-spready/un-perplexed-spready-various-articles/146-comparative-analysis-of-mistral-7b-and-olmo2-7b-on-the-ollama-platform"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"OLMo-2-1124-13B & 7B · Issue #7863 · ollama/ollama","url":"https://github.com/ollama/ollama/issues/7863"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | Ai2","url":"https://allenai.org/blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"HellaSwag Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/hellaswag"},{"title":"GitHub - heilcheng/openevals: Benchmarking suite for open-weight language models · GitHub","url":"https://github.com/heilcheng/gemma-benchmark"}]

Based on the web search results, here's what I found about OLMo 2 benchmark results for MMLU, HellaSwag, and ARC:

## OLMo 2 Benchmark Results

### MMLU Performance
OLMo 2 achieved 63.7 for the 7B model and 67.5 for the 13B model on MMLU. OLMo 2 features a 9-point increase in MMLU compared to the original OLMo 7B model.

### General Performance Comparison
The 7B version of OLMo 2 notably outperforms Meta's Llama 3.1 8B on several English academic benchmarks, while the 13B version surpasses Qwen 2.5 7B, des
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-18T07:12:29.430231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "InternLM3 8B base model huggingface 2025 Shanghai AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "InternLM3 8B base model huggingface 2025 Shanghai AI"
  }
}
```

</details>

---

### Tool result

_source line 107 · 2026-05-18T07:12:29.430389+00:00_

Web search results for query: "Llama 4 Maverick base pretrained HuggingFace "meta-llama/Llama-4-Maverick" non-instruct"

Links: [{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Original · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Original"},{"title":"unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Llama-4-Maverick-17B-128E-Instruct-GGUF"},{"title":"meta-llama/Llama-4-Maverick-17B-128E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"},{"title":"RedHatAI/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/RedHatAI/Llama-4-Maverick-17B-128E-Instruct"},{"title":"future-technologies/FineTuned-Meta-Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/future-technologies/FineTuned-Meta-Llama-4-Maverick-17B-128E-Instruct"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"}]

Based on the search results, here's what I found about the Llama 4 Maverick base pretrained model on HuggingFace:

## Model Details

Llama 4 Maverick is a 17 billion parameter model with 128 experts. The model is available on HuggingFace under the meta-llama organization.

## Available Variants

Both Llama 4 Maverick and Llama 4 Scout model weights are available directly on the Hugging Face Hub under the meta-llama organization
…[truncated 939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-18T07:12:29.430549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-18T07:12:29.430684+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"
  }
}
```

</details>

---

### Tool call

_source line 110 · 2026-05-18T07:12:29.430809+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 2 7B 13B MMLU ARC HellaSwag exact scores table arxiv 2501.00656"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 2 7B 13B MMLU ARC HellaSwag exact scores table arxiv 2501.00656"
  }
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-18T07:12:29.430940+00:00_

Web search results for query: "Qwen3 8B base benchmark MMLU ARC HellaSwag scores 2025"

Links: [{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"An empirical study of Qwen3 quantization | Visual Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44267-026-00114-4"},{"title":"eaddario/Qwen3-8B-GGUF · Hugging Face","url":"https://huggingface.co/eaddario/Qwen3-8B-GGUF"},{"title":"Swallow LLM Leaderboard","url":"https://swallow-llm.github.io/leaderboard/about.en.html"},{"title":"Top LLM Benchmarks Explained: MMLU, HellaSwag, BBH, and Beyond - Confident AI","url":"https://www.confident-ai.com/blog/llm-benchmarks-mmlu-hellaswag-and-beyond"},{"title":"LLM Benchmarks Compared: MMLU, HumanEval, GSM8K and More (2026)","url":"https://www.lxt.ai/blog/llm-benchmarks/"},{"title":"We Benchmarked 12 Small Language Models Across 8 Tasks to Find the Best Base Model for Fine-Tuning — distil labs","url":"https://www.distillabs.ai/blog/we-benchmarked-12-small-language-models-across-8-tasks-to-find-the-best-base-model-for-fine-tuning/"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"Qwen3 8B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-8b-instruct"},{"title":"LLM Benchmark Wars 2025–2026: Performance, Cost, Speed, and Value | RankSaga","url":"https://ranksaga.com/blog/llm-benchmark-wars-2025-2026/"}]

Based on the search results, I found relevant benchmark information about Qwen3-8B-Base. Here's what I found:

Qwen-8B's MMLU score is 74.7 in its full precision form, though this appears to be from a quantization study focused on performance degradation at lower bit widths.

The search results include detailed benchmark data from an empirical study of Qwen3 quantization published in early 2025. Zero-shot accuracy is evaluated across reasoning benchmarks including ARC-Easy, ARC-C
…[truncated 654 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 112 · 2026-05-18T07:12:29.431093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"
  }
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-18T07:12:29.431224+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "allenai OLMo-2-0425-1B base model training tokens release April 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "allenai OLMo-2-0425-1B base model training tokens release April 2025"
  }
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-18T07:12:29.431386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ministral 3 8B 14B base benchmark MMLU scores comparison Qwen3 December 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ministral 3 8B 14B base benchmark MMLU scores comparison Qwen3 December 2025"
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-18T07:12:29.431526+00:00_

Web search results for query: "Gemma 3 12B base pretrained benchmark scores MMLU 2025"

Links: [{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google: Gemma 3 12B Review | Pricing, Benchmarks & Capabilities (2026) | Design for Online","url":"https://designforonline.com/ai-models/google-gemma-3-12b/"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"LLM Benchmarks March 2025","url":"https://www.timetoact-group.at/en/insights/llm-benchmarks/llm-benchmarks-march-2025"}]

Based on the search results, I found benchmark information for Gemma 3 12B, though the specific MMLU score for the base pretrained model wasn't directly listed in these results. Here's what I found:

**Gemma 3 12B Benchmark Performance:**

For the Gemma 3 12B model, MMLU-Pro shows a score of 59.5%. This is from the instruction-tuned (IT) variant.

The search results primarily focus on the instruction-tuned (IT) versions of Gemma 3 rather than the base pretrained models. Gemma 3 has been evaluated across benchmarks like MMLU-Pro (27B: 67.5), but specific base model MMLU scores for the 12B variant were not included in the available search results.

For contex
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-18T07:12:29.431684+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 1B 4B 12B 27B MMLU exact score pretrained base model benchmark table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 1B 4B 12B 27B MMLU exact score pretrained base model benchmark table"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-18T07:12:29.431813+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ministral 3 3B 8B 14B base model context length architecture layers gated access"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ministral 3 3B 8B 14B base model context length architecture layers gated access"
  }
}
```

</details>

---

### Tool result

_source line 118 · 2026-05-18T07:12:29.431944+00:00_

Web search results for query: "Llama 3.3 8B base model huggingface release 2024 2025"

Links: [{"title":"meta-llama/Llama-3.1-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.1-8B"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"meta-llama/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Meta-Llama-3-8B"},{"title":"meta-llama/Llama-3.2-3B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B"},{"title":"NousResearch/Meta-Llama-3-8B · Hugging Face","url":"https://huggingface.co/NousResearch/Meta-Llama-3-8B"},{"title":"meta-llama/Llama-3.2-3B-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"},{"title":"meta-llama/Llama-3.3-70B-Instruct · Release of an 8B model?","url":"https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct/discussions/11"},{"title":"nvidia/Llama-3.1-8B-Instruct-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Llama-3.1-8B-Instruct-NVFP4"},{"title":"meta-llama/Llama-Guard-3-8B · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-Guard-3-8B"},{"title":"QuantFactory/Meta-Llama-3-8B-GGUF · Hugging Face","url":"https://huggingface.co/QuantFactory/Meta-Llama-3-8B-GGUF"}]

Based on the search results, here's what I found regarding Llama 3.3 8B base model on Hugging Face:

Llama 3.3 is mentioned in Meta's Hugging Face collection, with the 71B model being updated on December 21, 2024. However, the search results indicate that as of late 2024, users were waiting for an 8B model release.

The Llama 3.3 8B Instruct model became available through third-party APIs (like OpenRouter) in mid-2025, but based on the search results provided, there is no direct mention of an official Llama 3.3 8B base model being released on Hugging Face's main meta-llama repository during 2024-2025.

The search results primarily show information about:
- Llama 3.1 8B released July 23, 2024
- Llama 3 8B released April 18, 2024
- L
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-18T07:12:29.432103+00:00_

Web search results for query: "InternLM3 8B base model huggingface 2025 Shanghai AI"

Links: [{"title":"GitHub - InternLM/InternLM: Official release of InternLM series (InternLM, InternLM2, InternLM2.5, InternLM3). · GitHub","url":"https://github.com/InternLM/InternLM"},{"title":"internlm/internlm3-8b-instruct · Hugging Face","url":"https://huggingface.co/internlm/internlm3-8b-instruct"},{"title":"InternLM3 Open Source: Achieving High-Performance Models with 4T Data | by OpenMMLab | Medium","url":"https://openmmlab.medium.com/internlm3-open-source-achieving-high-performance-models-with-4t-data-c18e94bd5c6a"},{"title":"internlm/internlm3-8b-instruct-gguf · Hugging Face","url":"https://huggingface.co/internlm/internlm3-8b-instruct-gguf"},{"title":"internlm (Intern Large Models)","url":"https://huggingface.co/internlm"},{"title":"InternLM3 - a internlm Collection","url":"https://huggingface.co/collections/internlm/internlm3"},{"title":"Internlm3 8b Instruct - a Hugging Face Space by internlm","url":"https://huggingface.co/spaces/internlm/internlm3-8b-instruct"},{"title":"HuggingFace Transformers 😊 — InternLM","url":"https://internlm.readthedocs.io/en/latest/inference/huggingface_transformers.html"},{"title":"internlm3-8b-instruct | AI Model Details","url":"https://www.aimodels.fyi/models/huggingFace/internlm3-8b-instruct-internlm"},{"title":"Intern-ai","url":"https://internlm.intern-ai.org.cn/"}]

Based on the search results, here's what I found about InternLM3 8B:

## Overview

InternLM3 has open-sourced an 8-billion parameter instruction model, InternLM3-8B-Instruct, designed for general-purpose usage and advanced reasoning. InternLM is a conversational language model that is developed by Shanghai AI Laboratory.

## Release Date

On January 15, Shanghai AI Lab announced a major upgrade to the InternLM model with the release of InternLM3.

## Key Features

InternLM3 offers state-of-the-art performance on reasoning and knowledge-intensive tasks surpassing models like L
…[truncated 681 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-18T07:12:29.432273+00:00_

Web search results for query: "Falcon 3 7B 10B base model huggingface 2024 2025 TII"

Links: [{"title":"tiiuae/Falcon3-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Base"},{"title":"Welcome to the Falcon 3 Family of Open Models!","url":"https://huggingface.co/blog/falcon3"},{"title":"tiiuae/Falcon3-10B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-10B-Base"},{"title":"TII launches world’s most powerful SLMs under 13B parameters","url":"https://www.middleeastainews.com/p/tii-launches-most-powerful-slm"},{"title":"Falcon 3: UAE’s Technology Innovation Institute Launches World’s most Powerful Small AI Models that can also be run on Light Infrastructures, including Laptops | Technology Innovation Institute","url":"https://www.tii.ae/news/falcon-3-uaes-technology-innovation-institute-launches-worlds-most-powerful-small-ai-models"},{"title":"tiiuae/Falcon3-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Instruct"},{"title":"tiiuae/Falcon3-10B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-10B-Instruct"},{"title":"Technology Innovation Institute TII-UAE Just Released Falcon 3: A Family of Open-Source AI Models with 30 New Model Checkpoints from 1B to 10B - MarkTechPost","url":"https://www.marktechpost.com/2024/12/17/technology-innovation-institute-tii-uae-just-released-falcon-3-a-family-of-open-source-ai-models-with-30-new-model-checkpoints-from-1b-to-10b/"},{"title":"tiiuae/Falcon3-3B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-3B-Base"},{"title":"tiiuae/Falcon3-Mamba-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-Mamba-7B-Instruct"}]

Based on the search results, here's what I found about Falcon 3 models:

## Overview

Falcon3 is a family of decoder-only large language models under 10 billion parameters, developed by Technology Innovation Institute (TII) in Abu Dhabi. The Falcon 3 family of Open Foundation Models was released in
…[truncated 1299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-18T07:12:29.432473+00:00_

Web search results for query: "DeepSeek-R1-Distill-Qwen-14B benchmark MMLU MATH AIME pass@1 scores"

Links: [{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/deepseek-r1"},{"title":"deepseek-ai/DeepSeek-R1 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1-Distill-Qwen-14B - Model Info, Parameters, Benchmarks - SiliconFlow\"","url":"https://www.siliconflow.com/models/deepseek-r1-distill-qwen-14b"},{"title":"DeepSeek R1 Distill Qwen 14B: Pricing, Benchmarks & Performance","url":"https://llm-stats.com/models/deepseek-r1-distill-qwen-14b"},{"title":"DeepSeek-R1: Features, o1 Comparison, Distilled Models & More | DataCamp","url":"https://www.datacamp.com/blog/deepseek-r1"},{"title":"Deployment-ready reasoning with quantized DeepSeek-R1 models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/03/03/deployment-ready-reasoning-quantized-deepseek-r1-models"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-7B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"},{"title":"How to Benchmark DeepSeek-R1 Distilled Models on GPQA Using Ollama and OpenAI’s simple-evals | Towards Data Science","url":"https://towardsdatascience.com/how-to-benchmark-deepseek-r1-distilled-models-on-gpqa-using-ollama-and-openais-simple-evals/"},{"title":"deepseek-ai/DeepSeek-R1-Distill-Qwen-14B · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"}]

Based on the search results, I found benchmark scores for DeepSeek-R1-Distill-Qwen-14B:

## Benchmark Scores for DeepSeek-R1-Distill-Qwen-14B (Pass@1)

**AIME 2024:** 69.7% pass rate

**MATH-500:** 93.9% accuracy

**MMLU:** The search results do not contain specific MMLU pass@1 scores for the 14B distilled model specifically. However, DeepSeek-R1 (t
…[truncated 316 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-18T07:12:29.432685+00:00_

Web search results for query: "OLMo 2 7B 13B MMLU ARC HellaSwag exact scores table arxiv 2501.00656"

Links: [{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"[2501.00656] 2 OLMo 2 Furious","url":"https://arxiv.org/abs/2501.00656"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"allenai/OLMo-2-1124-13B-RM · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B-RM"},{"title":"allenai/OLMo-2-1124-13B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-13B"},{"title":"eaddario/OLMo-2-1124-7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/eaddario/OLMo-2-1124-7B-Instruct-GGUF"},{"title":"OLMoE: Open Mixture-of-Experts Language Models","url":"https://arxiv.org/html/2409.02060v1"},{"title":"allenai/OLMo-2-0325-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0325-32B-Instruct"},{"title":"GitHub - allenai/OLMo: Modeling, training, eval, and inference code for OLMo · GitHub","url":"https://github.com/allenai/OLMo"}]

I found information about OLMo 2 from arxiv paper 2501.00656. The search results include some benchmark scores, though the complete table with all the exact scores you're looking for may require viewing the full PDF directly.

Based on the search results, here are the scores I found:

For OLMo 2 7B and 13B models, the scores improved as follows: ARC: 80.2 → 83.5 for 13B; MMLU: 59.8 → 63.7 for 7B, 63.4 → 67.5 for 13B.

The search results also indicate that HellaSwag scores improved, along with reading comprehension and math skills benchmarks, though the specific HellaSwag scores aren't explicitly listed in the excerpts I retrieved.

For the most complete and detailed table of exact scores for MMLU, ARC, HellaSwag, and other benchmarks for b
…[truncated 281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-18T07:12:29.432854+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MAP-Neo 7B base model huggingface 2025 fully open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MAP-Neo 7B base model huggingface 2025 fully open source"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-18T07:12:29.432995+00:00_

Web search results for query: "allenai OLMo-2-0425-1B base model training tokens release April 2025"

Links: [{"title":"GitHub - allenai/OLMo: Modeling, training, eval, and inference code for OLMo · GitHub","url":"https://github.com/allenai/OLMo"},{"title":"allenai/OLMo-2-0425-1B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B"},{"title":"allenai/OLMo-2-0425-1B-early-training · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-early-training"},{"title":"allenai/OLMo-2-0425-1B-DPO · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-DPO"},{"title":"allenai/OLMo-2-0425-1B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-Instruct"},{"title":"allenai/OLMo-2-0425-1B-SFT · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-0425-1B-SFT"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"OLMo-2-0425-1B-SFT huggingface.co api & allenai OLMo-2-0425-1B-SFT github AI Model - Toolify","url":"https://www.toolify.ai/ai-model/allenai-olmo-2-0425-1b-sft"},{"title":"Olmo from Ai2","url":"https://allenai.org/olmo"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"}]

Based on the search results, here's what I found about the Allen AI OLMo-2-0425-1B base model:

## Training Tokens

For the 1B model, the model was trained on 50B high quality tokens. However, this represents only the primary training run. OLMo 2 1B is pretrained on 4T tokens of high-quality data, specifically using the OLMo-mix-1124 as well as Dolmino-mix-1124 for mid-training.

## Model Architecture and Training Approach

The 1B model was trained three times with different data order on 50B high quality tokens, with the last checkpoint of seed 42 used as the final checkpoint.

## Release Date

The model naming follows Allen AI's updated convention. The OLMo naming convention was updated to include the model name, model version, mod
…[truncated 391 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-18T07:12:29.433150+00:00_

Web search results for query: "Phi-4 mini 3.8B base pretrained model HuggingFace release date benchmark"

Links: [{"title":"microsoft/Phi-4-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-instruct"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"unsloth/Phi-4-mini-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-mini-reasoning-GGUF"},{"title":"Phi-4 Mini: Microsoft's Best Small Model (3.8B) — Guide & Benchmarks | Local AI Master","url":"https://localaimaster.com/models/phi-4-mini"},{"title":"microsoft/Phi-3-mini-4k-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3-mini-4k-instruct"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"unsloth/Phi-4-mini-instruct-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF"},{"title":"microsoft/Phi-3.5-mini-instruct · Hugging Face","url":"https://huggingface.co/microsoft/Phi-3.5-mini-instruct"},{"title":"Mungert/Phi-4-mini-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Phi-4-mini-reasoning-GGUF"}]

Based on the search results, here's the information about Phi-4 mini 3.8B:

## Release Information

Phi-4 (microsoft/phi-4 on HuggingFace) is the December 2024 release of Microsoft's Phi family. More specifically, Phi-4 Mini was published on March 19, 2026, representing a later update to the Phi-4 family.

## Base Model Availability

The search results primarily show instruct and reasoning variants of Phi-4-mini rather than explicit base pretrained models. However, the 3.8B parameters Phi-4-mini-instruct model was compared with a set of models over a variety of benchmarks using an internal
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-18T07:12:29.433306+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolLM2 7B base model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolLM2 7B base model huggingface 2025"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-18T07:12:29.433467+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phi-4 14B MMLU benchmark score base model december 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phi-4 14B MMLU benchmark score base model december 2024"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-18T07:12:29.433605+00:00_

Web search results for query: "Ministral 3 3B 8B 14B base model context length architecture layers gated access"

Links: [{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Ministral 3 — Megatron Bridge","url":"https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/vlm/ministral3.html"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"Ministral 3","url":"https://arxiv.org/html/2601.08584v1"},{"title":"mistralai / ministral-14b-instruct-2512","url":"https://docs.api.nvidia.com/nim/reference/mistralai-ministral-14b-instruct-2512"},{"title":"Ministral 3 14B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/ministral-3-14b"},{"title":"Mistral 3 14B Reasoning 2512: Comprehensive Review, Features, and Performance Insights - GenAI Content","url":"https://www.genaicontent.org/news/mistral-3-14b-review-features-performance"},{"title":"Ministral 3 | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.08584"},{"title":"Ministral 3 - How to Run Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/models/tutorials/ministral-3"}]

Based on the search results, here is comprehensive information about Ministral 3:

## Model Sizes and Variants

The Ministral 3 series is available in three model sizes: 3B, 8B, and 14B parameters, with base, instruct, and reasoning variants available for each size, each with image understanding capabilities and all under the Apache 2.0 license.

## Architecture and Layers

The family consists of three sizes: 3B, 8B, and 14B parameters, with 26, 34, and 40 layers respectively.

More detailed architecture specifications:

- **Ministral 3 3B:** 3.4B parameter vision-language model with 26 layers, 3072 hidden size, 32 attention heads, and 8 query groups (GQA)
- **Ministral 3 8B:** 8.4B parameter vis
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-18T07:12:29.433754+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yi-1.5 9B base model huggingface 01.AI 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yi-1.5 9B base model huggingface 01.AI 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 130 · 2026-05-18T07:12:29.433884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mistral Nemo 12B base model huggingface 2024 benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mistral Nemo 12B base model huggingface 2024 benchmark"
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-18T07:12:29.434020+00:00_

Web search results for query: "Ministral 3 8B 14B base benchmark MMLU scores comparison Qwen3 December 2025"

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Ministral 3 (14B Reasoning 2512) vs Qwen3 VL 8B Thinking Comparison","url":"https://llm-stats.com/models/compare/ministral-14b-latest-vs-qwen3-vl-8b-thinking"},{"title":"Ministral 3 (14B Reasoning 2512) vs Qwen3.5-9B Comparison","url":"https://llm-stats.com/models/compare/ministral-14b-latest-vs-qwen3.5-9b"},{"title":"Ministral 3 (14B Base 2512) vs Qwen3 VL 30B A3B Thinking Comparison","url":"https://llm-stats.com/models/compare/ministral-3-14b-base-2512-vs-qwen3-vl-30b-a3b-thinking"},{"title":"Ministral 3 (14B Reasoning 2512) vs Qwen3 VL 30B A3B Thinking Comparison","url":"https://llm-stats.com/models/compare/ministral-14b-latest-vs-qwen3-vl-30b-a3b-thinking"},{"title":"Ministral 3 vs Others: Accuracy, Token Efficiency, and the Best Model per Budget","url":"https://kaitchup.substack.com/p/ministral-3-vs-others-accuracy-token"},{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"Ministral 3 (3B Instruct 2512) vs Qwen3.5-2B Comparison","url":"https://llm-stats.com/models/compare/ministral-3-3b-instruct-2512-vs-qwen3.5-2b"},{"title":"MiniStral 3 (14B Instruct 2512) vs Qwen3.5-0.8B Comparison","url":"https://llm-stats.com/models/compare/ministral-3-14b-instruct-2512-vs-qwen3.5-0.8b"},{"title":"Ministral 3 (8B Instruct 2512) vs Qwen3 VL 8B Thinking Comparison: Benchmarks, Pricing & Performance","url":"https://llm-stats.com/models/compare/ministral-3-8b-instruct-2512-vs-qwen3-vl-8b-thinking"}]

Based on the search results, here's information about Ministral 3 and Qwen3 base model benchmark comparisons:

## Base Model MMLU Scores

Ministral 3 (14B Base) scores MMLU at 79.4%, while Qwen3 VL 30B A3B Thinking scores MMLU at 87.6%.

Ministral 3 (14B Base) also scores MMLU-Redux at 82.0%.

## Model Variants and Release Infor
…[truncated 682 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-18T07:12:29.434181+00:00_

Web search results for query: "Gemma 3 1B 4B 12B 27B MMLU exact score pretrained base model benchmark table"

Links: [{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Gemma 3 model card | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core/model_card_3"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Gemma 3 Technical Report","url":"https://arxiv.org/html/2503.19786v1"},{"title":"Gemma 3 Model: Multimodal & Efficient LLM","url":"https://www.emergentmind.com/topics/gemma-3-model"},{"title":"Gemma-3 LLMs: Multimodal DeepMind Models","url":"https://www.emergentmind.com/topics/gemma-3-models"},{"title":"Announcing Gemma 3n preview: powerful, efficient, mobile-first AI - Google Developers Blog","url":"https://developers.googleblog.com/en/introducing-gemma-3n/"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"GitHub - heilcheng/openevals: Benchmarking suite for open-weight language models · GitHub","url":"https://github.com/heilcheng/gemma-benchmark"}]

Based on the search results, I found some MMLU benchmark information for Gemma 3 models, though the results mention MMLU-Pro rather than standard MMLU. Let me search more specifically for the standard MMLU scores across all model sizes.

Links: [{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"(PDF) Gemma 3 Technical Report","url":"https://www.researchgate.net/publication/390175982_Gemma_3_Technical_Report"},{"title":"Google Gemma 4: A Te
…[truncated 2704 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-18T07:12:29.434359+00:00_

Web search results for query: "open source base LLM 7B 8B 14B released 2025 2026 Qwen Llama Gemma Mistral"

Links: [{"title":"Best Open-Source LLM Models in 2026: Coding, Local, Agentic AI, Benchmarks, and License","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Open-Source LLMs in 2026 - Featherless","url":"https://featherless.ai/blog/best-open-source-llms-2026"},{"title":"Best Open Source LLMs in 2026: DeepSeek, Llama & More","url":"https://www.miniloop.ai/blog/best-open-source-llms-2026"},{"title":"Open-Source LLM Landscape 2026, 15+ Model Families Mapped | Presenc AI","url":"https://presenc.ai/research/open-source-llm-landscape-2026"},{"title":"Open-Source LLM Landscape 2026: DeepSeek V4 vs Llama 4 vs Qwen 3.5 vs Gemma 4","url":"https://codersera.com/blog/open-source-llms-landscape-2026/"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open-Source LLM 2026: 8 Tested, 3 Beat GPT-4 | TECHSY","url":"https://techsy.io/en/blog/best-open-source-llms-2026"},{"title":"library","url":"https://ollama.com/library"},{"title":"Open Source LLM Comparison Table (2026) | ComputingForGeeks","url":"https://computingforgeeks.com/open-source-llm-comparison/"}]

Based on the search results, here's a comprehensive overview of open source base LLMs in the 7B-14B range released in 2025-2026 from the major providers you mentioned:

## Qwen
Qwen 3.5 (released February 2026) is a native vision-language model with 397B total parameters (17B active per pass), supporting 201 languages and offering a 1M token context window. The Qwen 3 family also includes smaller variants (32B, 14B, 8B, 4B) that run on consumer hardware. Qwen3 is a strong fit when you need multilingual support, commercial flexibility, and a broad eco
…[truncated 1576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-18T07:12:29.434519+00:00_

Web search results for query: "Phi-4 14B MMLU benchmark score base model december 2024"

Links: [{"title":"Qwen3.5-27B vs Phi-4: When Twice the Parameters Is Not Twice as Obvious | Awesome Agents","url":"https://awesomeagents.ai/tools/qwen-3-5-27b-vs-phi-4/"},{"title":"Microsoft PHI-4: A 14B Parameter Model That Rivals Models 5x Its Size - Developers Digest","url":"https://www.developersdigest.tech/blog/microsoft-phi-4-guide"},{"title":"Phi-4: Small Language Models That Pack a Punch | Microsoft Community Hub","url":"https://techcommunity.microsoft.com/blog/educatordeveloperblog/phi-4-small-language-models-that-pack-a-punch/4464167"},{"title":"Microsoft releases full Phi-4 model with weights under MIT license","url":"https://the-decoder.com/microsoft-releases-full-phi-4-model-with-weights-under-mit-license/"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"Phi-4 Technical Report","url":"https://arxiv.org/html/2412.08905v1"},{"title":"Phi-4 - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/phi-4"},{"title":"Phi 4 by Microsoft: Complete Performance Review & Benchmarks (2025)","url":"https://airank.dev/models/phi-4"},{"title":"microsoft/phi-4 · Hugging Face","url":"https://huggingface.co/microsoft/phi-4"},{"title":"Phi-4","url":"https://ai.azure.com/catalog/models/Phi-4"}]

Based on the search results, here is the MMLU benchmark score for Phi-4 14B base model from December 2024:

On MMLU (a broad test of knowledge across 57 subjects), Phi-4 scores 84.8%. Microsoft released Phi-4 in December 2024, and this MMLU score of 84.8 puts Phi-4 ahead of Llama-3.3-70B on the same evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-18T07:12:29.434675+00:00_

Web search results for query: "SmolLM2 7B base model huggingface 2025"

Links: [{"title":"HuggingFaceTB/SmolLM2-1.7B · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-GGUF"},{"title":"SmolLM2 - a HuggingFaceTB Collection","url":"https://huggingface.co/collections/HuggingFaceTB/smollm2"},{"title":"tensorblock/SmolLM2-1.7B-GGUF · Hugging Face","url":"https://huggingface.co/tensorblock/SmolLM2-1.7B-GGUF"},{"title":"HuggingFaceTB/SmolLM2-1.7B-Instruct-16k · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct-16k"},{"title":"HuggingFaceTB/SmolLM2-135M · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolLM2-135M"},{"title":"bartowski/SmolLM2-1.7B-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/SmolLM2-1.7B-Instruct-GGUF"},{"title":"GitHub - huggingface/smollm: Everything about the SmolLM and SmolVLM family of models · GitHub","url":"https://github.com/huggingface/smollm"},{"title":"HuggingFaceTB/SmolVLM-Instruct · Hugging Face","url":"https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct"}]

Based on the search results, here's what I found about SmolLM2 models:

## Overview

SmolLM2 is a family of compact language models available in three sizes: 135M, 360M, and 1.7B parameters. Note that there isn't a 7B variant in the SmolLM2 family—the largest model is 1.7B.

## Base Model Details

These models are capable of solving a wide range of tasks while being lightweight enough to run on-device. The 1.7B variant demonstrates significant advances over its predecessor SmolLM1-1.7B, particularly in instruction following, knowledge, reasoning, and mathematics. It was trained on 11 trillion tokens using a diverse dataset combination: FineW
…[truncated 598 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-18T07:12:29.434827+00:00_

Web search results for query: "MAP-Neo 7B base model huggingface 2025 fully open source"

Links: [{"title":"m-a-p/neo_7b · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b"},{"title":"Paper page - MAP-Neo: Highly Capable and Transparent Bilingual Large \nLanguage Model Series","url":"https://huggingface.co/papers/2405.19327"},{"title":"GitHub - multimodal-art-projection/MAP-NEO · GitHub","url":"https://github.com/multimodal-art-projection/MAP-NEO"},{"title":"m-a-p/neo_7b_instruct_v0.1 · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b_instruct_v0.1"},{"title":"m-a-p/neo_7b_sft_v0.1 · Hugging Face","url":"https://huggingface.co/m-a-p/neo_7b_sft_v0.1"},{"title":"MAP-NEO/README.md at main · multimodal-art-projection/MAP-NEO","url":"https://github.com/multimodal-art-projection/MAP-NEO/blob/main/README.md"},{"title":"GitHub - huggingface/open-r1: Fully open reproduction of DeepSeek-R1 · GitHub","url":"https://github.com/huggingface/open-r1"},{"title":"nvidia/OpenMath-Nemotron-7B · Hugging Face","url":"https://huggingface.co/nvidia/OpenMath-Nemotron-7B"},{"title":"neulab/Pangea-7B · Hugging Face","url":"https://huggingface.co/neulab/Pangea-7B"},{"title":"m-a-p/YuE-s1-7B-anneal-en-cot · Hugging Face","url":"https://huggingface.co/m-a-p/YuE-s1-7B-anneal-en-cot"}]

Based on the search results, here's what I found about MAP-Neo 7B:

## MAP-Neo 7B Overview

MAP-Neo is a fully open-sourced bilingual LLM with 7B parameters that achieves performance comparable to existing state-of-the-art LLMs.

## Key Characteristics

MAP-NEO is a fully open-sourced Large Language Model that includes the pretraining data, a data processing pipeline (Matrix), pretraining scripts, and alignment code, and is trained from scratch on 4.5T English and Chinese tokens, exhibiting performance comparable to LLaMA2 7B.

## Complete Transparency

All details to reproduce MAP-Neo are open-sourced, including the cleaned pre-training corpus, data cleaning pipeline, checkpoints, and well-optimiz
…[truncated 697 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-18T07:12:29.434984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"
  }
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-18T07:12:29.435116+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-18T07:12:29.435249+00:00_

Web search results for query: "Mistral Nemo 12B base model huggingface 2024 benchmark"

Links: [{"title":"nvidia/Mistral-NeMo-12B-Base · Hugging Face","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Base"},{"title":"nvidia/Mistral-NeMo-12B-Instruct · Hugging Face","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Instruct"},{"title":"Mistral NeMo | Mistral AI","url":"https://mistral.ai/news/mistral-nemo"},{"title":"Mistral NeMo 12B | Open Laboratory","url":"https://openlaboratory.com/models/mistral-nemo-12b/"},{"title":"Mistral NeMo 12B — A comprehensive look at the next-generation enterprise AI model | UnfoldAI","url":"https://unfoldai.com/mistral-nemo-12b-review/"},{"title":"mistralai/Mistral-Nemo-Base-2407 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Nemo-Base-2407"},{"title":"mistralai/Mistral-Nemo-Instruct-2407 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407"},{"title":"starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF · Hugging Face","url":"https://huggingface.co/starble-dev/Mistral-Nemo-12B-Instruct-2407-GGUF"},{"title":"EasierAI/Mistral-NeMo-12B · Hugging Face","url":"https://huggingface.co/EasierAI/Mistral-NeMo-12B"},{"title":"README.md · nvidia/Mistral-NeMo-12B-Base at main","url":"https://huggingface.co/nvidia/Mistral-NeMo-12B-Base/blob/main/README.md"}]

Based on the search results, here's comprehensive information about the Mistral Nemo 12B base model and its 2024 benchmarks:

## Model Overview

Mistral-NeMo-12B-Base is a Large Language Model (LLM) composed of 12B parameters, trained jointly by NVIDIA and Mistral AI. The model was trained between May 2024 and June 2024.

## Key Capabilities

Mistral-NeMo-12B-Base is a completion model intended for use in over 80+ programming languages and designed for global, multilingual applications. It is fast, trained on function-calling, has a large context window, and is particularly strong in English, French, German, Spanish, Italian, Portuguese, Chine
…[truncated 815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-18T07:12:29.435429+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-18T07:12:29.435574+00:00_

Web search results for query: "Yi-1.5 9B base model huggingface 01.AI 2024 2025"

Links: [{"title":"01-ai (01-ai)","url":"https://huggingface.co/01-ai"},{"title":"GitHub - 01-ai/Yi-1.5: Yi-1.5 is an upgraded version of Yi, delivering stronger performance in coding, math, reasoning, and instruction-following capability. · GitHub","url":"https://github.com/01-ai/Yi-1.5"},{"title":"01-ai/Yi-1.5-9B · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B"},{"title":"Paper page - Yi: Open Foundation Models by 01.AI","url":"https://huggingface.co/papers/2403.04652"},{"title":"01-ai/Yi-1.5-9B-Chat-16K · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B-Chat-16K"},{"title":"Yi 1.5 34B | Open Laboratory","url":"https://openlaboratory.ai/models/yi-1_5-34b"},{"title":"01-ai/Yi-Coder-1.5B-Chat · Hugging Face","url":"https://huggingface.co/01-ai/Yi-Coder-1.5B-Chat"},{"title":"Models – Hugging Face","url":"https://huggingface.co/models"},{"title":"01-ai/Yi-1.5-9B · extended context","url":"https://huggingface.co/01-ai/Yi-1.5-9B/discussions/1"},{"title":"01-ai/Yi-1.5-9B-32K · Hugging Face","url":"https://huggingface.co/01-ai/Yi-1.5-9B-32K"}]

Based on the search results, here's what I found about the Yi-1.5 9B base model from 01.AI on Hugging Face:

## Overview
Yi-1.5 is an upgraded version of Yi, delivering stronger performance in coding, math, reasoning, and instruction-following capability. The Yi-1.5 series models were open-sourced on 2024-05-13, further improving coding, math, reasoning, and instruction-following abilities.

## Model Availability
The Yi 1.5 family includes multiple parameter scales and configurations, such as 6B, 9B, and 34B models, in both base and chat forms, and offers long-context and multimodal versions. The Yi-1.5-9B base model is available on Hugging Face at the official 01-ai organization.

## Performance
Yi-1.5-9B is the top performer among similarly sized open-source models. The base model achieves reported scores of 76.3 on MMLU, 54.
…[truncated 459 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-18T07:12:29.435816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 14B base model huggingface benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 14B base model huggingface benchmark 2025"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-18T07:12:29.435969+00:00_

Web search results for query: "Gemma 3 7B 12B base model HuggingFace release date 2025 benchmark parameters"

Links: [{"title":"Gemma 3 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma3"},{"title":"Gemma 3 Release - a google Collection","url":"https://huggingface.co/collections/google/gemma-3-release"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"Google's Gemma 3: Features, Benchmarks, Performance and Implementation","url":"https://www.analyticsvidhya.com/blog/2025/03/gemma-3/"},{"title":"google/gemma-3-27b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-27b-it"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"google/gemma-7b · Hugging Face","url":"https://huggingface.co/google/gemma-7b"},{"title":"Gemma releases | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/releases"},{"title":"Gemma 3: Google’s new open model based on Gemini 2.0","url":"https://blog.google/technology/developers/gemma-3/"}]

Based on the search results, here's the information about Gemma 3:

## Model Sizes and Parameters

Gemma 3 is a multimodal model with pretrained and instruction-tuned variants, available in 1B, 13B, and 27B parameters. However, other sources indicate it comes in four distinct sizes – 1B, 4B, 12B, and 27B parameters with both base (pre-trained) and instruction-tuned variants. Note that there is no 7B variant in Gemma 3; the search results mention a 4B and 12B model instead.

## Release Date

Gemma 3 12B was released on March 12, 2025 by Google.

## Training Data

The 27B model was trained with 14 trillion tokens, the 12B model was trained with 12 trillion tokens, 4B model was trained with 4 trillion tokens and 1B with 2 trillion tokens.

…[truncated 482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-18T07:12:29.436133+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-18T07:12:29.436267+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 2 9B base model huggingface benchmark 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 2 9B base model huggingface benchmark 2024"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-18T07:12:29.436468+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "StarCoder2 7B 15B base model huggingface 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "StarCoder2 7B 15B base model huggingface 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-18T07:12:29.436621+00:00_

Web search results for query: "Qwen3 7B 8B 14B base model HuggingFace release date benchmark MMLU parameters 2025"

Links: [{"title":"Qwen/Qwen3.6-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.6-27B"},{"title":"Qwen/Qwen3.5-9B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-9B"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"GitHub - QwenLM/Qwen3.6: Qwen3.6 is the large language model series developed by Qwen team, Alibaba Group. · GitHub","url":"https://github.com/QwenLM/Qwen3.6"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen/Qwen3.5-0.8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-0.8B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen/Qwen3.5-27B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3.5-27B"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"GitHub - QwenLM/Qwen: The official repo of Qwen (通义千问) chat & pretrained large language model proposed by Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/Qwen"}]

Based on the search results, here's the information about Qwen3 models:

## Release Date and Model Sizes

Qwen3 was announced as the latest addition to the Qwen family of large language models, with the release occurring in 2025. Six dense models were open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, under Apache 2.0 license.

## Model Parameters and Performance

The overall performance of Qwen3 dense base models matches that of Qwen2.5 base models with more parameters. For instance, Qwen3-1.7B/4B/8B/14B/32B-Base performs as well as Qwen2.5-3B/7B/14B/32B/72B-Base, respectively.

## MMLU Benchmark

The search results reference MMLU benchmark testing. For MMLU-ProX, they report the averag
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-18T07:12:29.436786+00:00_

Web search results for query: "Llama 4 Scout Maverick 7B 8B parameters MoE active base model HuggingFace 2025"

Links: [{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://huggingface.co/blog/llama4-release"},{"title":"The Llama 4 herd: The beginning of a new era of natively multimodal AI innovation","url":"https://ai.meta.com/blog/llama-4-multimodal-intelligence/"},{"title":"Evolution of Meta’s LLaMA Models and Parameter-Efficient Fine-Tuning of Large Language Models: A Survey","url":"https://arxiv.org/html/2510.12178v1"},{"title":"meta-llama/Llama-4-Scout-17B-16E · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E"},{"title":"Llama4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/llama4"},{"title":"meta-llama (Meta Llama)","url":"https://huggingface.co/meta-llama"},{"title":"Llama 4 (Scout/Maverick) - D-Central","url":"https://d-central.tech/ai/model/llama-4/"},{"title":"Welcome Llama 4 Maverick & Scout on Hugging Face","url":"https://github.com/huggingface/blog/blob/main/llama4-release.md"},{"title":"meta-llama/Llama-4-Maverick-17B-128E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct"},{"title":"meta-llama/Llama-4-Scout-17B-16E-Instruct · Hugging Face","url":"https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct"}]

Based on the search results, here's detailed information about Llama 4 Scout and Maverick:

## Model Parameters and Architecture

Llama 4 Maverick (~400B) and Llama 4 Scout (~109B) were released by Meta in 2025. Both models feature Mixture of Experts (MoE) architecture:

- Both are Mixture of Experts (MoE) models with 17B active parameters
- Llama 4 Maverick with 17B active parameters out of ~400B total, with 128 experts
- Llama 4 Scout also has 17B active parameters out of ~109B total, using just 16 experts

## MoE Architecture Details

The two models differ in their expert implementation:

- Llama Scout is a ful
…[truncated 891 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 149 · 2026-05-18T07:12:29.436949+00:00_

Web search results for query: "Qwen3 14B base model huggingface benchmark 2025"

Links: [{"title":"Qwen/Qwen3-14B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"nvidia/Qwen3-14B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-NVFP4"},{"title":"unsloth/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/unsloth/Qwen3-14B-Base"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"},{"title":"nvidia/Qwen3-14B-FP8 · Hugging Face","url":"https://huggingface.co/nvidia/Qwen3-14B-FP8"},{"title":"Quantized Models for Qwen/Qwen3-14B – Hugging Face","url":"https://huggingface.co/models?other=base_model%3Aquantized%3AQwen%2FQwen3-14B"},{"title":"GitHub - QwenLM/Qwen3: Qwen3 is the large language model series developed by Qwen team, Alibaba Cloud. · GitHub","url":"https://github.com/QwenLM/qwen3"}]

Based on the search results, here's what I found about the Qwen3 14B base model and its 2025 benchmarks:

## Model Specifications

Qwen3-14B-Base has 14.8B parameters (13.2B non-embedding parameters), 40 layers, 40 attention heads (Q) and 8 for KV with Group Query Attention (GQA), and a context length of 32,768 tokens.

## Benchmark Performance

Qwen3-14B-Base performs as well as Qwen2.5-32B-Base, and notably outperforms larger Qwen2.5 models in areas like STEM, coding, and reasoning.

More specifically, Qwen3-14B-Base achieves very competitive results compared to Qwen2.5-32B-Base, demonstrating significant efficiency gains.

## Training and Performance

Qwen3 is pre-trained on 36 trillion tokens across 119 languages, tripling the language coverage of Qwen2.5, with a rich mi
…[truncated 434 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-18T07:12:29.437109+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"
  }
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-18T07:12:29.437245+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 12B base pretrained \"gemma-3-12b-pt\" HuggingFace gated benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 12B base pretrained \"gemma-3-12b-pt\" HuggingFace gated benchmark MMLU"
  }
}
```

</details>

---

### Tool call

_source line 152 · 2026-05-18T07:12:29.437400+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"
  }
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-18T07:12:29.437536+00:00_

Web search results for query: "OLMo 2 7B 13B benchmark MMLU scores training tokens 2024"

Links: [{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | Ai2","url":"https://allenai.org/blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"OLMo 2: The best fully open language model to date | Ai2","url":"https://allenai.org/blog/olmo2"},{"title":"OLMo release notes | Ai2","url":"https://allenai.org/olmo/release-notes"},{"title":"2 OLMo 2 Furious OLMo Team Pete Walsh 1 Luca Soldaini 1 Dirk Groeneveld 1","url":"https://arxiv.org/pdf/2501.00656"},{"title":"allenai/OLMo-2-1124-7B-Instruct Free Chat Online - skywork.ai - Skywork ai","url":"https://skywork.ai/blog/models/allenai-olmo-2-1124-7b-instruct-free-chat-online-skywork-ai/"},{"title":"OLMo 2 7B vs 13B: Research Performance and Resource Analysis | Markaicode","url":"https://markaicode.com/vs/olmo-2-7b-vs-13b/"},{"title":"OLMo 1.7–7B: A 24 point improvement on MMLU | by Ai2 | Ai2 Blog | Medium","url":"https://medium.com/ai2-blog/olmo-1-7-7b-a-24-point-improvement-on-mmlu-92b43f7d269d"},{"title":"allenai/OLMo-2-1124-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-2-1124-7B"},{"title":"(PDF) 2 OLMo 2 Furious","url":"https://www.researchgate.net/publication/387671074_2_OLMo_2_Furious"},{"title":"allenai/OLMo-7B · Hugging Face","url":"https://huggingface.co/allenai/OLMo-7B"}]

Based on the search results, here's the key information about OLMo 2 7B and 13B models:

## Training Tokens

OLMo 2 is a family of 7B and 13B models trained on up to 5T tokens. More specifically, OLMo 2 7B is trained for approximately one epoch on the first-stage dataset, while OLMo 2 13B is trained for 1.2 epochs up to 5T tokens.

## MMLU Benchmark Scores

OLMo 2 achieved MMLU scores of 63.7 for the 7B model and 67.5 for the 13B model. This represents a 9-point increase in MMLU compared to the original OLMo 7B model.

## Training Approach

OLMo 2 is pretrained in two stages using a curriculum approach. In the first
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-18T07:12:29.437698+00:00_

Web search results for query: "Gemma 2 9B base model huggingface benchmark 2024"

Links: [{"title":"google/gemma-2-9b · Hugging Face","url":"https://huggingface.co/google/gemma-2-9b"},{"title":"RedHatAI/gemma-2-9b-it-FP8 · Hugging Face","url":"https://huggingface.co/RedHatAI/gemma-2-9b-it-FP8"},{"title":"google/gemma-2-2b · Hugging Face","url":"https://huggingface.co/google/gemma-2-2b"},{"title":"bartowski/gemma-2-9b-it-GGUF · Hugging Face","url":"https://huggingface.co/bartowski/gemma-2-9b-it-GGUF"},{"title":"neuralmagic/gemma-2-9b-it-FP8 · Hugging Face","url":"https://huggingface.co/neuralmagic/gemma-2-9b-it-FP8"},{"title":"Gemma 2: Improving Open Language Models at a Practical Size","url":"https://arxiv.org/html/2408.00118v2"},{"title":"google/gemma-2-2b-it · Hugging Face","url":"https://huggingface.co/google/gemma-2-2b-it"},{"title":"Gemma2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/gemma2"},{"title":"google/gemma-2-27b · Hugging Face","url":"https://huggingface.co/google/gemma-2-27b"},{"title":"google/recurrentgemma-9b · Hugging Face","url":"https://huggingface.co/google/recurrentgemma-9b"}]

Based on the search results, here's information about the Gemma 2 9B base model and its benchmark performance:

## Model Overview

Gemma 2 is a family of language models with pretrained and instruction-tuned variants, available in 2B, 9B, 27B parameters. The 9B model was trained with 8 trillion tokens, and the 2B and 9B models are trained with knowledge distillation.

## Architecture

The architecture features interleaved local attention (4096 tokens) and global attention (8192 tokens) and grouped-query attention (GQA) to increase inference performance.

## Benchmark Performance

The search results include benchmark information for the Gemma 2 9B instruction-tuned variant. The unquantized gemma-2-9b-it model achieves an average score of 73.23 on the OpenLLM benchmark (version 1).

Additionally, there was a massive improvement in the models
…[truncated 458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-18T07:12:29.437856+00:00_

Web search results for query: "StarCoder2 7B 15B base model huggingface 2024 2025"

Links: [{"title":"Starcoder2 · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/starcoder2"},{"title":"bigcode/starcoder2-15b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-15b"},{"title":"GitHub - bigcode-project/starcoder2: Home of StarCoder2! · GitHub","url":"https://github.com/bigcode-project/starcoder2"},{"title":"bigcode/starcoder2-7b · Hugging Face","url":"https://huggingface.co/bigcode/starcoder2-7b"},{"title":"Starcoder2","url":"https://huggingface.co/docs/transformers/v4.46.0/model_doc/starcoder2"},{"title":"StarCoder2: AI-Powered Code Generation by ServiceNow, Hugging Face and NVIDIA | by My Social | 𝐀𝐈 𝐦𝐨𝐧𝐤𝐬.𝐢𝐨 | Medium","url":"https://medium.com/aimonks/starcoder2-ai-powered-code-generation-by-servicenow-hugging-face-and-nvidia-7f51763af0e6"},{"title":"blog/starcoder2.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/starcoder2.md"},{"title":"bigcode (BigCode)","url":"https://huggingface.co/bigcode"},{"title":"FineTuning StarCoder2 on Google Colab T4 GPU","url":"https://medium.com/codex/finetuning-starcoder2-on-google-colab-t4-gpu-a7a416efde4e"},{"title":"StarCoder 2 is a code-generating AI that runs on most GPUs | TechCrunch","url":"https://techcrunch.com/2024/02/28/starcoder-2-is-a-code-generating-ai-that-runs-on-most-gpus/"}]

Based on the search results, here's what I found about StarCoder2 7B and 15B base models on Hugging Face:

## Release Information

StarCoder2 was released on February 29, 2024 and added to Hugging Face Transformers on February 28, 2024.

## Model Overview

StarCoder2 is a family of open LLMs for code and comes in 3 different sizes with 3B, 7B and 15B parameters.

## StarCoder2-7B Details

StarCoder2-7B is a 7B parameter model trained on 17 programming languages from The Stack v2, with opt-out requests excluded. The model uses Grouped Query Attention, a context window o
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 156 · 2026-05-18T07:12:29.438023+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Falcon3 7B 10B MMLU benchmark scores training data 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Falcon3 7B 10B MMLU benchmark scores training data 2024"
  }
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-18T07:12:29.438161+00:00_

Web search results for query: "Qwen3 14B base training tokens data size MMLU benchmark score release date April 2025"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3 14B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-14b/"},{"title":"An Empirical Study of Qwen3 Quantization","url":"https://arxiv.org/html/2505.02214v1"},{"title":"2025-05-13 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00069-Qwen3_Technical_Report.pdf"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"An empirical study of Qwen3 quantization | Visual Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44267-026-00114-4"},{"title":"Qwen3 4B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen3-4b"},{"title":"Qwen3 14B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/qwen3-14b-instruct"},{"title":"Qwen3 0.6B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-0_6b/"},{"title":"Home GPU LLM Leaderboard: Best Open Source Models by VRAM Tier with Token/s Benchmarks | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/home-gpu-llm-leaderboard/"}]

Based on the search results, here's the information about Qwen3 14B:

## Key Information:

**Release Date:** Qwen3-14B was officially released on April 29, 2025.

**MMLU Benchmark Score:** Qwen3-14B-Base attains scores of 81.05 on MMLU.

**Training Data:** While the search results don't provide the exact training token count specifically for Qwen3-14B, they indicate that the Qwen3 series was developed by Alibaba Cloud's Qwen team and represents a significant advancement in their model lineup.

**Model Size:** Qwen3-14B is a dense model with 14 billion total parameters.

The model demonstrates strong performa
…[truncated 522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-18T07:12:29.438328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 3 release date January March 2025 google 4B 12B"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 3 release date January March 2025 google 4B 12B"
  }
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-18T07:12:29.438465+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OLMo 3 7B base model allenai huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OLMo 3 7B base model allenai huggingface 2025"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-18T07:12:29.438602+00:00_

Web search results for query: "Gemma 3 12B base pretrained "gemma-3-12b-pt" HuggingFace gated benchmark MMLU"

Links: [{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"google/gemma-3-12b-it · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-it"},{"title":"google/gemma-3-12b-pt · Hugging Face","url":"https://huggingface.co/google/gemma-3-12b-pt"},{"title":"cjvt/GaMS3-12B-Instruct · Hugging Face","url":"https://huggingface.co/cjvt/GaMS3-12B-Instruct"},{"title":"gemma3:12b","url":"https://ollama.com/library/gemma3:12b"},{"title":"Gemma 3 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-3/"},{"title":"litert-community/Gemma3-12B-IT · Hugging Face","url":"https://huggingface.co/litert-community/Gemma3-12B-IT"},{"title":"google/gemma-3-12b-pt at main","url":"https://huggingface.co/google/gemma-3-12b-pt/tree/main"},{"title":"Gemma 3 12B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-12b-it"},{"title":"INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0 · Hugging Face","url":"https://huggingface.co/INSAIT-Institute/MamayLM-Gemma-3-12B-IT-v1.0"}]

Based on the search results, here's what I found regarding Gemma 3 12B base pretrained model:

## Model Access
To access Gemma on Hugging Face, you're required to review and agree to Google's usage license, and you need to be logged in to Hugging Face. The model is indeed gated on HuggingFace.

## Model Specifications
Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions.

## MMLU Benchmark
Regarding MMLU benchmarks, the search results indicate that Gemma 3 has been evaluated across benchmarks like MMLU-Pro (27B: 67.5), Live
…[truncated 351 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-18T07:12:29.438761+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-18T07:12:29.438900+00:00_

Web search results for query: "Gemma 3 release date January March 2025 google 4B 12B"

Links: [{"title":"Gemma releases | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/releases"},{"title":"Gemma 3 - D-Central","url":"https://d-central.tech/ai/model/gemma-3/"},{"title":"Gemma (language model) - Wikipedia","url":"https://en.wikipedia.org/wiki/Gemma_(language_model)"},{"title":"Gemma 3 4B Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/gemma-3-4b-it"},{"title":"Gemma 3 4B – Try & Compare | Roboflow Playground","url":"https://playground.roboflow.com/models/google/gemma-3-4b"},{"title":"Gemma 3 12B Model Specs, Costs & Benchmarks (April 2026) | Galaxy.ai","url":"https://blog.galaxy.ai/model/gemma-3-12b-it"},{"title":"Introducing Gemma 3: The Developer Guide - Google Developers Blog","url":"https://developers.googleblog.com/en/introducing-gemma3/"},{"title":"Gemma 3 12B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/gemma-3-12b"},{"title":"Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM","url":"https://huggingface.co/blog/gemma3"},{"title":"Notes on Google’s Gemma 3","url":"https://simonwillison.net/2025/Mar/12/gemma-3/"}]

Based on the search results, here's what I found about Gemma 3's release:

Gemma 3 was released on March 12, 2025. This was not in January, but rather in March 2025 as part of your search query timeframe.

Google DeepMind's March 2025 Gemma family includes vision-capable models (4B+) with 128K context and official quantization-aware 4-bit variants.

**Available Model Sizes:**
Gemma 3 was offered in 1, 4, 12, and 27 billion parameter sizes with support for over 140 languages. So the 4B and 12B models you mentioned in your query were indeed released as part of the Gemma 3 family.

**Key Features:**
As multimodal models, they support both text and image input. Additionally, Gemma 3 handles context windows up to 128k tokens, understand
…[truncated 235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-18T07:12:29.439059+00:00_

Web search results for query: "Mistral Small 3 7B 8B base model 2025 HuggingFace parameters benchmark"

Links: [{"title":"unsloth/Mistral-Small-24B-Base-2501-bnb-4bit · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501-bnb-4bit"},{"title":"Mistral 7B","url":"https://mistral.ai/news/announcing-mistral-7b"},{"title":"unsloth/Mistral-Small-24B-Base-2501 · Hugging Face","url":"https://huggingface.co/unsloth/Mistral-Small-24B-Base-2501"},{"title":"NVIDIA-Accelerated Mistral 3 Open Models Deliver Efficiency, Accuracy at Any Scale | NVIDIA Technical Blog","url":"https://developer.nvidia.com/blog/nvidia-accelerated-mistral-3-open-models-deliver-efficiency-accuracy-at-any-scale/"},{"title":"Mistral Docs","url":"https://docs.mistral.ai/models/overview"},{"title":"Introducing Mistral 3 | Mistral AI","url":"https://mistral.ai/news/mistral-3"},{"title":"mistralai/Mistral-7B-Instruct-v0.3 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3"},{"title":"mistralai/Mistral-7B-v0.1 · Hugging Face","url":"https://huggingface.co/mistralai/Mistral-7B-v0.1"},{"title":"Mistral · Hugging Face","url":"https://huggingface.co/docs/transformers/en/model_doc/mistral"},{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"}]

Based on the search results, here's what I found about Mistral models in 2025:

## Mistral Small 3 (2501)

Mistral Small 3 (2501) sets a new benchmark in the "small" Large Language Models category below 70B, boasting 24B parameters and achieving state-of-the-art capabilities comparable to larger models.

## Ministral 3 Series

For smaller models, Mistral released the Ministral 3 family, which includes multiple parameter sizes:

A suite of small, dense high-performance models (called Ministral 3) of sizes 3B, 8B, and 14B, each with Base, Instruct, and Reasoning variants (nine models total) All the models were trained on NVIDIA Hopper GPUs and are now available through Mistral AI on Hugging Face.

## 
…[truncated 688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-18T07:12:29.439213+00:00_

Web search results for query: "OLMo 3 7B base model allenai huggingface 2025"

Links: [{"title":"allenai/Olmo-3-1025-7B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1025-7B"},{"title":"allenai/Olmo-3-1125-32B · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-1125-32B"},{"title":"Olmo 3 - a allenai Collection","url":"https://huggingface.co/collections/allenai/olmo-3"},{"title":"allenai/Olmo-3-7B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Instruct"},{"title":"allenai/Olmo-3-7B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think"},{"title":"allenai/Olmo-3.1-32B-Instruct · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Instruct"},{"title":"allenai/Olmo-3.1-32B-Think · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3.1-32B-Think"},{"title":"allenai/Olmo-3-7B-RL-Zero-Math · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-RL-Zero-Math"},{"title":"Mungert/Olmo-3-1025-7B-GGUF · Hugging Face","url":"https://huggingface.co/Mungert/Olmo-3-1025-7B-GGUF"},{"title":"allenai/Olmo-3-7B-Think-DPO · Hugging Face","url":"https://huggingface.co/allenai/Olmo-3-7B-Think-DPO"}]

Based on the web search results, here's what I found about the OLMo 3 7B base model from Allen AI on Hugging Face:

## Overview

OLMo 3 is a new family of 7B and 32B models, with a suite that includes Base, Instruct, and Think variants. The Base models were trained using a staged training approach.

## Training Details

The main dataset used is dolma3_6T-mix-1025, consisting of 5.93T tokens with coverage of 97.53%+ of total pretraining budget. The training mix composition includes 20% code, 28% web pages, 19% math, 14% QA, 8% thinking, 6% instruction, and 5% PDFs.

## Model Availability

The base model is available on Hugging Face at `allenai/Olmo-3-1025-7B`. The research paper and details are available at https://allenai.org/papers/olmo3.

## Licensing and Usage

This model is licensed under A
…[truncated 353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 165 · 2026-05-18T07:12:29.439395+00:00_

Web search results for query: "Falcon3 7B 10B MMLU benchmark scores training data 2024"

Links: [{"title":"Welcome to the Falcon 3 Family of Open Models! | Falcon","url":"https://falcon-lm.github.io/blog/falcon-3/"},{"title":"Welcome to the Falcon 3 Family of Open Models!","url":"https://huggingface.co/blog/falcon3"},{"title":"🐺🐦‍⬛ LLM Comparison/Test: DeepSeek-V3, QVQ-72B-Preview, Falcon3 10B, Llama 3.3 70B, Nemotron 70B in my updated MMLU-Pro CS benchmark","url":"https://huggingface.co/blog/wolfram/llm-comparison-test-2025-01-02"},{"title":"tiiuae/Falcon3-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-7B-Base"},{"title":"tiiuae/Falcon3-1B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon3-1B-Base"},{"title":"Falcon LLM Architecture: Deep Dive into its Design and Performance | SaM Solutions","url":"https://sam-solutions.com/blog/falcon-llm-architecture/"},{"title":"Experience Advanced AI Anywhere with Falcon 3's Lightweight Design","url":"https://www.analyticsvidhya.com/blog/2024/12/falcon-3/"},{"title":"TII launches world’s most powerful SLMs under 13B parameters","url":"https://www.middleeastainews.com/p/tii-launches-most-powerful-slm"},{"title":"Falcon 3 series sets new benchmarks for open-source LLMs on a single GPU","url":"https://the-decoder.com/abu-dhabis-tii-releases-falcon-3-setting-new-benchmarks-for-efficient-open-source-ai-models/"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1/"}]

Based on the search results, here's the information about Falcon3 7B and 10B MMLU benchmark scores and training data:

## MMLU Benchmark Scores

Falcon3-7B-Base achieved scores of 67.4 on MMLU and 39.2 on MMLU-PRO, while Falcon3-10B-Base achieved 73.1 on MMLU and 42.5 on MMLU-PRO respectively.

## Training Data

The 7B model was trained on 14 trillion tokens using 1024 H100 GPU chips, leveraging web, code, STEM, and curated hig
…[truncated 585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-18T07:12:29.439564+00:00_

Web search results for query: "Llama 3.1 8B base MMLU benchmark training tokens 15T 2024"

Links: [{"title":"Llama 3.1 8B Instruct - NGC Catalog - NVIDIA","url":"https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/llama-3_1-8b-instruct-nemo"},{"title":"MLPerf Training Adds Llama 3.1 8B Benchmark - MLCommons","url":"https://mlcommons.org/2025/10/training-llama-3-1-8b/"},{"title":"Llama 3.1 8B - Intelligence, Performance & Price Analysis","url":"https://artificialanalysis.ai/models/llama-3-1-instruct-8b"},{"title":"Introducing Meta Llama 3: The most capable openly available LLM to date","url":"https://ai.meta.com/blog/meta-llama-3/"},{"title":"Llama 3.1","url":"https://www.llama.com/llama3_1/"},{"title":"Llama 3's Performance Benchmark Values Explained | by Ingrid Stevens | Medium","url":"https://medium.com/@ingridwickstevens/more-llm-acronyms-an-explainer-on-llama-3s-performance-benchmark-values-36722c6dcabb"},{"title":"Llama 3.2: Revolutionizing edge AI and vision with open, customizable models","url":"https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/"},{"title":"llama-models/models/llama3_1/eval_details.md at main · meta-llama/llama-models","url":"https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/eval_details.md"},{"title":"Meta's New Llama 3.1 AI Model: Use Cases & Benchmark","url":"https://research.aimultiple.com/meta-llama/"},{"title":"Llama 3.1 Guide: What to know about Meta's new 405B model and its data","url":"https://kili-technology.com/large-language-models-llms/llama-3-1-guide-what-to-know-about-meta-s-new-405b-model-and-its-data"}]

Based on the search results, I found relevant information about Llama 3.1 8B's training and MMLU benchmark performance:

## Training Tokens

Llama 3.1 used about 15T multilingual tokens, compared to 1.8T tokens for Llama 2. This confirms the 15T token training mentioned in your query.

## MMLU Benchmark Performance

For the Llama 3.1 8B base model specifically:

- For the p
…[truncated 587 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-18T07:12:29.439726+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2.5 14B MMLU benchmark base model training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2.5 14B MMLU benchmark base model training tokens"
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-18T07:12:29.439856+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 4 base model release 2026 huggingface google"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 4 base model release 2026 huggingface google"
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-18T07:12:29.439981+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Falcon H1 7B 14B hybrid model huggingface 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Falcon H1 7B 14B hybrid model huggingface 2025"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-18T07:12:29.440155+00:00_

Here are all findings compiled in structured format.

---

## Gemma 3 (Google DeepMind)

**Release date:** March 12, 2025 (added to HuggingFace Transformers); public release ~March 25, 2025

**License:** Gemma Terms of Use (custom Google license)

**Gated:** Yes. Requires agreeing to Google's usage license on HuggingFace before downloading.

**Base (pretrained) versions exist:** Yes. All sizes have a `-pt` (pretrained) variant.

| Size | HuggingFace Repo ID | Parameters | Modality | Context Window | Training Tokens | MMLU (base) | HellaSwag (base) |
|------|---------------------|------------|----------|----------------|-----------------|-------------|------------------|
| 1B | `google/gemma-3-1b-pt` | 1B | Text only | 32K | 2T | 38.8% | 62.3 |
| 4B | `google/gemma-3-4b-pt` | 4B | Text + Image | 128K | 4T | 58.1% | 77.2 |
| 12B | `google/gemma-3-12b-pt` | 12B | Text + Image | 128K | 12T | 71.9% | 84.2 |
| 27B | `google/gemma-3-27b-pt` | 27B | Text + Image | 128K | 14T | 76.9% | 85.6 |

**Instruction-tuned counterparts** use the `-it` suffix (e.g., `google/gemma-3-12b-it`).

**Additional notes:**
- 140+ language support
- Trained using knowledge distillation from larger Gemini models
- Trained on TPUv4p, TPUv5p, and TPUv5e hardware
- A 270M text-only variant also exists, trained on 6T tokens
- Gemma 3 4B-IT beats Gemma 2 27B-IT; Gemma 3 27B-IT is comparable to Gemini 1.5 Pro
- Technical report: [arxiv.org/abs/2503.19786](https://arxiv.org/abs/2503.19786)

---

## OLMo 2 (Allen Institute for AI / Ai2)

**License:** Apache 2.0 (fully open, including training data, code, and weights)

**Gated:** No. All models are openly available.

**Base (pretrained) versions exist:** Yes. The base repo IDs below are the pretrained models; instruct/SFT/DPO variants have corresponding suffixes.

| Size | HuggingFace Repo ID | Parameters | Release Date | Training Tokens | MMLU (base) |
|------|---------------------|------------|--------------|-----------------|-------------|
| 1B | `alle
…[truncated 3695 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "elapsed_ms": 25
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-18T07:12:29.440346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"
  }
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-18T07:12:29.440501+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen3 8B 14B base training data tokens pretraining technical report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen3 8B 14B base training data tokens pretraining technical report"
  }
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-18T07:12:29.440634+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-18T07:12:29.440766+00:00_

Web search results for query: "Qwen2.5 14B MMLU benchmark base model training tokens"

Links: [{"title":"Qwen2.5-LLM: Extending the boundary of LLMs | Qwen","url":"https://qwenlm.github.io/blog/qwen2.5-llm/"},{"title":"2025-01-06 Qwen2.5 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2412.15115"},{"title":"Qwen2.5 14B Instruct Benchmarks, Pricing & Context Window","url":"https://llm-stats.com/models/qwen-2.5-14b-instruct"},{"title":"2025-01-26 Qwen2.5-1M Technical Report","url":"https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/Qwen2_5_1M_Technical_Report.pdf"},{"title":"Qwen 2.5 14B | Open Laboratory","url":"https://openlaboratory.ai/models/qwen-2_5-14b"},{"title":"Technical Report Qwen2.5-Coder Technical Report Binyuan Hui* Jian Yang*","url":"https://arxiv.org/pdf/2409.12186"},{"title":"Qwen2.5-Coder Technical Report","url":"https://arxiv.org/html/2409.12186v3"},{"title":"Qwen 2.5","url":"https://qwen2.org/qwen2-5/"},{"title":"Qwen2.5-LLM: Extending the Boundary of LLMs - Alibaba Cloud Community","url":"https://www.alibabacloud.com/blog/601786"},{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"}]

Based on the search results, here's what I found about Qwen2.5-14B:

## MMLU Benchmark Performance

The Qwen2.5-14B model achieves a score of 79.7 on MMLU, demonstrating strong performance on this general language understanding benchmark.

## Training Tokens

The pre-training dataset was expanded from 7 trillion tokens to a maximum of 18 trillion tokens. This represents the training data size used for the Qwen2.5 series models, including the 14B variant.

## Additional Context

Qwen2.5 models, including the 14B variant, are pretrained on a large-scale corpus comprising up to 18 trillion tokens, with the pretraining data covering diverse domains and curated for high data quality.

The Qwen2.5-14B base model demonstrates competitive performance, particul
…[truncated 189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-18T07:12:29.440918+00:00_

Web search results for query: "Gemma 4 base model release 2026 huggingface google"

Links: [{"title":"google/gemma-4-26B-A4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"Gemma 4 — Google DeepMind","url":"https://deepmind.google/models/gemma/gemma-4/"},{"title":"google/gemma-4-E4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B-it"},{"title":"google/gemma-4-26B-A4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B-it"},{"title":"What Is Google Gemma 4? Architecture, Benchmarks, and Why It Matters | WaveSpeed Blog","url":"https://wavespeed.ai/blog/posts/what-is-google-gemma-4/"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"google/gemma-4-E4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B"},{"title":"Gemma4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma4"},{"title":"Gemma 4: Byte for byte, the most capable open models","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"}]

I've found comprehensive information about the Gemma 4 base model release. Here's what I found:

## Gemma 4 Release

On April 2, 2026, Google DeepMind released Gemma 4 — four open-weight models built from the same research lineage as Gemini 3, now shipped under the Apache 2.0 license.

## Model Variants

The models are available in four distinct sizes: E2B, E4B, 26B A4B, and 31B. This release includes open-weights models in both pre-trained and instruction-tuned variants.

## Key Capabilities

Gemma 4 models are multimodal, handling text and image input (with audio supported on small models) and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

## Availability

You can download Gemma 4 model
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-18T07:12:29.441078+00:00_

Web search results for query: "Falcon H1 7B 14B hybrid model huggingface 2025"

Links: [{"title":"tiiuae/Falcon-H1R-7B · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1R-7B"},{"title":"Introducing Falcon H1R 7B","url":"https://huggingface.co/blog/tiiuae/falcon-h1r-7b"},{"title":"tiiuae/Falcon-H1R-7B-GGUF · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1R-7B-GGUF"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1/"},{"title":"Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling | Falcon","url":"https://falcon-lm.github.io/blog/falcon-h1r-7b/"},{"title":"FalconH1","url":"https://huggingface.co/docs/transformers/en/model_doc/falcon_h1"},{"title":"tiiuae/Falcon-H1-7B-Instruct · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1-7B-Instruct"},{"title":"[2507.22448] Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance","url":"https://arxiv.org/abs/2507.22448"},{"title":"Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance","url":"https://huggingface.co/blog/tiiuae/falcon-h1"},{"title":"tiiuae/Falcon-H1-7B-Base · Hugging Face","url":"https://huggingface.co/tiiuae/Falcon-H1-7B-Base"}]

Based on the search results, here's information about the Falcon H1 hybrid models:

## Falcon-H1 Hybrid Model Family

Falcon-H1 is a series of large language models featuring hybrid architecture designs that combines Transformer-based attention with State Space Models (SSMs), known for superior long-context memory and computational efficiency.

### Model Sizes and Availability

Falcon-H1 is released in multiple configurations, including base and instruction-tuned variants at 0.5B, 1.5B, 1.5B-deep, 3B, 7B, and 34B parameters.

### Key Features

- The amount of attention and mamba heads can be adjusted independently, allowing for an optim
…[truncated 1098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-18T07:12:29.441231+00:00_

Web search results for query: "DeepSeek V2 Lite base 15.7B HuggingFace release date gated benchmark MMLU training tokens"

Links: [{"title":"deepseek-ai/DeepSeek-V2-Lite · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite"},{"title":"deepseek-ai/DeepSeek-V4-Pro · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base"},{"title":"deepseek-ai/DeepSeek-V2-Lite-Chat · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite-Chat"},{"title":"lmstudio-community/DeepSeek-Coder-V2-Lite-Instruct-GGUF · Hugging Face","url":"https://huggingface.co/lmstudio-community/DeepSeek-Coder-V2-Lite-Instruct-GGUF"},{"title":"GitHub - deepseek-ai/DeepSeek-Coder-V2: DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Coder-V2"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct"},{"title":"deepseek-ai/DeepSeek-V2 · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-V2"},{"title":"deepseek-ai/DeepSeek-Coder-V2-Base · Hugging Face","url":"https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Base"},{"title":"GitHub - deepseek-ai/DeepSeek-LLM: DeepSeek LLM: Let there be answers · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-LLM"}]

Based on the search results, here's what I found about DeepSeek V2 Lite base 15.7B:

**Model Architecture & Parameters:**
DeepSeek-V2-Lite comprises 15.7B total parameters, of which 2.4B are activated for each token.

**Training Details:**
During pre-training, the maximum sequence length was set to 4K, and DeepSeek-V2-Lite was trained on 5.7T tokens. DeepSeek-V2-Lite was trained from scratch on the same pre-training corpus of DeepSeek-V2, which is not polluted by any SFT d
…[truncated 625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-18T07:12:29.441408+00:00_

Web search results for query: "Qwen3 8B 14B base training data tokens pretraining technical report"

Links: [{"title":"2025-05-15 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://arxiv.org/pdf/2505.09388"},{"title":"Qwen3-8B-Base: Open 8B LLM Overview","url":"https://www.emergentmind.com/topics/qwen3-8b-base"},{"title":"Qwen3: Think Deeper, Act Faster | Qwen","url":"https://qwenlm.github.io/blog/qwen3/"},{"title":"Qwen/Qwen3-14B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-14B-Base"},{"title":"[Literature Review] Qwen3 Technical Report","url":"https://www.themoonlight.io/en/review/qwen3-technical-report"},{"title":"Qwen3 Technical Report","url":"https://arxiv.org/html/2505.09388v1"},{"title":"2025-05-13 Qwen3 Technical Report Qwen Team https://huggingface.co/Qwen","url":"https://cdn.jsdelivr.net/gh/yanfeng98/paper-is-all-you-need/papers/00069-Qwen3_Technical_Report.pdf"},{"title":"(PDF) QWEN TECHNICAL REPORT","url":"https://www.researchgate.net/publication/377112868_QWEN_TECHNICAL_REPORT"},{"title":"Qwen3 Technical Report: Reasoning in Pre-Training and Post-Training","url":"https://thesalt.substack.com/p/qwen3-technical-report-reasoning"},{"title":"Qwen/Qwen3-8B-Base · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B-Base"}]

Based on the search results, here's the information about Qwen3 8B and 14B base models' pretraining details from the technical report:

## Pretraining Data and Tokens

Qwen3 uses approximately 36 trillion tokens covering 119 languages and dialects, which is a significant expansion compared to its predecessor.

### Three-Stage Pretraining Process

In the first stage (S1), the model was pretrained on over 30 trillion tokens with a context length of 4K tokens, which provided the model with basic language skills and general knowledge. In the second stage (S2), the dataset was improved by increasing the proportion of knowledge-intensive data such as STEM, coding, and reasoning tasks, and the mode
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-18T07:12:29.441627+00:00_

Here are the compiled findings from all three searches.

---

## SEARCH 1: Llama 4 Base Model Release

**Important caveat:** Llama 4 does NOT have any models in the 7B-14B parameter range. All Llama 4 models have 17B active parameters (MoE), with total parameter counts of 109B+ . There is no Llama 4 equivalent of the old Llama 3.1 8B.

### Llama 4 Scout

| Field | Detail |
|---|---|
| **Full name** | Llama 4 Scout 17B 16E |
| **HuggingFace repo (base)** | `meta-llama/Llama-4-Scout-17B-16E` |
| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Scout-17B-16E-Instruct` |
| **Parameter count** | 17B active, ~109B total (16 experts) |
| **Release date** | April 5, 2025 |
| **Gated?** | Yes -- requires accepting the Llama 4 Community License Agreement on HuggingFace |
| **Base (non-instruct) version?** | Yes (`meta-llama/Llama-4-Scout-17B-16E`) |
| **Training data size** | ~40 trillion tokens (multimodal), cutoff August 2024 |
| **Context window** | 10M tokens (pretrained at 256K) |
| **Architecture** | Mixture-of-Experts (MoE), auto-regressive, natively multimodal |
| **Benchmark** | Not individually broken out in public announcements for the base model |

### Llama 4 Maverick

| Field | Detail |
|---|---|
| **Full name** | Llama 4 Maverick 17B 128E |
| **HuggingFace repo (base)** | `meta-llama/Llama-4-Maverick-17B-128E` (also `meta-llama/Llama-4-Maverick-17B-128E-Original` for Meta format) |
| **HuggingFace repo (instruct)** | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` |
| **Parameter count** | 17B active, ~400B total (128 experts) |
| **Release date** | April 5, 2025 |
| **Gated?** | Yes -- same Llama 4 Community License |
| **Base (non-instruct) version?** | Yes |
| **Training data size** | ~22 trillion tokens (multimodal), cutoff August 2024 |
| **Context window** | 1M tokens |
| **Architecture** | MoE, auto-regressive, natively multimodal |

### Llama 4 Behemoth (not released)

Announced but still in training at time of Scout/Maverick release. 288B active p
…[truncated 6973 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-18T07:12:29.441803+00:00_

Web search results for query: "Ministral 3 8B 14B base model HuggingFace repo ID release date 2025 2026 training data benchmark MMLU"

Links: [{"title":"mistralai/Ministral-3-3B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512"},{"title":"mistralai/Ministral-3-8B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Base-2512"},{"title":"Ministral3","url":"https://huggingface.co/docs/transformers/main/en/model_doc/ministral3"},{"title":"mistralai/Ministral-3-14B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Reasoning-2512"},{"title":"mistralai/Ministral-3-3B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-3B-Base-2512"},{"title":"Ministral 3 - a mistralai Collection","url":"https://huggingface.co/collections/mistralai/ministral-3"},{"title":"mistralai/Ministral-3-14B-Base-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Base-2512"},{"title":"mistralai/Ministral-3-14B-Instruct-2512-BF16 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512-BF16"},{"title":"mistralai/Ministral-3-8B-Reasoning-2512 · Hugging Face","url":"https://huggingface.co/mistralai/Ministral-3-8B-Reasoning-2512"}]

Now let me search for more specific information about training data and benchmark performance including MMLU scores:

Links: [{"title":"Ministral 3 Abstract","url":"https://arxiv.org/pdf/2601.08584"},{"title":"Multilingual MMLU Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/multilingual-mmlu"},{"title":"Mistral: Ministral 3B Free Chat Online - Skywork ai","url":"https://skywork.ai/blog/models/mistral-ministral-3b-free-chat-online/"},{"title":"Mistral 3: Model Family, Architecture, Benchmarks & More - CometAPI - All AI Models in One 
…[truncated 4435 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-18T07:12:29.441966+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gemma 4 base model HuggingFace 2026 parameters 12B release date"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gemma 4 base model HuggingFace 2026 parameters 12B release date"
  }
}
```

</details>

---

### Tool call

_source line 182 · 2026-05-18T07:12:29.442104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"
  }
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-18T07:12:29.442238+00:00_

Web search results for query: "Gemma 4 base model HuggingFace 2026 parameters 12B release date"

Links: [{"title":"Gemma4 · Hugging Face","url":"https://huggingface.co/docs/transformers/model_doc/gemma4"},{"title":"google/gemma-4-31B · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B"},{"title":"nvidia/Gemma-4-26B-A4B-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Gemma-4-26B-A4B-NVFP4"},{"title":"Gemma 4 model overview | Google AI for Developers","url":"https://ai.google.dev/gemma/docs/core"},{"title":"google/gemma-4-26B-A4B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-26B-A4B-it"},{"title":"google/gemma-4-31B-it · Hugging Face","url":"https://huggingface.co/google/gemma-4-31B-it"},{"title":"Welcome Gemma 4: Frontier multimodal intelligence on device","url":"https://huggingface.co/blog/gemma4"},{"title":"nvidia/Gemma-4-31B-IT-NVFP4 · Hugging Face","url":"https://huggingface.co/nvidia/Gemma-4-31B-IT-NVFP4"},{"title":"google/gemma-4-E4B · Hugging Face","url":"https://huggingface.co/google/gemma-4-E4B"},{"title":"Gemma 4: Our most capable open models to date","url":"https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/"}]

Based on the search results, here's what I found regarding Gemma 4:

## Gemma 4 Model Overview

Gemma 4 is a multimodal model with pretrained and instruction-tuned variants, available in E2B, E4B, 31B and 26B-A4B (MoE) parameter sizes. 

**Important Note:** The search results do not show a 12B base model variant. The available sizes are E2B, E4B, 26B A4B, and 31B.

## Release Date

The model was added to Hugging Face Transformers on 2026-04-01.

## Model Characteristics

Gemma 4 models are multimodal, handling text and image input (with audio supported on small models) and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages.

If you were specifically looking for information about a 12B parameter model,
…[truncated 192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-18T07:12:29.442413+00:00_

Web search results for query: "Phi-4 reasoning 14B HuggingFace release date gated benchmark AIME MATH training"

Links: [{"title":"microsoft/Phi-4-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning"},{"title":"Phi-4 Local Setup: Microsoft's 14B Reasoning on 12GB GPUs | Local AI Master","url":"https://localaimaster.com/blog/phi-4-local-setup"},{"title":"microsoft/Phi-4-mini-flash-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-flash-reasoning"},{"title":"Microsoft Phi-4 Reasoning: Small Model, Big Math | Awesome Agents","url":"https://awesomeagents.ai/reviews/review-phi-4-reasoning/"},{"title":"microsoft/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-reasoning-plus"},{"title":"Phi 4 Reasoning Benchmarks, Model Specs, and Comparisons - DEV Community","url":"https://dev.to/best_codes/phi-4-reasoning-benchmarks-model-specs-and-comparisons-4hk"},{"title":"unsloth/Phi-4-reasoning-plus · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-reasoning-plus"},{"title":"unsloth/Phi-4-reasoning-GGUF · Hugging Face","url":"https://huggingface.co/unsloth/Phi-4-reasoning-GGUF"},{"title":"microsoft/Phi-4-mini-reasoning · Hugging Face","url":"https://huggingface.co/microsoft/Phi-4-mini-reasoning"},{"title":"Microsoft Launches Two Powerful Phi-4 Reasoning Models","url":"https://www.analyticsvidhya.com/blog/2025/05/phi-4-reasoning-models/"}]

Based on the search results, here's comprehensive information about Phi-4 reasoning models:

## Release Timeline

The original Phi-4 (14B) was released in December 2024 under MIT license. Phi-4-reasoning and Phi-4-reasoning-plus were released simultaneously on April 30, 2025. Phi-4-mini-flash-reasoning was released on July 9, 2025.

## Model Specifications

The core text models are Phi-4-reasoning and Phi-4-reasoning-plus, both 14B parameters with a 32K token context window. Both ship under MIT license, run locally via Ollama on a consumer GPU, an
…[truncated 826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-18T07:12:29.442642+00:00_

Here is the compiled structured report of all findings.

---

## Search 1: DeepSeek V3 Base Model

DeepSeek-V3 is **not** in the 7B-14B range. It is a large MoE model. However, the DeepSeek ecosystem includes several models that do fall in the target range.

### DeepSeek-V3 (for reference, out of range)
- **Full name:** DeepSeek-V3
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V3-Base`
- **Total parameters:** 671B (+14B MTP module = 685B total weights)
- **Active parameters:** 37B per token
- **Architecture:** MoE (256 experts)
- **Release date:** December 2024 (V3-0324 update March 2025; V3.1 and V3.2 followed)
- **Gated:** No (MIT license)
- **Base version exists:** Yes (`deepseek-ai/DeepSeek-V3-Base`)
- **Training data:** ~14.8T tokens
- **NOT in 7B-14B range**

### DeepSeek-V2-Lite (in range)
- **Full name:** DeepSeek-V2-Lite
- **HuggingFace repo:** `deepseek-ai/DeepSeek-V2-Lite`
- **Total parameters:** 15.7B
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** May 7, 2024
- **Gated:** No (MIT license)
- **Base version exists:** Yes (this IS the base version; chat version at `deepseek-ai/DeepSeek-V2-Lite-Chat`)
- **Training data:** 5.7T tokens (same pre-training corpus as DeepSeek-V2)
- **Benchmarks:** Outperforms 7B dense and 16B MoE models on many English/Chinese benchmarks (specific MMLU not retrieved)

### DeepSeek-Coder-V2-Lite-Base (in range)
- **Full name:** DeepSeek-Coder-V2-Lite-Base
- **HuggingFace repo:** `deepseek-ai/DeepSeek-Coder-V2-Lite-Base`
- **Total parameters:** 15.7B (sometimes cited as 16B)
- **Active parameters:** 2.4B per token
- **Architecture:** MoE (2 shared experts + 64 routed experts, 6 activated per token)
- **Release date:** June 2024
- **Gated:** No
- **Base version exists:** Yes (this IS the base; instruct variant at `deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct`)
- **Training data:** Not separately disclosed; code-focused extension of V2 d
…[truncated 9792 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "elapsed_ms": 27
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-18T07:12:29.442912+00:00_

Now I have comprehensive data. Here is the structured compilation of all findings.

---

## Open-Source Base LLMs (7B-14B Parameters) Released 2024-2026

### 1. Qwen3-8B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-8B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-8B-Base` |
| **Parameters** | 8B (7.6B non-embedding) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | MMLU ~74.7; performs on par with Qwen2.5-14B-Base. Top HumanEval (76.0) under 8B. Strong CJK multilingual. |

### 2. Qwen3-14B-Base (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen3-14B-Base |
| **HuggingFace Repo** | `Qwen/Qwen3-14B-Base` |
| **Parameters** | 14.8B (13.2B non-embedding), 40 layers, GQA (40 Q heads / 8 KV heads) |
| **Release Date** | May 2025 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 36T tokens, 119 languages |
| **Benchmarks** | Performs on par with Qwen2.5-32B-Base; outperforms larger Qwen2.5 in STEM, coding, reasoning. Context 32K. |

### 3. Qwen2.5-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-7B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-7B` |
| **Parameters** | 7B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | 18T tokens |
| **Benchmarks** | MMLU 74.2, MATH 49.8, HumanEval 57.9. Context 128K, generates up to 8K tokens. |

### 4. Qwen2.5-14B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-14B |
| **HuggingFace Repo** | `Qwen/Qwen2.5-14B` |
| **Parameters** | 14B |
| **Release Date** | September 2024 |
| **Gated** | No (Apache 2.0) |
| **Base Version Exists** | Yes |
| **Training Data** | Up to 18T tokens |
| **Benchmarks** | MMLU 79.7. Context 128K. |

### 5. Qwen2.5-Coder-7B (Alibaba)

| Field | Detail |
|---|---|
| **Full Name** | Qwen2.5-Coder-7B |
| **HuggingFac
…[truncated 17678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_2025-2026-base-models_20260518T070717",
  "tool": "Agent",
  "elapsed_ms": 28
}
```

</details>

---

### Assistant

_source line 187 · 2026-05-18T07:12:29.443153+00:00_

搜索完成。以下是汇总。

---

## 全部候选模型（7B-14B dense base，按推荐度排序）

| 模型 | HF Repo ID | 参数量 | 发布日期 | License | Gated | 训练数据 | MMLU (base) |
|---|---|---|---|---|---|---|---|
| **Qwen3-8B-Base** | `Qwen/Qwen3-8B-Base` | 8.2B | 2025-04 | Apache 2.0 | No | 36T tokens | 79.7 |
| **Qwen3-14B-Base** | `Qwen/Qwen3-14B-Base` | 14.8B | 2025-04 | Apache 2.0 | No | 36T tokens | 81.1 |
| **Phi-4** | `microsoft/phi-4` | 14.7B | 2024-12 | MIT | No | 9.8T tokens | 84.8 |
| **Ministral-3-8B-Base** | `mistralai/Ministral-3-8B-Base-2512` | 8.4B | 2025-12 | Apache 2.0 | No | 未公开 | 70.6 |
| **Ministral-3-14B-Base** | `mistralai/Ministral-3-14B-Base-2512` | ~14B | 2025-12 | Apache 2.0 | No | 未公开 | 79.4 |
| **Gemma 3 12B PT** | `google/gemma-3-12b-pt` | 12B | 2025-03 | Gemma ToU | **Yes** | 12T tokens | 71.9 |
| **OLMo 2 7B** | `allenai/OLMo-2-1124-7B` | 7B | 2024-11 | Apache 2.0 | No | 4T tokens | 63.7 |
| **OLMo 2 13B** | `allenai/OLMo-2-1124-13B` | 13B | 2024-11 | Apache 2.0 | No | 5T tokens | 67.5 |
| **Falcon3-10B-Base** | `tiiuae/Falcon3-10B-Base` | 10B | 2024-12 | Falcon 2.0 | No | 14T+2T | 73.1 |
| **Falcon3-7B-Base** | `tiiuae/Falcon3-7B-Base` | 7B | 2024-12 | Falcon 2.0 | No | 14T tokens | 67.4 |
| **Falcon-H1-7B-Base** | `tiiuae/Falcon-H1-7B-Base` | 7B | 2025 | Open | No | 未公开 | — |
| Qwen2.5-7B | `Qwen/Qwen2.5-7B` | 7B | 2024-09 | Apache 2.0 | No | 18T tokens | 74.2 |
| Qwen2.5-14B | `Qwen/Qwen2.5-14B` | 14B | 2024-09 | Apache 2.0 | No | 18T tokens | 79.7 |
| Mistral-Nemo-12B | `mistralai/Mistral-Nemo-Base-2407` | 12B | 2024-07 | Apache 2.0 | No | 未公开 | 68.0 |
| Llama 3.1 8B | `meta-llama/Llama-3.1-8B` | 8B | 2024-07 | Llama CLA | **Yes** | 15T tokens | 65.6 |
| Yi-1.5-9B | `01-ai/Yi-1.5-9B` | 9B | 2024-05 | Apache 2.0 | No | ~3T tokens | 76.3 |

### 排除的模型
- **Llama 4**: 全部 MoE（Scout 17B active/109B total），无 dense 7B-14B base
- **DeepSeek R2**: 未发布
- **DeepSeek V3/V4**: 671B+ MoE，远超范围
- **DeepSeek-R1-Distill-***: 是 SFT 微调模型，不是 base pretrained model，不适合做 controlled contamination injection
- **Gemma 4**: MoE 架构，无 dense 7B-14B
- **InternLM3-8B**: base checkpoint 未公开发布（仅 instruct）

---

## 推荐

### 1. 最佳 5 模型组合（全部 2024Q4-2025，全部 non-gated）

| Family | 模型 | 理由 |
|---|---|---|
| **Qwen** (Alibaba) | Qwen3-8B-Base | 2025-04，36T tokens，Apache 2.0，MMLU 79.7，直接替代 Qwen 2.5 |
| **Phi** (Microsoft) | Phi-4 | 2024-12，MIT，MMLU 84.8，14.7B 强基线 |
| **Mistral** (Mistral AI) | Ministral-3-8B-Base | 2025-12，Apache 2.0，替代 Mistral v0.3 |
| **OLMo** (Allen AI) | OLMo-2-1124-7B | 完全开源（数据+代码+权重），Apache 2.0，学术可复现性最强 |
| **Falcon** (TII) | Falcon3-10B-Base | 2024-12，14T tokens，MMLU 73.1 |

**优势**：5 个不同机构/家族，全部 non-gated，全部 2024Q4+，覆盖不同训练规模（4T-36T tokens）和能力水平（MMLU 63.7-84.8），审稿人无法质疑模型过时。

**备选**：如果想用 Google 家族替换 Falcon，可选 Gemma 3 12B PT（但 gated）。

### 2. Llama-3.1-8B 的替代

Llama 4 无 dense 7B-14B，所以 Meta 家族无直接替代。最佳替代方案按优先级：

1. **Phi-4** (14.7B) — 不同家族，MIT 开放，性能最强
2. **OLMo-2-7B** — 参数量最接近（7B），完全开源，学术论文天然认可
3. **Falcon3-10B-Base** — 不同家族，non-gated

### 3. Qwen 3 状况

**Qwen3 已发布（2025-04-29）**，有完整的 base 系列。Qwen3-8B-Base 在 36T tokens 上训练，MMLU 79.7（vs Qwen2.5-7B 的 74.2），性能已达 Qwen2.5-14B 水平。**强烈建议用 Qwen3-8B-Base 替换 Qwen 2.5**。技术报告：arXiv 2505.09388。

---

### 实际操作注意

- Phi-4 是 14.7B，bf16 下约 29.4GB，96GB GPU 做 LoRA SFT 无压力
- Ministral-3-8B-Base 是 2025-12 发布，如果论文投稿时间早于此，改用 Mistral-Nemo-Base-2407 (12B, 2024-07)
- OLMo 2 的 MMLU 偏低（63.7），但其完全开源属性在 contamination 研究中是加分项（审稿人重视可复现性）
- Falcon-H1-7B 是 hybrid SSM+Attention 架构，可能引入架构差异混淆因素，建议用 Falcon3 而非 H1

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_2025-2026-base-models_20260518T070717"
}
```

</details>

---
