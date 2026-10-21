# paper citation update

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_paper_citation-update_20260521T175241.jsonl`
- **Structured JSON:** [`1be7ed551619e61fe8a3.json`](../../sessions/1b/1be7ed551619e61fe8a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-21T17:54:20.336566+00:00_

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
  "session": "worker_paper_citation-update_20260521T175241",
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

_source line 2 · 2026-05-21T17:54:20.336981+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T17:54:20.337177+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2504.13837 \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2504.13837 \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T17:54:20.337313+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2509.21154 \"GRPO is Secretly a Process Reward Model\" Sullivan 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2509.21154 \"GRPO is Secretly a Process Reward Model\" Sullivan 2025"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T17:54:20.337436+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T17:54:20.337760+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 19401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T17:54:20.337966+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T17:54:20.338138+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
12	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
13	
14	\paragraph{Reward hacking and Goodhart's Law.}
15	Goodhart's Law is established theoretically~\citep{manheim-goodhart-taxonomy, skalse-reward-hacking, karwowski-goodhar
…[truncated 1844 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T17:54:20.338340+00:00_

Web search results for query: "arXiv 2509.21154 "GRPO is Secretly a Process Reward Model" Sullivan 2025"

Links: [{"title":"[2509.21154] GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/abs/2509.21154"},{"title":"Paper page - GRPO is Secretly a Process Reward Model","url":"https://huggingface.co/papers/2509.21154"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan","url":"https://arxiv.org/pdf/2509.21154"},{"title":"Are complicated loss functions necessary for teaching LLMs to reason?","url":"https://arxiv.org/pdf/2603.18756"},{"title":"Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic","url":"https://arxiv.org/pdf/2603.01162"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Hail to the Thief: Exploring Attacks and Defenses in Decentralised GRPO","url":"https://arxiv.org/pdf/2511.09780"}]

Based on the web search results, here's what I found about the arXiv paper 2509.21154:

## Paper Summary

The paper titled "GRPO is Secretly a Process Reward Model" is by Michael Sullivan and 1 other author (the co-author is Alexander Koller).

## Main Contribution

The paper provides theoretical proof that the Group Relative Policy Optimization (GRPO) RL algorithm equipped with an outcome reward model (ORM) is in fact equivalent to a process reward model (PRM)-aware RL objective equipped with a non-trivial, Monte-Carlo-based PRM (given mild assumptions).

## Key Findings

The authors identify a flaw in the GRPO objective that interacts with imbalanced process steps and rewards to hinder both exploration and exploitation (under different conditions).

## Proposed Solution

The authors propose a simple modification to the algorithm to mitigate this defect (λ-GRPO), and show that LLMs tuned with λ-GRPO outperform LLMs tuned with standard GRPO on downstream reasoning tasks and reach peak perform
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T17:54:20.338536+00:00_

Web search results for query: "arXiv 2504.13837 "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model""

Links: [{"title":"[2504.13837v1] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/abs/2504.13837v1"},{"title":"[2504.13837] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/abs/2504.13837"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/does-reinforcement-learning-really-incentivize-reasoning-capacity-in-llms-beyond-the-base-model-b98412ebabee"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250413837Y/abstract"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"Limit of RLVR","url":"https://limit-of-rlvr.github.io/"},{"title":"GitHub - LeapLabTHU/limit-of-RLVR: repo for paper https://arxiv.org/abs/2504.13837 · GitHub","url":"https://github.com/LeapLabTHU/limit-of-RLVR"},{"title":"November 25, 2025 Does Reinforcement Learning Really Incentivize Reasoning","url":"https://arxiv.org/pdf/2504.13837"}]

I found the paper for you. Here's what this research is about:

## Overview

Reinforcement Learning with Verifiable Rewards (RLVR) has recently demonstrated notable success in enhancing the reasoning performance of large language models (LLMs), particularly on mathematics and programming tasks.

## Main Findings

The paper challenges a common assumption about RL training. It is widely believed that RLVR enables LLMs to continuously self-improve, thus acquiring novel reasoning abilities tha
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T17:54:20.338763+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org abs 2504.13837 Yang Yue full author list NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org abs 2504.13837 Yang Yue full author list NeurIPS 2025"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T17:54:20.338917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org abs 2509.21154 Michael Sullivan Alexander Koller GRPO process reward model authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org abs 2509.21154 Michael Sullivan Alexander Koller GRPO process reward model authors"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T17:54:20.339059+00:00_

Web search results for query: "arxiv.org abs 2504.13837 Yang Yue full author list NeurIPS 2025"

Links: [{"title":"[2504.13837] Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?","url":"https://arxiv.org/abs/2504.13837"},{"title":"Artificial Intelligence Apr 2025","url":"https://arxiv.org/list/cs.AI/2025-04?skip=275&show=250"},{"title":"November 25, 2025 Does Reinforcement Learning Really Incentivize Reasoning","url":"https://arxiv.org/pdf/2504.13837"},{"title":"NeurIPS 2025 Best Paper Awards - by David Mataciunas","url":"https://aiconnections.substack.com/p/neurips-2025-best-paper-awards"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"Estimating the Causal Effect of Early ArXiving on Paper Acceptance","url":"https://arxiv.org/pdf/2306.13891"}]

Based on the search results, here is the information about arxiv paper 2504.13837:

**Full Author List:**
Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang

**Title:**
Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

**Conference Status:**
NeurIPS 2025 Oral; ICML 2025 AI4MATH workshop best paper

**Note:** The first author Yang Yue and the sixth author Yang Yue share the same English name but different Chinese names.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T17:54:20.339238+00:00_

Web search results for query: "arxiv.org abs 2509.21154 Michael Sullivan Alexander Koller GRPO process reward model authors"

Links: [{"title":"[2509.21154] GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/abs/2509.21154"},{"title":"GRPO is Secretly a Process Reward Model","url":"https://arxiv.org/html/2509.21154v1"},{"title":"Paper page - GRPO is Secretly a Process Reward Model","url":"https://huggingface.co/papers/2509.21154"},{"title":"GRPO IS SECRETLY A PROCESS REWARD MODEL Michael Sullivan","url":"https://arxiv.org/pdf/2509.21154"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Shaping Explanations: Semantic Reward Modeling with Encoder-Only Transformers for GRPO","url":"https://arxiv.org/pdf/2509.13081"},{"title":"[2509.13081] Shaping Explanations: Semantic Reward Modeling with Encoder-Only Transformers for GRPO","url":"https://arxiv.org/abs/2509.13081"},{"title":"Optimizing Safe and Aligned Language Generation: A Multi-Objective GRPO   Approach","url":"https://arxiv.org/pdf/2503.21819"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** GRPO is Secretly a Process Reward Model

**Authors:** Michael Sullivan and Alexander Koller

**arXiv ID:** 2509.21154

**Main Contribution:** The paper provides theoretical proof that the Group Relative Policy Optimization (GRPO) RL algorithm equipped with an outcome reward model (ORM) is in fact equivalent to a process reward model (PRM)-aware RL objective equipped with a non-trivial, Monte-Carlo-based PRM.

**Key Finding:** The authors identify a flaw in the GRPO objective that interacts with imbalanced process steps and rewards, and propose a simple modification to the algorithm (λ-GRPO) that shows improved performance on downstream reasoning tasks.

The paper was submitted on September 25, 2025, with the latest version (v3) released on February 20, 2
…[truncated 107 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T17:54:20.339441+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
  "old_string": "@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}",
  "new_string": "@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n@inproceedings{yue2025rl-reasoning-limit,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Yang Yue and Shiji Song and Gao Huang},\n  title        = {{Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  note         = {arXiv:2504.13837},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO is Secretly a Process Reward Model}},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
    "old_string": "@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}",
    "new_string": "@article{alphaproof2025,\n  author       = {Thomas Hubert and Rishi Mehta and Laurent Sartran and others},\n  title        = {{Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  doi          = {10.1038/s41586-025-09833-y},\n}\n\n@inproceedings{yue2025rl-reasoning-limit,\n  author       = {Yang Yue and Zhiqi Chen and Rui Lu and Andrew Zhao and Zhaokai Wang and Yang Yue and Shiji Song and Gao Huang},\n  title        = {{Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2025},\n  note         = {arXiv:2504.13837},\n}\n\n@article{sullivan2025grpo-prm,\n  author       = {Michael Sullivan and Alexander Koller},\n  title        = {{GRPO is Secretly a Process Reward Model}},\n  journal      = {arXiv preprint arXiv:2509.21154},\n  year         = {2025},\n  eprint       = {2509.21154},\n  archivePrefix = {arXiv},\n}"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T17:54:20.339658+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T17:54:20.339868+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.",
  "new_string": "Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\n\\citet{sullivan2025grpo-prm} prove that GRPO with outcome rewards is implicitly equivalent to a Monte-Carlo PRM, providing a mechanistic explanation for why component-level gaming emerges: the per-step credit assignment inherent in GRPO concentrates reward on easily satisfiable components."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "old_string": "Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.",
    "new_string": "Symbolic feedback approaches~\\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.\n\\citet{sullivan2025grpo-prm} prove that GRPO with outcome rewards is implicitly equivalent to a Monte-Carlo PRM, providing a mechanistic explanation for why component-level gaming emerges: the per-step credit assignment inherent in GRPO concentrates reward on easily satisfiable components."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T17:54:20.340032+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T17:54:20.340201+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "old_string": "\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.",
  "new_string": "\\citet{yue2025rl-reasoning-limit} demonstrate that RLVR redistributes probability mass toward already-solvable paths rather than eliciting fundamentally new reasoning, consistent with the gaming behaviours we observe where models amplify existing shortcuts instead of acquiring deeper logical structure.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "old_string": "\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe.",
    "new_string": "\\citet{yue2025rl-reasoning-limit} demonstrate that RLVR redistributes probability mass toward already-solvable paths rather than eliciting fundamentally new reasoning, consistent with the gaming behaviours we observe where models amplify existing shortcuts instead of acquiring deeper logical structure.\n\\citet{kwa-catastrophic-goodhart} show that heavy-tailed reward misspecification causes \\emph{catastrophic} Goodhart where KL regularization provably fails, offering a theoretical lens for why GRPO's KL penalty does not prevent the ISR collapse we observe."
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T17:54:20.340364+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T17:54:20.340499+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T17:54:20.340660+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15} evaluate execution accuracy alone, with no diagnostic for structural quality.
6	AlphaProof~\citep{alphaproof2025} applies RL-based formal verification at scale in Lean~4; STA-style diagnostics could probe whether similar structural degeneration occurs in theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}: \citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
12	Symbolic feedback approaches~\citep{rlsf} use solver certificates as token-level rewards, achieving gains on program synthesis; ISR differs in operating at the component level (LOO ablation) rather than the token level, and our results show this structural signal is gamed when optimized.
13	\citet{sullivan2025grpo-prm} prove that GRPO with outcome rewards is implicitly equivalent to a Monte-Carlo PRM, providing a mechanistic explanation for why component-level
…[truncated 2445 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_citation-update_20260521T175241",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-21T17:54:20.340873+00:00_

Done. Summary of changes:

**references.bib** — added two entries:
- `yue2025rl-reasoning-limit`: `@inproceedings` (NeurIPS 2025 Oral)
- `sullivan2025grpo-prm`: `@article` (arXiv preprint)

**related_work.tex** — added two citations:
- Line 13: Sullivan et al. in "Process rewards" paragraph — GRPO implicitly acts as a Monte-Carlo PRM, explaining component-level gaming.
- Line 19: Yue et al. in "Reward hacking" paragraph — RLVR redistributes probability mass rather than eliciting new reasoning, consistent with observed gaming behaviours.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_citation-update_20260521T175241"
}
```

</details>

---
