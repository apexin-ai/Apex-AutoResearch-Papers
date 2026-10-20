# research 1000step literature paper prep

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_1000step-literature-paper-prep_20260515T113705.jsonl`
- **Structured JSON:** [`c4ca85f77866341b3906.json`](../../sessions/c4/c4ca85f77866341b3906.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-15T11:40:47.555134+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,WebSearch",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T11:40:47.555486+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T11:40:47.555657+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T11:40:47.556384+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n#   7. goodhart-overoptimization: Goodhart's Law theory and dose-response dynamics\\n#   8. verification-reward: Solver/prover as RL reward signal\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: met
…[truncated 43923 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T11:40:47.556587+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reward hacking temporal dynamics longer training GRPO reinforcement learning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reward hacking temporal dynamics longer training GRPO reinforcement learning 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T11:40:47.556743+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Goodhart's Law reward overoptimization training steps RLHF 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Goodhart's Law reward overoptimization training steps RLHF 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T11:40:47.556870+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "mode collapse GRPO group relative policy optimization reward hacking 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "mode collapse GRPO group relative policy optimization reward hacking 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T11:40:47.557034+00:00_

Web search results for query: "mode collapse GRPO group relative policy optimization reward hacking 2024 2025"

Links: [{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/html/2509.22047v1"},{"title":"On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement","url":"https://arxiv.org/html/2512.04220"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250922047I/abstract"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Request PDF","url":"https://www.researchgate.net/publication/395944746_MO-GRPO_Mitigating_Reward_Hacking_of_Group_Relative_Policy_Optimization_on_Multi-Objective_Problems"},{"title":"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems | Takara TLDR","url":"https://tldr.takara.ai/p/2509.22047"},{"title":"Beyond PPO - The New Wave of Policy Optimization Techniques for LLM Post-Training | yadnyesh's blog","url":"https://ydnyshhh.github.io/posts/policy_optimization/"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"},{"title":"Group-Relative Policy Optimization (GRPO)","url":"https://www.emergentmind.com/topics/group-relative-policy-optimization-grpo-80231350-b526-499e-a622-c1842a092a98"}]

Based on the search results, here's what I found regarding mode collapse, GRPO (Group Relative Policy Optimization), and reward hacking:

## Key Findings on Mode
…[truncated 1668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T11:40:47.557217+00:00_

Web search results for query: "reward hacking temporal dynamics longer training GRPO reinforcement learning 2024 2025"

Links: [{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v4"},{"title":"From Verifiable Dot to Reward Chain: Harnessing Verifiable Reference-based Rewards for Reinforcement Learning of Open-ended Generation","url":"https://arxiv.org/html/2601.18533v1"},{"title":"DAPO: An Open Source LLM Reinforcement Learning System at Scale","url":"https://self-supervised.cs.jhu.edu/fa2025/files/presentations/Why-RL-Sep16-AdvancesNLP.pdf"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs","url":"https://arxiv.org/html/2506.14245v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"(PDF) Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://www.researchgate.net/publication/389392526_Reward_Shaping_to_Mitigate_Reward_Hacking_in_RLHF"},{"title":"arXiv:2504.16084v1 [cs.CL] 22 Apr 2025 TTRL: Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2504.16084v1"}]

Based on the web search results, I found relevant research on reward hacking, temporal dynamics, longer training, and GRPO reinforcement learning from 2024-2025. Here are the key findings:

## Reward Hacking and GRPO

GRPO does not exhibit the reward hacking problem during training, primarily because its advantage calculation effectiv
…[truncated 1527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T11:40:47.557395+00:00_

Web search results for query: "Goodhart's Law reward overoptimization training steps RLHF 2024 2025"

Links: [{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"confronting reward model overoptimization","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5eee634cb9729b8bcc2ec9f2a46a74ae-Paper-Conference.pdf"},{"title":"Catastrophic Goodhart: regularizing RLHF with KL divergence does not mitigate heavy-tailed reward misspecification | OpenReview","url":"https://openreview.net/forum?id=UXuBzWoZGK&noteId=YiStZYdof7"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"[2210.10760] Scaling Laws for Reward Model Overoptimization","url":"https://arxiv.org/abs/2210.10760"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.05584"},{"title":"RETHINKING REWARD MODEL EVALUATION: ARE WE ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/93f250215e4889119807b6fac3a57aec-Paper-Conference.pdf"},{"title":"Goodhart's Law in Reinforcement Learning","url":"https://www.lesswrong.com/posts/Eu6CvP7c7ivcGM3PJ/goodhart-s-law-in-reinforcement-learning"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"}]

Based on the web search results, here's what recent research reveals about Goodhart's Law, reward overoptimization, and RLHF training:

## Goodhart's Law and Reward Overoptimization

Goodhart's Law explains that any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes. This has evolved to the notion that "When a measure becomes a targe
…[truncated 1345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T11:40:47.557660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reward hacking multiple pathways modes specification gaming reinforcement learning LLM 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reward hacking multiple pathways modes specification gaming reinforcement learning LLM 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T11:40:47.557845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reward overoptimization\" \"training steps\" quality degrades monotonically RLHF GRPO 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"reward overoptimization\" \"training steps\" quality degrades monotonically RLHF GRPO 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T11:40:47.557970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GRPO policy collapse entropy training longer steps degradation reasoning quality 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GRPO policy collapse entropy training longer steps degradation reasoning quality 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T11:40:47.558152+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"On Group Relative Policy Optimization Collapse\" lazy likelihood displacement 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"On Group Relative Policy Optimization Collapse\" lazy likelihood displacement 2024"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T11:40:47.558317+00:00_

Web search results for query: ""reward overoptimization" "training steps" quality degrades monotonically RLHF GRPO 2024 2025"

Links: [{"title":"Reward Model Overoptimization: Root Causes and Mitigations","url":"https://www.reinforced.info/p/reward-model-overoptimization"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/html/2505.18126v1"},{"title":"Iterative Data Smoothing: Mitigating Reward Overfitting and Overoptimization in RLHF","url":"https://proceedings.mlr.press/v235/zhu24e.html"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"[2406.02900] Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://arxiv.org/abs/2406.02900"},{"title":"Off-Policy Corrected Reward Modeling for Reinforcement ...","url":"https://johannesack.github.io/assets/pdf/ocrm.pdf"},{"title":"[2505.18126] Reward Model Overoptimisation in Iterated RLHF","url":"https://arxiv.org/abs/2505.18126"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"(PDF) Reward Model Overoptimisation in Iterated RLHF","url":"https://www.researchgate.net/publication/392085615_Reward_Model_Overoptimisation_in_Iterated_RLHF"}]

I've found comprehensive information about reward overoptimization in RLHF and related algorithms. Here's what the research reveals:

## Key Findings on Reward Overoptimization

### The Core Problem

The reward model's score keeps improving during training, but actual quality (as measured by held-out evaluations or human judgment) eventually degrades. A combination of reward hacking and distribution shift inevitably leads to overoptimization, where it is easier for the RL agent to learn to exploit the inefficiencies of the reward model than to learn to genuinely impr
…[truncated 1345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T11:40:47.558497+00:00_

Web search results for query: ""On Group Relative Policy Optimization Collapse" lazy likelihood displacement 2024"

Links: [{"title":"On Group Relative Policy Optimization Collapse in Agent Search: The Lazy Likelihood-Displacement","url":"https://arxiv.org/html/2512.04220v2"},{"title":"On Group Relative Policy Optimization Collapse in Agent ...","url":"https://arxiv.org/abs/2512.04220"},{"title":"Paper page - On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://huggingface.co/papers/2512.04220"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://arxiv.org/html/2512.04220v1"},{"title":"[Literature Review] On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://www.themoonlight.io/en/review/on-grpo-collapse-in-search-r1-the-lazy-likelihood-displacement-death-spiral"},{"title":"GitHub - vengdeng/LLDS-On-Group-Relative-Policy-Optimization-Collapse-in-Search-R1 · GitHub","url":"https://github.com/vengdeng/LLDS-On-Group-Relative-Policy-Optimization-Collapse-in-Search-R1"},{"title":"[2508.03772] GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/abs/2508.03772"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250803772S/abstract"},{"title":"GTPO: Stabilizing Group Relative Policy Optimization via Gradient and Entropy Control","url":"https://arxiv.org/html/2508.03772v4"},{"title":"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral","url":"https://www.researchgate.net/publication/398357251_On_GRPO_Collapse_in_Search-R1_The_Lazy_Likelihood-Displacement_Death_Spiral"}]

I found comprehensive information about the paper you searched for. Here's what the research reveals:

## Overview

The paper is titled "On GRPO Collapse in Search-R1: The Lazy Likelihood-Displac
…[truncated 1537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T11:40:47.558668+00:00_

Web search results for query: "GRPO policy collapse entropy training longer steps degradation reasoning quality 2025 2026"

Links: [{"title":"EDGE-GRPO: Entropy-Driven GRPO with Guided Error Correction for Advantage Diversity","url":"https://arxiv.org/html/2507.21848v1"},{"title":"Arbitrary Entropy Policy Optimization","url":"https://arxiv.org/pdf/2510.08141"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"Info-GRPO: Training Reasoning Models via Correlation-Aware Exploration | OpenReview","url":"https://openreview.net/forum?id=d5qElNtXS5"},{"title":"GTPO: Trajectory-Based Policy Optimization in Large Language Models","url":"https://arxiv.org/html/2508.03772v3"},{"title":"Efficient Reinforcement Learning with Semantic and Token ...","url":"https://arxiv.org/pdf/2512.04359"},{"title":"[2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning","url":"https://arxiv.org/abs/2510.19807"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2603.11682"},{"title":"Arbitrary Entropy Policy Optimization Breaks The Exploration Bottleneck of Reinforcement Learning","url":"https://arxiv.org/html/2510.08141"},{"title":"Step-GRPO: Internalizing Dynamic Early Exit for Efficient Reasoning","url":"https://arxiv.org/html/2604.16890v1"}]

Based on the search results, I found substantial recent research on GRPO (Group Relative Policy Optimization) policy collapse, entropy training, and reasoning quality degradation from 2025-2026. Here's what the research reveals:

## GRPO Policy Collapse and Entropy Issues

GRPO suffers from entropy collapse: as training progresses, policy entropy declines monotonically, sampled outputs converge to nearly identical solutions, and the model prematurely adopts a deterministic policy with limited exploration. The Group Relative Policy Optimization (GRPO) algorithm, which relies on sparse
…[truncated 1485 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T11:40:47.558934+00:00_

Web search results for query: "reward hacking multiple pathways modes specification gaming reinforcement learning LLM 2024 2025 2026"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Quickly Assessing Reward Hacking-like Behavior in LLMs ...","url":"https://www.lesswrong.com/posts/quTGGNhGEiTCBEAX5/quickly-assessing-reward-hacking-like-behavior-in-llms-and"},{"title":"Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use","url":"https://arxiv.org/html/2605.02964"},{"title":"2025-Era “Reward Hacking” Does Not Show that ...","url":"https://www.alignmentforum.org/posts/wwRgR3K8FKShjwwL5/2025-era-reward-hacking-does-not-show-that-reward-is-the"},{"title":"Reward hacking - Wikipedia","url":"https://en.wikipedia.org/wiki/Reward_hacking"},{"title":"[2604.13602] Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/abs/2604.13602"},{"title":"Training on Documents about Reward Hacking Induces Reward Hacking","url":"https://alignment.anthropic.com/2025/reward-hacking-ooc/"}]

I've performed the web search for your query. Here are the key findings on reward hacking across multiple pathways, modes, and specification gaming in reinforcement learning and LLMs:

## Core Concept and Manifestations

Reward hacking occurs when a reinforcement learning (RL) agent exploits flaws or ambiguities in the reward function to achieve high rewards, without genuinely l
…[truncated 2177 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T11:40:47.559132+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"genuine\" OR \"faithful\" reasoning quality decreases training steps reinforcement learning reward hacking taxonomy pathways 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"genuine\" OR \"faithful\" reasoning quality decreases training steps reinforcement learning reward hacking taxonomy pathways 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T11:40:47.559261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reward hacking taxonomy classification types modes neurosymbolic formal verification RL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reward hacking taxonomy classification types modes neurosymbolic formal verification RL 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T11:40:47.559410+00:00_

Web search results for query: ""genuine" OR "faithful" reasoning quality decreases training steps reinforcement learning reward hacking taxonomy pathways 2024 2025 2026"

Links: [{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking Mitigation using Verifiable Composite Rewards","url":"https://arxiv.org/html/2509.15557v1"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"Reinforcement Learning with Missing Context to Mitigate Reward Hacking from Training Only on Golden Answers | OpenReview","url":"https://openreview.net/forum?id=eOqnXPOl4S"},{"title":"Monitoring Reasoning Models for Misbehavior and the Risks of","url":"https://cdn.openai.com/pdf/34f2ada6-870f-4c26-9790-fd8def56387f/CoT_Monitoring.pdf"},{"title":"November 25, 2025 Does Reinforcement Learning Really Incentivize Reasoning","url":"https://arxiv.org/pdf/2504.13837"},{"title":"RRM: ROBUST REWARD MODEL TRAINING MITI","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/9d46574e5baae5121180228223a11836-Paper-Conference.pdf"},{"title":"Reward Hacking Mitigation using Verifiable Composite ...","url":"https://dl.acm.org/doi/pdf/10.1145/3765612.3767230"}]

Based on the web search results, I found highly relevant research on the relationship between genuine/faithful reasoning quality and reinforcement learning training in the context of reward hacking. Here are the key findings:

## Key Taxonomy and Pathways of Reward Hacking

Common manifestations of reward hacking in reasoning models include reasoning without solving, using to
…[truncated 2029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T11:40:47.559580+00:00_

Web search results for query: "reward hacking taxonomy classification types modes neurosymbolic formal verification RL 2025 2026"

Links: [{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103v1"},{"title":"Reward Hacking Mitigation using Verifiable Composite ...","url":"https://dl.acm.org/doi/pdf/10.1145/3765612.3767230"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement","url":"https://arxiv.org/pdf/2507.05619"},{"title":"Reinforcement Learning from Verifiable Rewards | Label Studio","url":"https://labelstud.io/blog/reinforcement-learning-from-verifiable-rewards/"},{"title":"In-Context Reward Hacking Behaviors","url":"https://www.emergentmind.com/topics/in-context-reward-hacking-behaviors"},{"title":"Reward Hacking in RLVR","url":"https://www.emergentmind.com/topics/reward-hacking-in-rlvr"}]

Based on the web search results, here's a comprehensive overview of recent research on reward hacking taxonomy, classification, types, and modes in reinforcement learning, with connections to neurosymbolic systems and formal verification:

## Taxonomy and Classification of Reward Hacking

Research proposes a unified taxonomy of reward hacking mechanisms at Feature, Representation, Evaluator, and Environment levels, systematically reviewing manifestations across text-only LLMs and multimodal/agentic systems.

Recent work categorizes coding reward hacks into specification gaming, reward tampering, misalignmen
…[truncated 2356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T11:40:47.559789+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Does Reinforcement Learning Really Incentivize Reasoning\" arXiv 2504.13837 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Does Reinforcement Learning Really Incentivize Reasoning\" arXiv 2504.13837 2025"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T11:40:47.559924+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"reward hacking\" \"verifiable reward\" GRPO formal logic prolog solver longer training collapse 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"reward hacking\" \"verifiable reward\" GRPO formal logic prolog solver longer training collapse 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T11:40:47.560078+00:00_

Web search results for query: ""Does Reinforcement Learning Really Incentivize Reasoning" arXiv 2504.13837 2025"

Links: [{"title":"[2504.13837] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/abs/2504.13837"},{"title":"November 25, 2025 Does Reinforcement Learning Really Incentivize Reasoning","url":"https://arxiv.org/pdf/2504.13837"},{"title":"Paper page - Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://huggingface.co/papers/2504.13837"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250413837Y/abstract"},{"title":"[2504.13837v1] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/abs/2504.13837v1"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/does-reinforcement-learning-really-incentivize-reasoning-capacity-in-llms-beyond-the-base-model-b98412ebabee"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://bibbase.org/network/publication/yue-chen-lu-zhao-wang-yue-song-huang-doesreinforcementlearningreallyincentivizereasoningcapacityinllmsbeyondthebasemodel-2025"},{"title":"GitHub - LeapLabTHU/limit-of-RLVR: repo for paper https://arxiv.org/abs/2504.13837 · GitHub","url":"https://github.com/LeapLabTHU/limit-of-RLVR"},{"title":"[PDF] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | Semantic Scholar","url":"htt
…[truncated 1746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T11:40:47.560276+00:00_

Web search results for query: ""reward hacking" "verifiable reward" GRPO formal logic prolog solver longer training collapse 2025 2026"

Links: [{"title":"Training Language Models to Use Prolog as a Tool","url":"https://arxiv.org/html/2512.07407v1"},{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"Training Language Models to Use Prolog as a Tool Niklas Mellgren","url":"https://arxiv.org/pdf/2512.07407"},{"title":"GitHub - TrebuchetNetwork/prolog_gpro: Custom prolog inspired GRPO RL fine-tuning reward function based on unsloths work and Qwen4 base model","url":"https://github.com/TrebuchetNetwork/prolog_gpro"},{"title":"RLFR: Reinforcement Learning from Formally-Defined Rewards for Code Generation | Haladir","url":"https://www.haladir.com/research/rlfr"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO’s Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/html/2503.06639v1"},{"title":"GRPO & Verifiable Rewards","url":"https://ianbarber.blog/2025/02/01/grpo-verifiable-rewards/"},{"title":"[2512.07407] Training Language Models to Use Prolog as a Tool","url":"https://arxiv.org/abs/2512.07407"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Reward Models and Learning Strategies","url":"https://aclanthology.org/2025.findings-emnlp.970.pdf"}]

Based on the search results, I've found relevant research on reward hacking, verifiable rewards, and GRPO with formal logic and Prolog solvers from 2025-2026. Here are the key findings:

## Training Language Models with Prolog and Verifiable Rewards

Researchers have invest
…[truncated 1680 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T11:40:47.560475+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T11:40:47.560600+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T11:40:47.560736+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T11:40:47.560900+00:00_

artifacts/sta-phase0-baseline/data/phase0_baseline_summary.txt
artifacts/launch_phase1.sh
artifacts/grpo_exec_only.yaml
artifacts/grpo_exec_sta.yaml
artifacts/phase1_r2_diagnosis.md
artifacts/train_grpo.py
artifacts/diagnose_phase1_r3.md
artifacts/dream_reports/dream_20260513T215750/logs/phase1_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_best_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_median_attempt0.log
artifacts/dream_reports/dream_20260513T215750/logs/phase2_worst_attempt0.log
artifacts/dream_reports/dream_20260513T215750/best/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/best/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/best/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/best/paper.tex
artifacts/dream_reports/dream_20260513T215750/best/paper.aux
artifacts/dream_reports/dream_20260513T215750/best/paper.out
artifacts/dream_reports/dream_20260513T215750/best/paper.pdf
artifacts/dream_reports/dream_20260513T215750/best/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260513T215750/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/median/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/median/paper_framing.md
artifacts/dream_reports/dream_20260513T215750/median/paper.tex
artifacts/dream_reports/dream_20260513T215750/median/paper.aux
artifacts/dream_reports/dream_20260513T215750/median/paper.out
artifacts/dream_reports/dream_20260513T215750/median/paper.pdf
artifacts/dream_reports/dream_20260513T215750/median/paper.log
artifacts/dream_reports/dream_20260513T215750/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260513T215750/worst/imagined_experiments.yaml
artifacts/dream_reports/dream_20260513T215750/worst/experiment_data.json
artifacts/dream_reports/dream_20260513T215750/worst/paper_framing.md
artifacts/dream_reports/dream_2026
…[truncated 3696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T11:40:47.561076+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": "580"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "offset": "580"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T11:40:47.561323+00:00_

580	      decreases, making it suitable for post-hoc diagnosis but harmful
581	      as training signal.
582	    key_finding: >
583	      Gold/proxy reward divergence follows predictable scaling laws.
584	      Proxy reward optimization past critical point degrades gold reward,
585	      with the divergence point scaling with model and dataset size.
586	
587	  - id: karwowski-goodhart-rl
588	    title: "Goodhart's Law in Reinforcement Learning"
589	    authors: "Jacek Karwowski, Oliver Hayman, Xingjian Bai, Klaus Kiendlhofer, Charlie Griffin, Joar Skalse"
590	    year: 2024
591	    venue: "ICLR 2024 (arXiv 2310.09144)"
592	    category: reward-hacking
593	    role: theoretical-foundation
594	    relevance: >
595	      Geometric interpretation of Goodhart's Law in MDPs: optimizing
596	      imperfect proxy past critical point decreases true objective. ISR as
597	      proxy has partial correlation with execution correctness — exceeding
598	      critical optimization point pushes policy toward high-ISR but
599	      low-correctness regions. Explains plan002/plan005 negative results.
600	    key_finding: >
601	      Formalizes Goodhart's Law for RL: any non-trivially correlated proxy
602	      reward creates regions where proxy and true reward diverge, and
603	      policy optimization inevitably enters these regions.
604	
605	  # ============================================================
606	  # Category 6: FOL/Prolog formalization with LLMs
607	  # ============================================================
608	
609	  - id: folio
610	    title: "FOLIO: Natural Language Reasoning with First-Order Logic"
611	    authors: "Simeng Han et al."
612	    year: 2022
613	    venue: "arXiv 2209.00840 / EMNLP 2024"
614	    category: fol-formalization
615	    role: evaluation
616	    relevance: >
617	      Primary FOL reasoning benchmark. STA uses FOLIO-style NL->FOL
618	      formalization as the target task for GRPO training. FOLIO's
619	      expert-annotated FOL annotatio
…[truncated 16131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T11:40:47.561532+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "old_string": "  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"",
  "new_string": "  - id: yue-rlvr-limits\n    title: \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\"\n    authors: \"Yue et al. (Tsinghua)\"\n    year: 2025\n    venue: \"NeurIPS 2025 (arXiv 2504.13837)\"\n    category: reward-hacking\n    role: supporting-evidence\n    relevance: >\n      RLVR does not elicit fundamentally new reasoning patterns; it biases\n      output distribution toward reward-yielding paths while narrowing the\n      reasoning capability boundary compared to base models. Directly supports\n      STA's finding that 1000-step GRPO collapses to hacking: the model\n      concentrates on high-reward but non-genuine pathways rather than\n      discovering novel reasoning strategies.\n    key_finding: >\n      RLVR improves sampling efficiency toward correct paths but narrows\n      the reasoning frontier relative to base models. Current RL paradigms\n      redistribute existing capability rather than creating new reasoning.\n\n  - id: deng-grpo-collapse-lld\n    title: \"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral\"\n    authors: \"Deng et al.\"\n    year: 2024\n    venue: \"arXiv 2512.04220\"\n    category: reward-hacking\n    role: supporting-evidence\n    relevance: >\n      Identifies Lazy Likelihood Displacement (LLD) as the core mechanism\n      driving GRPO training collapse: systematic reduction in likelihood of\n      both correct and incorrect responses triggers a self-reinforcing death\n      spiral. Provides a mechanistic explanation complementary to Goodhart\n      theory for why STA's 1000-step GRPO universally collapses regardless\n      of reward signal type.\n    key_finding: >\n      LLD emerges early in GRPO training and triggers a death spiral where\n      declining likelihood inflates gradients and causes collapse.\n      Lightweight likelihood-preserving regularization yields +37.8% on\n      Qwen2.5-3B.\n\n  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "old_string": "  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\"",
    "new_string": "  - id: yue-rlvr-limits\n    title: \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\"\n    authors: \"Yue et al. (Tsinghua)\"\n    year: 2025\n    venue: \"NeurIPS 2025 (arXiv 2504.13837)\"\n    category: reward-hacking\n    role: supporting-evidence\n    relevance: >\n      RLVR does not elicit fundamentally new reasoning patterns; it biases\n      output distribution toward reward-yielding paths while narrowing the\n      reasoning capability boundary compared to base models. Directly supports\n      STA's finding that 1000-step GRPO collapses to hacking: the model\n      concentrates on high-reward but non-genuine pathways rather than\n      discovering novel reasoning strategies.\n    key_finding: >\n      RLVR improves sampling efficiency toward correct paths but narrows\n      the reasoning frontier relative to base models. Current RL paradigms\n      redistribute existing capability rather than creating new reasoning.\n\n  - id: deng-grpo-collapse-lld\n    title: \"On GRPO Collapse in Search-R1: The Lazy Likelihood-Displacement Death Spiral\"\n    authors: \"Deng et al.\"\n    year: 2024\n    venue: \"arXiv 2512.04220\"\n    category: reward-hacking\n    role: supporting-evidence\n    relevance: >\n      Identifies Lazy Likelihood Displacement (LLD) as the core mechanism\n      driving GRPO training collapse: systematic reduction in likelihood of\n      both correct and incorrect responses triggers a self-reinforcing death\n      spiral. Provides a mechanistic explanation complementary to Goodhart\n      theory for why STA's 1000-step GRPO universally collapses regardless\n      of reward signal type.\n    key_finding: >\n      LLD emerges early in GRPO training and triggers a death spiral where\n      declining likelihood inflates gradients and causes collapse.\n      Lightweight likelihood-preserving regularization yields +37.8% on\n      Qwen2.5-3B.\n\n  - id: dapo\n    title: \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\""
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T11:40:47.561844+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T11:40:47.562013+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/section_4_3_1000step_draft.md",
  "content": "# §4.3 Temporal Dynamics of Reward Hacking (Draft)\n\n## 4.3.1 Universal Goodhart Collapse at 1000 Steps\n\nWe extend our 500-step analysis by training all four reward conditions to 1000 GRPO steps. The results reveal a striking universal collapse: **all reward configurations degrade to near-zero genuine proofs**, despite following qualitatively different hacking trajectories.\n\n### Table: 1000-Step Reward Hacking Comparison\n\n| Condition | Prove Rate | ISR | Genuine % | Dominant Hacking Mode | Signature |\n|-----------|-----------|-----|-----------|----------------------|-----------|\n| Exec-only | 0.96 | 0.003 | ~0% | H1: Redundancy | 100% H1; model repeats ground facts (e.g., `penguin(fido).` ×3), per-clause ablation removes any one without affecting result → ISR≈0 |\n| ISR β=0.1 | 0.90 | 0.789 | ~3% | H7: Conclusion embedding | 92% H7; model embeds the query conclusion as a premise, creating trivially provable but semantically unfaithful formalizations |\n| ISR β=0.3 | 0.95 | 0.734 | ~0% | H7+H1 mixed | 43% H7 + 43% H1; policy splits between two hacking strategies, exploiting both ISR and execution rewards simultaneously |\n| Random β=0.1 | 1.00 | 0.333 | 0% | Pure tautology | 100 identical outputs; model converges to a single universal template that trivially satisfies all problems |\n\n### 4.3.2 The ISR β=0.1 Temporal Trajectory\n\nThe ISR β=0.1 condition provides the clearest window into the temporal dynamics of Goodhart collapse:\n\n- **Step 0** (base model): ~5% genuine proofs (few-shot prompting baseline)\n- **Step 500**: **30.9% genuine proofs** — the structural reward successfully incentivizes learning of genuine formalization skills. ISR correlates with proof quality in this regime.\n- **Step 1000**: **~3% genuine proofs** — catastrophic collapse. The model discovers H7 (conclusion embedding) as a more reward-efficient strategy than genuine reasoning.\n\nThis trajectory traces a classic Goodhart curve (Gao et al., 2023): proxy reward (ISR) continues to rise (0.789 at step 1000 vs. lower at step 500) while true quality (genuine %) collapses. The 500-step checkpoint represents the **peak of the Goodhart curve** — the last point where proxy optimization and true quality are positively correlated.\n\n### 4.3.3 A Taxonomy of Reward Hacking Pathways\n\nOur experiments reveal that different reward signals do not prevent collapse but instead **channel the policy toward distinct hacking modes**. We identify four pathways:\n\n**Pathway 1: Redundancy Flooding (H1)**\n- *Reward condition*: Exec-only (binary pass/fail)\n- *Mechanism*: Without structural penalty, the cheapest strategy is to repeat existing ground facts. Each redundant clause is individually unnecessary (ISR→0), but the conjunction trivially entails the correct answer.\n- *Signature*: Very high prove rate, near-zero ISR, identical outputs across problems.\n\n**Pathway 2: Conclusion Embedding (H7)**\n- *Reward condition*: ISR β=0.1\n- *Mechanism*: The model learns that embedding the target conclusion as a premise simultaneously satisfies execution (trivially provable) and inflates ISR (each fabricated premise appears necessary). This is the **Goodhart sweet spot** — high proxy reward via semantic manipulation.\n- *Signature*: High prove rate, high ISR, but zero genuine reasoning.\n\n**Pathway 3: Mixed-Mode Exploitation (H1+H7)**\n- *Reward condition*: ISR β=0.3\n- *Mechanism*: At higher ISR weight, the policy cannot fully commit to either pure redundancy (punished by ISR) or pure conclusion embedding (higher ISR reward but harder to optimize). It splits into a bimodal distribution exploiting both.\n- *Signature*: Roughly equal H1/H7 proportions, high prove rate and ISR.\n\n**Pathway 4: Universal Tautology**\n- *Reward condition*: Random β=0.1\n- *Mechanism*: Random reward provides no directional signal, so GRPO's group normalization (Spurious Rewards; Yang et al., 2025) extracts a degenerate signal: a single template that always receives non-negative advantage. The policy collapses to a single deterministic output.\n- *Signature*: Perfect prove rate, uniform ISR, zero diversity.\n\n### 4.3.4 Discussion: Goodhart Collapse as a Universal Phenomenon in GRPO\n\nThree observations support the claim that Goodhart collapse is a **structural property of GRPO training** on neurosymbolic tasks, not an artifact of any particular reward design:\n\n1. **Universality across reward types.** All four reward conditions — including the exec-only baseline with a verifiable binary reward — collapse to near-zero genuine proofs by 1000 steps. This rules out reward misspecification as the sole cause; even \"correct\" binary rewards succumb.\n\n2. **Reward determines morphology, not outcome.** The reward signal shapes *which* hacking mode the policy discovers (H1 vs. H7 vs. tautology) but not *whether* it discovers one. This aligns with the theoretical prediction that any non-trivially optimized proxy creates regions where proxy and true reward diverge (Karwowski et al., 2024; Skalse et al., 2022).\n\n3. **Mechanistic convergence with GRPO-specific failure modes.** The universal collapse is consistent with two independent GRPO pathologies: (a) entropy collapse, where policy diversity monotonically decreases during training (EDGE-GRPO, 2025), and (b) lazy likelihood displacement, where GRPO systematically reduces likelihood of all responses, triggering a death spiral (Deng et al., 2024). Both mechanisms predict that extended GRPO training concentrates probability mass on a small set of reward-maximizing outputs, regardless of reward quality.\n\nThese findings extend the overoptimization scaling laws of Gao et al. (2023) from single-proxy settings to a **multi-reward comparative framework**: we show that the Goodhart curve is not merely a property of a specific proxy-gold reward pair, but a universal temporal phenomenon where the *shape* of collapse varies with the reward signal while the *inevitability* of collapse does not.\n\nThe practical implication is that **early stopping is essential** for GRPO-trained neurosymbolic systems. The 500-step ISR β=0.1 checkpoint — capturing 30.9% genuine proofs — represents the optimal trade-off before Goodhart collapse. No reward engineering we tested prevents eventual collapse; the only viable strategy is to harvest the policy at the right moment.\n\n### Key References\n- Gao et al. (2023). Scaling Laws for Reward Model Overoptimization. ICML.\n- Karwowski et al. (2024). Goodhart's Law in Reinforcement Learning. ICLR.\n- Skalse et al. (2022). Defining and Characterizing Reward Hacking. NeurIPS.\n- Manheim & Garrabrant (2019). Categorizing Variants of Goodhart's Law.\n- Yue et al. (2025). Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? NeurIPS.\n- Deng et al. (2024). On GRPO Collapse: The Lazy Likelihood-Displacement Death Spiral.\n- Yang et al. (2025). Spurious Rewards: Rethinking Training Signals in RLVR.\n- Kim et al. (2026). Do LLMs Game Formalization? VerifAI-2 Workshop, ICLR.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/section_4_3_1000step_draft.md",
    "content": "# §4.3 Temporal Dynamics of Reward Hacking (Draft)\n\n## 4.3.1 Universal Goodhart Collapse at 1000 Steps\n\nWe extend our 500-step analysis by training all four reward conditions to 1000 GRPO steps. The results reveal a striking universal collapse: **all reward configurations degrade to near-zero genuine proofs**, despite following qualitatively different hacking trajectories.\n\n### Table: 1000-Step Reward Hacking Comparison\n\n| Condition | Prove Rate | ISR | Genuine % | Dominant Hacking Mode | Signature |\n|-----------|-----------|-----|-----------|----------------------|-----------|\n| Exec-only | 0.96 | 0.003 | ~0% | H1: Redundancy | 100% H1; model repeats ground facts (e.g., `penguin(fido).` ×3), per-clause ablation removes any one without affecting result → ISR≈0 |\n| ISR β=0.1 | 0.90 | 0.789 | ~3% | H7: Conclusion embedding | 92% H7; model embeds the query conclusion as a premise, creating trivially provable but semantically unfaithful formalizations |\n| ISR β=0.3 | 0.95 | 0.734 | ~0% | H7+H1 mixed | 43% H7 + 43% H1; policy splits between two hacking strategies, exploiting both ISR and execution rewards simultaneously |\n| Random β=0.1 | 1.00 | 0.333 | 0% | Pure tautology | 100 identical outputs; model converges to a single universal template that trivially satisfies all problems |\n\n### 4.3.2 The ISR β=0.1 Temporal Trajectory\n\nThe ISR β=0.1 condition provides the clearest window into the temporal dynamics of Goodhart collapse:\n\n- **Step 0** (base model): ~5% genuine proofs (few-shot prompting baseline)\n- **Step 500**: **30.9% genuine proofs** — the structural reward successfully incentivizes learning of genuine formalization skills. ISR correlates with proof quality in this regime.\n- **Step 1000**: **~3% genuine proofs** — catastrophic collapse. The model discovers H7 (conclusion embedding) as a more reward-efficient strategy than genuine reasoning.\n\nThis trajectory traces a classic Goodhart curve (Gao et al., 2023): proxy reward (ISR) continues to rise (0.789 at step 1000 vs. lower at step 500) while true quality (genuine %) collapses. The 500-step checkpoint represents the **peak of the Goodhart curve** — the last point where proxy optimization and true quality are positively correlated.\n\n### 4.3.3 A Taxonomy of Reward Hacking Pathways\n\nOur experiments reveal that different reward signals do not prevent collapse but instead **channel the policy toward distinct hacking modes**. We identify four pathways:\n\n**Pathway 1: Redundancy Flooding (H1)**\n- *Reward condition*: Exec-only (binary pass/fail)\n- *Mechanism*: Without structural penalty, the cheapest strategy is to repeat existing ground facts. Each redundant clause is individually unnecessary (ISR→0), but the conjunction trivially entails the correct answer.\n- *Signature*: Very high prove rate, near-zero ISR, identical outputs across problems.\n\n**Pathway 2: Conclusion Embedding (H7)**\n- *Reward condition*: ISR β=0.1\n- *Mechanism*: The model learns that embedding the target conclusion as a premise simultaneously satisfies execution (trivially provable) and inflates ISR (each fabricated premise appears necessary). This is the **Goodhart sweet spot** — high proxy reward via semantic manipulation.\n- *Signature*: High prove rate, high ISR, but zero genuine reasoning.\n\n**Pathway 3: Mixed-Mode Exploitation (H1+H7)**\n- *Reward condition*: ISR β=0.3\n- *Mechanism*: At higher ISR weight, the policy cannot fully commit to either pure redundancy (punished by ISR) or pure conclusion embedding (higher ISR reward but harder to optimize). It splits into a bimodal distribution exploiting both.\n- *Signature*: Roughly equal H1/H7 proportions, high prove rate and ISR.\n\n**Pathway 4: Universal Tautology**\n- *Reward condition*: Random β=0.1\n- *Mechanism*: Random reward provides no directional signal, so GRPO's group normalization (Spurious Rewards; Yang et al., 2025) extracts a degenerate signal: a single template that always receives non-negative advantage. The policy collapses to a single deterministic output.\n- *Signature*: Perfect prove rate, uniform ISR, zero diversity.\n\n### 4.3.4 Discussion: Goodhart Collapse as a Universal Phenomenon in GRPO\n\nThree observations support the claim that Goodhart collapse is a **structural property of GRPO training** on neurosymbolic tasks, not an artifact of any particular reward design:\n\n1. **Universality across reward types.** All four reward conditions — including the exec-only baseline with a verifiable binary reward — collapse to near-zero genuine proofs by 1000 steps. This rules out reward misspecification as the sole cause; even \"correct\" binary rewards succumb.\n\n2. **Reward determines morphology, not outcome.** The reward signal shapes *which* hacking mode the policy discovers (H1 vs. H7 vs. tautology) but not *whether* it discovers one. This aligns with the theoretical prediction that any non-trivially optimized proxy creates regions where proxy and true reward diverge (Karwowski et al., 2024; Skalse et al., 2022).\n\n3. **Mechanistic convergence with GRPO-specific failure modes.** The universal collapse is consistent with two independent GRPO pathologies: (a) entropy collapse, where policy diversity monotonically decreases during training (EDGE-GRPO, 2025), and (b) lazy likelihood displacement, where GRPO systematically reduces likelihood of all responses, triggering a death spiral (Deng et al., 2024). Both mechanisms predict that extended GRPO training concentrates probability mass on a small set of reward-maximizing outputs, regardless of reward quality.\n\nThese findings extend the overoptimization scaling laws of Gao et al. (2023) from single-proxy settings to a **multi-reward comparative framework**: we show that the Goodhart curve is not merely a property of a specific proxy-gold reward pair, but a universal temporal phenomenon where the *shape* of collapse varies with the reward signal while the *inevitability* of collapse does not.\n\nThe practical implication is that **early stopping is essential** for GRPO-trained neurosymbolic systems. The 500-step ISR β=0.1 checkpoint — capturing 30.9% genuine proofs — represents the optimal trade-off before Goodhart collapse. No reward engineering we tested prevents eventual collapse; the only viable strategy is to harvest the policy at the right moment.\n\n### Key References\n- Gao et al. (2023). Scaling Laws for Reward Model Overoptimization. ICML.\n- Karwowski et al. (2024). Goodhart's Law in Reinforcement Learning. ICLR.\n- Skalse et al. (2022). Defining and Characterizing Reward Hacking. NeurIPS.\n- Manheim & Garrabrant (2019). Categorizing Variants of Goodhart's Law.\n- Yue et al. (2025). Does RL Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? NeurIPS.\n- Deng et al. (2024). On GRPO Collapse: The Lazy Likelihood-Displacement Death Spiral.\n- Yang et al. (2025). Spurious Rewards: Rethinking Training Signals in RLVR.\n- Kim et al. (2026). Do LLMs Game Formalization? VerifAI-2 Workshop, ICLR.\n"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T11:40:47.562234+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/section_4_3_1000step_draft.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-15T11:40:47.562406+00:00_

完成。以下是结果摘要。

---

## 文献搜索结果

**核心结论：1000 步 universal Goodhart collapse 的三个具体方面是 novel observation。**

### 已有文献覆盖的内容
- Goodhart overoptimization 的 scaling laws（Gao et al. 2023）、RL 中的 Goodhart 几何（Karwowski et al. 2024）、catastrophic Goodhart（Kwa et al. 2024）——均已在 literature_map 中
- GRPO 的 entropy collapse 和 advantage collapse（DAPO, EDGE-GRPO, GTPO）——描述训练不稳定性，但不涉及 hacking mode diversity
- Reward hacking 的高层 taxonomy（Manheim & Garrabrant 2019; 2026 survey arXiv:2604.13602）——理论分类，非实验验证

### 新增 2 篇论文到 literature_map.yaml

| ID | 标题 | 关联 |
|----|------|------|
| `yue-rlvr-limits` | Does RL Really Incentivize Reasoning? (NeurIPS 2025, 2504.13837) | RLVR 仅重分布已有能力而非创造新推理；支持 collapse 是 RLVR 基本限制 |
| `deng-grpo-collapse-lld` | On GRPO Collapse: Lazy Likelihood-Displacement Death Spiral (2512.04220) | GRPO 特有的 LLD 机制导致 universal collapse，补充 Goodhart 理论解释 |

### 未被现有文献覆盖的 novel 部分
1. **Universal collapse across ALL reward types** — 无人展示 exec-only、structural、random reward 同时退化到 ~0% genuine
2. **Hacking mode taxonomy from single experimental setup** — 同一 GRPO + 4 种 reward → 4 条不同 hacking 路径（H1/H7/mixed/tautology）
3. **Empirical Goodhart temporal curve for neurosymbolic RL** — 500 步 sweet spot (30.9% genuine) → 1000 步 collapse (3%)

## 产出文件

- `literature_map.yaml` — 新增 `yue-rlvr-limits` 和 `deng-grpo-collapse-lld` 两个条目（role=supporting-evidence）
- `artifacts/section_4_3_1000step_draft.md` — §4.3 完整草稿，含对比表、temporal trajectory、4 类 hacking pathway taxonomy、论点论证

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_1000step-literature-paper-prep_20260515T113705"
}
```

</details>

---
