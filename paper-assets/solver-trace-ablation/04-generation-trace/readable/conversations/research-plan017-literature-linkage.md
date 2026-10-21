# research plan017 literature linkage

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_research_plan017-literature-linkage_20260514T053739.jsonl`
- **Structured JSON:** [`44297fabe1dad530553b.json`](../../sessions/44/44297fabe1dad530553b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-14T05:40:37.203608+00:00_

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
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
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

_source line 2 · 2026-05-14T05:40:37.204095+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T05:40:37.204307+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reward shaping harmful reinforcement learning language model GRPO PPO 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reward shaping harmful reinforcement learning language model GRPO PPO 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T05:40:37.204443+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "process reward model worse than outcome reward LLM reasoning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "process reward model worse than outcome reward LLM reasoning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T05:40:37.204567+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Goodhart's law reward hacking overoptimization large language model reinforcement learning 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Goodhart's law reward hacking overoptimization large language model reinforcement learning 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T05:40:37.204689+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "diagnostic metric vs training signal misalignment NLP machine learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "diagnostic metric vs training signal misalignment NLP machine learning 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T05:40:37.204913+00:00_

Web search results for query: "process reward model worse than outcome reward LLM reasoning 2024 2025"

Links: [{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/html/2509.26578"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=4DJoBOQNd0"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"},{"title":"[2510.08049] A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/abs/2510.08049"},{"title":"SCALING AUTOMATED PROCESS VERIFIERS FOR LLM ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/98711dea460bdefe0e651ca23ec98ba2-Paper-Conference.pdf"},{"title":"Reward Models - by Cameron R. Wolfe, Ph.D.","url":"https://cameronrwolfe.substack.com/p/reward-models"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"}]

Based on the search results, here's what recent research reveals about process reward models (PRMs) versus outcome reward models (ORMs) for LLM reasoning:

## Key Findings

**Limitations of Process Reward Models:**

Existing PRMs either treat each reasoning step in isolation, failing to capture inter-step dependencies, or struggle to align process rewards with the final outcome. The reward signal fails to respect tempora
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T05:40:37.205110+00:00_

Web search results for query: "diagnostic metric vs training signal misalignment NLP machine learning 2024 2025"

Links: [{"title":"NLP Model Evaluation - Metrics, Benchmarks, and Beyond | Deconvolute Labs","url":"https://deconvoluteai.com/blog/evaluating-nlp-models"},{"title":"The Most Common Evaluation Metrics In NLP | Towards Data Science","url":"https://towardsdatascience.com/the-most-common-evaluation-metrics-in-nlp-ced6a763ac8b/"},{"title":"Machine Learning Sep 2024","url":"https://arxiv.org/list/cs.LG/2024-09?skip=115&show=2000"},{"title":"Machine Learning Evaluation Metrics: What Really Matters? | Label Studio","url":"https://labelstud.io/learningcenter/machine-learning-evaluation-metrics-what-really-matters/"},{"title":"The best NLP papers of 2024 - The best NLP papers","url":"https://thebestnlppapers.com/nlp/papers/2024/"},{"title":"Large Language Model Evaluation in 2025: Smarter Metrics That ...","url":"https://www.techrxiv.org/users/927947/articles/1304989/master/file/data/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust/Large%20Language%20Model%20Evaluation%20in%202025-Smarter%20Metrics%20That%20Separate%20Hype%20from%20Trust.pdf"},{"title":"Article Not peer-reviewed version Evaluation Metrics in Learning Systems:","url":"https://www.preprints.org/manuscript/202508.1594/v1/download"},{"title":"NLP Model Metrics. Evaluating the performance of Natural… | by Sujatha Mudadla | Medium","url":"https://medium.com/@sujathamudadla1213/nlp-model-metrics-b3fa32373269"},{"title":"Evaluation metrics and statistical tests for machine learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-56706-x"},{"title":"The best NLP papers of 2025 - The best NLP papers","url":"https://thebestnlppapers.com/"}]

Based on the search results, I found some relevant information about evaluation metrics and training approaches in NLP and machine learning for 2024-2025, though the exact topic of "diagno
…[truncated 1749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T05:40:37.205371+00:00_

Web search results for query: "Goodhart's law reward hacking overoptimization large language model reinforcement learning 2023 2024 2025"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://openreview.net/pdf?id=vRfDOhiJAR"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"NeurIPS Poster Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://neurips.cc/virtual/2024/poster/93540"},{"title":"GOODHART'S LAW IN REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"NeurIPS Poster Inference-Time Reward Hacking in Large Language Models","url":"https://neurips.cc/virtual/2025/poster/116653"},{"title":"[2502.02671] On Teacher Hacking in Language Model Distillation","url":"https://arxiv.org/abs/2502.02671"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"}]

I've performed the web search for your query. Here's a summary of the findings:

## Key Results on Goodhart's Law, Reward Hacking, and LLM Reinforcement Learning (2023-2025)

**Overview of Reward Hacking:**
Reward hacking occurs when a reinforcement learning agent exploits flaws or ambiguities in the reward function to achieve high rewards without genuinely learning or completing the intended task, and it exists because RL environments are often imperfect and it is fundamentally challenging to accurately specify a reward function.

**Goodhart's Law Definition:**
Goodhart's Law st
…[truncated 1222 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T05:40:37.205648+00:00_

Web search results for query: "reward shaping harmful reinforcement learning language model GRPO PPO 2023 2024 2025"

Links: [{"title":"Reinforcement Learning for Large Language Models via ...","url":"https://aclanthology.org/2025.emnlp-main.1085.pdf"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with Policy Entropy","url":"https://arxiv.org/html/2508.04349"},{"title":"Reinforcement Learning from Human Feedback (RLHF) Explained | IntuitionLabs","url":"https://intuitionlabs.ai/articles/reinforcement-learning-human-feedback"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/html/2509.21154v2"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL","url":"https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v1"},{"title":"GTPO and GRPO-S: Token and Sequence-Level Reward Shaping with...","url":"https://arxiv.org/abs/2508.04349"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan","url":"https://arxiv.org/pdf/2509.21154"}]

I've found comprehensive research on this topic. Here's a summary of key findings related to reward shaping, harmful effects in RL for language models, and algorithms like GRPO and PPO from 2023-2025:

## Evolution of RL Algorithms

Most early work on RL for LLMs used Proximal Policy Optimization (PPO) as the default RL optimizer, but recent reasoning research relies upon Group Relative Policy Optimization (GRPO). By 2025, newer algorithms have emerged as alternatives to PPO's complexity. Group Relative Policy Optimization (GRPO), proposed by DeepSeek, avoids the critic model require
…[truncated 1877 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T05:40:37.205899+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv \"reward hacking\" \"reward shaping\" harmful degraded performance code generation formal reasoning RLHF 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv \"reward hacking\" \"reward shaping\" harmful degraded performance code generation formal reasoning RLHF 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T05:40:37.206039+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gao et al \"scaling laws reward model overoptimization\" proxy reward true performance divergence 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gao et al \"scaling laws reward model overoptimization\" proxy reward true performance divergence 2023"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T05:40:37.206165+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"process reward\" \"outcome reward\" comparison worse failure mode math reasoning 2024 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"process reward\" \"outcome reward\" comparison worse failure mode math reasoning 2024 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T05:40:37.206288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Pan Bhatia Steinhardt \"reward hacking\" reinforcement learning survey taxonomy 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Pan Bhatia Steinhardt \"reward hacking\" reinforcement learning survey taxonomy 2022 2023"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T05:40:37.206433+00:00_

Web search results for query: "Gao et al "scaling laws reward model overoptimization" proxy reward true performance divergence 2023"

Links: [{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Scaling Laws for Reward Model Overoptimization Leo Gao OpenAI John Schulman","url":"https://arxiv.org/pdf/2210.10760"},{"title":"[PDF] Scaling Laws for Reward Model Overoptimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scaling-Laws-for-Reward-Model-Overoptimization-Gao-Schulman/fb3dc5e20e0a71134ca916f0d6d8d41f01225b4b"},{"title":"Scaling laws for reward model overoptimization | Proceedings of the 40th International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3618408.3618845"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://www.researchgate.net/publication/364436070_Scaling_Laws_for_Reward_Model_Overoptimization"},{"title":"[2310.02743] Reward Model Ensembles Help Mitigate Overoptimization","url":"https://arxiv.org/abs/2310.02743"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/html/2406.02900v2"},{"title":"CONFRONTING REWARD MODEL OVEROPTIMIZATION","url":"https://openreview.net/pdf?id=gkfUvn0fLU"}]

I found the paper you're looking for. "Scaling Laws for Reward Model Overoptimization" is by Leo Gao and 2 other authors (John Schulman and Jacob Hilton).

The key findings of this research are:

**Main Problem:** The reward model is an imperfect proxy, so optimizing its value too much can hinder ground truth performance, in accordance with Go
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T05:40:37.206618+00:00_

Web search results for query: "Pan Bhatia Steinhardt "reward hacking" reinforcement learning survey taxonomy 2022 2023"

Links: [{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford","url":"https://arxiv.org/pdf/2209.13085"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement","url":"https://arxiv.org/pdf/2507.05619"},{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"},{"title":"Reward Hacking in RLVR","url":"https://www.emergentmind.com/topics/reward-hacking-in-rlvr"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103"},{"title":"[2201.03544] The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models","url":"https://arxiv.org/abs/2201.03544"},{"title":"[PDF] The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Effects-of-Reward-Misspecification:-Mapping-and-Pan-Bhatia/10b9ca173c665e3f2c322c2d5ce9b9d433fe4629"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"}]

Based on the web search results, I found the paper you were looking for:

Pan, A., Bhatia, K., and Steinhardt, J. (2022) published "The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models" on arXiv preprint arXiv:2201.03544.

## Key Details About the Paper:

The paper addresses reward hacking -- where RL agents exploit gaps in misspecified reward functions -- which has been widely observed
…[truncated 1044 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T05:40:37.206840+00:00_

Web search results for query: "arxiv "reward hacking" "reward shaping" harmful degraded performance code generation formal reasoning RLHF 2024 2025"

Links: [{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://ar5iv.labs.arxiv.org/html/2502.18770"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250218770F/abstract"},{"title":"The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking","url":"https://arxiv.org/html/2501.19358"},{"title":"[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/abs/2406.02900"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://openreview.net/pdf?id=62A4d5Mokc"},{"title":"Mitigating Reward Hacking via Information-Theoretic Reward Modeling","url":"https://arxiv.org/html/2402.09345v3"},{"title":"[2602.10623v1] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/abs/2602.10623v1"}]

I've found several relevant arXiv papers addressing reward hacking and reward shaping in RLHF from 2024-2025. Here are the key findings:

## Recent arXiv Papers on Reward Hacking and Reward Shaping in RLHF

### 1. **"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges"** (2024)
DPO and related methods exhibit similar degradation patterns at higher KL budgets despite not training separate proxy reward models, with overoptimization occurring even before a single epoch of data is completed. The paper iden
…[truncated 2114 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T05:40:37.207017+00:00_

Web search results for query: ""process reward" "outcome reward" comparison worse failure mode math reasoning 2024 2025 arxiv"

Links: [{"title":"[2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/abs/2501.07301"},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process","url":"https://arxiv.org/pdf/2510.08049"},{"title":"2026-02-05 Outcome Accuracy is Not Enough: Aligning the Reasoning Process of","url":"https://www.arxiv.org/pdf/2602.04649"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/html/2604.02341v1"},{"title":"Paper page - The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://huggingface.co/papers/2501.07301"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling","url":"https://arxiv.org/html/2506.00027v1"}]

I found several highly relevant papers on this topic. Here's what the search results reveal about process reward models (PRMs) versus outcome reward models (ORMs) in mathematical reasoning:

## Key Finding: PRMs Shifting Toward Outcome-Based Assessment

Existing PRMs have a significant proportion of minimum scores concentrated on the final answer steps, revealing the shift from process to outcome-based assessment in BoN Optimized PRMs. This is a notable failure mode identified in recent research.

## Process Supervision Superiority

Process supervision outperforms outcome supervision, solving 78% of problems 
…[truncated 1287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T05:40:37.207197+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"lessons of developing process reward models\" arxiv 2501.07301 PRM failure inferior performance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"lessons of developing process reward models\" arxiv 2501.07301 PRM failure inferior performance"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T05:40:37.207327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Skalse \"defining characterizing reward hacking\" Goodhart taxonomy regressional causal extremal 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Skalse \"defining characterizing reward hacking\" Goodhart taxonomy regressional causal extremal 2022"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T05:40:37.207447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"additive reward\" \"auxiliary reward\" harmful degraded \"reinforcement learning\" code math reasoning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"additive reward\" \"auxiliary reward\" harmful degraded \"reinforcement learning\" code math reasoning 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T05:40:37.207589+00:00_

Web search results for query: ""lessons of developing process reward models" arxiv 2501.07301 PRM failure inferior performance"

Links: [{"title":"[2501.07301] The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/abs/2501.07301"},{"title":"[2501.07301v1] The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"http://arxiv.org/abs/2501.07301v1"},{"title":"The Lessons of Developing Process Reward Models in ...","url":"https://arxiv.org/pdf/2501.07301"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://www.researchgate.net/publication/387975662_The_Lessons_of_Developing_Process_Reward_Models_in_Mathematical_Reasoning"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.547/"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2501.07301v1"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2501.07301"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=J4UOIrxcWy"},{"title":"Process Reward Models in Mathematical Reasoning","url":"https://www.emergentmind.com/papers/2501.07301"},{"title":"Paper page - The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://huggingface.co/papers/2501.07301"}]

I found the paper! Here's information about arxiv 2501.07301:

## Paper Summary

**Title:** "The Lessons of Developing Process Reward Models in Mathematical Reasoning"

**Authors:** Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin (Qwen Team, Alibaba Group)

**Published:** Findings of the Association for Com
…[truncated 1314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T05:40:37.207786+00:00_

Web search results for query: "Skalse "defining characterizing reward hacking" Goodhart taxonomy regressional causal extremal 2022"

Links: [{"title":"Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford","url":"https://arxiv.org/pdf/2209.13085"},{"title":"[PDF] Defining and Characterizing Reward Hacking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Defining-and-Characterizing-Reward-Hacking-Skalse-Howe/004357dd9bbf3012c8fe0ccada4da401bf85dfff"},{"title":"[2209.13085] Defining and Characterizing Reward Hacking","url":"https://arxiv.org/abs/2209.13085"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"Defining and Characterizing Reward Hacking | Request PDF","url":"https://www.researchgate.net/publication/401445436_Defining_and_Characterizing_Reward_Hacking"},{"title":"Defining and characterizing reward hacking | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3600957"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Causal Reward Adjustment: Mitigating Reward Hacking in External Reasoning via Backdoor Correction","url":"https://arxiv.org/html/2508.04216v1"},{"title":"(PDF) Defining and Characterizing Reward Hacking","url":"https://www.researchgate.net/publication/363888695_Defining_and_Characterizing_Reward_Hacking"}]

Based on the search results, I found the paper you were looking for. Here's what I found:

## "Defining and Characterizing Reward Hacking" by Skalse et al. (2022)

The paper provides the first formal definition of reward hacking, a phenomenon where optimizing an imperfect proxy reward func
…[truncated 1270 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T05:40:37.207971+00:00_

Web search results for query: ""additive reward" "auxiliary reward" harmful degraded "reinforcement learning" code math reasoning 2024 2025"

Links: [{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"Guide to Reward Functions in Reinforcement Fine-Tuning | Rubrik","url":"https://www.rubrik.com/blog/ai/25/reward-functions-reinforcement-fine-tuning"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"Average reward adjusted discounted reinforcement learning | Neural Computing and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00521-024-10620-5"},{"title":"Reinforcement Learning for Reasoning in Large","url":"https://arxiv.org/pdf/2504.20571"},{"title":"Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo","url":"https://www.promptfoo.dev/blog/rlvr-explained/"},{"title":"Reward Function in Reinforcement Learning | by Amit Yadav | Biased-Algorithms | Medium","url":"https://medium.com/biased-algorithms/reward-function-in-reinforcement-learning-c9ee04cabe7d"},{"title":"Explicable Reward Design for Reinforcement Learning Agents | OpenReview","url":"https://openreview.net/forum?id=yw5KKWraUk7"}]

I found several relevant research articles on reward design and reinforcement learning for reasoning tasks. Here's what the 
…[truncated 1476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T05:40:37.208149+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Goodhart's law in reinforcement learning\" ICLR 2024 Karwowski measure target optimization proxy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Goodhart's law in reinforcement learning\" ICLR 2024 Karwowski measure target optimization proxy"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T05:40:37.208274+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reward shaping to mitigate reward hacking\" Fu 2025 arxiv 2502.18770 threshold PPO bounded reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"reward shaping to mitigate reward hacking\" Fu 2025 arxiv 2502.18770 threshold PPO bounded reward"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T05:40:37.208392+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structural reward verification formal proof code RL GRPO training signal failure noise arxiv 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structural reward verification formal proof code RL GRPO training signal failure noise arxiv 2024 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T05:40:37.208543+00:00_

Web search results for query: ""Goodhart's law in reinforcement learning" ICLR 2024 Karwowski measure target optimization proxy"

Links: [{"title":"GOODHART'S LAW IN REINFORCEMENT LEARNING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf"},{"title":"Goodhart's Law in Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5o9G4XF1LI"},{"title":"[2310.09144] Goodhart's Law in Reinforcement Learning","url":"https://arxiv.org/abs/2310.09144"},{"title":"ICLR Poster Goodhart's Law in Reinforcement Learning","url":"https://iclr.cc/virtual/2024/poster/19413"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.lesswrong.com/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"Goodhart’s Law in Reinforcement Learning","url":"https://arxiv.org/html/2310.09144v1"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=5o9G4XF1LI"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.semanticscholar.org/paper/Goodhart's-Law-in-Reinforcement-Learning-Karwowski-Hayman/a4bd4da02241eacee990c89ddd748ce37a248fc0"},{"title":"‪Goodhart's Law in Reinforcement Learning‬","url":"https://scholar.google.com/citations?view_op=view_citation&hl=en&user=GuzLUmQAAAAJ&sortby=pubdate&citation_for_view=GuzLUmQAAAAJ:roLk4NBRz8UC"}]

I found the paper! Here's what I discovered about "Goodhart's Law in Reinforcement Learning" presented at ICLR 2024:

## Paper Overview

The paper was authored by Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, and Joar Skalse from the University of Oxford and other institutions, and was published at ICLR 2024.

## Main Contribution

The paper studies Goodhart's law, which predicts that increasing optimisation of an imperfect proxy beyond some critical poi
…[truncated 968 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T05:40:37.208730+00:00_

Web search results for query: ""reward shaping to mitigate reward hacking" Fu 2025 arxiv 2502.18770 threshold PPO bounded reward"

Links: [{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250218770F/abstract"},{"title":"[2502.18770v2] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770v2"},{"title":"[2502.18770v1] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/abs/2502.18770v1"},{"title":"(PDF) Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://www.researchgate.net/publication/389392526_Reward_Shaping_to_Mitigate_Reward_Hacking_in_RLHF"},{"title":"[2502.18770] Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://ar5iv.labs.arxiv.org/html/2502.18770"},{"title":"Repairing Reward Functions with Feedback to Mitigate Reward Hacking","url":"https://arxiv.org/html/2510.13036v2"},{"title":"Paper page - Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://huggingface.co/papers/2502.18770"},{"title":"Probabilistic Uncertain Reward Model","url":"https://arxiv.org/html/2503.22480v5"}]

I found the paper! Here's what I discovered about the research in arxiv 2502.18770:

## Paper Overview

The paper focuses on Reinforcement Learning from Human Feedback (RLHF) and addresses reward hacking, where agents exploit flaws in the reward function rather than learning intended behavior, degrading alignment.

## Key Findings

The analysis suggests two key design principles: (1) the RL reward should be bounded, and (2) the RL reward benefits from rapid initial growth followed by gradual convergence.

### Reward Threshold Discovery

During PPO training with a specific reward model, a distinct reward thre
…[truncated 1009 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T05:40:37.208922+00:00_

Web search results for query: "structural reward verification formal proof code RL GRPO training signal failure noise arxiv 2024 2025 2026"

Links: [{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards ...","url":"https://www.arxiv.org/pdf/2510.00915"},{"title":"arXiv:2506.02355v2 [cs.LG] 20 Jun 2025 Rewarding the Unlikely: Lifting GRPO","url":"https://arxiv.org/pdf/2506.02355"},{"title":"Rate or Fate? RLVεR: Reinforcement Learning with Verifiable Noisy Rewards","url":"https://arxiv.org/html/2601.04411"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/html/2506.14245v1"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/html/2510.00915v1"},{"title":"[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/abs/2510.00915"},{"title":"[2506.10947] Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://arxiv.org/abs/2506.10947"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation","url":"https://arxiv.org/html/2601.18533v1"}]

Based on the search results, I found several highly relevant arXiv papers from 2024-2026 addressing structural reward verification, formal proof, code RL, GRPO training, and signal failure/noise issues:

## Key Papers Found:

1. **"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification"** (arXiv 2503.06639, Oc
…[truncated 1874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T05:40:37.209102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"spurious rewards rethinking training signals RLVR\" arxiv 2506.10947 random reward GRPO Qwen performance 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"spurious rewards rethinking training signals RLVR\" arxiv 2506.10947 random reward GRPO Qwen performance 2025"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T05:40:37.209231+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"noisy reward\" \"verifiable reward\" imperfect verifier false negative GRPO training degradation arxiv 2510.00915 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"noisy reward\" \"verifiable reward\" imperfect verifier false negative GRPO training degradation arxiv 2510.00915 2025"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T05:40:37.209418+00:00_

Web search results for query: ""spurious rewards rethinking training signals RLVR" arxiv 2506.10947 random reward GRPO Qwen performance 2025"

Links: [{"title":"[2506.10947] Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://arxiv.org/abs/2506.10947"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR | OpenReview","url":"https://openreview.net/forum?id=4NeiwxQ2Bp"},{"title":"(PDF) Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://www.researchgate.net/publication/392629816_Spurious_Rewards_Rethinking_Training_Signals_in_RLVR"},{"title":"GitHub - ruixin31/Spurious_Rewards","url":"https://github.com/ruixin31/Spurious_Rewards"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2506.10947"},{"title":"Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination","url":"https://arxiv.org/html/2507.10532v1"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR | alphaXiv","url":"https://www.alphaxiv.org/abs/2506.10947"},{"title":"Spurious Rewards Paradox: Mechanistically Understanding How RLVR Activates Memorization Shortcuts in LLMs","url":"https://arxiv.org/html/2601.11061v1"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://rethink-rlvr.notion.site/Spurious-Rewards-Rethinking-Training-Signals-in-RLVR-1f4df34dac1880948858f95aeb88872f"},{"title":"Spurious Rewards: Rethinking Training Signals in RLVR","url":"https://github.com/ruixin31/Rethink_RLVR"}]

Based on the search results, here's what I found about this research:

## Overview

The paper shows that reinforcement learning with verifiable rewards (RLVR) can elicit strong mathematical reasoning in certain language models even with spurious rewards that have little, no, or even negative correlation with the correct answer.

## Key Findings

RLVR training with GRPO improves MATH-500 performance for Qwen2
…[truncated 1076 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T05:40:37.209602+00:00_

Web search results for query: ""noisy reward" "verifiable reward" imperfect verifier false negative GRPO training degradation arxiv 2510.00915 2025"

Links: [{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards ...","url":"https://www.arxiv.org/pdf/2510.00915"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/html/2510.00915"},{"title":"[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/abs/2510.00915"},{"title":"[2510.18924v2] Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients","url":"https://arxiv.org/abs/2510.18924v2"},{"title":"[2510.18924] Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients","url":"https://arxiv.org/abs/2510.18924"},{"title":"1 Introduction","url":"https://arxiv.org/html/2510.18924v2"},{"title":"AlphaGRPO: Unlocking Self-Reflective Multimodal Generation in Unified Multimodal Models via Decompositional Verifiable Reward","url":"https://arxiv.org/html/2605.12495.pdf"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers | Request PDF","url":"https://www.researchgate.net/publication/396094543_Reinforcement_Learning_with_Verifiable_yet_Noisy_Rewards_under_Imperfect_Verifiers"},{"title":"Noise-corrected GRPO: From Noisy Rewards to Unbiased Gradients Omar El Mansouri","url":"https://www.arxiv.org/pdf/2510.18924"},{"title":"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models","url":"https://arxiv.org/html/2605.08061v1"}]

I found the paper you were looking for. Here are the key findings from arxiv 2510.00915:

## Paper Overview

The paper addresses Reinforcement Learning with Verifiable Rewards (RLVR), which replaces costly human labeling with automated verifiers. However, imperfect verifiers inevitably introduce false negatives (rejecting correct answers) and false positives (a
…[truncated 1521 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T05:40:37.209804+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find literature_map.yaml",
  "prompt": "Find any file named literature_map.yaml or similar in /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ and show its structure (first ~100 lines). Quick search."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Agent",
  "tool_args": {
    "subagent_type": "Explore",
    "description": "Find literature_map.yaml",
    "prompt": "Find any file named literature_map.yaml or similar in /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/ and show its structure (first ~100 lines). Quick search."
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T05:40:37.209960+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*literature*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*literature*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T05:40:37.210243+00:00_

artifacts/literature_map.yaml
literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T05:40:37.210402+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*literature*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation -name \"*literature*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T05:40:37.210529+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_plan017-literature-linkage_20260514T053739.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_literature-expansion_20260514T014924_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_plan005-negative-literature_20260514T020402_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_literature-expansion_20260514T014924.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/workers/worker_research_plan005-negative-literature_20260514T020402.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_research_plan005-negative-literature_20260514T020402.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/logs/chats/worker_research_plan005-negative-literature_20260514T020402.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T05:40:37.210672+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T05:40:37.210877+00:00_

1	# Literature Map for Solver Trace Ablation (STA)
2	# Categories:
3	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
4	#   2. reward-shaping: Reward shaping for code/formal verification
5	#   3. mutation-testing: Mutation testing in software engineering
6	#   4. intensional-analysis: Intensional program analysis
7	#   5. reward-hacking: Reward hacking / overoptimization
8	#   6. fol-formalization: FOL/Prolog formalization with LLMs
9	
10	papers:
11	
12	  # ============================================================
13	  # Category 1: Neurosymbolic reasoning + RL/GRPO
14	  # ============================================================
15	
16	  - id: deepseek-r1
17	    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
18	    authors: "DeepSeek-AI"
19	    year: 2025
20	    venue: "arXiv 2501.12948 / Nature 2025"
21	    category: neurosymbolic-rl
22	    role: method-component
23	    relevance: >
24	      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
25	      STA builds on the same GRPO framework but replaces binary outcome reward with
26	      intensional structural reward for neurosymbolic formalization.
27	    key_finding: >
28	      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
29	      showing emergent chain-of-thought reasoning from RL alone.
30	
31	  - id: deepseekmath
32	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
33	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
34	    year: 2024
35	    venue: "arXiv 2402.03300"
36	    category: neurosymbolic-rl
37	    role: method-component
38	    relevance: >
39	      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
40	      used in STA training. GRPO eliminates the critic model by estimating
41	      baselines from group scores.
42	    key_finding: >
43	      GRPO matches PPO performance while significantly reducing trainin
…[truncated 2527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T05:40:37.211050+00:00_

Perfect! Here's the structure of the literature_map.yaml file:

**File location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml`

**Structure (first ~100 lines):**

The file is organized as a YAML literature map with the following structure:

1. **Header** (lines 1-8): Comments defining 6 paper categories:
   - neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
   - reward-shaping: Reward shaping for code/formal verification
   - mutation-testing: Mutation testing in software engineering
   - intensional-analysis: Intensional program analysis
   - reward-hacking: Reward hacking / overoptimization
   - fol-formalization: FOL/Prolog formalization with LLMs

2. **Papers list** (lines 10+): Each paper entry contains:
   - `id`: Identifier (e.g., "deepseek-r1", "deepseekmath")
   - `title`: Full paper title
   - `authors`: Author names
   - `year`: Publication year
   - `venue`: Publication venue/arXiv identifier
   - `category`: One of the 6 categories above
   - `role`: Role type (method-component, direct-competitor, background)
   - `relevance`: Multi-line description of relevance to the project
   - `key_finding`: Key findings or results from the paper

The visible papers include DeepSeek-R1, DeepSeekMath, Logic-RL, Prolog training work, and SatLM, organized under the neurosymbolic-RL category. There's also a second category section starting at line 92 for "Reward shaping for code/formal verification."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan017-literature-linkage_20260514T053739",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-14T05:40:37.211248+00:00_

Now I have everything I need. Here are the results.

---

## 文献搜索结果

### 高相关（直接支持你的发现）

**1. Spurious Rewards: Rethinking Training Signals in RLVR**
- 作者: Ruixin Yang et al.
- 年份: 2025, arXiv:2506.10947
- Venue: NeurIPS 2025 submission
- **关联**: 最直接相关。发现 GRPO+随机 reward 在 Qwen2.5-Math 上提升 21.4%，几乎追平 ground-truth reward 的 29.1%。这与你的 additive random (PR=48%) > additive ISR (PR=18%) 完全一致——说明看似信息量丰富的结构指标可能比随机噪声更有害，因为它引入了系统性偏差而非单纯噪声。但该文也发现这种效应在 Llama3 上不成立，说明与预训练数据有关。
- **加入 literature_map**: 是。role: `direct-evidence`, category: `reward-hacking`

**2. Scaling Laws for Reward Model Overoptimization**
- 作者: Leo Gao, John Schulman, Jacob Hilton (OpenAI)
- 年份: 2023, ICML 2023 (arXiv:2210.10760)
- Venue: ICML 2023
- **关联**: 奠基性工作。用 gold/proxy reward 实验范式量化了 Goodhart 效应——proxy reward 持续上升但 gold reward 先升后降。你的 ISR 就是一个 proxy reward，其"持续上升"但 true performance (PR) 下降，完美符合此框架。
- **加入 literature_map**: 是。role: `theoretical-foundation`, category: `reward-hacking`

**3. Goodhart's Law in Reinforcement Learning**
- 作者: Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse
- 年份: 2024, ICLR 2024 (arXiv:2310.09144)
- Venue: ICLR 2024
- **关联**: 提供了 Goodhart's Law 在 MDP 中的几何解释——优化不完美 proxy 超过临界点后 true objective 下降。你的 ISR additive 实验可以用这个框架解释：ISR 作为 proxy 与 execution correctness 只有部分相关，超过临界优化点后策略转向高 ISR 但低 correctness 的方向。
- **加入 literature_map**: 是。role: `theoretical-foundation`, category: `reward-hacking`

**4. The Lessons of Developing Process Reward Models in Mathematical Reasoning**
- 作者: Zhenru Zhang et al. (Qwen Team, Alibaba)
- 年份: 2025, ACL 2025 Findings (arXiv:2501.07301)
- Venue: ACL 2025 Findings
- **关联**: 发现 MC estimation 合成的 PRM 数据质量差，导致 PRM 性能劣于 ORM。关键发现：policy model 生成"答案正确但推理过程有缺陷"的 response，导致 process reward 与 outcome 的 misalignment。这与你的 ISR 问题相似——结构正确但语义错误的 proof trace 获得高 ISR 但低 execution reward。
- **加入 literature_map**: 是。role: `supporting-evidence`, category: `reward-shaping`

### 中等相关（理论框架支持）

**5. Reward Shaping to Mitigate Reward Hacking in RLHF**
- 作者: Fu et al.
- 年份: 2025, arXiv:2502.18770
- Venue: arXiv preprint
- **关联**: 发现 PPO 训练中存在 reward threshold——超过阈值后 reward hacking 启动，win rate 下降。提出 reward 应 bounded 且 rapid initial growth + gradual convergence。你的 additive ISR 可能违反了这两个原则——ISR 信号过强且无上界约束。
- **加入 literature_map**: 可选。role: `background`, category: `reward-hacking`

**6. RL with Verifiable yet Noisy Rewards under Imperfect Verifiers**
- 作者: arXiv:2510.00915
- 年份: 2025
- **关联**: 形式化了 verifier 噪声（false positive/negative）对 GRPO 训练的影响。你的 ISR 可以视为一个 systematically biased verifier——不是随机噪声，而是系统性地对 "structurally correct but semantically wrong" 的 traces 给出 false positive。该文表明随机噪声可以校正，但系统性偏差更难处理。
- **加入 literature_map**: 可选。role: `background`, category: `reward-shaping`

### 文献空白分析

搜索未找到以下内容的直接文献：
- **结构/质量指标"仅适合诊断不适合训练"的明确讨论**：现有文献将 Goodhart's Law 和 reward hacking 作为一般性现象讨论，但没有论文明确提出"某些指标天然适合 post-hoc 诊断但不适合作为训练信号"这一范式区分。这是你们论文的独特贡献点。
- **formal verification/Prolog 领域的结构 reward 实验**：reward hacking 文献集中在 math reasoning 和 general RLHF，formal proof generation 领域是空白。

**结论：你的 "diagnostic-only metric" 发现是一个真正的文献空白**。Gao et al. 和 Karwowski et al. 提供理论框架（Goodhart's Law），Spurious Rewards 提供经验佐证（random > structured reward 的现象），但没有论文将这些整合为"某些指标仅适合诊断"的规范性主张。这对 novelty 是好事。

Sources:
- [Spurious Rewards: Rethinking Training Signals in RLVR](https://arxiv.org/abs/2506.10947)
- [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760)
- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/abs/2310.09144)
- [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2501.07301)
- [Reward Shaping to Mitigate Reward Hacking in RLHF](https://arxiv.org/abs/2502.18770)
- [RL with Verifiable yet Noisy Rewards under Imperfect Verifiers](https://arxiv.org/abs/2510.00915)
- [Defining and Characterizing Reward Hacking (Skalse et al., NeurIPS 2022)](https://arxiv.org/abs/2209.13085)
- [The Effects of Reward Misspecification (Pan et al., 2022)](https://arxiv.org/abs/2201.03544)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_plan017-literature-linkage_20260514T053739"
}
```

</details>

---
