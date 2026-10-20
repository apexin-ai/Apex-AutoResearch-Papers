# research phase adaptive compression lit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_research_phase-adaptive-compression-lit_20260514T022741.jsonl`
- **Structured JSON:** [`06786c26a3872ebe12ad.json`](../../sessions/06/06786c26a3872ebe12ad.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-14T02:33:30.607873+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T02:33:30.608264+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T02:33:30.608594+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T02:33:30.608975+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approx
…[truncated 5474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T02:33:30.609231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dynamic adaptive KV cache eviction strategy LLM inference 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dynamic adaptive KV cache eviction strategy LLM inference 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T02:33:30.609445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "compound sparsity interaction attention head pruning KV cache compression joint 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "compound sparsity interaction attention head pruning KV cache compression joint 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T02:33:30.609630+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "phase-dependent reasoning behavior LLM chain-of-thought exploration exploitation stages 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "phase-dependent reasoning behavior LLM chain-of-thought exploration exploitation stages 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T02:33:30.609814+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "performance inversion crossover compression strategy LLM different conditions 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "performance inversion crossover compression strategy LLM different conditions 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T02:33:30.610037+00:00_

Web search results for query: "dynamic adaptive KV cache eviction strategy LLM inference 2024 2025"

Links: [{"title":"[2407.11550] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/abs/2407.11550"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/TreeAI-Lab/Awesome-KV-Cache-Management"},{"title":"Multi-tier dynamic storage of KV cache for LLM inference under resource-constrained conditions | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02200-4"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/html/2407.11550"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/pdf/2508.06297"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference | OpenReview","url":"https://openreview.net/forum?id=tcisuhGsQZ"},{"title":"Hierarchical Adaptive Eviction for KV Cache Management in Multimodal Language Models","url":"https://arxiv.org/html/2602.02197v1"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240711550F/abstract"}]

Based on the search results, here are the key findings on dynamic adaptive KV cache eviction strategies for LLM inference in 2024-2025:

## Ada-KV: Adaptive Budget Allocation

Recent efforts aim to reduce K
…[truncated 1502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T02:33:30.610311+00:00_

Web search results for query: "compound sparsity interaction attention head pruning KV cache compression joint 2024 2025"

Links: [{"title":"A Systematic Exploration of KV Cache Compression ...","url":"https://arxiv.org/pdf/2503.11816"},{"title":"UNCOMP: Can Matrix Entropy Uncover Sparsity?","url":"https://aclanthology.org/2025.emnlp-main.209.pdf"},{"title":"SPARK: Query-Aware Unstructured Sparsity with","url":"https://arxiv.org/pdf/2508.15212"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys","url":"https://arxiv.org/html/2603.14224v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"[2505.22913] Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference","url":"https://arxiv.org/abs/2505.22913"},{"title":"Mixing Importance with Diversity: Joint Optimization for KV Cache Compression in Large Vision-Language Models","url":"https://arxiv.org/html/2510.20707"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"}]

Based on the web search results, I found several relevant research papers and approaches on KV cache compression, attention head pruning, and sparsity in 2024-2025. Here are the key findings:

## Research on Combined Sparsity and KV Cache Compression (2024-2025)

Recent methods typically operate on sparsity along a single axis—such as pruning attention heads or compressing individual dimensions, but there is growing work on joint optimization approaches.

### Joint Optimization Approaches

MixKV joint
…[truncated 1540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T02:33:30.610620+00:00_

Web search results for query: "performance inversion crossover compression strategy LLM different conditions 2024 2025"

Links: [{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"GitHub - microsoft/LLMLingua: [EMNLP'23, ACL'24] To speed up LLMs' inference and enhance LLM's perceive of key information, compress the prompt and KV-Cache, which achieves up to 20x compression with minimal performance loss. · GitHub","url":"https://github.com/microsoft/LLMLingua"},{"title":"CCF: A Context Compression Framework for Efficient Long-Sequence Language Modeling","url":"https://arxiv.org/html/2509.09199v1"},{"title":"Frontiers | A survey of model compression techniques: past, present, and future","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1518965/full"},{"title":"Better Language Model Inversion by Compactly Representing Next-Token Distributions | OpenReview","url":"https://openreview.net/forum?id=FZp6cheXt2"},{"title":"A survey of model compression techniques: past, present, and future - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11965593/"},{"title":"LLM Performance and AI Hardware: 2023–2025 Breakthroughs | by Oleksandr Kucherenko | Medium","url":"https://medium.com/@olku/llm-performance-and-ai-hardware-2023-2025-breakthroughs-fa3a1f8dc505"},{"title":"GitHub - HuangOwen/Awesome-LLM-Compression: Awesome LLM compression research papers and tools. · GitHub","url":"https://github.com/HuangOwen/Awesome-LLM-Compression"},{"title":"Compression Laws for Large Language Models","url":"https://arxiv.org/pdf/2504.04342"},{"title":"A Survey of Efficient LLM Inference Serving","url":"https://aclanthology.org/2025.inlg-main.32.pdf"}]

Based on the search results, here's what I found regarding LLM compression strategies and different conditions in 2024-2025:

## Overvi
…[truncated 1698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T02:33:30.610899+00:00_

Web search results for query: "phase-dependent reasoning behavior LLM chain-of-thought exploration exploitation stages 2024 2025"

Links: [{"title":"Reasoning in Large Language Models: From Chain-of-Thought to Massively Decomposed Agentic Processes[v1] | Preprints.org","url":"https://www.preprints.org/manuscript/202512.2242"},{"title":"NeurIPS Poster Can Language Models Perform Robust Reasoning in Chain-of-thought Prompting with Noisy Rationales?","url":"https://neurips.cc/virtual/2024/poster/95956"},{"title":"[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models","url":"https://arxiv.org/abs/2201.11903"},{"title":"What Makes a Good Reasoning Chain? Uncovering ...","url":"https://aclanthology.org/2025.emnlp-main.329.pdf"},{"title":"A Survey of Chain-of-X Paradigms for LLMs","url":"https://aclanthology.org/2025.coling-main.719.pdf"},{"title":"Toward large reasoning models: A survey of reinforced reasoning with large language models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12546433/"},{"title":"arXiv:2507.03327v1 [cs.CL] 4 Jul 2025 Preprint. Under review.","url":"https://arxiv.org/pdf/2507.03327"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Towards Reasoning Era: A Survey of Long Chain-of-Thought","url":"https://long-cot.github.io/"},{"title":"Breaking the Reasoning Barrier A Survey on LLM Complex ...","url":"https://aclanthology.org/2025.findings-acl.386.pdf"}]

Based on the search results, here's what I found regarding phase-dependent reasoning behavior in LLMs with chain-of-thought exploration/exploitation stages in 2024-2025:

## Key Research Findings

### Exploration-Exploitation in Chain-of-Thought Reasoning

Research demonstrates that chain-of-thought prompting with noisy rationales follows a principle of exploration and exploitation: (1) rephrasing and selecting rationales in the input spa
…[truncated 1600 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T02:33:30.611141+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LServe sparse attention low-bit KV cache joint compression 2025 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LServe sparse attention low-bit KV cache joint compression 2025 LLM"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T02:33:30.611320+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"phase transition\" pruning sparsity threshold LLM catastrophic collapse 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"phase transition\" pruning sparsity threshold LLM catastrophic collapse 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T02:33:30.611526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "token importance shift reasoning steps LLM attention pattern change during generation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "token importance shift reasoning steps LLM attention pattern change during generation 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T02:33:30.611709+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DuoAttention RazorAttention layer-aware KV cache budget allocation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DuoAttention RazorAttention layer-aware KV cache budget allocation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T02:33:30.611944+00:00_

Web search results for query: "LServe sparse attention low-bit KV cache joint compression 2025 LLM"

Links: [{"title":"Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys","url":"https://arxiv.org/html/2603.14224v1"},{"title":"[2502.14866] LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention","url":"https://arxiv.org/abs/2502.14866"},{"title":"GitHub - mit-han-lab/omniserve: [MLSys'25] QServe: W4A8KV4 Quantization and System Co-design for Efficient LLM Serving; [MLSys'25] LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention · GitHub","url":"https://github.com/mit-han-lab/omniserve"},{"title":"LSERVE: EFFICIENT LONG-SEQUENCE LLM SERVING WITH UNIFIED SPARSE ATTENTION","url":"https://arxiv.org/pdf/2502.14866"},{"title":"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention","url":"https://hanlab.mit.edu/projects/lserve"},{"title":"1 Introduction","url":"https://arxiv.org/html/2502.14866v2"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget | OpenReview","url":"https://openreview.net/forum?id=9HK2rHNAhd"},{"title":"SALS: Sparse Attention in Latent Space for KV cache Compression","url":"https://arxiv.org/pdf/2510.24273"},{"title":"LServe: system for faster long-sequence LLM serving via hybrid sparse attention | by SACHIN KUMAR | Medium","url":"https://medium.com/@techsachin/lserve-system-for-faster-long-sequence-llm-serving-via-hybrid-sparse-attention-a3b10c50256f"},{"title":"Oaken: Fast and Efficient LLM Serving with Online-Offline ...","url":"https://jongse-park.github.io/files/paper/2025-isca-oaken.pdf"}]

Based on the search results, here's what I found about LServe and sparse attention with low-bit KV cache compression for LLMs:

## LServe Overview

LServe is an efficient system that accelerates long-sequence LLM serving via hybrid sparse attention, unifying different hardware-friendly, structured sparsity patterns for both prefilling 
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T02:33:30.612225+00:00_

Web search results for query: ""phase transition" pruning sparsity threshold LLM catastrophic collapse 2025 2026"

Links: [{"title":"Phase transitions in large language model compression | npj Artificial Intelligence","url":"https://www.nature.com/articles/s44387-026-00072-8"},{"title":"Phase Transitions in Neural Networks Pruning","url":"https://arxiv.org/html/2602.15224"},{"title":"Mitigating Catastrophic Forgetting in Large Language ...","url":"https://aclanthology.org/2025.emnlp-main.1108.pdf"},{"title":"GitHub - whucs21Mzy/Model-Phase-Transitions: Navigating Model Phase Transitions to Enable Extreme Lossless Compression: A Perspective","url":"https://github.com/whucs21Mzy/Model-Phase-Transitions"},{"title":"CFSP: An Efficient Structured Pruning Framework for LLMs ...","url":"https://aclanthology.org/2025.coling-main.626.pdf"},{"title":"ICLR 2025 Workshop on Sparsity in LLMs (SLLM)","url":"https://arxiv.org/pdf/2503.04992v2"},{"title":"(PDF) Modeling Pruning as a Phase Transition: A Thermodynamic Analysis of Neural Activations","url":"https://www.researchgate.net/publication/398817442_Modeling_Pruning_as_a_Phase_Transition_A_Thermodynamic_Analysis_of_Neural_Activations"},{"title":"Scaling with Collapse: Efficient and Predictable Training of LLM Families","url":"https://arxiv.org/html/2509.25087v1"},{"title":"A review of state-of-the-art techniques for large language model compression | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02019-z"},{"title":"Mitigating Catastrophic Forgetting in Large Language Models with Forgetting-aware Pruning","url":"https://arxiv.org/html/2509.08255"}]

Based on the web search results, I found substantial recent research on phase transitions in LLM pruning and sparsity thresholds. Here are the key findings:

## Phase Transition Points in LLM Compression

All compression methods converge toward a universal phase transition boundary where aggressive compression trigg
…[truncated 1583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T02:33:30.612513+00:00_

Web search results for query: "token importance shift reasoning steps LLM attention pattern change during generation 2024 2025"

Links: [{"title":"State of AI 2025: 100T Token LLM Usage Study | OpenRouter","url":"https://openrouter.ai/state-of-ai"},{"title":"LLM Fundamentals — Tokens, Attention & Transformers (2026) | MyEngineeringPath","url":"https://myengineeringpath.dev/genai-engineer/llm-fundamentals/"},{"title":"Extending Token Computation for LLM Reasoning | Proceedings of the 2024 8th International Conference on Computer Science and Artificial Intelligence","url":"https://dl.acm.org/doi/10.1145/3709026.3709050"},{"title":"Think Clearly: Improving Reasoning via Redundant Token Pruning","url":"https://choidae1.github.io/assets/publications/think-clearly/Thinking_Clearly__Enhancing_Reasoning_with_Redundant_Token_Pruning.pdf"},{"title":"Rethinking Thinking Tokens: LLMs as Improvement Operators","url":"https://arxiv.org/html/2510.01123v1"},{"title":"Preprint version THINK-AT-HARD: SELECTIVE LATENT ITERATIONS TO","url":"https://nicsefc.ee.tsinghua.edu.cn/nics_file/pdf/c1a5580e-cabe-4d31-b7b3-f01d3d3ba6db.pdf"},{"title":"[2403.14932] Extending Token Computation for LLM Reasoning","url":"https://arxiv.org/abs/2403.14932"},{"title":"Data Mining and Machine Learning Lab Is Chain-of-Thought Reasoning of LLMs a","url":"https://arxiv.org/pdf/2508.01191"},{"title":"LLM Wrapped 2025 - Danial Amin","url":"https://danial-amin.github.io/pages/articles/2025-12-07-llm-wrapped-2025.html"},{"title":"Improving Reasoning via Redundant Token Pruning","url":"https://aclanthology.org/2025.findings-emnlp.1169.pdf"}]

Based on the search results, here's what I found about token importance shifts and attention pattern changes in LLM reasoning during generation:

## Key Findings on Token Importance and Attention Patterns

**Attention Inefficiencies in Reasoning:**

Large Language Models often struggle with complex reasoning tasks due to inefficient attention distributions, and researchers 
…[truncated 1543 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T02:33:30.612787+00:00_

Web search results for query: "DuoAttention RazorAttention layer-aware KV cache budget allocation 2024 2025"

Links: [{"title":"Published in Transactions on Machine Learning Research (05/2025)","url":"https://openreview.net/pdf?id=z3JZzu9EA3"},{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget ...","url":"https://arxiv.org/pdf/2407.11550"},{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/html/2603.20616"},{"title":"RazorAttention: Efficient KV Cache Compression Through Retrieval Heads | OpenReview","url":"https://openreview.net/forum?id=tkiZQlL04w"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget | OpenReview","url":"https://openreview.net/forum?id=9HK2rHNAhd"},{"title":"More Tokens, Lower Precision: Towards the Optimal Token-Precision Trade-off in KV Cache Compression","url":"https://arxiv.org/html/2412.12706v1"},{"title":"RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression","url":"https://arxiv.org/html/2502.14051v3"},{"title":"KV Cache Compression for Inference Efficiency in LLMs: A Review","url":"https://arxiv.org/html/2508.06297v1"},{"title":"GitHub - TreeAI-Lab/Awesome-KV-Cache-Management: This repository serves as a comprehensive survey of LLM development, featuring numerous research papers along with their corresponding code links. · GitHub","url":"https://github.com/treeai-lab/awesome-kv-cache-management"}]

Based on the web search results, here's what I found about DuoAttention, RazorAttention, and layer-aware KV cache budget allocation:

## DuoAttention

DuoAttention introduces a parameterized approach to distinguish between two types of attention heads. DuoAttention uses a rigid binary classification (Retrieval vs. Streaming) for KV c
…[truncated 1484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T02:33:30.613032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SqueezeAttention layer-wise optimal budget KV cache 2D management 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SqueezeAttention layer-wise optimal budget KV cache 2D management 2025"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T02:33:30.613217+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking tokens\" \"reasoning phase\" attention sparsity budget allocation LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking tokens\" \"reasoning phase\" attention sparsity budget allocation LLM 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T02:33:30.613387+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MixedDimKV beyond token eviction mixed dimension budget KV cache 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MixedDimKV beyond token eviction mixed dimension budget KV cache 2026"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T02:33:30.613701+00:00_

Web search results for query: "SqueezeAttention layer-wise optimal budget KV cache 2D management 2025"

Links: [{"title":"[2404.04793] SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://arxiv.org/abs/2404.04793"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget | OpenReview","url":"https://openreview.net/forum?id=9HK2rHNAhd"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://arxiv.org/html/2404.04793v1"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/3b0a8df568ec496a717566a7f8158aaa-Abstract-Conference.html"},{"title":"ICLR Poster SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://iclr.cc/virtual/2025/poster/30707"},{"title":"GitHub - hetailang/SqueezeAttention","url":"https://github.com/hetailang/squeezeattention?__from__=talkingdev"},{"title":"Published as a conference paper at ICLR 2025 SQUEEZEATTENTION: 2D MANAGEMENT","url":"https://openreview.net/pdf?id=9HK2rHNAhd"},{"title":"Paper page - SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://huggingface.co/papers/2404.04793"},{"title":"SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/squeezeattention-2d-management-kv-cache-llm-inference"},{"title":"[Quick Review] SqueezeAttention: 2D Management of KV-Cache in LLM Inference via Layer-wise Optimal Budget","url":"https://liner.com/review/squeezeattention-2d-management-of-kvcache-in-llm-inference-via-layerwise"}]

Based on the search results, I found comprehensive information about SqueezeAttention:

## Overview

SqueezeAttention is a method for optimizing 
…[truncated 1306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T02:33:30.613943+00:00_

Web search results for query: "MixedDimKV beyond token eviction mixed dimension budget KV cache 2026"

Links: [{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/html/2603.20616"},{"title":"[2603.20616] Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/abs/2603.20616"},{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation","url":"https://arxiv.org/pdf/2603.20616"},{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"Paper page - IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs","url":"https://huggingface.co/papers/2604.10539"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"No Token Left Behind: Reliable KV Cache Compression via Importance-Aware Mixed Precision Quantization","url":"https://arxiv.org/html/2402.18096"},{"title":"RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory","url":"https://arxiv.org/html/2605.06675"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v1"}]

Based on my web search results, I found comprehensive information about MixedDimKV and related KV cache compression research from 2026.

## Overview of MixedDimKV

MixedDimKV is a mixed-dimension KV cache compression method that allocates dimensions to tokens at a more granular level, with MixedDimKV-H further integrating head-level importance information.

## Key Innovation

The core innovation of MixedDimKV goes beyond traditional token eviction methods. Existing token eviction methods reduce memory by discarding le
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T02:33:30.614214+00:00_

Web search results for query: ""thinking tokens" "reasoning phase" attention sparsity budget allocation LLM 2025 2026"

Links: [{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=E1FrjgaG1J"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=2i6Rp0gCq6"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://aclanthology.org/2025.findings-acl.1274.pdf"},{"title":"arXiv:2412.18547v5 [cs.CL] 2 Jun 2025 Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/pdf/2412.18547"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens | OpenReview","url":"https://openreview.net/forum?id=ahatk5qrmB"},{"title":"Token-Budget-Aware LLM Reasoning","url":"https://arxiv.org/html/2412.18547v4"},{"title":"Token-Budget-Aware LLM Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1274/"},{"title":"BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens","url":"https://arxiv.org/html/2508.17196v1"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf"}]

I've completed the web search for your query about "thinking tokens," "reasoning phase," "attention sparsity," and "budget allocation" in LLMs for 2025-2026. Here are the key findings:

## Key Research Areas

### Thinking Tokens and Reasoning Dynamics
Thinking tokens are tokens expressing reflection or transition, such as "Hmm", "Wait" and "Therefore," which are crucial for LRM's reasoning performance while other tokens have minimal impacts. Research observes an MI peaks phenomenon where mutual information between intermediate representations and the correct answer 
…[truncated 1497 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T02:33:30.614471+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RaaS reasoning-aware attention sparsity milestone tokens importance decay ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RaaS reasoning-aware attention sparsity milestone tokens importance decay ACL 2025"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T02:33:30.614665+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LKV end-to-end learning head-wise budget token selection KV cache eviction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LKV end-to-end learning head-wise budget token selection KV cache eviction 2025"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T02:33:30.614819+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Twilight adaptive attention sparsity hierarchical top-p pruning NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Twilight adaptive attention sparsity hierarchical top-p pruning NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T02:33:30.614941+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking tokens\" \"information peaks\" mutual information reasoning LLM ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking tokens\" \"information peaks\" mutual information reasoning LLM ICLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T02:33:30.615106+00:00_

Web search results for query: "Twilight adaptive attention sparsity hierarchical top-p pruning NeurIPS 2025"

Links: [{"title":"NeurIPS Poster Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning","url":"https://neurips.cc/virtual/2025/poster/117668"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning | OpenReview","url":"https://openreview.net/forum?id=Ve693NkzcU"},{"title":"GitHub - tsinghua-ideal/Twilight: [NeurIPS'25 Spotlight] Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"https://github.com/tsinghua-ideal/Twilight"},{"title":"[2502.02770] Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning","url":"https://arxiv.org/abs/2502.02770"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-𝑝 Pruning","url":"https://arxiv.org/html/2502.02770v1"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"https://openreview.net/pdf/690f5f6390bd74e24fcac72c3bcf39e1a480e996.pdf"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning","url":"http://people.iiis.tsinghua.edu.cn/~gaomy/pubs/twilight.neurips25.pdf"},{"title":"Tsinghua IDEAL · GitHub","url":"https://github.com/tsinghua-ideal"},{"title":"dblp: Twilight: Adaptive Attention Sparsity with Hierarchical Top-&lt;i>p&lt;/i> Pruning.","url":"https://dblp.org/rec/journals/corr/abs-2502-02770.html"},{"title":"Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning | Efficient AI","url":"https://research.nvidia.com/labs/eai/publication/twilight/"}]

I found comprehensive information about Twilight from NeurIPS 2025. Here's what the research presents:

## Overview

Twilight is a framework that enhances any existing sparse attention algorithm with adaptive budget decision capabilities without sacrificing accuracy. It's a NeurIPS 2025 spotlight paper that exploits KV cache sparsity efficiently and dynamically through Top-P sampling.

## Problem and Key In
…[truncated 1159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T02:33:30.615292+00:00_

Web search results for query: "RaaS reasoning-aware attention sparsity milestone tokens importance decay ACL 2025"

Links: [{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient ...","url":"https://aclanthology.org/2025.findings-acl.131.pdf"},{"title":"[2502.11147] RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/abs/2502.11147"},{"title":"RaaS: Reasoning-Aware Attention Sparsity for Efficient LLM Reasoning","url":"https://arxiv.org/html/2502.11147v2"},{"title":"Accepted Findings Papers - ACL 2025","url":"https://2025.aclweb.org/program/find_papers/"},{"title":"Efficient Long-Decoding Inference with Reasoning-Aware Attention Sparsity","url":"https://arxiv.org/html/2502.11147v1"},{"title":"ACL 2025 — My First Dive into the NLP Universe | by Nikhil Verma | Medium","url":"https://lih-verma.medium.com/acl-2025-my-first-dive-into-the-nlp-universe-c9fc0ae809b1"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2100&show=25"},{"title":"DeepSeek's Liang Wenfeng & Peking University's Yang Yaodong's Team Win Best Paper Award at ACL 2025 with NSA Paper","url":"https://eu.36kr.com/en/p/3401632759482502"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1126/"}]

Based on the web search results, I found detailed information about the RaaS paper:

## RaaS: Reasoning-Aware Attention Sparsity

RaaS identifies a new attention pattern during the decode stage of reasoning tasks, where milestone tokens (analogous to lemmas in mathematical proofs) emerge, are utilized, and then become unimportant afterward. The algorithm identifies milestone tokens and retains their KV vectors until they are no longer needed, achieving high accuracy with O(L) time and O(L) memo
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T02:33:30.615509+00:00_

Web search results for query: "LKV end-to-end learning head-wise budget token selection KV cache eviction 2025"

Links: [{"title":"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/html/2605.06676"},{"title":"[2605.06676] LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction","url":"https://arxiv.org/abs/2605.06676"},{"title":"Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression","url":"https://arxiv.org/html/2603.20616"},{"title":"GitHub - FFY0/AdaKV: The Official Implementation of Ada-KV [NeurIPS 2025] · GitHub","url":"https://github.com/FFY0/AdaKV"},{"title":"Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/html/2407.11550"},{"title":"Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs","url":"https://arxiv.org/html/2512.03324v2"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget ...","url":"https://aclanthology.org/2025.findings-emnlp.737.pdf"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation","url":"https://arxiv.org/html/2509.09754v1"},{"title":"KV Cache Strategies for LLM Efficiency","url":"https://www.emergentmind.com/topics/kv-cache-strategy"},{"title":"ICLR LLMs Know What to Drop: Self-Attention Guided KV Cache Eviction for Efficient Long-Context Inference","url":"https://iclr.cc/virtual/2025/33493"}]

Based on the search results, I found comprehensive information about LKV:

## LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction

LKV (Learned KV Eviction) is the first framework that reformulates KV cache compression as a unified, end-to-end differentiable optimization problem.

### Key Components

LKV introduces LKV-H, a global budgeting mechanism that uncovers intrinsic head importance, and LKV-T, a matrix-free selector for efficient inference
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T02:33:30.615715+00:00_

Web search results for query: ""thinking tokens" "information peaks" mutual information reasoning LLM ICLR 2026"

Links: [{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=E1FrjgaG1J"},{"title":"[2506.02867] Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://arxiv.org/abs/2506.02867"},{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://arxiv.org/html/2506.02867v1"},{"title":"[Literature Review] Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://www.themoonlight.io/en/review/demystifying-reasoning-dynamics-with-mutual-information-thinking-tokens-are-information-peaks-in-llm-reasoning"},{"title":"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.02867v1"},{"title":"Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://openreview.net/pdf/c3c72e4c1f8357c9104201b84b6fba745157bb28.pdf"},{"title":"[2506.02867v2] Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks in LLM Reasoning","url":"https://arxiv.org/abs/2506.02867v2"},{"title":"Rohan Paul on X: \"Large Reasoning Models' (LRMs) internal reasoning process is poorly understood. This paper uses mutual information to identify \"thinking tokens\" as crucial steps. Methods 🔧: → Representation Recycling reuses informative states at Mutual Information peaks by re-feeding them https://t.co/e72Q9EPfFN\" / X","url":"https://x.com/rohanpaul_ai/status/1930785755162358271"},{"title":"Dongrui Liu, Shanghai Jiao Tong University, Shanghai AI Lab","url":"https://shenqildr.github.io/"},{"title":"Demyst
…[truncated 1880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T02:33:30.615932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LAVa layer-wise KV cache eviction dynamic budget allocation EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LAVa layer-wise KV cache eviction dynamic budget allocation EMNLP 2025"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T02:33:30.616061+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "importance-based eviction fails high compression KV cache retrieval failure degradation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "importance-based eviction fails high compression KV cache retrieval failure degradation 2025"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T02:33:30.616178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"taming fragility\" KV cache eviction irreversible failure token loss 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"taming fragility\" KV cache eviction irreversible failure token loss 2025"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T02:33:30.616337+00:00_

Web search results for query: "LAVa layer-wise KV cache eviction dynamic budget allocation EMNLP 2025"

Links: [{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.737/"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget ...","url":"https://aclanthology.org/2025.findings-emnlp.737.pdf"},{"title":"[2509.09754] LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation","url":"https://arxiv.org/abs/2509.09754"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation","url":"https://arxiv.org/html/2509.09754v1"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250909754S/abstract"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation Yiqun Shen12*","url":"https://arxiv.org/pdf/2509.09754"},{"title":"Reformulating KV Cache Eviction Problem for Long-Context LLM Inference","url":"https://arxiv.org/html/2605.07234"},{"title":"GitHub - October2001/Awesome-KV-Cache-Compression: 📰 Must-read papers on KV Cache Compression (constantly updating 🤗).","url":"https://github.com/October2001/Awesome-KV-Cache-Compression"},{"title":"[2407.11550] Ada-KV: Optimizing KV Cache Eviction by Adaptive Budget Allocation for Efficient LLM Inference","url":"https://arxiv.org/abs/2407.11550"},{"title":"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation","url":"https://www.researchgate.net/publication/395473960_LAVa_Layer-wise_KV_Cache_Eviction_with_Dynamic_Budget_Allocation"}]

Based on the search results, I found comprehensive information about LAVa. Here's what I discovered:

## LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation

LAVa is the first unified strategy for cache eviction and dynamic budget allocation that, unlike prior methods, does not rely on training or the combination of multiple strategies. The paper was publis
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T02:33:30.616584+00:00_

Web search results for query: ""taming fragility" KV cache eviction irreversible failure token loss 2025"

Links: [{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"[2510.13334] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/abs/2510.13334"},{"title":"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=nJgS06sX3O"},{"title":"GitHub - FFY0/DefensiveKV: Official Implementation for [ICLR26] DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference · GitHub","url":"https://github.com/FFY0/DefensiveKV"},{"title":"DEFENSIVEKV: TAMING THE FRAGILITY OF KV CACHE ...","url":"https://openreview.net/pdf?id=nJgS06sX3O"},{"title":"TAMING THE FRAGILITY OF KV CACHE EVICTION","url":"https://openreview.net/pdf/2d8c7805c4fcdb477dd04f7b60dd05bd9551c246.pdf"},{"title":"[PDF] Taming the Fragility of KV Cache Eviction in LLM Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Taming-the-Fragility-of-KV-Cache-Eviction-in-LLM-Feng-Guo/10b323b80b3f57a7f15d44eb5a72872a3adfbcb3"},{"title":"(PDF) Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.researchgate.net/publication/396517805_Taming_the_Fragility_of_KV_Cache_Eviction_in_LLM_Inference"},{"title":"KV CACHE","url":"https://openreview.net/pdf/4f90ebf4b448b894eca910de4dd1aebff9c26579.pdf"},{"title":"[Literature Review] Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://www.themoonlight.io/en/review/taming-the-fragility-of-kv-cache-eviction-in-llm-inference"}]

I found comprehensive results for your search query. Here's what I found:

## "Taming the Fragility of KV Cache Eviction in LLM Inference"

The paper addresses how large language models face substantial memory and runtime overhead from the transformer's Key-Value cache, with recent methods employing a scoring-aggre
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T02:33:30.616775+00:00_

Web search results for query: "importance-based eviction fails high compression KV cache retrieval failure degradation 2025"

Links: [{"title":"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction","url":"https://arxiv.org/html/2605.04075"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"KV CACHE","url":"https://openreview.net/pdf/4f90ebf4b448b894eca910de4dd1aebff9c26579.pdf"},{"title":"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics","url":"https://arxiv.org/html/2603.01426"},{"title":"KV Cache Eviction in Transformer LLMs","url":"https://www.emergentmind.com/topics/kv-cache-eviction"},{"title":"HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference","url":"https://arxiv.org/html/2601.13684v1"},{"title":"Taming the Fragility of KV Cache Eviction in LLM Inference","url":"https://arxiv.org/html/2510.13334v1"},{"title":"[2512.14946] EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving","url":"https://arxiv.org/abs/2512.14946"},{"title":"Published as preprint paper G-KV: DECODING-TIME KV CACHE EVICTION WITH","url":"https://arxiv.org/pdf/2512.00504"},{"title":"Achieving More Consistent KV Cache Eviction via Pseudo ...","url":"https://aclanthology.org/2025.emnlp-main.1732.pdf"}]

I've performed a web search on the topic of importance-based eviction, KV cache compression, and retrieval failures in 2025. Here are the key findings:

## Key Research Findings

Conventional importance-based eviction methods suffer from abrupt performance degradation when the cache budget is restricted to extremely low ratios (e.g., 5%–10%).

### Failure Modes

Sharp decline in performance with cache eviction contrasts with previous reports suggesting that up to 80% of the KV cache could be evicted with minimal impact on performance. Issues arise during the generation phase due to c
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T02:33:30.616951+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"pitfalls of KV cache compression\" attention score metric failure 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"pitfalls of KV cache compression\" attention score metric failure 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T02:33:30.617073+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NSA native sparse attention DeepSeek hardware-aligned trainable sparse ACL 2025 best paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NSA native sparse attention DeepSeek hardware-aligned trainable sparse ACL 2025 best paper"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T02:33:30.617229+00:00_

Web search results for query: "NSA native sparse attention DeepSeek hardware-aligned trainable sparse ACL 2025 best paper"

Links: [{"title":"[2502.11089] Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/abs/2502.11089"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1126/"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively","url":"https://arxiv.org/pdf/2502.11089"},{"title":"Paper page - Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://huggingface.co/papers/2502.11089"},{"title":"DeepSeek's Liang Wenfeng & Peking University's Yang Yaodong's Team Win Best Paper Award at ACL 2025 with NSA Paper","url":"https://eu.36kr.com/en/p/3401632759482502"},{"title":"Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://arxiv.org/html/2502.11089v1"},{"title":"Hardware-Aligned and Natively Trainable Sparse Attention","url":"https://aclanthology.org/2025.acl-long.1126.pdf"},{"title":"AI on AI: Sparse Attention, from NSA to DSA – Champaign Magazine","url":"https://champaignmagazine.com/2025/09/30/ai-on-ai-sparse-attention-from-nsa-to-dsa/"},{"title":"DeepSeek on X: \"🚀 Introducing NSA: A Hardware-Aligned and Natively Trainable Sparse Attention mechanism for ultra-fast long-context training &amp; inference! Core components of NSA: • Dynamic hierarchical sparse strategy • Coarse-grained token compression • Fine-grained token selection 💡 With https://t.co/zjXuBzzDCp\" / X","url":"https://x.com/deepseek_ai/status/1891745487071609327?lang=en"},{"title":"DeepSeek's Next-Generation Technology Wins the ACL 2025 Best Paper Award, Enhancing Long-Text Processing Efficiency by 11 Times!","url":"https://news.aibase.com/news/20107"}]

Based on the search results, I found comprehensive information about the NSA paper and its A
…[truncated 1482 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T02:33:30.617432+00:00_

Web search results for query: ""pitfalls of KV cache compression" attention score metric failure 2025 arXiv"

Links: [{"title":"[2510.00636] Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/abs/2510.00636"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention from Future Queries Distribution","url":"https://arxiv.org/html/2510.00636v1"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention","url":"https://arxiv.org/pdf/2510.00636"},{"title":"Preprint THE PITFALLS OF KV CACHE COMPRESSION","url":"https://arxiv.org/pdf/2510.00231"},{"title":"Expected Attention: KV Cache Compression by Estimating Attention From Future Queries Distribution | OpenReview","url":"https://openreview.net/forum?id=VmojW15eRc"},{"title":"[2510.00231] The Pitfalls of KV Cache Compression","url":"https://arxiv.org/abs/2510.00231"},{"title":"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression","url":"https://arxiv.org/html/2602.02199"},{"title":"Decoding-Time KV Cache Eviction with Global Attention","url":"https://arxiv.org/pdf/2512.00504"},{"title":"GitHub - NVIDIA/kvpress: LLM KV cache compression made easy · GitHub","url":"https://github.com/NVIDIA/kvpress"},{"title":"Understanding the Physics of Key-Value Cache Compression for LLMs through Attention Dynamics","url":"https://arxiv.org/html/2603.01426"}]

Based on the search results, I found highly relevant recent research on this topic from 2025:

## Key Findings on KV Cache Compression Pitfalls

### Attention Score Metric Limitations

While attention-score-based KV cache pruning shows promise, it faces critical practical limitations: attention scores from future tokens are unavailable during compression, and modern implementations like Flash Attention do not materialize the full attention matrix, making past scores inaccessible.

Metrics like attention score exhibit sparse spikes, and these spikes often
…[truncated 1100 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T02:33:30.617643+00:00_

called mcp__agent-ml-research__save_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "literature_scan_phase_adaptive.md",
  "content": "# Literature Scan: Phase-Adaptive Compound Compression\n\n**Date**: 2026-05-14  \n**Focus**: Papers (2024–2026) relevant to phase-gated compound sparsity and the magnitude crossover phenomenon\n\n---\n\n## 1. Phase-Adaptive / Dynamic Compression\n\n### 1.1 Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\n- **Authors**: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\n- **Venue**: NeurIPS 2025 Spotlight\n- **Core**: Uses top-p sampling idea to adaptively decide per-token/per-step attention budget — prunes up to 98% tokens dynamically\n- **Relation**: **Support** — demonstrates that fixed budget is suboptimal and adaptive per-step budget is superior, but operates at token level within a single sparsity axis (no compound interaction)\n- **Gap**: Does not address compound sparsity or phase-dependent metric switching\n\n### 1.2 LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\n- **Authors**: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\n- **Venue**: EMNLP 2025 Findings\n- **Core**: First unified strategy for cache eviction + dynamic budget via Layer Attention Output Loss; discovers that layer budgets matter for generation, head budgets for extraction\n- **Relation**: **Support** — task-conditional budget allocation aligns with our per-phase budget idea; but no temporal/phase axis\n- **Gap**: Budget allocation is static per task type, not dynamic across reasoning phases\n\n### 1.3 LKV: End-to-End Learning of Head-wise Budgets and Token Selection\n- **Authors**: (arXiv 2605.06676)\n- **Venue**: arXiv 2026\n- **Core**: First end-to-end differentiable framework for jointly learning head budgets (LKV-H) and token selection (LKV-T), replacing all heuristics\n- **Relation**: **Orthogonal/Complement** — learned budget allocation is the mechanism we need; could serve as backbone for phase-gated controller\n- **Gap**: Does not model temporal phase transitions; budget is learned offline, not adapted per generation step\n\n### 1.4 SOL: Self-Optimizing Language Models — Compute Where it Counts\n- **Venue**: arXiv 2605.10875, 2026\n- **Core**: Learns per-token compute allocation policy (easy tokens less compute, hard tokens more)\n- **Relation**: **Methodological parallel** — per-token adaptive allocation analogous to per-phase adaptive compression; validates learned controller approach\n\n### 1.5 Token-Budget-Aware LLM Reasoning\n- **Venue**: ACL 2025 Findings\n- **Core**: LLMs can adaptively allocate thinking budget per query difficulty using self-consistency as proxy\n- **Relation**: **Support** — reasoning budget should vary; directly supports phase-adaptive compression for reasoning models\n\n### 1.6 BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens\n- **Venue**: arXiv 2508.17196, 2025\n- **Core**: Inserts special control tokens to inform model of remaining token budget; two-stage SFT+RL pipeline\n- **Relation**: **Orthogonal** — budget-aware generation from compute perspective; could inspire phase-transition signaling tokens\n\n---\n\n## 2. Compound/Joint Sparsity Interaction\n\n### 2.1 SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\n- **Venue**: AAAI 2026\n- **Core**: Reports compound KV cache sparsity (channel + token) produces **super-additive degradation** (ThinK+SnapKV退化65%)\n- **Relation**: **Direct competitor** — first to quantify compound super-additivity; our work extends this with phase-dependent analysis\n\n### 2.2 SLiM: One-shot Quantization and Sparsity with Low-rank Approximation\n- **Authors**: Mozaffari et al.\n- **Venue**: ICML 2025\n- **Core**: Q+S aggregated error is non-additive; uses low-rank adapter to compensate compound compression error\n- **Relation**: **Support** — independently confirms non-additive compound error; complementary framework for error compensation\n\n### 2.3 LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\n- **Venue**: MLSys 2025\n- **Core**: Integrates sparse attention + low-bit KV cache quantization into single GPU kernel; treats them as separate components without joint optimization\n- **Relation**: **Background** — demonstrates industrial need for compound compression; lacks interaction analysis\n\n### 2.4 GRASPrune: Global Gating for Budgeted Structured Pruning\n- **Authors**: Wang et al.\n- **Venue**: ACL 2026 Main\n- **Core**: Learned gate scores for joint pruning of FFN channels + KV head groups under global budget\n- **Relation**: **Direct competitor** — joint pruning with learned gates; but static (no phase adaptation)\n\n### 2.5 Compression Ordering: A Systematic Study\n- **Venue**: arXiv 2511.19495, 2025\n- **Core**: P→KD→Q ordering is optimal; quantization-first causes irreversible information loss; interaction depends on ordering\n- **Relation**: **Support** — ordering matters for compound compression; our phase-gating is a temporal ordering dimension\n\n### 2.6 EVICPRESS: Joint KV-Cache Compression and Eviction\n- **Venue**: arXiv 2512.14946, 2025\n- **Core**: Jointly optimizes eviction and compression (quantization) for KV cache\n- **Relation**: **Method-component** — joint optimization within KV cache; single-axis temporal, no head pruning compound\n\n---\n\n## 3. Reasoning-Phase-Dependent Model Behavior\n\n### 3.1 RaaS: Reasoning-Aware Attention Sparsity\n- **Venue**: ACL 2025 Findings\n- **Core**: Discovers **milestone tokens** in reasoning — tokens that emerge, become important, then fade permanently. Achieves O(L) time+memory for reasoning tasks\n- **Relation**: **Strong support** — directly demonstrates phase-dependent token importance dynamics; \"first important then not\" pattern is a specific case of our phase-dependent importance observation\n- **Gap**: Only considers single eviction dimension; does not study compound interaction\n\n### 3.2 Demystifying Reasoning Dynamics: Thinking Tokens are Information Peaks\n- **Venue**: NeurIPS 2025\n- **Core**: MI between intermediate representations and correct answer exhibits **sudden peaks** at thinking tokens (\"Hmm\", \"Wait\", \"Therefore\"); these tokens are disproportionately important\n- **Relation**: **Strong support** — reasoning has discrete information-critical phases; compression during peaks would be catastrophic, compression between peaks could be aggressive\n- **Gap**: Information-theoretic analysis only; no compression/sparsity experiments\n\n### 3.3 Decision Representation Transitions in Layer-Pruned LLMs\n- **Venue**: arXiv 2605.07271, 2026\n- **Core**: Layer pruning reveals Silent/Decisive Phase; Decision Margin undergoes **sign reversal** (negative→positive) at Transition Point\n- **Relation**: **Strong support** — sign reversal in pruning sensitivity is directly analogous to our magnitude crossover; pruning Silent Phase崩溃 vs Decisive Phase安全\n- **Gap**: Layer pruning (spatial), not temporal phase during generation\n\n### 3.4 Doing More With Less: Revisiting LLM Pruning for Test-Time Scaling\n- **Venue**: arXiv 2604.25098, 2026\n- **Core**: Unstructured pruning + TTS can **exceed** unpruned baseline (Qwen3-8B); structured pruning catastrophically fails\n- **Relation**: **Support** — another performance inversion case; method that hurts in one regime helps in another\n\n---\n\n## 4. KV Cache Eviction Strategy Comparison\n\n### 4.1 DefensiveKV: Taming the Fragility of KV Cache Eviction\n- **Venue**: ICLR 2026\n- **Core**: Reveals that stability assumption (fixed important subset) is **fragile**; importance scores are highly non-stationary. Proposes defensive aggregation to control worst-case risk\n- **Relation**: **Direct support** — independently discovers that importance-based methods fail under certain conditions due to importance non-stationarity; directly related to our crossover finding\n- **Gap**: Analyzes fragility statistically; does not decompose into discrete phases or compound interaction\n\n### 4.2 The Pitfalls of KV Cache Compression\n- **Venue**: arXiv 2510.00231, 2025\n- **Core**: In multi-instruction prompting, certain instructions degrade much more rapidly with compression — effectively ignored by LLM; compression method + instruction order bias interactions\n- **Relation**: **Support** — demonstrates condition-dependent failure of uniform compression; analogous to our phase-dependent failure\n\n### 4.3 Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\n- **Venue**: NeurIPS 2025\n- **Core**: Per-head adaptive budget allocation based on attention pattern concentration\n- **Relation**: **Method-component** — per-head adaptation is the spatial analog of our per-phase adaptation\n\n### 4.4 SqueezeAttention: 2D Management of KV-Cache\n- **Venue**: ICLR 2025\n- **Core**: Joint layer-wise + sequence-wise budget optimization; layers categorized by cosine similarity of attention output\n- **Relation**: **Method-component** — 2D optimization (layer × sequence); we add the 3rd dimension (temporal phase)\n\n### 4.5 The Sparse Frontier: Sparse Attention Trade-offs\n- **Venue**: arXiv 2504.17768, 2025\n- **Core**: No universal optimal sparse attention strategy; optimal trade-off depends on task and phase (prefilling vs decoding)\n- **Relation**: **Support** — confirms strategy optimality is condition-dependent; but only prefill/decode, not fine-grained reasoning phases\n\n### 4.6 MixedDimKV: Beyond Token Eviction\n- **Venue**: arXiv 2603.20616, 2026\n- **Core**: Allocates dimensions to tokens at granular level (not binary keep/evict); achieves full attention quality at 6.25% cache\n- **Relation**: **Method-component** — continuous budget allocation is more flexible than binary eviction; potential mechanism for smooth phase transitions\n\n### 4.7 OBCache: Optimal Brain KV Cache Pruning\n- **Venue**: arXiv 2510.07651, 2025\n- **Core**: Second-order Taylor approximation for joint K-V pruning saliency; key-pruning impacts more than value-pruning\n- **Relation**: **Method-component** — principled saliency computation; K vs V asymmetry potentially phase-dependent\n\n---\n\n## 5. Magnitude Crossover / Performance Inversion Phenomena\n\n### 5.1 Phase Transitions in Large Language Model Compression\n- **Authors**: Ma et al.\n- **Venue**: npj Artificial Intelligence (Nature), 2026\n- **Core**: Universal phase transition boundaries; structured pruning collapses at 30-45%, unstructured at 55-65%. Multi-dimensional PTP orthogonal — joint safe zone achievable\n- **Relation**: **Direct support** — phase transitions exist per compression axis and are independent; crossing one PTP while another is safe explains our crossover\n\n### 5.2 Phase Transitions in Neural Networks Pruning\n- **Venue**: arXiv 2602.15224, 2026\n- **Core**: Thermodynamic analysis; free-energy transition predicts sharp collapse; performance stable (3-5% variation) before transition, 30%+ drop after\n- **Relation**: **Support** — sharp transition mechanism; our crossover may be importance-based method crossing PTP while random stays below\n\n### 5.3 RetentiveKV: State-Space Memory for Uncertainty-Aware Eviction\n- **Venue**: arXiv 2605.04075, 2026\n- **Core**: \"Deferred Importance\" phenomenon — tokens exhibit low initial salience but become pivotal at later timesteps\n- **Relation**: **Strong support** — directly relevant to our finding; importance scores computed early are misleading for later-phase utility\n\n### 5.4 More Than a Quick Glance: Overcoming Greedy Bias in KV-Cache Compression\n- **Venue**: arXiv 2602.02199, 2026\n- **Core**: Single attention-score metric is \"greedy\" — misses structurally relevant tokens that are not currently attended; proposes multi-metric scoring\n- **Relation**: **Support** — single importance metric failure under certain conditions is our crossover in metric space\n\n---\n\n## 6. Novelty Assessment\n\n### What is KNOWN in the literature:\n1. Compound compression error is non-additive / super-additive (SparK, SLiM)\n2. Importance scores are non-stationary during generation (RaaS, DefensiveKV, RetentiveKV)\n3. Phase transitions exist independently per compression axis (Ma et al.)\n4. Adaptive budget allocation outperforms uniform (Ada-KV, LAVa, SqueezeAttention, Twilight)\n5. Reasoning has discrete information phases with different computational needs (MI peaks, milestone tokens)\n6. Fixed sparsity strategies fail under certain conditions (Sparse Frontier, Pitfalls)\n\n### What is NOT known (our novelty gap):\n1. **Magnitude crossover in compound sparsity**: No paper reports that importance-based eviction is dramatically superior at one phase but catastrophically inferior at another phase within the same compound sparsity setup. DefensiveKV identifies fragility but does not decompose it into compound × phase interaction.\n2. **Phase gradient asymmetry (900×)**: The quantitative finding that importance method's sensitivity to phase changes is ~900× random's gradient is unprecedented.\n3. **Phase-gated compound controller**: No existing work proposes switching eviction strategy (not just budget) based on reasoning phase in a compound sparsity context.\n4. **Interaction-aware phase boundaries**: Existing phase-adaptive methods (RaaS, ThinKV) adapt budget within one compression axis; none address how phase boundaries should differ when multiple axes interact.\n\n### Closest potential competitor:\n- **ThinKV** (ICLR 2026 Oral): Phase-based strategy for KV cache but single compression axis\n- **DefensiveKV** (ICLR 2026): Addresses importance instability but not compound interaction or phase decomposition\n- **GRASPrune** (ACL 2026): Joint compound pruning with learned gates but static (no phase adaptation)\n\n**Conclusion**: The magnitude crossover phenomenon in compound sparsity — where the optimal strategy flips between phases — appears to be a genuinely novel finding. The closest related observations are (a) DefensiveKV's fragility analysis (statistical, not phase-decomposed), (b) RaaS's milestone token dynamics (single axis), and (c) phase transition theory (single axis thresholds). Our contribution unifies these into a compound × phase interaction framework.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "mcp__agent-ml-research__save_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "literature_scan_phase_adaptive.md",
    "content": "# Literature Scan: Phase-Adaptive Compound Compression\n\n**Date**: 2026-05-14  \n**Focus**: Papers (2024–2026) relevant to phase-gated compound sparsity and the magnitude crossover phenomenon\n\n---\n\n## 1. Phase-Adaptive / Dynamic Compression\n\n### 1.1 Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\n- **Authors**: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\n- **Venue**: NeurIPS 2025 Spotlight\n- **Core**: Uses top-p sampling idea to adaptively decide per-token/per-step attention budget — prunes up to 98% tokens dynamically\n- **Relation**: **Support** — demonstrates that fixed budget is suboptimal and adaptive per-step budget is superior, but operates at token level within a single sparsity axis (no compound interaction)\n- **Gap**: Does not address compound sparsity or phase-dependent metric switching\n\n### 1.2 LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\n- **Authors**: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\n- **Venue**: EMNLP 2025 Findings\n- **Core**: First unified strategy for cache eviction + dynamic budget via Layer Attention Output Loss; discovers that layer budgets matter for generation, head budgets for extraction\n- **Relation**: **Support** — task-conditional budget allocation aligns with our per-phase budget idea; but no temporal/phase axis\n- **Gap**: Budget allocation is static per task type, not dynamic across reasoning phases\n\n### 1.3 LKV: End-to-End Learning of Head-wise Budgets and Token Selection\n- **Authors**: (arXiv 2605.06676)\n- **Venue**: arXiv 2026\n- **Core**: First end-to-end differentiable framework for jointly learning head budgets (LKV-H) and token selection (LKV-T), replacing all heuristics\n- **Relation**: **Orthogonal/Complement** — learned budget allocation is the mechanism we need; could serve as backbone for phase-gated controller\n- **Gap**: Does not model temporal phase transitions; budget is learned offline, not adapted per generation step\n\n### 1.4 SOL: Self-Optimizing Language Models — Compute Where it Counts\n- **Venue**: arXiv 2605.10875, 2026\n- **Core**: Learns per-token compute allocation policy (easy tokens less compute, hard tokens more)\n- **Relation**: **Methodological parallel** — per-token adaptive allocation analogous to per-phase adaptive compression; validates learned controller approach\n\n### 1.5 Token-Budget-Aware LLM Reasoning\n- **Venue**: ACL 2025 Findings\n- **Core**: LLMs can adaptively allocate thinking budget per query difficulty using self-consistency as proxy\n- **Relation**: **Support** — reasoning budget should vary; directly supports phase-adaptive compression for reasoning models\n\n### 1.6 BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens\n- **Venue**: arXiv 2508.17196, 2025\n- **Core**: Inserts special control tokens to inform model of remaining token budget; two-stage SFT+RL pipeline\n- **Relation**: **Orthogonal** — budget-aware generation from compute perspective; could inspire phase-transition signaling tokens\n\n---\n\n## 2. Compound/Joint Sparsity Interaction\n\n### 2.1 SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\n- **Venue**: AAAI 2026\n- **Core**: Reports compound KV cache sparsity (channel + token) produces **super-additive degradation** (ThinK+SnapKV退化65%)\n- **Relation**: **Direct competitor** — first to quantify compound super-additivity; our work extends this with phase-dependent analysis\n\n### 2.2 SLiM: One-shot Quantization and Sparsity with Low-rank Approximation\n- **Authors**: Mozaffari et al.\n- **Venue**: ICML 2025\n- **Core**: Q+S aggregated error is non-additive; uses low-rank adapter to compensate compound compression error\n- **Relation**: **Support** — independently confirms non-additive compound error; complementary framework for error compensation\n\n### 2.3 LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\n- **Venue**: MLSys 2025\n- **Core**: Integrates sparse attention + low-bit KV cache quantization into single GPU kernel; treats them as separate components without joint optimization\n- **Relation**: **Background** — demonstrates industrial need for compound compression; lacks interaction analysis\n\n### 2.4 GRASPrune: Global Gating for Budgeted Structured Pruning\n- **Authors**: Wang et al.\n- **Venue**: ACL 2026 Main\n- **Core**: Learned gate scores for joint pruning of FFN channels + KV head groups under global budget\n- **Relation**: **Direct competitor** — joint pruning with learned gates; but static (no phase adaptation)\n\n### 2.5 Compression Ordering: A Systematic Study\n- **Venue**: arXiv 2511.19495, 2025\n- **Core**: P→KD→Q ordering is optimal; quantization-first causes irreversible information loss; interaction depends on ordering\n- **Relation**: **Support** — ordering matters for compound compression; our phase-gating is a temporal ordering dimension\n\n### 2.6 EVICPRESS: Joint KV-Cache Compression and Eviction\n- **Venue**: arXiv 2512.14946, 2025\n- **Core**: Jointly optimizes eviction and compression (quantization) for KV cache\n- **Relation**: **Method-component** — joint optimization within KV cache; single-axis temporal, no head pruning compound\n\n---\n\n## 3. Reasoning-Phase-Dependent Model Behavior\n\n### 3.1 RaaS: Reasoning-Aware Attention Sparsity\n- **Venue**: ACL 2025 Findings\n- **Core**: Discovers **milestone tokens** in reasoning — tokens that emerge, become important, then fade permanently. Achieves O(L) time+memory for reasoning tasks\n- **Relation**: **Strong support** — directly demonstrates phase-dependent token importance dynamics; \"first important then not\" pattern is a specific case of our phase-dependent importance observation\n- **Gap**: Only considers single eviction dimension; does not study compound interaction\n\n### 3.2 Demystifying Reasoning Dynamics: Thinking Tokens are Information Peaks\n- **Venue**: NeurIPS 2025\n- **Core**: MI between intermediate representations and correct answer exhibits **sudden peaks** at thinking tokens (\"Hmm\", \"Wait\", \"Therefore\"); these tokens are disproportionately important\n- **Relation**: **Strong support** — reasoning has discrete information-critical phases; compression during peaks would be catastrophic, compression between peaks could be aggressive\n- **Gap**: Information-theoretic analysis only; no compression/sparsity experiments\n\n### 3.3 Decision Representation Transitions in Layer-Pruned LLMs\n- **Venue**: arXiv 2605.07271, 2026\n- **Core**: Layer pruning reveals Silent/Decisive Phase; Decision Margin undergoes **sign reversal** (negative→positive) at Transition Point\n- **Relation**: **Strong support** — sign reversal in pruning sensitivity is directly analogous to our magnitude crossover; pruning Silent Phase崩溃 vs Decisive Phase安全\n- **Gap**: Layer pruning (spatial), not temporal phase during generation\n\n### 3.4 Doing More With Less: Revisiting LLM Pruning for Test-Time Scaling\n- **Venue**: arXiv 2604.25098, 2026\n- **Core**: Unstructured pruning + TTS can **exceed** unpruned baseline (Qwen3-8B); structured pruning catastrophically fails\n- **Relation**: **Support** — another performance inversion case; method that hurts in one regime helps in another\n\n---\n\n## 4. KV Cache Eviction Strategy Comparison\n\n### 4.1 DefensiveKV: Taming the Fragility of KV Cache Eviction\n- **Venue**: ICLR 2026\n- **Core**: Reveals that stability assumption (fixed important subset) is **fragile**; importance scores are highly non-stationary. Proposes defensive aggregation to control worst-case risk\n- **Relation**: **Direct support** — independently discovers that importance-based methods fail under certain conditions due to importance non-stationarity; directly related to our crossover finding\n- **Gap**: Analyzes fragility statistically; does not decompose into discrete phases or compound interaction\n\n### 4.2 The Pitfalls of KV Cache Compression\n- **Venue**: arXiv 2510.00231, 2025\n- **Core**: In multi-instruction prompting, certain instructions degrade much more rapidly with compression — effectively ignored by LLM; compression method + instruction order bias interactions\n- **Relation**: **Support** — demonstrates condition-dependent failure of uniform compression; analogous to our phase-dependent failure\n\n### 4.3 Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\n- **Venue**: NeurIPS 2025\n- **Core**: Per-head adaptive budget allocation based on attention pattern concentration\n- **Relation**: **Method-component** — per-head adaptation is the spatial analog of our per-phase adaptation\n\n### 4.4 SqueezeAttention: 2D Management of KV-Cache\n- **Venue**: ICLR 2025\n- **Core**: Joint layer-wise + sequence-wise budget optimization; layers categorized by cosine similarity of attention output\n- **Relation**: **Method-component** — 2D optimization (layer × sequence); we add the 3rd dimension (temporal phase)\n\n### 4.5 The Sparse Frontier: Sparse Attention Trade-offs\n- **Venue**: arXiv 2504.17768, 2025\n- **Core**: No universal optimal sparse attention strategy; optimal trade-off depends on task and phase (prefilling vs decoding)\n- **Relation**: **Support** — confirms strategy optimality is condition-dependent; but only prefill/decode, not fine-grained reasoning phases\n\n### 4.6 MixedDimKV: Beyond Token Eviction\n- **Venue**: arXiv 2603.20616, 2026\n- **Core**: Allocates dimensions to tokens at granular level (not binary keep/evict); achieves full attention quality at 6.25% cache\n- **Relation**: **Method-component** — continuous budget allocation is more flexible than binary eviction; potential mechanism for smooth phase transitions\n\n### 4.7 OBCache: Optimal Brain KV Cache Pruning\n- **Venue**: arXiv 2510.07651, 2025\n- **Core**: Second-order Taylor approximation for joint K-V pruning saliency; key-pruning impacts more than value-pruning\n- **Relation**: **Method-component** — principled saliency computation; K vs V asymmetry potentially phase-dependent\n\n---\n\n## 5. Magnitude Crossover / Performance Inversion Phenomena\n\n### 5.1 Phase Transitions in Large Language Model Compression\n- **Authors**: Ma et al.\n- **Venue**: npj Artificial Intelligence (Nature), 2026\n- **Core**: Universal phase transition boundaries; structured pruning collapses at 30-45%, unstructured at 55-65%. Multi-dimensional PTP orthogonal — joint safe zone achievable\n- **Relation**: **Direct support** — phase transitions exist per compression axis and are independent; crossing one PTP while another is safe explains our crossover\n\n### 5.2 Phase Transitions in Neural Networks Pruning\n- **Venue**: arXiv 2602.15224, 2026\n- **Core**: Thermodynamic analysis; free-energy transition predicts sharp collapse; performance stable (3-5% variation) before transition, 30%+ drop after\n- **Relation**: **Support** — sharp transition mechanism; our crossover may be importance-based method crossing PTP while random stays below\n\n### 5.3 RetentiveKV: State-Space Memory for Uncertainty-Aware Eviction\n- **Venue**: arXiv 2605.04075, 2026\n- **Core**: \"Deferred Importance\" phenomenon — tokens exhibit low initial salience but become pivotal at later timesteps\n- **Relation**: **Strong support** — directly relevant to our finding; importance scores computed early are misleading for later-phase utility\n\n### 5.4 More Than a Quick Glance: Overcoming Greedy Bias in KV-Cache Compression\n- **Venue**: arXiv 2602.02199, 2026\n- **Core**: Single attention-score metric is \"greedy\" — misses structurally relevant tokens that are not currently attended; proposes multi-metric scoring\n- **Relation**: **Support** — single importance metric failure under certain conditions is our crossover in metric space\n\n---\n\n## 6. Novelty Assessment\n\n### What is KNOWN in the literature:\n1. Compound compression error is non-additive / super-additive (SparK, SLiM)\n2. Importance scores are non-stationary during generation (RaaS, DefensiveKV, RetentiveKV)\n3. Phase transitions exist independently per compression axis (Ma et al.)\n4. Adaptive budget allocation outperforms uniform (Ada-KV, LAVa, SqueezeAttention, Twilight)\n5. Reasoning has discrete information phases with different computational needs (MI peaks, milestone tokens)\n6. Fixed sparsity strategies fail under certain conditions (Sparse Frontier, Pitfalls)\n\n### What is NOT known (our novelty gap):\n1. **Magnitude crossover in compound sparsity**: No paper reports that importance-based eviction is dramatically superior at one phase but catastrophically inferior at another phase within the same compound sparsity setup. DefensiveKV identifies fragility but does not decompose it into compound × phase interaction.\n2. **Phase gradient asymmetry (900×)**: The quantitative finding that importance method's sensitivity to phase changes is ~900× random's gradient is unprecedented.\n3. **Phase-gated compound controller**: No existing work proposes switching eviction strategy (not just budget) based on reasoning phase in a compound sparsity context.\n4. **Interaction-aware phase boundaries**: Existing phase-adaptive methods (RaaS, ThinKV) adapt budget within one compression axis; none address how phase boundaries should differ when multiple axes interact.\n\n### Closest potential competitor:\n- **ThinKV** (ICLR 2026 Oral): Phase-based strategy for KV cache but single compression axis\n- **DefensiveKV** (ICLR 2026): Addresses importance instability but not compound interaction or phase decomposition\n- **GRASPrune** (ACL 2026): Joint compound pruning with learned gates but static (no phase adaptation)\n\n**Conclusion**: The magnitude crossover phenomenon in compound sparsity — where the optimal strategy flips between phases — appears to be a genuinely novel finding. The closest related observations are (a) DefensiveKV's fragility analysis (statistical, not phase-decomposed), (b) RaaS's milestone token dynamics (single axis), and (c) phase transition theory (single axis thresholds). Our contribution unifies these into a compound × phase interaction framework.\n"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T02:33:30.617926+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'literature_scan_phase_adaptive.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "mcp__agent-ml-research__save_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T02:33:30.618079+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/ 2>/dev/null && echo \"EXISTS\" || echo \"NO_DIR\"",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/ 2>/dev/null && echo \"EXISTS\" || echo \"NO_DIR\"",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T02:33:30.618203+00:00_

_project
m1_phase_segmentation_analysis.md
m2_m4_code_readiness.md
manifest.yaml
mvp_ii_analysis.md
mvp_ii_profiling_v2
mvp_ii_profiling_v3
mvp_ii_v3_analysis.md
mvp_interaction_index_profiling
pacs
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T02:33:30.618353+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/literature_scan_phase_adaptive.md",
  "content": "# Literature Scan: Phase-Adaptive Compound Compression\n\n**Date**: 2026-05-14  \n**Focus**: Papers (2024-2026) relevant to phase-gated compound sparsity and the magnitude crossover phenomenon\n\n---\n\n## 1. Phase-Adaptive / Dynamic Compression\n\n### 1.1 Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\n- **Authors**: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\n- **Venue**: NeurIPS 2025 Spotlight\n- **Core**: Uses top-p sampling idea to adaptively decide per-token/per-step attention budget -- prunes up to 98% tokens dynamically\n- **Relation**: **Support** -- demonstrates that fixed budget is suboptimal and adaptive per-step budget is superior, but operates at token level within a single sparsity axis (no compound interaction)\n- **Gap**: Does not address compound sparsity or phase-dependent metric switching\n\n### 1.2 LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\n- **Authors**: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\n- **Venue**: EMNLP 2025 Findings\n- **Core**: First unified strategy for cache eviction + dynamic budget via Layer Attention Output Loss; discovers that layer budgets matter for generation, head budgets for extraction\n- **Relation**: **Support** -- task-conditional budget allocation aligns with our per-phase budget idea; but no temporal/phase axis\n- **Gap**: Budget allocation is static per task type, not dynamic across reasoning phases\n\n### 1.3 LKV: End-to-End Learning of Head-wise Budgets and Token Selection\n- **Venue**: arXiv 2605.06676, 2026\n- **Core**: First end-to-end differentiable framework for jointly learning head budgets (LKV-H) and token selection (LKV-T), replacing all heuristics\n- **Relation**: **Orthogonal/Complement** -- learned budget allocation is the mechanism we need; could serve as backbone for phase-gated controller\n- **Gap**: Does not model temporal phase transitions; budget is learned offline, not adapted per generation step\n\n### 1.4 SOL: Self-Optimizing Language Models -- Compute Where it Counts\n- **Venue**: arXiv 2605.10875, 2026\n- **Core**: Learns per-token compute allocation policy (easy tokens less compute, hard tokens more)\n- **Relation**: **Methodological parallel** -- per-token adaptive allocation analogous to per-phase adaptive compression; validates learned controller approach\n\n### 1.5 Token-Budget-Aware LLM Reasoning\n- **Venue**: ACL 2025 Findings (arXiv 2412.18547)\n- **Core**: LLMs can adaptively allocate thinking budget per query difficulty using self-consistency as proxy\n- **Relation**: **Support** -- reasoning budget should vary; directly supports phase-adaptive compression for reasoning models\n\n### 1.6 BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens\n- **Venue**: arXiv 2508.17196, 2025\n- **Core**: Inserts special control tokens to inform model of remaining token budget; two-stage SFT+RL pipeline\n- **Relation**: **Orthogonal** -- budget-aware generation from compute perspective; could inspire phase-transition signaling\n\n---\n\n## 2. Compound/Joint Sparsity Interaction\n\n### 2.1 SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\n- **Venue**: AAAI 2026\n- **Core**: Reports compound KV cache sparsity (channel + token) produces super-additive degradation (ThinK+SnapKV degrades 65%)\n- **Relation**: **Direct competitor** -- first to quantify compound super-additivity; our work extends this with phase-dependent analysis\n\n### 2.2 SLiM: One-shot Quantization and Sparsity with Low-rank Approximation\n- **Authors**: Mozaffari et al.\n- **Venue**: ICML 2025\n- **Core**: Q+S aggregated error is non-additive; uses low-rank adapter to compensate compound compression error\n- **Relation**: **Support** -- independently confirms non-additive compound error; complementary error compensation framework\n\n### 2.3 LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\n- **Venue**: MLSys 2025\n- **Core**: Integrates sparse attention + low-bit KV cache quantization into single GPU kernel; treats as separate components\n- **Relation**: **Background** -- demonstrates industrial need for compound compression; lacks interaction analysis\n\n### 2.4 GRASPrune: Global Gating for Budgeted Structured Pruning\n- **Authors**: Wang et al.\n- **Venue**: ACL 2026 Main\n- **Core**: Learned gate scores for joint pruning of FFN channels + KV head groups under global budget\n- **Relation**: **Direct competitor** -- joint pruning with learned gates; but static (no phase adaptation)\n\n### 2.5 A Systematic Study of Compression Ordering for LLMs\n- **Venue**: arXiv 2511.19495, 2025\n- **Core**: P->KD->Q ordering optimal; quantization-first causes irreversible information loss; interaction depends on ordering\n- **Relation**: **Support** -- ordering matters for compound compression; our phase-gating is a temporal ordering dimension\n\n### 2.6 EVICPRESS: Joint KV-Cache Compression and Eviction\n- **Venue**: arXiv 2512.14946, 2025\n- **Core**: Jointly optimizes eviction and compression (quantization) for KV cache\n- **Relation**: **Method-component** -- joint optimization within KV cache; single temporal axis, no head pruning compound\n\n---\n\n## 3. Reasoning-Phase-Dependent Model Behavior\n\n### 3.1 RaaS: Reasoning-Aware Attention Sparsity\n- **Authors**: Hu, Huang, Wang et al.\n- **Venue**: ACL 2025 Findings\n- **Core**: Discovers milestone tokens in reasoning -- tokens emerge, become important, then fade permanently. Achieves O(L) time+memory\n- **Relation**: **Strong support** -- directly demonstrates phase-dependent token importance dynamics; \"first important then not\" pattern is a specific case of our observation\n- **Gap**: Only considers single eviction dimension; no compound interaction study\n\n### 3.2 Demystifying Reasoning Dynamics: Thinking Tokens are Information Peaks\n- **Venue**: NeurIPS 2025\n- **Core**: MI between intermediate representations and correct answer exhibits sudden peaks at thinking tokens (\"Hmm\", \"Wait\", \"Therefore\"); these tokens are disproportionately important\n- **Relation**: **Strong support** -- reasoning has discrete info-critical phases; compression during peaks catastrophic, between peaks aggressive compression possible\n- **Gap**: Information-theoretic analysis only; no compression/sparsity experiments\n\n### 3.3 Decision Representation Transitions in Layer-Pruned LLMs\n- **Venue**: arXiv 2605.07271, 2026\n- **Core**: Layer pruning reveals Silent/Decisive Phase; Decision Margin undergoes sign reversal (neg->pos) at Transition Point\n- **Relation**: **Strong support** -- sign reversal in pruning sensitivity directly analogous to our magnitude crossover\n- **Gap**: Layer pruning (spatial), not temporal phase during generation\n\n### 3.4 Doing More With Less: Revisiting LLM Pruning for Test-Time Scaling\n- **Venue**: arXiv 2604.25098, 2026\n- **Core**: Unstructured pruning + TTS can exceed unpruned baseline (Qwen3-8B); structured pruning catastrophically fails\n- **Relation**: **Support** -- another performance inversion case; method that hurts in one regime helps in another\n\n### 3.5 NSA: Native Sparse Attention (DeepSeek)\n- **Venue**: ACL 2025 Best Paper\n- **Core**: Hardware-aligned trainable sparse attention with dynamic hierarchical strategy (coarse compression + fine selection)\n- **Relation**: **Background** -- demonstrates that sparse attention should be natively trained, not post-hoc; hierarchical strategy resonates with multi-phase approach\n\n---\n\n## 4. KV Cache Eviction Strategy Comparison\n\n### 4.1 DefensiveKV: Taming the Fragility of KV Cache Eviction\n- **Venue**: ICLR 2026\n- **Core**: Reveals stability assumption (fixed important subset) is fragile; importance scores are highly non-stationary. Proposes defensive aggregation for worst-case risk control\n- **Relation**: **Direct support** -- independently discovers importance-based methods fail under certain conditions due to non-stationarity; directly related to our crossover\n- **Gap**: Statistical analysis, not phase-decomposed; no compound interaction\n\n### 4.2 The Pitfalls of KV Cache Compression\n- **Venue**: arXiv 2510.00231, 2025\n- **Core**: In multi-instruction prompting, certain instructions degrade much more rapidly; compression method + instruction order bias interactions\n- **Relation**: **Support** -- condition-dependent failure of uniform compression; analogous to phase-dependent failure\n\n### 4.3 RetentiveKV: Uncertainty-Aware Multimodal KV Cache Eviction\n- **Venue**: arXiv 2605.04075, 2026\n- **Core**: \"Deferred Importance\" phenomenon -- tokens exhibit low initial salience but become pivotal at later timesteps\n- **Relation**: **Strong support** -- directly relevant; importance scores computed early mislead later-phase utility\n\n### 4.4 More Than a Quick Glance: Overcoming Greedy Bias in KV-Cache Compression\n- **Venue**: arXiv 2602.02199, 2026\n- **Core**: Single attention-score metric is \"greedy\" -- misses structurally relevant tokens; proposes multi-metric scoring\n- **Relation**: **Support** -- single metric failure under certain conditions is our crossover in metric space\n\n### 4.5 Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\n- **Venue**: NeurIPS 2025\n- **Core**: Per-head adaptive budget based on attention pattern concentration\n- **Relation**: **Method-component** -- per-head adaptation is spatial analog of our per-phase adaptation\n\n### 4.6 SqueezeAttention: 2D Management of KV-Cache\n- **Venue**: ICLR 2025\n- **Core**: Joint layer-wise + sequence-wise budget optimization; layers categorized by cosine similarity\n- **Relation**: **Method-component** -- 2D optimization (layer x sequence); we add 3rd dimension (temporal phase)\n\n### 4.7 The Sparse Frontier: Sparse Attention Trade-offs\n- **Venue**: arXiv 2504.17768, 2025\n- **Core**: No universal optimal sparse attention strategy; optimal trade-off depends on task and phase (prefilling vs decoding)\n- **Relation**: **Support** -- confirms strategy optimality is condition-dependent\n\n### 4.8 MixedDimKV: Beyond Token Eviction\n- **Venue**: arXiv 2603.20616, 2026\n- **Core**: Allocates dimensions to tokens at granular level (not binary keep/evict); full attention quality at 6.25% cache\n- **Relation**: **Method-component** -- continuous budget allocation enables smooth phase transitions\n\n### 4.9 OBCache: Optimal Brain KV Cache Pruning\n- **Venue**: arXiv 2510.07651, 2025\n- **Core**: Second-order Taylor for joint K-V pruning saliency; key-pruning impacts more than value-pruning\n- **Relation**: **Method-component** -- principled saliency; K vs V asymmetry potentially phase-dependent\n\n---\n\n## 5. Magnitude Crossover / Performance Inversion\n\n### 5.1 Phase Transitions in Large Language Model Compression\n- **Authors**: Ma et al.\n- **Venue**: npj Artificial Intelligence (Nature), 2026\n- **Core**: Universal phase transition boundaries; structured 30-45% collapse, unstructured 55-65%. Multi-dimensional PTP orthogonal -- joint safe zone achievable but narrow\n- **Relation**: **Direct support** -- phase transitions per axis are independent; crossing one PTP while another is safe explains our crossover\n\n### 5.2 Phase Transitions in Neural Networks Pruning (Thermodynamic)\n- **Venue**: arXiv 2602.15224, 2026\n- **Core**: Free-energy transition predicts sharp collapse; 3-5% stable before, 30%+ drop after\n- **Relation**: **Support** -- our crossover may be importance-method crossing PTP while random stays below\n\n### 5.3 UniComp: Unified Evaluation of LLM Compression\n- **Authors**: Wang et al.\n- **Venue**: arXiv 2602.09130, 2026\n- **Core**: 40+ benchmarks; compression has consistent knowledge bias -- reasoning/multilingual degrade most\n- **Relation**: **Background** -- compression effects are task-dependent; supports per-phase evaluation\n\n---\n\n## 6. Novelty Assessment\n\n### KNOWN in the literature:\n1. Compound compression error is non-additive / super-additive (SparK, SLiM)\n2. Importance scores are non-stationary during generation (RaaS, DefensiveKV, RetentiveKV)\n3. Phase transitions exist independently per compression axis (Ma et al., arXiv 2602.15224)\n4. Adaptive budget allocation outperforms uniform (Ada-KV, LAVa, SqueezeAttention, Twilight)\n5. Reasoning has discrete information phases with different computational needs (MI peaks, milestone tokens)\n6. Fixed sparsity strategies fail under certain conditions (Sparse Frontier, Pitfalls)\n\n### NOT known -- our novelty gap:\n1. **Magnitude crossover in compound sparsity**: No paper reports importance-based eviction dramatically superior at one phase but catastrophically inferior at another within compound sparsity. DefensiveKV identifies fragility but not compound x phase interaction.\n2. **Phase gradient asymmetry (900x)**: The quantitative finding that importance method's sensitivity to phase is ~900x random's gradient is unprecedented.\n3. **Phase-gated compound controller**: No existing work proposes switching eviction strategy (not just budget) based on reasoning phase in compound sparsity context.\n4. **Interaction-aware phase boundaries**: Existing phase-adaptive methods (RaaS, ThinKV) adapt budget within one axis; none address how boundaries should differ when multiple axes interact.\n\n### Closest competitors:\n| Paper | Threat Level | Why not a blocker |\n|-------|-------------|-------------------|\n| ThinKV (ICLR 2026 Oral) | High | Phase-based but single compression axis |\n| DefensiveKV (ICLR 2026) | Medium | Importance instability but no compound or phase decomposition |\n| GRASPrune (ACL 2026) | Medium | Joint compound pruning but static, no phase |\n| SparK (AAAI 2026) | Medium | Compound super-additivity but no phase analysis |\n\n### Conclusion\nThe magnitude crossover phenomenon in compound sparsity -- where the optimal strategy flips between reasoning phases -- is a genuinely novel finding. The closest observations are: (a) DefensiveKV's fragility (statistical, not phase-decomposed), (b) RaaS's milestone tokens (single axis), and (c) phase transition theory (per-axis thresholds). Our contribution unifies these into a compound x phase interaction framework with quantitative crossover evidence.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/literature_scan_phase_adaptive.md",
    "content": "# Literature Scan: Phase-Adaptive Compound Compression\n\n**Date**: 2026-05-14  \n**Focus**: Papers (2024-2026) relevant to phase-gated compound sparsity and the magnitude crossover phenomenon\n\n---\n\n## 1. Phase-Adaptive / Dynamic Compression\n\n### 1.1 Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\n- **Authors**: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\n- **Venue**: NeurIPS 2025 Spotlight\n- **Core**: Uses top-p sampling idea to adaptively decide per-token/per-step attention budget -- prunes up to 98% tokens dynamically\n- **Relation**: **Support** -- demonstrates that fixed budget is suboptimal and adaptive per-step budget is superior, but operates at token level within a single sparsity axis (no compound interaction)\n- **Gap**: Does not address compound sparsity or phase-dependent metric switching\n\n### 1.2 LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\n- **Authors**: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\n- **Venue**: EMNLP 2025 Findings\n- **Core**: First unified strategy for cache eviction + dynamic budget via Layer Attention Output Loss; discovers that layer budgets matter for generation, head budgets for extraction\n- **Relation**: **Support** -- task-conditional budget allocation aligns with our per-phase budget idea; but no temporal/phase axis\n- **Gap**: Budget allocation is static per task type, not dynamic across reasoning phases\n\n### 1.3 LKV: End-to-End Learning of Head-wise Budgets and Token Selection\n- **Venue**: arXiv 2605.06676, 2026\n- **Core**: First end-to-end differentiable framework for jointly learning head budgets (LKV-H) and token selection (LKV-T), replacing all heuristics\n- **Relation**: **Orthogonal/Complement** -- learned budget allocation is the mechanism we need; could serve as backbone for phase-gated controller\n- **Gap**: Does not model temporal phase transitions; budget is learned offline, not adapted per generation step\n\n### 1.4 SOL: Self-Optimizing Language Models -- Compute Where it Counts\n- **Venue**: arXiv 2605.10875, 2026\n- **Core**: Learns per-token compute allocation policy (easy tokens less compute, hard tokens more)\n- **Relation**: **Methodological parallel** -- per-token adaptive allocation analogous to per-phase adaptive compression; validates learned controller approach\n\n### 1.5 Token-Budget-Aware LLM Reasoning\n- **Venue**: ACL 2025 Findings (arXiv 2412.18547)\n- **Core**: LLMs can adaptively allocate thinking budget per query difficulty using self-consistency as proxy\n- **Relation**: **Support** -- reasoning budget should vary; directly supports phase-adaptive compression for reasoning models\n\n### 1.6 BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens\n- **Venue**: arXiv 2508.17196, 2025\n- **Core**: Inserts special control tokens to inform model of remaining token budget; two-stage SFT+RL pipeline\n- **Relation**: **Orthogonal** -- budget-aware generation from compute perspective; could inspire phase-transition signaling\n\n---\n\n## 2. Compound/Joint Sparsity Interaction\n\n### 2.1 SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\n- **Venue**: AAAI 2026\n- **Core**: Reports compound KV cache sparsity (channel + token) produces super-additive degradation (ThinK+SnapKV degrades 65%)\n- **Relation**: **Direct competitor** -- first to quantify compound super-additivity; our work extends this with phase-dependent analysis\n\n### 2.2 SLiM: One-shot Quantization and Sparsity with Low-rank Approximation\n- **Authors**: Mozaffari et al.\n- **Venue**: ICML 2025\n- **Core**: Q+S aggregated error is non-additive; uses low-rank adapter to compensate compound compression error\n- **Relation**: **Support** -- independently confirms non-additive compound error; complementary error compensation framework\n\n### 2.3 LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\n- **Venue**: MLSys 2025\n- **Core**: Integrates sparse attention + low-bit KV cache quantization into single GPU kernel; treats as separate components\n- **Relation**: **Background** -- demonstrates industrial need for compound compression; lacks interaction analysis\n\n### 2.4 GRASPrune: Global Gating for Budgeted Structured Pruning\n- **Authors**: Wang et al.\n- **Venue**: ACL 2026 Main\n- **Core**: Learned gate scores for joint pruning of FFN channels + KV head groups under global budget\n- **Relation**: **Direct competitor** -- joint pruning with learned gates; but static (no phase adaptation)\n\n### 2.5 A Systematic Study of Compression Ordering for LLMs\n- **Venue**: arXiv 2511.19495, 2025\n- **Core**: P->KD->Q ordering optimal; quantization-first causes irreversible information loss; interaction depends on ordering\n- **Relation**: **Support** -- ordering matters for compound compression; our phase-gating is a temporal ordering dimension\n\n### 2.6 EVICPRESS: Joint KV-Cache Compression and Eviction\n- **Venue**: arXiv 2512.14946, 2025\n- **Core**: Jointly optimizes eviction and compression (quantization) for KV cache\n- **Relation**: **Method-component** -- joint optimization within KV cache; single temporal axis, no head pruning compound\n\n---\n\n## 3. Reasoning-Phase-Dependent Model Behavior\n\n### 3.1 RaaS: Reasoning-Aware Attention Sparsity\n- **Authors**: Hu, Huang, Wang et al.\n- **Venue**: ACL 2025 Findings\n- **Core**: Discovers milestone tokens in reasoning -- tokens emerge, become important, then fade permanently. Achieves O(L) time+memory\n- **Relation**: **Strong support** -- directly demonstrates phase-dependent token importance dynamics; \"first important then not\" pattern is a specific case of our observation\n- **Gap**: Only considers single eviction dimension; no compound interaction study\n\n### 3.2 Demystifying Reasoning Dynamics: Thinking Tokens are Information Peaks\n- **Venue**: NeurIPS 2025\n- **Core**: MI between intermediate representations and correct answer exhibits sudden peaks at thinking tokens (\"Hmm\", \"Wait\", \"Therefore\"); these tokens are disproportionately important\n- **Relation**: **Strong support** -- reasoning has discrete info-critical phases; compression during peaks catastrophic, between peaks aggressive compression possible\n- **Gap**: Information-theoretic analysis only; no compression/sparsity experiments\n\n### 3.3 Decision Representation Transitions in Layer-Pruned LLMs\n- **Venue**: arXiv 2605.07271, 2026\n- **Core**: Layer pruning reveals Silent/Decisive Phase; Decision Margin undergoes sign reversal (neg->pos) at Transition Point\n- **Relation**: **Strong support** -- sign reversal in pruning sensitivity directly analogous to our magnitude crossover\n- **Gap**: Layer pruning (spatial), not temporal phase during generation\n\n### 3.4 Doing More With Less: Revisiting LLM Pruning for Test-Time Scaling\n- **Venue**: arXiv 2604.25098, 2026\n- **Core**: Unstructured pruning + TTS can exceed unpruned baseline (Qwen3-8B); structured pruning catastrophically fails\n- **Relation**: **Support** -- another performance inversion case; method that hurts in one regime helps in another\n\n### 3.5 NSA: Native Sparse Attention (DeepSeek)\n- **Venue**: ACL 2025 Best Paper\n- **Core**: Hardware-aligned trainable sparse attention with dynamic hierarchical strategy (coarse compression + fine selection)\n- **Relation**: **Background** -- demonstrates that sparse attention should be natively trained, not post-hoc; hierarchical strategy resonates with multi-phase approach\n\n---\n\n## 4. KV Cache Eviction Strategy Comparison\n\n### 4.1 DefensiveKV: Taming the Fragility of KV Cache Eviction\n- **Venue**: ICLR 2026\n- **Core**: Reveals stability assumption (fixed important subset) is fragile; importance scores are highly non-stationary. Proposes defensive aggregation for worst-case risk control\n- **Relation**: **Direct support** -- independently discovers importance-based methods fail under certain conditions due to non-stationarity; directly related to our crossover\n- **Gap**: Statistical analysis, not phase-decomposed; no compound interaction\n\n### 4.2 The Pitfalls of KV Cache Compression\n- **Venue**: arXiv 2510.00231, 2025\n- **Core**: In multi-instruction prompting, certain instructions degrade much more rapidly; compression method + instruction order bias interactions\n- **Relation**: **Support** -- condition-dependent failure of uniform compression; analogous to phase-dependent failure\n\n### 4.3 RetentiveKV: Uncertainty-Aware Multimodal KV Cache Eviction\n- **Venue**: arXiv 2605.04075, 2026\n- **Core**: \"Deferred Importance\" phenomenon -- tokens exhibit low initial salience but become pivotal at later timesteps\n- **Relation**: **Strong support** -- directly relevant; importance scores computed early mislead later-phase utility\n\n### 4.4 More Than a Quick Glance: Overcoming Greedy Bias in KV-Cache Compression\n- **Venue**: arXiv 2602.02199, 2026\n- **Core**: Single attention-score metric is \"greedy\" -- misses structurally relevant tokens; proposes multi-metric scoring\n- **Relation**: **Support** -- single metric failure under certain conditions is our crossover in metric space\n\n### 4.5 Ada-KV: Adaptive Budget Allocation for KV Cache Eviction\n- **Venue**: NeurIPS 2025\n- **Core**: Per-head adaptive budget based on attention pattern concentration\n- **Relation**: **Method-component** -- per-head adaptation is spatial analog of our per-phase adaptation\n\n### 4.6 SqueezeAttention: 2D Management of KV-Cache\n- **Venue**: ICLR 2025\n- **Core**: Joint layer-wise + sequence-wise budget optimization; layers categorized by cosine similarity\n- **Relation**: **Method-component** -- 2D optimization (layer x sequence); we add 3rd dimension (temporal phase)\n\n### 4.7 The Sparse Frontier: Sparse Attention Trade-offs\n- **Venue**: arXiv 2504.17768, 2025\n- **Core**: No universal optimal sparse attention strategy; optimal trade-off depends on task and phase (prefilling vs decoding)\n- **Relation**: **Support** -- confirms strategy optimality is condition-dependent\n\n### 4.8 MixedDimKV: Beyond Token Eviction\n- **Venue**: arXiv 2603.20616, 2026\n- **Core**: Allocates dimensions to tokens at granular level (not binary keep/evict); full attention quality at 6.25% cache\n- **Relation**: **Method-component** -- continuous budget allocation enables smooth phase transitions\n\n### 4.9 OBCache: Optimal Brain KV Cache Pruning\n- **Venue**: arXiv 2510.07651, 2025\n- **Core**: Second-order Taylor for joint K-V pruning saliency; key-pruning impacts more than value-pruning\n- **Relation**: **Method-component** -- principled saliency; K vs V asymmetry potentially phase-dependent\n\n---\n\n## 5. Magnitude Crossover / Performance Inversion\n\n### 5.1 Phase Transitions in Large Language Model Compression\n- **Authors**: Ma et al.\n- **Venue**: npj Artificial Intelligence (Nature), 2026\n- **Core**: Universal phase transition boundaries; structured 30-45% collapse, unstructured 55-65%. Multi-dimensional PTP orthogonal -- joint safe zone achievable but narrow\n- **Relation**: **Direct support** -- phase transitions per axis are independent; crossing one PTP while another is safe explains our crossover\n\n### 5.2 Phase Transitions in Neural Networks Pruning (Thermodynamic)\n- **Venue**: arXiv 2602.15224, 2026\n- **Core**: Free-energy transition predicts sharp collapse; 3-5% stable before, 30%+ drop after\n- **Relation**: **Support** -- our crossover may be importance-method crossing PTP while random stays below\n\n### 5.3 UniComp: Unified Evaluation of LLM Compression\n- **Authors**: Wang et al.\n- **Venue**: arXiv 2602.09130, 2026\n- **Core**: 40+ benchmarks; compression has consistent knowledge bias -- reasoning/multilingual degrade most\n- **Relation**: **Background** -- compression effects are task-dependent; supports per-phase evaluation\n\n---\n\n## 6. Novelty Assessment\n\n### KNOWN in the literature:\n1. Compound compression error is non-additive / super-additive (SparK, SLiM)\n2. Importance scores are non-stationary during generation (RaaS, DefensiveKV, RetentiveKV)\n3. Phase transitions exist independently per compression axis (Ma et al., arXiv 2602.15224)\n4. Adaptive budget allocation outperforms uniform (Ada-KV, LAVa, SqueezeAttention, Twilight)\n5. Reasoning has discrete information phases with different computational needs (MI peaks, milestone tokens)\n6. Fixed sparsity strategies fail under certain conditions (Sparse Frontier, Pitfalls)\n\n### NOT known -- our novelty gap:\n1. **Magnitude crossover in compound sparsity**: No paper reports importance-based eviction dramatically superior at one phase but catastrophically inferior at another within compound sparsity. DefensiveKV identifies fragility but not compound x phase interaction.\n2. **Phase gradient asymmetry (900x)**: The quantitative finding that importance method's sensitivity to phase is ~900x random's gradient is unprecedented.\n3. **Phase-gated compound controller**: No existing work proposes switching eviction strategy (not just budget) based on reasoning phase in compound sparsity context.\n4. **Interaction-aware phase boundaries**: Existing phase-adaptive methods (RaaS, ThinKV) adapt budget within one axis; none address how boundaries should differ when multiple axes interact.\n\n### Closest competitors:\n| Paper | Threat Level | Why not a blocker |\n|-------|-------------|-------------------|\n| ThinKV (ICLR 2026 Oral) | High | Phase-based but single compression axis |\n| DefensiveKV (ICLR 2026) | Medium | Importance instability but no compound or phase decomposition |\n| GRASPrune (ACL 2026) | Medium | Joint compound pruning but static, no phase |\n| SparK (AAAI 2026) | Medium | Compound super-additivity but no phase analysis |\n\n### Conclusion\nThe magnitude crossover phenomenon in compound sparsity -- where the optimal strategy flips between reasoning phases -- is a genuinely novel finding. The closest observations are: (a) DefensiveKV's fragility (statistical, not phase-decomposed), (b) RaaS's milestone tokens (single axis), and (c) phase transition theory (per-axis thresholds). Our contribution unifies these into a compound x phase interaction framework with quantitative crossover evidence.\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T02:33:30.618647+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/literature_scan_phase_adaptive.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T02:33:30.618785+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "phase-gated-compound-sparse",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T02:33:30.618988+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml\", \"content\": \"## Literature Map — Phase-Gated Compound Sparsity\\n## 增量扫描: 2026-05-14\\n\\n# ============================================================\\n# 已知文献（baseline）\\n# ============================================================\\n\\n- paper_id: spark-aaai2026\\n  title: \\\"SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning\\\"\\n  venue: AAAI 2026\\n  year: 2026\\n  category: direct-competitor\\n  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标\\n  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation\\n\\n- paper_id: thinkv-iclr2026\\n  title: \\\"ThinKV\\\"\\n  venue: ICLR 2026 Oral\\n  year: 2026\\n  category: method-component\\n  relevance: phase 划分思想来源，但只做单一压缩策略\\n  key_finding: KV cache 可按 phase 划分应用不同策略\\n\\n- paper_id: rac-neurips2025\\n  title: \\\"RAC\\\"\\n  venue: NeurIPS 2025\\n  year: 2025\\n  category: background\\n  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择\\n  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM\\n\\n- paper_id: raas-acl2025\\n  title: \\\"RaaS\\\"\\n  venue: ACL 2025\\n  year: 2025\\n  category: method-component\\n  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance\\n  key_finding: token importance 随 decoding phase 非单调变化\\n\\n- paper_id: mixeddimkv-2026\\n  title: \\\"MixedDimKV\\\"\\n  year: 2026\\n  category: method-component\\n  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行\\n  key_finding: 多维度压缩 budget allocation 优于均匀分配\\n\\n# ============================================================\\n# 新增 — Compound / Joint Compression Interaction\\n# ============================================================\\n\\n- paper_id: slim-icml2025\\n  title: \\\"SLiM: One-shot Quantization and Sparsity with Low-rank Approx
…[truncated 5474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T02:33:30.619150+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -name \"literature_map.yaml\" 2>/dev/null",
  "description": "Find literature_map.yaml path"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse -name \"literature_map.yaml\" 2>/dev/null",
    "description": "Find literature_map.yaml path"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T02:33:30.619270+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T02:33:30.619384+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T02:33:30.619583+00:00_

1	## Literature Map — Phase-Gated Compound Sparsity
2	## 增量扫描: 2026-05-14
3	
4	# ============================================================
5	# 已知文献（baseline）
6	# ============================================================
7	
8	- paper_id: spark-aaai2026
9	  title: "SparK: Query-Aware Unstructured Sparsity with Recoverable KV Cache Channel Pruning"
10	  venue: AAAI 2026
11	  year: 2026
12	  category: direct-competitor
13	  relevance: 首篇报告 compound sparsity 总是 super-additive（ThinK+SnapKV 退化 65%），核心对标
14	  key_finding: compound KV cache sparsity (channel + token) 产生 super-additive degradation
15	
16	- paper_id: thinkv-iclr2026
17	  title: "ThinKV"
18	  venue: ICLR 2026 Oral
19	  year: 2026
20	  category: method-component
21	  relevance: phase 划分思想来源，但只做单一压缩策略
22	  key_finding: KV cache 可按 phase 划分应用不同策略
23	
24	- paper_id: rac-neurips2025
25	  title: "RAC"
26	  venue: NeurIPS 2025
27	  year: 2025
28	  category: background
29	  relevance: reasoning model 对 sparsity 更敏感，支撑评估任务选择
30	  key_finding: reasoning model 对 sparsity 敏感度高于一般 LLM
31	
32	- paper_id: raas-acl2025
33	  title: "RaaS"
34	  venue: ACL 2025
35	  year: 2025
36	  category: method-component
37	  relevance: milestone tokens 先重要后衰减，支撑 phase-dependent importance
38	  key_finding: token importance 随 decoding phase 非单调变化
39	
40	- paper_id: mixeddimkv-2026
41	  title: "MixedDimKV"
42	  year: 2026
43	  category: method-component
44	  relevance: multi-dimension compression budget allocation，与 joint controller 思路平行
45	  key_finding: 多维度压缩 budget allocation 优于均匀分配
46	
47	# ============================================================
48	# 新增 — Compound / Joint Compression Interaction
49	# ============================================================
50	
51	- paper_id: slim-icml2025
52	  title: "SLiM: One-shot Quantization and Sparsity with Low-rank Approximation for LLM Weight Compression"
53	  authors: Mozaffari et al.
54	  venue: ICML 2025
55	  year: 2025
56	  category: method-component
57	  relevance: 首个正式处理 compou
…[truncated 5330 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T02:33:30.619754+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml",
  "old_string": "- paper_id: sol-2026\n  title: \"SOL: Self-Optimizing Language Models — Compute Where it Counts\"\n  venue: arXiv 2605.10875\n  year: 2026\n  category: method-component\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算",
  "new_string": "- paper_id: sol-2026\n  title: \"SOL: Self-Optimizing Language Models — Compute Where it Counts\"\n  venue: arXiv 2605.10875\n  year: 2026\n  category: method-component\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\n\n# ============================================================\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\n# ============================================================\n\n- paper_id: twilight-neurips2025\n  title: \"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\"\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\n  venue: NeurIPS 2025 Spotlight\n  year: 2025\n  category: method-component\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\n\n- paper_id: lava-emnlp2025\n  title: \"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\"\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\n  venue: EMNLP 2025 Findings\n  year: 2025\n  category: method-component\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\n\n- paper_id: lkv-2026\n  title: \"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\"\n  venue: arXiv 2605.06676\n  year: 2026\n  category: method-component\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\n\n- paper_id: defensivekv-iclr2026\n  title: \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\"\n  venue: ICLR 2026\n  year: 2026\n  category: direct-competitor\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\n\n- paper_id: retentivekv-2026\n  title: \"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\"\n  venue: arXiv 2605.04075\n  year: 2026\n  category: background\n  relevance: \"Deferred Importance\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\n\n- paper_id: pitfalls-kvcache-2025\n  title: \"The Pitfalls of KV Cache Compression\"\n  venue: arXiv 2510.00231\n  year: 2025\n  category: background\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\n\n- paper_id: greedy-bias-kvcache-2026\n  title: \"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\"\n  venue: arXiv 2602.02199\n  year: 2026\n  category: background\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\n\n- paper_id: thinking-tokens-mi-neurips2025\n  title: \"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\"\n  venue: NeurIPS 2025\n  year: 2025\n  category: background\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\n\n- paper_id: lserve-mlsys2025\n  title: \"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\"\n  venue: MLSys 2025\n  year: 2025\n  category: background\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\n\n- paper_id: squeezeattention-iclr2025\n  title: \"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\"\n  venue: ICLR 2025\n  year: 2025\n  category: method-component\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\n\n- paper_id: nsa-acl2025\n  title: \"NSA: Native Sparse Attention\"\n  authors: DeepSeek\n  venue: ACL 2025 Best Paper\n  year: 2025\n  category: background\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\n\n- paper_id: evicpress-2025\n  title: \"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\"\n  venue: arXiv 2512.14946\n  year: 2025\n  category: method-component\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\n\n- paper_id: phase-transition-pruning-thermo-2026\n  title: \"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\"\n  venue: arXiv 2602.15224\n  year: 2026\n  category: background\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\n\n- paper_id: token-budget-aware-acl2025\n  title: \"Token-Budget-Aware LLM Reasoning\"\n  venue: ACL 2025 Findings\n  year: 2025\n  category: background\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml",
    "old_string": "- paper_id: sol-2026\n  title: \"SOL: Self-Optimizing Language Models — Compute Where it Counts\"\n  venue: arXiv 2605.10875\n  year: 2026\n  category: method-component\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算",
    "new_string": "- paper_id: sol-2026\n  title: \"SOL: Self-Optimizing Language Models — Compute Where it Counts\"\n  venue: arXiv 2605.10875\n  year: 2026\n  category: method-component\n  relevance: learned policy 按 token difficulty 分配 compute，与 learned joint controller 方法论平行\n  key_finding: 学习 per-token compute allocation policy，easy tokens 少算 hard tokens 多算\n\n# ============================================================\n# 新增 — Phase-Adaptive Dynamic Compression (2026-05-14 scan)\n# ============================================================\n\n- paper_id: twilight-neurips2025\n  title: \"Twilight: Adaptive Attention Sparsity with Hierarchical Top-p Pruning\"\n  authors: Lin, Tang, Yang, Wang, Tang, Tian, Stoica, Han, Gao\n  venue: NeurIPS 2025 Spotlight\n  year: 2025\n  category: method-component\n  relevance: 证明 fixed budget 次优，per-step adaptive budget 更优；但单轴无 compound interaction\n  key_finding: top-p 采样思想做 per-step adaptive attention budget，最多 prune 98% tokens\n\n- paper_id: lava-emnlp2025\n  title: \"LAVa: Layer-wise KV Cache Eviction with Dynamic Budget Allocation\"\n  authors: Shen, Yuan, Zhang, Wang, Jiang, Nguyen\n  venue: EMNLP 2025 Findings\n  year: 2025\n  category: method-component\n  relevance: layer budgets 对 generation 重要、head budgets 对 extraction 重要——支撑 task-conditional budget\n  key_finding: 基于 Layer Attention Output Loss 的 unified eviction + dynamic budget；budget 需求 task-dependent\n\n- paper_id: lkv-2026\n  title: \"LKV: End-to-End Learning of Head-wise Budgets and Token Selection for LLM KV Cache Eviction\"\n  venue: arXiv 2605.06676\n  year: 2026\n  category: method-component\n  relevance: 首个端到端可微 budget+selection 联合学习框架；可作 phase-gated controller backbone\n  key_finding: LKV-H 学 head budget + LKV-T 学 token selection，全面超越启发式方法\n\n- paper_id: defensivekv-iclr2026\n  title: \"DefensiveKV: Taming the Fragility of KV Cache Eviction in LLM Inference\"\n  venue: ICLR 2026\n  year: 2026\n  category: direct-competitor\n  relevance: 独立发现 importance-based eviction 的脆弱性——stability assumption 不成立，importance 高度非稳态\n  key_finding: mean aggregation 在极端情况下 vulnerable；defensive aggregation 控制 worst-case risk，2.3-4.3x 质量损失降低\n\n- paper_id: retentivekv-2026\n  title: \"RetentiveKV: State-Space Memory for Uncertainty-Aware Multimodal KV Cache Eviction\"\n  venue: arXiv 2605.04075\n  year: 2026\n  category: background\n  relevance: \"Deferred Importance\" 现象——token 初始 salience 低但后期变 pivotal，直接支撑 crossover 机制\n  key_finding: 视觉 tokens 存在 deferred importance——早期不重要晚期关键；单一时刻 importance 评估不可靠\n\n- paper_id: pitfalls-kvcache-2025\n  title: \"The Pitfalls of KV Cache Compression\"\n  venue: arXiv 2510.00231\n  year: 2025\n  category: background\n  relevance: multi-instruction 场景下部分指令被压缩严重忽略——condition-dependent failure\n  key_finding: 特定 instructions 在压缩下退化极快甚至完全被忽略；compression method + order 产生 bias 交互\n\n- paper_id: greedy-bias-kvcache-2026\n  title: \"More Than a Quick Glance: Overcoming the Greedy Bias in KV-Cache Compression\"\n  venue: arXiv 2602.02199\n  year: 2026\n  category: background\n  relevance: 单一 attention-score metric 是 greedy 的——miss structurally relevant tokens\n  key_finding: 单 metric 有 greedy bias；multi-metric scoring 克服 condition-dependent metric failure\n\n- paper_id: thinking-tokens-mi-neurips2025\n  title: \"Demystifying Reasoning Dynamics with Mutual Information: Thinking Tokens are Information Peaks\"\n  venue: NeurIPS 2025\n  year: 2025\n  category: background\n  relevance: reasoning 中 MI 在 thinking tokens 处突然 peak——compression 需避开 info-critical phases\n  key_finding: thinking tokens (Hmm/Wait/Therefore) 处 MI 突增；这些 tokens 对推理性能不成比例重要\n\n- paper_id: lserve-mlsys2025\n  title: \"LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention\"\n  venue: MLSys 2025\n  year: 2025\n  category: background\n  relevance: sparse attention + KV quantization 工业级联合部署但无 interaction 分析\n  key_finding: 统一 static/dynamic sparsity + KV quant 到单 GPU kernel；prefilling 2.9x 加速\n\n- paper_id: squeezeattention-iclr2025\n  title: \"SqueezeAttention: 2D Management of KV-Cache via Layer-wise Optimal Budget\"\n  venue: ICLR 2025\n  year: 2025\n  category: method-component\n  relevance: layer × sequence 二维 budget 优化；我们增加第三维——temporal phase\n  key_finding: layer-wise cosine similarity 区分 layer 重要性，30-70% memory reduction\n\n- paper_id: nsa-acl2025\n  title: \"NSA: Native Sparse Attention\"\n  authors: DeepSeek\n  venue: ACL 2025 Best Paper\n  year: 2025\n  category: background\n  relevance: hardware-aligned trainable sparse attention；hierarchical 策略（coarse compression + fine selection）呼应 multi-phase\n  key_finding: 端到端可训练 sparse attention，64k 解码 11.6x 加速；coarse+fine 分层策略\n\n- paper_id: evicpress-2025\n  title: \"EVICPRESS: Joint KV-Cache Compression and Eviction for Efficient LLM Serving\"\n  venue: arXiv 2512.14946\n  year: 2025\n  category: method-component\n  relevance: 联合 eviction + quantization 优化 KV cache——compound 方向但仅 KV 内部\n  key_finding: joint eviction + quantization 优于独立应用；但无 head pruning compound\n\n- paper_id: phase-transition-pruning-thermo-2026\n  title: \"Phase Transitions in Neural Networks Pruning (Thermodynamic Analysis)\"\n  venue: arXiv 2602.15224\n  year: 2026\n  category: background\n  relevance: 自由能分析预测 sharp collapse；transition 前稳定 3-5%，跨越后 30%+ 骤降\n  key_finding: free-energy phase transition 预测 pruning 崩溃点；importance 方法可能在某 phase 跨越 PTP\n\n- paper_id: token-budget-aware-acl2025\n  title: \"Token-Budget-Aware LLM Reasoning\"\n  venue: ACL 2025 Findings\n  year: 2025\n  category: background\n  relevance: reasoning budget 应按 query 难度自适应分配——支撑 phase-adaptive compression\n  key_finding: self-consistency 作为 thinking necessity proxy 动态调整 reasoning token budget"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T02:33:30.620061+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-14T02:33:30.620241+00:00_

调研完成。产出：

1. **`artifacts/literature_scan_phase_adaptive.md`** — 完整调研报告，覆盖 5 个方向共 ~30 篇论文，含 novelty assessment
2. **`literature_map.yaml`** — 追加 15 条新文献条目

**核心结论**：
- 没有论文报告过类似的 compound sparsity × phase 维度的 magnitude crossover 现象
- 最接近的工作：DefensiveKV（importance 脆弱性，但统计而非 phase 分解）、RaaS（milestone tokens 单轴）、phase transition theory（单轴阈值）
- 900× phase gradient asymmetry 和 phase-gated strategy switching（非 budget tuning）在 compound context 下是独有发现
- 主要竞品威胁：ThinKV（单轴 phase）、GRASPrune（compound 但静态）、DefensiveKV（importance 非稳态但无 compound 分析）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_phase-adaptive-compression-lit_20260514T022741"
}
```

</details>

---
