# research ref audit batch1

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 31
- **Original source:** `logs/chats/worker_research_ref-audit-batch1_20260526T061956.jsonl`
- **Structured JSON:** [`3a0532c7ca35c7733597.json`](../../sessions/3a/3a0532c7ca35c7733597.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

63 recorded events

### Tool call

_source line 1 · 2026-05-26T06:24:31.243010+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T06:24:31.243633+00:00_

1	% === Statistical Methods ===
2	
3	@article{cameron2008bootstrap,
4	  author    = {A. Colin Cameron and Jonah B. Gelbach and Douglas L. Miller},
5	  title     = {Bootstrap-Based Improvements for Inference with Clustered Errors},
6	  journal   = {Review of Economics and Statistics},
7	  volume    = {90},
8	  number    = {3},
9	  pages     = {414--427},
10	  year      = {2008},
11	}
12	
13	@book{wellek2010,
14	  author    = {Stefan Wellek},
15	  title     = {Testing Statistical Hypotheses of Equivalence and Noninferiority},
16	  publisher = {Chapman and Hall/CRC},
17	  edition   = {2nd},
18	  year      = {2010},
19	}
20	
21	@article{moulton1990,
22	  author  = {Brent R. Moulton},
23	  title   = {An Illustration of a Pitfall in Estimating the Effects of Aggregate Variables on Micro Units},
24	  journal = {The Review of Economics and Statistics},
25	  volume  = {72},
26	  number  = {2},
27	  pages   = {334--338},
28	  year    = {1990},
29	}
30	
31	@book{cohen1988,
32	  author    = {Cohen, Jacob},
33	  title     = {Statistical Power Analysis for the Behavioral Sciences},
34	  edition   = {2nd},
35	  publisher = {Lawrence Erlbaum Associates},
36	  year      = {1988}
37	}
38	
39	@article{kruschke2013bayesian,
40	  title={Bayesian estimation supersedes the t test},
41	  author={Kruschke, John K},
42	  journal={Journal of Experimental Psychology: General},
43	  volume={142},
44	  number={2},
45	  pages={573--603},
46	  year={2013},
47	  publisher={American Psychological Association}
48	}
49	
50	@article{kruschke2018rejecting,
51	  title={Rejecting or accepting parameter values in {B}ayesian estimation},
52	  author={Kruschke, John K},
53	  journal={Advances in Methods and Practices in Psychological Science},
54	  volume={1},
55	  number={2},
56	  pages={270--280},
57	  year={2018},
58	  publisher={SAGE Publications}
59	}
60	
61	% === Execution Simulation ===
62	
63	@inproceedings{gu2024cruxeval,
64	  title={{CRUXEval}: A Benchmark for Code Reasoning, Understanding and Exec
…[truncated 23079 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T06:24:31.243917+00:00_

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
  "session": "worker_research_ref-audit-batch1_20260526T061956",
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

_source line 4 · 2026-05-26T06:24:31.244080+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T06:24:31.244283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "REPOEXEC Evaluate Code Generation Repository-Level Executable Benchmark Nam Dau Bui Nguyen NAACL 2025",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'aclanthology.org', 'arxiv.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "REPOEXEC Evaluate Code Generation Repository-Level Executable Benchmark Nam Dau Bui Nguyen NAACL 2025",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'aclanthology.org', 'arxiv.org', 'openreview.net']"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-26T06:24:31.244438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodeMind Framework Challenge Large Language Models Code Reasoning Liu Zhang Ibrahimzada Jabbarvand 2024",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'aclanthology.org', 'arxiv.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodeMind Framework Challenge Large Language Models Code Reasoning Liu Zhang Ibrahimzada Jabbarvand 2024",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'aclanthology.org', 'arxiv.org', 'openreview.net']"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T06:24:31.244572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PatchReasoner Scalable Supervising Software Agents Xu Tan Liu Peng Gao He 2025",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PatchReasoner Scalable Supervising Software Agents Xu Tan Liu Peng Gao He 2025",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-26T06:24:31.244711+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Introducing SWE-bench Verified Chowdhury Aung Shern 2024 OpenAI",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'openai.com']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Introducing SWE-bench Verified Chowdhury Aung Shern 2024 OpenAI",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'openai.com']"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T06:24:31.244908+00:00_

Web search results for query: "REPOEXEC Evaluate Code Generation Repository-Level Executable Benchmark Nam Dau Bui Nguyen NAACL 2025"

Links: [{"title":"On the Impacts of Contexts on Repository-Level Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.82/"},{"title":"RepoExec: Evaluate Code Generation with a Repository-Level Executable Benchmark","url":"https://arxiv.org/html/2406.11927v1/"},{"title":"[2406.11927v2] REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark","url":"https://arxiv.org/abs/2406.11927v2"},{"title":"On the Impacts of Contexts on Repository-Level Code Generation","url":"https://arxiv.org/html/2406.11927v3"},{"title":"[2406.11927v1] REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark","url":"https://arxiv.org/abs/2406.11927v1"},{"title":"[2406.11927] On the Impacts of Contexts on Repository-Level Code Generation","url":"https://arxiv.org/abs/2406.11927"},{"title":"In Line with Context: Repository-Level Code Generation via Context Inlining","url":"https://arxiv.org/pdf/2601.00376"},{"title":"On the Impacts of Contexts on Repository-Level Code Generation","url":"https://arxiv.org/pdf/2406.11927"},{"title":"What to Retrieve for Effective Retrieval-Augmented Code ...","url":"https://arxiv.org/pdf/2503.20589"}]

Based on the search results, here's what I found about REPOEXEC:

RepoExec is a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization. The work is authored by Nam Le Hai, Dung Manh Nguyen, and Nghi D. Q. Bui from FPT Software AI Center and Hanoi University of Science and Technology in Vietnam.

RepoExec focuses on three main aspects: executability, functional correctness through automated test case generation with high coverage rate, and carefully crafted cross-file contexts to accurately generate code. The work explores a controlled scenario where developers specify necessa
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T06:24:31.245081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Let's Verify Step by Step Lightman Kosaraju Burda Edwards Baker 2023 arXiv",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Let's Verify Step by Step Lightman Kosaraju Burda Edwards Baker 2023 arXiv",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'openreview.net']"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T06:24:31.245217+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Predictive Mutation Testing via Natural Language Channel Kim Ju Tao Hu Baik 2022 IEEE TSE",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'ieeexplore.ieee.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Predictive Mutation Testing via Natural Language Channel Kim Ju Tao Hu Baik 2022 IEEE TSE",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'ieeexplore.ieee.org']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T06:24:31.245375+00:00_

Web search results for query: "CodeMind Framework Challenge Large Language Models Code Reasoning Liu Zhang Ibrahimzada Jabbarvand 2024"

Links: [{"title":"[2402.09664v4] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"https://arxiv.org/abs/2402.09664v4"},{"title":"[PDF] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/e3af189157c0c0fe12a77043c09539caf996cde5"},{"title":"[2402.09664v1] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"http://arxiv.org/abs/2402.09664v1"},{"title":"[2402.09664v2] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"http://arxiv.org/abs/2402.09664v2"},{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/f75673eefe0217464a1d30f6d373e696e26ae055"},{"title":"How Does LLM Reasoning Work for Code? A Survey and a Call to Action","url":"https://arxiv.org/html/2506.13932v1"},{"title":"Code to Think, Think to Code: A Survey on Code-Enhanced Reasoning and Reasoning-Driven Code Intelligence in LLMs","url":"https://arxiv.org/html/2502.19411v1"},{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"https://arxiv.org/html/2402.09664v3"}]

Based on the search results, here's what I found about the CodeMind Framework:

## Overview

CodeMind is a framework to challenge large language models for code reasoning, authored by Changshu Liu, Shizhuo Dylan Zhang, Ali Reza Ibrahimzada, and Reyhaneh Jabbarvand. The paper was submitted on February 15, 2024.

## Key Findings

An extensive evaluation of nine LLMs across five benchmarks in two different programming languages using CodeMind shows that LLMs fairly follow cont
…[truncated 990 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T06:24:31.245543+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Is Mutation an Adequate Substitute for Real Faults\" Andrews Briand Labiche ICSE 2005",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'dl.acm.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Is Mutation an Adequate Substitute for Real Faults\" Andrews Briand Labiche ICSE 2005",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'dl.acm.org']"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T06:24:31.245695+00:00_

Web search results for query: "PatchReasoner Scalable Supervising Software Agents Xu Tan Liu Peng Gao He 2025"

Links: [{"title":"[2510.22775] Scalable Supervising Software Agents with Patch Reasoner","url":"https://arxiv.org/abs/2510.22775"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=14750&show=50"},{"title":"Scalable Supervising Software Agents with Patch Reasoner","url":"https://arxiv.org/html/2510.22775v1"},{"title":"dblp: Pinjia He","url":"https://dblp.org/pid/147/1619.html"},{"title":"Preprint SCALABLE SUPERVISING SOFTWARE AGENTS WITH PATCH REASONER","url":"https://arxiv.org/pdf/2510.22775"},{"title":"PatchPilot: A Cost-Efficient Software Engineering Agent with Early Attempts on Formal Verification","url":"https://arxiv.org/html/2502.02747v2"}]

Based on the search results, I found the research paper you're looking for:

**"Scalable Supervising Software Agents with Patch Reasoner"** by Junjielong Xu, Boyin Tan, Xiaoyuan Liu, Chao Peng, Pengfei Gao, and Pinjia He, published in October 2025.

**Overview:**
The paper proposes R4P, a patch verifier model to provide scalable rewards for training and testing software engineering (SWE) agents via reasoning.

**Key Problem:**
The issue is twofold: (1) building and running test sandbox is rather heavy and fragile, and (2) data with high-coverage tests is naturally rare and threatened by test hacking via edge cases.

**Core Approach:**
Patch verification is considered fundamentally a reasoning task, mirroring how human repository maintainers review patches without writing and running new reproduction tests.

The paper was submitted on October 26, 2025 to arXiv and is available at arXiv:2510.22775.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T06:24:31.245873+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mostly Harmless Econometrics Empiricist's Companion Angrist Pischke 2009 Princeton University Press",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'press.princeton.edu']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mostly Harmless Econometrics Empiricist's Companion Angrist Pischke 2009 Princeton University Press",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'press.princeton.edu']"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-26T06:24:31.246011+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Synchromesh Reliable Code Generation Retrieving Translating Poesia Polozov Le Tiwari ICLR 2022",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Synchromesh Reliable Code Generation Retrieving Translating Poesia Polozov Le Tiwari ICLR 2022",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'openreview.net']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-26T06:24:31.246173+00:00_

Web search results for query: "Introducing SWE-bench Verified Chowdhury Aung Shern 2024 OpenAI"

Links: [{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"SWE-bench Multimodal: Do AI Systems Generalize to Visual Software Domains?","url":"https://arxiv.org/html/2410.03859v1"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"},{"title":"SWE-Bench-CL: Continual Learning for Coding Agents","url":"https://arxiv.org/pdf/2507.00014"},{"title":"[2507.00014] SWE-Bench-CL: Continual Learning for Coding Agents","url":"https://arxiv.org/abs/2507.00014"},{"title":"Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI","url":"https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"}]

Based on the search results, here's what I found about "Introducing SWE-bench Verified":

The paper/blog was authored by Neil Chowdhury, James Aung, Chan Jun Shern, Oliver Jaffe, Dane Sherburn, Giulio Starace, Evan Mays, Rachel Dias, Marwan Aljubeh, Mia Glaese, Carlos E. Jimenez, John Yang, Leyton Ho, Tejal Patwardhan, Kevin Liu, and Aleksander Madry from OpenAI.

SWE-bench Verified was created in 2024 to address issues in the original SWE-bench benchmark. The team worked with expert software engineers to review 1,699 SWE-bench problems and filter out problematic ones. This review process resulted in SWE-bench Verified, a curated set of 500 problems.

The paper was first published in August 2024, and the testing identified some SWE-bench tasks which may be hard or impossible to solve, leading to SWE-bench systematically underestimating models' autonomous software engine capabilities.

The work was published on OpenAI's official blog at: htt
…[truncated 156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T06:24:31.246357+00:00_

Web search results for query: "Let's Verify Step by Step Lightman Kosaraju Burda Edwards Baker 2023 arXiv"

Links: [{"title":"[2305.20050v1] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050v1"},{"title":"[2305.20050] Let's Verify Step by Step","url":"https://arxiv.org/abs/2305.20050"},{"title":"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math","url":"https://arxiv.org/html/2510.13744v1"},{"title":"[2305.20050] Let's Verify Step by Step","url":"http://export.arxiv.org/abs/2305.20050"},{"title":"[PDF] Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"},{"title":"Figure 2 from Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc/figure/2"},{"title":"Table 3 from Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc/figure/5"},{"title":"[2305.20050] Let's Verify Step by Step - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.20050"},{"title":"Let’s Verify Step by Step Hunter Lightman∗ Vineet Kosaraju∗ Yura Burda∗","url":"https://arxiv.org/pdf/2305.20050"}]

I found the paper you're looking for. Here's the information:

"Let's Verify Step by Step" is authored by Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. The paper was published on arXiv on May 31, 2023 with the arXiv ID 2305.20050.

The paper compares outcome supervision (which provides feedback for a final result) versus process supervision (which provides feedback for each intermediate reasoning step), finding that process supervision significantly outperforms outcome supervision for training models
…[truncated 217 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T06:24:31.246526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AlphaCode 2 Technical Report Google DeepMind 2023",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'deepmind.google']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AlphaCode 2 Technical Report Google DeepMind 2023",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'arxiv.org', 'deepmind.google']"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-26T06:24:31.246657+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Cohen 1988 Statistical Power Analysis Behavioral Sciences Lawrence Erlbaum",
  "allowed_domains": "['semanticscholar.org', 'dblp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Cohen 1988 Statistical Power Analysis Behavioral Sciences Lawrence Erlbaum",
    "allowed_domains": "['semanticscholar.org', 'dblp.org']"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-26T06:24:31.246834+00:00_

Web search results for query: ""Is Mutation an Adequate Substitute for Real Faults" Andrews Briand Labiche ICSE 2005"

Links: [{"title":"Are mutants a valid substitute for real faults in software testing? | Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering","url":"https://dl.acm.org/doi/abs/10.1145/2635868.2635929"},{"title":"Are Mutants a Valid Substitute for Real Faults in Software ...","url":"https://pdfs.semanticscholar.org/f0a6/2b5d5b33a882c9e67f9662d525ab672756d4.pdf"},{"title":"[PDF] Is mutation an appropriate tool for testing experiments? [software testing] | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-mutation-an-appropriate-tool-for-testing-Andrews-Briand/0cb937952b654695e5afdbc86e690894f34605fa"},{"title":"Equivalent Mutants in the Wild: Identifying and Efficiently Suppressing Equivalent Mutants for Java Programs | Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis","url":"https://dl.acm.org/doi/10.1145/3650212.3680310"},{"title":"LEAM++: Learning for Selective Mutation Fault Construction | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3725528"},{"title":"[PDF] Are mutants a valid substitute for real faults in software testing? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Are-mutants-a-valid-substitute-for-real-faults-in-Just-Jalali/e126c283f2d5b521ed535c2bbd265fe3ccd14d9f"},{"title":"Evaluating random mutant selection at class-level in projects with non-adequate test suites | Proceedings of the 20th International Conference on Evaluation and Assessment in Software Engineering","url":"https://dl.acm.org/doi/10.1145/2915970.2915992"},{"title":"Is Mutation an Appropriate Tool for Testing Experiments?","url":"https://pdfs.semanticscholar.org/78f6/1e32fc6e3f7ec6328f3ef4e2a9c9be2fd34f.pdf"},{"title":"Is mutation an appropriate tool for testing experiments? | Proceedings of the 27t
…[truncated 1302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T06:24:31.247022+00:00_

Web search results for query: "Predictive Mutation Testing via Natural Language Channel Kim Ju Tao Hu Baik 2022 IEEE TSE"

Links: [{"title":"Predictive Mutation Analysis via Natural Language Channel in Source Code","url":"https://arxiv.org/pdf/2104.10865"},{"title":"[PDF] Predictive Mutation Analysis via the Natural Language Channel in Source Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/29f44d6f53d383f9251d6b54810bb23277c9445f"},{"title":"Contextual Predictive Mutation Testing","url":"https://arxiv.org/pdf/2309.02389"},{"title":"Test Case Level Predictive Mutation Testing Combining PIE and Natural Language Features | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10479449/"},{"title":"Predictive Mutation Testing | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/8304576/"}]

Based on the search results, I found information about research on Predictive Mutation Testing via Natural Language. Here are the key findings:

The paper "Predictive Mutation Analysis via Natural Language Channel in Source Code" was written by Jinhan Kim, Juyoung Jeon, Shin Hong, and Shin Yoo from KAIST and Handong Global University, with a preprint date of January 5, 2022.

However, I should note that the authors in your query (Kim Ju, Tao Hu, and Baik) don't appear to match the authors in the search results. The paper I found is titled "Predictive Mutation Analysis via Natural Language Channel" (rather than "Testing"), and proposes Seshat, a Predictive Mutation Analysis technique that can accurately predict the entire kill matrix, and exploits the natural language channel in code to learn the relationship between syntactic and semantic concepts of test cases and the mutants they can kill.

Empirical evaluation using programs in DEFECTS4J shows that Seshat can predict kill matrices with an average F-score of 0.83 for versions that are up to years apart.

If you're looking for a different paper w
…[truncated 168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-26T06:24:31.247199+00:00_

Web search results for query: "Mostly Harmless Econometrics Empiricist's Companion Angrist Pischke 2009 Princeton University Press"

Links: [{"title":"[PDF] A statistician's perspective on “Mostly Harmless Econometrics: An Empiricist's Companion”, by Joshua D. Angrist and Jörn-Steffen Pischke | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-statistician's-perspective-on-%E2%80%9CMostly-Harmless-An-Gelman/28c52d811da781780406a9de5ba895a0794bdb16"},{"title":"[PDF] Mostly Harmless Econometrics: An Empiricist's Companion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mostly-Harmless-Econometrics:-An-Empiricist's-Angrist-Pischke/a432377e8c4e782ff764701f50f84dca3c10663b"},{"title":"Table 3.3 from Mostly Harmless Econometrics: An Empiricist's Companion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mostly-Harmless-Econometrics:-An-Empiricist's-Angrist-Pischke/a432377e8c4e782ff764701f50f84dca3c10663b/figure/3"},{"title":"Pischke, Jörn-Steffen | Princeton University Press","url":"https://press.princeton.edu/our-authors/pischke-jorn-steffen"},{"title":"Mostly Harmless Econometrics | Princeton University Press","url":"https://press.princeton.edu/books/paperback/9780691120355/mostly-harmless-econometrics"},{"title":"Mostly Harmless Econometrics: An Empiricist’s Companion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mostly-Harmless-Econometrics:-An-Empiricist%E2%80%99s-Harris-Skeels/c0242a689162e9e3994766a1b986638b51834e0d"},{"title":"Angrist, Joshua D. | Princeton University Press","url":"https://press.princeton.edu/our-authors/angrist-joshua-d"},{"title":"Instructor Resources for Mostly Harmless Econometrics","url":"https://press.princeton.edu/instructor-resources/mostly-harmless-econometrics"}]

Based on the search results, here's information about *Mostly Harmless Econometrics: An Empiricist's Companion*:

The book was authored by Joshua David Angrist and Jörn-Steffen Pischke and published in 2008. It 
…[truncated 789 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T06:24:31.247412+00:00_

Web search results for query: "Cohen 1988 Statistical Power Analysis Behavioral Sciences Lawrence Erlbaum"

Links: [{"title":"Scalp Application of LED Therapy to Improve Thinking and Memory in Veterans With Gulf War Illness","url":"https://cdn.clinicaltrials.gov/large-docs/78/NCT01782378/Prot_SAP_000.pdf"},{"title":"Epidermal Coverage of Traumatic Wound Injuries Via Use of Autologous Spray Skin Applied Over Bilayered Wound Matrix","url":"https://cdn.clinicaltrials.gov/large-docs/68/NCT02469168/Prot_SAP_000.pdf"},{"title":"The interrelationships between customer satisfaction, ...","url":"https://pdfs.semanticscholar.org/713a/5f309bce921c1ce4cd93e8f3fde5ed92d77b.pdf"},{"title":"A Comparison of a Currently Marketed Hearing Aid Programmed With Two Different Fitting Methods","url":"https://cdn.clinicaltrials.gov/large-docs/74/NCT03498274/SAP_000.pdf"},{"title":"Statistical Power Analysis for the Behavioral Sciences | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Statistical-Power-Analysis-for-the-Behavioral-Cohen/4d8a5338042da99819746ff835b6f299135e2023"},{"title":"Statistical Inferences Using Effect Sizes in Human Endothelial Function Research","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8654719/"},{"title":"Effect size and statistical power in the rodent fear conditioning literature – A systematic review","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5919667/"},{"title":"Effect size and statistical power in the rodent fear conditioning literature – a systematic review","url":"https://www.biorxiv.org/content/10.1101/116202.full.pdf"},{"title":"Intervening Early With Neglected Children","url":"https://cdn.clinicaltrials.gov/large-docs/52/NCT02093052/Prot_SAP_000.pdf"},{"title":"Bupropion for Depression in ESRD Patients on Hemodialysis","url":"https://cdn.clinicaltrials.gov/large-docs/77/NCT02238977/Prot_SAP_000.pdf"}]

I found the reference you were looking for in the search results. Cohen, J. (1988). Statistical Power Analysis for the Beha
…[truncated 523 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-26T06:24:31.247624+00:00_

Web search results for query: "Synchromesh Reliable Code Generation Retrieving Translating Poesia Polozov Le Tiwari ICLR 2022"

Links: [{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"},{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"dblp: Oleksandr Polozov","url":"https://dblp.org/pid/151/3318.html"},{"title":"[2201.11227v1] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227v1"},{"title":"[2201.11227] Synchromesh: Reliable code generation from pre-trained language models","url":"https://arxiv.org/abs/2201.11227"},{"title":"TYPE-CONSTRAINED CODE GENERATION WITH ...","url":"https://openreview.net/pdf?id=DNAapYMXkc"},{"title":"CodeRL: Mastering Code Generation through Pretrained ...","url":"https://openreview.net/pdf?id=WaGvb7OzySA"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"Automated Code Review Using Large Language Models ...","url":"https://arxiv.org/pdf/2507.18476"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Synchromesh: Reliable Code Generation from Pre-trained Language Models

The paper was authored by Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Christopher Meek, and Sumit Gulwani, and was published at ICLR 2022.

### Overview

The paper addresses the problem that pre-trained language models often violate syntactic and semantic rules of their output language, limiting their practical usability, and proposes Synchromesh as a framework for substantially improving the reliability of pre-trained models for code generation.

### 
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T06:24:31.247832+00:00_

Web search results for query: "AlphaCode 2 Technical Report Google DeepMind 2023"

Links: [{"title":"2023-12-06 AlphaCode 2 Technical Report AlphaCode Team, Google DeepMind","url":"https://deepmind.google/AlphaCode2_Tech_Report.pdf"},{"title":"[PDF] AlphaCode 2 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AlphaCode-2-Technical-Report/67be4a0c75c2b2da3e834eb12b8305050a64a525"},{"title":"2023: A Year of Groundbreaking Advances in AI and Computing — Google DeepMind","url":"https://deepmind.google/blog/2023-a-year-of-groundbreaking-advances-in-ai-and-computing/"},{"title":"TOWARD TRUSTWORTHY DIFFICULTY ASSESSMENTS: LARGE LANGUAGE MODELS AS JUDGES","url":"https://www.arxiv.org/pdf/2511.18597"},{"title":"Competitive programming with AlphaCode — Google DeepMind","url":"https://deepmind.google/blog/competitive-programming-with-alphacode/"},{"title":"Programming with AI: Evaluating ChatGPT, Gemini, AlphaCode,","url":"https://arxiv.org/pdf/2411.09224"}]

I found the AlphaCode 2 Technical Report from Google DeepMind. Here are the key findings:

AlphaCode 2 is a new and enhanced system with massively improved performance, powered by Gemini. AlphaCode 2 relies on the combination of powerful language models and a bespoke search and reranking mechanism.

**Performance Results:**
When evaluated on the same platform as the original AlphaCode, AlphaCode 2 solved 1.7× more problems, and performed better than 85% of competition participants.

**Background:**
AlphaCode was the first AI system to perform at the level of the median competitor in competitive programming, a difficult reasoning task involving advanced maths, logic and computer science.

The technical report was published on December 6, 2023, and provides details about how AlphaCode 2 improves upon the original system through fine-tuning the Gemini Pro model and implementing a sophisticated pipeline involving sampling, clustering, execution, filtering, and reranking mechanisms. The full te
…[truncated 156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T06:24:31.248055+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "REPOEXEC Nam Le Hai authors NAACL 2025 Findings ACL Anthology",
  "allowed_domains": "['aclanthology.org', 'arxiv.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "REPOEXEC Nam Le Hai authors NAACL 2025 Findings ACL Anthology",
    "allowed_domains": "['aclanthology.org', 'arxiv.org', 'openreview.net']"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-26T06:24:31.248211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Predictive Mutation Analysis via Natural Language Channel\" Kim Jeon Hong Yoo IEEE TSE 2024",
  "allowed_domains": "['ieeexplore.ieee.org', 'semanticscholar.org', 'dblp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Predictive Mutation Analysis via Natural Language Channel\" Kim Jeon Hong Yoo IEEE TSE 2024",
    "allowed_domains": "['ieeexplore.ieee.org', 'semanticscholar.org', 'dblp.org']"
  }
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T06:24:31.248344+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Andrews Briand Labiche 2005 ICSE \"Is mutation an appropriate tool\" OR \"Is mutation an adequate substitute\"",
  "allowed_domains": "['semanticscholar.org', 'dblp.org', 'dl.acm.org', 'ieeexplore.ieee.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Andrews Briand Labiche 2005 ICSE \"Is mutation an appropriate tool\" OR \"Is mutation an adequate substitute\"",
    "allowed_domains": "['semanticscholar.org', 'dblp.org', 'dl.acm.org', 'ieeexplore.ieee.org']"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-26T06:24:31.248478+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Synchromesh Poesia Polozov ICLR 2022 exact title \"Reliable code generation from pre-trained language models\"",
  "allowed_domains": "['openreview.net', 'dblp.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Synchromesh Poesia Polozov ICLR 2022 exact title \"Reliable code generation from pre-trained language models\"",
    "allowed_domains": "['openreview.net', 'dblp.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T06:24:31.248608+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Angrist Pischke \"Mostly Harmless Econometrics\" publication year 2008 OR 2009 Princeton",
  "allowed_domains": "['press.princeton.edu', 'semanticscholar.org', 'worldcat.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Angrist Pischke \"Mostly Harmless Econometrics\" publication year 2008 OR 2009 Princeton",
    "allowed_domains": "['press.princeton.edu', 'semanticscholar.org', 'worldcat.org']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T06:24:31.248754+00:00_

Web search results for query: "REPOEXEC Nam Le Hai authors NAACL 2025 Findings ACL Anthology"

Links: [{"title":"Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.123/"},{"title":"Improving Vietnamese-English Cross-Lingual Retrieval for Legal and General Domains - ACL Anthology","url":"https://aclanthology.org/2025.naacl-short.12/"},{"title":"Findings of the Association for Computational Linguistics: NAACL 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-naacl/"},{"title":"Findings of the Association for Computational Linguistics (2025) - ACL Anthology","url":"https://aclanthology.org/events/findings-2025/"},{"title":"Findings of the Association for Computational Linguistics - ACL Anthology","url":"https://aclanthology.org/venues/findings/"},{"title":"MaGiX: A Multi-Granular Adaptive Graph Intelligence Framework for Enhancing Cross-Lingual RAG - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.279/"},{"title":"Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 3: Industry Track) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.naacl-industry/"}]

Based on the search results, I found that Nam Le Hai is one of the authors on the paper "Enhancing Discriminative Representation in Similar Relation Clusters for Few-Shot Continual Relation Extraction" by Le et al., NAACL 2025. However, the search results did not find a paper specifically titled "REPOEXEC" in the NAACL 2025 Findings. 

The search returned several papers featuring Nam Le Hai as an author at NAACL 2025 and other venues, but none matching "REPOEXEC" in the query. If you're looking for a specific REPOEXEC paper in the NAACL 2025 Findings, you may want to search directly on the ACL Anthology or provide additional details ab
…[truncated 117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T06:24:31.248925+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CodeMind Liu Zhang Ibrahimzada Jabbarvand ACL 2024 Findings conference publication",
  "allowed_domains": "['aclanthology.org', 'semanticscholar.org', 'dblp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CodeMind Liu Zhang Ibrahimzada Jabbarvand ACL 2024 Findings conference publication",
    "allowed_domains": "['aclanthology.org', 'semanticscholar.org', 'dblp.org']"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T06:24:31.249053+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lightman \"Let's Verify Step by Step\" ICLR 2024 conference publication",
  "allowed_domains": "['openreview.net', 'dblp.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lightman \"Let's Verify Step by Step\" ICLR 2024 conference publication",
    "allowed_domains": "['openreview.net', 'dblp.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T06:24:31.249204+00:00_

Web search results for query: "Andrews Briand Labiche 2005 ICSE "Is mutation an appropriate tool" OR "Is mutation an adequate substitute""

Links: [{"title":"[PDF] Is mutation an appropriate tool for testing experiments? [software testing] | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Is-mutation-an-appropriate-tool-for-testing-Andrews-Briand/0cb937952b654695e5afdbc86e690894f34605fa"},{"title":"Is mutation an appropriate tool for testing experiments? | Proceedings of the 27th international conference on Software engineering","url":"https://dl.acm.org/doi/10.1145/1062455.1062530"},{"title":"Is mutation an appropriate tool for testing experiments? [software testing] | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/1553583/"},{"title":"[PDF] Stress testing real-time systems with genetic algorithms | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Stress-testing-real-time-systems-with-genetic-Briand-Labiche/29577c14b8f9629ed720412194b1d824d30eec6c"},{"title":"BAP1 Missense Mutation c.2054 A>T (p.E685V) Completely Disrupts Normal Splicing through Creation of a Novel 5’ Splice Site in a Human Mesothelioma Cell Line","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4382119/"},{"title":"Mutation bias shapes the spectrum of adaptive substitutions","url":"https://www.biorxiv.org/content/10.1101/2021.04.14.438663.full.pdf"},{"title":"Tailored Mutants Fit Bugs Better","url":"https://arxiv.org/pdf/1611.02516"}]

I found the paper you're looking for! The paper is "Is mutation an appropriate tool for testing experiments?" by James H. Andrews, Lionel Claude Briand, and Yvan Labiche, published in the Proceedings of the 27th International Conference on Software Engineering (ICSE 2005).

The paper concludes that based on the data available, the use of mutation operators is yielding trustworthy results, with generated mutants being similar to real faults, though mutants appear to be different from hand-seeded 
…[truncated 306 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-26T06:24:31.249386+00:00_

Web search results for query: "Angrist Pischke "Mostly Harmless Econometrics" publication year 2008 OR 2009 Princeton"

Links: [{"title":"Mostly harmless econometrics : an empiricist's companion | WorldCat.org","url":"https://www.worldcat.org/title/mostly-harmless-econometrics-an-empiricists-companion/oclc/231586808?page=citation"},{"title":"[PDF] Mostly Harmless Econometrics: An Empiricist's Companion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mostly-Harmless-Econometrics:-An-Empiricist's-Angrist-Pischke/a432377e8c4e782ff764701f50f84dca3c10663b"},{"title":"Mostly Harmless Econometrics | Princeton University Press","url":"https://press.princeton.edu/books/paperback/9780691120355/mostly-harmless-econometrics"},{"title":"Figure 4.1 from Mostly Harmless Econometrics: An Empiricist's Companion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mostly-Harmless-Econometrics:-An-Empiricist's-Angrist-Pischke/a432377e8c4e782ff764701f50f84dca3c10663b/figure/7"},{"title":"Table 3.3 from Mostly Harmless Econometrics: An Empiricist's Companion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mostly-Harmless-Econometrics:-An-Empiricist's-Angrist-Pischke/a432377e8c4e782ff764701f50f84dca3c10663b/figure/3"},{"title":"Pischke, Jörn-Steffen | Princeton University Press","url":"https://press.princeton.edu/our-authors/pischke-jorn-steffen"},{"title":"[Princeton University Press Econometrics Collection] | Princeton University Press","url":"https://press.princeton.edu/books/econometrics"},{"title":"[PDF] A statistician's perspective on “Mostly Harmless Econometrics: An Empiricist's Companion”, by Joshua D. Angrist and Jörn-Steffen Pischke | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-statistician's-perspective-on-%E2%80%9CMostly-Harmless-An-Gelman/28c52d811da781780406a9de5ba895a0794bdb16"},{"title":"Angrist, Joshua D. | Princeton University Press","url":"https://press.princeton.edu/our-authors/angrist-joshua-d"}]

Ba
…[truncated 285 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T06:24:31.249559+00:00_

Web search results for query: "Synchromesh Poesia Polozov ICLR 2022 exact title "Reliable code generation from pre-trained language models""

Links: [{"title":"[PDF] Synchromesh: Reliable code generation from pre-trained language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Synchromesh:-Reliable-code-generation-from-language-Poesia-Polozov/b62d63580b81a2cbb20c3c1593dd62d118e4cb07"},{"title":"Synchromesh: Reliable Code Generation from Pre-trained Language Models | OpenReview","url":"https://openreview.net/forum?id=KmtVD97J43e"},{"title":"dblp: Oleksandr Polozov","url":"https://dblp.org/pid/151/3318.html"},{"title":"Under review as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=ICSvW69W5K"},{"title":"dblp: Gabriel Poesia","url":"https://dblp.org/pid/150/2695.html"},{"title":"TYPE-CONSTRAINED CODE GENERATION WITH ...","url":"https://openreview.net/pdf?id=LYVyioTwvF"},{"title":"Published as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=ix7rLVHXyY"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=ac93gRzxxV"},{"title":"Automatic Code Generation using Pre-Trained Language Models","url":"https://arxiv.org/pdf/2102.10535"}]

Based on the search results, I found the paper you're looking for:

"Synchromesh: Reliable code generation from pre-trained language models" by Gabriel Poesia, Oleksandr Polozov, Vu Le, Ashish Tiwari, Gustavo Soares, Christopher Meek, and Sumit Gulwani was published at ICLR 2022.

The paper proposes Synchromesh, a framework for substantially improving the reliability of pre-trained models for code generation. The framework comprises two components: Target Similarity Tuning (TST) for semantic example selection, and Constrained Semantic Decoding (CSD) for constraining the output to valid programs in the target language.

The paper is available on OpenReview at https://openreview.net/forum?id=KmtVD97J43e


REMINDER: You MUST include the so
…[truncated 67 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T06:24:31.249732+00:00_

Web search results for query: ""Predictive Mutation Analysis via Natural Language Channel" Kim Jeon Hong Yoo IEEE TSE 2024"

Links: [{"title":"Predictive Mutation Analysis via Natural Language Channel in Source Code","url":"https://arxiv.org/pdf/2104.10865"},{"title":"[PDF] Predictive Mutation Analysis via the Natural Language Channel in Source Code | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Predictive-Mutation-Analysis-via-the-Natural-in-Kim-Jeon/29f44d6f53d383f9251d6b54810bb23277c9445f"},{"title":"Predicting the mutational drivers of future SARS-CoV-2 variants of concern","url":"https://www.medrxiv.org/content/10.1101/2021.06.21.21259286.full.pdf"},{"title":"“Infostery” analysis of short molecular dynamics simulations identifies highly sensitive residues and predicts deleterious mutations","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6208415/"},{"title":"Test Case Level Predictive Mutation Testing Combining PIE and Natural Language Features | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10479449/"}]

Based on the search results, I found information about this research:

The paper "Predictive Mutation Analysis via Natural Language Channel in Source Code" is authored by Jinhan Kim, Juyoung Jeon, Shin Hong, and Shin Yoo. (Note: The search found "Jinhan Kim" and "Shin Yoo" rather than "Kim Jeon Hong Yoo" as listed in your query.)

The paper proposes Seshat, a Predictive Mutation Analysis (PMA) technique that can accurately predict the entire kill matrix. Seshat exploits the natural language channel in code, and learns the relationship between the syntactic and semantic concepts of each test case and the mutants it can kill.

Empirical evaluation using programs in DEFECTS4J shows that Seshat can predict kill matrices with an average F-score of 0.83 for versions that are up to years apart, which is an improvement of F-score by 0.14 and 0.45 points over the state-of-the-art predictive mutation testing
…[truncated 387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T06:24:31.249938+00:00_

Web search results for query: "Lightman "Let's Verify Step by Step" ICLR 2024 conference publication"

Links: [{"title":"Published as a conference paper at ICLR 2024 SELFCHECK:","url":"https://openreview.net/pdf?id=pTHfApDakA"},{"title":"Under review as a conference paper at ICLR 2024","url":"https://openreview.net/pdf?id=lifLHzadgr"},{"title":"Published as a conference paper at COLM 2024","url":"https://openreview.net/pdf?id=stmqBSW2dV"},{"title":"dblp: Let's Verify Step by Step.","url":"https://dblp.org/rec/conf/iclr/LightmanKBEBLLS24.html"},{"title":"dblp: BibTeX records: Ilya Sutskever","url":"https://dblp.org/pid/60/5276.html?view=bibtex"},{"title":"[PDF] Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=ouRX6A8RQJ"},{"title":"Let's Verify Step by Step | OpenReview","url":"https://openreview.net/forum?id=v8L0pN6EOi"},{"title":"Figure 2 from Let's Verify Step by Step | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Verify-Step-by-Step-Lightman-Kosaraju/be8db99310602d66bba64bcf41a572c45816fbfc/figure/2"},{"title":"Under review as a conference paper at ICLR 2024 LET’S REWARD STEP BY STEP:","url":"https://openreview.net/pdf?id=RSQL6xvUYW"}]

Based on the web search results, I found information about the publication you're looking for:

"Let's Verify Step by Step" is a paper by Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, and Karl Cobbe that was published at ICLR 2024.

The paper is available on OpenReview. The work uses step-level human feedback to build a robust verifier of LLM reasoning that achieves 78% accuracy on a subset of the MATH test set. More specifically, the paper finds that process supervision s
…[truncated 220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-26T06:24:31.250103+00:00_

Web search results for query: "CodeMind Liu Zhang Ibrahimzada Jabbarvand ACL 2024 Findings conference publication"

Links: [{"title":"dblp: Reyhaneh Jabbarvand Behrouz","url":"https://dblp.org/pid/18/10505.html"},{"title":"[PDF] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/e3af189157c0c0fe12a77043c09539caf996cde5"},{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/f75673eefe0217464a1d30f6d373e696e26ae055"},{"title":"CodeM: Less Data Yields More Versatility via Ability Matrix - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.40/"},{"title":"Findings of the Association for Computational Linguistics: NAACL 2024 - ACL Anthology","url":"https://aclanthology.org/volumes/2024.findings-naacl/"},{"title":"ACL 2024 The 62nd Annual Meeting of the Association for","url":"https://aclanthology.org/2024.acl-short.0.pdf"}]

Based on the search results, I found information about the CodeMind publication:

CodeMind: A Framework to Challenge Large Language Models for Code Reasoning was authored by Changshu Liu, Shizhuo Dylan Zhang, and Reyhaneh Jabbarvand. However, according to the search results, the paper appears in NAACL-HLT (Findings) 2024, not ACL 2024.

The paper was published on February 15, 2024, and it presents an extensive evaluation of nine LLMs across five benchmarks in two different programming languages, showing that LLMs fairly follow control flow constructs and explain how inputs evolve to output, particularly for simple programs.

Note: The search results show Ali Reza Ibrahimzada is listed as a co-author on some of Jabbarvand's other publications from 2024, but the specific CodeMind paper lists the three authors mentioned above.


REMINDER
…[truncated 92 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-26T06:24:31.250305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org \"On the Impacts of Contexts on Repository-Level Code Generation\" OR \"REPOEXEC\" 2025",
  "allowed_domains": "['aclanthology.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org \"On the Impacts of Contexts on Repository-Level Code Generation\" OR \"REPOEXEC\" 2025",
    "allowed_domains": "['aclanthology.org']"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-26T06:24:31.250441+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jinhan Kim \"Predictive Mutation\" \"Natural Language Channel\" IEEE Transactions Software Engineering Jeon Hong Yoo",
  "allowed_domains": "['ieeexplore.ieee.org', 'dblp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jinhan Kim \"Predictive Mutation\" \"Natural Language Channel\" IEEE Transactions Software Engineering Jeon Hong Yoo",
    "allowed_domains": "['ieeexplore.ieee.org', 'dblp.org']"
  }
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T06:24:31.250565+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dblp Andrews Briand Labiche ICSE 2005 mutation testing title",
  "allowed_domains": "['dblp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dblp Andrews Briand Labiche ICSE 2005 mutation testing title",
    "allowed_domains": "['dblp.org']"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-26T06:24:31.250685+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:aclanthology.org CodeMind \"Framework to Challenge Large Language Models\" Liu Zhang Ibrahimzada",
  "allowed_domains": "['aclanthology.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:aclanthology.org CodeMind \"Framework to Challenge Large Language Models\" Liu Zhang Ibrahimzada",
    "allowed_domains": "['aclanthology.org']"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T06:24:31.250839+00:00_

Web search results for query: "dblp Andrews Briand Labiche ICSE 2005 mutation testing title"

Links: [{"title":"dblp: ICSE 2005","url":"https://dblp.org/db/conf/icse/icse2005.html"},{"title":"dblp: An Analysis and Survey of the Development of Mutation Testing.","url":"https://dblp.org/rec/journals/tse/JiaH11.html"},{"title":"Is the Stack Distance Between Test Case and Method Correlated With Test   Effectiveness?","url":"https://arxiv.org/pdf/1903.05432"},{"title":"Runtime class recompilation during mutation testing","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11720483"},{"title":"Runtime class recompilation during mutation testing","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12430235"},{"title":"dblp: Towards Symbolic Model-Based Mutation Testing: Combining Reachability and Refinement Checking","url":"https://dblp.org/rec/journals/corr/abs-1202-6123.html"},{"title":"dblp: Automating the mutation testing of aspect-oriented Java programs.","url":"https://dblp.org/rec/conf/icse/FerrariNRM10.html"},{"title":"Test Case Generation using Mutation Operators and Fault Classification","url":"https://arxiv.org/pdf/1002.2197"},{"title":"dblp: Efficient Mutation Testing in Configurable Systems.","url":"https://dblp.org/rec/conf/icse/Al-HajjajiKBLS17.html"}]

Based on the search results, the title of the paper by James H. Andrews, Lionel C. Briand, and Yvan Labiche from ICSE 2005 is "Is mutation an appropriate tool for testing experiments?"


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T06:24:31.251003+00:00_

Web search results for query: "Jinhan Kim "Predictive Mutation" "Natural Language Channel" IEEE Transactions Software Engineering Jeon Hong Yoo"

Links: [{"title":"dblp: Jinhan Kim","url":"https://dblp.org/pid/99/6681.html"},{"title":"dblp: Shin Hong","url":"https://dblp.org/pid/28/7539.html"},{"title":"Predictive Mutation Analysis via Natural Language Channel in Source Code","url":"https://arxiv.org/pdf/2104.10865"},{"title":"A predictive language model for SARS-CoV-2 evolution","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11663983/"},{"title":"Predicting the mutational drivers of future SARS-CoV-2 variants of concern","url":"https://www.medrxiv.org/content/10.1101/2021.06.21.21259286.full.pdf"}]

Based on the search results, I found information about the paper you're looking for:

Jinhan Kim, Juyoung Jeon, Shin Hong, Shin Yoo authored "Predictive Mutation Analysis via the Natural Language Channel in Source Code." The paper was published in ACM Transactions on Software Engineering and Methodology, volume 31, issue 4, pages 73:1-73:27 (2022).

Note: The publication is in ACM Transactions on Software Engineering and Methodology, not IEEE Transactions on Software Engineering as mentioned in your query. Additionally, the co-author is "Shin Yoo," not "Jeon Hong Yoo" as listed in your search query.

The paper proposes Seshat, a Predictive Mutation Analysis technique that can accurately predict the entire kill matrix, exploiting the natural language channel in code and learning the relationship between syntactic and semantic concepts of test cases and the mutants they can kill.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T06:24:31.251154+00:00_

Web search results for query: "site:aclanthology.org CodeMind "Framework to Challenge Large Language Models" Liu Zhang Ibrahimzada"

Links: [{"title":"CodeMind: Evaluating Large Language Models for Code Reasoning","url":"https://arxiv.org/pdf/2402.09664"},{"title":"From Effectiveness to Efficiency: Uncovering Linguistic Bias in Large   Language Model-based Code Generation","url":"https://arxiv.org/pdf/2406.00602"},{"title":"Guided Code Generation with LLMs: A Multi-Agent Framework for Complex   Code Tasks","url":"https://arxiv.org/pdf/2501.06625"},{"title":"Towards Advancing Code Generation with Large Language Models: A Research   Roadmap","url":"https://arxiv.org/pdf/2501.11354"},{"title":"Large Language Models Are Highly Vulnerable to Adversarial Hallucination Attacks in Clinical Decision Support: A Multi-Model Assurance Analysis","url":"https://www.medrxiv.org/content/10.1101/2025.03.18.25324184.full.pdf"}]

I found a related paper on CodeMind, but it appears the search didn't return results specifically from aclanthology.org. The first result shows CodeMind is a framework designed to gauge the code reasoning abilities of LLMs through explicit and implicit code reasoning tasks, authored by Changshu Liu, Yang Chen, and Reyhaneh Jabbarvand.

However, the authors in the top result (Liu, Chen, Jabbarvand) don't match exactly the names you specified (Liu, Zhang, Ibrahimzada). The search with the site restriction to aclanthology.org didn't return the specific paper you're looking for. 

This could mean:
1. The paper may not be indexed in the aclanthology.org results
2. The exact title, author names, or other details might be slightly different than specified
3. The paper may be available on arXiv but not yet in the ACL Anthology

Would you like me to try a different search with alternative keywords or author name variations to help locate the specific paper you're looking for?


REMINDER: You MUST include the sources above in your response to the user using markdown hy
…[truncated 9 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-26T06:24:31.251331+00:00_

Web search results for query: "site:aclanthology.org "On the Impacts of Contexts on Repository-Level Code Generation" OR "REPOEXEC" 2025"

Links: [{"title":"On the Impacts of Contexts on Repository-Level Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.82/"},{"title":"On the Impacts of Contexts on Repository-Level Code Generation","url":"https://arxiv.org/pdf/2406.11927"},{"title":"RepoScope: Leveraging Call Chain-Aware Multi-View Context for Repository-Level Code Generation","url":"https://arxiv.org/pdf/2507.14791"},{"title":"Impact-driven Context Filtering For Cross-file Code Completion","url":"https://arxiv.org/pdf/2508.05970"},{"title":"ReCUBE: Evaluating Repository-Level Context Utilization in Code Generation","url":"https://arxiv.org/pdf/2603.25770"}]

I found the paper you're looking for! Here's what the search revealed:

The paper introduces RepoExec, a benchmark for evaluating repository-level code generation, focusing on executability, functional correctness, and dependency utilization. The study evaluates 18 models, revealing that retaining full dependency context yields the best performance, while smaller context sizes can be misleading.

Pretrained LLMs excel in correctness but often reimplement dependencies, while instruction-tuned models better utilize dependencies but sometimes introduce unnecessary complexity. The authors propose an instruction-tuning dataset that improves dependency handling and introduce a new metric, Dependency Invocation Rate (DIR), to measure context utilization. Experiments show that instruction-tuned models improve DIR by over 10%, and multi-round debugging further enhances both correctness and dependency use.

The paper is published in the Findings of the Association for Computational Linguistics: NAACL 2025 and the dataset and source code are available at https://github.com/FSoft-AI4Code/RepoExec.


REMINDER: You MUST include the sources above in your response to the user using markdown h
…[truncated 10 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-26T06:24:31.251554+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "aclanthology.org 2025.findings-naacl.82 \"On the Impacts of Contexts\" authors",
  "allowed_domains": "['aclanthology.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "aclanthology.org 2025.findings-naacl.82 \"On the Impacts of Contexts\" authors",
    "allowed_domains": "['aclanthology.org']"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T06:24:31.251696+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dblp CodeMind \"Framework to Challenge\" Jabbarvand 2024 Findings ACL",
  "allowed_domains": "['dblp.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dblp CodeMind \"Framework to Challenge\" Jabbarvand 2024 Findings ACL",
    "allowed_domains": "['dblp.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T06:24:31.251889+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kim Jeon Hong Yoo \"Predictive Mutation Analysis\" TOSEM 2022 volume 31 authors",
  "allowed_domains": "['dblp.org', 'dl.acm.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kim Jeon Hong Yoo \"Predictive Mutation Analysis\" TOSEM 2022 volume 31 authors",
    "allowed_domains": "['dblp.org', 'dl.acm.org']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-26T06:24:31.252041+00:00_

Web search results for query: "aclanthology.org 2025.findings-naacl.82 "On the Impacts of Contexts" authors"

Links: [{"title":"On the Impacts of Contexts on Repository-Level Code Generation - ACL Anthology","url":"https://aclanthology.org/2025.findings-naacl.82/"},{"title":"NAACL 2025 Annual Conference of the Nations of the Americas Chapter of","url":"https://aclanthology.org/2025.findings-naacl.0.pdf"},{"title":"On the Impacts of Contexts on Repository-Level Code ...","url":"https://aclanthology.org/2025.findings-naacl.82.pdf"},{"title":"*I, We*, and *They*: A Linguistic and Narrative Exploration of the Authorship Process","url":"https://www.biorxiv.org/content/10.1101/2021.06.14.448236.full.pdf"},{"title":"The Impact of Scene Context on Visual Object Recognition: Comparing Humans, Monkeys, and Computational Models","url":"https://www.biorxiv.org/content/10.1101/2024.05.27.596127.full.pdf"}]

Based on the search results, the authors of "On the Impacts of Contexts on Repository-Level Code Generation" (2025.findings-naacl.82) are Nam Le Hai, Dung Manh Nguyen, and Nghi D. Q. Bui.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-26T06:24:31.252195+00:00_

Web search results for query: "Kim Jeon Hong Yoo "Predictive Mutation Analysis" TOSEM 2022 volume 31 authors"

Links: [{"title":"Predictive Mutation Analysis via the Natural Language Channel in Source Code | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3510417"},{"title":"A Comprehensive Study on Large Language Models for Mutation Testing | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3805038"},{"title":"dblp: ACM Transactions on Software Engineering and Methodology, Volume 31","url":"https://dblp.org/db/journals/tosem/tosem31.html"},{"title":"Predictive Mutation Analysis via Natural Language Channel in Source Code","url":"https://arxiv.org/pdf/2104.10865"},{"title":"TOSEM: Vol 31, No 4 - ACM Digital Library","url":"https://dl.acm.org/toc/tosem/2022/31/4"}]

Based on the web search results, I found the information about the "Predictive Mutation Analysis" paper published in TOSEM 2022 volume 31:

The authors are Jinhan Kim, Juyoung Jeon, Shin Hong, and Shin Yoo, and the paper was published in ACM Transactions on Software Engineering and Methodology (TOSEM), Volume 31, Issue 4. The article was published on July 12, 2022.

The full title of the paper is "Predictive Mutation Analysis via the Natural Language Channel in Source Code."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-26T06:24:31.252351+00:00_

Web search results for query: "dblp CodeMind "Framework to Challenge" Jabbarvand 2024 Findings ACL"

Links: [{"title":"dblp: Reyhaneh Jabbarvand Behrouz","url":"https://dblp.org/pid/18/10505.html"},{"title":"[PDF] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/e3af189157c0c0fe12a77043c09539caf996cde5"},{"title":"dblp: NAACL-HLT Findings 2024","url":"https://dblp.org/db/conf/naacl/naacl2024f.html"},{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/f75673eefe0217464a1d30f6d373e696e26ae055"},{"title":"dblp: ACL","url":"https://dblp.org/db/conf/acl/index.html"},{"title":"dblp: EMNLP (Findings) 2024","url":"https://dblp.org/db/conf/emnlp/emnlp2024f.html"},{"title":"CodeMind: Evaluating Large Language Models for Code Reasoning","url":"https://arxiv.org/pdf/2402.09664"}]

Based on the search results, I found information about the CodeMind paper by Jabbarvand and colleagues:

CodeMind: A Framework to Challenge Large Language Models for Code Reasoning was authored by Changshu Liu, Shizhuo Dylan Zhang, and Reyhaneh Jabbarvand, published in 2024.

The framework is designed to gauge the code reasoning abilities of LLMs through explicit and implicit code reasoning tasks: Independent Execution Reasoning (IER), Specification Reasoning (SR) and Dynamic Semantics Reasoning (DSR).

Key findings from the research show that an extensive evaluation of nine LLMs across five benchmarks in two different programming languages using CodeMind shows that LLMs fairly follow control flow constructs and, in general, explain how inputs evolve to output, specifically for simple programs and the ones they can correctly synthesize.

It's worth noting that while your query mentioned ACL, the 
…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T06:24:31.252520+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "dblp.org \"CodeMind\" Jabbarvand 2024 conference proceedings venue",
  "allowed_domains": "['dblp.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "dblp.org \"CodeMind\" Jabbarvand 2024 conference proceedings venue",
    "allowed_domains": "['dblp.org']"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-26T06:24:31.252667+00:00_

Web search results for query: "dblp.org "CodeMind" Jabbarvand 2024 conference proceedings venue"

Links: [{"title":"dblp: Reyhaneh Jabbarvand Behrouz","url":"https://dblp.org/pid/18/10505.html"},{"title":"Evaluating large language models in biomedical data science challenges through a classroom experiment","url":"https://www.biorxiv.org/content/10.1101/2025.07.12.664517.full.pdf"},{"title":"RefDeduR: A text-normalization and decision-tree aided R package enabling accurate and high-throughput reference deduplication for large datasets","url":"https://www.biorxiv.org/content/10.1101/2022.09.29.510210.full.pdf"},{"title":"dblp: Companion Proceedings of the ACM on Web Conference 2024, WWW 2024, Singapore, Singapore, May 13-17, 2024","url":"https://dblp.org/rec/conf/www/2024c.html"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"},{"title":"The Virtual Lab: AI Agents Design New SARS-CoV-2 Nanobodies with Experimental Validation","url":"https://www.biorxiv.org/content/10.1101/2024.11.11.623004.full.pdf"},{"title":"Citation-Grounded Code Comprehension: Preventing LLM Hallucination Through Hybrid Retrieval and Graph-Augmented Context","url":"https://arxiv.org/pdf/2512.12117"},{"title":"Automatic ICD coding using LLMs: a systematic review","url":"https://www.medrxiv.org/content/10.1101/2025.07.30.25330916.full.pdf"},{"title":"dblp: Open Conference Proceedings","url":"https://dblp.org/db/series/ocp/index.html"}]

Based on the search results, CodeMind: A Framework to Challenge Large Language Models for Code Reasoning is authored by Changshu Liu, Shizhuo Dylan Zhang, and Reyhaneh Jabbarvand, and was published on arXiv as CoRR abs/2402.09664 in 2024.

The search results indicate this is a preprint publication rather than a conference proceedings publication. If you need information about whether this 
…[truncated 195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T06:24:31.252859+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2402.09664 CodeMind published venue \"Findings of\" ACL NAACL EMNLP 2024",
  "allowed_domains": "['arxiv.org', 'semanticscholar.org', 'aclanthology.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2402.09664 CodeMind published venue \"Findings of\" ACL NAACL EMNLP 2024",
    "allowed_domains": "['arxiv.org', 'semanticscholar.org', 'aclanthology.org']"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-26T06:24:31.253067+00:00_

Web search results for query: "arxiv 2402.09664 CodeMind published venue "Findings of" ACL NAACL EMNLP 2024"

Links: [{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"https://arxiv.org/html/2402.09664v3"},{"title":"[2402.09664] CodeMind: Evaluating Large Language Models for Code Reasoning","url":"https://arxiv.org/abs/2402.09664"},{"title":"[2402.09664v4] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"https://arxiv.org/abs/2402.09664v4"},{"title":"[2402.09664v1] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"http://arxiv.org/abs/2402.09664v1"},{"title":"CodeMind: Evaluating Large Language Models for Implicit and Explicit Code Execution Reasoning","url":"https://arxiv.org/html/2402.09664"},{"title":"[2402.09664v2] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning","url":"http://arxiv.org/abs/2402.09664v2"}]

The search results show information about the CodeMind paper (arXiv 2402.09664), but they don't contain information about the published venue (such as "Findings of ACL", "Findings of NAACL", "Findings of EMNLP" 2024). Let me search more specifically for the publication venue information.

Links: [{"title":"[2402.09664] CodeMind: Evaluating Large Language Models for Code Reasoning","url":"https://arxiv.org/abs/2402.09664"},{"title":"Findings of the Association for Computational Linguistics (2024) - ACL Anthology","url":"https://aclanthology.org/events/findings-2024/"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2024 - ACL Anthology","url":"https://aclanthology.org/volumes/2024.findings-emnlp/"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.findings-emnlp.0.pdf"},{"title":"The 2024 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2024/"},{"title":"Findin
…[truncated 4477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T06:24:31.253252+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"CodeMind\" \"Findings of\" EMNLP 2024 Jabbarvand Liu Zhang Ibrahimzada",
  "allowed_domains": "['aclanthology.org', 'semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"CodeMind\" \"Findings of\" EMNLP 2024 Jabbarvand Liu Zhang Ibrahimzada",
    "allowed_domains": "['aclanthology.org', 'semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-26T06:24:31.253415+00:00_

Web search results for query: ""CodeMind" "Findings of" EMNLP 2024 Jabbarvand Liu Zhang Ibrahimzada"

Links: [{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/f75673eefe0217464a1d30f6d373e696e26ae055"},{"title":"[PDF] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/e3af189157c0c0fe12a77043c09539caf996cde5"},{"title":"Do Large Language Models Pay Similar Attention Like Human Programmers   When Generating Code?","url":"https://arxiv.org/pdf/2306.01220"},{"title":"Are Decoder-Only Large Language Models the Silver Bullet for Code Search?","url":"https://arxiv.org/pdf/2410.22240"},{"title":"Multiple Large Language Models’ Performance on the Chinese Medical Licensing Examination: Quantitative Comparative Study","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12707437/"},{"title":"Evaluating large language models in biomedical data science challenges through a classroom experiment","url":"https://www.biorxiv.org/content/10.1101/2025.07.12.664517.full.pdf"},{"title":"From Effectiveness to Efficiency: Uncovering Linguistic Bias in Large   Language Model-based Code Generation","url":"https://arxiv.org/pdf/2406.00602"},{"title":"EMNLP 2024 The 2024 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2024.findings-emnlp.0.pdf"}]

Based on the search results, I found information about the CodeMind paper. CodeMind: A Framework to Challenge Large Language Models for Code Reasoning was authored by Changshu Liu, Shizhuo Dylan Zhang, Ali Reza Ibrahimzada, and Reyhaneh Jabbarvand, published in 2024.

An extensive evaluation of nine LLMs across five benchmarks in two different programming languages using CodeMind shows that LLMs fairly follow contro
…[truncated 575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-26T06:24:31.253583+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "semanticscholar.org CodeMind \"Findings of the Association\" 2024 venue Liu Zhang",
  "allowed_domains": "['semanticscholar.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "tool_args": {
    "query": "semanticscholar.org CodeMind \"Findings of the Association\" 2024 venue Liu Zhang",
    "allowed_domains": "['semanticscholar.org']"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-26T06:24:31.253738+00:00_

Web search results for query: "semanticscholar.org CodeMind "Findings of the Association" 2024 venue Liu Zhang"

Links: [{"title":"CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/f75673eefe0217464a1d30f6d373e696e26ae055"},{"title":"[PDF] CodeMind: A Framework to Challenge Large Language Models for Code Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CodeMind:-A-Framework-to-Challenge-Large-Language-Liu-Zhang/e3af189157c0c0fe12a77043c09539caf996cde5"},{"title":"Exploring Young Adults' Mental Health Help‐Seeking Journey: Preliminary Findings on Resource Navigation Behavior | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exploring-Young-Adults'-Mental-Health-Help%E2%80%90Seeking-Liu-Zhang/c2fe0c335c3155a0ef7b0078c8bed4f07ad7eef0"},{"title":"CodeMind: Evaluating Large Language Models for Code Reasoning","url":"https://arxiv.org/pdf/2402.09664"},{"title":"[PDF] DeepDA: LSTM-based Deep Data Association Network for Multi-Targets Tracking in Clutter | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeepDA:-LSTM-based-Deep-Data-Association-Network-in-Liu-Zhang/8ce65f0f08d0633a8f55db1f076c839050c1d210"}]

Based on the search results, I found information about the CodeMind paper on Semantic Scholar. The CodeMind paper was authored by Changshu Liu and Shizhuo Dylan Zhang (along with Ali Reza Ibrahimzada and Reyhaneh Jabbarvand) and published in February 2024.

However, the search results do not contain specific information about it being published as "Findings of the Association" or details about the venue. The results show the paper exists on Semantic Scholar, but the venue/journal information from these particular results shows it was either on arXiv or at a conference, though the exact venue name matching your query is not clearly stated in the retrieved content.

If
…[truncated 282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_ref-audit-batch1_20260526T061956",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-26T06:24:31.254027+00:00_

全部搜索完成，以下是核查报告。

---

## 引用核查报告（第 1 批：11 条）

### 1. `nam2025repoexec` — REPOEXEC
- **bib 中**: author={Nam, Hai and Dau, Thang and Bui, Nhat and Nguyen, Nghi D. Q.}, year={2025}, booktitle={NAACL}, title={REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark}
- **核实结果**: author={Nam Le Hai and Dung Manh Nguyen and Nghi D. Q. Bui}（3 位作者，非 4 位）, year={2025}, venue={Findings of NAACL 2025}, title={On the Impacts of Contexts on Repository-Level Code Generation}（发表版标题已更改）
- **结论**: ⚠️ 有差异
- **差异**:
  - **title**: `REPOEXEC: Evaluate Code Generation with a Repository-Level Executable Benchmark` → 发表版为 `On the Impacts of Contexts on Repository-Level Code Generation`（arXiv v1/v2 用旧标题，v3/camera-ready 已改名）
  - **author**: 4 位→3 位，且姓名拼写有误（`Dau, Thang` → 不存在此作者；`Bui, Nhat` → 应为 `Nghi D. Q. Bui`）。正确作者：Nam Le Hai, Dung Manh Nguyen, Nghi D. Q. Bui
  - **booktitle**: `NAACL` → 应为 `Findings of NAACL 2025`

---

### 2. `liu2024codemind` — CodeMind
- **bib 中**: author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh}, year={2024}, journal={arXiv preprint arXiv:2402.09664}
- **核实结果**: author={Changshu Liu and Shizhuo Dylan Zhang and Ali Reza Ibrahimzada and Reyhaneh Jabbarvand}, year={2024}, venue={arXiv preprint arXiv:2402.09664}
- **结论**: ✅ 正确
- 作者、年份、标题均匹配。未找到正式会议发表记录，arXiv preprint 标注合理。

---

### 3. `xu2025patchreasoner` — Patch Reasoner
- **bib 中**: author={Xu, Junjielong and Tan, Boyin and Liu, Xiaoyuan and Peng, Chao and Gao, Pengfei and He, Pinjia}, year={2025}, journal={arXiv preprint arXiv:2510.22775}
- **核实结果**: 同上，完全匹配
- **结论**: ✅ 正确

---

### 4. `chowdhury2024swebenchverified` — SWE-bench Verified
- **bib 中**: author={Chowdhury, Neil and Aung, James and Shern, Chan Jun and ...}, year={2024}, url={https://openai.com/index/introducing-swe-bench-verified/}
- **核实结果**: 作者列表、年份、URL 均匹配
- **结论**: ✅ 正确

---

### 5. `lightman2023letsverify` — Let's Verify Step by Step
- **bib 中**: author={Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and ...}, year={2023}, journal={arXiv preprint arXiv:2305.20050}
- **核实结果**: author 一致, year={2024}, venue={ICLR 2024}（DBLP 记录：`conf/iclr/LightmanKBEBLLS24`）
- **结论**: ⚠️ 有差异
- **差异**:
  - **year**: `2023` → 应为 `2024`（已正式发表于 ICLR 2024）
  - **venue**: `arXiv preprint` → 应为 `ICLR 2024`

---

### 6. `kim2022predictive` — Predictive Mutation Testing
- **bib 中**: author={Kim, Jinhan and Ju, Juyoung and Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon}, year={2022}, journal={IEEE TSE}, title={Predictive Mutation Testing via Natural Language Channel}
- **核实结果**: author={Kim, Jinhan and Jeon, Juyoung and Hong, Shin and Yoo, Shin}, year={2022}, journal={ACM Transactions on Software Engineering and Methodology}, volume={31}, number={4}, title={Predictive Mutation Analysis via the Natural Language Channel in Source Code}
- **结论**: ⚠️ 严重差异（多字段错误）
- **差异**:
  - **title**: `Predictive Mutation Testing via Natural Language Channel` → `Predictive Mutation Analysis via the Natural Language Channel in Source Code`
  - **author**: `Ju, Juyoung` → `Jeon, Juyoung`；`Tao, Robert and Hu, Nhat-Tan and Baik, Shin Yoo Juyeon`（3 个虚构作者）→ `Hong, Shin and Yoo, Shin`（实际只有 4 位作者）
  - **journal**: `IEEE TSE` → `ACM Transactions on Software Engineering and Methodology (TOSEM)`

---

### 7. `andrews2005mutation` — Is Mutation an Adequate Substitute...
- **bib 中**: author={Andrews, James H and Briand, Lionel C and Labiche, Yvan}, year={2005}, booktitle={ICSE}, title={Is Mutation an Adequate Substitute for Real Faults?}
- **核实结果**: author 一致, year={2005}, booktitle={ICSE 2005}, title={Is Mutation an Appropriate Tool for Testing Experiments?}
- **结论**: ⚠️ 有差异
- **差异**:
  - **title**: `Is Mutation an Adequate Substitute for Real Faults?` → `Is Mutation an Appropriate Tool for Testing Experiments?`（bib 标题疑似与 Just et al. 2014 的 "Are Mutants a Valid Substitute for Real Faults in Software Testing?" 混淆）

---

### 8. `angrist2009mostly` — Mostly Harmless Econometrics
- **bib 中**: author={Angrist, Joshua D. and Pischke, Jörn-Steffen}, year={2009}, publisher={Princeton University Press}
- **核实结果**: 完全匹配（Princeton University Press 官网确认 2009 年出版）
- **结论**: ✅ 正确

---

### 9. `poesia2022synchromesh` — Synchromesh
- **bib 中**: author={Poesia, Gabriel and Polozov, Oleksandr and Le, Vu and Tiwari, Ashish and Soares, Gustavo and Meek, Christopher and Gulwani, Sumit}, year={2022}, booktitle={ICLR}, title={Synchromesh: Reliable Code Generation by Retrieving and Transforming}
- **核实结果**: author 一致, year={2022}, booktitle={ICLR 2022}, title={Synchromesh: Reliable Code Generation from Pre-trained Language Models}
- **结论**: ⚠️ 有差异
- **差异**:
  - **title**: `...by Retrieving and Transforming` → `...from Pre-trained Language Models`（副标题完全不同）

---

### 10. `alphacode2023team` — AlphaCode 2 Technical Report
- **bib 中**: author={AlphaCode Team}, year={2023}, institution={Google DeepMind}
- **核实结果**: 完全匹配
- **结论**: ✅ 正确

---

### 11. `cohen1988` — Statistical Power Analysis
- **bib 中**: author={Cohen, Jacob}, year={1988}, title={Statistical Power Analysis for the Behavioral Sciences}, edition={2nd}, publisher={Lawrence Erlbaum Associates}
- **核实结果**: 完全匹配
- **结论**: ✅ 正确

---

## 汇总

| # | Key | 结论 | 严重程度 |
|---|-----|------|----------|
| 1 | `nam2025repoexec` | ⚠️ 标题/作者/venue 均有误 | 高 |
| 2 | `liu2024codemind` | ✅ 正确 | — |
| 3 | `xu2025patchreasoner` | ✅ 正确 | — |
| 4 | `chowdhury2024swebenchverified` | ✅ 正确 | — |
| 5 | `lightman2023letsverify` | ⚠️ 应更新为 ICLR 2024 | 中 |
| 6 | `kim2022predictive` | ⚠️ 标题/作者/期刊全错 | **极高** |
| 7 | `andrews2005mutation` | ⚠️ 标题错误 | 高 |
| 8 | `angrist2009mostly` | ✅ 正确 | — |
| 9 | `poesia2022synchromesh` | ⚠️ 标题错误 | 高 |
| 10 | `alphacode2023team` | ✅ 正确 | — |
| 11 | `cohen1988` | ✅ 正确 | — |

**5 条正确，6 条有差异**（其中 `kim2022predictive` 最为严重——作者列表含虚构姓名、期刊也标错）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_ref-audit-batch1_20260526T061956"
}
```

</details>

---
