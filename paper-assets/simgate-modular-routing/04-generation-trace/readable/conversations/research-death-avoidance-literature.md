# research death avoidance literature

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_research_death-avoidance-literature_20260513T205941.jsonl`
- **Structured JSON:** [`eaa60711977a7c35c909.json`](../../sessions/ea/eaa60711977a7c35c909.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-13T21:03:54.082178+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T21:03:54.082501+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T21:03:54.082665+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "literature_map.yaml",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "literature_map.yaml",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T21:03:54.082822+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T21:03:54.082952+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "paper_framing.md",
  "max_chars": "12000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "paper_framing.md",
    "max_chars": "12000"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T21:03:54.083191+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md\", \"content\": \"# Paper Framing — simgate-modular-routing\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (ARR short paper, 4 pages + references)\\n- Fallback: EMNLP 2026 Findings\\n- Deadline: ARR May 25, 2026 (12 days remaining)\\n\\n## Core Insight\\n\\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 98% ties in sparse-reward settings) and discover that **death avoidance accounts for ~93% of routing signal** on ScienceWorld. Non-death performance is approximately equal between modalities. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\\n\\n## Core Claims (2 claims for short paper)\\n\\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (+30-60pp), with **death avoidance as the dominant mechanism** (~93% of episode-level routing labels are det-preferred). Non-death score deltas are small and inconsistent (range: -6.8 to +4.2, most near 0). The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance. Evidence: 14+ task types consistently show death-dominated signal; only 1 task type is internal-preferred (pure lookup task with 0% death rate).\\n\\n**C2 (Episode-level counterfactual labeling as diagnostic methodology)**: Per-step oracle labeling degenerates in sparse-reward environments (98.2% tie rate on ScienceWorld). Episode-level 
…[truncated 9780 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T21:03:54.083346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "catastrophic failure LLM agent tool use safety irreversible action"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "catastrophic failure LLM agent tool use safety irreversible action"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-13T21:03:54.083475+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ScienceWorld benchmark failure mode death penalty negative score LLM agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ScienceWorld benchmark failure mode death penalty negative score LLM agent"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T21:03:54.083590+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "safe exploration reinforcement learning LLM agent constraint satisfaction safety critic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "safe exploration reinforcement learning LLM agent constraint satisfaction safety critic"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-13T21:03:54.083731+00:00_

Web search results for query: "catastrophic failure LLM agent tool use safety irreversible action"

Links: [{"title":"PARTNERSHIP ON AI Prioritizing Real-Time Failure Detection in AI Agents 1","url":"https://partnershiponai.org/wp-content/uploads/2025/09/agents-real-time-failure-detection.pdf?vgo_ee=zBAC1la9zQyJHSnpG6BgMHYqtA2DVnJIxaZdlyzMse4LqANZiVSdqdBDKQ%3D%3D:UuOdAvb8Al76ab6ZrhxDyj0LJ66FZeBh"},{"title":"SafeHarbor: Defining Precise Decision Boundaries via Hierarchical Memory-Augmented Guardrail for LLM Agent Safety","url":"https://arxiv.org/html/2605.05704"},{"title":"When Refusals Fail: Unstable Safety Mechanisms in Long-Context LLM Agents","url":"https://arxiv.org/pdf/2512.02445"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492v1"},{"title":"Taxonomy of Failure Mode in Agentic AI Systems","url":"https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf"},{"title":"The risk of destructive capabilities in agentic ai - Noma Security","url":"https://noma.security/blog/the-risk-of-destructive-capabilities-in-agentic-ai/"},{"title":"Towards Verifiably Safe Tool Use for LLM Agents Aarya Doshi","url":"https://arxiv.org/pdf/2601.08012"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/topics/agent-safetybench"},{"title":"Agent Safety | Microsoft Learn","url":"https://learn.microsoft.com/en-us/agent-framework/agents/safety"},{"title":"How Do LLMs Fail In Agentic Scenarios?","url":"https://arxiv.org/pdf/2512.07497"}]

I found comprehensive information on catastrophic failures in LLM agents related to tool use safety and irreversible actions. Here are the key findings:

## Irreversible Actions and Catastrophic Failures

Irreversible failures involve one-way operations that cannot be undone, or can only be reversed with extre
…[truncated 1652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T21:03:54.083904+00:00_

Web search results for query: "safe exploration reinforcement learning LLM agent constraint satisfaction safety critic"

Links: [{"title":"LLM-Guided Safe Reinforcement Learning for Energy System Topology Reconfiguration","url":"https://arxiv.org/html/2603.14018"},{"title":"Benchmarking Safe Exploration in Deep Reinforcement Learning Alex Ray∗ OpenAI","url":"https://cdn.openai.com/safexp-short.pdf"},{"title":"Safe Exploration in Reinforcement Learning:","url":"https://papers.nips.cc/paper_files/paper/2023/file/5d4cd12ef6efedbf26b69b410f1f7d67-Paper-Conference.pdf"},{"title":"Safety-Aware Reinforcement Learning via Contrastive State Representations | OpenReview","url":"https://openreview.net/forum?id=lxKH0pnbhS"},{"title":"GitHub - chauncygu/Safe-Reinforcement-Learning-Baselines: The repository is for safe reinforcement learning baselines. · GitHub","url":"https://github.com/chauncygu/Safe-Reinforcement-Learning-Baselines"},{"title":"Safety-constrained reinforcement learning with a distributional safety critic | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-022-06187-8"},{"title":"LA-RL: Language Action-guided Reinforcement Learning with Safety Guarantees for Autonomous Highway Driving","url":"https://arxiv.org/html/2512.05686v1"},{"title":"1 Safe Reinforcement Learning for Power System Control: A Review","url":"https://arxiv.org/pdf/2407.00681"},{"title":"Safety Representations for Safer Policy Learning | OpenReview","url":"https://openreview.net/forum?id=gJG4IPwg6l"},{"title":"A Comprehensive Survey on Safe Reinforcement Learning","url":"https://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf"}]

Based on the search results, here's what I found on safe exploration in reinforcement learning with LLM agents, constraint satisfaction, and safety critics:

## Key Research Areas

**LLM-Guided Safe RL Frameworks:**
Recent work proposes LLM-guided safe reinforcement learning frameworks that introduce differentiable sa
…[truncated 1699 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-13T21:03:54.084121+00:00_

Web search results for query: "ScienceWorld benchmark failure mode death penalty negative score LLM agent"

Links: [{"title":"ScienceWorld Benchmark","url":"https://www.emergentmind.com/topics/scienceworld-benchmark"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"How to Use AI Agents to Run LLM Benchmarks: A Custom Evaluation Framework | MindStudio","url":"https://www.mindstudio.ai/blog/ai-agents-custom-llm-benchmark-evaluation"},{"title":"Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems","url":"https://arxiv.org/html/2604.22708v1"},{"title":"Killed by LLM","url":"https://r0bk.github.io/killedbyllm/"},{"title":"AgentBench: Evaluating LLMs as Agents | OpenReview","url":"https://openreview.net/forum?id=zAdUB0aCTQ"},{"title":"Which Agent Causes Task Failures and When? On ...","url":"https://arxiv.org/pdf/2505.00212"},{"title":"AI Model Leaderboards & Benchmarks | Scale Labs","url":"https://labs.scale.com/leaderboard"},{"title":"Where LLM Agents Fail And How They can Learn From Failures | OpenReview","url":"https://openreview.net/forum?id=PFR4E8583W"},{"title":"Top 10 Open Datasets for LLM Safety, Toxicity & Bias Evaluation | Promptfoo","url":"https://www.promptfoo.dev/blog/top-llm-safety-bias-benchmarks/"}]

Based on the search results, I found information about ScienceWorld benchmark and its failure modes for LLM agents. Here's what the research shows:

## ScienceWorld Benchmark Overview

ScienceWorld employs quantitative scoring across three axes: task completion rate, average episode reward, and action validity, with scores derived from the fraction of subgoals accomplished before an invalid action or the specified maximal number of steps.

## Key Failure Modes

The benchmark reveals several critical failure modes for LLM agents:

**Valid Action Generation as a Major Bottleneck:** Large static LMs often produce unexecutable or context-inappropriate a
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T21:03:54.084311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogRouter ScienceWorld adaptive computation routing LLM agent 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogRouter ScienceWorld adaptive computation routing LLM agent 2024"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T21:03:54.084445+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ITP-R \"internal thought process\" world model routing ScienceWorld"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ITP-R \"internal thought process\" world model routing ScienceWorld"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T21:03:54.084563+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Check Yourself Before You Wreck Yourself\" LLM agent safety quitting 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Check Yourself Before You Wreck Yourself\" LLM agent safety quitting 2025"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-13T21:03:54.084686+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ReTool AgentMath code interpreter routing when to use tool LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ReTool AgentMath code interpreter routing when to use tool LLM 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T21:03:54.084797+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Toolformer ART Chameleon tool use learning LLM counterfactual labeling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Toolformer ART Chameleon tool use learning LLM counterfactual labeling"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T21:03:54.084936+00:00_

Web search results for query: "ITP-R "internal thought process" world model routing ScienceWorld"

Links: [{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530"},{"title":"Frontiers | An Integrated World Modeling Theory (IWMT) of Consciousness: Combining Integrated Information and Global Neuronal Workspace Theories With the Free Energy Principle and Active Inference Framework; Toward Solving the Hard Problem and Characterizing Agentic Causation","url":"https://frontiersin.org/articles/10.3389/frai.2020.00030/full"},{"title":"Internal world models in humans, animals, and AI - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0896627324004549"},{"title":"What is Information Processing Theory? Stages, Models & Limitations for 2026 | Research.com","url":"https://research.com/education/what-is-information-processing-theory"},{"title":"Frontiers | Integrated world modeling theory expanded: Implications for the future of consciousness","url":"https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2022.642397/full"},{"title":"Integrated world modeling theory expanded: Implications for the future of consciousness - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9730424/"},{"title":"Information-Processing Theory - an overview | ScienceDirect Topics","url":"https://www.sciencedirect.com/topics/psychology/information-processing-theory"},{"title":"Information Processing Theory – Educational Learning Theories","url":"https://openoregon.pressbooks.pub/educationallearningtheories3rd/chapter/chapter-12-information-processing-theory-2/"},{"title":"Integrated Information Theory (IIT)","url":"https://www.emergentmind.com/topics/integrated-information-theory-iit"},{"title":"Critiques of World Models","url":"https://arxiv.org/pdf/2507.05169"}]

Based on the web search results, I found relevant information about your query. The most relevant match is 
…[truncated 1328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-13T21:03:54.085148+00:00_

Web search results for query: "CogRouter ScienceWorld adaptive computation routing LLM agent 2024"

Links: [{"title":"Towards Generalized Routing: Model and Agent Orchestration for Adaptive and Efficient Inference","url":"https://arxiv.org/html/2509.07571v1"},{"title":"INPUT-ADAPTIVE ALLOCATION OF LM COMPUTATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"},{"title":"Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization","url":"https://arxiv.org/html/2602.23008"},{"title":"Large language model-based multi-agent systems for automated foundation design: router-driven task classification and expert selection framework | AI in Civil Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s43503-026-00088-8"},{"title":"Efficient Routing of Inference Requests across LLM Instances in Cloud-Edge Computing","url":"https://arxiv.org/html/2507.15553v1"},{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"GitHub - AGI-Edgerunners/LLM-Agents-Papers: A repo lists papers related to LLM based agent · GitHub","url":"https://github.com/AGI-Edgerunners/LLM-Agents-Papers"},{"title":"A data-augmented model routing framework for efficient LLM deployment in edge–cloud environments | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-08034-8"},{"title":"GitHub - luo-junyu/Awesome-Agent-Papers: [Up-to-date] Large Language Model Agent: A Survey on Methodology, Applications and Challenges · GitHub","url":"https://github.com/luo-junyu/Awesome-Agent-Papers"},{"title":"1 Optimizing NetGPT via Routing-Based Synergy and Reinforcement Learning","url":"https://www.arxiv.org/pdf/2511.22217"}]

Based on the web search results, I found information related to LLM adaptive routing and agent sy
…[truncated 1648 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T21:03:54.085324+00:00_

Web search results for query: "Toolformer ART Chameleon tool use learning LLM counterfactual labeling"

Links: [{"title":"[2302.04761] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://arxiv.org/abs/2302.04761"},{"title":"Self-Training Large Language Models for Tool-Use Without Demonstrations","url":"https://arxiv.org/html/2502.05867v1"},{"title":"[PDF] Toolformer: Language Models Can Teach Themselves to Use Tools | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Toolformer:-Language-Models-Can-Teach-Themselves-to-Schick-Dwivedi-Yu/53d128ea815bcc0526856eb5a9c42cc977cb36a7"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://www.researchgate.net/publication/368392996_Toolformer_Language_Models_Can_Teach_Themselves_to_Use_Tools?_tp=eyJjb250ZXh0Ijp7InBhZ2UiOiJzY2llbnRpZmljQ29udHJpYnV0aW9ucyIsInByZXZpb3VzUGFnZSI6bnVsbH19"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | OpenReview","url":"https://openreview.net/forum?id=Yacmpz84TH"},{"title":"Toolformer: How Language Models Learn to Use Tools by Themselves | by Darshan Tank | Medium","url":"https://medium.com/@darshantank_55417/toolformer-how-language-models-learn-to-use-tools-by-themselves-9724fb64ed0e"},{"title":"Tool learning with language models: a comprehensive survey of methods, pipelines, and benchmarks | Vicinagearth | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44336-025-00024-x"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | Research - AI at Meta","url":"https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://arxiv.org/pdf/2302.04761"},{"title":"Enhancing LLM Tool Use with High-quality Instruction Data from Knowledge Graph","url":"https://arxiv.org/html/2506.21071v1"}]

Based on the search results, here'
…[truncated 1691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-13T21:03:54.085508+00:00_

Web search results for query: ""Check Yourself Before You Wreck Yourself" LLM agent safety quitting 2025"

Links: [{"title":"[2510.16492] Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/abs/2510.16492"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv251016492K/abstract"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety | OpenReview","url":"https://openreview.net/forum?id=ALwpW0ygzI"},{"title":"Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://arxiv.org/html/2510.16492"},{"title":"NeurIPS Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://neurips.cc/virtual/2025/loc/san-diego/125248"},{"title":"Benjamin Plaut","url":"https://bplaut.github.io/"},{"title":"Ponnurangam Kumaraguru “PK” on X: \"🎉 New paper accepted to the NeurIPS 2025 “Reliable ML from Unreliable Data” Workshop: “Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety.” 📜 Preprint: https://t.co/bMWbFiER02 https://t.co/vKVz2cmssG\" / X","url":"https://x.com/ponguru/status/1986649704671957348"},{"title":"(PDF) Check Yourself Before You Wreck Yourself: Selectively Quitting Improves LLM Agent Safety","url":"https://www.researchgate.net/publication/396714988_Check_Yourself_Before_You_Wreck_Yourself_Selectively_Quitting_Improves_LLM_Agent_Safety"},{"title":"Check Yourself Before You Wreck Yourself: Selectively","url":"https://arxiv.org/pdf/2510.16492"},{"title":"The 36 toolkits included in the ToolEmu benchmark. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-36-toolkits-included-in-the-ToolEmu-benchmark_tbl1_396714988"}]

Based on the search results, here's what I found about "Check Yourself Before You Wreck Yourself":

…[truncated 1377 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T21:03:54.085697+00:00_

Web search results for query: "ReTool AgentMath code interpreter routing when to use tool LLM 2024 2025"

Links: [{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/html/2504.11536v1"},{"title":"ReTool: A Tool-Augmented Reinforcement Learning Framework for Optimizing LLM Reasoning with Computational Tools - MarkTechPost","url":"https://www.marktechpost.com/2025/04/20/retool-a-tool-augmented-reinforcement-learning-framework-for-optimizing-llm-reasoning-with-computational-tools/"},{"title":"AgentMath","url":"https://arxiv.org/pdf/2512.20745"},{"title":"ReTool: RL Framework for Tool-Integrated LLMs","url":"https://www.emergentmind.com/topics/retool"},{"title":"Published as a conference paper at ICLR 2026 RETOOL:","url":"https://openreview.net/pdf?id=tRk1nofSmz"},{"title":"ReTool: Reinforcement Learning for Strategic Tool Use in LLMs | OpenReview","url":"https://openreview.net/forum?id=tRk1nofSmz"},{"title":"ReTool","url":"https://retool-rl.github.io/"},{"title":"[2504.11536] ReTool: Reinforcement Learning for Strategic Tool Use in LLMs","url":"https://arxiv.org/abs/2504.11536"},{"title":"GitHub - verl-project/verl: verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework · GitHub","url":"https://github.com/verl-project/verl"},{"title":"Retool 2025 Feature Releases — AI, Agents & More","url":"https://retoolers.io/blog-posts/retool-2025-feature-releases-ai-multipage-apps-agents-more"}]

Based on the search results, here's what I found about ReTool, AgentMath, code interpreter routing, and when to use tools with LLMs in 2024-2025:

## ReTool: Strategic Tool Use in LLMs

ReTool is a reinforcement learning (RL) framework designed to enable strategic tool use in LLMs, with a particular emphasis on integrating code-interpreter (CI) capabilities directly into the reasoning loop.

### Key Features for Tool Routing

ReTool enhances long-form reasoning with tool-integrated learning through two key features: (1) dynamic in
…[truncated 1785 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T21:03:54.085885+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogRouter \"cognitive router\" LLM reasoning adaptive computation CoPO reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogRouter \"cognitive router\" LLM reasoning adaptive computation CoPO reinforcement learning"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-13T21:03:54.086028+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"death avoidance\" \"failure prevention\" reinforcement learning reward decomposition penalty avoidance vs positive reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"death avoidance\" \"failure prevention\" reinforcement learning reward decomposition penalty avoidance vs positive reward"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T21:03:54.086148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MTRouter ScienceWorld multi-turn LLM routing cost GPT 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MTRouter ScienceWorld multi-turn LLM routing cost GPT 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-13T21:03:54.086260+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Where LLM Agents Fail\" failure analysis agent benchmark 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Where LLM Agents Fail\" failure analysis agent benchmark 2025"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T21:03:54.086369+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARES \"adaptive routing\" LLM reasoning \"Mixture of Depths\" compute allocation 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARES \"adaptive routing\" LLM reasoning \"Mixture of Depths\" compute allocation 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T21:03:54.086526+00:00_

Web search results for query: "CogRouter "cognitive router" LLM reasoning adaptive computation CoPO reinforcement learning"

Links: [{"title":"[2506.09033] Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://arxiv.org/abs/2506.09033"},{"title":"Cog-Rethinker: Hierarchical Metacognitive Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/html/2510.15979"},{"title":"CP-Router: An Uncertainty-Aware Router Between LLM and LRM","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40589/44550"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and ...","url":"https://arxiv.org/pdf/2506.09033"},{"title":"[2510.15979] Cog-Rethinker: Hierarchical Metacognitive Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/abs/2510.15979"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.09033v1"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://arxiv.org/html/2506.09033v3"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://ulab-uiuc.github.io/Router-R1/"},{"title":"Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=DWf4vroKWJ"},{"title":"Paper page - Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning","url":"https://huggingface.co/papers/2506.09033"}]

Based on the search results, I found research related to LLM routing and reasoning with adaptive computation using reinforcement learning, though the specific term "CogRouter" with "CoPO" reinforcement learning wasn't directly found. Here are the most relevant results:

## Router-R1: Multi-Round LLM Routing via Reinforcement Learning

Router-R1 is a reinforcement learning (RL)-based framew
…[truncated 1453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-13T21:03:54.086720+00:00_

Web search results for query: ""death avoidance" "failure prevention" reinforcement learning reward decomposition penalty avoidance vs positive reward"

Links: [{"title":"Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/html/2306.13944"},{"title":"[2306.13944] Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/abs/2306.13944"},{"title":"Explainable Reinforcement Learning via Reward Decomposition","url":"https://web.engr.oregonstate.edu/~erwig/papers/ExplainableRL_XAI19.pdf"},{"title":"Avoiding Death through Fear Intrinsic Conditioning","url":"https://arxiv.org/html/2506.05529v1"},{"title":"Modular deep reinforcement learning from reward and punishment for robot navigation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0893608020304184"},{"title":"[1911.02166] Distributional Reward Decomposition for Reinforcement Learning","url":"https://arxiv.org/abs/1911.02166"},{"title":"Decomposition Methods with Deep Corrections for ...","url":"https://arxiv.org/pdf/1802.01772"},{"title":"Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications","url":"https://arxiv.org/html/2408.10215v1"},{"title":"Reward Machines: Exploiting Reward Function Structure in Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/357800313_Reward_Machines_Exploiting_Reward_Function_Structure_in_Reinforcement_Learning"},{"title":"Lecture 13: Reinforcement learning | MLVU","url":"https://mlvu.github.io/lecture13/"}]

Based on the search results, here's what I found regarding death avoidance, failure prevention, and reward decomposition in reinforcement learning:

## Death Avoidance and Intrinsic Conditioning

A central challenge in engineering reward functions comes from environments containing states that carry high negative rewards but provide no feedback to the agent, with death being one such stimulus that fa
…[truncated 1353 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-13T21:03:54.086948+00:00_

Web search results for query: "MTRouter ScienceWorld multi-turn LLM routing cost GPT 2025 2026"

Links: [{"title":"MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings","url":"https://arxiv.org/html/2604.23530"},{"title":"[2604.23530] MTRouter: Cost-Aware Multi-Turn LLM Routing with History-Model Joint Embeddings","url":"https://arxiv.org/abs/2604.23530"},{"title":"GitHub - ZhangYiqun018/MTRouter: [ACL 2026] Official implementation of MTRouter, a cost-aware multi-turn LLM routing framework accepted to ACL 2026 Main Conference. · GitHub","url":"https://github.com/ZhangYiqun018/MTRouter"},{"title":"GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub","url":"https://github.com/ulab-uiuc/LLMRouter"},{"title":"GMTRouter: Personalized LLM Router over Multi-turn User Interactions","url":"https://arxiv.org/html/2511.08590v1"},{"title":"Intelligent LLM Routing: How Multi-Model AI Cuts Costs by 85% — Swfte AI","url":"https://www.swfte.com/blog/intelligent-llm-routing-multi-model-ai"},{"title":"GitHub - lm-sys/RouteLLM: A framework for serving and evaluating LLM routers - save LLM costs without compromising quality · GitHub","url":"https://github.com/lm-sys/RouteLLM"},{"title":"RouteLLM: An Open-Source Framework for Cost-Effective LLM Routing - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2024-07-01-routellm/"},{"title":"RouteLLM: Learning to Route LLMs with Preference Data","url":"https://arxiv.org/html/2406.18665v3"},{"title":"[2511.08590] GMTRouter: Personalized LLM Router over Multi-turn User Interactions","url":"https://arxiv.org/abs/2511.08590"}]

Based on the search results, here's what I found about MTRouter, ScienceWorld, multi-turn LLM routing, and cost relative to GPT models:

## MTRouter Overview

MTRouter is a cost-aware multi-turn LLM routing framework accepted to the ACL 2026 Main Conference. It encodes the interaction history and candidate models into joint history-model embeddings, an
…[truncated 1008 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T21:03:54.087150+00:00_

Web search results for query: ""Where LLM Agents Fail" failure analysis agent benchmark 2025"

Links: [{"title":"WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES","url":"https://arxiv.org/pdf/2509.25370"},{"title":"[2509.25370] Where LLM Agents Fail and How They can Learn From Failures","url":"https://arxiv.org/abs/2509.25370"},{"title":"Which Agent Causes Task Failures and When? On ...","url":"https://arxiv.org/pdf/2505.00212"},{"title":"Where LLM Agents Fail And How They can Learn From Failures | OpenReview","url":"https://openreview.net/forum?id=PFR4E8583W"},{"title":"How Do LLMs Fail In Agentic Scenarios?","url":"https://arxiv.org/pdf/2512.07497"},{"title":"[2502.15865] Standard Benchmarks Fail -- Auditing LLM Agents in Finance Must Prioritize Risk","url":"https://arxiv.org/abs/2502.15865"},{"title":"How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis of Success and Failure Scenarios of Various LLMs in Agentic Simulations","url":"https://arxiv.org/html/2512.07497"},{"title":"Where LLM Agents Fail and How They can Learn From Failures | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.25370v1"},{"title":"Seeing the Whole Elephant: A Benchmark for Failure Attribution in LLM-based Multi-Agent Systems","url":"https://arxiv.org/html/2604.22708v1"},{"title":"TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks | OpenReview","url":"https://openreview.net/forum?id=LZnKNApvhG"}]

Based on the search results, I found comprehensive information about "Where LLM Agents Fail," a significant research work on LLM agent failure analysis:

## Key Findings

Large Language Model (LLM) agents, which integrate planning, memory, reflection, and tool-use modules, have shown promise in solving complex, multi-step tasks. Yet their sophisticated architectures amplify vulnerability to cascading failures, where a single root-cause error propagates through subsequent decisions, leading to task failure.

### Main Contributions

The research intr
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T21:03:54.087326+00:00_

Web search results for query: "ARES "adaptive routing" LLM reasoning "Mixture of Depths" compute allocation 2024 2025"

Links: [{"title":"ARES: Adaptive Reasoning Effort Selection for Efficient LLM Agents","url":"https://arxiv.org/pdf/2603.07915"},{"title":"Mixture-of-Recursions: Learning Dynamic Recursive Depths for Adaptive Token-Level Computation","url":"https://arxiv.org/html/2507.10524v1"},{"title":"ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping","url":"https://arxiv.org/html/2510.08457v1"},{"title":"Route to Reason: Adaptive Routing for LLM and Reasoning Strategy Selection","url":"https://arxiv.org/html/2505.19435v1"},{"title":"[2505.19435] Route to Reason: Adaptive Routing for LLM and Reasoning Strategy Selection","url":"https://arxiv.org/abs/2505.19435"},{"title":"Mixture-of-Recursions: A New Era of Adaptive Token-Level Computation in Transformers | by Santhosraj | Medium","url":"https://medium.com/@santhosraj14/mixture-of-recursions-a-new-era-of-adaptive-token-level-computation-in-transformers-43dd65f357b4"},{"title":"BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute | OpenReview","url":"https://openreview.net/forum?id=tFBIbCVXkG"},{"title":"GitHub - koayon/awesome-adaptive-computation: A curated reading list of research in Adaptive Computation, Inference-Time Computation & Mixture of Experts (MoE). · GitHub","url":"https://github.com/koayon/awesome-adaptive-computation"},{"title":"ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference","url":"https://arxiv.org/html/2602.23681"},{"title":"BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute","url":"https://arxiv.org/html/2506.22716v1"}]

Based on the search results, I found several relevant papers on adaptive routing and LLM reasoning. Here are the key findings:

## ARES Framework

ARES (Adaptive Reasoning Effort Selection) is a framework that dynamically allocates reasoning effort at each step. Unlike traditional model routing
…[truncated 1582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T21:03:54.087511+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Safe Reinforcement Learning with Dead-Ends\" avoidance recovery 2023 dead-end states catastrophic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Safe Reinforcement Learning with Dead-Ends\" avoidance recovery 2023 dead-end states catastrophic"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-13T21:03:54.087636+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ScienceWorld environment reward structure penalty task failure Wang 2022 interactive science"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ScienceWorld environment reward structure penalty task failure Wang 2022 interactive science"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T21:03:54.087753+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM agent \"error analysis\" \"failure mode\" tool invocation hallucination grounding error interactive environment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM agent \"error analysis\" \"failure mode\" tool invocation hallucination grounding error interactive environment"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T21:03:54.087867+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Dyna-Think\" OR \"SwiftSage\" LLM agent fast slow thinking deterministic module routing 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Dyna-Think\" OR \"SwiftSage\" LLM agent fast slow thinking deterministic module routing 2024"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-13T21:03:54.088024+00:00_

Web search results for query: "ScienceWorld environment reward structure penalty task failure Wang 2022 interactive science"

Links: [{"title":"(PDF) Reward Is Enough: LLMs Are In-Context Reinforcement Learners","url":"https://www.researchgate.net/publication/392530375_Reward_Is_Enough_LLMs_Are_In-Context_Reinforcement_Learners"},{"title":"GitHub - allenai/ScienceWorld: ScienceWorld is a text-based virtual environment centered around accomplishing tasks from the standardized elementary science curriculum. · GitHub","url":"https://github.com/allenai/ScienceWorld"},{"title":"Unleashing Embodied Task Planning Ability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2506.23127"},{"title":"[PDF] ScienceWorld: Is your Agent Smarter than a 5th Grader? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ScienceWorld:-Is-your-Agent-Smarter-than-a-5th-Wang-Jansen/0e41fd22d483047bd8fdb1757d90c7702493567e"},{"title":"[2203.07540] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://arxiv.org/abs/2203.07540"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? | Request PDF","url":"https://www.researchgate.net/publication/372924838_ScienceWorld_Is_your_Agent_Smarter_than_a_5th_Grader"},{"title":"SCIENCEWORLD: Is your Agent Smarter than a 5","url":"https://aclanthology.org/2022.emnlp-main.775.pdf"},{"title":"ScienceWorld: Is your Agent Smarter than a 5th Grader? - ACL Anthology","url":"https://aclanthology.org/2022.emnlp-main.775/"},{"title":"Knowledge-enhanced Agents for Interactive Text Games Prateek Chhikara","url":"https://arxiv.org/pdf/2305.05091"},{"title":"[Quick Review] ScienceWorld: Is your Agent Smarter than a 5th Grader?","url":"https://liner.com/review/scienceworld-is-your-agent-smarter-than-5th-grader"}]

Based on the search results, here's information about the ScienceWorld environment's reward structure and task failure penalties:

## Reward Structure

At each step, the agent observes the result of its ac
…[truncated 1045 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T21:03:54.088209+00:00_

Web search results for query: ""Safe Reinforcement Learning with Dead-Ends" avoidance recovery 2023 dead-end states catastrophic"

Links: [{"title":"Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/pdf/2306.13944"},{"title":"[2306.13944] Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://arxiv.org/abs/2306.13944"},{"title":"Safe Reinforcement Learning With Dead-Ends Avoidance and Recovery | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10319093/"},{"title":"1 Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery","url":"https://events.infovaya.com/uploads/documents/pdfviewer/d6/eb/135115-4706.pdf"},{"title":"Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery | Papers With Code","url":"https://paperswithcode.com/paper/safe-reinforcement-learning-with-dead-ends"},{"title":"Safety-oriented Reinforcement Learning","url":"https://www.emergentmind.com/topics/safety-oriented-reinforcement-learning-safe-rl"},{"title":"[2301.05664] Risk Sensitive Dead-end Identification in Safety-Critical Offline Reinforcement Learning","url":"https://arxiv.org/abs/2301.05664"},{"title":"Published in Transactions on Machine Learning Research (01/2023)","url":"https://openreview.net/pdf?id=oKlEOT83gI"},{"title":"State-wise safe reinforcement learning: a survey","url":"https://dl.acm.org/doi/10.24963/ijcai.2023/763"},{"title":"safe-reinforcement-learning-with-dead-ends-avoidance- ...","url":"https://scispace.com/pdf/safe-reinforcement-learning-with-dead-ends-avoidance-and-34dh6ttc.pdf"}]

I found relevant search results for your query. Here's what I found:

## Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery

The paper addresses safety as one of the main challenges in applying reinforcement learning to realistic environmental tasks. Existing methods tend to adopt overly conservative policy to avoid unsafe situations, but this severely hinde
…[truncated 1169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T21:03:54.088391+00:00_

Web search results for query: "LLM agent "error analysis" "failure mode" tool invocation hallucination grounding error interactive environment"

Links: [{"title":"LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions","url":"https://arxiv.org/html/2509.18970v1"},{"title":"LLM Behavioral Failure Modes: 12 Failure Patterns and the Defense Map","url":"https://ceaksan.com/en/llm-behavioral-failure-modes"},{"title":"LLM Agentic Failure Modes: Task Drift, Reward Hacking, Alignment Faking and More","url":"https://ceaksan.com/en/llm-agentic-failure-modes"},{"title":"Building AI Agents That Don't Break in Production","url":"https://labs.adaline.ai/p/building-ai-agents-that-dont-break-in-production"},{"title":"Why Multi-Agent LLM Systems Fail & How to Fix Them","url":"https://redis.io/blog/why-multi-agent-llm-systems-fail/"},{"title":"AI SRE Hallucination Guardrails: 4 Engineering Fixes - Neubird","url":"https://neubird.ai/blog/ai-sre-hallucination-guardrails/"},{"title":"LLM hallucinations and failures: lessons from 5 examples","url":"https://www.evidentlyai.com/blog/llm-hallucination-examples"},{"title":"How Do LLMs Fail In Agentic Scenarios?","url":"https://docs.kamiwaza.ai/assets/files/How_do_LLMs_fail_in_agentic_scenarios-eff27cdb81518717588e1fcdee00aec4.pdf"},{"title":"Where LLM Agents Fail and How They can Learn From Failures | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.25370v1"},{"title":"Detecting AI Agent Failure Modes in Production: A Framework for Observability-Driven Diagnosis | Latitude","url":"https://latitude.so/blog/ai-agent-failure-detection-guide"}]

Here are the search results for your query about LLM agent error analysis, failure modes, tool invocation, hallucination, and grounding errors in interactive environments:

## Key Findings

**Hallucination and Tool Invocation Failures**

LLM-based agents are typically trained with insufficient exposure to diverse and complex tool-use scenarios, making them prone
…[truncated 1810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T21:03:54.088593+00:00_

Web search results for query: ""Dyna-Think" OR "SwiftSage" LLM agent fast slow thinking deterministic module routing 2024"

Links: [{"title":"SwiftSage | AI2","url":"https://swiftsage.github.io/"},{"title":"GitHub - SwiftSage/SwiftSage: SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks · GitHub","url":"https://github.com/yuchenlin/swiftsage/"},{"title":"SWIFTSAGE: A Generative Agent with Fast and Slow ...","url":"https://openreview.net/pdf?id=Rzk3GP1HN7"},{"title":"Dyna-Think: Synergizing Reasoning, Acting, and World Model Simulation in AI Agents","url":"https://arxiv.org/html/2506.00320v1"},{"title":"SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks | OpenReview","url":"https://openreview.net/forum?id=Rzk3GP1HN7"},{"title":"[2305.17390] SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks","url":"https://arxiv.org/abs/2305.17390"},{"title":"(PDF) SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks","url":"https://www.researchgate.net/publication/371136862_SwiftSage_A_Generative_Agent_with_Fast_and_Slow_Thinking_for_Complex_Interactive_Tasks"},{"title":"Shiyu Huang (黄世宇) Haidian District, Beijing, China, 100084 huangsy1314@163.com","url":"http://tartrl.cn/download/local/?filename=CV.pdf"},{"title":"How Should We Maximize the Planning Ability of LLMs While Reducing the Computation Cost? Meet SwiftSage: A Novel Generative Agent for Complex Interactive Reasoning Tasks, Inspired by the Dual-Process Theory of Human Cognition - MarkTechPost","url":"https://www.marktechpost.com/2023/06/03/how-should-we-maximize-the-planning-ability-of-llms-while-reducing-the-computation-cost-meet-swiftsage-a-novel-generative-agent-for-complex-interactive-reasoning-tasks-inspired-by-the-dual-process/"},{"title":"GitHub - yxf203/Awesome-Efficient-Agents: Survey and paper list on efficiency-guided LLM agents (memory, tool learning, planning). · Git
…[truncated 2723 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T21:03:54.088777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Avoiding Death through Fear\" intrinsic conditioning reinforcement learning terminal states 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Avoiding Death through Fear\" intrinsic conditioning reinforcement learning terminal states 2025"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T21:03:54.088902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Towards Verifiably Safe Tool Use\" LLM agents safety verification 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Towards Verifiably Safe Tool Use\" LLM agents safety verification 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-13T21:03:54.089037+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SwiftSage ScienceWorld performance score results dual process agent 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SwiftSage ScienceWorld performance score results dual process agent 2023"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-13T21:03:54.089156+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM agent \"negative reward\" \"penalty avoidance\" benefit decomposition tool use \"where does the benefit come from\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM agent \"negative reward\" \"penalty avoidance\" benefit decomposition tool use \"where does the benefit come from\""
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-13T21:03:54.089296+00:00_

Web search results for query: ""Towards Verifiably Safe Tool Use" LLM agents safety verification 2025"

Links: [{"title":"[2601.08012] Towards Verifiably Safe Tool Use for LLM Agents","url":"https://arxiv.org/abs/2601.08012"},{"title":"Towards Verifiably Safe Tool Use for LLM Agents","url":"https://arxiv.org/html/2601.08012"},{"title":"Towards Verifiably Safe Tool Use for LLM Agents Aarya Doshi","url":"https://arxiv.org/pdf/2601.08012"},{"title":"Llm Agents Achieve Verifiably Safe Tool Use, Mitigating Data Leaks And System Risks","url":"https://quantumzeitgeist.com/llm-agents-verifiably-safe-tool/"},{"title":"Towards Verifiably Safe Tool Use for LLM Agents - CMU School of ...","url":"https://www.cs.cmu.edu/~ckaestne/pdf/icsenier16.pdf"},{"title":"Towards Verifiably Safe Tool Use for LLM Agents (ICSE 2026 - New Ideas and Emerging Results (NIER)) - ICSE 2026","url":"https://conf.researchr.org/details/icse-2026/icse-2026-nier/41/Towards-Verifiably-Safe-Tool-Use-for-LLM-Agents"},{"title":"Eunsuk Kang's research works | Carnegie Mellon University and other places","url":"https://www.researchgate.net/scientific-contributions/Eunsuk-Kang-2152208722"}]

Based on the search results, here's what I found about "Towards Verifiably Safe Tool Use for LLM Agents":

## Overview

This is a paper by Aarya Doshi and 5 other authors that addresses how large language model (LLM)-based AI agents can safely use tools such as data sources, APIs, search engines, code sandboxes, and even other agents.

## The Problem

While tool use empowers agents to perform complex tasks, LLMs may invoke unintended tool interactions and introduce risks, such as leaking sensitive data or overwriting critical records, which are unacceptable in enterprise contexts. Current model-based safeguards enhance reliability but cannot guarantee system safety, and methods like information flow control (IFC) and temporal constraints aim to provide guarantees but often require extensive human annotation.

## The Proposed
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T21:03:54.089455+00:00_

Web search results for query: ""Avoiding Death through Fear" intrinsic conditioning reinforcement learning terminal states 2025"

Links: [{"title":"[2506.05529] Avoiding Death through Fear Intrinsic Conditioning","url":"https://arxiv.org/abs/2506.05529"},{"title":"Avoiding Death through Fear Intrinsic Conditioning","url":"https://arxiv.org/html/2506.05529v1"},{"title":"Combating Deep Reinforcement Learning's Sisyphean Curse with Intrinsic Fear | OpenReview","url":"https://openreview.net/forum?id=r1tHvHKge"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=0&show=2000"},{"title":"(PDF) Combating Reinforcement Learning's Sisyphean Curse with Intrinsic Fear","url":"https://www.researchgate.net/publication/324387231_Combating_Reinforcement_Learning's_Sisyphean_Curse_with_Intrinsic_Fear"},{"title":"Fear based Intrinsic Reward as a Barrier Function for ...","url":"https://par.nsf.gov/servlets/purl/10601093"},{"title":"[1611.01211] Combating Reinforcement Learning's Sisyphean Curse with Intrinsic Fear","url":"https://arxiv.org/abs/1611.01211"},{"title":"Combating Reinforcement Learning's Sisyphean Curse with Intrinsic Fear | DeepAI","url":"https://deepai.org/publication/combating-reinforcement-learning-s-sisyphean-curse-with-intrinsic-fear"},{"title":"Computational modeling of threat learning reveals links with anxiety and neuroanatomy in humans | eLife","url":"https://elifesciences.org/articles/66169"},{"title":"Biologically based neural circuit modelling for the study of fear learning and extinction | npj Science of Learning","url":"https://www.nature.com/articles/npjscilearn201615"}]

Based on the search results, I found relevant information about this topic. The most recent paper matching your query is:

## "Avoiding Death through Fear Intrinsic Conditioning" (2025)

This work introduces an intrinsic reward function inspired by early amygdala development and produces this intrinsic reward through a novel memory-augmented 
…[truncated 1119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-13T21:03:54.089615+00:00_

Web search results for query: "SwiftSage ScienceWorld performance score results dual process agent 2023"

Links: [{"title":"[2305.17390] SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks","url":"https://arxiv.org/abs/2305.17390"},{"title":"SWIFTSAGE: A Generative Agent with Fast and Slow ...","url":"https://arxiv.org/pdf/2305.17390"},{"title":"SwiftSage | AI2","url":"https://swiftsage.github.io/"},{"title":"SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks | OpenReview","url":"https://openreview.net/forum?id=Rzk3GP1HN7"},{"title":"SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230517390Y/abstract"},{"title":"SWIFTSAGE: a generative agent with fast and slow thinking ...","url":"https://dl.acm.org/doi/10.5555/3666122.3667156"},{"title":"[2305.17390v1] SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks","url":"https://arxiv.org/abs/2305.17390v1"},{"title":"(PDF) SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks","url":"https://www.researchgate.net/publication/371136862_SwiftSage_A_Generative_Agent_with_Fast_and_Slow_Thinking_for_Complex_Interactive_Tasks"},{"title":"How Should We Maximize the Planning Ability of LLMs While Reducing the Computation Cost? Meet SwiftSage: A Novel Generative Agent for Complex Interactive Reasoning Tasks, Inspired by the Dual-Process Theory of Human Cognition - MarkTechPost","url":"https://www.marktechpost.com/2023/06/03/how-should-we-maximize-the-planning-ability-of-llms-while-reducing-the-computation-cost-meet-swiftsage-a-novel-generative-agent-for-complex-interactive-reasoning-tasks-inspired-by-the-dual-process/"},{"title":"SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks","url":"https://arxiv.org/html/2305.17390v2"}]

Based on the search results, here's 
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T21:03:54.089781+00:00_

Web search results for query: "LLM agent "negative reward" "penalty avoidance" benefit decomposition tool use "where does the benefit come from""

Links: [{"title":"ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents","url":"https://arxiv.org/html/2603.01620v3"},{"title":"[2502.10325] Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/abs/2502.10325"},{"title":"Process Reward Models for LLM Agents: Practical Framework and Directions","url":"https://arxiv.org/html/2502.10325v1"},{"title":"Towards Socially and Morally Aware RL agent: Reward Design With LLM","url":"https://arxiv.org/html/2401.12459"},{"title":"Empowering LLM Tool Invocation with Tool-call Reward Model | OpenReview","url":"https://openreview.net/forum?id=LnBEASInVr"},{"title":"From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models","url":"https://arxiv.org/html/2604.09459v1"},{"title":"A Simple Framework for Intrinsic Reward-Shaping for RL using LLM Feedback","url":"https://alexzhang13.github.io/assets/pdfs/Reward_Shaping_LLM.pdf"},{"title":"Scaling Autonomous Agents via Automatic Reward Modeling And Planning | OpenReview","url":"https://openreview.net/forum?id=womU9cEwcO"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"Planner-R1: Reward Shaping Enables Efficient Agentic RL with Smaller LLMs","url":"https://arxiv.org/html/2509.25779v2"}]

Based on the web search results, I found relevant research on reward decomposition, penalty avoidance, and tool use in LLM agents. Here are the key findings:

## Reward Decomposition and Penalty Avoidance in Tool-Integrated LLM Agents

### ToolRLA Framework

A multiplicative composition approach decomposes reward into tool-name, coverage, and parameter accuracy sub-scores, where a wrong tool selection collapses correctness regardless of parameter quality. A large negative complia
…[truncated 1688 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-13T21:03:54.089958+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BEACON ScienceWorld reinforcement learning LLM agent trajectory-level optimization 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BEACON ScienceWorld reinforcement learning LLM agent trajectory-level optimization 2024"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-13T21:03:54.090104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"input-adaptive\" LLM computation allocation routing ScienceWorld ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"input-adaptive\" LLM computation allocation routing ScienceWorld ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-13T21:03:54.090219+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "constrained MDP safe reinforcement learning \"avoid catastrophe\" \"catastrophic state\" irreversible failure agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "tool_args": {
    "query": "constrained MDP safe reinforcement learning \"avoid catastrophe\" \"catastrophic state\" irreversible failure agent"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-13T21:03:54.090359+00:00_

Web search results for query: "BEACON ScienceWorld reinforcement learning LLM agent trajectory-level optimization 2024"

Links: [{"title":"GitHub - tmgthb/Autonomous-Agents: Autonomous Agents (LLMs) research papers. Updated Daily. · GitHub","url":"https://github.com/tmgthb/Autonomous-Agents"},{"title":"Milestone-Guided Policy Learning for Long-Horizon Language Agents","url":"https://arxiv.org/html/2605.06078"},{"title":"GitHub - Yifan-Song793/ETO: Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents (ACL 2024 Main Conference) · GitHub","url":"https://github.com/Yifan-Song793/ETO"},{"title":"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents | alphaXiv","url":"https://www.alphaxiv.org/overview/2403.02502v2"},{"title":"Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning","url":"https://arxiv.org/html/2511.14460v1"},{"title":"EPO: Entropy-regularized Policy Optimization for LLM Agents Reinforcement Learning","url":"https://arxiv.org/html/2509.22576v1"},{"title":"Unleashing Interactive Agent Planning Ability in LLMs via Multi-Trajectory Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=5ZXCFetbyW"},{"title":"Reinforcement Learning for LLM Agent Planning","url":"https://aclanthology.org/2025.emnlp-industry.116.pdf"},{"title":"[Quick Review] Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents","url":"https://liner.com/review/trial-and-error-explorationbased-trajectory-optimization-for-llm-agents"},{"title":"Trial and Error: Exploration-Based Trajectory Optimization of LLM Agents - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.409/"}]

Based on the search results, here's what I found about BEACON and trajectory-level optimization for LLM agents:

## BEACON: Milestone-Guided Policy Learning

BEACON is a milestone-guided policy learning framework that leverages the compositional structure of long-horizon tasks to ensure precise credit assignment
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-13T21:03:54.090523+00:00_

Web search results for query: ""input-adaptive" LLM computation allocation routing ScienceWorld ICLR 2025"

Links: [{"title":"INPUT-ADAPTIVE ALLOCATION OF LM COMPUTATION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ff414825df833edb8b1839e3d5d495e9-Paper-Conference.pdf"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation | OpenReview","url":"https://openreview.net/forum?id=6qUUgw9bAZ"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b3f0556612685c076269f91b2129334f-Paper-Conference.pdf"},{"title":"ICLR 2025 Orals","url":"https://iclr.cc/virtual/2025/events/oral"},{"title":"ICLR 2025 Schedule","url":"https://iclr.cc/virtual/2025/calendar"},{"title":"ICLR 2025 Papers","url":"https://iclr.cc/virtual/2025/papers.html"},{"title":"ICLR 2025 Workshop on Sparsity in LLMs (SLLM) FASTER, CHEAPER, JUST AS GOOD:","url":"http://minlanyu.seas.harvard.edu/writeup/sllm25-score.pdf"},{"title":"ICML Poster BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute","url":"https://icml.cc/virtual/2025/poster/43788"},{"title":"ICLR 2025 Workshop LLM Reason and Plan | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2025%2FWorkshop%2FLLM_Reason_and_Plan"},{"title":"Learning How Hard to Think: Input-Adaptive Allocation of LM Computation | Andi Peng","url":"https://andipeng.com/publication/2025-iclr-adaptivecompute/"}]

The search has found relevant results about input-adaptive computation allocation for language models presented at ICLR 2025. Here's what I found:

## Main Research Paper

The work presents a framework for adaptively scaling test-time LM computation, a learned model for estimating the marginal benefit of additional computation in LM decoding, an efficient algorithm for allocating computation to queries, and experiments demonstrating significant improvements in LM efficiency and output quality.

## Key Approach

The approach predicts the d
…[truncated 1167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-13T21:03:54.090694+00:00_

Web search results for query: "constrained MDP safe reinforcement learning "avoid catastrophe" "catastrophic state" irreversible failure agent"

Links: [{"title":"A Survey of Safe Reinforcement Learning and Constrained MDPs: A Technical Survey on Single-Agent and Multi-Agent Safety","url":"https://arxiv.org/html/2505.17342v1"},{"title":"State-wise Safe Reinforcement Learning: A Survey","url":"https://www.ijcai.org/proceedings/2023/0763.pdf"},{"title":"State-wise Constrained Policy Optimization","url":"https://arxiv.org/html/2306.12594"},{"title":"State-wise Safe Reinforcement Learning: A Survey","url":"https://arxiv.org/html/2302.03122"},{"title":"Safety-oriented Reinforcement Learning","url":"https://www.emergentmind.com/topics/safety-oriented-reinforcement-learning-safe-rl"},{"title":"RL Constraints That Still Let Unsafe Policies Through | by Nexumo | Mar, 2026 | Medium","url":"https://medium.com/@Nexumo_/rl-constraints-that-still-let-unsafe-policies-through-663b447824b7"},{"title":"[2302.03122] State-wise Safe Reinforcement Learning: A Survey","url":"https://ar5iv.labs.arxiv.org/html/2302.03122"},{"title":"Safe Reinforcement Learning for Constrained Markov Decision Processes with Stochastic Stopping Time","url":"https://arxiv.org/html/2403.15928"},{"title":"SB-TRPO: Towards Safe Reinforcement Learning with Hard Constraints","url":"https://arxiv.org/html/2512.23770"},{"title":"Safe Reinforcement Learning in Constrained Markov ...","url":"https://realworldml.github.io/files/cr/24_SNO_MDP_paper.pdf"}]

I've performed the web search on constrained MDPs in safe reinforcement learning with a focus on avoiding catastrophic states and irreversible failures. Here are the key findings:

## Core Framework

A common framework for Safe RL is the Constrained Markov Decision Process (CMDP) introduced by Altman (1999), in which an agent seeks to maximize expected return subject to one or more constraints (e.g., bounds on certain costs or probabilities of unsafe events).

## Cata
…[truncated 1727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-13T21:03:54.090947+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "ideas.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "ideas.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-13T21:03:54.091125+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'simgate-modular-routing'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-13T21:03:54.091248+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "simgate-modular-routing",
  "file": "memory.md",
  "max_chars": "6000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "simgate-modular-routing",
    "file": "memory.md",
    "max_chars": "6000"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-13T21:03:54.091409+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md\", \"content\": \"## Phase 1 MVP 最终结论 (2026-05-13)\\n\\n### Verdict: PASS (4/5 tasks 显著正向)\\n\\nPhase 1 验证了 fork-based deterministic evaluation 在 ScienceWorld 上显著优于纯 LLM 内部推理。\\n\\n### 关键设计决策与教训\\n\\n1. **Tie-break 策略**: `>` (strict) 而非 `>=`。95%+ 步骤 score_delta=0（稀疏奖励），`>=` 会让 oracle 退化为 always-internal。\\n\\n2. **Death filter 只用于有 fork 的模式**: always-internal 是纯 LLM baseline，不能调 fork/is_lethal。\\n\\n3. **melt 与 change-state internal 分数巧合相同**: 共享 environment variations，不是数据重复。\\n\\n4. **vLLM 兼容性**: torch 2.10.0 + vLLM 0.18.1 需注释 select_algorithm.py 1695/2164 行。\\n\\n5. **phase1_signal.py 不支持 --seed 参数**。\\n\\n### 竞品对标\\n- CogRouter (arXiv 2602.12662): Qwen2.5-7B, Score=84.6, SR=72.0%。路由 thinking depth（4 levels）。\\n- ITP-R (arXiv 2601.08955): Learned WM + K-head gating, SR=63.91%。WM 有 compounding error。\\n\\n## ⚠️ 核心发现：Det 优势几乎完全来自死亡回避 (2026-05-13)\\n\\n### Death rate 分析\\n\\n| 数据集 | I_death | D_death | Δ(D-I) | Δ_no_death |\\n|--------|---------|---------|--------|------------|\\n| Prescreening (8 tasks) | 48.6% | 5.4% | +43.9 | **-4.5** |\\n| MVP (5 tasks) | 41.0% | 12.0% | +29.2 | **-0.4** |\\n\\n**排除死亡 episode 后 det 反而略差于 internal。** Det 全部优势来自 death filter 阻止致命动作（\\\"focus on 错误对象\\\" → -100），不是推理质量更好。\\n\\n### 对 Paper Framing 的影响\\n- 原 framing \\\"det improves agent performance\\\" 需调整\\n- 实际机制：fork-based safety gate（检测并阻止致命动作）\\n- 更可防御的 claim：\\\"selective routing prevents catastrophic failures\\\"\\n- Router 应学到\\\"有风险时走 det，安全时走 internal\\\"\\n\\n### SFT 数据 class imbalance\\n- MVP 3 tasks 后处理：750 SFT triples，全标 \\\"deterministic\\\"（0 个 internal wins）\\n- 原因：包含 death 的 episode det 必赢；no-death episode 多为 tie\\n- 需要 step-level death risk features 而非 episode-level labels\\n\\n## Labeling 策略演进 (2026-05-13)\\n\\n### 1-step labeling → 不可行（tie rate 98.2%）\\n### Episode-terminal (K=10) → Director 取消（成本太高，78h 双卡）\\n### Plan 
…[truncated 1628 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-13T21:03:54.091600+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-13T21:03:54.091726+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-13T21:03:54.091852+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-13T21:03:54.091965+00:00_

death_aware_labeling.py
diagnosis_mvp-p1-gpu1-v2.md
dream_reports
phase1_progress_report.md
plan_001b_task_selection.md
router_sft_train.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-13T21:03:54.092143+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/literature_survey_death_avoidance.md",
  "content": "# 文献调研：LLM Agent Catastrophic Failure / Death Avoidance 机制\n\n**日期**: 2026-05-13\n**目的**: 调研是否有论文发现过类似 \"deterministic computation 的优势主要来自 death avoidance\" 的现象\n\n---\n\n## 一、直接相关论文（ScienceWorld 上的 Agent 方法）\n\n### 1. SwiftSage (Lin et al., NeurIPS 2023)\n- **标题**: SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks\n- **Venue**: NeurIPS 2023\n- **ScienceWorld 成绩**: 84.7 avg score（SOTA at the time）\n- **与我们的关系**: 最直接的架构类比——Swift（小模型行为克隆）+ Sage（GPT-4 慢思考）的双模块路由。Sage 模块在 Swift 失败时介入，本质上也是一种 failure recovery 机制。但 **没有量化分析** fast/slow 切换的收益来自 failure avoidance vs positive guidance。\n- **定位**: 互补/背景。SwiftSage 证明了双模块路由在 ScienceWorld 上有效，但没做我们的 decomposition 分析。\n\n### 2. CogRouter (arXiv 2602.12662)\n- **ScienceWorld 成绩**: Score=84.6, SR=72.0%\n- **方法**: Qwen2.5-7B，路由 thinking depth（4 levels），用 CoPO (RL) 训练\n- **与我们的关系**: 路由 thinking depth 而非 internal/deterministic modality。没有 death avoidance 分析，没有 counterfactual decomposition。\n- **定位**: 背景/对标。不同路由维度，不竞争。\n\n### 3. ITP-R (arXiv 2601.08955)\n- **ScienceWorld 成绩**: SR=63.91%（低于 CogRouter）\n- **方法**: Learned world model + K-head gating\n- **与我们的关系**: 路由到 approximate LLM world model（而非 deterministic simulator），有 compounding error 问题。没有 death avoidance 分析。\n- **定位**: 背景。说明 approximate world model 不如 exact simulation。\n\n### 4. MTRouter (Zhang et al., ACL 2026)\n- **标题**: MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings\n- **ScienceWorld 成绩**: 53.8 avg（超过 GPT-5 的 48.4，成本降 58.7%）\n- **与我们的关系**: 多模型路由（不同 LLM 之间），非 LLM vs deterministic 路由。但在 ScienceWorld 上有结果，是 routing 方向的 concurrent work。\n- **定位**: 背景。不同路由目标（cost-aware multi-model vs safety-aware modality）。\n\n### 5. BEACON (Milestone-Guided Policy Learning, 2025-2026)\n- **方法**: Trajectory-level RL，milestone-based credit assignment\n- **与我们的关系**: 解决 credit misattribution 问题（正确的早期动作被 terminal failure 惩罚）。与我们的发现呼应——ScienceWorld 的稀疏奖励导致 credit assignment 困难。但关注 RL 训练效率，非 routing。\n- **定位**: 互补。他们的 credit misattribution 问题正是我们的 death-dominated signal 的另一面。\n\n### 6. ScienceWorld 原始论文 (Wang et al., EMNLP 2022)\n- **标题**: ScienceWorld: Is your Agent Smarter than a 5th Grader?\n- **奖励结构**: 完成所有 subgoals = 100 分，稀疏奖励（多数步骤 reward=0）。\n- **关于 -100 penalty**: 搜索未找到原始论文明确讨论 -100 death penalty 的设计意图。需要直接查看源码确认 penalty 结构。\n- **定位**: 基础背景。\n\n---\n\n## 二、Tool Use Learning 文献\n\n### 7. Toolformer (Schick et al., NeurIPS 2023)\n- **方法**: Self-supervised tool-use learning，通过 API call insertion + loss reduction filtering\n- **与我们的关系**: 标准 tool-use learning baseline。差异：(1) 我们用 environment forking 做 hindsight counterfactual labeling（不是 self-supervised），(2) 我们的 framing 是 safety-aware（不是 general tool selection）。\n- **定位**: 背景，必须引用并明确区分。\n\n### 8. ReTool (ICLR 2026)\n- **标题**: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- **方法**: RL 训练 LLM 学习 when/how 调用 code interpreter，outcome-driven reward\n- **与我们的关系**: 最接近的 \"when to invoke tool\" 工作。差异：(1) implicit routing（entangled with backbone），我们用 explicit modular router；(2) 没做 benefit decomposition（failure avoidance vs positive guidance）。\n- **定位**: 互补/部分竞争。我们的 decomposition 分析是他们缺失的。\n\n### 9. ToolRLA (2026)\n- **标题**: ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents\n- **方法**: 将 tool invocation reward 分解为 tool-name / coverage / parameter accuracy sub-scores\n- **与我们的关系**: 做了 reward decomposition，但维度不同（tool selection accuracy vs death avoidance mechanism）。他们分解的是\"哪个维度的 tool use 做得好\"，我们分解的是\"tool use 的收益来自哪种机制\"。\n- **定位**: 互补。方法论上有呼应（都在做 decomposition），但分析维度完全不同。\n\n---\n\n## 三、LLM Agent Safety / Failure Analysis\n\n### 10. Check Yourself Before You Wreck Yourself (Kumaraguru et al., NeurIPS 2025 Workshop)\n- **方法**: Prompting LLM agent 在不确定时主动 quit，在 ToolEmu 上评估\n- **与我们的关系**: **最接近我们 \"death avoidance\" framing 的工作**。他们的 \"selective quitting\" 本质上是 death avoidance 的一种形式——识别高风险场景并退出。差异：(1) 他们用 prompting，我们用 learned router；(2) 他们的 quitting 是放弃任务，我们的 routing 是切换到更安全的 modality（仍完成任务）。\n- **定位**: **高度相关，必须引用**。我们的 router 可以理解为 \"selective quitting from LLM reasoning, switching to deterministic computation\" 而非完全放弃。\n\n### 11. SafeHarbor (arXiv 2605.05704, 2026)\n- **方法**: Hierarchical memory-augmented guardrail for LLM agent safety\n- **与我们的关系**: Agent safety guardrail，但关注 policy compliance / harmful action prevention，非 task-level catastrophic failure。\n- **定位**: 背景（safety 大方向）。\n\n### 12. Towards Verifiably Safe Tool Use for LLM Agents (Doshi et al., ICSE 2026)\n- **方法**: STPA + capability-enhanced MCP framework，formal safety specification\n- **与我们的关系**: 形式化 tool safety，但面向 enterprise scenarios（data leak, record overwrite），非 interactive environment 的 catastrophic failure。\n- **定位**: 背景（broader safety context）。\n\n### 13. Where LLM Agents Fail and How They Can Learn From Failures (2025)\n- **方法**: AgentErrorTaxonomy + AgentErrorBench + AgentDebug\n- **环境**: ALFWorld, GAIA, WebShop\n- **与我们的关系**: Failure taxonomy 和 debugging framework。分类了 agent failure modes 但没有量化 \"failure avoidance vs positive performance\" 的分解。\n- **定位**: 背景。我们的 death avoidance finding 可以看作是他们 taxonomy 中一种特定 failure mode 的量化分析。\n\n### 14. How Do LLMs Fail In Agentic Scenarios? (2025)\n- **方法**: Qualitative analysis of success/failure scenarios\n- **与我们的关系**: Failure mode 分析但定性为主，没有量化 decomposition。\n- **定位**: 背景。\n\n### 15. Agent-SafetyBench\n- **方法**: Evaluating LLM agent safety across multiple risk dimensions\n- **与我们的关系**: Safety benchmark，面向 harmful action prevention 而非 task performance decomposition。\n- **定位**: 远景背景。\n\n---\n\n## 四、Safe RL 文献\n\n### 16. Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery (RA-L / ICRA 2024)\n- **方法**: 学习 optimal boundary 区分 safe/unsafe states，pretrain recovery policy + safety critic\n- **与我们的关系**: **概念上最接近的 Safe RL 工作**。他们的 \"dead-end states\"（无论什么 policy 都必然失败的状态）= 我们的 \"death states\"。他们的 safety critic = 我们的 router-as-death-detector。差异：(1) 他们在 continuous control（robotics），我们在 text-based interactive environments；(2) 他们训练 recovery policy，我们切换 computation modality。\n- **定位**: **重要背景，建议引用**。建立 \"death avoidance as a routing mechanism\" 与 Safe RL 的联系。\n\n### 17. Combating RL's Sisyphean Curse with Intrinsic Fear (Lipton et al., 2016)\n- **方法**: 学习 fear model 预测 imminent catastrophe probability，用于 penalize Q-learning\n- **与我们的关系**: 早期 \"death avoidance\" 工作。他们发现 DRL agents 会周期性地重新访问 catastrophic states（Sisyphean curse）。我们的 router 本质上也是一个 fear model——预测 \"这一步用 LLM 内部推理是否会导致 catastrophe\"。\n- **定位**: 互补/理论背景。\n\n### 18. Avoiding Death through Fear Intrinsic Conditioning (Sanchez et al., 2025)\n- **方法**: 生物启发的 amygdala-like memory network，intrinsic reward for death avoidance\n- **与我们的关系**: 最新的 death avoidance RL 工作，使用 memory-augmented network 学习 \"fear\"。与我们的 router 在功能上类似（都在学 death prediction），但方法完全不同。\n- **定位**: 背景。\n\n### 19. Constrained MDP / State-wise Safe RL (Garcia & Fernandez, JMLR 2015; 多篇 survey)\n- **核心框架**: CMDP with safety constraints，state-wise constraint satisfaction\n- **与我们的关系**: 我们的 router 可以看作一种 state-wise safety mechanism——在每个 state 决定是否切换到 \"safe\" (deterministic) modality。但我们不是在 CMDP 框架下优化，而是用 counterfactual labeling + SFT。\n- **定位**: 理论背景。可以在 Related Work 中简短提及 \"our router can be viewed as a learned state-wise safety gate\"。\n\n---\n\n## 五、Adaptive Computation / Routing\n\n### 20. Learning How Hard to Think (ICLR 2025)\n- **方法**: Input-adaptive compute allocation, learned marginal benefit estimator\n- **与我们的关系**: Compute allocation 方向，但面向 decoding budget（best-of-k, routing to expensive vs cheap decoder），非 modality routing。\n- **定位**: 远景背景。\n\n### 21. ARES: Adaptive Reasoning Effort Selection (2026)\n- **方法**: Lightweight router 预测 optimal reasoning effort level\n- **与我们的关系**: Intra-model thinking level routing，非 inter-modality routing。\n- **定位**: 背景。\n\n### 22. Router-R1 (2025-2026)\n- **方法**: RL-based multi-LLM routing with think + route actions\n- **与我们的关系**: Multi-model routing via RL。差异：multi-model（不同 LLM）vs single-modality（LLM vs deterministic）。\n- **定位**: 背景。\n\n---\n\n## 六、核心问题回答\n\n### Q1: \"99% death avoidance\" finding 是否有先例？\n\n**没有直接先例。** 没有找到任何论文量化过 \"tool invocation / modality routing 的收益中，failure prevention vs positive guidance 各占多少\"。\n\n最接近的工作：\n- **Intrinsic Fear** (Lipton 2016) 和 **Dead-Ends Avoidance** (ICRA 2024) 在 Safe RL 中研究了 death/catastrophe avoidance，但没有做 \"benefit decomposition\"（将 routing/tool-use 收益分解为 death avoidance vs positive improvement）。\n- **\"Check Yourself\"** (NeurIPS 2025 WS) 提出 selective quitting 提升 safety，但没有量化 quitting 的收益有多少来自 catastrophe prevention vs 其他。\n- **ToolRLA** (2026) 做了 reward decomposition，但分解维度是 tool-selection accuracy，不是 failure prevention mechanism。\n- **SwiftSage** 有 fast/slow 路由但没分析路由收益的来源。\n\n**我们的 \"~93% death avoidance dominance\" 发现是 novel 的。**\n\n### Q2: 论文中应该引用的相关工作\n\n**必须引用（Related Work 段落）**:\n1. **SwiftSage** (Lin et al., 2023) — 最接近的 ScienceWorld 双模块路由\n2. **Toolformer** (Schick et al., 2023) — Tool-use learning baseline\n3. **ReTool** (ICLR 2026) — When to use tools via RL\n4. **\"Check Yourself\"** (2025) — LLM agent selective quitting for safety\n5. **Dead-Ends Avoidance** (ICRA 2024) — Safe RL dead-end detection\n6. **Intrinsic Fear** (Lipton et al., 2016) — Death avoidance in RL\n7. **ScienceWorld** (Wang et al., EMNLP 2022) — 环境\n8. **ReAct** (Yao et al., 2023) — Agent baseline\n9. **CogRouter** — ScienceWorld routing baseline\n10. **ITP-R** — World model routing baseline\n\n**建议引用（单句提及）**:\n11. **MTRouter** (ACL 2026) — ScienceWorld 上的 concurrent routing work\n12. **BEACON** — Trajectory-level RL on ScienceWorld\n13. **Garcia & Fernandez** (JMLR 2015) — Safe RL survey（CMDP framework）\n14. **Where LLM Agents Fail** (2025) — Agent failure taxonomy\n15. **ToolRLA** (2026) — Reward decomposition for tool use\n\n### Q3: Novelty claim 是否安全？\n\n**安全，但需要精确表述。**\n\n我们的 novelty 有两层：\n1. **Empirical finding（强 novelty）**: 首次量化 \"modality routing 的收益 decomposition\"——在 ScienceWorld 上 ~93% 来自 death avoidance。没有任何论文做过类似分解。\n2. **Methodology（中等 novelty）**: Episode-level counterfactual labeling 解决了 per-step oracle 在稀疏奖励下退化的问题（98% tie rate）。这个方法论是 specific to sparse-reward interactive environments 的贡献。\n\n**潜在攻击面**:\n- \"Death avoidance is trivial — just always use deterministic\" → 回应：我们的贡献是 finding，不是 routing method。Always-det 确实是强 baseline，这正是 finding 的一部分。\n- \"This is just Safe RL\" → 回应：Safe RL 研究 death avoidance 但在 continuous control；我们在 LLM agent + text environment 中首次展示 death avoidance 主导 routing signal。\n- \"Check Yourself already showed this\" → 回应：他们的 quitting 是放弃任务，我们切换 modality 继续完成任务；他们没有 benefit decomposition。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/literature_survey_death_avoidance.md",
    "content": "# 文献调研：LLM Agent Catastrophic Failure / Death Avoidance 机制\n\n**日期**: 2026-05-13\n**目的**: 调研是否有论文发现过类似 \"deterministic computation 的优势主要来自 death avoidance\" 的现象\n\n---\n\n## 一、直接相关论文（ScienceWorld 上的 Agent 方法）\n\n### 1. SwiftSage (Lin et al., NeurIPS 2023)\n- **标题**: SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks\n- **Venue**: NeurIPS 2023\n- **ScienceWorld 成绩**: 84.7 avg score（SOTA at the time）\n- **与我们的关系**: 最直接的架构类比——Swift（小模型行为克隆）+ Sage（GPT-4 慢思考）的双模块路由。Sage 模块在 Swift 失败时介入，本质上也是一种 failure recovery 机制。但 **没有量化分析** fast/slow 切换的收益来自 failure avoidance vs positive guidance。\n- **定位**: 互补/背景。SwiftSage 证明了双模块路由在 ScienceWorld 上有效，但没做我们的 decomposition 分析。\n\n### 2. CogRouter (arXiv 2602.12662)\n- **ScienceWorld 成绩**: Score=84.6, SR=72.0%\n- **方法**: Qwen2.5-7B，路由 thinking depth（4 levels），用 CoPO (RL) 训练\n- **与我们的关系**: 路由 thinking depth 而非 internal/deterministic modality。没有 death avoidance 分析，没有 counterfactual decomposition。\n- **定位**: 背景/对标。不同路由维度，不竞争。\n\n### 3. ITP-R (arXiv 2601.08955)\n- **ScienceWorld 成绩**: SR=63.91%（低于 CogRouter）\n- **方法**: Learned world model + K-head gating\n- **与我们的关系**: 路由到 approximate LLM world model（而非 deterministic simulator），有 compounding error 问题。没有 death avoidance 分析。\n- **定位**: 背景。说明 approximate world model 不如 exact simulation。\n\n### 4. MTRouter (Zhang et al., ACL 2026)\n- **标题**: MTRouter: Cost-Aware Multi-Turn LLM Routing with History–Model Joint Embeddings\n- **ScienceWorld 成绩**: 53.8 avg（超过 GPT-5 的 48.4，成本降 58.7%）\n- **与我们的关系**: 多模型路由（不同 LLM 之间），非 LLM vs deterministic 路由。但在 ScienceWorld 上有结果，是 routing 方向的 concurrent work。\n- **定位**: 背景。不同路由目标（cost-aware multi-model vs safety-aware modality）。\n\n### 5. BEACON (Milestone-Guided Policy Learning, 2025-2026)\n- **方法**: Trajectory-level RL，milestone-based credit assignment\n- **与我们的关系**: 解决 credit misattribution 问题（正确的早期动作被 terminal failure 惩罚）。与我们的发现呼应——ScienceWorld 的稀疏奖励导致 credit assignment 困难。但关注 RL 训练效率，非 routing。\n- **定位**: 互补。他们的 credit misattribution 问题正是我们的 death-dominated signal 的另一面。\n\n### 6. ScienceWorld 原始论文 (Wang et al., EMNLP 2022)\n- **标题**: ScienceWorld: Is your Agent Smarter than a 5th Grader?\n- **奖励结构**: 完成所有 subgoals = 100 分，稀疏奖励（多数步骤 reward=0）。\n- **关于 -100 penalty**: 搜索未找到原始论文明确讨论 -100 death penalty 的设计意图。需要直接查看源码确认 penalty 结构。\n- **定位**: 基础背景。\n\n---\n\n## 二、Tool Use Learning 文献\n\n### 7. Toolformer (Schick et al., NeurIPS 2023)\n- **方法**: Self-supervised tool-use learning，通过 API call insertion + loss reduction filtering\n- **与我们的关系**: 标准 tool-use learning baseline。差异：(1) 我们用 environment forking 做 hindsight counterfactual labeling（不是 self-supervised），(2) 我们的 framing 是 safety-aware（不是 general tool selection）。\n- **定位**: 背景，必须引用并明确区分。\n\n### 8. ReTool (ICLR 2026)\n- **标题**: ReTool: Reinforcement Learning for Strategic Tool Use in LLMs\n- **方法**: RL 训练 LLM 学习 when/how 调用 code interpreter，outcome-driven reward\n- **与我们的关系**: 最接近的 \"when to invoke tool\" 工作。差异：(1) implicit routing（entangled with backbone），我们用 explicit modular router；(2) 没做 benefit decomposition（failure avoidance vs positive guidance）。\n- **定位**: 互补/部分竞争。我们的 decomposition 分析是他们缺失的。\n\n### 9. ToolRLA (2026)\n- **标题**: ToolRLA: Multiplicative Reward Decomposition for Tool-Integrated Agents\n- **方法**: 将 tool invocation reward 分解为 tool-name / coverage / parameter accuracy sub-scores\n- **与我们的关系**: 做了 reward decomposition，但维度不同（tool selection accuracy vs death avoidance mechanism）。他们分解的是\"哪个维度的 tool use 做得好\"，我们分解的是\"tool use 的收益来自哪种机制\"。\n- **定位**: 互补。方法论上有呼应（都在做 decomposition），但分析维度完全不同。\n\n---\n\n## 三、LLM Agent Safety / Failure Analysis\n\n### 10. Check Yourself Before You Wreck Yourself (Kumaraguru et al., NeurIPS 2025 Workshop)\n- **方法**: Prompting LLM agent 在不确定时主动 quit，在 ToolEmu 上评估\n- **与我们的关系**: **最接近我们 \"death avoidance\" framing 的工作**。他们的 \"selective quitting\" 本质上是 death avoidance 的一种形式——识别高风险场景并退出。差异：(1) 他们用 prompting，我们用 learned router；(2) 他们的 quitting 是放弃任务，我们的 routing 是切换到更安全的 modality（仍完成任务）。\n- **定位**: **高度相关，必须引用**。我们的 router 可以理解为 \"selective quitting from LLM reasoning, switching to deterministic computation\" 而非完全放弃。\n\n### 11. SafeHarbor (arXiv 2605.05704, 2026)\n- **方法**: Hierarchical memory-augmented guardrail for LLM agent safety\n- **与我们的关系**: Agent safety guardrail，但关注 policy compliance / harmful action prevention，非 task-level catastrophic failure。\n- **定位**: 背景（safety 大方向）。\n\n### 12. Towards Verifiably Safe Tool Use for LLM Agents (Doshi et al., ICSE 2026)\n- **方法**: STPA + capability-enhanced MCP framework，formal safety specification\n- **与我们的关系**: 形式化 tool safety，但面向 enterprise scenarios（data leak, record overwrite），非 interactive environment 的 catastrophic failure。\n- **定位**: 背景（broader safety context）。\n\n### 13. Where LLM Agents Fail and How They Can Learn From Failures (2025)\n- **方法**: AgentErrorTaxonomy + AgentErrorBench + AgentDebug\n- **环境**: ALFWorld, GAIA, WebShop\n- **与我们的关系**: Failure taxonomy 和 debugging framework。分类了 agent failure modes 但没有量化 \"failure avoidance vs positive performance\" 的分解。\n- **定位**: 背景。我们的 death avoidance finding 可以看作是他们 taxonomy 中一种特定 failure mode 的量化分析。\n\n### 14. How Do LLMs Fail In Agentic Scenarios? (2025)\n- **方法**: Qualitative analysis of success/failure scenarios\n- **与我们的关系**: Failure mode 分析但定性为主，没有量化 decomposition。\n- **定位**: 背景。\n\n### 15. Agent-SafetyBench\n- **方法**: Evaluating LLM agent safety across multiple risk dimensions\n- **与我们的关系**: Safety benchmark，面向 harmful action prevention 而非 task performance decomposition。\n- **定位**: 远景背景。\n\n---\n\n## 四、Safe RL 文献\n\n### 16. Safe Reinforcement Learning with Dead-Ends Avoidance and Recovery (RA-L / ICRA 2024)\n- **方法**: 学习 optimal boundary 区分 safe/unsafe states，pretrain recovery policy + safety critic\n- **与我们的关系**: **概念上最接近的 Safe RL 工作**。他们的 \"dead-end states\"（无论什么 policy 都必然失败的状态）= 我们的 \"death states\"。他们的 safety critic = 我们的 router-as-death-detector。差异：(1) 他们在 continuous control（robotics），我们在 text-based interactive environments；(2) 他们训练 recovery policy，我们切换 computation modality。\n- **定位**: **重要背景，建议引用**。建立 \"death avoidance as a routing mechanism\" 与 Safe RL 的联系。\n\n### 17. Combating RL's Sisyphean Curse with Intrinsic Fear (Lipton et al., 2016)\n- **方法**: 学习 fear model 预测 imminent catastrophe probability，用于 penalize Q-learning\n- **与我们的关系**: 早期 \"death avoidance\" 工作。他们发现 DRL agents 会周期性地重新访问 catastrophic states（Sisyphean curse）。我们的 router 本质上也是一个 fear model——预测 \"这一步用 LLM 内部推理是否会导致 catastrophe\"。\n- **定位**: 互补/理论背景。\n\n### 18. Avoiding Death through Fear Intrinsic Conditioning (Sanchez et al., 2025)\n- **方法**: 生物启发的 amygdala-like memory network，intrinsic reward for death avoidance\n- **与我们的关系**: 最新的 death avoidance RL 工作，使用 memory-augmented network 学习 \"fear\"。与我们的 router 在功能上类似（都在学 death prediction），但方法完全不同。\n- **定位**: 背景。\n\n### 19. Constrained MDP / State-wise Safe RL (Garcia & Fernandez, JMLR 2015; 多篇 survey)\n- **核心框架**: CMDP with safety constraints，state-wise constraint satisfaction\n- **与我们的关系**: 我们的 router 可以看作一种 state-wise safety mechanism——在每个 state 决定是否切换到 \"safe\" (deterministic) modality。但我们不是在 CMDP 框架下优化，而是用 counterfactual labeling + SFT。\n- **定位**: 理论背景。可以在 Related Work 中简短提及 \"our router can be viewed as a learned state-wise safety gate\"。\n\n---\n\n## 五、Adaptive Computation / Routing\n\n### 20. Learning How Hard to Think (ICLR 2025)\n- **方法**: Input-adaptive compute allocation, learned marginal benefit estimator\n- **与我们的关系**: Compute allocation 方向，但面向 decoding budget（best-of-k, routing to expensive vs cheap decoder），非 modality routing。\n- **定位**: 远景背景。\n\n### 21. ARES: Adaptive Reasoning Effort Selection (2026)\n- **方法**: Lightweight router 预测 optimal reasoning effort level\n- **与我们的关系**: Intra-model thinking level routing，非 inter-modality routing。\n- **定位**: 背景。\n\n### 22. Router-R1 (2025-2026)\n- **方法**: RL-based multi-LLM routing with think + route actions\n- **与我们的关系**: Multi-model routing via RL。差异：multi-model（不同 LLM）vs single-modality（LLM vs deterministic）。\n- **定位**: 背景。\n\n---\n\n## 六、核心问题回答\n\n### Q1: \"99% death avoidance\" finding 是否有先例？\n\n**没有直接先例。** 没有找到任何论文量化过 \"tool invocation / modality routing 的收益中，failure prevention vs positive guidance 各占多少\"。\n\n最接近的工作：\n- **Intrinsic Fear** (Lipton 2016) 和 **Dead-Ends Avoidance** (ICRA 2024) 在 Safe RL 中研究了 death/catastrophe avoidance，但没有做 \"benefit decomposition\"（将 routing/tool-use 收益分解为 death avoidance vs positive improvement）。\n- **\"Check Yourself\"** (NeurIPS 2025 WS) 提出 selective quitting 提升 safety，但没有量化 quitting 的收益有多少来自 catastrophe prevention vs 其他。\n- **ToolRLA** (2026) 做了 reward decomposition，但分解维度是 tool-selection accuracy，不是 failure prevention mechanism。\n- **SwiftSage** 有 fast/slow 路由但没分析路由收益的来源。\n\n**我们的 \"~93% death avoidance dominance\" 发现是 novel 的。**\n\n### Q2: 论文中应该引用的相关工作\n\n**必须引用（Related Work 段落）**:\n1. **SwiftSage** (Lin et al., 2023) — 最接近的 ScienceWorld 双模块路由\n2. **Toolformer** (Schick et al., 2023) — Tool-use learning baseline\n3. **ReTool** (ICLR 2026) — When to use tools via RL\n4. **\"Check Yourself\"** (2025) — LLM agent selective quitting for safety\n5. **Dead-Ends Avoidance** (ICRA 2024) — Safe RL dead-end detection\n6. **Intrinsic Fear** (Lipton et al., 2016) — Death avoidance in RL\n7. **ScienceWorld** (Wang et al., EMNLP 2022) — 环境\n8. **ReAct** (Yao et al., 2023) — Agent baseline\n9. **CogRouter** — ScienceWorld routing baseline\n10. **ITP-R** — World model routing baseline\n\n**建议引用（单句提及）**:\n11. **MTRouter** (ACL 2026) — ScienceWorld 上的 concurrent routing work\n12. **BEACON** — Trajectory-level RL on ScienceWorld\n13. **Garcia & Fernandez** (JMLR 2015) — Safe RL survey（CMDP framework）\n14. **Where LLM Agents Fail** (2025) — Agent failure taxonomy\n15. **ToolRLA** (2026) — Reward decomposition for tool use\n\n### Q3: Novelty claim 是否安全？\n\n**安全，但需要精确表述。**\n\n我们的 novelty 有两层：\n1. **Empirical finding（强 novelty）**: 首次量化 \"modality routing 的收益 decomposition\"——在 ScienceWorld 上 ~93% 来自 death avoidance。没有任何论文做过类似分解。\n2. **Methodology（中等 novelty）**: Episode-level counterfactual labeling 解决了 per-step oracle 在稀疏奖励下退化的问题（98% tie rate）。这个方法论是 specific to sparse-reward interactive environments 的贡献。\n\n**潜在攻击面**:\n- \"Death avoidance is trivial — just always use deterministic\" → 回应：我们的贡献是 finding，不是 routing method。Always-det 确实是强 baseline，这正是 finding 的一部分。\n- \"This is just Safe RL\" → 回应：Safe RL 研究 death avoidance 但在 continuous control；我们在 LLM agent + text environment 中首次展示 death avoidance 主导 routing signal。\n- \"Check Yourself already showed this\" → 回应：他们的 quitting 是放弃任务，我们切换 modality 继续完成任务；他们没有 benefit decomposition。\n"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-13T21:03:54.092437+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/literature_survey_death_avoidance.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_death-avoidance-literature_20260513T205941",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-13T21:03:54.092622+00:00_

调研完成。核心结论：

## "~93% death avoidance" 发现没有直接先例

没有找到任何论文量化过 "tool invocation / modality routing 的收益中 failure prevention vs positive guidance 各占多少"。这是 novel finding。

## 最接近的 5 篇论文

| 论文 | 关系 | 差异 |
|------|------|------|
| **"Check Yourself Before You Wreck Yourself"** (NeurIPS 2025 WS) | selective quitting for safety | 放弃任务 vs 切换modality继续完成；没有benefit decomposition |
| **Dead-Ends Avoidance** (ICRA 2024) | safe RL dead-end detection | continuous control robotics；没做收益分解 |
| **Intrinsic Fear** (Lipton 2016) | death avoidance in RL 的先驱 | 传统RL，不是LLM agent |
| **SwiftSage** (NeurIPS 2023) | ScienceWorld 双模块路由，84.7分 | 没分析路由收益来源 |
| **ReTool** (ICLR 2026) | RL学when to use code interpreter | implicit routing，没做failure vs positive分解 |

## Novelty claim 安全

- **强 novelty**: 首次量化 modality routing benefit decomposition
- **中等 novelty**: Episode-level counterfactual labeling 方法论
- **主要攻击面**: "trivial → just always-det"，回应：contribution 是 finding 不是 method；always-det 是强 baseline 正是 finding 的核心

完整调研已写入 `artifacts/literature_survey_death_avoidance.md`，涵盖 22 篇论文，附建议引用列表。

Sources:
- [SwiftSage](https://arxiv.org/abs/2305.17390)
- [Check Yourself Before You Wreck Yourself](https://arxiv.org/abs/2510.16492)
- [Safe RL with Dead-Ends Avoidance](https://arxiv.org/abs/2306.13944)
- [Intrinsic Fear](https://arxiv.org/abs/1611.01211)
- [ReTool](https://arxiv.org/abs/2504.11536)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [MTRouter](https://arxiv.org/abs/2604.23530)
- [Where LLM Agents Fail](https://arxiv.org/abs/2509.25370)
- [Towards Verifiably Safe Tool Use](https://arxiv.org/abs/2601.08012)
- [Avoiding Death through Fear](https://arxiv.org/abs/2506.05529)
- [ToolRLA](https://arxiv.org/html/2603.01620v3)
- [ScienceWorld](https://arxiv.org/abs/2203.07540)
- [ARES](https://arxiv.org/pdf/2603.07915)
- [Router-R1](https://arxiv.org/abs/2506.09033)
- [How Do LLMs Fail in Agentic Scenarios](https://arxiv.org/pdf/2512.07497)
- [BEACON](https://arxiv.org/html/2605.06078)
- [Learning How Hard to Think](https://openreview.net/forum?id=6qUUgw9bAZ)
- [Safe RL Survey (Garcia & Fernandez)](https://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf)
- [SafeHarbor](https://arxiv.org/html/2605.05704)
- [AgentMath](https://arxiv.org/pdf/2512.20745)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_death-avoidance-literature_20260513T205941"
}
```

</details>

---
