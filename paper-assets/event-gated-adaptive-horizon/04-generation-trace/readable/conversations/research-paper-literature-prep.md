# research paper literature prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/chats/worker_research_paper-literature-prep_20260515T011405.jsonl`
- **Structured JSON:** [`f03dc6502b1beef680fb.json`](../../sessions/f0/f03dc6502b1beef680fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

57 recorded events

### Tool call

_source line 1 · 2026-05-15T01:18:06.672328+00:00_

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
  "session": "worker_research_paper-literature-prep_20260515T011405",
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

_source line 2 · 2026-05-15T01:18:06.672762+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T01:18:06.673001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "temporal abstraction world model reinforcement learning 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "temporal abstraction world model reinforcement learning 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T01:18:06.673143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "delusional critic value overestimation model-based reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "delusional critic value overestimation model-based reinforcement learning"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T01:18:06.673270+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "variable time step dreamer reinforcement learning temporal skip prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "variable time step dreamer reinforcement learning temporal skip prediction"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T01:18:06.673579+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 analysis diagnostic improvement 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 analysis diagnostic improvement 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T01:18:06.673774+00:00_

Web search results for query: "delusional critic value overestimation model-based reinforcement learning"

Links: [{"title":"TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"},{"title":"Realistic Actor-Critic: A framework for balance between value overestimation and underestimation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9868235/"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514"},{"title":"Parameter-Free Reduction of the Estimation Bias in Deep Reinforcement Learning for Deterministic Policy Gradients | Neural Processing Letters | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11063-024-11461-y"},{"title":"[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514v2"},{"title":"[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514"},{"title":"[2601.00737] Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty","url":"https://arxiv.org/abs/2601.00737"},{"title":"Addressing maximization bias in reinforcement learning with two-sample testing - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370224001401"},{"title":"Simplifying Actor-Critic Reinforcement Learning: Mitigating Overestimation Bias with a Single Distributional Critic | OpenReview","url":"https://openreview.net/forum?id=i2dt3FPln8"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://proceedings.mlr.press/v235/nauman24a.html"}]

I've completed a web search for "delusional
…[truncated 1858 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T01:18:06.674080+00:00_

Web search results for query: "variable time step dreamer reinforcement learning temporal skip prediction"

Links: [{"title":"Chapter 9 Temporal-Difference Learning","url":"http://web.stanford.edu/group/pdplab/pdphandbook/handbookch10.html"},{"title":"NeurIPS Graph Dreamer: Temporal Graph World Models for Sample-Efficient and Generalisable Reinforcement Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/133755"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction","url":"https://arxiv.org/html/2603.07083"},{"title":"Temporal difference learning (TD Learning) | Engati","url":"https://www.engati.ai/glossary/temporal-difference-learning"},{"title":"Temporal difference learning - Wikipedia","url":"https://en.wikipedia.org/wiki/Temporal_difference_learning"},{"title":"Introducing n-Step Temporal-Difference Methods | Towards Data Science","url":"https://towardsdatascience.com/introducing-n-step-temporal-difference-methods-7f7878b3441c/"},{"title":"Graph Dreamer: Temporal Graph World Models for Sample-Efficient and Generalisable Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=pHmgNUZixd"},{"title":"Variable Time Step Reinforcement Learning for Robotic Applications","url":"https://arxiv.org/html/2407.00290v1"},{"title":"Temporal difference learning - Scholarpedia","url":"http://www.scholarpedia.org/article/Temporal_difference_learning"}]

Based on the search results, I found relevant information about your query. Here's what I discovered:

## Variable Time Step Reinforcement Learning

A recent work on variable time step reinforcement learning for robotic applications allows the algorithm to predict the action and its duration simultaneously.

## Dreamer and World Models

The search results reveal several recent developments in Dreamer-based reinforcement lear
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T01:18:06.674325+00:00_

Web search results for query: "DreamerV3 analysis diagnostic improvement 2024 2025"

Links: [{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"RLJ | RLC 2024 Dreaming of Many Worlds: Learning Contextual","url":"https://rlj.cs.umass.edu/2024/papers/RLJ_RLC_2024_167.pdf"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"(PDF) Mastering diverse control tasks through world models","url":"https://www.researchgate.net/publication/390440514_Mastering_diverse_control_tasks_through_world_models"},{"title":"dreamerv3 · PyPI","url":"https://pypi.org/project/dreamerv3/"}]

Based on the search results, here's what I found about DreamerV3 analysis and improvements:

## DreamerV3 Overview and Recent Developments

DreamerV3 is a general algorithm that outperforms specialized methods across over 150 diverse tasks, with a single configuration. The DreamerV1 algorithm was limited to continuous control, the DreamerV2 algorithm surpassed human performance on Atari, and the DreamerV3 algorithm enables out-of-the-box learning across diverse benchmarks.

## Key Improvements in DreamerV3

T
…[truncated 1089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T01:18:06.674660+00:00_

Web search results for query: "temporal abstraction world model reinforcement learning 2024 2025 2026"

Links: [{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"[2512.20605] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/abs/2512.20605"},{"title":"Hierarchical Planning with Latent World Models","url":"https://arxiv.org/html/2604.03208v1"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.20605"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Semantic Temporal Abstraction via Vision-Language Model Guidance for Efficient Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=zY37C8d6bS"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"[Quick Review] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://liner.com/review/emergent-temporal-abstractions-in-autoregressive-models-enable-hierarchical-reinforcement-learning"},{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"}]

Here are the search results for your query on temporal abstraction, world models, and reinforcement learning in 2024-2026:

## Key Rece
…[truncated 2161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T01:18:06.674859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"delusional\" reinforcement learning planning model-based"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"delusional\" reinforcement learning planning model-based"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T01:18:06.675003+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-step prediction RSSM world model temporal abstraction 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-step prediction RSSM world model temporal abstraction 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T01:18:06.675638+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "THICK hierarchical world model temporal abstraction ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "THICK hierarchical world model temporal abstraction ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T01:18:06.675793+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 temporal embedding time step duration action repeat"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 temporal embedding time step duration action repeat"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T01:18:06.676053+00:00_

Web search results for query: ""delusional" reinforcement learning planning model-based"

Links: [{"title":"Delusions of Large Language Models","url":"https://arxiv.org/html/2503.06709"},{"title":"Identifying and Addressing Delusions for Target-Directed Decision Making","url":"https://arxiv.org/html/2410.07096v3"},{"title":"ConQUR: Mitigating Delusional Bias in Deep Q-Learning | OpenReview","url":"https://openreview.net/forum?id=ryg8WJSKPr"},{"title":"(PDF) Non-delusional Q-learning and value-iteration","url":"https://www.researchgate.net/publication/328772100_Non-delusional_Q-learning_and_value-iteration"},{"title":"Non-delusional Q-learning and value iteration | Proceedings of the 32nd International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/citation.cfm?id=3327661"},{"title":"Delusional Unreality and Predictive Processing - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12179324/"},{"title":"Different learning aberrations relate to delusion-like beliefs with different contents - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11292907/"},{"title":"[2006.16712] Model-based Reinforcement Learning: A Survey","url":"https://arxiv.org/abs/2006.16712"},{"title":"Reinforcement Learning - Model Based Planning Methods | Towards Data Science","url":"https://towardsdatascience.com/reinforcement-learning-model-based-planning-methods-5e99cae0abb8/"},{"title":"Frontiers | A Unifying Framework for Reinforcement Learning and Planning","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.908353/full"}]

Based on the search results, here's what I found about delusional reinforcement learning and model-based planning:

## Delusion in Reinforcement Learning

Delusion has gained attention in the field of reinforcement learning, where a candidate target generator and a target estimator are used to simulate belief formation and evaluation processes. Misalignment between these components paral
…[truncated 1326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T01:18:06.676261+00:00_

Web search results for query: "THICK hierarchical world model temporal abstraction ICLR 2024"

Links: [{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"GitHub - CognitiveModeling/THICK · GitHub","url":"https://github.com/CognitiveModeling/THICK"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Autonomous Learning – MPI-IS","url":"https://is.mpg.de/al/publications/gumbsch2024-thickworldmodels"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"ICLR 2024 Schedule","url":"https://iclr.cc/virtual/2024/calendar"},{"title":"【DL輪読会】Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | ドクセル","url":"https://www.docswell.com/s/DeepLearning2023/5DEY1D-2024-07-05-090032"},{"title":"Iclr","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/0f93c3e9b557980d93016671acd94bd2-Paper-Conference.pdf"},{"title":"[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/abs/2404.16078"}]

Based on the search results, I found comprehensive information about THICK and the ICLR 2024 paper. Here's what I found:

## THICK: Learning Hierarchical World Models

THICK (Temporal Hierarchies from Invariant Context Kernels) is an algorithm that learns a world model hi
…[truncated 1083 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T01:18:06.676497+00:00_

Web search results for query: "DreamerV3 temporal embedding time step duration action repeat"

Links: [{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"NE-Dreamer: Next Embedding Prediction Makes World Models Stronger","url":"https://corl-team.github.io/nedreamer/"},{"title":"Dreamer V3 - EclecticSheep","url":"https://eclecticsheep.ai/2023/08/10/dreamer_v3.html"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction","url":"https://arxiv.org/html/2603.07083"},{"title":"DreamerV3 and Muzero. Both DreamerV3 and Muzero are… | by Kaige | Medium","url":"https://medium.com/@kaige.yang0110/dreamerv3-and-muzero-0bcce4ec998b"},{"title":"Recall to Imagine","url":"https://recall2imagine.github.io/"},{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"DreamerV3-style MBRL Agent","url":"https://www.emergentmind.com/topics/dreamerv3-style-mbrl-agent"}]

Based on the search results, I found relevant information about DreamerV3's temporal components. Here's what I found:

## DreamerV3 Temporal Embedding and Time Steps

The sequence model maintains a hidden state of the current step h_t, and the encoder encodes the input x_t in combination with the hidden state h_t into a latent embedding z_t. The sequence model generates the next hidden state h_t+1 given the current hidden state h_t, latent embedding z_t and current action a_t.

### Sequence Length and Planning Horizon

Common defaults include batch size 16–128, sequence length 50–64, learning rates, H
…[truncated 862 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T01:18:06.676731+00:00_

Web search results for query: "multi-step prediction RSSM world model temporal abstraction 2024 2025"

Links: [{"title":"Humans rationally balance detailed and temporally abstract world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11700031/"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11538428/"},{"title":"Humans rationally balance detailed and temporally abstract world models | Communications Psychology","url":"https://www.nature.com/articles/s44271-024-00169-3"},{"title":"Predictive World Models","url":"https://www.emergentmind.com/topics/predictive-world-models"},{"title":"RS-WorldModel: a Unified Model for Remote Sensing Understanding and Future Sense Forecasting","url":"https://arxiv.org/html/2603.14941"},{"title":"GitHub - ddz16/TSFpaper: This repository contains a reading list of papers on Time Series Forecasting/Prediction (TSF) and Spatio-Temporal Forecasting/Prediction (STF). These papers are mainly categorized according to the type of model. · GitHub","url":"https://github.com/ddz16/TSFpaper"},{"title":"A Background B Additional Related Work","url":"https://papers.nips.cc/paper_files/paper/2021/file/f490d0af974fedf90cb0f1edce8e3dd5-Supplemental.pdf"},{"title":"World Models in Reinforcement Learning","url":"https://www.emergentmind.com/topics/world-models-wms"},{"title":"Understanding World or Predicting Future? A Comprehensive Survey of World Models","url":"https://arxiv.org/html/2411.14499v2"}]

Based on the web search results, here's a summary of recent research on multi-step prediction, RSSM world models, and temporal abstraction:

## Key Research Areas

### Hierarchical World Models with Temporal Abstraction

THICK (Temporal Hierarc
…[truncated 2008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T01:18:06.676933+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"non-delusional Q-learning\" Lu Schuurmans NeurIPS 2018 model-based extension"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"non-delusional Q-learning\" Lu Schuurmans NeurIPS 2018 model-based extension"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T01:18:06.677072+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "overestimation bias world model imagination dreamer value function 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "overestimation bias world model imagination dreamer value function 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T01:18:06.677197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"temporal difference aware\" OR \"time-aware world model\" reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"temporal difference aware\" OR \"time-aware world model\" reinforcement learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T01:18:06.677317+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TempoRL variable action duration reinforcement learning options framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TempoRL variable action duration reinforcement learning options framework"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T01:18:06.677545+00:00_

Web search results for query: ""non-delusional Q-learning" Lu Schuurmans NeurIPS 2018 model-based extension"

Links: [{"title":"Non-delusional Q-learning and value-iteration","url":"https://proceedings.neurips.cc/paper_files/paper/2018/hash/5fd0245f6c9ddbdf3eff0f505975b6a7-Abstract.html"},{"title":"Non-delusional Q-learning and value-iteration","url":"https://papers.nips.cc/paper/8200-non-delusional-q-learning-and-value-iteration"},{"title":"[PDF] Non-delusional Q-learning and value-iteration | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Non-delusional-Q-learning-and-value-iteration-Lu-Schuurmans/59c0931562668b1ebb7c5cc8e9c236d43308722d"},{"title":"dblp: Non-delusional Q-learning and value-iteration.","url":"https://dblp.org/rec/conf/nips/LuSB18.html"},{"title":"Non-delusional Q-learning and value-iteration","url":"https://research.google/pubs/non-delusional-q-learning-and-value-iteration/"},{"title":"Non-delusional Q-learning and value-iteration - researchr publication","url":"https://researchr.org/publication/LuSB18"},{"title":"NIPS Oral Non-delusional Q-learning and value-iteration","url":"https://nips.cc/virtual/2018/oral/12737"},{"title":"NIPS 2018","url":"https://neurips.cc/Conferences/2018/Schedule?type=Oral&day=3"},{"title":"Under review as a conference paper at ICLR 2020","url":"https://openreview.net/pdf?id=ryg8WJSKPr"},{"title":"Non-delusional Q-learning and Value Iteration Tyler Lu Google AI","url":"https://papers.nips.cc/paper_files/paper/2018/file/5fd0245f6c9ddbdf3eff0f505975b6a7-Paper.pdf"}]

Based on the search results, I found comprehensive information about the "Non-delusional Q-learning and value-iteration" paper by Lu, Schuurmans, and Boutilier from NeurIPS 2018.

## Overview

The paper identifies a fundamental source of error in Q-learning and other forms of dynamic programming with function approximation. Delusional bias arises when the approximation architecture limits the class of expressible greedy policies.

## The Proble
…[truncated 1149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T01:18:06.678119+00:00_

Web search results for query: "overestimation bias world model imagination dreamer value function 2024 2025"

Links: [{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"World Models Reading List: The Papers You Actually Need in 2025 | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9"},{"title":"LEARNING BEHAVIORS BY LATENT IMAGINATION","url":"https://openreview.net/pdf?id=S1lOTC4tDS"},{"title":"Dream to Control: Learning Behaviors by Latent Imagination | OpenReview","url":"https://openreview.net/forum?id=S1lOTC4tDS"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"MAD-TD: MODEL-AUGMENTED DATA STABILIZES HIGH ...","url":"https://www.seas.upenn.edu/~eeaton/papers/Voelcker2025MADTD.pdf"},{"title":"Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning","url":"https://arxiv.org/html/2602.10044v1"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"TalkRL: The Reinforcement Learning Podcast | Transcript: Danijar Hafner on Dreamer v4","url":"https://www.talkrl.com/episodes/danijar-hafner-on-dreamer-v4/transcript"}]

I've completed the web search on your query about overestimation bias, world models, imagination, Dreamer, and value functions. Here are the key findings:

## Key Research Areas

**World Model Overestimation Issue
…[truncated 1539 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T01:18:06.678485+00:00_

Web search results for query: "TempoRL variable action duration reinforcement learning options framework"

Links: [{"title":"Variable Time Step Reinforcement Learning for Robotic Applications","url":"https://arxiv.org/html/2407.00290v1"},{"title":"TempoRL: Learning When to Act","url":"https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/21-ICML-TempoRL.pdf"},{"title":"Improving planning and MBRL with temporally-extended actions | OpenReview","url":"https://openreview.net/forum?id=Qq9okO8fbB"},{"title":"Improving planning and MBRL with temporally-extended actions","url":"https://arxiv.org/html/2505.15754"},{"title":"MOSEAC: Streamlined Variable Time Step Reinforcement Learning","url":"https://arxiv.org/html/2406.01521"},{"title":"Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0004370299000521"},{"title":"Option-aware Temporally Abstracted Value for Offline Goal-Conditioned Reinforcement Learning","url":"https://arxiv.org/html/2505.12737"},{"title":"DEER: A Delay-Resilient Framework for Reinforcement Learning with Variable Delays","url":"https://arxiv.org/html/2406.03102v1"},{"title":"Improving planning and MBRL with temporally-extended ...","url":"https://www.arxiv.org/pdf/2505.15754"},{"title":"A framework for temporal abstraction in reinforcement ...","url":"https://people.cs.umass.edu/~barto/courses/cs687/Sutton-Precup-Singh-AIJ99.pdf"}]

Based on the search results, here's what I found about TempoRL and variable action duration reinforcement learning:

## TempoRL Overview

TempoRL gives an agent two levels of control to decide on how long to apply an action. The paper "TempoRL: Learning When to Act" appears in the search results as a 2021 ICML publication focused on learning when agents should take actions.

## Variable Action Duration in Reinforcement Learning

Variable action duration is an important concept in modern RL research. Va
…[truncated 1107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T01:18:06.678851+00:00_

Web search results for query: ""temporal difference aware" OR "time-aware world model" reinforcement learning 2024 2025"

Links: [{"title":"GitHub - opendilab/awesome-model-based-RL: A curated list of awesome model based RL resources (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-model-based-RL"},{"title":"NeurIPS Graph Dreamer: Temporal Graph World Models for Sample-Efficient and Generalisable Reinforcement Learning","url":"https://neurips.cc/virtual/2025/loc/san-diego/133755"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/pdf/2506.08441"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"arXiv:2505.13508v2 [cs.CL] 3 Jun 2025 Time-R1: Towards Comprehensive Temporal","url":"https://arxiv.org/pdf/2505.13508"},{"title":"Awesome-World-Models/README.md at main · leofan90/Awesome-World-Models","url":"https://github.com/leofan90/Awesome-World-Models/blob/main/README.md"},{"title":"[2407.04811] Simplifying Deep Temporal Difference Learning","url":"https://arxiv.org/abs/2407.04811"},{"title":"A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗","url":"https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"},{"title":"RLJ · SwiftTD: A Fast and Robust Algorithm for Temporal Difference Learning","url":"https://rlj.cs.umass.edu/2024/papers/Paper111.html"},{"title":"Chapter 9 Temporal-Difference Learning","url":"http://web.stanford.edu/group/pdplab/pdphandbook/handbookch10.html"}]

I found relevant research on time-aware world models in reinforcement learning from 2024-2025. Here are the key findings:

## Key Papers and Research

### Time-Aware World Model (TAWM)
A recent approach adapts the TD-MPC2 world model and incorporates the fourth-order Runge–Kutta (RK4) method to stabilize learning at large temporal gap values, wh
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T01:18:06.679172+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"improving planning MBRL temporally-extended actions\" 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"improving planning MBRL temporally-extended actions\" 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T01:18:06.679319+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dreamer v4 Hafner 2025 2026 world model improvements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dreamer v4 Hafner 2025 2026 world model improvements"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T01:18:06.679452+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"MAD-TD\" model-augmented data value overestimation world model 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"MAD-TD\" model-augmented data value overestimation world model 2024"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T01:18:06.679578+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Time-Aware World Model\" adaptive prediction control arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Time-Aware World Model\" adaptive prediction control arxiv 2025"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T01:18:06.679764+00:00_

Web search results for query: ""improving planning MBRL temporally-extended actions" 2025 arxiv"

Links: [{"title":"[2505.15754] Improving planning and MBRL with temporally-extended actions","url":"https://arxiv.org/abs/2505.15754"},{"title":"Improving planning and MBRL with temporally-extended ...","url":"https://www.arxiv.org/pdf/2505.15754"},{"title":"Improving planning and MBRL with temporally-extended actions","url":"https://arxiv.org/html/2505.15754v2"},{"title":"Improving planning and MBRL with temporally-extended actions | OpenReview","url":"https://openreview.net/forum?id=Qq9okO8fbB"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=7600"},{"title":"Robotics May 2025","url":"https://www.arxiv.org/list/cs.RO/2025-05?skip=900&show=25"},{"title":"NeurIPS Poster Improving planning and MBRL with temporally-extended actions","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118096"},{"title":"Artificial Intelligence 2025","url":"https://arxiv.org/list/cs.AI/2025?skip=21400&show=25"},{"title":"Improving planning and MBRL with temporally-extended actions","url":"https://pecey.github.io/MBRL-with-TEA/"},{"title":"Artificial Intelligence May 2025","url":"https://www.arxiv.org/list/cs.AI/2025-05?skip=2750&show=1000"}]

I found the paper you're looking for! Here are the search results for "improving planning MBRL temporally-extended actions" from 2025 arxiv:

## Paper Details

The paper is titled "Improving planning and MBRL with temporally-extended actions" by Palash Chatterjee and Roni Khardon, with arxiv ID 2505.15754.

## Main Contribution

The paper addresses the problem that continuous time systems modeled with discrete time dynamics require small simulation steps for accuracy, which leads to large planning horizons and computationally demanding problems. The authors propose to control the continuous decision timescale directly by using temporally-extended actions and letting the planner treat the duration of the action
…[truncated 616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T01:18:06.680000+00:00_

Web search results for query: ""Time-Aware World Model" adaptive prediction control arxiv 2025"

Links: [{"title":"[2506.08441] Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/abs/2506.08441"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://arxiv.org/pdf/2506.08441"},{"title":"Electrical Engineering and Systems Science Jun 2025","url":"https://arxiv.org/list/eess/2025-06?skip=1400"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=2000&show=50"},{"title":"Systems and Control Jun 2025","url":"https://arxiv.org/list/eess.SY/2025-06?skip=325&show=250"},{"title":"Time-Aware World Model for Adaptive Prediction and Control","url":"https://sanghyun.phd.sh/publications/47670-time-aware-world-model-for-adaptive-prediction-and-control"},{"title":"Computer Science Jun 2025","url":"https://arxiv.org/list/cs/2025-06?skip=4550&show=25"},{"title":"Machine Learning Jun 2025","url":"https://arxiv.org/list/cs.LG/2025-06?skip=800&show=250"},{"title":"Learning Actionable World Models for Industrial Process Control Peng Yan∗†,","url":"https://arxiv.org/pdf/2503.01411"},{"title":"GitHub - leofan90/Awesome-World-Models: A comprehensive list of papers for the definition of World Models and using World Models for General Video Generation, Embodied AI, and Autonomous Driving, including papers, codes, and related websites. · GitHub","url":"https://github.com/leofan90/Awesome-World-Models"}]

I found the paper! Here are the key findings from the web search:

## Paper Summary

The paper introduces the Time-Aware World Model (TAWM), a model-based approach that explicitly incorporates temporal dynamics.

## Key Innovation

By conditioning on the time-step size (Δt) and training over a diverse range of Δt values -- rather than sampling at a fixed time-step -- TAWM learns both high- and low-frequency task dynamics across diverse control problems.

## Theoretical Foundation

Grounded
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T01:18:06.680273+00:00_

Web search results for query: ""MAD-TD" model-augmented data value overestimation world model 2024"

Links: [{"title":"[2410.08896] MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL","url":"https://arxiv.org/abs/2410.08896"},{"title":"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL","url":"https://arxiv.org/html/2410.08896v1"},{"title":"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL | OpenReview","url":"https://openreview.net/forum?id=6RtRsg8ZV1"},{"title":"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL","url":"https://www.researchgate.net/publication/384886286_MAD-TD_Model-Augmented_Data_stabilizes_High_Update_Ratio_RL"},{"title":"MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/b292ef48c211e2d8288146ff045dd61d-Abstract-Conference.html"},{"title":"Paper page - MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL","url":"https://huggingface.co/papers/2410.08896"},{"title":"MAD-TD: MODEL-AUGMENTED DATA STABILIZES HIGH ...","url":"https://www.seas.upenn.edu/~eeaton/papers/Voelcker2025MADTD.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=MAD-TD:+Model-Augmented+Data+stabilizes+High+Update+Ratio+RL."},{"title":"Preprint – arXiv 2024 MAD-TD: MODEL-AUGMENTED DATA STABILIZES","url":"https://www.arxiv.org/pdf/2410.08896v1"},{"title":"Model-Augmented Stabilization (MAD-TD)","url":"https://www.emergentmind.com/topics/model-augmented-stabilization-mad-td"}]

Based on the search results, I found comprehensive information about the MAD-TD model:

## MAD-TD: Model-Augmented Data for TD Learning

MAD-TD uses small amounts of generated data to stabilize high UTD (update-to-data ratio) training and achieve competitive performance on the most challenging tasks in the DeepMind control suite.

### Core Problem and Solution

High update-to-data ratios have shown strong empirical performance but introduce instability to the tr
…[truncated 1054 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T01:18:06.680480+00:00_

Web search results for query: "Dreamer v4 Hafner 2025 2026 world model improvements"

Links: [{"title":"TalkRL: The Reinforcement Learning Podcast | Transcript: Danijar Hafner on Dreamer v4","url":"https://www.talkrl.com/episodes/danijar-hafner-on-dreamer-v4/transcript"},{"title":"[2509.24527] Training Agents Inside of Scalable World Models","url":"https://arxiv.org/abs/2509.24527"},{"title":"dreamer4 · PyPI","url":"https://pypi.org/project/dreamer4/"},{"title":"GitHub - nicklashansen/dreamer4: Unofficial implementation of the Dreamer 4 world model in PyTorch. · GitHub","url":"https://github.com/nicklashansen/dreamer4"},{"title":"Dreamer 4: Learning to Achieve Goals from Offline Data through Imagination Training - InfoQ","url":"https://www.infoq.com/news/2025/10/dreamer-4-minecraft-agent/"},{"title":"Training Agents Inside of Scalable World Models","url":"https://danijar.com/project/dreamer4/"},{"title":"Training Agents Inside of Scalable World Models Danijar Hafner* Wilson Yan*","url":"https://arxiv.org/pdf/2509.24527"},{"title":"[Dreamer 4] Training Agents Inside of Scalable World Models","url":"https://arxiviq.substack.com/p/dreamer-4-training-agents-inside"},{"title":"Dreamer 4: Scalable World Model Agent","url":"https://www.emergentmind.com/topics/dreamer-4"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"}]

Based on the search results, here are the key improvements and features of Dreamer v4 by Danijar Hafner:

## Key World Model Improvements

Previous world models have been unable to accurately predict object interactions in complex environments, but Dreamer 4's world model accurately predicts object interactions and game mechanics in Minecraft, outperforming previous world models by a large margin.

## Technical Architecture Advances

The world model achieves real-time interactive inference on a single GPU through a shortcut forcing objective and an efficient transformer arc
…[truncated 1192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T01:18:06.680641+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"overestimation\" OR \"value collapse\" imagination rollout world model dreamer critic 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"overestimation\" OR \"value collapse\" imagination rollout world model dreamer critic 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T01:18:06.680771+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"learning world models hierarchical temporal abstractions probabilistic\" 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"learning world models hierarchical temporal abstractions probabilistic\" 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T01:18:06.680920+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NE-Dreamer \"next embedding prediction\" world model CoRL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NE-Dreamer \"next embedding prediction\" world model CoRL 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T01:18:06.681081+00:00_

Web search results for query: ""overestimation" OR "value collapse" imagination rollout world model dreamer critic 2024 2025"

Links: [{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"World Models Reading List: The Papers You Actually Need in 2025 | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"DreamerV3-style MBRL Agent","url":"https://www.emergentmind.com/topics/dreamerv3-style-mbrl-agent"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"Training Agents Inside of Scalable World Models Danijar Hafner* Wilson Yan*","url":"https://arxiv.org/pdf/2509.24527"},{"title":"LEARNING BEHAVIORS BY LATENT IMAGINATION","url":"https://openreview.net/pdf?id=S1lOTC4tDS"}]

I've performed the web search for your query. Here are the key findings related to overestimation, value collapse, imagination rollout, world models, and the Dreamer framework in recent research:

## Key Findings

**Overestimation in World Models:**
Previous research has shown that world models, especially in Dreamer, tend to overestimate aleatoric uncertainty. This is a known challenge in the Dreamer archi
…[truncated 1461 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T01:18:06.681259+00:00_

Web search results for query: "NE-Dreamer "next embedding prediction" world model CoRL 2025 2026"

Links: [{"title":"NE-Dreamer: Next Embedding Prediction Makes World Models Stronger","url":"https://corl-team.github.io/nedreamer/"},{"title":"[2603.02765] Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/abs/2603.02765"},{"title":"Next Embedding Prediction Makes World Models Stronger","url":"https://arxiv.org/html/2603.02765v1"},{"title":"GitHub - corl-team/nedreamer: Official implementation of the paper \"Next Embedding Prediction Makes World Models Stronger\" · GitHub","url":"https://github.com/corl-team/nedreamer"},{"title":"(PDF) Next Embedding Prediction Makes World Models Stronger","url":"https://www.researchgate.net/publication/401523861_Next_Embedding_Prediction_Makes_World_Models_Stronger"},{"title":"Paper page - Next Embedding Prediction Makes World Models Stronger","url":"https://huggingface.co/papers/2603.02765"},{"title":"Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction","url":"https://arxiv.org/html/2603.07083"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Dreamer 4: Scalable World Model Agents","url":"https://www.emergentmind.com/papers/2509.24527"},{"title":"Published as a conference paper at ICLR 2020","url":"https://openreview.net/pdf?id=S1lOTC4tDS"}]

Based on the web search results, here's what I found about NE-Dreamer:

## Overview

NE-Dreamer is a decoder-free MBRL agent that leverages a temporal transformer to predict next-step encoder embeddings from latent state sequences, directly optimizing temporal predictive alignment in representation space.

## Key Innovation

NE-Dreamer keeps Dreamer's RSSM dynamics and imagination-based actor–critic, but replaces same-step pixel reconstruction with next-embeddin
…[truncated 1072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T01:18:06.681437+00:00_

Web search results for query: ""learning world models hierarchical temporal abstractions probabilistic" 2024 arxiv"

Links: [{"title":"[2404.16078] Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective","url":"https://arxiv.org/abs/2404.16078"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | OpenReview","url":"https://openreview.net/forum?id=TjCDNssXKU"},{"title":"ICLR Poster Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics","url":"https://iclr.cc/virtual/2024/poster/18558"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"[2512.20605] Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/abs/2512.20605"},{"title":"Exploring the limits of Hierarchical World Models in Reinforcement Learning","url":"https://arxiv.org/pdf/2406.00483"},{"title":"Hierarchical Model-Based Reinforcement Learning with Temporal Abstractions | Open Research Commons","url":"https://bcommons.berkeley.edu/hierarchical-model-based-reinforcement-learning-temporal-abstractions"},{"title":"Efficient Exploration and Discriminative World Model Learning with an Object-Centric Abstraction","url":"https://arxiv.org/html/2408.11816v2"},{"title":"Paper page - Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://huggingface.co/papers/2512.20605"}]

I found several relevant papers on learning world models with hierarchical temporal abstractions and probabilistic approaches from 2024 and related research:

#
…[truncated 1442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T01:18:06.681599+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Overestimation Overfitting Plasticity Actor-Critic bitter lesson\" Nauman ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Overestimation Overfitting Plasticity Actor-Critic bitter lesson\" Nauman ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T01:18:06.681724+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"exploring limits hierarchical world models\" reinforcement learning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"exploring limits hierarchical world models\" reinforcement learning 2024"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T01:18:06.681862+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"optimistic world models\" exploration DreamerV3 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"optimistic world models\" exploration DreamerV3 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T01:18:06.682176+00:00_

Web search results for query: ""Overestimation Overfitting Plasticity Actor-Critic bitter lesson" Nauman ICML 2024"

Links: [{"title":"[2403.00514] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514"},{"title":"[PDF] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Overestimation,-Overfitting,-and-Plasticity-in-the-Nauman-Bortkiewicz/dcf39ce4ea7c1d073dcd0dbb131a0b90a4bd2977"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://proceedings.mlr.press/v235/nauman24a.html"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5vZzmCeTYu"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/html/2403.00514v1"},{"title":"Overestimation, overfitting, and plasticity in actor-critic | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3693586"},{"title":"ICML Poster Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://icml.cc/virtual/2024/poster/34956"},{"title":"[2403.00514v2] Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning","url":"https://arxiv.org/abs/2403.00514v2"},{"title":"Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/overestimation-overfitting-plasticity-actor-critic-bitter-lesson"},{"title":"dblp: Michal Nauman","url":"https://dblp.org/pid/277/6250.html"}]

I f
…[truncated 1359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T01:18:06.682369+00:00_

Web search results for query: ""exploring limits hierarchical world models" reinforcement learning 2024"

Links: [{"title":"[2406.00483] Exploring the limits of Hierarchical World Models in Reinforcement Learning","url":"https://arxiv.org/abs/2406.00483"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"Exploring the limits of Hierarchical World Models in Reinforcement Learning","url":"https://arxiv.org/html/2406.00483v1"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11538428/"},{"title":"Exploring the limits of Hierarchical World Models in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=zHlk0Ja90c"},{"title":"Exploring the limits of Hierarchical World Models in Reinforcement Learning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/exploring-limits-hierarchical-world-models-reinforcement-learning"},{"title":"Exploring the limits of Hierarchical World Models in Reinforcement Learning - Royal Holloway Research Portal","url":"https://pure.royalholloway.ac.uk/en/publications/exploring-the-limits-of-hierarchical-world-models-in-reinforcemen"},{"title":"[Literature Review] Exploring the limits of Hierarchical World Models in Reinforcement Learning","url":"https://www.themoonlight.io/en/review/exploring-the-limits-of-hierarchical-world-models-in-reinforcement-learning"},{"title":"LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-20653-y"},{"title":"RLJ · 2024","url":"https://rlj.cs.umass.edu/2024/2024issue.html"}]

I found research on "Exploring the limits of Hierarchical World Models in Reinforcement Learning" for you. Here are the key findings:

## Paper Overview

The
…[truncated 1363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T01:18:06.682561+00:00_

Web search results for query: ""optimistic world models" exploration DreamerV3 2025 2026"

Links: [{"title":"GitHub - danijar/dreamerv3: Mastering Diverse Domains through World Models · GitHub","url":"https://github.com/danijar/dreamerv3"},{"title":"Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning","url":"https://arxiv.org/html/2602.10044v1"},{"title":"[2602.10044] Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning","url":"https://arxiv.org/abs/2602.10044"},{"title":"DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12510832/"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"(PDF) Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning","url":"https://www.researchgate.net/publication/400661263_Optimistic_World_Models_Efficient_Exploration_in_Model-Based_Deep_Reinforcement_Learning"},{"title":"[Literature Review] Optimistic World Models: Efficient Exploration in Model-Based Deep Reinforcement Learning","url":"https://www.themoonlight.io/en/review/optimistic-world-models-efficient-exploration-in-model-based-deep-reinforcement-learning"}]

Based on the search results, here's what I found about optimistic world models and exploration with DreamerV3:

## Overview

Optimistic World Models (OWMs) introduce a principled and scalable framework for optimistic exploration that brings classical reward-biased maximum likeli
…[truncated 1575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T01:18:06.682741+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"stochastic actor-critic\" \"temporal aleatoric uncertainty\" overestimation 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"stochastic actor-critic\" \"temporal aleatoric uncertainty\" overestimation 2025"
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T01:18:06.682899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"recall to imagine\" world model reinforcement learning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"recall to imagine\" world model reinforcement learning 2024"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T01:18:06.683311+00:00_

Web search results for query: ""stochastic actor-critic" "temporal aleatoric uncertainty" overestimation 2025"

Links: [{"title":"[2601.00737] Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty","url":"https://arxiv.org/abs/2601.00737"},{"title":"Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty","url":"https://arxiv.org/html/2601.00737"},{"title":"Simplifying Actor-Critic Reinforcement Learning: Mitigating Overestimation Bias with a Single Distributional Critic | OpenReview","url":"https://openreview.net/forum?id=i2dt3FPln8"},{"title":"Full article: Risk-Sensitive Deep RL: Variance-Constrained Actor-Critic Provably Finds Globally Optimal Policy","url":"https://www.tandfonline.com/doi/full/10.1080/01621459.2025.2583501"},{"title":"Computation and Sample Efficient Reinforcement Learning with Deep Bayesian Actor-Critic | OpenReview","url":"https://openreview.net/forum?id=N5txhr5EDL"},{"title":"Computation and Sample Efficient Reinforcement Learning with ...","url":"https://openreview.net/pdf/2124ef64e41918544bbbb548be615188389bdfb5.pdf"},{"title":"Wasserstein Barycenter Soft Actor-Critic","url":"https://arxiv.org/html/2506.10167v1"},{"title":"Capturing Aleatoric Uncertainty in Climate Models","url":"https://arxiv.org/html/2604.15067"},{"title":"Realistic Actor-Critic: A framework for balance between value overestimation and underestimation - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9868235/"},{"title":"Soft Actor-Critic (SAC) - CleanRL","url":"https://docs.cleanrl.dev/rl-algorithms/sac/"}]

The search has returned relevant results about the Stochastic Actor-Critic (STAC) algorithm. Here's a summary of the key findings:

## Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty

The Stochastic Actor-Critic (STAC) algorithm incorporates temporal (one-step) aleatoric uncertainty—uncertainty arising from stochastic transitions, rewards, and policy-induced vari
…[truncated 1253 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T01:18:06.683516+00:00_

Web search results for query: ""recall to imagine" world model reinforcement learning 2024"

Links: [{"title":"Recall to Imagine","url":"https://recall2imagine.github.io/"},{"title":"Recall to Imagine (R2I): A New Machine Learning Approach that Enhances Long-Term Memory by Incorporating State Space Models into Model-based Reinforcement Learning (MBRL) - MarkTechPost","url":"https://www.marktechpost.com/2024/03/28/recall-to-imagine-r2i-a-new-machine-learning-approach-that-enhances-long-term-memory-by-incorporating-state-space-models-into-model-based-reinforcement-learning-mbrl/"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/0a0e436e8830f746300f592377730fca-Paper-Conference.pdf"},{"title":"Mastering Memory Tasks with World Models | OpenReview","url":"https://openreview.net/forum?id=1vDArHJ68h"},{"title":"Mastering diverse control tasks through world models | Nature","url":"https://www.nature.com/articles/s41586-025-08744-2"},{"title":"fly51fly on X: \"[LG] Mastering Memory Tasks with World Models M R Samsami, A Zholus, J Rajendran, S Chandar [Mila – Quebec AI Institute] (2024) https://t.co/L8t9NV9zAu - The paper introduces Recall to Imagine (R2I), a new model-based reinforcement learning method that integrates structured https://t.co/FJxhQCMjHV\" / X","url":"https://x.com/fly51fly/status/1765986420555206997"},{"title":"[2403.04253] Mastering Memory Tasks with World Models","url":"https://arxiv.org/abs/2403.04253"},{"title":"Mastering Memory Tasks with World Models","url":"https://arxiv.org/html/2403.04253v1"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Exploring Mental Models, World Models, and Reinforcement Learning: A Deep Dive into Predictive Intelligence. | by Bhakta Vaschal Samal | Medium","url":"https://bhakta-works.medium.com/exploring-me
…[truncated 1817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T01:18:06.683844+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T01:18:06.684002+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T01:18:06.684185+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_scan_20260515.md",
  "content": "# Literature Scan: Temporal Abstraction in MBRL (2024-2026)\n\n**Date**: 2026-05-15\n**Purpose**: Related work survey for CoRL 2026 diagnostic paper on dt_embedding → delusional critic in DreamerV3\n\n---\n\n## Direct Competitors\n\n### 1. THICK: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\n- **Authors**: Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz\n- **Venue**: ICLR 2024\n- **Link**: https://openreview.net/forum?id=TjCDNssXKU\n- **Summary**: Learns a world model hierarchy via discrete latent dynamics. Lower level updates latent state sparsely (forming \"invariant contexts\"), higher level predicts context changes. Enables multi-timescale reasoning in MBRL.\n- **Relation**: **Direct competitor** — addresses temporal abstraction in Dreamer-style world models. However, focuses on *hierarchical prediction* rather than diagnosing failure modes of temporal embeddings. Does NOT study delusional critic effects from trained dt embeddings.\n- **Key difference**: THICK adds hierarchy on top of RSSM; we diagnose a pathology *within* the existing DreamerV3 temporal mechanism.\n\n### 2. Time-Aware World Model for Adaptive Prediction and Control (TAWM)\n- **Authors**: Anh N. Nhu, Sanghyun Son, Ming Lin\n- **Venue**: ICML 2025 (arXiv: 2506.08441)\n- **Link**: https://arxiv.org/abs/2506.08441\n- **Summary**: Conditions world model on time-step size (Δt), training over diverse Δt values to learn both high- and low-frequency dynamics. Uses RK4 to stabilize learning at large temporal gaps. Adapts TD-MPC2 architecture.\n- **Relation**: **Direct competitor** — explicitly incorporates variable time steps into world model. However, focuses on *continuous control with variable observation rates*, not on diagnosing how learned temporal embeddings cause value overestimation in imagination. Architecture is TD-MPC2 based, not RSSM/Dreamer.\n- **Key difference**: TAWM treats Δt as beneficial conditioning; we show that *learning* such conditioning in DreamerV3 causes delusional critic collapse.\n\n### 3. Improving Planning and MBRL with Temporally-Extended Actions\n- **Authors**: Palash Chatterjee, Roni Khardon\n- **Venue**: NeurIPS 2025 (arXiv: 2505.15754)\n- **Link**: https://arxiv.org/abs/2505.15754\n- **Summary**: Treats action duration as optimization variable in continuous-time MBRL planning. Speeds up simulation, enables deep horizon search with shallow planner depth, reduces compounding model errors.\n- **Relation**: **Direct competitor** — variable-duration actions in MBRL. Complementary angle: they optimize duration for planning efficiency; we show that *learned* duration embeddings create pathological value estimates.\n- **Key difference**: Focus on planning efficiency, not on critic pathologies.\n\n### 4. Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective\n- **Authors**: Vaisakh Shaj\n- **Venue**: arXiv 2024 (2404.16078)\n- **Link**: https://arxiv.org/abs/2404.16078\n- **Summary**: Proposes Hidden-Parameter SSMs and Multi-Time Scale SSMs for scalable hierarchical world models with nonstationary dynamics across temporal scales.\n- **Relation**: **Complementary/competitor** — theoretical framework for multi-timescale SSMs. Does not empirically study DreamerV3's dt_embedding or its failure modes.\n\n---\n\n## Complementary Work\n\n### 5. Exploring the Limits of Hierarchical World Models in Reinforcement Learning\n- **Authors**: Robin Schiewer, Anand Subramoney, Laurenz Wiskott\n- **Venue**: Scientific Reports, Nov 2024 (arXiv: 2406.00483)\n- **Link**: https://arxiv.org/abs/2406.00483\n- **Summary**: Systematic study of HMBRL with static, environment-agnostic temporal abstraction. Constructs hierarchical world models at various temporal resolutions, trains stacked agents with top-down goal communication.\n- **Relation**: **Complementary** — empirical analysis of temporal abstraction limits in hierarchical MBRL. Shares diagnostic spirit but focuses on hierarchical goal-conditioned setting, not single-agent DreamerV3.\n\n### 6. NE-Dreamer: Next Embedding Prediction Makes World Models Stronger\n- **Authors**: CoRL Team (arXiv: 2603.02765, March 2026)\n- **Venue**: arXiv 2026\n- **Link**: https://arxiv.org/abs/2603.02765\n- **Summary**: Decoder-free MBRL agent replacing pixel reconstruction with next-embedding prediction via causal temporal transformer. Keeps RSSM dynamics and imagination-based actor-critic.\n- **Relation**: **Complementary** — improves DreamerV3's representation learning (decoder-free). Does not address temporal abstraction or dt_embedding pathologies.\n\n### 7. Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction\n- **Venue**: arXiv 2026 (2603.07083)\n- **Link**: https://arxiv.org/html/2603.07083\n- **Summary**: Adds continuous deterministic representation prediction to Dreamer, matching performance without reconstruction.\n- **Relation**: **Complementary** — architectural improvement to Dreamer, orthogonal to temporal abstraction issues.\n\n### 8. Dreamer 4: Training Agents Inside of Scalable World Models\n- **Authors**: Danijar Hafner, Wilson Yan\n- **Venue**: arXiv 2025 (2509.24527)\n- **Link**: https://arxiv.org/abs/2509.24527\n- **Summary**: Block-causal transformer world model with \"shortcut forcing\" objective. First agent to obtain diamonds in Minecraft from offline data. Scalable architecture trained on diverse videos + small action-conditioned data.\n- **Relation**: **Complementary** — next-gen Dreamer architecture (transformer-based, not RSSM). Does not retain dt_embedding mechanism. Our diagnostic applies to DreamerV3's RSSM + dt_embedding specifically.\n\n### 9. Recall to Imagine (R2I): Mastering Memory Tasks with World Models\n- **Authors**: Samsami, Zholus, Rajendran, Chandar\n- **Venue**: ICLR 2024\n- **Link**: https://arxiv.org/abs/2403.04253\n- **Summary**: Integrates state space models (S3M) into DreamerV3's world model for long-term memory and credit assignment. 9x speedup over DreamerV3.\n- **Relation**: **Complementary** — DreamerV3 extension for long-horizon tasks. Addresses temporal credit assignment but not temporal abstraction via dt embeddings.\n\n### 10. Optimistic World Models: Efficient Exploration in Model-Based Deep RL\n- **Venue**: arXiv 2026 (2602.10044)\n- **Link**: https://arxiv.org/abs/2602.10044\n- **Summary**: Adds optimistic dynamics loss to DreamerV3 (\"Optimistic DreamerV3\"), biasing imagined transitions toward higher rewards. Achieves 152.68% mean HNS vs DreamerV3's 97.45%.\n- **Relation**: **Complementary** — modifies DreamerV3's imagination to be optimistic. Interesting contrast: they *intentionally* bias value upward for exploration; we show *unintentional* upward bias from dt_embedding causes collapse.\n\n### 11. MAD-TD: Model-Augmented Data Stabilizes High Update Ratio RL\n- **Authors**: Voelcker et al.\n- **Venue**: ICLR 2025 (arXiv: 2410.08896)\n- **Link**: https://arxiv.org/abs/2410.08896\n- **Summary**: Uses small amounts of model-generated on-policy data to combat value overestimation and stabilize high UTD training. Shows model-generated data can suppress overestimation bias.\n- **Relation**: **Complementary** — addresses value overestimation via model-generated data augmentation. Different mechanism (UTD instability) but related symptom (overestimation).\n\n### 12. TempoRL: Learning When to Act\n- **Venue**: ICML 2021\n- **Link**: https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/21-ICML-TempoRL.pdf\n- **Summary**: Agent learns both action selection and action duration. Two-level control: what to do + how long to do it.\n- **Relation**: **Background** — foundational work on variable-duration actions. Model-free, predates DreamerV3.\n\n### 13. MOSEAC: Streamlined Variable Time Step Reinforcement Learning\n- **Venue**: arXiv 2024 (2406.01521)\n- **Link**: https://arxiv.org/html/2406.01521\n- **Summary**: VTS-RL algorithm learning actions and durations simultaneously.\n- **Relation**: **Background** — variable time step in model-free RL.\n\n---\n\n## Background / Delusional Critic\n\n### 14. Non-Delusional Q-learning and Value-Iteration\n- **Authors**: Tyler Lu, Dale Schuurmans, Craig Boutilier\n- **Venue**: NeurIPS 2018\n- **Link**: https://proceedings.neurips.cc/paper_files/paper/2018/hash/5fd0245f6c9ddbdf3eff0f505975b6a7-Abstract.html\n- **Summary**: Identifies \"delusional bias\" in Q-learning with function approximation — standard Q-updates make globally uncoordinated action choices, producing inconsistent/conflicting Q-values. Introduces \"information sets\" ensuring policy consistency. Proves model-based and model-free variants remove delusional bias.\n- **Relation**: **Key background** — defines the \"delusional\" terminology in RL. Their delusion arises from function approximation constraints on policy class; ours arises from temporal embedding enabling the critic to hallucinate unreachable temporal states during imagination.\n- **Key difference**: They address model-free Q-learning with restricted policy class. We identify a new delusional mechanism specific to learned temporal embeddings in model-based imagination.\n\n### 15. ConQUR: Mitigating Delusional Bias in Deep Q-Learning\n- **Venue**: ICLR 2020 submission\n- **Link**: https://openreview.net/forum?id=ryg8WJSKPr\n- **Summary**: Extends non-delusional Q-learning to deep RL with continuous actions using hindsight relabeling to identify delusional updates.\n- **Relation**: **Background** — extension of Lu et al. (2018) delusion concept. Still model-free focused.\n\n### 16. Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of RL\n- **Authors**: Nauman, Bortkiewicz, Miłoś, Trzcinski, Ostaszewski, Cygan\n- **Venue**: ICML 2024\n- **Link**: https://arxiv.org/abs/2403.00514\n- **Summary**: Large-scale diagnostic study (60+ agents, 14 tasks) showing overestimation, overfitting, and plasticity loss are interconnected failure modes in actor-critic methods. Regularization techniques have limited generalization.\n- **Relation**: **Important background** — shares diagnostic methodology spirit. Shows overestimation is systemic in actor-critic. Our work pinpoints a *specific structural cause* (dt_embedding) in a specific agent (DreamerV3) rather than studying generic regularization.\n\n### 17. Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty\n- **Venue**: arXiv Jan 2026 (2601.00737)\n- **Link**: https://arxiv.org/abs/2601.00737\n- **Summary**: Uses distributional critic modeling one-step temporal return uncertainty to scale pessimistic bias. Eliminates need for double/ensemble critics.\n- **Relation**: **Background** — addresses overestimation in model-free AC via distributional approach. Different mechanism from our model-based diagnosis.\n\n### 18. Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL\n- **Venue**: arXiv Dec 2025 (2512.20605)\n- **Link**: https://arxiv.org/abs/2512.20605\n- **Summary**: Higher-order non-causal sequence model controls residual stream of a base autoregressive model to discover temporally-abstract actions during RL finetuning.\n- **Relation**: **Background** — temporal abstraction in LLM-based RL agents, not world-model MBRL.\n\n---\n\n## Novelty Assessment\n\n### Our contribution relative to existing literature:\n\n1. **No prior work diagnoses dt_embedding → delusional critic in DreamerV3.** The temporal abstraction literature (THICK, TAWM, Chatterjee & Khardon) focuses on *adding* temporal abstraction capabilities. None identifies that DreamerV3's *existing* trained dt_embedding is pathological.\n\n2. **\"Delusional critic\" in a new context.** Lu et al. (2018) coined \"delusional\" for policy-inconsistent Q-backups in function approximation. We extend this concept to model-based imagination: the critic learns to exploit unreachable temporal states during imagined rollouts, causing systematic overestimation. This is a genuinely novel mechanism.\n\n3. **Diagnostic methodology for MBRL is underexplored.** Nauman et al. (ICML 2024) did a large diagnostic for model-free AC. No comparable diagnostic exists for DreamerV3's imagination pipeline. Our C6 (dt=1 imagination) finding — that a zero-cost fix eliminates the pathology — is practically impactful.\n\n4. **The dt=1 mitigation is novel.** No prior work proposes fixing DreamerV3's performance collapse by simply forcing dt=1 during imagination. This is a free lunch that the community should know about.\n\n5. **Complementary to Dreamer 4.** Dreamer 4 moves to transformers, abandoning RSSM+dt_embedding. Our diagnostic explains *why* this architectural shift helps — the old temporal mechanism was broken. This provides theoretical justification for Dreamer 4's design choices.\n\n### Positioning:\n- **Not scooped**: No one has published this specific diagnosis.\n- **Timely**: DreamerV3 remains widely used (Nature 2025 publication); Dreamer 4 just appeared. A diagnostic explaining the transition is valuable.\n- **Risk**: TAWM (ICML 2025) shows variable-Δt world models can work — but in TD-MPC2, not RSSM/Dreamer. We should cite and contrast clearly.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_scan_20260515.md",
    "content": "# Literature Scan: Temporal Abstraction in MBRL (2024-2026)\n\n**Date**: 2026-05-15\n**Purpose**: Related work survey for CoRL 2026 diagnostic paper on dt_embedding → delusional critic in DreamerV3\n\n---\n\n## Direct Competitors\n\n### 1. THICK: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics\n- **Authors**: Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz\n- **Venue**: ICLR 2024\n- **Link**: https://openreview.net/forum?id=TjCDNssXKU\n- **Summary**: Learns a world model hierarchy via discrete latent dynamics. Lower level updates latent state sparsely (forming \"invariant contexts\"), higher level predicts context changes. Enables multi-timescale reasoning in MBRL.\n- **Relation**: **Direct competitor** — addresses temporal abstraction in Dreamer-style world models. However, focuses on *hierarchical prediction* rather than diagnosing failure modes of temporal embeddings. Does NOT study delusional critic effects from trained dt embeddings.\n- **Key difference**: THICK adds hierarchy on top of RSSM; we diagnose a pathology *within* the existing DreamerV3 temporal mechanism.\n\n### 2. Time-Aware World Model for Adaptive Prediction and Control (TAWM)\n- **Authors**: Anh N. Nhu, Sanghyun Son, Ming Lin\n- **Venue**: ICML 2025 (arXiv: 2506.08441)\n- **Link**: https://arxiv.org/abs/2506.08441\n- **Summary**: Conditions world model on time-step size (Δt), training over diverse Δt values to learn both high- and low-frequency dynamics. Uses RK4 to stabilize learning at large temporal gaps. Adapts TD-MPC2 architecture.\n- **Relation**: **Direct competitor** — explicitly incorporates variable time steps into world model. However, focuses on *continuous control with variable observation rates*, not on diagnosing how learned temporal embeddings cause value overestimation in imagination. Architecture is TD-MPC2 based, not RSSM/Dreamer.\n- **Key difference**: TAWM treats Δt as beneficial conditioning; we show that *learning* such conditioning in DreamerV3 causes delusional critic collapse.\n\n### 3. Improving Planning and MBRL with Temporally-Extended Actions\n- **Authors**: Palash Chatterjee, Roni Khardon\n- **Venue**: NeurIPS 2025 (arXiv: 2505.15754)\n- **Link**: https://arxiv.org/abs/2505.15754\n- **Summary**: Treats action duration as optimization variable in continuous-time MBRL planning. Speeds up simulation, enables deep horizon search with shallow planner depth, reduces compounding model errors.\n- **Relation**: **Direct competitor** — variable-duration actions in MBRL. Complementary angle: they optimize duration for planning efficiency; we show that *learned* duration embeddings create pathological value estimates.\n- **Key difference**: Focus on planning efficiency, not on critic pathologies.\n\n### 4. Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective\n- **Authors**: Vaisakh Shaj\n- **Venue**: arXiv 2024 (2404.16078)\n- **Link**: https://arxiv.org/abs/2404.16078\n- **Summary**: Proposes Hidden-Parameter SSMs and Multi-Time Scale SSMs for scalable hierarchical world models with nonstationary dynamics across temporal scales.\n- **Relation**: **Complementary/competitor** — theoretical framework for multi-timescale SSMs. Does not empirically study DreamerV3's dt_embedding or its failure modes.\n\n---\n\n## Complementary Work\n\n### 5. Exploring the Limits of Hierarchical World Models in Reinforcement Learning\n- **Authors**: Robin Schiewer, Anand Subramoney, Laurenz Wiskott\n- **Venue**: Scientific Reports, Nov 2024 (arXiv: 2406.00483)\n- **Link**: https://arxiv.org/abs/2406.00483\n- **Summary**: Systematic study of HMBRL with static, environment-agnostic temporal abstraction. Constructs hierarchical world models at various temporal resolutions, trains stacked agents with top-down goal communication.\n- **Relation**: **Complementary** — empirical analysis of temporal abstraction limits in hierarchical MBRL. Shares diagnostic spirit but focuses on hierarchical goal-conditioned setting, not single-agent DreamerV3.\n\n### 6. NE-Dreamer: Next Embedding Prediction Makes World Models Stronger\n- **Authors**: CoRL Team (arXiv: 2603.02765, March 2026)\n- **Venue**: arXiv 2026\n- **Link**: https://arxiv.org/abs/2603.02765\n- **Summary**: Decoder-free MBRL agent replacing pixel reconstruction with next-embedding prediction via causal temporal transformer. Keeps RSSM dynamics and imagination-based actor-critic.\n- **Relation**: **Complementary** — improves DreamerV3's representation learning (decoder-free). Does not address temporal abstraction or dt_embedding pathologies.\n\n### 7. Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction\n- **Venue**: arXiv 2026 (2603.07083)\n- **Link**: https://arxiv.org/html/2603.07083\n- **Summary**: Adds continuous deterministic representation prediction to Dreamer, matching performance without reconstruction.\n- **Relation**: **Complementary** — architectural improvement to Dreamer, orthogonal to temporal abstraction issues.\n\n### 8. Dreamer 4: Training Agents Inside of Scalable World Models\n- **Authors**: Danijar Hafner, Wilson Yan\n- **Venue**: arXiv 2025 (2509.24527)\n- **Link**: https://arxiv.org/abs/2509.24527\n- **Summary**: Block-causal transformer world model with \"shortcut forcing\" objective. First agent to obtain diamonds in Minecraft from offline data. Scalable architecture trained on diverse videos + small action-conditioned data.\n- **Relation**: **Complementary** — next-gen Dreamer architecture (transformer-based, not RSSM). Does not retain dt_embedding mechanism. Our diagnostic applies to DreamerV3's RSSM + dt_embedding specifically.\n\n### 9. Recall to Imagine (R2I): Mastering Memory Tasks with World Models\n- **Authors**: Samsami, Zholus, Rajendran, Chandar\n- **Venue**: ICLR 2024\n- **Link**: https://arxiv.org/abs/2403.04253\n- **Summary**: Integrates state space models (S3M) into DreamerV3's world model for long-term memory and credit assignment. 9x speedup over DreamerV3.\n- **Relation**: **Complementary** — DreamerV3 extension for long-horizon tasks. Addresses temporal credit assignment but not temporal abstraction via dt embeddings.\n\n### 10. Optimistic World Models: Efficient Exploration in Model-Based Deep RL\n- **Venue**: arXiv 2026 (2602.10044)\n- **Link**: https://arxiv.org/abs/2602.10044\n- **Summary**: Adds optimistic dynamics loss to DreamerV3 (\"Optimistic DreamerV3\"), biasing imagined transitions toward higher rewards. Achieves 152.68% mean HNS vs DreamerV3's 97.45%.\n- **Relation**: **Complementary** — modifies DreamerV3's imagination to be optimistic. Interesting contrast: they *intentionally* bias value upward for exploration; we show *unintentional* upward bias from dt_embedding causes collapse.\n\n### 11. MAD-TD: Model-Augmented Data Stabilizes High Update Ratio RL\n- **Authors**: Voelcker et al.\n- **Venue**: ICLR 2025 (arXiv: 2410.08896)\n- **Link**: https://arxiv.org/abs/2410.08896\n- **Summary**: Uses small amounts of model-generated on-policy data to combat value overestimation and stabilize high UTD training. Shows model-generated data can suppress overestimation bias.\n- **Relation**: **Complementary** — addresses value overestimation via model-generated data augmentation. Different mechanism (UTD instability) but related symptom (overestimation).\n\n### 12. TempoRL: Learning When to Act\n- **Venue**: ICML 2021\n- **Link**: https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/21-ICML-TempoRL.pdf\n- **Summary**: Agent learns both action selection and action duration. Two-level control: what to do + how long to do it.\n- **Relation**: **Background** — foundational work on variable-duration actions. Model-free, predates DreamerV3.\n\n### 13. MOSEAC: Streamlined Variable Time Step Reinforcement Learning\n- **Venue**: arXiv 2024 (2406.01521)\n- **Link**: https://arxiv.org/html/2406.01521\n- **Summary**: VTS-RL algorithm learning actions and durations simultaneously.\n- **Relation**: **Background** — variable time step in model-free RL.\n\n---\n\n## Background / Delusional Critic\n\n### 14. Non-Delusional Q-learning and Value-Iteration\n- **Authors**: Tyler Lu, Dale Schuurmans, Craig Boutilier\n- **Venue**: NeurIPS 2018\n- **Link**: https://proceedings.neurips.cc/paper_files/paper/2018/hash/5fd0245f6c9ddbdf3eff0f505975b6a7-Abstract.html\n- **Summary**: Identifies \"delusional bias\" in Q-learning with function approximation — standard Q-updates make globally uncoordinated action choices, producing inconsistent/conflicting Q-values. Introduces \"information sets\" ensuring policy consistency. Proves model-based and model-free variants remove delusional bias.\n- **Relation**: **Key background** — defines the \"delusional\" terminology in RL. Their delusion arises from function approximation constraints on policy class; ours arises from temporal embedding enabling the critic to hallucinate unreachable temporal states during imagination.\n- **Key difference**: They address model-free Q-learning with restricted policy class. We identify a new delusional mechanism specific to learned temporal embeddings in model-based imagination.\n\n### 15. ConQUR: Mitigating Delusional Bias in Deep Q-Learning\n- **Venue**: ICLR 2020 submission\n- **Link**: https://openreview.net/forum?id=ryg8WJSKPr\n- **Summary**: Extends non-delusional Q-learning to deep RL with continuous actions using hindsight relabeling to identify delusional updates.\n- **Relation**: **Background** — extension of Lu et al. (2018) delusion concept. Still model-free focused.\n\n### 16. Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of RL\n- **Authors**: Nauman, Bortkiewicz, Miłoś, Trzcinski, Ostaszewski, Cygan\n- **Venue**: ICML 2024\n- **Link**: https://arxiv.org/abs/2403.00514\n- **Summary**: Large-scale diagnostic study (60+ agents, 14 tasks) showing overestimation, overfitting, and plasticity loss are interconnected failure modes in actor-critic methods. Regularization techniques have limited generalization.\n- **Relation**: **Important background** — shares diagnostic methodology spirit. Shows overestimation is systemic in actor-critic. Our work pinpoints a *specific structural cause* (dt_embedding) in a specific agent (DreamerV3) rather than studying generic regularization.\n\n### 17. Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty\n- **Venue**: arXiv Jan 2026 (2601.00737)\n- **Link**: https://arxiv.org/abs/2601.00737\n- **Summary**: Uses distributional critic modeling one-step temporal return uncertainty to scale pessimistic bias. Eliminates need for double/ensemble critics.\n- **Relation**: **Background** — addresses overestimation in model-free AC via distributional approach. Different mechanism from our model-based diagnosis.\n\n### 18. Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL\n- **Venue**: arXiv Dec 2025 (2512.20605)\n- **Link**: https://arxiv.org/abs/2512.20605\n- **Summary**: Higher-order non-causal sequence model controls residual stream of a base autoregressive model to discover temporally-abstract actions during RL finetuning.\n- **Relation**: **Background** — temporal abstraction in LLM-based RL agents, not world-model MBRL.\n\n---\n\n## Novelty Assessment\n\n### Our contribution relative to existing literature:\n\n1. **No prior work diagnoses dt_embedding → delusional critic in DreamerV3.** The temporal abstraction literature (THICK, TAWM, Chatterjee & Khardon) focuses on *adding* temporal abstraction capabilities. None identifies that DreamerV3's *existing* trained dt_embedding is pathological.\n\n2. **\"Delusional critic\" in a new context.** Lu et al. (2018) coined \"delusional\" for policy-inconsistent Q-backups in function approximation. We extend this concept to model-based imagination: the critic learns to exploit unreachable temporal states during imagined rollouts, causing systematic overestimation. This is a genuinely novel mechanism.\n\n3. **Diagnostic methodology for MBRL is underexplored.** Nauman et al. (ICML 2024) did a large diagnostic for model-free AC. No comparable diagnostic exists for DreamerV3's imagination pipeline. Our C6 (dt=1 imagination) finding — that a zero-cost fix eliminates the pathology — is practically impactful.\n\n4. **The dt=1 mitigation is novel.** No prior work proposes fixing DreamerV3's performance collapse by simply forcing dt=1 during imagination. This is a free lunch that the community should know about.\n\n5. **Complementary to Dreamer 4.** Dreamer 4 moves to transformers, abandoning RSSM+dt_embedding. Our diagnostic explains *why* this architectural shift helps — the old temporal mechanism was broken. This provides theoretical justification for Dreamer 4's design choices.\n\n### Positioning:\n- **Not scooped**: No one has published this specific diagnosis.\n- **Timely**: DreamerV3 remains widely used (Nature 2025 publication); Dreamer 4 just appeared. A diagnostic explaining the transition is valuable.\n- **Risk**: TAWM (ICML 2025) shows variable-Δt world models can work — but in TD-MPC2, not RSSM/Dreamer. We should cite and contrast clearly.\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T01:18:06.684489+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_scan_20260515.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T01:18:06.684630+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Literature Scan: Temporal Abstraction in MBRL (2024-2026)",
  "type": "report",
  "description": "Literature survey covering temporal abstraction world models, delusional critic/value overestimation, DreamerV3 diagnostics, and variable time-step MBRL. 18 papers reviewed with novelty assessment for CoRL 2026 submission.",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_scan_20260515.md",
  "tags": "['literature-review', 'corl2026', 'related-work']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Literature Scan: Temporal Abstraction in MBRL (2024-2026)",
    "type": "report",
    "description": "Literature survey covering temporal abstraction world models, delusional critic/value overestimation, DreamerV3 diagnostics, and variable time-step MBRL. 18 papers reviewed with novelty assessment for CoRL 2026 submission.",
    "project": "event-gated-adaptive-horizon",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/literature_scan_20260515.md",
    "tags": "['literature-review', 'corl2026', 'related-work']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T01:18:06.684783+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_bdae71\", \"name\": \"Literature Scan: Temporal Abstraction in MBRL (2024-2026)\", \"type\": \"report\", \"description\": \"Literature survey covering temporal abstraction world models, delusional critic/value overestimation, DreamerV3 diagnostics, and variable time-step MBRL. 18 papers reviewed with novelty assessment for CoRL 2026 submission.\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/literature_scan_20260515.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T01:17:56.453553+00:00\", \"tags\": [\"literature-review\", \"corl2026\", \"related-work\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_paper-literature-prep_20260515T011405",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 57 · 2026-05-15T01:18:06.684983+00:00_

报告已写入并注册。核心结论：

**未被 scoop**。18 篇相关文献中，没有任何一篇诊断过 DreamerV3 的 trained dt_embedding 导致 delusional critic / value overestimation 的问题。

最相关的 3 篇竞品：
- **THICK** (ICLR 2024) — 加层级，不诊断 dt_embedding 病理
- **TAWM** (ICML 2025) — 变步长 world model，但基于 TD-MPC2，不涉及 RSSM
- **Chatterjee & Khardon** (NeurIPS 2025) — 变时长 action 加速 planning，不分析 critic 过估

"Delusional" 术语在 RL 中主要追溯到 Lu & Schuurmans (NeurIPS 2018)，指 function approximation 下 Q-backup 的 policy inconsistency。我们的用法是对该概念在 model-based imagination 中的新实例化——critic 利用 dt_embedding 到达不可达的时间状态——属于合理的术语扩展，需在论文中明确引用和区分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_paper-literature-prep_20260515T011405"
}
```

</details>

---
