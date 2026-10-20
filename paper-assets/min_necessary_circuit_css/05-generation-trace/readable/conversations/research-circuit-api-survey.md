# research circuit api survey

**Transformer Model EAP-IG** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_research_circuit-api-survey_20260512T095923.jsonl`
- **Structured JSON:** [`55b12518db9a3c28073c.json`](../../sessions/55/55b12518db9a3c28073c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-12T10:03:41.001597+00:00_

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
  "session": "worker_research_circuit-api-survey_20260512T095923",
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

_source line 2 · 2026-05-12T10:03:41.002034+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-12T10:03:41.002249+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TransformerLens PyPI latest version 2025 2026 install HookedTransformer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TransformerLens PyPI latest version 2025 2026 install HookedTransformer"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T10:03:41.002396+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EAP-IG Edge Attribution Patching Integrated Gradients GitHub implementation TransformerLens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EAP-IG Edge Attribution Patching Integrated Gradients GitHub implementation TransformerLens"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-12T10:03:41.002594+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AtP* Attribution Patching Kramár 2024 GitHub implementation code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AtP* Attribution Patching Kramár 2024 GitHub implementation code"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-12T10:03:41.002774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "stevenxcao edge-pruning GitHub NeurIPS 2024 nnsight"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "stevenxcao edge-pruning GitHub NeurIPS 2024 nnsight"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-12T10:03:41.002913+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ArthurConmy Automatic-Circuit-Discovery ACDC GitHub install API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ArthurConmy Automatic-Circuit-Discovery ACDC GitHub install API"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-12T10:03:41.003043+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS config-bagging circuit stability arXiv 2603.00523 GitHub code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS config-bagging circuit stability arXiv 2603.00523 GitHub code"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T10:03:41.003170+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MIB benchmark mechanistic interpretability arXiv 2504.13151 GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MIB benchmark mechanistic interpretability arXiv 2504.13151 GitHub"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T10:03:41.003351+00:00_

Web search results for query: "TransformerLens PyPI latest version 2025 2026 install HookedTransformer"

Links: [{"title":"transformer-lens · PyPI","url":"https://pypi.org/project/transformer-lens/"},{"title":"transformer_lens.HookedTransformer - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.HookedTransformer.html"},{"title":"GitHub - TransformerLensOrg/TransformerLens: A library for mechanistic interpretability of GPT-style language models · GitHub","url":"https://github.com/TransformerLensOrg/TransformerLens"},{"title":"TransformerLens/transformer_lens/HookedTransformer.py at main · TransformerLensOrg/TransformerLens","url":"https://github.com/TransformerLensOrg/TransformerLens/blob/main/transformer_lens/HookedTransformer.py"},{"title":"transformer_lens.HookedTransformerConfig - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.HookedTransformerConfig.html"},{"title":"How-to Transformer Mechanistic Interpretability—in 50 ...","url":"https://www.lesswrong.com/posts/hnzHrdqn3nrjveayv/how-to-transformer-mechanistic-interpretability-in-50-lines"},{"title":"Client Challenge","url":"https://pypi.org/project/transformer-lens/1.1.1/"},{"title":"piwheels - transformer-lens","url":"https://www.piwheels.org/project/transformer-lens/"},{"title":"TransformerLens Quick Reference – BorisTheBrave.Com","url":"https://www.boristhebrave.com/2025/03/29/transformerlens-quick-reference/"},{"title":"Transformer Lens Main Demo Notebook - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/demos/Main_Demo.html"}]

Based on the search results, here's what I found about TransformerLens on PyPI:

## Overview
TransformerLens lets you load in 50+ different open source language models, and exposes the internal activations of the model to you. You can cache any internal activation in the model, and a
…[truncated 1284 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T10:03:41.003571+00:00_

Web search results for query: "stevenxcao edge-pruning GitHub NeurIPS 2024 nnsight"

Links: [{"title":"GitHub - princeton-nlp/Edge-Pruning: [NeurIPS 2024 Spotlight] Code and data for the paper \"Finding Transformer Circuits with Edge Pruning\".","url":"https://github.com/princeton-nlp/edge-pruning"},{"title":"GitHub - RelationalML/SpectralPruningBraess: Codebase for \"Spectral Graph Pruning Against Over-squashing and Over-smoothing\" (NeurIPS 2024)","url":"https://github.com/RelationalML/SpectralPruningBraess"},{"title":"NeurIPS Poster Finding Transformer Circuits With Edge Pruning","url":"https://neurips.cc/virtual/2024/poster/96350"},{"title":"neural-network-pruning · GitHub Topics · GitHub","url":"https://github.com/topics/neural-network-pruning"},{"title":"GitHub - BaiTheBest/SparseLLM: Official Repo for SparseLLM: Global Pruning of LLMs (NeurIPS 2024)","url":"https://github.com/baithebest/sparsellm"},{"title":"neurips-2024 · GitHub Topics · GitHub","url":"https://github.com/topics/neurips-2024"},{"title":"Machine Learning and the Physical Sciences, NeurIPS 2024","url":"https://ml4physicalsciences.github.io/2024/"},{"title":"Highlights of NeurIPS 2023 from Reading All 3584 Abstracts | Alex L. Zhang","url":"https://alexzhang13.github.io/blog/2024/neurips2023/"},{"title":"GitHub - Persdre/NeurIPS-2024-LLM-Papers: Accepted LLM Papers in NeurIPS 2024 · GitHub","url":"https://github.com/Persdre/NeurIPS-2024-LLM-Papers"},{"title":"GitHub - he-y/Awesome-Pruning: A curated list of neural network pruning resources. · GitHub","url":"https://github.com/he-y/Awesome-Pruning"}]

Based on the search results, I found information about the Edge-Pruning project from NeurIPS 2024:

This is a NeurIPS 2024 Spotlight paper titled "Finding Transformer Circuits with Edge Pruning". The GitHub repository is located at princeton-nlp/Edge-Pruning.

Edge Pruning leverages gradient-based pruning techniques, but instead of removing neurons or components, prunes the edges between components.

…[truncated 612 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T10:03:41.003812+00:00_

Web search results for query: "AtP* Attribution Patching Kramár 2024 GitHub implementation code"

Links: [{"title":"GitHub - koayon/atp_star: PyTorch and NNsight implementation of AtP* (Kramar et al 2024, DeepMind)","url":"https://github.com/koayon/atp_star"},{"title":"[2403.00745] AtP*: An efficient and scalable method for localizing LLM behaviour to components","url":"https://arxiv.org/abs/2403.00745"},{"title":"János Kramár on X: \"New @GoogleDeepmind mech interp research! 🎉https://t.co/eB9aeBL05b Can we massively speed up the process of finding important nodes in LLMs? Yes! Introducing AtP*, an improved variant of Attribution Patching (AtP) that beats all our baselines on efficiency and effectiveness. 🧵 https://t.co/aThAaGhW41\" / X","url":"https://x.com/JanosKramar/status/1764657270263046567"},{"title":"Attribution Patching for NN Interpretability","url":"https://www.emergentmind.com/topics/attribution-patching-atp"},{"title":"AtP^*: An efficient and scalable method for localizing LLM behaviour to components","url":"https://arxiv.org/html/2403.00745v1"},{"title":"@gsarti on Hugging Face: \"🔍 Today's pick in Interpretability & Analysis of LMs: AtP*: An efficient and…\"","url":"https://huggingface.co/posts/gsarti/409511202209405"},{"title":"Part 4: Challenges and Future Work","url":"https://ziyu-yao-nlp-lab.github.io/ICML25-MI-Tutorial.github.io/static/other_assets/presentation-main-final-part4.pdf"},{"title":"How to use and interpret activation patching","url":"https://arxiv.org/html/2404.15255v1"},{"title":"GitHub - Aaquib111/edge-attribution-patching: Code for my NeurIPS 2024 ATTRIB paper titled \"Attribution Patching Outperforms Automated Circuit Discovery\" · GitHub","url":"https://github.com/Aaquib111/edge-attribution-patching"},{"title":"GitHub - interpretingdl/eacl2024_transformer_interpretability_tutorial: Materials for EACL2024 tutorial: Transformer-specific Interpretability · GitHub","url":"https://github.com/interpretingdl/eacl2024_transformer_interpr
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T10:03:41.004061+00:00_

Web search results for query: "EAP-IG Edge Attribution Patching Integrated Gradients GitHub implementation TransformerLens"

Links: [{"title":"GitHub - hannamw/EAP-IG · GitHub","url":"https://github.com/hannamw/eap-ig"},{"title":"Edge Attribution Patching (EAP)","url":"https://www.emergentmind.com/topics/edge-attribution-patching-eap"},{"title":"Going Beyond Circuit Overlap When Finding Model ...","url":"https://hannamw.github.io/preprints-posters/mech_interp_workshop_poster.pdf"},{"title":"GitHub - Aaquib111/edge-attribution-patching: Code for my NeurIPS 2024 ATTRIB paper titled \"Attribution Patching Outperforms Automated Circuit Discovery\" · GitHub","url":"https://github.com/Aaquib111/edge-attribution-patching"},{"title":"GitHub - TransformerLensOrg/TransformerLens: A library for mechanistic interpretability of GPT-style language models · GitHub","url":"https://github.com/TransformerLensOrg/TransformerLens"},{"title":"Have Faith in Faithfulness: Going Beyond Circuit Overlap When Finding Model","url":"https://openreview.net/pdf?id=grXgesr5dT"},{"title":"Tutorials - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/content/tutorials.html"},{"title":"@gsarti on Hugging Face: \"🔍 Today's pick in Interpretability & Analysis of LMs: Have Faith in…\"","url":"https://huggingface.co/posts/gsarti/292464465490361"},{"title":"GitHub - FarnoushRJ/RelP: [NeurIPS 2025 MechInterp Workshop - Spotlight] Official implementation of the paper \"RelP: Faithful and Efficient Circuit Discovery in Language Models via Relevance Patching\" · GitHub","url":"https://github.com/FarnoushRJ/RelP"},{"title":"Attribution Patching Outperforms Automated Circuit Discovery","url":"https://www.researchgate.net/publication/386190657_Attribution_Patching_Outperforms_Automated_Circuit_Discovery"}]

Based on the search results, I found comprehensive information about EAP-IG and its GitHub implementation:

## Edge Attribution Patching with Integrated Gradients (EAP
…[truncated 1490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T10:03:41.004283+00:00_

Web search results for query: "ArthurConmy Automatic-Circuit-Discovery ACDC GitHub install API"

Links: [{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"Automatic circuit discovery | Arthur’s Site","url":"https://arthurconmy.github.io/automatic_circuit_discovery/"},{"title":"Automatic-Circuit-Discovery/acdc/ioi/utils.py at main · ArthurConmy/Automatic-Circuit-Discovery","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/acdc/ioi/utils.py"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery/tree/main"},{"title":"Automatic-Circuit-Discovery/README.md at main · ArthurConmy/Automatic-Circuit-Discovery","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/README.md"},{"title":"[2304.14997] Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://arxiv.org/abs/2304.14997"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability | OpenReview","url":"https://openreview.net/forum?id=89ia77nZ8u"},{"title":"Towards Automated Circuit Discovery for Mechanistic Interpretability","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/34e1dbe95d34d7ebaf99b9bcaeb5b2be-Abstract-Conference.html"},{"title":"ACDC_Main_Demo.ipynb - Colaboratory","url":"https://colab.research.google.com/github/ArthurConmy/Automatic-Circuit-Discovery/blob/main/notebooks/colabs/ACDC_Main_Demo.ipynb"},{"title":"Towards automated circuit discovery for mechanistic interpretability | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3666841"}]

Based on the search results, here's information about the ArthurConmy ACDC (Automatic Circuit Discovery) repository:

## Project Overview

This is the accompanying code to the paper "Towards Automated Circu
…[truncated 1142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-12T10:03:41.004488+00:00_

Web search results for query: "MIB benchmark mechanistic interpretability arXiv 2504.13151 GitHub"

Links: [{"title":"[2504.13151] MIB: A Mechanistic Interpretability Benchmark","url":"https://arxiv.org/abs/2504.13151"},{"title":"GitHub - aaronmueller/MIB: Landing page for MIB: A Mechanistic Interpretability Benchmark · GitHub","url":"https://github.com/aaronmueller/MIB"},{"title":"MIB: A Mechanistic Interpretability Benchmark","url":"https://arxiv.org/html/2504.13151v1"},{"title":"MIB: A Mechanistic Interpretability Benchmark - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250413151M/abstract"},{"title":"[2504.13151v1] MIB: A Mechanistic Interpretability Benchmark","url":"https://arxiv.org/abs/2504.13151v1"},{"title":"MIB – Project Page","url":"https://mib-bench.github.io/"},{"title":"MIB: A Mechanistic Interpretability Benchmark | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.13151v2"},{"title":"MIB: A Mechanistic Interpretability Benchmark | OpenReview","url":"https://openreview.net/forum?id=sSrOwve6vb"},{"title":"mib-bench (Mechanistic Interpretability Benchmark)","url":"https://huggingface.co/mib-bench"},{"title":"BlackboxNLP-2025 MIB Shared Task: Improving Circuit Faithfulness via Better Edge Selection","url":"https://arxiv.org/html/2510.25786v1"}]

Based on the search results, here's what I found about MIB (Mechanistic Interpretability Benchmark) with arXiv identifier 2504.13151:

## Overview

MIB is a Mechanistic Interpretability Benchmark with two tracks spanning four tasks and five models. MIB favors methods that precisely and concisely recover relevant causal pathways or causal variables in neural language models.

## Two Tracks

The benchmark consists of two main evaluation tracks:

1. **Circuit Localization Track**: This compares methods that locate the model components - and connections between them - most important for performing a task (e.g., attribution patching or information flow routes).

2. **Causal Variable Localization Track
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T10:03:41.004717+00:00_

Web search results for query: "CIRCUS config-bagging circuit stability arXiv 2603.00523 GitHub code"

Links: [{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523"},{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"Bagging Provides Assumption-free Stability","url":"https://arxiv.org/pdf/2301.12600"},{"title":"Bagging Provides Assumption-free Stability","url":"https://www.aimodels.fyi/papers/arxiv/bagging-provides-assumption-free-stability"},{"title":"[2301.12600] Bagging Provides Assumption-free Stability","url":"https://arxiv.org/abs/2301.12600"},{"title":"Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/html/2505.24731v1"},{"title":"[2603.19840] Explainable cluster analysis: a bagging approach","url":"https://arxiv.org/abs/2603.19840"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=202&show=2000"},{"title":"[2301.12600v2] Bagging Provides Assumption-free Stability","url":"https://arxiv.org/abs/2301.12600v2"},{"title":"[2505.24731] Circuit Stability Characterizes Language Model Generalization","url":"https://arxiv.org/abs/2505.24731"}]

Great! I found detailed information about the paper. Here are the key findings:

## CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles

The paper is authored by Swapnil Parekh and was submitted on February 28, 2026 to arXiv.

### Overview
Mechanistic circuit discovery is notoriously sensitive to arbitrary analyst choices, especially pruning thresholds and feature dictionaries, and the method reframes circuit discovery as an uncertainty-quantification problem over these analytic degrees of freedom.

### Method
The method adapts stability selection, replacing data subsampling with config-bagging over pruning thresholds. CIRCUS constructs an ensemble of attribution graphs by pruning a single raw
…[truncated 1156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T10:03:41.004932+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/transformer-lens/",
  "prompt": "Extract: latest version number, Python version requirements, torch version requirements, install command, and key dependencies listed"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/transformer-lens/",
    "prompt": "Extract: latest version number, Python version requirements, torch version requirements, install command, and key dependencies listed"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-12T10:03:41.005088+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/hannamw/eap-ig",
  "prompt": "Extract: README content including installation instructions, API usage examples, key functions, dependencies, how to run EAP-IG, output format, and any code snippets showing how to use the library"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/hannamw/eap-ig",
    "prompt": "Extract: README content including installation instructions, API usage examples, key functions, dependencies, how to run EAP-IG, output format, and any code snippets showing how to use the library"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T10:03:41.005230+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/koayon/atp_star",
  "prompt": "Extract: README content including installation instructions, API usage examples, key functions, dependencies (nnsight, TransformerLens, torch), and output format. Include any code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/koayon/atp_star",
    "prompt": "Extract: README content including installation instructions, API usage examples, key functions, dependencies (nnsight, TransformerLens, torch), and output format. Include any code snippets."
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-12T10:03:41.005403+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/princeton-nlp/edge-pruning",
  "prompt": "Extract: README content including installation instructions, dependencies (nnsight version, torch version), API usage, how to run edge pruning, key scripts, model support, and output format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/princeton-nlp/edge-pruning",
    "prompt": "Extract: README content including installation instructions, dependencies (nnsight version, torch version), API usage, how to run edge pruning, key scripts, model support, and output format"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-12T10:03:41.005554+00:00_

# TransformerLens Package Information

**Latest Version:** 3.2.1 (released May 9, 2026)

**Python Requirements:** "Python <4.0, >=3.10"

**Install Command:** 
```
pip install transformer-lens
```

**Torch Version Requirements:** Not explicitly listed on this PyPI page

**Key Dependencies:** The page does not provide a detailed dependency list, though it mentions optional extras for `evals` and `lit`. The library is described as "An implementation of transformers tailored for mechanistic interpretability" that works with 50+ language model architectures.

**Note:** For Python 3.8 or 3.9 users, the documentation specifies an alternative installation: `pip install 'transformer-lens~=2.0'`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-12T10:03:41.005717+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/ArthurConmy/Automatic-Circuit-Discovery",
  "prompt": "Extract: README content including installation instructions, dependencies (TransformerLens version, torch), API usage examples, how to run ACDC, IOI task example, key files, and output format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/ArthurConmy/Automatic-Circuit-Discovery",
    "prompt": "Extract: README content including installation instructions, dependencies (TransformerLens version, torch), API usage examples, how to run ACDC, IOI task example, key files, and output format"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T10:03:41.005859+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/aaronmueller/MIB",
  "prompt": "Extract: README content including installation, evaluation framework, supported methods, how to evaluate circuit discovery methods, datasets, models supported, and any standard evaluation API"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/aaronmueller/MIB",
    "prompt": "Extract: README content including installation, evaluation framework, supported methods, how to evaluate circuit discovery methods, datasets, models supported, and any standard evaluation API"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-12T10:03:41.006001+00:00_

# AtP* Repository Summary

## Overview
This GitHub repository contains an unofficial implementation of the AtP* algorithm from Kramar et al. 2024 (DeepMind). The project focuses on "Improved Attribution Patching for Localizing Large Model Behaviour."

## Key Concepts
**Attribution Patching** is described as "a quick approximation to the more precise _Activation Patching_ which details the contribution of each component to some metric." The method uses first-order Taylor approximation for computing component contributions.

## Core Dependencies
The implementation relies on:
- **PyTorch** - for deep learning operations
- **NNsight** - described as used for "caching and interventions"
- **TransformerLens** - (inferred from project context)

## Available Files
The repository includes:
- `atp.py` - main algorithm implementation
- `interventions.py` - intervention mechanisms
- `helpers.py` - utility functions
- `main.py` - entry point
- `plot.py` - visualization tools
- `prompt_store.py` - prompt management

## Development Status
The project checklist indicates completed items including core AtP and QK-Fix implementations, with ongoing work on GPU optimization, circuit-finding algorithms, and experimental validation.

**Note:** The README content shown does not include explicit installation instructions or API usage examples in the extracted material.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-12T10:03:41.006159+00:00_

# EAP-IG Library: Installation and Usage Guide

## Overview
EAP-IG is a Python library for identifying circuits in autoregressive transformer language models. A circuit represents the subset of model components responsible for specific tasks.

## Installation

**Basic installation:**
```bash
pip install .
```

**With visualization support:**
```bash
pip install .[viz]
```

**Graphviz setup (required for visualization):**

MacOS:
```bash
brew install graphviz
export CFLAGS="-I$(brew --prefix graphviz)/include"
export LDFLAGS="-L$(brew --prefix graphviz)/lib"
pip install .
```

Ubuntu:
```bash
apt-get update
apt-get install -y graphviz libgraphviz-dev build-essential
```

## Core Usage Pipeline

The circuit-finding workflow involves four main steps:

1. **Define a task** with clean/corrupted inputs, labels, and performance metrics
   ```
   dataloader = EAPDataset('greater-than').to_dataloader()
   metric = [your metric]
   ```

2. **Create computational graph** representing model architecture
   ```
   graph = Graph.from_model(model)
   ```

3. **Calculate attribution scores** using an attribution method
   ```
   attribute(model, graph, dataloader, metric, method='EAP-IG-inputs', ig_steps=5)
   ```

4. **Extract and evaluate circuit** by selecting top-ranked components
   ```
   graph.apply_topn(n)
   results = evaluate_graph(model, graph, dataloader, metric)
   ```

## Attribution Methods

The library supports multiple scoring approaches:
- **EAP**: First-order approximation (O(1) complexity)
- **EAP-IG (inputs)**: Integrated gradients over interpolated embeddings
- **EAP-IG (activations)**: Integrated gradients over component activations
- **Clean-Corrupted**: Gradient computation at two points

## Model Compatibility

Compatible with TransformerLens autoregressive models including GPT-2, Pythia, Mistral, Llama, and Gemma. Requires pre-LayerNorm architecture. Grouped Query Attention models need ungrouping via `model.cfg.ungroup_grouped_query_attention = True`.

##
…[truncated 191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-12T10:03:41.006332+00:00_

# ACDC: Automatic Circuit Discovery - Key Information

## Overview
This repository contains code for the paper "Towards Automated Circuit Discovery for Mechanistic Interpretability" (NeurIPS 2023 Spotlight). The project focuses on automatically discovering circuits in neural networks.

## Installation

**System Dependencies:**
- Ubuntu Linux: `sudo apt-get install libgl1-mesa-glx graphviz build-essential graphviz-dev`
- Mac OS X: `brew install graphviz` plus environment variable configuration for Graphviz paths

**Python Setup:**
```
git clone https://github.com/ArthurConmy/Automatic-Circuit-Discovery.git
cd Automatic-Circuit-Discovery
poetry env use 3.10
poetry install
```
Requirements: Python 3.8+ and Poetry package manager

## Key Dependencies
- **TransformerLens**: The codebase builds on abstractions like `HookPoint`s and standardized `HookedTransformer`s from this library
- Supports Python 3.8+ (3.10 recommended)

## Primary Entry Points

1. **Main ACDC execution**: `acdc/main.py` with accompanying Colab notebook
2. **Edge editing**: `notebooks/editing_edges.py` demonstrating computational graph modifications
3. **Implementation details**: `notebooks/implementation_demo.py` for low-level editable graph concepts

## Testing
```
pytest -vvv -m "not slow"        # Standard tests
pytest -s -m slow                # Comprehensive tests
```

## Repository Structure
- `acdc/` - Core implementation
- `experiments/` - Reproducibility scripts and result generation
- `notebooks/` - Tutorial and demo notebooks
- `subnetwork_probing/` - Additional probing methodology

## License
MIT License

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T10:03:41.006485+00:00_

# Edge Pruning: Installation and Usage Guide

## Installation

After installing PyTorch, install dependencies with:
```bash
pip install -r requirements.txt
```

**Note:** For GPT-2 circuits with newer transformer versions, use `requirements-experimental.txt` instead.

## Key Dependencies

The README doesn't explicitly list version requirements for specific packages like nnsight or torch. Users should refer to the `requirements.txt` and `requirements-experimental.txt` files for exact dependency specifications.

## Core Concept

The method expands hidden state tensors and employs binary masks for edge pruning. As noted: *"masks and their optimization are implemented with the L0 trick"* using floating-point values that are later discretized to 0 or 1 through threshold-based rounding.

## Main Scripts by Model Type

**GPT-2 Experiments:**
- Pruning: `src/prune/fpt2_{ioi/gt/gp}.py`
- Evaluation: `src/eval/{ioi/gt/gp}.py`
- Visualization: `src/modeling/vis_fpt2.py` and `draw_fpt2.py`

**Tracr Experiments:**
- Pruning: `src/prune/erazr_{reverse/xproportion}.py`
- Modeling: `src/modeling/modeling_erazr.py`

**CodeLlama:**
- Pruning: `src/prune/fllama_boolean_expressions_{fs/ip}.py`
- Evaluation: `src/eval/boolean_expressions.py`

## Output Format

Evaluation produces circuit edge data (saved as JSON) for visualization and analysis of discovered transformer circuits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-12T10:03:41.006649+00:00_

# MIB: Mechanistic Interpretability Benchmark

## Overview

MIB is a comprehensive benchmark for comparing featurization and localization methods in neural networks, featuring two distinct tracks with corresponding codebases and evaluation frameworks.

## Two Tracks

**Circuit Localization Track**
This track evaluates methods for discovering "graphs of causal dependencies in neural networks." The pipeline involves computing importance scores, ablating components below thresholds, and evaluating circuit performance against two separate criteria: how well circuits perform independently versus how effectively they replicate full model behavior.

**Causal Variable Localization Track**
This track assesses featurization approaches—transforming model activations to isolate specific causal variables. The methodology includes curating contrastive datasets, training featurizers (when applicable), and evaluating through intervention experiments in transformed spaces.

## Datasets and Models

The benchmark encompasses five datasets representing varied complexity levels: IOI, MCQA, Arithmetic, ARC, and RAVEL. Each includes train, validation, public test, and private test sets.

Four language models standardize comparisons: "GPT-2 Small, Qwen-2.5 (0.5B), Gemma-2 (2B), Llama-3.1 (8B)." An InterpBench model with ground-truth circuit encoding enables meaningful metrics like AUROC calculation.

## Submission Requirements

- **Circuit track**: 9 circuits per model/task combination in specified formats
- **Causal variable track**: featurization function, token position function, and trained featurizer files

Rate limits restrict submissions to "2 submission per user per week" on the private test set.

## Citation

Mueller et al., 2025, arXiv:2504.13151

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-12T10:03:41.006864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UFO-101 Auto-Circuit GitHub library circuit discovery TransformerLens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UFO-101 Auto-Circuit GitHub library circuit discovery TransformerLens"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T10:03:41.007000+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TransformerLens ioi_dataset IOI dataset API transformer_lens.rs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TransformerLens ioi_dataset IOI dataset API transformer_lens.rs"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T10:03:41.007128+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CIRCUS arXiv 2603.00523 Swapnil Parekh GitHub code release implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CIRCUS arXiv 2603.00523 Swapnil Parekh GitHub code release implementation"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-12T10:03:41.007254+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/princeton-nlp/edge-pruning/blob/main/requirements.txt",
  "prompt": "List all dependencies and their version constraints from the requirements.txt file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/princeton-nlp/edge-pruning/blob/main/requirements.txt",
    "prompt": "List all dependencies and their version constraints from the requirements.txt file"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-12T10:03:41.007390+00:00_

# Dependencies from Edge-Pruning requirements.txt

The project lists 19 dependencies with specific version constraints:

| Package | Version |
|---------|---------|
| absl-py | 2.1.0 |
| accelerate | 1.2.1 |
| acdc | 0.1.1 |
| chex | 0.1.89 |
| datasets | 3.2.0 |
| einops | 0.8.1 |
| evaluate | 0.4.3 |
| flash-attn | 2.7.2.post1 |
| graphviz | 0.20.3 |
| haiku | 0.01 |
| jax | 0.5.2 |
| networkx | 3.4.2 |
| numpy | 2.2.3 |
| scipy | 1.15.2 |
| tensorflow | 2.18.0 |
| torch | 2.5.1+cu121 |
| tqdm | 4.67.1 |
| transformer-lens | 2.15.0 |
| typing-extensions | 4.12.2 |

The dependencies span machine learning frameworks (PyTorch, TensorFlow, JAX), scientific computing libraries, neural network utilities, and development tools. All versions are pinned to specific releases without flexible version ranges.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-12T10:03:41.007566+00:00_

Web search results for query: "TransformerLens ioi_dataset IOI dataset API transformer_lens.rs"

Links: [{"title":"transformer_lens.evals - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.evals.html"},{"title":"transformer-lens-interpretability","url":"https://lobehub.com/skills/47thstreet-clawdagent-transformer-lens"},{"title":"Dataset API — small-text documentation","url":"https://small-text.readthedocs.io/en/latest/api/dataset.html"},{"title":"transformer_lens.utils - TransformerLens Documentation","url":"https://transformerlensorg.github.io/TransformerLens/generated/code/transformer_lens.utils.html"},{"title":"transformer-lens-interpretability - Agent Skill by zechenzhangagi/ai-research-skills","url":"https://agentskills.so/skills/zechenzhangagi-ai-research-skills-transformer-lens-interpretability"},{"title":"GitHub - redwoodresearch/Easy-Transformer","url":"https://github.com/redwoodresearch/easy-transformer"},{"title":"GitHub - amakelov/activation-patching-illusion: Code for \"Is This the Subspace You Are Looking for? An Interpretability Illusion for Subspace Activation Patching\" · GitHub","url":"https://github.com/amakelov/activation-patching-illusion"},{"title":"transformer-lens skill by orchestra-research/ai-research-skills","url":"https://playbooks.com/skills/orchestra-research/ai-research-skills/transformer-lens"},{"title":"Updated quickstart guide for mechanistic interpretability | Apart Research","url":"https://apartresearch.com/news/updated-quickstart-guide-for-mechanistic-interpretability"},{"title":"Easy-Transformer/easy_transformer/ioi_dataset.py at main · redwoodresearch/Easy-Transformer","url":"https://github.com/redwoodresearch/Easy-Transformer/blob/main/easy_transformer/ioi_dataset.py"}]

Based on the search results, here's information about TransformerLens's IOI dataset API:

## IOIDataset API Overview

IOIDataset is a dataset class for Indirect Object Identification ta
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-12T10:03:41.007774+00:00_

Web search results for query: "CIRCUS arXiv 2603.00523 Swapnil Parekh GitHub code release implementation"

Links: [{"title":"[2603.00523] CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/abs/2603.00523"},{"title":"CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles","url":"https://arxiv.org/html/2603.00523v2"},{"title":"Swapnil Parekh – AI","url":"https://swapnilparekh.github.io/"},{"title":"GitHub - midas-research/interpreting-AES-Integrated-Gradients · GitHub","url":"https://github.com/midas-research/interpreting-AES-Integrated-Gradients"},{"title":"[2603.03359] ACES: Accent Subspaces for Coupling, Explanations, and Stress-Testing in Automatic Speech Recognition","url":"https://arxiv.org/abs/2603.03359"},{"title":"GitHub - zhjohnchan/arXiv-text-generation-papers: A curated list of text generation papers in arXiv. · GitHub","url":"https://github.com/zhjohnchan/arXiv-text-generation-papers"},{"title":"[2603.20415] The Nature of Technical Debt in Research Software","url":"https://arxiv.org/abs/2603.20415"},{"title":"Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs","url":"https://arxiv.org/html/2603.24511v1"},{"title":"[2604.00770] Thinking Wrong in Silence: Backdoor Attacks on Continuous Latent Reasoning","url":"https://arxiv.org/abs/2604.00770"},{"title":"GitHub - swapnil-saxena/address-parser: This repository contains an implementation of a US address parser built using spaCy NLP library.","url":"https://github.com/swapnil-saxena/address-parser"}]

Based on the search results, I found information about the CIRCUS paper:

CIRCUS: Circuit Consensus under Uncertainty via Stability Ensembles is authored by Swapnil Parekh and addresses the sensitivity of mechanistic circuit discovery to arbitrary analyst choices. 

The CIRCUS method constructs an ensemble of attribution graphs by pruning a single raw attribution run under multiple configurations, assigns each edge a sta
…[truncated 735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-12T10:03:41.007973+00:00_

Web search results for query: "UFO-101 Auto-Circuit GitHub library circuit discovery TransformerLens"

Links: [{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery · GitHub","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery"},{"title":"GitHub - UFO-101/auto-circuit: A library for efficient patching and automatic circuit discovery. · GitHub","url":"https://github.com/UFO-101/auto-circuit"},{"title":"UFO-101 - Overview","url":"https://github.com/UFO-101"},{"title":"GitHub - ArthurConmy/Automatic-Circuit-Discovery","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery/tree/main"},{"title":"AutoCircuit","url":"https://ufo-101.github.io/auto-circuit/"},{"title":"1) Getting Started - AutoCircuit","url":"https://ufo-101.github.io/auto-circuit/guides/1)_Getting_Started/"},{"title":"auto-circuit/README.md at main · UFO-101/auto-circuit","url":"https://github.com/UFO-101/auto-circuit/blob/main/README.md"},{"title":"Automatic-Circuit-Discovery/README.md at main · ArthurConmy/Automatic-Circuit-Discovery","url":"https://github.com/ArthurConmy/Automatic-Circuit-Discovery/blob/main/README.md"},{"title":"auto-circuit · PyPI","url":"https://pypi.org/project/auto-circuit/"},{"title":"Requires my fork of TransformerLens (https://github.com/UFO-101/TransformerLens) - until this change is released in the main package: https://github.com/TransformerLensOrg/TransformerLens/pull/699 · GitHub","url":"https://gist.github.com/UFO-101/41b7ff0b250babe69bf16071e76658a6"}]

Based on the search results, here's what I found:

The auto-circuit library by UFO-101 is described as "a library for efficient patching and automatic circuit discovery." It requires Python >=3.10 and <4.0.

The library appears to be an improved alternative to an earlier project. The ACDC (Automatic Circuit Discovery) codebase recommends using the Auto Circuit library by @UFO-101 instead, noting that the ACDC codebase has "many sharp edges."

The ACDC library builds upon abstractions (HookPoin
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-12T10:03:41.008165+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/UFO-101/auto-circuit",
  "prompt": "Extract: README content including installation, dependencies, key API functions, supported methods (ACDC, EAP, Edge Pruning, etc.), model support, output format, and code examples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/UFO-101/auto-circuit",
    "prompt": "Extract: README content including installation, dependencies, key API functions, supported methods (ACDC, EAP, Edge Pruning, etc.), model support, output format, and code examples"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-12T10:03:41.008305+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pypi.org/project/auto-circuit/",
  "prompt": "Extract: latest version, Python version requirement, torch requirement, all dependencies, and install command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pypi.org/project/auto-circuit/",
    "prompt": "Extract: latest version, Python version requirement, torch requirement, all dependencies, and install command"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T10:03:41.008442+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.00523",
  "prompt": "Extract: whether there is a link to code/GitHub repository, and the exact config-bagging algorithm description (B parameter, threshold selection, stability score formula)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2603.00523",
    "prompt": "Extract: whether there is a link to code/GitHub repository, and the exact config-bagging algorithm description (B parameter, threshold selection, stability score formula)"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T10:03:41.008577+00:00_

I cannot extract the requested information from the provided content. The webpage displays only an error message: "A required part of this site couldn't load. This may be due to a browser extension, network issues, or browser settings."

The page does not contain any details about:
- Latest version numbers
- Python version requirements
- Torch dependencies
- Installation commands
- Other package dependencies

To obtain this information, you would need to access a successfully loaded version of the page or visit the project's documentation, repository, or official installation guide directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-12T10:03:41.008727+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/princeton-nlp/edge-pruning/blob/main/requirements-experimental.txt",
  "prompt": "List all dependencies and their version constraints from this experimental requirements file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/princeton-nlp/edge-pruning/blob/main/requirements-experimental.txt",
    "prompt": "List all dependencies and their version constraints from this experimental requirements file"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-12T10:03:41.008874+00:00_

# AutoCircuit Library Summary

## Installation
Install via pip: `pip install auto-circuit`

## Core Purpose
AutoCircuit is "a library for efficient patching and automatic circuit discovery" in transformer models. It was presented as an oral spotlight at COLM 2024, based on the paper "Transformer Circuit Metrics are not Robust."

## Key Features

### Edge Patching
The library enables straightforward edge patching with syntax like:
```python
patch_edges = ["Resid Start->MLP 2", "MLP 2->A2.4.Q", "A2.4->Resid End"]
with patch_mode(model, ablations, patch_edges):
    patched_out = model(tokens)
```

### Ablation Methods
Supports multiple ablation approaches, including tokenwise mean corruption techniques for source ablation generation.

### Automatic Circuit Discovery
Implements mask gradient pruning for attribution-based circuit identification:
```python
attrution_patching_scores = mask_gradient_prune_scores(
    model=model, dataloader=test_loader, grad_function="logit"
)
```

### Visualization
Includes graph visualization capabilities for circuit analysis and interpretation.

## Technical Stack
- **Primary Language:** Python (99.7%)
- **Documentation:** Available at UFO-101.github.io/auto-circuit
- **Repository Metrics:** 97 stars, 19 forks, 10 releases

The repository contains experimental demos, comprehensive test suites, and measurement caches for reproducible research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-12T10:03:41.009018+00:00_

# Dependencies from requirements-experimental.txt

Based on the file content, here are all the dependencies and their version constraints:

1. **accelerate** - version 1.9.0
2. **datasets** - version 3.3.2
3. **einops** - no version specified
4. **evaluate** - no version specified
5. **flash_attn** - version 2.8.2
6. **graphviz** - no version specified
7. **networkx** - version 3.4.2
8. **numpy** - version 2.2.6
9. **scipy** - no version specified
10. **torch** - version 2.7.1
11. **torchvision** - version 0.22.1
12. **tqdm** - no version specified
13. **transformers** - version 4.54.0

The file also contains commented-out entries for haiku and jax. Seven packages have pinned versions, while six have no version constraints specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T10:03:41.009172+00:00_

# CIRCUS Paper Analysis

## Code/GitHub Repository
No link to a code repository or GitHub is provided in the content shown. The page displays standard arXiv metadata and bibliographic tools, but no code availability statement is visible.

## Algorithm Description
The provided abstract contains limited algorithmic details. The available information states:

**Core approach:** "CIRCUS prunes one attribution graph under B configurations, assigns each edge an empirical inclusion frequency s(e) in [0,1]" measuring robustness across configuration families.

**Key limitations in this excerpt:**
- The **B parameter** (number of configurations) is mentioned but not numerically specified
- **Threshold selection methodology** is not detailed
- **Stability score formula** is indicated as s(e) ∈ [0,1] representing "inclusion frequency," but the exact computational formula is absent

The abstract emphasizes the method yields a "core/contingent/noise decomposition" analogous to Bayesian variable selection, but full algorithmic specifications would require accessing the complete paper PDF or HTML version linked on the page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-12T10:03:41.009375+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/html/2603.00523",
  "prompt": "Extract: (1) the config-bagging algorithm details - B parameter value, threshold range, stability score formula s(e), (2) which base methods CIRCUS wraps (EAP-IG, ACDC, etc.), (3) whether code is released (GitHub link), (4) the Core/Contingent/Noise thresholds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/html/2603.00523",
    "prompt": "Extract: (1) the config-bagging algorithm details - B parameter value, threshold range, stability score formula s(e), (2) which base methods CIRCUS wraps (EAP-IG, ACDC, etc.), (3) whether code is released (GitHub link), (4) the Core/Contingent/Noise thresholds"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-12T10:03:41.009531+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MIB benchmark circuit localization track GitHub code evaluation API edge scores format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MIB benchmark circuit localization track GitHub code evaluation API edge scores format"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-12T10:03:41.009661+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hannamw eap-ig requirements.txt dependencies pyproject.toml TransformerLens version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hannamw eap-ig requirements.txt dependencies pyproject.toml TransformerLens version"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T10:03:41.009849+00:00_

Web search results for query: "hannamw eap-ig requirements.txt dependencies pyproject.toml TransformerLens version"

Links: [{"title":"Why Should I Choose pyproject.toml over requirements.txt for managing dependencies? | pydevtools","url":"https://pydevtools.com/handbook/explanation/pyproject-vs-requirements/"},{"title":"GitHub - hannamw/EAP-IG · GitHub","url":"https://github.com/hannamw/eap-ig"},{"title":"TransformerLens/pyproject.toml at main · TransformerLensOrg/TransformerLens","url":"https://github.com/TransformerLensOrg/TransformerLens/blob/main/pyproject.toml"},{"title":"PEP 735 – Dependency Groups in pyproject.toml | peps.python.org","url":"https://peps.python.org/pep-0735/"},{"title":"Install dependencies from pyproject.toml like from requirements.txt with -r · Issue #11584 · pypa/pip","url":"https://github.com/pypa/pip/issues/11584"},{"title":"The Complete Guide to pyproject.toml: replace setup.py and requirements.txt | by devsjc | Medium","url":"https://medium.com/@devsjc/the-complete-guide-to-pyproject-toml-replace-setup-py-and-requirements-txt-553f899dc267"},{"title":"Install dependencies from pyproject.toml like from requirements.txt with -r, (again) · Issue #13449 · pypa/pip","url":"https://github.com/pypa/pip/issues/13449"},{"title":"Manually adding dependencies to pyproject.toml - Packaging - Discussions on Python.org","url":"https://discuss.python.org/t/manually-adding-dependencies-to-pyproject-toml/18345"},{"title":"PEP 633 – Dependency specification in pyproject.toml using an exploded TOML table | peps.python.org","url":"https://peps.python.org/pep-0633/"},{"title":"PEP 725 – Specifying external dependencies in pyproject.toml | peps.python.org","url":"https://peps.python.org/pep-0725/"}]

Based on the search results, I found the hannamw/eap-ig library works with autoregressive transformer LMs in TransformerLens. The GitHub repository for the eap-ig project is available at https://github.com/hannamw/eap-ig.

However, the search results don't conta
…[truncated 528 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-12T10:03:41.010047+00:00_

# CIRCUS: Circuit Consensus under Uncertainty - Key Details

## (1) Config-Bagging Algorithm Details

**B Parameter & Threshold Range:**
The paper uses B=25 for stability analysis and B=9 for main evaluation, implemented as "a 5×5 grid" for the larger set. The configurations cross node and edge cumulative-influence thresholds in opposite directions to ensure non-nested pruning.

**Stability Score Formula:**
As stated in Equation 1: "s(e) = (1/B) Σ 𝟙[e ∈ E^(b)]" where the score represents empirical inclusion frequency across configurations, ranging from 0 to 1.

## (2) Base Methods Wrapped by CIRCUS

CIRCUS doesn't wrap existing circuit discovery frameworks like ACDC or EAP-IG. Instead, it builds directly on attribution graphs produced by "cross-layer transcoders (CLTs)" using publicly available tools (Ameisen et al., 2025; Hanna et al., 2025) for Gemma-2-2B and Llama-3.2-1B models.

## (3) Code Release Status

The paper includes no GitHub link or code release information. The author acknowledges "the teams that open-sourced attribution tools" but provides no repository for CIRCUS itself.

## (4) Core/Contingent/Noise Thresholds

The taxonomy uses stability score thresholds:
- **Core:** s(e) = 1 (edges in every view)
- **Contingent:** 0.5 ≤ s(e) < 1 (alternative pathways)
- **Noise:** s(e) < 0.5 (edges in fewer than half of views)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-12T10:03:41.010445+00:00_

Web search results for query: "MIB benchmark circuit localization track GitHub code evaluation API edge scores format"

Links: [{"title":"MIB – Project Page","url":"https://mib-bench.github.io/"},{"title":"MIB: A Mechanistic Interpretability Benchmark","url":"https://arxiv.org/html/2504.13151v1"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble Strategies for Circuit Localization Methods","url":"https://arxiv.org/html/2510.06811"},{"title":"GitHub - aaronmueller/MIB: Landing page for MIB: A Mechanistic Interpretability Benchmark · GitHub","url":"https://github.com/aaronmueller/MIB"},{"title":"MIB: A Mechanistic Interpretability Benchmark | OpenReview","url":"https://openreview.net/forum?id=sSrOwve6vb"},{"title":"GitHub - hannamw/MIB-circuit-track","url":"https://github.com/hannamw/MIB-circuit-track"},{"title":"Shared Task - BlackboxNLP 2025 - GitHub Pages","url":"https://blackboxnlp.github.io/2025/task/"},{"title":"BlackboxNLP-2025 MIB Shared Task: Exploring Ensemble ...","url":"https://aclanthology.org/2025.blackboxnlp-1.31.pdf"},{"title":"Findings of the BlackboxNLP 2025 Shared Task: Localizing Circuits and Causal Variables in Language Models","url":"https://arxiv.org/html/2511.18409v1"},{"title":"[2504.13151] MIB: A Mechanistic Interpretability Benchmark","url":"https://arxiv.org/abs/2504.13151"}]

Based on the search results, here's what I found about the MIB benchmark circuit localization track:

## Overview

The circuit localization track compares methods that locate the model components—and connections between them—most important for performing a task (e.g., attribution patching or information flow routes).

## Code & Repository

Code is available at this GitHub URL, with the main repository at https://github.com/hannamw/MIB-circuit-track. This repository provides code for the circuit localization track of the Mechanistic Interpretability Benchmark, including code for circuit discovery and evaluation.

## Edge Scores Format

Each circuit is a di
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-12T10:03:41.010662+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/hannamw/eap-ig/blob/main/pyproject.toml",
  "prompt": "Extract all dependencies, version constraints, Python version requirement, and package metadata from this pyproject.toml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/hannamw/eap-ig/blob/main/pyproject.toml",
    "prompt": "Extract all dependencies, version constraints, Python version requirement, and package metadata from this pyproject.toml"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-12T10:03:41.010831+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/hannamw/MIB-circuit-track",
  "prompt": "Extract: README content including installation, how to run evaluation, supported circuit discovery methods, input/output format for circuits, and how to add a new method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/hannamw/MIB-circuit-track",
    "prompt": "Extract: README content including installation, how to run evaluation, supported circuit discovery methods, input/output format for circuits, and how to add a new method"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-12T10:03:41.010967+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/swapnilparekh/circus",
  "prompt": "Check if this repository exists and extract any content about CIRCUS implementation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/swapnilparekh/circus",
    "prompt": "Check if this repository exists and extract any content about CIRCUS implementation"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-12T10:03:41.011103+00:00_

# EAP-IG Project Dependencies and Metadata

**Package Information:**
- Name: "eap"
- Version: "2.0.0"
- Python requirement: >=3.10
- Author: Michael Hanna (mh2parker@gmail.com)

**Core Dependencies:**
- matplotlib >= 3.10.1
- transformer-lens >= 2.15.0

**Optional Dependencies:**
- viz group: pygraphviz >= 1.14

**Build System:**
- Backend: hatchling
- Build requirement: hatchling

The project uses a standard pyproject.toml configuration with minimal dependencies focused on visualization and machine learning transformer analysis utilities.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-12T10:03:41.011232+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-12T10:03:41.011363+00:00_

# MIB Circuit Localization Track: Key Information

## Installation
The repository requires minimal dependencies. Users should `pip install .` after pulling submodules with `git submodule update --init --recursive`. The core dependency is EAP-IG, though visualizing circuits requires optionally installing `pygraphviz`. Testing used `torch == 2.4.1`.

## Circuit Discovery Methods
The framework supports several attribution approaches:

- **Edge Attribution Patching (EAP)** with node/neuron variants via `--level` parameter
- **EAP with Optimal Ablations** requiring preliminary computation via `oa.py` script
- **EAP-IG** in two variants: inputs-focused and activations-focused interpolations
- **Exact Activation Patching** for precise but computationally expensive analysis
- **Information Flow Routes (IFR)**
- **Uniform Gradient Sampling (UGS)** requiring mask training beforehand

## Running Attribution
Execute circuit discovery using: `"python run_attribution.py --models [MODELS] --tasks [TASKS]"` with parameters for method, granularity level, and ablation strategy.

## Evaluation Process
Similar command structure: `"python run_evaluation.py --models [MODELS] --tasks [TASKS]"` generates faithfulness scores and CPR/CMD metrics saved as pickle files.

## Circuit Formats
Submissions accept either single files with floating-point importance scores or nine binary membership circuits at specified edge percentage thresholds: 0.1%, 0.2%, 0.5%, 1%, 2%, 5%, 10%, 20%, 50%.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-12T10:03:41.011538+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "nnsight PyPI latest version 2025 2026 TransformerLens compatibility"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "tool_args": {
    "query": "nnsight PyPI latest version 2025 2026 TransformerLens compatibility"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-12T10:03:41.011670+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://github.com/UFO-101/auto-circuit/blob/main/pyproject.toml",
  "prompt": "Extract all dependencies, version constraints, Python version requirement from this pyproject.toml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://github.com/UFO-101/auto-circuit/blob/main/pyproject.toml",
    "prompt": "Extract all dependencies, version constraints, Python version requirement from this pyproject.toml"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-12T10:03:41.013554+00:00_

# Auto-Circuit Dependencies Summary

## Python Version
- **Required:** Python 3.10 or higher (`"python = "^3.10"`)

## Main Dependencies
- torch >= 2.1.1
- transformer-lens >= 1.13.0
- einops >= 0.6.1
- ordered-set >= 4.1.0
- plotly >= 5.18.0
- kaleido == 0.2.1
- blobfile >= 2.0.2
- word2word >= 1.0.0
- vscode-tqdm >= 4.66.2
- tracr-pypi >= 1.0.0

## Development Dependencies
- pre-commit ^3.3.3
- ipykernel ^6.25.0
- ipywidgets ^8.1.0
- jupyter ^1.0.0
- pytest ^7.4.0
- pyright ^1.1.350
- ipytest ^0.13.3

## Documentation Dependencies
- mkdocs-material ^9.5.17
- mkdocstrings (with Python extras) ^0.24.3
- mkdocs-gen-files ^0.5.0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-12T10:03:41.014621+00:00_

Web search results for query: "nnsight PyPI latest version 2025 2026 TransformerLens compatibility"

Links: [{"title":"transformer-lens · PyPI","url":"https://pypi.org/project/transformer-lens/"},{"title":"nnsight · PyPI","url":"https://pypi.org/project/nnsight/"},{"title":"sae-lens · PyPI","url":"https://pypi.org/project/sae-lens/"},{"title":"piwheels - transformer-lens","url":"https://www.piwheels.org/project/transformer-lens/"},{"title":"transformers · PyPI","url":"https://pypi.org/project/transformers/"},{"title":"GitHub - TransformerLensOrg/TransformerLens: A library for mechanistic interpretability of GPT-style language models · GitHub","url":"https://github.com/TransformerLensOrg/TransformerLens"},{"title":"nnsight and nnterp | Learn Mechanistic Interpretability","url":"https://learnmechinterp.com/topics/nnsight-and-nnterp/"},{"title":"piwheels - nnsight","url":"https://www.piwheels.org/project/nnsight/"},{"title":"Releases · ndif-team/nnsight","url":"https://github.com/ndif-team/nnsight/releases"},{"title":"transformers-openpi · PyPI","url":"https://pypi.org/project/transformers-openpi/"}]

Based on the search results, here's what I found about nnsight and its compatibility with TransformerLens:

## nnsight Latest Version

The latest version of nnsight was released on March 20, 2026.

## TransformerLens Compatibility

While the search results indicate that SAEs can be used with NNsight or any other framework by extracting activations and passing them to the SAE's encode() and decode() methods, there isn't explicit information about direct dependency compatibility between nnsight and TransformerLens in the PyPI documentation.

However, the search results show that nnsight works with any PyTorch model and complements TransformerLens as a tool for interpretability research that works directly with HuggingFace models. This suggests they can be used together for interpretability work, though they serve somewhat different purposes in the mechanistic interpretabili
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-12T10:03:41.015000+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/API_SURVEY.md",
  "content": "# Circuit Discovery API Survey\n\n> 调研日期：2026-05-12\n> 目标：确认 EAP-IG / AtP* / Edge Pruning / ACDC 四种电路发现方法的库、API、兼容性，以及 CIRCUS / MIB 的可复用性。\n\n---\n\n## 1. TransformerLens\n\n- **Version**: 3.2.1（2026-05-09 发布）；v2.x 仍可通过 `pip install 'transformer-lens~=2.0'` 安装\n- **Install**: `pip install transformer-lens`\n- **Python**: >=3.10, <4.0\n- **Torch**: 未在 PyPI 显式声明最低版本，实际兼容 torch >=2.1\n- **GPT-2 Small 加载**:\n  ```python\n  from transformer_lens import HookedTransformer\n  model = HookedTransformer.from_pretrained(\"gpt2-small\")\n  # v3.x 推荐 TransformerBridge，但 HookedTransformer 仍可用\n  ```\n- **IOI Dataset API**:\n  ```python\n  from transformer_lens.evals import ioi_eval, IOIDataset\n  dataset = IOIDataset(\n      tokenizer=model.tokenizer,\n      num_samples=100,\n  )\n  # dataset.toks: tokenized sentences\n  # dataset.s_tokenIDs / dataset.io_tokenIDs: subject/IO token positions\n  # ioi_eval(model) → (avg_logit_diff, accuracy)\n  ```\n- **Hook 机制**（edge-level attribution 基础）:\n  ```python\n  # 每个组件有标准 hook point name, e.g.:\n  # \"blocks.{layer}.attn.hook_result\"  (attention output)\n  # \"blocks.{layer}.mlp.hook_post\"     (MLP output)\n  # \"blocks.{layer}.hook_resid_pre\"    (residual stream)\n  cache = {}\n  model.run_with_cache(tokens, names_filter=lambda name: \"hook_result\" in name)\n  ```\n- **Source**: [PyPI](https://pypi.org/project/transformer-lens/) · [GitHub](https://github.com/TransformerLensOrg/TransformerLens)\n\n---\n\n## 2. EAP-IG（Edge Attribution Patching with Integrated Gradients）\n\n- **Repo**: https://github.com/hannamw/eap-ig\n- **Package**: `eap` v2.0.0\n- **Install**:\n  ```bash\n  git clone https://github.com/hannamw/eap-ig.git\n  cd eap-ig && pip install .\n  # 可选可视化: pip install .[viz]  (需系统装 graphviz)\n  ```\n- **Python**: >=3.10\n- **Dependencies**: `transformer-lens >= 2.15.0`, `matplotlib >= 3.10.1`\n- **核心 API（4 步流程）**:\n  ```python\n  from eap import Graph, attribute, evaluate_graph, EAPDataset\n\n  # 1. 加载模型\n  model = HookedTransformer.from_pretrained(\"gpt2-small\")\n\n  # 2. 构建计算图（自动从模型结构提取 nodes/edges）\n  graph = Graph.from_model(model)\n\n  # 3. 计算 edge attribution scores\n  dataloader = EAPDataset('greater-than').to_dataloader()\n  metric = ...  # 自定义 metric function\n  attribute(\n      model, graph, dataloader, metric,\n      method='EAP-IG-inputs',  # 或 'EAP-IG-activations', 'EAP'\n      ig_steps=5               # IG 插值步数 m\n  )\n  # graph 内部存储每条 edge 的 attribution score\n\n  # 4. Top-K thresholding → binary circuit\n  graph.apply_topn(n=100)   # 保留 top-100 edges\n  results = evaluate_graph(model, graph, dataloader, metric)\n  ```\n- **Attribution 方法**:\n  | 方法 | 复杂度 | 说明 |\n  |------|--------|------|\n  | `EAP` | O(1) | 一阶近似 |\n  | `EAP-IG-inputs` | O(m) | 输入 embedding 层面的 IG |\n  | `EAP-IG-activations` | O(m) | 每个组件 activation 层面的 IG |\n  | `clean-corrupted` | O(2) | 两点梯度 |\n- **Output**: `Graph` 对象，每条 edge 有 `.score` 属性；`apply_topn(n)` 后变为 binary mask\n- **模型兼容**: GPT-2, Pythia, Mistral, Llama, Qwen, OLMo, Gemma（需 pre-LayerNorm；GQA 模型需 `model.cfg.ungroup_grouped_query_attention = True`）\n- **论文**: Syed et al. 2023 \"Attribution Patching Outperforms Automated Circuit Discovery\"；Hanna et al. 2024 \"Have Faith in Faithfulness\"\n\n---\n\n## 3. AtP*（Attribution Patching Star）\n\n- **论文**: Kramár et al. 2024, \"AtP*: An efficient and scalable method for localizing LLM behaviour to components\" ([arXiv:2403.00745](https://arxiv.org/abs/2403.00745))\n- **官方代码**: DeepMind 未开源官方实现\n- **社区实现**: https://github.com/koayon/atp_star（非官方，PyTorch + NNsight 实现）\n- **Install**: `git clone https://github.com/koayon/atp_star.git`（无 PyPI 包，无 pyproject.toml / requirements.txt 公开）\n- **Dependencies**: PyTorch, NNsight（用于 caching/interventions）\n- **核心改进**（相对于标准 AtP）:\n  1. **QK-Fix**: 对 attention 节点显式线性化 attention probabilities（而非 softmax inputs）\n  2. **GradDrop**: 将 residual skip 路径上的 gradient 置零，消除 path-cancellation\n- **关键文件**: `atp.py`（核心算法）, `interventions.py`（干预机制）, `main.py`（入口）\n- **Output**: 组件级别的 attribution scores（node-level，非 edge-level）\n- **状态**: 开发中，尚不成熟；核心 AtP + QK-Fix 已实现，GPU 优化和 circuit-finding 部分仍 WIP\n- **⚠️ 注意**: AtP* 原论文是 **node-level** localization（定位重要组件），不直接产出 edge-level scores。要得到 edge-level circuit 需额外适配。\n\n---\n\n## 4. Edge Pruning\n\n- **Repo**: https://github.com/princeton-nlp/edge-pruning（NeurIPS 2024 Spotlight）\n- **论文**: Bhaskar et al. 2024, \"Finding Transformer Circuits with Edge Pruning\"\n- **Install**:\n  ```bash\n  git clone https://github.com/princeton-nlp/edge-pruning.git\n  cd edge-pruning\n  pip install -r requirements.txt\n  # GPT-2 + 新版 transformers: pip install -r requirements-experimental.txt\n  ```\n- **Dependencies（requirements.txt，原版）**:\n  - `torch == 2.5.1+cu121`\n  - `transformer-lens == 2.15.0`\n  - `accelerate == 1.2.1`, `datasets == 3.2.0`, `einops == 0.8.1`\n  - `flash-attn == 2.7.2.post1`\n  - `numpy == 2.2.3`, `scipy == 1.15.2`, `networkx == 3.4.2`\n  - `jax == 0.5.2`, `tensorflow == 2.18.0`（用于 Tracr 实验，非核心）\n- **Dependencies（requirements-experimental.txt，新版）**:\n  - `torch == 2.7.1`\n  - `transformers == 4.54.0`（HuggingFace，**不再依赖 TransformerLens**）\n  - `flash_attn == 2.8.2`, `accelerate == 1.9.0`\n- **核心方法**: 使用 L0 regularization 对 edge masks 进行可微优化（非贪心搜索），mask 值连续优化后 threshold → binary\n- **Key Scripts**:\n  | 任务 | Pruning 脚本 | 评估脚本 |\n  |------|-------------|---------|\n  | IOI | `src/prune/fpt2_ioi.py` | `src/eval/ioi.py` |\n  | Greater-Than | `src/prune/fpt2_gt.py` | `src/eval/gt.py` |\n  | Gendered Pronoun | `src/prune/fpt2_gp.py` | `src/eval/gp.py` |\n  | CodeLlama Boolean | `src/prune/fllama_boolean_expressions_*.py` | `src/eval/boolean_expressions.py` |\n- **Output**: JSON 格式的 edge set（pruned circuit），可通过 `src/modeling/vis_fpt2.py` 可视化\n- **⚠️ 注意**: 原版依赖 `transformer-lens==2.15.0`；实验版已迁移到 HuggingFace `transformers`。**不使用 nnsight**。\n\n---\n\n## 5. ACDC（Automatic Circuit Discovery）\n\n- **Repo**: https://github.com/ArthurConmy/Automatic-Circuit-Discovery（NeurIPS 2023 Spotlight）\n- **论文**: Conmy et al. 2023, \"Towards Automated Circuit Discovery for Mechanistic Interpretability\"\n- **Install**:\n  ```bash\n  git clone https://github.com/ArthurConmy/Automatic-Circuit-Discovery.git\n  cd Automatic-Circuit-Discovery\n  # 推荐用 poetry:\n  poetry env use 3.10\n  poetry install\n  # 或 conda/venv + pip install -e .\n  ```\n- **System deps**: `graphviz`, `libgraphviz-dev`（Ubuntu）或 `brew install graphviz`（Mac）\n- **Python**: >=3.8（推荐 3.10）\n- **Dependencies**: TransformerLens（HookPoints + HookedTransformer 抽象），具体版本由 poetry.lock 管理\n- **核心 API**:\n  ```python\n  # 主入口: acdc/main.py\n  # IOI 示例: 加载 GPT-2 Small + IOI dataset\n  from acdc.ioi.utils import get_ioi_gpt2_small\n  model, dataset = get_ioi_gpt2_small()\n\n  # 运行 ACDC 搜索（迭代 knock-out + 恢复）\n  # 见 notebooks/colabs/ACDC_Main_Demo.ipynb\n  ```\n- **算法**: 迭代地逐条删除 edge，检查 metric 变化是否超过 threshold τ；不超过则永久删除\n- **Output**: 计算图中保留的 edge set。GPT-2 Small + IOI 任务上从 ~32,000 edges 筛选出 68 条。\n- **⚠️ 推荐替代**: 作者推荐使用 **Auto-Circuit**（`pip install auto-circuit`）替代原始 ACDC 代码库\n\n### 5.1 Auto-Circuit（推荐的现代替代）\n\n- **Repo**: https://github.com/UFO-101/auto-circuit\n- **Install**: `pip install auto-circuit`\n- **Python**: >=3.10\n- **Dependencies**: `transformer-lens >= 1.13.0`, `torch >= 2.1.1`, `einops >= 0.6.1`, `plotly >= 5.18.0`\n- **核心 API**:\n  ```python\n  from auto_circuit.model_utils.micro_model_utils import MicroModel\n  from auto_circuit.prune_algos.mask_gradient import mask_gradient_prune_scores\n  from auto_circuit.types import PatchType\n\n  # Attribution-based circuit discovery\n  scores = mask_gradient_prune_scores(\n      model=model, dataloader=test_loader, grad_function=\"logit\"\n  )\n\n  # Edge patching\n  from auto_circuit.utils.patch_mode import patch_mode\n  patch_edges = [\"Resid Start->MLP 2\", \"MLP 2->A2.4.Q\", \"A2.4->Resid End\"]\n  with patch_mode(model, ablations, patch_edges):\n      patched_out = model(tokens)\n  ```\n- **支持方法**: ACDC, mask gradient pruning, attribution patching 等多种算法\n- **论文**: COLM 2024 Oral Spotlight, \"Transformer Circuit Metrics are not Robust\"\n\n---\n\n## 6. CIRCUS（Circuit Consensus under Uncertainty via Stability Ensembles）\n\n- **论文**: Parekh 2026, [arXiv:2603.00523](https://arxiv.org/abs/2603.00523)\n- **代码**: **未开源**（截至 2026-05-12 无 GitHub 仓库）\n- **方法概述**: Config-bagging over pruning thresholds\n  1. 对单次 attribution run 的结果，用 B 组不同 pruning 配置（node threshold × edge threshold 网格）进行裁剪\n  2. 每条 edge 计算 stability score: `s(e) = (1/B) Σ 𝟙[e ∈ E^(b)]`\n  3. 按 stability score 划分三层:\n     - **Core**: s(e) = 1（所有配置都保留）\n     - **Contingent**: 0.5 ≤ s(e) < 1（替代路径）\n     - **Noise**: s(e) < 0.5\n- **参数**: 主实验用 B=9（3×3 网格），稳定性分析用 B=25（5×5 网格）\n- **Base Attribution**: 基于 cross-layer transcoders (CLTs) 的 attribution graph，**不直接 wrap EAP-IG/ACDC**\n- **模型**: Gemma-2-2B（50 prompts），Llama-3.2-1B（20 prompts）\n- **结果**: Consensus circuit 比 union 小 ~40×，faithfulness 相当\n- **⚠️ 自行复现**: 核心逻辑简单——对任意 edge-level scores 做多阈值 bagging，可用 ~50 行 Python 实现:\n  ```python\n  def config_bag(edge_scores, thresholds, B=9):\n      \"\"\"edge_scores: dict{edge: float}, thresholds: list of cutoff values\"\"\"\n      counts = {e: 0 for e in edge_scores}\n      for t in thresholds:\n          for e, s in edge_scores.items():\n              if s >= t:\n                  counts[e] += 1\n      return {e: counts[e] / len(thresholds) for e in edge_scores}\n  ```\n\n---\n\n## 7. MIB Benchmark（Mechanistic Interpretability Benchmark）\n\n- **论文**: Mueller et al. 2025, [arXiv:2504.13151](https://arxiv.org/abs/2504.13151)（ICML 2025）\n- **Landing page**: https://github.com/aaronmueller/MIB\n- **Circuit Track 代码**: https://github.com/hannamw/MIB-circuit-track\n- **Install**:\n  ```bash\n  git clone https://github.com/hannamw/MIB-circuit-track.git\n  cd MIB-circuit-track\n  git submodule update --init --recursive  # 拉取 EAP-IG 子模块\n  pip install .\n  ```\n- **测试环境**: `torch == 2.4.1`\n- **支持的 Circuit Discovery 方法**:\n  - EAP（node / edge / neuron 级别，通过 `--level` 参数）\n  - EAP-IG（inputs / activations 两种变体）\n  - Exact Activation Patching\n  - Information Flow Routes (IFR)\n  - Uniform Gradient Sampling (UGS)\n  - EAP with Optimal Ablations\n- **模型**: GPT-2 Small, Qwen-2.5-0.5B, Gemma-2-2B, Llama-3.1-8B, InterpBench（含 ground-truth circuit）\n- **任务**: IOI, MCQA, Arithmetic, ARC, RAVEL\n- **运行**:\n  ```bash\n  # Attribution\n  python run_attribution.py --models gpt2-small --tasks ioi --method EAP-IG-inputs --level edge\n\n  # Evaluation\n  python run_evaluation.py --models gpt2-small --tasks ioi\n  ```\n- **Circuit 格式**:\n  - 浮点 scores: 单个 `.json` / `.pt` 文件，`{edge_name: float_score}`\n  - Binary circuits: 9 个文件，对应 edge 比例 thresholds（0.1%, 0.2%, 0.5%, 1%, 2%, 5%, 10%, 20%, 50%）\n- **评估指标**:\n  - **CPR**（Circuit Performance Ratio）: 电路独立执行时的性能保留率\n  - **CMD**（Circuit-Model Difference）: 电路行为与完整模型行为的差异\n- **⚠️ 复用价值**: MIB circuit track 基于 EAP-IG 库构建，可直接作为标准化评估框架使用\n\n---\n\n## 8. Compatibility Matrix\n\n### Python 版本\n\n| 库 | Python 要求 |\n|----|------------|\n| TransformerLens 3.x | >=3.10 |\n| EAP-IG 2.0 | >=3.10 |\n| Edge Pruning | >=3.10（推断） |\n| ACDC | >=3.8（推荐 3.10） |\n| Auto-Circuit | >=3.10 |\n| AtP*（社区版） | >=3.10（推断） |\n\n**结论**: Python 3.10 是所有库的安全基线。\n\n### PyTorch 版本\n\n| 库 | Torch 版本 |\n|----|-----------|\n| TransformerLens 3.x | >=2.1 |\n| EAP-IG 2.0 | 未声明（跟随 TransformerLens） |\n| Edge Pruning（原版） | ==2.5.1+cu121 |\n| Edge Pruning（实验版） | ==2.7.1 |\n| ACDC | 未显式声明 |\n| Auto-Circuit | >=2.1.1 |\n| MIB Circuit Track | ==2.4.1（测试版本） |\n\n**结论**: `torch >= 2.4, < 2.6` 是兼容性最优区间（覆盖 Edge Pruning 原版和 MIB）。如果不用 Edge Pruning 原版，`torch >= 2.4` 即可。\n\n### TransformerLens vs NNsight\n\n| 库 | 框架依赖 |\n|----|---------|\n| EAP-IG | TransformerLens >=2.15.0 |\n| Edge Pruning（原版） | TransformerLens ==2.15.0 |\n| Edge Pruning（实验版） | HuggingFace transformers（无 TransformerLens） |\n| ACDC | TransformerLens（版本由 poetry 管理） |\n| Auto-Circuit | TransformerLens >=1.13.0 |\n| AtP*（社区版） | NNsight + PyTorch |\n\n**结论**:\n- EAP-IG / Edge Pruning（原版） / ACDC / Auto-Circuit 全部基于 **TransformerLens**，共存无问题\n- AtP* 社区实现用 **NNsight**，但 NNsight 与 TransformerLens 无直接冲突（不同包，不同 hook 机制），可在同一环境安装\n- **推荐**: 统一使用 TransformerLens 生态（EAP-IG + Auto-Circuit），AtP* 如需使用则参考论文自行在 TransformerLens 上实现 QK-Fix + GradDrop\n\n### 潜在冲突\n\n1. **TransformerLens 2.x vs 3.x**: EAP-IG 和 Edge Pruning 要求 `>=2.15.0`，Auto-Circuit 要求 `>=1.13.0`。TransformerLens 3.x 保留了 `HookedTransformer` 兼容层，但可能有 breaking changes。**建议先用 `transformer-lens~=2.15` 保守路线**，待 EAP-IG 更新后再升级。\n2. **Edge Pruning 的额外依赖**: 原版 pinned `jax==0.5.2` 和 `tensorflow==2.18.0`（Tracr 实验用），与 torch 同装可能导致 CUDA 冲突。**若只做 GPT-2 实验，可删除 jax/tensorflow 行**。\n3. **flash-attn**: Edge Pruning 要求 `flash-attn==2.7.2.post1`，需编译安装且 CUDA 版本敏感。\n\n---\n\n## 9. Recommended requirements.txt\n\n```txt\n# Core\npython>=3.10\ntorch==2.5.1  # 兼容 Edge Pruning 原版；CUDA 版本按 GPU 选择\ntransformer-lens==2.15.0  # EAP-IG + Edge Pruning + Auto-Circuit 共同基线\n\n# EAP-IG (circuit discovery)\neap @ git+https://github.com/hannamw/eap-ig.git\nmatplotlib>=3.10.1\n\n# Auto-Circuit (ACDC 替代 + 多种方法)\nauto-circuit>=0.1.0\n\n# Edge Pruning (clone separately, use its own requirements)\n# git clone https://github.com/princeton-nlp/edge-pruning.git\n\n# Common\neinops>=0.8.1\ndatasets>=3.2.0\naccelerate>=1.2.1\nnetworkx>=3.4.2\nnumpy>=2.2.0\nscipy>=1.15.0\ntqdm>=4.67.0\n\n# Visualization (optional)\ngraphviz>=0.20.3\n# pygraphviz>=1.14  # 需系统 apt install libgraphviz-dev\nplotly>=5.18.0\n\n# Flash Attention (optional, 需编译)\n# flash-attn==2.7.2.post1\n\n# NNsight (仅 AtP* 社区实现需要)\n# nnsight>=0.3\n```\n\n---\n\n## 10. 推荐集成策略\n\n对于 StructFuse 项目，推荐以下集成路径：\n\n1. **主力框架**: TransformerLens 2.15.x + EAP-IG 2.0 作为 edge-level attribution 的核心\n2. **ACDC**: 通过 Auto-Circuit 库调用（比原始 ACDC 代码更稳定）\n3. **Edge Pruning**: 作为独立模块，clone 仓库后用其原版 requirements 运行（避免依赖冲突）\n4. **AtP***: 不推荐用社区实现（不成熟 + node-level only）；如需 AtP* 的 QK-Fix，在 EAP-IG 框架内自行实现更可控\n5. **CIRCUS Config-Bagging**: 自行实现（<100 行），作为 post-processing 叠加在任意 edge attribution 方法之上\n6. **评估**: 直接复用 MIB Circuit Track 框架（`run_attribution.py` + `run_evaluation.py`），获得标准化的 CPR/CMD 指标\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/API_SURVEY.md",
    "content": "# Circuit Discovery API Survey\n\n> 调研日期：2026-05-12\n> 目标：确认 EAP-IG / AtP* / Edge Pruning / ACDC 四种电路发现方法的库、API、兼容性，以及 CIRCUS / MIB 的可复用性。\n\n---\n\n## 1. TransformerLens\n\n- **Version**: 3.2.1（2026-05-09 发布）；v2.x 仍可通过 `pip install 'transformer-lens~=2.0'` 安装\n- **Install**: `pip install transformer-lens`\n- **Python**: >=3.10, <4.0\n- **Torch**: 未在 PyPI 显式声明最低版本，实际兼容 torch >=2.1\n- **GPT-2 Small 加载**:\n  ```python\n  from transformer_lens import HookedTransformer\n  model = HookedTransformer.from_pretrained(\"gpt2-small\")\n  # v3.x 推荐 TransformerBridge，但 HookedTransformer 仍可用\n  ```\n- **IOI Dataset API**:\n  ```python\n  from transformer_lens.evals import ioi_eval, IOIDataset\n  dataset = IOIDataset(\n      tokenizer=model.tokenizer,\n      num_samples=100,\n  )\n  # dataset.toks: tokenized sentences\n  # dataset.s_tokenIDs / dataset.io_tokenIDs: subject/IO token positions\n  # ioi_eval(model) → (avg_logit_diff, accuracy)\n  ```\n- **Hook 机制**（edge-level attribution 基础）:\n  ```python\n  # 每个组件有标准 hook point name, e.g.:\n  # \"blocks.{layer}.attn.hook_result\"  (attention output)\n  # \"blocks.{layer}.mlp.hook_post\"     (MLP output)\n  # \"blocks.{layer}.hook_resid_pre\"    (residual stream)\n  cache = {}\n  model.run_with_cache(tokens, names_filter=lambda name: \"hook_result\" in name)\n  ```\n- **Source**: [PyPI](https://pypi.org/project/transformer-lens/) · [GitHub](https://github.com/TransformerLensOrg/TransformerLens)\n\n---\n\n## 2. EAP-IG（Edge Attribution Patching with Integrated Gradients）\n\n- **Repo**: https://github.com/hannamw/eap-ig\n- **Package**: `eap` v2.0.0\n- **Install**:\n  ```bash\n  git clone https://github.com/hannamw/eap-ig.git\n  cd eap-ig && pip install .\n  # 可选可视化: pip install .[viz]  (需系统装 graphviz)\n  ```\n- **Python**: >=3.10\n- **Dependencies**: `transformer-lens >= 2.15.0`, `matplotlib >= 3.10.1`\n- **核心 API（4 步流程）**:\n  ```python\n  from eap import Graph, attribute, evaluate_graph, EAPDataset\n\n  # 1. 加载模型\n  model = HookedTransformer.from_pretrained(\"gpt2-small\")\n\n  # 2. 构建计算图（自动从模型结构提取 nodes/edges）\n  graph = Graph.from_model(model)\n\n  # 3. 计算 edge attribution scores\n  dataloader = EAPDataset('greater-than').to_dataloader()\n  metric = ...  # 自定义 metric function\n  attribute(\n      model, graph, dataloader, metric,\n      method='EAP-IG-inputs',  # 或 'EAP-IG-activations', 'EAP'\n      ig_steps=5               # IG 插值步数 m\n  )\n  # graph 内部存储每条 edge 的 attribution score\n\n  # 4. Top-K thresholding → binary circuit\n  graph.apply_topn(n=100)   # 保留 top-100 edges\n  results = evaluate_graph(model, graph, dataloader, metric)\n  ```\n- **Attribution 方法**:\n  | 方法 | 复杂度 | 说明 |\n  |------|--------|------|\n  | `EAP` | O(1) | 一阶近似 |\n  | `EAP-IG-inputs` | O(m) | 输入 embedding 层面的 IG |\n  | `EAP-IG-activations` | O(m) | 每个组件 activation 层面的 IG |\n  | `clean-corrupted` | O(2) | 两点梯度 |\n- **Output**: `Graph` 对象，每条 edge 有 `.score` 属性；`apply_topn(n)` 后变为 binary mask\n- **模型兼容**: GPT-2, Pythia, Mistral, Llama, Qwen, OLMo, Gemma（需 pre-LayerNorm；GQA 模型需 `model.cfg.ungroup_grouped_query_attention = True`）\n- **论文**: Syed et al. 2023 \"Attribution Patching Outperforms Automated Circuit Discovery\"；Hanna et al. 2024 \"Have Faith in Faithfulness\"\n\n---\n\n## 3. AtP*（Attribution Patching Star）\n\n- **论文**: Kramár et al. 2024, \"AtP*: An efficient and scalable method for localizing LLM behaviour to components\" ([arXiv:2403.00745](https://arxiv.org/abs/2403.00745))\n- **官方代码**: DeepMind 未开源官方实现\n- **社区实现**: https://github.com/koayon/atp_star（非官方，PyTorch + NNsight 实现）\n- **Install**: `git clone https://github.com/koayon/atp_star.git`（无 PyPI 包，无 pyproject.toml / requirements.txt 公开）\n- **Dependencies**: PyTorch, NNsight（用于 caching/interventions）\n- **核心改进**（相对于标准 AtP）:\n  1. **QK-Fix**: 对 attention 节点显式线性化 attention probabilities（而非 softmax inputs）\n  2. **GradDrop**: 将 residual skip 路径上的 gradient 置零，消除 path-cancellation\n- **关键文件**: `atp.py`（核心算法）, `interventions.py`（干预机制）, `main.py`（入口）\n- **Output**: 组件级别的 attribution scores（node-level，非 edge-level）\n- **状态**: 开发中，尚不成熟；核心 AtP + QK-Fix 已实现，GPU 优化和 circuit-finding 部分仍 WIP\n- **⚠️ 注意**: AtP* 原论文是 **node-level** localization（定位重要组件），不直接产出 edge-level scores。要得到 edge-level circuit 需额外适配。\n\n---\n\n## 4. Edge Pruning\n\n- **Repo**: https://github.com/princeton-nlp/edge-pruning（NeurIPS 2024 Spotlight）\n- **论文**: Bhaskar et al. 2024, \"Finding Transformer Circuits with Edge Pruning\"\n- **Install**:\n  ```bash\n  git clone https://github.com/princeton-nlp/edge-pruning.git\n  cd edge-pruning\n  pip install -r requirements.txt\n  # GPT-2 + 新版 transformers: pip install -r requirements-experimental.txt\n  ```\n- **Dependencies（requirements.txt，原版）**:\n  - `torch == 2.5.1+cu121`\n  - `transformer-lens == 2.15.0`\n  - `accelerate == 1.2.1`, `datasets == 3.2.0`, `einops == 0.8.1`\n  - `flash-attn == 2.7.2.post1`\n  - `numpy == 2.2.3`, `scipy == 1.15.2`, `networkx == 3.4.2`\n  - `jax == 0.5.2`, `tensorflow == 2.18.0`（用于 Tracr 实验，非核心）\n- **Dependencies（requirements-experimental.txt，新版）**:\n  - `torch == 2.7.1`\n  - `transformers == 4.54.0`（HuggingFace，**不再依赖 TransformerLens**）\n  - `flash_attn == 2.8.2`, `accelerate == 1.9.0`\n- **核心方法**: 使用 L0 regularization 对 edge masks 进行可微优化（非贪心搜索），mask 值连续优化后 threshold → binary\n- **Key Scripts**:\n  | 任务 | Pruning 脚本 | 评估脚本 |\n  |------|-------------|---------|\n  | IOI | `src/prune/fpt2_ioi.py` | `src/eval/ioi.py` |\n  | Greater-Than | `src/prune/fpt2_gt.py` | `src/eval/gt.py` |\n  | Gendered Pronoun | `src/prune/fpt2_gp.py` | `src/eval/gp.py` |\n  | CodeLlama Boolean | `src/prune/fllama_boolean_expressions_*.py` | `src/eval/boolean_expressions.py` |\n- **Output**: JSON 格式的 edge set（pruned circuit），可通过 `src/modeling/vis_fpt2.py` 可视化\n- **⚠️ 注意**: 原版依赖 `transformer-lens==2.15.0`；实验版已迁移到 HuggingFace `transformers`。**不使用 nnsight**。\n\n---\n\n## 5. ACDC（Automatic Circuit Discovery）\n\n- **Repo**: https://github.com/ArthurConmy/Automatic-Circuit-Discovery（NeurIPS 2023 Spotlight）\n- **论文**: Conmy et al. 2023, \"Towards Automated Circuit Discovery for Mechanistic Interpretability\"\n- **Install**:\n  ```bash\n  git clone https://github.com/ArthurConmy/Automatic-Circuit-Discovery.git\n  cd Automatic-Circuit-Discovery\n  # 推荐用 poetry:\n  poetry env use 3.10\n  poetry install\n  # 或 conda/venv + pip install -e .\n  ```\n- **System deps**: `graphviz`, `libgraphviz-dev`（Ubuntu）或 `brew install graphviz`（Mac）\n- **Python**: >=3.8（推荐 3.10）\n- **Dependencies**: TransformerLens（HookPoints + HookedTransformer 抽象），具体版本由 poetry.lock 管理\n- **核心 API**:\n  ```python\n  # 主入口: acdc/main.py\n  # IOI 示例: 加载 GPT-2 Small + IOI dataset\n  from acdc.ioi.utils import get_ioi_gpt2_small\n  model, dataset = get_ioi_gpt2_small()\n\n  # 运行 ACDC 搜索（迭代 knock-out + 恢复）\n  # 见 notebooks/colabs/ACDC_Main_Demo.ipynb\n  ```\n- **算法**: 迭代地逐条删除 edge，检查 metric 变化是否超过 threshold τ；不超过则永久删除\n- **Output**: 计算图中保留的 edge set。GPT-2 Small + IOI 任务上从 ~32,000 edges 筛选出 68 条。\n- **⚠️ 推荐替代**: 作者推荐使用 **Auto-Circuit**（`pip install auto-circuit`）替代原始 ACDC 代码库\n\n### 5.1 Auto-Circuit（推荐的现代替代）\n\n- **Repo**: https://github.com/UFO-101/auto-circuit\n- **Install**: `pip install auto-circuit`\n- **Python**: >=3.10\n- **Dependencies**: `transformer-lens >= 1.13.0`, `torch >= 2.1.1`, `einops >= 0.6.1`, `plotly >= 5.18.0`\n- **核心 API**:\n  ```python\n  from auto_circuit.model_utils.micro_model_utils import MicroModel\n  from auto_circuit.prune_algos.mask_gradient import mask_gradient_prune_scores\n  from auto_circuit.types import PatchType\n\n  # Attribution-based circuit discovery\n  scores = mask_gradient_prune_scores(\n      model=model, dataloader=test_loader, grad_function=\"logit\"\n  )\n\n  # Edge patching\n  from auto_circuit.utils.patch_mode import patch_mode\n  patch_edges = [\"Resid Start->MLP 2\", \"MLP 2->A2.4.Q\", \"A2.4->Resid End\"]\n  with patch_mode(model, ablations, patch_edges):\n      patched_out = model(tokens)\n  ```\n- **支持方法**: ACDC, mask gradient pruning, attribution patching 等多种算法\n- **论文**: COLM 2024 Oral Spotlight, \"Transformer Circuit Metrics are not Robust\"\n\n---\n\n## 6. CIRCUS（Circuit Consensus under Uncertainty via Stability Ensembles）\n\n- **论文**: Parekh 2026, [arXiv:2603.00523](https://arxiv.org/abs/2603.00523)\n- **代码**: **未开源**（截至 2026-05-12 无 GitHub 仓库）\n- **方法概述**: Config-bagging over pruning thresholds\n  1. 对单次 attribution run 的结果，用 B 组不同 pruning 配置（node threshold × edge threshold 网格）进行裁剪\n  2. 每条 edge 计算 stability score: `s(e) = (1/B) Σ 𝟙[e ∈ E^(b)]`\n  3. 按 stability score 划分三层:\n     - **Core**: s(e) = 1（所有配置都保留）\n     - **Contingent**: 0.5 ≤ s(e) < 1（替代路径）\n     - **Noise**: s(e) < 0.5\n- **参数**: 主实验用 B=9（3×3 网格），稳定性分析用 B=25（5×5 网格）\n- **Base Attribution**: 基于 cross-layer transcoders (CLTs) 的 attribution graph，**不直接 wrap EAP-IG/ACDC**\n- **模型**: Gemma-2-2B（50 prompts），Llama-3.2-1B（20 prompts）\n- **结果**: Consensus circuit 比 union 小 ~40×，faithfulness 相当\n- **⚠️ 自行复现**: 核心逻辑简单——对任意 edge-level scores 做多阈值 bagging，可用 ~50 行 Python 实现:\n  ```python\n  def config_bag(edge_scores, thresholds, B=9):\n      \"\"\"edge_scores: dict{edge: float}, thresholds: list of cutoff values\"\"\"\n      counts = {e: 0 for e in edge_scores}\n      for t in thresholds:\n          for e, s in edge_scores.items():\n              if s >= t:\n                  counts[e] += 1\n      return {e: counts[e] / len(thresholds) for e in edge_scores}\n  ```\n\n---\n\n## 7. MIB Benchmark（Mechanistic Interpretability Benchmark）\n\n- **论文**: Mueller et al. 2025, [arXiv:2504.13151](https://arxiv.org/abs/2504.13151)（ICML 2025）\n- **Landing page**: https://github.com/aaronmueller/MIB\n- **Circuit Track 代码**: https://github.com/hannamw/MIB-circuit-track\n- **Install**:\n  ```bash\n  git clone https://github.com/hannamw/MIB-circuit-track.git\n  cd MIB-circuit-track\n  git submodule update --init --recursive  # 拉取 EAP-IG 子模块\n  pip install .\n  ```\n- **测试环境**: `torch == 2.4.1`\n- **支持的 Circuit Discovery 方法**:\n  - EAP（node / edge / neuron 级别，通过 `--level` 参数）\n  - EAP-IG（inputs / activations 两种变体）\n  - Exact Activation Patching\n  - Information Flow Routes (IFR)\n  - Uniform Gradient Sampling (UGS)\n  - EAP with Optimal Ablations\n- **模型**: GPT-2 Small, Qwen-2.5-0.5B, Gemma-2-2B, Llama-3.1-8B, InterpBench（含 ground-truth circuit）\n- **任务**: IOI, MCQA, Arithmetic, ARC, RAVEL\n- **运行**:\n  ```bash\n  # Attribution\n  python run_attribution.py --models gpt2-small --tasks ioi --method EAP-IG-inputs --level edge\n\n  # Evaluation\n  python run_evaluation.py --models gpt2-small --tasks ioi\n  ```\n- **Circuit 格式**:\n  - 浮点 scores: 单个 `.json` / `.pt` 文件，`{edge_name: float_score}`\n  - Binary circuits: 9 个文件，对应 edge 比例 thresholds（0.1%, 0.2%, 0.5%, 1%, 2%, 5%, 10%, 20%, 50%）\n- **评估指标**:\n  - **CPR**（Circuit Performance Ratio）: 电路独立执行时的性能保留率\n  - **CMD**（Circuit-Model Difference）: 电路行为与完整模型行为的差异\n- **⚠️ 复用价值**: MIB circuit track 基于 EAP-IG 库构建，可直接作为标准化评估框架使用\n\n---\n\n## 8. Compatibility Matrix\n\n### Python 版本\n\n| 库 | Python 要求 |\n|----|------------|\n| TransformerLens 3.x | >=3.10 |\n| EAP-IG 2.0 | >=3.10 |\n| Edge Pruning | >=3.10（推断） |\n| ACDC | >=3.8（推荐 3.10） |\n| Auto-Circuit | >=3.10 |\n| AtP*（社区版） | >=3.10（推断） |\n\n**结论**: Python 3.10 是所有库的安全基线。\n\n### PyTorch 版本\n\n| 库 | Torch 版本 |\n|----|-----------|\n| TransformerLens 3.x | >=2.1 |\n| EAP-IG 2.0 | 未声明（跟随 TransformerLens） |\n| Edge Pruning（原版） | ==2.5.1+cu121 |\n| Edge Pruning（实验版） | ==2.7.1 |\n| ACDC | 未显式声明 |\n| Auto-Circuit | >=2.1.1 |\n| MIB Circuit Track | ==2.4.1（测试版本） |\n\n**结论**: `torch >= 2.4, < 2.6` 是兼容性最优区间（覆盖 Edge Pruning 原版和 MIB）。如果不用 Edge Pruning 原版，`torch >= 2.4` 即可。\n\n### TransformerLens vs NNsight\n\n| 库 | 框架依赖 |\n|----|---------|\n| EAP-IG | TransformerLens >=2.15.0 |\n| Edge Pruning（原版） | TransformerLens ==2.15.0 |\n| Edge Pruning（实验版） | HuggingFace transformers（无 TransformerLens） |\n| ACDC | TransformerLens（版本由 poetry 管理） |\n| Auto-Circuit | TransformerLens >=1.13.0 |\n| AtP*（社区版） | NNsight + PyTorch |\n\n**结论**:\n- EAP-IG / Edge Pruning（原版） / ACDC / Auto-Circuit 全部基于 **TransformerLens**，共存无问题\n- AtP* 社区实现用 **NNsight**，但 NNsight 与 TransformerLens 无直接冲突（不同包，不同 hook 机制），可在同一环境安装\n- **推荐**: 统一使用 TransformerLens 生态（EAP-IG + Auto-Circuit），AtP* 如需使用则参考论文自行在 TransformerLens 上实现 QK-Fix + GradDrop\n\n### 潜在冲突\n\n1. **TransformerLens 2.x vs 3.x**: EAP-IG 和 Edge Pruning 要求 `>=2.15.0`，Auto-Circuit 要求 `>=1.13.0`。TransformerLens 3.x 保留了 `HookedTransformer` 兼容层，但可能有 breaking changes。**建议先用 `transformer-lens~=2.15` 保守路线**，待 EAP-IG 更新后再升级。\n2. **Edge Pruning 的额外依赖**: 原版 pinned `jax==0.5.2` 和 `tensorflow==2.18.0`（Tracr 实验用），与 torch 同装可能导致 CUDA 冲突。**若只做 GPT-2 实验，可删除 jax/tensorflow 行**。\n3. **flash-attn**: Edge Pruning 要求 `flash-attn==2.7.2.post1`，需编译安装且 CUDA 版本敏感。\n\n---\n\n## 9. Recommended requirements.txt\n\n```txt\n# Core\npython>=3.10\ntorch==2.5.1  # 兼容 Edge Pruning 原版；CUDA 版本按 GPU 选择\ntransformer-lens==2.15.0  # EAP-IG + Edge Pruning + Auto-Circuit 共同基线\n\n# EAP-IG (circuit discovery)\neap @ git+https://github.com/hannamw/eap-ig.git\nmatplotlib>=3.10.1\n\n# Auto-Circuit (ACDC 替代 + 多种方法)\nauto-circuit>=0.1.0\n\n# Edge Pruning (clone separately, use its own requirements)\n# git clone https://github.com/princeton-nlp/edge-pruning.git\n\n# Common\neinops>=0.8.1\ndatasets>=3.2.0\naccelerate>=1.2.1\nnetworkx>=3.4.2\nnumpy>=2.2.0\nscipy>=1.15.0\ntqdm>=4.67.0\n\n# Visualization (optional)\ngraphviz>=0.20.3\n# pygraphviz>=1.14  # 需系统 apt install libgraphviz-dev\nplotly>=5.18.0\n\n# Flash Attention (optional, 需编译)\n# flash-attn==2.7.2.post1\n\n# NNsight (仅 AtP* 社区实现需要)\n# nnsight>=0.3\n```\n\n---\n\n## 10. 推荐集成策略\n\n对于 StructFuse 项目，推荐以下集成路径：\n\n1. **主力框架**: TransformerLens 2.15.x + EAP-IG 2.0 作为 edge-level attribution 的核心\n2. **ACDC**: 通过 Auto-Circuit 库调用（比原始 ACDC 代码更稳定）\n3. **Edge Pruning**: 作为独立模块，clone 仓库后用其原版 requirements 运行（避免依赖冲突）\n4. **AtP***: 不推荐用社区实现（不成熟 + node-level only）；如需 AtP* 的 QK-Fix，在 EAP-IG 框架内自行实现更可控\n5. **CIRCUS Config-Bagging**: 自行实现（<100 行），作为 post-processing 叠加在任意 edge attribution 方法之上\n6. **评估**: 直接复用 MIB Circuit Track 框架（`run_attribution.py` + `run_evaluation.py`），获得标准化的 CPR/CMD 指标\n"
  }
}
````

</details>

---

### Tool result

_source line 62 · 2026-05-12T10:03:41.015560+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/structfuse-context/artifacts/structfuse-mvp/API_SURVEY.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_circuit-api-survey_20260512T095923",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-12T10:03:41.015863+00:00_

调研报告已写入 `artifacts/structfuse-mvp/API_SURVEY.md`。

关键发现：

- **EAP-IG**（`hannamw/eap-ig` v2.0）是最成熟的 edge-level attribution 库，依赖 `transformer-lens>=2.15.0`，4 步 API（Graph → attribute → topn → evaluate）
- **ACDC** 原始代码作者推荐用 **Auto-Circuit**（`pip install auto-circuit`）替代，同样基于 TransformerLens
- **Edge Pruning**（`princeton-nlp/edge-pruning`）用 L0 mask 优化，原版也依赖 TransformerLens 2.15.0（**不是 nnsight**），实验版已迁移到 HuggingFace transformers
- **AtP*** 官方未开源，社区实现（`koayon/atp_star`）不成熟且是 node-level，不推荐直接用
- **CIRCUS** 无开源代码，但 config-bagging 逻辑简单可自行实现（~50 行）
- **MIB Circuit Track** 基于 EAP-IG 构建，可直接作为标准化评估框架复用
- **兼容性**: Python 3.10 + torch 2.5.x + transformer-lens 2.15.0 是所有库的安全公共基线

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_circuit-api-survey_20260512T095923"
}
```

</details>

---
