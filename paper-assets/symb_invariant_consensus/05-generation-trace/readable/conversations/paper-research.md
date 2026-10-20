# paper research

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_paper_research_20260520T101251.jsonl`
- **Structured JSON:** [`13c3959cd8bed89590e7.json`](../../sessions/13/13c3959cd8bed89590e7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-20T10:17:32.766587+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T10:17:32.767395+00:00_

1	meta:
2	  last_updated: '2026-05-20T04:43:12Z'
3	  total_papers: 53
4	categories:
5	- key: self_consistency_and_variants
6	  name: Self-Consistency & Variants
7	  narrative: SC decoding and improvements
8	- key: symbolic_reasoning_llm
9	  name: Neuro-Symbolic Reasoning
10	  narrative: LLMs combined with formal solvers
11	- key: maxsat_constraint_nlp
12	  name: MAX-SAT & Constraint NLP
13	  narrative: Constraint satisfaction applied to NLP
14	- key: folio_proofwriter_sota
15	  name: Benchmark SOTA
16	  narrative: SOTA methods on FOLIO/ProofWriter
17	- key: reasoning_model_diversity
18	  name: Reasoning Model Diversity
19	  narrative: Trace diversity in reasoning vs non-reasoning models
20	- key: multi_path_aggregation
21	  name: Multi-Path Aggregation
22	  narrative: Aggregating multiple reasoning paths
23	- key: verification_reranking
24	  name: Verification & Reranking
25	  narrative: ORM/PRM verification methods
26	- key: debate_multi_agent
27	  name: Debate & Multi-Agent
28	  narrative: Debate and multi-agent aggregation
29	- key: benchmarks_and_datasets
30	  name: Benchmarks & Datasets
31	  narrative: Evaluation datasets
32	- key: negative_results_analysis
33	  name: Negative Results
34	  narrative: Precedents for negative-result papers
35	- key: oracle_upper_bound_experiments
36	  name: Oracle Upper Bounds
37	  narrative: Oracle substitution diagnostics
38	- key: condorcet_voting_theory
39	  name: Condorcet & Voting Theory
40	  narrative: CJT, voting theory, ensemble independence
41	papers:
42	  wang2023sc:
43	    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models
44	    authors:
45	    - Wang et al.
46	    year: 2023
47	    venue: ICLR 2023
48	    bibtex_key: wang2023sc
49	    category: self_consistency_and_variants
50	    role: foundation
51	    relevance: Foundational SC method; our primary baseline
52	    verified: false
53	    added_by: migration
54	    added_at: '2026-05-20T04:43:12Z'
55	    arxiv_id: '2203.11171'
56	  chen20
…[truncated 30833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T10:17:32.767842+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"from core.tools.semantic_scholar import search_papers; print('S2 available')\" 2>&1 || echo \"S2 not available\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"from core.tools.semantic_scholar import search_papers; print('S2 available')\" 2>&1 || echo \"S2 not available\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T10:17:32.768205+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"from core.tools.literature import add_to_literature_map; print('literature tool available')\" 2>&1 || echo \"literature tool not available\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"from core.tools.literature import add_to_literature_map; print('literature tool available')\" 2>&1 || echo \"literature tool not available\""
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T10:17:32.768450+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    from core.tools.semantic_scholar import search_papers; print('S2 available')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'core'
S2 not available

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T10:17:32.768664+00:00_

Traceback (most recent call last):
  File "&lt;string>", line 1, in &lt;module>
    from core.tools.literature import add_to_literature_map; print('literature tool available')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'core'
literature tool not available

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T10:17:32.768942+00:00_

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
  "session": "worker_paper_research_20260520T101251",
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

_source line 8 · 2026-05-20T10:17:32.769160+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T10:17:32.769389+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LogicGuide symbolic reasoning LLM arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LogicGuide symbolic reasoning LLM arxiv"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-20T10:17:32.769586+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SatLM SAT-based language model reasoning arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SatLM SAT-based language model reasoning arxiv"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T10:17:32.769780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SymbCoT symbolic chain-of-thought reasoning arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SymbCoT symbolic chain-of-thought reasoning arxiv"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T10:17:32.769995+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "complexity-based prompting chain of thought Fu 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "complexity-based prompting chain of thought Fu 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T10:17:32.770192+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "He DeBERTa decoding-enhanced BERT pretraining arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "He DeBERTa decoding-enhanced BERT pretraining arxiv"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T10:17:32.770418+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "NLI verifier LLM reasoning natural language inference verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "NLI verifier LLM reasoning natural language inference verification"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T10:17:32.770624+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kadavath \"language models mostly know\" calibration arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kadavath \"language models mostly know\" calibration arxiv"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-20T10:17:32.770828+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "selective prediction large language models abstention arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "selective prediction large language models abstention arxiv"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T10:17:32.771106+00:00_

Web search results for query: "LogicGuide symbolic reasoning LLM arxiv"

Links: [{"title":"Neuro-Symbolic Artificial Intelligence: Towards Improving the Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2508.13678v1"},{"title":"Logic-LM: Empowering Large Language Models with Symbolic Solvers for   Faithful Logical Reasoning","url":"https://arxiv.org/pdf/2305.12295"},{"title":"Arxiv","url":"https://www.arxiv.org/pdf/2508.03366"},{"title":"[2305.12295] Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning","url":"https://arxiv.org/abs/2305.12295"},{"title":"Non-Interactive Symbolic-Aided Chain-of-Thought for Logical Reasoning","url":"https://arxiv.org/pdf/2508.12425"},{"title":"[2405.18357] Faithful Logical Reasoning via Symbolic Chain-of-Thought","url":"https://arxiv.org/abs/2405.18357"},{"title":"GitHub - teacherpeterpan/Logic-LLM: The project page for \"LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning\" · GitHub","url":"https://github.com/teacherpeterpan/Logic-LLM"}]

Based on the search results, I found information about LogicGuide and related symbolic reasoning approaches for LLMs:

LogicGuide (Poesia et al., 2024) introduces a general logical reasoning system to assist LLMs by formalizing the reasoning process to ensure that step-by-step reasoning remains sound and reliable.

The search results show that LogicGuide is part of a broader research area focused on enhancing LLMs' logical reasoning capabilities through symbolic approaches. Other related work in this area includes:

- Logic-LM, which integrates LLMs with symbolic solvers by first utilizing LLMs to translate natural language problems into symbolic formulation, then having a deterministic symbolic solver perform inference on the formulated problem.

- SymbCoT (Symbolic Chain-of-Thought), an LLM-based framework that translates natural language context into symbolic format and derives step-by
…[truncated 340 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T10:17:32.771521+00:00_

Web search results for query: "SymbCoT symbolic chain-of-thought reasoning arxiv"

Links: [{"title":"Faithful Logical Reasoning via Symbolic Chain-of-Thought","url":"https://www.summarizepaper.com/en/arxiv-id/2405.18357v1/"},{"title":"[2405.18357] Faithful Logical Reasoning via Symbolic Chain-of-Thought","url":"https://arxiv.org/abs/2405.18357"},{"title":"[2405.18357v1] Faithful Logical Reasoning via Symbolic Chain-of-Thought","url":"https://arxiv.org/abs/2405.18357v1"},{"title":"[2405.18357v2] Faithful Logical Reasoning via Symbolic Chain-of-Thought","url":"https://arxiv.org/abs/2405.18357v2"},{"title":"Faithful Logical Reasoning via Symbolic Chain-of-Thought | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/faithful-logical-reasoning-via-symbolic-chain-thought"},{"title":"[PDF] Faithful Logical Reasoning via Symbolic Chain-of-Thought | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Faithful-Logical-Reasoning-via-Symbolic-Xu-Fei/1b1265a7fc7debcdd0cd92fc1d9b51fc55d57fdc"},{"title":"Faithful Logical Reasoning via Symbolic Chain-of-Thought | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/faithful-logical-reasoning-via-symbolic-chain-of-thought-d44b5d8e90ba"},{"title":"GitHub - Aiden0526/SymbCoT: Codes and Data for ACL 2024 Paper \"Faithful Logical Reasoning via Symbolic Chain-of-Thought\". · GitHub","url":"https://github.com/Aiden0526/SymbCoT"}]

I found comprehensive information about SymbCoT! Here's what the research shows:

## Overview

SymbCoT is a fully LLM-based framework that integrates symbolic expressions and logic rules with Chain-of-Thought prompting to strengthen the logical reasoning capability of LLMs.

## The Problem it Addresses

While Chain-of-Thought technique enhances the reasoning ability of LLMs, it might still struggle in handling logical reasoning that relies much on symbolic expressions and rigid deducing rules.

## How it Works

SymbCoT first translates the natura
…[truncated 753 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T10:17:32.771813+00:00_

Web search results for query: "SatLM SAT-based language model reasoning arxiv"

Links: [{"title":"[2305.09656] SatLM: Satisfiability-Aided Language Models Using Declarative Prompting","url":"https://ar5iv.labs.arxiv.org/html/2305.09656"},{"title":"[2305.09656] SatLM: Satisfiability-Aided Language Models Using Declarative Prompting","url":"https://arxiv.org/abs/2305.09656"},{"title":"SATLM: Satisfiability-Aided Language Models Using Declarative Prompting Xi Ye","url":"https://arxiv.org/pdf/2305.09656"},{"title":"SATLM: satisfiability-aided language models using ...","url":"https://dl.acm.org/doi/10.5555/3666122.3668096"},{"title":"Can Large Language Models Reason? A Characterization via 3-SAT","url":"https://arxiv.org/html/2408.07215v2"},{"title":"[2505.16368] SATURN: SAT-based Reinforcement Learning to Unleash LLMs Reasoning","url":"https://arxiv.org/abs/2505.16368"},{"title":"SATURN: SAT-based Reinforcement Learning to Unleash Language Model Reasoning","url":"https://arxiv.org/html/2505.16368v1"}]

I found comprehensive information about SatLM. Here are the key findings:

## Overview

SatLM is a satisfiability-aided language modeling approach for improving the reasoning capabilities of LLMs. It uses declarative prompting and casts natural language reasoning problems as satisfiability (SAT) problems.

## How It Works

The approach uses an LLM to generate a declarative task specification rather than an imperative program and leverages an off-the-shelf automated theorem prover to derive the final answer. While program-aided approaches work well for tasks that require forward reasoning, they are less effective for constraint solving problems that require more sophisticated planning and search.

## Key Advantages

The declarative specification is closer to the problem description than the reasoning steps are, so the LLM can parse it out of the description more accurately. Additionally, by offloading the actual reasoning task to an automated theorem prover, the approach 
…[truncated 668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T10:17:32.772132+00:00_

Web search results for query: "He DeBERTa decoding-enhanced BERT pretraining arxiv"

Links: [{"title":"[PDF] DeBERTa: Decoding-enhanced BERT with Disentangled Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeBERTa:-Decoding-enhanced-BERT-with-Disentangled-He-Liu/14b65a86c82e38fce0eb3506e0d4084ad5cdb583"},{"title":"[2006.03654] DeBERTa: Decoding-enhanced BERT with Disentangled Attention","url":"https://arxiv.org/abs/2006.03654"},{"title":"[2006.03654v1] DeBERTa: Decoding-enhanced BERT with Disentangled Attention","url":"https://arxiv.org/abs/2006.03654v1"},{"title":"[2006.03654v6] DeBERTa: Decoding-enhanced BERT with Disentangled Attention","url":"https://arxiv.org/abs/2006.03654v6"},{"title":"DeBERTa: Decoding-enhanced BERT with Disentangled Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200603654H"},{"title":"deberta: decoding-enhanced bert with dis","url":"https://arxiv.org/pdf/2006.03654"},{"title":"[PDF] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeBERTaV3:-Improving-DeBERTa-using-ELECTRA-Style-He-Gao/972706306f85b1bfb40c7d35c796ad5174eb0c9c"},{"title":"DeBERTa: Decoding-Enhanced BERT with Disentangled Attention - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/deberta-decoding-enhanced-bert-with-disentangled-attention-2/"}]

Based on the search results, I found information about the DeBERTa paper you're looking for:

DeBERTa (Decoding-enhanced BERT with disentangled attention) is a new model architecture that improves the BERT and RoBERTa models using two novel techniques.

The first technique is the disentangled attention mechanism, where each word is represented using two vectors that encode its content and position, respectively, and the attention weights among words are computed using disentangled matrices on their contents and relative positions, resp
…[truncated 594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T10:17:32.772424+00:00_

Web search results for query: "complexity-based prompting chain of thought Fu 2023 arxiv"

Links: [{"title":"Chain-of-Thought Prompting: A Comprehensive Analysis of Reasoning Techniques in Large Language Models | by Pier-Jean Malandrino | Scub-Lab","url":"https://lab.scub.net/chain-of-thought-prompting-a-comprehensive-analysis-of-reasoning-techniques-in-large-language-b67fdd2eb72a?gi=df023719e094"},{"title":"Understanding Chain-of-Thought Prompting","url":"https://dzone.com/articles/chain-of-thought-prompting"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"},{"title":"Multi-Step Reasoning with Large Language Models, a Survey","url":"https://arxiv.org/html/2407.11511v2"},{"title":"Pattern-Aware Chain-of-Thought Prompting in Large Language Models","url":"https://arxiv.org/html/2404.14812v1"},{"title":"Enhancing Chain of Thought Prompting in Large Language Models via Reasoning Patterns","url":"https://arxiv.org/html/2404.14812v2"},{"title":"[2210.00720] Complexity-Based Prompting for Multi-Step Reasoning","url":"https://arxiv.org/abs/2210.00720"},{"title":"[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models","url":"https://arxiv.org/abs/2201.11903"},{"title":"Complexity-Based Prompting for Multi-Step Reasoning","url":"https://arxiv.org/pdf/2210.00720"}]

Based on the search results, I found information about the paper you're looking for:

The paper is "Complexity-based prompting for multi-step reasoning" by Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark, and Tushar Khot, published in The Eleventh International Conference on Learning Representations (ICLR 2023) in Kigali, Rwanda in May 2023. The arXiv preprint identifier is arXiv:2210.00720.

The work studies the impact of the complexity of the reasoning chain (the number of steps) and introduces a reasoning approach called complexity-based prompting. Complexity-based prompting chooses examples with complex reas
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T10:17:32.772721+00:00_

Web search results for query: "Kadavath "language models mostly know" calibration arxiv"

Links: [{"title":"[PDF] Language Models (Mostly) Know What They Know | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927"},{"title":"Language Models (Mostly) Know What They Know","url":"https://bibbase.org/network/publication/kadavath-conerly-askell-henighan-drain-perez-schiefer-hatfielddodds-etal-languagemodelsmostlyknowwhattheyknow-2022"},{"title":"Language Models (Mostly) Know What They Know | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2683f0b3b83a56dc82614c7e4257c3b6d/lumeng"},{"title":"Do Large Language Models Know What They Don’t Know? Evaluating Epistemic Calibration via Prediction Markets","url":"https://arxiv.org/html/2512.16030"},{"title":"[2211.00151] A Close Look into the Calibration of Pre-trained Language Models","url":"https://ar5iv.labs.arxiv.org/html/2211.00151"},{"title":"(PDF) Language Models (Mostly) Know What They Know (2022) | Saurav Kadavath | 413 Citations","url":"https://scispace.com/papers/language-models-mostly-know-what-they-know-zkg0pou4"},{"title":"Calibrating Large Language Models with Sample Consistency","url":"https://arxiv.org/html/2402.13904"},{"title":"[2207.05221] Language Models (Mostly) Know What They Know","url":"https://arxiv.org/abs/2207.05221"},{"title":"Language Models (Mostly) Know What They Know - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022arXiv220705221K/abstract"}]

I found the research paper you were looking for! Here's what I found:

The paper "Language Models (Mostly) Know What They Know" by Saurav Kadavath and 35 other authors studies whether language models can evaluate the validity of their own claims and predict which questions they will be able to answer correctly.

The research shows that larger models are well-calibrated on diverse multiple choice and true/false questions when they are provid
…[truncated 830 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T10:17:32.773038+00:00_

Web search results for query: "NLI verifier LLM reasoning natural language inference verification"

Links: [{"title":"Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning","url":"https://arxiv.org/html/2601.05705v1"},{"title":"Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/verification-refinement-natural-language-explanations-through-llm"},{"title":"Verification and Refinement of Natural Language ...","url":"https://www.emergentmind.com/papers/2405.01379"},{"title":"Logic-Parametric Neuro-Symbolic NLI: Controlling Logical Formalisms for Verifiable LLM Reasoning","url":"https://arxiv.org/pdf/2601.05705"},{"title":"Verification and Refinement of Natural Language Explanations through   LLM-Symbolic Theorem Proving","url":"https://arxiv.org/pdf/2405.01379"},{"title":"Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving","url":"https://arxiv.org/html/2405.01379v2"},{"title":"[2405.01379v1] Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving","url":"https://arxiv.org/abs/2405.01379v1"},{"title":"Faithful and Robust LLM-Driven Theorem Proving for NLI Explanations","url":"https://arxiv.org/pdf/2505.24264"}]

I've found comprehensive search results on NLI verifiers and LLM reasoning for natural language inference verification. Here's what the research shows:

## Key Approaches

Large language models (LLMs) and theorem provers (TPs) can be effectively combined for verifiable natural language inference (NLI). This neuro-symbolic approach has become a prominent direction in the field.

## Notable Frameworks

**Explanation-Refiner**: A neuro-symbolic framework that integrates TPs with LLMs to generate and formalize explanatory sentences and suggest potential inference strategies for NLI, with the TP employed to provide form
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T10:17:32.773351+00:00_

Web search results for query: "selective prediction large language models abstention arxiv"

Links: [{"title":"Selective “Selective Prediction”: Reducing Unnecessary Abstention in Vision-Language Reasoning","url":"https://arxiv.org/html/2402.15610v2"},{"title":"Adaptation with Self-Evaluation to Improve Selective Prediction in LLMs","url":"https://arxiv.org/pdf/2310.11689"},{"title":"[2402.15610] Selective \"Selective Prediction\": Reducing Unnecessary Abstention in Vision-Language Reasoning","url":"https://arxiv.org/abs/2402.15610"},{"title":"Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations","url":"https://mediatum.ub.tum.de/doc/1833233/myixm5kiahv0gqrhyi3qfc56g.2404.10960v1.pdf"},{"title":"The Art of Refusal: A Survey of Abstention in Large Language Models","url":"https://arxiv.org/html/2407.18418v1"},{"title":"Know Your Limits: A Survey of Abstention in Large Language Models","url":"https://arxiv.org/html/2407.18418v2"},{"title":"Selective \"Selective Prediction\": Reducing Unnecessary Abstention in   Vision-Language Reasoning","url":"https://arxiv.org/pdf/2402.15610"},{"title":"Do LLMs Know When to NOT Answer? Investigating Abstention Abilities of Large Language Models","url":"https://arxiv.org/html/2407.16221v1"},{"title":"Geometry-Calibrated Conformal Abstention for Language Models","url":"https://arxiv.org/html/2604.27914"},{"title":"Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models","url":"https://arxiv.org/html/2502.06884v1"}]

Here are the search results for "selective prediction large language models abstention arxiv":

The search returned several relevant papers on this topic:

1. **ReCoVERR** - Selective prediction minimizes incorrect predictions from vision-language models (VLMs) by allowing them to abstain from answering when uncertain. However, selective prediction may be over-cautious and abstain too frequently, even on many correct predictions. ReCoVERR is
…[truncated 1191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T10:17:32.773677+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Poesia LogicGuide guided reasoning LLM 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Poesia LogicGuide guided reasoning LLM 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-20T10:17:32.773917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu RoBERTa robustly optimized BERT pretraining arxiv 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu RoBERTa robustly optimized BERT pretraining arxiv 2019"
  }
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T10:17:32.774141+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DeBERTaV3 improving DeBERTa ELECTRA He 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DeBERTaV3 improving DeBERTa ELECTRA He 2023 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-20T10:17:32.774365+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "cross-encoder NLI fact verification MNLI textual entailment reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "cross-encoder NLI fact verification MNLI textual entailment reasoning"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T10:17:32.774576+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Geifman selective prediction deep neural networks 2017 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Geifman selective prediction deep neural networks 2017 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-20T10:17:32.774783+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Guo calibration modern neural networks 2017 ICML"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Guo calibration modern neural networks 2017 ICML"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T10:17:32.775026+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"self-evaluation improves selective generation\" Ren Zhao LLM 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"self-evaluation improves selective generation\" Ren Zhao LLM 2023 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T10:17:32.775283+00:00_

Web search results for query: "Liu RoBERTa robustly optimized BERT pretraining arxiv 2019"

Links: [{"title":"[PDF] RoBERTa: A Robustly Optimized BERT Pretraining Approach | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RoBERTa:-A-Robustly-Optimized-BERT-Pretraining-Liu-Ott/077f8329a7b6fa3b7c877a57b81eb6c18b5f87de"},{"title":"Liu, Yinhan, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. “RoBERTa: A Robustly Optimized BERT Pretraining Approach.” arXiv, July 26, 2019. - Virtual Routes","url":"https://virtual-routes.org/portal-item/roberta-a-robustly-optimized-bert-pretraining-approach-lui-et-al-2019/"},{"title":"RoBERTa- A Robustly Optimized BERT Pretraining Approach","url":"https://hyunyoung2.github.io/2021/03/15/RoBERTa/"},{"title":"[1907.11692] RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://arxiv.org/abs/1907.11692"},{"title":"[1907.11692v1] RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://arxiv.org/abs/1907.11692v1"},{"title":"[1907.11692] RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://ar5iv.labs.arxiv.org/html/1907.11692"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach","url":"https://scispace.com/pdf/roberta-a-robustly-optimized-bert-pretraining-approach-2rj0bdyhim.pdf"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190711692L/abstract"},{"title":"RoBERTa: A Robustly Optimized BERT Pretraining Approach | OpenReview","url":"https://openreview.net/forum?id=SyxS0T4tvS"}]

Based on the search results, here's what I found about the paper:

The paper "RoBERTa: A Robustly Optimized BERT Pretraining Approach" was authored by Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov, published on arxiv.org on July 26, 2019, with the identi
…[truncated 854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-20T10:17:32.775580+00:00_

Web search results for query: "DeBERTaV3 improving DeBERTa ELECTRA He 2023 arxiv"

Links: [{"title":"[2111.09543v1] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v1"},{"title":"[2111.09543v4] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v4"},{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543"},{"title":"[2111.09543v2] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543v2"},{"title":"Published as a conference paper at ICLR 2023 DEBERTAV3: IMPROVING DEBERTA USING","url":"https://arxiv.org/pdf/2111.09543"},{"title":"[PDF] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeBERTaV3:-Improving-DeBERTa-using-ELECTRA-Style-He-Gao/972706306f85b1bfb40c7d35c796ad5174eb0c9c"},{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://ar5iv.labs.arxiv.org/html/2111.09543"},{"title":"Work in progress DeBERTaV3: Improving DeBERTa using ELECTRA-","url":"https://arxiv.org/pdf/2111.09543v1"},{"title":"GitHub - microsoft/DeBERTa: The implementation of DeBERTa · GitHub","url":"https://github.com/microsoft/DeBERTa"}]

I found the paper you're looking for! Here are the key findings:

## Paper Overview

DeBERTaV3 improves the original DeBERTa model by replacing mask language modeling (MLM) with replaced token detection (RTD), a more sample-efficient pre-training task.

## Key Problem and Solution

Vanilla embedding sharing in ELECTRA hurts training efficiency and model pe
…[truncated 767 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T10:17:32.775853+00:00_

Web search results for query: "Poesia LogicGuide guided reasoning LLM 2023 arxiv"

Links: [{"title":"[2306.04031] Certified Deductive Reasoning with Language Models","url":"https://arxiv.org/abs/2306.04031"},{"title":"CERTIFIED DEDUCTIVE REASONING WITH LANGUAGE MODELS","url":"https://arxiv.org/pdf/2306.04031"},{"title":"Guiding Reasoning in Small Language Models with LLM Assistance","url":"https://arxiv.org/html/2504.09923v2"},{"title":"Problem-Solving Logic Guided Curriculum In-Context Learning for LLMs Complex Reasoning","url":"https://arxiv.org/html/2502.15401v1"},{"title":"From Implicit Exploration to Structured Reasoning: Leveraging Guideline and Refinement for LLMs","url":"https://arxiv.org/pdf/2509.06284"}]

I found the paper you're looking for! The paper is titled "Certified Deductive Reasoning with Language Models" by Gabriel Poesia and other authors, published on arXiv in June 2023.

Here's what the paper is about:

The paper introduces a class of tools for language models called "guides" that use state and incremental constraints to guide generation, with a specific implementation called LogicGuide for logical reasoning. The work addresses the issue that language models often produce logically unsound or inconsistent rationales, which is particularly problematic when reliable reasoning traces are needed for self-improvement.

In experiments on PrOntoQA, ProofWriter and Syllogism Validity datasets, LogicGuide significantly improves the performance of GPT-3, GPT-3.5 Turbo and LLaMA (with accuracy gains up to 35%), while reducing content effects. By training only on certified self-generated reasoning, models can self-improve while avoiding learning from their own hallucinations.

You can access the paper at: https://arxiv.org/abs/2306.04031


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-20T10:17:32.776173+00:00_

Web search results for query: "Geifman selective prediction deep neural networks 2017 arxiv"

Links: [{"title":"[1705.08500] Selective Classification for Deep Neural Networks","url":"https://arxiv.org/abs/1705.08500"},{"title":"[PDF] Selective Classification for Deep Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Selective-Classification-for-Deep-Neural-Networks-Geifman-El-Yaniv/2ed7cc027367295b1a7d7cd49406acfa5c580138"},{"title":"(PDF) Selective Classification for Deep Neural Networks","url":"https://www.researchgate.net/publication/317100919_Selective_Classification_for_Deep_Neural_Networks"},{"title":"GitHub - geifmany/selective_deep_learning: Code for the paper \"Selective Classification for Deep Neural Networks\" · GitHub","url":"https://github.com/geifmany/selective_deep_learning"},{"title":"Ran El-Yaniv","url":"https://geifmany.github.io/papers/Phd_talk.pdf"},{"title":"[1901.09192] SelectiveNet: A Deep Neural Network with an Integrated Reject Option","url":"https://arxiv.org/abs/1901.09192"},{"title":"ICML oral selectivenet_pdf","url":"https://geifmany.github.io/papers/icml_oral.pdf"},{"title":"[PDF] SelectiveNet: A Deep Neural Network with an Integrated Reject Option | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SelectiveNet:-A-Deep-Neural-Network-with-an-Reject-Geifman-El-Yaniv/0e587ccf0395daf87a29caa6ec94741339fa2a4b"},{"title":"Bridging the Gap Between Active Learning and Selective ...","url":"https://arxiv.org/pdf/2304.03870"},{"title":"A Deep Neural Network with an Integrated Reject Option","url":"http://proceedings.mlr.press/v97/geifman19a/geifman19a.pdf"}]

I found the paper you're looking for! Here are the key details:

**Title:** Selective Classification for Deep Neural Networks

**Authors:** Yonatan Geifman and Ran El-Yaniv

**Publication:** Published in Advances in Neural Information Processing Systems, 2017

**ArXiv ID:** 1705.08500

**Main Contribution:** The paper presents a method to constru
…[truncated 647 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T10:17:32.776474+00:00_

Web search results for query: "Guo calibration modern neural networks 2017 ICML"

Links: [{"title":"\"On Calibration of Modern Neural Networks\", Guo et al. • David Stutz","url":"https://davidstutz.de/on-calibration-of-modern-neural-networks-guo-et-al/"},{"title":"Neural Network Calibration","url":"https://geoffpleiss.com/blog/nn_calibration.html"},{"title":"On Calibration of Modern Neural Networks","url":"https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Calibration_of_Neural_Nets.md"},{"title":"On Calibration of Modern Neural Networks Chuan Guo Kilian Q. Weinberger","url":"https://fernandoperezc.github.io/Advanced-Topics-in-Machine-Learning-and-Data-Science/Fluri.pdf"},{"title":"On Calibration of Modern Neural Networks","url":"https://proceedings.mlr.press/v70/guo17a.html"},{"title":"On calibration of modern neural networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305518"},{"title":"On Calibration of Modern Neural Networks","url":"https://arxiv.org/pdf/1706.04599"},{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"Guo, C., Pleiss, G., Sun Y. and Weinberger, K.Q. (2017）On Calibration of Modern Neural Networks. Proceedings of the 34th International Conference on Machine Learning, Sydney, Vol. 70, 1321-1330. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(czeh4tfqyw2orz553k1w0r45))/reference/referencespapers?referenceid=3648829"},{"title":"[PDF] On Calibration of Modern Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Calibration-of-Modern-Neural-Networks-Guo-Pleiss/d65ce2b8300541414bfe51d03906fca72e93523c"}]

I found information about the Guo et al. paper on neural network calibration. Here are the key findings:

## Paper Overview

The paper "On Calibration of Modern Neural Networks" was authored by Chuan Guo, Geoff Pleiss, Yu Sun, a
…[truncated 1206 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T10:17:32.776775+00:00_

Web search results for query: "cross-encoder NLI fact verification MNLI textual entailment reasoning"

Links: [{"title":"Natural Language Inference (NLI) — Also Known as Recognizing Textual Entailment (RTE) | by Julian Wang | Medium","url":"https://medium.com/@j.wang.mlds_97641/natural-language-inference-nli-also-known-as-recognizing-textual-entailment-rte-384295708089"},{"title":"Cross-Document Cross-Lingual Natural Language Inference via RST-enhanced Graph Fusion and Interpretability Prediction","url":"https://arxiv.org/html/2504.12324v1"},{"title":"Minds versus Machines: Rethinking Entailment Verification with Language Models","url":"https://arxiv.org/html/2402.03686v1"},{"title":"NLI Cross Encoders: 6 Ways to Use Them","url":"https://huggingface.co/blog/dleemiller/nli-xenc-ways-to-use"},{"title":"Natural Language Inference: An Overview | Towards Data Science","url":"https://towardsdatascience.com/natural-language-inference-an-overview-57c0eecf6517/"},{"title":"cross-encoder/nli-distilroberta-base · Hugging Face","url":"https://huggingface.co/cross-encoder/nli-distilroberta-base"},{"title":"Are Machines Better at Complex Reasoning? Unveiling Human-Machine   Inference Gaps in Entailment Verification","url":"https://arxiv.org/pdf/2402.03686"}]

I've completed the web search for your query. Here are the key findings:

## Overview of NLI, Cross-Encoders, and Fact Verification

Natural Language Inference (NLI), also known historically as Recognizing Textual Entailment (RTE), is a foundational task in natural language understanding that challenges machines to reason about relationships between text pairs, determining whether a hypothesis logically follows from a premise.

The task has three possible outcomes: Entailment (the hypothesis must be true if the premise is true), Contradiction (the hypothesis must be false if the premise is true), and Neutral (the truth of the hypothesis cannot be determined from the premise).

## Cross-Encoders for NLI

Cross-encoder models 
…[truncated 788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T10:17:32.777085+00:00_

Web search results for query: ""self-evaluation improves selective generation" Ren Zhao LLM 2023 arxiv"

Links: [{"title":"[2312.09300] Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/abs/2312.09300"},{"title":"Paper page - Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://huggingface.co/papers/2312.09300"},{"title":"Think Twice Before Assure: Confidence Estimation for Large Language Models through Reflection on Multiple Answers","url":"https://arxiv.org/html/2403.09972v1"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://proceedings.mlr.press/v239/ren23a.html"},{"title":"LLMs can learn self-restraint through iterative self-reflection","url":"https://arxiv.org/html/2405.13022v2"},{"title":"Steering Large Language Models to Evaluate and Amplify Creativity","url":"https://arxiv.org/html/2412.06060v1"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/pdf/2312.09300"},{"title":"[PDF] Self-Evaluation Improves Selective Generation in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/04365f0f1db4c659c3297cb8e70c39b38ed3b487"},{"title":"Self-Evaluation Improves Selective Generation in Large Language Models","url":"https://arxiv.org/html/2312.09300v1"}]

I found the paper you're looking for! 

The paper "Self-Evaluation Improves Selective Generation in Large Language Models" has authors Jie Ren, Yao Zhao, Tu Vu, Peter J. Liu, and Balaji Lakshminarayanan, and it was published on December 14, 2023 as arXiv preprint arXiv:2312.09300.

The paper addresses how safe deployment of large language models (LLMs) may benefit from a reliable method for assessing their generated content to determine when to abstain or to selectively generate. The authors instruct an LLM to self-evaluate its answers, employing either a multi-way comparison or a point-wise evaluati
…[truncated 491 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T10:17:32.777391+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Williams Bowman MNLI multi-genre natural language inference 2018 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Williams Bowman MNLI multi-genre natural language inference 2018 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-20T10:17:32.777608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Thorne FEVER fact extraction verification NLI 2018 NAACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Thorne FEVER fact extraction verification NLI 2018 NAACL"
  }
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T10:17:32.777824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Honovich TRUE evaluating factual consistency NLI 2022 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Honovich TRUE evaluating factual consistency NLI 2022 arxiv"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T10:17:32.778057+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Xiong \"can LLMs express uncertainty\" calibration verbalized confidence 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Xiong \"can LLMs express uncertainty\" calibration verbalized confidence 2024 arxiv"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-20T10:17:32.778345+00:00_

Web search results for query: "Thorne FEVER fact extraction verification NLI 2018 NAACL"

Links: [{"title":"FEVER: a Large-scale Dataset for Fact Extraction and VERification - ACL Anthology","url":"https://aclanthology.org/N18-1074/"},{"title":"Fact Extraction and VERification","url":"https://fever.ai/dataset/fever.html"},{"title":"Combining Fact Extraction and Verification withNeural ...","url":"https://arxiv.org/pdf/1811.07039"},{"title":"fever/fever · Datasets at Hugging Face","url":"https://huggingface.co/datasets/fever/fever"},{"title":"fever · Datasets at Hugging Face","url":"https://huggingface.co/datasets/fever"},{"title":"First Workshop on Fact Extraction and VERification","url":"https://fever.ai/2018/workshop.html"},{"title":"[1803.05355] FEVER: a large-scale dataset for Fact Extraction and VERification","url":"https://arxiv.org/abs/1803.05355"},{"title":"[PDF] FEVER: a Large-scale Dataset for Fact Extraction and VERification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/FEVER:-a-Large-scale-Dataset-for-Fact-Extraction-Thorne-Vlachos/b1d24e8e08435b7c52335485a0d635abf9bc604c"},{"title":"(PDF) FEVEROUS: Fact Extraction and VERification Over Unstructured and Structured information","url":"https://www.researchgate.net/publication/352308193_FEVEROUS_Fact_Extraction_and_VERification_Over_Unstructured_and_Structured_information"},{"title":"FEVER: a large-scale dataset for Fact Extraction and VERification","url":"https://arxiv.org/pdf/1803.05355"}]

Based on the search results, here's what I found about the FEVER paper by Thorne et al. at NAACL 2018:

## Overview

The FEVER (Fact Extraction and VERification) paper introduces a new publicly available dataset for verification against textual sources, authored by James Thorne, Andreas Vlachos, Christos Christodoulopoulos, and Arpit Mittal.

## Dataset Characteristics

The dataset consists of 185,445 claims generated by altering sentences extracted from Wikipedia and subsequently verified without kn
…[truncated 950 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T10:17:32.778653+00:00_

Web search results for query: "Honovich TRUE evaluating factual consistency NLI 2022 arxiv"

Links: [{"title":"[PDF] TRUE: Re-evaluating Factual Consistency Evaluation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TRUE:-Re-evaluating-Factual-Consistency-Evaluation-Honovich-Aharoni/c69f9a5185b4c29525bedb2dcc79d20b42c14cc6"},{"title":"[2204.04991] TRUE: Re-evaluating Factual Consistency Evaluation","url":"https://arxiv.org/abs/2204.04991"},{"title":"(PDF) TRUE: Re-evaluating Factual Consistency Evaluation","url":"https://www.researchgate.net/publication/361069161_TRUE_Re-evaluating_Factual_Consistency_Evaluation"},{"title":"Multilingual Summarization with Factual Consistency Evaluation","url":"https://arxiv.org/html/2212.10622v2"},{"title":"TRUE: Re-evaluating Factual Consistency Evaluation - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.287/"},{"title":"Less is More for Improving Automatic Evaluation of Factual Consistency","url":"https://arxiv.org/html/2404.06579v1"},{"title":"TRUE: Re-evaluating Factual Consistency Evaluation Or HonovichT ∗ Roee AharoniG","url":"https://arxiv.org/pdf/2204.04991"},{"title":"TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models","url":"https://arxiv.org/html/2305.11171"},{"title":"Verify with Caution: The Pitfalls of Relying on Imperfect Factuality Metrics","url":"https://arxiv.org/html/2501.14883v2"},{"title":"TRUE: Re-evaluating Factual Consistency Evaluation | Request PDF","url":"https://www.researchgate.net/publication/362262710_TRUE_Re-evaluating_Factual_Consistency_Evaluation"}]

Based on the search results, I found information about the TRUE paper by Honovich et al. Here's what I found:

## TRUE: Re-evaluating Factual Consistency Evaluation

The paper "TRUE: Re-evaluating Factual Consistency Evaluation" was authored by Or Honovich, Roee Aharoni, Jonathan Herzig, Hagai Taitelbaum, Doron Kukliansy, Vered Cohen, Thomas Scialom, Idan Szpektor, Avinatan Hassidim, and Yos
…[truncated 978 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-20T10:17:32.778966+00:00_

Web search results for query: "Xiong "can LLMs express uncertainty" calibration verbalized confidence 2024 arxiv"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"On Verbalized Confidence Scores for LLMs Daniel Yang∗ ETH Zurich","url":"https://arxiv.org/pdf/2412.14737"},{"title":"Rewarding Doubt: A Reinforcement Learning Approach to ...","url":"https://arxiv.org/pdf/2503.02623"},{"title":"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs","url":"https://arxiv.org/html/2306.13063v2"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey","url":"https://arxiv.org/html/2503.15850v1"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"[2306.13063] Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs","url":"https://arxiv.org/abs/2306.13063"},{"title":"LLMs Should Express Uncertainty Explicitly","url":"https://arxiv.org/pdf/2604.05306"},{"title":"Uncertainty Distillation: Teaching Language Models to Express Semantic Confidence","url":"https://arxiv.org/pdf/2503.14749"}]

I found research related to your query. The main paper you're looking for appears to be "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs" by Xiong et al.

The paper focuses on empowering large language models to accurately express confidence in their answers, which is essential for trustworthy decision-making. Confidence elicitation is the process of estimating LLM's confidence in their responses without model fine-tuning or accessing internal information, and the concept of verbalized confidence prompts LLMs to express confidence directly.

Key findings include that prompting strategies can mitigate overconfidence, though improvements diminish as
…[truncated 451 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T10:17:32.779265+00:00_

Web search results for query: "Williams Bowman MNLI multi-genre natural language inference 2018 arxiv"

Links: [{"title":"Lost in Inference: Rediscovering the Role of Natural Language Inference for Large Language Models","url":"https://arxiv.org/html/2411.14103v1"},{"title":"MultiNLI","url":"https://cims.nyu.edu/~sbowman/multinli/"},{"title":"[2106.09449] DocNLI: A Large-scale Dataset for Document-level Natural Language Inference","url":"https://ar5iv.labs.arxiv.org/html/2106.09449"},{"title":"A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference - ACL Anthology","url":"https://aclanthology.org/N18-1101/"},{"title":"[1704.05426] A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference","url":"https://arxiv.org/abs/1704.05426"},{"title":"[1704.05426v2] A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference","url":"https://arxiv.org/abs/1704.05426v2"},{"title":"Are Natural Language Inference Models IMPPRESsive? Learning IMPlicature   and PRESupposition","url":"https://arxiv.org/pdf/2004.03066"},{"title":"Annotation Artifacts in Natural Language Inference Data","url":"https://arxiv.org/pdf/1803.02324"},{"title":"Don't Learn, Ground: A Case for Natural Language Inference with Visual Grounding","url":"https://arxiv.org/pdf/2511.17358"}]

Based on the search results, I found information about the paper you're looking for:

The paper "A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference" was authored by Adina Williams, Nikita Nangia, and Samuel Bowman and was published in 2018 in the Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies.

This paper introduces the Multi-Genre Natural Language Inference (MultiNLI) corpus, a dataset designed for use in the development and evaluation of machine learning models for sentence understanding. The corpus contains 433k examples and offers data from t
…[truncated 470 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T10:17:32.779641+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "old_string": "- key: condorcet_voting_theory\n  name: Condorcet & Voting Theory\n  narrative: CJT, voting theory, ensemble independence",
  "new_string": "- key: condorcet_voting_theory\n  name: Condorcet & Voting Theory\n  narrative: CJT, voting theory, ensemble independence\n- key: nli_verification\n  name: NLI as Verification\n  narrative: Natural language inference models used for fact/reasoning verification\n- key: calibration_selective_prediction\n  name: Calibration & Selective Prediction\n  narrative: Confidence calibration, selective prediction, and abstention in neural networks and LLMs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "old_string": "- key: condorcet_voting_theory\n  name: Condorcet & Voting Theory\n  narrative: CJT, voting theory, ensemble independence",
    "new_string": "- key: condorcet_voting_theory\n  name: Condorcet & Voting Theory\n  narrative: CJT, voting theory, ensemble independence\n- key: nli_verification\n  name: NLI as Verification\n  narrative: Natural language inference models used for fact/reasoning verification\n- key: calibration_selective_prediction\n  name: Calibration & Selective Prediction\n  narrative: Confidence calibration, selective prediction, and abstention in neural networks and LLMs"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T10:17:32.780054+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T10:17:32.780504+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "offset": "800"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "offset": "800"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T10:17:32.780784+00:00_

800	    added_at: '2026-05-20T04:43:12Z'
801	  kish1965design:
802	    title: Survey Sampling
803	    authors:
804	    - Kish, Leslie
805	    year: 1965
806	    venue: John Wiley & Sons, New York, 1965
807	    bibtex_key: kish1965design
808	    category: condorcet_voting_theory
809	    role: foundation
810	    relevance: Source of the design effect formula Deff = 1 + (K-1)ρ, from which our Effective-K = K/Deff = K/(1+(K-1)κ) derives.
811	      Kish's design effect quantifies how clustering/correlation inflates variance relative to simple random sampling. Must
812	      cite when using Eff-K to avoid novelty overclaim — the formula is an established statistical concept applied to a new
813	      domain (LLM trace aggregation)
814	    verified: true
815	    added_by: migration
816	    added_at: '2026-05-20T04:43:12Z'
817	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T10:17:32.781215+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "old_string": "    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'",
  "new_string": "    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'\n  poesia2023logicguide:\n    title: Certified Deductive Reasoning with Language Models\n    authors:\n    - Poesia et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: poesia2023logicguide\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: Introduces LogicGuide, using state-based constraints to guide LLM generation for sound deductive\n      reasoning. Achieves up to +35% accuracy on ProofWriter/PrOntoQA. Complementary to SICA — LogicGuide constrains\n      generation, SICA aggregates post-hoc constraints.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.04031'\n  ye2024satlm:\n    title: 'SatLM: Satisfiability-Aided Language Models Using Declarative Prompting'\n    authors:\n    - Ye et al.\n    year: 2024\n    venue: NeurIPS 2023\n    bibtex_key: ye2024satlm\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: LLM generates declarative SAT specifications, offloads solving to automated theorem prover. Closest\n      to SICA's constraint-solving philosophy but uses single-path declarative prompting rather than multi-path\n      aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2305.09656'\n  xu2024symbcot:\n    title: Faithful Logical Reasoning via Symbolic Chain-of-Thought\n    authors:\n    - Xu et al.\n    year: 2024\n    venue: ACL 2024\n    bibtex_key: xu2024symbcot\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: SymbCoT translates NL to symbolic format, derives step-by-step plans with symbolic logic rules,\n      and verifies translation+reasoning. Evaluated on FOLIO. Single-path symbolic verification vs SICA's multi-path\n      constraint aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2405.18357'\n  fu2023complexity:\n    title: Complexity-Based Prompting for Multi-Step Reasoning\n    authors:\n    - Fu et al.\n    year: 2023\n    venue: ICLR 2023\n    bibtex_key: fu2023complexity\n    category: self_consistency_and_variants\n    role: foundation\n    relevance: Selects CoT exemplars with more reasoning steps (higher complexity), improving SC aggregation.\n      Shows that reasoning chain quality matters for SC — complementary to SICA's constraint-quality weighting.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2210.00720'\n  he2021deberta:\n    title: 'DeBERTa: Decoding-enhanced BERT with Disentangled Attention'\n    authors:\n    - He et al.\n    year: 2021\n    venue: ICLR 2021\n    bibtex_key: he2021deberta\n    category: nli_verification\n    role: foundation\n    relevance: Introduces disentangled attention and enhanced mask decoder. DeBERTa-large-MNLI is our primary\n      NLI cross-encoder for inter-trace entailment scoring in the SICA pipeline.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2006.03654'\n  liu2019roberta:\n    title: 'RoBERTa: A Robustly Optimized BERT Pretraining Approach'\n    authors:\n    - Liu et al.\n    year: 2019\n    venue: arXiv 2019\n    bibtex_key: liu2019roberta\n    category: nli_verification\n    role: foundation\n    relevance: Robustly optimized BERT pretraining. RoBERTa-large-MNLI serves as alternative NLI backbone\n      for entailment-based verification in our ablation experiments.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1907.11692'\n  williams2018mnli:\n    title: A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference\n    authors:\n    - Williams et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: williams2018mnli\n    category: nli_verification\n    role: foundation\n    relevance: Introduces Multi-Genre NLI (MultiNLI) corpus with 433k examples across 10 genres. The training\n      dataset for our DeBERTa/RoBERTa NLI cross-encoders used in SICA's entailment scoring.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1704.05426'\n  thorne2018fever:\n    title: 'FEVER: a Large-scale Dataset for Fact Extraction and VERification'\n    authors:\n    - Thorne et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: thorne2018fever\n    category: nli_verification\n    role: background\n    relevance: Establishes NLI-based fact verification paradigm with 185k claims against Wikipedia. Demonstrates\n      that entailment models can serve as verifiers — foundational for using NLI as reasoning verification.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1803.05355'\n  honovich2022true:\n    title: 'TRUE: Re-evaluating Factual Consistency Evaluation'\n    authors:\n    - Honovich et al.\n    year: 2022\n    venue: NAACL 2022\n    bibtex_key: honovich2022true\n    category: nli_verification\n    role: background\n    relevance: Shows NLI-based metrics achieve strong factual consistency evaluation across tasks. Validates\n      using NLI cross-encoders as general-purpose verification tools — supports our use of NLI for inter-trace\n      consistency checking.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2204.04991'\n  kadavath2022know:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Kadavath et al.\n    year: 2022\n    venue: arXiv 2022\n    bibtex_key: kadavath2022know\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Shows LLMs can predict P(I Know) — probability of answering correctly. Foundation for confidence-based\n      selective prediction. Motivates SICA's constraint-agreement as an alternative confidence signal to model\n      self-evaluation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2207.05221'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Guo et al.\n    year: 2017\n    venue: ICML 2017\n    bibtex_key: guo2017calibration\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Foundational work showing modern deep networks are poorly calibrated. Introduces temperature scaling\n      for post-hoc calibration. Provides theoretical grounding for why raw model confidence is unreliable —\n      motivates constraint-based confidence in SICA.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1706.04599'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Geifman, Yonatan\n    - El-Yaniv, Ran\n    year: 2017\n    venue: NeurIPS 2017\n    bibtex_key: geifman2017selective\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Formalizes selective classification with guaranteed risk control. Establishes the accuracy-coverage\n      tradeoff framework. SICA's constraint-satisfaction ratio can serve as a selection function for selective\n      prediction.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1705.08500'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Ren et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: ren2023selfevaluation\n    category: calibration_selective_prediction\n    role: background\n    relevance: LLM self-evaluation for selective generation via multi-way comparison and point-wise evaluation.\n      Shows self-assessment can improve abstention decisions. Contrast with SICA's external constraint-based\n      confidence rather than self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2312.09300'\n  xiong2024uncertainty:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Xiong et al.\n    year: 2024\n    venue: ICLR 2024\n    bibtex_key: xiong2024uncertainty\n    category: calibration_selective_prediction\n    role: background\n    relevance: Comprehensive evaluation of verbalized confidence elicitation showing overconfidence and limited\n      calibration in LLMs. Directly motivates SICA's approach — using symbolic constraint satisfaction as an\n      external confidence measure rather than relying on LLM self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.13063'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "old_string": "    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'",
    "new_string": "    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'\n  poesia2023logicguide:\n    title: Certified Deductive Reasoning with Language Models\n    authors:\n    - Poesia et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: poesia2023logicguide\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: Introduces LogicGuide, using state-based constraints to guide LLM generation for sound deductive\n      reasoning. Achieves up to +35% accuracy on ProofWriter/PrOntoQA. Complementary to SICA — LogicGuide constrains\n      generation, SICA aggregates post-hoc constraints.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.04031'\n  ye2024satlm:\n    title: 'SatLM: Satisfiability-Aided Language Models Using Declarative Prompting'\n    authors:\n    - Ye et al.\n    year: 2024\n    venue: NeurIPS 2023\n    bibtex_key: ye2024satlm\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: LLM generates declarative SAT specifications, offloads solving to automated theorem prover. Closest\n      to SICA's constraint-solving philosophy but uses single-path declarative prompting rather than multi-path\n      aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2305.09656'\n  xu2024symbcot:\n    title: Faithful Logical Reasoning via Symbolic Chain-of-Thought\n    authors:\n    - Xu et al.\n    year: 2024\n    venue: ACL 2024\n    bibtex_key: xu2024symbcot\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: SymbCoT translates NL to symbolic format, derives step-by-step plans with symbolic logic rules,\n      and verifies translation+reasoning. Evaluated on FOLIO. Single-path symbolic verification vs SICA's multi-path\n      constraint aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2405.18357'\n  fu2023complexity:\n    title: Complexity-Based Prompting for Multi-Step Reasoning\n    authors:\n    - Fu et al.\n    year: 2023\n    venue: ICLR 2023\n    bibtex_key: fu2023complexity\n    category: self_consistency_and_variants\n    role: foundation\n    relevance: Selects CoT exemplars with more reasoning steps (higher complexity), improving SC aggregation.\n      Shows that reasoning chain quality matters for SC — complementary to SICA's constraint-quality weighting.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2210.00720'\n  he2021deberta:\n    title: 'DeBERTa: Decoding-enhanced BERT with Disentangled Attention'\n    authors:\n    - He et al.\n    year: 2021\n    venue: ICLR 2021\n    bibtex_key: he2021deberta\n    category: nli_verification\n    role: foundation\n    relevance: Introduces disentangled attention and enhanced mask decoder. DeBERTa-large-MNLI is our primary\n      NLI cross-encoder for inter-trace entailment scoring in the SICA pipeline.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2006.03654'\n  liu2019roberta:\n    title: 'RoBERTa: A Robustly Optimized BERT Pretraining Approach'\n    authors:\n    - Liu et al.\n    year: 2019\n    venue: arXiv 2019\n    bibtex_key: liu2019roberta\n    category: nli_verification\n    role: foundation\n    relevance: Robustly optimized BERT pretraining. RoBERTa-large-MNLI serves as alternative NLI backbone\n      for entailment-based verification in our ablation experiments.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1907.11692'\n  williams2018mnli:\n    title: A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference\n    authors:\n    - Williams et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: williams2018mnli\n    category: nli_verification\n    role: foundation\n    relevance: Introduces Multi-Genre NLI (MultiNLI) corpus with 433k examples across 10 genres. The training\n      dataset for our DeBERTa/RoBERTa NLI cross-encoders used in SICA's entailment scoring.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1704.05426'\n  thorne2018fever:\n    title: 'FEVER: a Large-scale Dataset for Fact Extraction and VERification'\n    authors:\n    - Thorne et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: thorne2018fever\n    category: nli_verification\n    role: background\n    relevance: Establishes NLI-based fact verification paradigm with 185k claims against Wikipedia. Demonstrates\n      that entailment models can serve as verifiers — foundational for using NLI as reasoning verification.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1803.05355'\n  honovich2022true:\n    title: 'TRUE: Re-evaluating Factual Consistency Evaluation'\n    authors:\n    - Honovich et al.\n    year: 2022\n    venue: NAACL 2022\n    bibtex_key: honovich2022true\n    category: nli_verification\n    role: background\n    relevance: Shows NLI-based metrics achieve strong factual consistency evaluation across tasks. Validates\n      using NLI cross-encoders as general-purpose verification tools — supports our use of NLI for inter-trace\n      consistency checking.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2204.04991'\n  kadavath2022know:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Kadavath et al.\n    year: 2022\n    venue: arXiv 2022\n    bibtex_key: kadavath2022know\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Shows LLMs can predict P(I Know) — probability of answering correctly. Foundation for confidence-based\n      selective prediction. Motivates SICA's constraint-agreement as an alternative confidence signal to model\n      self-evaluation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2207.05221'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Guo et al.\n    year: 2017\n    venue: ICML 2017\n    bibtex_key: guo2017calibration\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Foundational work showing modern deep networks are poorly calibrated. Introduces temperature scaling\n      for post-hoc calibration. Provides theoretical grounding for why raw model confidence is unreliable —\n      motivates constraint-based confidence in SICA.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1706.04599'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Geifman, Yonatan\n    - El-Yaniv, Ran\n    year: 2017\n    venue: NeurIPS 2017\n    bibtex_key: geifman2017selective\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Formalizes selective classification with guaranteed risk control. Establishes the accuracy-coverage\n      tradeoff framework. SICA's constraint-satisfaction ratio can serve as a selection function for selective\n      prediction.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1705.08500'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Ren et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: ren2023selfevaluation\n    category: calibration_selective_prediction\n    role: background\n    relevance: LLM self-evaluation for selective generation via multi-way comparison and point-wise evaluation.\n      Shows self-assessment can improve abstention decisions. Contrast with SICA's external constraint-based\n      confidence rather than self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2312.09300'\n  xiong2024uncertainty:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Xiong et al.\n    year: 2024\n    venue: ICLR 2024\n    bibtex_key: xiong2024uncertainty\n    category: calibration_selective_prediction\n    role: background\n    relevance: Comprehensive evaluation of verbalized confidence elicitation showing overconfidence and limited\n      calibration in LLMs. Directly motivates SICA's approach — using symbolic constraint satisfaction as an\n      external confidence measure rather than relying on LLM self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.13063'"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T10:17:32.781578+00:00_

&lt;tool_use_error>Found 53 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_by: migration
    added_at: '2026-05-20T04:43:12Z'&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T10:17:32.781913+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "old_string": "    relevance: Source of the design effect formula Deff = 1 + (K-1)ρ, from which our Effective-K = K/Deff = K/(1+(K-1)κ) derives.\n      Kish's design effect quantifies how clustering/correlation inflates variance relative to simple random sampling. Must\n      cite when using Eff-K to avoid novelty overclaim — the formula is an established statistical concept applied to a new\n      domain (LLM trace aggregation)\n    verified: true\n    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'",
  "new_string": "    relevance: Source of the design effect formula Deff = 1 + (K-1)ρ, from which our Effective-K = K/Deff = K/(1+(K-1)κ) derives.\n      Kish's design effect quantifies how clustering/correlation inflates variance relative to simple random sampling. Must\n      cite when using Eff-K to avoid novelty overclaim — the formula is an established statistical concept applied to a new\n      domain (LLM trace aggregation)\n    verified: true\n    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'\n  poesia2023logicguide:\n    title: Certified Deductive Reasoning with Language Models\n    authors:\n    - Poesia et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: poesia2023logicguide\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: Introduces LogicGuide, using state-based constraints to guide LLM generation for sound deductive\n      reasoning. Achieves up to +35% accuracy on ProofWriter/PrOntoQA. Complementary to SICA — LogicGuide constrains\n      generation, SICA aggregates post-hoc constraints.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.04031'\n  ye2024satlm:\n    title: 'SatLM: Satisfiability-Aided Language Models Using Declarative Prompting'\n    authors:\n    - Ye et al.\n    year: 2024\n    venue: NeurIPS 2023\n    bibtex_key: ye2024satlm\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: LLM generates declarative SAT specifications, offloads solving to automated theorem prover. Closest\n      to SICA's constraint-solving philosophy but uses single-path declarative prompting rather than multi-path\n      aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2305.09656'\n  xu2024symbcot:\n    title: Faithful Logical Reasoning via Symbolic Chain-of-Thought\n    authors:\n    - Xu et al.\n    year: 2024\n    venue: ACL 2024\n    bibtex_key: xu2024symbcot\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: SymbCoT translates NL to symbolic format, derives step-by-step plans with symbolic logic rules,\n      and verifies translation+reasoning. Evaluated on FOLIO. Single-path symbolic verification vs SICA's multi-path\n      constraint aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2405.18357'\n  fu2023complexity:\n    title: Complexity-Based Prompting for Multi-Step Reasoning\n    authors:\n    - Fu et al.\n    year: 2023\n    venue: ICLR 2023\n    bibtex_key: fu2023complexity\n    category: self_consistency_and_variants\n    role: foundation\n    relevance: Selects CoT exemplars with more reasoning steps (higher complexity), improving SC aggregation.\n      Shows that reasoning chain quality matters for SC — complementary to SICA's constraint-quality weighting.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2210.00720'\n  he2021deberta:\n    title: 'DeBERTa: Decoding-enhanced BERT with Disentangled Attention'\n    authors:\n    - He et al.\n    year: 2021\n    venue: ICLR 2021\n    bibtex_key: he2021deberta\n    category: nli_verification\n    role: foundation\n    relevance: Introduces disentangled attention and enhanced mask decoder. DeBERTa-large-MNLI is our primary\n      NLI cross-encoder for inter-trace entailment scoring in the SICA pipeline.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2006.03654'\n  liu2019roberta:\n    title: 'RoBERTa: A Robustly Optimized BERT Pretraining Approach'\n    authors:\n    - Liu et al.\n    year: 2019\n    venue: arXiv 2019\n    bibtex_key: liu2019roberta\n    category: nli_verification\n    role: foundation\n    relevance: Robustly optimized BERT pretraining. RoBERTa-large-MNLI serves as alternative NLI backbone\n      for entailment-based verification in our ablation experiments.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1907.11692'\n  williams2018mnli:\n    title: A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference\n    authors:\n    - Williams et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: williams2018mnli\n    category: nli_verification\n    role: foundation\n    relevance: Introduces Multi-Genre NLI (MultiNLI) corpus with 433k examples across 10 genres. The training\n      dataset for our DeBERTa/RoBERTa NLI cross-encoders used in SICA's entailment scoring.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1704.05426'\n  thorne2018fever:\n    title: 'FEVER: a Large-scale Dataset for Fact Extraction and VERification'\n    authors:\n    - Thorne et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: thorne2018fever\n    category: nli_verification\n    role: background\n    relevance: Establishes NLI-based fact verification paradigm with 185k claims against Wikipedia. Demonstrates\n      that entailment models can serve as verifiers — foundational for using NLI as reasoning verification.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1803.05355'\n  honovich2022true:\n    title: 'TRUE: Re-evaluating Factual Consistency Evaluation'\n    authors:\n    - Honovich et al.\n    year: 2022\n    venue: NAACL 2022\n    bibtex_key: honovich2022true\n    category: nli_verification\n    role: background\n    relevance: Shows NLI-based metrics achieve strong factual consistency evaluation across tasks. Validates\n      using NLI cross-encoders as general-purpose verification tools — supports our use of NLI for inter-trace\n      consistency checking.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2204.04991'\n  kadavath2022know:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Kadavath et al.\n    year: 2022\n    venue: arXiv 2022\n    bibtex_key: kadavath2022know\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Shows LLMs can predict P(I Know) — probability of answering correctly. Foundation for confidence-based\n      selective prediction. Motivates SICA's constraint-agreement as an alternative confidence signal to model\n      self-evaluation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2207.05221'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Guo et al.\n    year: 2017\n    venue: ICML 2017\n    bibtex_key: guo2017calibration\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Foundational work showing modern deep networks are poorly calibrated. Introduces temperature scaling\n      for post-hoc calibration. Provides theoretical grounding for why raw model confidence is unreliable —\n      motivates constraint-based confidence in SICA.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1706.04599'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Geifman, Yonatan\n    - El-Yaniv, Ran\n    year: 2017\n    venue: NeurIPS 2017\n    bibtex_key: geifman2017selective\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Formalizes selective classification with guaranteed risk control. Establishes the accuracy-coverage\n      tradeoff framework. SICA's constraint-satisfaction ratio can serve as a selection function for selective\n      prediction.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1705.08500'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Ren et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: ren2023selfevaluation\n    category: calibration_selective_prediction\n    role: background\n    relevance: LLM self-evaluation for selective generation via multi-way comparison and point-wise evaluation.\n      Shows self-assessment can improve abstention decisions. Contrast with SICA's external constraint-based\n      confidence rather than self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2312.09300'\n  xiong2024uncertainty:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Xiong et al.\n    year: 2024\n    venue: ICLR 2024\n    bibtex_key: xiong2024uncertainty\n    category: calibration_selective_prediction\n    role: background\n    relevance: Comprehensive evaluation of verbalized confidence elicitation showing overconfidence and limited\n      calibration in LLMs. Directly motivates SICA's approach — using symbolic constraint satisfaction as an\n      external confidence measure rather than relying on LLM self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.13063'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "old_string": "    relevance: Source of the design effect formula Deff = 1 + (K-1)ρ, from which our Effective-K = K/Deff = K/(1+(K-1)κ) derives.\n      Kish's design effect quantifies how clustering/correlation inflates variance relative to simple random sampling. Must\n      cite when using Eff-K to avoid novelty overclaim — the formula is an established statistical concept applied to a new\n      domain (LLM trace aggregation)\n    verified: true\n    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'",
    "new_string": "    relevance: Source of the design effect formula Deff = 1 + (K-1)ρ, from which our Effective-K = K/Deff = K/(1+(K-1)κ) derives.\n      Kish's design effect quantifies how clustering/correlation inflates variance relative to simple random sampling. Must\n      cite when using Eff-K to avoid novelty overclaim — the formula is an established statistical concept applied to a new\n      domain (LLM trace aggregation)\n    verified: true\n    added_by: migration\n    added_at: '2026-05-20T04:43:12Z'\n  poesia2023logicguide:\n    title: Certified Deductive Reasoning with Language Models\n    authors:\n    - Poesia et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: poesia2023logicguide\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: Introduces LogicGuide, using state-based constraints to guide LLM generation for sound deductive\n      reasoning. Achieves up to +35% accuracy on ProofWriter/PrOntoQA. Complementary to SICA — LogicGuide constrains\n      generation, SICA aggregates post-hoc constraints.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.04031'\n  ye2024satlm:\n    title: 'SatLM: Satisfiability-Aided Language Models Using Declarative Prompting'\n    authors:\n    - Ye et al.\n    year: 2024\n    venue: NeurIPS 2023\n    bibtex_key: ye2024satlm\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: LLM generates declarative SAT specifications, offloads solving to automated theorem prover. Closest\n      to SICA's constraint-solving philosophy but uses single-path declarative prompting rather than multi-path\n      aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2305.09656'\n  xu2024symbcot:\n    title: Faithful Logical Reasoning via Symbolic Chain-of-Thought\n    authors:\n    - Xu et al.\n    year: 2024\n    venue: ACL 2024\n    bibtex_key: xu2024symbcot\n    category: symbolic_reasoning_llm\n    role: direct-competitor\n    relevance: SymbCoT translates NL to symbolic format, derives step-by-step plans with symbolic logic rules,\n      and verifies translation+reasoning. Evaluated on FOLIO. Single-path symbolic verification vs SICA's multi-path\n      constraint aggregation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2405.18357'\n  fu2023complexity:\n    title: Complexity-Based Prompting for Multi-Step Reasoning\n    authors:\n    - Fu et al.\n    year: 2023\n    venue: ICLR 2023\n    bibtex_key: fu2023complexity\n    category: self_consistency_and_variants\n    role: foundation\n    relevance: Selects CoT exemplars with more reasoning steps (higher complexity), improving SC aggregation.\n      Shows that reasoning chain quality matters for SC — complementary to SICA's constraint-quality weighting.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2210.00720'\n  he2021deberta:\n    title: 'DeBERTa: Decoding-enhanced BERT with Disentangled Attention'\n    authors:\n    - He et al.\n    year: 2021\n    venue: ICLR 2021\n    bibtex_key: he2021deberta\n    category: nli_verification\n    role: foundation\n    relevance: Introduces disentangled attention and enhanced mask decoder. DeBERTa-large-MNLI is our primary\n      NLI cross-encoder for inter-trace entailment scoring in the SICA pipeline.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2006.03654'\n  liu2019roberta:\n    title: 'RoBERTa: A Robustly Optimized BERT Pretraining Approach'\n    authors:\n    - Liu et al.\n    year: 2019\n    venue: arXiv 2019\n    bibtex_key: liu2019roberta\n    category: nli_verification\n    role: foundation\n    relevance: Robustly optimized BERT pretraining. RoBERTa-large-MNLI serves as alternative NLI backbone\n      for entailment-based verification in our ablation experiments.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1907.11692'\n  williams2018mnli:\n    title: A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference\n    authors:\n    - Williams et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: williams2018mnli\n    category: nli_verification\n    role: foundation\n    relevance: Introduces Multi-Genre NLI (MultiNLI) corpus with 433k examples across 10 genres. The training\n      dataset for our DeBERTa/RoBERTa NLI cross-encoders used in SICA's entailment scoring.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1704.05426'\n  thorne2018fever:\n    title: 'FEVER: a Large-scale Dataset for Fact Extraction and VERification'\n    authors:\n    - Thorne et al.\n    year: 2018\n    venue: NAACL 2018\n    bibtex_key: thorne2018fever\n    category: nli_verification\n    role: background\n    relevance: Establishes NLI-based fact verification paradigm with 185k claims against Wikipedia. Demonstrates\n      that entailment models can serve as verifiers — foundational for using NLI as reasoning verification.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1803.05355'\n  honovich2022true:\n    title: 'TRUE: Re-evaluating Factual Consistency Evaluation'\n    authors:\n    - Honovich et al.\n    year: 2022\n    venue: NAACL 2022\n    bibtex_key: honovich2022true\n    category: nli_verification\n    role: background\n    relevance: Shows NLI-based metrics achieve strong factual consistency evaluation across tasks. Validates\n      using NLI cross-encoders as general-purpose verification tools — supports our use of NLI for inter-trace\n      consistency checking.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2204.04991'\n  kadavath2022know:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Kadavath et al.\n    year: 2022\n    venue: arXiv 2022\n    bibtex_key: kadavath2022know\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Shows LLMs can predict P(I Know) — probability of answering correctly. Foundation for confidence-based\n      selective prediction. Motivates SICA's constraint-agreement as an alternative confidence signal to model\n      self-evaluation.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2207.05221'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Guo et al.\n    year: 2017\n    venue: ICML 2017\n    bibtex_key: guo2017calibration\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Foundational work showing modern deep networks are poorly calibrated. Introduces temperature scaling\n      for post-hoc calibration. Provides theoretical grounding for why raw model confidence is unreliable —\n      motivates constraint-based confidence in SICA.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1706.04599'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Geifman, Yonatan\n    - El-Yaniv, Ran\n    year: 2017\n    venue: NeurIPS 2017\n    bibtex_key: geifman2017selective\n    category: calibration_selective_prediction\n    role: foundation\n    relevance: Formalizes selective classification with guaranteed risk control. Establishes the accuracy-coverage\n      tradeoff framework. SICA's constraint-satisfaction ratio can serve as a selection function for selective\n      prediction.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '1705.08500'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Ren et al.\n    year: 2023\n    venue: arXiv 2023\n    bibtex_key: ren2023selfevaluation\n    category: calibration_selective_prediction\n    role: background\n    relevance: LLM self-evaluation for selective generation via multi-way comparison and point-wise evaluation.\n      Shows self-assessment can improve abstention decisions. Contrast with SICA's external constraint-based\n      confidence rather than self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2312.09300'\n  xiong2024uncertainty:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Xiong et al.\n    year: 2024\n    venue: ICLR 2024\n    bibtex_key: xiong2024uncertainty\n    category: calibration_selective_prediction\n    role: background\n    relevance: Comprehensive evaluation of verbalized confidence elicitation showing overconfidence and limited\n      calibration in LLMs. Directly motivates SICA's approach — using symbolic constraint satisfaction as an\n      external confidence measure rather than relying on LLM self-reported confidence.\n    verified: false\n    added_by: worker\n    added_at: '2026-05-20T12:00:00Z'\n    arxiv_id: '2306.13063'"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T10:17:32.782718+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T10:17:32.783010+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
  "old_string": "  total_papers: 53",
  "new_string": "  total_papers: 67"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml",
    "old_string": "  total_papers: 53",
    "new_string": "  total_papers: 67"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T10:17:32.783390+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T10:17:32.783646+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml') as f:\n    data = yaml.safe_load(f)\npapers = data['papers']\nprint(f'Total papers in file: {len(papers)}')\nnew_keys = ['poesia2023logicguide','ye2024satlm','xu2024symbcot','fu2023complexity','he2021deberta','liu2019roberta','williams2018mnli','thorne2018fever','honovich2022true','kadavath2022know','guo2017calibration','geifman2017selective','ren2023selfevaluation','xiong2024uncertainty']\nfor k in new_keys:\n    p = papers[k]\n    print(f'  {k}: {p[\\\"category\\\"]} / {p[\\\"venue\\\"]}')\n\"\n",
  "description": "Validate YAML and check new entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/literature_map.yaml') as f:\n    data = yaml.safe_load(f)\npapers = data['papers']\nprint(f'Total papers in file: {len(papers)}')\nnew_keys = ['poesia2023logicguide','ye2024satlm','xu2024symbcot','fu2023complexity','he2021deberta','liu2019roberta','williams2018mnli','thorne2018fever','honovich2022true','kadavath2022know','guo2017calibration','geifman2017selective','ren2023selfevaluation','xiong2024uncertainty']\nfor k in new_keys:\n    p = papers[k]\n    print(f'  {k}: {p[\\\"category\\\"]} / {p[\\\"venue\\\"]}')\n\"\n",
    "description": "Validate YAML and check new entries"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T10:17:32.783892+00:00_

Total papers in file: 67
  poesia2023logicguide: symbolic_reasoning_llm / arXiv 2023
  ye2024satlm: symbolic_reasoning_llm / NeurIPS 2023
  xu2024symbcot: symbolic_reasoning_llm / ACL 2024
  fu2023complexity: self_consistency_and_variants / ICLR 2023
  he2021deberta: nli_verification / ICLR 2021
  liu2019roberta: nli_verification / arXiv 2019
  williams2018mnli: nli_verification / NAACL 2018
  thorne2018fever: nli_verification / NAACL 2018
  honovich2022true: nli_verification / NAACL 2022
  kadavath2022know: calibration_selective_prediction / arXiv 2022
  guo2017calibration: calibration_selective_prediction / ICML 2017
  geifman2017selective: calibration_selective_prediction / NeurIPS 2017
  ren2023selfevaluation: calibration_selective_prediction / arXiv 2023
  xiong2024uncertainty: calibration_selective_prediction / ICLR 2024

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_research_20260520T101251",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-20T10:17:32.784174+00:00_

YAML 验证通过，67 篇论文全部正确解析。

**新增 14 篇论文汇总：**

| 方向 | 新增 | 论文 |
|------|------|------|
| 1. Symbolic verification | +3 | LogicGuide (Poesia'23), SatLM (Ye, NeurIPS'23), SymbCoT (Xu, ACL'24) |
| 2. SC & aggregation | +1 | Complexity-Based Prompting (Fu, ICLR'23) |
| 3. NLI as verifier | +5 | DeBERTa (He, ICLR'21), RoBERTa (Liu'19), MultiNLI (Williams, NAACL'18), FEVER (Thorne, NAACL'18), TRUE (Honovich, NAACL'22) |
| 4. Calibration & selective prediction | +5 | Kadavath'22, Guo (ICML'17), Geifman (NeurIPS'17), Ren'23, Xiong (ICLR'24) |

新增 2 个 category：`nli_verification`、`calibration_selective_prediction`。所有论文 `verified: false`，待后续统一核实。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_research_20260520T101251"
}
```

</details>

---
