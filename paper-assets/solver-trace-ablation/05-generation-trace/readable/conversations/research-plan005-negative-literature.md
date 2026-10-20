# research plan005 negative literature

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_research_plan005-negative-literature_20260514T020402.jsonl`
- **Structured JSON:** [`5c4bd4ccd012a6fe48a8.json`](../../sessions/5c/5c4bd4ccd012a6fe48a8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-14T02:09:20.210125+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T02:09:20.210610+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T02:09:20.210951+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T02:09:20.211477+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO el
…[truncated 11174 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T02:09:20.211769+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "auxiliary reward degradation multi-objective reinforcement learning performance tradeoff 2023 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "auxiliary reward degradation multi-objective reinforcement learning performance tradeoff 2023 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T02:09:20.211994+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "reward shaping negative side effects reinforcement learning penalty auxiliary objective"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "reward shaping negative side effects reinforcement learning penalty auxiliary objective"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T02:09:20.212207+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "process reward vs outcome reward conflict LLM GRPO training 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "process reward vs outcome reward conflict LLM GRPO training 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T02:09:20.212438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "structural reward degradation reinforcement learning auxiliary task interference 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "structural reward degradation reinforcement learning auxiliary task interference 2023 2024"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T02:09:20.212656+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"multi-objective RLHF\" \"reward conflict\" OR \"auxiliary reward\" OR \"reward tradeoff\" language model 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"multi-objective RLHF\" \"reward conflict\" OR \"auxiliary reward\" OR \"reward tradeoff\" language model 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T02:09:20.212961+00:00_

Web search results for query: "auxiliary reward degradation multi-objective reinforcement learning performance tradeoff 2023 2024 2025"

Links: [{"title":"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting","url":"https://arxiv.org/html/2509.11452v1"},{"title":"Reinforcement Learning Journal 2025 Cover Page","url":"https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"},{"title":"Published as a conference paper at RLC 2024","url":"https://openreview.net/pdf?id=qMlueQODdv"},{"title":"Multi-objective reward generalization: improving performance of Deep Reinforcement Learning for applications in single-asset trading - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10770001/"},{"title":"EMORL: Ensemble Multi-Objective Reinforcement ...","url":"https://aclanthology.org/2025.sigdial-1.33.pdf"},{"title":"GitHub - blacksnail789521/Agentic-RL-Training-Recipes: Training Recipes for Agentic Reinforcement Learning in LLMs: A Survey · GitHub","url":"https://github.com/blacksnail789521/Agentic-RL-Training-Recipes"},{"title":"Multi-objective optimization for dynamic logistics scheduling based on hierarchical deep reinforcement learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-18309-y"},{"title":"Multi-Task Reward Learning from Human Ratings","url":"https://arxiv.org/html/2506.09183v1"},{"title":"Asynchronous Agentic Reinforcement Learning: A Tradeoff of Systems","url":"https://people.eecs.berkeley.edu/~kubitron/courses/cs262a-F25/projects/reports/project1008_paper_ver2_72488057446561351955.pdf"},{"title":"Learning Fair Pareto-Optimal Policies in Multi-Objective ...","url":"https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_350.pdf"}]

I've performed the web search for your query on auxiliary reward degradation and multi-objective reinforcement learning performance tradeoffs from 2023-2025. Here are the key findings:

## Recent Research on Multi-Objective RL and Performance Tradeoffs

### LLM Alignment and Dynamic Rew
…[truncated 1639 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T02:09:20.213285+00:00_

Web search results for query: "process reward vs outcome reward conflict LLM GRPO training 2024 2025"

Links: [{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=4DJoBOQNd0"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL","url":"https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf"},{"title":"Paper page - Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://huggingface.co/papers/2509.03403"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"},{"title":"Let’s Verify Step by Step, ORM vs PRM | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/lets-verify-step-by-step-orm-vs-prm-613ecffb59ab"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"}]

Based on the search results, here's what I found about process reward vs outcome reward conflict in LLM GRPO training:

## Key Findings

### The Core Conflict

Since verifiers can only verify outcome results, rewards are 
…[truncated 1588 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T02:09:20.213607+00:00_

Web search results for query: "structural reward degradation reinforcement learning auxiliary task interference 2023 2024"

Links: [{"title":"Structure in Deep Reinforcement Learning: A Survey and ...","url":"https://www.jair.org/index.php/jair/article/download/15703/27028/38774"},{"title":"(PDF) Overcoming Reward Model Noise in Instruction-Guided Reinforcement Learning","url":"https://www.researchgate.net/publication/384295139_Overcoming_Reward_Model_Noise_in_Instruction-Guided_Reinforcement_Learning"},{"title":"Journal of Artificial Intelligence Research 79 (2024) 1167-1236","url":"https://arxiv.org/pdf/2306.16021"},{"title":"Reinforcement Learning for Finite Space Mean-Field Type ...","url":"https://rlj.cs.umass.edu/2025/RLJ_2025_CoverPages.pdf"},{"title":"Reward Models in Deep Reinforcement Learning: A Survey","url":"https://arxiv.org/html/2506.15421v1"},{"title":"Published as a conference paper at RLC 2024","url":"https://openreview.net/pdf?id=qMlueQODdv"},{"title":"Reward Models in Deep Reinforcement Learning: A Survey","url":"https://www.ijcai.org/proceedings/2025/1199.pdf"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Alternating Reinforcement Learning and Supervised Fine- ...","url":"https://aclanthology.org/2024.emnlp-main.252.pdf"}]

I found several research papers related to reinforcement learning, reward design, and auxiliary tasks from 2023-2024. Here are the key findings:

## Key Research Areas

**Auxiliary Tasks and Reward Structures:**
Auxiliary losses help with generalization and serve as entry points for human-like inductive biases, with metrics inspired by the geometry of latent decompositions helping to learn optimal values in multi-task settings.

**Reward Model Degradation:**
Research reveals a critica
…[truncated 1175 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T02:09:20.213944+00:00_

Web search results for query: "reward shaping negative side effects reinforcement learning penalty auxiliary objective"

Links: [{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Reward shaping — Mastering Reinforcement Learning","url":"https://gibberblot.github.io/rl-notes/single-agent/reward-shaping.html"},{"title":"Reward Function in Reinforcement Learning | by Amit Yadav | Biased-Algorithms | Medium","url":"https://medium.com/biased-algorithms/reward-function-in-reinforcement-learning-c9ee04cabe7d"},{"title":"Penalty-Based Reward Shaping in RL","url":"https://www.emergentmind.com/topics/penalty-based-reward-shaping"},{"title":"Reward Shaping for Faster Learning in Reinforcement ...","url":"https://codesignal.com/learn/courses/advanced-rl-techniques-optimization-and-beyond/lessons/reward-shaping-for-faster-learning-in-reinforcement-learning"},{"title":"AI Safety 101 : Reward Misspecification","url":"https://www.lesswrong.com/posts/mMBoPnFrFqQJKzDsZ/ai-safety-101-reward-misspecification"},{"title":"What is reward shaping in reinforcement learning?","url":"https://milvus.io/ai-quick-reference/what-is-reward-shaping-in-reinforcement-learning"},{"title":"Behavior Alignment via Reward Function Optimization Dhawal Gupta∗","url":"https://people.cs.umass.edu/~pthomas/papers/Gupta2023.pdf"},{"title":"Real-World DRL: 5 Essential Reward Functions for Modeling Objectives and Constraints | by Zhong Hong | Medium","url":"https://medium.com/@zhonghong9998/real-world-drl-5-essential-reward-functions-for-modeling-objectives-and-constraints-e742325d4747"},{"title":"Reinforcement Learning Reward And Punishment | Restackio","url":"https://www.restack.io/p/reinforcement-learning-answer-reward-punishment-cat-ai"}]

Based on the search results, here's an overview of reward shaping, negative side effects, penalty-based approaches, and auxiliary objectives in reinforc
…[truncated 2392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T02:09:20.214260+00:00_

Web search results for query: ""multi-objective RLHF" "reward conflict" OR "auxiliary reward" OR "reward tradeoff" language model 2024 2025"

Links: [{"title":"Confronting Reward Model Overoptimization with Constrained RLHF | OpenReview","url":"https://openreview.net/forum?id=gkfUvn0fLU"},{"title":"Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts | RLHFlow","url":"https://rlhflow.github.io/posts/2024-05-29-multi-objective-reward-modeling/"},{"title":"GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub","url":"https://github.com/RLHFlow/RLHF-Reward-Modeling"},{"title":"Interpretable Preferences via Multi-Objective Reward ...","url":"https://aclanthology.org/2024.findings-emnlp.620.pdf"},{"title":"[2310.04373] Confronting Reward Model Overoptimization with Constrained RLHF","url":"https://arxiv.org/abs/2310.04373"},{"title":"Optimizing Language Models with Fair and Stable Reward ...","url":"https://aclanthology.org/2024.emnlp-main.565.pdf"},{"title":"Reward Model Overoptimisation in Iterated RLHF | OpenReview","url":"https://openreview.net/forum?id=efoe5VJfKz"},{"title":"Towards Reward Fairness in RLHF: From a Resource ...","url":"https://aclanthology.org/2025.acl-long.163.pdf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"}]

Based on my search results, I've found several relevant papers and resources on multi-objective RLHF addressing reward conflict and tradeoffs in language model alignment. Here's what I discovered:

## Key Research Areas

**Multi-Objective Reward Modeling:**

The RLHF process typically starts by training a reward model using human preference data, with conventional RMs trained on pairwise responses to the same user request. However, human preferences are multi-faceted, a
…[truncated 1676 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T02:09:20.214570+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.03403",
  "prompt": "Extract: title, all authors, year, venue/conference, abstract. Focus on whether they report that process rewards can hurt outcome performance, and what solutions they propose."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.03403",
    "prompt": "Extract: title, all authors, year, venue/conference, abstract. Focus on whether they report that process rewards can hurt outcome performance, and what solutions they propose."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T02:09:20.214826+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2310.04373",
  "prompt": "Extract: title, all authors, year, venue/conference, abstract. Focus on findings about composite reward model overoptimization - does adding auxiliary/component rewards degrade primary performance? What solutions do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2310.04373",
    "prompt": "Extract: title, all authors, year, venue/conference, abstract. Focus on findings about composite reward model overoptimization - does adding auxiliary/component rewards degrade primary performance? What solutions do they propose?"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T02:09:20.215045+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf",
  "prompt": "Extract: title, all authors, year, venue. What is the main finding about GRPO and process reward models? Does this paper discuss any conflict or tradeoff between process and outcome rewards?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://openreview.net/pdf/1f109913a199dad205fa51f554aaa5e2a5a782d5.pdf",
    "prompt": "Extract: title, all authors, year, venue. What is the main finding about GRPO and process reward models? Does this paper discuss any conflict or tradeoff between process and outcome rewards?"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T02:09:20.215275+00:00_

# Research Paper Summary

**Title:** Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training

**Authors:** Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal

**Year:** 2025

**Venue:** arXiv (Computer Science > Machine Learning)

## Key Findings on Process Rewards

The paper identifies a critical tension: while Process Reward Models (PRMs) provide "fine-grained guidance for intermediate steps, they frequently suffer from inaccuracies and are susceptible to reward hacking." Meanwhile, Outcome Reward Models (ORMs) lack sufficient granularity to evaluate reasoning quality accurately.

## Proposed Solution

Rather than directly combining PRM and ORM signals, the authors introduce **PROF (PRocess cOnsistency Filter)**, a data curation method that selectively uses process rewards. The approach "retains correct responses with higher averaged process values and incorrect responses with lower averaged process values, while maintaining positive/negative training sample balance."

**Results:** This filtering strategy achieved "over 4% improvement in final accuracy compared to the blending approaches" while also enhancing intermediate reasoning quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T02:09:20.215506+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"auxiliary loss\" OR \"auxiliary reward\" \"hurts\" OR \"degrades\" OR \"reduces\" primary task performance reinforcement learning LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"auxiliary loss\" OR \"auxiliary reward\" \"hurts\" OR \"degrades\" OR \"reduces\" primary task performance reinforcement learning LLM 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T02:09:20.215743+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mudgal Agarwal \"reward bonus\" OR \"bonus reward\" degradation RLHF primary objective 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mudgal Agarwal \"reward bonus\" OR \"bonus reward\" degradation RLHF primary objective 2024"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T02:09:20.215981+00:00_

# Research Summary: Reward Model Overoptimization

**Title:** Confronting Reward Model Overoptimization with Constrained RLHF

**Authors:** Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer

**Year:** 2023

**Venue:** arXiv (cs.LG/cs.AI)

## Key Findings on Composite Reward Models

The paper conducts "the first study on overoptimization in composite RMs" and demonstrates that correlation between component reward models significantly influences where performance degradation occurs.

**Main Problem:** When combining multiple reward models representing different quality aspects, the system becomes vulnerable to overoptimization—where "accumulating higher reward is associated with worse human ratings" beyond certain thresholds.

## Proposed Solutions

1. **Constrained Reinforcement Learning:** The authors apply constrained RL to prevent agents from exceeding each component model's "threshold of usefulness," keeping all models within effective operating ranges.

2. **Dynamic Weighting via Lagrange Multipliers:** Rather than static weighting, their approach learns dynamic weights naturally expressed through Lagrange multipliers, addressing the compositional weighting challenge.

3. **Adaptive Gradient-Free Optimization:** An additional method identifies optimal performance points during training using gradient-free techniques, enabling single-run identification and optimization.

The research suggests these constraints improve evaluation performance by maintaining component models within their reliable ranges.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T02:09:20.216243+00:00_

I appreciate your request, but I need to inform you that the content provided appears to be a raw PDF file with compressed/encoded streams rather than readable text. The document contains binary PDF objects (streams with /FlateDecode filters) that cannot be meaningfully extracted without proper PDF parsing.

From the visible metadata in the PDF structure, I can see this is a multi-page document with annotations and embedded fonts, but I cannot reliably extract:
- The title
- Author names
- Publication year
- Venue information
- Content about GRPO and process reward models
- Information about conflicts between process and outcome rewards

**To help you effectively, I would need:**
1. The actual text content of the paper (not the raw PDF binary)
2. A properly formatted text version
3. Or access to the paper through a PDF viewer that can extract text

If you can provide the paper's text content or a clearer version, I'll be happy to extract the specific information you're requesting while following your guidelines about quote length and attribution.

[Binary content (application/pdf, 890.6KB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/6c8ab3fa-f3c3-483d-b115-dccc1097e77a/tool-results/webfetch-1778724288088-yoo47l.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T02:09:20.216531+00:00_

Web search results for query: "Mudgal Agarwal "reward bonus" OR "bonus reward" degradation RLHF primary objective 2024"

Links: [{"title":"Interpretable Preferences via Multi-Objective Reward ...","url":"https://aclanthology.org/2024.findings-emnlp.620.pdf"},{"title":"Over-Optimization | RLHF Book by Nathan Lambert","url":"https://rlhfbook.com/c/14-over-optimization"},{"title":"Investigating Reward Hacking When Using Vision-Language ...","url":"https://cs224r.stanford.edu/projects/pdfs/CS_224R_Final_Project.pdf"},{"title":"Reward Over-Optimization in AI","url":"https://www.emergentmind.com/topics/reward-over-optimization"},{"title":"Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/e45caa3d5273d105b8d045e748636957-Paper-Conference.pdf"},{"title":"Adaptive Length Bias Mitigation in Reward Models for RLHF","url":"https://aclanthology.org/2025.findings-naacl.169.pdf"},{"title":"GitHub - RLHFlow/RLHF-Reward-Modeling: Recipes to train reward model for RLHF. · GitHub","url":"https://github.com/RLHFlow/RLHF-Reward-Modeling"},{"title":"Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts | RLHFlow","url":"https://rlhflow.github.io/posts/2024-05-29-multi-objective-reward-modeling/"},{"title":"Enhancing RLHF with Weighted Preference Optimization","url":"https://aclanthology.org/2024.emnlp-main.475.pdf"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"}]

Based on my search results, I wasn't able to find a research paper or work specifically by "Mudgal Agarwal" with the exact terms "reward bonus" OR "bonus reward" and "degradation RLHF primary objective" from 2024.

The search returned relevant papers about RLHF (Reinforcement Learning from Human Feedback), reward model degradation, and related topics from 2024, but none appear to be authored by someone with the name Mud
…[truncated 702 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T02:09:20.216951+00:00_

Web search results for query: ""auxiliary loss" OR "auxiliary reward" "hurts" OR "degrades" OR "reduces" primary task performance reinforcement learning LLM 2024 2025"

Links: [{"title":"On Auxiliary Tasks in Deep Reinforcement Learning | Yunfan’s Blog","url":"https://yunfanj.com/blog/2021/03/14/AuxTasks.html"},{"title":"Learning through Auxiliary Tasks | Unsupervised Thoughts","url":"https://vivien000.github.io/blog/journal/learning-though-auxiliary_tasks.html"},{"title":"What is Auxiliary Tasks? | Activeloop Glossary","url":"https://www.activeloop.ai/resources/glossary/auxiliary-tasks/"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"A framework for mitigating malicious RLHF feedback in LLM training using consensus based reward | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-92889-7"},{"title":"LLM Reinforcement Learning | IBM","url":"https://www.ibm.com/think/topics/llm-reinforcement-learning"},{"title":"Tutorial #4: auxiliary tasks in deep reinforcement learning - Research Blog | RBC Borealis","url":"https://rbcborealis.com/research-blogs/tutorial-4-auxiliary-tasks-deep-reinforcement-learning/"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Pushing RL Boundaries: Integrating Foundational Models, e.g. LLMs and VLMs, into Reinforcement Learning | by Elahe Aghapour | TDS Archive | Medium","url":"https://medium.com/data-science/pushing-boundaries-integrating-foundational-models-e-g-556cfb6d0632"},{"title":"Efficient Reinforcement Learning with Large Language Model Priors","url":"https://arxiv.org/html/2410.07927v1"}]

I found some relevant results, but let me search more specifically for recent research on negative effects of auxiliary losses/rewards on LLMs and reinforcement learning in 2024
…[truncated 7457 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T02:09:20.217296+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.06337",
  "prompt": "Extract: title, all authors, year, venue. What is the main finding about gradient conflicts in GRPO? Does adding auxiliary objectives or rewards hurt the primary reasoning performance? What solutions do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2512.06337",
    "prompt": "Extract: title, all authors, year, venue. What is the main finding about gradient conflicts in GRPO? Does adding auxiliary objectives or rewards hurt the primary reasoning performance? What solutions do they propose?"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T02:09:20.217527+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf",
  "prompt": "Extract: title, all authors, year, venue. What is the main finding about negative transfer in auxiliary-task learning? How does adding auxiliary tasks degrade primary task performance, and what solution do they propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf",
    "prompt": "Extract: title, all authors, year, venue. What is the main finding about negative transfer in auxiliary-task learning? How does adding auxiliary tasks degrade primary task performance, and what solution do they propose?"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T02:09:20.217786+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"process reward\" \"outcome reward\" conflict degradation LLM reasoning GRPO RL training 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"process reward\" \"outcome reward\" conflict degradation LLM reasoning GRPO RL training 2024 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T02:09:20.218012+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Skalse reward hacking taxonomy auxiliary objective side effects reinforcement learning 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Skalse reward hacking taxonomy auxiliary objective side effects reinforcement learning 2022 2023"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T02:09:20.218237+00:00_

# DaGRPO Paper Summary

**Title:** DaGRPO: Rectifying Gradient Conflict in Reasoning via Distinctiveness-Aware Group Relative Policy Optimization

**Authors:** Xuan Xie, Xuan Wang, Wenjie Wang, Shuai Chen, Wei Lin

**Year:** 2025

**Venue:** arXiv (cs.AI)

## Main Finding on Gradient Conflicts

The researchers theoretically identified that "homogeneous samples induce destructive gradient conflicts" in standard GRPO, particularly affecting routine queries. Additionally, hard queries suffer from "the scarcity of valid positive samples," leading to ineffective optimization.

## Impact of Auxiliary Objectives

The document does not discuss whether auxiliary objectives or rewards harm primary reasoning performance. It focuses exclusively on problems within the GRPO framework itself rather than examining multi-objective trade-offs.

## Proposed Solutions

DaGRPO introduces two mechanisms:

1. **Sequence-level Gradient Rectification:** This approach "dynamically mask[s] sample pairs with low distinctiveness," directly eliminating gradient conflicts at their source.

2. **Off-policy Data Augmentation:** This mechanism "introduces high-quality anchors to recover training signals for challenging tasks," addressing the shortage of effective samples for difficult problems.

The method achieved "+4.7% average accuracy gain on math benchmarks" and demonstrated mitigation of gradient explosion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T02:09:20.218474+00:00_

I appreciate your request, but I'm unable to extract the information you're looking for from the provided content. The text appears to be a PDF file in binary/encoded format rather than readable plain text about a research paper on auxiliary-task learning and negative transfer.

To help you effectively, I would need:
- The paper's title, authors, year, and venue in readable format
- Clear text describing their findings on negative transfer
- Details about their proposed solution

If you could provide the paper as readable text (copy-pasted from a PDF viewer or the paper's abstract/introduction), I'd be happy to extract and summarize:
- Complete citation information
- The main findings regarding how auxiliary tasks can degrade primary task performance
- Their proposed mitigation approach

Alternatively, if you have a link to the paper or can share its title and authors, I can help you locate and analyze the key findings.

[Binary content (application/pdf, 2.1MB) also saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/6c8ab3fa-f3c3-483d-b115-dccc1097e77a/tool-results/webfetch-1778724326805-nekjrt.pdf]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T02:09:20.218766+00:00_

Web search results for query: "Skalse reward hacking taxonomy auxiliary objective side effects reinforcement learning 2022 2023"

Links: [{"title":"Defining and Characterizing Reward Hacking Joar Skalse∗ University of Oxford","url":"https://arxiv.org/pdf/2209.13085"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"[PDF] Defining and Characterizing Reward Hacking | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Defining-and-Characterizing-Reward-Hacking-Skalse-Howe/004357dd9bbf3012c8fe0ccada4da401bf85dfff"},{"title":"[2209.13085] Defining and Characterizing Reward Hacking","url":"https://arxiv.org/abs/2209.13085"},{"title":"Reward Hacking in RLVR","url":"https://www.emergentmind.com/topics/reward-hacking-in-rlvr"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement","url":"https://arxiv.org/pdf/2507.05619"},{"title":"A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future","url":"https://arxiv.org/html/2504.12328v1"},{"title":"Scaling Laws for Reward Model Overoptimization","url":"https://proceedings.mlr.press/v202/gao23h/gao23h.pdf"},{"title":"correlated proxies:anew definition and improved mitigation ...","url":"https://arxiv.org/pdf/2403.03185"}]

I found several highly relevant sources about reward hacking, Skalse's work, and related taxonomies. Here's what the search revealed:

## Key Findings

Skalse et al. (2022) provided the first formal definition of reward hacking, a phenomenon where optimizing an imperfect proxy reward function leads to poor performance according to the true reward function. They define a proxy as unhackable if increasing the expected proxy return can never decrease the expected true return.

A key insight from their work is
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T02:09:20.219088+00:00_

Web search results for query: ""process reward" "outcome reward" conflict degradation LLM reasoning GRPO RL training 2024 2025 2026"

Links: [{"title":"Navigate the Unknown: Enhancing LLM Reasoning with Intrinsic Motivation Guided Exploration","url":"https://arxiv.org/html/2505.17621v1"},{"title":"LLM Reasoning with Process Rewards for Outcome-Guided Steps","url":"https://arxiv.org/html/2604.02341v1"},{"title":"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training","url":"https://arxiv.org/html/2509.03403v1"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"Outcome-based Exploration for LLM Reasoning","url":"https://arxiv.org/pdf/2509.06941"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"RM-R1: Reward Modeling as Reasoning","url":"https://arxiv.org/pdf/2505.02387"},{"title":"PRL: Process Reward Learning Improves LLMs’ Reasoning Ability and Broadens the Reasoning Boundary","url":"https://arxiv.org/html/2601.10201v1"},{"title":"On Designing Effective RL Reward at Training Time for LLM Reasoning","url":"https://arxiv.org/html/2410.15115v1"},{"title":"GitHub - bobxwu/learning-from-rewards-llm-papers: A comrephensive collection of learning from rewards in the post-training and test-time scaling of LLMs, with a focus on both reward models and learning strategies across training, inference, and post-inference stages. · GitHub","url":"https://github.com/bobxwu/learning-from-rewards-llm-papers"}]

Based on the search results, I found several highly relevant papers and discussions about process reward and outcome reward conflicts in LLM reasoning with GRPO RL training. Here are the key findings:

## Process Reward vs. Outcome Reward Conflicts

Directly combining exploration rewards with outcome-based rewards creates co
…[truncated 1918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T02:09:20.219400+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.15115",
  "prompt": "Extract: title, all authors, year, venue. Main findings about how reward design at training time affects LLM reasoning. Do they report cases where adding structured/process rewards hurts outcome performance? What solutions?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2410.15115",
    "prompt": "Extract: title, all authors, year, venue. Main findings about how reward design at training time affects LLM reasoning. Do they report cases where adding structured/process rewards hurts outcome performance? What solutions?"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T02:09:20.219630+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.02341",
  "prompt": "Extract: title, all authors, year, venue. Main finding about PROGRS - outcome-conditioned process rewards. Do they report that naive process rewards hurt outcome accuracy? What is \"outcome-conditioned centering\"?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2604.02341",
    "prompt": "Extract: title, all authors, year, venue. Main finding about PROGRS - outcome-conditioned process rewards. Do they report that naive process rewards hurt outcome accuracy? What is \"outcome-conditioned centering\"?"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T02:09:20.219875+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2209.13085",
  "prompt": "Extract: title, all authors, year, venue. What is the formal definition of reward hacking? Key theorem: can optimizing a proxy reward decrease true reward? What does the \"unhackability\" condition say about auxiliary reward objectives?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2209.13085",
    "prompt": "Extract: title, all authors, year, venue. What is the formal definition of reward hacking? Key theorem: can optimizing a proxy reward decrease true reward? What does the \"unhackability\" condition say about auxiliary reward objectives?"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T02:09:20.220093+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ForkMerge \"negative transfer\" auxiliary task learning NeurIPS 2023 Zheng Ge Long"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ForkMerge \"negative transfer\" auxiliary task learning NeurIPS 2023 Zheng Ge Long"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T02:09:20.220317+00:00_

# Paper Summary

**Title:** On Designing Effective RL Reward at Training Time for LLM Reasoning

**Authors:** Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu

**Year:** 2024

**Venue:** arXiv (cs.LG - Computer Science/Machine Learning)

## Main Findings

The researchers discovered a counterintuitive problem: despite strong inference-time performance, reward models can actually degrade RL training outcomes. They found that "an LLM can receive high rewards from some of these reward models by repeating correct but unnecessary reasoning steps, leading to a severe reward hacking issue."

Specifically, they evaluated Outcome-supervised Reward Models (ORM) and Process-supervised Reward Models (PRM), finding that these learned rewards "may NOT help or even hurt RL training, producing worse performances than LLMs trained with the success reward only."

## Solutions Proposed

The team introduced two reward refinement techniques:

1. **Clipping** - Constrains accumulated reward magnitude
2. **Delta** - Restricts reward growth across trajectories

Both techniques ensure that "the accumulative reward of any reasoning trajectory is upper-bounded to keep a learned reward model effective without being exploited."

These refinements enabled improvements across 1.5B and 7B parameter models on MATH and GSM8K benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T02:09:20.220553+00:00_

# Paper Analysis

**Title:** LLM Reasoning with Process Rewards for Outcome-Guided Steps

**Authors:** Mohammad Rezaei, Jens Lehmann, Sahar Vahdati

**Year:** 2026

**Venue:** Submitted to IJCNN 2026 conference

## Main Findings

**PROGRS Framework:**
The paper introduces PROGRS, which treats process rewards as relative preferences within outcome groups rather than absolute targets, keeping outcome correctness dominant.

**Naive Process Rewards as Harmful:**
Yes, the authors document this problem: "PRM scores are often imperfectly aligned with final correctness and can reward locally fluent reasoning that still ends in an incorrect answer. When optimized as absolute rewards, such signals can amplify fluent failure modes and induce reward hacking."

**Outcome-Conditioned Centering:**
This technique "shifts PRM scores of incorrect trajectories to have zero mean within each prompt group. It removes systematic bias while preserving informative rankings." This prevents misaligned process rewards from corrupting the training signal while maintaining their guidance value on intermediate steps.

The approach demonstrates consistent improvements across multiple mathematical reasoning benchmarks with fewer rollouts needed compared to outcome-only baselines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T02:09:20.220824+00:00_

# Paper Summary

**Title:** Defining and Characterizing Reward Hacking

**Authors:** Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger

**Year:** 2022 (submitted); revised 2025

**Venue:** arXiv (cs.LG - Computer Science, Machine Learning)

## Formal Definition of Reward Hacking

The paper defines reward hacking as "optimizing an imperfect proxy reward function leads to poor performance according to the true reward function." A proxy is considered "unhackable" when "increasing the expected proxy return can never decrease the expected true return."

## Key Theorem on Proxy Optimization

The central finding demonstrates a strong constraint: **for the full set of stochastic policies, two reward functions can only be unhackable if one remains constant.** This reveals that yes, optimizing a proxy reward can decrease true reward performance under most realistic conditions.

## Unhackability and Auxiliary Objectives

The unhackability condition indicates a fundamental tension in AI alignment. While narrower reward functions or simplified distinctions might intuitively seem safer, the paper shows this approach "is usually not the case." The research uncovers "a tension between using reward functions to specify narrow tasks and aligning AI systems with human values," suggesting that auxiliary objectives cannot easily solve reward specification problems through simplification alone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T02:09:20.221110+00:00_

Web search results for query: "ForkMerge "negative transfer" auxiliary task learning NeurIPS 2023 Zheng Ge Long"

Links: [{"title":"NeurIPS Poster ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://neurips.cc/virtual/2023/poster/70098"},{"title":"GitHub - thuml/ForkMerge: Code release of paper \"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning\" (NeurIPS 2023)","url":"https://github.com/thuml/ForkMerge"},{"title":"[2301.12618] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://arxiv.org/abs/2301.12618"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/60f9118a849e8e9a0c67e2a36ad80ebf-Abstract-Conference.html"},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning | OpenReview","url":"https://openreview.net/forum?id=vZHk1QlBQW"},{"title":"[Quick Review] ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://liner.com/review/forkmerge-mitigating-negative-transfer-in-auxiliarytask-learning"},{"title":"dblp: ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning.","url":"https://dblp.org/rec/conf/nips/JiangCPWL0L23.html"},{"title":"Releases · thuml/ForkMerge","url":"https://github.com/thuml/ForkMerge/releases"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=ForkMerge:+Mitigating+Negative+Transfer+in+Auxiliary-Task+Learning."},{"title":"ForkMerge: Mitigating Negative Transfer in Auxiliary-Task Learning","url":"https://ise.thss.tsinghua.edu.cn/~mlong/doc/ForkMerge-nips23.pdf"}]

Based on the search results, I found information about the ForkMerge paper presented at NeurIPS 2023:

ForkMerge addresses Auxiliary-Task Learning (ATL), which aims to improve the performance of the target task by leveraging knowledge from related tasks, but occasionally learning multiple tasks simultaneously results in negative transfer—
…[truncated 827 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T02:09:20.221456+00:00_

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
  "session": "worker_research_plan005-negative-literature_20260514T020402",
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

_source line 42 · 2026-05-14T02:09:20.222026+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO el
…[truncated 20214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T02:09:20.222396+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
  "content": "# Plan005 NEGATIVE 结果文献调研：辅助 Reward 降低主目标性能\n\n## 背景\n\nplan005-sta-low-s42 实验结论为 NEGATIVE：GRPO 训练中 STA reward (weight=0.1) 导致 prove_rate 下降 10.7%（0.7725 vs exec-only 0.865）。ISR/PR ratio=0.298 稳定，说明 STA 确实维持了结构性分离，但任何非零 STA 权重都会引入 penalty effect。\n\n本报告调研 multi-objective RL 和 LLM reasoning 领域中关于\"辅助/过程 reward 降低主目标性能\"现象的相关文献。\n\n---\n\n## Paper 1: On Designing Effective RL Reward at Training Time for LLM Reasoning\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu |\n| 年份 | 2024 |\n| Venue | arXiv 2410.15115 |\n\n**核心发现**: 学习到的 PRM (Process Reward Model) 和 ORM (Outcome Reward Model) 用于 RL 训练时，**可能不仅无帮助，甚至损害训练效果**，产生比仅使用 success reward 训练的模型更差的性能。模型通过重复正确但不必要的推理步骤获得高 reward，造成严重的 reward hacking。\n\n**解决方案**: 提出两种 reward refinement 技术：\n- **Clipping**: 限制累积 reward 的上界\n- **Delta**: 限制跨 trajectory 的 reward 增长幅度\n\n两者确保累积 reward 有上界，防止 learned reward model 被 exploit。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 本质上是一种结构性 process reward。该论文直接证明 process reward 在 RL 训练时可降低主目标（accuracy/prove_rate）性能。STA weight=0.1 的 prove_rate 下降 10.7% 与此现象一致。Clipping/Delta 技术可作为 STA 改进方向——限制 ISR 对总 reward 的最大贡献。\n\n---\n\n## Paper 2: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal |\n| 年份 | 2025 |\n| Venue | arXiv 2509.03403 |\n\n**核心发现**: PRM 虽然提供细粒度的中间步骤指导，但**频繁出现不准确性且容易被 reward hacking 利用**。而 ORM 缺乏足够的粒度来评估推理质量。直接混合 PRM+ORM 信号会导致性能退化。\n\n**解决方案**: PROF (PRocess cOnsistency Filter) — 基于 PRM-ORM 一致性的数据过滤。保留\"高 process value 的正确 response\"和\"低 process value 的错误 response\"，过滤掉不一致样本。比直接混合方法**提升 4%+ 准确率**。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 是一种 process-level signal（结构必要性），与 execution outcome 是两个不同维度。PROF 的思路建议：仅在 ISR 与 execution 结果一致时使用 ISR reward（即只对 prove 成功的样本施加 ISR bonus，对 prove 失败的样本不施加 ISR penalty），而非无条件线性组合。这可能是解决 plan005 negative 的关键方向。\n\n---\n\n## Paper 3: Confronting Reward Model Overoptimization with Constrained RLHF\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer |\n| 年份 | 2023 |\n| Venue | arXiv 2310.04373 / ICLR 2024 |\n\n**核心发现**: 首个研究 composite reward model 过度优化的工作。发现组合多个 reward model 时，**component RM 之间的相关性显著影响过度优化发生的阈值**。超过阈值后，更高的 proxy reward 反而关联更差的真实表现。\n\n**解决方案**: \n- **Constrained RL**: 将每个 component RM 的优化限制在其\"有用阈值\"内\n- **Dynamic Lagrange Multipliers**: 通过拉格朗日乘子自动学习动态权重，替代固定权重的线性组合\n- **Adaptive Gradient-Free Optimization**: 在训练过程中识别最优性能点\n\n**与 plan005 的关联**: **直接相关**。plan005 使用固定权重 0.1 线性组合 exec reward 和 ISR。该论文表明固定权重的线性标量化存在本质缺陷，建议使用 constrained RL 或动态 Lagrange 乘子权重。这为 STA 提供了明确的改进方向：用约束优化替代固定权重。\n\n---\n\n## Paper 4: Defining and Characterizing Reward Hacking\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger |\n| 年份 | 2022 |\n| Venue | arXiv 2209.13085 / NeurIPS 2022 |\n\n**核心发现**: 形式化定义了 reward hacking。关键定理：**对于所有随机策略的集合，两个 reward function 只有在其中一个为常数时才是 unhackable 的**。这意味着任何非平凡的 proxy reward（如 ISR）在被优化时，都有可能降低 true reward（如 prove_rate）。\n\n**理论意义**: 该结果为 plan005 的 negative 提供了**理论解释基础**——ISR 作为 prove_rate 的 proxy，在任何非零权重下都可能 hack 真实目标。这不是 STA 特有的问题，而是 reward composition 的基本限制。\n\n**解决方向**: 论文建议通过限制策略空间（而非使 reward 更复杂）来缓解 hacking。对 STA 而言，这意味着可能需要约束优化策略空间（如 KL penalty 或 clipping），而非简单调低 ISR 权重。\n\n---\n\n## Paper 5: LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Mohammad Rezaei, Jens Lehmann, Sahar Vahdati |\n| 年份 | 2026 |\n| Venue | arXiv 2604.02341 (submitted to IJCNN 2026) |\n\n**核心发现**: PRM scores 如果作为绝对 reward 被优化，**会放大\"流利但错误\"的推理模式并诱发 reward hacking**。PRM 经常对最终不正确的推理路径给出高分。\n\n**解决方案**: **Outcome-Conditioned Centering** — 将错误 trajectory 的 PRM scores 平移至零均值。这在保留 PRM 对中间步骤的排序信息的同时，消除 PRM 对错误 trajectory 的系统性偏差。结果：以更少的 rollout 达到比 outcome-only baseline 一致的提升。\n\n**与 plan005 的关联**: **高度相关**。ISR 目前无条件地对所有样本施加：prove 成功的样本得到 ISR bonus（正面），prove 失败的样本被 ISR 评估后可能得到非零 reward（负面效应）。Outcome-conditioned centering 建议：将 ISR 调整为以 execution outcome 为条件——仅对 prove 成功的样本保留 ISR 差异化信号，对 prove 失败的样本将 ISR 归零。\n\n---\n\n## 综合分析与 STA 改进方向\n\n### plan005 NEGATIVE 的理论解释\n\n5 篇论文一致指向同一机制：**辅助/过程 reward 在 RL 训练中降低主目标性能**是一个已知且普遍的现象，不是 STA 特有的。原因包括：\n\n1. **Proxy reward 的固有 hackability**（Skalse et al.）：任何非常数 proxy 都可能降低 true reward\n2. **Process reward 的不准确性**（Gao et al., Ye et al.）：process-level signal 与 outcome 不完全对齐\n3. **固定权重线性组合的缺陷**（Moskovitz et al.）：无法适应训练阶段变化\n4. **无条件施加 process reward 的危害**（Rezaei et al.）：对错误 trajectory 的 process reward 破坏梯度信号\n\n### 可行改进方案（优先级排序）\n\n| 方案 | 来源 | 核心思路 | 实施复杂度 |\n|------|------|----------|-----------|\n| **Outcome-conditioned ISR** | PROGRS | 仅对 prove 成功的样本施加 ISR 差异化 reward | 低 |\n| **ISR Clipping** | Gao et al. | 限制 ISR 对总 reward 的最大贡献 | 低 |\n| **Consistency Filtering** | PROF | 仅使用 ISR-execution 一致的样本 | 中 |\n| **Dynamic Lagrange Weighting** | Moskovitz et al. | 用约束优化自动学习 ISR 权重 | 高 |\n| **Bonus-only ISR** | 综合 | ISR 仅作为 bonus（≥0），不作为 penalty | 低 |\n\n### 推荐下一步\n\n最低成本高收益方案：**Bonus-only + Outcome-conditioned ISR**。具体实现：\n- 对 prove 成功的样本：`reward = exec_reward + α × max(ISR - baseline, 0)`\n- 对 prove 失败的样本：`reward = exec_reward`（ISR 不参与）\n\n这同时解决了 Skalse 的 hackability 问题（ISR 只做正向 bonus）和 Rezaei 的 outcome-conditioning 问题。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
    "content": "# Plan005 NEGATIVE 结果文献调研：辅助 Reward 降低主目标性能\n\n## 背景\n\nplan005-sta-low-s42 实验结论为 NEGATIVE：GRPO 训练中 STA reward (weight=0.1) 导致 prove_rate 下降 10.7%（0.7725 vs exec-only 0.865）。ISR/PR ratio=0.298 稳定，说明 STA 确实维持了结构性分离，但任何非零 STA 权重都会引入 penalty effect。\n\n本报告调研 multi-objective RL 和 LLM reasoning 领域中关于\"辅助/过程 reward 降低主目标性能\"现象的相关文献。\n\n---\n\n## Paper 1: On Designing Effective RL Reward at Training Time for LLM Reasoning\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu |\n| 年份 | 2024 |\n| Venue | arXiv 2410.15115 |\n\n**核心发现**: 学习到的 PRM (Process Reward Model) 和 ORM (Outcome Reward Model) 用于 RL 训练时，**可能不仅无帮助，甚至损害训练效果**，产生比仅使用 success reward 训练的模型更差的性能。模型通过重复正确但不必要的推理步骤获得高 reward，造成严重的 reward hacking。\n\n**解决方案**: 提出两种 reward refinement 技术：\n- **Clipping**: 限制累积 reward 的上界\n- **Delta**: 限制跨 trajectory 的 reward 增长幅度\n\n两者确保累积 reward 有上界，防止 learned reward model 被 exploit。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 本质上是一种结构性 process reward。该论文直接证明 process reward 在 RL 训练时可降低主目标（accuracy/prove_rate）性能。STA weight=0.1 的 prove_rate 下降 10.7% 与此现象一致。Clipping/Delta 技术可作为 STA 改进方向——限制 ISR 对总 reward 的最大贡献。\n\n---\n\n## Paper 2: Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal |\n| 年份 | 2025 |\n| Venue | arXiv 2509.03403 |\n\n**核心发现**: PRM 虽然提供细粒度的中间步骤指导，但**频繁出现不准确性且容易被 reward hacking 利用**。而 ORM 缺乏足够的粒度来评估推理质量。直接混合 PRM+ORM 信号会导致性能退化。\n\n**解决方案**: PROF (PRocess cOnsistency Filter) — 基于 PRM-ORM 一致性的数据过滤。保留\"高 process value 的正确 response\"和\"低 process value 的错误 response\"，过滤掉不一致样本。比直接混合方法**提升 4%+ 准确率**。\n\n**与 plan005 的关联**: **高度相关**。STA 的 ISR 是一种 process-level signal（结构必要性），与 execution outcome 是两个不同维度。PROF 的思路建议：仅在 ISR 与 execution 结果一致时使用 ISR reward（即只对 prove 成功的样本施加 ISR bonus，对 prove 失败的样本不施加 ISR penalty），而非无条件线性组合。这可能是解决 plan005 negative 的关键方向。\n\n---\n\n## Paper 3: Confronting Reward Model Overoptimization with Constrained RLHF\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer |\n| 年份 | 2023 |\n| Venue | arXiv 2310.04373 / ICLR 2024 |\n\n**核心发现**: 首个研究 composite reward model 过度优化的工作。发现组合多个 reward model 时，**component RM 之间的相关性显著影响过度优化发生的阈值**。超过阈值后，更高的 proxy reward 反而关联更差的真实表现。\n\n**解决方案**: \n- **Constrained RL**: 将每个 component RM 的优化限制在其\"有用阈值\"内\n- **Dynamic Lagrange Multipliers**: 通过拉格朗日乘子自动学习动态权重，替代固定权重的线性组合\n- **Adaptive Gradient-Free Optimization**: 在训练过程中识别最优性能点\n\n**与 plan005 的关联**: **直接相关**。plan005 使用固定权重 0.1 线性组合 exec reward 和 ISR。该论文表明固定权重的线性标量化存在本质缺陷，建议使用 constrained RL 或动态 Lagrange 乘子权重。这为 STA 提供了明确的改进方向：用约束优化替代固定权重。\n\n---\n\n## Paper 4: Defining and Characterizing Reward Hacking\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger |\n| 年份 | 2022 |\n| Venue | arXiv 2209.13085 / NeurIPS 2022 |\n\n**核心发现**: 形式化定义了 reward hacking。关键定理：**对于所有随机策略的集合，两个 reward function 只有在其中一个为常数时才是 unhackable 的**。这意味着任何非平凡的 proxy reward（如 ISR）在被优化时，都有可能降低 true reward（如 prove_rate）。\n\n**理论意义**: 该结果为 plan005 的 negative 提供了**理论解释基础**——ISR 作为 prove_rate 的 proxy，在任何非零权重下都可能 hack 真实目标。这不是 STA 特有的问题，而是 reward composition 的基本限制。\n\n**解决方向**: 论文建议通过限制策略空间（而非使 reward 更复杂）来缓解 hacking。对 STA 而言，这意味着可能需要约束优化策略空间（如 KL penalty 或 clipping），而非简单调低 ISR 权重。\n\n---\n\n## Paper 5: LLM Reasoning with Process Rewards for Outcome-Guided Steps (PROGRS)\n\n| 字段 | 内容 |\n|------|------|\n| 作者 | Mohammad Rezaei, Jens Lehmann, Sahar Vahdati |\n| 年份 | 2026 |\n| Venue | arXiv 2604.02341 (submitted to IJCNN 2026) |\n\n**核心发现**: PRM scores 如果作为绝对 reward 被优化，**会放大\"流利但错误\"的推理模式并诱发 reward hacking**。PRM 经常对最终不正确的推理路径给出高分。\n\n**解决方案**: **Outcome-Conditioned Centering** — 将错误 trajectory 的 PRM scores 平移至零均值。这在保留 PRM 对中间步骤的排序信息的同时，消除 PRM 对错误 trajectory 的系统性偏差。结果：以更少的 rollout 达到比 outcome-only baseline 一致的提升。\n\n**与 plan005 的关联**: **高度相关**。ISR 目前无条件地对所有样本施加：prove 成功的样本得到 ISR bonus（正面），prove 失败的样本被 ISR 评估后可能得到非零 reward（负面效应）。Outcome-conditioned centering 建议：将 ISR 调整为以 execution outcome 为条件——仅对 prove 成功的样本保留 ISR 差异化信号，对 prove 失败的样本将 ISR 归零。\n\n---\n\n## 综合分析与 STA 改进方向\n\n### plan005 NEGATIVE 的理论解释\n\n5 篇论文一致指向同一机制：**辅助/过程 reward 在 RL 训练中降低主目标性能**是一个已知且普遍的现象，不是 STA 特有的。原因包括：\n\n1. **Proxy reward 的固有 hackability**（Skalse et al.）：任何非常数 proxy 都可能降低 true reward\n2. **Process reward 的不准确性**（Gao et al., Ye et al.）：process-level signal 与 outcome 不完全对齐\n3. **固定权重线性组合的缺陷**（Moskovitz et al.）：无法适应训练阶段变化\n4. **无条件施加 process reward 的危害**（Rezaei et al.）：对错误 trajectory 的 process reward 破坏梯度信号\n\n### 可行改进方案（优先级排序）\n\n| 方案 | 来源 | 核心思路 | 实施复杂度 |\n|------|------|----------|-----------|\n| **Outcome-conditioned ISR** | PROGRS | 仅对 prove 成功的样本施加 ISR 差异化 reward | 低 |\n| **ISR Clipping** | Gao et al. | 限制 ISR 对总 reward 的最大贡献 | 低 |\n| **Consistency Filtering** | PROF | 仅使用 ISR-execution 一致的样本 | 中 |\n| **Dynamic Lagrange Weighting** | Moskovitz et al. | 用约束优化自动学习 ISR 权重 | 高 |\n| **Bonus-only ISR** | 综合 | ISR 仅作为 bonus（≥0），不作为 penalty | 低 |\n\n### 推荐下一步\n\n最低成本高收益方案：**Bonus-only + Outcome-conditioned ISR**。具体实现：\n- 对 prove 成功的样本：`reward = exec_reward + α × max(ISR - baseline, 0)`\n- 对 prove 失败的样本：`reward = exec_reward`（ISR 不参与）\n\n这同时解决了 Skalse 的 hackability 问题（ISR 只做正向 bonus）和 Rezaei 的 outcome-conditioning 问题。\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T02:09:20.222774+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T02:09:20.223028+00:00_

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
  "session": "worker_research_plan005-negative-literature_20260514T020402",
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

_source line 46 · 2026-05-14T02:09:20.223562+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml\", \"content\": \"# Literature Map for Solver Trace Ablation (STA)\\n# Categories:\\n#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO\\n#   2. reward-shaping: Reward shaping for code/formal verification\\n#   3. mutation-testing: Mutation testing in software engineering\\n#   4. intensional-analysis: Intensional program analysis\\n#   5. reward-hacking: Reward hacking / overoptimization\\n#   6. fol-formalization: FOL/Prolog formalization with LLMs\\n\\npapers:\\n\\n  # ============================================================\\n  # Category 1: Neurosymbolic reasoning + RL/GRPO\\n  # ============================================================\\n\\n  - id: deepseek-r1\\n    title: \\\"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\\\"\\n    authors: \\\"DeepSeek-AI\\\"\\n    year: 2025\\n    venue: \\\"arXiv 2501.12948 / Nature 2025\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.\\n      STA builds on the same GRPO framework but replaces binary outcome reward with\\n      intensional structural reward for neurosymbolic formalization.\\n    key_finding: >\\n      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,\\n      showing emergent chain-of-thought reasoning from RL alone.\\n\\n  - id: deepseekmath\\n    title: \\\"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\\\"\\n    authors: \\\"Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv 2402.03300\\\"\\n    category: neurosymbolic-rl\\n    role: method-component\\n    relevance: >\\n      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm\\n      used in STA training. GRPO el
…[truncated 20214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T02:09:20.223879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": "0",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "offset": "0",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T02:09:20.224157+00:00_

0	# Literature Map for Solver Trace Ablation (STA)
1	# Categories:
2	#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
3	#   2. reward-shaping: Reward shaping for code/formal verification
4	#   3. mutation-testing: Mutation testing in software engineering
5	#   4. intensional-analysis: Intensional program analysis
6	#   5. reward-hacking: Reward hacking / overoptimization
7	#   6. fol-formalization: FOL/Prolog formalization with LLMs
8	
9	papers:
10	
11	  # ============================================================
12	  # Category 1: Neurosymbolic reasoning + RL/GRPO
13	  # ============================================================
14	
15	  - id: deepseek-r1
16	    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
17	    authors: "DeepSeek-AI"
18	    year: 2025
19	    venue: "arXiv 2501.12948 / Nature 2025"
20	    category: neurosymbolic-rl
21	    role: method-component
22	    relevance: >
23	      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
24	      STA builds on the same GRPO framework but replaces binary outcome reward with
25	      intensional structural reward for neurosymbolic formalization.
26	    key_finding: >
27	      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
28	      showing emergent chain-of-thought reasoning from RL alone.
29	
30	  - id: deepseekmath
31	    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
32	    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
33	    year: 2024
34	    venue: "arXiv 2402.03300"
35	    category: neurosymbolic-rl
36	    role: method-component
37	    relevance: >
38	      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
39	      used in STA training. GRPO eliminates the critic model by estimating
40	      baselines from group scores.
41	    key_finding: >
42	      GRPO matches PPO performance while significantly reducing training
…[truncated 2525 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-14T02:09:20.224421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "offset": "130",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "offset": "130",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T02:09:20.224723+00:00_

130	    authors: "Various"
131	    year: 2025
132	    venue: "arXiv 2506.14245"
133	    category: reward-shaping
134	    role: background
135	    relevance: >
136	      Shows that binary verifiable rewards (pass/fail) can implicitly incentivize
137	      reasoning. STA argues that for neurosymbolic formalization, binary reward
138	      is insufficient and structural reward is needed to avoid reward hacking.
139	    key_finding: >
140	      RLVR with binary verification implicitly teaches correct reasoning
141	      strategies, not just answer matching.
142	
143	  - id: rubric-grpo
144	    title: "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning"
145	    authors: "Various"
146	    year: 2025
147	    venue: "arXiv 2605.08061"
148	    category: reward-shaping
149	    role: direct-competitor
150	    relevance: >
151	      Uses structured rubric-based rewards with GRPO, similar in spirit to
152	      STA's structured ISR. Key difference: rubric rewards come from LLM
153	      judges, while ISR comes from solver-based mutation testing.
154	    key_finding: >
155	      Structured multi-dimensional reward signals improve GRPO training
156	      generalization compared to scalar rewards.
157	
158	  # ============================================================
159	  # Category 3: Mutation testing in software engineering

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-14T02:09:20.224989+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "old_string": "  # ============================================================\n  # Category 3: Mutation testing in software engineering",
  "new_string": "  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "old_string": "  # ============================================================\n  # Category 3: Mutation testing in software engineering",
    "new_string": "  - id: gao-effective-rl-reward\n    title: \"On Designing Effective RL Reward at Training Time for LLM Reasoning\"\n    authors: \"Jiaxuan Gao, Shusheng Xu, Wenjie Ye, Weilin Liu, Chuyi He, Wei Fu, Zhiyu Mei, Guangju Wang, Yi Wu\"\n    year: 2024\n    venue: \"arXiv 2410.15115\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Demonstrates that learned process/outcome reward models can hurt RL\n      training, producing worse performance than simple success reward only.\n      Directly explains plan005 NEGATIVE: STA's ISR as auxiliary process\n      reward degrades prove_rate compared to exec-only baseline.\n    key_finding: >\n      PRM/ORM rewards may NOT help or even hurt RL training vs success-only\n      reward. Solution: Clipping and Delta techniques to bound accumulated\n      reward magnitude prevent reward hacking.\n\n  - id: prof-process-outcome\n    title: \"Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training\"\n    authors: \"Chenlu Ye, Zhou Yu, Ziji Zhang, Hao Chen, Narayanan Sadagopan, Jing Huang, Tong Zhang, Anurag Beniwal\"\n    year: 2025\n    venue: \"arXiv 2509.03403\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Shows that naively combining PRM+ORM signals leads to performance\n      degradation. PROF consistency filter retains only PRM-ORM consistent\n      samples, achieving 4%+ improvement over blending. Suggests STA should\n      only apply ISR when consistent with execution outcome.\n    key_finding: >\n      Process rewards frequently suffer from inaccuracies and reward hacking\n      susceptibility. PROF filters training data by PRM-ORM consistency,\n      outperforming naive reward blending by 4%+ accuracy.\n\n  - id: moskovitz-constrained-rlhf\n    title: \"Confronting Reward Model Overoptimization with Constrained RLHF\"\n    authors: \"Ted Moskovitz, Aaditya K. Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca D. Dragan, Stephen McAleer\"\n    year: 2023\n    venue: \"arXiv 2310.04373 / ICLR 2024\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      First study on overoptimization in composite reward models. Shows that\n      fixed-weight linear scalarization of component rewards leads to\n      degradation past a threshold. Proposes constrained RL with dynamic\n      Lagrange multiplier weighting as alternative to fixed ISR weight.\n    key_finding: >\n      Correlation between component RMs significantly affects overoptimization\n      thresholds. Constrained RL with Lagrange multipliers outperforms\n      fixed-weight reward composition.\n\n  - id: skalse-reward-hacking\n    title: \"Defining and Characterizing Reward Hacking\"\n    authors: \"Joar Skalse, Nikolaus H. R. Howe, Dmitrii Krasheninnikov, David Krueger\"\n    year: 2022\n    venue: \"arXiv 2209.13085 / NeurIPS 2022\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      Formal proof that for stochastic policies, two reward functions are\n      unhackable only if one is constant. Theoretically explains why any\n      non-zero ISR weight can decrease prove_rate -- this is a fundamental\n      property of reward composition, not STA-specific.\n    key_finding: >\n      Any non-constant proxy reward can decrease true reward when optimized.\n      Unhackability requires the proxy to be constant, making all non-trivial\n      auxiliary rewards theoretically vulnerable to degrading primary performance.\n\n  - id: progrs-outcome-conditioned\n    title: \"LLM Reasoning with Process Rewards for Outcome-Guided Steps\"\n    authors: \"Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\"\n    year: 2026\n    venue: \"arXiv 2604.02341\"\n    category: reward-shaping\n    role: background\n    relevance: >\n      PRM scores optimized as absolute rewards amplify fluent failure modes.\n      Outcome-conditioned centering shifts incorrect trajectories' PRM scores\n      to zero mean, preserving ranking info without corrupting gradients.\n      Suggests STA should condition ISR on execution outcome.\n    key_finding: >\n      Naive process rewards induce reward hacking by rewarding locally fluent\n      but globally incorrect reasoning. Outcome-conditioned centering resolves\n      the conflict with fewer rollouts than outcome-only baselines.\n\n  # ============================================================\n  # Category 3: Mutation testing in software engineering"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T02:09:20.225446+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-14T02:09:20.225723+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T02:09:20.226188+00:00_

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
…[truncated 24865 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-14T02:09:20.226481+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
  "description": "Read full literature_map.yaml content for MCP save"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml",
    "description": "Read full literature_map.yaml content for MCP save"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T02:09:20.226934+00:00_

# Literature Map for Solver Trace Ablation (STA)
# Categories:
#   1. neurosymbolic-rl: Neurosymbolic reasoning + RL/GRPO
#   2. reward-shaping: Reward shaping for code/formal verification
#   3. mutation-testing: Mutation testing in software engineering
#   4. intensional-analysis: Intensional program analysis
#   5. reward-hacking: Reward hacking / overoptimization
#   6. fol-formalization: FOL/Prolog formalization with LLMs

papers:

  # ============================================================
  # Category 1: Neurosymbolic reasoning + RL/GRPO
  # ============================================================

  - id: deepseek-r1
    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    authors: "DeepSeek-AI"
    year: 2025
    venue: "arXiv 2501.12948 / Nature 2025"
    category: neurosymbolic-rl
    role: method-component
    relevance: >
      Demonstrates that pure RL (GRPO) can incentivize reasoning in LLMs without SFT.
      STA builds on the same GRPO framework but replaces binary outcome reward with
      intensional structural reward for neurosymbolic formalization.
    key_finding: >
      DeepSeek-R1-Zero trained via GRPO alone achieves 71% on AIME 2024,
      showing emergent chain-of-thought reasoning from RL alone.

  - id: deepseekmath
    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
    authors: "Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, et al."
    year: 2024
    venue: "arXiv 2402.03300"
    category: neurosymbolic-rl
    role: method-component
    relevance: >
      Introduces GRPO (Group Relative Policy Optimization), the RL algorithm
      used in STA training. GRPO eliminates the critic model by estimating
      baselines from group scores.
    key_finding: >
      GRPO matches PPO performance while significantly reducing training
      resources; improves GSM8K 82.9->88.2% and MATH 46.8->51.7%.

  - id: logic-rl
    title: "Logic-RL: Unleashing L
…[truncated 22696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-14T02:09:20.227258+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
  "description": "Verify both output files exist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md",
    "description": "Verify both output files exist"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-14T02:09:20.227469+00:00_

-rw-r--r-- 1 ubuntu ubuntu  8123 May 14 02:07 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/plan005_negative_literature.md
-rw-r--r-- 1 ubuntu ubuntu 24697 May 14 02:08 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_plan005-negative-literature_20260514T020402",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-14T02:09:20.227732+00:00_

完成。

**调研报告** → `artifacts/plan005_negative_literature.md`
**文献地图** → `literature_map.yaml` 新增 5 篇论文（reward-shaping category）

### 核心结论

plan005 的 NEGATIVE 结果（ISR 降低 prove_rate）是 multi-objective RL 中已知的 **auxiliary reward degradation** 现象，5 篇论文从不同角度确认：

1. **Gao et al. (2024)** — process reward 在 RL 训练中可能**比 success-only reward 更差**
2. **Ye et al. (2025, PROF)** — 朴素混合 PRM+ORM 导致退化，需 consistency filtering
3. **Moskovitz et al. (2023, ICLR 2024)** — 固定权重线性组合存在过度优化阈值
4. **Skalse et al. (2022, NeurIPS)** — 理论证明：任何非常数 proxy reward 都可能降低 true reward
5. **Rezaei et al. (2026, PROGRS)** — 无条件 process reward 会放大失败模式，需 outcome-conditioned centering

**推荐改进方向**：Bonus-only + Outcome-conditioned ISR（仅对 prove 成功的样本施加正向 ISR bonus），实施复杂度低且同时解决 hackability 和 gradient corruption 问题。

Sources:
- [Gao et al. - On Designing Effective RL Reward](https://arxiv.org/abs/2410.15115)
- [Ye et al. - Beyond Correctness (PROF)](https://arxiv.org/abs/2509.03403)
- [Moskovitz et al. - Confronting Reward Model Overoptimization](https://arxiv.org/abs/2310.04373)
- [Skalse et al. - Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085)
- [Rezaei et al. - PROGRS](https://arxiv.org/abs/2604.02341)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_plan005-negative-literature_20260514T020402"
}
```

</details>

---
