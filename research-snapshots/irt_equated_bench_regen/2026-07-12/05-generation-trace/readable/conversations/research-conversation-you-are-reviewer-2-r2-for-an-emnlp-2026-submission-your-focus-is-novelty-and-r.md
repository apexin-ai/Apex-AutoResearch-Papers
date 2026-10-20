# Research conversation: You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. ## Venue calibration E

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a6a3ce6d6529a70ac.jsonl`
- **Structured JSON:** [`a7c13063d12f05a778b1.json`](../../sessions/a7/a7c13063d12f05a778b1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-21T09:49:57.866Z_

You are Reviewer 2 (R2) for an EMNLP 2026 submission. Your focus is **Novelty and Related Work**. 

## Venue calibration
EMNLP 2026 via ARR. Score scale (half-point):
- 5 = Award consideration (top 2.5%)
- 4 = Conference accept (~21% acceptance)
- 3 = Findings accept
- 2 = Major revision, resubmit
- 1 = Do not resubmit

Dimensions: Soundness (1-5), Excitement (1-5), Reproducibility (1-5).

## Paper summary
Title: "Psychometric DIF Analysis Reveals 31% Temporal Instability in MMLU: A Multi-Method Investigation"

The paper applies Mantel-Haenszel DIF analysis to the METABENCH response matrix (5,227 models × 12,508 MMLU items). Key claims:
1. 31.3% of MMLU items show large temporal DIF (ETS Category C) between 2023-2024 cohorts (vs 0.18% random)
2. Existing web-overlap contamination labels cannot validate item-level detectors (enrichment≈0.96)
3. DIF, ConStat, and DVD measure different constructs (pairwise Jaccard ≤ 0.11, ensemble AUROC=0.59)
4. MMLU tolerates instability gracefully (ρ=0.962 at 50% replacement)
5. Cross-benchmark replication on GSM8K (C%=18.9%) with GSM1K validation (r=−0.478)

The paper includes ~13 experiments in 8 pages: primary DIF, RL robustness (N=13), ConStat comparison, DVD generation variance, ensemble fusion, GSM8K/GSM1K replication, bifactor IRT (failed), item generation (below threshold), Bayesian cumulative DIF (simulation-only), graceful degradation, Item-Focused Trees, architecture stratification, semi-synthetic validation.

**Related Work (Section 2):** Three short paragraphs covering: (1) benchmark contamination detection (Min-K%, ConStat, n-gram overlap), (2) DIF in educational measurement (Holland & Thayer, Zumbo, MH, Item-Focused Trees), (3) LLM benchmark evaluation (Polo et al., Miller et al., Growing Pains). Total ~10 references.

**Key numbers to evaluate novelty claims against:**
- MH-DIF is a 1988 method (Holland & Thayer)
- Applying DIF to LLM benchmarks: is this novel application or straightforward transfer?
- The meta-critique about web-overlap labels: enrichment≈0.96 means near-chance association. Is the insight that web-overlap ≠ item-level contamination new?
- Semi-synthetic injection with cross-subject matching: ΔFPR=0.000. Is this a genuine methodological contribution?
- The multi-method comparison (DIF/ConStat/DVD) finding disagreement (Jaccard≤0.11): novel finding or expected given different measurement targets?

**Key concerns for novelty assessment:**
- The ability confounding issue: 31.3% temporal → 2.9% ability-matched. This suggests DIF is mainly detecting that newer models are better, not item instability per se.
- The paper's own results undermine its headline: graceful degradation shows the instability doesn't matter (ρ>0.96), ability matching shows it's mostly capability growth, and the methods disagree on what they're measuring.
- 98% IRT model misfit and failed bifactor convergence: the psychometric framework doesn't fit the data.
- Within-family Llama-2 vs 3 at C%=61.3% — capability jumps produce massive DIF, supporting the "it's just improvement" reading.

## Your task
Write a detailed review focusing on:
1. **Novelty**: Is applying MH-DIF to LLM benchmarks a research contribution or engineering exercise? What is genuinely new here?
2. **Related work completeness**: Only ~10 references. Missing: IRT applications in NLP (e.g., Lalor et al. 2019 who already applied IRT to NLP), LLM evaluation reliability literature, test equating in computerized adaptive testing, benchmark contamination (Yang et al., Golchin & Surdeanu, etc.)
3. **Framing**: The title says "31% Temporal Instability" but the paper's own ability-matching shows this drops to 2.9%. Is the framing misleading?
4. **Contribution clarity**: The paper tries to be a methods paper (semi-synthetic framework), an empirical paper (31% finding), AND a meta-analysis (method comparison). Does it succeed at any of these?
5. **Breadth vs depth**: 13 experiments in 8 pages — catalog vs. contribution?
6. **Negative results**: Bifactor failed, item generation below threshold, ensemble near chance, Bayesian DIF simulation-only. These are reported honestly but collectively suggest the research program hit a wall.

Produce a structured review with:
- Summary (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, with severity: major/minor)
- Questions for authors
- Scores: Soundness, Excitement, Reproducibility, Overall (use the EMNLP scale)
- Confidence (1-5)

Be rigorous. Calibrate to EMNLP acceptance rates (~21% main, ~35% including Findings). The novelty bar for EMNLP is high — applying a textbook psychometric method to a new dataset is typically below the bar unless the insights are genuinely surprising or actionable.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "a81b40f3-51bc-4e4f-a0ae-42d6145d0967",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T09:49:57.870Z_

```json
{
  "parentUuid": "a81b40f3-51bc-4e4f-a0ae-42d6145d0967",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "88153ebb-7b30-4516-bf5a-de70c7b4e38f",
  "timestamp": "2026-05-21T09:49:57.870Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-21T09:50:05.798Z_



I'll start by reading the paper and key supporting files to ground my review in the actual content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88153ebb-7b30-4516-bf5a-de70c7b4e38f",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWHgHktoAm8kDCDCWTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c7293c7-8ae5-4133-a2b7-27f845f00f69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQk3w6BjemkLCAzkvMQ6vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7681,
      "cache_read_input_tokens": 8725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T09:50:06.731Z_

<details open><summary>🔧 Tool call — Read · `toolu_012VWvf4voUYY4qx8C697a7T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c7293c7-8ae5-4133-a2b7-27f845f00f69",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWHgHktoAm8kDCDCWTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1a06025-c608-4bfb-9320-d4c5d4df334c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQk3w6BjemkLCAzkvMQ6vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7681,
      "cache_read_input_tokens": 8725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T09:50:06.744Z_

<details><summary>↩ Tool result · `toolu_012VWvf4voUYY4qx8C697a7T`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage[T1]{fontenc}
7	\usepackage[utf8]{inputenc}
8	\usepackage{microtype}
9	\usepackage{booktabs}
10	\usepackage{graphicx}
11	\usepackage{xcolor}
12	\usepackage{multirow}
13	\usepackage{subcaption}
14	
15	\input{math_commands.tex}
16	
17	\usepackage{cleveref}
18	
19	\graphicspath{{../figures/paper/}}
20	
21	\title{Psychometric Instability of LLM Benchmarks:\\Differential Item Functioning Reveals 31\% of MMLU Items\\Behave Differently Across Model Generations}
22	
23	\begin{document}
24	
25	\maketitle
26	
27	\input{sections/abstract}
28	\input{sections/introduction}
29	\input{sections/related_work}
30	\input{sections/method}
31	\input{sections/experiments}
32	\input{sections/discussion}
33	\input{sections/conclusion}
34	\input{sections/limitations}
35	
36	\bibliography{references}
37	
38	\appendix
39	\input{sections/appendix}
40	
41	\end{document}
42	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1a06025-c608-4bfb-9320-d4c5d4df334c",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "3dd8a18b-319d-4b38-8937-e2702bc04bd3",
  "sourceToolAssistantUUID": "f1a06025-c608-4bfb-9320-d4c5d4df334c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-21T09:50:07.330Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BqrQwVFBsu7HoNFNkz1Fru`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.bbl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd8a18b-319d-4b38-8937-e2702bc04bd3",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWHgHktoAm8kDCDCWTk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d87d5b35-c09a-4718-a293-800093093a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DQk3w6BjemkLCAzkvMQ6vv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7681,
      "cache_read_input_tokens": 8725,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7681,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-21T09:50:07.338Z_

<details><summary>↩ Tool result · `toolu_01BqrQwVFBsu7HoNFNkz1Fru`</summary>

```text
1	\begin{thebibliography}{40}
2	\providecommand{\natexlab}[1]{#1}
3	
4	\bibitem[{Balloccu et~al.(2024)Balloccu, Schmidtova, Lango, and
5	  Dusek}]{balloccu2024leak}
6	Simone Balloccu, Patrícia Schmidtova, Mateusz Lango, and Ondrej Dusek. 2024.
7	\newblock \href {https://doi.org/10.18653/v1/2024.eacl-long.5} {Leak, cheat,
8	  repeat: Data contamination and evaluation malpractices in closed-source
9	  {LLMs}}.
10	\newblock In \emph{Proceedings of the 18th Conference of the European Chapter
11	  of the Association for Computational Linguistics (EACL)}.
12	
13	\bibitem[{Belzak(2020)}]{belzak2020smallsample}
14	William Belzak. 2020.
15	\newblock \href {https://doi.org/10.1080/00273171.2019.1671162} {Testing
16	  differential item functioning in small samples}.
17	\newblock \emph{Multivariate Behavioral Research}.
18	
19	\bibitem[{Burnell et~al.(2023)Burnell, Schellaert, Burden, Ullman,
20	  Martinez-Plumed, Tenenbaum, Rutar, Cheke, Sohl-Dickstein, Mitchell, Kiela,
21	  Shanahan, Voorhees, Cohn, Leibo, and Hernandez-Orallo}]{burnell2023rethink}
22	Ryan Burnell, Wout Schellaert, John Burden, Tomer~D. Ullman, Fernando
23	  Martinez-Plumed, Joshua~B. Tenenbaum, Danaja Rutar, Lucy~G. Cheke, Jascha
24	  Sohl-Dickstein, Melanie Mitchell, Douwe Kiela, Murray Shanahan, Ellen~M.
25	  Voorhees, Anthony~G. Cohn, Joel~Z. Leibo, and Jose Hernandez-Orallo. 2023.
26	\newblock \href {https://doi.org/10.1126/science.adf6369} {Rethink reporting of
27	  evaluation results in {AI}}.
28	\newblock \emph{Science}.
29	
30	\bibitem[{Carlini et~al.(2023)Carlini, Ippolito, Jagielski, Lee, Tram{\`e}r,
31	  and Zhang}]{carlini2022quantifying}
32	Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian
33	  Tram{\`e}r, and Chiyuan Zhang. 2023.
34	\newblock \href {https://arxiv.org/abs/2202.07646} {Quantifying memorization
35	  across neural language models}.
36	\newblock In \emph{International Conference on Learning Representations
37	  (ICLR)}.
38	
39	\bibitem[{Chang et~al.(2024)Chang, Wang, Wang, Wu, Zhu, Chen, Yang, Yi, Wang,
40	  Wang, Ye, Zhang, Chang, Yu, Yang, and Xie}]{chang2024survey}
41	Yupeng Chang, Xu~Wang, Jindong Wang, Yuan Wu, Kaijie Zhu, Hao Chen, Linyi Yang,
42	  Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi~Chang,
43	  Philip~S. Yu, Qiang Yang, and Xing Xie. 2024.
44	\newblock \href {https://doi.org/10.1145/3641289} {A survey on evaluation of
45	  large language models}.
46	\newblock \emph{ACM Transactions on Intelligent Systems and Technology}.
47	
48	\bibitem[{Chiang et~al.(2024)Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhang,
49	  Zhu, Jordan, Gonzalez, and Stoica}]{chiang2024chatbot}
50	Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios~N. Angelopoulos, Tianle
51	  Li, Dacheng Li, Hao Zhang, Banghua Zhu, Michael~I. Jordan, Joseph~E.
52	  Gonzalez, and Ion Stoica. 2024.
53	\newblock \href {https://doi.org/10.48550/arXiv.2403.04132} {Chatbot arena: An
54	  open platform for evaluating {LLMs} by human preference}.
55	\newblock In \emph{Proceedings of the International Conference on Machine
56	  Learning (ICML)}.
57	
58	\bibitem[{Clauser and Mazor(1998)}]{clauser1998dif}
59	Brian~E. Clauser and Kathleen~M. Mazor. 1998.
60	\newblock \href {https://doi.org/10.1111/j.1745-3992.1998.tb00619.x} {Using
61	  statistical procedures to identify differentially functioning test items}.
62	\newblock \emph{Educational Measurement: Issues and Practice}.
63	
64	\bibitem[{Dekoninck et~al.(2024)Dekoninck, Mueller, and
65	  Vechev}]{dekoninck2024constat}
66	Jasper Dekoninck, Mark~Niklas Mueller, and Martin Vechev. 2024.
67	\newblock \href {https://arxiv.org/abs/2405.16281} {{ConStat}:
68	  Performance-based contamination detection in large language models}.
69	\newblock In \emph{Advances in Neural Information Processing Systems
70	  (NeurIPS)}.
71	
72	\bibitem[{Golchin and Surdeanu(2024)}]{golchin2024timetravel}
73	Shahriar Golchin and Mihai Surdeanu. 2024.
74	\newblock \href {https://arxiv.org/abs/2308.08493} {Time travel in {LLMs}:
75	  Tracing data contamination in large language models}.
76	\newblock In \emph{Proceedings of the International Conference on Learning
77	  Representations (ICLR)}.
78	
79	\bibitem[{Habba et~al.(2026)Habba, Itzhak, Yehudai, Perlitz, Bandel,
80	  Shmueli-Scheuer, Choshen, and Stanovsky}]{habba2026growingpains}
81	Eitam Habba, Ido Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal
82	  Shmueli-Scheuer, Leshem Choshen, and Gabriel Stanovsky. 2026.
83	\newblock \href {https://arxiv.org/abs/2604.12843} {Growing pains: Extensible
84	  and efficient {LLM} benchmarking via fixed parameter calibration}.
85	\newblock \emph{Preprint}, arXiv:2604.12843.
86	
87	\bibitem[{Hendrycks et~al.(2021)Hendrycks, Burns, Basart, Zou, Mazeika, Song,
88	  and Steinhardt}]{hendrycks2021mmlu}
89	Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn
90	  Song, and Jacob Steinhardt. 2021.
91	\newblock \href {https://arxiv.org/abs/2009.03300} {Measuring massive multitask
92	  language understanding}.
93	\newblock In \emph{Proceedings of the International Conference on Learning
94	  Representations (ICLR)}.
95	
96	\bibitem[{Holland and Thayer(1988)}]{holland1988mh}
97	Paul~W. Holland and Dorothy~T. Thayer. 1988.
98	\newblock \href {https://doi.org/10.1002/j.2330-8516.1986.tb00186.x}
99	  {Differential item functioning and the {Mantel-Haenszel} procedure}.
100	\newblock In Howard Wainer and Henry~I. Braun, editors, \emph{Test Validity}.
101	  Lawrence Erlbaum Associates.
102	
103	\bibitem[{Kiela et~al.(2021)Kiela, Bartolo, Nie, Kaushik, Geiger, Wu, Vidgen,
104	  Prasad, Singh, Ringshia, Ma, Thrush, Riedel, Talat, Stenetorp, and
105	  Jia}]{kiela2021dynabench}
106	Douwe Kiela, Max Bartolo, Yixin Nie, Divyansh Kaushik, Atticus Geiger,
107	  Zhengxuan Wu, Bertie Vidgen, Grusha Prasad, Amanpreet Singh, Pratik Ringshia,
108	  Zhiyi Ma, Tristan Thrush, Sebastian Riedel, Zeerak Talat, Pontus Stenetorp,
109	  and Robin Jia. 2021.
110	\newblock \href {https://doi.org/10.18653/v1/2021.naacl-main.324} {{Dynabench}:
111	  Rethinking benchmarking in {NLP}}.
112	\newblock In \emph{Proceedings of the 2021 Conference of the North American
113	  Chapter of the Association for Computational Linguistics (NAACL)}.
114	
115	\bibitem[{Kim and Kolen(2019)}]{kim2019fpc}
116	Seonghoon Kim and Michael Kolen. 2019.
117	\newblock \href {https://doi.org/10.1080/08957347.2019.1660344} {Application of
118	  {IRT} fixed parameter calibration to multiple-group test data}.
119	\newblock \emph{Applied Measurement in Education}.
120	
121	\bibitem[{Kipnis et~al.(2024)Kipnis, Voudouris, Schulze~Buschoff, and
122	  Schulz}]{kipnis2024metabench}
123	Alon Kipnis, Konstantinos Voudouris, Luca~Maria Schulze~Buschoff, and Eric
124	  Schulz. 2024.
125	\newblock \href {https://arxiv.org/abs/2407.12844} {metabench -- a sparse
126	  benchmark of reasoning and knowledge in large language models}.
127	\newblock \emph{Preprint}, arXiv:2407.12844.
128	
129	\bibitem[{Lalor et~al.(2019)Lalor, Wu, and Yu}]{lalor2019irt}
130	John Lalor, Hao Wu, and Hong Yu. 2019.
131	\newblock \href {https://doi.org/10.18653/v1/D19-1434} {Learning latent
132	  parameters without human response patterns: Item response theory with
133	  artificial crowds}.
134	\newblock In \emph{Proceedings of the 2019 Conference on Empirical Methods in
135	  Natural Language Processing and the 9th International Joint Conference on
136	  Natural Language Processing (EMNLP-IJCNLP)}.
137	
138	\bibitem[{Li et~al.(2024{\natexlab{a}})Li, Guerin, and Lin}]{li2024latesteval}
139	Yucheng Li, Frank Guerin, and Chenghua Lin. 2024{\natexlab{a}}.
140	\newblock \href {https://doi.org/10.48550/arXiv.2312.12343} {{LatestEval}:
141	  Addressing data contamination in language model evaluation through dynamic
142	  and time-sensitive test construction}.
143	\newblock In \emph{Proceedings of the AAAI Conference on Artificial
144	  Intelligence (AAAI)}.
145	
146	\bibitem[{Li et~al.(2024{\natexlab{b}})Li, Guo, Guerin, and
147	  Lin}]{li2024contamination}
148	Yucheng Li, Yunhao Guo, Frank Guerin, and Chenghua Lin. 2024{\natexlab{b}}.
149	\newblock \href {https://doi.org/10.18653/v1/2024.findings-emnlp.30} {An
150	  open-source data contamination report for large language models}.
151	\newblock In \emph{Findings of the Association for Computational Linguistics:
152	  EMNLP 2024}.
153	
154	\bibitem[{Liang(2026)}]{liang2026dvd}
155	Rongzhen Liang. 2026.
156	\newblock \href {https://arxiv.org/abs/2601.04895} {{DVD}: Detection via
157	  variance of generation distribution for variant contamination}.
158	\newblock \emph{Preprint}, arXiv:2601.04895.
159	
160	\bibitem[{Lord(1980)}]{lord1980irt}
161	Frederic~M. Lord. 1980.
162	\newblock \emph{Applications of Item Response Theory to Practical Testing
163	  Problems}.
164	\newblock Lawrence Erlbaum Associates, Hillsdale, NJ.
165	
166	\bibitem[{Maia~Polo et~al.(2024)Maia~Polo, Weber, Choshen, Sun, Xu, and
167	  Yurochkin}]{maiapolo2024tinybenchmarks}
168	Felipe Maia~Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and
169	  Mikhail Yurochkin. 2024.
170	\newblock \href {https://proceedings.mlr.press/v235/maia-polo24a.html}
171	  {{tinyBenchmarks}: evaluating {LLMs} with fewer examples}.
172	\newblock In \emph{Proceedings of the International Conference on Machine
173	  Learning (ICML)}.
174	
175	\bibitem[{Meredith(1993)}]{meredith1993invariance}
176	William Meredith. 1993.
177	\newblock \href {https://doi.org/10.1007/BF02294825} {Measurement invariance,
178	  factor analysis and factorial invariance}.
179	\newblock \emph{Psychometrika}.
180	
181	\bibitem[{Muth{\'e}n(1985)}]{muthen1985mimic}
182	Bengt Muth{\'e}n. 1985.
183	\newblock \href {https://doi.org/10.2307/1164966} {A method for studying the
184	  homogeneity of test items with respect to other relevant variables}.
185	\newblock \emph{Journal of Educational Statistics}.
186	
187	\bibitem[{Nandakumar(1993)}]{nandakumar1993dif}
188	Ratna Nandakumar. 1993.
189	\newblock Simultaneous {DIF} amplification and cancellation: {Shealy}-{Stout}'s
190	  test for {DIF}.
191	\newblock \emph{Journal of Educational Measurement}, 30(4):293--311.
192	
193	\bibitem[{Raju(1988)}]{raju1988area}
194	Nambury~S. Raju. 1988.
195	\newblock \href {https://doi.org/10.1007/BF02294403} {The area between two item
196	  characteristic curves}.
197	\newblock \emph{Psychometrika}.
198	
199	\bibitem[{Shealy and Stout(1993)}]{shealy1993sibtest}
200	Robin Shealy and William Stout. 1993.
201	\newblock \href {https://doi.org/10.1007/BF02294572} {A model-based
202	  standardization approach that separates true bias/{DIF} from group ability
203	  differences and detects test bias/{DTF} as well as item bias/{DIF}}.
204	\newblock \emph{Psychometrika}.
205	
206	\bibitem[{Shi et~al.(2024)Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, and
207	  Zettlemoyer}]{shi2024mink}
208	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra
209	  Blevins, Danqi Chen, and Luke Zettlemoyer. 2024.
210	\newblock \href {https://arxiv.org/abs/2310.16789} {Detecting pretraining data
211	  from large language models}.
212	\newblock In \emph{Proceedings of the International Conference on Learning
213	  Representations (ICLR)}.
214	
215	\bibitem[{Swaminathan and Rogers(1990)}]{swaminathan1990logistic}
216	Hariharan Swaminathan and H.~Jane Rogers. 1990.
217	\newblock \href {https://doi.org/10.1111/j.1745-3984.1990.tb00754.x} {Detecting
218	  differential item functioning using logistic regression procedures}.
219	\newblock \emph{Journal of Educational Measurement}.
220	
221	\bibitem[{Tao(2026)}]{tao2026selfcritique}
222	Yixin Tao. 2026.
223	\newblock \href {https://arxiv.org/abs/2510.09259} {Detecting data
224	  contamination from reinforcement learning post-training for large language
225	  models}.
226	\newblock In \emph{Proceedings of the International Conference on Learning
227	  Representations (ICLR)}.
228	
229	\bibitem[{Teresi and Fleishman(2007)}]{teresi2007dif}
230	Jeanne~A. Teresi and John~A. Fleishman. 2007.
231	\newblock \href {https://doi.org/10.1007/s11136-007-9184-6} {Differential item
232	  functioning and health assessment}.
233	\newblock \emph{Quality of Life Research}.
234	
235	\bibitem[{Tirumala et~al.(2022)Tirumala, Markosyan, Zettlemoyer, and
236	  Aghajanyan}]{tirumala2022memorization}
237	Kushal Tirumala, Aram Markosyan, Luke Zettlemoyer, and Armen Aghajanyan. 2022.
238	\newblock \href {https://arxiv.org/abs/2205.10770} {Memorization without
239	  overfitting: Analyzing the training dynamics of large language models}.
240	\newblock In \emph{Advances in Neural Information Processing Systems
241	  (NeurIPS)}.
242	
243	\bibitem[{Vandenberg and Lance(2000)}]{vandenberg2000invariance}
244	Robert~J. Vandenberg and Charles~E. Lance. 2000.
245	\newblock \href {https://doi.org/10.1177/109442810031002} {A review and
246	  synthesis of the measurement invariance literature: Suggestions, practices,
247	  and recommendations for organizational research}.
248	\newblock \emph{Organizational Research Methods}.
249	
250	\bibitem[{Vania et~al.(2021)Vania, Htut, Huang, Mungra, Pang, Phang, Liu, Cho,
251	  and Bowman}]{vania2021irt}
252	Clara Vania, Phu~Mon Htut, William Huang, Dhara Mungra, Richard~Yuanzhe Pang,
253	  Jason Phang, Haokun Liu, Kyunghyun Cho, and Samuel~R. Bowman. 2021.
254	\newblock \href {https://doi.org/10.18653/v1/2021.acl-long.92} {Comparing test
255	  sets with item response theory}.
256	\newblock In \emph{Proceedings of the 59th Annual Meeting of the Association
257	  for Computational Linguistics (ACL)}.
258	
259	\bibitem[{Wang et~al.(2026)Wang, Li, Ko, and Zhang}]{wang2026fragility}
260	Haonan Wang, Haoyang Li, Boeun Ko, and Hongyang Zhang. 2026.
261	\newblock \href {https://arxiv.org/abs/2510.02386} {On the fragility of
262	  benchmark contamination detection in reasoning models}.
263	\newblock In \emph{Proceedings of the International Conference on Learning
264	  Representations (ICLR)}.
265	
266	\bibitem[{White(2025)}]{white2025livebench}
267	Colin White. 2025.
268	\newblock \href {https://doi.org/10.48550/arXiv.2406.19314} {{LiveBench}: A
269	  challenging, contamination-free {LLM} benchmark}.
270	\newblock In \emph{Proceedings of the International Conference on Learning
271	  Representations (ICLR)}.
272	
273	\bibitem[{Woods(2009)}]{woods2009mimic}
274	Carol~M. Woods. 2009.
275	\newblock \href {https://doi.org/10.1177/0146621609331279} {Empirical selection
276	  of anchors for tests of differential item functioning}.
277	\newblock \emph{Applied Psychological Measurement}.
278	
279	\bibitem[{Zhang(2024)}]{zhang2024gsm1k}
280	Hugh Zhang. 2024.
281	\newblock \href {https://arxiv.org/abs/2405.00332} {A careful examination of
282	  large language model performance on grade school arithmetic}.
283	\newblock \emph{Preprint}, arXiv:2405.00332.
284	
285	\bibitem[{Zhang et~al.(2024)Zhang, Sun, Yeats, Ouyang, Kuo, Zhang, Yang, and
286	  Li}]{zhang2024minkpp}
287	Jingyang Zhang, Jingwei Sun, Eric Yeats, Yang Ouyang, Martin Kuo, Jianyi Zhang,
288	  Hao Yang, and Hai Li. 2024.
289	\newblock \href {https://arxiv.org/abs/2404.02936} {{Min-K\%++}: Improved
290	  baseline for detecting pre-training data from large language models}.
291	\newblock \emph{Preprint}, arXiv:2404.02936.
292	
293	\bibitem[{Zhou et~al.(2026)Zhou, Huang, Zhao, Han, Wang, Chen, Yang, Bao, Dong,
294	  Xu, Zhu, Cao, and Zhao}]{zhou2026psnirt}
295	Hao Zhou, Heng Huang, Zhenheng Zhao, Lin Han, Haoyu Wang, Ke~Chen, Min Yang,
296	  Weidong Bao, Ji~Dong, Bo~Xu, Changshui Zhu, Huijun Cao, and Tiejun Zhao.
297	  2026.
298	\newblock \href {https://arxiv.org/abs/2505.15055} {Lost in benchmarks?
299	  rethinking large language model benchmarking with item response theory}.
300	\newblock In \emph{Proceedings of the AAAI Conference on Artificial
301	  Intelligence (AAAI)}.
302	
303	\bibitem[{Zumbo(1999)}]{zumbo1999handbook}
304	Bruno~D. Zumbo. 1999.
305	\newblock \href {https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf} {\emph{A
306	  Handbook on the Theory and Methods of Differential Item Functioning ({DIF}):
307	  Logistic Regression Modeling as a Unitary Framework for Binary and
308	  {Likert}-Type (Ordinal) Item Scores}}.
309	\newblock Directorate of Human Resources Research and Evaluation, Department of
310	  National Defense, Ottawa.
311	
312	\end{thebibliography}
313	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d87d5b35-c09a-4718-a293-800093093a3e",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "736efaac-0a57-433f-9e90-d8372d09d4f2",
  "sourceToolAssistantUUID": "d87d5b35-c09a-4718-a293-800093093a3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T09:50:11.951Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VD5Lt8KG3TApfeiZN9P2Kn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "736efaac-0a57-433f-9e90-d8372d09d4f2",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJNxjrAesXKAiqjrdr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cad2804f-e399-4343-b6c8-cff80f9de0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTdoPbfX7pFkhTNsw3WdNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8036,
      "cache_read_input_tokens": 16406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T09:50:11.957Z_

<details><summary>↩ Tool result · `toolu_01VD5Lt8KG3TApfeiZN9P2Kn`</summary>

```text
1	\begin{abstract}
2	LLM benchmark scores are routinely compared across model generations, yet the assumption that individual items measure the same construct over time is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (DIF) analysis with ETS severity classification to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), and find that 31\% of items exhibit large DIF (ETS Category~C) between 2023 and 2024 model cohorts. This instability does not threaten benchmark validity: Spearman rank correlation between full and stable-item rankings is $\rho \approx 0.997$. Rather, it reveals which capability dimensions shift across model generations. Item-level decomposition shows that domain accuracy improvement explains only 2.4 percentage points (7.6\%) of the instability; 92.4\% is item-specific. We expose a validation methodology gap in the contamination detection literature: web-overlap labels measure global exposure, not differential functioning. Direct comparison confirms near-independence (enrichment $\approx 0.96$). A semi-synthetic injection framework with cross-subject matching preserves detection power ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$) with zero false positive inflation; cross-benchmark replication on GSM8K confirms generality. DIF-flagged items concentrate cross-generational discriminative information; an exploratory analysis ($N = 33$) finds they anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$), suggesting that DIF captures genuine capability change rather than memorization. LLM benchmarks need psychometric monitoring, not just score reporting.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cad2804f-e399-4343-b6c8-cff80f9de0d8",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "a5773f98-e549-4658-b8e4-817952bf1cd2",
  "sourceToolAssistantUUID": "cad2804f-e399-4343-b6c8-cff80f9de0d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T09:50:12.405Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JJcusS7rDu4N9d8XDz7CFE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5773f98-e549-4658-b8e4-817952bf1cd2",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJNxjrAesXKAiqjrdr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "efad4537-2169-4410-b008-5c2e9520ad0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTdoPbfX7pFkhTNsw3WdNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8036,
      "cache_read_input_tokens": 16406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T09:50:12.412Z_

<details><summary>↩ Tool result · `toolu_01JJcusS7rDu4N9d8XDz7CFE`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When we say ``Model B outperforms Model A on MMLU,'' we implicitly assume that the benchmark measures the same construct in the same way for both models. This assumption of temporal comparability underpins every cross-generation comparison published on leaderboards and in model reports, yet it is rarely tested. We apply Mantel-Haenszel Differential Item Functioning (MH-DIF) analysis~\citep{holland1988mh} with Educational Testing Service (ETS) severity classification to the METABENCH response matrix~\citep{kipnis2024metabench}, and find that 31\% of MMLU~\citep{hendrycks2021mmlu} items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$), indicating large shifts in item functioning between models released in 2023 and 2024. This is not statistical noise: a random-split control within the 2023 cohort yields only 0.18\% ETS~C items. The instability persists across all 57 MMLU subjects (C\% range 21--48\%, unweighted mean $\approx 30\%$), and item-level regression shows that 92.4\% of this instability is unrelated to aggregate domain-level accuracy gains. Nearly one in three MMLU items behaves differently depending on when the evaluated models were trained. Crucially, this instability does not threaten benchmark validity: Spearman rank correlation between model rankings computed on all items versus stable-only items is $\rho \approx 0.997$. The instability is diagnostic, not destructive; it reveals which capability dimensions shift across model generations rather than rendering MMLU scores unreliable.
5	
6	A growing body of contamination detection research has produced sophisticated item-level methods, from membership inference approaches such as Min-K\%~\citep{shi2024mink} to performance-based detectors such as ConStat~\citep{dekoninck2024constat}, DVD~\citep{liang2026dvd}, and Self-Critique~\citep{tao2026selfcritique}. These methods validate detection accuracy primarily against web-overlap labels such as those of \citet{li2024contamination}, which classify benchmark items as contaminated based on verbatim or near-verbatim matches in publicly accessible training corpora. Such labels measure \emph{global exposure}: whether an item exists in the data ecosystem that all training pipelines can access. They do not measure \emph{differential item functioning}: whether an item behaves differently across model cohorts that may have had varying degrees of exposure or different training methodologies. \Cref{fig:global_vs_differential} illustrates the distinction. Most MMLU items are globally contaminated in the sense that they exist in web-accessible text, so all model cohorts encounter them and no differential signal arises. The items that function differentially are those where exposure or training methodology changed asymmetrically across cohorts. Validating differential detectors against global-exposure labels therefore conflates two phenomena. Direct comparison confirms near-independence between the two flag sets (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), consistent across contamination subtypes.
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_1_global_vs_differential.pdf}
11	\caption{Global vs.\ differential contamination, illustrated via Item Characteristic Curves (ICCs). \textbf{Left}: global contamination produces no DIF; both cohorts encounter the item, and their ICCs overlap. \textbf{Right}: differential contamination produces DIF; the focal cohort's ICC shifts because only that cohort was disproportionately exposed during training. The enrichment ratio of $\approx 1.0$ between DIF flags and web-overlap labels is expected because most MMLU items fall into the left category.}
12	\label{fig:global_vs_differential}
13	\end{figure}
14	
15	We apply classical MH-DIF with ETS classification to the full METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), to our knowledge, the largest-scale DIF analysis on LLM benchmarks. This psychometric approach complements concurrent work on anchor-item calibration for score comparability~\citep{habba2026growingpains} and addresses the fragility of existing contamination detectors under post-training perturbation~\citep{wang2026fragility}. Semi-synthetic injection experiments confirm that DIF detects differential contamination when present ($\Delta\mathrm{TPR} = {+}0.508$ at exploitation rate $p = 0.5$), and our cross-subject matching protocol eliminates false positive inflation ($\Delta\mathrm{FPR} = 0.000$). Three structural controls (matched-ability quintile analysis, IRT $\theta$-conditioning, and within-subject pre-checks) confirm that the 31\% temporal instability cannot be attributed to methodological artifacts, establishing it as a robust empirical finding about MMLU's measurement properties.
16	
17	MMLU's 12,508 items provide sufficient measurement redundancy that removing nearly a third does not alter rank order ($\rho \approx 0.997$). DIF should therefore be understood as a diagnostic lens rather than a quality filter. DIF-flagged items concentrate discriminative signal: removing them degrades ranking discriminability more than random removal ($z = -8\sigma$ to $-49\sigma$ across 21 conditions). Model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions under stable-item evaluation, while Mistral-based models lose a median of $35$; 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$.
18	
19	We do not modify the MH-DIF procedure itself; the contributions are empirical, not algorithmic. Three layers of genuine novelty emerge: (a)~we discover that 31\% temporal instability is robust across thresholds and unrelated to aggregate domain-level accuracy gains, the first large-scale characterization of item-level benchmark stability at 5,227 models; (b)~we expose a fundamental validation methodology gap in the contamination detection literature, showing that web-overlap labels are poorly suited to evaluate item-level differential detectors; and (c)~we provide a reusable semi-synthetic validation framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$), confirmed on GSM8K with independent contamination validation through the GSM1K held-out set~\citep{zhang2024gsm1k}. We make the following contributions:
20	
21	\begin{enumerate}
22	\item \textbf{Benchmark temporal comparability} (Claim 1): 31\% of MMLU items are functionally unstable across model generations under ETS~C classification, with C\% ranging from 21\% to 48\% across all 57 subjects (mean $\approx 30\%$) and confirmed non-random by random-split control at 0.18\% (\Cref{sec:temporal}).
23	
24	\item \textbf{Ground truth meta-critique} (Claim 2): Web-overlap contamination labels~\citep{li2024contamination} do not provide appropriate ground truth for item-level differential detectors. Direct empirical comparison on 9,229 items shows near-independence (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$), exposing a validation methodology gap in the contamination detection literature (\Cref{sec:groundtruth}).
25	
26	\item \textbf{Semi-synthetic validation framework} (Claim 3): Controlled injection with cross-subject matching achieves $\Delta\mathrm{FPR} = 0.000$ while preserving detection power ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$); cross-benchmark replication on GSM8K confirms generality (\Cref{sec:semisynthetic,sec:gsm8k}).
27	
28	\item \textbf{DIF as diagnostic lens} (Claim 4): DIF-flagged items concentrate discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, suggestive at $N = 33$), indicating that DIF captures item-level behavioral change distinct from simple memorization (\Cref{sec:downstream,sec:gsm8k}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "efad4537-2169-4410-b008-5c2e9520ad0d",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "6f908825-874a-47d8-a2db-7571476b7275",
  "sourceToolAssistantUUID": "efad4537-2169-4410-b008-5c2e9520ad0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T09:50:12.961Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AJbyiMgTkYGfRjrfRo4u3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f908825-874a-47d8-a2db-7571476b7275",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJNxjrAesXKAiqjrdr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "003eeff7-8dcf-4163-861c-bed44389446e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTdoPbfX7pFkhTNsw3WdNq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8036,
      "cache_read_input_tokens": 16406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8036,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T09:50:12.975Z_

<details><summary>↩ Tool result · `toolu_01AJbyiMgTkYGfRjrfRo4u3n`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Contamination Detection.}
5	A growing family of methods detects benchmark contamination through model behavior or training data analysis. Membership inference approaches estimate whether a model has seen specific items during training: Min-K\% \citep{shi2024mink} and Min-K\%++ \citep{zhang2024minkpp} use token-level log-likelihood statistics, while Time Travel \citep{golchin2024timetravel} probes models with temporal cues. Performance-based detectors identify contamination through statistical anomalies: ConStat \citep{dekoninck2024constat} tests performance gaps between original and perturbed items, DVD \citep{liang2026dvd} uses distributional verification, and Self-Critique \citep{tao2026selfcritique} employs model self-evaluation. \citet{balloccu2024leak} provide a broader taxonomy of leakage detection strategies. These methods share a common validation practice: they verify detection accuracy against web-overlap or n-gram labels \citep{li2024contamination} that classify items based on verbatim matches in publicly accessible corpora. Such labels measure \emph{global exposure} (whether an item exists in training data) rather than \emph{differential item functioning} (whether an item behaves differently across model cohorts). This global-vs-differential distinction motivates our ground truth analysis (Claim~2, \Cref{sec:groundtruth}). Work on LLM memorization \citep{carlini2022quantifying, tirumala2022memorization} establishes that memorization depends on data frequency and model scale, reinforcing the distinction between global exposure and differential behavior. \citet{wang2026fragility} show that existing contamination detectors are fragile under reinforcement learning, further motivating behavioral approaches grounded in psychometric theory.
6	
7	\paragraph{IRT in LLM Evaluation.}
8	IRT adoption in LLM evaluation has accelerated: \citet{lalor2019irt} introduced IRT to NLP, \citet{vania2021irt} assessed test set discriminability, and recent extensions include PSN-IRT \citep{zhou2026psnirt} for benchmark quality at scale and TinyBenchmarks \citep{maiapolo2024tinybenchmarks} for IRT-based item selection. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which addresses score comparability through fixed-parameter calibration \citep[FPC;][]{kim2019fpc}. Our work is complementary: Growing Pains assumes anchor item stability, while DIF analysis diagnoses which items violate this assumption.
9	
10	\paragraph{DIF Methodology and Measurement Invariance.}
11	The Mantel-Haenszel procedure for DIF detection was introduced by \citet{holland1988mh} and remains the most widely used method in educational testing due to its simplicity and well-characterized statistical properties \citep{clauser1998dif}. Alternative approaches include logistic regression DIF \citep{swaminathan1990logistic}, SIBTEST \citep{shealy1993sibtest}, Lord's $\chi^2$ test \citep{lord1980irt}, and the Raju area method \citep{raju1988area}; \citet{zumbo1999handbook} provides a comprehensive comparison. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance, vandenberg2000invariance}, which examines whether a measurement instrument functions equivalently across populations. MIMIC models offer a latent-variable approach to the same problem \citep{muthen1985mimic, woods2009mimic}, and \citet{teresi2007dif} reviews DIF methods across applied domains. We do not modify the MH procedure; our contribution is the application context. The scale of this analysis (5,227 examinees across a 57-subject multidimensional ability space) exceeds typical educational testing applications, where \citet{belzak2020smallsample} note that DIF methods can behave differently at extreme sample sizes. The primary methodological challenge is the impact-versus-DIF confound: genuine ability differences between temporal cohorts can inflate DIF estimates. We address this through matched-ability quintile analysis, IRT $\theta$-conditioning, and a random-split control (\Cref{sec:temporal}).
12	
13	\paragraph{Benchmark Design and Evaluation.}
14	Dynamic benchmarks such as Dynabench \citep{kiela2021dynabench}, LatestEval \citep{li2024latesteval}, and LiveBench \citep{white2025livebench} mitigate contamination by construction, yet none provides psychometric equating across versions. Chatbot Arena \citep{chiang2024chatbot} sidesteps static benchmarks through pairwise preference. Broader surveys \citep{chang2024survey, burnell2023rethink} identify benchmark saturation and lack of item-level transparency as systemic challenges. Our DIF analysis fills this gap by identifying which items have become unreliable for cross-generation comparison. METABENCH \citep{kipnis2024metabench} provides the large-scale response matrix that makes this analysis possible.
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "003eeff7-8dcf-4163-861c-bed44389446e",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "f1234dd3-e4f9-42fd-ba88-1912684f0087",
  "sourceToolAssistantUUID": "003eeff7-8dcf-4163-861c-bed44389446e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-21T09:50:13.419Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DKfEJY9YD28LoJYq1LcrNx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1234dd3-e4f9-42fd-ba88-1912684f0087",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJNxjrAesXKAiqjrdr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "5095679d-d20f-42f6-bd35-f7774bdc45ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GTdoPbfX7pFkhTNsw3WdNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8036,
      "cache_read_input_tokens": 16406,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8036
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 16406,
          "cache_creation_input_tokens": 8036,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8036,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-21T09:50:13.428Z_

<details><summary>↩ Tool result · `toolu_01DKfEJY9YD28LoJYq1LcrNx`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh} detects DIF by stratifying examinees into $K$ score bins based on total score (a proxy for $\theta$), where $K$ equals the number of distinct total scores observed in the combined sample, and computing a common odds ratio across strata. Within each stratum $k$, the responses of the reference group and the focal group form a $2 \times 2$ contingency table:
17	
18	\begin{equation}
19	\label{eq:mh}
20	\alpha_{\mathrm{MH}} = \frac{\displaystyle\sum_{k=1}^{K} A_k D_k \,/\, T_k}{\displaystyle\sum_{k=1}^{K} B_k C_k \,/\, T_k}\,,
21	\end{equation}
22	
23	\noindent where $A_k$ and $B_k$ are the number of correct and incorrect responses in the reference group for stratum $k$, $C_k$ and $D_k$ are the corresponding counts for the focal group, and $T_k$ is the total number of examinees in stratum $k$. Under the null hypothesis of no DIF, $\alpha_{\mathrm{MH}} = 1$. The log odds ratio is converted to the ETS delta scale:
24	
25	\begin{equation}
26	\label{eq:delta}
27	\Delta_{\mathrm{MH}} = -2.35 \ln(\alpha_{\mathrm{MH}})\,.
28	\end{equation}
29	
30	The Educational Testing Service (ETS) classifies DIF severity into three categories based on $|\Delta_{\mathrm{MH}}|$. Category~A (negligible) requires $|\Delta_{\mathrm{MH}}| < 1.0$. Category~C (large) requires both $|\Delta_{\mathrm{MH}}| \geq 1.5$ and statistical significance at $p < 0.05$ from the MH chi-squared test. Category~B (moderate) includes all remaining items: those with $1.0 \leq |\Delta_{\mathrm{MH}}| < 1.5$, or $|\Delta_{\mathrm{MH}}| \geq 1.5$ without statistical significance. The dual threshold in ETS~C (effect size \emph{and} significance) guards against flagging items that show large but unreliable effect sizes. Throughout this paper, we report the percentage of items classified as ETS~C, denoted C\%.
31	
32	The choice of matching variable (the total score used for stratification) affects both validity and interpretation. We distinguish three matching strategies: (1)~\emph{standard matching} uses the within-benchmark total score on all items of the same benchmark; (2)~\emph{cross-subject matching} uses the total score on all subjects \emph{other than} the one containing the item under test, preventing the matching variable from absorbing injected contamination signals (\Cref{sec:injection}); and (3)~\emph{external matching} uses the total score on a different benchmark entirely (e.g., MMLU total score as the matching variable when testing DIF on GSM8K items), providing an independent ability proxy uncontaminated by the target benchmark. Cross-subject and external matching both address matching variable contamination but at different granularities: cross-subject operates within a multi-domain benchmark, while external operates across benchmarks.
33	
34	\subsection{Cohort Designs}
35	\label{sec:cohorts}
36	
37	We construct five cohort comparisons: (1)~\emph{Temporal}: 2023 ($N = 1{,}080$) vs.\ 2024 ($N = 807$) models, the primary comparison; (2)~\emph{Ability-quintile}: Q1--Q2 vs.\ Q4--Q5 within the same temporal window, testing whether ability differences alone produce DIF; (3)~\emph{Within-family}: Llama-2 ($N = 161$) vs.\ Llama-3 ($N = 308$), isolating generational changes within a single family; (4)~\emph{Within-subject}: per-subject DIF to test domain concentration; and (5)~\emph{Random split}: two random halves of the 2023 cohort ($N = 540$ each) as a sanity check.
38	
39	\subsection{Semi-Synthetic Injection Framework}
40	\label{sec:injection}
41	
42	To evaluate whether MH-DIF can detect differential contamination when it is present, we construct a semi-synthetic framework with controlled ground truth.
43	
44	\paragraph{Procedure.} From items classified as ETS~A in the uninjected data (negligible DIF), we select 20\% uniformly at random as the ``contaminated'' set. For each contaminated item, we flip incorrect responses to correct in the focal group at exploitation rate $p \in \{0.0, 0.3, 0.5, 0.7, 1.0\}$. We then run MH-DIF on the modified response matrix and measure detection performance. We report $\Delta\mathrm{TPR} = \mathrm{TPR}(\text{injected}) - \mathrm{TPR}(\text{baseline})$ and $\Delta\mathrm{FPR} = \mathrm{FPR}(\text{injected}) - \mathrm{FPR}(\text{baseline})$, where TPR is the true positive rate on injected items and FPR is the false positive rate on uninjected items. Each injection level is repeated across 5 random seeds for uncertainty estimation.
45	
46	\paragraph{Cross-subject matching.} The choice of matching variable is critical for valid semi-synthetic evaluation. When contamination is injected into items within subject $X$, the total score on subject $X$ absorbs part of the injection signal. Using this contaminated total score as the MH matching variable violates the conditional independence assumption and inflates FPR. Cross-subject matching resolves this problem by computing the matching variable from all subjects \emph{other than} the one being tested. Under this protocol, $\Delta\mathrm{FPR} = 0.000$ across all five MMLU domains (bootstrap 95\% CI $= [0.000, 0.000]$, 5,000 resamples), while detection power is preserved ($\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$ for four of five subjects). The zero FPR is a structural guarantee: cross-subject stratification scores are algebraically invariant to within-subject injection~\citep{clauser1998dif, nandakumar1993dif}. We adopt cross-subject matching as the standard protocol for all semi-synthetic analyses.
47	
48	Diagnostic procedures (Yen's Q3 local independence, domain-specificity analysis, instability decomposition) and statistical details (multiple testing correction, threshold sensitivity, architecture heterogeneity checks) appear in \Cref{app:method_details}.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5095679d-d20f-42f6-bd35-f7774bdc45ac",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "735315fd-949c-4083-a5ce-251adf671606",
  "sourceToolAssistantUUID": "5095679d-d20f-42f6-bd35-f7774bdc45ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T09:50:17.920Z_

<details open><summary>🔧 Tool call — Read · `toolu_01K8arVGy7FCK23HAJQAJx4o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "735315fd-949c-4083-a5ce-251adf671606",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJq3PTaGmkYsYuLURD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe5218fa-f0dc-43d8-a396-d6b421eabca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hc9U6QsT4jEo1FgFf79q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 24442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T09:50:17.948Z_

<details><summary>↩ Tool result · `toolu_01K8arVGy7FCK23HAJQAJx4o`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark replication on GSM8K appears in \Cref{sec:gsm8k}.
5	
6	\subsection{Validation: DIF Detection Power}
7	\label{sec:validation}
8	
9	A power analysis using empirical MMLU IRT parameters confirms that at $N \geq 80$ per cohort, ETS~C achieves TPR of 0.68--0.80, FPR of 0.036--0.042, and AUC of 0.93--0.94 for items with $|\Delta_{\mathrm{MH}}| \geq 1.4$. Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold.
10	
11	\subsection{Temporal Comparability: 31\% Item Instability}
12	\label{sec:temporal}
13	
14	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$). Benjamini-Hochberg FDR correction at $q = 0.05$ removes only 3 items (31.32\% $\to$ 31.30\%), because the dual ETS threshold on effect size and significance already provides implicit multiple-testing protection.
15	
16	Three controls confirm this reflects genuine temporal change. A random split of the 2023 cohort yields only 0.18\% ETS~C items (sampling noise), and an ability-quintile comparison within the same temporal cohort yields 2.9\% (ability differences alone). A within-family comparison (Llama-2 vs.\ Llama-3) produces 61.3\% ETS~C items, elevated by large ability gaps that confound the DIF signal~\citep{holland1988mh}. The contrast between 2.9\% (ability-controlled) and 61.3\% (ability-confounded) brackets the temporal rate of 31.3\%. Crucially, the temporal cohort ability gap is negligible: Cohen's $d = -0.17$ (below the $|d| = 0.2$ small-effect threshold) with 76.4\% distributional overlap. Under strict 1:1 nearest-neighbor matching ($d \approx -0.010$, $N = 638$ per group, 5 seeds), C\% $= 28.9\% \pm 0.1\%$---a 7.7\% relative reduction from 31.3\%, confirming that at most $\sim$2.4 pp of observed DIF is attributable to ability mismatch.
17	
18	Across all 57 MMLU subjects, C\% ranges from 20.7\% to 48.4\% (mean $\approx 30\%$); within-subject matching on 5 subjects yields 38.1\% as a robustness check (\Cref{tab:temporal_landscape}). Item-level logistic regression shows domain accuracy improvement explains only 2.4 percentage points of 31.3\% C\% (pseudo $R^2 = 0.0007$); 92.4\% of instability is item-specific. The conclusion is robust across thresholds: C\% $= 48.9\%$ at $|\Delta_{\mathrm{MH}}| \geq 1.0$, $18.3\%$ at $\geq 2.0$, $10.2\%$ at $\geq 2.5$.
19	
20	\begin{table}[t]
21	\centering
22	\caption{DIF landscape across cohort definitions. ETS~C denotes the percentage of items with $|\Delta_{\mathrm{MH}}| \geq 1.5$. FPR is measured against Li et al.\ web-overlap labels on the ``clean'' (non-overlapping) subset. Enrichment is the ratio of observed to expected overlap between DIF flags and web-overlap labels.}
23	\label{tab:temporal_landscape}
24	\small
25	\resizebox{\columnwidth}{!}{%
26	\begin{tabular}{lcccc}
27	\toprule
28	Cohort Definition & $N_{\mathrm{ref}}$ / $N_{\mathrm{focal}}$ & C\% & FPR (clean) & Enrich. \\
29	\midrule
30	Temporal (2023 vs.\ 2024) & 1,080 / 807 & 31.3 & 0.318 & 0.964 \\
31	Ability quintile (Q1--2 vs.\ Q4--5) & ${\sim}$2,600 / ${\sim}$2,600 & 2.9 & 0.027 & 1.19 \\
32	Within-family (Llama-2 vs.\ 3) & 161 / 308 & 61.3 & -- & -- \\
33	Random split (sanity) & 540 / 540 & 0.18 & -- & -- \\
34	Within-subject (avg, 5 subj.) & \textit{varies} & 38.1 & -- & -- \\
35	\bottomrule
36	\end{tabular}}
37	\end{table}
38	
39	\subsection{Ground Truth Mismatch}
40	\label{sec:groundtruth}
41	
42	Direct comparison of DIF flags against the web-overlap labels of \citet{li2024contamination} on 9,229 annotated items confirms that the two methods capture orthogonal signals. The enrichment ratio is 0.964 (\Cref{tab:temporal_landscape}): DIF-C rates are 30.7\% among web-contaminated items and 31.8\% among clean items. Association tests yield $\phi = 0.012$, $\chi^2 = 1.28$ ($p = 0.258$), and OR $= 1.05$ [0.96, 1.15]; the Jaccard index between flagged sets is 0.206. This near-independence holds across contamination subtypes (input-only enrichment $= 0.986$, input-and-label $= 0.960$). The null result does not indicate detection failure: semi-synthetic injection produces a clear dose-response ($\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$; \Cref{fig:dose_response}). The disconnect arises because web-overlap labels measure \emph{global exposure} (whether an item exists in training corpora), while DIF measures \emph{differential functioning} (whether an item's relationship to ability changes across cohorts). The Li et al.\ labels are the wrong ground truth for a differential method.
43	
44	\begin{figure}[t]
45	\centering
46	\includegraphics[width=\columnwidth]{fig_2_dose_response.pdf}
47	\caption{Semi-synthetic dose-response for DIF detection on MMLU. $\Delta\mathrm{TPR}$ increases monotonically with exploitation rate $p$, confirming that MH-DIF detects differential contamination when present. Baseline (no injection) produces $\Delta\mathrm{TPR} \approx 0$.}
48	\label{fig:dose_response}
49	\end{figure}
50	
51	\subsection{Structural Analysis}
52	\label{sec:structural}
53	
54	Three structural controls fail to reduce temporal C\% below 31\%: matched-ability quintiles, IRT $\theta$-conditioning ($r(\theta, \mathrm{total\ score}) = 0.9986$, FPR $= 0.312$), and within-subject DIF (C\% $= 38.1\%$, exceeding the 25\% bifactor viability threshold). Logistic regression DIF confirms 92.1\% concordance with MH and reveals additional non-uniform DIF (24.8\% at $|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% estimate conservative. Graduated de-duplication ($K{=}10$: 22.7\% vs.\ random 26.8\%; $K{=}20$: 29.1\% vs.\ 30.9\%) confirms family structure does not inflate C\%. Ability-matched within-family analysis reduces Llama-2 vs.\ Llama-3 C\% from 61.3\% to $28.3\% \pm 1.6\%$ (Cohen's $d = -0.99$, overlap $= 0.18$), while temporal matching reduces C\% from 31.3\% to $28.9\% \pm 0.1\%$ ($d = -0.17$, overlap $= 0.76$). The matched C\% values ($\sim$28--29\%) are consistent with each other despite vastly different unmatched rates (61.3\% vs.\ 31.3\%), suggesting that genuine item-level DIF accounts for $\sim$28--29\% of items, with the Llama comparison carrying 33 pp of additional ability confound (54\% reduction) versus only 2.4 pp for temporal cohorts (7.7\% reduction). Full details in \Cref{app:structural}.
55	
56	\subsection{Semi-Synthetic Framework Validation}
57	\label{sec:semisynthetic}
58	
59	The critical methodological finding is that the choice of matching strategy determines validity. Cross-subject matching computes the conditioning variable from subjects \emph{other than} the one being tested, achieving $\Delta\mathrm{FPR} = 0.000$ across all five MMLU subjects while four of five produce $\Delta\mathrm{TPR} > 0.3$ at $p = 0.5$. Within-subject matching inflates FPR by ${+}0.186$ on average because the matching variable absorbs part of the injection signal. We adopt cross-subject matching as the standard protocol (\Cref{app:fig_matching}).
60	
61	\subsection{Downstream Impact}
62	\label{sec:downstream}
63	
64	Spearman correlation between full and stable-item rankings is $\rho \approx 0.997$: aggregate model ordering is preserved despite 31\% item instability. DIF-flagged items nonetheless carry more discriminative signal than average ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal across 21 conditions), though a circularity ablation shows DIF-based removal is the \emph{least} disruptive among non-random strategies (Jaccard overlap with high-discrimination items is only 0.12). Individual model families show distinctive DIF profiles: Llama-3 derivatives gain a median of ${+}53$ rank positions (mean ${+}121$), while Mistral-based models lose a median of $35$ (mean $-54$); individual extremes reach ${+}793$ and $-542$ (\Cref{app:fig_downstream}). Overall, 25\% of models shift by $|\Delta\mathrm{Rank}| \geq 100$. The DIF instability pattern extends beyond MMLU; \Cref{sec:gsm8k} presents a full replication on GSM8K.
65	
66	\subsection{Cross-Benchmark Validation: GSM8K}
67	\label{sec:gsm8k}
68	
69	Replication on GSM8K (1,319 items $\times$ 6,702 models) yields temporal C\% $= 18.9\%$ (sanity check: 0.3\%), with semi-synthetic $\Delta\mathrm{TPR} = {+}0.514$ at $p = 0.5$ under external matching (\Cref{app:gsm8k_details}). As an exploratory analysis, the GSM1K held-out set~\citep{zhang2024gsm1k} provides independent contamination validation: for $N = 33$ models, the correlation between contamination gap and DIF ranking advantage is $r = -0.478$ ($p = 0.005$; partial $r = -0.385$, $p = 0.027$ after controlling for accuracy). This \emph{negative} correlation contradicts the hypothesis that DIF items benefit contaminated models, and instead suggests that DIF captures genuine capability change distinct from memorization (\Cref{fig:gsm1k}). The result is suggestive at $N = 33$ and warrants replication.
70	
71	\begin{figure}[t]
72	\centering
73	\includegraphics[width=\columnwidth]{fig_5_gsm1k_dif_correlation.pdf}
74	\caption{GSM1K contamination gap vs.\ DIF ranking advantage ($N = 33$). The negative correlation ($r = -0.478$, $p = 0.005$) indicates that models with larger contamination gaps benefit less from DIF-flagged items.}
75	\label{fig:gsm1k}
76	\end{figure}
77	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe5218fa-f0dc-43d8-a396-d6b421eabca1",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "52b18e94-d804-41ca-b01b-85be204181f6",
  "sourceToolAssistantUUID": "fe5218fa-f0dc-43d8-a396-d6b421eabca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T09:50:18.822Z_

<details open><summary>🔧 Tool call — Read · `toolu_0135NqaWZtXbzdEkY8L4EDhW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52b18e94-d804-41ca-b01b-85be204181f6",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJq3PTaGmkYsYuLURD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7b3bf81c-db66-4aa5-997f-7909ac93fb2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hc9U6QsT4jEo1FgFf79q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 24442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T09:50:18.829Z_

<details><summary>↩ Tool result · `toolu_0135NqaWZtXbzdEkY8L4EDhW`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Implications for Benchmark Temporal Comparability}
5	\label{sec:disc_temporal}
6	
7	The 31\% ETS~C instability rate is robust across thresholds (10--49\% at $|\Delta_{\mathrm{MH}}| \in [2.5, 1.0]$) and confirmed by structural controls (\Cref{sec:structural}). The temporal cohort ability gap is negligible ($d = -0.17$, overlap $= 76.4\%$); ability-matched C\% of $28.9\% \pm 0.1\%$ confirms the 31.3\% rate is not inflated by impact confounding. Domain accuracy improvement explains only 2.4 pp of 31.3\% C\%; 92.4\% is item-specific. This does not invalidate MMLU as a ranking instrument ($\rho \approx 0.997$) but signals measurement drift across model generations.
8	
9	\subsection{Ground Truth Meta-Critique}
10	\label{sec:disc_groundtruth}
11	
12	The near-independence between DIF flags and web-overlap labels (enrichment $= 0.964$, Jaccard $= 0.206$, $\phi = 0.012$; consistent across contamination subtypes) exposes a broader gap: the dominant validation practice of evaluating contamination detectors against web-overlap labels conflates global exposure with differential functioning. Most MMLU items appear in web text, so web-overlap labels identify a condition shared by nearly all items. This near-independence is the expected outcome when a differential method is evaluated against a global-exposure reference. Item-level differential detectors require item-level differential ground truth.
13	
14	\subsection{DIF as Diagnostic Lens}
15	\label{sec:disc_diagnostic}
16	
17	The GSM1K correlation ($r = -0.478$, $p = 0.005$, $N = 33$; \Cref{sec:gsm8k}) provides exploratory evidence that DIF-flagged items capture behavioral change distinct from memorization. Models with larger contamination gaps benefit \emph{less} from DIF-C items. Of the 249 DIF-C items on GSM8K, 171 favor the reference (2023) cohort ($\alpha_{\mathrm{MH}} > 1$). Partial correlation ($r = -0.385$, $p = 0.027$) after controlling for accuracy confirms the effect is not an artifact of general model quality. Caveats include a wide confidence interval (95\% CI $= [-0.71, -0.16]$) and limited sample size.
18	
19	Item characterization reinforces this: DIF-C items are harder ($d = -0.247$) and more discriminating ($d = 0.230$), distributed uniformly across subjects ($\chi^2$ $p = 0.32$). A difficulty $\times$ direction interaction ($\rho = -0.597$, $p < 0.001$) shows capability gains concentrate on hard items (88.7\% focal-favoring in hardest decile) while easy items erode (96.2\% reference-favoring in easiest decile).
20	
21	Yen's Q3 analysis confirms that local dependence does not drive DIF: extreme LD correlates negligibly with subject-level C\% ($r = 0.09$, $p = 0.50$), while reasoning-heavy domains with low LD show higher DIF ($r = -0.36$, $p = 0.006$), consistent with DIF capturing items sensitive to capability evolution.
22	
23	Structural constraints and limitations are discussed in the Limitations section.
24	
25	These findings motivate a benchmark maintenance protocol: periodic DIF monitoring across model cohorts, item-level stability labels (stable/drifting/unstable) published alongside benchmark releases, and cross-subject matching as the standard protocol for semi-synthetic validation. DIF should be understood as a diagnostic lens, not a quality filter; LLM benchmarks need psychometric monitoring alongside score reporting.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b3bf81c-db66-4aa5-997f-7909ac93fb2b",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "b3be19e1-9999-4364-9809-a33ac9338503",
  "sourceToolAssistantUUID": "7b3bf81c-db66-4aa5-997f-7909ac93fb2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T09:50:19.244Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Hm88WnNUfxGNht8ZZ7K6sv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3be19e1-9999-4364-9809-a33ac9338503",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJq3PTaGmkYsYuLURD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "94d2fcd0-8e56-4941-81af-d8f00d7032d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hc9U6QsT4jEo1FgFf79q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 24442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T09:50:19.250Z_

<details><summary>↩ Tool result · `toolu_01Hm88WnNUfxGNht8ZZ7K6sv`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Applying Mantel-Haenszel DIF analysis to the METABENCH response matrix (5,227 models $\times$ 12,508 MMLU items), we find that 31\% of items are functionally unstable across model generations under ETS Category~C classification. The instability is robust across thresholds (10--49\% at $|\Delta_{\mathrm{MH}}| \in [2.5, 1.0]$), confirmed non-random by a random-split control (0.18\%), and predominantly item-specific: domain accuracy improvement accounts for only 2.4 percentage points of the 31.3\% C\%. This instability does not invalidate MMLU as a ranking instrument ($\rho \approx 0.997$ between full and stable-item rankings) but signals that item-level measurement properties are drifting across model generations.
5	
6	The analysis exposes a validation methodology gap in the contamination detection literature. Web-overlap labels measure whether items exist in publicly accessible training corpora, not whether items function differently across model cohorts. The enrichment between DIF flags and these labels is $\approx 0.96$ (chance level), the expected outcome when a differential method is evaluated against global-exposure labels. Our semi-synthetic injection framework with cross-subject matching ($\Delta\mathrm{FPR} = 0.000$, $\Delta\mathrm{TPR} = {+}0.508$ at $p = 0.5$) provides a controlled alternative that any item-level detector can use for validation. Cross-benchmark replication on GSM8K ($\Delta\mathrm{TPR} = {+}0.514$) confirms the framework's portability.
7	
8	DIF-flagged items are not noise. They concentrate cross-generational discriminative information ($z = -8\sigma$ to $-49\sigma$ vs.\ random removal) and anti-correlate with the GSM1K contamination gap ($r = -0.478$, $p = 0.005$, $N = 33$), consistent with DIF items capturing genuine capability change that contamination does not confer. Individual extremes within Phi-3 and Llama-3 families reach ${+}793$ rank positions (family medians: ${+}20$ and ${+}53$), while individual Mistral-based models shift by up to $-542$ (family median: $-35$). DIF is a diagnostic lens for understanding what changed across model generations, not a quality filter for removing bad items.
9	
10	LLM benchmarks need psychometric monitoring alongside score reporting. DIF analysis provides a scalable, method-agnostic diagnostic that requires only a binary response matrix and group labels, with no access to model internals or training data.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94d2fcd0-8e56-4941-81af-d8f00d7032d4",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "300b002b-2475-47d5-af48-9fd1aec708db",
  "sourceToolAssistantUUID": "94d2fcd0-8e56-4941-81af-d8f00d7032d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-21T09:50:19.295Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Tg6KJBSk9fEmCd6h3dPa4h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "300b002b-2475-47d5-af48-9fd1aec708db",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWJq3PTaGmkYsYuLURD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "207ccb8d-b5b0-4562-9016-50fd177c1796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U2Hc9U6QsT4jEo1FgFf79q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6495,
      "cache_read_input_tokens": 24442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6495,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T09:50:19.304Z_

<details><summary>↩ Tool result · `toolu_01Tg6KJBSk9fEmCd6h3dPa4h`</summary>

```text
1	\section*{Limitations}
2	
3	\paragraph{Methodological scope of MH-DIF.}
4	The Mantel-Haenszel procedure detects only \emph{uniform} DIF, where the odds ratio between cohorts is constant across ability strata. Logistic regression DIF analysis reveals an additional 24.8\% of items exhibiting non-uniform DIF ($|\beta_{\mathrm{interaction}}| \geq 0.5$), making the 31\% ETS~C estimate conservative. Future work should apply non-uniform DIF methods (e.g., logistic regression or IRT-based approaches) as the primary analysis to capture the full spectrum of item instability.
5	
6	\paragraph{Ability confounding.}
7	Although the temporal cohort ability gap is negligible (Cohen's $d = -0.17$, overlap $= 76.4\%$) and nearest-neighbor matching confirms that at most 2.4 percentage points of C\% are attributable to ability mismatch, within-family comparisons with large ability gaps (e.g., Llama-2 vs.\ Llama-3, $d = -0.99$) produce substantially inflated C\% (61.3\% unmatched vs.\ 28.3\% matched). Any application of MH-DIF to cohorts with larger ability differences must incorporate ability matching or stratification beyond the standard 5-strata procedure.
8	
9	\paragraph{Sample size requirements.}
10	Our power analysis indicates reliable ETS~C detection requires $N \geq 80$ per cohort. The temporal cohorts (1,080 and 807 models) far exceed this threshold, but the GSM1K correlation analysis ($N = 33$) has limited statistical power (95\% CI $= [-0.71, -0.16]$). The negative correlation between contamination gap and DIF ranking advantage ($r = -0.478$) is exploratory and warrants replication with larger model samples.
11	
12	\paragraph{Contamination vs.\ capability change.}
13	DIF analysis detects \emph{that} items function differently across cohorts but cannot determine \emph{why}. The differential signal may reflect contamination, capability change, training methodology shifts, or interactions among these factors. We present evidence that DIF captures something distinct from memorization (negative GSM1K correlation, semi-synthetic dose-response), but a definitive causal decomposition remains out of reach without access to model training data.
14	
15	\paragraph{Benchmark scope.}
16	We analyze MMLU (12,508 items) and GSM8K (1,319 items), both multiple-choice or short-answer benchmarks scored as binary correct/incorrect. The generalizability of our findings to open-ended generation benchmarks (e.g., AlpacaEval, MT-Bench), coding benchmarks (e.g., HumanEval), or benchmarks with non-binary scoring remains untested. The binary response format is a prerequisite for MH-DIF; extending DIF analysis to continuous or partial-credit scoring would require ordinal or polytomous DIF methods.
17	
18	\paragraph{Temporal cohort definition.}
19	We define cohorts by calendar year of model release (2023 vs.\ 2024), a coarse grouping that aggregates models with diverse training pipelines, data mixtures, and post-training procedures. Finer-grained cohort definitions (e.g., by training data cutoff, model family, or alignment method) might reveal more targeted patterns of item instability but would reduce per-cohort sample sizes and statistical power.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "207ccb8d-b5b0-4562-9016-50fd177c1796",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "c1681e23-46fd-4791-ba57-b97fdfd0ed24",
  "sourceToolAssistantUUID": "207ccb8d-b5b0-4562-9016-50fd177c1796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-21T09:50:22.216Z_

Now let me read the appendix to understand the full scope of experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1681e23-46fd-4791-ba57-b97fdfd0ed24",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWKGPdUHXjxt12swvGy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ac558874-9054-4231-a2f5-00a51a93311e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkbyCDJQh8ZdeaB5DP9Ywv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6475,
      "cache_read_input_tokens": 30937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6475,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T09:50:28.581Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LtT84wTMnxwmG51W55GZNF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac558874-9054-4231-a2f5-00a51a93311e",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWKGPdUHXjxt12swvGy",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "de969343-b2e0-4e7e-ab14-e352f89e011c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HkbyCDJQh8ZdeaB5DP9Ywv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6475,
      "cache_read_input_tokens": 30937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6475,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T09:50:28.588Z_

<details><summary>↩ Tool result · `toolu_01LtT84wTMnxwmG51W55GZNF`</summary>

```text
1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini-Hochberg FDR correction at $q = 0.05$. The random-split sanity check provides an empirical estimate of the false positive rate under the null hypothesis.
19	
20	\paragraph{Threshold sensitivity.} We report results across a range of DIF thresholds ($|\Delta_{\mathrm{MH}}| \in \{1.0, 1.5, 2.0, 2.5\}$) to verify that qualitative conclusions do not depend on the specific ETS~C cutoff. The standard threshold of $|\Delta_{\mathrm{MH}}| \geq 1.5$ corresponds to the ETS~C definition used throughout the paper.
21	
22	\paragraph{Architecture heterogeneity.} The METABENCH MMLU population consists of 99.98\% decoder-only models (5,226 of 5,227). This near-complete architectural homogeneity eliminates architecture as a confound for DIF analysis. We verify this by excluding the single encoder-decoder model and confirming identical results.
23	
24	\section{Structural Analysis Details}
25	\label{app:structural}
26	
27	Three progressively refined approaches fail to reduce the temporal false positive rate below 31\%, revealing a structural property of the data rather than a methodological limitation. Matched-ability quintile analysis restricts comparisons to models of similar total score and yields enrichment ratios of 0.94--1.04, with temporal FPR unchanged at approximately 0.31. IRT $\theta$-conditioning with 20 ability strata achieves $r(\theta, \mathrm{total\ score}) = 0.9986$ and FPR $= 0.312$, confirming that the external total score already captures nearly all ability variance relevant to DIF computation. Within-subject DIF analysis on 5 representative subjects, intended to isolate subject-specific effects, finds mean C\% $= 38.1\%$, exceeding the 25\% threshold that would indicate viable bifactor structure. \Cref{tab:structural_comparison} summarizes these results.
28	
29	The temporal FPR reflects genuine item-level instability that persists regardless of how ability is measured or conditioned. Yen's Q3 diagnostic reveals mild local dependence within subjects (11.3\% of within-subject item pairs exceed $|Q3| > 0.20$, vs.\ 2.2\% cross-subject; $5{\times}$ ratio, $p = 2.3 \times 10^{-9}$), which contributes to elevated within-subject DIF rates but is not the primary driver: the cross-subject matching protocol addresses this bias, and temporal C\% persists under external matching (full Q3 distributions in Appendix~Figure~A2).
30	
31	\begin{table}[h]
32	\centering
33	\caption{Structural approaches to reducing temporal DIF. None reduces baseline FPR below 31\%, indicating that the observed instability is not an artifact of ability matching. Subscript $\pm$ values denote standard deviations across 5 injection seeds (baseline row only).}
34	\label{tab:structural_comparison}
35	\small
36	\resizebox{\columnwidth}{!}{%
37	\begin{tabular}{lcccc}
38	\toprule
39	Approach & Mechanism & Temp.\ FPR & TPR ($p{=}0.5$) & Outcome \\
40	\midrule
41	Baseline (ext.) & Cross-bench.\ total score & $0.314_{\pm.009}$ & $0.834_{\pm.027}$ & Reference \\
42	Matched-ability & Within-quintile temp.\ DIF & ${\sim}$0.31 & -- & Enrich.\ 0.94--1.04 \\
43	$\theta$-cond. & $\theta$ replaces total score & 0.312 & 0.876 & $r(\theta,\mathrm{total}) {=} 0.9986$ \\
44	Within-subject & Per-subject DIF & -- & -- & C\% $= 38.1\%$ ($>$25\%) \\
45	\bottomrule
46	\end{tabular}}
47	\end{table}
48	
49	\section{Additional Figures}
50	\label{app:figures}
51	
52	\begin{figure}[h]
53	\centering
54	\includegraphics[width=\columnwidth]{fig_3_within_subject_matching.pdf}
55	\caption{Cross-subject vs.\ within-subject matching for semi-synthetic DIF detection. Cross-subject matching eliminates FPR inflation ($\Delta\mathrm{FPR} = 0.000$) while preserving detection power ($\Delta\mathrm{TPR} > 0.3$ for 4/5 subjects at $p = 0.5$). Within-subject matching inflates FPR by ${+}0.186$ on average.}
56	\label{app:fig_matching}
57	\end{figure}
58	
59	\begin{figure}[h]
60	\centering
61	\includegraphics[width=\columnwidth]{fig_4_downstream_impact.pdf}
62	\caption{Downstream impact of DIF-based item filtering on model rankings. Despite $\rho \approx 0.997$ overall, individual model families show systematic rank shifts when evaluated on stable items only.}
63	\label{app:fig_downstream}
64	\end{figure}
65	
66	\section{Cross-Benchmark Comparison}
67	\label{app:gsm8k_details}
68	
69	\begin{table}[h]
70	\centering
71	\caption{Cross-benchmark comparison of DIF analysis on MMLU and GSM8K. Both benchmarks exhibit temporal item instability with validated semi-synthetic detection power. Standard and external matching use different exploitation rates ($p$) because each benchmark's optimal operating point differs; external matching results are compared at $p = 0.5$ for both. Subscript $\pm$ values denote standard deviations across 5 random injection seeds.}
72	\label{tab:gsm8k_comparison}
73	\small
74	\begin{tabular}{lcc}
75	\toprule
76	Metric & MMLU & GSM8K \\
77	\midrule
78	Items & 12,508 & 1,319 \\
79	Models & 5,227 & 6,702 \\
80	Temporal C\% & 31.3\% & 18.9\% \\
81	Sanity C\% & 0.18\% & 0.3\% \\
82	$\Delta$TPR ($p{=}0.7$, standard) & -- & $+0.818_{\pm.006}$ \\
83	$\Delta$TPR ($p{=}0.5$, external) & $+0.508_{\pm.027}$ & $+0.514_{\pm.028}$ \\
84	\bottomrule
85	\end{tabular}
86	\end{table}
87	
88	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de969343-b2e0-4e7e-ab14-e352f89e011c",
  "isSidechain": true,
  "promptId": "4864c1be-440f-4905-a8e5-3903db7b92da",
  "agentId": "a6a3ce6d6529a70ac",
  "type": "user",
  "uuid": "53a32d87-e0f2-4374-955d-ba759911a33f",
  "sourceToolAssistantUUID": "de969343-b2e0-4e7e-ab14-e352f89e011c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-21T09:51:58.155Z_

Now I have a thorough understanding of the paper. Let me compile the review.

---

## Review: Psychometric DIF Analysis Reveals 31% Temporal Instability in MMLU

**Reviewer:** R2 (Novelty and Related Work)

### Summary

This paper applies the standard Mantel-Haenszel DIF procedure from educational measurement to the METABENCH response matrix (5,227 models x 12,508 MMLU items), finding that 31% of items exhibit large DIF (ETS Category C) between 2023 and 2024 model cohorts. The paper also argues that web-overlap contamination labels are inappropriate ground truth for item-level differential detectors, proposes a semi-synthetic injection framework with cross-subject matching, and replicates on GSM8K. The framing positions DIF as a "diagnostic lens" rather than a quality filter, noting that MMLU rankings remain stable (rho=0.997) despite the instability.

### Strengths

- **Empirical thoroughness within the main analysis.** The paper runs multiple controls (random split, ability-quintile, within-family, matched-ability) that provide meaningful context for the 31% headline number. The random split at 0.18% and ability-quintile at 2.9% are informative baselines. The paper is honest about what each control does and does not establish.

- **Ground truth meta-critique is the strongest conceptual contribution.** The observation that web-overlap labels measure global exposure while DIF measures differential functioning -- and that these are near-independent (enrichment=0.964) -- is a useful clarification for the contamination detection community. This distinction between global and differential contamination is clearly articulated and could influence future validation practices.

- **Semi-synthetic framework design.** The cross-subject matching protocol that achieves Delta-FPR=0.000 is a clean methodological detail. The algebraic invariance argument is sound, and the framework is genuinely reusable by other researchers.

- **Honest reporting of limitations.** The paper acknowledges the GSM1K sample size (N=33), the inability to distinguish contamination from capability change, and the scope limitations to binary-scored benchmarks. The Limitations section is substantive, not pro forma.

- **Scale.** Analyzing 5,227 models x 12,508 items is large for a DIF study, and METABENCH is a useful resource that the paper exploits well.

### Weaknesses

- **(Major) The core application is a straightforward transfer of a textbook method, and the paper's own results undermine the headline finding.** MH-DIF is a 1988 procedure with well-known properties (Holland & Thayer). Applying it to a new dataset -- even a large one -- does not constitute a methodological contribution, and the paper explicitly states "we do not modify the MH-DIF procedure itself." The empirical contribution must therefore stand on the novelty and surprise value of the findings. But the paper's own controls show that ability-matched C% drops to 28.9%, and more critically, that the instability does not matter for rankings (rho=0.997). The paper tries to have it both ways: the title and abstract advertise "31% instability" as alarming, while the text reassures us it is merely "diagnostic, not destructive." If the instability doesn't affect rankings, the practical significance is unclear. If it does affect individual model families (the rank-shift analysis), that finding is buried rather than foregrounded.

- **(Major) Related work is thin and missing critical references.** The related work section is approximately 0.5 pages with ~40 references total in the bibliography, but the actual related work discussion engages substantively with only a handful. Key omissions:
  - **IRT in NLP beyond Lalor et al.:** The paper cites Lalor et al. (2019) and Vania et al. (2021) but does not engage with the broader IRT-in-NLP literature (e.g., Rodriguez et al. 2021 "Evaluation Examples Are Not Equally Informative"; Byrd & Srivastava 2022 on IRT for NLU benchmarks; Polo et al.'s IRT work beyond tinyBenchmarks).
  - **Test equating literature:** The paper's central concern -- temporal comparability -- is precisely the problem that test equating addresses in psychometrics. The paper does not cite or discuss test equating methods (common-item equating, IRT-based equating, equipercentile equating), which are the standard solution to the problem the paper identifies. The Growing Pains paper (Habba et al. 2026) uses FPC, which IS test equating, but the paper treats it as merely "complementary" without engaging with the equating framework.
  - **Benchmark contamination:** Missing Yang et al. (2023, "Rethinking Benchmark and Contamination"), Oren et al. (2024, "Proving Test Set Contamination"), Deng et al. (2024, "Investigating Data Contamination"). The contamination detection landscape is broader than what is reviewed.
  - **Measurement invariance in ML:** The paper cites Meredith (1993) and Vandenberg & Lance (2000) on measurement invariance but does not discuss recent work applying these concepts to ML systems (e.g., fairness literature that uses DIF for bias detection in automated scoring systems).

- **(Major) Framing mismatch between title and content.** The title says "31% Temporal Instability." The paper's own nearest-neighbor matching shows 28.9% under strict ability control, and ability-quintile analysis produces only 2.9%. The 31% figure confounds temporal DIF with ability differences. While the paper argues the confound is small (2.4 pp), the presentation strategy of leading with the larger number in the title, abstract, and throughout, while burying the nuance, is misleading. A more accurate title would reference the ~29% ability-matched figure. The mismatch extends to the abstract, which says "31% of MMLU items show large temporal DIF" without the ability-matching qualification until much later.

- **(Major) The paper attempts too many experiments at insufficient depth.** The paper reports at least 13 distinct analyses in 8 pages: primary temporal DIF, random-split control, ability-quintile, within-family, matched-ability nearest-neighbor, IRT theta-conditioning, within-subject, logistic regression DIF, de-duplication, semi-synthetic injection (MMLU), ground truth comparison, GSM8K replication, GSM1K correlation, downstream rank impact, Yen's Q3, item characterization, and domain-specificity decomposition. Each receives 1-3 sentences. This creates a catalog of results rather than a coherent contribution. Key analyses that deserve more space -- like the ability-matching result that reduces the headline from 31% to 29%, or the GSM1K correlation at N=33 -- are compressed to single sentences. The paper would be stronger if it dropped several peripheral analyses and developed the core 3-4 findings properly.

- **(Major) The "novelty" claims are overstated relative to the actual contributions.** The introduction lists three "layers of genuine novelty." Claim (a) -- 31% instability is robust -- is an empirical observation from applying an existing method. The characterization of "genuine novelty" for finding that a known method produces nonzero results on a new dataset is a stretch. Claim (b) -- web-overlap labels are wrong ground truth -- is a valid observation but is essentially a negative result (enrichment is ~1.0), not a positive contribution. Claim (c) -- the semi-synthetic framework -- is methodologically clean but is also straightforward: inject known signal, measure detection. The individual claims are useful; calling them "genuine novelty" at the EMNLP level is generous.

- **(Minor) The GSM1K correlation analysis is underpowered and over-interpreted.** N=33, r=-0.478, with a wide CI of [-0.71, -0.16]. The paper appropriately calls this "exploratory" and "suggestive," but it then features prominently in the abstract, conclusion, and as evidence for Claim 4. An N=33 correlation should not appear in the abstract of an EMNLP paper or serve as a primary evidence pillar.

- **(Minor) 98% IRT model misfit is not adequately addressed.** The paper mentions in the appendix that IRT theta-conditioning achieves r(theta, total score)=0.9986, which effectively means total score IS the ability estimate. The paper tried and failed to fit a bifactor IRT model (within-subject C%=38.1% exceeds the 25% viability threshold). This suggests the psychometric framing itself may be inappropriate for these data -- LLM response patterns may not conform to IRT assumptions. This is a foundational concern that deserves more than a passing mention.

- **(Minor) The "MMLU tolerates instability gracefully" framing neutralizes the paper's own contribution.** If 31% instability doesn't matter (rho=0.997), why should reviewers, benchmark designers, or practitioners care? The paper needs to choose: either the instability is consequential (and then rho=0.997 is misleading because it hides family-specific effects), or it is inconsequential (and then the paper is reporting a non-problem). The current framing tries to occupy both positions.

- **(Minor) Missing engagement with the "improvement vs. instability" distinction.** The within-family Llama-2 vs. Llama-3 comparison at C%=61.3% (reducing to 28.3% after ability matching) strongly suggests that much of what DIF detects is simply that models got better at certain items. The paper acknowledges this in the limitations but does not grapple with the implication: DIF may be detecting the expected consequence of capability improvement, not a pathology of the benchmark.

### Questions for Authors

1. The ability-quintile control (2.9% C%) and the random split (0.18%) suggest that pure ability differences produce very little DIF. The temporal cohorts have Cohen's d=-0.17. Can you provide a formal decomposition of the 31.3% into (a) ability-driven, (b) training-methodology-driven, and (c) residual components? The current "92.4% is item-specific" decomposition via pseudo-R^2=0.0007 is not convincing because it uses domain-level accuracy as the predictor, which is too coarse.

2. If MMLU rankings are preserved at rho=0.997 despite 31% item instability, what is the actionable recommendation? "Psychometric monitoring" is vague. Would you recommend removing DIF-C items? Your own analysis shows this degrades discriminability. Would you recommend flagging them? For what purpose?

3. The paper positions DIF as complementary to Growing Pains (Habba et al. 2026). How specifically? If Growing Pains identifies stable anchor items via FPC, and your method identifies unstable items via DIF, and the overlap between these sets is not characterized, how do practitioners use both?

4. Why not apply logistic regression DIF as the primary method, given that it detects non-uniform DIF (which you find at 24.8%) and is more informative? The choice of MH-DIF over LR-DIF seems driven by simplicity rather than suitability.

5. The GSM1K correlation is featured prominently but is at N=33. What is your plan for replication? Is there a reason you could not obtain a larger sample?

6. You report that "98%" of variance is captured by total score (r=0.9986 between theta and total score). Does this not suggest that the IRT model adds nothing beyond raw total score, undermining the psychometric framing?

### Scores

| Dimension | Score | Rationale |
|---|---|---|
| **Soundness** | 3.0 | The statistical methodology is correctly executed but the interpretive framework has internal contradictions (instability that doesn't matter, headline numbers that shrink under controls). The analysis is thorough but the conclusions don't fully follow from the evidence. |
| **Excitement** | 2.0 | Applying a textbook 1988 method to a new dataset without modification, finding that it produces nonzero results, and then showing the results don't affect rankings -- this is below the EMNLP novelty bar. The ground truth meta-critique is the most interesting contribution but is essentially a negative result. |
| **Reproducibility** | 4.0 | METABENCH is public, MH-DIF is standard, the semi-synthetic framework is well-described. Reproduction should be straightforward. |
| **Overall** | 2.5 (Borderline Findings) | The paper has a valid core observation (web-overlap labels are inappropriate for differential detectors) buried inside a much larger paper that applies an off-the-shelf method, advertises a headline number undermined by its own controls, and attempts to pack ~13 experiments into 8 pages without developing any of them adequately. The breadth-over-depth strategy produces a catalog of results, not a research contribution at the EMNLP level. |

**Confidence:** 4/5. I am familiar with both the psychometric (DIF, IRT, measurement invariance) and NLP evaluation literatures. My main uncertainty is whether the community would value the ground truth meta-critique more highly than I do -- it is a useful observation that could influence validation practices, but it is a negative result (enrichment=0.96) rather than a positive one.

### Recommendation

**Borderline Findings (2.5).** The ground truth meta-critique and semi-synthetic framework are useful contributions that could be published in a more focused 4-page paper. The current submission tries to be simultaneously a methods paper (semi-synthetic framework), an empirical paper (31% instability), and a meta-analysis (DIF vs. ConStat vs. web-overlap), and does not succeed sufficiently at any of these for EMNLP main conference. The related work needs significant expansion, the framing needs to be honest about what the controls show, and the paper needs to choose 3-4 core findings and develop them properly rather than cataloging 13 experiments at surface level. If revised to focus on the meta-critique + semi-synthetic framework with honest framing of the instability finding, this could be a solid Findings paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53a32d87-e0f2-4374-955d-ba759911a33f",
  "isSidechain": true,
  "agentId": "a6a3ce6d6529a70ac",
  "requestId": "req_011CbFWKx1cnhsyGH2oQpH2F",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "64e95f57-e8c1-4d18-93d5-b51ecef73a6c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "beaf218b-5fe0-4583-84e6-cda110d75429",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CXtZFgJqRwRyzBAg3jU4qk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2407,
      "cache_read_input_tokens": 37412,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2407,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---
