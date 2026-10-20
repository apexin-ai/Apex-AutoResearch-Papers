# paper research

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 103
- **Recorded user turns:** 0
- **Tool calls:** 51
- **Original source:** `logs/chats/worker_paper_research_20260517T201057.jsonl`
- **Structured JSON:** [`648177553b25962f4c97.json`](../../sessions/64/648177553b25962f4c97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

103 recorded events

### Tool call

_source line 1 · 2026-05-17T20:18:22.502081+00:00_

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
  "session": "worker_paper_research_20260517T201057",
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

_source line 2 · 2026-05-17T20:18:22.502417+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T20:18:22.502576+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/ 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib 2>/dev/null || echo \"no bib file yet\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/ 2>/dev/null; echo \"---\"; cat /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib 2>/dev/null || echo \"no bib file yet\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T20:18:22.502786+00:00_

acl.sty
acl_natbib.bst
main.aux
main.log
main.out
main.pdf
main.tex
references.bib
sections
---
% References for: Spectral Early Warning Signals for Model Collapse
% All entries must be verified before final submission.
% Do not add unverified citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T20:18:22.502954+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shumailov et al 2024 Nature \"AI models collapse when trained on recursively generated data\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shumailov et al 2024 Nature \"AI models collapse when trained on recursively generated data\""
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-17T20:18:22.503082+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob 2024 \"model collapse demystified\" OR \"tale of tails\" theoretical analysis"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob 2024 \"model collapse demystified\" OR \"tale of tails\" theoretical analysis"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T20:18:22.503204+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alemohammad 2024 \"self-consuming generative models go MAD\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alemohammad 2024 \"self-consuming generative models go MAD\""
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-17T20:18:22.503322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser 2024 SIGMA spectral analysis model collapse OPT-125M"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser 2024 SIGMA spectral analysis model collapse OPT-125M"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T20:18:22.503438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gudibande 2024 \"false promise of imitating proprietary LLMs\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gudibande 2024 \"false promise of imitating proprietary LLMs\""
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T20:18:22.503592+00:00_

Web search results for query: "Shumailov et al 2024 Nature "AI models collapse when trained on recursively generated data""

Links: [{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"A Note on Shumailov et al. (2024): ‘AI Models Collapse When Trained on Recursively Generated Data’","url":"https://arxiv.org/html/2410.12954v2"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"[PDF] AI models collapse when trained on recursively generated data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AI-models-collapse-when-trained-on-recursively-data-Shumailov-Shumaylov/603d3f90fc40f79ff51258f0295de3ec5107f73e"},{"title":"[2410.12954] A Note on Shumailov et al. (2024): `AI Models Collapse When Trained on Recursively Generated Data'","url":"https://arxiv.org/abs/2410.12954"},{"title":"Author Correction: AI models collapse when trained on recursively generated data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11981929/"},{"title":"AI models collapse when trained on recursively generated data","url":"https://www.pure.ed.ac.uk/ws/portalfiles/portal/460496122/ShumailovEtalNature2024AIModelsCollapseWhen.pdf"},{"title":"A note on “AI models collapse when trained on recursively generated data” | by Ali Borji | Medium","url":"https://medium.com/@aliborji/a-note-on-ai-models-collapse-when-trained-on-recursively-generated-data-5bee1de1ab87"},{"title":"A Note on Shumailov et al. (2024): 'AI Models Collapse ...","url":"https://arxiv.org/pdf/2410.12954"},{"title":"Using AI to train AI: Model collapse could be coming for LLMs, say researchers","url":"https://techxplore.com/news/2024-07-ai-collapse-llms.html"}]

I've successfully found the paper you're looking for. Here's what I found:

## Publication Details
The paper "AI models collapse when trained on recursively generate
…[truncated 1119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T20:18:22.503875+00:00_

Web search results for query: "Dohmatob 2024 "model collapse demystified" OR "tale of tails" theoretical analysis"

Links: [{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://proceedings.mlr.press/v235/dohmatob24b.html"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/html/2402.07043v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Model Collapse Demystified: The Case of Regression Elvis Dohmatob§ ∗","url":"https://par.nsf.gov/servlets/purl/10649436"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tale-tails-model-collapse-as-change-scaling"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"[Quick Review] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://liner.com/review/tale-tails-model-collapse-as-change-scaling-laws"}]

Based on the search results, I found relevant information about Dohmatob's 2024 theoretical work on model collapse:

## Summary of Findings

Dohmatob and colleagues developed a theoretical framework of model collapse through the lens of scaling laws. They published two key papers in 2024:

1.
…[truncated 1296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T20:18:22.504053+00:00_

Web search results for query: "Alemohammad 2024 "self-consuming generative models go MAD""

Links: [{"title":"[2307.01850] Self-Consuming Generative Models Go MAD","url":"https://arxiv.org/abs/2307.01850"},{"title":"[PDF] Self-Consuming Generative Models Go MAD | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consuming-Generative-Models-Go-MAD-Alemohammad-Casco-Rodriguez/ad022cd5da75637ac3e0a8f8cc4f0d394ba5ff7a"},{"title":"Self-Consuming Generative Models Go MAD | OpenReview","url":"https://openreview.net/forum?id=ShjMHfmPs0"},{"title":"(PDF) Self-Consuming Generative Models Go MAD","url":"https://www.researchgate.net/publication/372136378_Self-Consuming_Generative_Models_Go_MAD"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/ebc042e767de551803ccfcc45e2454f5-Paper-Conference.pdf"},{"title":"Self-Consuming Generative Models Go MAD | Montreal AI Ethics Institute","url":"https://montrealethics.ai/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming AI Resources","url":"https://dsp.rice.edu/ai-loops/"},{"title":"SELF-CONSUMING GENERATIVE MODELS GO MAD - Houston Methodist Scholars","url":"https://scholars.houstonmethodist.org/en/publications/self-consuming-generative-models-go-mad/"},{"title":"Self-Consuming Generative Models Go MAD | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10570494"},{"title":"Ethics and Psychology: Self-Consuming Generative Models GO MAD","url":"https://www.ethicalpsychology.com/2024/09/self-consuming-generative-models-go-mad.html"}]

The search results show that the paper "Self-Consuming Generative Models Go MAD" was authored by Sina Alemohammad, Josue Casco-Rodriguez, Lorenzo Luzi, Ahmed Imtiaz Humayun, Hossein Babaei, Daniel LeJeune, Ali Siahkoohi, and Richard G. Baraniuk.

The paper addresses how advances in generative AI algorithms have led to the temptation to use AI-synthesized data to train next-generation models, and 
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T20:18:22.504232+00:00_

Web search results for query: "Gudibande 2024 "false promise of imitating proprietary LLMs""

Links: [{"title":"[2305.15717] The False Promise of Imitating Proprietary LLMs","url":"https://arxiv.org/abs/2305.15717"},{"title":"THE FALSE PROMISE OF IMITATING PROPRIETARY ...","url":"https://openreview.net/pdf?id=Kz3yckpCN5"},{"title":"The False Promise of Imitating Proprietary LLMs Arnav Gudibande∗ UC Berkeley","url":"https://arxiv.org/pdf/2305.15717"},{"title":"[PDF] The False Promise of Imitating Proprietary LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-False-Promise-of-Imitating-Proprietary-LLMs-Gudibande-Wallace/5d44f16a36ba7ae6b3d9d7c98bbc1b877e598f35"},{"title":"Paper page - The False Promise of Imitating Proprietary LLMs","url":"https://huggingface.co/papers/2305.15717"},{"title":"The False Promise of Imitating Proprietary LLMs","url":"https://www.researchgate.net/publication/371041153_The_False_Promise_of_Imitating_Proprietary_LLMs"},{"title":"dblp: Arnav Gudibande","url":"https://dblp.org/pid/348/5805.html"},{"title":"[2305.15717v1] The False Promise of Imitating Proprietary LLMs","url":"https://arxiv.org/abs/2305.15717v1"},{"title":"“The False Promise of Imitating Proprietary LLMs” — A Provectus Perspective","url":"https://www.linkedin.com/pulse/false-promise-imitating-proprietary-llms-provectus-perspective"},{"title":"The False Promise of Imitating Proprietary LLMs. - DBLP","url":"https://dblp.dagstuhl.de/rec/journals/corr/abs-2305-15717.html"}]

Based on the search results, I found the paper you're looking for:

"The False Promise of Imitating Proprietary Language Models" was published as a conference paper at ICLR 2024 by Arnav Gudibande, Eric Wallace, Charlie Snell, and colleagues from UC Berkeley.

The paper examines an emerging method to cheaply improve a weaker language model by finetuning it on outputs from a stronger model, such as proprietary systems like ChatGPT (e.g., Alpaca, Self-Instruct, and others). 

Initially, the
…[truncated 744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T20:18:22.504401+00:00_

Web search results for query: "Gerstgrasser 2024 SIGMA spectral analysis model collapse OPT-125M"

Links: [{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385v2"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385v2"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Collapse or Thrive?Perils and Promises of Synthetic Data ...","url":"https://arxiv.org/pdf/2410.16713"},{"title":"Addressing Concerns of Model Collapse from Synthetic Data in AI","url":"https://www.gretel.ai/blog/addressing-concerns-of-model-collapse-from-synthetic-data-in-ai"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"},{"title":"A Probabilistic Perspective on Model Collapse","url":"https://arxiv.org/html/2505.13947"}]

I found relevant results about your search query. Here's what I found:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix. By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the 
…[truncated 1108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T20:18:22.504586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "model collapse recursive synthetic training 2024 2025 curse of recursion language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "model collapse recursive synthetic training 2024 2025 curse of recursion language models"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-17T20:18:22.504781+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "spectral analysis model collapse singular values 2024 2025 effective rank neural network representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "spectral analysis model collapse singular values 2024 2025 effective rank neural network representations"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T20:18:22.504909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DoReMi data mixing optimization language model training Xie 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DoReMi data mixing optimization language model training Xie 2024"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-17T20:18:22.505029+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "adaptive data mixing language model training 2024 2025 data proportions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "adaptive data mixing language model training 2024 2025 data proportions"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T20:18:22.505148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "early warning signals neural network training spectral critical transitions 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "early warning signals neural network training spectral critical transitions 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T20:18:22.505291+00:00_

Web search results for query: "spectral analysis model collapse singular values 2024 2025 effective rank neural network representations"

Links: [{"title":"[2410.07799] Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/abs/2410.07799"},{"title":"ICML Poster Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://icml.cc/virtual/2025/poster/43837"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers | OpenReview","url":"https://openreview.net/forum?id=sRKtbGsebH"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/html/2410.07799v2"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers | OpenReview","url":"https://openreview.net/forum?id=X6xzYP2cMk"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mind-gap-spectral-analysis-rank-collapse-signal"},{"title":"(PDF) Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers","url":"https://www.researchgate.net/publication/384811192_Mind_the_Gap_a_Spectral_Analysis_of_Rank_Collapse_and_Signal_Propagation_in_Transformers"},{"title":"Preprint. Under Review. Spectral Collapse Drives Loss of Plasticity in Deep","url":"https://arxiv.org/pdf/2509.22335"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers - Paper Detail","url":"https://deeplearn.org/arxiv/572034/mind-the-gap:-a-spectral-analysis-of-rank-collapse-and-signal-propagation-in-attention-layers"},{"title":"Approaching Deep Learning through the Spectral Dynamics of Weights","url":"https://ttic.edu/ripl/assets/publications/yunis24.pdf"}]

I've completed the web search 
…[truncated 1678 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-17T20:18:22.505472+00:00_

Web search results for query: "DoReMi data mixing optimization language model training Xie 2024"

Links: [{"title":"[2305.10429] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/abs/2305.10429"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/dcba6be91359358c2355cd920da3fcbd-Paper-Conference.pdf"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=lXuByUeHhd"},{"title":"[PDF] DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DoReMi:-Optimizing-Data-Mixtures-Speeds-Up-Language-Xie-Pham/9b4f7c97c0b83a80c32bc0b93595cbcfb4ecb16d"},{"title":"GitHub - sangmichaelxie/doremi: Pytorch implementation of DoReMi, a method for optimizing the data mixture weights in language modeling datasets · GitHub","url":"https://github.com/sangmichaelxie/doremi"},{"title":"DoReMi: Optimizing Data Mixtures for LM Pretraining","url":"https://hunterheidenreich.com/notes/natural-language-processing/language-models/doremi-data-mixture-optimization/"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining | Request PDF","url":"https://www.researchgate.net/publication/401463528_DoReMi_Optimizing_Data_Mixtures_Speeds_Up_Language_Model_Pretraining"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language ...","url":"https://crfm.stanford.edu/2023/09/14/doremi.html"},{"title":"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining","url":"https://arxiv.org/pdf/2305.10429"},{"title":"Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models","url":"https://arxiv.org/html/2508.11953v1"}]

Based on the search results, I can provide you with comprehensive information about DoReMi:

## DoReMi: Data Mixing Optimization for Language Mode
…[truncated 1415 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T20:18:22.505686+00:00_

Web search results for query: "early warning signals neural network training spectral critical transitions 2024 2025"

Links: [{"title":"Predicting critical transitions with machine learning trained on surrogates of historical data | Communications Physics","url":"https://www.nature.com/articles/s42005-025-02172-4"},{"title":"Identifying early-warning signals of critical transitions with strong noise by dynamical network markers | Scientific Reports","url":"https://www.nature.com/articles/srep17501"},{"title":"Universal early warning signals of phase transitions in climate systems | Journal of The Royal Society Interface | The Royal Society","url":"https://royalsocietypublishing.org/rsif/article/20/201/20220562/90332/Universal-early-warning-signals-of-phase"},{"title":"Early-warning industrial fault detection based on physics-guided residual learning and calibrated CRNNs | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-48227-6"},{"title":"Machine learning methods trained on simple models can predict critical transitions in complex natural systems - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/35223058/"},{"title":"Early warning signals of complex critical transitions in deterministic dynamics | Nonlinear Dynamics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11071-024-10023-0"},{"title":"Learning from the past: predicting critical transitions with machine learning trained on surrogates of historical data","url":"https://arxiv.org/html/2410.09707v1"},{"title":"Training LSTM-neural networks on early warning signals of declining cooperation in simulated repeated public good games - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/32509538/"},{"title":"Efficacy of early warning signals and spectral periodicity for predicting transitions in bipolar patients: An actigraphy study - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/34099627/"},{"title":"Unveiling critical transition in a transport network model: stochasticity 
…[truncated 2086 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T20:18:22.505894+00:00_

Web search results for query: "adaptive data mixing language model training 2024 2025 data proportions"

Links: [{"title":"DATA MIXING LAWS: OPTIMIZING DATA MIXTURES BY ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025 AIOLI:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/71cc3acb2578bdd1e52bf9f85bbb1af0-Paper-Conference.pdf"},{"title":"Optimizing Pre-Training Data Mixtures with ...","url":"https://aclanthology.org/2025.acl-long.1564.pdf"},{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"Rethinking Multilingual Continual Pretraining: Data Mixing for Adapting LLMs Across Languages and Resources","url":"https://arxiv.org/html/2504.04152v2"},{"title":"Mixtera: A Data Plane for Foundation Model Training","url":"https://arxiv.org/html/2502.19790v2"},{"title":"SampleMix: A Sample-wise Pre-training Data Mixing Strategey by Coordinating Data Quality and Diversity","url":"https://arxiv.org/html/2503.01506v1"},{"title":"OpenMOSS Data Mixing Laws: Optimizing Data Mixtures by Predicting","url":"https://arxiv.org/pdf/2403.16952"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance | OpenReview","url":"https://openreview.net/forum?id=jjCB27TMK3"},{"title":"Rethinking Data Mixture for Large Language Models: A Comprehensive Survey and New Perspectives","url":"https://arxiv.org/html/2505.21598v1"}]

Based on the search results, here's an overview of recent research on adaptive data mixing for language model training in 2024-2025:

## Key Research Areas

**Data Mixing Laws Framework**

Recent work studies optimizing the mixture proportions of pretraining data for large language models by establishing a quantitative framework that predicts loss given any mixture proportion. Researchers
…[truncated 1538 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T20:18:22.506083+00:00_

Web search results for query: "model collapse recursive synthetic training 2024 2025 curse of recursion language models"

Links: [{"title":"The AI Model Collapse Risk is Not Solved in 2025","url":"https://www.winssolutions.org/ai-model-collapse-2025-recursive-training/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | OpenReview","url":"https://openreview.net/forum?id=5B2K4LRgmz"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"AI model collapse: The synthetic data trap and how to avoid it","url":"https://insights.manageengine.com/artificial-intelligence/ai-model-collapse-synthetic-data-trap/"},{"title":"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training","url":"https://arxiv.org/html/2509.04796v1"},{"title":"AI models collapse when trained on recursively generated data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/39048682/"},{"title":"AI-training-on-synthetic-data-th
…[truncated 2234 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T20:18:22.506273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gerstgrasser 2024 \"Is Model Collapse Inevitable\" breaking curse recursion accumulating real synthetic data arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gerstgrasser 2024 \"Is Model Collapse Inevitable\" breaking curse recursion accumulating real synthetic data arXiv"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T20:18:22.506402+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Data Mixing Laws\" Ye 2024 ICLR 2025 predicting language modeling performance arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Data Mixing Laws\" Ye 2024 ICLR 2025 predicting language modeling performance arXiv"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T20:18:22.506523+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"knowledge collapse\" synthetic training LLM 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"knowledge collapse\" synthetic training LLM 2024 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-17T20:18:22.506660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"spectral collapse\" loss of plasticity deep learning 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"spectral collapse\" loss of plasticity deep learning 2024 2025 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T20:18:22.506808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Scheffer 2009 \"early warning signals for critical transitions\" Nature"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Scheffer 2009 \"early warning signals for critical transitions\" Nature"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T20:18:22.506966+00:00_

Web search results for query: "Gerstgrasser 2024 "Is Model Collapse Inevitable" breaking curse recursion accumulating real synthetic data arXiv"

Links: [{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Rylan Schaeffer","url":"https://rylanschaeffer.github.io/content/research/2024_arxiv_is_model_collapse_inevitable/main.html"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/html/2404.01413v2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of","url":"https://arxiv.org/pdf/2404.01413"},{"title":"[2404.01413v1] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413v1"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/is-model-collapse-inevitable-breaking-curse-recursion"},{"title":"[PDF] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/e8815da26d4e6cac8b23b7e6aa75cec028cb66d2"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data | Stanford SALT Lab","url":"https://saltlab.stanford.edu/papers/gerstgrasser-is-model-collapse-2024/"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by","url":"https://openreview.net/pdf/264715d321dd6b63cbc356483cbb650791eb374b.pdf"},{"title":"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data - ADS","url":"https://ui.adsabs.harvard.edu/abs/202
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-17T20:18:22.507147+00:00_

Web search results for query: "Scheffer 2009 "early warning signals for critical transitions" Nature"

Links: [{"title":"Early-warning signals for critical transitions | Nature","url":"https://www.nature.com/articles/nature08227"},{"title":"Early-warning signals for critical transitions - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/19727193/"},{"title":"Early-warning signals for critical transitions - Wageningen University & Research","url":"https://research.wur.nl/en/publications/early-warning-signals-for-critical-transitions/"},{"title":"(PDF) Early-Warning Signals for Critical Transitions","url":"https://www.researchgate.net/publication/26786476_Early-Warning_Signals_for_Critical_Transitions"},{"title":"REVIEWS Early-warning signals for critical transitions","url":"https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf"},{"title":"Early Warning Signals for Critical Transitions: A Generalized Modeling Approach - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3271022/"},{"title":"Early-warning signals for critical transitions - Archive ouverte HAL","url":"https://hal.science/hal-02195562"},{"title":"Early-warning signals for critical transitions Extrait du Rhuthmos","url":"https://scispace.com/pdf/early-warning-signals-for-critical-transitions-1qy2ayqlyk.pdf"},{"title":"Early Warning Signals for Critical Transitions: A Generalized Modeling Approach","url":"https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1002360&type=printable"},{"title":"Early-warning Signals for Critical Temperature Transitions","url":"https://par.nsf.gov/servlets/purl/10202827"}]

I've found the article you're looking for. The paper is by Scheffer, M., Bascompte, J., Brock, W. et al., titled "Early-warning signals for critical transitions," published in Nature 461, 53–59 (2009).

The article addresses complex systems ranging from ecosystems to financial markets and the climate that can have critical thresholds or tipping points where a sudden shi
…[truncated 372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-17T20:18:22.507316+00:00_

Web search results for query: ""Data Mixing Laws" Ye 2024 ICLR 2025 predicting language modeling performance arXiv"

Links: [{"title":"[2403.16952] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/html/2403.16952v2"},{"title":"DATA MIXING LAWS: OPTIMIZING DATA MIXTURES BY ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf"},{"title":"[2403.16952v1] Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://arxiv.org/abs/2403.16952v1"},{"title":"ICLR Poster Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance","url":"https://iclr.cc/virtual/2025/poster/28624"},{"title":"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240316952Y/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/5f67d864aae6115374fed7beddd119e0-Paper-Conference.pdf"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining | OpenReview","url":"https://openreview.net/forum?id=IKJyRyHpHV"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"}]

I found the paper you're searching for! Here are the key details:

## Paper Overview

The paper is titled "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance" and is authored by Jiasheng Ye and colleagues.

## Main Contribution

The work discovers the quantitative predictability of model performance regarding data mixture proportions in function forms, which they refer to as the data mixin
…[truncated 1019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-17T20:18:22.507497+00:00_

Web search results for query: ""spectral collapse" loss of plasticity deep learning 2024 2025 arXiv"

Links: [{"title":"Preprint. Under Review. Spectral Collapse Drives Loss of Plasticity in Deep","url":"https://arxiv.org/pdf/2509.22335"},{"title":"[2509.22335] Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning","url":"https://arxiv.org/abs/2509.22335"},{"title":"(PDF) Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning","url":"https://www.researchgate.net/publication/395944214_Spectral_Collapse_Drives_Loss_of_Plasticity_in_Deep_Continual_Learning"},{"title":"[PDF] Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning | Semantic Scholar","url":"https://api.semanticscholar.org/arXiv:2509.22335"},{"title":"SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning","url":"https://arxiv.org/html/2605.04712"},{"title":"Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning | OpenReview","url":"https://openreview.net/forum?id=l3ZwWmZ5Ht"},{"title":"NeurIPS Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/136070"},{"title":"Do Neural Networks Lose Plasticity in a Gradually Changing World?","url":"https://arxiv.org/html/2602.09234v1"},{"title":"Preserving Plasticity in Continual Learning with Adaptive Linearity Injection","url":"https://arxiv.org/html/2505.09486v1"},{"title":"[2303.07507] Loss of Plasticity in Continual Deep Reinforcement Learning","url":"https://ar5iv.labs.arxiv.org/html/2303.07507"}]

I found highly relevant results for your search query on spectral collapse and loss of plasticity in deep learning. Here are the key findings:

## Main Paper

The research investigates why deep neural networks suffer from loss of plasticity in continual learning, failing to learn new tasks without reinitializing parameters, showing that this failure is preceded by Hessian spectral co
…[truncated 1094 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-17T20:18:22.507733+00:00_

Web search results for query: ""knowledge collapse" synthetic training LLM 2024 2025 arXiv"

Links: [{"title":"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training","url":"https://arxiv.org/html/2509.04796v1"},{"title":"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term ConvergenceThis project is supported by the AI2050 program at Schmidt Sciences (Grant G-24-66104) and Army Research Office Award W911NF-23-1-0030. We also thank Cong Ma from UChicago, Hongning Wang and Bo Li from Tsinghua, Pinyan Lu and Gavin Tang from Shanghai University of Finance and Economics for helpful discussions and suggestions.","url":"https://arxiv.org/html/2510.16657v1"},{"title":"[2509.04796] Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training","url":"https://arxiv.org/abs/2509.04796"},{"title":"Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/pdf/2511.05535"},{"title":"[2406.07515] Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification","url":"https://arxiv.org/abs/2406.07515"},{"title":"Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls","url":"https://arxiv.org/html/2510.01631v1"},{"title":"AI models collapse when trained on recursively generated data | Nature","url":"https://www.nature.com/articles/s41586-024-07566-y"},{"title":"GitHub - pengr/LLM-Synthetic-Data: A live reading list for LLM data synthesis (Updated to July, 2025). · GitHub","url":"https://github.com/pengr/LLM-Synthetic-Data"},{"title":"[2404.01413] Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data","url":"https://arxiv.org/abs/2404.01413"},{"title":"Synthetic Data Generation Using Large Language Models: Advances in Text and Code","url":"https://arxiv.org/html/2503.14023v1"}]

Here are the search results for "kn
…[truncated 1868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-17T20:18:22.507932+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Noci 2024 \"Mind the Gap\" spectral analysis rank collapse attention layers arXiv authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Noci 2024 \"Mind the Gap\" spectral analysis rank collapse attention layers arXiv authors"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-17T20:18:22.508060+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "synthetic data quality evaluation LLM 2024 \"scaling up with synthesized data requires verification\" arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "synthetic data quality evaluation LLM 2024 \"scaling up with synthesized data requires verification\" arXiv"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-17T20:18:22.508180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dohmatob 2024 \"strong model collapse\" arXiv 2410.04840"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dohmatob 2024 \"strong model collapse\" arXiv 2410.04840"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-17T20:18:22.508299+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "effective rank matrix neural network representation collapse 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "effective rank matrix neural network representation collapse 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-17T20:18:22.508414+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "early warning signals tipping points machine learning loss landscape 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "early warning signals tipping points machine learning loss landscape 2024 arXiv"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-17T20:18:22.508545+00:00_

Web search results for query: "synthetic data quality evaluation LLM 2024 "scaling up with synthesized data requires verification" arXiv"

Links: [{"title":"[2406.07515] Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification","url":"https://arxiv.org/abs/2406.07515"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification","url":"https://arxiv.org/html/2406.07515v2"},{"title":"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification | OpenReview","url":"https://openreview.net/forum?id=MQXrTMonT1"}]

I found the paper you were looking for! The search returned results for **"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"**.

Here are the key details:

**Paper Information:**
- **arXiv ID:** 2406.07515
- **Title:** Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification
- **Latest Version:** October 25, 2024

**Main Focus:**

The paper investigates the use of verification on synthesized data to prevent model collapse, based on the observation that it is easier for both humans and machines to tell between good and bad examples than to generate high-quality samples.

**Methodology:**

The authors provide a theoretical characterization using Gaussian mixtures, linear classifiers, and linear verifiers to derive conditions with measurable proxies to assess whether the verifier can effectively select synthesized data that leads to optimal performance.

**Experimental Results:**

They experiment with two practical tasks -- computing matrix eigenvalues with transformers and news summarization with LLMs -- which both exhibit model collapse when trained on generated data, and show that verifiers, even imperfect ones, can indeed be harnessed to prevent model collapse and that their proposed proxy measure strongly correlates with performance.

The paper addresses the critical problem of model collapse when scaling LLMs with synthetic data, proposing veri
…[truncated 136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-17T20:18:22.508739+00:00_

Web search results for query: "Noci 2024 "Mind the Gap" spectral analysis rank collapse attention layers arXiv authors"

Links: [{"title":"[2410.07799] Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/abs/2410.07799"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/html/2410.07799v2"},{"title":"MIND THE GAP: A SPECTRAL ANALYSIS OF RANK ...","url":"https://openreview.net/pdf?id=X6xzYP2cMk"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers | OpenReview","url":"https://openreview.net/forum?id=sRKtbGsebH&noteId=l6QNJ27YLu"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and ...","url":"https://arxiv.org/pdf/2410.07799"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers","url":"https://arxiv.org/html/2410.07799v1"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/mind-gap-spectral-analysis-rank-collapse-signal"},{"title":"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers - Paper Detail","url":"https://deeplearn.org/arxiv/572034/mind-the-gap:-a-spectral-analysis-of-rank-collapse-and-signal-propagation-in-attention-layers"},{"title":"[Literature Review] Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://www.themoonlight.io/en/review/mind-the-gap-a-spectral-analysis-of-rank-collapse-and-signal-propagation-in-attention-layers"},{"title":"(PDF) Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Transformers","url":"https://www.researchgate.net/publication/384811192_Mind_the_Gap_a_Spectral_Analysis_of_Rank_Collapse_and_Signal_Propagation_in_Transformers"}]

Bas
…[truncated 1381 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-17T20:18:22.508920+00:00_

Web search results for query: "Dohmatob 2024 "strong model collapse" arXiv 2410.04840"

Links: [{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Strong Model Collapse","url":"https://arxiv.org/html/2410.04840.pdf"},{"title":"Strong Model Collapse | Request PDF","url":"https://www.researchgate.net/publication/384700001_Strong_Model_Collapse"},{"title":"Elvis Dohmatob on X: \"1/n Introducing our new preprint: Strong Model Collapse https://t.co/spdA6sGtDT, wherein we show that within the \"scaling laws\" paradigm, even 1% bad / synthetic data in the training corpus might lead to model collapse, an eventual critical flattening or even degradation of model https://t.co/ydRtUVe0BT\" / X","url":"https://x.com/dohmatobelvis/status/1844300320811241477"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v2"},{"title":"Future of AI Models: A Computational perspective on Model collapse","url":"https://arxiv.org/pdf/2511.05535"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"Position: Model Collapse Does Not Mean What You Think Anonymous Author(s)","url":"https://openreview.net/pdf?id=ygfzWIGDN8"}]

I found the paper you're looking for! Here's information about the work:

## "Strong Model Collapse" (arXiv 2410.04840)

This paper was authored by Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, and Julia Kempe, submitted on October 7, 2024.

### Main Findings

The paper establishes the existence of a strong form of the model collapse phenomenon—a critical pe
…[truncated 1015 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-17T20:18:22.509104+00:00_

Web search results for query: "effective rank matrix neural network representation collapse 2024 arXiv"

Links: [{"title":"Provable Emergence of Deep Neural Collapse and Low-Rank Bias in 𝐿²-Regularized Nonlinear Networks","url":"https://arxiv.org/html/2402.03991v2"},{"title":"[2410.07799] Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers","url":"https://arxiv.org/abs/2410.07799"},{"title":"Neural Rank Collapse: Weight Decay and Small Within-Class Variability Yield Low-Rank Bias","url":"https://arxiv.org/html/2402.03991v1"},{"title":"Preventing Representational Rank Collapse in MPNNs by Splitting the Computational Graph","url":"https://arxiv.org/html/2409.11504v2"},{"title":"Neural Collapse versus Low-rank Bias: Is Deep Neural Collapse Really Optimal?","url":"https://arxiv.org/html/2405.14468v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.10609"},{"title":"[2308.16800] Rank Collapse Causes Over-Smoothing and Over-Correlation in Graph Neural Networks","url":"https://arxiv.org/abs/2308.16800"},{"title":"[2402.03991] Provable Emergence of Deep Neural Collapse and Low-Rank Bias in $L^2$-Regularized Nonlinear Networks","url":"https://arxiv.org/abs/2402.03991"},{"title":"The Persistence of Neural Collapse Despite Low-Rank Bias","url":"https://arxiv.org/html/2410.23169"},{"title":"The Persistence of Neural Collapse Despite Low-Rank Bias: An Analytic Perspective Through Unconstrained Features","url":"https://arxiv.org/html/2410.23169v1"}]

I found several highly relevant papers from arXiv on this topic. Here are the key results:

## Main Papers Found:

1. **"Provable Emergence of Deep Neural Collapse and Low-Rank Bias in L²-Regularized Nonlinear Networks"** (arXiv:2402.03991)
   This paper presents a unified theoretical framework connecting the first property of Deep Neural Collapse (DNC1) to the emergence of implicit low-rank bias in nonlinear networks trained with L² weight decay reg
…[truncated 1392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-17T20:18:22.509297+00:00_

Web search results for query: "early warning signals tipping points machine learning loss landscape 2024 arXiv"

Links: [{"title":"Deep learning for predicting the occurrence of tipping points","url":"https://arxiv.org/html/2407.18693v2"},{"title":"Deep learning for early warning signals of tipping points | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2106140118"},{"title":"Deep learning for predicting the occurrence of tipping points","url":"https://www.researchgate.net/publication/382639058_Deep_learning_for_predicting_the_occurrence_of_tipping_points"},{"title":"Deep learning for predicting the occurrence of tipping points | Royal Society Open Science | The Royal Society","url":"https://royalsocietypublishing.org/rsos/article/12/7/242240/235692/Deep-learning-for-predicting-the-occurrence-of"},{"title":"Detecting and forecasting tipping points from sample variance alone","url":"https://arxiv.org/html/2602.10817"},{"title":"Deep learning for early warning signals of tipping points","url":"https://pubmed.ncbi.nlm.nih.gov/34544867/"},{"title":"EGUsphere - Tipping Point Detection and Early-Warnings in climate, ecological, and human systems","url":"https://egusphere.copernicus.org/preprints/2023/egusphere-2023-1773/"},{"title":"Deep learning for predicting rate-induced tipping | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-024-00937-0"},{"title":"Deep learning for predicting the occurrence of tipping points - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12303098/"},{"title":"Interpretable Early Warnings using Machine Learning in an Online Game-experiment","url":"https://arxiv.org/html/2502.09880v1"}]

I found several relevant results for your search query about early warning signals, tipping points, and machine learning. Here are the key findings:

## Main Research Areas

**Deep Learning for Tipping Point Prediction:**
Deep learning algorithms can provide early warning signals of tipping points in real-world systems, predicti
…[truncated 1473 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-17T20:18:22.509482+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03385",
  "prompt": "Extract the full list of authors, title, submission date, and any venue information for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.03385",
    "prompt": "Extract the full list of authors, title, submission date, and any venue information for this paper."
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-17T20:18:22.509629+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bury 2021 PNAS \"deep learning for early warning signals of tipping points\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bury 2021 PNAS \"deep learning for early warning signals of tipping points\" authors"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-17T20:18:22.509760+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"collapse or thrive\" \"perils and promises\" synthetic data self-generating world 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"collapse or thrive\" \"perils and promises\" synthetic data self-generating world 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-17T20:18:22.509878+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feng Dohmatob Kempe 2024 \"model collapse\" scaling laws mixture real synthetic ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feng Dohmatob Kempe 2024 \"model collapse\" scaling laws mixture real synthetic ICLR"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-17T20:18:22.510009+00:00_

# Paper Information

**Title:** "SIGMA: Scalable Spectral Insights for LLM Model Collapse"

**Authors:**
1. Yi Gu
2. Lingyou Pang
3. Xiangkun Ye
4. Tianyu Wang
5. Jianyu Lin
6. Carey E. Priebe
7. Alexander Aue

**Submission Date:** January 6, 2026 (v1); most recent revision March 23, 2026 (v3)

**Venue Information:** 
- **Category:** Computer Science > Machine Learning (cs.LG)
- **arXiv Identifier:** 2601.03385
- **DOI:** https://doi.org/10.48550/arXiv.2601.03385

**Subject Classifications:**
- Primary: Machine Learning (cs.LG); Probability (math.PR)
- MSC: 68T50 (Primary), 60F05 (Secondary)
- ACM: I.2.7; G.3

The paper presents a framework addressing "a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality" in large language models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-17T20:18:22.510162+00:00_

Web search results for query: "Bury 2021 PNAS "deep learning for early warning signals of tipping points" authors"

Links: [{"title":"Deep learning for early warning signals of tipping points | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2106140118"},{"title":"Deep learning for early warning signals of tipping points - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021PNAS..11806140B/abstract"},{"title":"Deep learning for early warning signals of tipping points","url":"https://pubmed.ncbi.nlm.nih.gov/34544867/"},{"title":"Deep learning for early warning signals of tipping points","url":"https://www.pnas.org/doi/pdf/10.1073/pnas.2106140118"},{"title":"GitHub - ThomasMBury/deep-early-warnings-pnas: Repository to accompany the publication 'Deep learning for early warning signals of tipping points', PNAS (2021) · GitHub","url":"https://github.com/ThomasMBury/deep-early-warnings-pnas"},{"title":"(PDF) Deep learning for early warning signals of tipping points","url":"https://www.researchgate.net/publication/354718209_Deep_learning_for_early_warning_signals_of_tipping_points"},{"title":"Deep learning for early warning signals of tipping points - Wageningen University & Research","url":"https://research.wur.nl/en/publications/deep-learning-for-early-warning-signals-of-tipping-points"},{"title":"Deep learning for early warning signals of tipping points | Thomas Bury","url":"https://www.thomasbury.net/publications/bury_pnas_21/"},{"title":"Deep learning for tipping points: Preprocessing matters | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.2207720119"},{"title":"Deep learning for tipping points: Preprocessing matters - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9477405/"}]

Based on the search results, I found the 2021 PNAS paper on "Deep learning for early warning signals of tipping points." The authors are Bury, T. M., Sujith, R. I., Pavithran, I., Scheffer, M., Lenton, T. M., Anand, M., & Bauch, C. T. (2021), and the paper was published in Proceedin
…[truncated 800 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-17T20:18:22.510339+00:00_

Web search results for query: "Feng Dohmatob Kempe 2024 "model collapse" scaling laws mixture real synthetic ICLR"

Links: [{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"[2410.04840] Strong Model Collapse","url":"https://arxiv.org/abs/2410.04840"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"ICLR A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://iclr.cc/virtual/2024/22420"},{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"},{"title":"Strong Model Collapse | OpenReview","url":"https://openreview.net/forum?id=et5l9qPUhm"},{"title":"Strong Model Collapse Elvis Dohmatob1 e.dohmatob@meta.com Yunzhen Feng1,2,∗","url":"https://arxiv.org/pdf/2410.04840"},{"title":"Model Collapse Demystified: The Case of Regression","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/53dbd7e34fab703a639964e2d3ee9e84-Abstract-Conference.html"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"}]

I found relevant research papers matching your search. Here are the key results:

## Main Papers Found

**1. "Strong Model Collapse" (ICLR 2025)**

Authors: Elvis Dohmatob, Yunzhen Feng, Arjun Subramonian, Julia Kempe

This paper studies model collapse—a critical performance degradation due to synthetic data in the training corpus—within the scaling laws paradigm that underpins large n
…[truncated 1531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-17T20:18:22.510516+00:00_

Web search results for query: ""collapse or thrive" "perils and promises" synthetic data self-generating world 2024 arXiv"

Links: [{"title":"[2410.16713] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/abs/2410.16713"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | OpenReview","url":"https://openreview.net/forum?id=Xr5iINA3zU"},{"title":"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://arxiv.org/html/2410.16713v2"},{"title":"Collapse or Thrive?Perils and Promises of Synthetic Data ...","url":"https://arxiv.org/pdf/2410.16713"},{"title":"(PDF) Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World"},{"title":"[PDF] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Collapse-or-Thrive-Perils-and-Promises-of-Synthetic-Kazdan-Schaeffer/4b510679ec7f6d138b04d5d0afff9ff316264974"},{"title":"COLLAPSE OR THRIVE? PERILS AND PROMISES OF","url":"https://www.researchgate.net/publication/385140496_Collapse_or_Thrive_Perils_and_Promises_of_Synthetic_Data_in_a_Self-Generating_World/fulltext/67186c5a24a01038d0001510/Collapse-or-Thrive-Perils-and-Promises-of-Synthetic-Data-in-a-Self-Generating-World.pdf?origin=scientificContributions"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.16713"},{"title":"GitHub - RylanSchaeffer/KoyejoLab-Collapse-or-Thrive: Code for Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World","url":"https://github.com/RylanSchaeffer/KoyejoLab-Collapse-or-Thrive"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/25
…[truncated 1865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-17T20:18:22.510727+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.07043",
  "prompt": "Extract the full list of authors, title, venue if mentioned, and submission date for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2402.07043",
    "prompt": "Extract the full list of authors, title, venue if mentioned, and submission date for this paper."
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-17T20:18:22.510866+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.16713",
  "prompt": "Extract the full list of authors, title, and submission date for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2410.16713",
    "prompt": "Extract the full list of authors, title, and submission date for this paper."
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-17T20:18:22.510989+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2307.01850",
  "prompt": "Extract the full list of authors and venue for this paper (Self-Consuming Generative Models Go MAD)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2307.01850",
    "prompt": "Extract the full list of authors and venue for this paper (Self-Consuming Generative Models Go MAD)."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-17T20:18:22.511108+00:00_

# Paper Details

**Title:** "A Tale of Tails: Model Collapse as a Change of Scaling Laws"

**Authors:**
- Elvis Dohmatob
- Yunzhen Feng
- Pu Yang
- Francois Charton
- Julia Kempe

**Venue:** ICML 2024

**Submission Date:** February 10, 2024 (v1); revised May 31, 2024 (v2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-17T20:18:22.511226+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.22335",
  "prompt": "Extract the full list of authors, title, submission date, and any venue information for this paper about spectral collapse and loss of plasticity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.22335",
    "prompt": "Extract the full list of authors, title, submission date, and any venue information for this paper about spectral collapse and loss of plasticity."
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-17T20:18:22.511344+00:00_

# Paper Details

**Title:** "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"

**Authors:**
1. Joshua Kazdan
2. Rylan Schaeffer
3. Apratim Dey
4. Matthias Gerstgrasser
5. Rafael Rafailov
6. David L. Donoho
7. Sanmi Koyejo

**Submission Date:** October 22, 2024 (initial submission); most recent version March 17, 2025

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-17T20:18:22.511461+00:00_

# Authors and Venue

**Authors:**
1. Sina Alemohammad
2. Josue Casco-Rodriguez
3. Lorenzo Luzi
4. Ahmed Imtiaz Humayun
5. Hossein Babaei
6. Daniel LeJeune
7. Ali Siahkoohi
8. Richard G. Baraniuk

**Venue:**
The paper was submitted to arXiv on July 4, 2023 (arXiv:2307.01850). It is categorized under Computer Science > Machine Learning, with additional classifications in Artificial Intelligence and Computer Vision and Pattern Recognition. There is no specific conference or journal venue listed on this abstract page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-17T20:18:22.511583+00:00_

# Paper Information

**Title:** "Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning"

**Authors:**
1. Naicheng He
2. Kaicheng Guo
3. Arjun Prakash
4. Saket Tiwari
5. Ruo Yu Tao
6. Tyrone Serapio
7. Amy Greenwald
8. George Konidaris

**Submission Date:** September 26, 2025 (v1); September 29, 2025 (v2)

**Venue Information:** Posted to arXiv under Computer Science > Machine Learning (cs.LG); also classified under Artificial Intelligence (cs.AI)

**arXiv Identifier:** 2509.22335

**Key Finding:** The research demonstrates that "Hessian spectral collapse at new-task initialization" prevents neural networks from learning new tasks effectively without parameter reinitialization, and proposes regularization strategies to address this issue.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-17T20:18:22.511744+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu 2024 \"what makes good data for alignment\" data selection quality arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu 2024 \"what makes good data for alignment\" data selection quality arXiv"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-17T20:18:22.511869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "representation collapse neural network continual learning dimensional reduction 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "representation collapse neural network continual learning dimensional reduction 2024 arXiv"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-17T20:18:22.511986+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2406.07515",
  "prompt": "Extract the full list of authors, title, and venue for this paper about scaling up with synthesized data requires verification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2406.07515",
    "prompt": "Extract the full list of authors, title, and venue for this paper about scaling up with synthesized data requires verification."
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-17T20:18:22.512101+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.04796",
  "prompt": "Extract the full list of authors, title, and submission date for this paper about knowledge collapse in LLMs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.04796",
    "prompt": "Extract the full list of authors, title, and submission date for this paper about knowledge collapse in LLMs."
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-17T20:18:22.512219+00:00_

# Paper Details

**Title:** "Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification"

**Authors:** 
- Yunzhen Feng
- Elvis Dohmatob
- Pu Yang
- Francois Charton
- Julia Kempe

**Venue:** arXiv:2406.07515 (Computer Science > Machine Learning)

The research addresses how verifiers can prevent model degradation when large language models train on AI-generated content, demonstrating this through theoretical analysis and experiments in matrix eigenvalue computation and news summarization tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-17T20:18:22.512338+00:00_

# Paper Information

**Title:** "Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training"

**Authors:**
1. Figarri Keisha
2. Zekun Wu
3. Ze Wang
4. Adriano Koshiyama
5. Philip Treleaven

**Submission Date:** September 5, 2025

The research examines how language models experience degradation in factual accuracy while maintaining surface-level coherence when trained recursively on synthetic data. The team proposes domain-specific synthetic training as a mitigation strategy and develops evaluation frameworks to detect distinct phases of this epistemic deterioration.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-17T20:18:22.512490+00:00_

Web search results for query: "Liu 2024 "what makes good data for alignment" data selection quality arXiv"

Links: [{"title":"[2312.15685] What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning","url":"https://arxiv.org/abs/2312.15685"},{"title":"What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning","url":"https://arxiv.org/html/2312.15685v2"},{"title":"What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/what-makes-good-data-alignment-comprehensive-study"},{"title":"Less is More: Improving LLM Alignment via Preference Data Selection","url":"https://arxiv.org/html/2502.14560v4"},{"title":"WHAT MAKES GOOD DATA FOR ALIGNMENT? A ...","url":"https://openreview.net/pdf?id=BTKAeLqLMw"},{"title":"A Data Selection Principle for LLM Alignment via Fine- ...","url":"https://arxiv.org/pdf/2508.07638"},{"title":"dblp: What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning.","url":"https://dblp.org/rec/journals/corr/abs-2312-15685.html"},{"title":"What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning | OpenReview","url":"https://openreview.net/forum?id=BTKAeLqLMw"},{"title":"ICLR Poster What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning","url":"https://iclr.cc/virtual/2024/poster/19215"},{"title":"Principled Data Selection for Alignment: The Hidden Risks of Difficult Examples","url":"https://arxiv.org/html/2502.09650v1"}]

I found the paper you're looking for! Here are the key details:

## Paper Overview

The paper is titled "What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection in Instruction Tuning" by Wei Liu, Weihao Zeng, Keqing He, Yong Jiang, and Ju
…[truncated 1378 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-17T20:18:22.512688+00:00_

Web search results for query: "representation collapse neural network continual learning dimensional reduction 2024 arXiv"

Links: [{"title":"Rethinking Continual Learning with Progressive Neural ...","url":"https://arxiv.org/pdf/2505.24254"},{"title":"Rethinking Continual Learning with Progressive Neural Collapse","url":"https://arxiv.org/html/2505.24254v1"},{"title":"preventing collapse in contrastive learning","url":"https://arxiv.org/pdf/2403.18699"},{"title":"Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/html/2505.15239v1"},{"title":"[2505.24254] Rethinking Continual Learning with Progressive Neural Collapse","url":"https://arxiv.org/abs/2505.24254"},{"title":"Wide Neural Networks Trained with Weight Decay Provably Exhibit Neural Collapse","url":"https://arxiv.org/html/2410.04887v1"},{"title":"Memory-efficient Continual Learning with Neural Collapse Contrastive","url":"https://arxiv.org/html/2412.02865v2"},{"title":"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective","url":"https://arxiv.org/html/2509.16499v1"},{"title":"Neural Collapse beyond the Unconstrainted Features Model: Landscape, Dynamics, and Generalization in the Mean-Field Regime","url":"https://arxiv.org/html/2501.19104v1"},{"title":"[2505.15239] Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/abs/2505.15239"}]

I've found several highly relevant papers on arXiv related to your search query about representation collapse, neural networks, continual learning, and dimensional reduction from 2024 onwards:

## Key Findings:

**1. Rethinking Continual Learning with Progressive Neural Collapse (arXiv:2505.24254)**
This paper addresses continual learning (CL), which aims to build an agent that can continuously learn a sequence of tasks where catastrophic forgetting is a key challenge, while noting that deep neural networks converge to a terminal state calle
…[truncated 1634 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-17T20:18:22.512859+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2305.15717",
  "prompt": "Extract the full list of authors and venue for this paper (The False Promise of Imitating Proprietary LLMs)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2305.15717",
    "prompt": "Extract the full list of authors and venue for this paper (The False Promise of Imitating Proprietary LLMs)."
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-17T20:18:22.512983+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2403.16952",
  "prompt": "Extract the full list of authors for Data Mixing Laws paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2403.16952",
    "prompt": "Extract the full list of authors for Data Mixing Laws paper."
  }
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-17T20:18:22.513102+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.01413",
  "prompt": "Extract the full list of authors for this paper (Is Model Collapse Inevitable?)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2404.01413",
    "prompt": "Extract the full list of authors for this paper (Is Model Collapse Inevitable?)."
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-17T20:18:22.513221+00:00_

# Paper Details

**Authors:**
1. Arnav Gudibande
2. Eric Wallace
3. Charlie Snell
4. Xinyang Geng
5. Hao Liu
6. Pieter Abbeel
7. Sergey Levine
8. Dawn Song

**Venue:**
The paper was submitted to arXiv in the Computer Science > Computation and Language (cs.CL) category on May 25, 2023. No traditional conference or journal venue is specified on this abstract page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-17T20:18:22.513344+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dakos 2012 \"methods for detecting early warnings of critical transitions\" time series review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dakos 2012 \"methods for detecting early warnings of critical transitions\" time series review"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-17T20:18:22.513462+00:00_

# Authors of "Data Mixing Laws" Paper

Based on the arXiv page, the complete author list is:

1. Jiasheng Ye
2. Peiju Liu
3. Tianxiang Sun
4. Jun Zhan
5. Yunhua Zhou
6. Xipeng Qiu

The paper was submitted on March 25, 2024, and accepted by ICLR 2025.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-17T20:18:22.513579+00:00_

# Authors of "Is Model Collapse Inevitable?"

Based on the arXiv page, the paper has 14 authors:

1. Matthias Gerstgrasser
2. Rylan Schaeffer
3. Apratim Dey
4. Rafael Rafailov
5. Henry Sleight
6. John Hughes
7. Tomasz Korbak
8. Rajashree Agrawal
9. Dhruv Pai
10. Andrey Gromov
11. Daniel A. Roberts
12. Diyi Yang
13. David L. Donoho
14. Sanmi Koyejo

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-17T20:18:22.513753+00:00_

Web search results for query: "Dakos 2012 "methods for detecting early warnings of critical transitions" time series review"

Links: [{"title":"Methods for detecting early warnings of critical transitions in time series illustrated using simulated ecological data - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/22815897/"},{"title":"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data | PLOS One","url":"https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0041010"},{"title":"Methods for Detecting Early Warnings of Critical Transitions in ...","url":"https://harvardforest1.fas.harvard.edu/publications/pdfs/Dakos_PLoS1_2012.pdf"},{"title":"Early-warning signals – Vasilis Dakos","url":"https://www.vasilisdakos.info/?page_id=1192"},{"title":"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC3398887/"},{"title":"(PDF) Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data","url":"https://www.researchgate.net/publication/229427899_Methods_for_Detecting_Early_Warnings_of_Critical_Transitions_in_Time_Series_Illustrated_Using_Simulated_Ecological_Data"},{"title":"Methods For Detecting Early Warnings Of Critical Transitions ...","url":"https://dash.harvard.edu/bitstreams/7312037c-ad30-6bd4-e053-0100007fdf3b/download"},{"title":"Methods For Detecting Early Warnings Of Critical Transitions In Time Series Illustrated Using Simulated Ecological Data","url":"https://dash.harvard.edu/entities/publication/73120378-a86c-6bd4-e053-0100007fdf3b"},{"title":"[PDF] Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Methods-for-Detecting-Early-Warnings-of-Critical-in-Dakos-Carpenter/b22b4090
…[truncated 1894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-17T20:18:22.513913+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AIOLI 2025 ICLR adaptive online data mixing language model pretraining arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AIOLI 2025 ICLR adaptive online data mixing language model pretraining arXiv"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-17T20:18:22.514038+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Roy Vetterli 2007 \"effective rank\" matrix singular value distribution definition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Roy Vetterli 2007 \"effective rank\" matrix singular value distribution definition"
  }
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-17T20:18:22.514156+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Model Collapse Demystified\" Dohmatob Feng Kempe NeurIPS 2024 arXiv regression"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Model Collapse Demystified\" Dohmatob Feng Kempe NeurIPS 2024 arXiv regression"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-17T20:18:22.514303+00:00_

Web search results for query: "Roy Vetterli 2007 "effective rank" matrix singular value distribution definition"

Links: [{"title":"(PDF) The Effective Rank: A Measure of Effective Dimensionality","url":"https://www.researchgate.net/publication/37450697_The_Effective_Rank_A_Measure_of_Effective_Dimensionality"},{"title":"THE EFFECTIVE RANK: A MEASURE OF EFFECTIVE DIMENSIONALITY","url":"https://www.eurasip.org/Proceedings/Eusipco/Eusipco2007/Papers/a5p-h05.pdf"},{"title":"Effective Rank and Dimensionality Reduction: from","url":"https://www.centrosraffa.org/public/1f685cea-d1d8-4fb7-a8e4-05be677952d1.pdf"},{"title":"Estimating the Effective Rank of Vision Transformers via Low-Rank Factorization","url":"https://arxiv.org/pdf/2512.00792"},{"title":"Effective Rank and Dimensionality Reduction","url":"https://mpra.ub.uni-muenchen.de/113068/1/MPRA_paper_113068.pdf"},{"title":"[PDF] The effective rank: A measure of effective dimensionality | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-effective-rank:-A-measure-of-effective-Roy-Vetterli/497eb64754cace3afd79aab6062fddf8ca21b60f"},{"title":"The effective rank (plain) and the rank (dashed) of the matrix A of... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-effective-rank-plain-and-the-rank-dashed-of-the-matrix-A-of-Section-23-as-a_fig1_37450697"},{"title":"Matrix Information Theory for Self-Supervised Learning","url":"https://arxiv.org/pdf/2305.17326"},{"title":"The effective rank: A measure of effective dimensionality | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7098875/"},{"title":"The Effective Rank: A Measure of Effective Dimensionality","url":"https://infoscience.epfl.ch/entities/publication/f3c74b8f-1cad-43ed-8696-04b318d58703"}]

Based on the web search results, I found comprehensive information about Roy & Vetterli's 2007 definition of effective rank:

## Definition

The effective rank is defined as the exponential of the
…[truncated 952 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-17T20:18:22.514474+00:00_

Web search results for query: "AIOLI 2025 ICLR adaptive online data mixing language model pretraining arXiv"

Links: [{"title":"Published as a conference paper at ICLR 2025 AIOLI:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/71cc3acb2578bdd1e52bf9f85bbb1af0-Paper-Conference.pdf"},{"title":"Aioli: A unified optimization framework for language model data mixing","url":"https://arxiv.org/html/2411.05735"},{"title":"[2411.05735] Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://arxiv.org/abs/2411.05735"},{"title":"DATA MIXING LAWS: OPTIMIZING DATA MIXTURES BY ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/cc84bfabe6389d8883fc2071c848f62a-Paper-Conference.pdf"},{"title":"[2505.23878] Actor-Critic based Online Data Mixing For Language Model Pre-Training","url":"https://arxiv.org/abs/2505.23878"},{"title":"Aioli: A Unified Optimization Framework for Language Model Data Mixing | OpenReview","url":"https://openreview.net/forum?id=R8nT7EqoYF"},{"title":"[2312.02406] Efficient Online Data Mixing For Language Model Pre-Training","url":"https://arxiv.org/abs/2312.02406"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05629"},{"title":"Paper page - Aioli: A Unified Optimization Framework for Language Model Data Mixing","url":"https://huggingface.co/papers/2411.05735"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"}]

Based on the search results, here's information about AIOLI:

## Overview

AIOLI is a new online method which directly estimates the mixing law parameters throughout training and uses them to dynamically adjust proportions. AIOLI is a simple new online data mixing method derived from the LMO framework. Unlike existing online methods, AIOLI directly estimates the parameters from the current training run by fitting the mixing law on the history of losses and dynamic mixture proportions so far. AIOLI is thus able to dynami
…[truncated 1264 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-17T20:18:22.514671+00:00_

Web search results for query: ""Model Collapse Demystified" Dohmatob Feng Kempe NeurIPS 2024 arXiv regression"

Links: [{"title":"Model Collapse Demystified: The Case of Regression","url":"https://proceedings.neurips.cc/paper_files/paper/2024/hash/53dbd7e34fab703a639964e2d3ee9e84-Abstract-Conference.html"},{"title":"NeurIPS Poster Model Collapse Demystified: The Case of Regression","url":"https://neurips.cc/virtual/2024/poster/94468"},{"title":"Model Collapse Demystified: The Case of Regression Elvis Dohmatob§ ∗","url":"https://papers.neurips.cc/paper_files/paper/2024/file/53dbd7e34fab703a639964e2d3ee9e84-Paper-Conference.pdf"},{"title":"Overcoming the AI Data Crisis: A New Solution to Model Collapse | by NYU Center for Data Science | Medium","url":"https://nyudatascience.medium.com/overcoming-the-ai-data-crisis-a-new-solution-to-model-collapse-ddc5b382e182"},{"title":"Model Collapse Demystified: The Case of Regression | OpenReview","url":"https://openreview.net/forum?id=bioHNTRnQk"},{"title":"Strong Model Collapse - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004840D/abstract"},{"title":"Published as a conference paper at ICLR 2025 STRONG MODEL COLLAPSE","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/284afdc2309f9667d2d4fb9290235b0c-Paper-Conference.pdf"},{"title":"A Tale of Tails: Model Collapse as a Change of Scaling Laws | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10534888-tale-tails-model-collapse-change-scaling-laws"},{"title":"[2402.07712] Model Collapse Demystified: The Case of Regression","url":"https://arxiv.org/abs/2402.07712"},{"title":"[2402.07043] A Tale of Tails: Model Collapse as a Change of Scaling Laws","url":"https://arxiv.org/abs/2402.07043"}]

I found relevant information about the paper you requested. Here are the search results:

## "Model Collapse Demystified: The Case of Regression"

The paper was authored by Elvis Dohmatob, Yunzhen Feng, and Julia Kempe and was presented at Advances in Neu
…[truncated 1160 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-17T20:18:22.514899+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2411.05735",
  "prompt": "Extract the full list of authors for AIOLI paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2411.05735",
    "prompt": "Extract the full list of authors for AIOLI paper."
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-17T20:18:22.515030+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Martin Mahoney 2021 \"implicit self-regularization\" spectral analysis weight matrices deep neural networks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Martin Mahoney 2021 \"implicit self-regularization\" spectral analysis weight matrices deep neural networks"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-17T20:18:22.515150+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "synthetic data detection filtering LLM quality 2024 arXiv watermark perplexity filter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "tool_args": {
    "query": "synthetic data detection filtering LLM quality 2024 arXiv watermark perplexity filter"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-17T20:18:22.515281+00:00_

# Authors of the Aioli Paper

Based on the arXiv page, the complete list of authors for "Aioli: A Unified Optimization Framework for Language Model Data Mixing" is:

1. Mayee F. Chen
2. Michael Y. Hu
3. Nicholas Lourie
4. Kyunghyun Cho
5. Christopher Ré

The paper was submitted on November 8, 2024, and revised on April 21, 2025, with acceptance at ICLR 2025.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-17T20:18:22.515430+00:00_

Web search results for query: "Martin Mahoney 2021 "implicit self-regularization" spectral analysis weight matrices deep neural networks"

Links: [{"title":"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning","url":"https://jmlr.org/papers/v22/20-410.html"},{"title":"[1810.01075] Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning","url":"https://arxiv.org/abs/1810.01075"},{"title":"[PDF] Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Implicit-Self-Regularization-in-Deep-Neural-from-Martin-Mahoney/97d6efc6b524bff216c5a77f243821c2980b2073"},{"title":"[1901.08276] Traditional and Heavy-Tailed Self Regularization in Neural Network Models","url":"https://arxiv.org/abs/1901.08276"},{"title":"Implicit Self-Regularization in Deep Neural Networks","url":"https://jmlr.org/papers/volume22/20-410/20-410.pdf"},{"title":"https://scholar.google.com/scholar_lookup?title=Im...","url":"https://scholar.google.com/scholar_lookup?title=Implicit+self-regularization+in+deep+neural+networks:+Evidence+from+random+matrix+theory+and+implications+for+learning&author=Martin,+C.H.&author=Mahoney,+M.W.&publication_year=2021&journal=J.+Mach.+Learn.+Res.&volume=22&pages=7479%E2%80%937551"},{"title":"Data Diversity as Implicit Regularization: How Does Diversity Shape the Weight Space of Deep Neural Networks?","url":"https://arxiv.org/html/2410.14602"},{"title":"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning","url":"https://jmlr.csail.mit.edu/beta/papers/v22/20-410.html"},{"title":"(PDF) Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning","url":"https://www.researchgate.net/publication/328107188
…[truncated 2065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-17T20:18:22.515617+00:00_

Web search results for query: "synthetic data detection filtering LLM quality 2024 arXiv watermark perplexity filter"

Links: [{"title":"The data-quality illusion: Rethinking Classifier-based quality filtering for LLM Pretraining","url":"https://arxiv.org/html/2510.00866v1"},{"title":"Enhancing Watermarking Quality for LLMs via Contextual Generation States Awareness","url":"https://arxiv.org/html/2506.07403"},{"title":"Dataset Protection via Watermarked Canaries in Retrieval-Augmented LLMs","url":"https://arxiv.org/html/2502.10673"},{"title":"Ultra-FineWeb: Efficient Data Filtering and Verification for High-Quality LLM Training Data","url":"https://arxiv.org/html/2505.05427v1"},{"title":"GitHub - tianyi-lab/Cherry_LLM: [NAACL'24] Self-data filtering of LLM instruction-tuning data using a novel perplexity-based difficulty score, without using any other models · GitHub","url":"https://github.com/tianyi-lab/Cherry_LLM"},{"title":"Towards Better Statistical Understanding of Watermarking LLMs","url":"https://arxiv.org/html/2403.13027"},{"title":"Dataset Watermarking for Closed LLMs with Provable Detection","url":"https://arxiv.org/html/2605.06865"},{"title":"Robust Data Watermarking in Language Models by Injecting Fictitious Knowledge","url":"https://arxiv.org/html/2503.04036v2"},{"title":"WaterMax: breaking the LLM watermark detectability-robustness-quality trade-off","url":"https://arxiv.org/html/2403.04808v3"},{"title":"Improving Detection of Watermarked Language Models","url":"https://arxiv.org/html/2508.13131v1"}]

I've completed the web search for your query about synthetic data detection, filtering, LLM quality, and related topics from 2024 arXiv papers. Here are the key findings:

## Main Research Areas Found:

**1. Data Quality Filtering for LLM Pretraining**

Recent surveys identify classifier-based and perplexity-based filtering as the most widely used techniques for data selection, with classifier-based methods being the most effective in practice. Classifier
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-17T20:18:22.515860+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-17T20:18:22.516001+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
figures
logs
memory.md
mistakes.lock
mistakes.yaml
paper
paper_framing.md
registry.lock
registry.yaml
report.md
study_status.lock
task_context
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-17T20:18:22.516166+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml",
  "content": "papers:\n  # ============================================================\n  # Cluster 1: model_collapse_core (6 papers)\n  # ============================================================\n  - bibtex_key: shumailov2024collapse\n    title: \"AI models collapse when trained on recursively generated data\"\n    authors: \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\"\n    year: 2024\n    venue: \"Nature\"\n    arxiv_id: \"2305.17493\"\n    doi: \"10.1038/s41586-024-07566-y\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Shows that training on model-generated data causes irreversible defects where tails of the original content distribution disappear, leading to model collapse across LLMs, VAEs, and GMMs.\"\n    relevance: \"Seminal paper defining model collapse. Our work provides spectral EWS to detect collapse onset before irreversible degradation.\"\n\n  - bibtex_key: dohmatob2024tails\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2402.07043\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Provides first theoretical framework for model collapse through scaling laws, showing how tail distributions vanish across generations with validated experiments on transformers.\"\n    relevance: \"Theoretical foundation for understanding collapse dynamics. Our spectral metrics connect to their scaling law framework.\"\n\n  - bibtex_key: alemohammad2024mad\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2307.01850\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Introduces Model Autophagy Disorder (MAD) showing that without fresh real data, autophagous loops cause progressive quality/diversity loss in just a few generations.\"\n    relevance: \"Establishes MAD framework for self-consuming loops. Our EWS can detect MADness onset before quality degrades.\"\n\n  - bibtex_key: gerstgrasser2024inevitable\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\"\n    year: 2024\n    venue: \"arXiv\"\n    arxiv_id: \"2404.01413\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Shows that accumulating synthetic data alongside real data avoids model collapse, with finite upper bound on test error independent of iteration count.\"\n    relevance: \"Key mitigation result. Our EWS enables knowing when to inject real data vs. when accumulation suffices.\"\n\n  - bibtex_key: dohmatob2024demystified\n    title: \"Model Collapse Demystified: The Case of Regression\"\n    authors: \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    arxiv_id: \"2402.07712\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Derives analytical formulas for model collapse in high-dimensional regression, revealing modified scaling laws with crossover phenomena in both under- and over-parameterized regimes.\"\n    relevance: \"Provides analytical collapse characterization. Our spectral metrics offer empirical detection aligned with their theory.\"\n\n  - bibtex_key: dohmatob2025strong\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\"\n    year: 2025\n    venue: \"ICLR 2025\"\n    arxiv_id: \"2410.04840\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Proves that even 1% synthetic data in training corpus leads to model collapse within scaling laws paradigm, using operator-valued free probability theory.\"\n    relevance: \"Strongest theoretical result on collapse inevitability. Motivates need for early detection even with small synthetic contamination.\"\n\n  # ============================================================\n  # Cluster 2: spectral_analysis_collapse (5 papers)\n  # ============================================================\n  - bibtex_key: gu2026sigma\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander\"\n    year: 2026\n    venue: \"arXiv\"\n    arxiv_id: \"2601.03385\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Proposes SIGMA framework using spectral bounds of embedding Gram matrix to quantify model collapse, benchmarking on OPT-125M across recursive training generations.\"\n    relevance: \"Most directly related work. Uses spectral analysis for collapse detection. Our contribution extends with EWS methodology and predictive capability.\"\n\n  - bibtex_key: naderi2025mindgap\n    title: \"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers\"\n    authors: \"Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared\"\n    year: 2025\n    venue: \"ICML 2025\"\n    arxiv_id: \"2410.07799\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Uses Random Matrix Theory to uncover spectral gap between largest singular values as cause of rank collapse in attention, proposing eigenvalue removal as mitigation.\"\n    relevance: \"Provides spectral characterization of rank collapse in transformers. Our work applies similar spectral analysis to detect data-driven collapse.\"\n\n  - bibtex_key: he2025spectral\n    title: \"Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning\"\n    authors: \"He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2509.22335\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Shows Hessian spectral collapse at new-task initialization prevents learning, proposing effective rank regularization and L2 penalties to preserve plasticity.\"\n    relevance: \"Demonstrates spectral collapse as mechanism for plasticity loss. Parallels our finding that spectral signatures predict collapse in recursive training.\"\n\n  - bibtex_key: roy2007effectiverank\n    title: \"The Effective Rank: A Measure of Effective Dimensionality\"\n    authors: \"Roy, Olivier and Vetterli, Martin\"\n    year: 2007\n    venue: \"EUSIPCO 2007\"\n    arxiv_id: \"\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Defines effective rank as exponential of Shannon entropy of normalized singular value distribution, providing continuous measure of matrix dimensionality.\"\n    relevance: \"Foundation metric for our EWS. We track effective rank decline of representation matrices as collapse indicator.\"\n\n  - bibtex_key: martin2021implicit\n    title: \"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning\"\n    authors: \"Martin, Charles H. and Mahoney, Michael W.\"\n    year: 2021\n    venue: \"JMLR\"\n    arxiv_id: \"1810.01075\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Applies RMT to analyze weight matrix spectra in DNNs, identifying implicit self-regularization through heavy-tailed spectral distributions correlated with model quality.\"\n    relevance: \"Establishes spectral analysis of weight matrices as diagnostic tool. Our approach extends to representation matrices under recursive training.\"\n\n  # ============================================================\n  # Cluster 3: data_mixing_strategies (4 papers)\n  # ============================================================\n  - bibtex_key: xie2023doremi\n    title: \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\"\n    authors: \"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2305.10429\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Uses group DRO on proxy model to optimize domain mixture proportions, improving downstream accuracy by 6.5% and reaching baseline performance with 2.6x fewer steps.\"\n    relevance: \"Establishes data mixing optimization. Our EWS can inform when to adjust mixing ratios during recursive training.\"\n\n  - bibtex_key: ye2025mixinglaws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng\"\n    year: 2025\n    venue: \"ICLR 2025\"\n    arxiv_id: \"2403.16952\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Discovers quantitative data mixing laws predicting model performance from mixture proportions, enabling optimization of 1B model training with 48% fewer steps.\"\n    relevance: \"Provides predictive framework for data mixing. Our spectral EWS complements by detecting when current mixture causes collapse.\"\n\n  - bibtex_key: chen2025aioli\n    title: \"Aioli: A Unified Optimization Framework for Language Model Data Mixing\"\n    authors: \"Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\\\'{e}, Christopher\"\n    year: 2025\n    venue: \"ICLR 2025\"\n    arxiv_id: \"2411.05735\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Unifies existing data mixing methods into common optimization framework, proposing online method that dynamically estimates mixing law parameters during training.\"\n    relevance: \"Online mixing adjustment mechanism. Our EWS provides signal for when to trigger mixture proportion updates.\"\n\n  - bibtex_key: kazdan2024collapsethrive\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi\"\n    year: 2024\n    venue: \"arXiv\"\n    arxiv_id: \"2410.16713\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Studies three data workflows (replace/accumulate/fixed-compute) showing collapse only under replacement, with non-trivial real-synthetic data interactions.\"\n    relevance: \"Characterizes when synthetic data helps vs. hurts. Our EWS enables real-time workflow selection based on spectral health.\"\n\n  # ============================================================\n  # Cluster 4: synthetic_data_quality (3 papers)\n  # ============================================================\n  - bibtex_key: gudibande2024falsepromise\n    title: \"The False Promise of Imitating Proprietary LLMs\"\n    authors: \"Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2305.15717\"\n    doi: \"\"\n    category: synthetic_data_quality\n    verified: true\n    abstract_short: \"Shows imitation models trained on proprietary LLM outputs appear fluent but close little capability gap, revealing fundamental quality limitations of synthetic training data.\"\n    relevance: \"Demonstrates quality degradation from synthetic imitation. Our spectral metrics can quantify this capability gap during training.\"\n\n  - bibtex_key: feng2024verification\n    title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n    authors: \"Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia\"\n    year: 2024\n    venue: \"arXiv\"\n    arxiv_id: \"2406.07515\"\n    doi: \"\"\n    category: synthetic_data_quality\n    verified: true\n    abstract_short: \"Shows that even imperfect verifiers can prevent model collapse when scaling with synthetic data, providing theoretical conditions for effective verification.\"\n    relevance: \"Verification as collapse prevention. Our EWS serves as a verification signal indicating when synthetic data quality degrades.\"\n\n  - bibtex_key: keisha2025knowledge\n    title: \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\"\n    authors: \"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip\"\n    year: 2025\n    venue: \"arXiv\"\n    arxiv_id: \"2509.04796\"\n    doi: \"\"\n    category: synthetic_data_quality\n    verified: true\n    abstract_short: \"Defines three-stage knowledge collapse where factual accuracy erodes while fluency persists, creating confidently wrong outputs under recursive synthetic training.\"\n    relevance: \"Identifies knowledge collapse as distinct from perplexity collapse. Our spectral EWS may detect this before factual degradation manifests.\"\n\n  # ============================================================\n  # Cluster 5: early_warning_signals (3 papers)\n  # ============================================================\n  - bibtex_key: scheffer2009ews\n    title: \"Early-warning signals for critical transitions\"\n    authors: \"Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George\"\n    year: 2009\n    venue: \"Nature\"\n    arxiv_id: \"\"\n    doi: \"10.1038/nature08227\"\n    category: early_warning_signals\n    verified: true\n    abstract_short: \"Proposes generic early warning signals (rising variance, autocorrelation, spectral reddening) indicating proximity to critical tipping points in complex systems.\"\n    relevance: \"Foundational EWS theory. We adapt critical slowing down indicators to neural network representation space for collapse detection.\"\n\n  - bibtex_key: bury2021deeplearning\n    title: \"Deep learning for early warning signals of tipping points\"\n    authors: \"Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.\"\n    year: 2021\n    venue: \"PNAS\"\n    arxiv_id: \"\"\n    doi: \"10.1073/pnas.2106140118\"\n    category: early_warning_signals\n    verified: true\n    abstract_short: \"Develops deep learning algorithm for EWS that generalizes across systems, providing higher sensitivity and fewer false positives than generic statistical indicators.\"\n    relevance: \"Demonstrates ML-based EWS for tipping points. Inspires our approach of learning spectral EWS patterns for model collapse detection.\"\n\n  - bibtex_key: dakos2012methods\n    title: \"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data\"\n    authors: \"Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten\"\n    year: 2012\n    venue: \"PLOS ONE\"\n    arxiv_id: \"\"\n    doi: \"10.1371/journal.pone.0041010\"\n    category: early_warning_signals\n    verified: true\n    abstract_short: \"Comprehensive comparison of metric-based and model-based EWS methods for time series, providing practical toolbox for detecting approaching critical transitions.\"\n    relevance: \"Methodological reference for EWS detection. We adapt their time-series indicators to spectral metric trajectories during training.\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml",
    "content": "papers:\n  # ============================================================\n  # Cluster 1: model_collapse_core (6 papers)\n  # ============================================================\n  - bibtex_key: shumailov2024collapse\n    title: \"AI models collapse when trained on recursively generated data\"\n    authors: \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin\"\n    year: 2024\n    venue: \"Nature\"\n    arxiv_id: \"2305.17493\"\n    doi: \"10.1038/s41586-024-07566-y\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Shows that training on model-generated data causes irreversible defects where tails of the original content distribution disappear, leading to model collapse across LLMs, VAEs, and GMMs.\"\n    relevance: \"Seminal paper defining model collapse. Our work provides spectral EWS to detect collapse onset before irreversible degradation.\"\n\n  - bibtex_key: dohmatob2024tails\n    title: \"A Tale of Tails: Model Collapse as a Change of Scaling Laws\"\n    authors: \"Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2402.07043\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Provides first theoretical framework for model collapse through scaling laws, showing how tail distributions vanish across generations with validated experiments on transformers.\"\n    relevance: \"Theoretical foundation for understanding collapse dynamics. Our spectral metrics connect to their scaling law framework.\"\n\n  - bibtex_key: alemohammad2024mad\n    title: \"Self-Consuming Generative Models Go MAD\"\n    authors: \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2307.01850\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Introduces Model Autophagy Disorder (MAD) showing that without fresh real data, autophagous loops cause progressive quality/diversity loss in just a few generations.\"\n    relevance: \"Establishes MAD framework for self-consuming loops. Our EWS can detect MADness onset before quality degrades.\"\n\n  - bibtex_key: gerstgrasser2024inevitable\n    title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n    authors: \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi\"\n    year: 2024\n    venue: \"arXiv\"\n    arxiv_id: \"2404.01413\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Shows that accumulating synthetic data alongside real data avoids model collapse, with finite upper bound on test error independent of iteration count.\"\n    relevance: \"Key mitigation result. Our EWS enables knowing when to inject real data vs. when accumulation suffices.\"\n\n  - bibtex_key: dohmatob2024demystified\n    title: \"Model Collapse Demystified: The Case of Regression\"\n    authors: \"Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia\"\n    year: 2024\n    venue: \"NeurIPS 2024\"\n    arxiv_id: \"2402.07712\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Derives analytical formulas for model collapse in high-dimensional regression, revealing modified scaling laws with crossover phenomena in both under- and over-parameterized regimes.\"\n    relevance: \"Provides analytical collapse characterization. Our spectral metrics offer empirical detection aligned with their theory.\"\n\n  - bibtex_key: dohmatob2025strong\n    title: \"Strong Model Collapse\"\n    authors: \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\"\n    year: 2025\n    venue: \"ICLR 2025\"\n    arxiv_id: \"2410.04840\"\n    doi: \"\"\n    category: model_collapse_core\n    verified: true\n    abstract_short: \"Proves that even 1% synthetic data in training corpus leads to model collapse within scaling laws paradigm, using operator-valued free probability theory.\"\n    relevance: \"Strongest theoretical result on collapse inevitability. Motivates need for early detection even with small synthetic contamination.\"\n\n  # ============================================================\n  # Cluster 2: spectral_analysis_collapse (5 papers)\n  # ============================================================\n  - bibtex_key: gu2026sigma\n    title: \"SIGMA: Scalable Spectral Insights for LLM Model Collapse\"\n    authors: \"Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander\"\n    year: 2026\n    venue: \"arXiv\"\n    arxiv_id: \"2601.03385\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Proposes SIGMA framework using spectral bounds of embedding Gram matrix to quantify model collapse, benchmarking on OPT-125M across recursive training generations.\"\n    relevance: \"Most directly related work. Uses spectral analysis for collapse detection. Our contribution extends with EWS methodology and predictive capability.\"\n\n  - bibtex_key: naderi2025mindgap\n    title: \"Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers\"\n    authors: \"Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared\"\n    year: 2025\n    venue: \"ICML 2025\"\n    arxiv_id: \"2410.07799\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Uses Random Matrix Theory to uncover spectral gap between largest singular values as cause of rank collapse in attention, proposing eigenvalue removal as mitigation.\"\n    relevance: \"Provides spectral characterization of rank collapse in transformers. Our work applies similar spectral analysis to detect data-driven collapse.\"\n\n  - bibtex_key: he2025spectral\n    title: \"Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning\"\n    authors: \"He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2509.22335\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Shows Hessian spectral collapse at new-task initialization prevents learning, proposing effective rank regularization and L2 penalties to preserve plasticity.\"\n    relevance: \"Demonstrates spectral collapse as mechanism for plasticity loss. Parallels our finding that spectral signatures predict collapse in recursive training.\"\n\n  - bibtex_key: roy2007effectiverank\n    title: \"The Effective Rank: A Measure of Effective Dimensionality\"\n    authors: \"Roy, Olivier and Vetterli, Martin\"\n    year: 2007\n    venue: \"EUSIPCO 2007\"\n    arxiv_id: \"\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Defines effective rank as exponential of Shannon entropy of normalized singular value distribution, providing continuous measure of matrix dimensionality.\"\n    relevance: \"Foundation metric for our EWS. We track effective rank decline of representation matrices as collapse indicator.\"\n\n  - bibtex_key: martin2021implicit\n    title: \"Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning\"\n    authors: \"Martin, Charles H. and Mahoney, Michael W.\"\n    year: 2021\n    venue: \"JMLR\"\n    arxiv_id: \"1810.01075\"\n    doi: \"\"\n    category: spectral_analysis_collapse\n    verified: true\n    abstract_short: \"Applies RMT to analyze weight matrix spectra in DNNs, identifying implicit self-regularization through heavy-tailed spectral distributions correlated with model quality.\"\n    relevance: \"Establishes spectral analysis of weight matrices as diagnostic tool. Our approach extends to representation matrices under recursive training.\"\n\n  # ============================================================\n  # Cluster 3: data_mixing_strategies (4 papers)\n  # ============================================================\n  - bibtex_key: xie2023doremi\n    title: \"DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining\"\n    authors: \"Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2305.10429\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Uses group DRO on proxy model to optimize domain mixture proportions, improving downstream accuracy by 6.5% and reaching baseline performance with 2.6x fewer steps.\"\n    relevance: \"Establishes data mixing optimization. Our EWS can inform when to adjust mixing ratios during recursive training.\"\n\n  - bibtex_key: ye2025mixinglaws\n    title: \"Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance\"\n    authors: \"Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng\"\n    year: 2025\n    venue: \"ICLR 2025\"\n    arxiv_id: \"2403.16952\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Discovers quantitative data mixing laws predicting model performance from mixture proportions, enabling optimization of 1B model training with 48% fewer steps.\"\n    relevance: \"Provides predictive framework for data mixing. Our spectral EWS complements by detecting when current mixture causes collapse.\"\n\n  - bibtex_key: chen2025aioli\n    title: \"Aioli: A Unified Optimization Framework for Language Model Data Mixing\"\n    authors: \"Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\\\'{e}, Christopher\"\n    year: 2025\n    venue: \"ICLR 2025\"\n    arxiv_id: \"2411.05735\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Unifies existing data mixing methods into common optimization framework, proposing online method that dynamically estimates mixing law parameters during training.\"\n    relevance: \"Online mixing adjustment mechanism. Our EWS provides signal for when to trigger mixture proportion updates.\"\n\n  - bibtex_key: kazdan2024collapsethrive\n    title: \"Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World\"\n    authors: \"Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi\"\n    year: 2024\n    venue: \"arXiv\"\n    arxiv_id: \"2410.16713\"\n    doi: \"\"\n    category: data_mixing_strategies\n    verified: true\n    abstract_short: \"Studies three data workflows (replace/accumulate/fixed-compute) showing collapse only under replacement, with non-trivial real-synthetic data interactions.\"\n    relevance: \"Characterizes when synthetic data helps vs. hurts. Our EWS enables real-time workflow selection based on spectral health.\"\n\n  # ============================================================\n  # Cluster 4: synthetic_data_quality (3 papers)\n  # ============================================================\n  - bibtex_key: gudibande2024falsepromise\n    title: \"The False Promise of Imitating Proprietary LLMs\"\n    authors: \"Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2305.15717\"\n    doi: \"\"\n    category: synthetic_data_quality\n    verified: true\n    abstract_short: \"Shows imitation models trained on proprietary LLM outputs appear fluent but close little capability gap, revealing fundamental quality limitations of synthetic training data.\"\n    relevance: \"Demonstrates quality degradation from synthetic imitation. Our spectral metrics can quantify this capability gap during training.\"\n\n  - bibtex_key: feng2024verification\n    title: \"Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification\"\n    authors: \"Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia\"\n    year: 2024\n    venue: \"arXiv\"\n    arxiv_id: \"2406.07515\"\n    doi: \"\"\n    category: synthetic_data_quality\n    verified: true\n    abstract_short: \"Shows that even imperfect verifiers can prevent model collapse when scaling with synthetic data, providing theoretical conditions for effective verification.\"\n    relevance: \"Verification as collapse prevention. Our EWS serves as a verification signal indicating when synthetic data quality degrades.\"\n\n  - bibtex_key: keisha2025knowledge\n    title: \"Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training\"\n    authors: \"Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip\"\n    year: 2025\n    venue: \"arXiv\"\n    arxiv_id: \"2509.04796\"\n    doi: \"\"\n    category: synthetic_data_quality\n    verified: true\n    abstract_short: \"Defines three-stage knowledge collapse where factual accuracy erodes while fluency persists, creating confidently wrong outputs under recursive synthetic training.\"\n    relevance: \"Identifies knowledge collapse as distinct from perplexity collapse. Our spectral EWS may detect this before factual degradation manifests.\"\n\n  # ============================================================\n  # Cluster 5: early_warning_signals (3 papers)\n  # ============================================================\n  - bibtex_key: scheffer2009ews\n    title: \"Early-warning signals for critical transitions\"\n    authors: \"Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George\"\n    year: 2009\n    venue: \"Nature\"\n    arxiv_id: \"\"\n    doi: \"10.1038/nature08227\"\n    category: early_warning_signals\n    verified: true\n    abstract_short: \"Proposes generic early warning signals (rising variance, autocorrelation, spectral reddening) indicating proximity to critical tipping points in complex systems.\"\n    relevance: \"Foundational EWS theory. We adapt critical slowing down indicators to neural network representation space for collapse detection.\"\n\n  - bibtex_key: bury2021deeplearning\n    title: \"Deep learning for early warning signals of tipping points\"\n    authors: \"Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.\"\n    year: 2021\n    venue: \"PNAS\"\n    arxiv_id: \"\"\n    doi: \"10.1073/pnas.2106140118\"\n    category: early_warning_signals\n    verified: true\n    abstract_short: \"Develops deep learning algorithm for EWS that generalizes across systems, providing higher sensitivity and fewer false positives than generic statistical indicators.\"\n    relevance: \"Demonstrates ML-based EWS for tipping points. Inspires our approach of learning spectral EWS patterns for model collapse detection.\"\n\n  - bibtex_key: dakos2012methods\n    title: \"Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data\"\n    authors: \"Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten\"\n    year: 2012\n    venue: \"PLOS ONE\"\n    arxiv_id: \"\"\n    doi: \"10.1371/journal.pone.0041010\"\n    category: early_warning_signals\n    verified: true\n    abstract_short: \"Comprehensive comparison of metric-based and model-based EWS methods for time series, providing practical toolbox for detecting approaching critical transitions.\"\n    relevance: \"Methodological reference for EWS detection. We adapt their time-series indicators to spectral metric trajectories during training.\"\n"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-17T20:18:22.516462+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-17T20:18:22.516592+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-17T20:18:22.516742+00:00_

1	% References for: Spectral Early Warning Signals for Model Collapse
2	% All entries must be verified before final submission.
3	% Do not add unverified citations.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-17T20:18:22.516885+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib",
  "content": "% References for: Spectral Early Warning Signals for Model Collapse\n% All entries must be verified before final submission.\n% Do not add unverified citations.\n\n% ============================================================\n% Cluster 1: model_collapse_core\n% ============================================================\n\n@article{shumailov2024collapse,\n  title={AI models collapse when trained on recursively generated data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024},\n  doi={10.1038/s41586-024-07566-y}\n}\n\n@inproceedings{dohmatob2024tails,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024mad,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@article{gerstgrasser2024inevitable,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  journal={arXiv preprint arXiv:2404.01413},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024demystified,\n  title={Model Collapse Demystified: The Case of Regression},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  booktitle={Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year={2024}\n}\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={The Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n% ============================================================\n% Cluster 2: spectral_analysis_collapse\n% ============================================================\n\n@article{gu2026sigma,\n  title={{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author={Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal={arXiv preprint arXiv:2601.03385},\n  year={2026}\n}\n\n@inproceedings{naderi2025mindgap,\n  title={Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers},\n  author={Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared},\n  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year={2025}\n}\n\n@inproceedings{he2025spectral,\n  title={Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning},\n  author={He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George},\n  booktitle={Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year={2025}\n}\n\n@inproceedings{roy2007effectiverank,\n  title={The Effective Rank: A Measure of Effective Dimensionality},\n  author={Roy, Olivier and Vetterli, Martin},\n  booktitle={15th European Signal Processing Conference (EUSIPCO)},\n  year={2007}\n}\n\n@article{martin2021implicit,\n  title={Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning},\n  author={Martin, Charles H. and Mahoney, Michael W.},\n  journal={Journal of Machine Learning Research},\n  volume={22},\n  number={165},\n  pages={1--73},\n  year={2021}\n}\n\n% ============================================================\n% Cluster 3: data_mixing_strategies\n% ============================================================\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{ye2025mixinglaws,\n  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},\n  author={Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng},\n  booktitle={The Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{chen2025aioli,\n  title={Aioli: A Unified Optimization Framework for Language Model Data Mixing},\n  author={Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\'{e}, Christopher},\n  booktitle={The Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@article{kazdan2024collapsethrive,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  journal={arXiv preprint arXiv:2410.16713},\n  year={2024}\n}\n\n% ============================================================\n% Cluster 4: synthetic_data_quality\n% ============================================================\n\n@inproceedings{gudibande2024falsepromise,\n  title={The False Promise of Imitating Proprietary {LLMs}},\n  author={Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn},\n  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@article{feng2024verification,\n  title={Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},\n  author={Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia},\n  journal={arXiv preprint arXiv:2406.07515},\n  year={2024}\n}\n\n@article{keisha2025knowledge,\n  title={Knowledge Collapse in {LLMs}: When Fluency Survives but Facts Fail under Recursive Synthetic Training},\n  author={Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  journal={arXiv preprint arXiv:2509.04796},\n  year={2025}\n}\n\n% ============================================================\n% Cluster 5: early_warning_signals\n% ============================================================\n\n@article{scheffer2009ews,\n  title={Early-warning signals for critical transitions},\n  author={Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal={Nature},\n  volume={461},\n  pages={53--59},\n  year={2009},\n  doi={10.1038/nature08227}\n}\n\n@article{bury2021deeplearning,\n  title={Deep learning for early warning signals of tipping points},\n  author={Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={118},\n  number={39},\n  pages={e2106140118},\n  year={2021},\n  doi={10.1073/pnas.2106140118}\n}\n\n@article{dakos2012methods,\n  title={Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data},\n  author={Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten},\n  journal={PLOS ONE},\n  volume={7},\n  number={7},\n  pages={e41010},\n  year={2012},\n  doi={10.1371/journal.pone.0041010}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib",
    "content": "% References for: Spectral Early Warning Signals for Model Collapse\n% All entries must be verified before final submission.\n% Do not add unverified citations.\n\n% ============================================================\n% Cluster 1: model_collapse_core\n% ============================================================\n\n@article{shumailov2024collapse,\n  title={AI models collapse when trained on recursively generated data},\n  author={Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal={Nature},\n  volume={631},\n  pages={755--759},\n  year={2024},\n  doi={10.1038/s41586-024-07566-y}\n}\n\n@inproceedings{dohmatob2024tails,\n  title={A Tale of Tails: Model Collapse as a Change of Scaling Laws},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  booktitle={Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year={2024}\n}\n\n@inproceedings{alemohammad2024mad,\n  title={Self-Consuming Generative Models Go {MAD}},\n  author={Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@article{gerstgrasser2024inevitable,\n  title={Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data},\n  author={Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  journal={arXiv preprint arXiv:2404.01413},\n  year={2024}\n}\n\n@inproceedings{dohmatob2024demystified,\n  title={Model Collapse Demystified: The Case of Regression},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  booktitle={Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year={2024}\n}\n\n@inproceedings{dohmatob2025strong,\n  title={Strong Model Collapse},\n  author={Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle={The Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n% ============================================================\n% Cluster 2: spectral_analysis_collapse\n% ============================================================\n\n@article{gu2026sigma,\n  title={{SIGMA}: Scalable Spectral Insights for {LLM} Model Collapse},\n  author={Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  journal={arXiv preprint arXiv:2601.03385},\n  year={2026}\n}\n\n@inproceedings{naderi2025mindgap,\n  title={Mind the Gap: a Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers},\n  author={Naderi, Alireza and Nait Saada, Thiziri and Tanner, Jared},\n  booktitle={Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year={2025}\n}\n\n@inproceedings{he2025spectral,\n  title={Spectral Collapse Drives Loss of Plasticity in Deep Continual Learning},\n  author={He, Naicheng and Guo, Kaicheng and Prakash, Arjun and Tiwari, Saket and Tao, Ruo Yu and Serapio, Tyrone and Greenwald, Amy and Konidaris, George},\n  booktitle={Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year={2025}\n}\n\n@inproceedings{roy2007effectiverank,\n  title={The Effective Rank: A Measure of Effective Dimensionality},\n  author={Roy, Olivier and Vetterli, Martin},\n  booktitle={15th European Signal Processing Conference (EUSIPCO)},\n  year={2007}\n}\n\n@article{martin2021implicit,\n  title={Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning},\n  author={Martin, Charles H. and Mahoney, Michael W.},\n  journal={Journal of Machine Learning Research},\n  volume={22},\n  number={165},\n  pages={1--73},\n  year={2021}\n}\n\n% ============================================================\n% Cluster 3: data_mixing_strategies\n% ============================================================\n\n@inproceedings{xie2023doremi,\n  title={{DoReMi}: Optimizing Data Mixtures Speeds Up Language Model Pretraining},\n  author={Xie, Sang Michael and Pham, Hieu and Dong, Xuanyi and Du, Nan and Liu, Hanxiao and Lu, Yifeng and Liang, Percy and Le, Quoc V. and Ma, Tengyu and Yu, Adams Wei},\n  booktitle={Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{ye2025mixinglaws,\n  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},\n  author={Ye, Jiasheng and Liu, Peiju and Sun, Tianxiang and Zhan, Jun and Zhou, Yunhua and Qiu, Xipeng},\n  booktitle={The Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@inproceedings{chen2025aioli,\n  title={Aioli: A Unified Optimization Framework for Language Model Data Mixing},\n  author={Chen, Mayee F. and Hu, Michael Y. and Lourie, Nicholas and Cho, Kyunghyun and R\\'{e}, Christopher},\n  booktitle={The Thirteenth International Conference on Learning Representations (ICLR)},\n  year={2025}\n}\n\n@article{kazdan2024collapsethrive,\n  title={Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World},\n  author={Kazdan, Joshua and Schaeffer, Rylan and Dey, Apratim and Gerstgrasser, Matthias and Rafailov, Rafael and Donoho, David L. and Koyejo, Sanmi},\n  journal={arXiv preprint arXiv:2410.16713},\n  year={2024}\n}\n\n% ============================================================\n% Cluster 4: synthetic_data_quality\n% ============================================================\n\n@inproceedings{gudibande2024falsepromise,\n  title={The False Promise of Imitating Proprietary {LLMs}},\n  author={Gudibande, Arnav and Wallace, Eric and Snell, Charlie and Geng, Xinyang and Liu, Hao and Abbeel, Pieter and Levine, Sergey and Song, Dawn},\n  booktitle={The Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024}\n}\n\n@article{feng2024verification,\n  title={Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification},\n  author={Feng, Yunzhen and Dohmatob, Elvis and Yang, Pu and Charton, Francois and Kempe, Julia},\n  journal={arXiv preprint arXiv:2406.07515},\n  year={2024}\n}\n\n@article{keisha2025knowledge,\n  title={Knowledge Collapse in {LLMs}: When Fluency Survives but Facts Fail under Recursive Synthetic Training},\n  author={Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  journal={arXiv preprint arXiv:2509.04796},\n  year={2025}\n}\n\n% ============================================================\n% Cluster 5: early_warning_signals\n% ============================================================\n\n@article{scheffer2009ews,\n  title={Early-warning signals for critical transitions},\n  author={Scheffer, Marten and Bascompte, Jordi and Brock, William A. and Brovkin, Victor and Carpenter, Stephen R. and Dakos, Vasilis and Held, Hermann and van Nes, Egbert H. and Rietkerk, Max and Sugihara, George},\n  journal={Nature},\n  volume={461},\n  pages={53--59},\n  year={2009},\n  doi={10.1038/nature08227}\n}\n\n@article{bury2021deeplearning,\n  title={Deep learning for early warning signals of tipping points},\n  author={Bury, Thomas M. and Sujith, R. I. and Pavithran, Induja and Scheffer, Marten and Lenton, Timothy M. and Anand, Madhur and Bauch, Chris T.},\n  journal={Proceedings of the National Academy of Sciences},\n  volume={118},\n  number={39},\n  pages={e2106140118},\n  year={2021},\n  doi={10.1073/pnas.2106140118}\n}\n\n@article{dakos2012methods,\n  title={Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data},\n  author={Dakos, Vasilis and Carpenter, Stephen R. and Brock, William A. and Ellison, Aaron M. and Guttal, Vishwesha and Ives, Anthony R. and Kefi, Saran and Livina, Vasilis and Seekell, David A. and van Nes, Egbert H. and Scheffer, Marten},\n  journal={PLOS ONE},\n  volume={7},\n  number={7},\n  pages={e41010},\n  year={2012},\n  doi={10.1371/journal.pone.0041010}\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-17T20:18:22.517123+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-17T20:18:22.517281+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:register_artifact,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:register_artifact,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-17T20:18:22.517408+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-17T20:18:22.517529+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "literature_map",
  "type": "data",
  "description": "Literature map with 21 verified papers across 5 clusters: model_collapse_core (6), spectral_analysis_collapse (5), data_mixing_strategies (4), synthetic_data_quality (3), early_warning_signals (3)",
  "project": "spectral_collapse_ews",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml",
  "tags": "['literature', 'references', 'survey']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "literature_map",
    "type": "data",
    "description": "Literature map with 21 verified papers across 5 clusters: model_collapse_core (6), spectral_analysis_collapse (5), data_mixing_strategies (4), synthetic_data_quality (3), early_warning_signals (3)",
    "project": "spectral_collapse_ews",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/literature_map.yaml",
    "tags": "['literature', 'references', 'survey']"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-17T20:18:22.517748+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_0d761c\", \"name\": \"literature_map\", \"type\": \"data\", \"description\": \"Literature map with 21 verified papers across 5 clusters: model_collapse_core (6), spectral_analysis_collapse (5), data_mixing_strategies (4), synthetic_data_quality (3), early_warning_signals (3)\", \"path\": \"projects/spectral_collapse_ews/artifacts/_project/data/literature_map.yaml\", \"url\": null, \"project\": \"spectral_collapse_ews\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T20:18:07.222575+00:00\", \"tags\": [\"literature\", \"references\", \"survey\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-17T20:18:22.517895+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "references_bib",
  "type": "paper",
  "description": "BibTeX file with 21 verified entries for the spectral collapse EWS paper",
  "project": "spectral_collapse_ews",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib",
  "tags": "['bibtex', 'references', 'paper']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260517T201057",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "references_bib",
    "type": "paper",
    "description": "BibTeX file with 21 verified entries for the spectral collapse EWS paper",
    "project": "spectral_collapse_ews",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/paper/references.bib",
    "tags": "['bibtex', 'references', 'paper']"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-17T20:18:22.518034+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260517_7c64e3\", \"name\": \"references_bib\", \"type\": \"paper\", \"description\": \"BibTeX file with 21 verified entries for the spectral collapse EWS paper\", \"path\": \"projects/spectral_collapse_ews/artifacts/_project/paper/references.bib\", \"url\": null, \"project\": \"spectral_collapse_ews\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-17T20:18:08.803908+00:00\", \"tags\": [\"bibtex\", \"references\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_5/projects/spectral_collapse_ews/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260517T201057",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 103 · 2026-05-17T20:18:22.518202+00:00_

文献搜索完成。共 21 篇 verified 论文，分布如下：

| Cluster | 数量 | 关键论文 |
|---------|------|---------|
| **model_collapse_core** | 6 | Shumailov 2024 Nature, Dohmatob 2024 ICML/NeurIPS, Alemohammad 2024 ICLR, Gerstgrasser 2024, Dohmatob 2025 ICLR |
| **spectral_analysis_collapse** | 5 | Gu 2026 SIGMA, Naderi 2025 ICML, He 2025 NeurIPS, Roy 2007 effective rank, Martin 2021 JMLR |
| **data_mixing_strategies** | 4 | Xie 2023 DoReMi, Ye 2025 ICLR, Chen 2025 AIOLI, Kazdan 2024 |
| **synthetic_data_quality** | 3 | Gudibande 2024 ICLR, Feng 2024 verification, Keisha 2025 knowledge collapse |
| **early_warning_signals** | 3 | Scheffer 2009 Nature, Bury 2021 PNAS, Dakos 2012 PLOS ONE |

输出文件：
- `literature_map.yaml` -- 完整论文元数据（title, authors, venue, arxiv_id, category, relevance）
- `paper/references.bib` -- 21 条 BibTeX 条目

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260517T201057"
}
```

</details>

---
