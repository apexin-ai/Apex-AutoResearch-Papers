# research citation verification

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 29
- **Original source:** `logs/chats/worker_research_citation_verification_20260520T173215.jsonl`
- **Structured JSON:** [`482869cbc0c1a4d4e597.json`](../../sessions/48/482869cbc0c1a4d4e597.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

59 recorded events

### Tool call

_source line 1 · 2026-05-20T17:36:39.397605+00:00_

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
  "session": "worker_research_citation_verification_20260520T173215",
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

_source line 2 · 2026-05-20T17:36:39.397960+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T17:36:39.398122+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T17:36:39.398319+00:00_

artifacts/dream_reports/dream_20260520T112859/median/references.bib
artifacts/dream_reports/dream_20260520T112859/worst/references.bib
artifacts/dream_reports/dream_20260520T152228/median/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T17:36:39.398491+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T17:36:39.398625+00:00_

artifacts/dream_reports/dream_20260520T112859/best/paper.tex
artifacts/dream_reports/dream_20260520T112859/median/paper.tex
artifacts/dream_reports/dream_20260520T112859/worst/paper.tex
artifacts/dream_reports/dream_20260520T152228/best/paper.tex
artifacts/dream_reports/dream_20260520T152228/median/paper.tex
artifacts/dream_reports/dream_20260520T152228/worst/paper.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T17:36:39.398761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T17:36:39.398914+00:00_

1	@inproceedings{berry2003ambiguity,
2	  title={From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity},
3	  author={Berry, Daniel M. and Kamsties, Erik},
4	  year={2003},
5	  url={https://cs.uwaterloo.ca/~dberry/FTP_SITE/tech.reports/ambiguity.handbook.pdf}
6	}
7	
8	@inproceedings{li2024ambiguity,
9	  title={Linguistically Grounded Ambiguity in Natural Language Processing},
10	  author={Li, Jian and others},
11	  booktitle={Proceedings of ACL},
12	  year={2024}
13	}
14	
15	@inproceedings{massey2014evaluating,
16	  title={Evaluating Existing Security and Privacy Requirements for Legal Compliance},
17	  author={Massey, Aaron K. and Rutledge, Robert L. and others},
18	  booktitle={Requirements Engineering Journal},
19	  year={2014}
20	}
21	
22	@inproceedings{chantree2006identifying,
23	  title={Identifying Nocuous Ambiguities in Natural Language Requirements},
24	  author={Chantree, Francis and Nuseibeh, Bashar and de Roeck, Anne and Willis, Alistair},
25	  booktitle={Proceedings of RE},
26	  year={2006}
27	}
28	
29	@article{wasow2005intuitions,
30	  title={Intuitions and Models of Vagueness and Ambiguity},
31	  author={Wasow, Thomas and Perfors, Amy and Beaver, David},
32	  journal={Handbook of Experimental Semantics and Pragmatics},
33	  year={2005}
34	}
35	
36	@article{kennedy2007vagueness,
37	  title={Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives},
38	  author={Kennedy, Christopher},
39	  journal={Linguistics and Philosophy},
40	  volume={30},
41	  pages={1--45},
42	  year={2007}
43	}
44	
45	@inproceedings{ruan2024toolemu,
46	  title={Identifying the Risks of {LM} Agents with an {LM}-Emulated Sandbox},
47	  author={Ruan, Yangjun and others},
48	  booktitle={Proceedings of ICLR},
49	  year={2024}
50	}
51	
52	@inproceedings{zhan2024injecagent,
53	  title={InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated {LLM} Agents},
54	  author={Zhan, Qiusi and others},
55	  booktitle={Findings of
…[truncated 1332 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T17:36:39.399080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T17:36:39.399285+00:00_

1	@inproceedings{berry2003ambiguity,
2	  title={From contract drafting to software specification: Linguistic sources of ambiguity},
3	  author={Berry, Daniel M and Kamsties, Erik},
4	  year={2003},
5	  booktitle={Technical Report}
6	}
7	
8	@inproceedings{li2024drip,
9	  title={{DRIP-R}: Divergent Readings of Imprecise Policies in Retail},
10	  author={Li, Xiang and others},
11	  year={2024},
12	  booktitle={Proceedings of EMNLP}
13	}
14	
15	@inproceedings{massey2014,
16	  title={Evaluating existing security and privacy requirements for legal compliance},
17	  author={Massey, Aaron K and Rutledge, Richard L and others},
18	  year={2014},
19	  booktitle={Requirements Engineering}
20	}
21	
22	@inproceedings{ruan2024toolemu,
23	  title={{ToolEmu}: Identifying risks of LM agents with an LM-emulated sandbox},
24	  author={Ruan, Yangjun and others},
25	  year={2024},
26	  booktitle={Proceedings of ICLR}
27	}
28	
29	@inproceedings{liu2024injecagent,
30	  title={{InjecAgent}: Benchmarking indirect prompt injections in tool-integrated LLM agents},
31	  author={Liu, Qiusi and others},
32	  year={2024},
33	  booktitle={Findings of ACL}
34	}
35	
36	@inproceedings{zhang2024agentpex,
37	  title={{AgentPex}: Policy enforcement examination for LLM-based agents},
38	  author={Zhang, Yifei and others},
39	  year={2024},
40	  booktitle={Proceedings of NeurIPS}
41	}
42	
43	@inproceedings{tau2bench2024,
44	  title={$\tau^2$-bench: A benchmark for tool-augmented agent policies},
45	  author={Anonymous},
46	  year={2024},
47	  booktitle={arXiv preprint}
48	}
49	
50	@inproceedings{yuan2024rjudge,
51	  title={{R-Judge}: Benchmarking safety risk awareness for LLM agents},
52	  author={Yuan, Tongxin and others},
53	  year={2024},
54	  booktitle={Proceedings of EMNLP}
55	}
56	
57	@inproceedings{sclar2024quantifying,
58	  title={Quantifying language models' sensitivity to spurious features in prompt design},
59	  author={Sclar, Melanie and others},
60	  year={2024},
61	  booktitle={Proceedings o
…[truncated 1636 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T17:36:39.399513+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "τ²-bench tau-bench \"Benchmarking Agents\" customer service Yao Shunyu 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "τ²-bench tau-bench \"Benchmarking Agents\" customer service Yao Shunyu 2024"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T17:36:39.399664+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DRIP-R benchmark LLM agents ambiguity policy retail 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DRIP-R benchmark LLM agents ambiguity policy retail 2024"
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T17:36:39.399792+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Toolformer Schick NeurIPS 2023 2024 tool-augmented language models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Toolformer Schick NeurIPS 2023 2024 tool-augmented language models"
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-20T17:36:39.399914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Massey \"requirements engineering\" ambiguity classification policy privacy 2014"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Massey \"requirements engineering\" ambiguity classification policy privacy 2014"
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T17:36:39.400045+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Berry Kamsties \"nocuous ambiguity\" 2003 \"linguistic sources of ambiguity\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Berry Kamsties \"nocuous ambiguity\" 2003 \"linguistic sources of ambiguity\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T17:36:39.400256+00:00_

Web search results for query: "τ²-bench tau-bench "Benchmarking Agents" customer service Yao Shunyu 2024"

Links: [{"title":"τ-bench: Tool-Agent-User Interaction Benchmark","url":"https://www.emergentmind.com/papers/2406.12045"},{"title":"GitHub - sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub","url":"https://github.com/sierra-research/tau-bench"},{"title":"Paper page - τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://huggingface.co/papers/2406.12045"},{"title":"[2406.12045] $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://arxiv.org/abs/2406.12045"},{"title":"[PDF] τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%84-bench:-A-Benchmark-for-Tool-Agent-User-in-Domains-Yao-Shinn/70aa016c1f68fd5c0261f26ad20017b8307650af"},{"title":"{$\\tau$}-bench: A Benchmark for \\underline{T}ool-\\ ...","url":"https://openreview.net/forum?id=roNSXZpUDN"},{"title":"GitHub - sierra-research/tau2-bench: τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains · GitHub","url":"https://github.com/sierra-research/tau2-bench"},{"title":"𝜏-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains","url":"https://arxiv.org/html/2603.13686v1"},{"title":"τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://arxiv.org/pdf/2406.12045"},{"title":"(PDF) \\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://www.researchgate.net/publication/381517740_tau-bench_A_Benchmark_for_Tool-Agent-User_Interaction_in_Real-World_Domains"}]

Based on the search results, I found relevant information about your query:

## τ-bench and τ²-bench

τ-bench is a benchmark with two domains (retail and airline) emulating dynamic conversations between a user (simulated by language models) and a customer service agent provided 
…[truncated 992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T17:36:39.400467+00:00_

Web search results for query: "Toolformer Schick NeurIPS 2023 2024 tool-augmented language models"

Links: [{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract-Conference.html"},{"title":"NeurIPS Poster Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://neurips.cc/virtual/2023/poster/71288"},{"title":"[PDF] Toolformer: Language Models Can Teach Themselves to Use Tools | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Toolformer:-Language-Models-Can-Teach-Themselves-to-Schick-Dwivedi-Yu/53d128ea815bcc0526856eb5a9c42cc977cb36a7"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://arxiv.org/pdf/2302.04761"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools Timo Schick","url":"https://openreview.net/pdf?id=Yacmpz84TH"},{"title":"NeurIPS 2023 Toolformer: Language Models Can Teach Themselves to Use Tools Oral","url":"https://neurips.cc/virtual/2023/oral/73843"},{"title":"Toolformer: Language Models Can Teach Themselves to Use Tools | Research - AI at Meta","url":"https://ai.meta.com/research/publications/toolformer-language-models-can-teach-themselves-to-use-tools/"},{"title":"[2302.04761] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://arxiv.org/abs/2302.04761"},{"title":"[Quick Review] Toolformer: Language Models Can Teach Themselves to Use Tools","url":"https://liner.com/review/toolformer-language-models-can-teach-themselves-to-use-tools"}]

I've found comprehensive information about Toolformer. Here are the key findings:

## Overview

Toolformer is a model trained to decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction. This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for
…[truncated 1136 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T17:36:39.400657+00:00_

Web search results for query: "Massey "requirements engineering" ambiguity classification policy privacy 2014"

Links: [{"title":"Ambiguity in Privacy Policies and the Impact of Regulation","url":"https://epe.brightspotcdn.com/a7/fc/0e46b060d5475a2a3b8c9ee8846b/65-jls-ambiguity-in-privacy-policies.pdf"},{"title":"Accepted To: 2016 IEEE International Conference on Requirements Engineering","url":"https://www.cs.cmu.edu/~breaux/publications/jbhatia-re16.pdf"},{"title":"Ambiguity in Privacy Policies and the Impact of Regulation","url":"https://oag.ca.gov/sites/all/files/agweb/pdfs/privacy/reidenberg-ambiguity.pdf"},{"title":"[PDF] Identifying and classifying ambiguity for regulatory requirements | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Identifying-and-classifying-ambiguity-for-Massey-Rutledge/ae7de2388daabab5cc00e46a1f89871365b6d550"},{"title":"Modeling Regulatory Ambiguities for Requirements Analysis | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-319-69904-2_19"},{"title":"dblp: Aaron K. Massey","url":"https://dblp.org/pid/30/6548.html"},{"title":"Ambiguity and Generality in Natural Language Privacy Policies","url":"https://par.nsf.gov/servlets/purl/10317899"},{"title":"Identifying and Classifying Ambiguity for Regulatory Requirements","url":"https://www.cc.gatech.edu/~aianton/assets/2014_re14_ambiguity.pdf"},{"title":"Identifying and classifying ambiguity for regulatory requirements | Request PDF","url":"https://www.researchgate.net/publication/288485563_Identifying_and_classifying_ambiguity_for_regulatory_requirements"}]

Based on the search results, I found information about the work by Massey and colleagues on requirements engineering and ambiguity classification related to regulatory requirements and privacy.

Massey, A.K., Rutledge, R.L., Antón, A.I., and P.P. Swire presented a paper titled "Identifying and Classifying Ambiguity for Regulatory Requirements" at the IEEE 22nd International Requirements Engine
…[truncated 601 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T17:36:39.400826+00:00_

Web search results for query: "DRIP-R benchmark LLM agents ambiguity policy retail 2024"

Links: [{"title":"[2605.07699v1] DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain","url":"https://arxiv.org/abs/2605.07699v1"},{"title":"[2605.07699] DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain","url":"https://arxiv.org/abs/2605.07699"},{"title":"DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain","url":"https://arxiv.org/html/2605.07699v1"},{"title":"RetailBench: Evaluating Long-Horizon Autonomous Decision-Making and Strategy Stability of LLM Agents in Realistic Retail Environments","url":"https://arxiv.org/pdf/2603.16453"},{"title":"CAR-bench: Evaluating the Consistency and Limit-Awareness of LLM Agents under Real-World Uncertainty","url":"https://arxiv.org/html/2601.22027"},{"title":"Ambig-DS: A Benchmark for Task-Framing Ambiguity in Data-Science Agents","url":"https://arxiv.org/html/2605.09698"}]

Based on the search results, here's what I found about DRIP-R:

DRIP-R is a benchmark that systematically exploits real-world retail policy ambiguities to construct scenarios in which no single correct resolution exists. 

LLM-based agents are increasingly deployed for routine but consequential tasks in real-world domains, where their behavior is governed by inherently ambiguous domain policies that admit multiple valid interpretations. Despite the prevalence of such ambiguities in practice, existing agent benchmarks largely assume unambiguous, well-specified policies, leaving a critical evaluation gap.

DRIP-R comprises a curated set of policy-ambiguous return scenarios paired with realistic customer personas, a full-duplex conversational simulation with tool-calling capabilities and a multi-judge evaluation framework. 

Experiments show that frontier models fundamentally disagree on identical polic
…[truncated 356 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T17:36:39.401003+00:00_

Web search results for query: "Berry Kamsties "nocuous ambiguity" 2003 "linguistic sources of ambiguity""

Links: [{"title":"Ambiguity Detection: Towards a Tool Explaining Ambiguity Sources | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-642-14192-8_20"},{"title":"An NLP approach for cross-domain ambiguity detection in requirements engineering | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-019-00261-7"},{"title":"Analysing anaphoric ambiguity in natural language requirements | Requirements Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00766-011-0119-y"},{"title":"(PDF) Sources of Ambiguity in Language","url":"https://www.researchgate.net/publication/323750508_Sources_of_Ambiguity_in_Language"},{"title":"Ambiguity and tacit knowledge in requirements elicitation interviews | Requirements Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00766-016-0249-3"},{"title":"Automatic Identification of Nocuous Ambiguity | Research on Language and Computation | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11168-008-9058-2"},{"title":"(PDF) From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity (2003) | Daniel M. Berry | 240 Citations","url":"https://scispace.com/papers/from-contract-drafting-to-software-specification-linguistic-z11rvqj117"},{"title":"[PDF] From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/From-Contract-Drafting-to-Software-Specification:-Berry-Kamsties/d9917b27dec5b1a921a410921da59199436a6e2c"},{"title":"Ambiguity: Some Bibliographical Notes","url":"https://old.panlex.org/pubs/etc/ambib.html"}]

Based on the search results, I found information about Berry, Kamsties, and the 2003 work on linguistic sources of ambiguity:

Berry, D.M., Kamsties, E
…[truncated 1057 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T17:36:39.401238+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PhantomPolicy \"probing implicit policy violations\" LLM agents Wang 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PhantomPolicy \"probing implicit policy violations\" LLM agents Wang 2024"
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-20T17:36:39.401395+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentPex \"policy enforcement examination\" LLM agents Zhang 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentPex \"policy enforcement examination\" LLM agents Zhang 2024"
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T17:36:39.401530+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wasow Perfors Beaver \"ambiguity avoidance\" 2005 Stanford"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wasow Perfors Beaver \"ambiguity avoidance\" 2005 Stanford"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-20T17:36:39.401656+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kennedy Christopher \"vagueness and grammar\" \"relative and absolute gradable adjectives\" Linguistics Philosophy 2007"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kennedy Christopher \"vagueness and grammar\" \"relative and absolute gradable adjectives\" Linguistics Philosophy 2007"
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T17:36:39.401777+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ferreira Bailey Ferraro \"good-enough representations\" language comprehension 2002"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ferreira Bailey Ferraro \"good-enough representations\" language comprehension 2002"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T17:36:39.401921+00:00_

Web search results for query: "PhantomPolicy "probing implicit policy violations" LLM agents Wang 2024"

Links: [{"title":"Policy-Invisible Violations in LLM-Based Agents","url":"https://arxiv.org/html/2604.12177v1"},{"title":"[2604.12177] Policy-Invisible Violations in LLM-Based Agents","url":"https://arxiv.org/abs/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents Jie Wu∗ Atlassian Ming Gong","url":"https://arxiv.org/pdf/2604.12177"},{"title":"Training-Free Policy Violation Detection via Activation-Space Whitening in LLMs","url":"https://arxiv.org/pdf/2512.03994"},{"title":"Measuring the Propensity for Misaligned Behaviour in LLM ...","url":"https://arxiv.org/pdf/2506.04018"}]

I found relevant results for PhantomPolicy. Here's what the search revealed:

PhantomPolicy addresses a failure mode in LLM-based agents where they can execute actions that are syntactically valid, user-sanctioned, and semantically appropriate, yet still violate organizational policy because the facts needed for correct policy judgment are hidden at decision time—called "policy-invisible violations."

PhantomPolicy is a benchmark spanning eight violation categories with balanced violation and safe-control cases, in which all tool responses contain clean business data without policy metadata.

PhantomPolicy is deliberately designed as a diagnostic unit-test suite, not a large-scale corpus for statistical generalization, where each case isolates a specific policy-invisible failure mode and probes a well-defined logical boundary.

The research manually reviewed all 600 model traces produced by five frontier models and evaluated them using human-reviewed trace labels.

The research paper was published in April 2026 and appears to be available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T17:36:39.402092+00:00_

Web search results for query: "Wasow Perfors Beaver "ambiguity avoidance" 2005 Stanford"

Links: [{"title":"Ambiguity Avoidance is Overrated✝ Thomas Wasow Stanford University","url":"https://web.stanford.edu/~wasow/Ambiguity"},{"title":"Managing Ambiguity in Reference Generation: The Role of Surface Structure - Khan - 2012 - Topics in Cognitive Science - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/full/10.1111/j.1756-8765.2011.01167.x"},{"title":"Ambiguity Avoidance is Overrated✝","url":"https://web.stanford.edu/~wasow/Ambiguity.pdf"},{"title":"Ambiguity - Cognitive Classics","url":"https://cognitiveclassics.blogs.sas.ac.uk/hums-list/ambiguity/"},{"title":"Tom Wasow's Home Page","url":"https://web.stanford.edu/~wasow/"},{"title":"[PDF] The puzzle of ambiguity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-puzzle-of-ambiguity-Wasow-Perfors/a86da753a89ceef24e505867b2b4d1ef95655b6b"},{"title":"The Puzzle of Ambiguity† Thomas Wasow, Amy Perfors, and David Beaver","url":"https://web.stanford.edu/~wasow/Lapointe.pdf"},{"title":"The puzzle of ambiguity | Andrew Perfors","url":"http://perfors.net/publication/wasowetal05/"},{"title":"The puzzle of ambiguity : Find an Expert : The University of Melbourne","url":"https://findanexpert.unimelb.edu.au/scholarlywork/1234731-the-puzzle-of-ambiguity"},{"title":"(PDF) The Puzzle of Ambiguity","url":"https://www.researchgate.net/publication/2841280_The_Puzzle_of_Ambiguity"}]

I found the paper you're looking for! Here are the results:

The paper is "The Puzzle of Ambiguity" by Wasow, Thomas, Amy Perfors, and David Beaver (2005), published in C. O. Orgun and P. Sells (eds) Morphology and the Web of Grammar pp.265-282 by CSLI Publications at Stanford.

The paper argues for the importance of ambiguity as a common characteristic of natural language, distinguishes between ambiguity and vagueness, identifies distinct types of ambiguity, and suggests that the fact that language has not evolved to re
…[truncated 293 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T17:36:39.402315+00:00_

Web search results for query: "AgentPex "policy enforcement examination" LLM agents Zhang 2024"

Links: [{"title":"\\tool: Proactive Runtime Enforcement of LLM Agent Safety via Probabilistic Model Checking","url":"https://arxiv.org/html/2508.00500v1"},{"title":"Towards Enforcing Company Policy Adherence in Agentic Workflows","url":"https://arxiv.org/html/2507.16459v1"},{"title":"Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents","url":"https://arxiv.org/pdf/2509.23994"},{"title":"\\tool: Customizable Runtime Enforcement for Safe and Reliable LLM Agents","url":"https://arxiv.org/html/2503.18666v1"},{"title":"AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents","url":"https://cposkitt.github.io/files/publications/agentspec_llm_enforcement_icse26.pdf"},{"title":"[Literature Review] AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents","url":"https://www.themoonlight.io/en/review/agentspec-customizable-runtime-enforcement-for-safe-and-reliable-llm-agents"}]

Based on the search results, I found information related to your query, though the results don't appear to contain a paper specifically titled "AgentPex" with "policy enforcement examination" by Zhang in 2024. However, the search did return several highly relevant papers on policy enforcement for LLM agents:

The most relevant result appears to be **AgentSpec: Customizable Runtime Enforcement for Safe and Reliable LLM Agents**, authored by Haoyu Wang, Christopher M. Poskitt, and Jun Sun from Singapore Management University. This paper addresses similar concerns about LLM agent safety.

The search also returned other related 2024 papers on policy enforcement and safety:
- "TrustAgent: Towards Safe and Trustworthy LLM-based Agents" by Wenyue Hua, Xianjun Yang, Mingyu Jin, Zelong Li, Wei Cheng, Ruixiang Tang, and Yongfeng Zhang (2024)
- "Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents" with policy enforcement tested o
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T17:36:39.402494+00:00_

Web search results for query: "Kennedy Christopher "vagueness and grammar" "relative and absolute gradable adjectives" Linguistics Philosophy 2007"

Links: [{"title":"the semantics of relative and absolute gradable adjectives","url":"https://semantics.uchicago.edu/kennedy/docs/vg-epub.pdf"},{"title":"Towards a Grammar of Vagueness∗ Christopher Kennedy Northwestern University","url":"https://amor.cms.hu-berlin.de/~h2816i3x/Lehre/2004_HS_Graduierung/Kennedy_2004_Vaguness.pdf"},{"title":"Christopher Kennedy, Vagueness and grammar: The semantics of relative and absolute gradable adjectives - PhilPapers","url":"https://philpapers.org/rec/KENVAG"},{"title":"The Semantics of Relative and Absolute Gradable Predicates","url":"https://semanticsarchive.net/Archive/zFkZGUzZ/.vaguenessandgrammar.pdf"},{"title":"[PDF] Vagueness and grammar: the semantics of relative and absolute gradable adjectives | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Vagueness-and-Grammar-:-The-Semantics-of-Relative-Kennedy/142d8f3a645d8866831a2f7c935cb632e6878cdc"},{"title":"(PDF) Vagueness and grammar: The semantics of relative and absolute gradable adjectives","url":"https://www.researchgate.net/publication/225837256_Vagueness_and_grammar_The_semantics_of_relative_and_absolute_gradable_adjectives"},{"title":"Vagueness and grammar: the semantics of relative and absolute gradable adjectives | Linguistics and Philosophy | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10988-006-9008-0"}]

I found the work you're looking for! This paper by Christopher Kennedy investigates how linguistic expressions influence vagueness, focusing on the positive form of gradable adjectives. It develops a semantic analysis of relative gradable adjectives and introduces absolute gradable adjectives—adjectives that are gradable but have positive forms relating objects to maximal or minimal degrees without vagueness.

Kennedy argues that the truth conditional difference between relat
…[truncated 460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T17:36:39.402677+00:00_

Web search results for query: "Ferreira Bailey Ferraro "good-enough representations" language comprehension 2002"

Links: [{"title":"\"Good-enough representations in language comprehension\" by F. Ferreira, Karl Bailey et al.","url":"https://digitalcommons.andrews.edu/behavioral-pubs/43/"},{"title":"Ferreira, F., Bailey, K.G. and Ferraro, V. (2002) Good-Enough Representations in Language Comprehension. Current Directions in Psychological Science, 11, 11-15. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2154694"},{"title":"Good-enough representations in language comprehension - Andrews University Research Portal","url":"https://andrews.elsevierpure.com/en/publications/good-enough-representations-in-language-comprehension/"},{"title":"Good-Enough Representations in Language Comprehension","url":"https://ferreiralab.faculty.ucdavis.edu/wp-content/uploads/sites/222/2015/05/Ferreira-et-al.-2002_GoodEnoughRepresentations_Current-Directions-in-Psych-Sci.pdf"},{"title":"[PDF] Good-Enough Representations in Language Comprehension | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Good-Enough-Representations-in-Language-Ferreira-Bailey/411da58de5ad35da54d38553c1741b5905a867ab"},{"title":"The 'Good Enough' Approach to Language Comprehension","url":"https://ferreiralab.faculty.ucdavis.edu/wp-content/uploads/sites/222/2015/05/Ferreira-Patson-2007_GoodEnoughApproach_Lang-Ling-Compass.pdf"},{"title":"The ‘Good Enough’ Approach to Language Comprehension - Ferreira - 2007 - Language and Linguistics Compass - Wiley Online Library","url":"https://compass.onlinelibrary.wiley.com/doi/abs/10.1111/j.1749-818X.2007.00007.x"},{"title":"Good-Enough Representations in Language Comprehension - Fernanda Ferreira, Karl G.D. Bailey, Vittoria Ferraro, 2002","url":"https://journals.sagepub.com/doi/10.1111/1467-8721.00158"},{"title":"Good Enough Representations in Language Comprehension | Request PDF","url":"https://w
…[truncated 871 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T17:36:39.402884+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.07699 DRIP-R authors Amazon Science retail policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.07699 DRIP-R authors Amazon Science retail policy"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-20T17:36:39.403019+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"PhantomPolicy\" LLM agent policy violation benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"PhantomPolicy\" LLM agent policy violation benchmark 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T17:36:39.403143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"AgentPex\" agent policy benchmark evaluation 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"AgentPex\" agent policy benchmark evaluation 2024"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-20T17:36:39.403321+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"PolicyBank\" agent policy benchmark dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"PolicyBank\" agent policy benchmark dataset"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T17:36:39.403483+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "tau-bench tau2-bench \"Shunyu Yao\" NeurIPS 2024 sierra-research arXiv 2406.12045"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "tau-bench tau2-bench \"Shunyu Yao\" NeurIPS 2024 sierra-research arXiv 2406.12045"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T17:36:39.403635+00:00_

Web search results for query: "arXiv 2605.07699 DRIP-R authors Amazon Science retail policy"

Links: [{"title":"[2605.07699v1] DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain","url":"https://arxiv.org/abs/2605.07699v1"},{"title":"[2605.07699] DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain","url":"https://arxiv.org/abs/2605.07699"},{"title":"DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain","url":"https://arxiv.org/html/2605.07699"},{"title":"DRIPS: Domain Randomisation for Image-based Perivascular spaces Segmentation","url":"https://www.medrxiv.org/content/10.1101/2025.10.22.25337423.full.pdf"},{"title":"Dynamic demand transfer estimation for online retailing using machine learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11188934"}]

Based on the search results, here's the information about arXiv paper 2605.07699:

The paper titled "DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain" was submitted on May 8, 2026, with authors Hsuvas Borkakoty, Sebastian Pohl, Cheng Wang, Bei Chen, and Yufang Hou.

Hsuvas Borkakoty, Sebastian Pohl, and Yufang Hou are affiliated with Interdisciplinary Transformation University Austria, while Cheng Wang and Bei Chen are affiliated with Amazon Berlin.

The paper introduces DRIP-R, a benchmark that systematically exploits real-world retail policy ambiguities to construct scenarios in which no single correct resolution exists.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-20T17:36:39.403806+00:00_

Web search results for query: ""PolicyBank" agent policy benchmark dataset"

Links: [{"title":"PolicyBank: Evolving Policy Understanding for LLM Agents","url":"https://arxiv.org/html/2604.15505"},{"title":"[2604.15505] PolicyBank: Evolving Policy Understanding for LLM Agents","url":"https://arxiv.org/abs/2604.15505"},{"title":"Analyzing and Internalizing Complex Policy Documents for LLM Agents","url":"https://arxiv.org/pdf/2510.11588"},{"title":"Policy Benchmarking for Public Policy Offices","url":"https://datacalculus.com/en/blog/public-policy-offices/policy-development-manager/policy-benchmarking-for-public-policy-offices"},{"title":"PolicySimEval: A Benchmark for Evaluating Policy Outcomes through Agent-Based Simulation","url":"https://arxiv.org/html/2502.07853v1"},{"title":"TAU-bench extension: benchmarking policy-aware agents in realistic settings","url":"https://toloka.ai/blog/tau-bench-extension-benchmarking-policy-aware-agents-in-realistic-settings/"},{"title":"Beyond IVR: Benchmarking Customer Support LLM Agents for Business-Adherence","url":"https://arxiv.org/pdf/2601.00596"}]

Based on the search results, here's what I found about PolicyBank:

PolicyBank is a memory mechanism that maintains structured, tool-level policy insights and iteratively refines them—unlike existing memory mechanisms that treat the policy as immutable ground truth, reinforcing "compliant but wrong" behaviors.

**Key Aspects:**

PolicyBank addresses the challenge that LLM agents operating under organizational policies must comply with authorization constraints typically specified in natural language, yet such specifications inevitably contain ambiguities and logical or semantic gaps that cause the agent's behavior to systematically diverge from the true requirements.

The approach lets an agent evolve its policy understanding through interaction and corrective feedback from pre-deployment testing to autonomously refine its interpretation and close specification gaps.

**Benchmark Da
…[truncated 542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T17:36:39.403985+00:00_

Web search results for query: ""PhantomPolicy" LLM agent policy violation benchmark 2024 2025"

Links: [{"title":"[2604.12177] Policy-Invisible Violations in LLM-Based Agents","url":"https://arxiv.org/abs/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents Jie Wu∗ Atlassian Ming Gong","url":"https://arxiv.org/pdf/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents","url":"https://arxiv.org/html/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents | Takara TLDR","url":"https://tldr.takara.ai/p/2604.12177"},{"title":"Training-Free Policy Violation Detection via Activation-Space Whitening in LLMs","url":"https://arxiv.org/pdf/2512.03994"},{"title":"Agent-SafetyBench: Evaluating LLM Agent Safety","url":"https://www.emergentmind.com/topics/agent-safetybench"},{"title":"Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection","url":"https://arxiv.org/pdf/2510.03485"}]

Based on the search results, I found comprehensive information about PhantomPolicy:

## PhantomPolicy Benchmark Overview

PhantomPolicy is a benchmark spanning eight violation categories with balanced violation and safe-control cases, in which all tool responses contain clean business data without policy metadata.

## The Problem It Addresses

LLM-based agents can execute actions that are syntactically valid, user-sanctioned, and semantically appropriate, yet still violate organizational policy because the facts needed for correct policy judgment are hidden at decision time. This failure mode is called policy-invisible violations: cases in which compliance depends on entity attributes, contextual state, or session history absent from the agent's visible context.

## Evaluation Methodology

The researchers manually reviewed all 600 model traces produced by five frontier models and evaluated them using human-reviewed trace labels. Manual review changed 32 labels (5.3%) relative to the original case-level annotations,
…[truncated 619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T17:36:39.404198+00:00_

Web search results for query: ""AgentPex" agent policy benchmark evaluation 2024"

Links: [{"title":"Agent-Pex: Automated Evaluation and Testing of AI Agents - Microsoft Research","url":"https://www.microsoft.com/en-us/research/project/agent-pex-automated-evaluation-and-testing-of-ai-agents/"},{"title":"Willful Disobedience: Automatically Detecting Failures in Agentic Traces","url":"https://arxiv.org/pdf/2603.23806"},{"title":"𝜏-Bench: Benchmarking AI agents for the real-world | Sierra","url":"https://sierra.ai/blog/benchmarking-ai-agents"},{"title":"8 benchmarks shaping the next generation of AI agents","url":"https://tessl.io/blog/8-benchmarks-shaping-the-next-generation-of-ai-agents/"},{"title":"Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection","url":"https://arxiv.org/pdf/2510.03485"},{"title":"The Reliability Gap: Agent Benchmarks for Enterprise – Paul Simmering","url":"https://simmering.dev/blog/agent-benchmarks/"},{"title":"Beyond Accuracy: A Multi-Dimensional Framework for Evaluating Enterprise Agentic AI Systems","url":"https://arxiv.org/html/2511.14136v1"}]

Based on the search results, here's what I found about AgentPex:

## Overview

AgentPex extracts behavioral rules from agent prompts and system instructions, then uses these specifications to automatically evaluate traces for compliance. It's a tool developed by Microsoft Research for automated evaluation and testing of AI agents.

## Key Features

Unlike traditional testing, Agent-Pex leverages the rules embedded in agent prompts and traces, enabling precise, context-aware validation. AgentPex determines whether any rules were violated across multiple steps of the trace, providing reasoning and scores across different dimensions of compliance (e.g., argument validity, output compliance, plan sufficiency, tool-usage appropriateness).

## 2024 Evaluation Results

AgentPex was evaluated on 424 traces from τ²-bench across models in telecom, retail, and airline 
…[truncated 849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T17:36:39.404437+00:00_

Web search results for query: "tau-bench tau2-bench "Shunyu Yao" NeurIPS 2024 sierra-research arXiv 2406.12045"

Links: [{"title":"tau-bench/README.md at main · sierra-research/tau-bench","url":"https://github.com/sierra-research/tau-bench/blob/main/README.md"},{"title":"GitHub - sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub","url":"https://github.com/sierra-research/tau-bench"},{"title":"GitHub - sierra-research/tau2-bench: τ-Bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains · GitHub","url":"https://github.com/sierra-research/tau2-bench"},{"title":"[2406.12045] $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://arxiv.org/abs/2406.12045"},{"title":"[PDF] τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%84-bench:-A-Benchmark-for-Tool-Agent-User-in-Domains-Yao-Shinn/70aa016c1f68fd5c0261f26ad20017b8307650af"},{"title":"(PDF) \\tau$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://www.researchgate.net/publication/381517740_tau-bench_A_Benchmark_for_Tool-Agent-User_Interaction_in_Real-World_Domains"},{"title":"τ-bench: Tool-Agent-User Interaction Benchmark","url":"https://www.emergentmind.com/papers/2406.12045"},{"title":"Paper page - τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains","url":"https://huggingface.co/papers/2406.12045"},{"title":"$\\tau^2$-Bench: Evaluating Conversational Agents in a Dual-Control Environment","url":"https://arxiv.org/pdf/2506.07982"}]

Based on the search results, here's what I found about these benchmarks:

## τ-bench

τ-bench is a benchmark emulating dynamic conversations between a user (simulated by language models) and a language agent provided with domain-specific API tools and policy guidelines. The benchmark addresses the fact that existing benchmarks do not test language agents on their interac
…[truncated 1159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T17:36:39.404645+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2604.12177 \"Policy-Invisible Violations\" PhantomPolicy authors Jie Wu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2604.12177 \"Policy-Invisible Violations\" PhantomPolicy authors Jie Wu"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-20T17:36:39.404780+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Agent-Pex Microsoft Research paper arXiv authors 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Agent-Pex Microsoft Research paper arXiv authors 2024 2025"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T17:36:39.404905+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PolicyBank arXiv 2604.15505 authors \"Evolving Policy Understanding\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PolicyBank arXiv 2604.15505 authors \"Evolving Policy Understanding\""
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-20T17:36:39.405027+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Massey Rutledge Anton \"Identifying and Classifying Ambiguity\" RE 2014 IEEE conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Massey Rutledge Anton \"Identifying and Classifying Ambiguity\" RE 2014 IEEE conference"
  }
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T17:36:39.405148+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Berry Kamsties Krieger 2003 \"From Contract Drafting\" technical report handbook chapter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Berry Kamsties Krieger 2003 \"From Contract Drafting\" technical report handbook chapter"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T17:36:39.405312+00:00_

Web search results for query: "PolicyBank arXiv 2604.15505 authors "Evolving Policy Understanding""

Links: [{"title":"[2604.15505] PolicyBank: Evolving Policy Understanding for LLM Agents","url":"https://arxiv.org/abs/2604.15505"},{"title":"PolicyBank: Evolving Policy Understanding for LLM Agents","url":"https://arxiv.org/html/2604.15505"},{"title":"Improving citizen-government interactions with generative artificial intelligence: Novel human-computer interaction strategies for policy understanding through large language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11651614/"},{"title":"Live in the Moment: Learning Dynamics Model Adapted to Evolving Policy","url":"https://arxiv.org/pdf/2207.12141"},{"title":"[2504.15313] PolicyEvol-Agent: Evolving Policy via Environment Perception and Self-Awareness with Theory of Mind","url":"https://arxiv.org/abs/2504.15313"}]

Based on the search results, here's what I found about the paper:

The arXiv paper 2604.15505 titled "PolicyBank: Evolving Policy Understanding for LLM Agents" was submitted on April 16, 2026 and was authored by Jihye Choi, Jinsung Yoon, Long T. Le, Somesh Jha, and Tomas Pfister.

The paper addresses how LLM agents operating under organizational policies must comply with authorization constraints typically specified in natural language, and how such specifications often contain ambiguities and logical or semantic gaps that cause the agent's behavior to diverge from the true requirements.

The paper proposes PolicyBank, a memory mechanism that maintains structured, tool-level policy insights and iteratively refines them, unlike existing memory mechanisms that treat the policy as immutable ground truth.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-20T17:36:39.405476+00:00_

Web search results for query: "Agent-Pex Microsoft Research paper arXiv authors 2024 2025"

Links: [{"title":"Agent-Pex: Automated Evaluation and Testing of AI Agents - Microsoft Research","url":"https://www.microsoft.com/en-us/research/project/agent-pex-automated-evaluation-and-testing-of-ai-agents/"},{"title":"Willful Disobedience: Automatically Detecting Failures in Agentic Traces","url":"https://arxiv.org/pdf/2603.23806"},{"title":"Impact of Patient Communication Style on Agentic AI-Generated Clinical Advice in E-Medicine","url":"https://www.medrxiv.org/content/10.64898/2025.12.02.25341475.full.pdf"},{"title":"Enhancing memory retrieval in generative agents through LLM-trained cross attention networks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12092450/"},{"title":"Optimizing Order Sets With a Large Language Model–Powered Multiagent System","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12457977/"},{"title":"Microsoft New Future of Work Report 2025 A summary of recent research from","url":"https://www.microsoft.com/en-us/research/wp-content/uploads/2025/12/New-Future-Of-Work-Report-2025.pdf"}]

Based on the search results, I found information about Agent-Pex (also referred to as AgentPex):

AgentPex is an AI-powered tool designed to systematically evaluate agentic traces. It extracts behavioral rules from agent prompts and system instructions, then uses these specifications to automatically evaluate traces for compliance.

**Authors:** The paper is authored by Reshabh K Sharma (University of Washington), Shraddha Barke (Microsoft Research), and Benjamin Zorn (Microsoft Research).

**Publication:** The paper is titled "Willful Disobedience: Automatically Detecting Failures in Agentic Traces" and was published in 2026. The paper is available on arXiv at https://arxiv.org/pdf/2603.23806.

**Overview:** The research evaluated AgentPex on 424 traces from τ²-bench across models in telecom, retail, and airline customer service. Results show that AgentPex
…[truncated 296 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-20T17:36:39.405651+00:00_

Web search results for query: "arXiv 2604.12177 "Policy-Invisible Violations" PhantomPolicy authors Jie Wu"

Links: [{"title":"[2604.12177] Policy-Invisible Violations in LLM-Based Agents","url":"https://arxiv.org/abs/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents","url":"https://arxiv.org/html/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents Jie Wu∗ Atlassian Ming Gong","url":"https://arxiv.org/pdf/2604.12177"},{"title":"Policy-Invisible Violations in LLM-Based Agents | Takara TLDR","url":"https://tldr.takara.ai/p/2604.12177"},{"title":"Towards Policy-Compliant Agents: Learning Efficient Guardrails For Policy Violation Detection","url":"https://arxiv.org/pdf/2510.03485"},{"title":"Training-Free Policy Violation Detection via Activation-Space Whitening in LLMs","url":"https://arxiv.org/pdf/2512.03994"}]

I found the paper you're looking for! Here's what I found:

arXiv paper 2604.12177 is titled "Policy-Invisible Violations in LLM-Based Agents" with authors Jie Wu and Ming Gong.

The paper addresses a failure mode where LLM-based agents can execute actions that are syntactically valid, user-sanctioned, and semantically appropriate, yet still violate organizational policy because the facts needed for correct policy judgment are hidden at decision time—called policy-invisible violations, which are cases where compliance depends on entity attributes, contextual state, or session history absent from the agent's visible context.

The authors present PhantomPolicy, a benchmark spanning eight violation categories with balanced violation and safe-control cases where all tool responses contain clean business data without policy metadata, and they manually review all 600 model traces produced by five frontier models using human-reviewed trace labels.

Manual review changed 32 labels (5.3%) relative to the original case-level annotations, confirming the need for trace-level human review.


REMINDER: You MUST include the sources abo
…[truncated 58 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-20T17:36:39.405830+00:00_

Web search results for query: "Berry Kamsties Krieger 2003 "From Contract Drafting" technical report handbook chapter"

Links: [{"title":"(PDF) From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity","url":"https://www.researchgate.net/publication/228861133_From_Contract_Drafting_to_Software_Specification_Linguistic_Sources_of_Ambiguity"},{"title":"From Contract Drafting to Software Specification: Linguistic ...","url":"https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf"},{"title":"(PDF) From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity (2003) | Daniel M. Berry | 240 Citations","url":"https://scispace.com/papers/from-contract-drafting-to-software-specification-linguistic-z11rvqj117"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=From+contract+drafting+to+software+specification:+Linguistic+sources+of+ambiguity%E2%80%94A+handbook&amp=&author=D.+M.+Berry&amp=&author=E.+Kamsties&amp=&author=M.+M.+Krieger&amp=&publication_year=2003&amp=&pages=753"},{"title":"Ambiguity and tacit knowledge in requirements elicitation interviews | Requirements Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s00766-016-0249-3"},{"title":"An NLP approach for cross-domain ambiguity detection in requirements engineering | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-019-00261-7"},{"title":"[PDF] From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/From-Contract-Drafting-to-Software-Specification:-Berry-Kamsties/d9917b27dec5b1a921a410921da59199436a6e2c"},{"title":"Requirements for tools for ambiguity identification and measurement in natural language requirements specifications | Requirements Engineering","url":"https://link.springer.com/article/10.1007/s00766-008-0063-7"},{"title":"Detecting requi
…[truncated 1508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T17:36:39.406005+00:00_

Web search results for query: "Massey Rutledge Anton "Identifying and Classifying Ambiguity" RE 2014 IEEE conference"

Links: [{"title":"Identifying and classifying ambiguity for regulatory requirements | Request PDF","url":"https://www.researchgate.net/publication/288485563_Identifying_and_classifying_ambiguity_for_regulatory_requirements"},{"title":"RE 2014: Identifying and Classifying Ambiguity for Regulatory Requirements - Speaker Deck","url":"https://speakerdeck.com/akmassey/re-2014-identifying-and-classifying-ambiguity-for-regulatory-requirements"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Identifying+and+classifying+ambiguity+for+regulatory+requirements&amp=&author=A.+K.+Massey&amp=&author=R.+L.+Rutledge&amp=&author=A.+I.+Ant%C3%B3n&amp=&author=P.+P.+Swire&amp=&publication_year=2014&amp=&pages=83-92"},{"title":"[PDF] Identifying and classifying ambiguity for regulatory requirements | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Identifying-and-classifying-ambiguity-for-Massey-Rutledge/ae7de2388daabab5cc00e46a1f89871365b6d550"},{"title":"dblp: Aaron K. Massey","url":"https://dblp.org/pid/30/6548.html"},{"title":"Modeling Regulatory Ambiguities for Requirements Analysis | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-319-69904-2_19"},{"title":"Identifying and Classifying Ambiguity for Regulatory Requirements","url":"https://www.cc.gatech.edu/~aianton/assets/2014_re14_ambiguity.pdf"},{"title":"Modeling Regulatory Ambiguities for Requirements Analysis | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Modeling-Regulatory-Ambiguities-for-Requirements-Massey-Holtgrefe/0056133fa70e57eb76e4bfdfc0cf7b7ebd97eca1"}]

I found the paper you're searching for. Here are the key details:

"Identifying and Classifying Ambiguity for Regulatory Requirements" was presented at the 2014 IEEE 22nd International Requirements Engineering Conference (RE) by authors Aaron Massey (Univer
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-20T17:36:39.406235+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-20T17:36:39.406394+00:00_

=1.11.0
=1.24.0
=1.50.0
=2.0.0
README.md
__pycache__
_project
ambiguity_taxonomy.md
ambiguity_taxonomy_extended.md
analysis
analysis_diag001
analyze.py
api_fallback_comparison.md
clause_templates.json
clause_templates_diag001.json
clause_templates_full.json
clauses_authscope.json
clauses_coreferential.json
clauses_mini_pilot.json
clauses_mini_pilot_coref_v2.json
clauses_mini_pilot_coref_v3.json
clauses_perturbation_control.json
clauses_supplement.json
config.py
config_local.py
diag_001
dream_reports
figures
fix_coreferential.py
fix_pilot_v3.py
fix_pilot_v3b.py
fix_pilot_v3c.py
full_study
generate_cp_part2.py
generate_scopal_31_50.py
harness.py
harness_local.py
info_delta_per_clause.py
injection_pipeline.py
judge.py
judgments
judgments_diag001
judgments_mini_pilot
local_model_client.py
manifest.yaml
plan_002
plan_005
plan_006
plan_009
plan_010
requirements.txt
results
results_diag001
results_mini_pilot
results_mini_pilot_v2
review_issues.yaml
review_reports
run_full_study.py
run_mini_pilot_v3.py
run_plan005.py
run_plan005_gpt41.py
run_plan006.py
run_plan010.py
scripts
setup_vllm.sh
taubench_policy_format.md
tool_response_supplement_log.json
validate_clauses.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-20T17:36:39.406591+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/citation_verification.json",
  "content": "{\n  \"verification_date\": \"2026-05-20\",\n  \"citations\": [\n    {\n      \"key\": \"tau2bench\",\n      \"claimed\": {\n        \"authors\": \"Yao et al.\",\n        \"year\": 2024,\n        \"title\": \"τ²-bench: Benchmarking Agents in Real-World Customer Service (bib1) / A benchmark for tool-augmented agent policies (bib2)\",\n        \"venue\": \"NeurIPS 2024 (bib1) / arXiv preprint (bib2)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan\",\n        \"year\": 2024,\n        \"title\": \"τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\",\n        \"venue\": \"NeurIPS 2024\",\n        \"arxiv_id\": \"2406.12045\"\n      },\n      \"search_evidence\": \"arXiv 2406.12045 confirms the paper by Yao et al. from Sierra Research. OpenReview link (roNSXZpUDN) confirms NeurIPS 2024 venue. Note: the paper is τ-bench (tau-bench), NOT τ²-bench. τ²-bench is a separate 2025 paper by Barres et al. (arXiv 2506.07982) extending τ-bench to dual-control settings. Both bib files have incorrect titles.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Title wrong in both bib files — correct title is 'τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains'\",\n        \"τ²-bench is a DIFFERENT paper (Barres et al., 2025) — if the paper actually uses τ²-bench, the citation must be updated to the correct paper\",\n        \"bib2 lists 'Anonymous' as author — should be Yao, Shinn, Razavi, Narasimhan\"\n      ]\n    },\n    {\n      \"key\": \"drip_r\",\n      \"claimed\": {\n        \"authors\": \"Murthy, Rudra et al. (bib1) / Li, Xiang et al. (bib2)\",\n        \"year\": 2024,\n        \"title\": \"DRIP-R: Benchmarking LLM Agents on Retail Policy Decision Quality Under Ambiguity (bib1) / Divergent Readings of Imprecise Policies in Retail (bib2)\",\n        \"venue\": \"NeurIPS 2024 (bib1) / EMNLP 2024 (bib2)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Hsuvas Borkakoty, Sebastian Pohl, Cheng Wang, Bei Chen, Yufang Hou\",\n        \"year\": 2026,\n        \"title\": \"DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2605.07699\"\n      },\n      \"search_evidence\": \"arXiv 2605.07699 posted May 8, 2026. Authors are from IT:U Austria and Amazon Berlin. No 2024 version of this paper exists. The claimed authors (Murthy/Li), year (2024), venues (NeurIPS/EMNLP), and titles are all fabricated.\",\n      \"status\": \"suspicious\",\n      \"issues\": [\n        \"CRITICAL: Paper was posted May 2026, NOT 2024 — citing it as 2024 is anachronistic\",\n        \"Authors completely wrong in both bib files — actual authors are Borkakoty, Pohl, Wang, Chen, Hou\",\n        \"Title wrong in both bib files\",\n        \"Venue wrong — not published at any conference, only arXiv preprint as of May 2026\",\n        \"HIGH RISK: This citation appears to be hallucinated/fabricated with invented author names and venues\"\n      ]\n    },\n    {\n      \"key\": \"toolformer\",\n      \"claimed\": {\n        \"authors\": \"Timo Schick et al.\",\n        \"year\": 2024,\n        \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\",\n        \"venue\": \"NeurIPS 2024 (as claimed by reviewer)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom\",\n        \"year\": 2023,\n        \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\",\n        \"venue\": \"NeurIPS 2023\",\n        \"arxiv_id\": \"2302.04761\"\n      },\n      \"search_evidence\": \"NeurIPS proceedings page and OpenReview confirm NeurIPS 2023 (poster + oral). The paper was an arXiv preprint in Feb 2023 and presented at NeurIPS 2023. Reviewer correctly identified the year error.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Year wrong: NeurIPS 2023, not 2024\",\n        \"Note: Toolformer not found in the bib files examined — may be in a different version of the paper\"\n      ]\n    },\n    {\n      \"key\": \"massey2014\",\n      \"claimed\": {\n        \"authors\": \"Massey, Aaron K. and Rutledge, Robert L. and others\",\n        \"year\": 2014,\n        \"title\": \"Evaluating Existing Security and Privacy Requirements for Legal Compliance\",\n        \"venue\": \"Requirements Engineering Journal\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Aaron K. Massey, Richard L. Rutledge, Annie I. Antón, Peter P. Swire\",\n        \"year\": 2014,\n        \"title\": \"Identifying and Classifying Ambiguity for Regulatory Requirements\",\n        \"venue\": \"IEEE 22nd International Requirements Engineering Conference (RE 2014)\",\n        \"arxiv_id\": null\n      },\n      \"search_evidence\": \"Confirmed via Semantic Scholar, ResearchGate, and Georgia Tech repository. Paper presented at RE 2014 in Karlskrona, Sweden. Pages 83-92. The bib title 'Evaluating Existing Security and Privacy Requirements for Legal Compliance' is a DIFFERENT Massey paper.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Title wrong — 'Evaluating Existing Security and Privacy Requirements for Legal Compliance' is a different paper by Massey\",\n        \"Venue wrong — it's a conference (IEEE RE 2014), not 'Requirements Engineering Journal'\",\n        \"Co-author first name wrong: Richard (not Robert) L. Rutledge\",\n        \"Missing co-authors: Annie I. Antón and Peter P. Swire should be listed\"\n      ]\n    },\n    {\n      \"key\": \"berry2003\",\n      \"claimed\": {\n        \"authors\": \"Berry, Daniel M. and Kamsties, Erik\",\n        \"year\": 2003,\n        \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity\",\n        \"venue\": \"Technical Report / URL only\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Daniel M. Berry, Erik Kamsties, Michael M. Krieger\",\n        \"year\": 2003,\n        \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity — A Handbook\",\n        \"venue\": \"Technical Report, University of Waterloo\",\n        \"arxiv_id\": null,\n        \"url\": \"https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf\"\n      },\n      \"search_evidence\": \"Confirmed via Semantic Scholar (240+ citations), ResearchGate, and UWaterloo CS dept. Berry (UWaterloo), Kamsties (U Essen), Krieger (UCLA). The third author (Krieger) is missing from the bib entry.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Missing third author: Michael M. Krieger\",\n        \"Note: 'nocuous ambiguity' as a specific term is more associated with Chantree et al. (2006), though Berry & Kamsties discuss ambiguity types extensively\"\n      ]\n    },\n    {\n      \"key\": \"policybank\",\n      \"claimed\": {\n        \"authors\": \"unknown (possibly missing from References)\",\n        \"year\": \"unknown\",\n        \"title\": \"PolicyBank\",\n        \"venue\": \"unknown\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Jihye Choi, Jinsung Yoon, Long T. Le, Somesh Jha, Tomas Pfister\",\n        \"year\": 2026,\n        \"title\": \"PolicyBank: Evolving Policy Understanding for LLM Agents\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2604.15505\"\n      },\n      \"search_evidence\": \"arXiv 2604.15505, submitted April 16, 2026. The paper proposes PolicyBank as a memory mechanism for LLM agents to evolve policy understanding. If referenced in the paper's Table 12, the bib entry must be added.\",\n      \"status\": \"verified\",\n      \"issues\": [\n        \"If cited in the paper but missing from References, this is a critical omission that must be fixed\",\n        \"Paper is from April 2026 — ensure the citation year is correct in context\"\n      ]\n    },\n    {\n      \"key\": \"phantompolicy\",\n      \"claimed\": {\n        \"authors\": \"Wang, Zhe and others\",\n        \"year\": 2024,\n        \"title\": \"PhantomPolicy: Probing Implicit Policy Violations in LLM Agents\",\n        \"venue\": \"ACL 2024\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Jie Wu, Ming Gong\",\n        \"year\": 2026,\n        \"title\": \"Policy-Invisible Violations in LLM-Based Agents\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2604.12177\"\n      },\n      \"search_evidence\": \"arXiv 2604.12177, April 2026. PhantomPolicy is the NAME OF THE BENCHMARK within the paper, not the paper title. Authors are Jie Wu and Ming Gong (Atlassian). No paper titled 'PhantomPolicy: Probing Implicit Policy Violations' by Wang et al. at ACL 2024 exists.\",\n      \"status\": \"suspicious\",\n      \"issues\": [\n        \"CRITICAL: Authors completely wrong — Wu & Gong, not Wang et al.\",\n        \"Year wrong: 2026, not 2024\",\n        \"Venue wrong: arXiv preprint, not ACL 2024\",\n        \"Title wrong: actual paper title is 'Policy-Invisible Violations in LLM-Based Agents'\",\n        \"HIGH RISK: Citation appears hallucinated — fabricated authors and venue\"\n      ]\n    },\n    {\n      \"key\": \"agentpex\",\n      \"claimed\": {\n        \"authors\": \"Zhang, Yifei and others\",\n        \"year\": 2024,\n        \"title\": \"AgentPex: Policy enforcement examination for LLM-based agents\",\n        \"venue\": \"NeurIPS 2024\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Reshabh K Sharma, Shraddha Barke, Benjamin Zorn\",\n        \"year\": 2026,\n        \"title\": \"Willful Disobedience: Automatically Detecting Failures in Agentic Traces\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2603.23806\"\n      },\n      \"search_evidence\": \"Agent-Pex is a Microsoft Research project. The paper 'Willful Disobedience: Automatically Detecting Failures in Agentic Traces' (arXiv 2603.23806, March 2026) describes the AgentPex tool. No paper by Zhang et al. at NeurIPS 2024 with this title exists.\",\n      \"status\": \"suspicious\",\n      \"issues\": [\n        \"CRITICAL: Authors completely wrong — Sharma, Barke, Zorn (Microsoft Research), not Zhang et al.\",\n        \"Year wrong: 2026, not 2024\",\n        \"Venue wrong: arXiv preprint, not NeurIPS 2024\",\n        \"Title wrong: actual paper title is 'Willful Disobedience: Automatically Detecting Failures in Agentic Traces'\",\n        \"HIGH RISK: Citation appears hallucinated — fabricated authors, title, and venue\"\n      ]\n    },\n    {\n      \"key\": \"wasow2005\",\n      \"claimed\": {\n        \"authors\": \"Wasow, Thomas and Perfors, Amy and Beaver, David\",\n        \"year\": 2005,\n        \"title\": \"Intuitions and Models of Vagueness and Ambiguity (bib1) / Ambiguity avoidance is overrated (bib2)\",\n        \"venue\": \"Handbook of Experimental Semantics and Pragmatics (bib1) / Stanford Occasional Papers in Linguistics (bib2)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Thomas Wasow, Amy Perfors, David Beaver\",\n        \"year\": 2005,\n        \"title\": \"The Puzzle of Ambiguity\",\n        \"venue\": \"In C. O. Orgun and P. Sells (eds), Morphology and the Web of Grammar, pp. 265-282, CSLI Publications, Stanford\",\n        \"arxiv_id\": null,\n        \"url\": \"https://web.stanford.edu/~wasow/Lapointe.pdf\"\n      },\n      \"search_evidence\": \"Confirmed via Stanford faculty page and Semantic Scholar. The paper is 'The Puzzle of Ambiguity' in Orgun & Sells (eds). Note: there is ALSO a separate paper 'Ambiguity Avoidance is Overrated' by the same authors. Both bib entries have wrong titles — neither 'Intuitions and Models of Vagueness and Ambiguity' nor the venue 'Handbook of Experimental Semantics and Pragmatics' matched.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"bib1 title 'Intuitions and Models of Vagueness and Ambiguity' does not match any found Wasow paper — may be hallucinated\",\n        \"bib1 venue 'Handbook of Experimental Semantics and Pragmatics' is wrong\",\n        \"bib2 title 'Ambiguity avoidance is overrated' is a real paper but appears to be a different publication\",\n        \"Need to determine which Wasow paper is actually cited in the text and use the correct reference\"\n      ]\n    },\n    {\n      \"key\": \"kennedy2007\",\n      \"claimed\": {\n        \"authors\": \"Kennedy, Christopher\",\n        \"year\": 2007,\n        \"title\": \"Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives\",\n        \"venue\": \"Linguistics and Philosophy, vol. 30, pp. 1-45\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Christopher Kennedy\",\n        \"year\": 2007,\n        \"title\": \"Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives\",\n        \"venue\": \"Linguistics and Philosophy, vol. 30, pp. 1-45\",\n        \"arxiv_id\": null,\n        \"doi\": \"10.1007/s10988-006-9008-0\"\n      },\n      \"search_evidence\": \"Confirmed via Springer (Linguistics and Philosophy), PhilPapers, Semantic Scholar. Kennedy is at University of Chicago. All metadata matches.\",\n      \"status\": \"verified\",\n      \"issues\": []\n    },\n    {\n      \"key\": \"ferreira2002\",\n      \"claimed\": {\n        \"authors\": \"Ferreira, Fernanda and Bailey, Karl G.D. and Ferraro, Vittoria\",\n        \"year\": 2002,\n        \"title\": \"Good-Enough Representations in Language Comprehension\",\n        \"venue\": \"Current Directions in Psychological Science\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Fernanda Ferreira, Karl G.D. Bailey, Vittoria Ferraro\",\n        \"year\": 2002,\n        \"title\": \"Good-Enough Representations in Language Comprehension\",\n        \"venue\": \"Current Directions in Psychological Science, vol. 11, pp. 11-15\",\n        \"arxiv_id\": null,\n        \"doi\": \"10.1111/1467-8721.00158\"\n      },\n      \"search_evidence\": \"Confirmed via SAGE Journals, Semantic Scholar, Andrews University repository. All metadata matches. Note: bib entry type should be @article, not @inproceedings (it's a journal article).\",\n      \"status\": \"verified\",\n      \"issues\": [\n        \"Minor: bib entry type is @inproceedings but should be @article (journal paper)\"\n      ]\n    }\n  ],\n  \"summary\": {\n    \"total\": 11,\n    \"verified\": 3,\n    \"corrected\": 5,\n    \"unverified\": 0,\n    \"suspicious\": 3\n  },\n  \"critical_findings\": [\n    \"DRIP-R, PhantomPolicy, AgentPex: All three have fabricated/hallucinated author names, wrong years (2024 vs actual 2026), and wrong venues. These appear to be LLM-generated citations with invented metadata.\",\n    \"τ-bench vs τ²-bench confusion: The paper may be conflating two different benchmarks. τ-bench (Yao et al., 2024) and τ²-bench (Barres et al., 2025) are separate works.\",\n    \"Toolformer year: NeurIPS 2023, not 2024 (reviewer already flagged this).\",\n    \"Massey: Wrong paper title cited — 'Evaluating Existing Security...' is a different Massey paper from 'Identifying and Classifying Ambiguity...'\",\n    \"Wasow: Title in bib1 ('Intuitions and Models of Vagueness and Ambiguity') could not be verified as a real paper.\"\n  ],\n  \"recommended_actions\": [\n    \"Immediately fix DRIP-R, PhantomPolicy, and AgentPex citations — these are the highest risk for reviewer flags on fabricated references\",\n    \"Verify which τ-bench variant is actually used in experiments and cite accordingly\",\n    \"Fix Toolformer year to 2023\",\n    \"Fix Massey title to 'Identifying and Classifying Ambiguity for Regulatory Requirements'\",\n    \"Add Krieger as third author for Berry & Kamsties (2003)\",\n    \"Determine correct Wasow (2005) paper and fix title/venue\",\n    \"Add PolicyBank to References if cited in text\",\n    \"Change Ferreira et al. bib entry type from @inproceedings to @article\"\n  ]\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/citation_verification.json",
    "content": "{\n  \"verification_date\": \"2026-05-20\",\n  \"citations\": [\n    {\n      \"key\": \"tau2bench\",\n      \"claimed\": {\n        \"authors\": \"Yao et al.\",\n        \"year\": 2024,\n        \"title\": \"τ²-bench: Benchmarking Agents in Real-World Customer Service (bib1) / A benchmark for tool-augmented agent policies (bib2)\",\n        \"venue\": \"NeurIPS 2024 (bib1) / arXiv preprint (bib2)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan\",\n        \"year\": 2024,\n        \"title\": \"τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains\",\n        \"venue\": \"NeurIPS 2024\",\n        \"arxiv_id\": \"2406.12045\"\n      },\n      \"search_evidence\": \"arXiv 2406.12045 confirms the paper by Yao et al. from Sierra Research. OpenReview link (roNSXZpUDN) confirms NeurIPS 2024 venue. Note: the paper is τ-bench (tau-bench), NOT τ²-bench. τ²-bench is a separate 2025 paper by Barres et al. (arXiv 2506.07982) extending τ-bench to dual-control settings. Both bib files have incorrect titles.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Title wrong in both bib files — correct title is 'τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains'\",\n        \"τ²-bench is a DIFFERENT paper (Barres et al., 2025) — if the paper actually uses τ²-bench, the citation must be updated to the correct paper\",\n        \"bib2 lists 'Anonymous' as author — should be Yao, Shinn, Razavi, Narasimhan\"\n      ]\n    },\n    {\n      \"key\": \"drip_r\",\n      \"claimed\": {\n        \"authors\": \"Murthy, Rudra et al. (bib1) / Li, Xiang et al. (bib2)\",\n        \"year\": 2024,\n        \"title\": \"DRIP-R: Benchmarking LLM Agents on Retail Policy Decision Quality Under Ambiguity (bib1) / Divergent Readings of Imprecise Policies in Retail (bib2)\",\n        \"venue\": \"NeurIPS 2024 (bib1) / EMNLP 2024 (bib2)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Hsuvas Borkakoty, Sebastian Pohl, Cheng Wang, Bei Chen, Yufang Hou\",\n        \"year\": 2026,\n        \"title\": \"DRIP-R: A Benchmark for Decision-Making and Reasoning Under Real-World Policy Ambiguity in the Retail Domain\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2605.07699\"\n      },\n      \"search_evidence\": \"arXiv 2605.07699 posted May 8, 2026. Authors are from IT:U Austria and Amazon Berlin. No 2024 version of this paper exists. The claimed authors (Murthy/Li), year (2024), venues (NeurIPS/EMNLP), and titles are all fabricated.\",\n      \"status\": \"suspicious\",\n      \"issues\": [\n        \"CRITICAL: Paper was posted May 2026, NOT 2024 — citing it as 2024 is anachronistic\",\n        \"Authors completely wrong in both bib files — actual authors are Borkakoty, Pohl, Wang, Chen, Hou\",\n        \"Title wrong in both bib files\",\n        \"Venue wrong — not published at any conference, only arXiv preprint as of May 2026\",\n        \"HIGH RISK: This citation appears to be hallucinated/fabricated with invented author names and venues\"\n      ]\n    },\n    {\n      \"key\": \"toolformer\",\n      \"claimed\": {\n        \"authors\": \"Timo Schick et al.\",\n        \"year\": 2024,\n        \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\",\n        \"venue\": \"NeurIPS 2024 (as claimed by reviewer)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom\",\n        \"year\": 2023,\n        \"title\": \"Toolformer: Language Models Can Teach Themselves to Use Tools\",\n        \"venue\": \"NeurIPS 2023\",\n        \"arxiv_id\": \"2302.04761\"\n      },\n      \"search_evidence\": \"NeurIPS proceedings page and OpenReview confirm NeurIPS 2023 (poster + oral). The paper was an arXiv preprint in Feb 2023 and presented at NeurIPS 2023. Reviewer correctly identified the year error.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Year wrong: NeurIPS 2023, not 2024\",\n        \"Note: Toolformer not found in the bib files examined — may be in a different version of the paper\"\n      ]\n    },\n    {\n      \"key\": \"massey2014\",\n      \"claimed\": {\n        \"authors\": \"Massey, Aaron K. and Rutledge, Robert L. and others\",\n        \"year\": 2014,\n        \"title\": \"Evaluating Existing Security and Privacy Requirements for Legal Compliance\",\n        \"venue\": \"Requirements Engineering Journal\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Aaron K. Massey, Richard L. Rutledge, Annie I. Antón, Peter P. Swire\",\n        \"year\": 2014,\n        \"title\": \"Identifying and Classifying Ambiguity for Regulatory Requirements\",\n        \"venue\": \"IEEE 22nd International Requirements Engineering Conference (RE 2014)\",\n        \"arxiv_id\": null\n      },\n      \"search_evidence\": \"Confirmed via Semantic Scholar, ResearchGate, and Georgia Tech repository. Paper presented at RE 2014 in Karlskrona, Sweden. Pages 83-92. The bib title 'Evaluating Existing Security and Privacy Requirements for Legal Compliance' is a DIFFERENT Massey paper.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Title wrong — 'Evaluating Existing Security and Privacy Requirements for Legal Compliance' is a different paper by Massey\",\n        \"Venue wrong — it's a conference (IEEE RE 2014), not 'Requirements Engineering Journal'\",\n        \"Co-author first name wrong: Richard (not Robert) L. Rutledge\",\n        \"Missing co-authors: Annie I. Antón and Peter P. Swire should be listed\"\n      ]\n    },\n    {\n      \"key\": \"berry2003\",\n      \"claimed\": {\n        \"authors\": \"Berry, Daniel M. and Kamsties, Erik\",\n        \"year\": 2003,\n        \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity\",\n        \"venue\": \"Technical Report / URL only\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Daniel M. Berry, Erik Kamsties, Michael M. Krieger\",\n        \"year\": 2003,\n        \"title\": \"From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity — A Handbook\",\n        \"venue\": \"Technical Report, University of Waterloo\",\n        \"arxiv_id\": null,\n        \"url\": \"https://cs.uwaterloo.ca/~dberry/handbook/ambiguityHandbook.pdf\"\n      },\n      \"search_evidence\": \"Confirmed via Semantic Scholar (240+ citations), ResearchGate, and UWaterloo CS dept. Berry (UWaterloo), Kamsties (U Essen), Krieger (UCLA). The third author (Krieger) is missing from the bib entry.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"Missing third author: Michael M. Krieger\",\n        \"Note: 'nocuous ambiguity' as a specific term is more associated with Chantree et al. (2006), though Berry & Kamsties discuss ambiguity types extensively\"\n      ]\n    },\n    {\n      \"key\": \"policybank\",\n      \"claimed\": {\n        \"authors\": \"unknown (possibly missing from References)\",\n        \"year\": \"unknown\",\n        \"title\": \"PolicyBank\",\n        \"venue\": \"unknown\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Jihye Choi, Jinsung Yoon, Long T. Le, Somesh Jha, Tomas Pfister\",\n        \"year\": 2026,\n        \"title\": \"PolicyBank: Evolving Policy Understanding for LLM Agents\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2604.15505\"\n      },\n      \"search_evidence\": \"arXiv 2604.15505, submitted April 16, 2026. The paper proposes PolicyBank as a memory mechanism for LLM agents to evolve policy understanding. If referenced in the paper's Table 12, the bib entry must be added.\",\n      \"status\": \"verified\",\n      \"issues\": [\n        \"If cited in the paper but missing from References, this is a critical omission that must be fixed\",\n        \"Paper is from April 2026 — ensure the citation year is correct in context\"\n      ]\n    },\n    {\n      \"key\": \"phantompolicy\",\n      \"claimed\": {\n        \"authors\": \"Wang, Zhe and others\",\n        \"year\": 2024,\n        \"title\": \"PhantomPolicy: Probing Implicit Policy Violations in LLM Agents\",\n        \"venue\": \"ACL 2024\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Jie Wu, Ming Gong\",\n        \"year\": 2026,\n        \"title\": \"Policy-Invisible Violations in LLM-Based Agents\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2604.12177\"\n      },\n      \"search_evidence\": \"arXiv 2604.12177, April 2026. PhantomPolicy is the NAME OF THE BENCHMARK within the paper, not the paper title. Authors are Jie Wu and Ming Gong (Atlassian). No paper titled 'PhantomPolicy: Probing Implicit Policy Violations' by Wang et al. at ACL 2024 exists.\",\n      \"status\": \"suspicious\",\n      \"issues\": [\n        \"CRITICAL: Authors completely wrong — Wu & Gong, not Wang et al.\",\n        \"Year wrong: 2026, not 2024\",\n        \"Venue wrong: arXiv preprint, not ACL 2024\",\n        \"Title wrong: actual paper title is 'Policy-Invisible Violations in LLM-Based Agents'\",\n        \"HIGH RISK: Citation appears hallucinated — fabricated authors and venue\"\n      ]\n    },\n    {\n      \"key\": \"agentpex\",\n      \"claimed\": {\n        \"authors\": \"Zhang, Yifei and others\",\n        \"year\": 2024,\n        \"title\": \"AgentPex: Policy enforcement examination for LLM-based agents\",\n        \"venue\": \"NeurIPS 2024\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Reshabh K Sharma, Shraddha Barke, Benjamin Zorn\",\n        \"year\": 2026,\n        \"title\": \"Willful Disobedience: Automatically Detecting Failures in Agentic Traces\",\n        \"venue\": \"arXiv preprint\",\n        \"arxiv_id\": \"2603.23806\"\n      },\n      \"search_evidence\": \"Agent-Pex is a Microsoft Research project. The paper 'Willful Disobedience: Automatically Detecting Failures in Agentic Traces' (arXiv 2603.23806, March 2026) describes the AgentPex tool. No paper by Zhang et al. at NeurIPS 2024 with this title exists.\",\n      \"status\": \"suspicious\",\n      \"issues\": [\n        \"CRITICAL: Authors completely wrong — Sharma, Barke, Zorn (Microsoft Research), not Zhang et al.\",\n        \"Year wrong: 2026, not 2024\",\n        \"Venue wrong: arXiv preprint, not NeurIPS 2024\",\n        \"Title wrong: actual paper title is 'Willful Disobedience: Automatically Detecting Failures in Agentic Traces'\",\n        \"HIGH RISK: Citation appears hallucinated — fabricated authors, title, and venue\"\n      ]\n    },\n    {\n      \"key\": \"wasow2005\",\n      \"claimed\": {\n        \"authors\": \"Wasow, Thomas and Perfors, Amy and Beaver, David\",\n        \"year\": 2005,\n        \"title\": \"Intuitions and Models of Vagueness and Ambiguity (bib1) / Ambiguity avoidance is overrated (bib2)\",\n        \"venue\": \"Handbook of Experimental Semantics and Pragmatics (bib1) / Stanford Occasional Papers in Linguistics (bib2)\"\n      },\n      \"verified\": false,\n      \"corrected\": {\n        \"authors\": \"Thomas Wasow, Amy Perfors, David Beaver\",\n        \"year\": 2005,\n        \"title\": \"The Puzzle of Ambiguity\",\n        \"venue\": \"In C. O. Orgun and P. Sells (eds), Morphology and the Web of Grammar, pp. 265-282, CSLI Publications, Stanford\",\n        \"arxiv_id\": null,\n        \"url\": \"https://web.stanford.edu/~wasow/Lapointe.pdf\"\n      },\n      \"search_evidence\": \"Confirmed via Stanford faculty page and Semantic Scholar. The paper is 'The Puzzle of Ambiguity' in Orgun & Sells (eds). Note: there is ALSO a separate paper 'Ambiguity Avoidance is Overrated' by the same authors. Both bib entries have wrong titles — neither 'Intuitions and Models of Vagueness and Ambiguity' nor the venue 'Handbook of Experimental Semantics and Pragmatics' matched.\",\n      \"status\": \"corrected\",\n      \"issues\": [\n        \"bib1 title 'Intuitions and Models of Vagueness and Ambiguity' does not match any found Wasow paper — may be hallucinated\",\n        \"bib1 venue 'Handbook of Experimental Semantics and Pragmatics' is wrong\",\n        \"bib2 title 'Ambiguity avoidance is overrated' is a real paper but appears to be a different publication\",\n        \"Need to determine which Wasow paper is actually cited in the text and use the correct reference\"\n      ]\n    },\n    {\n      \"key\": \"kennedy2007\",\n      \"claimed\": {\n        \"authors\": \"Kennedy, Christopher\",\n        \"year\": 2007,\n        \"title\": \"Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives\",\n        \"venue\": \"Linguistics and Philosophy, vol. 30, pp. 1-45\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Christopher Kennedy\",\n        \"year\": 2007,\n        \"title\": \"Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives\",\n        \"venue\": \"Linguistics and Philosophy, vol. 30, pp. 1-45\",\n        \"arxiv_id\": null,\n        \"doi\": \"10.1007/s10988-006-9008-0\"\n      },\n      \"search_evidence\": \"Confirmed via Springer (Linguistics and Philosophy), PhilPapers, Semantic Scholar. Kennedy is at University of Chicago. All metadata matches.\",\n      \"status\": \"verified\",\n      \"issues\": []\n    },\n    {\n      \"key\": \"ferreira2002\",\n      \"claimed\": {\n        \"authors\": \"Ferreira, Fernanda and Bailey, Karl G.D. and Ferraro, Vittoria\",\n        \"year\": 2002,\n        \"title\": \"Good-Enough Representations in Language Comprehension\",\n        \"venue\": \"Current Directions in Psychological Science\"\n      },\n      \"verified\": true,\n      \"corrected\": {\n        \"authors\": \"Fernanda Ferreira, Karl G.D. Bailey, Vittoria Ferraro\",\n        \"year\": 2002,\n        \"title\": \"Good-Enough Representations in Language Comprehension\",\n        \"venue\": \"Current Directions in Psychological Science, vol. 11, pp. 11-15\",\n        \"arxiv_id\": null,\n        \"doi\": \"10.1111/1467-8721.00158\"\n      },\n      \"search_evidence\": \"Confirmed via SAGE Journals, Semantic Scholar, Andrews University repository. All metadata matches. Note: bib entry type should be @article, not @inproceedings (it's a journal article).\",\n      \"status\": \"verified\",\n      \"issues\": [\n        \"Minor: bib entry type is @inproceedings but should be @article (journal paper)\"\n      ]\n    }\n  ],\n  \"summary\": {\n    \"total\": 11,\n    \"verified\": 3,\n    \"corrected\": 5,\n    \"unverified\": 0,\n    \"suspicious\": 3\n  },\n  \"critical_findings\": [\n    \"DRIP-R, PhantomPolicy, AgentPex: All three have fabricated/hallucinated author names, wrong years (2024 vs actual 2026), and wrong venues. These appear to be LLM-generated citations with invented metadata.\",\n    \"τ-bench vs τ²-bench confusion: The paper may be conflating two different benchmarks. τ-bench (Yao et al., 2024) and τ²-bench (Barres et al., 2025) are separate works.\",\n    \"Toolformer year: NeurIPS 2023, not 2024 (reviewer already flagged this).\",\n    \"Massey: Wrong paper title cited — 'Evaluating Existing Security...' is a different Massey paper from 'Identifying and Classifying Ambiguity...'\",\n    \"Wasow: Title in bib1 ('Intuitions and Models of Vagueness and Ambiguity') could not be verified as a real paper.\"\n  ],\n  \"recommended_actions\": [\n    \"Immediately fix DRIP-R, PhantomPolicy, and AgentPex citations — these are the highest risk for reviewer flags on fabricated references\",\n    \"Verify which τ-bench variant is actually used in experiments and cite accordingly\",\n    \"Fix Toolformer year to 2023\",\n    \"Fix Massey title to 'Identifying and Classifying Ambiguity for Regulatory Requirements'\",\n    \"Add Krieger as third author for Berry & Kamsties (2003)\",\n    \"Determine correct Wasow (2005) paper and fix title/venue\",\n    \"Add PolicyBank to References if cited in text\",\n    \"Change Ferreira et al. bib entry type from @inproceedings to @article\"\n  ]\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-20T17:36:39.406957+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/citation_verification.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-20T17:36:39.407112+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-20T17:36:39.407265+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-20T17:36:39.407397+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "citation_verification",
  "type": "report",
  "description": "全量引用验证报告：11条引用的真实性和准确性检查，发现3条可疑（疑似虚构）、5条需修正、3条已验证",
  "project": "policy_ambiguity_safety",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/citation_verification.json",
  "tags": "['citation', 'verification', 'quality-check']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "citation_verification",
    "type": "report",
    "description": "全量引用验证报告：11条引用的真实性和准确性检查，发现3条可疑（疑似虚构）、5条需修正、3条已验证",
    "project": "policy_ambiguity_safety",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/citation_verification.json",
    "tags": "['citation', 'verification', 'quality-check']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-20T17:36:39.407598+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_9f7f77\", \"name\": \"citation_verification\", \"type\": \"report\", \"description\": \"全量引用验证报告：11条引用的真实性和准确性检查，发现3条可疑（疑似虚构）、5条需修正、3条已验证\", \"path\": \"projects/policy_ambiguity_safety/artifacts/_project/report/citation_verification.json\", \"url\": null, \"project\": \"policy_ambiguity_safety\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T17:36:25.002136+00:00\", \"tags\": [\"citation\", \"verification\", \"quality-check\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation_verification_20260520T173215",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 59 · 2026-05-20T17:36:39.407781+00:00_

验证完成。结果写入 `artifacts/citation_verification.json`。

## 核心发现

**3 条高危（疑似虚构）：**

| 引用 | 问题 |
|------|------|
| **DRIP-R** | 实际 Borkakoty et al., **2026** (arXiv 2605.07699)。bib 中的 Murthy/Li et al. 2024、NeurIPS/EMNLP venue 全部是编造的 |
| **PhantomPolicy** | 实际 Jie Wu & Ming Gong, **2026** (arXiv 2604.12177)。bib 中 Wang et al. ACL 2024 是编造的 |
| **AgentPex** | 实际 Sharma, Barke, Zorn (Microsoft Research), **2026** (arXiv 2603.23806)。bib 中 Zhang et al. NeurIPS 2024 是编造的 |

**5 条需修正：**

| 引用 | 问题 |
|------|------|
| **τ-bench / τ²-bench** | 正确标题 "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"（Yao et al., NeurIPS 2024, arXiv 2406.12045）。τ²-bench 是另一篇论文（Barres et al., 2025） |
| **Toolformer** | NeurIPS **2023**，不是 2024 |
| **Massey** | 标题错——bib 中是另一篇 Massey 论文。正确标题 "Identifying and Classifying Ambiguity for Regulatory Requirements"，RE 2014 |
| **Berry & Kamsties** | 缺第三作者 Michael M. Krieger |
| **Wasow (2005)** | bib1 标题 "Intuitions and Models of Vagueness and Ambiguity" 查无此文。实际论文标题 "The Puzzle of Ambiguity"（CSLI Publications） |

**3 条已验证：** Kennedy (2007)、Ferreira et al. (2002)、PolicyBank（但需确认是否已加入 References）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_citation_verification_20260520T173215"
}
```

</details>

---
