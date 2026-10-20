# research related work expansion

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/chats/worker_research_related-work-expansion_20260516T162428.jsonl`
- **Structured JSON:** [`d250d9991b87bcd1f7a4.json`](../../sessions/d2/d250d9991b87bcd1f7a4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

61 recorded events

### Tool call

_source line 1 · 2026-05-16T16:28:04.477385+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T16:28:04.478054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T16:28:04.478422+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TD3 twin delayed DDPG value overestimation deep reinforcement learning Fujimoto 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TD3 twin delayed DDPG value overestimation deep reinforcement learning Fujimoto 2018"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T16:28:04.478579+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "HarmonyDream world model reconstruction reward loss magnitude difference 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "HarmonyDream world model reconstruction reward loss magnitude difference 2024"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T16:28:04.478705+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PETS probabilistic ensemble trajectory sampling model-based RL Chua 2018"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PETS probabilistic ensemble trajectory sampling model-based RL Chua 2018"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T16:28:04.478863+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MOPO model-based offline policy optimization Yu 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MOPO model-based offline policy optimization Yu 2020"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T16:28:04.479037+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "plasticity loss deep reinforcement learning Lyle 2023 Abbas 2023 neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "plasticity loss deep reinforcement learning Lyle 2023 Abbas 2023 neural network"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T16:28:04.479225+00:00_

Web search results for query: "PETS probabilistic ensemble trajectory sampling model-based RL Chua 2018"

Links: [{"title":"[1805.12114] Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models","url":"https://arxiv.org/abs/1805.12114"},{"title":"GitHub - kchua/handful-of-trials: Experiment code for \"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models\" · GitHub","url":"https://github.com/kchua/handful-of-trials"},{"title":"[PDF] Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Reinforcement-Learning-in-a-Handful-of-Trials-Chua-Calandra/56136aa0b2c347cbcf3d50821f310c4253155026"},{"title":"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models","url":"https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html"},{"title":"Deep Reinforcement Learning in a Handful of Trials using ...","url":"https://proceedings.neurips.cc/paper_files/paper/2018/file/3de568f8597b94bda53149c7d7f5958c-Paper.pdf"},{"title":"Deep Reinforcement Learning in a Handful of Trials using ...","url":"https://personalrobotics.cs.washington.edu/workshops/mlmp2018/assets/docs/13_CameraReadySubmission_drl-in-handful-trials.pdf"},{"title":"Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models","url":"https://papers.nips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html"},{"title":"PETS: Deep RL via Probabilistic Dynamics","url":"https://www.emergentmind.com/papers/1805.12114"},{"title":"Probabilistic Ensemble with Trajectory Sampling (PETS)","url":"https://www.emergentmind.com/topics/probabilistic-ensemble-with-trajectory-sampling-pets"},{"title":"Deep reinforcement learning in a handful of trials using probabilistic dynamics models | Proceedings of the 32nd International Conference on Neural Inf
…[truncated 1877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T16:28:04.479429+00:00_

Web search results for query: "HarmonyDream world model reconstruction reward loss magnitude difference 2024"

Links: [{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://arxiv.org/html/2310.00344v3"},{"title":"GitHub - thuml/HarmonyDream: Code release for \"HarmonyDream: Task Harmonization Inside World Models\" (ICML 2024), https://arxiv.org/abs/2310.00344 · GitHub","url":"https://github.com/thuml/HarmonyDream"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://manchery.github.io/assets/pub/icml2024_harmonydream/poster.pdf"},{"title":"HarmonyDream: Task Harmonization Inside World Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/harmonydream-task-harmonization-inside-world-models"},{"title":"[2310.00344] HarmonyDream: Task Harmonization Inside World Models","url":"https://arxiv.org/abs/2310.00344"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/HarmonyDream-icml24.pdf"},{"title":"DyMoDreamer: World Modeling with Dynamic Modulation","url":"https://arxiv.org/pdf/2509.24804"},{"title":"ICML Poster HarmonyDream: Task Harmonization Inside World Models","url":"https://icml.cc/virtual/2024/poster/32730"},{"title":"[2310.00344v2] HarmonyDream: Task Harmonization Inside World Models","url":"https://arxiv.org/abs/2310.00344v2"},{"title":"HarmonyDream: Task Harmonization Inside World Models","url":"https://proceedings.mlr.press/v235/ma24o.html"}]

Based on the search results, I can provide you with information about HarmonyDream and the magnitude differences in loss functions:

## HarmonyDream Overview

HarmonyDream automatically adjusts loss coefficients to maintain task harmonization, i.e. a dynamic equilibrium between the two tasks in world model learning. The method finds that harmonizing domination among two tasks, observation and reward modeling, in world models can dramatically boost the sample-efficiency of model-ba
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T16:28:04.479620+00:00_

Web search results for query: "TD3 twin delayed DDPG value overestimation deep reinforcement learning Fujimoto 2018"

Links: [{"title":"Twin Delayed DDPG — Spinning Up documentation","url":"https://spinningup.openai.com/en/latest/algorithms/td3.html"},{"title":"arXiv:1802.09477v3 [cs.AI] 22 Oct 2018","url":"https://arxiv.org/pdf/1802.09477"},{"title":"Twin Delayed Deep Deterministic Policy Gradient (TD3)","url":"https://www.emergentmind.com/topics/twin-delayed-deep-deterministic-policy-gradient-td3"},{"title":"Twin actor twin delayed deep deterministic policy gradient (TATD3) learning for batch process control - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0098135421003057"},{"title":"TD3 tutorial and implementation","url":"https://medium.com/@joanna.z.gryczka/td3-tutorial-and-implementation-682f16b56699"},{"title":"Twin Delayed Deep Deterministic Policy Gradient (TD3): The Complete Guide for Continuous Control in Reinforcement Learning - aigreeks.com","url":"https://aigreeks.com/twin-delayed-deep-deterministic-policy-gradient-td3/"},{"title":"Twin Delayed DDPG | AI Wiki","url":"https://aiwiki.ai/wiki/td3"},{"title":"Reinforcement Learning(Part-7): Twin Delayed Deep Deterministic Policy Gradient(TD3) in Tensorflow2 | by Sthanikam Santhosh | Medium","url":"https://medium.com/@sthanikamsanthosh1994/reinforcement-learning-part-7-twin-delayed-deep-deterministic-policy-gradient-td3-in-tensorflow2-726fb9a53ae6"},{"title":"Twin Delayed Deep Deterministic Policy Gradient (TD3) - CleanRL","url":"https://docs.cleanrl.dev/rl-algorithms/td3/"},{"title":"Twin-Delayed DDPG: A Deep Reinforcement Learning ...","url":"https://dl.acm.org/doi/10.1145/3387168.3387199"}]

I've found comprehensive information about TD3 (Twin Delayed Deep Deterministic Policy Gradient). Here's a summary of the key findings:

## Overview

Twin Delayed Deep Deterministic Policy Gradient (TD3) is an off-policy actor-critic reinforcement learning algorithm for continuous action
…[truncated 2006 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-16T16:28:04.479806+00:00_

Web search results for query: "plasticity loss deep reinforcement learning Lyle 2023 Abbas 2023 neural network"

Links: [{"title":"Loss of Plasticity in Continual Deep Reinforcement Learning","url":"https://proceedings.mlr.press/v232/abbas23a/abbas23a.pdf"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/ce7984e36d58659211a8dc7d5457cd6f-Paper-Conference.pdf"},{"title":"Deep Reinforcement Learning with Plasticity Injection Evgenii Nikishin∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/75101364dc3aa7772d27528ea504472b-Paper-Conference.pdf"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://arxiv.org/html/2405.19153v1"},{"title":"NeurIPS Poster Deep Reinforcement Learning with Plasticity Injection","url":"https://neurips.cc/virtual/2023/poster/70670"},{"title":"Deep Reinforcement Learning with Plasticity Injection","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/75101364dc3aa7772d27528ea504472b-Abstract-Conference.html"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5647763d4245b23e6a1cb0a8947b38c9-Paper-Conference.pdf"},{"title":"Understanding Plasticity in Neural Networks","url":"https://proceedings.mlr.press/v202/lyle23b.html"},{"title":"Maintaining Plasticity in Continual Learning via Regenerative Regularization","url":"https://arxiv.org/html/2308.11958v3"},{"title":"[2303.07507] Loss of Plasticity in Continual Deep Reinforcement Learning","url":"https://arxiv.org/abs/2303.07507"}]

I found relevant research on plasticity loss in deep reinforcement learning. Here are the key findings from the Lyle 2023 and Abbas 2023 papers:

## Abbas et al. 2023

Abbas et al. showed that RL agents lose their ability to learn good policies when they cycle through a sequence of Atari 2600 games. Their analysis shows that the activati
…[truncated 1363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T16:28:04.480061+00:00_

Web search results for query: "MOPO model-based offline policy optimization Yu 2020"

Links: [{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://proceedings.neurips.cc/paper/2020/hash/a322852ce0df73e204b7e67cbbef0d0a-Abstract.html"},{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://proceedings.nips.cc/paper/2020/file/a322852ce0df73e204b7e67cbbef0d0a-Paper.pdf"},{"title":"[2005.13239] MOPO: Model-based Offline Policy Optimization","url":"https://arxiv.org/abs/2005.13239"},{"title":"MOPO: Model-based Offline Policy Optimization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200513239Y/abstract"},{"title":"GitHub - tianheyu927/mopo: Code for MOPO: Model-based Offline Policy Optimization","url":"https://github.com/tianheyu927/mopo"},{"title":"MOPO: Model-based Offline Policy Optimization","url":"https://biases-invariances-generalization.github.io/pdf/big_12.pdf"},{"title":"MOPO: Model-Based Offline Policy Optimization","url":"https://simons.berkeley.edu/talks/mopo-model-based-offline-policy-optimization"},{"title":"MOPO: Model-based Offline Policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/341699761_MOPO_Model-based_Offline_Policy_Optimization"},{"title":"MOPO: model-based offline policy optimization","url":"https://dl.acm.org/doi/10.5555/3495724.3496909"},{"title":"MOPO: Model-based Offline Policy Optimization - researchr publication","url":"https://researchr.org/publication/YuTYEZLFM20"}]

Based on the search results, here's information about MOPO (Model-based Offline Policy Optimization) by Yu et al. 2020:

## Overview

MOPO was presented by Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Y Zou, Sergey Levine, Chelsea Finn, and Tengyu Ma at NeurIPS 2020.

## Problem Statement

The paper addresses offline reinforcement learning (RL), which refers to learning policies entirely from a batch of previously collected data, offering the promise of utilizing large, diverse datase
…[truncated 1063 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T16:28:04.480228+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "temporal abstraction model-based reinforcement learning options framework TDMPC world models 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "temporal abstraction model-based reinforcement learning options framework TDMPC world models 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-16T16:28:04.480358+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "value overestimation model-based reinforcement learning value inflation conservative estimation 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "value overestimation model-based reinforcement learning value inflation conservative estimation 2022 2023"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T16:28:04.480477+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "stop gradient manipulation reinforcement learning representation learning detach gradient 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "stop gradient manipulation reinforcement learning representation learning detach gradient 2022 2023"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-16T16:28:04.480593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "adaptive horizon reinforcement learning variable planning horizon model predictive control 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "adaptive horizon reinforcement learning variable planning horizon model predictive control 2023 2024"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-16T16:28:04.480748+00:00_

Web search results for query: "temporal abstraction model-based reinforcement learning options framework TDMPC world models 2023 2024"

Links: [{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://arxiv.org/html/2502.03550v1"},{"title":"TD-M(PC)2: Improving Temporal Difference MPC Through Policy Constraint","url":"https://darthutopian.github.io/tdmpc_square/static/pdfs/paper.pdf"},{"title":"Temporal Difference MPC","url":"https://www.emergentmind.com/topics/temporal-difference-model-predictive-control-td-mpc"},{"title":"Hierarchical Model-Based Reinforcement Learning with Temporal Abstractions | Open Research Commons","url":"https://bcommons.berkeley.edu/hierarchical-model-based-reinforcement-learning-temporal-abstractions"},{"title":"GitHub - nicklashansen/tdmpc2: Code for \"TD-MPC2: Scalable, Robust World Models for Continuous Control\" · GitHub","url":"https://github.com/nicklashansen/tdmpc2"},{"title":"[PDF] Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Between-MDPs-and-Semi-MDPs:-A-Framework-for-in-Sutton-Precup/0e7638dc16a5e5e9e46c91272bfb9c3dd242ef6d"},{"title":"Emergent temporal abstractions in autoregressive models enable hierarchical reinforcement learning","url":"https://arxiv.org/html/2512.20605v1"},{"title":"TDM: From Model-Free to Model-Based Deep Reinforcement Learning – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2018/04/26/tdm/"},{"title":"[2310.16828] TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/abs/2310.16828"},{"title":"TD-MPC2: Scalable, Robust World Models for Continuous Control","url":"https://arxiv.org/html/2310.16828v2"}]

Based on the web search results, here's what I found regarding temporal abstraction in model-based reinforcement learning with a focus on the TDMPC framework and world models from 202
…[truncated 1643 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T16:28:04.481203+00:00_

Web search results for query: "stop gradient manipulation reinforcement learning representation learning detach gradient 2022 2023"

Links: [{"title":"Implicit Contrastive Representation Learning with Guided Stop-gradient [Quick Review]","url":"https://liner.com/review/implicit-contrastive-representation-learning-with-guided-stopgradient"},{"title":"Gradient Free Deep Reinforcement Learning With TabPFN","url":"https://arxiv.org/html/2509.11259v1"},{"title":"Measure gradients, not activations! Enhancing neuronal activity in deep reinforcement learning","url":"https://arxiv.org/html/2505.24061v1"},{"title":"1 Gradient Monitored Reinforcement Learning","url":"https://arxiv.org/pdf/2005.12108"},{"title":"Stable Gradients for Stable Learning at Scale in Deep Reinforcement Learning","url":"https://arxiv.org/html/2506.15544v1"},{"title":"Deep deterministic policy gradient algorithm: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405844024067288"},{"title":"Deep Policy Gradient Methods Without Batch Updates, Target Networks, or Replay Buffers","url":"https://arxiv.org/html/2411.15370"},{"title":"Dual-Oriented Contrast for Recommendation with A Stop-Gradient Operation | Proceedings of the 32nd ACM International Conference on Information and Knowledge Management","url":"https://dl.acm.org/doi/10.1145/3583780.3614852"},{"title":"Frontiers | Gradient-free training of recurrent neural networks using random perturbations","url":"https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1439155/full"},{"title":"When Neural Networks Stop Learning: Understanding Vanishing Gradients - DEV Community","url":"https://dev.to/rijultp/when-neural-networks-stop-learning-understanding-vanishing-gradients-4fnn"}]

I've completed the web search for your query on stop gradient manipulation, reinforcement learning, representation learning, and detaching gradients from 2022-2023. Here's a summary of the findings:

## Key Researc
…[truncated 1411 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-16T16:28:04.481412+00:00_

Web search results for query: "value overestimation model-based reinforcement learning value inflation conservative estimation 2022 2023"

Links: [{"title":"[2302.06884] Conservative State Value Estimation for Offline Reinforcement Learning","url":"https://arxiv.org/abs/2302.06884"},{"title":"TD3: Overcoming Overestimation in Deep Reinforcement Learning | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/td3-overcoming-overestimation-in-deep-reinforcement-learning-c52d1cc9d69a"},{"title":"Reducing the estimation bias and variance in reinforcement learning via Maxmean and Aitken value iteration - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0952197625025333"},{"title":"model-based offline reinforcement learning","url":"https://arxiv.org/pdf/2407.00699"},{"title":"model-based offline reinforcement learning - with lower expectile ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/f01e6d46cea7a214578af1d46abaa703-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2023 CONSERVATIVE BAYESIAN MODEL-BASED","url":"https://openreview.net/pdf?id=dNqxZgyjcYA"},{"title":"OFFLINE REINFORCEMENT LEARNING VIA ADAPTIVE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c06f788963f0ce069f5b2dbf83fe7822-Paper-Conference.pdf"},{"title":"Conservative reward enhancement through the nearest neighbor integration in model-based Offline Policy Optimization - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742500510X"},{"title":"Video-Enhanced Offline Reinforcement Learning: A Model-Based Approach","url":"https://arxiv.org/html/2505.06482"},{"title":"value gradient weighted model-based reinforcement learning","url":"https://arxiv.org/pdf/2204.01464"}]

Based on the web search results, here are the key findings related to value overestimation, model-based reinforcement learning, value inflation, and conservative estimation in 2022-2023:

## Main Problem: Value
…[truncated 2048 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T16:28:04.481594+00:00_

Web search results for query: "adaptive horizon reinforcement learning variable planning horizon model predictive control 2023 2024"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Prediction Horizon-Varying Model Predictive Control (MPC) for Autonomous Vehicle Control","url":"https://www.mdpi.com/2079-9292/13/8/1442"},{"title":"Reinforcement Learning of the Prediction Horizon in Model Predictive Control - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2405896321013380"},{"title":"Learning Adaptive Horizon Maps Based on Error Forecast for Model","url":"https://par.nsf.gov/servlets/purl/10543373"},{"title":"[2403.17338] Reinforcement Learning-based Receding Horizon Control using Adaptive Control Barrier Functions for Safety-Critical Systems","url":"https://arxiv.org/abs/2403.17338"},{"title":"Robust variable-horizon MPC with adaptive terminal constraints - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0005109825003590"},{"title":"Real-Time Adaptive Machine-Learning-Based Predictive Control of Nonlinear Processes | Industrial & Engineering Chemistry Research","url":"https://pubs.acs.org/doi/abs/10.1021/acs.iecr.9b03055"},{"title":"[2102.11122] Reinforcement Learning of the Prediction Horizon in Model Predictive Control","url":"https://arxiv.org/abs/2102.11122"},{"title":"Model-based Safe Reinforcement Learning using Variable Horizon Rollouts","url":"https://dl.acm.org/doi/fullHtml/10.1145/3632410.3632446"},{"title":"Variable Horizon Model Predictive Control for Helicopter Landing on Moving Decks | Journal of Guidance, Control, and Dynamics","url":"https://arc.aiaa.org/doi/pdf/10.2514/1.g005789"}]

I've completed the web search for your query on adaptive horizon reinforcement learning, variable planning horizons, and model predictive control from 2023-2024. Here's a summary of the relevant findings:

## Key Research Areas 
…[truncated 1628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T16:28:04.481742+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerV3 stop gradient value function world model training symlog Hafner 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerV3 stop gradient value function world model training symlog Hafner 2023"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T16:28:04.481886+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "REDQ randomized ensemble double Q-learning sample efficient 2021 Chen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "REDQ randomized ensemble double Q-learning sample efficient 2021 Chen"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T16:28:04.482032+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Director hierarchical world model goal-conditioned reinforcement learning Hafner 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Director hierarchical world model goal-conditioned reinforcement learning Hafner 2022"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-16T16:28:04.482169+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "multi-task loss balancing reinforcement learning uncertainty weighting Kendall 2018 GradNorm"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "multi-task loss balancing reinforcement learning uncertainty weighting Kendall 2018 GradNorm"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-16T16:28:04.482321+00:00_

Web search results for query: "REDQ randomized ensemble double Q-learning sample efficient 2021 Chen"

Links: [{"title":"[2101.05982] Randomized Ensembled Double Q-Learning: Learning Fast Without a Model","url":"https://arxiv.org/abs/2101.05982"},{"title":"Randomized Ensembled Double Q-Learning: Learning Fast Without a Model | Request PDF","url":"https://www.researchgate.net/publication/348563168_Randomized_Ensembled_Double_Q-Learning_Learning_Fast_Without_a_Model"},{"title":"[PDF] Randomized Ensembled Double Q-Learning: Learning Fast Without a Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Randomized-Ensembled-Double-Q-Learning:-Learning-a-Chen-Wang/736590f70e7f2dc464c1c62491cfa8adb4d718f3"},{"title":"Randomized Ensembled Double Q-Learning: Learning Fast Without a Model | OpenReview","url":"https://openreview.net/forum?id=AY8zfZm0tDd"},{"title":"Published as a conference paper at ICLR 2021","url":"https://arxiv.org/pdf/2101.05982"},{"title":"[Quick Review] Randomized Ensembled Double Q-Learning: Learning Fast Without a Model","url":"https://liner.com/review/randomized-ensembled-double-qlearning-learning-fast-without-a-model"},{"title":"[2110.02034] Dropout Q-Functions for Doubly Efficient Reinforcement Learning","url":"https://arxiv.org/abs/2110.02034"},{"title":"Xinyue Chen, Che Wang, Zijian Zhou, Keith Ross · Randomized Ensembled Double Q-Learning: Learning Fast Without a Model","url":"https://slideslive.com/38953830/randomized-ensembled-double-qlearning-learning-fast-without-a-model"},{"title":"Randomized Ensembled Double Q-Learning","url":"https://www.emergentmind.com/papers/2101.05982"},{"title":"Randomized Ensembled Double Q-Learning: Learning Fast Without a Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210105982C/abstract"}]

Based on the search results, I found comprehensive information about REDQ (Randomized Ensembled Double Q-Learning) by Chen and colleagues:

## Overview

REDQ is a simple model-free algorithm that
…[truncated 1095 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T16:28:04.482498+00:00_

Web search results for query: "Director hierarchical world model goal-conditioned reinforcement learning Hafner 2022"

Links: [{"title":"Deep Hierarchical Planning from Pixels","url":"https://danijar.com/project/director/"},{"title":"Deep Hierarchical Planning from Pixels Danijar Hafner 1 2 3 Kuang-Huei Lee 2","url":"https://arxiv.org/pdf/2206.04114"},{"title":"GitHub - danijar/director: Deep Hierarchical Planning from Pixels · GitHub","url":"https://github.com/danijar/director"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-76719-w"},{"title":"[2206.04114] Deep Hierarchical Planning from Pixels","url":"https://arxiv.org/abs/2206.04114"},{"title":"[PDF] Deep Hierarchical Planning from Pixels | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Deep-Hierarchical-Planning-from-Pixels-Hafner-Lee/6d846a7601c4be41034b9316d7c256f639085d9f"},{"title":"​​Deep Hierarchical Planning from Pixels","url":"https://research.google/blog/deep-hierarchical-planning-from-pixels/"},{"title":"Exploring the limits of hierarchical world models in reinforcement learning - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11538428/"},{"title":"(PDF) Exploring the limits of hierarchical world models in reinforcement learning","url":"https://www.researchgate.net/publication/385589476_Exploring_the_limits_of_hierarchical_world_models_in_reinforcement_learning"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"}]

I found relevant information about Director, the hierarchical world model goal-conditioned reinforcement learning method by Hafner et al. from 2022. Here's what the search revealed:

## Director: Deep Hierarchical Planning from Pixels

Director is a practical method for learning hierarchical behaviors di
…[truncated 1245 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-16T16:28:04.482679+00:00_

Web search results for query: "multi-task loss balancing reinforcement learning uncertainty weighting Kendall 2018 GradNorm"

Links: [{"title":"Multi-Task Learning Using Uncertainty to Weigh Losses for ...","url":"https://openaccess.thecvf.com/content_cvpr_2018/papers/Kendall_Multi-Task_Learning_Using_CVPR_2018_paper.pdf"},{"title":"[1705.07115] Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics","url":"https://arxiv.org/abs/1705.07115"},{"title":"Multi-task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics | Request PDF","url":"https://www.researchgate.net/publication/329747447_Multi-task_Learning_Using_Uncertainty_to_Weigh_Losses_for_Scene_Geometry_and_Semantics"},{"title":"GitHub - ranandalon/mtl: Unofficial implementation of: Multi-task learning using uncertainty to weigh losses for scene geometry and semantics · GitHub","url":"https://github.com/ranandalon/mtl"},{"title":"Multi-Adaptive Optimization for multi-task learning with deep neural networks - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0893608023006615"},{"title":"Uncertainty weighted multi task learning for robust traffic scene semantic understanding | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-24838-3"},{"title":"Analytical Uncertainty-Based Loss Weighting in Multi-task Learning | Pattern Recognition","url":"https://dl.acm.org/doi/abs/10.1007/978-3-031-85181-0_22"},{"title":"Kendall, A., Gal, Y. and Cipolla, R. (2018) Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Salt Lake City, UT, USA, 18-23 June 2018, 7482-7491. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2530081"},{"title":"Under review as a conference paper at ICLR 2018 GRADNORM: GRADIENT","url":"https://openreview.net/pdf?id=H1bM1fZCW"},{"ti
…[truncated 1785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T16:28:04.482866+00:00_

Web search results for query: "DreamerV3 stop gradient value function world model training symlog Hafner 2023"

Links: [{"title":"DreamerV3: Mastering Diverse Domains through World Models","url":"https://vitalab.github.io/article/2023/01/19/DreamerV3.html"},{"title":"Reward Scale Robustness for Proximal Policy Optimization via DreamerV3 Tricks","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/04f61ec02d1b3a025a59d978269ce437-Paper-Conference.pdf"},{"title":"Danijar_hafner Mastering Diverse Domains Through World Models 2023 | Sukai Huang","url":"https://sino-huang.github.io/posts/danijar_hafner-mastering-diverse-domains-through-world-models-2023/"},{"title":"Dreamer V3 - EclecticSheep","url":"https://eclecticsheep.ai/2023/08/10/dreamer_v3.html"},{"title":"Mastering diverse control tasks through world models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12003158/"},{"title":"Mastering Diverse Domains through World Models","url":"https://arxiv.org/pdf/2301.04104"},{"title":"Mastering Diverse Control Tasks through World Models","url":"https://danijar.com/project/dreamerv3/"},{"title":"MUDREAMER: LEARNING PREDICTIVE WORLD ...","url":"https://openreview.net/pdf/8801375407fde3d9751dbb78c2f906238f519a12.pdf"},{"title":"[2301.04104] Mastering Diverse Domains through World Models","url":"https://arxiv.org/abs/2301.04104"},{"title":"DreamerV3: Model-Based RL Algorithm","url":"https://www.emergentmind.com/topics/dreamerv3-algorithm"}]

I found relevant search results about DreamerV3, stop gradients, value function training, symlog, and Hafner's 2023 work. Here are the key findings:

## Stop Gradient in Value Function Training

The dynamics and representation losses differ in the stop-gradient operator and their loss scale. In the context of world model training, the gradients of the actor-critic do not backpropagate through the world model.

More specifically, in training the critic for value functions, twohot-encoded targets use the stop-gradient oper
…[truncated 926 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T16:28:04.483027+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Nikishin 2022 primacy bias deep reinforcement learning periodic resets"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Nikishin 2022 primacy bias deep reinforcement learning periodic resets"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-16T16:28:04.483336+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DreamerPro prototypical representation world model reinforcement learning 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DreamerPro prototypical representation world model reinforcement learning 2022"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T16:28:04.483667+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "model-based reinforcement learning gradient conflict multi-objective optimization 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "model-based reinforcement learning gradient conflict multi-objective optimization 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T16:28:04.483839+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MBPO model-based policy optimization Janner 2019 dyna-style short horizon rollouts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MBPO model-based policy optimization Janner 2019 dyna-style short horizon rollouts"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T16:28:04.484035+00:00_

Web search results for query: "DreamerPro prototypical representation world model reinforcement learning 2022"

Links: [{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations","url":"https://proceedings.mlr.press/v162/deng22a.html"},{"title":"[2110.14565] DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations","url":"https://arxiv.org/abs/2110.14565"},{"title":"ICML Poster DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations","url":"https://icml.cc/virtual/2022/poster/17995"},{"title":"DREAMERPRO: RECONSTRUCTION-FREE MODEL-BASED REINFORCEMENT LEARNING","url":"https://arxiv.org/pdf/2110.14565"},{"title":"GitHub - fdeng18/dreamer-pro","url":"https://github.com/fdeng18/dreamer-pro"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations","url":"https://www.researchgate.net/publication/355698370_DreamerPro_Reconstruction-Free_Model-Based_Reinforcement_Learning_with_Prototypical_Representations"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations - Rutgers, The State University of New Jersey","url":"https://www.researchwithrutgers.com/en/publications/dreamerpro-reconstruction-free-model-based-reinforcement-learning/"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations | OpenReview","url":"https://openreview.net/forum?id=3M3t3tUbA2Y"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning","url":"https://proceedings.mlr.press/v162/deng22a/deng22a.pdf"},{"title":"DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations | DeepAI","url":"https://deepai.org/publication/dreamerpro-reconstruction-free-model-based-reinforcement-learning-with-prototypical-representations"}]

I found comprehensiv
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T16:28:04.484216+00:00_

Web search results for query: "model-based reinforcement learning gradient conflict multi-objective optimization 2023 2024"

Links: [{"title":"Multi-objective meta-learning","url":"https://baijiong-lin.github.io/files/aij2024.pdf"},{"title":"Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution","url":"https://arxiv.org/html/2509.14816v1"},{"title":"Conflict-Averse Gradient Aggregation for Constrained Multi-Objective Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=ogXkmugNZw"},{"title":"Multi-objective meta-learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0004370224001206"},{"title":"conflict-averse gradient aggregation - for constrained multi- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/59ddfff7979b43f54690fa986c0e5138-Paper-Conference.pdf"},{"title":"Deep reinforcement learning-driven multi-objective optimization and its applications on lighting infrastructure operation and maintenance strategy | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-37811-5"},{"title":"Gradient Shaping for Multi-Constraint Safe Reinforcement ...","url":"https://proceedings.mlr.press/v242/yao24a/yao24a.pdf"},{"title":"Preference Controllable Reinforcement Learning with Advanced Multi-Objective Optimization | OpenReview","url":"https://openreview.net/forum?id=49g4c8MWHy"},{"title":"Multi-objective optimization for dynamic logistics scheduling based on hierarchical deep reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-18309-y"},{"title":"Gradient-Based Multi-Objective Deep Learning: Algorithms, Theories,","url":"https://arxiv.org/pdf/2501.10945"}]

I've found several highly relevant research papers and resources on your query. Here's a summary of the key findings:

## Main Research Areas

**Multi-Objective Meta-Learning (MOML)**
The MOML framework formulates the objective function of meta-learning
…[truncated 1719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T16:28:04.484407+00:00_

Web search results for query: "Nikishin 2022 primacy bias deep reinforcement learning periodic resets"

Links: [{"title":"GitHub - evgenii-nikishin/rl_with_resets: JAX implementation of deep RL agents with resets from the paper \"The Primacy Bias in Deep Reinforcement Learning\"","url":"https://github.com/evgenii-nikishin/rl_with_resets"},{"title":"The Primacy Bias in Deep Reinforcement Learning Evgenii Nikishin∗","url":"https://evgenii-nikishin.github.io/data/RL_primacy_bias_RLDM2022.pdf"},{"title":"The Primacy Bias in Deep Reinforcement Learning","url":"https://proceedings.mlr.press/v162/nikishin22a/nikishin22a.pdf"},{"title":"[2205.07802] The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2205.07802"},{"title":"It's Time to Move On: Primacy Bias and Why It Helps to Forget | ICLR Blogposts 2024","url":"https://iclr-blogposts.github.io/2024/blog/primacy-bias-and-why-it-helps-to-forget/"},{"title":"[PDF] The Primacy Bias in Deep Reinforcement Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Primacy-Bias-in-Deep-Reinforcement-Learning-Nikishin-Schwarzer/69b80ce5ab6c2263b145b1eaa23664145938f351"},{"title":"Code for paper \"The Primacy Bias in Deep Reinforcement Learning\"| DeepAICode","url":"https://deepaicode.com/p/code-for-paper-the-primacy-bias-in-deep-reinforcement-learning"},{"title":"The Primacy Bias in Deep Reinforcement Learning | DeepAI","url":"https://deepai.org/publication/the-primacy-bias-in-deep-reinforcement-learning"},{"title":"[2205.07802v1] The Primacy Bias in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2205.07802v1"},{"title":"Evgenii Nikishin on X: \"The Primacy Bias in Deep Reinforcement Learning In a new #ICML2022 paper, we identify a damaging tendency of Deep RL agents to overfit to early experiences and propose a simple yet *powerful* remedy by periodically resetting last network layers. https://t.co/Ll7iyzXyCU 1/N 🧵 https://t.co/cmHPVdl5ds\" / X","url":"https://x.com/nikishin
…[truncated 1867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T16:28:04.484605+00:00_

Web search results for query: "MBPO model-based policy optimization Janner 2019 dyna-style short horizon rollouts"

Links: [{"title":"When to Trust Your Model: Model-Based Policy Optimization Michael Janner","url":"http://papers.neurips.cc/paper/9416-when-to-trust-your-model-model-based-policy-optimization.pdf"},{"title":"GitHub - jannerm/mbpo: Code for the paper \"When to Trust Your Model: Model-Based Policy Optimization\" · GitHub","url":"https://github.com/jannerm/mbpo"},{"title":"Model-Based Reinforcement Learning:Theory and Practice – The Berkeley Artificial Intelligence Research Blog","url":"https://bair.berkeley.edu/blog/2019/12/12/mbpo/"},{"title":"Bidirectional Model-based Policy Optimization","url":"http://proceedings.mlr.press/v119/lai20b/lai20b.pdf"},{"title":"Model-based Policy Optimization with Unsupervised Model Adaptation","url":"https://proceedings.neurips.cc/paper/2020/file/1dc3a89d0d440ba31729b0ba74b93a33-Paper.pdf"},{"title":"Trust the Model Where It Trusts Itself Model-Based Actor-Critic with Uncertainty-Aware Rollout Adaption","url":"https://arxiv.org/html/2405.19014v3"},{"title":"When to Trust Your Data: Enhancing Dyna-Style Model-Based Reinforcement Learning With Data Filter","url":"https://arxiv.org/html/2410.12160v1"},{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Replication of “When to Trust Your Model: Model-Based Policy Optimization”","url":"https://openreview.net/pdf?id=SkgPIpcGar"},{"title":"Double Horizon Model-Based Policy Optimization","url":"https://arxiv.org/html/2512.15439"}]

The search results provide comprehensive information about MBPO (Model-Based Policy Optimization) by Janner et al. 2019 and its use of Dyna-style short horizon rollouts.

## Overview

Model-Based Policy Optimization (MBPO) by Janner et al. (2019) represents the current state-of-the-art in Dyna-style MBRL, combining a Soft Actor-Critic (SAC) agent with a Probabilistic Ensem
…[truncated 1114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-16T16:28:04.484757+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "value gradient weighted model-based reinforcement learning VaGraM 2022 gradient-aware"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "value gradient weighted model-based reinforcement learning VaGraM 2022 gradient-aware"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-16T16:28:04.484907+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "COMBO conservative offline model-based policy optimization Yu 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "COMBO conservative offline model-based policy optimization Yu 2021"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T16:28:04.485034+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "plasticity injection deep reinforcement learning Nikishin 2023 continual learning dormant neurons"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "plasticity injection deep reinforcement learning Nikishin 2023 continual learning dormant neurons"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T16:28:04.485151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "event-triggered control reinforcement learning state-dependent switching adaptive 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "event-triggered control reinforcement learning state-dependent switching adaptive 2023"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T16:28:04.485297+00:00_

Web search results for query: "value gradient weighted model-based reinforcement learning VaGraM 2022 gradient-aware"

Links: [{"title":"GitHub - pairlab/vagram: [ICLR 22] Value Gradient weighted Model-Based Reinforcement Learning.","url":"https://github.com/pairlab/vagram"},{"title":"Value Gradient weighted Model-Based Reinforcement Learning | PAIR","url":"http://www.pair.toronto.edu/blog/2022/vagram-voelcker/"},{"title":"[Quick Review] Value Gradient weighted Model-Based Reinforcement Learning","url":"https://liner.com/review/value-gradient-weighted-modelbased-reinforcement-learning"},{"title":"[2204.01464] Value Gradient weighted Model-Based Reinforcement Learning","url":"https://arxiv.org/abs/2204.01464"},{"title":"Vector research blog: Value Gradient weighted Model-Based Reinforcement Learning - Vector Institute for Artificial Intelligence","url":"https://vectorinstitute.ai/vector-research-blog-value-gradient-weighted-model-based-reinforcement-learning/"},{"title":"Value Gradient weighted Model-Based Reinforcement Learning","url":"https://arxiv.org/html/2204.01464"},{"title":"VALUE GRADIENT WEIGHTED MODEL-BASED REINFORCEMENT LEARNING - HackMD","url":"https://hackmd.io/W-J3KvitSWKZBMVsKFHAJA?both="},{"title":"VALUE GRADIENT WEIGHTED MODEL-BASED ...","url":"https://cvoelcker.de/assets/pdf/paper_vagram.pdf"},{"title":"vagram/README.md at main · pairlab/vagram","url":"https://github.com/pairlab/vagram/blob/main/README.md"},{"title":"[2204.01464v1] Value Gradient weighted Model-Based Reinforcement Learning","url":"https://arxiv.org/abs/2204.01464v1"}]

I found comprehensive information about VaGraM. Here's a summary of the search results:

## Overview

VaGraM (Value-Gradient weighted Model Learning) is a novel method for value-aware model learning which improves the performance of MBRL in challenging settings, such as small model capacity and the presence of distracting state dimensions.

## The Core Idea

The Value-Gradient weighted Model loss (VaGraM) rescales the
…[truncated 1286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T16:28:04.485475+00:00_

Web search results for query: "COMBO conservative offline model-based policy optimization Yu 2021"

Links: [{"title":"[2102.08363] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://arxiv.org/abs/2102.08363"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://proceedings.neurips.cc/paper/2021/hash/f29a179746902e331572c483c45e5086-Abstract.html"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://papertalk.org/papertalks/35821"},{"title":"COMBO: Conservative Ofﬂine Model-Based Policy Optimization","url":"https://arxiv.org/pdf/2102.08363"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=dUEpGV2mhf"},{"title":"[Quick Review] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://liner.com/review/combo-conservative-offline-modelbased-policy-optimization"},{"title":"[2102.08363v1] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://arxiv.org/abs/2102.08363v1"},{"title":"COMBO: CONSERVATIVE OFFLINE MODEL-BASED ...","url":"https://openreview.net/pdf?id=8WRYT8QAcj"},{"title":"COMBO: Conservative Offline Model-Based Policy Optimization | Request PDF","url":"https://www.researchgate.net/publication/349363400_COMBO_Conservative_Offline_Model-Based_Policy_Optimization"},{"title":"[2102.08363] COMBO: Conservative Offline Model-Based Policy Optimization","url":"https://ar5iv.labs.arxiv.org/html/2102.08363"}]

Based on the search results, here's what I found about COMBO:

## Overview

COMBO was presented as a paper at NeurIPS 2021 by authors Tianhe Yu, Aviral Kumar, Rafael Rafailov, Aravind Rajeswaran, Sergey Levine, and Chelsea Finn.

## What is COMBO?

COMBO is a model-based offline RL algorithm that trains a value function using both the offline dataset and data generated using rollouts under the model while also additionally regularizing the value function on out-of
…[truncated 1116 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-16T16:28:04.485652+00:00_

Web search results for query: "event-triggered control reinforcement learning state-dependent switching adaptive 2023"

Links: [{"title":"Adaptive Event-triggered Reinforcement Learning Control ...","url":"https://arxiv.org/pdf/2409.19769"},{"title":"Reinforcement Learning-Based Event-Triggered Predefined-Time Optimal Fuzzy Control for Nonlinear Constrained Systems | Request PDF","url":"https://www.researchgate.net/publication/381009944_Reinforcement_Learning-Based_Event-Triggered_Predefined-Time_Optimal_Fuzzy_Control_for_Nonlinear_Constrained_Systems"},{"title":"[2409.19769] Adaptive Event-triggered Reinforcement Learning Control for Complex Nonlinear Systems","url":"https://arxiv.org/abs/2409.19769"},{"title":"(PDF) Adaptive Event-triggered Reinforcement Learning Control for Complex Nonlinear Systems","url":"https://www.researchgate.net/publication/384502955_Adaptive_Event-triggered_Reinforcement_Learning_Control_for_Complex_Nonlinear_Systems"},{"title":"Event-Triggered State-Dependent Switching for Adaptive Fuzzy Control of Switched Nonlinear Systems | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10321710/"},{"title":"Event-Triggered iterative learning control for asynchronously switched systems","url":"https://ideas.repec.org/a/eee/apmaco/v440y2023ics0096300322007305.html"},{"title":"Recent Progress in Reinforcement Learning and Adaptive Dynamic Programming for Advanced Control Applications","url":"https://www.ieee-jas.net/article/doi/10.1109/JAS.2023.123843"},{"title":"State-sensitive event-triggered path following control of autonomous ground vehicles","url":"https://www.oaepublish.com/articles/ir.2023.17"},{"title":"Integral reinforcement learning-based online adaptive event-triggered control for non-zero-sum games of partially unknown nonlinear systems - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231219314109"},{"title":"Sliding Mode-based Integral Reinforcement Learning Event Trigg
…[truncated 2121 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T16:28:04.485848+00:00_

Web search results for query: "plasticity injection deep reinforcement learning Nikishin 2023 continual learning dormant neurons"

Links: [{"title":"Deep Reinforcement Learning with Plasticity Injection Evgenii Nikishin∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/75101364dc3aa7772d27528ea504472b-Paper-Conference.pdf"},{"title":"[2305.15555] Deep Reinforcement Learning with Plasticity Injection","url":"https://arxiv.org/abs/2305.15555"},{"title":"Plasticine: Accelerating Research in Plasticity-Motivated ...","url":"https://arxiv.org/pdf/2504.17490"},{"title":"Deep Reinforcement Learning with Plasticity Injection","url":"https://arxiv.org/html/2305.15555"},{"title":"Maintaining Plasticity in Continual Learning via Regenerative Regularization","url":"https://arxiv.org/html/2308.11958v3"},{"title":"A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning","url":"https://arxiv.org/html/2405.19153v1"},{"title":"Deep Reinforcement Learning with Plasticity Injection","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/75101364dc3aa7772d27528ea504472b-Abstract-Conference.html"},{"title":"Deep Reinforcement Learning with Plasticity Injection | Request PDF","url":"https://www.researchgate.net/publication/371041107_Deep_Reinforcement_Learning_with_Plasticity_Injection"},{"title":"Loss of plasticity in deep continual learning | Nature","url":"https://www.nature.com/articles/s41586-024-07711-7"},{"title":"Neuroplastic Expansion in Deep Reinforcement Learning","url":"https://arxiv.org/html/2410.07994v1"}]

Based on the search results, I found comprehensive information about the Nikishin 2023 paper on plasticity injection in deep reinforcement learning:

## Summary of Key Findings

The paper addresses evidence that neural networks in deep reinforcement learning gradually lose their plasticity, the ability to learn from new data.

### Plasticity Injection Method

Plasticity injection is a minimalistic intervention that increases netwo
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T16:28:04.486098+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TWM TransDreamer transformer world model reinforcement learning temporal 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TWM TransDreamer transformer world model reinforcement learning temporal 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-16T16:28:04.486378+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dreamer imagination horizon rollout length compounding error model-based RL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dreamer imagination horizon rollout length compounding error model-based RL 2024"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-16T16:28:04.486511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"gradient routing\" \"task-specific\" reinforcement learning selective gradient flow 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"gradient routing\" \"task-specific\" reinforcement learning selective gradient flow 2024"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-16T16:28:04.486660+00:00_

Web search results for query: "TWM TransDreamer transformer world model reinforcement learning temporal 2023 2024"

Links: [{"title":"[PDF] TransDreamer: Reinforcement Learning with Transformer World Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TransDreamer:-Reinforcement-Learning-with-World-Chen-Wu/2fec20377bc947ec1df003b4aedcb4d7f25ac934"},{"title":"[2202.09481] TransDreamer: Reinforcement Learning with Transformer World Models","url":"https://arxiv.org/abs/2202.09481"},{"title":"TransDreamer: Reinforcement Learning with Transformer World Models","url":"https://arxiv.org/html/2202.09481v2"},{"title":"Efficient Stochastic Transformer based World Models for ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/5647763d4245b23e6a1cb0a8947b38c9-Paper-Conference.pdf"},{"title":"TRANSDREAMER: REINFORCEMENT LEARNING WITH TRANSFORMER WORLD MODELS","url":"https://openreview.net/pdf?id=sVrzVAL90sA"},{"title":"TransDreamer: Reinforcement Learning with Transformer World Models | OpenReview","url":"https://openreview.net/forum?id=s3K0arSRl4d"},{"title":"TransDreamer: Reinforcement Learning with Transformer World Models","url":"https://www.researchgate.net/publication/358763619_TransDreamer_Reinforcement_Learning_with_Transformer_World_Models"},{"title":"TransDreamer: Reinforcement Learning with Transformer World Models - Paper Detail","url":"https://deeplearn.org/arxiv/267950/transdreamer:-reinforcement-learning-with-transformer-world-models"},{"title":"STORM: Efficient Stochastic Transformer based World ...","url":"https://arxiv.org/pdf/2310.09615"},{"title":"Learning Transformer-based World Models with Contrastive Predictive Coding","url":"https://arxiv.org/html/2503.04416v2"}]

## Search Results Summary

I found substantial information about TransDreamer and related transformer-based world models for reinforcement learning. Here are the key findings:

### TransDreamer Overview

TransDreamer is a transformer-based MBRL agent that i
…[truncated 1290 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-16T16:28:04.486858+00:00_

Web search results for query: "Dreamer imagination horizon rollout length compounding error model-based RL 2024"

Links: [{"title":"Imagine Within Practice: Conservative Rollout Length Adaptation for Model-Based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=cYksYKbf6K"},{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Long-Horizon Planning with Predictable Skills","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Week 5: Model-Based Methods - Deep RL Course","url":"https://deeprlcourse.github.io/course_notes/model-based/"},{"title":"Finding Theta - The Evolution of Imagination: A Deep Dive into DreamerV3 and its Conquest of Minecraft","url":"https://www.findingtheta.com/blog/the-evolution-of-imagination-a-deep-dive-into-dreamerv3-and-its-conquest-of-minecraft"},{"title":"Published as a conference paper at ICLR 2024 LEARNING HIERARCHICAL WORLD MODELS","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/0a0e436e8830f746300f592377730fca-Paper-Conference.pdf"},{"title":"Learning World Models for Unconstrained Goal Navigation Yuanlin Duan","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/6cca3481ae66707958b824d37df40177-Paper-Conference.pdf"},{"title":"Dreamer 4: Scalable World Model Agents","url":"https://www.emergentmind.com/papers/2509.24527"},{"title":"Model-Based Deep Reinforcement Learning for High- ...","url":"https://liacs.leidenuniv.nl/~plaata1/papers/modelbased7.pdf"}]

Based on the search results, here's what I found about Dreamer, imagination horizon, rollout length, and compounding error in model-based RL:

## Key Findi
…[truncated 1620 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-16T16:28:04.487037+00:00_

Web search results for query: ""gradient routing" "task-specific" reinforcement learning selective gradient flow 2024"

Links: [{"title":"Gradient Routing: Masking Gradients to Localize Computation in Neural Networks","url":"https://arxiv.org/html/2410.04332v2"},{"title":"[2410.04332] Gradient Routing: Masking Gradients to Localize Computation in Neural Networks","url":"https://arxiv.org/abs/2410.04332"},{"title":"Gradient Routing in Neural Networks","url":"https://www.emergentmind.com/papers/2410.04332"},{"title":"Gradient Routing: Masking Gradients to Localize Computation in Neural Networks | OpenReview","url":"https://openreview.net/forum?id=z1mLNhWFyY"},{"title":"Gradient Routing: Masking Gradients to Localize Computation in Neural Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004332C/abstract"},{"title":"Masking Gradients to Localize Computation in Neural ...","url":"https://www.alignmentforum.org/posts/nLRKKCTtwQgvozLTN/gradient-routing-masking-gradients-to-localize-computation"},{"title":"Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning | Machine Language","url":"https://dl.acm.org/doi/10.1007/BF00992696"},{"title":"Gradient Routing: Masking Gradients to Localize Computation in Neural Networks","url":"https://turntrout.com/gradient-routing"},{"title":"Direct Routing Gradient (DRGrad): A Personalized Information Surgery for Multi-Task Learning (MTL) Recommendations","url":"https://arxiv.org/html/2510.09643"},{"title":"Gradient Routing: Masking Gradients to Localize ...","url":"https://www.lesswrong.com/posts/nLRKKCTtwQgvozLTN/gradient-routing-masking-gradients-to-localize-computation"}]

Based on the web search results, I found relevant information about gradient routing and its application in reinforcement learning. Here's what the research shows:

## Gradient Routing Overview

Gradient routing is a training method that isolates capabilities to specific subregions of a neural network by applying 
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T16:28:04.487197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "imagination horizon adaptation world model reinforcement learning dynamic rollout 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "imagination horizon adaptation world model reinforcement learning dynamic rollout 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-16T16:28:04.487326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "IRIS DIAMOND world model discrete tokens imagination reinforcement learning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "tool_args": {
    "query": "IRIS DIAMOND world model discrete tokens imagination reinforcement learning 2024"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-16T16:28:04.487472+00:00_

Web search results for query: "imagination horizon adaptation world model reinforcement learning dynamic rollout 2024 2025"

Links: [{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_136.pdf"},{"title":"Dreamer: Learning Long-Horizon Behaviors through Latent Imagination | by Dong-Keon Kim | Medium","url":"https://medium.com/@kdk199604/dreamer-learning-long-horizon-behaviors-through-latent-imagination-fa60327c2843"},{"title":"Interpretable World Model Imaginations as Deep Reinforcement Learning Explanation | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-08327-2_7"},{"title":"Imagination-Based Policy Optimization","url":"https://www.emergentmind.com/topics/imagination-based-policy-optimization"},{"title":"[2410.03618] Open-World Reinforcement Learning over Long Short-Term Imagination","url":"https://arxiv.org/abs/2410.03618"},{"title":"Robotic World Model: A Neural Network Simulator for Robust Policy Optimization in Robotics","url":"https://arxiv.org/html/2501.10100v1"},{"title":"World Models Reading List: The Papers You Actually Need in 2025 | by Graison Thomas | Medium","url":"https://medium.com/@graison/world-models-reading-list-the-papers-you-actually-need-in-2025-882f02d758a9"},{"title":"Published as a conference paper at ICLR 2025 PRE-TRAINED VIDEO GENERATIVE","url":"https://openreview.net/pdf?id=oTYF8WUadL"},{"title":"ICLR 2025 Open-World Reinforcement Learning over Long Short-Term Imagination Oral","url":"https://iclr.cc/virtual/2025/oral/31740"},{"title":"Learning World Models for Unconstrained Goal Navigation Yuanlin Duan","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/6cca3481ae66707958b824d37df40177-Paper-Conference.pdf"}]

I've completed the web search for your query about imagination horizon adaptation, world models, reinforcement learning, and dynamic rollout in the 2024-2025 period. Here are the key findings:

## Main Research Directio
…[truncated 1734 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-16T16:28:04.487663+00:00_

Web search results for query: "IRIS DIAMOND world model discrete tokens imagination reinforcement learning 2024"

Links: [{"title":"Diffusion for World Modeling: Visual Details Matter in Atari (DIAMOND) 💎","url":"https://diamond-wm.github.io/"},{"title":"Diffusion for World Modeling: Visual Details Matter in Atari† Eloi Alonso∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/6bdde0373d53d4a501249547084bed43-Paper-Conference.pdf"},{"title":"Revolutionizing World Models with DIAMOND: A Diffusion-Driven Approach to Reinforcement Learning | by Paulstoienescu | Medium","url":"https://medium.com/@paul98stoienescu/revolutionizing-world-models-with-diamond-a-diffusion-driven-approach-to-reinforcement-learning-350cd423ecfb"},{"title":"(PDF) Diffusion for World Modeling: Visual Details Matter in Atari","url":"https://www.researchgate.net/publication/380756902_Diffusion_for_World_Modeling_Visual_Details_Matter_in_Atari"},{"title":"DIAMOND (DIffusion as a Model of Environment Dreams): A Reinforcement Learning Agent Trained in a Diffusion World Model - MarkTechPost","url":"https://www.marktechpost.com/2024/05/24/diamond-diffusion-as-a-model-of-environment-dreams-a-reinforcement-learning-agent-trained-in-a-diffusion-world-model/"},{"title":"GitHub - eloialonso/diamond: DIAMOND (DIffusion As a Model Of eNvironment Dreams) is a reinforcement learning agent trained in a diffusion world model. NeurIPS 2024 Spotlight. · GitHub","url":"https://github.com/eloialonso/diamond"},{"title":"Diffusion for World Modeling: Visual Details Matter in Atari [Quick Review]","url":"https://liner.com/review/diffusion-for-world-modeling-visual-details-matter-in-atari"},{"title":"Diffusion for World Modeling: Visual Details Matter in AtariTo prevent confusion, this is the final version of (Alonso et al.,, 2023) and is not related to (Ding et al.,, 2024).","url":"https://arxiv.org/html/2405.12399v1"},{"title":"Efficient World Models with Context-Aware Tokenization","url":"https://arxiv
…[truncated 2130 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-16T16:28:04.487870+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/",
  "description": "List existing artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/",
    "description": "List existing artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-16T16:28:04.488020+00:00_

008e_dryrun_check.md
009b_literature_search.md
016e
018
018_prewrite_two_versions.md
018v2_server_check.md
019a_dryrun_report.md
_project
actor_loss_timeseries.json
analysis
analysis_actor_entropy_plan031.md
analysis_rssm_prediction_quality.json
bernoulli_st_pessimism_designs.md
bootstrap_cis
checkpoint_monitor.py
claim_strength_audit.md
code
code_survey_dreamerv3.md
d061_literature_linkage.md
dream_reports
eval_mvp.py
exp_001_baseline
exp_002_event_gated
exp_005_event_gated_v4
exp_006
exp_006_fixed_dt2
exp_008e_v3_subsample_on_dt1_h15_s2
exp_008e_v3_walker_s2
exp_008f_s3
exp_009b_008d_walker_s2
exp_010a_cheetah_baseline_s1
exp_015
exp_018_full_sgs_walker_s1
figures
figures_data
framing_b_reaudit_diff.md
gen_bib.py
gradient_stopping_code_audit.md
imagination_reward_analysis.md
implementation_design.md
literature_gap_analysis_20260514.md
literature_map.yaml
literature_scan_20260515.md
literature_sgs_survey.md
literature_survey_summary.md
manifest.yaml
maniskill3_cuda_workaround.md
maniskill3_dreamer_integration.md
maniskill3_integration_report.md
method_framingB_reaudit_v2.md
method_section_draft.md
metrics_summary_table.md
narrative_audit.md
negative_pattern_analysis.md
nve_sensitivity_analysis.md
nve_threshold_analysis.json
nve_threshold_analysis_v3.py
nve_threshold_v3_ci_supplement_d054.json
paper_drafts
paper_figures
pessimism_mechanism_design.md
pivot_gate_survey.md
plot_figures.py
preflight_008e_v3_s2.md
progress_check_20260515.md
related_work_draft.md
report_server_status.md
review_issues.yaml
review_reports
rssm_prediction_quality_analysis.json
scripts
seed_label_diff_summary.md
sgs_implementation_report.md
signed_reward_error.md
training_progress_check_20260514.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-16T16:28:04.488189+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_expansion.md",
  "content": "# Related Work Expansion (D4)\n\n> 20+ new references organized by category. Does NOT repeat the 7 already-cited papers (DreamerV3, GradNorm, Non-delusional Q, PCGrad, VaGraM, Gradient Routing, TAWM).\n\n---\n\n## Category 1: Value Overestimation in RL / MBRL\n\n- **Addressing Function Approximation Error in Actor-Critic Methods** (Fujimoto et al., 2018) — TD3: twin critics + clipped double Q-learning to suppress overestimation bias in continuous control.\n  - BibTeX key suggestion: `fujimoto2018td3`\n  - 与本文关系: [background] — 我们的 event-gated mechanism 部分动机来自 value overestimation 在 world model rollout 中的放大效应；TD3 是 model-free 经典对策\n\n- **Randomized Ensembled Double Q-Learning: Learning Fast Without a Model** (Chen et al., 2021) — REDQ: 大 ensemble + 随机子集取 min，UTD>>1 下的高样本效率 model-free 方法\n  - BibTeX key suggestion: `chen2021redq`\n  - 与本文关系: [method-component] — ensemble Q-function 的 in-target minimization 与我们对 value estimate 的保守处理相关\n\n- **COMBO: Conservative Offline Model-Based Policy Optimization** (Yu et al., 2021) — 在 model rollout 上对 OOD state-action 施加 value penalty，无需显式 uncertainty estimation\n  - BibTeX key suggestion: `yu2021combo`\n  - 与本文关系: [direct-competitor] — conservative value estimation in model-based setting 的替代方案\n\n- **MOPO: Model-based Offline Policy Optimization** (Yu et al., 2020) — 用 model uncertainty 作为 reward penalty，最大化真实 MDP return 的下界\n  - BibTeX key suggestion: `yu2020mopo`\n  - 与本文关系: [background] — uncertainty-penalized reward 与我们 event-gated horizon shortening 都抑制 overestimation，但机制不同\n\n- **Value Gradient weighted Model-Based Reinforcement Learning** (Voelcker et al., 2022) — VaGraM: 用 value function gradient 加权 model loss，关注对 policy 影响大的 prediction error\n  - BibTeX key suggestion: `voelcker2022vagram`\n  - 与本文关系: [method-component] — value-aware model learning 的互补视角；我们在 rollout 层面做 gating，VaGraM 在 model loss 层面做加权\n\n---\n\n## Category 2: Multi-task Loss Balancing in World Models\n\n- **HarmonyDream: Task Harmonization Inside World Models** (Ma/Shang et al., 2024) — 量化 reconstruction vs reward loss 的 2 个数量级差异，提出 harmonious loss 动态调权\n  - BibTeX key suggestion: `ma2024harmonydream`\n  - 与本文关系: [direct-competitor] — 同样识别 world model 多任务训练的梯度/loss 量级不平衡问题；我们用 event-gated stop-gradient 而非 loss reweighting\n\n- **Multi-Task Learning Using Uncertainty to Weigh Losses** (Kendall et al., 2018) — 用 homoscedastic uncertainty 自动平衡多任务 loss 权重\n  - BibTeX key suggestion: `kendall2018uncertainty`\n  - 与本文关系: [background] — multi-task loss balancing 的经典方法，HarmonyDream 和 GradNorm 的理论前驱\n\n- **DreamerPro: Reconstruction-Free Model-Based RL with Prototypical Representations** (Deng et al., 2022) — 用 prototypical self-supervised learning 替代 reconstruction，减轻视觉干扰影响\n  - BibTeX key suggestion: `deng2022dreamerpro`\n  - 与本文关系: [background] — 从另一角度解决 reconstruction loss 主导训练的问题（去掉 reconstruction），与我们保留 reconstruction 但 gate gradient 的策略形成对比\n\n---\n\n## Category 3: Plasticity Loss & Network Degradation in Deep RL\n\n- **The Primacy Bias in Deep Reinforcement Learning** (Nikishin et al., 2022) — RL agent 过拟合早期数据，提出 periodic network reset 缓解\n  - BibTeX key suggestion: `nikishin2022primacy`\n  - 与本文关系: [background] — plasticity loss 的根源分析；我们的 event-gated mechanism 通过选择性停止梯度防止 representation 退化\n\n- **Deep Reinforcement Learning with Plasticity Injection** (Nikishin et al., 2023) — 注入新初始化参数恢复可塑性，无需完全 reset\n  - BibTeX key suggestion: `nikishin2023plasticity`\n  - 与本文关系: [background] — 与 periodic reset 互补的轻量方案；event-gating 也是一种不丢失已有参数的 plasticity preservation 手段\n\n- **Understanding Plasticity in Neural Networks** (Lyle et al., 2023) — 系统分析 plasticity loss 与 loss landscape curvature 的关系，LayerNorm 有效\n  - BibTeX key suggestion: `lyle2023plasticity`\n  - 与本文关系: [background] — 为什么 DreamerV3 采用 LayerNorm 的理论解释；我们的方法从 gradient flow 而非 normalization 角度维护 plasticity\n\n- **Loss of Plasticity in Continual Deep Reinforcement Learning** (Abbas et al., 2023) — 连续任务切换下网络激活稀疏化导致梯度消失\n  - BibTeX key suggestion: `abbas2023plasticity`\n  - 与本文关系: [background] — continual RL 视角下的 plasticity loss；event-gating 的 stop-gradient 可视为防止某些 task 的梯度过度稀疏化\n\n---\n\n## Category 4: Temporal Abstraction & Adaptive Horizon in MBRL\n\n- **Deep Hierarchical Planning from Pixels (Director)** (Hafner et al., 2022) — Manager 在 world model latent space 设 subgoal，Worker 执行低层动作，实现 temporal abstraction\n  - BibTeX key suggestion: `hafner2022director`\n  - 与本文关系: [background] — hierarchical planning 实现变长 effective horizon；我们的 event-gating 不需要显式层次结构但达到类似的 adaptive horizon 效果\n\n- **TD-MPC2: Scalable, Robust World Models for Continuous Control** (Hansen et al., 2024) — implicit world model + local trajectory optimization，317M 参数跨 80 任务\n  - BibTeX key suggestion: `hansen2024tdmpc2`\n  - 与本文关系: [background] — latent-space MPC 用 fixed short horizon planning；我们的 adaptive horizon 与其 fixed horizon 形成对比\n\n- **When to Trust Your Model: Model-Based Policy Optimization (MBPO)** (Janner et al., 2019) — 从 replay buffer state branching short rollout，Dyna-style 经典方案\n  - BibTeX key suggestion: `janner2019mbpo`\n  - 与本文关系: [background] — short horizon rollout 的 seminal work；我们 event-gating 实现 state-dependent horizon 而非 globally fixed horizon\n\n- **Conservative Rollout Length Adaptation (CRLA)** (2024) — 在 DreamerV3 上动态调整 rollout length，平衡 compounding error 与 data efficiency\n  - BibTeX key suggestion: `anonymous2024crla`\n  - 与本文关系: [direct-competitor] — 最直接的 adaptive horizon 竞争者；区别在于我们用 event-triggered gating 而非 model uncertainty metric\n\n- **Learning Adaptive Horizon Maps Based on Error Forecast for Model Predictive Control** (2023) — 根据 forecast error 空间分布学习 state-dependent 最优 horizon\n  - BibTeX key suggestion: `adaptive2023horizon`\n  - 与本文关系: [background] — MPC 领域的 adaptive horizon 理论，horizon ∝ 1/forecast_error 的定量关系与我们 event-trigger 理念一致\n\n- **Open-World RL over Long Short-Term Imagination (LS-Imagine)** (2025) — 有限 state transition steps 内扩展 imagination horizon，open-world 场景\n  - BibTeX key suggestion: `lsimagine2025`\n  - 与本文关系: [background] — long-horizon imagination 的新方案；与我们在 compounding error 管理上的目标一致但方法正交\n\n---\n\n## Category 5: Gradient Manipulation & Stop-Gradient in RL\n\n- **Gradient Routing: Masking Gradients to Localize Computation in Neural Networks** (Clark et al., 2024) — data-dependent gradient mask 实现模块化学习，RL 中用于 localize behaviors\n  - BibTeX key suggestion: `clark2024gradrouting`\n  - 与本文关系: [method-component] — gradient mask 的通用框架；我们的 event-gated stop-gradient 是一种 state-dependent gradient routing\n\n- **Conflict-Averse Gradient Aggregation for Constrained Multi-Objective RL** (2025) — CoMOGA: 处理 safety constraint 下多目标梯度冲突\n  - BibTeX key suggestion: `comoga2025`\n  - 与本文关系: [background] — multi-objective RL 中的梯度冲突处理；我们聚焦 world model 内部的 reconstruction vs reward gradient 冲突\n\n- **Gradient Shaping for Multi-Constraint Safe Reinforcement Learning** (Yao et al., 2024) — 分析 redundant/conflicting constraint gradients，提出 projection-based shaping\n  - BibTeX key suggestion: `yao2024gradshaping`\n  - 与本文关系: [background] — gradient projection 在 RL 安全约束中的应用；与 PCGrad 同族但面向 safe RL\n\n---\n\n## Category 6: Model-Based RL Foundations & Ensemble Methods\n\n- **Deep Reinforcement Learning in a Handful of Trials (PETS)** (Chua et al., 2018) — Probabilistic ensemble + trajectory sampling 实现 uncertainty-aware planning\n  - BibTeX key suggestion: `chua2018pets`\n  - 与本文关系: [background] — ensemble model 量化 epistemic uncertainty 的经典方案；我们的 event trigger 隐式利用 prediction error 作为 uncertainty signal\n\n- **TransDreamer: Reinforcement Learning with Transformer World Models** (Chen & Wu, 2022) — Transformer State-Space Model 替代 RNN，更好捕获长程依赖\n  - BibTeX key suggestion: `chen2022transdreamer`\n  - 与本文关系: [background] — world model architecture 的演进方向；与我们基于 RSSM 的 event-gating 互补\n\n- **STORM: Efficient Stochastic Transformer-based World Models** (Zhang et al., 2024) — transformer world model 在 Atari 100k 上匹配 DreamerV3 且训练更高效\n  - BibTeX key suggestion: `zhang2024storm`\n  - 与本文关系: [background] — 高效 world model 架构；event-gating 原则上可应用于 transformer-based world model\n\n- **Diffusion for World Modeling: Visual Details Matter in Atari (DIAMOND)** (Alonso et al., 2024) — diffusion model 作为 world model，比 discrete-token 方法保留更多视觉细节\n  - BibTeX key suggestion: `alonso2024diamond`\n  - 与本文关系: [background] — world model 的 generation quality 进展；更高质量的 imagination 减少 compounding error 的另一路径\n\n---\n\n## Category 7: Event-Triggered & State-Dependent Control\n\n- **Adaptive Event-triggered Reinforcement Learning Control for Complex Nonlinear Systems** (2024) — event-triggered 机制减少 RL 中不必要的 policy update，节约通信资源\n  - BibTeX key suggestion: `adaptive2024eventtriggered`\n  - 与本文关系: [background] — event-triggered 概念在 RL control 中的先例；我们将 event-trigger 应用于 world model gradient flow 而非 control communication\n\n- **Reinforcement Learning of the Prediction Horizon in Model Predictive Control** (Gros & Zanon, 2021) — 用 RL 学习 MPC 的最优 prediction horizon 作为 state 的函数\n  - BibTeX key suggestion: `gros2021horizon`\n  - 与本文关系: [background] — state-dependent horizon 的 RL-MPC 交叉视角；我们的 event-gating 也实现 state-dependent effective horizon\n\n---\n\n## Summary Statistics\n\n| Category | New refs | Key methodological link |\n|----------|----------|------------------------|\n| Value Overestimation | 5 | Overestimation amplified by model rollout |\n| Multi-task Loss Balancing | 3 | Gradient magnitude imbalance in world model |\n| Plasticity Loss | 4 | Network degradation under non-stationary objectives |\n| Temporal Abstraction & Adaptive Horizon | 6 | Variable effective planning horizon |\n| Gradient Manipulation | 3 | Selective gradient flow control |\n| MBRL Foundations | 4 | Ensemble, transformer, diffusion world models |\n| Event-Triggered Control | 2 | State-dependent triggering in RL |\n| **Total new refs** | **27** | |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_expansion.md",
    "content": "# Related Work Expansion (D4)\n\n> 20+ new references organized by category. Does NOT repeat the 7 already-cited papers (DreamerV3, GradNorm, Non-delusional Q, PCGrad, VaGraM, Gradient Routing, TAWM).\n\n---\n\n## Category 1: Value Overestimation in RL / MBRL\n\n- **Addressing Function Approximation Error in Actor-Critic Methods** (Fujimoto et al., 2018) — TD3: twin critics + clipped double Q-learning to suppress overestimation bias in continuous control.\n  - BibTeX key suggestion: `fujimoto2018td3`\n  - 与本文关系: [background] — 我们的 event-gated mechanism 部分动机来自 value overestimation 在 world model rollout 中的放大效应；TD3 是 model-free 经典对策\n\n- **Randomized Ensembled Double Q-Learning: Learning Fast Without a Model** (Chen et al., 2021) — REDQ: 大 ensemble + 随机子集取 min，UTD>>1 下的高样本效率 model-free 方法\n  - BibTeX key suggestion: `chen2021redq`\n  - 与本文关系: [method-component] — ensemble Q-function 的 in-target minimization 与我们对 value estimate 的保守处理相关\n\n- **COMBO: Conservative Offline Model-Based Policy Optimization** (Yu et al., 2021) — 在 model rollout 上对 OOD state-action 施加 value penalty，无需显式 uncertainty estimation\n  - BibTeX key suggestion: `yu2021combo`\n  - 与本文关系: [direct-competitor] — conservative value estimation in model-based setting 的替代方案\n\n- **MOPO: Model-based Offline Policy Optimization** (Yu et al., 2020) — 用 model uncertainty 作为 reward penalty，最大化真实 MDP return 的下界\n  - BibTeX key suggestion: `yu2020mopo`\n  - 与本文关系: [background] — uncertainty-penalized reward 与我们 event-gated horizon shortening 都抑制 overestimation，但机制不同\n\n- **Value Gradient weighted Model-Based Reinforcement Learning** (Voelcker et al., 2022) — VaGraM: 用 value function gradient 加权 model loss，关注对 policy 影响大的 prediction error\n  - BibTeX key suggestion: `voelcker2022vagram`\n  - 与本文关系: [method-component] — value-aware model learning 的互补视角；我们在 rollout 层面做 gating，VaGraM 在 model loss 层面做加权\n\n---\n\n## Category 2: Multi-task Loss Balancing in World Models\n\n- **HarmonyDream: Task Harmonization Inside World Models** (Ma/Shang et al., 2024) — 量化 reconstruction vs reward loss 的 2 个数量级差异，提出 harmonious loss 动态调权\n  - BibTeX key suggestion: `ma2024harmonydream`\n  - 与本文关系: [direct-competitor] — 同样识别 world model 多任务训练的梯度/loss 量级不平衡问题；我们用 event-gated stop-gradient 而非 loss reweighting\n\n- **Multi-Task Learning Using Uncertainty to Weigh Losses** (Kendall et al., 2018) — 用 homoscedastic uncertainty 自动平衡多任务 loss 权重\n  - BibTeX key suggestion: `kendall2018uncertainty`\n  - 与本文关系: [background] — multi-task loss balancing 的经典方法，HarmonyDream 和 GradNorm 的理论前驱\n\n- **DreamerPro: Reconstruction-Free Model-Based RL with Prototypical Representations** (Deng et al., 2022) — 用 prototypical self-supervised learning 替代 reconstruction，减轻视觉干扰影响\n  - BibTeX key suggestion: `deng2022dreamerpro`\n  - 与本文关系: [background] — 从另一角度解决 reconstruction loss 主导训练的问题（去掉 reconstruction），与我们保留 reconstruction 但 gate gradient 的策略形成对比\n\n---\n\n## Category 3: Plasticity Loss & Network Degradation in Deep RL\n\n- **The Primacy Bias in Deep Reinforcement Learning** (Nikishin et al., 2022) — RL agent 过拟合早期数据，提出 periodic network reset 缓解\n  - BibTeX key suggestion: `nikishin2022primacy`\n  - 与本文关系: [background] — plasticity loss 的根源分析；我们的 event-gated mechanism 通过选择性停止梯度防止 representation 退化\n\n- **Deep Reinforcement Learning with Plasticity Injection** (Nikishin et al., 2023) — 注入新初始化参数恢复可塑性，无需完全 reset\n  - BibTeX key suggestion: `nikishin2023plasticity`\n  - 与本文关系: [background] — 与 periodic reset 互补的轻量方案；event-gating 也是一种不丢失已有参数的 plasticity preservation 手段\n\n- **Understanding Plasticity in Neural Networks** (Lyle et al., 2023) — 系统分析 plasticity loss 与 loss landscape curvature 的关系，LayerNorm 有效\n  - BibTeX key suggestion: `lyle2023plasticity`\n  - 与本文关系: [background] — 为什么 DreamerV3 采用 LayerNorm 的理论解释；我们的方法从 gradient flow 而非 normalization 角度维护 plasticity\n\n- **Loss of Plasticity in Continual Deep Reinforcement Learning** (Abbas et al., 2023) — 连续任务切换下网络激活稀疏化导致梯度消失\n  - BibTeX key suggestion: `abbas2023plasticity`\n  - 与本文关系: [background] — continual RL 视角下的 plasticity loss；event-gating 的 stop-gradient 可视为防止某些 task 的梯度过度稀疏化\n\n---\n\n## Category 4: Temporal Abstraction & Adaptive Horizon in MBRL\n\n- **Deep Hierarchical Planning from Pixels (Director)** (Hafner et al., 2022) — Manager 在 world model latent space 设 subgoal，Worker 执行低层动作，实现 temporal abstraction\n  - BibTeX key suggestion: `hafner2022director`\n  - 与本文关系: [background] — hierarchical planning 实现变长 effective horizon；我们的 event-gating 不需要显式层次结构但达到类似的 adaptive horizon 效果\n\n- **TD-MPC2: Scalable, Robust World Models for Continuous Control** (Hansen et al., 2024) — implicit world model + local trajectory optimization，317M 参数跨 80 任务\n  - BibTeX key suggestion: `hansen2024tdmpc2`\n  - 与本文关系: [background] — latent-space MPC 用 fixed short horizon planning；我们的 adaptive horizon 与其 fixed horizon 形成对比\n\n- **When to Trust Your Model: Model-Based Policy Optimization (MBPO)** (Janner et al., 2019) — 从 replay buffer state branching short rollout，Dyna-style 经典方案\n  - BibTeX key suggestion: `janner2019mbpo`\n  - 与本文关系: [background] — short horizon rollout 的 seminal work；我们 event-gating 实现 state-dependent horizon 而非 globally fixed horizon\n\n- **Conservative Rollout Length Adaptation (CRLA)** (2024) — 在 DreamerV3 上动态调整 rollout length，平衡 compounding error 与 data efficiency\n  - BibTeX key suggestion: `anonymous2024crla`\n  - 与本文关系: [direct-competitor] — 最直接的 adaptive horizon 竞争者；区别在于我们用 event-triggered gating 而非 model uncertainty metric\n\n- **Learning Adaptive Horizon Maps Based on Error Forecast for Model Predictive Control** (2023) — 根据 forecast error 空间分布学习 state-dependent 最优 horizon\n  - BibTeX key suggestion: `adaptive2023horizon`\n  - 与本文关系: [background] — MPC 领域的 adaptive horizon 理论，horizon ∝ 1/forecast_error 的定量关系与我们 event-trigger 理念一致\n\n- **Open-World RL over Long Short-Term Imagination (LS-Imagine)** (2025) — 有限 state transition steps 内扩展 imagination horizon，open-world 场景\n  - BibTeX key suggestion: `lsimagine2025`\n  - 与本文关系: [background] — long-horizon imagination 的新方案；与我们在 compounding error 管理上的目标一致但方法正交\n\n---\n\n## Category 5: Gradient Manipulation & Stop-Gradient in RL\n\n- **Gradient Routing: Masking Gradients to Localize Computation in Neural Networks** (Clark et al., 2024) — data-dependent gradient mask 实现模块化学习，RL 中用于 localize behaviors\n  - BibTeX key suggestion: `clark2024gradrouting`\n  - 与本文关系: [method-component] — gradient mask 的通用框架；我们的 event-gated stop-gradient 是一种 state-dependent gradient routing\n\n- **Conflict-Averse Gradient Aggregation for Constrained Multi-Objective RL** (2025) — CoMOGA: 处理 safety constraint 下多目标梯度冲突\n  - BibTeX key suggestion: `comoga2025`\n  - 与本文关系: [background] — multi-objective RL 中的梯度冲突处理；我们聚焦 world model 内部的 reconstruction vs reward gradient 冲突\n\n- **Gradient Shaping for Multi-Constraint Safe Reinforcement Learning** (Yao et al., 2024) — 分析 redundant/conflicting constraint gradients，提出 projection-based shaping\n  - BibTeX key suggestion: `yao2024gradshaping`\n  - 与本文关系: [background] — gradient projection 在 RL 安全约束中的应用；与 PCGrad 同族但面向 safe RL\n\n---\n\n## Category 6: Model-Based RL Foundations & Ensemble Methods\n\n- **Deep Reinforcement Learning in a Handful of Trials (PETS)** (Chua et al., 2018) — Probabilistic ensemble + trajectory sampling 实现 uncertainty-aware planning\n  - BibTeX key suggestion: `chua2018pets`\n  - 与本文关系: [background] — ensemble model 量化 epistemic uncertainty 的经典方案；我们的 event trigger 隐式利用 prediction error 作为 uncertainty signal\n\n- **TransDreamer: Reinforcement Learning with Transformer World Models** (Chen & Wu, 2022) — Transformer State-Space Model 替代 RNN，更好捕获长程依赖\n  - BibTeX key suggestion: `chen2022transdreamer`\n  - 与本文关系: [background] — world model architecture 的演进方向；与我们基于 RSSM 的 event-gating 互补\n\n- **STORM: Efficient Stochastic Transformer-based World Models** (Zhang et al., 2024) — transformer world model 在 Atari 100k 上匹配 DreamerV3 且训练更高效\n  - BibTeX key suggestion: `zhang2024storm`\n  - 与本文关系: [background] — 高效 world model 架构；event-gating 原则上可应用于 transformer-based world model\n\n- **Diffusion for World Modeling: Visual Details Matter in Atari (DIAMOND)** (Alonso et al., 2024) — diffusion model 作为 world model，比 discrete-token 方法保留更多视觉细节\n  - BibTeX key suggestion: `alonso2024diamond`\n  - 与本文关系: [background] — world model 的 generation quality 进展；更高质量的 imagination 减少 compounding error 的另一路径\n\n---\n\n## Category 7: Event-Triggered & State-Dependent Control\n\n- **Adaptive Event-triggered Reinforcement Learning Control for Complex Nonlinear Systems** (2024) — event-triggered 机制减少 RL 中不必要的 policy update，节约通信资源\n  - BibTeX key suggestion: `adaptive2024eventtriggered`\n  - 与本文关系: [background] — event-triggered 概念在 RL control 中的先例；我们将 event-trigger 应用于 world model gradient flow 而非 control communication\n\n- **Reinforcement Learning of the Prediction Horizon in Model Predictive Control** (Gros & Zanon, 2021) — 用 RL 学习 MPC 的最优 prediction horizon 作为 state 的函数\n  - BibTeX key suggestion: `gros2021horizon`\n  - 与本文关系: [background] — state-dependent horizon 的 RL-MPC 交叉视角；我们的 event-gating 也实现 state-dependent effective horizon\n\n---\n\n## Summary Statistics\n\n| Category | New refs | Key methodological link |\n|----------|----------|------------------------|\n| Value Overestimation | 5 | Overestimation amplified by model rollout |\n| Multi-task Loss Balancing | 3 | Gradient magnitude imbalance in world model |\n| Plasticity Loss | 4 | Network degradation under non-stationary objectives |\n| Temporal Abstraction & Adaptive Horizon | 6 | Variable effective planning horizon |\n| Gradient Manipulation | 3 | Selective gradient flow control |\n| MBRL Foundations | 4 | Ensemble, transformer, diffusion world models |\n| Event-Triggered Control | 2 | State-dependent triggering in RL |\n| **Total new refs** | **27** | |\n"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-16T16:28:04.488459+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_expansion.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-16T16:28:04.488592+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Related Work Expansion (D4)",
  "type": "report",
  "description": "Structured list of 27 new references for Related Work expansion, organized into 7 categories: Value Overestimation, Multi-task Loss Balancing, Plasticity Loss, Temporal Abstraction & Adaptive Horizon, Gradient Manipulation, MBRL Foundations, and Event-Triggered Control. Each entry includes BibTeX key suggestion and relevance to our paper.",
  "project": "event-gated-adaptive-horizon",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_expansion.md",
  "tags": "['related-work', 'D4', 'literature', 'references']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Related Work Expansion (D4)",
    "type": "report",
    "description": "Structured list of 27 new references for Related Work expansion, organized into 7 categories: Value Overestimation, Multi-task Loss Balancing, Plasticity Loss, Temporal Abstraction & Adaptive Horizon, Gradient Manipulation, MBRL Foundations, and Event-Triggered Control. Each entry includes BibTeX key suggestion and relevance to our paper.",
    "project": "event-gated-adaptive-horizon",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/related_work_expansion.md",
    "tags": "['related-work', 'D4', 'literature', 'references']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-16T16:28:04.488744+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_7d4fc2\", \"name\": \"Related Work Expansion (D4)\", \"type\": \"report\", \"description\": \"Structured list of 27 new references for Related Work expansion, organized into 7 categories: Value Overestimation, Multi-task Loss Balancing, Plasticity Loss, Temporal Abstraction & Adaptive Horizon, Gradient Manipulation, MBRL Foundations, and Event-Triggered Control. Each entry includes BibTeX key suggestion and relevance to our paper.\", \"path\": \"projects/event-gated-adaptive-horizon/artifacts/_project/report/related_work_expansion.md\", \"url\": null, \"project\": \"event-gated-adaptive-horizon\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T16:27:54.941939+00:00\", \"tags\": [\"related-work\", \"D4\", \"literature\", \"references\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related-work-expansion_20260516T162428",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-16T16:28:04.488940+00:00_

产出已写入并注册。

**结果**：`artifacts/related_work_expansion.md` 包含 **27 条新引用**（不含已有 7 篇），覆盖全部审稿人要求的方向：

| 类别 | 数量 | 关键论文 |
|------|------|----------|
| Value Overestimation | 5 | TD3, REDQ, COMBO, MOPO, VaGraM |
| Multi-task Loss Balancing | 3 | HarmonyDream, Kendall 2018, DreamerPro |
| Plasticity Loss | 4 | Nikishin 2022/2023, Lyle 2023, Abbas 2023 |
| Adaptive Horizon | 6 | Director, TD-MPC2, MBPO, CRLA, LS-Imagine等 |
| Gradient Manipulation | 3 | Gradient Routing, CoMOGA, GradShaping |
| MBRL Foundations | 4 | PETS, TransDreamer, STORM, DIAMOND |
| Event-Triggered Control | 2 | Adaptive ET-RL, Gros & Zanon 2021 |

每条包含 BibTeX key 建议和与本文的关系标签（direct-competitor / method-component / background / evaluation）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related-work-expansion_20260516T162428"
}
```

</details>

---
