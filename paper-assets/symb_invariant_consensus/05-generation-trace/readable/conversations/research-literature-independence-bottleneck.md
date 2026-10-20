# research literature independence bottleneck

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_research_literature-independence-bottleneck_20260519T162224.jsonl`
- **Structured JSON:** [`529fa1b143598be5ad08.json`](../../sessions/52/529fa1b143598be5ad08.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-19T16:26:46.914067+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T16:26:46.914434+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T16:26:46.914645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM reasoning diversity self-consistency limitations sampling independence 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM reasoning diversity self-consistency limitations sampling independence 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T16:26:46.914782+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM debate reasoning multi-agent reasoning diversity independence 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM debate reasoning multi-agent reasoning diversity independence 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T16:26:46.914933+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "contrastive reasoning LLM independent constraint generation contrastive decoding 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "contrastive reasoning LLM independent constraint generation contrastive decoding 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T16:26:46.915068+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "test-time compute scaling process reward model diversity 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "test-time compute scaling process reward model diversity 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T16:26:46.915184+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM cannot self-correct self-correction limitations reasoning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM cannot self-correct self-correction limitations reasoning 2024 2025"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T16:26:46.915324+00:00_

Web search results for query: "contrastive reasoning LLM independent constraint generation contrastive decoding 2024 2025"

Links: [{"title":"Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning","url":"https://arxiv.org/html/2602.18232v1"},{"title":"Contrastive Decoding in Language Models","url":"https://www.emergentmind.com/topics/contrastive-decoding"},{"title":"Contrastive Decoding","url":"https://www.aussieai.com/research/contrastive-decoding"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Distillation Contrastive Decoding: Improving LLMs Reasoning with   Contrastive Decoding and Distillation","url":"https://arxiv.org/pdf/2402.14874"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/pdf/2502.09061"},{"title":"Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning","url":"https://arxiv.org/pdf/2602.18232"}]

I've found relevant research on contrastive reasoning, LLM constraint generation, and contrastive decoding. Here are the key findings from 2024-2025:

## Recent Developments in Contrastive Decoding for LLM Reasoning

**Core Technique:**
Contrastive decoding (CD) has recently emerged as a lightweight alternative for enhancing reasoning performance at inference time, without requiring additional training or multiple sampling paths, with existing CD-based methods improving generation quality by contrasting the main model with auxiliary distributions induced by weakened or perturbed contexts, thereby suppressing undesirable token candidates during decoding.

**Confidence-Driven Approaches:**
Recent evidence suggests that controlled modification of internal logit and attention distributions can enhance reasoning fidelity in LLMs. Unlike test-time scaling, contrastive decoding has recently emerged as a lightweight alternative for enhancing reasoning performance at inferenc
…[truncated 900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-19T16:26:46.915489+00:00_

Web search results for query: "LLM reasoning diversity self-consistency limitations sampling independence 2024 2025"

Links: [{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling | Request PDF","url":"https://www.researchgate.net/publication/392503883_Reasoning_Aware_Self-Consistency_Leveraging_Reasoning_Paths_for_Efficient_LLM_Sampling"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.184/"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for   Efficient LLM Sampling","url":"https://arxiv.org/pdf/2408.17017"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Expanding Search Space with Diverse Prompting Agents: An Efficient   Sampling Approach for LLM Mathematical Reasoning","url":"https://arxiv.org/pdf/2410.09780"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"}]

I've completed a web search for your query on LLM reasoning diversity, self-consistency, limitations, and sampling independence from 2024-2025. Here are the key findings:

## Self-Consistency and Sampling

Self-Consistency (SC) is a decoding strategy that enhances reasoning performance by sampling multiple reasoning paths and marginalizing over these samples. However, SC's effectiveness is tied to the number of reasoning paths sampled, creating a trade-off between performance and computational cost, with no systematic method to determine the optimal number of samples for any given task.

## Recent Limitations Identified

A critical limitation is that these approaches treat all samples equally for sampling decisions, basing stopping criteria solely on the consis
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T16:26:46.915649+00:00_

Web search results for query: "test-time compute scaling process reward model diversity 2025 2026"

Links: [{"title":"Test-Time Scaling with Diffusion Language Models via Reward-Guided Stitching","url":"https://arxiv.org/pdf/2602.22871"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via   Generative Reasoning","url":"https://arxiv.org/pdf/2504.00891"},{"title":"What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/pdf/2602.01070"},{"title":"Mode-Conditioning Unlocks Superior Test-Time Scaling","url":"https://arxiv.org/pdf/2512.01127"},{"title":"Scaling Test-Time Compute to Achieve IOI Gold Medal with Open-Weight Models","url":"https://arxiv.org/pdf/2510.14232"},{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time   Scaling","url":"https://arxiv.org/pdf/2502.06703"},{"title":"(PDF) Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://www.researchgate.net/publication/392466011_Revisiting_Test-Time_Scaling_A_Survey_and_a_Diversity-Aware_Method_for_Efficient_Reasoning"},{"title":"From Mathematical Reasoning to Code: Generalization of Process Reward Models in Test-Time Scaling","url":"https://arxiv.org/pdf/2506.00027"}]

Based on the search results, here's what I found about test-time compute scaling with process reward models and diversity in 2025-2026:

## Key Recent Research

**Test-Time Scaling Overview:**
Test-Time Scaling (TTS) methods are increasingly being researched to improve the reasoning performance of LLMs, with scaling test-time compute becoming central to frontier reasoning systems.

**Process Reward Models (PRMs):**
Effective TTS requires high-quality verifiers, such as Process Reward Models (PRMs). However, existing PRMs exhibit limited process supervision capabilities and struggle to generalize across different models and tasks.

**Diversity and Diversity Collapse:**
While parallel scaling relies on the model generating diverse and 
…[truncated 696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T16:26:46.915819+00:00_

Web search results for query: "LLM debate reasoning multi-agent reasoning diversity independence 2024 2025"

Links: [{"title":"Multi-Agent Debate Strategies","url":"https://www.emergentmind.com/topics/multi-agent-debate-mad-strategies"},{"title":"Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.992/"},{"title":"Prepare Reasoning Language Models for Multi-Agent Debate","url":"https://www.arxiv.org/pdf/2601.22297"},{"title":"Multi-Agent Debate Frameworks","url":"https://www.emergentmind.com/topics/multi-agent-debate-mad-frameworks"},{"title":"Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning","url":"https://arxiv.org/pdf/2511.07784"},{"title":"ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning","url":"https://arxiv.org/pdf/2602.00127"},{"title":"Improving factuality and reasoning in language models through multiagent debate | Proceedings of the 41st International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3692070.3692537"},{"title":"From Belief Entrenchment to Robust Reasoning in LLM Agents","url":"https://arxiv.org/pdf/2503.16814"}]

Based on the search results, here's what I found regarding LLM debate reasoning, multi-agent reasoning, diversity, and independence in 2024-2025:

## Key Research Areas

**Multi-Agent Debate Frameworks**

Multi-Agent Debate frameworks provide an expressive mechanism to harness the merits of collective reasoning, divergent exploration, and collaborative correction in LLMs. The Multi-Agent Debate (MAD) framework has multiple agents express their arguments in a "tit for tat" state with a judge managing the debate process, which encourages divergent thinking in LLMs for tasks requiring deep contemplation.

**Diversity and Agent Heterogeneity**

Deploying agents based on different foundation models or architectures (e.g., Gemini-Pro, PaLM 2-M, M
…[truncated 1060 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T16:26:46.916023+00:00_

Web search results for query: "LLM cannot self-correct self-correction limitations reasoning 2024 2025"

Links: [{"title":"[PDF] Large Language Models Cannot Self-Correct Reasoning Yet | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-Cannot-Self-Correct-Reasoning-Huang-Chen/6d4bacb69923e1e94fb4de468b939ce6db32fb51"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/abs/2310.01798"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.714/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"},{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"}]

Based on the search results, here's what recent research shows about LLM self-correction limitations:

## Key Findings on LLM Self-Correction Limitations

LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction.

### Intrinsic Self-Correction Challenges

The self-correction capability has been shown to be severely lacking in current LLMs, especially in the absence of external input (also called intri
…[truncated 975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T16:26:46.916205+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency LLM diversity collapse sampling bias same model 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency LLM diversity collapse sampling bias same model 2024 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-19T16:26:46.916330+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"encouraging divergent thinking\" LLM multi-agent debate EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"encouraging divergent thinking\" LLM multi-agent debate EMNLP 2024"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T16:26:46.916444+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CRANE constrained reasoning LLM generation 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CRANE constrained reasoning LLM generation 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-19T16:26:46.916557+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"mode conditioning\" test-time scaling diversity collapse reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"mode conditioning\" test-time scaling diversity collapse reasoning 2025"
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T16:26:46.916666+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-correction\" LLM survey critical mistakes external feedback 2025 TACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-correction\" LLM survey critical mistakes external feedback 2025 TACL"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T16:26:46.916799+00:00_

Web search results for query: "CRANE constrained reasoning LLM generation 2025 arxiv"

Links: [{"title":"Paper page - CRANE: Reasoning with constrained LLM generation","url":"https://huggingface.co/papers/2502.09061"},{"title":"[Literature Review] CRANE: Reasoning with constrained LLM generation","url":"https://www.themoonlight.io/en/review/crane-reasoning-with-constrained-llm-generation"},{"title":"[2502.09061] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061"},{"title":"[2502.09061v2] CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/abs/2502.09061v2"},{"title":"CRANE: Reasoning with constrained LLM generation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/crane-reasoning-constrained-llm-generation"},{"title":"CRANE: Reasoning with constrained LLM generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250209061B/abstract"},{"title":"Fast Controlled Generation from Language Models with Adaptive Weighted Rejection Sampling","url":"https://arxiv.org/html/2504.05410v1"},{"title":"Reasoning with constrained LLM generation - CRANE","url":"https://arxiv.org/pdf/2502.09061"},{"title":"CRANE: Reasoning with constrained LLM generation","url":"https://arxiv.org/html/2502.09061v1"}]

Based on the search results, I found information about CRANE: Reasoning with constrained LLM generation from 2025.

## Overview

CRANE addresses code generation, symbolic math reasoning, and other tasks that require LLMs to produce outputs that are both syntactically and semantically correct.

## The Core Problem

Constrained LLM generation is a promising direction to enforce adherence to formal grammar, but strict enforcement of formal constraints often diminishes the reasoning capabilities of LLMs. The paper provides a theoretical explanation for why constraining LLM outputs to very restrictive grammars that only allow syntactically valid final answers reduces the reasoning capabilities of 
…[truncated 898 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-19T16:26:46.916980+00:00_

Web search results for query: ""encouraging divergent thinking" LLM multi-agent debate EMNLP 2024"

Links: [{"title":"Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.992/"},{"title":"Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate","url":"https://iclr.cc/media/iclr-2025/Slides/28079.pdf"},{"title":"Encouraging Divergent Thinking in Large Language Models through   Multi-Agent Debate","url":"https://arxiv.org/pdf/2305.19118"},{"title":"Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate","url":"https://arxiv.org/html/2305.19118v4"},{"title":"Multiple LLM Agents Debate for Equitable Cultural Alignment","url":"https://arxiv.org/html/2505.24671v1"},{"title":"Multi-Agent Debate - AgentScope","url":"https://doc.agentscope.io/tutorial/workflow_multiagent_debate.html"},{"title":"Agree or Disagree: A Review of Multi-Agent Debate","url":"https://hungleai.substack.com/p/agree-or-disagree-a-review-of-multi"},{"title":"(PDF) Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate","url":"https://www.researchgate.net/publication/386185857_Encouraging_Divergent_Thinking_in_Large_Language_Models_through_Multi-Agent_Debate"},{"title":"[2305.19118] Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate","url":"https://arxiv.org/abs/2305.19118"}]

I found relevant results for your search! Here's what I found:

## "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate"

This is a paper by Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, and Zhaopeng Tu, published in 2024 at the Conference on Empirical Methods in Natural Language Processing (EMNLP) in Miami, Florida.

### Key Findings:

The paper proposes a Multi-Agent Debate (MAD) framework, in which multiple agents express their arguments in the state o
…[truncated 811 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T16:26:46.917153+00:00_

Web search results for query: "self-consistency LLM diversity collapse sampling bias same model 2024 arxiv"

Links: [{"title":"(PDF) Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://www.researchgate.net/publication/396095169_Verbalized_Sampling_How_to_Mitigate_Mode_Collapse_and_Unlock_LLM_Diversity"},{"title":"Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/html/2510.01171v3"},{"title":"Estimating the Self-Consistency of LLMs","url":"https://arxiv.org/pdf/2509.19489"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"arXiv:2311.16822v2 [cs.LG] 17 Jun 2024","url":"https://arxiv.org/pdf/2311.16822"},{"title":"VERBALIZED SAMPLING","url":"https://openreview.net/pdf/8a33b3e21a2ac895129060085579b4ec72c433d6.pdf"},{"title":"[2510.01171] Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/abs/2510.01171"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning","url":"https://arxiv.org/pdf/2511.01490"}]

I found several relevant papers from arxiv that relate to your search query. Here are the key findings:

## Self-Consistency and Diversity Issues

Self-Consistency Improves Chain of Thought Reasoning in Language Models (Wang et al., 2023, published at ICLR), which is a foundational work on the self-consistency method.

More recent work addresses problems with sampling from the same model. Research shows that typicality bias in preference data is a fundamental cause of mode collapse, reducing output diversity, and proposes Verbalized Sampling (VS), a prompting method that returns distributions of responses to improve diversity.

## Diversity Collapse Issues

When repeatedly training new models
…[truncated 966 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T16:26:46.917325+00:00_

Web search results for query: ""self-correction" LLM survey critical mistakes external feedback 2025 TACL"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/ojs/index.php/tacl/article/view/6755"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.78/"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00713/125177/When-Can-LLMs-Actually-Correct-Their-Own-Mistakes"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://arxiv.org/html/2406.01297v3"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"(PDF) When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/381152815_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of   Self-Correction of LLMs","url":"https://arxiv.org/pdf/2406.01297"},{"title":"GitHub - ryokamoi/llm-self-correction-papers: List of papers on Self-Correction of LLMs. · GitHub","url":"https://github.com/ryokamoi/llm-self-correction-papers"}]

I found the paper you're looking for! "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs" was published in TA
…[truncated 1313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T16:26:46.917487+00:00_

Web search results for query: ""mode conditioning" test-time scaling diversity collapse reasoning 2025"

Links: [{"title":"Mode-Conditioning Unlocks Superior Test-Time Scaling","url":"https://arxiv.org/html/2512.01127v1"},{"title":"Preprint Mode-Conditioning Unlocks Superior Test-Time Scaling Chen Henry Wu,","url":"https://www.arxiv.org/pdf/2512.01127"},{"title":"Mode-Conditioning Unlocks Superior Test-Time Compute Scaling","url":"https://openreview.net/pdf?id=hlTteJckoB"},{"title":"Mode-Conditioning Unlocks Superior Test-Time Scaling","url":"https://arxiv.org/pdf/2512.01127"},{"title":"[2512.01127] Mode-Conditioning Unlocks Superior Test-Time Scaling","url":"https://arxiv.org/abs/2512.01127"},{"title":"(PDF) Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://www.researchgate.net/publication/392466011_Revisiting_Test-Time_Scaling_A_Survey_and_a_Diversity-Aware_Method_for_Efficient_Reasoning"}]

Based on the search results, here's what I found about mode conditioning, test-time scaling, and diversity collapse:

## Overview

Parallel sampling promises substantial gains in test-time scaling, but its effectiveness is sharply limited by diversity collapse, where models concentrate on a few modes and repeated samples produce the same mistakes.

## The Mode-Conditioning Framework

The mode-conditioning (ModC) framework explicitly allocates test-time compute across reasoning modes using either specialist models or mode-specific prefixes. ModC consistently improves scaling across controlled graph-search tasks and large-scale reasoning benchmarks, spanning model families and sizes from 0.5B to 7B.

## Key Results

On OpenThoughts, fine-tuning Qwen2.5-7B with ModC achieves a 4× efficiency gain over standard training while also improving the maximum attainable Pass@k. Additionally, gradient clustering enables ModC without explicit mode labels, yielding up to 10% gains on datasets such as NuminaMath.

ModC improves reinfor
…[truncated 468 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T16:26:46.917679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"breaking mental set\" multi-agent debate diverse reasoning ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"breaking mental set\" multi-agent debate diverse reasoning ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-19T16:26:46.917803+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "GenPRM process reward model generative reasoning test-time compute 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "GenPRM process reward model generative reasoning test-time compute 2025"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T16:26:46.917935+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"can LLM agents really debate\" controlled study multi-agent logical reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"can LLM agents really debate\" controlled study multi-agent logical reasoning 2025"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-19T16:26:46.918051+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM self-correction key condition verification EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM self-correction key condition verification EMNLP 2024"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T16:26:46.918161+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"revisiting test-time scaling\" survey diversity-aware efficient reasoning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"revisiting test-time scaling\" survey diversity-aware efficient reasoning 2025"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-19T16:26:46.918278+00:00_

Web search results for query: ""revisiting test-time scaling" survey diversity-aware efficient reasoning 2025"

API Error: 503 Server tool validation is temporarily unavailable. Please try again. This is a server-side issue, usually temporary — try again in a moment. If it persists, check status.claude.com.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T16:26:46.918422+00:00_

Web search results for query: ""breaking mental set" multi-agent debate diverse reasoning ICLR 2025"

Links: [{"title":"Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate","url":"https://iclr.cc/media/iclr-2025/Slides/28079.pdf"},{"title":"Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/3de667dab3b3d812583abc0a786139a0-Abstract-Conference.html"},{"title":"GitHub - MraDonkey/DMAD: [ICLR 2025] Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate · GitHub","url":"https://github.com/MraDonkey/DMAD"},{"title":"ICLR Poster Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate","url":"https://iclr.cc/virtual/2025/poster/28079"},{"title":"Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate | OpenReview","url":"https://openreview.net/forum?id=t6QHYUOQL7"},{"title":"Free-MAD: Consensus-Free Multi-Agent Debate","url":"https://www.researchgate.net/publication/395526198_Free-MAD_Consensus-Free_Multi-Agent_Debate"},{"title":"Downloads 2025","url":"https://iclr.cc/Downloads/2025"},{"title":"ENCOURAGING CRITICAL THINKING FOR MULTI","url":"https://openreview.net/pdf/e4e36f9dc875aba53ed372517357cb765839bfa5.pdf"},{"title":"Learning to Break: Knowledge-Enhanced Reasoning in Multi-Agent Debate   System","url":"https://arxiv.org/pdf/2312.04854"}]

Based on the web search results, I found comprehensive information about this paper:

## Overview

"Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate" is presented at ICLR 2025. Large Language Models (LLMs) have seen significant progress but continue to struggle with persistent reasoning mistakes, with previous self-reflection methods proven limited due to the models' inherent fixed thinking patterns.

## The Problem

While Multi-Agent Debate (MAD) attempts to mitigate this by incorporating multiple agents, it often employs the same re
…[truncated 1029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T16:26:46.918591+00:00_

Web search results for query: ""can LLM agents really debate" controlled study multi-agent logical reasoning 2025"

Links: [{"title":"[2511.07784] Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning","url":"https://arxiv.org/abs/2511.07784"},{"title":"Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning | alphaXiv","url":"https://www.alphaxiv.org/overview/2511.07784v1"},{"title":"[PDF] Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-LLM-Agents-Really-Debate-A-Controlled-Study-of-Wu-Li/8f05bac54b47e4ab8a035e36731764165fe857a3"},{"title":"Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning","url":"https://arxiv.org/html/2511.07784v1"},{"title":"Can LLM Agents Really Debate? A Controlled Study of ...","url":"https://arxiv.org/pdf/2511.07784"},{"title":"Debate or Vote: Which Yields Better Decisions in Multi-Agent ...","url":"https://www.emergentmind.com/papers/2508.17536"},{"title":"AI agents debate their way to improved mathematical reasoning","url":"https://techxplore.com/news/2025-12-ai-agents-debate-mathematical.html"},{"title":"Multi-LLM-Agents Debate - Performance, Efficiency, and Scaling Challenges | ICLR Blogposts 2025","url":"https://d2jud02ci9yv69.cloudfront.net/2025-04-28-mad-159/blog/mad/"}]

I found a highly relevant study that directly matches your search query. Here are the key findings:

## Study Overview

Multi-agent debate (MAD) has recently emerged as a promising framework for improving the reasoning performance of large language models (LLMs), but whether LLM agents can genuinely engage in deliberative reasoning beyond simple ensembling or majority voting remains unclear. Researchers addressed this question through a controlled study using the Knight–Knave–Spy logic puzzle, which enables precise, step-wise evaluation of de
…[truncated 1025 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T16:26:46.918755+00:00_

Web search results for query: "GenPRM process reward model generative reasoning test-time compute 2025"

Links: [{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://ryanliu112.github.io/GenPRM/"},{"title":"Paper page - GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://huggingface.co/papers/2504.00891"},{"title":"[PDF] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GenPRM:-Scaling-Test-Time-Compute-of-Process-Reward-Zhao-Liu/bd94932b7604933a11d1538b0de6f9543089711f"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/genprm-scaling-test-time-compute-process-reward"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"}]

Based on the search results, I found comprehensive information about GenPRM:

## GenPRM Overview

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step.

## Key Challenges Addressed

Current PRMs face three key challenges: (1) limited process supervision and generalization capabilities, (2) dependence on scalar value prediction without leveraging the generative abilities of LLMs, and (3) inability to scale the test-time compute of PRMs.

## How GenPRM Differs

GenPRM redefines process supervision as a genera
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T16:26:46.918929+00:00_

Web search results for query: "LLM self-correction key condition verification EMNLP 2024"

Links: [{"title":"[Quick Review] Large Language Models Can Self-Correct with Key Condition Verification","url":"https://liner.com/review/large-language-models-can-selfcorrect-with-key-condition-verification"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.714/"},{"title":"[Literature Review] Large Language Models Can Self-Correct with Key Condition Verification","url":"https://www.themoonlight.io/en/review/large-language-models-can-self-correct-with-key-condition-verification"},{"title":"[2405.14092] Large Language Models Can Self-Correct with Key Condition Verification","url":"https://arxiv.org/abs/2405.14092"},{"title":"[2405.14092v3] Large Language Models Can Self-Correct with Key Condition Verification","url":"https://arxiv.org/abs/2405.14092v3"},{"title":"Large Language Models Can Self-Correct with Key ...","url":"https://aclanthology.org/2024.emnlp-main.714.pdf"},{"title":"Large Language Models Can Self-Correct with Key Condition Verification","url":"https://arxiv.org/pdf/2405.14092"},{"title":"LLM Self-Correction with DeCRIM: Decompose, Critique, and Refine for Enhanced Following of Instructions with Multiple Constraints - ACL Anthology","url":"https://aclanthology.org/2024.findings-emnlp.458/"},{"title":"Findings - EMNLP 2024","url":"https://2024.emnlp.org/program/accepted_findings/"}]

Based on the search results, here's what I found about the EMNLP 2024 paper on LLM self-correction with key condition verification:

## Paper Overview

The paper is titled "Large Language Models Can Self-Correct with Key Condition Verification" and was presented at the 2024 Conference on Empirical Methods in Natural Language Processing in Miami, Florida. The authors are Zhenyu Wu, Qingkai Zeng, Zhihan Zhang, Zhaoxuan Tan, Chao Shen, and Meng Jiang.

## Key Contribution

The paper proposes 
…[truncated 867 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T16:26:46.919106+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "revisiting test-time scaling survey diversity-aware efficient reasoning 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "revisiting test-time scaling survey diversity-aware efficient reasoning 2025 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-19T16:26:46.919229+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"expanding search space\" diverse prompting agents LLM mathematical reasoning sampling 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"expanding search space\" diverse prompting agents LLM mathematical reasoning sampling 2024"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T16:26:46.919343+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"thinking by subtraction\" confidence contrastive decoding LLM reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"thinking by subtraction\" confidence contrastive decoding LLM reasoning 2026"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-19T16:26:46.919455+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM self-correction reinforcement learning self-refine intrinsic 2025 ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM self-correction reinforcement learning self-refine intrinsic 2025 ICLR"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T16:26:46.919562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"ALIGN\" multi-agent LLM reasoning performance guarantees delegation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"ALIGN\" multi-agent LLM reasoning performance guarantees delegation 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T16:26:46.919693+00:00_

Web search results for query: ""expanding search space" diverse prompting agents LLM mathematical reasoning sampling 2024"

Links: [{"title":"[2410.09780] Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning","url":"https://arxiv.org/abs/2410.09780"},{"title":"(PDF) Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning","url":"https://www.researchgate.net/publication/384929093_Expanding_Search_Space_with_Diverse_Prompting_Agents_An_Efficient_Sampling_Approach_for_LLM_Mathematical_Reasoning"},{"title":"Expanding Search Space with Diverse Prompting Agents: An Efficient   Sampling Approach for LLM Mathematical Reasoning","url":"https://arxiv.org/pdf/2410.09780"},{"title":"Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning","url":"https://arxiv.org/html/2410.09780"},{"title":"GitHub - AGI-Edgerunners/LLM-Agents-Papers: A repo lists papers related to LLM based agent · GitHub","url":"https://github.com/AGI-Edgerunners/LLM-Agents-Papers"}]

I found the research paper you're looking for. Here's what the search revealed:

"Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning" is a research study that performs an experimental analysis of distinct prompting methods within mathematical reasoning, demonstrating that each method explores a distinct search space, with differentiation becoming more evident with increasing problem complexity.

The study applies an efficient sampling process that uniformly combines samples from diverse methods, which expands the maximum search space and achieves higher performance with fewer runs compared to single methods. Notably, for difficult questions in the MATH-hard dataset, maximum search space was achieved while utilizing approximately 43% fewer runs than single methods on average.

The resear
…[truncated 537 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-19T16:26:46.919857+00:00_

Web search results for query: ""thinking by subtraction" confidence contrastive decoding LLM reasoning 2026"

Links: [{"title":"Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning","url":"https://arxiv.org/html/2602.18232v1"},{"title":"[2602.18232] Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning","url":"https://arxiv.org/abs/2602.18232"},{"title":"Confidence-Driven Contrastive Decoding for LLM Reasoning","url":"https://arxiv.org/pdf/2602.18232"},{"title":"Contrastive Thinking Decoding can Improve Answers for Reasoning Models | OpenReview","url":"https://openreview.net/forum?id=czozyUMx2M"},{"title":"Distillation Contrastive Decoding: Improving LLMs Reasoning with   Contrastive Decoding and Distillation","url":"https://arxiv.org/pdf/2402.14874"}]

Based on the search results, I found a highly relevant paper on your topic:

## "Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning"

The paper proposes "Thinking by Subtraction," a confidence-driven contrastive decoding approach that improves reasoning reliability through targeted token-level intervention.

**Key Innovation:** The method detects low-confidence tokens during decoding and intervenes selectively at these positions by constructing a contrastive reference with minimal placeholders for high-confidence tokens, then refining predictions by subtracting this reference distribution at low-confidence locations.

**Motivation:** The approach is motivated by the observation that reasoning uncertainty is highly localized—a small subset of low-confidence tokens disproportionately contributes to reasoning errors and unnecessary output expansion.

**Context:** Contrastive decoding has recently emerged as a lightweight alternative for enhancing reasoning performance at inference time, without requiring additional training or multiple sampling paths.

The paper was published in February 2026 (arXiv preprint 2602.18232) and represent
…[truncated 182 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T16:26:46.920037+00:00_

Web search results for query: "revisiting test-time scaling survey diversity-aware efficient reasoning 2025 arxiv"

Links: [{"title":"[2506.04611v1] Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"http://arxiv.org/abs/2506.04611v1"},{"title":"[2506.04611] Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://arxiv.org/abs/2506.04611"},{"title":"(PDF) Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://www.researchgate.net/publication/392466011_Revisiting_Test-Time_Scaling_A_Survey_and_a_Diversity-Aware_Method_for_Efficient_Reasoning"},{"title":"[Literature Review] Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://www.themoonlight.io/en/review/revisiting-test-time-scaling-a-survey-and-a-diversity-aware-method-for-efficient-reasoning"},{"title":"Revisiting Test-Time Scaling: A Survey and a Diversity- ...","url":"https://arxiv.org/pdf/2506.04611"},{"title":"Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning | OpenReview","url":"https://openreview.net/forum?id=xwh5m2zGjb"},{"title":"Input-Time Scaling","url":"https://arxiv.org/html/2508.13654v2"}]

I found the paper you're looking for! Here's what the search revealed:

## Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning

Test-Time Scaling (TTS) improves the reasoning performance of Large Language Models (LLMs) by allocating additional compute during inference.

**Survey Structure:**
The paper conducts a structured survey of TTS methods and categorizes them into sampling-based, search-based, and trajectory optimization strategies.

**Key Finding:**
The authors observe that reasoning-optimized models often produce less diverse outputs, which limits TTS effectiveness.

**Proposed Solution:**
To address this, they propose ADA
…[truncated 602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-19T16:26:46.920195+00:00_

Web search results for query: ""ALIGN" multi-agent LLM reasoning performance guarantees delegation 2025 2026"

Links: [{"title":"ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning","url":"https://arxiv.org/pdf/2602.00127"},{"title":"ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260200127Z/abstract"},{"title":"[2602.00127] ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning","url":"https://arxiv.org/abs/2602.00127"},{"title":"ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning","url":"https://arxiv.org/html/2602.00127v1"},{"title":"Competitive Multi-Agent Delegation for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=nDdpp0285M"}]

Based on the search results, I found detailed information about ALIGN:

## ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning

ALIGN is a novel method that formulates LLM reasoning as an aligned delegation game, where a principal delegates a task to multiple agents that generate candidate solutions under designed incentives, and then selects among their outputs to produce a final answer.

### Key Features

This formulation induces structured interaction among agents while preserving alignment between agent and principal objectives.

### Performance Guarantees

The method establishes theoretical guarantees showing that, under a fair comparison with equal access to candidate solutions, ALIGN provably improves expected performance over single-agent generation, and the analysis accommodates correlated candidate answers and relaxes independence assumptions that are commonly used in prior work.

### Empirical Results

Empirical results across a broad range of LLM reasoning benchmarks consistently demonstrate that ALIGN outperforms strong single-agent and ensemble baselines.

The research was published on J
…[truncated 453 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T16:26:46.920358+00:00_

Web search results for query: "LLM self-correction reinforcement learning self-refine intrinsic 2025 ICLR"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"},{"title":"ReVISE: Learning to Refine at Test-Time via Intrinsic Self-Verification","url":"https://arxiv.org/pdf/2502.14565"},{"title":"Large Language Models have Intrinsic Self-Correction Ability | OpenReview","url":"https://openreview.net/forum?id=pTyEnkuSQ0"},{"title":"Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.24726"},{"title":"2024-10-7 Training Language Models to Self-Correct via Reinforcement Learning","url":"https://arxiv.org/pdf/2409.12917"},{"title":"GitHub - ryokamoi/llm-self-correction-papers: List of papers on Self-Correction of LLMs. · GitHub","url":"https://github.com/ryokamoi/llm-self-correction-papers"},{"title":"Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs","url":"https://arxiv.org/pdf/2410.23912"},{"title":"S$^2$R: Teaching LLMs to Self-verify and Self-correct via Reinforcement   Learning","url":"https://arxiv.org/pdf/2502.12853"}]

I found several relevant papers on LLM self-correction and reinforcement learning. Here are the key findings:

## Main Results

SCoRe is a multi-turn RL approach for teaching LLMs how to correct their own mistakes, achieving an absolute 15.6% gain on self-correction for reasoning problems from MATH and an absolute 9.1% gain on coding problems from HumanEval. The design of SCoRe is motivated by studying the failure modes of SFT and standard RL approaches, which indicate that reinforcement learning plays an essential role in self-trained self-correction.

## Other Related Work

ReVISE involves self-verification and reasoning correction using curriculum learning with preference pairs, achieving natural test-time scaling by integrating self-verification a
…[truncated 761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T16:26:46.920529+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"distillation contrastive decoding\" improving LLM reasoning 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"distillation contrastive decoding\" improving LLM reasoning 2024"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-19T16:26:46.920650+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SCoRe training language models self-correct reinforcement learning ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SCoRe training language models self-correct reinforcement learning ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T16:26:46.920763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"compute optimal\" test-time scaling 1B surpass 405B rethinking 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"compute optimal\" test-time scaling 1B surpass 405B rethinking 2025"
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-19T16:26:46.920888+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"scientific knowledge\" decoding constraints LLM reliability 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"scientific knowledge\" decoding constraints LLM reliability 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T16:26:46.921005+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"verbalized sampling\" mode collapse LLM diversity prompting 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"verbalized sampling\" mode collapse LLM diversity prompting 2025"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T16:26:46.921134+00:00_

Web search results for query: "SCoRe training language models self-correct reinforcement learning ICLR 2025"

Links: [{"title":"Training Language Models to Self-Correct via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=CjwERcAU7w"},{"title":"[Quick Review] Training Language Models to Self-Correct via Reinforcement Learning","url":"https://liner.com/review/training-language-models-to-selfcorrect-via-reinforcement-learning"},{"title":"Training Language Models to Self-Correct via Reinforcement Learning","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/871ac99fdc5282d0301934d23945ebaa-Abstract-Conference.html"},{"title":"[2409.12917] Training Language Models to Self-Correct via Reinforcement Learning","url":"https://arxiv.org/abs/2409.12917"},{"title":"2024-10-7 Training Language Models to Self-Correct via Reinforcement Learning","url":"https://arxiv.org/pdf/2409.12917"},{"title":"TRAINING LANGUAGE MODELS TO SELF-CORRECT","url":"https://openreview.net/pdf?id=CjwERcAU7w"},{"title":"ICLR 2025 Training Language Models to Self-Correct via Reinforcement Learning Oral","url":"https://iclr.cc/virtual/2025/oral/31899"}]

Based on the search results, here's what I found about SCoRe:

## Overview

SCoRe is a multi-turn online reinforcement learning approach that significantly improves an LLM's self-correction ability using entirely self-generated data. SCoRe trains only a single model that can both produce a response to a problem and also correct errors without any oracle feedback.

## Key Challenges Addressed

Prior approaches fall prey to either distribution shift, where trained models can correct base model errors but gains don't transfer to self-correction under the learned model's own mistakes, or behavior collapse, where learning simply produces the best first-attempt response followed by superficial modifications in the second attempt.

## Technical Approach

SCoRe addresses these challenges by training under the model's own dist
…[truncated 740 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-19T16:26:46.921288+00:00_

Web search results for query: ""distillation contrastive decoding" improving LLM reasoning 2024"

Links: [{"title":"GitHub - pphuc25/distil-cd: Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation","url":"https://github.com/pphuc25/distil-cd"},{"title":"Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation","url":"https://arxiv.org/html/2402.14874v1"},{"title":"[2402.14874] Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation","url":"https://arxiv.org/abs/2402.14874"},{"title":"Distillation Contrastive Decoding: Improving LLMs Reasoning with   Contrastive Decoding and Distillation","url":"https://arxiv.org/pdf/2402.14874"},{"title":"Merge, Ensemble, and Cooperate! A Survey on Collaborative Strategies in the Era of Large Language Models","url":"https://arxiv.org/html/2407.06089v1"},{"title":"Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation | OpenReview","url":"https://openreview.net/forum?id=Jk4zg8ET7e"},{"title":"Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/distillation-contrastive-decoding-improving-llms-reasoning-contrastive"},{"title":"DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs","url":"https://arxiv.org/html/2503.07067v1"}]

Based on the search results, here's what I found about distillation contrastive decoding for improving LLM reasoning in 2024:

## Overview

Distillation Contrastive Decoding (DCD) is a novel approach designed to enhance the reasoning capabilities of large language models (LLMs) during inference, introduced by Phuc Phan, Hieu Tran, and Long Phan in 2024.

## Key Innovation

DCD employs Contrastive Chain-of-thought Prompting and advanced distillation techniques, including Dropout and Quantiza
…[truncated 986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T16:26:46.921451+00:00_

Web search results for query: ""compute optimal" test-time scaling 1B surpass 405B rethinking 2025"

Links: [{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling","url":"https://ryanliu112.github.io/compute-optimal-tts/"},{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling | alphaXiv","url":"https://www.alphaxiv.org/resources/2502.06703v1"},{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling | OpenReview","url":"https://openreview.net/forum?id=CvjX9Lhpze"},{"title":"Paper page - Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling","url":"https://huggingface.co/papers/2502.06703"},{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling","url":"https://arxiv.org/html/2502.06703v1"},{"title":"[2502.06703] Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling","url":"https://arxiv.org/abs/2502.06703"},{"title":"ICLR Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling","url":"https://iclr.cc/virtual/2025/32788"},{"title":"GitHub - RyanLiu112/compute-optimal-tts: Official codebase for \"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\". · GitHub","url":"https://github.com/RyanLiu112/compute-optimal-tts"},{"title":"Can 1B LLM Surpass 405B LLM? Rethinking Compute- ...","url":"https://arxiv.org/pdf/2502.06703"}]

Based on the search results, here's what I found about this research:

## Overview

The paper "Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling" was published in 2025 as an arXiv preprint (arXiv:2502.06703).

## Key Findings

Test-Time Scaling (TTS) is an important method for improving the performance of Large Language Models (LLMs) by using additional computation during the inference phase. 

The research addresses two core questions:
1. What is the optimal approach to scale test-time computation across different policy models, PRM
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-19T16:26:46.921628+00:00_

Web search results for query: ""verbalized sampling" mode collapse LLM diversity prompting 2025"

Links: [{"title":"Paper page - Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://huggingface.co/papers/2510.01171"},{"title":"[2510.01171v2] Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/abs/2510.01171v2"},{"title":"GitHub - CHATS-lab/verbalized-sampling: Verbalized Sampling, a training-free prompting strategy to mitigate mode collapse in LLMs by requesting responses with probabilities. Achieves 2-3x diversity improvement while maintaining quality. Model-agnostic framework with CLI/API for creative writing, synthetic data generation, and dialogue simulation. · GitHub","url":"https://github.com/CHATS-lab/verbalized-sampling"},{"title":"Verbalized Sampling: Unlock LLM Diversity | by Kamalmeet Singh | Medium","url":"https://medium.com/@kamalmeet/verbalized-sampling-unlock-llm-diversity-101e4de1b4a3"},{"title":"[2510.01171] Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/abs/2510.01171"},{"title":"Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://arxiv.org/html/2510.01171v3"},{"title":"Verbalized Sampling","url":"https://www.verbalized-sampling.com/"},{"title":"(PDF) Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity","url":"https://www.researchgate.net/publication/396095169_Verbalized_Sampling_How_to_Mitigate_Mode_Collapse_and_Unlock_LLM_Diversity"},{"title":"Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity | OpenReview","url":"https://openreview.net/forum?id=9jQkmGunGo"}]

Based on the search results, I found comprehensive information about Verbalized Sampling (VS) and its approach to addressing mode collapse in LLMs.

## Overview

Post-training alignment often reduces LLM diversity, leading to a phenomenon known as mode collapse.
…[truncated 1474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T16:26:46.921788+00:00_

Web search results for query: ""scientific knowledge" decoding constraints LLM reliability 2025 2026"

Links: [{"title":"[2604.06603v1] Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/abs/2604.06603v1"},{"title":"[2604.06603] Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/abs/2604.06603"},{"title":"Scientific Knowledge-driven Decoding Constraints Improving the Reliability of LLMs","url":"https://arxiv.org/html/2604.06603v1"},{"title":"Guidance Microsoft Library: Controlled Decoding for LLMs 2026","url":"https://johal.in/guidance-microsoft-library-controlled-decoding-for-llms-2026-3/"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2503.15299"}]

I found relevant results for your search query. Here's what the research shows:

## Scientific Knowledge-driven Decoding Constraints for LLM Reliability

Large language models have shown strong knowledge reserves and task-solving capabilities, but still face the challenge of severe hallucination, hindering their practical application. 

A recent approach called SciDC proposes an LLM generation method that integrates subject-specific knowledge with strong constraints, by adopting strong LLMs to automatically convert flexible knowledge into multi-layered, standardized rules to effectively constrain model generation on domain tasks.

Experiments on scientific tasks including industrial formulation design, clinical tumor diagnosis and retrosynthesis planning demonstrate effectiveness, achieving a 12% accuracy improvement on average compared with vanilla generation.

In clinical diagnosis, LLMs occasionally exhibi
…[truncated 691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T16:26:46.921979+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-debate reinforcement learning\" SDRL reasoning model debate participant 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-debate reinforcement learning\" SDRL reasoning model debate participant 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-19T16:26:46.922103+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"belief entrenchment\" robust reasoning LLM agents 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"belief entrenchment\" robust reasoning LLM agents 2025"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T16:26:46.922217+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM intrinsic self-correction ability without external feedback 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM intrinsic self-correction ability without external feedback 2025"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T16:26:46.922348+00:00_

Web search results for query: ""belief entrenchment" robust reasoning LLM agents 2025"

Links: [{"title":"[2503.16814] From Belief Entrenchment to Robust Reasoning in LLM Agents","url":"https://arxiv.org/abs/2503.16814"},{"title":"From Belief Entrenchment to Robust Reasoning in LLM Agents","url":"https://arxiv.org/html/2503.16814"},{"title":"From Belief Entrenchment to Robust Reasoning in LLM Agents","url":"https://arxiv.org/pdf/2503.16814"},{"title":"GitHub - luo-junyu/Awesome-Agent-Papers: [Up-to-date] Large Language Model Agent: A Survey on Methodology, Applications and Challenges · GitHub","url":"https://github.com/luo-junyu/awesome-agent-papers"},{"title":"Reducing Belief Deviation in Reinforcement Learning for Active Reasoning","url":"https://arxiv.org/pdf/2510.12264"}]

Based on the search results, I found highly relevant research on this topic:

Multi-Agent Debate (MAD) has emerged as a promising inference scaling method for Large Language Model reasoning, but frequently suffers from belief entrenchment, where agents reinforce shared errors rather than correcting them.

Belief entrenchment is a phenomenon where models exhibit excessive confidence in their initial, often erroneous, outputs and resist correction. LLMs often prioritize consistency over accuracy because they are trained to maximize the likelihood of the next token based on context, leading them to align responses with their own previous outputs rather than objective truth.

Researchers have identified two distinct root causes: (1) the model's biased static initial belief and (2) homogenized debate dynamics that amplify the majority view regardless of correctness. 

In response to these challenges, a framework called DReaMAD (Diverse Reasoning via Multi-Agent Debate) has been proposed that first rectifies the static belief via strategic prior knowledge elicitation, then reshapes the debate dynamics by enforcing perspective diversity. DReaMAD significantly mitigates entrenchment, achieving a +9.5%
…[truncated 186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-19T16:26:46.922517+00:00_

Web search results for query: "LLM intrinsic self-correction ability without external feedback 2025"

Links: [{"title":"When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs","url":"https://www.researchgate.net/publication/385650033_When_Can_LLMs_Actually_Correct_Their_Own_Mistakes_A_Critical_Survey_of_Self-Correction_of_LLMs"},{"title":"Large Language Models have Intrinsic Self-Correction Ability | OpenReview","url":"https://openreview.net/forum?id=pTyEnkuSQ0"},{"title":"[2310.01798] Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/abs/2310.01798"},{"title":"Large Language Models Cannot Self-Correct Reasoning Yet | OpenReview","url":"https://openreview.net/forum?id=IkmD3fKBPQ"},{"title":"Learning From Correctness Without Prompting Makes LLM Efficient Reasoner","url":"https://arxiv.org/pdf/2403.19094"},{"title":"Enhancing LLM Planning Capabilities through Intrinsic Self-Critique","url":"https://arxiv.org/pdf/2512.24103"},{"title":"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis","url":"https://arxiv.org/pdf/2601.00828"},{"title":"Large Language Models Cannot Self-Correct Reasoning Yet","url":"https://arxiv.org/pdf/2310.01798"}]

Based on the search results, here's what recent research shows about LLM intrinsic self-correction ability without external feedback:

## Key Findings

LLMs cannot reliably correct their own reasoning without external feedback. In fact, self-correction can flip correct answers to incorrect ones.

No prior work shows successful intrinsic self-correction using only the model's own feedback. Additionally, LLMs cannot correct their own reasoning without external feedback—and correction attempts can actually make things worse.

## Recent 2025 Findings

A January 2026 study identified a striking paradox: weaker models (GPT-3.5, 66% accuracy) achieve 1.6× higher intrinsic correction rates than stronger models (DeepSeek, 94% accurac
…[truncated 732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T16:26:46.922673+00:00_

Web search results for query: ""self-debate reinforcement learning" SDRL reasoning model debate participant 2025 2026"

Links: [{"title":"Prepare Reasoning Language Models for Multi-Agent Debate with Self-Debate Reinforcement Learning","url":"https://arxiv.org/html/2601.22297v1"},{"title":"[2601.22297] Prepare Reasoning Language Models for Multi-Agent Debate with Self-Debate Reinforcement Learning","url":"https://arxiv.org/abs/2601.22297"},{"title":"Prepare Reasoning Language Models for Multi-Agent Debate with Self-Debate Reinforcement Learning","url":"https://arxiv.org/pdf/2601.22297"},{"title":"Prepare Reasoning Language Models for Multi-Agent Debate","url":"https://www.arxiv.org/pdf/2601.22297"},{"title":"Reinforcing Structured Chain-of-Thought for Video Understanding","url":"https://arxiv.org/pdf/2603.25942"},{"title":"Beyond the Trade-off: Self-Supervised Reinforcement Learning for Reasoning Models' Instruction Following","url":"https://arxiv.org/pdf/2508.02150"}]

Based on the web search results, I found comprehensive information about Self-Debate Reinforcement Learning (SDRL):

## Self-Debate Reinforcement Learning (SDRL)

Self-Debate Reinforcement Learning (SDRL) is a training framework that equips a single reasoning model with both strong problem-solving and private critique capabilities under debate.

### How SDRL Works

Given a prompt, SDRL first samples multiple candidate solutions, then constructs a debate context with diverse reasoning paths and generates second-turn responses conditioned on this context. SDRL jointly optimizes both the initial and debate-conditioned responses, yielding a model that is effective as both a standalone solver and a debate participant.

### Purpose and Context

Current RLVR (Reinforcement Learning with Verifiable Rewards) methods typically train LLMs to solve problems in isolation, without explicitly preparing them to synthesize and benefit from different rationales that arise during debate. SDRL addresses this by equippin
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T16:26:46.922852+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/",
  "description": "Check artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/",
    "description": "Check artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-19T16:26:46.923019+00:00_

_extracted
_project
aime30_v2_partial_analysis.md
analysis_exp045.md
analyze_adaptive_sica.py
analyze_discriminative_rate.py
analyze_expanded.py
analyze_seed_replication.py
appendix_prompt_template.md
backward_verification.py
case_study_materials.md
citation_verification.md
code_verify_report.md
constraint_ablation
constraint_extractor.py
constraint_extractor_fixed.py
crd_audit_report.md
cross_trace_unsat.py
d016_model_pivot_report.md
diagnose_exp039.md
diagnose_exp062_exp065.md
dream_reports
entropy_breakdown_crossmodel.json
exp-001
exp-005
exp-007-qwen72b-awq
exp-009
exp-010-mistral-v2
exp-011
exp-011-llama8b
exp-014
exp-016
exp-017-strategyqa-v3
exp-017-strategyqa-v3_analysis.md
exp-019
exp-021-oracle-folio
exp-022
exp-022-oracle-proofwriter
exp-023-discriminative-rate
exp-030-crossmodel-mistral-folio204
exp-031-oracle-folio-regen
exp-038
exp-045-backward-verification
exp-046
exp-060-cross-qwen25-14b-extractor
exp011_truncation_bias_analysis.md
exp019_analysis.md
exp033_analysis.md
exp046_analysis.md
exp069_data_pipeline_audit.md
exp_005_qwq_regime
exp_009_overhead
exp_016_weighted_sc
f2_discriminative_analysis.md
f2_preview.png
f3_preview.png
figures
fleiss_kappa_raw_all.json
fleiss_kappa_unified_merged.json
folio_c0_precheck_raw.json
folio_c0_precheck_report.md
gsm8k_pilot_14b
launch_mvp.sh
manifest.yaml
maxsat_diagnosis_proofwriter30_v2.md
mcnemar_recompute.py
oracle_experiment_design.md
pipeline.py
prepare_proofwriter.py
proofwriter30_v2
proofwriter30_v2_interim_analysis.md
quality_metrics.csv
report_proofwriter30_v2_progress.md
review_issues.yaml
review_reports
run_consistency_filtering.py
run_exp017_strategyqa.sh
run_exp018_arc.sh
run_exp024_llama70b.sh
run_exp025_qwen72b.sh
run_full_mvp.py
run_icl_oracle.py
run_icl_oracle.sh
run_mvp.py
sc_tiebreak_revalidation.py
sica_aime30_v2
sica_d012_14b
sica_expanded_14b
sica_folio30
sica_k_sensitivity_14b
status_check_20260519.md
summarize_k_sensitivity.py
trace_generator.py
track_discordant_pairs.py
westd16639_crash
…[truncated 167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-19T16:26:46.923192+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/literature_independence_bottleneck.md",
  "content": "# Literature Survey: Independence Bottleneck in LLM Self-Consistency\n\n> 调研日期: 2026-05-19 | 覆盖范围: 2024-2026 | 共 23 篇论文\n\n---\n\n## 1. LLM Reasoning Diversity & Self-Consistency Limitations\n\n### 1.1 Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity\n- **Authors**: Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, Weiyan Shi\n- **Venue**: arXiv 2510.01171 (Oct 2025), under review\n- **核心发现**: Post-training alignment 导致 LLM 产生 mode collapse，根本原因是 preference data 中的 typicality bias（人类标注者系统性偏好典型/流畅文本）。提出 Verbalized Sampling (VS)，通过 prompting 让模型显式输出 response 分布，diversity 提升 2-3x，无需额外训练。\n- **与我们的关系**: 直接解释了 SICA 中同模型采样 trace 高度同源的 data-level 根因——alignment 训练压缩了输出分布。VS 的 prompting 策略可作为打破 independence bottleneck 的轻量级 baseline。\n\n### 1.2 Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling\n- **Authors**: Aggarwal & Deshpande\n- **Venue**: NAACL 2025 (Long Paper)\n- **核心发现**: 标准 SC 对所有 sample 同等对待，仅基于 final answer 一致性做停止决策，缺乏区分 reasoning 质量的机制。RASC 动态评估 output 和 rationale，提升采样效率和 reasoning faithfulness。\n- **与我们的关系**: 揭示了 SC 的结构性缺陷：它不区分 reasoning path 质量，这与 SICA 的约束独立性问题互补——即使 path 多样，如果约束来源相同，增加 K 也无法提供新信息。\n\n### 1.3 Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning\n- **Authors**: Gisang Lee et al.\n- **Venue**: arXiv 2410.09780 (Oct 2024)\n- **核心发现**: 不同 prompting 方法（Text CoT / Code / Cumulative Reasoning）探索不同的搜索空间，且问题越难区分越明显。均匀混合多种方法的 sample 可以在减少 ~43% 采样次数的情况下达到最大搜索空间覆盖。\n- **与我们的关系**: 直接证据：同一模型的单一 prompting 方式产生的 trace 搜索空间高度重叠。多 prompting 策略是打破 independence bottleneck 的实用手段，可与 SICA 的 cross-model 策略结合。\n\n### 1.4 Confidence Improves Self-Consistency in LLMs\n- **Authors**: (2025)\n- **Venue**: arXiv 2502.06233 (Feb 2025)\n- **核心发现**: 在 SC 投票中引入 confidence weighting 可以提升准确率。但 greedy decoding 牺牲 diversity 和 robustness，beam search 产生的 reasoning 多样性系统性低于 random sampling。\n- **与我们的关系**: 确认了 SC 中 diversity-accuracy 的 tension：提高 confidence 可以改善投票质量，但不能解决底层的 independence 问题。SICA 需要在 confidence 和 independence 之间找到新的平衡点。\n\n---\n\n## 2. LLM Debate & Multi-Agent Reasoning\n\n### 2.1 Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate\n- **Authors**: Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu\n- **Venue**: EMNLP 2024 (Main)\n- **核心发现**: 提出 Multi-Agent Debate (MAD) 框架，agents 以 \"tit for tat\" 方式辩论，judge 管理过程。适度的对抗水平效果最好；过强则偏离正确答案。LLM 作为 judge 在 agent 异构时可能不公平。\n- **与我们的关系**: MAD 通过 debate 机制引入结构化 diversity，但仍受限于同模型的 \"思维同质性\"。这与 SICA 的 independence bottleneck 本质相同——debate 不等于独立。\n\n### 2.2 Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate (DMAD)\n- **Authors**: (2025)\n- **Venue**: ICLR 2025\n- **核心发现**: MAD 即使分配不同 persona，agents 仍使用同质化思维过程（fixed mental set）。借鉴心理学 mental set 理论，DMAD 强制 agents 使用不同的 reasoning approach（如代数 vs 几何 vs 枚举），打破固定思维模式。\n- **与我们的关系**: 核心相关——DMAD 的 \"mental set\" 概念直接对应 SICA 的 independence bottleneck。即使 K 很大，如果 traces 共享相同的 reasoning approach，约束也是冗余的。DMAD 的 diverse reasoning strategy 可以启发 SICA 的约束生成多样化。\n\n### 2.3 Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning\n- **Authors**: Wu, Li et al.\n- **Venue**: arXiv 2511.07784 (Nov 2025)\n- **核心发现**: 通过 Knight-Knave-Spy 逻辑谜题的受控实验发现：intrinsic reasoning strength 和 group diversity 是 debate 成功的主要驱动力，结构参数（顺序、confidence 可见性）影响有限。Majority pressure 会抑制独立纠错。\n- **与我们的关系**: 关键发现：majority pressure 抑制独立性。这直接映射到 SICA 场景——当多数 trace 收敛到相同（错误）约束时，少数正确 trace 的信号被淹没。Group diversity（异构模型）是关键。\n\n### 2.4 ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning\n- **Authors**: (2026)\n- **Venue**: arXiv 2602.00127 (Jan 2026)\n- **核心发现**: 将 LLM reasoning 建模为 aligned delegation game，principal 向 agents 委托任务，agents 生成 candidate solutions。理论证明在公平比较下 ALIGN 比 single-agent 更优，且分析 relaxes independence assumptions（允许 correlated answers）。\n- **与我们的关系**: 理论框架直接相关——ALIGN 明确 relaxes 了 independence assumption，承认 candidate answers 之间存在 correlation，仍能提供 performance guarantee。这为 SICA 在非独立约束下的理论分析提供了参考。\n\n### 2.5 From Belief Entrenchment to Robust Reasoning in LLM Agents (DReaMAD)\n- **Authors**: (2025)\n- **Venue**: arXiv 2503.16814 (Mar 2025)\n- **核心发现**: MAD 中的 belief entrenchment 有两个根因：(1) 模型的 biased static initial belief，(2) homogenized debate dynamics 放大多数观点。DReaMAD 通过 strategic prior knowledge elicitation 修正初始 belief，通过 enforcing perspective diversity 重塑 debate dynamics，accuracy +9.5% over ReAct。\n- **与我们的关系**: \"Homogenized debate dynamics\" 是 independence bottleneck 在 debate 场景的具体表现。DReaMAD 的两阶段策略（修正 prior + 强制 diversity）可以直接迁移到 SICA：先 diversify 约束来源，再防止约束收敛。\n\n### 2.6 Self-Debate Reinforcement Learning (SDRL)\n- **Authors**: Chenxi Liu, Yanshuo Chen, Ruibo Chen et al.\n- **Venue**: arXiv 2601.22297 (Jan 2026)\n- **核心发现**: 当前 RLVR 训练 LLM 独立解题，未训练其从不同 rationale 中学习。SDRL 联合优化 initial response 和 debate-conditioned response，使单一模型同时成为好的 solver 和好的 debate participant。\n- **与我们的关系**: SDRL 的关键 insight 是：模型需要被显式训练以利用 diverse reasoning trajectories。这暗示 SICA 的 independence bottleneck 部分源于模型本身未被训练去生成独立约束。\n\n---\n\n## 3. Contrastive Reasoning & Independent Constraint Generation\n\n### 3.1 Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning\n- **Authors**: (2026)\n- **Venue**: arXiv 2602.18232 (Feb 2026)\n- **核心发现**: Reasoning uncertainty 高度局部化——少量 low-confidence tokens 贡献了大部分 reasoning errors。通过在 low-confidence 位置构造 contrastive reference（high-confidence tokens 用 placeholder 替换）并减去其分布，选择性干预解码过程。\n- **与我们的关系**: 提供了识别 reasoning 中 \"薄弱环节\" 的方法。SICA 可以借鉴：对 trace 中 low-confidence 区域施加更强的约束验证，或者利用 confidence 差异来评估约束的独立性。\n\n### 3.2 Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation\n- **Authors**: Phuc Phan, Hieu Tran, Long Phan\n- **Venue**: arXiv 2402.14874 (Feb 2024)\n- **核心发现**: 标准 Contrastive Decoding 需要 expert + amateur 两个模型。DCD 用 Contrastive CoT Prompting + Distillation（Dropout/Quantization）在单模型内构造对比信号，消除了对 amateur model 的需求，减少内存开销。\n- **与我们的关系**: DCD 展示了在单模型内生成 contrastive signal 的可能性。这对 SICA 有启发：可以通过 perturbed/degraded 版本的 trace 来生成与原始 trace 相对独立的约束。\n\n### 3.3 CRANE: Reasoning with Constrained LLM Generation\n- **Authors**: (2025)\n- **Venue**: arXiv 2502.09061 (Feb 2025)\n- **核心发现**: 严格的语法约束会降低 LLM reasoning 能力（有理论解释）。但通过 carefully designed additional rules augmenting output grammar，可以同时保持 reasoning 能力和语法正确性。CRANE 在 accuracy 上比 unconstrained decoding 高达 +10%。\n- **与我们的关系**: 直接相关——CRANE 证明了 constraints 和 reasoning 之间存在 tension，但可以通过精心设计来调和。这对 SICA 的约束设计有指导意义：约束不应过于 restrictive 以免损害 reasoning diversity。\n\n### 3.4 Scientific Knowledge-driven Decoding Constraints (SciDC)\n- **Authors**: (2026)\n- **Venue**: arXiv 2604.06603 (Apr 2026)\n- **核心发现**: 将领域知识（工业配方、临床诊断、逆合成）转化为多层标准化规则作为 decoding constraints，平均 accuracy +12%。证明了来自外部知识的约束比模型自身的 \"implicit knowledge\" 更可靠。\n- **与我们的关系**: SciDC 的核心思路——将外部独立知识源转化为 decoding constraints——与 SICA 打破 independence bottleneck 的方向一致：从模型外部引入独立于 reasoning trace 的约束来源。\n\n---\n\n## 4. Test-Time Compute Scaling & Process Reward Models\n\n### 4.1 Mode-Conditioning Unlocks Superior Test-Time Scaling\n- **Authors**: Chen Henry Wu et al.\n- **Venue**: arXiv 2512.01127 (Dec 2025)\n- **核心发现**: Parallel sampling 的效果受限于 diversity collapse——finetuning 和 RL 会导致 generations 集中到少数 dominant modes。Mode-Conditioning (ModC) 通过 specialist models 或 mode-specific prefixes 显式分配 compute 到不同 reasoning modes，实现 4x efficiency gain。\n- **与我们的关系**: Diversity collapse 是 SICA independence bottleneck 的 test-time scaling 视角表述。ModC 的 mode-conditioning 策略可以直接用于 SICA：为不同 trace 指定不同的 reasoning mode，从而生成更独立的约束。\n\n### 4.2 GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n- **Authors**: Jian Zhao, Runze Liu et al.\n- **Venue**: AAAI 2026 (arXiv 2504.00891)\n- **核心发现**: 现有 PRM 是 discriminative scoring，能力有限且泛化差。GenPRM 将 process supervision 重新定义为 generative task（CoT + code verification → judgment），解决了 PRM 不能 scale test-time compute 的问题。\n- **与我们的关系**: GenPRM 的 generative verification 思路与 SICA 的 symbolic constraint verification 互补。PRM 评估 reasoning step 质量，SICA 评估约束一致性——两者可以融合为更强的 verification framework。\n\n### 4.3 Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning (ADAPT)\n- **Authors**: Ho-Lam Chung et al.\n- **Venue**: arXiv 2506.04611 (Jun 2025)\n- **核心发现**: 综述 TTS 方法（sampling-based / search-based / trajectory optimization）。关键观察：reasoning-optimized models 产生 less diverse outputs，限制 TTS 效果。提出 ADAPT（Diversity Aware Prefix fine-Tuning），用 8x less compute 达到 80% accuracy。\n- **与我们的关系**: 直接证据：reasoning 优化（如 RLHF/RLVF）损害了 output diversity。这解释了为什么 SICA 在强 reasoning model 上反而可能遇到更严重的 independence bottleneck。ADAPT 的 prefix tuning 是潜在的 lightweight fix。\n\n### 4.4 Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\n- **Authors**: Runze Liu et al.\n- **Venue**: arXiv 2502.06703 (Feb 2025), ICLR 2025\n- **核心发现**: Compute-optimal TTS 策略高度依赖 policy model、PRM 和问题难度的组合。在正确的 TTS 策略下，1B 模型可以超越 405B 模型（MATH-500），0.5B 超越 GPT-4o。\n- **与我们的关系**: 证明了 test-time compute allocation 的巨大潜力。但 diversity 是前提——如果 samples 不独立，增加 compute 的边际收益递减。这为 SICA 的 independence bottleneck 提供了经济学视角：打破 bottleneck = 提高 test-time compute 的 ROI。\n\n---\n\n## 5. LLM Self-Correction Limitations\n\n### 5.1 Large Language Models Cannot Self-Correct Reasoning Yet\n- **Authors**: Jie Huang, Xinyun Chen et al.\n- **Venue**: ICLR 2024\n- **核心发现**: LLM 在没有 external feedback 的情况下无法可靠地 self-correct reasoning。Self-correction 有时会把正确答案翻转为错误答案。Intrinsic self-correction（仅用模型自身反馈）系统性失败。\n- **与我们的关系**: 奠基性工作。Self-correction 失败的根因与 independence bottleneck 相同：模型用自身的（有偏的）知识去验证自身的（有偏的）输出，缺乏独立的 verification 信号。SICA 的 symbolic constraints 正是试图提供这种独立信号。\n\n### 5.2 When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\n- **Authors**: Ryo Kamoi et al.\n- **Venue**: TACL 2024\n- **核心发现**: (1) 没有工作成功展示了仅用 prompted LLM 反馈的 self-correction（除特殊适合任务外）；(2) Self-correction 在有 reliable external feedback 时有效；(3) Large-scale fine-tuning 可以 enable self-correction。许多研究存在不公平评估。\n- **与我们的关系**: 综述性确认：self-correction 需要 external feedback。这支持 SICA 的方法论——symbolic invariant checking 提供了一种 external（或至少 structurally independent）的 feedback 机制。但 independence bottleneck 意味着如果 constraints 也来自同一模型，这个 \"external\" 信号并不真正独立。\n\n### 5.3 Large Language Models Can Self-Correct with Key Condition Verification (ProCo)\n- **Authors**: Zhenyu Wu, Qingkai Zeng, Zhihan Zhang, Zhaoxuan Tan, Chao Shen, Meng Jiang\n- **Venue**: EMNLP 2024 (Main)\n- **核心发现**: 提出 verify-then-correct 框架：mask 问题中的 key condition，将当前 response 加入构造 verification question，预测被 mask 的 condition 来验证 response。GPT-3.5-Turbo 在 QA 上 +6.8 EM，arithmetic +14.1 accuracy。\n- **与我们的关系**: ProCo 的 key condition masking 是一种巧妙的 \"伪独立\" 验证——通过信息隐藏创造条件上的独立性。这个思路可以直接应用到 SICA：通过部分信息隐藏来生成与原始 trace 条件独立的约束。\n\n### 5.4 Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)\n- **Authors**: (Google DeepMind)\n- **Venue**: ICLR 2025 (Oral)\n- **核心发现**: SFT 和标准 RL 的 self-correction 失败源于 distribution shift（训练纠正 base model 错误但无法纠正自身错误）和 behavior collapse（第二轮仅做表面修改）。SCoRe 在模型自身分布下训练 + 正则化，MATH +15.6%, HumanEval +9.1%。\n- **与我们的关系**: Distribution shift 和 behavior collapse 是 independence bottleneck 在 self-correction 中的具体表现。SCoRe 通过在模型自身分布上训练来缓解——这暗示 SICA 也需要考虑约束生成器的分布特性。\n\n### 5.5 Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\n- **Authors**: (2026)\n- **Venue**: arXiv 2601.00828 (Jan 2026)\n- **核心发现**: Accuracy-Correction Paradox：弱模型（GPT-3.5, 66% accuracy）的 intrinsic correction rate 是强模型（DeepSeek, 94% accuracy）的 1.6x（26.8% vs 16.7%）。将 self-correction 分解为三个子能力：error detection、error localization、error correction。\n- **与我们的关系**: Accuracy-Correction Paradox 对 SICA 有直接启示：强模型的约束可能更准确但更同质（independence bottleneck 更严重），弱模型的约束可能更 diverse 但噪声更大。这指向一个 sweet spot：使用 moderately capable 模型或异构模型组合来平衡 accuracy 和 independence。\n\n---\n\n## 跨主题综合分析\n\n### Independence Bottleneck 的多视角确认\n\n| 视角 | 关键论文 | 核心证据 |\n|------|---------|---------|\n| Data-level | Verbalized Sampling | Typicality bias → mode collapse |\n| Training-level | ADAPT, ModC | RL/RLHF → diversity collapse |\n| Sampling-level | Expanding Search Space | 单一 prompting → 搜索空间重叠 |\n| Debate-level | DReaMAD, DMAD | Homogenized dynamics, mental set |\n| Self-correction-level | Huang et al., Kamoi et al. | 无外部反馈 → 系统性失败 |\n| Theoretical | ALIGN | 显式 relax independence assumption |\n\n### 潜在突破方向（基于文献）\n\n1. **Multi-mode constraint generation**: ModC + Expanding Search Space 的思路——为不同 trace 指定不同 reasoning mode\n2. **Information-hiding verification**: ProCo 的 key condition masking——通过信息隐藏创造条件独立性\n3. **Cross-model heterogeneity**: Can LLM Agents Really Debate? 的 evidence——异构模型是 diversity 的主要驱动力\n4. **External knowledge constraints**: SciDC 的思路——从外部知识源引入独立约束\n5. **Diversity-aware training**: SDRL + SCoRe 的思路——显式训练模型生成 diverse/independent 约束\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/literature_independence_bottleneck.md",
    "content": "# Literature Survey: Independence Bottleneck in LLM Self-Consistency\n\n> 调研日期: 2026-05-19 | 覆盖范围: 2024-2026 | 共 23 篇论文\n\n---\n\n## 1. LLM Reasoning Diversity & Self-Consistency Limitations\n\n### 1.1 Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity\n- **Authors**: Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, Weiyan Shi\n- **Venue**: arXiv 2510.01171 (Oct 2025), under review\n- **核心发现**: Post-training alignment 导致 LLM 产生 mode collapse，根本原因是 preference data 中的 typicality bias（人类标注者系统性偏好典型/流畅文本）。提出 Verbalized Sampling (VS)，通过 prompting 让模型显式输出 response 分布，diversity 提升 2-3x，无需额外训练。\n- **与我们的关系**: 直接解释了 SICA 中同模型采样 trace 高度同源的 data-level 根因——alignment 训练压缩了输出分布。VS 的 prompting 策略可作为打破 independence bottleneck 的轻量级 baseline。\n\n### 1.2 Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling\n- **Authors**: Aggarwal & Deshpande\n- **Venue**: NAACL 2025 (Long Paper)\n- **核心发现**: 标准 SC 对所有 sample 同等对待，仅基于 final answer 一致性做停止决策，缺乏区分 reasoning 质量的机制。RASC 动态评估 output 和 rationale，提升采样效率和 reasoning faithfulness。\n- **与我们的关系**: 揭示了 SC 的结构性缺陷：它不区分 reasoning path 质量，这与 SICA 的约束独立性问题互补——即使 path 多样，如果约束来源相同，增加 K 也无法提供新信息。\n\n### 1.3 Expanding Search Space with Diverse Prompting Agents: An Efficient Sampling Approach for LLM Mathematical Reasoning\n- **Authors**: Gisang Lee et al.\n- **Venue**: arXiv 2410.09780 (Oct 2024)\n- **核心发现**: 不同 prompting 方法（Text CoT / Code / Cumulative Reasoning）探索不同的搜索空间，且问题越难区分越明显。均匀混合多种方法的 sample 可以在减少 ~43% 采样次数的情况下达到最大搜索空间覆盖。\n- **与我们的关系**: 直接证据：同一模型的单一 prompting 方式产生的 trace 搜索空间高度重叠。多 prompting 策略是打破 independence bottleneck 的实用手段，可与 SICA 的 cross-model 策略结合。\n\n### 1.4 Confidence Improves Self-Consistency in LLMs\n- **Authors**: (2025)\n- **Venue**: arXiv 2502.06233 (Feb 2025)\n- **核心发现**: 在 SC 投票中引入 confidence weighting 可以提升准确率。但 greedy decoding 牺牲 diversity 和 robustness，beam search 产生的 reasoning 多样性系统性低于 random sampling。\n- **与我们的关系**: 确认了 SC 中 diversity-accuracy 的 tension：提高 confidence 可以改善投票质量，但不能解决底层的 independence 问题。SICA 需要在 confidence 和 independence 之间找到新的平衡点。\n\n---\n\n## 2. LLM Debate & Multi-Agent Reasoning\n\n### 2.1 Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate\n- **Authors**: Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang, Yan Wang, Rui Wang, Yujiu Yang, Shuming Shi, Zhaopeng Tu\n- **Venue**: EMNLP 2024 (Main)\n- **核心发现**: 提出 Multi-Agent Debate (MAD) 框架，agents 以 \"tit for tat\" 方式辩论，judge 管理过程。适度的对抗水平效果最好；过强则偏离正确答案。LLM 作为 judge 在 agent 异构时可能不公平。\n- **与我们的关系**: MAD 通过 debate 机制引入结构化 diversity，但仍受限于同模型的 \"思维同质性\"。这与 SICA 的 independence bottleneck 本质相同——debate 不等于独立。\n\n### 2.2 Breaking Mental Set to Improve Reasoning through Diverse Multi-Agent Debate (DMAD)\n- **Authors**: (2025)\n- **Venue**: ICLR 2025\n- **核心发现**: MAD 即使分配不同 persona，agents 仍使用同质化思维过程（fixed mental set）。借鉴心理学 mental set 理论，DMAD 强制 agents 使用不同的 reasoning approach（如代数 vs 几何 vs 枚举），打破固定思维模式。\n- **与我们的关系**: 核心相关——DMAD 的 \"mental set\" 概念直接对应 SICA 的 independence bottleneck。即使 K 很大，如果 traces 共享相同的 reasoning approach，约束也是冗余的。DMAD 的 diverse reasoning strategy 可以启发 SICA 的约束生成多样化。\n\n### 2.3 Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning\n- **Authors**: Wu, Li et al.\n- **Venue**: arXiv 2511.07784 (Nov 2025)\n- **核心发现**: 通过 Knight-Knave-Spy 逻辑谜题的受控实验发现：intrinsic reasoning strength 和 group diversity 是 debate 成功的主要驱动力，结构参数（顺序、confidence 可见性）影响有限。Majority pressure 会抑制独立纠错。\n- **与我们的关系**: 关键发现：majority pressure 抑制独立性。这直接映射到 SICA 场景——当多数 trace 收敛到相同（错误）约束时，少数正确 trace 的信号被淹没。Group diversity（异构模型）是关键。\n\n### 2.4 ALIGN: Aligned Delegation with Performance Guarantees for Multi-Agent LLM Reasoning\n- **Authors**: (2026)\n- **Venue**: arXiv 2602.00127 (Jan 2026)\n- **核心发现**: 将 LLM reasoning 建模为 aligned delegation game，principal 向 agents 委托任务，agents 生成 candidate solutions。理论证明在公平比较下 ALIGN 比 single-agent 更优，且分析 relaxes independence assumptions（允许 correlated answers）。\n- **与我们的关系**: 理论框架直接相关——ALIGN 明确 relaxes 了 independence assumption，承认 candidate answers 之间存在 correlation，仍能提供 performance guarantee。这为 SICA 在非独立约束下的理论分析提供了参考。\n\n### 2.5 From Belief Entrenchment to Robust Reasoning in LLM Agents (DReaMAD)\n- **Authors**: (2025)\n- **Venue**: arXiv 2503.16814 (Mar 2025)\n- **核心发现**: MAD 中的 belief entrenchment 有两个根因：(1) 模型的 biased static initial belief，(2) homogenized debate dynamics 放大多数观点。DReaMAD 通过 strategic prior knowledge elicitation 修正初始 belief，通过 enforcing perspective diversity 重塑 debate dynamics，accuracy +9.5% over ReAct。\n- **与我们的关系**: \"Homogenized debate dynamics\" 是 independence bottleneck 在 debate 场景的具体表现。DReaMAD 的两阶段策略（修正 prior + 强制 diversity）可以直接迁移到 SICA：先 diversify 约束来源，再防止约束收敛。\n\n### 2.6 Self-Debate Reinforcement Learning (SDRL)\n- **Authors**: Chenxi Liu, Yanshuo Chen, Ruibo Chen et al.\n- **Venue**: arXiv 2601.22297 (Jan 2026)\n- **核心发现**: 当前 RLVR 训练 LLM 独立解题，未训练其从不同 rationale 中学习。SDRL 联合优化 initial response 和 debate-conditioned response，使单一模型同时成为好的 solver 和好的 debate participant。\n- **与我们的关系**: SDRL 的关键 insight 是：模型需要被显式训练以利用 diverse reasoning trajectories。这暗示 SICA 的 independence bottleneck 部分源于模型本身未被训练去生成独立约束。\n\n---\n\n## 3. Contrastive Reasoning & Independent Constraint Generation\n\n### 3.1 Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning\n- **Authors**: (2026)\n- **Venue**: arXiv 2602.18232 (Feb 2026)\n- **核心发现**: Reasoning uncertainty 高度局部化——少量 low-confidence tokens 贡献了大部分 reasoning errors。通过在 low-confidence 位置构造 contrastive reference（high-confidence tokens 用 placeholder 替换）并减去其分布，选择性干预解码过程。\n- **与我们的关系**: 提供了识别 reasoning 中 \"薄弱环节\" 的方法。SICA 可以借鉴：对 trace 中 low-confidence 区域施加更强的约束验证，或者利用 confidence 差异来评估约束的独立性。\n\n### 3.2 Distillation Contrastive Decoding: Improving LLMs Reasoning with Contrastive Decoding and Distillation\n- **Authors**: Phuc Phan, Hieu Tran, Long Phan\n- **Venue**: arXiv 2402.14874 (Feb 2024)\n- **核心发现**: 标准 Contrastive Decoding 需要 expert + amateur 两个模型。DCD 用 Contrastive CoT Prompting + Distillation（Dropout/Quantization）在单模型内构造对比信号，消除了对 amateur model 的需求，减少内存开销。\n- **与我们的关系**: DCD 展示了在单模型内生成 contrastive signal 的可能性。这对 SICA 有启发：可以通过 perturbed/degraded 版本的 trace 来生成与原始 trace 相对独立的约束。\n\n### 3.3 CRANE: Reasoning with Constrained LLM Generation\n- **Authors**: (2025)\n- **Venue**: arXiv 2502.09061 (Feb 2025)\n- **核心发现**: 严格的语法约束会降低 LLM reasoning 能力（有理论解释）。但通过 carefully designed additional rules augmenting output grammar，可以同时保持 reasoning 能力和语法正确性。CRANE 在 accuracy 上比 unconstrained decoding 高达 +10%。\n- **与我们的关系**: 直接相关——CRANE 证明了 constraints 和 reasoning 之间存在 tension，但可以通过精心设计来调和。这对 SICA 的约束设计有指导意义：约束不应过于 restrictive 以免损害 reasoning diversity。\n\n### 3.4 Scientific Knowledge-driven Decoding Constraints (SciDC)\n- **Authors**: (2026)\n- **Venue**: arXiv 2604.06603 (Apr 2026)\n- **核心发现**: 将领域知识（工业配方、临床诊断、逆合成）转化为多层标准化规则作为 decoding constraints，平均 accuracy +12%。证明了来自外部知识的约束比模型自身的 \"implicit knowledge\" 更可靠。\n- **与我们的关系**: SciDC 的核心思路——将外部独立知识源转化为 decoding constraints——与 SICA 打破 independence bottleneck 的方向一致：从模型外部引入独立于 reasoning trace 的约束来源。\n\n---\n\n## 4. Test-Time Compute Scaling & Process Reward Models\n\n### 4.1 Mode-Conditioning Unlocks Superior Test-Time Scaling\n- **Authors**: Chen Henry Wu et al.\n- **Venue**: arXiv 2512.01127 (Dec 2025)\n- **核心发现**: Parallel sampling 的效果受限于 diversity collapse——finetuning 和 RL 会导致 generations 集中到少数 dominant modes。Mode-Conditioning (ModC) 通过 specialist models 或 mode-specific prefixes 显式分配 compute 到不同 reasoning modes，实现 4x efficiency gain。\n- **与我们的关系**: Diversity collapse 是 SICA independence bottleneck 的 test-time scaling 视角表述。ModC 的 mode-conditioning 策略可以直接用于 SICA：为不同 trace 指定不同的 reasoning mode，从而生成更独立的约束。\n\n### 4.2 GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n- **Authors**: Jian Zhao, Runze Liu et al.\n- **Venue**: AAAI 2026 (arXiv 2504.00891)\n- **核心发现**: 现有 PRM 是 discriminative scoring，能力有限且泛化差。GenPRM 将 process supervision 重新定义为 generative task（CoT + code verification → judgment），解决了 PRM 不能 scale test-time compute 的问题。\n- **与我们的关系**: GenPRM 的 generative verification 思路与 SICA 的 symbolic constraint verification 互补。PRM 评估 reasoning step 质量，SICA 评估约束一致性——两者可以融合为更强的 verification framework。\n\n### 4.3 Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning (ADAPT)\n- **Authors**: Ho-Lam Chung et al.\n- **Venue**: arXiv 2506.04611 (Jun 2025)\n- **核心发现**: 综述 TTS 方法（sampling-based / search-based / trajectory optimization）。关键观察：reasoning-optimized models 产生 less diverse outputs，限制 TTS 效果。提出 ADAPT（Diversity Aware Prefix fine-Tuning），用 8x less compute 达到 80% accuracy。\n- **与我们的关系**: 直接证据：reasoning 优化（如 RLHF/RLVF）损害了 output diversity。这解释了为什么 SICA 在强 reasoning model 上反而可能遇到更严重的 independence bottleneck。ADAPT 的 prefix tuning 是潜在的 lightweight fix。\n\n### 4.4 Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling\n- **Authors**: Runze Liu et al.\n- **Venue**: arXiv 2502.06703 (Feb 2025), ICLR 2025\n- **核心发现**: Compute-optimal TTS 策略高度依赖 policy model、PRM 和问题难度的组合。在正确的 TTS 策略下，1B 模型可以超越 405B 模型（MATH-500），0.5B 超越 GPT-4o。\n- **与我们的关系**: 证明了 test-time compute allocation 的巨大潜力。但 diversity 是前提——如果 samples 不独立，增加 compute 的边际收益递减。这为 SICA 的 independence bottleneck 提供了经济学视角：打破 bottleneck = 提高 test-time compute 的 ROI。\n\n---\n\n## 5. LLM Self-Correction Limitations\n\n### 5.1 Large Language Models Cannot Self-Correct Reasoning Yet\n- **Authors**: Jie Huang, Xinyun Chen et al.\n- **Venue**: ICLR 2024\n- **核心发现**: LLM 在没有 external feedback 的情况下无法可靠地 self-correct reasoning。Self-correction 有时会把正确答案翻转为错误答案。Intrinsic self-correction（仅用模型自身反馈）系统性失败。\n- **与我们的关系**: 奠基性工作。Self-correction 失败的根因与 independence bottleneck 相同：模型用自身的（有偏的）知识去验证自身的（有偏的）输出，缺乏独立的 verification 信号。SICA 的 symbolic constraints 正是试图提供这种独立信号。\n\n### 5.2 When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs\n- **Authors**: Ryo Kamoi et al.\n- **Venue**: TACL 2024\n- **核心发现**: (1) 没有工作成功展示了仅用 prompted LLM 反馈的 self-correction（除特殊适合任务外）；(2) Self-correction 在有 reliable external feedback 时有效；(3) Large-scale fine-tuning 可以 enable self-correction。许多研究存在不公平评估。\n- **与我们的关系**: 综述性确认：self-correction 需要 external feedback。这支持 SICA 的方法论——symbolic invariant checking 提供了一种 external（或至少 structurally independent）的 feedback 机制。但 independence bottleneck 意味着如果 constraints 也来自同一模型，这个 \"external\" 信号并不真正独立。\n\n### 5.3 Large Language Models Can Self-Correct with Key Condition Verification (ProCo)\n- **Authors**: Zhenyu Wu, Qingkai Zeng, Zhihan Zhang, Zhaoxuan Tan, Chao Shen, Meng Jiang\n- **Venue**: EMNLP 2024 (Main)\n- **核心发现**: 提出 verify-then-correct 框架：mask 问题中的 key condition，将当前 response 加入构造 verification question，预测被 mask 的 condition 来验证 response。GPT-3.5-Turbo 在 QA 上 +6.8 EM，arithmetic +14.1 accuracy。\n- **与我们的关系**: ProCo 的 key condition masking 是一种巧妙的 \"伪独立\" 验证——通过信息隐藏创造条件上的独立性。这个思路可以直接应用到 SICA：通过部分信息隐藏来生成与原始 trace 条件独立的约束。\n\n### 5.4 Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)\n- **Authors**: (Google DeepMind)\n- **Venue**: ICLR 2025 (Oral)\n- **核心发现**: SFT 和标准 RL 的 self-correction 失败源于 distribution shift（训练纠正 base model 错误但无法纠正自身错误）和 behavior collapse（第二轮仅做表面修改）。SCoRe 在模型自身分布下训练 + 正则化，MATH +15.6%, HumanEval +9.1%。\n- **与我们的关系**: Distribution shift 和 behavior collapse 是 independence bottleneck 在 self-correction 中的具体表现。SCoRe 通过在模型自身分布上训练来缓解——这暗示 SICA 也需要考虑约束生成器的分布特性。\n\n### 5.5 Decomposing LLM Self-Correction: The Accuracy-Correction Paradox and Error Depth Hypothesis\n- **Authors**: (2026)\n- **Venue**: arXiv 2601.00828 (Jan 2026)\n- **核心发现**: Accuracy-Correction Paradox：弱模型（GPT-3.5, 66% accuracy）的 intrinsic correction rate 是强模型（DeepSeek, 94% accuracy）的 1.6x（26.8% vs 16.7%）。将 self-correction 分解为三个子能力：error detection、error localization、error correction。\n- **与我们的关系**: Accuracy-Correction Paradox 对 SICA 有直接启示：强模型的约束可能更准确但更同质（independence bottleneck 更严重），弱模型的约束可能更 diverse 但噪声更大。这指向一个 sweet spot：使用 moderately capable 模型或异构模型组合来平衡 accuracy 和 independence。\n\n---\n\n## 跨主题综合分析\n\n### Independence Bottleneck 的多视角确认\n\n| 视角 | 关键论文 | 核心证据 |\n|------|---------|---------|\n| Data-level | Verbalized Sampling | Typicality bias → mode collapse |\n| Training-level | ADAPT, ModC | RL/RLHF → diversity collapse |\n| Sampling-level | Expanding Search Space | 单一 prompting → 搜索空间重叠 |\n| Debate-level | DReaMAD, DMAD | Homogenized dynamics, mental set |\n| Self-correction-level | Huang et al., Kamoi et al. | 无外部反馈 → 系统性失败 |\n| Theoretical | ALIGN | 显式 relax independence assumption |\n\n### 潜在突破方向（基于文献）\n\n1. **Multi-mode constraint generation**: ModC + Expanding Search Space 的思路——为不同 trace 指定不同 reasoning mode\n2. **Information-hiding verification**: ProCo 的 key condition masking——通过信息隐藏创造条件独立性\n3. **Cross-model heterogeneity**: Can LLM Agents Really Debate? 的 evidence——异构模型是 diversity 的主要驱动力\n4. **External knowledge constraints**: SciDC 的思路——从外部知识源引入独立约束\n5. **Diversity-aware training**: SDRL + SCoRe 的思路——显式训练模型生成 diverse/independent 约束\n"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T16:26:46.923485+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/artifacts/literature_independence_bottleneck.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-19T16:26:46.923646+00:00_

文献调研完成。23 篇论文按 5 个主题组织，写入 `artifacts/literature_independence_bottleneck.md`。

各主题覆盖：
- **Topic 1** (Reasoning Diversity / SC Limitations): 4 篇 — Verbalized Sampling, RASC, Expanding Search Space, Confidence SC
- **Topic 2** (Debate / Multi-Agent): 6 篇 — MAD, DMAD, Controlled Debate Study, ALIGN, DReaMAD, SDRL
- **Topic 3** (Contrastive / Constraint Generation): 4 篇 — Thinking by Subtraction, DCD, CRANE, SciDC
- **Topic 4** (Test-Time Scaling / PRM): 4 篇 — ModC, GenPRM, ADAPT Survey, Compute-Optimal TTS
- **Topic 5** (Self-Correction Limitations): 5 篇 — Huang et al., Kamoi Survey, ProCo, SCoRe, Accuracy-Correction Paradox

文末附跨主题综合分析表和 5 个潜在突破方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_literature-independence-bottleneck_20260519T162224"
}
```

</details>

---
