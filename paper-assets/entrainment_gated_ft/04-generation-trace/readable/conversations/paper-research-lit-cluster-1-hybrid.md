# paper research lit cluster 1 hybrid

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_paper_research_lit_cluster_1_hybrid_20260519T182256.jsonl`
- **Structured JSON:** [`525c3f5f7a16f4f9784d.json`](../../sessions/52/525c3f5f7a16f4f9784d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-19T18:25:18.903702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml"
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-19T18:25:18.904113+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-19T18:25:18.904349+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T18:25:18.904600+00:00_

1	# Literature Map for entrainment_gated_ft
2	# Auto-generated skeleton; Workers will populate per cluster
3	
4	clusters:
5	  - cluster_name: "Hybrid Architectures"
6	    target_count: 7
7	    papers:
8	      - bibtex_key: wang2025hybrid
9	        title: "Scaling Laws for Hybrid Language Models"
10	        authors: "Wang, Junxiong and others"
11	        year: 2025
12	        venue: "arXiv:2507.06457"
13	        category: "Hybrid Architectures"
14	        verified: true
15	        doi: ""
16	        url: "https://arxiv.org/abs/2507.06457"
17	        relevance: "Primary data source — 72-model zoo of hybrid recurrent-attention architectures"
18	
19	  - cluster_name: "Linear Recurrent Models"
20	    target_count: 6
21	    papers: []
22	
23	  - cluster_name: "Underspecification and Model Agreement"
24	    target_count: 5
25	    papers:
26	      - bibtex_key: damour2022underspecification
27	        title: "Underspecification Presents Challenges for Credibility in Modern Machine Learning"
28	        authors: "D'Amour, Alexander and Heller, Katherine and Moldovan, Dan and others"
29	        year: 2022
30	        venue: "JMLR"
31	        category: "Underspecification and Model Agreement"
32	        verified: true
33	        doi: ""
34	        url: ""
35	        relevance: "Framing anchor — defines underspecification; our finding is a specific instance"
36	
37	  - cluster_name: "Ensemble Diversity"
38	    target_count: 3
39	    papers: []
40	
41	  - cluster_name: "Dataset Cartography and Per-Example Analysis"
42	    target_count: 4
43	    papers: []
44	
45	  - cluster_name: "Attention Interpretability"
46	    target_count: 4
47	    papers: []
48	
49	  - cluster_name: "Benchmarks and Evaluation"
50	    target_count: 3
51	    papers:
52	      - bibtex_key: paperno2016lambada
53	        title: "The LAMBADA Dataset: Word Prediction Requiring a Broad Discourse Context"
54	        authors: "Paperno, Denis and Kruszewski, Germán and Lazaridou, Angeliki and others"
55	        year: 2
…[truncated 230 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T18:25:18.904894+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lieber et al 2024 \"Jamba: A Hybrid Transformer-Mamba Language Model\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lieber et al 2024 \"Jamba: A Hybrid Transformer-Mamba Language Model\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T18:25:18.905075+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Peng et al 2024 \"Eagle and Finch\" RWKV-6 arxiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Peng et al 2024 \"Eagle and Finch\" RWKV-6 arxiv paper"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T18:25:18.905244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "De et al 2024 \"Griffin: Mixing Gated Linear Recurrences with Local Attention\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "De et al 2024 \"Griffin: Mixing Gated Linear Recurrences with Local Attention\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-19T18:25:18.905409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dao Gu 2024 \"Transformers are SSMs\" Mamba-2 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dao Gu 2024 \"Transformers are SSMs\" Mamba-2 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T18:25:18.905584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hybrid recurrent attention architecture language model 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hybrid recurrent attention architecture language model 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-19T18:25:18.905780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jamba Mamba-2 RWKV-6 RecurrentGemma Griffin linear attention hybrid 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jamba Mamba-2 RWKV-6 RecurrentGemma Griffin linear attention hybrid 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T18:25:18.906010+00:00_

Web search results for query: "Peng et al 2024 "Eagle and Finch" RWKV-6 arxiv paper"

Links: [{"title":"[PDF] Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/157ed5647da39a7f5d33a84a90414b2a9e97e301"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://openreview.net/pdf/7503464277054ff67a466511be7bc9d259f12885.pdf"},{"title":"[2404.05892] Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://arxiv.org/abs/2404.05892"},{"title":"Paper page - Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://huggingface.co/papers/2404.05892"},{"title":"(PDF) Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://www.academia.edu/126419179/Eagle_and_Finch_RWKV_with_Matrix_Valued_States_and_Dynamic_Recurrence"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://arxiv.org/pdf/2404.05892"},{"title":"🦅 Eagle & 🐦 Finch - architecture paper is here","url":"https://blog.rwkv.com/p/eagle-and-finch-architecture-paper"}]

I found the paper you're looking for! Here's what I can tell you about it:

The paper "Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence" by Peng et al. was submitted on April 8, 2024, with the latest version (v4) on September 26, 2024.

**Key Details:**

- The paper presents Eagle (RWKV-5) and Finch (RWKV-6), sequence models improving upon the RWKV (RWKV-4) architecture.

- Their architectural design advancements include multi-headed matrix-valued states and a dynamic recurrence mechanism that improve expressivity while maintaining the inference efficiency characteristics of RNNs.

- They introduced a new multilingual corpus with 1.12 trillion tokens and trained four Eagle models ranging from 0.46 to 7.5 billion parameters, and two Finch models with 1.6 and 3.1 billion parameters
…[truncated 184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T18:25:18.906274+00:00_

Web search results for query: "De et al 2024 "Griffin: Mixing Gated Linear Recurrences with Local Attention" arxiv"

Links: [{"title":"Paper page - Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://huggingface.co/papers/2402.19427"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local ...","url":"https://www.summarizepaper.com/en/arxiv-id/2402.19427v1/"},{"title":"[2402.19427v1] Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/abs/2402.19427v1"},{"title":"[2402.19427] Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/abs/2402.19427"},{"title":"Explaining Modern Gated-Linear RNNs via A Unified Implicit Attention Formulation","url":"https://arxiv.org/html/2405.16504v2"},{"title":"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models","url":"https://arxiv.org/html/2404.07839v1"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://gonzoml.substack.com/p/griffin-mixing-gated-linear-recurrences"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/html/2402.19427v1"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local ...","url":"https://arxiv.org/pdf/2402.19427"}]

I found the paper you're looking for! Here are the key details:

**Paper:** Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models proposes Hawk, an RNN with gated linear recurrences, and Griffin, a hybrid model that mixes gated linear recurrences with local attention.

**Authors:** Soham De, Samuel L. Smith, Anushan Fernando, Aleksandar Botev, George Cristian-Muraru, Albert Gu, Ruba Haroun, Leonard Berrada, Yutian Chen, Srivatsan Srinivasan, Guillaume Desjardins, Arnaud Doucet, David Budden, Yee Whye T
…[truncated 494 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T18:25:18.906546+00:00_

Web search results for query: "Dao Gu 2024 "Transformers are SSMs" Mamba-2 arxiv"

Links: [{"title":"[PDF] Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Transformers-are-SSMs:-Generalized-Models-and-State-Dao-Gu/ca9f5b3bf0f54ad97513e6175b30497873670fed"},{"title":"Mamba-2 is here! - by Grigory Sapunov - Gonzo ML","url":"https://gonzoml.substack.com/p/mamba-2-is-here"},{"title":"[2405.21060] Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality","url":"https://arxiv.org/abs/2405.21060"},{"title":"[2405.21060v1] Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality","url":"https://arxiv.org/abs/2405.21060v1"},{"title":"Paper page - Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality","url":"https://huggingface.co/papers/2405.21060"},{"title":"Transformers are SSMs: Generalized Models and Efficient Algorithms","url":"https://arxiv.org/pdf/2405.21060"},{"title":"Understanding and Enhancing Mamba-Transformer Hybrids for Memory Recall and Language Modeling","url":"https://arxiv.org/html/2510.26912v1"},{"title":"GitHub - state-spaces/mamba: Mamba SSM architecture · GitHub","url":"https://github.com/state-spaces/mamba"},{"title":"Transformers are SSMs: Generalized Models and Efficient Algorithms Through","url":"https://openreview.net/pdf/54bf495d93336f1f195f264c1b6c2805169b3492.pdf"},{"title":"Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic   Models","url":"https://arxiv.org/pdf/2408.10189"}]

Based on the search results, I found the paper you're looking for:

**Paper Details:**
- **Title:** Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality
- **Authors:** Tri Dao and Albert Gu
- **Publication:** ArXiv, 2024, volume abs/2
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T18:25:18.906845+00:00_

Web search results for query: "hybrid recurrent attention architecture language model 2024 2025 arxiv"

Links: [{"title":"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights","url":"https://arxiv.org/html/2510.04800v1"},{"title":"Liger: Linearizing Large Language Models to Gated Recurrent Structures","url":"https://arxiv.org/pdf/2503.01496"},{"title":"Hybrid Architectures for Language Models:","url":"https://arxiv.org/pdf/2510.04800v1"},{"title":"Native Hybrid Attention for Efficient Sequence Modeling","url":"https://arxiv.org/html/2510.07019v1"},{"title":"Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts","url":"https://arxiv.org/html/2601.22156v1"},{"title":"A Systematic Analysis of Hybrid Linear Attention","url":"https://arxiv.org/pdf/2507.06457"},{"title":"WuNeng: Hybrid State with Attention","url":"https://arxiv.org/pdf/2504.19191"}]

Based on the search results, here are the key findings about hybrid recurrent attention architecture language models from 2024-2025 arxiv papers:

## Key Hybrid Architectures

Notable examples include Zamba, Jamba, Samba, Hunyuan-TurboS, Nemotron nano 2, and IBM Granite 4.0, which leverage Mamba's efficiency with global or local attention, scaling to over 1M context length.

Other hybrids—RecurrentGemma, Griffin, Titans, RWKV-X, MiniMax-01, and Qwen3-Next—combine diverse self-attention variants with different linear modules.

## Hybrid Design Approaches

Inter-layer hybrid architectures mix different layer types within the same model depth, with examples including Zamba, Jamba, Samba, and Minimax-01, which insert Transformer layers at fixed ratios among linear or recurrent layers.

In the head-wise splitting approach (e.g., Hymba, WuNeng), attention heads are divided into groups with each group assigned to a distinct module, while works like Liger process each token through all modules in parallel and fuse the outputs.

## Post-Training 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T18:25:18.907135+00:00_

Web search results for query: "Jamba Mamba-2 RWKV-6 RecurrentGemma Griffin linear attention hybrid 2024 2025"

Links: [{"title":"RecurrentGemma: Moving Past Transformers for Efficient Open Language   Models","url":"https://arxiv.org/pdf/2404.07839"},{"title":"RWKV-X: A Linear Complexity Hybrid Language Model","url":"https://arxiv.org/html/2504.21463"},{"title":"Jamba: A Hybrid Transformer-Mamba Language Model with Mixture-of-Experts | by Sulbha Jain | Nov, 2025 | Medium","url":"https://medium.com/@sulbha.jindal/jamba-a-hybrid-transformer-mamba-language-model-with-mixture-of-experts-506281f2398e"},{"title":"Transformers vs Mamba vs Linear Attention: Who Wins Long Context? | by Devansh | Medium","url":"https://machine-learning-made-simple.medium.com/transformers-vs-mamba-vs-linear-attention-who-wins-long-context-f1dc8ceb5ede"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for   Efficient Language Models","url":"https://arxiv.org/pdf/2402.19427"},{"title":"GitHub - radarFudan/Awesome-state-space-models: Collection of papers on state-space models · GitHub","url":"https://github.com/radarFudan/Awesome-state-space-models"},{"title":"The Hidden Attention of Mamba Models","url":"https://aclanthology.org/2025.acl-long.76.pdf"},{"title":"2Mamba2Furious: Linear in Complexity, Competitive in Accuracy","url":"https://arxiv.org/pdf/2602.17363"}]

Based on the search results, here's what I found about these hybrid language models and linear attention architectures:

## Jamba
Jamba is a hybrid transformer-mamba language model. Jamba matches or outperforms Mixtral and Llama-2 70B in reasoning, comprehension, and long-context benchmarks, despite a much smaller active parameter and memory footprint. Hybridizing attention and Mamba layers yields better loss curves and overall accuracy than pure attention or pure Mamba alone.

## RWKV-6
RWKV-6 improved training stability, facilitating greater scalability, with RWKV being a Linear RNN architecture.

## Recurrent
…[truncated 739 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T18:25:18.907431+00:00_

Web search results for query: "Lieber et al 2024 "Jamba: A Hybrid Transformer-Mamba Language Model" arxiv"

Links: [{"title":"[PDF] Jamba: A Hybrid Transformer-Mamba Language Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Jamba:-A-Hybrid-Transformer-Mamba-Language-Model-Lieber-Lenz/cbaf689fd9ea9bc939510019d90535d6249b3367"},{"title":"Paper page - Jamba: A Hybrid Transformer-Mamba Language Model","url":"https://huggingface.co/papers/2403.19887"},{"title":"Musing 37: Jamba: A Hybrid Transformer-Mamba Language Model","url":"https://aiscientist.substack.com/p/musing-37-jamba-a-hybrid-transformer"},{"title":"Jamba: A Hybrid Transformer-Mamba Language Model | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/jamba-hybrid-transformer-mamba-language-model"},{"title":"[2403.19887] Jamba: A Hybrid Transformer-Mamba Language Model","url":"https://arxiv.org/abs/2403.19887"},{"title":"Jamba-1.5: Hybrid Transformer-Mamba Models at Scale","url":"https://arxiv.org/html/2408.12570v1"},{"title":"Understanding and Enhancing Mamba-Transformer Hybrids for Memory Recall and Language Modeling","url":"https://arxiv.org/html/2510.26912v1"},{"title":"Jamba: A Hybrid Transformer-Mamba Language Model","url":"https://arxiv.org/html/2403.19887v1"},{"title":"JambaTalk: Speech-driven 3D Talking Head Generation based on a Hybrid Transformer-Mamba Model","url":"https://arxiv.org/html/2408.01627v2"},{"title":"Jamba: A Hybrid Transformer-Mamba Language Model Opher Lieber∗ Barak Lenz∗","url":"https://arxiv.org/pdf/2403.19887"}]

Based on the search results, I found detailed information about the Lieber et al. 2024 paper on Jamba.

## Summary

The paper presents Jamba, a new base large language model based on a novel hybrid Transformer-Mamba mixture-of-experts (MoE) architecture. Jamba interleaves blocks of Transformer and Mamba layers, enjoying the benefits of both model families, with MoE added in some of these layers to increase model capacity while keepi
…[truncated 1030 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T18:25:18.907740+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RecurrentGemma \"Moving Past Transformers\" Botev 2024 arxiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RecurrentGemma \"Moving Past Transformers\" Botev 2024 arxiv authors"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-19T18:25:18.907944+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hymba hybrid Mamba attention language model 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hymba hybrid Mamba attention language model 2024 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T18:25:18.908174+00:00_

Web search results for query: "RecurrentGemma "Moving Past Transformers" Botev 2024 arxiv authors"

Links: [{"title":"Paper page - RecurrentGemma: Moving Past Transformers for Efficient Open Language Models","url":"https://huggingface.co/papers/2404.07839"},{"title":"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/recurrentgemma-moving-past-transformers-efficient-open-language"},{"title":"[PDF] RecurrentGemma: Moving Past Transformers for Efficient Open Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RecurrentGemma:-Moving-Past-Transformers-for-Open-Botev-De/fe33be95849c556ce0bdffaa1d2c7db9bb2e2c61"},{"title":"2024-8-29 RecurrentGemma: Moving Past Transformers","url":"https://arxiv.org/pdf/2404.07839"},{"title":"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models","url":"https://arxiv.org/html/2404.07839v1"},{"title":"Marconi: Prefix Caching for the Era of Hybrid LLMs","url":"https://arxiv.org/html/2411.19379v2"},{"title":"Overflow Prevention Enhances Long-Context Recurrent LLMs","url":"https://arxiv.org/html/2505.07793v2"},{"title":"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240407839B/abstract"},{"title":"[2404.07839v2] RecurrentGemma: Moving Past Transformers for Efficient Open Language Models","url":"https://arxiv.org/abs/2404.07839v2"},{"title":"[2404.07839] RecurrentGemma: Moving Past Transformers for Efficient Open Language Models","url":"https://arxiv.org/abs/2404.07839"}]

Based on the search results, here is the information about the "RecurrentGemma: Moving Past Transformers" paper:

**Paper Details:**
- arXiv ID: 2404.07839, Published on April 11, 2024

**Authors:**
Aleksandar Botev, Soham De, Samuel L Smith, Anushan Fernando, George-Cristian Muraru, Ruba Haroun, Leonard Berrada, Razvan Pascanu, Pier Giuseppe S
…[truncated 1221 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T18:25:18.908425+00:00_

Web search results for query: "Hymba hybrid Mamba attention language model 2024 arxiv"

Links: [{"title":"Paper page - Hymba: A Hybrid-head Architecture for Small Language Models","url":"https://huggingface.co/papers/2411.13676"},{"title":"Hymba: A Hybrid-head Architecture for Small Language Models","url":"https://arxiv.org/html/2411.13676v1"},{"title":"Understanding and Enhancing Mamba-Transformer Hybrids for Memory Recall and Language Modeling","url":"https://arxiv.org/html/2510.26912v1"},{"title":"[2411.13676] Hymba: A Hybrid-head Architecture for Small Language Models","url":"https://arxiv.org/abs/2411.13676"},{"title":"Hybrid Architectures for Language Models: Systematic Analysis and Design Insights","url":"https://arxiv.org/html/2510.04800v1"},{"title":"An Empirical Study of Mamba-based Language Models","url":"https://arxiv.org/pdf/2406.07887"},{"title":"Hymba: A Hybrid-head Architecture for Small Language Models","url":"https://arxiv.org/pdf/2411.13676"}]

I found information about Hymba, a hybrid language model architecture paper from 2024. Here are the key details:

## Overview

Hymba is a novel LM architecture that integrates attention heads and SSM heads within the same layer, offering parallel and complementary processing of the same inputs.

## Key Features

The model introduces learnable meta tokens that are prepended to prompts, storing critical information and alleviating the "forced-to-attend" burden associated with attention mechanisms. Additionally, it incorporates cross-layer key-value (KV) sharing and partial sliding window attention, resulting in a compact cache size.

## Performance Results

Hymba's 1.5B-Base model surpasses all sub-2B public models in performance and even outperforms Llama-3.2-3B with 1.32% higher average accuracy, an 11.67x cache size reduction, and 3.49x throughput.

## Architecture Design

The model uses a head-wise splitting approach where attention heads are divided into groups, with each group assigned to a distinct mod
…[truncated 258 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T18:25:18.908694+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.13676",
  "prompt": "Extract the exact title, full list of authors (especially first author), submission date, and any venue/conference information for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2411.13676",
    "prompt": "Extract the exact title, full list of authors (especially first author), submission date, and any venue/conference information for this paper."
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-19T18:25:18.908886+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.05892",
  "prompt": "Extract the exact title, first author full name, submission date, and any venue/conference information for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2404.05892",
    "prompt": "Extract the exact title, first author full name, submission date, and any venue/conference information for this paper."
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T18:25:18.909051+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2405.21060",
  "prompt": "Extract the exact title, authors, submission date, and any venue/conference information (e.g., ICML 2024) for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2405.21060",
    "prompt": "Extract the exact title, authors, submission date, and any venue/conference information (e.g., ICML 2024) for this paper."
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T18:25:18.909229+00:00_

# Paper Information Extract

**Title:** "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"

**Authors:** Tri Dao and Albert Gu

**Submission Date:** May 31, 2024

**Venue:** ICML 2024 (International Conference on Machine Learning)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T18:25:18.909405+00:00_

# Paper Extraction Summary

**Title:** "Hymba: A Hybrid-head Architecture for Small Language Models"

**First Author:** Xin Dong

**Full Author List:** Xin Dong, Yonggan Fu, Shizhe Diao, Wonmin Byeon, Zijia Chen, Ameya Sunil Mahabaleshwarkar, Shih-Yang Liu, Matthijs Van Keirsbilck, Min-Hung Chen, Yoshi Suhara, Yingyan Lin, Jan Kautz, Pavlo Molchanov

**Submission Date:** November 20, 2024

**Venue/Conference Information:** No specific conference or venue is listed. The paper was submitted to arXiv (identifier: 2411.13676) in the Computation and Language category. The comments section notes the work is "20 pages, models are available on huggingface," but no traditional conference venue is mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T18:25:18.909576+00:00_

# Paper Information

**Exact Title:** "Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence"

**First Author Full Name:** Bo Peng

**Submission Date:** April 8, 2024 (v1 submission)

**Venue/Conference Information:** None specified. This paper was submitted to arXiv in the Computer Science > Computation and Language category (cs.CL). There is no traditional conference or journal venue listed in the metadata provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T18:25:18.909813+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Eagle and Finch\" RWKV Peng 2024 EMNLP ICML NeurIPS accepted venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Eagle and Finch\" RWKV Peng 2024 EMNLP ICML NeurIPS accepted venue"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T18:25:18.909989+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Griffin \"Mixing Gated Linear Recurrences\" De 2024 ICML NeurIPS accepted venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Griffin \"Mixing Gated Linear Recurrences\" De 2024 ICML NeurIPS accepted venue"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T18:25:18.910184+00:00_

Web search results for query: ""Eagle and Finch" RWKV Peng 2024 EMNLP ICML NeurIPS accepted venue"

Links: [{"title":"[PDF] Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | Semantic Scholar","url":"https://www.semanticscholar.org/paper/157ed5647da39a7f5d33a84a90414b2a9e97e301"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://arxiv.org/pdf/2404.05892"},{"title":"[2404.05892] Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://arxiv.org/abs/2404.05892"},{"title":"Peng Zhou","url":"https://pengzhouzp.github.io/"},{"title":"RWKV-CLIP: A Robust Vision-Language Representation ...","url":"https://aclanthology.org/2024.emnlp-main.276.pdf"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and ...","url":"https://openreview.net/pdf/9f3d829735b231725665ff226a4f732293ad4aa8.pdf"},{"title":"2024 in Post-Transformers Architectures (State Space Models, RWKV) [LS Live @ NeurIPS]","url":"https://www.latent.space/p/2024-post-transformers"},{"title":"2024 in Post-Transformers Architectures (State Space Models, RWKV) [LS Live @ NeurIPS]","url":"https://podcasts.apple.com/ug/podcast/2024-in-post-transformers-architectures-state-space/id1674008350?i=1000681506946"}]

Based on the search results, I found information about the "Eagle and Finch" paper:

Eagle and Finch are sequence models improving upon the RWKV (RWKV-4) architecture. The paper introduces two new architectures: Eagle (RWKV-5) and Finch (RWKV-6).

The paper was authored by Bo Peng and colleagues and was made available on arXiv on April 8, 2024.

However, based on the search results provided, I could not find definitive information about which specific venue (EMNLP, ICML, or NeurIPS) the "Eagle and Finch" paper was accepted to. The paper is referenced in citations on other publications, but the search results don't clearly indicate its final acceptance venue. The arXiv paper itself appears to be the primary pub
…[truncated 141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T18:25:18.910440+00:00_

Web search results for query: "Griffin "Mixing Gated Linear Recurrences" De 2024 ICML NeurIPS accepted venue"

Links: [{"title":"[2402.19427] Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/abs/2402.19427"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://gonzoml.substack.com/p/griffin-mixing-gated-linear-recurrences"},{"title":"2024-3-1 Griffin: Mixing Gated Linear Recurrences with","url":"https://arxiv.org/pdf/2402.19427"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local ...","url":"https://ucl-ellis.github.io/dm_csml_seminars/2024-03-22-Botev/"},{"title":"Paper page - Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://huggingface.co/papers/2402.19427"},{"title":"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models","url":"https://arxiv.org/html/2402.19427v1"},{"title":"GitHub - kyegomez/Griffin: Implementation of Griffin from the paper: \"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models\"","url":"https://github.com/kyegomez/Griffin"},{"title":"[Let’s Review] Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models by Dogukan Uraz Tuna | Medium | Medium","url":"https://medium.com/@dtunai/lets-review-griffin-mixing-gated-linear-recurrences-with-local-attention-for-efficient-lms-57c824846b3d"},{"title":"GitHub - knotgrass/Griffin: Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models · GitHub","url":"https://github.com/knotgrass/Griffin"}]

The paper "Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models" was released by DeepMind in late February 2024. It was initially submitted to arXiv on February 29, 2024.

However, based on the search results, I cannot find informatio
…[truncated 539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T18:25:18.910689+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/157ed5647da39a7f5d33a84a90414b2a9e97e301",
  "prompt": "What venue/conference was this paper published at? Look for EMNLP, ICML, NeurIPS, ICLR, or any other conference/journal name."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.semanticscholar.org/paper/157ed5647da39a7f5d33a84a90414b2a9e97e301",
    "prompt": "What venue/conference was this paper published at? Look for EMNLP, ICML, NeurIPS, ICLR, or any other conference/journal name."
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T18:25:18.910887+00:00_

I don't see any web page content provided in your message. The section marked "Web page content:" appears to be empty.

Could you please share the actual content of the web page or paper? Once you provide it, I'll be happy to identify the venue or conference where it was published, looking for mentions of EMNLP, ICML, NeurIPS, ICLR, or other conferences/journals.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T18:25:18.911071+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.semanticscholar.org/paper/Jamba:-A-Hybrid-Transformer-Mamba-Language-Model-Lieber-Lenz/cbaf689fd9ea9bc939510019d90535d6249b3367",
  "prompt": "What venue/conference was this paper published at? Look for any conference name like ICML, NeurIPS, ICLR, EMNLP, ACL, etc."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.semanticscholar.org/paper/Jamba:-A-Hybrid-Transformer-Mamba-Language-Model-Lieber-Lenz/cbaf689fd9ea9bc939510019d90535d6249b3367",
    "prompt": "What venue/conference was this paper published at? Look for any conference name like ICML, NeurIPS, ICLR, EMNLP, ACL, etc."
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T18:25:18.911254+00:00_

I don't see any web page content provided in your message. The area between the dashes appears to be empty:

```
Web page content:
---

---
```

Could you please share the actual web page content or paper details? Once you provide that information, I'll be happy to identify the venue or conference where the paper was published.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T18:25:18.911491+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Eagle and Finch\" RWKV EMNLP 2024 Findings proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Eagle and Finch\" RWKV EMNLP 2024 Findings proceedings"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T18:25:18.911767+00:00_

Web search results for query: ""Eagle and Finch" RWKV EMNLP 2024 Findings proceedings"

Links: [{"title":"Findings of EMNLP 2024","url":"https://www.proceedings.com/content/077/077401webtoc.pdf"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and ...","url":"https://www.emergentmind.com/papers/2404.05892"},{"title":"[2404.05892] Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://arxiv.org/abs/2404.05892"},{"title":"EMNLP Findings 2024 - Finch et al. - Emory NLP","url":"https://www.emorynlp.org/publications/emnlp-findings-2024-finch-et-al"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence","url":"https://arxiv.org/pdf/2404.05892"},{"title":"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/eagle-finch-rwkv-matrix-valued-states-dynamic"},{"title":"Eagle (RWKV-5) and Finch (RWKV-6): Marking Substantial Progress in Recurrent Neural Networks-Based Language Models by Integrating Multiheaded Matrix-Valued States and Dynamic Data-Driven Recurrence Mechanisms - MarkTechPost","url":"https://www.marktechpost.com/2024/04/12/eagle-rwkv-5-and-finch-rwkv-6-marking-substantial-progress-in-recurrent-neural-networks-based-language-models-by-integrating-multiheaded-matrix-valued-states-and-dynamic-data-driven-recurrence-me/"},{"title":"🦅 Eagle & 🐦 Finch - architecture paper is here","url":"https://blog.rwkv.com/p/eagle-and-finch-architecture-paper"},{"title":"Eagle (RWKV-5) and Finch (RWKV-6): Marking Substantial Progress in Recurrent Neural Networks-Based Language Models by Integrating Multiheaded Matrix-Valued States and Dynamic Data-Driven Recurrence Mechanisms Vineet Kumar Artificial Intelligence Category – MarkTechPost – PhD Studio","url":"https://phdstudio.org/2024/04/13/eagle-rwkv-5-and-finch-rwkv-6-marking-substantial-progress-in-recurrent-neural-networks-based-language-models-by-integrating-multiheaded-ma
…[truncated 1266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T18:25:18.912087+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml",
  "old_string": "        relevance: \"Primary data source — 72-model zoo of hybrid recurrent-attention architectures\"\n\n  - cluster_name: \"Linear Recurrent Models\"",
  "new_string": "        relevance: \"Primary data source — 72-model zoo of hybrid recurrent-attention architectures\"\n      - bibtex_key: lieber2024jamba\n        title: \"Jamba: A Hybrid Transformer-Mamba Language Model\"\n        authors: \"Lieber, Opher and others\"\n        year: 2024\n        venue: \"arXiv:2403.19887\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2403.19887\"\n        relevance: \"First production-scale hybrid interleaving Transformer and Mamba layers with MoE; key design reference for attention-ratio choices\"\n      - bibtex_key: peng2024eagle\n        title: \"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence\"\n        authors: \"Peng, Bo and others\"\n        year: 2024\n        venue: \"arXiv:2404.05892\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2404.05892\"\n        relevance: \"RWKV-5/6 with matrix-valued states and dynamic recurrence; pure-recurrent baseline in the hybrid architecture spectrum\"\n      - bibtex_key: de2024griffin\n        title: \"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models\"\n        authors: \"De, Soham and others\"\n        year: 2024\n        venue: \"arXiv:2402.19427\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2402.19427\"\n        relevance: \"Proposes Hawk (pure RNN) and Griffin (gated linear recurrence + local attention); matches Llama-2 with 6x fewer tokens\"\n      - bibtex_key: dao2024mamba2\n        title: \"Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality\"\n        authors: \"Dao, Tri and Gu, Albert\"\n        year: 2024\n        venue: \"ICML 2024\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2405.21060\"\n        relevance: \"Establishes SSD framework unifying SSMs and attention; Mamba-2 core layer used in many hybrid designs\"\n      - bibtex_key: botev2024recurrentgemma\n        title: \"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models\"\n        authors: \"Botev, Aleksandar and others\"\n        year: 2024\n        venue: \"arXiv:2404.07839\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2404.07839\"\n        relevance: \"Open-weight Griffin-based model combining linear recurrence with local sliding-window attention; directly comparable to hybrid zoo models\"\n      - bibtex_key: dong2024hymba\n        title: \"Hymba: A Hybrid-head Architecture for Small Language Models\"\n        authors: \"Dong, Xin and others\"\n        year: 2024\n        venue: \"arXiv:2411.13676\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2411.13676\"\n        relevance: \"Intra-layer head-wise hybrid mixing attention and SSM heads; contrasts with inter-layer hybrid designs like Jamba/Griffin\"\n\n  - cluster_name: \"Linear Recurrent Models\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml",
    "old_string": "        relevance: \"Primary data source — 72-model zoo of hybrid recurrent-attention architectures\"\n\n  - cluster_name: \"Linear Recurrent Models\"",
    "new_string": "        relevance: \"Primary data source — 72-model zoo of hybrid recurrent-attention architectures\"\n      - bibtex_key: lieber2024jamba\n        title: \"Jamba: A Hybrid Transformer-Mamba Language Model\"\n        authors: \"Lieber, Opher and others\"\n        year: 2024\n        venue: \"arXiv:2403.19887\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2403.19887\"\n        relevance: \"First production-scale hybrid interleaving Transformer and Mamba layers with MoE; key design reference for attention-ratio choices\"\n      - bibtex_key: peng2024eagle\n        title: \"Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence\"\n        authors: \"Peng, Bo and others\"\n        year: 2024\n        venue: \"arXiv:2404.05892\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2404.05892\"\n        relevance: \"RWKV-5/6 with matrix-valued states and dynamic recurrence; pure-recurrent baseline in the hybrid architecture spectrum\"\n      - bibtex_key: de2024griffin\n        title: \"Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models\"\n        authors: \"De, Soham and others\"\n        year: 2024\n        venue: \"arXiv:2402.19427\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2402.19427\"\n        relevance: \"Proposes Hawk (pure RNN) and Griffin (gated linear recurrence + local attention); matches Llama-2 with 6x fewer tokens\"\n      - bibtex_key: dao2024mamba2\n        title: \"Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality\"\n        authors: \"Dao, Tri and Gu, Albert\"\n        year: 2024\n        venue: \"ICML 2024\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2405.21060\"\n        relevance: \"Establishes SSD framework unifying SSMs and attention; Mamba-2 core layer used in many hybrid designs\"\n      - bibtex_key: botev2024recurrentgemma\n        title: \"RecurrentGemma: Moving Past Transformers for Efficient Open Language Models\"\n        authors: \"Botev, Aleksandar and others\"\n        year: 2024\n        venue: \"arXiv:2404.07839\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2404.07839\"\n        relevance: \"Open-weight Griffin-based model combining linear recurrence with local sliding-window attention; directly comparable to hybrid zoo models\"\n      - bibtex_key: dong2024hymba\n        title: \"Hymba: A Hybrid-head Architecture for Small Language Models\"\n        authors: \"Dong, Xin and others\"\n        year: 2024\n        venue: \"arXiv:2411.13676\"\n        category: \"Hybrid Architectures\"\n        verified: true\n        doi: \"\"\n        url: \"https://arxiv.org/abs/2411.13676\"\n        relevance: \"Intra-layer head-wise hybrid mixing attention and SSM heads; contrasts with inter-layer hybrid designs like Jamba/Griffin\"\n\n  - cluster_name: \"Linear Recurrent Models\""
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T18:25:18.912425+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T18:25:18.912656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft/literature_map.yaml",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T18:25:18.912924+00:00_

1	# Literature Map for entrainment_gated_ft
2	# Auto-generated skeleton; Workers will populate per cluster
3	
4	clusters:
5	  - cluster_name: "Hybrid Architectures"
6	    target_count: 7
7	    papers:
8	      - bibtex_key: wang2025hybrid
9	        title: "Scaling Laws for Hybrid Language Models"
10	        authors: "Wang, Junxiong and others"
11	        year: 2025
12	        venue: "arXiv:2507.06457"
13	        category: "Hybrid Architectures"
14	        verified: true
15	        doi: ""
16	        url: "https://arxiv.org/abs/2507.06457"
17	        relevance: "Primary data source — 72-model zoo of hybrid recurrent-attention architectures"
18	      - bibtex_key: lieber2024jamba
19	        title: "Jamba: A Hybrid Transformer-Mamba Language Model"
20	        authors: "Lieber, Opher and others"
21	        year: 2024
22	        venue: "arXiv:2403.19887"
23	        category: "Hybrid Architectures"
24	        verified: true
25	        doi: ""
26	        url: "https://arxiv.org/abs/2403.19887"
27	        relevance: "First production-scale hybrid interleaving Transformer and Mamba layers with MoE; key design reference for attention-ratio choices"
28	      - bibtex_key: peng2024eagle
29	        title: "Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence"
30	        authors: "Peng, Bo and others"
31	        year: 2024
32	        venue: "arXiv:2404.05892"
33	        category: "Hybrid Architectures"
34	        verified: true
35	        doi: ""
36	        url: "https://arxiv.org/abs/2404.05892"
37	        relevance: "RWKV-5/6 with matrix-valued states and dynamic recurrence; pure-recurrent baseline in the hybrid architecture spectrum"
38	      - bibtex_key: de2024griffin
39	        title: "Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models"
40	        authors: "De, Soham and others"
41	        year: 2024
42	        venue: "arXiv:2402.19427"
43	        category: "Hybrid Architectures"
44	        verified: true
45	        
…[truncated 1862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-19T18:25:18.913196+00:00_

YAML 格式正确，Hybrid Architectures cluster 现在有 7 篇论文（1 已有 + 6 新增）。

**新增 6 篇论文摘要：**

| bibtex_key | 标题 | 年份 | Venue | verified |
|---|---|---|---|---|
| `lieber2024jamba` | Jamba: A Hybrid Transformer-Mamba Language Model | 2024 | arXiv:2403.19887 | true |
| `peng2024eagle` | Eagle and Finch: RWKV with Matrix-Valued States and Dynamic Recurrence | 2024 | arXiv:2404.05892 | true |
| `de2024griffin` | Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models | 2024 | arXiv:2402.19427 | true |
| `dao2024mamba2` | Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality | 2024 | ICML 2024 | true |
| `botev2024recurrentgemma` | RecurrentGemma: Moving Past Transformers for Efficient Open Language Models | 2024 | arXiv:2404.07839 | true |
| `dong2024hymba` | Hymba: A Hybrid-head Architecture for Small Language Models | 2024 | arXiv:2411.13676 | true |

4 篇 must-cite 全部确认。额外 2 篇选了 RecurrentGemma（Griffin 架构的开源权重实现，inter-layer hybrid）和 Hymba（NVIDIA 的 intra-layer head-wise hybrid，与 Jamba/Griffin 的 inter-layer 设计形成对比）。Mamba-2 是唯一确认发表在顶会（ICML 2024）的论文，其余均为 arXiv preprint。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_lit_cluster_1_hybrid_20260519T182256"
}
```

</details>

---
