# paper research cluster2 infra

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_paper_research_cluster2_infra_20260521T181537.jsonl`
- **Structured JSON:** [`b08e17a256c79883e1b7.json`](../../sessions/b0/b08e17a256c79883e1b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-21T18:20:06.208060+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T18:20:06.208500+00:00_

1	meta:
2	  last_updated: "2026-05-20T14:00:00Z"
3	  total_papers: 16
4	
5	categories:
6	  - key: "gtheory_evaluation"
7	    name: "G-Theory & Evaluation Variance"
8	    narrative: "Applying Generalizability Theory and variance decomposition to LLM evaluation reliability"
9	  - key: "infrastructure_variance"
10	    name: "Infrastructure-Induced Variance"
11	    narrative: "Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference"
12	  - key: "prompt_sensitivity"
13	    name: "Prompt Sensitivity & Methodological Variance"
14	    narrative: "Prompt phrasing, seed, temperature, and ordering as variance sources"
15	  - key: "evaluation_methodology"
16	    name: "Evaluation Methodology"
17	    narrative: "Scoring artifacts, benchmark design, and evaluation protocol considerations"
18	
19	papers:
20	  mesting2026hidden:
21	    title: "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"
22	    authors:
23	      - "Messing, S."
24	    year: 2026
25	    venue: "arXiv"
26	    url: "https://arxiv.org/abs/2604.11581"
27	    category: "gtheory_evaluation"
28	    role: "direct-competitor"
29	    relevance: "Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology."
30	    verified: true
31	    added_by: "director"
32	    added_at: "2026-05-20T14:00:00Z"
33	
34	  brittlebench2026:
35	    title: "Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity"
36	    authors: []
37	    year: 2026
38	    venue: "arXiv"
39	    url: "https://arxiv.org/abs/2603.13285"
40	    category: "prompt_sensitivity"
41	    role: "direct-competitor"
42	    relevance: "Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single per
…[truncated 9509 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T18:20:06.208718+00:00_

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
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
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

_source line 4 · 2026-05-21T18:20:06.208860+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T18:20:06.209005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yuan LayerCast \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\" arXiv 2506.09501"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yuan LayerCast \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\" arXiv 2506.09501"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T18:20:06.209126+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Messina Scotta \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\" arXiv 2604.22411"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Messina Scotta \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\" arXiv 2604.22411"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T18:20:06.209242+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Batch Invariance Seed Locking\" \"Countering Nondeterminism in LLM Inference\" ThinkingMachines 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Batch Invariance Seed Locking\" \"Countering Nondeterminism in LLM Inference\" ThinkingMachines 2025"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T18:20:06.209374+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "numerical precision GPU nondeterminism LLM inference floating point reproducibility 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "numerical precision GPU nondeterminism LLM inference floating point reproducibility 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T18:20:06.209516+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CUDA nondeterminism deep learning inference hardware variance reproducibility neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CUDA nondeterminism deep learning inference hardware variance reproducibility neural network"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T18:20:06.209664+00:00_

Web search results for query: "Yuan LayerCast "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference" arXiv 2506.09501"

Links: [{"title":"[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/abs/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=Q3qAsZAEZw"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250609501Y/abstract"},{"title":"NeurIPS Poster Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/118169"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.09501"},{"title":"NeurIPS 2025 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference Oral","url":"https://neurips.cc/virtual/2025/oral/130305"},{"title":"GitHub - nanomaoli/llm_reproducibility · GitHub","url":"https://github.com/nanomaoli/llm_reproducibility"}]

I found the paper! Here's what I found about it:

This work presents the first systematic investigation into how numerical precision affects reproducibility in LLM inference, quantifying when and how model outputs diverge through carefully controlled experiments across various hardware, software, and precision settings.

The paper demonstrates that LLM reproducibility is fragile—changing system configuration such as evaluation batch size, GPU count, and GPU version can introduce significant differences in generated responses, with this issue being especially pronounced in reasoning models where minor rounding differe
…[truncated 919 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T18:20:06.209820+00:00_

Web search results for query: "Messina Scotta "Introducing Background Temperature to Characterise Hidden Randomness in LLMs" arXiv 2604.22411"

Links: [{"title":"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models","url":"https://arxiv.org/html/2604.22411"},{"title":"[2604.22411] Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models","url":"https://arxiv.org/abs/2604.22411"},{"title":"The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior","url":"https://arxiv.org/pdf/2512.12066"},{"title":"[2604.22771] The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model Token Distributions","url":"https://arxiv.org/abs/2604.22771"},{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12375657/"}]

I found the paper! Here's what the search reveals:

The paper "Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models" is by Alberto Messina and Stefano Scotta from RAI (Radiotelevisione Italiana), Centre for Research, Technological Innovation and Experimentation (CRITS), published on arXiv as 2604.22411 on April 24, 2026.

The paper addresses how large language models can produce divergent outputs for identical inputs even when decoding with temperature T=0. Recent work has highlighted implementation-level sources of nondeterminism, including batch-size variation, kernel non-invariance, and floating-point non-associativity.

The authors formalize this behavior by introducing the notion of "background temperature" (T_bg), the effective temperature induced by an implementation-dependent perturbation process observed even when nominal T=0. They provide clean definitions, show how T_bg relates to a stochastic perturbation governed by the inference en
…[truncated 337 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T18:20:06.209991+00:00_

Web search results for query: "numerical precision GPU nondeterminism LLM inference floating point reproducibility 2024 2025"

Links: [{"title":"[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/abs/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=Q3qAsZAEZw"},{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"NeurIPS Poster Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/118169"},{"title":"NeurIPS 2025 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference Oral","url":"https://neurips.cc/virtual/2025/loc/mexico-city/oral/130305"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250609501Y/abstract"},{"title":"GitHub - nanomaoli/llm_reproducibility · GitHub","url":"https://github.com/nanomaoli/llm_reproducibility"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.17826"}]

Here are the search results for your query on numerical precision, GPU nondeterminism, LLM inference, floating point, and reproducibility from 2024-2025:

## Key Findings

The first systematic investigation into how numerical precision affects reproducibility in LLM inference was recently published. Changing system configuration, such as evaluation batch size, GPU count, and GPU version, can introduce significant differences in the generated resp
…[truncated 1321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T18:20:06.210162+00:00_

Web search results for query: ""Batch Invariance Seed Locking" "Countering Nondeterminism in LLM Inference" ThinkingMachines 2025"

Links: [{"title":"Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"},{"title":"(PDF) BATCH INVARIANCE, SEED LOCKING, AND BEYOND: COUNTERING NONDETERMINISM IN LLM INFERENCE","url":"https://www.researchgate.net/publication/395667341_BATCH_INVARIANCE_SEED_LOCKING_AND_BEYOND_COUNTERING_NONDETERMINISM_IN_LLM_INFERENCE"},{"title":"Defeating Nondeterminism in LLM Inference: Theory to Deterministic Code Edits | Morph","url":"https://www.morphllm.com/defeating-nondeterminism-llm-inference"},{"title":"Defeating Nondeterminism in LLM Inference","url":"https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Musing 137: Defeating Nondeterminism in LLM Inference","url":"https://aiscientist.substack.com/p/musing-137-defeating-nondeterminism"},{"title":"Defeating nondeterminism in LLM inference, in practice | by Siddhant Gupta | Medium","url":"https://medium.com/@siddhantg314/defeating-nondeterminism-in-llm-inference-in-practice-38a7dd1e4112"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Explained: Defeating Nondeterminism in LLM Inference","url":"https://www.llmwatch.com/p/eli5-defeating-nondeterminism-in"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury","url":"https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"}]

I found relevant results for your se
…[truncated 1741 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T18:20:06.210428+00:00_

Web search results for query: "CUDA nondeterminism deep learning inference hardware variance reproducibility neural network"

Links: [{"title":"Solving Reproducibility Challenges in Deep Learning and LLMs: Our Journey","url":"https://www.ingonyama.com/post/solving-reproducibility-challenges-in-deep-learning-and-llms-our-journey"},{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"IMPLEMENTATIONS OF THE PARALLEL SUM IN CUDA. NON-DETERMINISTIC... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/IMPLEMENTATIONS-OF-THE-PARALLEL-SUM-IN-CUDA-NON-DETERMINISTIC-IMPLEMENTATIONS-SHOWN-IN_tbl2_387848485"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"Issues in the Reproducibility of Deep Learning Results","url":"https://par.nsf.gov/servlets/purl/10199663"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC   and deep learning applications","url":"https://arxiv.org/pdf/2408.05148"},{"title":"Defeating Nondeterminism: Achieving Predictable LLM Inference for AI Reliability","url":"https://nishadil.com/news/unlocking-predictability-conquering-nondeterminism-in-llm-inference-for-a-reliable-ai-future/3fcac37c348c0f9edcbac001a1d206c7"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow","url":"https://arxiv.org/html/2408.05148v3"}]

I've found comprehensive information on CUDA nondeterminism in deep lea
…[truncated 1793 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T18:20:06.210711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2506.09501 Yuan LayerCast authors full list NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2506.09501 Yuan LayerCast authors full list NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T18:20:06.210898+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications\" arXiv 2408.05148 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications\" arXiv 2408.05148 authors"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T18:20:06.211078+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Thinking Machines Lab \"batch invariance\" nondeterminism LLM authors blog 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Thinking Machines Lab \"batch invariance\" nondeterminism LLM authors blog 2025"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T18:20:06.211243+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GPU hardware type LLM inference accuracy variation empirical study A100 H100 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GPU hardware type LLM inference accuracy variation empirical study A100 H100 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T18:20:06.211459+00:00_

Web search results for query: ""Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications" arXiv 2408.05148 authors"

Links: [{"title":"[Literature Review] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://www.themoonlight.io/en/review/impacts-of-floating-point-non-associativity-on-reproducibility-for-hpc-and-deep-learning-applications"},{"title":"[2408.05148] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://arxiv.org/abs/2408.05148"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | ORNL","url":"https://www.ornl.gov/publication/impacts-floating-point-non-associativity-reproducibility-hpc-and-deep-learning"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/10820557/10820558/10820674.pdf"},{"title":"(PDF) Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://www.researchgate.net/publication/387848485_Impacts_of_floating-point_non-associativity_on_reproducibility_for_HPC_and_deep_learning_applications"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow","url":"https://arxiv.org/html/2408.05148v1"},{"title":"Impacts of floating-point non-associativity on rep
…[truncated 1466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T18:20:06.211699+00:00_

Web search results for query: "GPU hardware type LLM inference accuracy variation empirical study A100 H100 2024 2025"

Links: [{"title":"Private LLM Inference on Consumer Blackwell GPUs:","url":"https://arxiv.org/pdf/2601.09527"},{"title":"Best GPUs for LLM inference in 2025 | WhiteFiber","url":"https://www.whitefiber.com/compare/best-gpus-for-llm-inference-in-2025"},{"title":"Which GPUs Are Best Optimized for LLM Inference Workloads?","url":"https://www.gmicloud.ai/en/blog/which-gpus-are-best-optimized-for-llm-inference-workloads"},{"title":"LLM-Inference-Bench: Inference Benchmarking of","url":"https://arxiv.org/pdf/2411.00136"},{"title":"Understanding Performance Implications of LLM Inference on CPUs","url":"https://par.nsf.gov/servlets/purl/10576248"},{"title":"Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective","url":"https://arxiv.org/html/2410.04466v3"}]

I've completed the web search for your query. Here's what I found:

## Key Research Findings

The search results reveal several relevant studies on GPU hardware performance for LLM inference, particularly comparing A100 and H100 GPUs:

**Performance Comparisons:**
For a batch size of 64, LLaMA-3-70B on H100 is 7.8x faster than A100. Additionally, H100 GPU scales efficiently with an increase in batch size due to large DRAM and tensor core utilization compared to A100.

**Empirical Studies:**
- One benchmark study (LLM-Inference-Bench) evaluated LLaMA-3-8B and Mistral-7B on A100 and H100 GPUs, examining various inference optimization techniques.

- Another comprehensive hardware perspective study achieved 113.7-121.7 tokens/s on NVIDIA A100 GPUs for Llama3-8B with 4-bit quantization.

**Recent 2025 Research:**
A recent systematic evaluation of consumer GPUs benchmarked four open-weight models across 79 configurations spanning quantization formats (BF16, W4A16, NVFP4, MXFP4), context lengths (8k–64k), and three workloads: RAG, multi-LoRA agentic serving, and high-concurrency APIs
…[truncated 322 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T18:20:06.211945+00:00_

Web search results for query: "Thinking Machines Lab "batch invariance" nondeterminism LLM authors blog 2025"

Links: [{"title":"Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"},{"title":"Defeating Nondeterminism in LLM Inference","url":"https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/"},{"title":"Defeating nondeterminism in LLM inference, in practice | by Siddhant Gupta | Medium","url":"https://medium.com/@siddhantg314/defeating-nondeterminism-in-llm-inference-in-practice-38a7dd1e4112"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Towards Deterministic Inference in SGLang and Reproducible RL Training - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-09-22-sglang-deterministic/"},{"title":"The Deterministic LLM: Engineering Batch Invariance to Restore Data Integrity in Inference Pipelines","url":"https://blog.singlr.ai/non_deterministic_llm/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury","url":"https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines ...","url":"https://www.mbgsec.com/_archive/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"},{"title":"Billion-Dollar Unicorn Releases Long Article Solving LLM Inference Non - Deterministic Problem in First Public Statement After 7 - Month Establishment","url":"https://eu.36kr.com/en/p/3461963944908162"}]

Bas
…[truncated 1592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T18:20:06.212176+00:00_

Web search results for query: "arXiv 2506.09501 Yuan LayerCast authors full list NeurIPS 2025"

Links: [{"title":"[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/abs/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501"},{"title":"Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning","url":"https://arxiv.org/html/2506.09501v1"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"Anchor-controlled generative adversarial network for high-fidelity electromagnetic and structurally diverse metasurface design","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12397733/"},{"title":"Layer-wise Instance Binding for Regional and Occlusion Control in Text-to-Image Diffusion Transformers","url":"https://arxiv.org/pdf/2603.05769"}]

Based on the search results, I found the paper arXiv 2506.09501. Here are the full author details:

The authors are: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, and Zirui Liu.

The paper is titled "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference" and was accepted to the 39th Conference on Neural Information Processing Systems (NeurIPS 2025). The paper develops a lightweight inference pipeline called LayerCast, which stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T18:20:06.212440+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2408.05148 Shanmugavelu floating-point non-associativity SC24 venue DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2408.05148 Shanmugavelu floating-point non-associativity SC24 venue DOI"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-21T18:20:06.212638+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SGLang deterministic inference reproducible RL training LMSYS 2025 arXiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SGLang deterministic inference reproducible RL training LMSYS 2025 arXiv paper"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T18:20:06.212768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "vLLM nondeterminism reproducibility inference framework benchmark 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "vLLM nondeterminism reproducibility inference framework benchmark 2024 2025 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T18:20:06.212916+00:00_

Web search results for query: "arXiv 2408.05148 Shanmugavelu floating-point non-associativity SC24 venue DOI"

Links: [{"title":"(PDF) Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://www.researchgate.net/publication/387848485_Impacts_of_floating-point_non-associativity_on_reproducibility_for_HPC_and_deep_learning_applications"},{"title":"[2408.05148] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://arxiv.org/abs/2408.05148"},{"title":"SC24 Proceedings","url":"https://sc24.supercomputing.org/proceedings/workshops/workshop_pages/ws_corr108.html"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | ORNL","url":"https://www.ornl.gov/publication/impacts-floating-point-non-associativity-reproducibility-hpc-and-deep-learning"},{"title":"au:Shanmugavelu_S in:cs - SciRate Search","url":"https://scirate.com/search?q=au:Shanmugavelu_S+in:cs"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis","url":"https://dl.acm.org/doi/10.1109/SCW63240.2024.00028"},{"title":"Presentation – SC24 Schedule","url":"https://sc24.conference-program.com/presentation/?id=ws_corr108&sess=sess759"},{"title":"Impacts of Floating-Point non-Associativity on ...","url":"https://conferences.computer.org/sc-wpub/pdfs/SC-W2024-6oZmigAQfgJ1GhPL0yE3pS/555400a170/555400a170.pdf"},{"title":"Impacts of floating-point non-associativity on reproducibility ...","url":"https://arxiv.org/pdf/2408.05148"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Paper Details

The paper is titled "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning
…[truncated 1147 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T18:20:06.213092+00:00_

Web search results for query: "SGLang deterministic inference reproducible RL training LMSYS 2025 arXiv paper"

Links: [{"title":"Towards Deterministic Inference in SGLang and Reproducible RL Training - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-09-22-sglang-deterministic/"},{"title":"LMSYS Org on X: \"SGLang now supports deterministic LLM inference! Building on @thinkymachines batch-invariant kernels, we integrated deterministic attention &amp; sampling ops into a high-throughput engine - fully compatible with chunked prefill, CUDA graphs, radix cache, and non-greedy sampling. ✅ https://t.co/drH8Z0eKag\" / X","url":"https://x.com/lmsysorg/status/1970240927429206161"},{"title":"Deterministic Inference — SGLang","url":"https://sgl-project.github.io/advanced_features/deterministic_inference.html"},{"title":"sglang/docs/advanced_features/deterministic_inference.md at main · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/deterministic_inference.md"},{"title":"GitHub - aerlabsAI/ai-inference-resources: Curated collection of AI inference engineering resources — LLM serving, GPU kernels, quantization, distributed inference, and production deployment. Compiled from the AER Labs community.","url":"https://github.com/aerlabsAI/ai-inference-resources"},{"title":"DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2026-04-25-deepseek-v4/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/pdf/2511.17826"},{"title":"LLM-42: Enabling Determinism in LLM Inference with Verified Speculation","url":"https://arxiv.org/html/2601.17768v1"},{"tit
…[truncated 1841 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T18:20:06.213273+00:00_

Web search results for query: "vLLM nondeterminism reproducibility inference framework benchmark 2024 2025 arXiv"

Links: [{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning","url":"https://arxiv.org/html/2506.09501v1"},{"title":"GitHub - nanomaoli/llm_reproducibility · GitHub","url":"https://github.com/nanomaoli/llm_reproducibility"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/pdf/2511.17826"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.17826v1"},{"title":"Quantifying non‑deterministic drift in large language models","url":"https://arxiv.org/html/2601.19934v1"},{"title":"DiFR: Inference Verification Despite Nondeterminism","url":"https://arxiv.org/html/2511.20621"}]

Based on the web search results, I found several recent arXiv papers addressing vLLM nondeterminism, reproducibility, and inference frameworks in 2024-2025:

## Key Papers Found:

**1. "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning" (2025)**
This paper by Jiayi Yuan et al. (arXiv:2506.09501) addresses challenges and solutions for reproducible reasoning. The authors primarily use vLLM as the inference backend and conduct experiments on four recent LLMs across five commonly used LLM evaluation benchmarks including AIME'24, MATH500, and LiveCodeBench. They propose LayerCast, an optimized FP32 inference pipeline that performs computations in FP32 while retaining model weights in BF16 precision, balancing memory efficiency and reproducibility, released as a patch to vLLM.

**2. "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch" (2025)**
A
…[truncated 1121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T18:20:06.213484+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Deterministic Inference across Tensor Parallel Sizes\" TBIK arXiv 2511.17826 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Deterministic Inference across Tensor Parallel Sizes\" TBIK arXiv 2511.17826 authors venue"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T18:20:06.213617+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Quantifying non-deterministic drift in large language models\" arXiv 2601.19934 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Quantifying non-deterministic drift in large language models\" arXiv 2601.19934 authors"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T18:20:06.213773+00:00_

Web search results for query: ""Quantifying non-deterministic drift in large language models" arXiv 2601.19934 authors"

Links: [{"title":"[2601.19934] Quantifying non deterministic drift in large language models","url":"https://arxiv.org/abs/2601.19934"},{"title":"Quantifying non deterministic drift in large language models","url":"https://arxiv.org/pdf/2601.19934"},{"title":"Quantifying non‑deterministic drift in large language models","url":"https://arxiv.org/html/2601.19934v1"},{"title":"Quantifying Non‑Deterministic Drift in Large Language Models","url":"https://ubos.tech/quantifying-non%E2%80%91deterministic-drift-in-large-language-models-research-summary/"},{"title":"Entropy-Based Measurement of Value Drift and Alignment Work in Large Language Models","url":"https://arxiv.org/pdf/2512.03047"},{"title":"Non-Determinism of \"Deterministic\" LLM Settings","url":"https://arxiv.org/pdf/2408.04667"},{"title":"Benchmarking Large Language Model Volatility","url":"https://arxiv.org/pdf/2311.15180"},{"title":"LLM Output Drift: Cross-Provider Validation & Mitigation for Financial Workflows","url":"https://arxiv.org/pdf/2511.07585"}]

Based on the search results, I found the paper you're looking for:

**Title:** Quantifying non deterministic drift in large language models

**ArXiv ID:** 2601.19934

**Author:** Claire Nicholson

**Submitted:** January 12, 2026

**Summary:** The paper conducts repeated-run experiments to empirically quantify baseline behavioural drift, evaluating two publicly accessible models, gpt-4o-mini and llama3.1-8b, across five prompt categories using exact repeats, perturbed inputs, and reuse modes at temperatures of 0.0 and 0.7. The results show that nondeterminism persists even at temperature 0.0, with distinct variability patterns by model size, deployment, and prompt type.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T18:20:06.213956+00:00_

Web search results for query: ""Deterministic Inference across Tensor Parallel Sizes" TBIK arXiv 2511.17826 authors venue"

Links: [{"title":"[2511.17826] Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/abs/2511.17826"},{"title":"Deterministic Inference across Tensor Parallel Sizes That ...","url":"https://arxiv.org/pdf/2511.17826"},{"title":"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch | Request PDF","url":"https://www.researchgate.net/publication/397932505_Deterministic_Inference_across_Tensor_Parallel_Sizes_That_Eliminates_Training-Inference_Mismatch"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.17826"},{"title":"Tensor Parallel LLM Inferencing. As models increase in size, it becomes… | by Sneha Ghantasala | Thomson Reuters Labs | Medium","url":"https://medium.com/tr-labs-ml-engineering-blog/tensor-parallel-llm-inferencing-09138daf0ba7"},{"title":"Flash Communication: Reducing Tensor Parallelization Bottleneck for Fast   Large Language Model Inference","url":"https://arxiv.org/pdf/2412.04964"},{"title":"TPI-LLM: Serving 70B-scale LLMs Efficiently on Low-resource Edge Devices","url":"https://arxiv.org/pdf/2410.00531"}]

Based on the search results, here is the information about the paper:

**Title:** Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch

**ArXiv ID:** 2511.17826

**Authors:** Ziyang Zhang and 6 other authors. Additional author names visible in the search results include Xinheng Ding, Jiayi Yuan, and Rixin Liu.

**Main Contribution:** The paper proposes Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size.

**Venue:** The paper appears to be a preprint submitted to arXiv (cs.LG category - Computer Science: Machine Learning) on November 21, 2025. It i
…[truncated 277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T18:20:06.214140+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2511.17826 \"Ziyang Zhang\" TBIK full author list deterministic inference tensor parallel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2511.17826 \"Ziyang Zhang\" TBIK full author list deterministic inference tensor parallel"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-21T18:20:06.214261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Thinking Machines Lab \"Horace He\" \"defeating nondeterminism\" paper ResearchGate authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Thinking Machines Lab \"Horace He\" \"defeating nondeterminism\" paper ResearchGate authors full list"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-21T18:20:06.214407+00:00_

Web search results for query: "arXiv 2511.17826 "Ziyang Zhang" TBIK full author list deterministic inference tensor parallel"

Links: [{"title":"[2511.17826] Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/abs/2511.17826"},{"title":"System and methods for upsampling of decompressed genomic data after lossy compression using a neural network","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12417386"},{"title":"Identification of bioactive constituents for colitis from traditional Chinese medicine prescription via deep neural network","url":"https://www.biorxiv.org/content/10.1101/2023.05.31.542690.full.pdf"},{"title":"Scintillator ageing of the T2K near detectors from 2010 to 2021","url":"https://arxiv.org/pdf/2207.12982"},{"title":"Testing T2K's Bayesian constraints with priors in alternate parameterisations","url":"https://arxiv.org/pdf/2507.02101"}]

Perfect! I found the arXiv paper. According to the search results, the paper "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch" is by Ziyang Zhang and 6 other authors.

However, the search results only mention that there are 6 additional authors beyond Ziyang Zhang, but don't provide the complete list of all author names. To get the full author list, you would need to visit the arXiv page directly at https://arxiv.org/abs/2511.17826 or view the PDF.

The paper's main contribution is proposing Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size, which addresses the issue of non-deterministic behavior in LLM serving frameworks where identical inputs can yield different outputs when system configurations vary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T18:20:06.214587+00:00_

Web search results for query: "Thinking Machines Lab "Horace He" "defeating nondeterminism" paper ResearchGate authors full list"

Links: [{"title":"Connectionism - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Mira Murati’s New AI Lab Wants to Fix a Hidden Problem in LLMs | by Luna | Machine Learning Reviews | Medium","url":"https://medium.com/lunas-orbit/mira-muratis-new-ai-lab-wants-to-fix-a-hidden-problem-in-llms-6ab72dffd6fe"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Thinking Machines Lab wants to make AI models more consistent | TechCrunch","url":"https://techcrunch.com/2025/09/10/thinking-machines-lab-wants-to-make-ai-models-more-consistent/"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury","url":"https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"},{"title":"Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"},{"title":"Inside Thinking Machines Lab: Murati’s $12 billion AI startup tackles reproducibility","url":"https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/"}]

Based on the search results, I found information about the "Defeating Nondeterminism in LLM Inference" paper by Horace He in collaboration with others at Thinking Machines Lab, published September 10, 2025.

However, the search results show this is a **blog post** published on the Thinking Machines Lab
…[truncated 939 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T18:20:06.214743+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T18:20:06.214861+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T18:20:06.214971+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.17826",
  "prompt": "Extract the complete list of all authors and the submission date for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2511.17826",
    "prompt": "Extract the complete list of all authors and the submission date for this paper."
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T18:20:06.215083+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
  "prompt": "Extract the author name(s), publication date, and any formal citation information (e.g. technical report number, DOI) for this blog post."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
    "prompt": "Extract the author name(s), publication date, and any formal citation information (e.g. technical report number, DOI) for this blog post."
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T18:20:06.215200+00:00_

# Paper Authors and Submission Date

**Authors:**
1. Ziyang Zhang
2. Xinheng Ding
3. Jiayi Yuan
4. Rixin Liu
5. Huizi Mao
6. Jiarong Xing
7. Zirui Liu

**Submission Date:** November 21, 2025

The paper was "Submitted on 21 Nov 2025" according to the arXiv metadata displayed on the page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T18:20:06.215316+00:00_

# Citation Information for "Defeating Nondeterminism in LLM Inference"

**Author(s):** Horace He in collaboration with others at Thinking Machines Lab

**Publication Date:** September 10, 2025

**Formal Citation Information:**

The post provides its own suggested citations:

Chicago-style format: "He, Horace and Thinking Machines Lab, 'Defeating Nondeterminism in LLM Inference', Thinking Machines Lab: Connectionism, Sep 2025."

BibTeX format:
```
@article{he2025nondeterminism,
  author = {Horace He and Thinking Machines Lab},
  title = {Defeating Nondeterminism in LLM Inference},
  journal = {Thinking Machines Lab: Connectionism},
  year = {2025},
  note = {https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/},
  doi = {10.64434/tml.20250910}
}
```

**DOI:** 10.64434/tml.20250910

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T18:20:06.215498+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "meta:\n  last_updated: \"2026-05-20T14:00:00Z\"\n  total_papers: 16",
  "new_string": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "meta:\n  last_updated: \"2026-05-20T14:00:00Z\"\n  total_papers: 16",
    "new_string": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T18:20:06.215666+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-21T18:20:06.215797+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T18:20:06.215999+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T18:20:06.216123+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"\n    authors:\n      - \"Messina, A.\"\n      - \"Scotta, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"\n    authors:\n      - \"Messina, A.\"\n      - \"Scotta, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T18:20:06.216319+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T18:20:06.216465+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  thinkingmachines2025batch:\n    title: \"Defeating Nondeterminism in LLM Inference\"\n    authors:\n      - \"He, H.\"\n      - \"Thinking Machines Lab\"\n    year: 2025\n    venue: \"Thinking Machines Lab: Connectionism\"\n    url: \"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/\"\n    doi: \"10.64434/tml.20250910\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "new_string": "  thinkingmachines2025batch:\n    title: \"Defeating Nondeterminism in LLM Inference\"\n    authors:\n      - \"He, H.\"\n      - \"Thinking Machines Lab\"\n    year: 2025\n    venue: \"Thinking Machines Lab: Connectionism\"\n    url: \"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/\"\n    doi: \"10.64434/tml.20250910\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-21T18:20:06.216656+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-21T18:20:06.216788+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "offset": "255"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "offset": "255"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T18:20:06.216913+00:00_

255	      - "Lignos, C."
256	    year: 2025
257	    venue: "IJCNLP-AACL"
258	    url: "https://arxiv.org/abs/2509.22612"
259	    category: "gtheory_evaluation"
260	    role: "background"
261	    relevance: "Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error."
262	    verified: true
263	    added_by: "worker"
264	    added_at: "2026-05-21T00:00:00Z"
265	
266	  song2025exploring:
267	    title: "Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory"
268	    authors:
269	      - "Song, D."
270	      - "Lee, W.-C."
271	      - "Jiao, H."
272	    year: 2025
273	    venue: "arXiv"
274	    url: "https://arxiv.org/abs/2507.19980"
275	    category: "gtheory_evaluation"
276	    role: "background"
277	    relevance: "Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation."
278	    verified: true
279	    added_by: "worker"
280	    added_at: "2026-05-21T00:00:00Z"
281	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T18:20:06.217042+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    added_at: \"2026-05-21T00:00:00Z\"\n",
  "new_string": "    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "    added_at: \"2026-05-21T00:00:00Z\"\n",
    "new_string": "    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T18:20:06.217278+00:00_

&lt;tool_use_error>Found 6 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_at: "2026-05-21T00:00:00Z"
&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T18:20:06.217433+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"",
  "new_string": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "old_string": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"",
    "new_string": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\""
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T18:20:06.217666+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T18:20:06.217809+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "infrastructure_variance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Grep",
  "tool_args": {
    "pattern": "infrastructure_variance",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "output_mode": "count"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T18:20:06.217930+00:00_

6

Found 0 total occurrences across 0 files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T18:20:06.218060+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "category: \"infrastructure_variance\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "output_mode": "content",
  "-A": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Grep",
  "tool_args": {
    "pattern": "category: \"infrastructure_variance\"",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "output_mode": "content",
    "-A": "2"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-21T18:20:06.218184+00:00_

63:    category: "infrastructure_variance"
64-    role: "direct-competitor"
65-    relevance: "Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources."
--
78:    category: "infrastructure_variance"
79-    role: "method-component"
80-    relevance: "Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure."
--
123:    category: "infrastructure_variance"
124-    role: "method-component"
125-    relevance: "Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions."
--
295:    category: "infrastructure_variance"
296-    role: "background"
297-    relevance: "Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference."
--
315:    category: "infrastructure_variance"
316-    role: "method-component"
317-    relevance: "Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_cluster2_infra_20260521T181537",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-21T18:20:06.218349+00:00_

5 infrastructure_variance papers, all verified. Here's the summary:

## Infrastructure Variance Cluster — 5 papers verified

| # | Key | Paper | Venue | Status |
|---|-----|-------|-------|--------|
| 1 | `yuan2025layercast` | Yuan et al. — LayerCast, up to 9% accuracy variation from precision/GPU | NeurIPS 2025 (Oral) | verified, authors+venue updated |
| 2 | `messina2026background` | Messina & Scotta — background temperature T_bg formalization | arXiv 2604.22411 | verified, title+authors corrected |
| 3 | `thinkingmachines2025batch` | He & Thinking Machines Lab — batch-invariant kernels, 80/1000 unique at T=0 | Connectionism blog, DOI: 10.64434/tml.20250910 | verified, title+authors+URL+DOI added |
| 4 | `shanmugavelu2024floating` | Shanmugavelu et al. — FP non-associativity in CUDA reductions | SC'24 Workshops (IEEE) | **NEW**, verified |
| 5 | `zhang2025tbik` | Zhang et al. — TBIK for TP-invariant deterministic inference | arXiv 2511.17826 | **NEW**, verified |

Key corrections made:
- Yuan et al. venue upgraded from "arXiv" to "NeurIPS 2025 (Oral)", full 10-author list added
- Messina authors corrected: Alberto Messina → `Messina, A.`, Stefano Scotta → `Scotta, S.`
- ThinkingMachines title updated to official citation "Defeating Nondeterminism in LLM Inference", author Horace He added, DOI added
- `total_papers` updated 16 → 18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_cluster2_infra_20260521T181537"
}
```

</details>

---
