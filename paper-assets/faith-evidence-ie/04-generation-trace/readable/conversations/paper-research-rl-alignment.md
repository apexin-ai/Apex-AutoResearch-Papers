# paper research rl alignment

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_research_rl_alignment_20260517T154253.jsonl`
- **Structured JSON:** [`76d8f79676b540b8c6c6.json`](../../sessions/76/76d8f79676b540b8c6c6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-17T15:45:12.430821+00:00_

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
  "session": "worker_paper_research_rl_alignment_20260517T154253",
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

_source line 2 · 2026-05-17T15:45:12.431204+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T15:45:12.431460+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeepSeekMath Pushing the Limits of Mathematical Reasoning Open Language Models arxiv 2402.03300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeepSeekMath Pushing the Limits of Mathematical Reasoning Open Language Models arxiv 2402.03300"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T15:45:12.431600+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Direct Preference Optimization Your Language Model is Secretly a Reward Model Rafailov NeurIPS arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Direct Preference Optimization Your Language Model is Secretly a Reward Model Rafailov NeurIPS arxiv"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T15:45:12.431726+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Scaling Laws for Reward Model Overoptimization Gao ICML 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Scaling Laws for Reward Model Overoptimization Gao ICML 2023 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T15:45:12.431905+00:00_

Web search results for query: "DeepSeekMath Pushing the Limits of Mathematical Reasoning Open Language Models arxiv 2402.03300"

Links: [{"title":"[2402.03300] DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/abs/2402.03300"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical","url":"https://arxiv.org/pdf/2402.03300"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/html/2402.03300"},{"title":"Paper page - DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://huggingface.co/papers/2402.03300"},{"title":"GitHub - deepseek-ai/DeepSeek-Math: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-Math"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/deepseekmath-pushing-the-limits-of-mathematical-reasoning-in-open-language-models-f2665df4019e"},{"title":"Zhihong Shao 邵智宏 - Zhihong Shao 邵智宏","url":"https://zhihongshao.github.io/"},{"title":"[2402.03300v3] DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models","url":"https://arxiv.org/abs/2402.03300v3"},{"title":"DeepSeekMath: Advancing Math Reasoning","url":"https://www.emergentmind.com/papers/2402.03300"},{"title":"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240203300S/abstract"}]

I found the paper you're looking for. Here's a summary of the research:

## DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

Mathematical reasoning poses a significant challenge for language models due to its complex and structured nature. The paper introduces DeepSeekMath 7B, which contin
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-17T15:45:12.432117+00:00_

Web search results for query: "Direct Preference Optimization Your Language Model is Secretly a Reward Model Rafailov NeurIPS arxiv"

Links: [{"title":"[2305.18290] Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/abs/2305.18290"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/pdf/2305.18290"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/direct-preference-optimization-your-language-model-is-secretly-a-reward-model-5b8f44cb9b9b"},{"title":"Direct preference optimization: your language model is ...","url":"https://dl.acm.org/doi/10.5555/3666122.3668460"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model, Rafael Rafailov+, N/A, NeurIPS'24 · Issue #1412 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1412"},{"title":"NeurIPS Poster Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://neurips.cc/virtual/2023/poster/72164"},{"title":"[PDF] Direct Preference Optimization: Your Language Model is Secretly a Reward Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Direct-Preference-Optimization:-Your-Language-Model-Rafailov-Sharma/0d1c76d45afa012ded7ab741194baf142117c495"},{"title":"Paper page - Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://huggingface.co/papers/2305.18290"},{"title":"[2305.18290v2] Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/abs/2305.18290v2"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://papers.nips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract-Conference.html"}]

I fo
…[truncated 1374 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T15:45:12.432358+00:00_

Web search results for query: "Scaling Laws for Reward Model Overoptimization Gao ICML 2023 arxiv"

Links: [{"title":"Scaling laws for reward model overoptimization | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3618845"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"[PDF] Scaling Laws for Reward Model Overoptimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scaling-Laws-for-Reward-Model-Overoptimization-Gao-Schulman/fb3dc5e20e0a71134ca916f0d6d8d41f01225b4b"},{"title":"[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/abs/2406.02900"},{"title":"Scaling Laws for Reward Model Overoptimization Leo Gao OpenAI John Schulman","url":"https://arxiv.org/pdf/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.researchgate.net/publication/364436070_Scaling_Laws_for_Reward_Model_Overoptimization"},{"title":"ICML Poster Scaling Laws for Reward Model Overoptimization","url":"https://icml.cc/virtual/2023/poster/24924"},{"title":"ICML Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://icml.cc/virtual/2024/37712"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.summarizepaper.com/en/arxiv-id/2210.10760v1/"}]

Based on the search results, I found the paper you're looking for:

## "Scaling Laws for Reward Model Overoptimization" by Leo Gao et al.

**Publication Details:**
- Authors: Leo Gao, John Schulman, Jacob Hilton
- Published at ICML'23 (the 40th International Conference on Machine Learning) on July 23, 2023
- arXiv version: arXiv:2210.10760, submitted October 19, 2022

**Main Contributions:**
The paper uses a syntheti
…[truncated 953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T15:45:12.432553+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T15:45:12.432685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"R1-RE Cross-Domain Relation Extraction with RLVR\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"R1-RE Cross-Domain Relation Extraction with RLVR\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T15:45:12.433054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"RL Is Neither a Panacea Nor a Mirage\" structured prediction arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"RL Is Neither a Panacea Nor a Mirage\" structured prediction arxiv"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-17T15:45:12.433206+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"E-GRPO Entity-Aware Reward for Group Relative Policy Optimization\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"E-GRPO Entity-Aware Reward for Group Relative Policy Optimization\" arxiv"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T15:45:12.433397+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Confronting Reward Model Overoptimization with Constrained RLHF\" arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Confronting Reward Model Overoptimization with Constrained RLHF\" arxiv"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T15:45:12.433574+00:00_

Web search results for query: ""Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement" arxiv"

Links: [{"title":"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://arxiv.org/html/2502.16377v2"},{"title":"Instruction-Tuning LLMs for Event Extraction with ...","url":"https://www.arxiv.org/pdf/2502.16377"},{"title":"STEER: Structured Event Evidence for Video Reasoning via Multi-Objective Reinforcement Learning","url":"https://arxiv.org/html/2604.04415"},{"title":"[2502.16377] Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://arxiv.org/abs/2502.16377"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"},{"title":"MAVIS: Multi-Objective Alignment via Inference-Time Value-Guided Selection","url":"https://arxiv.org/html/2508.13415"},{"title":"Aligning Instruction Tasks Unlocks Large Language Models ...","url":"https://ar5iv.labs.arxiv.org/html/2305.11159"},{"title":"MAVIS: Multi-Objective Alignment via Value-Guided Inference-Time Search","url":"https://arxiv.org/html/2508.13415v2"}]

Based on the search results, I found the paper you're looking for:

**"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning"** was published in the ECIR 2026 conference (Advances in Information Retrieval).

The paper addresses the issue that current instruction-tuned LLMs often produce inconsistent formats, semantically drifted outputs, and event types that deviate from predefined schemes—problems that arise because supervised fine-tuning re
…[truncated 844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T15:45:12.433764+00:00_

Web search results for query: ""RL Is Neither a Panacea Nor a Mirage" structured prediction arxiv"

Links: [{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"[2508.16546] RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/abs/2508.16546"},{"title":"RL Is Neither a Panacea Nor a Mirage:","url":"https://arxiv.org/pdf/2508.16546"},{"title":"[2508.16546v1] RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/abs/2508.16546v1"},{"title":"RL Is Neither a Panacea Nor a Mirage","url":"https://www.alphaxiv.org/abs/2508.16546"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs - Paper Detail","url":"https://deeplearn.org/arxiv/631799/rl-is-neither-a-panacea-nor-a-mirage:-understanding-supervised-vs.-reinforcement-learning-fine-tuning-for-llms"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.16546v1"},{"title":"(PDF) RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://www.researchgate.net/publication/394920663_RL_Is_Neither_a_Panacea_Nor_a_Mirage_Understanding_Supervised_vs_Reinforcement_Learning_Fine-Tuning_for_LLMs"},{"title":"RL Is Neither a Panacea nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=91kwev26v7yyx2y46jpg"},{"title":"2025년 8월 25일 - by Kim Seonghyeon - arXiv Daily","url":"https://rosinality.substack.com/p/2025-8-25"}]

I found the paper you were looking for! Here are the key details:


…[truncated 1365 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T15:45:12.433975+00:00_

Web search results for query: ""R1-RE Cross-Domain Relation Extraction with RLVR" arxiv"

Links: [{"title":"[2507.04642] R1-RE: Cross-Domain Relation Extraction with RLVR","url":"https://arxiv.org/abs/2507.04642"},{"title":"R1-RE: Cross-Domain Relationship Extraction with RLVR","url":"https://arxiv.org/html/2507.04642v1"},{"title":"R1-RE: Cross-Domain Relation Extraction with RLVR","url":"https://arxiv.org/html/2507.04642"},{"title":"R1-RE: Cross-Domain Relation Extraction with RLVR Runpeng Dai1 Tong Zheng2","url":"https://arxiv.org/pdf/2507.04642"},{"title":"R1-RE: Cross-Domain Relationship Extraction with RLVR | Semantic Scholar","url":"https://www.semanticscholar.org/paper/R1-RE:-Cross-Domain-Relationship-Extraction-with-Dai-Zheng/ca336239e3b182b39001928628deb5b2e9c5eec9"},{"title":"Expanding RL with Verifiable Rewards Across Diverse Domains","url":"https://arxiv.org/pdf/2503.23829"},{"title":"arXiv:2504.20571v2 [cs.LG] 25 May 2025","url":"https://arxiv.org/pdf/2504.20571"},{"title":"RLPR: Extrapolating RLVR to general domains without verifiers","url":"https://arxiv.org/html/2506.18254v1"},{"title":"[2210.09345] CrossRE: A Cross-Domain Dataset for Relation Extraction","url":"https://arxiv.org/abs/2210.09345"},{"title":"Crossing the Reward Bridge: Expanding RL with Verifiable Rewards Across Diverse Domains","url":"https://arxiv.org/html/2503.23829v2"}]

I found the paper for you. Here are the key details about "R1-RE: Cross-Domain Relation Extraction with RLVR":

## Overview

R1-RE reframes relation extraction as a reasoning task guided by annotation guidelines and introduces the first reinforcement learning with verifiable reward (RLVR) framework for RE tasks, inspired by the workflow of human annotators.

## Problem and Approach

Traditional approaches typically frame RE as a supervised learning problem, directly mapping context to labels—an approach that often suffers from poor out-of-domain (OOD) generalization. The method elicits the reasoning abilities of sm
…[truncated 686 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T15:45:12.434264+00:00_

Web search results for query: ""Confronting Reward Model Overoptimization with Constrained RLHF" arxiv"

Links: [{"title":"[2310.04373] Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://arxiv.org/abs/2310.04373"},{"title":"CONFRONTING REWARD MODEL OVEROPTIMIZATION WITH CONSTRAINED RLHF Ted Moskovitz∗","url":"https://arxiv.org/pdf/2310.04373"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://arxiv.org/html/2310.04373v1"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/html/2505.18126v1"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10549975-confronting-reward-model-overoptimization-constrained-rlhf"},{"title":"Reward Model Overoptimization: Root Causes and Mitigations","url":"https://www.reinforced.info/p/reward-model-overoptimization"},{"title":"Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer","url":"https://arxiv.org/html/2405.16436v3"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231004373M/abstract"},{"title":"Mitigating Reward Over-Optimization in RLHF via Behavior-Supported Regularization","url":"https://arxiv.org/html/2503.18130v1"}]

I found the paper "Confronting Reward Model Overoptimization with Constrained RLHF" for you. Here's what I found:

## Overview

The paper is arXiv preprint 2310.04373 titled "Confronting Reward Model Overoptimization with Constrained RLHF", authored by Ted Moskovitz and colleagues.

## Key Problem

Large language models are typically aligned with human preferences by optimizing reward models (RMs) fitted to human feedback. However, human preferences are multi
…[truncated 1293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T15:45:12.434473+00:00_

Web search results for query: ""E-GRPO Entity-Aware Reward for Group Relative Policy Optimization" arxiv"

Links: [{"title":"Entity-aware Group Relative Policy Optimization (E-GRPO)","url":"https://www.emergentmind.com/topics/entity-aware-group-relative-policy-optimization-e-grpo"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent ...","url":"https://arxiv.org/pdf/2510.24694"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"},{"title":"EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance","url":"https://arxiv.org/html/2605.04960"},{"title":"[2601.00423] E-GRPO: High Entropy Steps Drive Effective Reinforcement Learning for Flow Models","url":"https://arxiv.org/abs/2601.00423"},{"title":"WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning","url":"https://arxiv.org/html/2602.17025v1"},{"title":"[2605.04960] EP-GRPO: Entropy-Progress Aligned Group Relative Policy Optimization with Implicit Process Guidance","url":"https://arxiv.org/abs/2605.04960"},{"title":"NGRPO: NEGATIVE-ENHANCED GROUP RELATIVE POLICY OPTIMIZATION","url":"https://arxiv.org/pdf/2509.18851"},{"title":"E-GRPO: High Entropy Steps Drive Effective Reinforcement Learning for Flow Models","url":"https://arxiv.org/html/2601.00423v1"},{"title":"Constrained Group Relative Policy Optimization","url":"https://arxiv.org/html/2602.05863"}]

I found information about E-GRPO (Entity-Aware Group Relative Policy Optimization) on arXiv. Here's what I found:

## Entity-Aware Group Relative Policy Optimization (E-GRPO)

E-GRPO is a reinforcement learning framework developed to fine-tune LLM search agents using dense entity-aware rewards. 

E-GRPO is a novel RL framework that enhances policy optimization by formulating a dense, entity-aware reward function from the entities within the synthetic training data.

### Key Features


…[truncated 1111 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T15:45:12.434671+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.24694 \"E-GRPO\" entity-aware search agent authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.24694 \"E-GRPO\" entity-aware search agent authors"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-17T15:45:12.434805+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Confronting Reward Model Overoptimization with Constrained RLHF\" Moskovitz ICLR 2024 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Confronting Reward Model Overoptimization with Constrained RLHF\" Moskovitz ICLR 2024 venue"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T15:45:12.434925+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Aligning Instruction-Tuned LLMs for Event Extraction\" GRPO authors ECIR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Aligning Instruction-Tuned LLMs for Event Extraction\" GRPO authors ECIR 2026"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T15:45:12.435072+00:00_

Web search results for query: "arxiv 2510.24694 "E-GRPO" entity-aware search agent authors"

Links: [{"title":"[2510.24694] Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://arxiv.org/abs/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://arxiv.org/html/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.24694v1"},{"title":"ReSeek: A Self-Correcting Framework for Search Agents with Instructive Rewards","url":"https://arxiv.org/html/2510.00568"},{"title":"HierSearch: A Hierarchical Enterprise Deep Search Framework Integrating Local and Web Searches","url":"https://arxiv.org/html/2508.08088"},{"title":"RANGER: Repository‑level Agent for Graph‑Enhanced Retrieval","url":"https://arxiv.org/html/2509.25257"},{"title":"Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics","url":"https://arxiv.org/html/2510.17797v1"},{"title":"Is Grep All You Need? How Agent Harnesses Reshape Agentic Search","url":"https://arxiv.org/html/2605.15184v1"},{"title":"Is Grep All You Need? How Agent Harnesses Reshape Agentic Search | HypaTerra","url":"https://hypaterra.com/events/1309/"}]

Based on the search results, I found information about arXiv paper 2510.24694. The paper is titled "Repurposing Synthetic Data for Fine-grained Search Agent Supervision".

The paper introduces Entity-aware Group Relative Policy Optimization (E-GRPO), a novel framework that formulates a dense entity-aware reward function. However, the search results do not display the author information for this paper. To get the author names, you would need to visit the arxiv.org abstract page directly at https://arxiv.org/abs/2510.24694, wher
…[truncated 172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-17T15:45:12.435261+00:00_

Web search results for query: ""Aligning Instruction-Tuned LLMs for Event Extraction" GRPO authors ECIR 2026"

Links: [{"title":"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://arxiv.org/html/2502.16377v1"},{"title":"Instruction-Tuning LLMs for Event Extraction with ...","url":"https://www.arxiv.org/pdf/2502.16377"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.677/"},{"title":"[2502.16377] Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://arxiv.org/abs/2502.16377"},{"title":"Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://www.researchgate.net/publication/389314784_Instruction-Tuning_LLMs_for_Event_Extraction_with_Annotation_Guidelines"},{"title":"[Literature Review] Instruction-Tuning LLMs for Event Extraction with Annotation Guidelines","url":"https://www.themoonlight.io/en/review/instruction-tuning-llms-for-event-extraction-with-annotation-guidelines"},{"title":"(PDF) ECLIPTICA - A Framework for Switchable LLM Alignment via CITA - Contrastive Instruction-Tuned Alignment","url":"https://www.researchgate.net/publication/399733998_ECLIPTICA_-_A_Framework_for_Switchable_LLM_Alignment_via_CITA_-_Contrastive_Instruction-Tuned_Alignment"},{"title":"Bluesky","url":"https://bsky.app/intent/compose?text=%22Aligning+Instruction-Tuned+LLMs+for+Event+Extraction+with+Multi-objective+Reinforcement+Learning.%22+at+#dblphttps://doi.org/10.1007/978-3-032-21300-6_50"},{"title":"Event Extraction in Large Language Model: A Holistic Survey of Method, Modality, and Future","url":"https://arxiv.org/html/2512.19537v1"}]

Based on the search results, I found the paper you'
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T15:45:12.435462+00:00_

Web search results for query: ""Confronting Reward Model Overoptimization with Constrained RLHF" Moskovitz ICLR 2024 venue"

Links: [{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"confronting reward model overoptimization","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf"},{"title":"[2310.04373] Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://arxiv.org/abs/2310.04373"},{"title":"ICLR Poster Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://iclr.cc/virtual/2024/poster/18133"},{"title":"CONFRONTING REWARD MODEL OVEROPTIMIZATION WITH CONSTRAINED RLHF Ted Moskovitz∗","url":"https://arxiv.org/pdf/2310.04373"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10549975-confronting-reward-model-overoptimization-constrained-rlhf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Russ Salakhutdinov on X: \"#ICLR2024: @McaleerStephen is presenting our work on Confronting Reward Model Overoptimization with Constrained RLHF. Paper: https://t.co/TKniz3tHCz with @ted_moskovitz, @Aaditya6284, @djstrouse, Tuomas Sandholm, @ancadianadragan. @ted_moskovitz could not make it to the https://t.co/LsgB5CcbvM\" / X","url":"https://x.com/rsalakhu/status/1787863384454488093"},{"title":"Confronting Reward Model Overoptimization with Constrained RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231004373M/abstract"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/html/2505.18126v2"}]

I found the paper! Here are the search results for "Confronting Reward Model Overoptimization with Constrained RLHF" by Moskovitz et al. at ICLR 2024:

## Paper Details

**Autho
…[truncated 1417 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T15:45:12.435652+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.24694 \"Repurposing Synthetic Data for Fine-grained Search Agent\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.24694 \"Repurposing Synthetic Data for Fine-grained Search Agent\" authors"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-17T15:45:12.435782+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2508.16546 \"RL Is Neither a Panacea Nor a Mirage\" authors Hangzhan Jin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2508.16546 \"RL Is Neither a Panacea Nor a Mirage\" authors Hangzhan Jin"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-17T15:45:12.435979+00:00_

Web search results for query: "arxiv 2510.24694 "Repurposing Synthetic Data for Fine-grained Search Agent" authors"

Links: [{"title":"[2510.24694] Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://arxiv.org/abs/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://arxiv.org/html/2510.24694v1"},{"title":"dblp: Repurposing Synthetic Data for Fine-grained Search Agent Supervision.","url":"https://dblp.org/rec/journals/corr/abs-2510-24694.html"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://www.researchgate.net/publication/397007255_Repurposing_Synthetic_Data_for_Fine-grained_Search_Agent_Supervision"},{"title":"Paper page - Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://huggingface.co/papers/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent ...","url":"https://arxiv.org/pdf/2510.24694"},{"title":"Repurposing Synthetic Data for Fine-grained Search Agent Supervision | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.24694v1"},{"title":"[Literature Review] Repurposing Synthetic Data for Fine-grained Search Agent Supervision","url":"https://www.themoonlight.io/en/review/repurposing-synthetic-data-for-fine-grained-search-agent-supervision"},{"title":"Automatic Synthetic Data and Fine-grained Adaptive Feature Alignment for Composed Person Retrieval","url":"https://arxiv.org/html/2311.16515v4"}]

Based on the search results, I found the authors of arXiv paper 2510.24694 "Repurposing Synthetic Data for Fine-grained Search Agent Supervision":

The authors are: Yida Zhao, Kuan Li, Xixi Wu, Liwen Zhang, Dingchu Zhang, Baixuan Li, Maojia Song, Zhuo Chen, Chenxi Wang, Xinyu Wang, Kewei Tu, Pengjun Xie, Jing
…[truncated 128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T15:45:12.436322+00:00_

Web search results for query: "arxiv 2508.16546 "RL Is Neither a Panacea Nor a Mirage" authors Hangzhan Jin"

Links: [{"title":"[2508.16546] RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/abs/2508.16546"},{"title":"RL Is Neither a Panacea Nor a Mirage:","url":"https://arxiv.org/pdf/2508.16546"},{"title":"[2508.16546v1] RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/abs/2508.16546v1"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://arxiv.org/html/2508.16546v1"},{"title":"RL Is Neither a Panacea Nor a Mirage","url":"https://www.alphaxiv.org/abs/2508.16546"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.16546v1"},{"title":"(PDF) RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs","url":"https://www.researchgate.net/publication/394920663_RL_Is_Neither_a_Panacea_Nor_a_Mirage_Understanding_Supervised_vs_Reinforcement_Learning_Fine-Tuning_for_LLMs"},{"title":"RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs - Paper Detail","url":"https://deeplearn.org/arxiv/631799/rl-is-neither-a-panacea-nor-a-mirage:-understanding-supervised-vs.-reinforcement-learning-fine-tuning-for-llms"},{"title":"RL Is Neither a Panacea nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=91kwev26v7yyx2y46jpg"},{"title":"fly51fly on X: \"[LG] RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs H Jin, S Lv, S Wu, M Hamdaq
…[truncated 1437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T15:45:12.436507+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Adjali Liang Bhatti Sonntag \"Event Extraction\" \"Multi-objective Reinforcement Learning\" GRPO arxiv preprint"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Adjali Liang Bhatti Sonntag \"Event Extraction\" \"Multi-objective Reinforcement Learning\" GRPO arxiv preprint"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T15:45:12.436667+00:00_

Web search results for query: "Adjali Liang Bhatti Sonntag "Event Extraction" "Multi-objective Reinforcement Learning" GRPO arxiv preprint"

Links: [{"title":"Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-032-21300-6_50"},{"title":"Retrieval-GRPO: A Multi-Objective Reinforcement Learning Framework for Dense Retrieval in Taobao Search","url":"https://arxiv.org/html/2511.13885v2"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"Reinforcement Learning Meets Large Language Models: A Survey of","url":"https://arxiv.org/pdf/2509.16679"},{"title":"[2601.05002] On the Hidden Objective Biases of Group-based Reinforcement Learning","url":"https://arxiv.org/abs/2601.05002"},{"title":"Early Exit via Reinforcement Learning in Reasoning Models","url":"https://www.aimodels.fyi/papers/arxiv/s-grpo-early-exit-via-reinforcement-learning"},{"title":"Artificial Intelligence Jul 2025","url":"https://arxiv.org/list/cs.AI/2025-07?skip=175&show=2000"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1100&show=2000"}]

Great! I found the paper you're looking for. The paper is by Adjali, O., Liang, S., Bhatti, O.S., and Sonntag, D. (2026) titled "Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning."

The paper introduces a reinforcement learning framework based on Group Relative Policy Optimization (GRPO) designed to optimize instruction-tuned LLMs for event and argument extraction. They propose three c
…[truncated 499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_rl_alignment_20260517T154253",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T15:45:12.437291+00:00_

所有 8 篇论文验证完成。以下是结果：

---

## Must-cite 论文（3篇）

## [GRPO / DeepSeekMath]
- title: DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models
- authors: Shao et al. (Zhihong Shao)
- venue: arXiv preprint (2024)
- year: 2024
- arxiv: 2402.03300
- doi: —
- bibtex_key: shao2024deepseekmath
- verified: true
- relevance: 提出 GRPO 算法，本论文直接使用 GRPO 训练 DocRE 模型
- verification_note: 确认 GRPO 在此论文中首次提出，作为 PPO 的变体用于数学推理。title/authors/arXiv ID 均与预期一致。

## [DPO]
- title: Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- authors: Rafailov et al. (Rafael Rafailov, Archit Sharma, Eric Mitchell, Stefano Ermon, Christopher D. Manning, Chelsea Finn)
- venue: NeurIPS 2023
- year: 2023
- arxiv: 2305.18290
- doi: 10.5555/3666122.3668460
- bibtex_key: rafailov2023dpo
- verified: true
- relevance: 本论文使用 DPO 作为对比方法训练 DocRE 模型，发现渐进退化现象
- verification_note: 确认 NeurIPS 2023（非 2024）。arXiv ID 2305.18290。

## [Gao et al. 2023 — Reward Overoptimization]
- title: Scaling Laws for Reward Model Overoptimization
- authors: Gao et al. (Leo Gao, John Schulman, Jacob Hilton)
- venue: ICML 2023
- year: 2023
- arxiv: 2210.10760
- doi: 10.5555/3618408.3618845
- bibtex_key: gao2023scaling
- verified: true
- relevance: 本论文发现 GRPO QLoRA catastrophic decoupling 与 reward hacking 相关，此文提供 reward overoptimization 理论基础
- verification_note: 确认 ICML 2023 (40th ICML)。arXiv 提交于 2022-10，发表于 2023。

---

## Gap-fill 论文（5篇）

## [Adjali et al. 2026 — GRPO for Event Extraction]
- title: Aligning Instruction-Tuned LLMs for Event Extraction with Multi-objective Reinforcement Learning
- authors: Adjali et al. (O. Adjali, S. Liang, O.S. Bhatti, D. Sonntag)
- venue: ECIR 2026 (Advances in Information Retrieval)
- year: 2026
- arxiv: —（无 arXiv 预印本）
- doi: 10.1007/978-3-032-21300-6_50
- bibtex_key: adjali2026aligning
- verified: true
- relevance: 直接使用 GRPO + 多目标 reward（format/BM25/task-specific）做 IE 任务，与本论文方法高度相似
- verification_note: 仅在 Springer 发表，无 arXiv 版本。ECIR 2026 确认。

## [R1-RE — RLVR for Relation Extraction]
- title: R1-RE: Cross-Domain Relation Extraction with RLVR
- authors: Dai et al. (Runpeng Dai, Tong Zheng, Run Yang, Kaixian Yu, Hongtu Zhu)
- venue: arXiv preprint (2025)
- year: 2025
- arxiv: 2507.04642
- doi: —
- bibtex_key: dai2025r1re
- verified: true
- relevance: 首个将 RLVR 用于关系抽取的工作，证明 RL 可提升 RE 跨域泛化能力，与本论文 GRPO-for-DocRE 直接可比
- verification_note: arXiv 2025-07-07。标题中 "Relation Extraction" 有时显示为 "Relationship Extraction"，同一论文。

## [Jin et al. 2025 — RL vs SFT Analysis]
- title: RL Is Neither a Panacea Nor a Mirage: Understanding Supervised vs. Reinforcement Learning Fine-Tuning for LLMs
- authors: Jin et al. (Hangzhan Jin, Sicheng Lv, Sifan Wu, Mohammad Hamdaqa)
- venue: arXiv preprint (2025)
- year: 2025
- arxiv: 2508.16546
- doi: —
- bibtex_key: jin2025rl_panacea
- verified: true
- relevance: 分析 SFT→RL 时表征变化与 OOD 性能，为本论文 catastrophic decoupling 分析提供理论支撑（SFT 严重过拟合时 RL 无法完全恢复）
- verification_note: Polytechnique Montreal / Mila。2025-08-22 提交。

## [E-GRPO — Entity-Aware Rewards in GRPO]
- title: Repurposing Synthetic Data for Fine-grained Search Agent Supervision
- authors: Zhao et al. (Yida Zhao, Kuan Li, Xixi Wu, Liwen Zhang, et al.)
- venue: arXiv preprint (2025)
- year: 2025
- arxiv: 2510.24694
- doi: —
- bibtex_key: zhao2025egrpo
- verified: true
- relevance: 提出 E-GRPO（entity-aware dense reward in GRPO），用实体匹配作为细粒度 reward，与本论文 evidence-level reward 设计思路一致
- verification_note: 论文主题为搜索代理，但核心贡献 E-GRPO 的 entity-aware reward 机制对本论文有直接参考价值。阿里巴巴团队。

## [Moskovitz et al. 2024 — Constrained RLHF]
- title: Confronting Reward Model Overoptimization with Constrained RLHF
- authors: Moskovitz et al. (Ted Moskovitz, Aaditya Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca Dragan, Stephen McAleer)
- venue: ICLR 2024
- year: 2024
- arxiv: 2310.04373
- doi: —
- bibtex_key: moskovitz2024constrained
- verified: true
- relevance: 研究 composite RM 的 overoptimization 及约束方法，为本论文多维度 reward (faithfulness + evidence + format) 的平衡问题提供理论支撑
- verification_note: 确认 ICLR 2024 poster。OpenReview ID: gkfUvn0fLU。

---

**总结**: 8/8 全部验证通过。3 篇 must-cite 信息与预期一致（DPO 是 NeurIPS 2023 非 2024）。5 篇 gap-fill 覆盖了 GRPO-for-IE (Adjali, R1-RE)、RL 理论分析 (Jin)、entity-aware reward (E-GRPO)、multi-objective reward hacking (Moskovitz) 四个维度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_rl_alignment_20260517T154253"
}
```

</details>

---
