# research literature scan retry

**Why Calibration Fails: A Taxonomy of Failure Modes in Dialect-Aware LLM User Simulation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_research_literature-scan-retry_20260513T054551.jsonl`
- **Structured JSON:** [`e1bb3b39566d9036117f.json`](../../sessions/e1/e1bb3b39566d9036117f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-13T05:50:03.871543+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read literature_map.yaml",
  "subagent_type": "Explore",
  "prompt": "Find and read the file literature_map.yaml in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/. Also check the artifacts subdirectory. Read the full contents of the file."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Agent",
  "tool_args": {
    "description": "Read literature_map.yaml",
    "subagent_type": "Explore",
    "prompt": "Find and read the file literature_map.yaml in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/. Also check the artifacts subdirectory. Read the full contents of the file."
  }
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-13T05:50:03.871929+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/literature_map.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-13T05:50:03.872094+00:00_

artifacts/literature_map.yaml
literature_map.yaml
artifacts/_project/report/literature_map.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-13T05:50:03.872264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-13T05:50:03.872588+00:00_

1	papers:
2	  # ============================================================
3	  # DIRECT-COMPETITOR
4	  # ============================================================
5	  # 未找到直接竞品。没有现有工作专门做"校准 LLM 用户模拟器的方言行为率偏差"。
6	  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。
7	  # 这验证了 DemoCalib 的新颖性。
8	
9	  # ============================================================
10	  # FOUNDATION
11	  # ============================================================
12	  - id: seshadri2026lost
13	    title: "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations"
14	    authors: "Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant"
15	    venue: "arXiv 2601.17087"
16	    year: 2026
17	    url: "https://arxiv.org/abs/2601.17087"
18	    category: foundation
19	    role: "Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration"
20	    relevance: high
21	    key_findings:
22	      - "Agent success rates vary up to 9pp across different user simulator LLMs"
23	      - "AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers"
24	      - "Simulated users introduce conversational artifacts absent from real human users"
25	      - "Disparities compound significantly with age for AAVE speakers"
26	    how_we_differ: "They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps"
27	
28	  - id: yao2024taubench
29	    title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
30	    authors: "Yao et al."
31	    venue: "arXiv 2406.12045"
32	    year: 2024
33	    url: "https://arxiv.org/abs/2406.12045"
34	    category: foundation
35	    role: "The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric"
36	    relevance: high
37	    key_findings:
3
…[truncated 16901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T05:50:03.872901+00:00_

Perfect! I've successfully retrieved the complete literature_map.yaml file from the project directory. Here's a summary of what it contains:

## File Location
**Main file:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml`

## Content Overview

The literature_map.yaml is a comprehensive reference map containing **20 papers** organized into 5 categories:

### Paper Categories:

1. **DIRECT-COMPETITOR (0 papers)**
   - Notes that no existing work directly addresses "calibrating LLM user simulator dialect behavior rate bias"
   - This validates the novelty of the DemoCalib project

2. **FOUNDATION (4 papers)**
   - seshadri2026lost: LLM-simulated users unreliable across demographics
   - yao2024taubench: tau-bench agent evaluation framework with user simulator
   - liu2024agentbench: Multi-environment agent benchmark
   - wang2024mint: Multi-turn interaction evaluation

3. **METHOD-COMPONENT (7 papers)**
   - Core algorithms and techniques: DPO, calibration methods, persona consistency, user LMs, alignment surveys
   - Key papers: rafailov2023dpo, zhao2021calibrate, abdulhai2025consistent, naous2025flipping

4. **EVALUATION (5 papers)**
   - lin2025redial: Dialect fairness in reasoning tasks (SE-AAVE benchmark)
   - faisal2024dialectbench: Multi-dialect NLP benchmark
   - gallegos2024bias: LLM bias survey
   - parrish2022bbq: Bias benchmark for QA
   - haq2026dialect: Dialect vs demographics bias quantification

5. **BACKGROUND (5 papers)**
   - Sociolinguistic and dialect-specific context
   - Key references: joshi2025dialect_survey, rickford1999aave (AAVE), kachru2008cultures (Indian English)

### Relevance Breakdown:
- **High relevance:** 8 papers
- **Medium relevance:** 11 papers
- **Low relevance:** 1 paper

The file provides structured metadata for each paper including title, authors, venue, year, URL, category, role description, key findings, and how the current project differs from each reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Agent",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T05:50:03.873135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T05:50:03.873503+00:00_

1	papers:
2	  # ============================================================
3	  # DIRECT-COMPETITOR
4	  # ============================================================
5	  # 未找到直接竞品。没有现有工作专门做"校准 LLM 用户模拟器的方言行为率偏差"。
6	  # 最接近的是 Haq & Saldias 2026（归入 evaluation），但他们只量化偏差，不提出校准方法。
7	  # 这验证了 DemoCalib 的新颖性。
8	
9	  # ============================================================
10	  # FOUNDATION
11	  # ============================================================
12	  - id: seshadri2026lost
13	    title: "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations"
14	    authors: "Seshadri, Cahyawijaya, Odumakinde, Singh, Goldfarb-Tarrant"
15	    venue: "arXiv 2601.17087"
16	    year: 2026
17	    url: "https://arxiv.org/abs/2601.17087"
18	    category: foundation
19	    role: "Documents that LLM user simulators are differentially effective proxies across demographic groups; AAVE and Indian English speakers get worst calibration"
20	    relevance: high
21	    key_findings:
22	      - "Agent success rates vary up to 9pp across different user simulator LLMs"
23	      - "AAVE speakers experience consistently worse success rates and calibration errors than SAE speakers"
24	      - "Simulated users introduce conversational artifacts absent from real human users"
25	      - "Disparities compound significantly with age for AAVE speakers"
26	    how_we_differ: "They document the problem; we propose BCP + DPO to calibrate simulator behavioral rates and close the gaps"
27	
28	  - id: yao2024taubench
29	    title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
30	    authors: "Yao et al."
31	    venue: "arXiv 2406.12045"
32	    year: 2024
33	    url: "https://arxiv.org/abs/2406.12045"
34	    category: foundation
35	    role: "The agent evaluation framework we build on; provides retail customer service domain with user simulator + tool-calling agent + pass^k metric"
36	    relevance: high
37	    key_findings:
3
…[truncated 16901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T05:50:03.873813+00:00_

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
  "session": "worker_research_literature-scan-retry_20260513T054551",
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

_source line 10 · 2026-05-13T05:50:03.874007+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T05:50:03.874180+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv LLM calibration dialect bias fairness 2026 May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv LLM calibration dialect bias fairness 2026 May"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T05:50:03.874353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv DPO bias mitigation fairness preference optimization 2026 May"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv DPO bias mitigation fairness preference optimization 2026 May"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T05:50:03.874551+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv LLM user simulator fairness agent evaluation bias 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv LLM user simulator fairness agent evaluation bias 2026"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T05:50:03.874742+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv AAVE Indian English LLM evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv AAVE Indian English LLM evaluation 2026"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-13T05:50:03.874929+00:00_

Web search results for query: "arxiv LLM calibration dialect bias fairness 2026 May"

Links: [{"title":"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles","url":"https://arxiv.org/html/2604.21152"},{"title":"Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures","url":"https://arxiv.org/html/2603.18729"},{"title":"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/html/2410.11005"},{"title":"[2410.11005] Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/abs/2410.11005"},{"title":"Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/html/2510.12462v3"},{"title":"AI Bias and Fairness: From Detection to Mitigation in 2026 | Zylos Research","url":"https://zylos.ai/research/2026-02-05-ai-bias-fairness"},{"title":"Simulating a Bias Mitigation Scenario in Large Language Models","url":"https://arxiv.org/html/2509.14438v1"},{"title":"Bias and Fairness in Large Language Models: A Survey","url":"https://arxiv.org/html/2309.00770v2"},{"title":"[2305.17926] Large Language Models are not Fair Evaluators","url":"https://arxiv.org/abs/2305.17926"},{"title":"One Language, Many Gaps: Evaluating Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/html/2410.11005v1"}]

I found several relevant ArXiv papers on LLM calibration, dialect bias, and fairness. Here's a summary of the key findings:

## Recent Research on Dialect Bias and Fairness in LLMs (2026)

### Dialect vs Demographics Study
Previous work showed that the number of undesirable behaviors in all three state-of-the-art LLMs (GPT-4, Claude 3 Opus, and Llama 3-8B) increased disproportionately more for users with a lower level of English proficiency, lower education status, and for individuals whom the models identify as origin
…[truncated 1295 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T05:50:03.875120+00:00_

Web search results for query: "arxiv DPO bias mitigation fairness preference optimization 2026 May"

Links: [{"title":"ϕ-DPO: Fairness Direct Preference Optimization Approach to Continual Learning in Large Multimodal Models","url":"https://arxiv.org/html/2602.22601"},{"title":"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment","url":"https://arxiv.org/html/2602.16438"},{"title":"[2601.19595] Intersectional Fairness via Mixed-Integer Optimization","url":"https://arxiv.org/abs/2601.19595"},{"title":"Us-vs-Them bias in Large Language Models","url":"https://arxiv.org/html/2512.13699"},{"title":"DPO: Fairness Direct Preference Optimization Approach to ...","url":"https://arxiv.org/pdf/2602.22601"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/pdf/2305.18290"},{"title":"Explainable post-training bias mitigation with distribution-based fairness metrics","url":"https://arxiv.org/html/2504.01223v3"},{"title":"A Comprehensive Survey of Direct Preference Optimization: Datasets, Theories, Variants, and Applications","url":"https://arxiv.org/html/2410.15595v3"},{"title":"[2406.10957] Eliminating Biased Length Reliance of Direct Preference Optimization via Down-Sampled KL Divergence","url":"https://arxiv.org/abs/2406.10957"},{"title":"Beyond Accuracy-Fairness: Stop evaluating bias mitigation methods solely on between-group metrics","url":"https://arxiv.org/html/2401.13391v1"}]

I found several relevant research papers on arXiv related to DPO, bias mitigation, and fairness. Here are the key findings:

## Recent Research (2026 and 2025)

**ϕ-DPO: Fairness Direct Preference Optimization** - A new Fairness DPO loss addresses the fairness problem caused by imbalanced data. This approach can mitigate forgetting, adapt continuously to new learning tasks, and maintain robustness under data imbalance in large multimodal models. This paper was published in March 2026.

**Intra-Fairness Dynamics:
…[truncated 1211 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-13T05:50:03.875303+00:00_

Web search results for query: "arxiv LLM user simulator fairness agent evaluation bias 2026"

Links: [{"title":"Evaluation and Benchmarking of LLM Agents: A Survey","url":"https://arxiv.org/html/2507.21504v1"},{"title":"Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations","url":"https://arxiv.org/html/2601.17087v1"},{"title":"FairEval: Evaluating Fairness in LLM-Based Recommendations","url":"https://arxiv.org/pdf/2504.07801"},{"title":"Evaluating and Mitigating LLM-as-a-judge Bias in Communication Systems","url":"https://arxiv.org/html/2510.12462v3"},{"title":"[2510.04317] FairAgent: Democratizing Fairness-Aware Machine Learning with LLM-Powered Agents","url":"https://arxiv.org/abs/2510.04317"},{"title":"Artificial Intelligence","url":"https://arxiv.org/list/cs.AI/new"},{"title":"GitHub - VoltAgent/awesome-ai-agent-papers: A curated collection of AI agent research papers released in 2026, covering agent engineering, memory, evaluation, workflows, and autonomous systems. · GitHub","url":"https://github.com/VoltAgent/awesome-ai-agent-papers"},{"title":"[2510.12217v2] HALF: Harm-Aware LLM Fairness Evaluation Aligned with Deployment","url":"https://arxiv.org/abs/2510.12217v2"},{"title":"Fairness Evaluation and Inference Level Mitigation in LLMs","url":"https://arxiv.org/html/2510.18914v4"},{"title":"FairAgent: Democratizing Fairness-Aware Machine Learning with LLM-Powered Agents","url":"https://arxiv.org/html/2510.04317v1"}]

I found several highly relevant arXiv papers related to your search query about LLM user simulators, fairness, agent evaluation, and bias in 2026. Here are the key findings:

## Most Relevant Paper

The most directly relevant result is "Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations," which investigates whether LLM-simulated users serve as reliable proxies for real human users in evaluating agents, finding that LLM-simulated users may not serve 
…[truncated 1523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T05:50:03.875479+00:00_

Web search results for query: "arxiv AAVE Indian English LLM evaluation 2026"

Links: [{"title":"IndicEval: A Bilingual Indian Educational","url":"https://arxiv.org/pdf/2602.16467v1"},{"title":"[2602.16467v1] IndicEval: A Bilingual Indian Educational Evaluation Framework for Large Language Models","url":"https://arxiv.org/abs/2602.16467v1"},{"title":"[2602.16467] IndicEval: A Bilingual Indian Educational Evaluation Framework for Large Language Models","url":"https://arxiv.org/abs/2602.16467"},{"title":"Towards Large Language Model driven Reference-less Translation Evaluation for English and Indian Languages","url":"https://arxiv.org/html/2404.02512"},{"title":"IndicEval: A Bilingual Indian Educational Evaluation Framework for Large Language Models","url":"https://arxiv.org/html/2602.16467"},{"title":"[2408.14845] AAVENUE: Detecting LLM Biases on NLU Tasks in AAVE via a Novel Benchmark","url":"https://arxiv.org/abs/2408.14845"},{"title":"IndicEval: A Bilingual Indian Educational Evaluation ...","url":"https://www.arxiv.org/pdf/2602.16467"},{"title":"Better To Ask in English? Evaluating Factual Accuracy of Multilingual LLMs in English and Low-Resource Languages","url":"https://arxiv.org/html/2504.20022"},{"title":"Revisiting Metric Reliability for Fine-grained Evaluation of Machine Translation and Summarization in Indian Languages","url":"https://arxiv.org/html/2510.07061"},{"title":"Multi-Dimensional Evaluation of LLMs for Grammatical Error CorrectionAccepted at AIED 2026","url":"https://arxiv.org/html/2605.07635"}]

Based on my search results, I found relevant papers from arXiv related to your query. Here are the key findings:

## IndicEval: Bilingual Indian Educational Evaluation

IndicEval is a scalable benchmarking platform designed to assess LLM performance using authentic high-stakes examination questions from UPSC, JEE, and NEET across STEM and humanities domains in both English and Hindi. This paper was published on February 18, 2026.

The study's main findin
…[truncated 1139 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T05:50:03.875689+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605 LLM dialect bias calibration fairness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605 LLM dialect bias calibration fairness"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-13T05:50:03.875864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605 DPO alignment fairness bias mitigation language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605 DPO alignment fairness bias mitigation language model"
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T05:50:03.875991+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605 user simulator calibration behavioral alignment dialogue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605 user simulator calibration behavioral alignment dialogue"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-13T05:50:03.876108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"phi-DPO\" fairness direct preference optimization continual learning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"phi-DPO\" fairness direct preference optimization continual learning 2026"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T05:50:03.876262+00:00_

Web search results for query: ""phi-DPO" fairness direct preference optimization continual learning 2026"

Links: [{"title":"[2602.22601] $ϕ$-DPO: Fairness Direct Preference Optimization Approach to Continual Learning in Large Multimodal Models","url":"https://arxiv.org/abs/2602.22601"},{"title":"ϕ-DPO: Fairness Direct Preference Optimization Approach to Continual Learning in Large Multimodal Models","url":"https://arxiv.org/html/2602.22601"},{"title":"DPO: Fairness Direct Preference Optimization Approach to ...","url":"https://arxiv.org/pdf/2602.22601"},{"title":"[2305.18290] Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/abs/2305.18290"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/pdf/2305.18290"},{"title":"Direct Preference Optimization: Your Language Model is Secretly a Reward Model | OpenReview","url":"https://openreview.net/forum?id=HPuSIXJaa9"},{"title":"Direct Preference Optimization Explained In-depth","url":"https://www.tylerromero.com/posts/2024-04-dpo/"},{"title":"Online DPO: Online Direct Preference Optimization with Fast-Slow Chasing","url":"https://arxiv.org/html/2406.05534v1"},{"title":"[2605.02626] Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models","url":"https://arxiv.org/abs/2605.02626"},{"title":"1 Introduction","url":"https://arxiv.org/html/2405.15065"}]

Based on the search results, here's what I found about ϕ-DPO (phi-DPO):

## Overview

ϕ-DPO is a novel Fairness Direct Preference Optimization (FaiDPO) framework for continual learning in Large Multimodal Models (LMMs). The research was published in March 2026.

## Key Problem and Solution

Fairness in continual learning for large multimodal models is an emerging yet underexplored challenge, particularly in the presence of imbalanced data distributions that can lead to biased model updates and suboptimal performance across tasks. 

The approac
…[truncated 964 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T05:50:03.876439+00:00_

Web search results for query: "arxiv 2605 LLM dialect bias calibration fairness"

Links: [{"title":"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/html/2410.11005v3"},{"title":"One Language, Many Gaps: Evaluating Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/html/2410.11005v1"},{"title":"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles","url":"https://arxiv.org/html/2604.21152"},{"title":"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/html/2605.02348v1"},{"title":"EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage","url":"https://arxiv.org/html/2605.03998v1"},{"title":"Improving Fairness in LLMs Through Testing-Time Adversaries","url":"https://arxiv.org/html/2505.12100"},{"title":"Calibrate, Don’t Curate: Label-Efficient Estimation from Noisy LLM Judges","url":"https://arxiv.org/html/2605.09702"},{"title":"Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures","url":"https://arxiv.org/html/2603.18729"},{"title":"[2410.11005] Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/abs/2410.11005"},{"title":"Bias and Fairness in Large Language Models: A Survey","url":"https://arxiv.org/html/2309.00770v2"}]

Based on the search results, I found several relevant papers related to LLM dialect bias, calibration, and fairness from arxiv. Here are the most relevant findings:

## Key Papers Found:

**1. Dialect vs Demographics: Quantifying LLM Bias (arxiv 2604.21152)**

This paper evaluates two open-weights language models (Gemma-3-12b and Qwen-3-VL-8b) across three demographic profiles (Black, Singaporean, and White), two identity signaling methods (Implicit Dialect vs. Explicit Declaration), and fo
…[truncated 1505 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-13T05:50:03.876610+00:00_

Web search results for query: "arxiv 2605 DPO alignment fairness bias mitigation language model"

Links: [{"title":"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/html/2605.02348v1"},{"title":"Detection, Classification, and Mitigation of Gender Bias in Large Language Models","url":"https://arxiv.org/html/2506.12527"},{"title":"A Statistical Framework for Alignment with Biased AI Feedback","url":"https://arxiv.org/html/2602.08259"},{"title":"Multi-Reward GRPO Fine-Tuning for De-biasing Large Language Models: A Study Based on Chinese-Context Discrimination Data","url":"https://arxiv.org/html/2511.06023"},{"title":"Vulnerabilities Mitigation for Safety-Aligned Language Models via Debiasing","url":"https://arxiv.org/html/2502.02153v1"},{"title":"Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment","url":"https://arxiv.org/html/2602.16438v1"},{"title":"[2405.16455] On the Algorithmic Bias of Aligning Large Language Models with RLHF: Preference Collapse and Matching Regularization","url":"https://arxiv.org/abs/2405.16455"},{"title":"Aligning Large Language Models with Counterfactual DPO","url":"https://arxiv.org/html/2401.09566v1"},{"title":"Published as a conference paper at ICLR 2025 EARLIER TOKENS CONTRIBUTE MORE:","url":"https://arxiv.org/pdf/2502.14340"},{"title":"Fairness Evaluation and Inference Level Mitigation in LLMs","url":"https://arxiv.org/html/2510.18914v4"}]

The search has returned several relevant papers related to DPO (Direct Preference Optimization), alignment, fairness, and bias mitigation in language models. Here are the key findings:

## Main Papers Found:

1. **Decoding-Time Debiasing via Process Reward Models** (arxiv 2605.02348): This paper takes a debiasing approach at decoding time, treating bias mitigation as a structured search over candidate tokens, with a Process Reward Model acting as a judge to score each candidate for both fairness and 
…[truncated 1578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T05:50:03.876833+00:00_

Web search results for query: "arxiv 2605 user simulator calibration behavioral alignment dialogue"

Links: [{"title":"SpokenUS: A Spoken User Simulator for Task-Oriented Dialogue","url":"https://arxiv.org/html/2603.16783"},{"title":"Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners","url":"https://arxiv.org/html/2605.08019v1"},{"title":"Mind the Sim2Real Gap in User Simulation for Agentic Tasks","url":"https://arxiv.org/html/2603.11245v1"},{"title":"Adversarial Training for Failure-Sensitive User Simulation in Mental","url":"https://www.arxiv.org/pdf/2512.20773"},{"title":"Adversarial Training for Failure-Sensitive User Simulation in Mental Health Dialogue Optimization","url":"https://arxiv.org/html/2512.20773v1"},{"title":"Flipping the Dialogue: Training and Evaluating User Language Models","url":"https://arxiv.org/html/2510.06552v1"},{"title":"Stayin’ Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data","url":"https://arxiv.org/html/2605.04029"},{"title":"Aligning Spoken Dialogue Models from User Interactions","url":"https://arxiv.org/html/2506.21463v1"},{"title":"Aligning Spoken Dialogue Models from User Interactions | OpenReview","url":"https://openreview.net/forum?id=kxFu9rQ0Mu"},{"title":"GitHub - bansky-cl/tods-arxiv-daily-paper: task-oriented dialogue system, especially for LLM, contain subtask: (1) intent-detection (2) slot filling (3) dialogue state tracking · GitHub","url":"https://github.com/bansky-cl/tods-arxiv-daily-paper"}]

Based on the search results, here are the most relevant papers related to your query about user simulator calibration, behavioral alignment, and dialogue:

## Key Relevant Papers:

**1. "Mind the Sim2Real Gap in User Simulation for Agentic Tasks" (2603.11245)**

This paper measures behavioral divergence between simulated and human users across four behavioral dimensions—communication styles, information pattern, cla
…[truncated 1522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T05:50:03.877023+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.11245 \"Mind the Sim2Real Gap\" user simulation agentic tasks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.11245 \"Mind the Sim2Real Gap\" user simulation agentic tasks"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-13T05:50:03.877151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.02348 \"Decoding-Time Debiasing\" process reward models bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.02348 \"Decoding-Time Debiasing\" process reward models bias"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T05:50:03.877269+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2603.18729 \"linguistic stereotypes\" multi-agent generative AI dialect bias"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2603.18729 \"linguistic stereotypes\" multi-agent generative AI dialect bias"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T05:50:03.877382+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv May 2026 LLM behavioral calibration preference alignment user simulation new paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv May 2026 LLM behavioral calibration preference alignment user simulation new paper"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T05:50:03.877530+00:00_

Web search results for query: "arxiv 2603.11245 "Mind the Sim2Real Gap" user simulation agentic tasks"

Links: [{"title":"[2603.11245] Mind the Sim2Real Gap in User Simulation for Agentic Tasks","url":"https://arxiv.org/abs/2603.11245"},{"title":"Mind the Sim2Real Gap in User Simulation for Agentic Tasks","url":"https://arxiv.org/html/2603.11245"},{"title":"Bridging the Sim2Real Gap: A Framework for Evaluating Vision Encoder Pre-Training for Visuomotor Policy Transfer","url":"https://arxiv.org/html/2501.16389v2"},{"title":"Natural Language Can Help Bridge the Sim2Real Gap","url":"https://arxiv.org/html/2405.10020v1"},{"title":"Abstract Sim2Real through Approximate Information States","url":"https://arxiv.org/html/2604.15289"},{"title":"Tendon Force Modeling for Sim2Real Transfer of Reinforcement Learning Policies for Tendon-Driven Robots","url":"https://arxiv.org/html/2603.04351v1"},{"title":"Towards Mitigating Sim2Real Gaps: A Formal Quantitative Approach∗11footnote 1∗This work was supported in part by the ARTPARK and the Siemens.","url":"https://arxiv.org/html/2411.11310v1"},{"title":"Few-shot Sim2Real Based on High Fidelity Rendering with Force Feedback Teleoperation","url":"https://arxiv.org/html/2503.01301v1"},{"title":"Grounding Sim-to-Real Generalization in Dexterous Manipulation: An Empirical Study with Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22876"},{"title":"AgentSim: A Platform for Verifiable Agent-Trace Simulation","url":"https://arxiv.org/html/2604.26653"}]

I found the paper! Here are the key details about arxiv 2603.11245 "Mind the Sim2Real Gap in User Simulation for Agentic Tasks":

## Overview

The paper addresses how LLM-based simulators are widely used as user proxies in multi-turn interactive settings, serving two roles: generating user turns and providing evaluation signals. However, these simulations are frequently assumed to be faithful to real human behaviors, often without rigorous verification.

## Study Design

Th
…[truncated 1181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T05:50:03.877723+00:00_

Web search results for query: "arxiv 2605.02348 "Decoding-Time Debiasing" process reward models bias"

Links: [{"title":"[2605.02348] Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/abs/2605.02348"},{"title":"[2605.02348v1] Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/abs/2605.02348v1"},{"title":"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation","url":"https://arxiv.org/html/2605.02348"},{"title":"Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/html/2604.27495"},{"title":"[2604.27495] Debiasing Reward Models via Causally Motivated Inference-Time Intervention","url":"https://arxiv.org/abs/2604.27495"},{"title":"SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/html/2603.12795"},{"title":"Distributional Process Reward Models: Calibrated Prediction of Future Rewards via Conditional Optimal Transport","url":"https://arxiv.org/html/2605.06785"},{"title":"Debiasing Reward Models by Representation Learning with Guarantees","url":"https://arxiv.org/html/2510.23751v1"},{"title":"[2510.23751] Debiasing Reward Models by Representation Learning with Guarantees","url":"https://arxiv.org/abs/2510.23751"},{"title":"[2603.12795] SteerRM: Debiasing Reward Models via Sparse Autoencoders","url":"https://arxiv.org/abs/2603.12795"}]

## Summary of arXiv 2605.02348: "Decoding-Time Debiasing via Process Reward Models"

I found the paper you're looking for! Here's an overview:

**Main Concept:**

The paper addresses how large language models pick up social biases from their training data and carry those biases into downstream applications, often reinforcing stereotypes around gender, race, religion, disability, age, and socioeconomic status.

**Approach:**

Rather than traditional fixes, the researc
…[truncated 934 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T05:50:03.877893+00:00_

Web search results for query: "arxiv 2603.18729 "linguistic stereotypes" multi-agent generative AI dialect bias"

Links: [{"title":"Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures","url":"https://arxiv.org/html/2603.18729"},{"title":"[2603.18729] Analysis Of Linguistic Stereotypes in Single and Multi-Agent Generative AI Architectures","url":"https://arxiv.org/abs/2603.18729"},{"title":"Standard Language Ideology in AI-Generated Language","url":"https://arxiv.org/html/2406.08726v1"},{"title":"Linguistic Bias in ChatGPT: Language Models Reinforce Dialect Discrimination","url":"https://arxiv.org/html/2406.08818v3"},{"title":"AI generates covertly racist decisions about people based on their dialect | Nature","url":"https://www.nature.com/articles/s41586-024-07856-5"},{"title":"Biased or Flawed? Mitigating Stereotypes in Generative Language Models by Addressing Task-Specific Flaws","url":"https://arxiv.org/html/2412.11414v1"},{"title":"[2406.08818] Linguistic Bias in ChatGPT: Language Models Reinforce Dialect Discrimination","url":"https://arxiv.org/abs/2406.08818"},{"title":"Linguistic Bias in Generative AI | Responsible AI Initiative","url":"https://re-ai.berkeley.edu/projects/linguistic-bias-generative-ai"},{"title":"Generative language models exhibit social identity biases | Nature Computational Science","url":"https://www.nature.com/articles/s43588-024-00741-1"},{"title":"Can LLM Agents Identify Spoken Dialects like a Linguist?","url":"https://arxiv.org/html/2603.29541"}]

I found the paper! Here are the key findings from arxiv 2603.18729:

## Overview
The paper addresses how LLM outputs exhibit discriminatory behavior, triggering stereotype-based inferences based on the dialect in which inputs are written.

## Main Focus
The bias is particularly pronounced when the same inputs are provided to LLMs in Standard American English (SAE) and African-American English (AAE). Dialect features may trigger stereotype-based inferences 
…[truncated 1255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T05:50:03.878071+00:00_

Web search results for query: "arxiv May 2026 LLM behavioral calibration preference alignment user simulation new paper"

Links: [{"title":"Stayin’ Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data","url":"https://arxiv.org/html/2605.04029v1"},{"title":"Aligning LLMs by Predicting Preferences from User Writing Samples","url":"https://arxiv.org/html/2505.23815v1"},{"title":"Mirroring Users: Towards Building Preference-aligned User Simulator with User Feedback in Recommendation","url":"https://arxiv.org/html/2508.18142v1"},{"title":"[2605.04029] Stayin' Aligned Over Time: Towards Longitudinal Human-LLM Alignment via Contextual Reflection and Privacy-Preserving Behavioral Data","url":"https://arxiv.org/abs/2605.04029"},{"title":"Large Language Models as Calibrated Measurement Instruments for Behavioral Parameters","url":"https://arxiv.org/html/2602.01022"},{"title":"[2603.02128] LLMs as Strategic Actors: Behavioral Alignment, Risk Calibration, and Argumentation Framing in Geopolitical Simulations","url":"https://arxiv.org/abs/2603.02128"},{"title":"[2601.01546] Improving Behavioral Alignment in LLM Social Simulations via Context Formation and Navigation","url":"https://arxiv.org/abs/2601.01546"},{"title":"2026-2-13 Evaluating Alignment of Behavioral Dispositions in LLMs","url":"https://arxiv.org/pdf/2602.11328"},{"title":"[2605.07162] CLIPer: Tailoring Diverse User Preference via Classifier-Guided Inference-Time Personalization","url":"https://arxiv.org/abs/2605.07162"},{"title":"The Behavioral Fabric of LLM-Powered GUI Agents: Human Values and Interaction Outcomes","url":"https://arxiv.org/html/2601.16356"}]

Based on the web search results, I found several relevant papers from May 2026 and nearby dates on arXiv that relate to LLM behavioral calibration, preference alignment, and user simulation:

## Key Papers Found:

**1. "Stayin' Aligned Over Time: Towards Longitudinal Human-LLM Alignment vi
…[truncated 1816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T05:50:03.878263+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605 dialect fairness AAVE language model evaluation May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605 dialect fairness AAVE language model evaluation May 2026"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-13T05:50:03.878389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604 2605 agent evaluation user simulator bias calibration tau-bench"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604 2605 agent evaluation user simulator bias calibration tau-bench"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T05:50:03.878507+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605 DPO GRPO fairness dialect sociolinguistic alignment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605 DPO GRPO fairness dialect sociolinguistic alignment"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T05:50:03.878675+00:00_

Web search results for query: "arxiv 2605 dialect fairness AAVE language model evaluation May 2026"

Links: [{"title":"One Language, Many Gaps: Evaluating Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/html/2410.11005v1"},{"title":"Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/html/2410.11005"},{"title":"One Language, Many Gaps: Evaluating Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks | OpenReview","url":"https://openreview.net/forum?id=hRSabwKj53"},{"title":"[2410.11005] Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/abs/2410.11005"},{"title":"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles","url":"https://arxiv.org/html/2604.21152"},{"title":"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models","url":"https://arxiv.org/html/2504.07100"},{"title":"Can Small-Scale Data Poisoning Exacerbate Dialect-Linked Biases in Large Language Models?","url":"https://arxiv.org/html/2507.19195v1"},{"title":"ASSESSING DIALECT FAIRNESS AND ROBUSTNESS","url":"https://openreview.net/pdf/9c62372e2b55a472df6c8b1c67c336abb5fc0cea.pdf"},{"title":"The Hrunting of AI: Where and How to Improve English Dialectal Fairness","url":"https://arxiv.org/html/2603.15187"},{"title":"Assessing Dialect Fairness and Robustness of Large ...","url":"https://openreview.net/pdf?id=dAucFaqLfg"}]

I found several relevant research papers on dialect fairness and AAVE language model evaluation. Here are the key findings from my search:

## ReDial: A Major Study on AAVE Dialect Fairness

ReDial (Reasoning with Dialect Queries) is the first high-quality, end-to-end human-annotated Standardized English (SE) and AAVE parallel dataset for reasoning tasks, containing over 1.2K SE-AAVE prompt pairs covering four can
…[truncated 1313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-13T05:50:03.878902+00:00_

Web search results for query: "arxiv 2604 2605 agent evaluation user simulator bias calibration tau-bench"

Links: [{"title":"GitHub - sierra-research/tau2-bench: τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains · GitHub","url":"https://github.com/sierra-research/tau2-bench"},{"title":"[2506.07982] $τ^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment","url":"https://arxiv.org/abs/2506.07982"},{"title":"$\\tau^2$-bench: : Evaluating Conversational Agents in a Dual-Control Environment | OpenReview","url":"https://openreview.net/forum?id=LGmO9VvuP5"},{"title":"Efficient Agent Evaluation via Diversity-Guided User Simulation","url":"https://arxiv.org/html/2604.21480"},{"title":"τ2-Bench: Evaluating Conversational Agents in a Dual- ...","url":"https://arxiv.org/pdf/2506.07982"},{"title":"{$\\tau$}-bench: A Benchmark for...","url":"https://openreview.net/forum?id=roNSXZpUDN"},{"title":"[2406.12045] $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://arxiv.org/abs/2406.12045"},{"title":"GitHub - sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub","url":"https://github.com/sierra-research/tau-bench"},{"title":"OccuBench: Evaluating AI Agents on Real-World Professional Tasks via Language Environment Simulation","url":"https://arxiv.org/html/2604.10866"},{"title":"τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://arxiv.org/pdf/2406.12045"}]

Based on the search results, I found information relevant to your query about agent evaluation, user simulators, and tau-bench:

## Key Results:

**τ-Bench Series Overview:**

τ-bench is a benchmark that emulates dynamic conversations between a user (simulated by language models) and a language agent provided with domain-specific API tools and policy guidelines. The benchmark employs an efficient and faithful evaluation process that compares the database state at the end of a conversation with the 
…[truncated 1124 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T05:50:03.879089+00:00_

Web search results for query: "arxiv 2605 DPO GRPO fairness dialect sociolinguistic alignment"

Links: [{"title":"Theoretical Limits of Language Model Alignment","url":"https://arxiv.org/html/2605.07105"},{"title":"A Unified Pair‑GRPO Family: From Implicit to Explicit Preference Constraints for Stable and General RL Alignment","url":"https://arxiv.org/html/2605.06375"},{"title":"Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph","url":"https://arxiv.org/html/2605.08037v1"},{"title":"RLHF: A comprehensive Survey for Cultural, Multimodal ...","url":"https://arxiv.org/pdf/2511.03939"},{"title":"Operationalizing Pluralistic Values in Large Language Model Alignment Reveals Trade-offs in Safety, Inclusivity, and Model Behavior","url":"https://arxiv.org/html/2511.14476"},{"title":"Multi-Reward GRPO Fine-Tuning for De-biasing Large Language Models: A Study Based on Chinese-Context Discrimination Data","url":"https://arxiv.org/html/2511.06023"},{"title":"Operationalizing Pluralistic Values in Large Language Model Alignment","url":"https://arxiv.org/pdf/2511.14476"},{"title":"Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles","url":"https://arxiv.org/html/2604.21152"},{"title":"RLHF: A comprehensive Survey for Cultural, Multimodal and Low Latency Alignment Methods","url":"https://arxiv.org/html/2511.03939v1"},{"title":"Topology-Enhanced Alignment for Large Language Models: Trajectory Topology Loss and Topological Preference Optimization","url":"https://arxiv.org/html/2605.07172"}]

I found several relevant papers from arXiv in the 2605 timeframe (May 2026). Here's what the search reveals:

The query matches multiple recent papers on language model alignment, particularly focusing on DPO and GRPO methods. Key findings include:

**On Fairness and Demographic Alignment:**
Group-Robust DPO (GR-DPO) extends DPO to address fairness by using an adversarial re-weighting schedule to explicitly target the
…[truncated 1172 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-13T05:50:03.879256+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2604.21480 \"Efficient Agent Evaluation\" \"Diversity-Guided User Simulation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2604.21480 \"Efficient Agent Evaluation\" \"Diversity-Guided User Simulation\""
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-13T05:50:03.879379+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv \"EnDive\" cross-dialect benchmark fairness LLM 2504.07100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv \"EnDive\" cross-dialect benchmark fairness LLM 2504.07100"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-13T05:50:03.879518+00:00_

Web search results for query: "arxiv 2604.21480 "Efficient Agent Evaluation" "Diversity-Guided User Simulation""

Links: [{"title":"[2604.21480] Efficient Agent Evaluation via Diversity-Guided User Simulation","url":"https://arxiv.org/abs/2604.21480"},{"title":"Efficient Agent Evaluation via Diversity-Guided User Simulation","url":"https://arxiv.org/html/2604.21480"},{"title":"Paper page - Efficient Agent Evaluation via Diversity-Guided User Simulation","url":"https://huggingface.co/papers/2604.21480"},{"title":"Beyond Static Benchmarks: Synthesizing Harmful Content via Persona-based Simulation for Robust Evaluation","url":"https://arxiv.org/html/2604.17020v1"},{"title":"AgentSim: A Platform for Verifiable Agent-Trace Simulation","url":"https://arxiv.org/html/2604.26653"},{"title":"Leveraging User Simulation to Develop and Evaluate Conversational Information Access Agents","url":"https://arxiv.org/html/2312.08041"},{"title":"Simulating Environments with Reasoning Models for Agent Training","url":"https://arxiv.org/html/2511.01824v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1393&show=1000"},{"title":"ARE: scaling up agent environments and evaluations","url":"https://arxiv.org/html/2509.17158v1"},{"title":"[2604.21328] Role of diversity in team performance: the case of missing expertise, an agent based simulation","url":"https://arxiv.org/abs/2604.21328"}]

I found the paper you searched for. Here are the key details:

**Title:** Efficient Agent Evaluation via Diversity-Guided User Simulation

**ArXiv ID:** 2604.21480

**Authors:** Itay Nakash, George Kour, and Ateret Anaby-Tavor from IBM Research

**Main Contribution:** The paper introduces DIVERT (Diversity-Induced Evaluation via Branching of Trajectories), an efficient, snapshot-based, coverage-guided user simulation framework for systematic exploration of agent-user interactions.

**Problem Addressed:** Current evaluation protocols rely on linear Monte Carlo rollouts of complete ag
…[truncated 496 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-13T05:50:03.879731+00:00_

Web search results for query: "arxiv "EnDive" cross-dialect benchmark fairness LLM 2504.07100"

Links: [{"title":"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in","url":"https://arxiv.org/pdf/2504.07100"},{"title":"[2504.07100] EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models","url":"https://arxiv.org/abs/2504.07100"},{"title":"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models","url":"https://arxiv.org/html/2504.07100v1"},{"title":"ENDIVE:ACROSS-DIALECT BENCHMARK FOR FAIR","url":"https://openreview.net/pdf?id=C7Mwox3C1u"},{"title":"Endive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=C7Mwox3C1u"},{"title":"EnDive: A Cross-Dialect Benchmark for Fairness and ...","url":"https://aclanthology.org/2025.findings-emnlp.913.pdf"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=3275&show=50"},{"title":"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.913/"},{"title":"[PDF] EnDive: A Cross-Dialect Benchmark for Fairness and ...","url":"https://www.semanticscholar.org/paper/EnDive:-A-Cross-Dialect-Benchmark-for-Fairness-and-Gupta-Cheung/1e4da0716688e6c3d904006c98ecdb1e4b4c6533"},{"title":"[2410.11005] Assessing Dialect Fairness and Robustness of Large Language Models in Reasoning Tasks","url":"https://arxiv.org/abs/2410.11005"}]

I found the arXiv paper you requested. Here are the key details about **EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models** (arXiv:2504.07100):

## Overview

EnDive (English Diversity) is a benchmark that evaluates five widely-used large language models (LLMs) across tasks in language understanding, algorithmic reasoning, mathematics, and logic.

## Motivation

The diversity of human langua
…[truncated 1212 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-13T05:50:03.879956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "offset": "320"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "offset": "320"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-13T05:50:03.880107+00:00_

320	      - "Captures variation in language styles, knowledge levels, and objectives"
321	    how_we_differ: "They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions"
322	
323	# ============================================================
324	# SUMMARY
325	# ============================================================
326	# Total: 20 papers
327	# - direct-competitor: 0 (novelty confirmed)
328	# - foundation: 4 (seshadri2026lost, yao2024taubench, liu2024agentbench, wang2024mint)
329	# - method-component: 7 (rafailov2023dpo, zhao2021calibrate, abdulhai2025consistent, naous2025flipping, li2025persona, wang2024alignment)
330	# - evaluation: 5 (lin2025redial, faisal2024dialectbench, gallegos2024bias, parrish2022bbq, haq2026dialect)
331	# - background: 5 (joshi2025dialect_survey, rickford1999aave, kachru2008cultures, sekulic2024daus, ahmad2025diversity)
332	# - high relevance: 8, medium: 11, low: 1
333	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-13T05:50:03.880265+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
  "old_string": "    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 20 papers\n# - direct-competitor: 0 (novelty confirmed)\n# - foundation: 4 (seshadri2026lost, yao2024taubench, liu2024agentbench, wang2024mint)\n# - method-component: 7 (rafailov2023dpo, zhao2021calibrate, abdulhai2025consistent, naous2025flipping, li2025persona, wang2024alignment)\n# - evaluation: 5 (lin2025redial, faisal2024dialectbench, gallegos2024bias, parrish2022bbq, haq2026dialect)\n# - background: 5 (joshi2025dialect_survey, rickford1999aave, kachru2008cultures, sekulic2024daus, ahmad2025diversity)\n# - high relevance: 8, medium: 11, low: 1",
  "new_string": "    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Anonymous (under review)\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 24 papers (updated 2026-05-13, +4 new)\n# - direct-competitor: 0 (novelty still confirmed)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 8 (+khan2026decoding)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 10, medium: 13, low: 1\n#\n# Scan notes (2026-05-13):\n# - sim2real2026gap is the closest to a competitor: same problem (user simulator infidelity in τ-bench),\n#   but they only diagnose (USI metric + human study), we prescribe (DPO calibration). Cite as motivation.\n# - No direct competitor found in the 2-week window. DemoCalib novelty remains intact.\n# - Also noted but not added (older, tangential):\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Intra-Fairness Dynamics (2602.16438): DPO spillover effects across fairness attributes\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml",
    "old_string": "    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 20 papers\n# - direct-competitor: 0 (novelty confirmed)\n# - foundation: 4 (seshadri2026lost, yao2024taubench, liu2024agentbench, wang2024mint)\n# - method-component: 7 (rafailov2023dpo, zhao2021calibrate, abdulhai2025consistent, naous2025flipping, li2025persona, wang2024alignment)\n# - evaluation: 5 (lin2025redial, faisal2024dialectbench, gallegos2024bias, parrish2022bbq, haq2026dialect)\n# - background: 5 (joshi2025dialect_survey, rickford1999aave, kachru2008cultures, sekulic2024daus, ahmad2025diversity)\n# - high relevance: 8, medium: 11, low: 1",
    "new_string": "    how_we_differ: \"They generate diverse profiles; we calibrate specific behavioral rates to match real dialect group distributions\"\n\n  # ============================================================\n  # NEW ADDITIONS (scan 2026-05-13)\n  # ============================================================\n\n  # --- FOUNDATION (new) ---\n  - id: sim2real2026gap\n    title: \"Mind the Sim2Real Gap in User Simulation for Agentic Tasks\"\n    authors: \"Anonymous (under review)\"\n    venue: \"arXiv 2603.11245\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2603.11245\"\n    category: foundation\n    role: \"First study running full τ-bench protocol with 451 real humans; introduces USI metric to quantify sim-vs-human behavioral divergence\"\n    relevance: high\n    key_findings:\n      - \"LLM simulators are excessively cooperative, stylistically uniform, and lack realistic frustration/ambiguity\"\n      - \"Simulated users create 'easy mode' that inflates agent success rates above human baseline\"\n      - \"Simulated feedback is uniformly positive; humans express calibrated dissatisfaction\"\n      - \"Higher model capability does not yield more faithful user simulation\"\n    how_we_differ: \"They quantify the sim2real gap but do not propose calibration methods; we use DPO to close the behavioral rate gap for specific dialect groups\"\n    scan_date: \"2026-05-13\"\n    note: \"Near-competitor in problem framing — directly validates our motivation. Not a direct competitor because they diagnose without prescribing a fix.\"\n\n  # --- METHOD-COMPONENT (new) ---\n  - id: khan2026decoding\n    title: \"Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation\"\n    authors: \"Khan, Muneeb Ur Raheem\"\n    venue: \"arXiv 2605.02348\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2605.02348\"\n    category: method-component\n    role: \"Decoding-time bias mitigation using Process Reward Model as fairness judge; alternative to our training-time DPO approach\"\n    relevance: medium\n    key_findings:\n      - \"Sequential debiasing raises bias scores by up to +0.40 over baseline while preserving fluency\"\n      - \"No weight changes needed — debiasing happens at inference via PRM scoring\"\n      - \"Gate calibration is model-dependent; no one-size-fits-all prompt works\"\n    how_we_differ: \"They debias at decoding time for general fairness; we train the simulator via DPO to match target behavioral distributions\"\n    scan_date: \"2026-05-13\"\n\n  # --- EVALUATION (new) ---\n  - id: gupta2025endive\n    title: \"EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models\"\n    authors: \"Gupta, Cheung et al.\"\n    venue: \"Findings of EMNLP 2025 (arXiv 2504.07100)\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2504.07100\"\n    category: evaluation\n    role: \"Cross-dialect benchmark covering 5 dialects including AAVE and Indian English — both our target dialects\"\n    relevance: high\n    key_findings:\n      - \"Covers AAVE (33M speakers), Indian English (250M speakers), Jamaican, Chicano, Singaporean English\"\n      - \"Few-shot LLM translation of SE to dialects, validated by native speakers (avg 6.02/7 faithfulness)\"\n      - \"LLMs show performance drops on non-standard dialects across understanding, reasoning, math, logic\"\n    how_we_differ: \"EnDive evaluates NLP task performance across dialects; we calibrate user simulator behavioral rates for those same dialect groups\"\n    scan_date: \"2026-05-13\"\n\n  # --- BACKGROUND (new) ---\n  - id: nakash2026divert\n    title: \"Efficient Agent Evaluation via Diversity-Guided User Simulation\"\n    authors: \"Nakash, Kour, Anaby-Tavor\"\n    venue: \"arXiv 2604.21480\"\n    year: 2026\n    url: \"https://arxiv.org/abs/2604.21480\"\n    category: background\n    role: \"DIVERT framework for efficient agent evaluation via branching trajectories; addresses Monte Carlo inefficiency in agent evaluation\"\n    relevance: medium\n    key_findings:\n      - \"Snapshot-based branching avoids redundant regeneration of early conversation prefixes\"\n      - \"Coverage-guided exploration uncovers deep failure modes from rare user behaviors\"\n    how_we_differ: \"They optimize evaluation efficiency; we optimize user simulator fidelity for dialect groups\"\n    scan_date: \"2026-05-13\"\n\n# ============================================================\n# SUMMARY\n# ============================================================\n# Total: 24 papers (updated 2026-05-13, +4 new)\n# - direct-competitor: 0 (novelty still confirmed)\n# - foundation: 5 (+sim2real2026gap)\n# - method-component: 8 (+khan2026decoding)\n# - evaluation: 6 (+gupta2025endive)\n# - background: 6 (+nakash2026divert)\n# - high relevance: 10, medium: 13, low: 1\n#\n# Scan notes (2026-05-13):\n# - sim2real2026gap is the closest to a competitor: same problem (user simulator infidelity in τ-bench),\n#   but they only diagnose (USI metric + human study), we prescribe (DPO calibration). Cite as motivation.\n# - No direct competitor found in the 2-week window. DemoCalib novelty remains intact.\n# - Also noted but not added (older, tangential):\n#   - ϕ-DPO (2602.22601): Fairness DPO for multimodal continual learning, different domain\n#   - Intra-Fairness Dynamics (2602.16438): DPO spillover effects across fairness attributes\n#   - Linguistic Stereotypes (2603.18729): SAE vs AAE bias in multi-agent architectures"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-13T05:50:03.880562+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/cost-verify-agent-rl/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-scan-retry_20260513T054551",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-13T05:50:03.880769+00:00_

更新完成。总结：

## 文献扫描结果（2026-05-13）

**新增 4 篇论文，无 direct competitor。DemoCalib 新颖性不变。**

### 重点关注

**sim2real2026gap** (arXiv 2603.11245) — "Mind the Sim2Real Gap in User Simulation for Agentic Tasks"
- 首次在 τ-bench 上跑 451 名真人用户，量化 sim2real 行为差距
- 结论：LLM 模拟器"过度合作、风格单一、缺乏真实挫败感"，虚增 agent 成功率
- **与我们最接近**：同一问题空间（τ-bench 模拟器保真度），但只诊断不开药。DemoCalib 的 DPO 校准是对他们发现的直接解决方案。论文中应作为核心 motivation 引用。

### 其他新增

| ID | 论文 | 类别 | 与我们的关系 |
|---|---|---|---|
| khan2026decoding | Decoding-Time Debiasing via PRM (2605.02348, May 4) | method-component | 互补：推理时去偏 vs 我们训练时 DPO |
| gupta2025endive | EnDive: Cross-Dialect Benchmark (EMNLP 2025 Findings) | evaluation | 覆盖 AAVE + Indian English，可引用为评估参照 |
| nakash2026divert | DIVERT: Diversity-Guided User Simulation (2604.21480) | background | 评估效率优化，间接相关 |

### 未收录但值得留意

- ϕ-DPO (2602.22601)：Fairness DPO 变体，但针对多模态持续学习
- Intra-Fairness Dynamics (2602.16438)：DPO 做公平性对齐时的 spillover 效应，写 limitation 时可引用
- Linguistic Stereotypes (2603.18729)：SAE vs AAE 在多 agent 架构中的刻板印象分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-scan-retry_20260513T054551"
}
```

</details>

---
