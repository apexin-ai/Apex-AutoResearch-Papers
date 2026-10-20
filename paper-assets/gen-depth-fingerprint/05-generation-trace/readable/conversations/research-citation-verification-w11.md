# research citation verification w11

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 27
- **Original source:** `logs/chats/worker_research_citation_verification_w11_20260520T155942.jsonl`
- **Structured JSON:** [`9416999d9ae16beeb908.json`](../../sessions/94/9416999d9ae16beeb908.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

55 recorded events

### Tool call

_source line 1 · 2026-05-20T16:05:21.080141+00:00_

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
  "session": "worker_research_citation_verification_w11_20260520T155942",
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

_source line 2 · 2026-05-20T16:05:21.080434+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T16:05:21.080650+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang attractor cycles recursive generation ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang attractor cycles recursive generation ACL 2025"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T16:05:21.080834+00:00_

Web search results for query: "Wang attractor cycles recursive generation ACL 2025"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing [Quick Review]","url":"https://liner.com/review/unveiling-attractor-cycles-in-large-language-models-dynamical-systems-view"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/html/2502.15208v1"},{"title":"A Dynamical Systems View of Successive Paraphrasing","url":"https://aclanthology.org/2025.acl-long.624.pdf"},{"title":"DTCRS: Dynamic Tree Construction for Recursive Summarization - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.536/"},{"title":"Unlocking Recursive Thinking of LLMs: Alignment via Refinement - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.582/"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/pdf/2502.15208"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | Request PDF","url":"https://www.researchgate.net/publication/394299645_Unveiling_Attractor_Cycles_in_Large_Language_Models_A_Dynamical_Systems_View_of_Successive_Paraphrasing"}]

## Search Results

I found relevant information about a paper on attractor cycles in large language models presented at ACL 2025. Here's what the research found:

The study reveals that successive paraphrasing converges to stable periodic states, such as 2-period attractor cycles, limitin
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T16:05:21.080986+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Sun late-stage stability iterative text generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Sun late-stage stability iterative text generation 2026"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T16:05:21.081129+00:00_

Web search results for query: "Sun late-stage stability iterative text generation 2026"

Links: [{"title":"[2601.04833] When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/abs/2601.04833"},{"title":"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/html/2601.04833v1"},{"title":"Text to Video Scene Stability: 2026 AI Generation Guide","url":"https://resource.digen.ai/text-to-video-scene-stability-guide-2026/"},{"title":"Unrestricted AI: Image, Video, and Text Generation (2026) | VideoAny Guide","url":"https://videoany.io/guides/ai-with-no-restrictions"},{"title":"A Survey on Parallel Text Generation: From Parallel Decoding to Diffusion Language Models","url":"https://arxiv.org/html/2508.08712v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=235&show=1000"},{"title":"When Large Language Models Meet Evolutionary Algorithms: Potential Enhancements and Challenges | Research","url":"https://spj.science.org/doi/10.34133/research.0646"}]

Based on the search results, I found the most relevant research:

The study "When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection" analyzes over 120k text samples and reveals Late-Stage Volatility Decay, where AI-generated text exhibits rapidly stabilizing log probability fluctuations as generation progresses, while human writing maintains higher variability throughout.

This divergence peaks in the second half of sequences, where AI-generated text shows 24--32% lower volatility. Based on this finding, the researchers propose two simple features: Derivative Dispersion and Local Volatility, which are computed exclusively from late-stage statistics.

Without perturbation sampling or additional model access, their method achieves state-of-the-art performance on EvoBench and MAGE benchmarks and demonstrates strong complementarity with existing global me
…[truncated 365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T16:05:21.081278+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo iterative retraining stability ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo iterative retraining stability ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T16:05:21.081437+00:00_

Web search results for query: "Guo iterative retraining stability ICLR 2024"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=JORAfH2xFd"},{"title":"GitHub - QB3/gen_models_dont_go_mad: Code to reproduce the experiments of the ICLR 2024 (spotlight) paper \"On the Stability of Iterative Retraining of Generative Models on their Own Data\" https://arxiv.org/abs/2310.00429","url":"https://github.com/QB3/gen_models_dont_go_mad"},{"title":"On the Stability of Iterative Retraining of Generative Models on their own Data | OpenReview","url":"https://openreview.net/forum?id=JORAfH2xFd"},{"title":"GitHub - ANLGBOY/ICLR-2024-OpenReview-Ratings · GitHub","url":"https://github.com/ANLGBOY/ICLR-2024-OpenReview-Ratings"},{"title":"ON THE STABILITY OF ITERATIVE RETRAINING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/339cab2a98edcba2d4ac42e5f8b64218-Paper-Conference.pdf"},{"title":"On the Stability of Iterative Retraining of Generative Models ...","url":"https://arxiv.org/pdf/2310.00429"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Could we see the collapse of generative AI? | Inria","url":"https://www.inria.fr/en/collapse-ia-generatives"},{"title":"Probing RLVR training instability through the lens of objective-level hacking","url":"https://arxiv.org/pdf/2602.01103"}]

Based on the search results, here's what I found about the paper on iterative retraining stability from ICLR 2024:

The paper is titled "On the Stability of Iterative Retraining of Generative Models on their Own Data," presented as a spotlight paper at ICLR 2024.

**Main Contributions:**

The paper shows the stability of iterative retraining of deep generative models by proving the existence of a fixed point under the following conditions: the first iteration generative model is sufficiently "well-trained" and each retraining iteration keeps a high enough proportion of the original clean data.

**Ke
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T16:05:21.081608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li self-consuming generative models 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li self-consuming generative models 2024"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T16:05:21.081792+00:00_

Web search results for query: "Li self-consuming generative models 2024"

Links: [{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences | OpenReview","url":"https://openreview.net/forum?id=cyv0LkIaoH"},{"title":"GitHub - nate-gillman/self-correcting-self-consuming: Official implementation of \"Self-Correcting Self-Consuming Loops for Generative Model Training\" (ICML 2024)","url":"https://github.com/nate-gillman/self-correcting-self-consuming"},{"title":"[Quick Review] Self-Correcting Self-Consuming Loops for Generative Model Training","url":"https://liner.com/review/selfcorrecting-selfconsuming-loops-for-generative-model-training"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"ICLR Poster Self-Consuming Generative Models Go MAD","url":"https://iclr.cc/virtual/2024/poster/18592"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/html/2402.11778v2"},{"title":"Towards theoretical understandings of self-consuming generative models | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692639"},{"title":"Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/pdf/2402.11778"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"}]

Based on the search results, here's what I found about self-consuming generative models research from 2024:

## Key Research

In 2024, research theoretically showed that iteratively retraining a generative model on its own generated samples with human curation optimizes human preferences, as published at NeurIPS 2024.

## Main Challenge: Model Autophagy Disorder (MAD)

A p
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T16:05:21.081937+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang MMD AI text detection 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang MMD AI text detection 2024"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T16:05:21.082076+00:00_

Web search results for query: "Zhang MMD AI text detection 2024"

Links: [{"title":"[2402.16041] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://arxiv.org/abs/2402.16041"},{"title":"LLM-DetectAIve: a Tool for Fine-Grained Machine-Generated Text Detection","url":"https://aclanthology.org/2024.emnlp-demo.35.pdf"},{"title":"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection","url":"https://arxiv.org/html/2605.01647v1"},{"title":"Published as a conference paper at ICLR 2024 DETECTING MACHINE-GENERATED TEXTS","url":"https://openreview.net/pdf?id=3fEKavFsnv"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880"},{"title":"AI-generated Text Detection: A Multifaceted Approach to Binary and Multiclass Classification","url":"https://arxiv.org/html/2505.11550v1"},{"title":"Distinguishing Human From Machine: A Review of Advances and Challenges in AI-Generated Text Detection | International Journal of Interactive Multimedia and Artificial Intelligence","url":"https://revistas.unir.net/index.php/ijimai/article/view/234"},{"title":"A Practical Examination of AI-Generated Text Detectors for Large Language Models","url":"https://arxiv.org/html/2412.05139v4"},{"title":"LLM-DetectAIve: a Tool for Fine-Grained Machine-Generated Text Detection","url":"https://arxiv.org/html/2408.04284"}]

Based on the search results, here's what I found about Zhang MMD AI text detection research from 2024:

A paper titled "Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy" was published in February 2024 by Shuhai Zhang and colleagues.

The researchers proposed a novel multi-population aware optimization method for MMD called MMD-MP, which aims to avoid variance increases and improve the stability of measuring distributional discrepancy, and they developed two methods for paragraph-based and se
…[truncated 505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T16:05:21.082226+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Weng knowledge attribution LLMs 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Weng knowledge attribution LLMs 2025"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T16:05:21.082363+00:00_

Web search results for query: "Weng knowledge attribution LLMs 2025"

Links: [{"title":"The 2025 AI Engineering Reading List - Latent.Space","url":"https://www.latent.space/p/2025-papers"},{"title":"Yixuan Weng - Homepage","url":"https://wengsyx.github.io/"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/pdf/2602.22787"},{"title":"Towards Verifiable Generation: A Benchmark for Knowledge-aware Language   Model Attribution","url":"https://arxiv.org/pdf/2310.05634"},{"title":"A Survey of Large Language Models Attribution","url":"https://arxiv.org/pdf/2311.03731"},{"title":"Source-Aware Training Enables Knowledge Attribution in Language Models","url":"https://arxiv.org/pdf/2404.01019"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"}]

Based on the web search results, here's what I found about knowledge attribution in LLMs related to 2025:

## Recent Work on Knowledge Attribution in LLMs

There's emerging research on "contributive attribution," which distinguishes between contextual knowledge (from the prompt or retrieved evidence) and parametric knowledge (stored in the model's weights).

Recent work has explored source-aware training to enable LLMs to cite the pretraining source supporting their parametric knowledge. A significant portion of an LLM's knowledge is acquired during pretraining, therefore citing evidence for this parametric knowledge can greatly enhance LLM trustworthiness.

## Key Challenges Being Addressed

Although LLM hallucinations have become a central research focus, existing detection techniques often miss a more fundamental issue: users lack visibility into where a model's answers come from, and while methods evaluate correctness, they don't evaluate provenance, even though provenance is essential for determining whether users can trust an answer.

The search results also show that Lilian Weng has contributed to work on prompting and knowledge in l
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T16:05:21.082536+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2502.15208 \"Unveiling Attractor Cycles\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2502.15208 \"Unveiling Attractor Cycles\" authors"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T16:05:21.082714+00:00_

Web search results for query: "arxiv 2502.15208 "Unveiling Attractor Cycles" authors"

Links: [{"title":"[2502.15208v1] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208v1"},{"title":"[2502.15208] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/abs/2502.15208"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical","url":"https://arxiv.org/pdf/2502.15208"},{"title":"[Literature Review] Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://www.themoonlight.io/en/review/unveiling-attractor-cycles-in-large-language-models-a-dynamical-systems-view-of-successive-paraphrasing"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"dblp: Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing.","url":"https://dblp.org/rec/journals/corr/abs-2502-15208.html"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing | Request PDF","url":"https://www.researchgate.net/publication/394299645_Unveiling_Attractor_Cycles_in_Large_Language_Models_A_Dynamical_Systems_View_of_Successive_Paraphrasing"}]

The authors of arxiv 2502.15208 "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" are Zhilin Wang, Yafu Li, Jianhao Yan, Yu Cheng, and Yue Zhang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T16:05:21.082861+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On the Stability of Iterative Retraining\" ICLR 2024 authors Bertrand Bousquet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On the Stability of Iterative Retraining\" ICLR 2024 authors Bertrand Bousquet"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T16:05:21.083013+00:00_

Web search results for query: ""On the Stability of Iterative Retraining" ICLR 2024 authors Bertrand Bousquet"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=JORAfH2xFd"},{"title":"ON THE STABILITY OF ITERATIVE RETRAINING ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/339cab2a98edcba2d4ac42e5f8b64218-Paper-Conference.pdf"},{"title":"On the Stability of Iterative Retraining of Generative Models ...","url":"https://arxiv.org/pdf/2310.00429"},{"title":"Could we see the collapse of generative AI? | Inria","url":"https://www.inria.fr/en/collapse-ia-generatives"},{"title":"On the Stability of Iterative Retraining of Generative Models on their own Data | OpenReview","url":"https://openreview.net/forum?id=JORAfH2xFd"},{"title":"GitHub - QB3/gen_models_dont_go_mad: Code to reproduce the experiments of the ICLR 2024 (spotlight) paper \"On the Stability of Iterative Retraining of Generative Models on their Own Data\" https://arxiv.org/abs/2310.00429","url":"https://github.com/QB3/gen_models_dont_go_mad"},{"title":"dblp: On the Stability of Iterative Retraining of Generative Models on their own Data.","url":"https://dblp.org/rec/conf/iclr/BertrandBDJG24.html"},{"title":"[2310.00429] On the Stability of Iterative Retraining of Generative Models on their own Data","url":"https://arxiv.org/abs/2310.00429"},{"title":"Quentin BERTRAND - Research","url":"https://qb3.github.io/research.html"}]

I found the paper! Here are the search results:

The paper "On the Stability of Iterative Retraining of Generative Models on Their Own Data" was presented at ICLR 2024 by Quentin Bertrand, Joey Bose, Alexandre Duplessis, Marco Jiralerspong, and Gauthier Gidel.

Note: I should clarify that Bertrand is not listed as "Bertrand Bousquet" in the actual paper. The author is Quentin Bertrand.

**About the Paper:**

The paper develops a framework to rigorously study the impact of training generative models on mixed datasets—fro
…[truncated 762 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T16:05:21.083177+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Theoretical Understandings of Self-Consuming Generative Models\" authors 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Theoretical Understandings of Self-Consuming Generative Models\" authors 2024"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T16:05:21.083318+00:00_

Web search results for query: ""Towards Theoretical Understandings of Self-Consuming Generative Models" authors 2024"

Links: [{"title":"[2402.11778v2] Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/abs/2402.11778v2"},{"title":"[2402.11778] Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/abs/2402.11778"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/pdf/2402.11778"},{"title":"Towards theoretical understandings of self-consuming generative models | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692639"},{"title":"Towards Theoretical Understandings of Self-Consuming Generative Models","url":"https://arxiv.org/html/2402.11778v2"}]

Based on the search results, I found the paper you're looking for:

**Title:** "Towards Theoretical Understandings of Self-Consuming Generative Models"

**Authors:** Shi Fu, Sen Zhang, Yingjie Wang, Xinmei Tian, and Dacheng Tao

**Publication:** Proceedings of the 41st International Conference on Machine Learning (PMLR 235), 2024

**Overview:** The paper tackles the emerging challenge of training generative models within a self-consuming loop, wherein successive generations of models are recursively trained on mixtures of real and synthetic data from previous generations. They construct a theoretical framework to rigorously evaluate how this training procedure impacts the data distributions learned by future models, including parametric and non-parametric models.

The paper is available on arXiv (preprint ID: 2402.11778) and was presented at ICML 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T16:05:21.083451+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.04833 \"When AI Settles Down\" authors Ke Sun"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.04833 \"When AI Settles Down\" authors Ke Sun"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T16:05:21.083618+00:00_

Web search results for query: "arxiv 2601.04833 "When AI Settles Down" authors Ke Sun"

Links: [{"title":"[2601.04833] When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/abs/2601.04833"},{"title":"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/html/2601.04833"},{"title":"Ke Sun's articles on arXiv","url":"https://arxiv.org/a/sun_k_3.html"},{"title":"The accuracy-bias trade-offs in AI text detection tools and their impact on fairness in scholarly publication","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12453642/"},{"title":"The Silent Author in Urology: Quantifying Large Language Model Influence at the Corpus Level","url":"https://www.medrxiv.org/content/10.1101/2025.07.21.25331681.full.pdf"},{"title":"Prevalence of Artificial Intelligence-Generated Text in Neurosurgical Publications: Implications for Academic Integrity and Ethical Authorship","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11920854/"},{"title":"Paper Reconstruction Evaluation: Evaluating Presentation and Hallucination in AI-written Papers","url":"https://arxiv.org/pdf/2604.01128"},{"title":"AI becomes a masterbrain scientist","url":"https://www.biorxiv.org/content/10.1101/2023.04.19.537579.full.pdf"},{"title":"Correction: Eliminating the AI digital divide by building local capacity","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12752974/"}]

I found the paper you're looking for. Here are the details:

**Title:** When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection

**ArXiv ID:** 2601.04833

**Authors:** Ke Sun, Guangsheng Bao, Han Cui, Yue Zhang from School of Engineering, Westlake University, China

**Main Contribution:** The paper reveals Late-Stage Volatility Decay: AI-generated text exhibits rapidly stabilizing log probability fluctuations as generation progresses, while human writing maintains higher variability
…[truncated 658 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T16:05:21.083784+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shuhai Zhang \"Multi-Population Aware Optimization\" \"Maximum Mean Discrepancy\" machine-generated text detection venue published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shuhai Zhang \"Multi-Population Aware Optimization\" \"Maximum Mean Discrepancy\" machine-generated text detection venue published"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T16:05:21.083929+00:00_

Web search results for query: "Shuhai Zhang "Multi-Population Aware Optimization" "Maximum Mean Discrepancy" machine-generated text detection venue published"

Links: [{"title":"[2402.16041] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://arxiv.org/abs/2402.16041"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy - Hong Kong Baptist University","url":"https://scholars.hkbu.edu.hk/en/publications/detecting-machine-generated-texts-by-multi-population-aware-optim"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240216041Z/abstract"},{"title":"[2402.16041] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://ar5iv.labs.arxiv.org/html/2402.16041"},{"title":"[Quick Review] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://liner.com/review/detecting-machinegenerated-texts-by-multipopulation-aware-optimization-for-maximum-mean"},{"title":"GitHub - ZSHsh98/MMD-MP: This is the source code for Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy (ICLR2024).","url":"https://github.com/ZSHsh98/MMD-MP"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://arxiv.org/html/2402.16041v2"},{"title":"multi-population aware optimization for maximum mean ...","url":"https://openreview.net/pdf?id=3fEKavFsnv"}]

Based on the search results, I found comprehensive information about this paper:

The paper "Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy" by Shuhai Zhang and co-authors was published in the Proceedings of the Twelfth Inter
…[truncated 678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T16:05:21.084068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Weng \"knowledge attribution\" language model 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Weng \"knowledge attribution\" language model 2025 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T16:05:21.084201+00:00_

Web search results for query: "Weng "knowledge attribution" language model 2025 arxiv"

Links: [{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/html/2602.22787"},{"title":"[2506.00783] KG-TRACES: Enhancing Large Language Models with Knowledge Graph-constrained Trajectory Reasoning and Attribution Supervision","url":"https://arxiv.org/abs/2506.00783"},{"title":"From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery","url":"https://arxiv.org/html/2505.13259v3"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/pdf/2602.22787"},{"title":"[2310.05634] Towards Verifiable Generation: A Benchmark for Knowledge-aware Language Model Attribution","url":"https://arxiv.org/abs/2310.05634"},{"title":"Towards Verifiable Generation: A Benchmark for Knowledge-aware Language   Model Attribution","url":"https://arxiv.org/pdf/2310.05634"},{"title":"Revealing the Parametric Knowledge of Language Models: A Unified   Framework for Attribution Methods","url":"https://arxiv.org/pdf/2404.18655"}]

Based on the search results, I found a highly relevant paper matching your query:

**"Probing for Knowledge Attribution in Large Language Models"** - This paper addresses knowledge attribution by distinguishing between contextual knowledge (from the prompt or retrieved evidence) and parametric knowledge (stored in the model's weights).

The paper shifts focus from asking whether the output is true to asking whether the model relied on the source the user intended. Attribution signals can help users detect when a model defaults to conflicting parametric knowledge or when it overly relies on irrelevant context.

The paper was published on arXiv on February 26, 2026 (arXiv:2602.22787) and appears to be authored by researchers including those with the surname Weng, as indicated in your search query. This work is particularly valuable for retrieval-augmented generation systems, wh
…[truncated 172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T16:05:21.084344+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.22787 \"Probing for Knowledge Attribution\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.22787 \"Probing for Knowledge Attribution\" authors"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T16:05:21.084472+00:00_

Web search results for query: "arxiv 2602.22787 "Probing for Knowledge Attribution" authors"

Links: [{"title":"[2602.22787] Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/abs/2602.22787"},{"title":"Probing for Knowledge Attribution in Large Language Models","url":"https://arxiv.org/pdf/2602.22787"},{"title":"Cracking double-blind review: Authorship attribution with deep learning | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0287611"},{"title":"Cracking Double-Blind Review: Authorship Attribution with Deep Learning","url":"https://arxiv.org/pdf/2211.07467"},{"title":"Cracking double-blind review: Authorship attribution with deep learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10313031/"},{"title":"Cracking Double-Blind Review: Authorship Attribution with Deep Learning","url":"https://arxiv.org/html/2211.07467"}]

Based on the search results, the authors of arXiv paper 2602.22787 "Probing for Knowledge Attribution in Large Language Models" are Ivo Brink, Alexander Boer, and Dennis Ulmer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T16:05:21.084627+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yixuan Weng knowledge attribution 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yixuan Weng knowledge attribution 2025"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T16:05:21.084773+00:00_

Web search results for query: "Yixuan Weng knowledge attribution 2025"

Links: [{"title":"Yixuan Weng - Homepage","url":"https://wengsyx.github.io/"},{"title":"Yixuan Weng - ACL Anthology","url":"https://aclanthology.org/people/yixuan-weng/"},{"title":"(PDF) Abduct, Act, Predict: Scaffolding Causal Inference for Automated Failure Attribution in Multi-Agent Systems","url":"https://www.researchgate.net/publication/395473903_Abduct_Act_Predict_Scaffolding_Causal_Inference_for_Automated_Failure_Attribution_in_Multi-Agent_Systems"},{"title":"ResearStudio: A Human-intervenable Framework for Building Controllable Deep Research Agents - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-demos.69/"},{"title":"(PDF) DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively","url":"https://www.researchgate.net/publication/396048565_DeepScientist_Advancing_Frontier-Pushing_Scientific_Findings_Progressively"},{"title":"Yixuan Weng's research works | Chinese Academy of Sciences and other places","url":"https://www.researchgate.net/scientific-contributions/Yixuan-Weng-2199153327"},{"title":"Yixuan Weng","url":"https://www.catalyzex.com/author/Yixuan%20Weng"}]

Based on the search results, here's what I found regarding Yixuan Weng and knowledge-related work in 2025:

Yixuan Weng had two papers accepted to ICLR 2025: CycleResearcher and Personality Alignment.

Additionally, Yixuan Weng co-authored a paper titled "Does knowledge localization hold true? surprising differences between entity and relation perspectives in language models", which addresses knowledge attribution questions from entity and relation perspectives in language models.

Weng also co-authored "ResearStudio: A Human-intervenable Framework for Building Controllable Deep Research Agents" for the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations.

The search results show active research involving knowledge-related topics, though the specific focus on "k
…[truncated 207 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T16:05:21.084909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Weng knowledge attribution LLM source tracing provenance 2025 ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Weng knowledge attribution LLM source tracing provenance 2025 ACL EMNLP"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T16:05:21.085046+00:00_

Web search results for query: "Weng knowledge attribution LLM source tracing provenance 2025 ACL EMNLP"

Links: [{"title":"Textual Option Weighting for Token-Efficient LLM-Based ...","url":"https://aclanthology.org/2025.findings-emnlp.874.pdf"},{"title":"MotivGraph-SoIQ: Integrating Motivational Knowledge ...","url":"https://aclanthology.org/2025.findings-emnlp.158.pdf"},{"title":"When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution","url":"https://arxiv.org/pdf/2603.17445"},{"title":"DebugLM: Learning Traceable Training Data Provenance for LLMs","url":"https://arxiv.org/pdf/2603.17884"},{"title":"Source-Aware Training Enables Knowledge Attribution in Language Models","url":"https://arxiv.org/pdf/2404.01019"},{"title":"Attention Consistency for LLMs Explanation","url":"https://aclanthology.org/2025.findings-emnlp.91.pdf"},{"title":"A Training-free Method for LLM Text Attribution","url":"https://arxiv.org/pdf/2501.02406"},{"title":"Source Attribution for Large Language Model-Generated Data","url":"https://arxiv.org/pdf/2310.00646"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Tracing the Data Trail: A Survey of Data Provenance, Transparency and Traceability in LLMs","url":"https://arxiv.org/pdf/2601.14311"}]

Based on the search results, I found several relevant papers related to knowledge attribution, source tracing, and provenance in LLMs, though the specific "Weng" paper you're looking for didn't appear in these particular results. Here's what I found:

**Related Recent Work (2025):**

1. **DebugLM** - A framework that equips LLMs with built-in data provenance, enabling them to explicitly trace the origins of their behaviors to specific training data sources.

2. **Source-Aware Training Enables Knowledge Attribution** - Addresses the need for techniques to identify and trace the origins of information in LLMs' re
…[truncated 855 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T16:05:21.085190+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Self-Consuming Generative Models with Curated Data\" NeurIPS 2024 authors Li"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Self-Consuming Generative Models with Curated Data\" NeurIPS 2024 authors Li"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T16:05:21.085334+00:00_

Web search results for query: ""Self-Consuming Generative Models with Curated Data" NeurIPS 2024 authors Li"

Links: [{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences | OpenReview","url":"https://openreview.net/forum?id=cyv0LkIaoH"},{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/self-consuming-generative-models-curated-data-provably"},{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences","url":"https://arxiv.org/html/2407.09499v1"},{"title":"Self-Consuming Generative Models with Curated Data ...","url":"https://hal.science/hal-04711701/document"},{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/b9e88ae0308cf82d0b0f634ddbdf809a-Abstract-Conference.html"},{"title":"Artificial Intelligence Jul 2024","url":"https://web3.arxiv.org/list/cs.AI/2024-07?skip=1500&show=500"},{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-04711701"},{"title":"[2407.09499] Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences","url":"https://arxiv.org/abs/2407.09499"},{"title":"Self-Consuming Generative Models with Curated Data Provably Optimize   Human Preferences","url":"https://arxiv.org/pdf/2407.09499"}]

Based on the search results, here's what I found about this paper:

The paper "Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences" was authored by Damien Ferbach, Quentin Bertrand, Avishek Joey Bose, and Gauthier Gidel, and was presented at NeurIPS in December 2024 in Vancouver.

This was a NeurIPS 2024 spotlight paper that theore
…[truncated 994 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T16:05:21.085470+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li self-consuming generative models text language model collapse 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li self-consuming generative models text language model collapse 2024 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T16:05:21.085620+00:00_

Web search results for query: "Li self-consuming generative models text language model collapse 2024 arxiv"

Links: [{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"Theoretical Proof that Auto-regressive Language Models Collapse when Real-world Data is a Finite Set","url":"https://arxiv.org/html/2412.14872"},{"title":"Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop","url":"https://arxiv.org/html/2311.16822v2"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"A linguistic analysis of undesirable outcomes in the era of generative AI","url":"https://arxiv.org/html/2410.12341v1"},{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258v2/"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"Convergence Dynamics and Stabilization Strategies of Co-Evolving   Generative Models","url":"https://arxiv.org/pdf/2503.08117"}]

I've successfully performed the web search for your query about self-consuming generative models and language model collapse. Here are the key findings:

## Main Research Areas

Emerging theoretical analyses of self-consuming generative models (also known as iterative retraining) suggest model collapse or stability may occur depending on the proportion of generated data used in each retraining iteration.

One theoretical proof demonstrates that once a corpus begins to incorporate generated data and no new real-world data is added, language model collapse is inevitable after sufficient time, no matter how small the amount of data each LM generates.

## Key Papers from 2024

Several important papers are cited in the search results:

1. **Model Collapse Analysis**: Research has stud
…[truncated 887 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T16:05:21.085784+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo model collapse ICLR 2024 generative models retraining"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo model collapse ICLR 2024 generative models retraining"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T16:05:21.085923+00:00_

Web search results for query: "Guo model collapse ICLR 2024 generative models retraining"

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=JORAfH2xFd"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/339cab2a98edcba2d4ac42e5f8b64218-Paper-Conference.pdf"},{"title":"Could we see the collapse of generative AI? | Inria","url":"https://www.inria.fr/en/collapse-ia-generatives"},{"title":"Escaping Model Collapse via Synthetic Data Verification:","url":"https://arxiv.org/pdf/2510.16657"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Nepotistically Trained Generative-AI Models Collapse","url":"https://arxiv.org/pdf/2311.12202"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on   Recursively Generated Data'","url":"https://arxiv.org/pdf/2410.12954"},{"title":"BEYOND MODEL COLLAPSE: SCALING UP WITH SYN","url":"https://openreview.net/pdf?id=MQXrTMonT1"}]

Based on the search results, here's what I found about model collapse research related to ICLR 2024 and generative models retraining:

## Key Research on Model Collapse

At the 2024 edition of ICLR, Quentin Bertrand, Joey Bose, Alexandre Duplessis, Marco Jiralerspong and Gauthier Gidel presented a paper entitled "On the stability of iterative retraining of generative models on their own data".

## The Core Problem

Retraining a multivariate Gaussian only on its generated data leads to its collapse: its covariance matrix vanishes to 0 linearly as a function of the number of retraining iterations. More broadly, model collapse is a phenomenon whereby an AI's output becomes increasingly biased, homogeneous, poor and inaccurate as a result of it generating its own supply of training data.

## Key Fin
…[truncated 674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T16:05:21.086065+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Weng knowledge localization entity relation language models 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Weng knowledge localization entity relation language models 2025 paper"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T16:05:21.086200+00:00_

Web search results for query: "Weng knowledge localization entity relation language models 2025 paper"

Links: [{"title":"GitHub - weiyifan1023/RaKE: Code and Data for CIKM 2024 Paper \"Does Knowledge Localization Hold True? Surprising Differences Between Entity and Relation Perspectives in Language Models\"","url":"https://github.com/weiyifan1023/RaKE"},{"title":"Published as a conference paper at ICLR 2025 PRECISE LOCALIZATION","url":"https://openreview.net/pdf?id=5xP1HDvpXI"},{"title":"Does Knowledge Localization Hold True? Surprising Differences Between Entity and Relation Perspectives in Language Models | Proceedings of the 33rd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/abs/10.1145/3627673.3679900"},{"title":"Does Knowledge Localization Hold True? Surprising Differences Between Entity and Relation Perspectives in Language Models","url":"https://arxiv.org/html/2409.00617v1"},{"title":"Does Knowledge Localization Hold True? Surprising Differences","url":"https://arxiv.org/pdf/2409.00617"},{"title":"[2409.00617] Does Knowledge Localization Hold True? Surprising Differences Between Entity and Relation Perspectives in Language Models","url":"https://arxiv.org/abs/2409.00617"},{"title":"CHILL at SemEval-2025 Task 2: You Can't Just Throw Entities and Hope -- Make Your LLM to Get Them Right","url":"https://arxiv.org/pdf/2506.13070"},{"title":"Friends and Grandmothers in Silico: Localizing Entity Cells in Language Models","url":"https://arxiv.org/pdf/2604.01404"}]

Based on the search results, I found relevant information about a paper by Weng and colleagues on knowledge localization and entity-relation perspectives in language models:

The paper titled "Does Knowledge Localization Hold True? Surprising Differences Between Entity and Relation Perspectives in Language Models" was authored by Yifan Wei, Xiaoyan Yu, Yixuan Weng, Huanhuan Ma, Yuanzhe Zhang, Jun Zhao, and Kang Liu.

The study investigates the differen
…[truncated 818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T16:05:21.086336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shuhai Zhang MMD-MP ICLR 2024 full author list bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shuhai Zhang MMD-MP ICLR 2024 full author list bibtex"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T16:05:21.086497+00:00_

Web search results for query: "Shuhai Zhang MMD-MP ICLR 2024 full author list bibtex"

Links: [{"title":"Hidden Division of Labor in Scientific Teams Revealed Through 1.6   Million LaTeX Files","url":"https://arxiv.org/pdf/2502.07263"},{"title":"2024 - Call For Papers","url":"https://iclr.cc/Conferences/2024/CallForPapers"},{"title":"ICLR 2024 Author Guide","url":"https://iclr.cc/Conferences/2024/AuthorGuide"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"},{"title":"ICLR 2024 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2024-paper-list/"},{"title":"Development of meta-prompts for Large Language Models to screen titles and abstracts for diagnostic test accuracy reviews","url":"https://www.medrxiv.org/content/10.1101/2023.10.31.23297818.full.pdf"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"Identification of bioactive constituents for colitis from traditional Chinese medicine prescription via deep neural network","url":"https://www.biorxiv.org/content/10.1101/2023.05.31.542690.full.pdf"},{"title":"dblp: ICLR","url":"https://dblp.org/db/conf/iclr/index.html"},{"title":"Remembering Unequally: Global and Disciplinary Bias in LLM Reconstruction of Scholarly Coauthor Lists","url":"https://arxiv.org/pdf/2511.00476"}]

The search results don't contain specific information about the paper "MMD-MP" by Shuhai Zhang at ICLR 2024. Let me try a more targeted search:

Links: [{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5b288823575bb29654b0953a251e933b-Paper-Conference.pdf"},{"title":"ICLR 2024 Author Guide","url":"https://iclr.cc/Conferences/2024/AuthorGuide"},{"title":"Thanks to reviewers list 2024","url":"https://www.ncbi.nlm.ni
…[truncated 1585 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T16:05:21.086666+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Weng knowledge tracing attribution LLM hallucination provenance 2025 NAACL ACL AAAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Weng knowledge tracing attribution LLM hallucination provenance 2025 NAACL ACL AAAI"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T16:05:21.086822+00:00_

Web search results for query: "Weng knowledge tracing attribution LLM hallucination provenance 2025 NAACL ACL AAAI"

Links: [{"title":"Frontiers | Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1622292/full"},{"title":"Survey and analysis of hallucinations in large language models: attribution to prompting strategies or model behavior","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12518350/"},{"title":"Why and How LLMs Hallucinate: Connecting the Dots with Subsequence   Associations","url":"https://arxiv.org/pdf/2504.12691"},{"title":"Extrinsic Hallucinations in LLMs | Lil'Log","url":"https://lilianweng.github.io/posts/2024-07-07-hallucination/"},{"title":"Distributional Semantics Tracing: A Framework for Explaining Hallucinations in Large Language Models","url":"https://arxiv.org/pdf/2510.06107"},{"title":"Where Did It Go Wrong? Attributing Undesirable LLM Behaviors via Representation Gradient Tracing","url":"https://arxiv.org/pdf/2510.02334"},{"title":"Hallucination Rates in 2025 — Accuracy, Refusal, and Liability | by Markus Brinsa | Medium","url":"https://medium.com/@markus_brinsa/hallucination-rates-in-2025-accuracy-refusal-and-liability-aa0032019ca1"},{"title":"HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models","url":"https://arxiv.org/pdf/2603.05828"},{"title":"Towards Verifiable Generation: A Benchmark for Knowledge-aware Language   Model Attribution","url":"https://arxiv.org/pdf/2310.05634"}]

Based on the search results, I found several recent papers on attribution, tracing, and hallucination in LLMs from 2025 and 2024. However, I did not find a specific paper by an author named "Weng" at NAACL, ACL, or AAAI conferences matching your exact query.

The search did return relevant papers on related topics:

1. A comprehensive survey presenting
…[truncated 1267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T16:05:21.087004+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2025.acl-long.624 \"Unveiling Attractor Cycles\" bibtex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2025.acl-long.624 \"Unveiling Attractor Cycles\" bibtex"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T16:05:21.087151+00:00_

Web search results for query: "aclanthology.org 2025.acl-long.624 "Unveiling Attractor Cycles" bibtex"

Links: [{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.624/"},{"title":"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing","url":"https://arxiv.org/pdf/2502.15208"},{"title":"Aclanthology","url":"https://aclanthology.org/2025.acl-long.624.pdf"},{"title":"Unveiling the Potential of BERT-family: A New Recipe for Building Scalable, General and Competitive Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1441/"},{"title":"Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.acl-long/"}]

I found the paper for you! The BibTeX entry for "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing" by Wang, Li, Yan, Cheng, and Zhang is available at aclanthology.org/2025.acl-long.624.

Here's the BibTeX information from the search result:

```bibtex
@inproceedings{wang-etal-2025-unveiling,
  title = "Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing",
  author = "Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue",
  editor = "Che, Wanxiang and Nabende, Joyce and Shutova, Ekaterina and Pilehvar, Mohammad Taher",
  booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
  month = jul,
  year = "2025",
  address = "Vienna, Austria",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2025.acl-long.624/",
  doi = "10.18653/v1/2025.acl-long.624",
  pages = "12740--12755"
}
```


REMINDER: You MUST include the s
…[truncated 68 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T16:05:21.087305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net \"Detecting Machine-Generated Texts\" \"Multi-Population\" 3fEKavFsnv authors Zhang Song Yang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net \"Detecting Machine-Generated Texts\" \"Multi-Population\" 3fEKavFsnv authors Zhang Song Yang"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T16:05:21.087440+00:00_

Web search results for query: "openreview.net "Detecting Machine-Generated Texts" "Multi-Population" 3fEKavFsnv authors Zhang Song Yang"

Links: [{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy - Hong Kong Baptist University","url":"https://scholars.hkbu.edu.hk/en/publications/detecting-machine-generated-texts-by-multi-population-aware-optim"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy | OpenReview","url":"https://openreview.net/forum?id=3fEKavFsnv"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://arxiv.org/html/2402.16041v1"},{"title":"Detecting Machine-Generated Texts by Multi-Population Aware Optimization   for Maximum Mean Discrepancy","url":"https://arxiv.org/pdf/2402.16041"},{"title":"Detecting Machine-Generated Texts: Not Just \"AI vs ...","url":"https://arxiv.org/pdf/2406.18259"},{"title":"[2402.16041] Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy","url":"https://arxiv.org/abs/2402.16041"}]

I found the research paper you're looking for! Here are the results:

The paper "Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy" was authored by Zhang, S., Song, Y., Yang, J., Li, Y., Han, B., and Tan, M. in 2024 and was published in Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024).

The paper proposes a novel multi-population aware optimization method for maximum mean discrepancy (MMD-MP) to detect machine-generated texts. The research addresses the challenge that machine-generated texts (MGTs) may carry critical risks such as plagiarism issues and hallucination information, making it urgent to detect MGTs in many situations.

Extensive experiments on various LLMs, such as GPT2 and ChatGPT, show superior detec
…[truncated 259 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T16:05:21.087597+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.04833 Sun Bao Cui Zhang \"When AI Settles Down\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.04833 Sun Bao Cui Zhang \"When AI Settles Down\" full author list"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T16:05:21.087731+00:00_

Web search results for query: "arxiv 2601.04833 Sun Bao Cui Zhang "When AI Settles Down" full author list"

Links: [{"title":"[2601.04833] When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/abs/2601.04833"},{"title":"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection","url":"https://arxiv.org/html/2601.04833"},{"title":"Prevalence of Artificial Intelligence-Generated Text in Neurosurgical Publications: Implications for Academic Integrity and Ethical Authorship","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11920854/"},{"title":"An ensemble approach for research article classification: a case study in artificial intelligence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11784741/"},{"title":"Stop DDoS Attacking the Research Community with AI-Generated Survey Papers","url":"https://arxiv.org/pdf/2510.09686"}]

Based on the search results, the full author list for arxiv paper 2601.04833 "When AI Settles Down" is: Ke Sun, Guangsheng Bao, Han Cui, and Yue Zhang. They are from the School of Engineering, Westlake University, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T16:05:21.087858+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Guo\" iterative generation model collapse self-consuming 2024 language model arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Guo\" iterative generation model collapse self-consuming 2024 language model arxiv"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T16:05:21.088004+00:00_

Web search results for query: ""Guo" iterative generation model collapse self-consuming 2024 language model arxiv"

Links: [{"title":"LLM as a Broken Telephone: Iterative Generation Distorts Information","url":"https://arxiv.org/html/2502.20258"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse","url":"https://arxiv.org/html/2404.05090v1"},{"title":"Model Collapse in the Self-Consuming Chain of Diffusion Finetuning: A Novel Perspective from Quantitative Trait Modeling","url":"https://arxiv.org/html/2407.17493v2"},{"title":"Characterizing Model Collapse in Large Language Models Using Semantic Networks and Next-Token Probability","url":"https://arxiv.org/html/2410.12341v2"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"}]

Based on the search results, I found relevant research on iterative generation, model collapse, and self-consuming generative models. Here are the key findings:

## Guo et al. Research on Language Models and Synthetic Text

Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, and Chloé Clavel published "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text" in April 2024. Their work demonstrated that iterative training on synthetic text does not preserve the nuanced richness of human language, particularly in creative tasks.

## Model
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T16:05:21.088152+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yanzhu Guo \"Curious Decline of Linguistic Diversity\" training language models synthetic text venue published 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yanzhu Guo \"Curious Decline of Linguistic Diversity\" training language models synthetic text venue published 2024"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T16:05:21.088302+00:00_

Web search results for query: "Yanzhu Guo "Curious Decline of Linguistic Diversity" training language models synthetic text venue published 2024"

Links: [{"title":"Paper page - The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://huggingface.co/papers/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.228/"},{"title":"[2311.09807] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/abs/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/curious-decline-linguistic-diversity-training-language-models"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on   Synthetic Text","url":"https://arxiv.org/pdf/2311.09807"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Archive ouverte HAL","url":"https://hal.science/hal-04593399"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text - Laboratoire d'informatique de l'X (LIX)","url":"https://hal.inrae.fr/X-LIX/hal-04593399v1"},{"title":"GitHub - YanzhuGuo/linguistic-diversity","url":"https://github.com/YanzhuGuo/linguistic-diversity"},{"title":"[PDF] The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Curious-Decline-of-Linguistic-Diversity:-Models-Guo-Shang/7d5ea474aa1cf732bb1d00faa07a5bb2c9119cfd"},{"title":"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text","url":"https://arxiv.org/html/2311.09807v2"}]

Based on the search results, here's what I found about the paper:

**Title:** "The Curious 
…[truncated 786 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_w11_20260520T155942",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 55 · 2026-05-20T16:05:21.088526+00:00_

## 验证结果

### 1. Wang et al. (ACL 2025) — attractor cycles in recursive generation
**✅ 真实存在**

"Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing"

```bibtex
@inproceedings{wang-etal-2025-unveiling,
  title     = {Unveiling Attractor Cycles in Large Language Models: A Dynamical Systems View of Successive Paraphrasing},
  author    = {Wang, Zhilin and Li, Yafu and Yan, Jianhao and Cheng, Yu and Zhang, Yue},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  month     = jul,
  year      = {2025},
  address   = {Vienna, Austria},
  publisher = {Association for Computational Linguistics},
  url       = {https://aclanthology.org/2025.acl-long.624/},
  pages     = {12740--12755}
}
```

---

### 2. Sun et al. (2026) — late-stage stability in iterative text generation
**✅ 真实存在**

"When AI Settles Down: Late-Stage Stability as a Signature of AI-Generated Text Detection"

```bibtex
@article{sun2026settles,
  title   = {When {AI} Settles Down: Late-Stage Stability as a Signature of {AI}-Generated Text Detection},
  author  = {Sun, Ke and Bao, Guangsheng and Cui, Han and Zhang, Yue},
  journal = {arXiv preprint arXiv:2601.04833},
  year    = {2026},
  url     = {https://arxiv.org/abs/2601.04833}
}
```

注意：该论文的焦点是用 late-stage volatility decay 做**检测**，而非研究 iterative generation 本身的 stability。审稿人描述的 framing 略有偏差但论文确实存在。

---

### 3. Guo et al. (ICLR 2024) — iterative retraining stability / model collapse
**⚠️ 近似匹配（作者+会议张冠李戴）**

ICLR 2024 上关于 iterative retraining stability 的论文是 **Bertrand et al.**，不是 Guo：

> Quentin Bertrand, Avishek Joey Bose, Alexandre Duplessis, Marco Jiralerspong, Gauthier Gidel. "On the Stability of Iterative Retraining of Generative Models on their Own Data." ICLR 2024 (Spotlight).

确实存在一篇 **Guo et al.** 关于 iterative training 导致 linguistic diversity 下降的论文，但发表在 **Findings of NAACL 2024**，不是 ICLR：

> Yanzhu Guo, Guokan Shang, Michalis Vazirgiannis, Chloé Clavel. "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text." Findings of NAACL 2024.

**结论：审稿人将两篇论文的作者和会议混在一起了。**

---

### 4. Li et al. (2024) — self-consuming generative models
**❌ 不存在（审稿人幻觉）**

2024 年 self-consuming generative models 方向的主要论文：
- Alemohammad et al. "Self-Consuming Generative Models Go MAD" (ICLR 2024)
- Bertrand et al. "Self-Consuming Generative Models with Curated Data..." (NeurIPS 2024)
- Gillman et al. "Self-Correcting Self-Consuming Loops" (ICML 2024)
- Fu et al. "Towards Theoretical Understandings of Self-Consuming Generative Models" (ICML 2024)

**没有任何一篇以 "Li" 为第一作者。** 搜索了 Google Scholar、Semantic Scholar、arXiv，包括不同关键词组合，均未找到匹配论文。

---

### 5. Zhang et al. (2024) — MMD-based AI text detection
**✅ 真实存在**

"Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy"

```bibtex
@inproceedings{zhang2024detecting,
  title     = {Detecting Machine-Generated Texts by Multi-Population Aware Optimization for Maximum Mean Discrepancy},
  author    = {Zhang, Shuhai and Song, Yiliao and Yang, Jiahao and Li, Yuanqing and Han, Bo and Tan, Mingkui},
  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
  year      = {2024},
  url       = {https://openreview.net/forum?id=3fEKavFsnv}
}
```

---

### 6. Weng et al. (2025) — knowledge attribution in LLMs
**❌ 不存在（审稿人幻觉）**

搜索范围：Google Scholar、arXiv、ACL Anthology、NAACL/ACL/EMNLP/AAAI 2025 accepted papers。Yixuan Weng 在 CIKM 2024 有一篇 knowledge localization 相关论文（"Does Knowledge Localization Hold True?"），但主题是 entity vs relation knowledge，不是 knowledge attribution，且年份不符。2025 年 knowledge attribution 相关论文的第一作者均非 Weng。

---

### 汇总

| # | 引用 | 状态 | 说明 |
|---|------|------|------|
| 1 | Wang et al. (ACL 2025) | ✅ 真实 | attractor cycles，完全匹配 |
| 2 | Sun et al. (2026) | ✅ 真实 | late-stage stability，arXiv preprint |
| 3 | Guo et al. (ICLR 2024) | ⚠️ 张冠李戴 | ICLR 2024 是 Bertrand et al.；Guo et al. 在 NAACL 2024 |
| 4 | Li et al. (2024) | ❌ 幻觉 | 无此论文 |
| 5 | Zhang et al. (2024) | ✅ 真实 | MMD-MP，ICLR 2024 |
| 6 | Weng et al. (2025) | ❌ 幻觉 | 无此论文 |

Sources:
- [Wang et al. ACL 2025](https://aclanthology.org/2025.acl-long.624/)
- [Sun et al. 2026](https://arxiv.org/abs/2601.04833)
- [Bertrand et al. ICLR 2024](https://openreview.net/forum?id=JORAfH2xFd)
- [Guo et al. NAACL 2024](https://aclanthology.org/2024.findings-naacl.228/)
- [Zhang et al. ICLR 2024](https://openreview.net/forum?id=3fEKavFsnv)
- [Yixuan Weng ACL Anthology](https://aclanthology.org/people/yixuan-weng/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_citation_verification_w11_20260520T155942"
}
```

</details>

---
