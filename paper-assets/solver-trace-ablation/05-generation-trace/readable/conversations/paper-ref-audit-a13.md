# paper ref audit a13

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_paper_ref-audit-a13_20260522T234649.jsonl`
- **Structured JSON:** [`45ed479c56cecdae183a.json`](../../sessions/45/45ed479c56cecdae183a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-22T23:49:29.847336+00:00_

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
  "session": "worker_paper_ref-audit-a13_20260522T234649",
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

_source line 2 · 2026-05-22T23:49:29.847654+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T23:49:29.847876+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lanham et al 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\" arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lanham et al 2023 \"Measuring Faithfulness in Chain-of-Thought Reasoning\" arXiv"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T23:49:29.848052+00:00_

Web search results for query: "Lanham et al 2023 "Measuring Faithfulness in Chain-of-Thought Reasoning" arXiv"

Links: [{"title":"[2307.13702] Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2307.13702"},{"title":"Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2402.13950v4"},{"title":"[PDF] Measuring Faithfulness in Chain-of-Thought Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/827afa7dd36e4afbb1a49c735bfbb2c69749756e"},{"title":"Measuring and Improving Faithfulness of Chain-of-Thought ...","url":"https://aclanthology.org/2024.findings-emnlp.882.pdf"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning [Quick Review]","url":"https://liner.com/review/measuring-faithfulness-in-chainofthought-reasoning"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham","url":"https://arxiv.org/pdf/2307.13702"},{"title":"Paper page - Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://huggingface.co/papers/2307.13702"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://www.researchgate.net/publication/372654386_Measuring_Faithfulness_in_Chain-of-Thought_Reasoning"},{"title":"Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps","url":"https://arxiv.org/html/2502.14829v3"}]

I found the paper! Here are the key details:

**"Measuring Faithfulness in Chain-of-Thought Reasoning"** is a paper by Tamera Lanham, Anna Chen, Ansh Radhakrishnan, Benoit Steiner, and 27 other authors, published on arXiv on July 17, 2023.

**Key findings:**

The paper investigates whether the stated reasoning in Chain-of-Thought (CoT) is a faithful explanation of the model's actual reasoning process for answering questions.

The authors investigate hypotheses for how CoT reasoning may be unfaithful by examining how model predictions change when they intervene on the CoT (e.g., b
…[truncated 370 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T23:49:29.848227+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Turpin et al 2023 \"Language Models Don't Always Say What They Think\" unfaithful explanations chain-of-thought arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Turpin et al 2023 \"Language Models Don't Always Say What They Think\" unfaithful explanations chain-of-thought arXiv"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T23:49:29.848406+00:00_

Web search results for query: "Turpin et al 2023 "Language Models Don't Always Say What They Think" unfaithful explanations chain-of-thought arXiv"

Links: [{"title":"[2305.04388v1] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://arxiv.org/abs/2305.04388v1"},{"title":"GitHub - milesaturpin/cot-unfaithfulness · GitHub","url":"https://github.com/milesaturpin/cot-unfaithfulness"},{"title":"[2305.04388] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://arxiv.org/abs/2305.04388"},{"title":"[PDF] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-Don't-Always-Say-What-They-Think:-Turpin-Michael/7dc928f41e15f65f1267bd87b0fcfcc7e715cb56"},{"title":"Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html"},{"title":"Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting - Paper Detail","url":"https://deeplearn.org/arxiv/373995/language-models-don't-always-say-what-they-think:-unfaithful-explanations-in-chain-of-thought-prompting"},{"title":"Language Models Don’t Always Say What They Think:","url":"https://papers.neurips.cc/paper_files/paper/2023/file/ed3fea9033a80fea1376299fa7863f4a-Paper-Conference.pdf"},{"title":"Language models don't always say what they think | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3669397"},{"title":"Language Models Don’t Always Say What They Think:","url":"https://arxiv.org/pdf/2305.04388"},{"title":"Language Models Don't Always Say What They Think: Unfaithful Explan
…[truncated 1580 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T23:49:29.848572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2509.22047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2509.22047"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-22T23:49:29.848743+00:00_

Web search results for query: "arXiv 2509.22047"

Links: [{"title":"Monitoring of COVID-19 Pandemic-related Psychopathology using Machine Learning","url":"https://www.medrxiv.org/content/10.1101/2021.07.13.21259962.full.pdf"},{"title":"The stransverse mass, MT2, in special cases","url":"https://arxiv.org/pdf/1103.5682"},{"title":"Charmless $B$ decay reconstruction in 2019 Belle II data","url":"https://arxiv.org/pdf/2005.13559"},{"title":"Detection of patient metadata in published articles for genomic epidemiology using machine learning and large language models","url":"https://www.medrxiv.org/content/10.1101/2025.04.25.25326298.full.pdf"},{"title":"Large-scale discovery and annotation of hidden substructure patterns in mass spectrometry profiles","url":"https://www.biorxiv.org/content/10.1101/2025.06.19.659491.full.pdf"}]

The search results don't contain information about arXiv paper 2509.22047. The results returned are for various other papers but not the specific arXiv ID you're looking for.

Let me try a more direct search for this paper:

Links: [{"title":"[2509.22047] MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems","url":"https://arxiv.org/abs/2509.22047"},{"title":"Measurement of Groomed Jet Substructure Observables in \\pp Collisions at   $\\sqrt{s} = 200$ GeV with STAR","url":"https://arxiv.org/pdf/2003.02114"},{"title":"Anti-microbial effect of filtered 222nm excimer lamps in a hospital waiting area","url":"https://www.medrxiv.org/content/10.1101/2021.09.03.21263096.full.pdf"},{"title":"Limits on Neutrino Emission from GRB 221009A from MeV to PeV using the   IceCube Neutrino Observatory","url":"https://arxiv.org/pdf/2302.05459"},{"title":"LiteRev, an Automation Tool to Support Literature Reviews: A Case Study on Acute and Early HIV Infection in Sub-Saharan Africa","url":"https://www.medrxiv.org/content/10.1101/2023.02.20.23286179.full.pdf"}]

Based on the search results, arXiv paper 2509.22047 is titled
…[truncated 872 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-22T23:49:29.848903+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.28063"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.28063"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-22T23:49:29.849063+00:00_

Web search results for query: "arXiv 2603.28063"

Links: [{"title":"Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/html/2603.28063"},{"title":"The SARS-CoV-2 Omicron sub-variant BA.2.86 is attenuated in hamsters","url":"https://www.biorxiv.org/content/10.1101/2023.11.10.566576.full.pdf"},{"title":"Immune escape and attenuated severity associated with the SARS-CoV-2 BA.2.86/JN.1 lineage","url":"https://www.medrxiv.org/content/10.1101/2024.04.17.24305964.full.pdf"},{"title":"[2603.28063] Reward Hacking as Equilibrium under Finite Evaluation","url":"https://arxiv.org/abs/2603.28063"},{"title":"Estimating the Causal Effect of Early ArXiving on Paper Acceptance","url":"https://arxiv.org/pdf/2306.13891"},{"title":"Unsupervised cross-domain data augmentation for long-document based prediction and explanation","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12321841"}]

Based on the search results, arXiv 2603.28063 is a paper titled "Reward Hacking as Equilibrium under Finite Evaluation" by Jiacheng Wang and Jinbin Huang, published on March 30, 2026.

The paper proves that under five minimal axioms — multi-dimensional quality, finite evaluation, effective optimization, resource finiteness, and combinatorial interaction — any optimized AI agent will systematically under-invest effort in quality dimensions not covered by its evaluation system. This result establishes reward hacking as a structural equilibrium, not a correctable bug, and holds regardless of the specific alignment method (RLHF, DPO, Constitutional AI, or others) or evaluation architecture employed.

The framework instantiates the multi-task principal-agent model of Holmström and Milgrom (1991) in the AI alignment setting and exploits a structural feature unique to AI systems — the known, differentiable architecture of reward models — to derive a computable distortion index that predicts both the direction and severity of hacking on each quality dimension 
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-22T23:49:29.849225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T23:49:29.849387+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodha
…[truncated 3162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-22T23:49:29.849539+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T23:49:29.849831+00:00_

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
…[truncated 22999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-22T23:49:29.850021+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2307.13702 Lanham \"Measuring Faithfulness\" full author list venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2307.13702 Lanham \"Measuring Faithfulness\" full author list venue"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-22T23:49:29.850175+00:00_

Web search results for query: "arxiv 2307.13702 Lanham "Measuring Faithfulness" full author list venue"

Links: [{"title":"[2307.13702] Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2307.13702"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://www.researchgate.net/publication/372654386_Measuring_Faithfulness_in_Chain-of-Thought_Reasoning"},{"title":"[PDF] Measuring Faithfulness in Chain-of-Thought Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/827afa7dd36e4afbb1a49c735bfbb2c69749756e"},{"title":"Paper page - Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://huggingface.co/papers/2307.13702"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning Tamera Lanham","url":"https://arxiv.org/pdf/2307.13702"},{"title":"Measuring the Faithfulness of Thinking Drafts in Large Reasoning Models","url":"https://arxiv.org/html/2505.13774v2"},{"title":"[2307.13702] Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://ar5iv.labs.arxiv.org/html/2307.13702"},{"title":"Measuring Faithfulness in Chain-of-Thought Reasoning","url":"https://axi.lims.ac.uk/paper/2307.13702"},{"title":"dblp: Measuring Faithfulness in Chain-of-Thought Reasoning.","url":"https://dblp.org/rec/journals/corr/abs-2307-13702.html"}]

Based on the search results, here is the information for arxiv paper 2307.13702:

**Full Author List:** Tamera Lanham, Anna Chen, Ansh Radhakrishnan, Benoit Steiner, Carson Denison, Danny Hernandez, Dustin Li, Esin Durmus, Evan Hubinger, Jackson Kernion, Kamile Lukosiute, Karina Nguyen, Newton Cheng, Nicholas Joseph, Nicholas Schiefer, Oliver Rausch, Robin Larson, Sam McCandlish, Sandipan Kundu, Saurav Kadavath, Shannon Yang, Thomas Henighan, Timothy Maxwell, Timothy Telleen-Lawton, Tristan Hume, Zac Hatfield-Dodds, Jared Kaplan, Jan Brauner, Samuel R. Bowman, Ethan Perez

**Title:** Measuring Faithfulness in Chain-of-Thought Reasoning

**Venue:** Co
…[truncated 203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-22T23:49:29.850326+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2305.04388 Turpin Michael Perez Bowman NeurIPS 2023 full citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2305.04388 Turpin Michael Perez Bowman NeurIPS 2023 full citation"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-22T23:49:29.850481+00:00_

Web search results for query: "arxiv 2305.04388 Turpin Michael Perez Bowman NeurIPS 2023 full citation"

Links: [{"title":"[2305.04388] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://arxiv.org/abs/2305.04388"},{"title":"[2305.04388v1] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://arxiv.org/abs/2305.04388v1"},{"title":"Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://arxiv.org/pdf/2305.04388"},{"title":"Language Models Don’t Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://arxiv.org/html/2305.04388v2"},{"title":"[PDF] Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-Don't-Always-Say-What-They-Think:-Turpin-Michael/7dc928f41e15f65f1267bd87b0fcfcc7e715cb56"},{"title":"(PDF) Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting","url":"https://www.researchgate.net/publication/370605254_Language_Models_Don't_Always_Say_What_They_Think_Unfaithful_Explanations_in_Chain-of-Thought_Prompting"},{"title":"Figure 1 from Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Models-Don't-Always-Say-What-They-Think:-Turpin-Michael/7dc928f41e15f65f1267bd87b0fcfcc7e715cb56/figure/1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?amp=&amp=&amp=&amp=&amp=&amp=&amp=&amp=&author=E.+Perez&author=J.+Michael&author=M.+Turpin&author=S.R.+Bowman&doi=10.48550/arXiv.2305.04388&journal=arXiv&publication_year=2023&title=Language+models+don%E2%80%99t+always+say+what+they+think:+Unfaithful+explanations+in+chain-of-thought+prompting"}]

Based on the sea
…[truncated 571 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-22T23:49:29.850684+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
  "old_string": "@article{nishimura2026specgaming,",
  "new_string": "@article{lanham2023faithfulness,\n  author       = {Tamera Lanham and Anna Chen and Ansh Radhakrishnan and Benoit Steiner and Carson Denison and Danny Hernandez and Dustin Li and Esin Durmus and Evan Hubinger and Jackson Kernion and Kamil{\\.e} Lukosiute and Karina Nguyen and Newton Cheng and Nicholas Joseph and Nicholas Schiefer and Oliver Rausch and Robin Larson and Sam McCandlish and Sandipan Kundu and Saurav Kadavath and Shannon Yang and Thomas Henighan and Timothy Maxwell and Timothy Telleen-Lawton and Tristan Hume and Zac Hatfield-Dodds and Jared Kaplan and Jan Brauner and Samuel R. Bowman and Ethan Perez},\n  title        = {{Measuring Faithfulness in Chain-of-Thought Reasoning}},\n  journal      = {arXiv preprint arXiv:2307.13702},\n  year         = {2023},\n  eprint       = {2307.13702},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{turpin2023unfaithful,\n  author       = {Miles Turpin and Julian Michael and Ethan Perez and Samuel R. Bowman},\n  title        = {{Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n  note         = {arXiv:2305.04388},\n}\n\n@article{nishimura2026specgaming,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib",
    "old_string": "@article{nishimura2026specgaming,",
    "new_string": "@article{lanham2023faithfulness,\n  author       = {Tamera Lanham and Anna Chen and Ansh Radhakrishnan and Benoit Steiner and Carson Denison and Danny Hernandez and Dustin Li and Esin Durmus and Evan Hubinger and Jackson Kernion and Kamil{\\.e} Lukosiute and Karina Nguyen and Newton Cheng and Nicholas Joseph and Nicholas Schiefer and Oliver Rausch and Robin Larson and Sam McCandlish and Sandipan Kundu and Saurav Kadavath and Shannon Yang and Thomas Henighan and Timothy Maxwell and Timothy Telleen-Lawton and Tristan Hume and Zac Hatfield-Dodds and Jared Kaplan and Jan Brauner and Samuel R. Bowman and Ethan Perez},\n  title        = {{Measuring Faithfulness in Chain-of-Thought Reasoning}},\n  journal      = {arXiv preprint arXiv:2307.13702},\n  year         = {2023},\n  eprint       = {2307.13702},\n  archivePrefix = {arXiv},\n}\n\n@inproceedings{turpin2023unfaithful,\n  author       = {Miles Turpin and Julian Michael and Ethan Perez and Samuel R. Bowman},\n  title        = {{Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n  note         = {arXiv:2305.04388},\n}\n\n@article{nishimura2026specgaming,"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T23:49:29.850926+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-22T23:49:29.851071+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
  "old_string": "\t\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n",
  "new_string": "\t\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\nParallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predictions~\\citep{lanham2023faithfulness, turpin2023unfaithful}; STA tests component necessity analogously but operates on solver-input clauses rather than natural-language CoT.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
    "old_string": "\t\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n",
    "new_string": "\t\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\nParallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predictions~\\citep{lanham2023faithfulness, turpin2023unfaithful}; STA tests component necessity analogously but operates on solver-input clauses rather than natural-language CoT.\n"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T23:49:29.851205+00:00_

&lt;tool_use_error>String to replace not found in file.
String: 	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-22T23:49:29.851324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
  "offset": "13",
  "limit": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
    "offset": "13",
    "limit": "3"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T23:49:29.851445+00:00_

13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-22T23:49:29.851583+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
  "old_string": "\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}",
  "new_string": "\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\nParallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predictions~\\citep{lanham2023faithfulness, turpin2023unfaithful}; STA tests component necessity analogously but operates on solver-input clauses rather than natural-language CoT.\n\n\\paragraph{Reward hacking and Goodhart's Law.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex",
    "old_string": "\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\n\n\\paragraph{Reward hacking and Goodhart's Law.}",
    "new_string": "\\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.\nParallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predictions~\\citep{lanham2023faithfulness, turpin2023unfaithful}; STA tests component necessity analogously but operates on solver-input clauses rather than natural-language CoT.\n\n\\paragraph{Reward hacking and Goodhart's Law.}"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T23:49:29.851790+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-22T23:49:29.851980+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib && cp /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "description": "Sync references.bib and related_work.tex to paper/ directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Bash",
  "tool_args": {
    "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib && cp /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "description": "Sync references.bib and related_work.tex to paper/ directory"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T23:49:29.852126+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-22T23:49:29.852269+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib && echo \"references.bib: IDENTICAL\" && diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex && echo \"related_work.tex: IDENTICAL\"",
  "description": "Verify docs/paper and paper/ copies are identical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Bash",
  "tool_args": {
    "command": "diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib && echo \"references.bib: IDENTICAL\" && diff /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex && echo \"related_work.tex: IDENTICAL\"",
    "description": "Verify docs/paper and paper/ copies are identical"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-22T23:49:29.852393+00:00_

references.bib: IDENTICAL
related_work.tex: IDENTICAL

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_ref-audit-a13_20260522T234649",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-22T23:49:29.852553+00:00_

## 结果

### Step 1: 两篇论文已添加

**Lanham et al., 2023**
- 完整引用: Tamera Lanham, Anna Chen, Ansh Radhakrishnan, ... Ethan Perez. "Measuring Faithfulness in Chain-of-Thought Reasoning." arXiv:2307.13702, 2023.
- bib key: `lanham2023faithfulness`
- 已添加到 `references.bib`
- 已在 `related_work.tex` L15 (process rewards 段落末尾) 添加引用

**Turpin et al., 2023**
- 完整引用: Miles Turpin, Julian Michael, Ethan Perez, Samuel R. Bowman. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023. arXiv:2305.04388.
- bib key: `turpin2023unfaithful`
- 已添加到 `references.bib`
- 已在同一句中引用

添加的句子:
> Parallel work on CoT faithfulness finds that stated reasoning steps are often not causally necessary for model predictions (Lanham et al., 2023; Turpin et al., 2023); STA tests component necessity analogously but operates on solver-input clauses rather than natural-language CoT.

### Step 2: arXiv ID 验证

| arXiv ID | 状态 | 标题 |
|----------|------|------|
| 2509.22047 | **存在** | "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems" (Ichihara et al., 2025) |
| 2603.28063 | **存在** | "Reward Hacking as Equilibrium under Finite Evaluation" (Wang & Huang, 2026) |

两个 arXiv ID 均真实存在，等 Director 决定是否添加到 bib。

`docs/paper/` 和 `paper/` 两个目录已同步，diff 验证一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_ref-audit-a13_20260522T234649"
}
```

</details>

---
