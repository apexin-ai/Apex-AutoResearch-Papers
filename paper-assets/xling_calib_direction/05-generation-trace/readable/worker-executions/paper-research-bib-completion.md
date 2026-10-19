# paper research bib completion

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 148
- **Recorded user turns:** 0
- **Tool calls:** 57
- **Original source:** `logs/workers/worker_paper_research_bib_completion_20260521T073708.log`
- **Structured JSON:** [`95a746b5333db28bf664.json`](../../sessions/95/95a746b5333db28bf664.json)

## Before a recorded user message

148 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction",
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "6b85677e-30a7-437a-a9ca-ebe267fa8ad3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-xling-calib-direction/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779359400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d66202e9-76a1-4f94-a30c-2f95274b8004",
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing files to understand the current state, then search for the papers that need verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "5bb0e5a9-eab3-4f73-9a37-65571abd4d5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013W99tdk6WZGQCeEcNnKTFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_0197JTAkkSQEkYx4RPYE4Hvz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "f9baa218-e2d5-4049-8167-6ed647c6d07a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013W99tdk6WZGQCeEcNnKTFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T07:37:21.029Z_

<details><summary>↩ Tool result · `toolu_0197JTAkkSQEkYx4RPYE4Hvz`</summary>

```text
1	% Use this file for citations not found in the ACL Anthology (contained in "anthology.bib").
2	
3	@book{Aho:72,
4	    author  = {Alfred V. Aho and Jeffrey D. Ullman},
5	    title   = {The Theory of Parsing, Translation and Compiling},
6	    year    = "1972",
7	    volume  = "1",
8	    publisher = {Prentice-Hall},
9	    address = {Englewood Cliffs, NJ}
10	}
11	
12	@book{APA:83,
13	    author  = {{American Psychological Association}},
14	    title   = {Publications Manual},
15	    year    = "1983",
16	    publisher = {American Psychological Association},
17	    address = {Washington, DC}
18	}
19	
20	@article{Chandra:81,
21		author = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},
22		year = "1981",
23		title = {Alternation},
24		journal = {Journal of the Association for Computing Machinery},
25		volume = "28",
26		number = "1",
27		pages = "114--133",
28		doi = "10.1145/322234.322243",
29	}
30	
31	@inproceedings{andrew2007scalable,
32	  title={Scalable training of {L1}-regularized log-linear models},
33	  author={Andrew, Galen and Gao, Jianfeng},
34	  booktitle={Proceedings of the 24th International Conference on Machine Learning},
35	  pages={33--40},
36	  year={2007},
37	}
38	
39	@book{Gusfield:97,
40	    author  = {Dan Gusfield},
41	    title   = {Algorithms on Strings, Trees and Sequences},
42	    year    = "1997",
43	    publisher = {Cambridge University Press},
44	    address = {Cambridge, UK}
45	}
46	
47	@article{rasooli-tetrault-2015,
48	    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},
49	    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},
50	    journal   = {Computing Research Repository},
51	    volume    = {arXiv:1503.06733},
52	    year      = {2015},
53	    url       = {http://arxiv.org/abs/1503.06733},
54	    note    = {version 2}
55	}
56	
57	@article{Ando2005,
58		Acmid = {1194905},
59		Author = {Ando, Rie Kubota and Zhang, Tong},
60		Issn = {1532-4435},
61		Issue_Date = {12/1/2005},
62		Journal = {Journal of Machine Learning Research},
63		Month = dec,
64		Numpages = {37},
65		Pages = {1817--1853},
66		Publisher = {JMLR.org},
67		Title = {A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data},
68		Volume = {6},
69		Year = {2005}
70	}
71	
72	% [TO_ADD_BIB] -- Verified citations added for Related Work section
73	
74	@article{kadavath2022language,
75	    title={Language Models (Mostly) Know What They Know},
76	    author={Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DaSilva, Nova and Tran-Johnson, Eli and others},
77	    journal={arXiv preprint arXiv:2207.05221},
78	    year={2022}
79	}
80	
81	@inproceedings{niculescu2005predicting,
82	    title={Predicting Good Probabilities with Supervised Learning},
83	    author={Niculescu-Mizil, Alexandru and Caruana, Rich},
84	    booktitle={Proceedings of the 22nd International Conference on Machine Learning},
85	    pages={625--632},
86	    year={2005},
87	    doi={10.1145/1102351.1102430}
88	}
89	
90	@inproceedings{conneau2018muse,
91	    title={Word Translation Without Parallel Data},
92	    author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\'e}gou, Herv{\'e}},
93	    booktitle={International Conference on Learning Representations},
94	    year={2018}
95	}
96	
97	@inproceedings{artetxe2018vecmap,
98	    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},
99	    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},
100	    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
101	    pages={789--798},
102	    year={2018}
103	}
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "0261ed63-5e8d-4cad-b350-6a56bb6b7b33",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib",
      "content": "% Use this file for citations not found in the ACL Anthology (contained in \"anthology.bib\").\n\n@book{Aho:72,\n    author  = {Alfred V. Aho and Jeffrey D. Ullman},\n    title   = {The Theory of Parsing, Translation and Compiling},\n    year    = \"1972\",\n    volume  = \"1\",\n    publisher = {Prentice-Hall},\n    address = {Englewood Cliffs, NJ}\n}\n\n@book{APA:83,\n    author  = {{American Psychological Association}},\n    title   = {Publications Manual},\n    year    = \"1983\",\n    publisher = {American Psychological Association},\n    address = {Washington, DC}\n}\n\n@article{Chandra:81,\n\tauthor = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},\n\tyear = \"1981\",\n\ttitle = {Alternation},\n\tjournal = {Journal of the Association for Computing Machinery},\n\tvolume = \"28\",\n\tnumber = \"1\",\n\tpages = \"114--133\",\n\tdoi = \"10.1145/322234.322243\",\n}\n\n@inproceedings{andrew2007scalable,\n  title={Scalable training of {L1}-regularized log-linear models},\n  author={Andrew, Galen and Gao, Jianfeng},\n  booktitle={Proceedings of the 24th International Conference on Machine Learning},\n  pages={33--40},\n  year={2007},\n}\n\n@book{Gusfield:97,\n    author  = {Dan Gusfield},\n    title   = {Algorithms on Strings, Trees and Sequences},\n    year    = \"1997\",\n    publisher = {Cambridge University Press},\n    address = {Cambridge, UK}\n}\n\n@article{rasooli-tetrault-2015,\n    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},\n    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},\n    journal   = {Computing Research Repository},\n    volume    = {arXiv:1503.06733},\n    year      = {2015},\n    url       = {http://arxiv.org/abs/1503.06733},\n    note    = {version 2}\n}\n\n@article{Ando2005,\n\tAcmid = {1194905},\n\tAuthor = {Ando, Rie Kubota and Zhang, Tong},\n\tIssn = {1532-4435},\n\tIssue_Date = {12/1/2005},\n\tJournal = {Journal of Machine Learning Research},\n\tMonth = dec,\n\tNumpages = {37},\n\tPages = {1817--1853},\n\tPublisher = {JMLR.org},\n\tTitle = {A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data},\n\tVolume = {6},\n\tYear = {2005}\n}\n\n% [TO_ADD_BIB] -- Verified citations added for Related Work section\n\n@article{kadavath2022language,\n    title={Language Models (Mostly) Know What They Know},\n    author={Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DaSilva, Nova and Tran-Johnson, Eli and others},\n    journal={arXiv preprint arXiv:2207.05221},\n    year={2022}\n}\n\n@inproceedings{niculescu2005predicting,\n    title={Predicting Good Probabilities with Supervised Learning},\n    author={Niculescu-Mizil, Alexandru and Caruana, Rich},\n    booktitle={Proceedings of the 22nd International Conference on Machine Learning},\n    pages={625--632},\n    year={2005},\n    doi={10.1145/1102351.1102430}\n}\n\n@inproceedings{conneau2018muse,\n    title={Word Translation Without Parallel Data},\n    author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\\'e}gou, Herv{\\'e}},\n    booktitle={International Conference on Learning Representations},\n    year={2018}\n}\n\n@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01KkGg4KY8ucmbg823c4efV1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "a1d38838-6ccb-485c-a061-c2e114c71773",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013W99tdk6WZGQCeEcNnKTFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T07:37:21.484Z_

<details><summary>↩ Tool result · `toolu_01KkGg4KY8ucmbg823c4efV1`</summary>

```text
1	% Requires: \usepackage{pifont} \newcommand{\cmark}{\ding{51}} \newcommand{\xmark}{\ding{55}}
2	% Requires: \usepackage{booktabs}
3	
4	\section{Related Work}
5	
6	\subsection{LLM Calibration and Internal Representations}
7	
8	Post-hoc calibration methods such as temperature scaling \cite{guo2017calibration} and Platt scaling \cite{niculescu2005predicting} treat model confidence as a scalar output to be recalibrated after training. These approaches assume access to a held-out validation set from the target distribution and operate entirely on output logits without inspecting internal representations.
9	A complementary line of work examines whether models can self-assess correctness through verbalized confidence. \citet{kadavath2022language} demonstrate that larger language models produce well-calibrated probability estimates when asked to evaluate their own answers, establishing that calibration information exists within the model prior to output generation.
10	
11	Recent studies shift attention from output-level calibration to representation-level probing. \citet{miao2026closing} identify that correctness and verbalized confidence occupy nearly orthogonal subspaces in hidden states (cosine similarity below 0.04), suggesting that standard confidence elicitation fails to capture the full calibration signal. Building on this observation, CORAL \cite{miao2026coral} trains correctness probes that transfer across tasks within English, achieving approximately 50\% ECE improvement over verbalized confidence baselines. CCPS \cite{khanmohammadi2025ccps} takes a complementary approach by measuring representation stability under input perturbations as a proxy for correctness. The Confidence Manifold framework \cite{confidence_manifold2026} reveals that calibration-relevant information concentrates in a low-dimensional subspace (3 to 8 dimensions), with as few as 25 labeled examples sufficient for 89\% probing accuracy. \citet{ji2025calibrating} further demonstrate that verbal uncertainty in LLMs corresponds to a linear direction in representation space, while \citet{joshi2025calibration} analyze how calibration signals evolve across layers, finding non-monotonic patterns that motivate layer selection.
12	
13	All of these studies operate exclusively in English and on a single model architecture. Our work extends correctness probing to 20 languages across 2 model families, revealing that transfer quality varies substantially across languages and architectures.
14	
15	\subsection{Cross-Lingual Probing and Transfer}
16	
17	Cross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.
18	
19	The technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \cite{wu2019beto}. % [TO_ADD_BIB]
20	\citet{liu2025middle} show that middle layers of fine-tuned LLMs exhibit stronger cross-lingual alignment than early or late layers, consistent with the depth patterns we observe for correctness probes.
21	
22	Our work differs in three respects: we probe correctness (an output-dependent signal that requires generating and evaluating answers), we provide systematic depth analysis with Pareto frontier characterization across architectures, and we evaluate 5 transfer methods (including linear projection inspired by MUSE/VecMap) across 20 languages.
23	
24	\subsection{Multilingual Calibration}
25	
26	Calibration quality varies dramatically across languages. \citet{zhou2025lace} document a 5$\times$ ECE gap between English and low-resource languages across 100+ languages and propose LACE, an adaptive layer ensemble that selects different layer combinations per language. While effective, LACE requires per-language validation data with correctness labels, limiting applicability to languages where such annotations exist.
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\caption{Comparison with closely related work on calibration probing and cross-lingual transfer. Target signals: KB = knowledge boundary, Corr.\ = correctness, Diff.\ = difficulty. Zero-CL = zero target-language correctness labels required.}
32	\label{tab:related_work}
33	\begin{tabular}{lcccccc}
34	\toprule
35	& \textbf{Target} & \textbf{\# Langs} & \textbf{Calib.} & \textbf{Zero-CL} & \textbf{Depth} & \textbf{Transfer} \\
36	& \textbf{Signal} & & \textbf{Metrics} & \textbf{Labels} & \textbf{Analysis} & \textbf{Methods} \\
37	\midrule
38	Xiao et al. & KB & 8 & \xmark & \cmark & \xmark & 1 \\
39	LACE & -- & 100+ & \cmark & \xmark & partial & -- \\
40	CORAL & Corr. & 1 & \cmark & -- & \cmark & 1 \\
41	Miao \& Ungar & Corr. & 1 & \xmark & -- & \xmark & -- \\
42	Civelli et al. & Diff. & 7 & \xmark & \cmark & \cmark & 1 \\
43	\midrule
44	\textbf{Ours} & \textbf{Corr.} & \textbf{20} & \cmark & \cmark & \cmark & \textbf{5} \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	The fundamental challenge that LACE addresses (per-language calibration heterogeneity) motivates our investigation, but our approach differs in both goal and mechanism. We analyze \emph{why} cross-lingual transfer of correctness probes fails (architecture-dependent depth-transferability tradeoffs, geometric divergence measured by CKA) rather than engineering a per-language compensation. Our method requires zero target-language correctness labels, transferring probes trained on English data alone.
50	
51	\subsection{Domain Adaptation Theory}
52	
53	The theoretical framework of \citet{bendavid2010theory} bounds target-domain error by source error plus a divergence term ($\mathcal{H}$-divergence) between source and target distributions, plus a joint ideal error. Applied to cross-lingual probe transfer, this predicts degradation proportional to the representational distance between languages. \citet{zhao2019invariant} prove a stronger negative result: when conditional distributions $P(Y|X)$ differ between domains, matching marginal distributions of representations can \emph{increase} target error rather than reduce it.
54	
55	This theoretical insight directly explains our empirical finding on CaCLR (Cross-lingual Calibration via Conditional Label-aware Representation matching). CaCLR applies MMD-based distributional matching to align probe logit distributions across languages. If distributional matching proves insufficient (pending experimental validation), this would align with the prediction of \citet{zhao2019invariant}: because conditional accuracy distributions $P(\text{correct}|\mathbf{h})$ differ between languages (due to varying model competence), marginal alignment may destroy the conditional structure that probes rely on. Our CKA partial correlation analysis further reveals a Simpson's Paradox where aggregate cross-lingual similarity masks within-layer divergence, a confounding pattern that naive cross-layer pooling obscures.
56	
57	\subsection{Probing Methodology and Evaluation}
58	
59	The methodological foundations of representation probing inform our experimental design. \citet{hewitt2019control} introduce control tasks that establish selectivity baselines, guarding against probes that succeed merely due to high capacity rather than genuine information in representations. \citet{voita2020mdl} propose minimum description length probes as an information-theoretic alternative, measuring the amount of effort required to extract a property. \citet{belinkov2022probing} surveys the broader landscape of probing classifiers, identifying best practices and common pitfalls including the capacity-informativeness tradeoff.
60	
61	We apply the control task framework of \citet{hewitt2019control} to cross-lingual correctness probing. English probing controls (Hewitt \& Liang selectivity) reveal layer-dependent selectivity patterns, with selectivity concentrated in deeper layers (L20+) --- raising concerns that shallow-layer positive results in low-resource languages may partly reflect capacity artifacts rather than genuine correctness signal. Cross-lingual control experiments are planned to quantify this. For measuring representational similarity across languages and layers, we employ CKA \cite{kornblith2019cka} with partial correlation analysis, revealing geometric structure invisible to standard pairwise comparisons. Conformal prediction \cite{angelopoulos2023conformal} offers distribution-free coverage guarantees complementary to our probing approach but requires per-language calibration data, which our zero-correctness-label setting explicitly avoids.
62	
63	Our work contributes the first systematic application of probing controls to cross-lingual transfer evaluation and applies CKA with depth-controlled partial correlation as a diagnostic for understanding transfer failure modes.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "d5a545ef-36b2-4638-813f-ead4169c8ae1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
      "content": "% Requires: \\usepackage{pifont} \\newcommand{\\cmark}{\\ding{51}} \\newcommand{\\xmark}{\\ding{55}}\n% Requires: \\usepackage{booktabs}\n\n\\section{Related Work}\n\n\\subsection{LLM Calibration and Internal Representations}\n\nPost-hoc calibration methods such as temperature scaling \\cite{guo2017calibration} and Platt scaling \\cite{niculescu2005predicting} treat model confidence as a scalar output to be recalibrated after training. These approaches assume access to a held-out validation set from the target distribution and operate entirely on output logits without inspecting internal representations.\nA complementary line of work examines whether models can self-assess correctness through verbalized confidence. \\citet{kadavath2022language} demonstrate that larger language models produce well-calibrated probability estimates when asked to evaluate their own answers, establishing that calibration information exists within the model prior to output generation.\n\nRecent studies shift attention from output-level calibration to representation-level probing. \\citet{miao2026closing} identify that correctness and verbalized confidence occupy nearly orthogonal subspaces in hidden states (cosine similarity below 0.04), suggesting that standard confidence elicitation fails to capture the full calibration signal. Building on this observation, CORAL \\cite{miao2026coral} trains correctness probes that transfer across tasks within English, achieving approximately 50\\% ECE improvement over verbalized confidence baselines. CCPS \\cite{khanmohammadi2025ccps} takes a complementary approach by measuring representation stability under input perturbations as a proxy for correctness. The Confidence Manifold framework \\cite{confidence_manifold2026} reveals that calibration-relevant information concentrates in a low-dimensional subspace (3 to 8 dimensions), with as few as 25 labeled examples sufficient for 89\\% probing accuracy. \\citet{ji2025calibrating} further demonstrate that verbal uncertainty in LLMs corresponds to a linear direction in representation space, while \\citet{joshi2025calibration} analyze how calibration signals evolve across layers, finding non-monotonic patterns that motivate layer selection.\n\nAll of these studies operate exclusively in English and on a single model architecture. Our work extends correctness probing to 20 languages across 2 model families, revealing that transfer quality varies substantially across languages and architectures.\n\n\\subsection{Cross-Lingual Probing and Transfer}\n\nCross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \\citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \\cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.\n\nThe technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \\cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \\cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]\n\\citet{liu2025middle} show that middle layers of fine-tuned LLMs exhibit stronger cross-lingual alignment than early or late layers, consistent with the depth patterns we observe for correctness probes.\n\nOur work differs in three respects: we probe correctness (an output-dependent signal that requires generating and evaluating answers), we provide systematic depth analysis with Pareto frontier characterization across architectures, and we evaluate 5 transfer methods (including linear projection inspired by MUSE/VecMap) across 20 languages.\n\n\\subsection{Multilingual Calibration}\n\nCalibration quality varies dramatically across languages. \\citet{zhou2025lace} document a 5$\\times$ ECE gap between English and low-resource languages across 100+ languages and propose LACE, an adaptive layer ensemble that selects different layer combinations per language. While effective, LACE requires per-language validation data with correctness labels, limiting applicability to languages where such annotations exist.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison with closely related work on calibration probing and cross-lingual transfer. Target signals: KB = knowledge boundary, Corr.\\ = correctness, Diff.\\ = difficulty. Zero-CL = zero target-language correctness labels required.}\n\\label{tab:related_work}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\textbf{Target} & \\textbf{\\# Langs} & \\textbf{Calib.} & \\textbf{Zero-CL} & \\textbf{Depth} & \\textbf{Transfer} \\\\\n& \\textbf{Signal} & & \\textbf{Metrics} & \\textbf{Labels} & \\textbf{Analysis} & \\textbf{Methods} \\\\\n\\midrule\nXiao et al. & KB & 8 & \\xmark & \\cmark & \\xmark & 1 \\\\\nLACE & -- & 100+ & \\cmark & \\xmark & partial & -- \\\\\nCORAL & Corr. & 1 & \\cmark & -- & \\cmark & 1 \\\\\nMiao \\& Ungar & Corr. & 1 & \\xmark & -- & \\xmark & -- \\\\\nCivelli et al. & Diff. & 7 & \\xmark & \\cmark & \\cmark & 1 \\\\\n\\midrule\n\\textbf{Ours} & \\textbf{Corr.} & \\textbf{20} & \\cmark & \\cmark & \\cmark & \\textbf{5} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe fundamental challenge that LACE addresses (per-language calibration heterogeneity) motivates our investigation, but our approach differs in both goal and mechanism. We analyze \\emph{why} cross-lingual transfer of correctness probes fails (architecture-dependent depth-transferability tradeoffs, geometric divergence measured by CKA) rather than engineering a per-language compensation. Our method requires zero target-language correctness labels, transferring probes trained on English data alone.\n\n\\subsection{Domain Adaptation Theory}\n\nThe theoretical framework of \\citet{bendavid2010theory} bounds target-domain error by source error plus a divergence term ($\\mathcal{H}$-divergence) between source and target distributions, plus a joint ideal error. Applied to cross-lingual probe transfer, this predicts degradation proportional to the representational distance between languages. \\citet{zhao2019invariant} prove a stronger negative result: when conditional distributions $P(Y|X)$ differ between domains, matching marginal distributions of representations can \\emph{increase} target error rather than reduce it.\n\nThis theoretical insight directly explains our empirical finding on CaCLR (Cross-lingual Calibration via Conditional Label-aware Representation matching). CaCLR applies MMD-based distributional matching to align probe logit distributions across languages. If distributional matching proves insufficient (pending experimental validation), this would align with the prediction of \\citet{zhao2019invariant}: because conditional accuracy distributions $P(\\text{correct}|\\mathbf{h})$ differ between languages (due to varying model competence), marginal alignment may destroy the conditional structure that probes rely on. Our CKA partial correlation analysis further reveals a Simpson's Paradox where aggregate cross-lingual similarity masks within-layer divergence, a confounding pattern that naive cross-layer pooling obscures.\n\n\\subsection{Probing Methodology and Evaluation}\n\nThe methodological foundations of representation probing inform our experimental design. \\citet{hewitt2019control} introduce control tasks that establish selectivity baselines, guarding against probes that succeed merely due to high capacity rather than genuine information in representations. \\citet{voita2020mdl} propose minimum description length probes as an information-theoretic alternative, measuring the amount of effort required to extract a property. \\citet{belinkov2022probing} surveys the broader landscape of probing classifiers, identifying best practices and common pitfalls including the capacity-informativeness tradeoff.\n\nWe apply the control task framework of \\citet{hewitt2019control} to cross-lingual correctness probing. English probing controls (Hewitt \\& Liang selectivity) reveal layer-dependent selectivity patterns, with selectivity concentrated in deeper layers (L20+) --- raising concerns that shallow-layer positive results in low-resource languages may partly reflect capacity artifacts rather than genuine correctness signal. Cross-lingual control experiments are planned to quantify this. For measuring representational similarity across languages and layers, we employ CKA \\cite{kornblith2019cka} with partial correlation analysis, revealing geometric structure invisible to standard pairwise comparisons. Conformal prediction \\cite{angelopoulos2023conformal} offers distribution-free coverage guarantees complementary to our probing approach but requires per-language calibration data, which our zero-correctness-label setting explicitly avoids.\n\nOur work contributes the first systematic application of probing controls to cross-lingual transfer evaluation and applies CKA with depth-controlled partial correlation as a diagnostic for understanding transfer failure modes.\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01VtLz63HEFX3v3tmJyK5Dzd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "1e4643ac-899c-409d-8e35-8b1aa865eac9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013W99tdk6WZGQCeEcNnKTFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T07:37:21.761Z_

<details><summary>↩ Tool result · `toolu_01VtLz63HEFX3v3tmJyK5Dzd`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:problem}
6	
7	Given a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at layer $l$. A \emph{correctness probe} is a linear classifier
8	\begin{equation}
9	  f_l(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)
10	  \label{eq:probe}
11	\end{equation}
12	trained to predict $p(\text{correct} \mid \mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.
13	
14	We distinguish correctness probing from two related tasks. \emph{Knowledge boundary probing} \citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \emph{Difficulty probing} \citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.
15	
16	\subsection{Experimental Framework}
17	\label{sec:framework}
18	
19	\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).
20	
21	\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \textsc{med} (ar, id, nl, pl, tr, uk, vi), and \textsc{low} (bn, hi, sw, te).
22	
23	\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \texttt{probe\_train} and \texttt{eval} portions. English binary correctness labels come from \texttt{probe\_train} only; all reported results use \texttt{eval} exclusively.
24	
25	\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer plus the final layer for all models, yielding 8--25 probed layers depending on architecture depth). We use 4-bit quantization (GPTQ-Int4 for Qwen3, W4A16 for Llama 4 Scout) and include a higher-precision validation ablation at representative layers to control for quantization artifacts.
26	
27	\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Soft-Binned ECE (SB-ECE) \citep{karandikar2021sbece} for calibration quality, and selectivity \citep{hewitt2019control}. Standard ECE (10-bin) and Brier score are reported in the Appendix. % [TO_ADD_BIB]
28	
29	\subsection{Transfer Methods}
30	\label{sec:transfer}
31	
32	We compare five methods ordered by complexity.
33	
34	\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.
35	
36	\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\boldsymbol{\delta} = \boldsymbol{\mu}_{\text{en}} - \boldsymbol{\mu}_t$ from target activations before applying the English probe.
37	
38	\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \mu_{\text{en},i}) / \sigma_{\text{en},i}$. After mean-shift, the target representation becomes $h_i + \delta_i$, and the scaled value is
39	\begin{equation}
40	  z'_i = \frac{h_i + \delta_i - \mu_{\text{en},i}}{\sigma_{\text{en},i}} = z_i + c_i
41	  \label{eq:meanshift}
42	\end{equation}
43	where $c_i = \delta_i / \sigma_{\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\mathbf{w}^\top \mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\Delta\text{AUROC} \equiv 0$. Our MVP experiments confirm this prediction exactly ($\Delta\text{AUROC} = 0.000000$ across 5 languages $\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.
44	
45	\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving
46	\begin{equation}
47	  \mathbf{R}^* = \arg\min_{\mathbf{R}^\top\mathbf{R}=\mathbf{I}} \|\mathbf{X}_t\mathbf{R} - \mathbf{X}_{\text{en}}\|_F
48	  \label{eq:procrustes}
49	\end{equation}
50	following cross-lingual word embedding alignment methods such as MUSE \citep{conneau2018muse} and VecMap \citep{artetxe2018vecmap}. % [TO_ADD_BIB]
51	Approximately 50 parallel pairs achieve 98\% of 200-pair performance. Resource tier matters: \textsc{high}-resource languages saturate at ${\sim}$20 pairs and \textsc{low}-resource at ${\sim}$50. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.
52	
53	\paragraph{(d) Few-shot probe training.} We combine the full English training data with 25, 50, or 100 target-language labeled examples and retrain the probe. This requires target-language correctness labels and serves as an upper-bound reference.
54	
55	\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:
56	\begin{equation}
57	  \mathcal{L} = \mathcal{L}_{\text{BCE}} + \alpha \cdot \mathcal{L}_{\text{SB-ECE}} + \beta \cdot \mathcal{L}_{\text{consistency}}
58	  \label{eq:caclr}
59	\end{equation}
60	$\mathcal{L}_{\text{BCE}}$ is standard binary cross-entropy on English \texttt{probe\_train} labels. $\mathcal{L}_{\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\mathcal{L}_{\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\mathbf{w}^\top \mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \S\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \texttt{probe\_train} portion (70\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\alpha$ and $\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.
61	
62	\subsection{Difficulty-Capability Decomposition}
63	\label{sec:decomposition}
64	
65	We train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:
66	\begin{equation}
67	  \mathbf{h}_l^{\text{res}} = \mathbf{h}_l - (\mathbf{h}_l \cdot \hat{\mathbf{w}}_{\text{diff}})\hat{\mathbf{w}}_{\text{diff}}
68	  \label{eq:residual}
69	\end{equation}
70	where $\hat{\mathbf{w}}_{\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\mathbf{h}_l^{\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.
71	
72	\subsection{Geometric Analysis}
73	\label{sec:geometric}
74	
75	We quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \citep{kornblith2019cka}. % [TO_ADD_BIB]
76	The central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations are positive (8 layers from Qwen2.5-7B + 9 layers from Llama-3.1-8B pilot models)). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.
77	
78	\subsection{Probing Controls}
79	\label{sec:controls}
80	
81	We validate probe quality with the control task framework of \citet{hewitt2019control}. % [TO_ADD_BIB]
82	Selectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot control task analysis on English (Qwen2.5-7B, 8 probed layers) shows selectivity concentrated in deeper layers: L20+ selectivity $> 0.20$, while shallow layers (L0--L12) show selectivity $< 0.05$, indicating that positive AUROC at shallow layers likely reflects capacity artifacts rather than genuine linguistic signal. Cross-lingual control experiments are planned to determine whether this pattern generalizes across target languages.
83	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "f108ed23-b74d-4509-b2ec-2aa407524d99",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$. A \\emph{correctness probe} is a linear classifier\n\\begin{equation}\n  f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)\n  \\label{eq:probe}\n\\end{equation}\ntrained to predict $p(\\text{correct} \\mid \\mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.\n\nWe distinguish correctness probing from two related tasks. \\emph{Knowledge boundary probing} \\citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \\emph{Difficulty probing} \\citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.\n\n\\subsection{Experimental Framework}\n\\label{sec:framework}\n\n\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).\n\n\\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \\textsc{med} (ar, id, nl, pl, tr, uk, vi), and \\textsc{low} (bn, hi, sw, te).\n\n\\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions. English binary correctness labels come from \\texttt{probe\\_train} only; all reported results use \\texttt{eval} exclusively.\n\n\\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer plus the final layer for all models, yielding 8--25 probed layers depending on architecture depth). We use 4-bit quantization (GPTQ-Int4 for Qwen3, W4A16 for Llama 4 Scout) and include a higher-precision validation ablation at representative layers to control for quantization artifacts.\n\n\\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Soft-Binned ECE (SB-ECE) \\citep{karandikar2021sbece} for calibration quality, and selectivity \\citep{hewitt2019control}. Standard ECE (10-bin) and Brier score are reported in the Appendix. % [TO_ADD_BIB]\n\n\\subsection{Transfer Methods}\n\\label{sec:transfer}\n\nWe compare five methods ordered by complexity.\n\n\\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.\n\n\\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\\boldsymbol{\\delta} = \\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ from target activations before applying the English probe.\n\n\\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \\mu_{\\text{en},i}) / \\sigma_{\\text{en},i}$. After mean-shift, the target representation becomes $h_i + \\delta_i$, and the scaled value is\n\\begin{equation}\n  z'_i = \\frac{h_i + \\delta_i - \\mu_{\\text{en},i}}{\\sigma_{\\text{en},i}} = z_i + c_i\n  \\label{eq:meanshift}\n\\end{equation}\nwhere $c_i = \\delta_i / \\sigma_{\\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\\mathbf{w}^\\top \\mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\\Delta\\text{AUROC} \\equiv 0$. Our MVP experiments confirm this prediction exactly ($\\Delta\\text{AUROC} = 0.000000$ across 5 languages $\\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.\n\n\\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving\n\\begin{equation}\n  \\mathbf{R}^* = \\arg\\min_{\\mathbf{R}^\\top\\mathbf{R}=\\mathbf{I}} \\|\\mathbf{X}_t\\mathbf{R} - \\mathbf{X}_{\\text{en}}\\|_F\n  \\label{eq:procrustes}\n\\end{equation}\nfollowing cross-lingual word embedding alignment methods such as MUSE \\citep{conneau2018muse} and VecMap \\citep{artetxe2018vecmap}. % [TO_ADD_BIB]\nApproximately 50 parallel pairs achieve 98\\% of 200-pair performance. Resource tier matters: \\textsc{high}-resource languages saturate at ${\\sim}$20 pairs and \\textsc{low}-resource at ${\\sim}$50. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.\n\n\\paragraph{(d) Few-shot probe training.} We combine the full English training data with 25, 50, or 100 target-language labeled examples and retrain the probe. This requires target-language correctness labels and serves as an upper-bound reference.\n\n\\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n  \\label{eq:caclr}\n\\end{equation}\n$\\mathcal{L}_{\\text{BCE}}$ is standard binary cross-entropy on English \\texttt{probe\\_train} labels. $\\mathcal{L}_{\\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \\citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \\emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\\mathbf{w}^\\top \\mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \\S\\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \\texttt{probe\\_train} portion (70\\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\\alpha$ and $\\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomposition}\n\nWe train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:\n\\begin{equation}\n  \\mathbf{h}_l^{\\text{res}} = \\mathbf{h}_l - (\\mathbf{h}_l \\cdot \\hat{\\mathbf{w}}_{\\text{diff}})\\hat{\\mathbf{w}}_{\\text{diff}}\n  \\label{eq:residual}\n\\end{equation}\nwhere $\\hat{\\mathbf{w}}_{\\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\\mathbf{h}_l^{\\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.\n\n\\subsection{Geometric Analysis}\n\\label{sec:geometric}\n\nWe quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \\citep{kornblith2019cka}. % [TO_ADD_BIB]\nThe central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations are positive (8 layers from Qwen2.5-7B + 9 layers from Llama-3.1-8B pilot models)). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nWe validate probe quality with the control task framework of \\citet{hewitt2019control}. % [TO_ADD_BIB]\nSelectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot control task analysis on English (Qwen2.5-7B, 8 probed layers) shows selectivity concentrated in deeper layers: L20+ selectivity $> 0.20$, while shallow layers (L0--L12) show selectivity $< 0.05$, indicating that positive AUROC at shallow layers likely reflects capacity artifacts rather than genuine linguistic signal. Cross-lingual control experiments are planned to determine whether this pattern generalizes across target languages.\n",
      "numLines": 83,
      "startLine": 1,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of the existing files. Let me now search for the 2025-2026 papers that need verification. I'll launch parallel web searches for the papers that need verification.

Let me load the WebSearch tool first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "d4297871-e886-47da-9540-dcc3866cdbb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SK5SBPaBpndL8QrjioDoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 25373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7513
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 12_

Now I'll search for the 2025-2026 papers that need verification. Let me load the WebSearch tool first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "3987b556-6e9b-4c88-990b-ae067fc75528",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SK5SBPaBpndL8QrjioDoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 25373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7513
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RsyZfgsEi3X7pjse7ZBL55`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "f75f5dcd-6caa-477c-8901-34c464bf994e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SK5SBPaBpndL8QrjioDoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7513,
      "cache_read_input_tokens": 25373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7513
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T07:37:26.355Z_

<details><summary>↩ Tool result · `toolu_01RsyZfgsEi3X7pjse7ZBL55`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "522377a1-67b8-49b7-a0de-be428bb8efe5",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the 2025-2026 papers in parallel. I'll batch the searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "804f6b4e-2a6c-493e-b685-c6097b7c461f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 16_

Searching for the 2025-2026 papers that need verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "546195f6-218f-4494-817b-f725f9f9a37c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Twio86VujwFfarrnkEz6Vq`</summary>

```json
{
  "query": "Xiao \"knowledge boundary\" cross-lingual probe transfer ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "c64f8293-241e-4d0b-94b3-7bd9a611b8f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T6RxCxA3CR4wYkhvSd5mXQ`</summary>

```json
{
  "query": "Zhou LACE adaptive layer ensemble multilingual calibration 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b39c6dce-4aaf-47e8-b61e-dd30cb483d16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BCkxnq3gHS2JA23cQADtQk`</summary>

```json
{
  "query": "Miao Ungar \"correctness-confidence orthogonality\" 2026 LLM representations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "7aff97ef-83bd-4e81-ac02-d2bedc18aa73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MqBVuuQehwG2VHFCSN5mkd`</summary>

```json
{
  "query": "Miao CORAL cross-task correctness probes 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8d751555-c291-479d-9e36-68d3f2a17868",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QchFTwSuvD6kmsxV35NjWJ`</summary>

```json
{
  "query": "Khanmohammadi CCPS perturbation stability calibration 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "30ef313e-f49c-4bd0-aa6c-4e2ec03435aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Niye8iEUY5PCVQgeYLt4r8`</summary>

```json
{
  "query": "\"Confidence Manifold\" framework LLM calibration low-dimensional subspace 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "684b98d7-23af-41c5-9b56-f8aa2ac88f30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0122yD6TiCpgveH4mdmo6T9c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 32886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
      },
      "output_tokens": 38,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-21T07:37:39.218Z_

<details><summary>↩ Tool result · `toolu_01T6RxCxA3CR4wYkhvSd5mXQ`</summary>

```text
Web search results for query: "Zhou LACE adaptive layer ensemble multilingual calibration 2025"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136v1"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=CUS9OTCGdt"},{"title":"Post-Training Quantization Methods","url":"https://www.emergentmind.com/topics/post-training-quantization-methods"},{"title":"Ivan Vulić's research works | University of Cambridge and other places","url":"https://researchgate.net/scientific-contributions/2034162457_Ivan_Vulic"},{"title":"Accepted Submissions | MELT Workshop @ COLM 2025","url":"https://melt-workshop.github.io/papers/"}]

I found the research paper you're looking for. Here's what the search revealed:

Zhou's work introduces Language-Aware Confidence Ensemble (LACE), a training-free method that adaptively selects an optimal ensemble of layers for each specific language.

The research addresses an important problem: the study conducts large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration.

The key insight behind LACE is that late-intermediate layers consistently offer a more reliable and better-calibrated signal compared to the final layer, which is biased by English-centric training and provides a poor signal for multilingual confidence.

LACE is effective because per-language layer selection avoids negative transfer from layers that are miscalibrated for the target language, and ensembling over the selected layers reduces variance while preserving language-relevant signals.

The paper was published on arXiv in October 2025 and is titled "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b0fa1306-5bd0-4d6b-9bdd-8508a4ac80bb",
  "tool_use_result": {
    "query": "Zhou LACE adaptive layer ensemble multilingual calibration 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01558qDqz9FCjzWkrqQbHC8M",
        "content": [
          {
            "title": "[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2510.03136"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136v1"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://www.researchgate.net/publication/396223351_Beyond_the_Final_Layer_Intermediate_Representations_for_Better_Multilingual_Calibration_in_Large_Language_Models"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=CUS9OTCGdt"
          },
          {
            "title": "Post-Training Quantization Methods",
            "url": "https://www.emergentmind.com/topics/post-training-quantization-methods"
          },
          {
            "title": "Ivan Vulić's research works | University of Cambridge and other places",
            "url": "https://researchgate.net/scientific-contributions/2034162457_Ivan_Vulic"
          },
          {
            "title": "Accepted Submissions | MELT Workshop @ COLM 2025",
            "url": "https://melt-workshop.github.io/papers/"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what the search revealed:\n\nZhou's work introduces Language-Aware Confidence Ensemble (LACE), a training-free method that adaptively selects an optimal ensemble of layers for each specific language.\n\nThe research addresses an important problem: the study conducts large-scale, systematic studies of multilingual calibration across six model families and over 100 languages, revealing that non-English languages suffer from systematically worse calibration.\n\nThe key insight behind LACE is that late-intermediate layers consistently offer a more reliable and better-calibrated signal compared to the final layer, which is biased by English-centric training and provides a poor signal for multilingual confidence.\n\nLACE is effective because per-language layer selection avoids negative transfer from layers that are miscalibrated for the target language, and ensembling over the selected layers reduces variance while preserving language-relevant signals.\n\nThe paper was published on arXiv in October 2025 and is titled \"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models.\""
    ],
    "durationSeconds": 5.439120321999999
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T07:37:39.392Z_

<details><summary>↩ Tool result · `toolu_01QchFTwSuvD6kmsxV35NjWJ`</summary>

```text
Web search results for query: "Khanmohammadi CCPS perturbation stability calibration 2025"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Reza Khan Mohammadi","url":"https://www.khanmohammadi.me/"},{"title":"Reza KHANMOHAMMADI | Student | Doctor of Philosophy | Michigan State University, East Lansing | MSU | Department of Computer Science and Engineering | Research profile","url":"https://www.researchgate.net/profile/Reza-Khanmohammadi"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News","url":"https://news.ycombinator.com/item?id=45055315"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"}]

Based on the search results, here's what I found about this research:

## Overview

CCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method that analyzes internal representational stability in LLMs by applying targeted adversarial perturbations to final hidden states, extracting features reflecting the model's response to these perturbations, and using a lightweight classifier to predict answer correctness.

## Key Results

Across four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points.

## Publication and Recognition

The work was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. It was nominated for the Outstanding Paper Award, placing in the top 0.4% of 8,174 submissions.

## Evaluation Scope

CCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "4f5a71d2-2300-42fe-b5c6-2acb184b2a6c",
  "tool_use_result": {
    "query": "Khanmohammadi CCPS perturbation stability calibration 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XqSeS4nXsmxoZ1bMDurxD6",
        "content": [
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.530/"
          },
          {
            "title": "GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://github.com/ledengary/CCPS"
          },
          {
            "title": "Reza Khan Mohammadi",
            "url": "https://www.khanmohammadi.me/"
          },
          {
            "title": "Reza KHANMOHAMMADI | Student | Doctor of Philosophy | Michigan State University, East Lansing | MSU | Department of Computer Science and Engineering | Research profile",
            "url": "https://www.researchgate.net/profile/Reza-Khanmohammadi"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF",
            "url": "https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/html/2505.21772v1"
          },
          {
            "title": "CCPS: Calibrating LLM Confidence via Perturbation Stability – EMNLP 2025 | Hacker News",
            "url": "https://news.ycombinator.com/item?id=45055315"
          },
          {
            "title": "[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/abs/2505.21772"
          }
        ]
      },
      "Based on the search results, here's what I found about this research:\n\n## Overview\n\nCCPS (Calibrating LLM Confidence by Probing Perturbed Representation Stability) is a novel method that analyzes internal representational stability in LLMs by applying targeted adversarial perturbations to final hidden states, extracting features reflecting the model's response to these perturbations, and using a lightweight classifier to predict answer correctness.\n\n## Key Results\n\nAcross four LLMs and three MMLU variants, CCPS reduces Expected Calibration Error by approximately 55% and Brier score by 21%, while increasing accuracy by 5 percentage points, Area Under the Precision-Recall Curve by 4 percentage points, and Area Under the Receiver Operating Characteristic Curve by 6 percentage points.\n\n## Publication and Recognition\n\nThe work was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing. It was nominated for the Outstanding Paper Award, placing in the top 0.4% of 8,174 submissions.\n\n## Evaluation Scope\n\nCCPS was evaluated on LLMs from 8B to 32B parameters (covering Llama, Qwen, and Mistral architectures) using MMLU and MMLU-Pro benchmarks in both multiple-choice and open-ended formats."
    ],
    "durationSeconds": 5.006802238000001
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-21T07:37:40.296Z_

<details><summary>↩ Tool result · `toolu_01Twio86VujwFfarrnkEz6Vq`</summary>

```text
Web search results for query: "Xiao "knowledge boundary" cross-lingual probe transfer ACL 2025"

Links: [{"title":"GitHub - DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries: [ACL 2025] Analyzing LLMs' Multilingual Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations","url":"https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries"},{"title":"Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1174/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Analyzing LLMs' Knowledge Boundary Cognition Across ...","url":"https://aclanthology.org/2025.acl-long.1174.pdf"},{"title":"LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs","url":"https://arxiv.org/pdf/2511.14774"}]

I found relevant information about your search query! Here are the key findings:

The paper "Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations" was authored by Chenghao Xiao, Hou Pong Chan, Hao Zhang, Mahani Aljunied, Lidong Bing, Noura Al Moubayed, and Yu Rong, and was published at ACL 2025.

The research constructs a multilingual evaluation suite comprising three representative types of knowledge boundary data to address the absence of standard testbeds for cross-lingual knowledge boundary analysis.

Key findings from the work include: Language differences in knowledge boundary perception follow a linear structure, which motivates a training-free alignment method that effectively transfers knowledge boundary perception ability across languages, thereby helping reduce hallucination risk in low-resource languages. Additionally, fine-tuning on bilingual question pair translation further enhances LLMs' recognition of knowledge boundaries across languages.

The code and datasets are publicly available at https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "fab00616-03ae-4217-89aa-ab22246b235a",
  "tool_use_result": {
    "query": "Xiao \"knowledge boundary\" cross-lingual probe transfer ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CcmUaLVcibTP8yPz6NHGfr",
        "content": [
          {
            "title": "GitHub - DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries: [ACL 2025] Analyzing LLMs' Multilingual Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations",
            "url": "https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries"
          },
          {
            "title": "Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1174/"
          },
          {
            "title": "Accepted Main Conference Papers - ACL 2025",
            "url": "https://2025.aclweb.org/program/main_papers/"
          },
          {
            "title": "Analyzing LLMs' Knowledge Boundary Cognition Across ...",
            "url": "https://aclanthology.org/2025.acl-long.1174.pdf"
          },
          {
            "title": "LiveCLKTBench: Towards Reliable Evaluation of Cross-Lingual Knowledge Transfer in Multilingual LLMs",
            "url": "https://arxiv.org/pdf/2511.14774"
          }
        ]
      },
      "I found relevant information about your search query! Here are the key findings:\n\nThe paper \"Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\" was authored by Chenghao Xiao, Hou Pong Chan, Hao Zhang, Mahani Aljunied, Lidong Bing, Noura Al Moubayed, and Yu Rong, and was published at ACL 2025.\n\nThe research constructs a multilingual evaluation suite comprising three representative types of knowledge boundary data to address the absence of standard testbeds for cross-lingual knowledge boundary analysis.\n\nKey findings from the work include: Language differences in knowledge boundary perception follow a linear structure, which motivates a training-free alignment method that effectively transfers knowledge boundary perception ability across languages, thereby helping reduce hallucination risk in low-resource languages. Additionally, fine-tuning on bilingual question pair translation further enhances LLMs' recognition of knowledge boundaries across languages.\n\nThe code and datasets are publicly available at https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries."
    ],
    "durationSeconds": 6.734809261999999
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T07:37:41.121Z_

<details><summary>↩ Tool result · `toolu_01MqBVuuQehwG2VHFCSN5mkd`</summary>

```text
Web search results for query: "Miao CORAL cross-task correctness probes 2026"

Links: [{"title":"Miranda Muqing Miao","url":"https://mmiao2.github.io/"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"GitHub - Human-Agent-Society/CORAL: CORAL is a robust, lightweight infrastructure for multi-agent autonomous self-evolution, built for autoresearch. Works with Claude Code, Codex, Cursor, OpenCode, Kiro, and more. · GitHub","url":"https://github.com/Human-Agent-Society/CORAL"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery","url":"https://arxiv.org/html/2604.01658v1"}]

Based on the search results, I found information about Miranda Muqing Miao's CORAL research from 2026:

CORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

The method uses a mechanistic interpretability approach to inference-time steering that extracts distributed correctness signals from frozen LLM residual stream activations via auxiliary probes, improving accuracy and calibration with cross-task generalization.

**Performance Results:**

CORAL consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average when evaluated across three 7B-parameter models. These gains transfer without retraining to four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

**Cross-Task Generalization:**

The probe captures a general-purpose correctness subspace rather than task-specific patterns.

CORAL was accepted at ICML 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "fb46ee8a-4b9e-4790-8b00-e2c351869a7e",
  "tool_use_result": {
    "query": "Miao CORAL cross-task correctness probes 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M5XiK6HeRB2ADcoVuWeNDg",
        "content": [
          {
            "title": "Miranda Muqing Miao",
            "url": "https://mmiao2.github.io/"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL):",
            "url": "https://arxiv.org/pdf/2602.06022"
          },
          {
            "title": "[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/abs/2602.06022"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
          },
          {
            "title": "GitHub - Human-Agent-Society/CORAL: CORAL is a robust, lightweight infrastructure for multi-agent autonomous self-evolution, built for autoresearch. Works with Claude Code, Codex, Cursor, OpenCode, Kiro, and more. · GitHub",
            "url": "https://github.com/Human-Agent-Society/CORAL"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"
          },
          {
            "title": "CORAL: Towards Autonomous Multi-Agent Evolution for Open-Ended Discovery",
            "url": "https://arxiv.org/html/2604.01658v1"
          }
        ]
      },
      "Based on the search results, I found information about Miranda Muqing Miao's CORAL research from 2026:\n\nCORAL (Correctness-Optimized Residual Activation Lens) is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.\n\nThe method uses a mechanistic interpretability approach to inference-time steering that extracts distributed correctness signals from frozen LLM residual stream activations via auxiliary probes, improving accuracy and calibration with cross-task generalization.\n\n**Performance Results:**\n\nCORAL consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average when evaluated across three 7B-parameter models. These gains transfer without retraining to four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.\n\n**Cross-Task Generalization:**\n\nThe probe captures a general-purpose correctness subspace rather than task-specific patterns.\n\nCORAL was accepted at ICML 2026."
    ],
    "durationSeconds": 7.098360799000002
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-21T07:37:41.268Z_

<details><summary>↩ Tool result · `toolu_01BCkxnq3gHS2JA23cQADtQk`</summary>

```text
Web search results for query: "Miao Ungar "correctness-confidence orthogonality" 2026 LLM representations"

Links: [{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"On LLMs' Internal Representation of Code Correctness","url":"https://arxiv.org/pdf/2512.07404"},{"title":"Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders","url":"https://arxiv.org/html/2604.19974"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning","url":"https://arxiv.org/html/2605.16824"},{"title":"can llms express their uncertainty? an empirical evaluation ...","url":"https://arxiv.org/pdf/2306.13063"}]

Based on the search results, I found relevant research related to your query. The most directly related paper appears to be "Are LLM Uncertainty and Correctness Encoded by the Same Features?" which uses sparse autoencoders to test whether uncertainty and correctness are encoded by distinct or overlapping feature populations, introducing a 2×2 quadrant framework that partitions model predictions along two independent axes, correctness and confidence.

Additionally, there's research characterizing the geometry of correctness representations in transformer activations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions.

The search results also show other recent 2026 work on LLM confidence and correctness, including papers on calibrating confidence estimates and detecting when LLMs are wrong.

However, I should note that the search results mention a GitHub link referencing "Miao" (in result 7), but I didn't find a specific paper explicitly authored by "Miao Ungar" with the exact phrase "correctness-confidence orthogonality" in the search results. The research landscape does contain substantial work on the relationship between correctness and confidence signals in LLM representations, but you may want to verify the exact citation details for the specific paper you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b1a42006-559a-45bd-8ac0-6d69e9c217a5",
  "tool_use_result": {
    "query": "Miao Ungar \"correctness-confidence orthogonality\" 2026 LLM representations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P6tiPtLzpQ77DmxQFfsg17",
        "content": [
          {
            "title": "Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/html/2603.06604"
          },
          {
            "title": "On LLMs' Internal Representation of Code Correctness",
            "url": "https://arxiv.org/pdf/2512.07404"
          },
          {
            "title": "Are LLM Uncertainty and Correctness Encoded by the Same Features? A Functional Dissociation via Sparse Autoencoders",
            "url": "https://arxiv.org/html/2604.19974"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/pdf/2505.21772"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning",
            "url": "https://arxiv.org/html/2605.16824"
          },
          {
            "title": "can llms express their uncertainty? an empirical evaluation ...",
            "url": "https://arxiv.org/pdf/2306.13063"
          }
        ]
      },
      "Based on the search results, I found relevant research related to your query. The most directly related paper appears to be \"Are LLM Uncertainty and Correctness Encoded by the Same Features?\" which uses sparse autoencoders to test whether uncertainty and correctness are encoded by distinct or overlapping feature populations, introducing a 2×2 quadrant framework that partitions model predictions along two independent axes, correctness and confidence.\n\nAdditionally, there's research characterizing the geometry of correctness representations in transformer activations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions.\n\nThe search results also show other recent 2026 work on LLM confidence and correctness, including papers on calibrating confidence estimates and detecting when LLMs are wrong.\n\nHowever, I should note that the search results mention a GitHub link referencing \"Miao\" (in result 7), but I didn't find a specific paper explicitly authored by \"Miao Ungar\" with the exact phrase \"correctness-confidence orthogonality\" in the search results. The research landscape does contain substantial work on the relationship between correctness and confidence signals in LLM representations, but you may want to verify the exact citation details for the specific paper you're looking for."
    ],
    "durationSeconds": 7.391258543
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T07:37:41.704Z_

<details><summary>↩ Tool result · `toolu_01Niye8iEUY5PCVQgeYLt4r8`</summary>

```text
Web search results for query: ""Confidence Manifold" framework LLM calibration low-dimensional subspace 2026"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Confidence Calibration in LLMs","url":"https://www.emergentmind.com/topics/confidence-calibration-in-llms"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/pdf/2602.08159"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"COSPADI: COMPRESSING LLMS VIA CALIBRATION- GUIDED SPARSE DICTIONARY LEARNING","url":"https://arxiv.org/pdf/2509.22075"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"}]

Based on the search results, here's what I found about the Confidence Manifold framework:

## The Confidence Manifold Framework

Language models encode a rich correctness signal internally that lives in a surprisingly low-dimensional subspace of just 3 to 8 dimensions, called the confidence manifold.

**Key Findings:**

The research characterized the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.

**Efficiency and Performance:**

A 7B model with 4096-dimensional hidden states encodes correctness in just 5 dimensions, 0.12% of its representational capacity. Additionally, centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy.

**Calibration Applications:**

Perturbations along low-dimensional calibration directions in hidden space can cut ECE by 30–50% with no impact on accuracy.

The research appears to have been published in early 2026, demonstrating that correctness representations in language models have a surprisingly compact geometric structure that can be leveraged for improved calibration and uncertainty estimation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "44928408-c1b7-4e46-b3c2-63c5536a98b4",
  "tool_use_result": {
    "query": "\"Confidence Manifold\" framework LLM calibration low-dimensional subspace 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01R9KLjfy5UQnJCz8zMLqhoh",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "Confidence Calibration in LLMs",
            "url": "https://www.emergentmind.com/topics/confidence-calibration-in-llms"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/pdf/2505.21772"
          },
          {
            "title": "COSPADI: COMPRESSING LLMS VIA CALIBRATION- GUIDED SPARSE DICTIONARY LEARNING",
            "url": "https://arxiv.org/pdf/2509.22075"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/html/2505.21772v1"
          }
        ]
      },
      "Based on the search results, here's what I found about the Confidence Manifold framework:\n\n## The Confidence Manifold Framework\n\nLanguage models encode a rich correctness signal internally that lives in a surprisingly low-dimensional subspace of just 3 to 8 dimensions, called the confidence manifold.\n\n**Key Findings:**\n\nThe research characterized the geometry of correctness representations across 9 models from 5 architecture families, finding that the discriminative signal occupies 3–8 dimensions, performance degrades with additional dimensions, and no nonlinear classifier improves over linear separation.\n\n**Efficiency and Performance:**\n\nA 7B model with 4096-dimensional hidden states encodes correctness in just 5 dimensions, 0.12% of its representational capacity. Additionally, centroid distance in the low-dimensional subspace matches trained probe performance (0.90 AUC), enabling few-shot detection: on GPT-2, 25 labeled examples achieve 89% of full-data accuracy.\n\n**Calibration Applications:**\n\nPerturbations along low-dimensional calibration directions in hidden space can cut ECE by 30–50% with no impact on accuracy.\n\nThe research appears to have been published in early 2026, demonstrating that correctness representations in language models have a surprisingly compact geometric structure that can be leveraged for improved calibration and uncertainty estimation."
    ],
    "durationSeconds": 7.07842872
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Good, I found several papers. Let me now search for the remaining ones.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "4a2c4b2d-58dd-4501-8e36-9c433baf5d3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 30_

Found several papers. Now searching for the remaining 2025-2026 papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "ed665436-c0e8-477e-86a9-305362cc4e68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JuTUjz3kS7FVKquMBSMEuv`</summary>

```json
{
  "query": "Ji 2025 \"verbal uncertainty\" \"linear direction\" LLM representation space calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "1e75b02b-f3bf-4b9a-bbdf-d3d2c2f81cb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011sERPKBX7xqezbMMnxx9bm`</summary>

```json
{
  "query": "Joshi 2025 \"calibration across layers\" LLM non-monotonic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b4ea5ab7-fdca-407b-8b22-3276acbf8197",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Dbb7juAPUmYiXLQtzUSgdz`</summary>

```json
{
  "query": "Liu Niehues 2025 \"middle layer\" cross-lingual alignment fine-tuned LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "bb430324-2754-4f13-825c-44caa0de636d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168FtZGNFnReBjbuLH93tcD`</summary>

```json
{
  "query": "Ravisankar 2026 DALI activation patching cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "bbac796c-d021-48c0-9e41-d7916574034d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D4M1Gc3YBKEs6EavG7NbQK`</summary>

```json
{
  "query": "Civelli 2026 \"shared geometry\" difficulty IRT cross-lingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e41c7618-4c5f-4b86-ae8a-d1be327f014d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N2pvkZB8UF3DFXtJAptWhp`</summary>

```json
{
  "query": "Miao Ungar 2026 \"closing the gap\" correctness confidence orthogonal subspace LLM arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "4530465b-1595-4b6f-861a-154723a77dd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbcheJHNVbBJg4E3Yvk2Ks",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4699,
      "cache_read_input_tokens": 33582,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4699
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-21T07:37:53.093Z_

<details><summary>↩ Tool result · `toolu_01JuTUjz3kS7FVKquMBSMEuv`</summary>

```text
Web search results for query: "Ji 2025 "verbal uncertainty" "linear direction" LLM representation space calibration"

Links: [{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/html/2503.14477v1"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce   Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/html/2512.22245"},{"title":"Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation","url":"https://arxiv.org/pdf/2512.22245"}]

I found the research you're looking for. The paper finds that "verbal uncertainty" is governed by a single linear feature in the representation space of LLMs, and shows that this has only moderate correlation with the actual "semantic uncertainty" of the model.

The paper is by Ziwei Ji and colleagues, published in 2025. The researchers show that the degree of uncertainty expressed by a model is mediated by a single direction, which they call the "Verbal Uncertainty Feature" (VUF). 

They apply this insight and show that (1) the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone and (2) they can intervene on verbal uncertainty at inference time and reduce hallucinations on short-form answers, achieving an average relative reduction of 32%.

The paper appears to be published in the proceedings of EMNLP 2025 and is also available on arXiv (2503.14477).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "3753919c-7c67-4ec2-bf49-265c4becfd8a",
  "tool_use_result": {
    "query": "Ji 2025 \"verbal uncertainty\" \"linear direction\" LLM representation space calibration",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Txp3fWjb9jmUCFD5Yr4Hyg",
        "content": [
          {
            "title": "[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/abs/2503.14477"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.187/"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://www.researchgate.net/publication/397424902_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/html/2503.14477v1"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce   Hallucinations",
            "url": "https://arxiv.org/pdf/2503.14477"
          },
          {
            "title": "(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/html/2512.22245"
          },
          {
            "title": "Calibrating LLM Judges: Linear Probes for Fast and Reliable Uncertainty Estimation",
            "url": "https://arxiv.org/pdf/2512.22245"
          }
        ]
      },
      "I found the research you're looking for. The paper finds that \"verbal uncertainty\" is governed by a single linear feature in the representation space of LLMs, and shows that this has only moderate correlation with the actual \"semantic uncertainty\" of the model.\n\nThe paper is by Ziwei Ji and colleagues, published in 2025. The researchers show that the degree of uncertainty expressed by a model is mediated by a single direction, which they call the \"Verbal Uncertainty Feature\" (VUF). \n\nThey apply this insight and show that (1) the mismatch between semantic and verbal uncertainty is a better predictor of hallucinations than semantic uncertainty alone and (2) they can intervene on verbal uncertainty at inference time and reduce hallucinations on short-form answers, achieving an average relative reduction of 32%.\n\nThe paper appears to be published in the proceedings of EMNLP 2025 and is also available on arXiv (2503.14477)."
    ],
    "durationSeconds": 5.829895838000004
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T07:37:55.295Z_

<details><summary>↩ Tool result · `toolu_0168FtZGNFnReBjbuLH93tcD`</summary>

```text
Web search results for query: "Ravisankar 2026 DALI activation patching cross-lingual"

Links: [{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.225/"},{"title":"[2504.09378] Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/abs/2504.09378"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/pdf/2504.09378"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/html/2504.09378v1"},{"title":"Separating Tongue from Thought: Activation Patching Reveals Language-Agnostic Concept Representations in Transformers","url":"https://arxiv.org/pdf/2411.08745"},{"title":"(PDF) Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://www.researchgate.net/publication/390773780_Can_you_map_it_to_English_The_Role_of_Cross-Lingual_Alignment_in_Multilingual_Performance_of_LLMs"}]

The search results show relevant research on this topic. Here's what I found:

Kartik Ravisankar and colleagues published research in 2026 at the 19th Conference of the European Chapter of the Association for Computational Linguistics. They introduced the Discriminative Alignment Index (DALI) to quantify instance-level alignment across 24 languages other than English and three distinct NLU tasks.

Through activation patching, the researchers showed that incorrect predictions in languages other than English can be fixed by patching their parallel English activations in the middle layers, thereby demonstrating the causal role of representation (mis)alignment in cross-lingual correctness. Results show that incorrect NLU predictions are strongly associated with lower representation alignment with English in the model's middle layers.

The work studied how large language models (LLMs), which can answer prompts in many languages despite being trained predominantly on English, leverage representation alignment to understand natural language understanding (NLU) tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8632d55e-d96f-4504-8821-e508652a8182",
  "tool_use_result": {
    "query": "Ravisankar 2026 DALI activation patching cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V5BCyepVwgP414z8Rt3ZSR",
        "content": [
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2026.eacl-long.225/"
          },
          {
            "title": "[2504.09378] Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/abs/2504.09378"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/pdf/2504.09378"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/html/2504.09378v1"
          },
          {
            "title": "Separating Tongue from Thought: Activation Patching Reveals Language-Agnostic Concept Representations in Transformers",
            "url": "https://arxiv.org/pdf/2411.08745"
          },
          {
            "title": "(PDF) Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://www.researchgate.net/publication/390773780_Can_you_map_it_to_English_The_Role_of_Cross-Lingual_Alignment_in_Multilingual_Performance_of_LLMs"
          }
        ]
      },
      "The search results show relevant research on this topic. Here's what I found:\n\nKartik Ravisankar and colleagues published research in 2026 at the 19th Conference of the European Chapter of the Association for Computational Linguistics. They introduced the Discriminative Alignment Index (DALI) to quantify instance-level alignment across 24 languages other than English and three distinct NLU tasks.\n\nThrough activation patching, the researchers showed that incorrect predictions in languages other than English can be fixed by patching their parallel English activations in the middle layers, thereby demonstrating the causal role of representation (mis)alignment in cross-lingual correctness. Results show that incorrect NLU predictions are strongly associated with lower representation alignment with English in the model's middle layers.\n\nThe work studied how large language models (LLMs), which can answer prompts in many languages despite being trained predominantly on English, leverage representation alignment to understand natural language understanding (NLU) tasks."
    ],
    "durationSeconds": 5.5955907179999995
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T07:37:55.489Z_

<details><summary>↩ Tool result · `toolu_011sERPKBX7xqezbMMnxx9bm`</summary>

```text
Web search results for query: "Joshi 2025 "calibration across layers" LLM non-monotonic"

Links: [{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/html/2511.00280v1"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.742/"},{"title":"GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub","url":"https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"},{"title":"(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"Detecting LLM Hallucination Through Layer-wise ...","url":"https://aclanthology.org/2025.emnlp-main.1644.pdf"}]

I found relevant research on this topic. Here are the search results:

The paper "Calibration Across Layers: Understanding Calibration Evolution in LLMs" was authored by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi in 2025.

The work investigates how calibration evolves throughout the network's depth, and analyzing multiple open-weight models on the MMLU benchmark, the authors uncovered a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.

The research identifies a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

Regarding the non-monotonic behavior, the paper shows that ECE and MCE scores first rise (in layers 26-28) and then decline (in layers 29-31).

The findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.

The paper was accepted at EMNLP 2025 (the main conference) and is available on arXiv as paper 2511.00280.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "284a123d-4ead-4170-bd8d-a4c71c658ac3",
  "tool_use_result": {
    "query": "Joshi 2025 \"calibration across layers\" LLM non-monotonic",
    "results": [
      {
        "tool_use_id": "srvtoolu_013kC8VoRHU6byJZBUH3DDkV",
        "content": [
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/html/2511.00280v1"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.742/"
          },
          {
            "title": "GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub",
            "url": "https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"
          },
          {
            "title": "(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=22850&show=2000"
          },
          {
            "title": "[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/abs/2511.00280"
          },
          {
            "title": "Detecting LLM Hallucination Through Layer-wise ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1644.pdf"
          }
        ]
      },
      "I found relevant research on this topic. Here are the search results:\n\nThe paper \"Calibration Across Layers: Understanding Calibration Evolution in LLMs\" was authored by Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi in 2025.\n\nThe work investigates how calibration evolves throughout the network's depth, and analyzing multiple open-weight models on the MMLU benchmark, the authors uncovered a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached.\n\nThe research identifies a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.\n\nRegarding the non-monotonic behavior, the paper shows that ECE and MCE scores first rise (in layers 26-28) and then decline (in layers 29-31).\n\nThe findings suggest that calibration is a distributed phenomenon, shaped throughout the network's forward pass, not just in its final projection, providing new insights into how confidence-regulating mechanisms operate within LLMs.\n\nThe paper was accepted at EMNLP 2025 (the main conference) and is available on arXiv as paper 2511.00280."
    ],
    "durationSeconds": 7.6872460280000015
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-21T07:37:56.748Z_

<details><summary>↩ Tool result · `toolu_01D4M1Gc3YBKEs6EavG7NbQK`</summary>

```text
Web search results for query: "Civelli 2026 "shared geometry" difficulty IRT cross-lingual"

Links: [{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/abs/2601.12731"},{"title":"[Literature Review] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://www.themoonlight.io/en/review/a-shared-geometry-of-difficulty-in-multilingual-language-models"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/pdf/2601.12731"},{"title":"(PDF) A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://www.researchgate.net/publication/399930732_A_Shared_Geometry_of_Difficulty_in_Multilingual_Language_Models"}]

The search returned results for the paper "A Shared Geometry of Difficulty in Multilingual Language Models" by Civelli et al. from 2026. Here's what I found:

The paper, authored by Stefano Civelli and colleagues, studies the multilingual geometry of problem-difficulty in LLMs by training linear probes using the AMC subset of the Easy2Hard benchmark, translated into 21 languages.

Difficulty is estimated via Item Response Theory (IRT) from human success rates.

Key findings include:

Difficulty-related signals emerge at two distinct stages of the model internals, corresponding to shallow (early-layers) and deep (later-layers) internal representations, that exhibit functionally different behaviors.

Probes trained on deep representations achieve high accuracy when evaluated on the same language but exhibit poor cross-lingual generalization. In contrast, probes trained on shallow representations generalize substantially better across languages, despite achieving lower within-language performance.

The results suggest that LLMs first form a language-agnostic representation of problem difficulty, which subsequently becomes language-specific.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "21cce169-b02b-44d2-b95f-d7f82b9d3c8a",
  "tool_use_result": {
    "query": "Civelli 2026 \"shared geometry\" difficulty IRT cross-lingual",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BFVJPEkJty8hAPF8dy8cY4",
        "content": [
          {
            "title": "A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/html/2601.12731"
          },
          {
            "title": "[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/abs/2601.12731"
          },
          {
            "title": "[Literature Review] A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://www.themoonlight.io/en/review/a-shared-geometry-of-difficulty-in-multilingual-language-models"
          },
          {
            "title": "A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/pdf/2601.12731"
          },
          {
            "title": "(PDF) A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://www.researchgate.net/publication/399930732_A_Shared_Geometry_of_Difficulty_in_Multilingual_Language_Models"
          }
        ]
      },
      "The search returned results for the paper \"A Shared Geometry of Difficulty in Multilingual Language Models\" by Civelli et al. from 2026. Here's what I found:\n\nThe paper, authored by Stefano Civelli and colleagues, studies the multilingual geometry of problem-difficulty in LLMs by training linear probes using the AMC subset of the Easy2Hard benchmark, translated into 21 languages.\n\nDifficulty is estimated via Item Response Theory (IRT) from human success rates.\n\nKey findings include:\n\nDifficulty-related signals emerge at two distinct stages of the model internals, corresponding to shallow (early-layers) and deep (later-layers) internal representations, that exhibit functionally different behaviors.\n\nProbes trained on deep representations achieve high accuracy when evaluated on the same language but exhibit poor cross-lingual generalization. In contrast, probes trained on shallow representations generalize substantially better across languages, despite achieving lower within-language performance.\n\nThe results suggest that LLMs first form a language-agnostic representation of problem difficulty, which subsequently becomes language-specific."
    ],
    "durationSeconds": 6.103555239000001
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T07:37:57.078Z_

<details><summary>↩ Tool result · `toolu_01N2pvkZB8UF3DFXtJAptWhp`</summary>

```text
Web search results for query: "Miao Ungar 2026 "closing the gap" correctness confidence orthogonal subspace LLM arXiv"

Links: [{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052"},{"title":"Miranda Muqing Miao","url":"https://mmiao2.github.io/"},{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"Bridging the Knowledge-Prediction Gap in LLMs on Multiple-Choice Questions","url":"https://arxiv.org/pdf/2509.23782"},{"title":"On the Fundamental Limits of LLMs at Scale","url":"https://arxiv.org/html/2511.12869v2"},{"title":"GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics","url":"https://arxiv.org/pdf/2604.02830"}]

I found the paper you're looking for! The research by Miao and Ungar presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another — a finding consistent across three open-weight models and four datasets.

When models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration (termed the "Reasoning Contamination Effect"), and the researchers introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it.

The paper is titled "Closing the Confidence-Faithfulness Gap in Large Language Models" and appears on arXiv as paper 2603.25052, dated April 1, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "24daebb7-d559-4d50-aa70-60edcee50009",
  "tool_use_result": {
    "query": "Miao Ungar 2026 \"closing the gap\" correctness confidence orthogonal subspace LLM arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MQFzsBUuj9PZe6oA1vd9cP",
        "content": [
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/html/2603.25052"
          },
          {
            "title": "Miranda Muqing Miao",
            "url": "https://mmiao2.github.io/"
          },
          {
            "title": "[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052"
          },
          {
            "title": "Bridging the Knowledge-Prediction Gap in LLMs on Multiple-Choice Questions",
            "url": "https://arxiv.org/pdf/2509.23782"
          },
          {
            "title": "On the Fundamental Limits of LLMs at Scale",
            "url": "https://arxiv.org/html/2511.12869v2"
          },
          {
            "title": "GRADE: Probing Knowledge Gaps in LLMs through Gradient Subspace Dynamics",
            "url": "https://arxiv.org/pdf/2604.02830"
          }
        ]
      },
      "I found the paper you're looking for! The research by Miao and Ungar presents a mechanistic interpretability analysis of verbalized confidence, using linear probes and contrastive activation addition (CAA) steering to show that calibration and verbalized confidence signals are encoded linearly but are orthogonal to one another — a finding consistent across three open-weight models and four datasets.\n\nWhen models are prompted to simultaneously reason through a problem and verbalize a confidence score, the reasoning process disrupts the verbalized confidence direction, exacerbating miscalibration (termed the \"Reasoning Contamination Effect\"), and the researchers introduce a two-stage adaptive steering pipeline that reads the model's internal accuracy estimate and steers verbalized output to match it.\n\nThe paper is titled \"Closing the Confidence-Faithfulness Gap in Large Language Models\" and appears on arXiv as paper 2603.25052, dated April 1, 2026."
    ],
    "durationSeconds": 6.225758322000002
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T07:37:59.860Z_

<details><summary>↩ Tool result · `toolu_01Dbb7juAPUmYiXLQtzUSgdz`</summary>

```text
Web search results for query: "Liu Niehues 2025 "middle layer" cross-lingual alignment fine-tuned LLM"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://www.researchgate.net/publication/384219551_Probing_the_Emergence_of_Cross-lingual_Alignment_during_LLM_Training"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - haebom","url":"https://slashpage.com/haebom/y9e1xp2xyyx54m7k35vz?lang=en&tl=en"}]

Based on the search results, here's what I found about the Liu and Niehues 2025 paper on middle-layer cross-lingual alignment in fine-tuned LLMs:

## Paper Overview

The paper is titled "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs" and was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.

## Key Findings

Through analysis of LLM internal representations from over 1,000+ language pairs, the authors discovered that middle layers exhibit the strongest potential for cross-lingual alignment.

## Methodology

Building on this finding, they proposed a middle-layer alignment objective integrated into task-specific training. The authors analyzed representations from Llama 3 and Qwen 2.5 across 1,000+ language pairs.

## Results and Applications

Applying alignment objectives to middle layers during LLM task-specific fine-tuning improves cross-lingual transfer and enhances alignment across all network depths. The researchers demonstrated transfer improvements across diverse tasks including slot filling, machine translation, and structured text generation.

The full paper is available on ArXiv and through the ACL Anthology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "10b5722b-1d95-4431-a807-14d83dcbf1aa",
  "tool_use_result": {
    "query": "Liu Niehues 2025 \"middle layer\" cross-lingual alignment fine-tuned LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D2RaPyeG1LGzzP4zUB9VQX",
        "content": [
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.778/"
          },
          {
            "title": "Probing the Emergence of Cross-lingual Alignment during LLM Training",
            "url": "https://www.researchgate.net/publication/384219551_Probing_the_Emergence_of_Cross-lingual_Alignment_during_LLM_Training"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"
          },
          {
            "title": "[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/pdf/2502.14830"
          },
          {
            "title": "[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/abs/2502.14830"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/html/2502.14830v1"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - haebom",
            "url": "https://slashpage.com/haebom/y9e1xp2xyyx54m7k35vz?lang=en&tl=en"
          }
        ]
      },
      "Based on the search results, here's what I found about the Liu and Niehues 2025 paper on middle-layer cross-lingual alignment in fine-tuned LLMs:\n\n## Paper Overview\n\nThe paper is titled \"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\" and was published at the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) in Vienna, Austria.\n\n## Key Findings\n\nThrough analysis of LLM internal representations from over 1,000+ language pairs, the authors discovered that middle layers exhibit the strongest potential for cross-lingual alignment.\n\n## Methodology\n\nBuilding on this finding, they proposed a middle-layer alignment objective integrated into task-specific training. The authors analyzed representations from Llama 3 and Qwen 2.5 across 1,000+ language pairs.\n\n## Results and Applications\n\nApplying alignment objectives to middle layers during LLM task-specific fine-tuning improves cross-lingual transfer and enhances alignment across all network depths. The researchers demonstrated transfer improvements across diverse tasks including slot filling, machine translation, and structured text generation.\n\nThe full paper is available on ArXiv and through the ACL Anthology."
    ],
    "durationSeconds": 11.107355075
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
I now have good information on all the papers. Let me also search for the classic papers' DOIs and the new papers to add (Conneau 2020 XLM-R, Lord 1980 IRT, Fedus 2022 Switch Transformers), plus get more details on some of the found papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "54bc0db6-b0ff-49df-8b3d-220338337769",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 44_

Found all the 2025-2026 papers. Now searching for the classic papers' DOIs and the new citations to add.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "57e9b178-2f11-4420-8b11-3dbc29c43d33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Pk1Gwg5iZQhyFXhXCCtgyx`</summary>

```json
{
  "query": "Guo \"On Calibration of Modern Neural Networks\" ICML 2017 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "2682a8df-b195-41bb-ba97-a69ef512cccf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cust3T8dYToW51HHGjoHLx`</summary>

```json
{
  "query": "Conneau \"Unsupervised Cross-lingual Representation Learning at Scale\" XLM-R ACL 2020 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "2cd6a943-75f5-4427-90a8-0dec9e5bbc9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S7ezAmkmZaUbWr1HqQSVz3`</summary>

```json
{
  "query": "Fedus \"Switch Transformers\" JMLR 2022 doi trillion parameter"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b16e6983-9939-4ab5-9842-0d03aa258d66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S4YcrtxGyQxFBcR9QB5zes`</summary>

```json
{
  "query": "Lord 1980 \"Applications of Item Response Theory to Practical Testing Problems\" ISBN Erlbaum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b755153a-e03d-4f4e-af07-7159f5c3b677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KEAUgJ2GBCauA78DQ5ZfuY`</summary>

```json
{
  "query": "Kornblith \"Similarity of Neural Network Representations Revisited\" CKA ICML 2019 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "11393fdc-c467-48c4-9422-0b61c8775bce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P1GT3e39kLmnQrFYnuGAvL`</summary>

```json
{
  "query": "Ben-David \"A Theory of Learning from Different Domains\" Machine Learning 2010 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "88afe82c-edce-4edf-9943-97d7081547a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5mF17mWmD7J8RtWUjFko8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1703,
      "cache_creation_input_tokens": 2712,
      "cache_read_input_tokens": 38281,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2712
      },
      "output_tokens": 12,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T07:38:10.560Z_

<details><summary>↩ Tool result · `toolu_01Pk1Gwg5iZQhyFXhXCCtgyx`</summary>

```text
Web search results for query: "Guo "On Calibration of Modern Neural Networks" ICML 2017 doi"

Links: [{"title":"[1706.04599] On Calibration of Modern Neural Networks","url":"https://arxiv.org/abs/1706.04599"},{"title":"\"On Calibration of Modern Neural Networks\", Guo et al. • David Stutz","url":"https://davidstutz.de/on-calibration-of-modern-neural-networks-guo-et-al/"},{"title":"On Calibration of Modern Neural Networks","url":"https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Calibration_of_Neural_Nets.md"},{"title":"On Calibration of Modern Neural Networks","url":"https://arxiv.org/pdf/1706.04599"},{"title":"(Open Access) On Calibration of Modern Neural Networks (2017) | Chuan Guo | 4418 Citations","url":"https://scispace.com/papers/on-calibration-of-modern-neural-networks-5cc9ha8ohx"},{"title":"On Calibration of Modern Neural Networks","url":"https://proceedings.mlr.press/v70/guo17a/guo17a.pdf"},{"title":"Revisiting the Calibration of Modern Neural Networks","url":"https://arxiv.org/pdf/2106.07998"},{"title":"[PDF] On Calibration of Modern Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Calibration-of-Modern-Neural-Networks-Guo-Pleiss/d65ce2b8300541414bfe51d03906fca72e93523c"},{"title":"On calibration of modern neural networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305518"}]

Based on the search results, here is the information about the paper:

**Citation Information:**

The paper "On Calibration of Modern Neural Networks" was authored by Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger and published at ICML 2017.

**Available DOI/Identifiers:**

- ArXiv ID: 1706.04599
- Published in Proceedings of the 34th International Conference on Machine Learning (PMLR 70), 2017
- ACM DOI reference: Available through the ACM Digital Library for ICML'17

**Paper Summary:**

The paper addresses confidence calibration – the problem of predicting probability estimates representative of the true correctness likelihood – which is important for classification models in many applications. The authors discovered that modern neural networks, unlike those from a decade ago, are poorly calibrated, with depth, width, weight decay, and Batch Normalization being important factors influencing calibration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "a46aa591-809b-4217-bed5-297c41378e07",
  "tool_use_result": {
    "query": "Guo \"On Calibration of Modern Neural Networks\" ICML 2017 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KqBnt8Fwh8ipu1jFoRdJnv",
        "content": [
          {
            "title": "[1706.04599] On Calibration of Modern Neural Networks",
            "url": "https://arxiv.org/abs/1706.04599"
          },
          {
            "title": "\"On Calibration of Modern Neural Networks\", Guo et al. • David Stutz",
            "url": "https://davidstutz.de/on-calibration-of-modern-neural-networks-guo-et-al/"
          },
          {
            "title": "On Calibration of Modern Neural Networks",
            "url": "https://github.com/vlgiitr/papers_we_read/blob/master/summaries/Calibration_of_Neural_Nets.md"
          },
          {
            "title": "On Calibration of Modern Neural Networks",
            "url": "https://arxiv.org/pdf/1706.04599"
          },
          {
            "title": "(Open Access) On Calibration of Modern Neural Networks (2017) | Chuan Guo | 4418 Citations",
            "url": "https://scispace.com/papers/on-calibration-of-modern-neural-networks-5cc9ha8ohx"
          },
          {
            "title": "On Calibration of Modern Neural Networks",
            "url": "https://proceedings.mlr.press/v70/guo17a/guo17a.pdf"
          },
          {
            "title": "Revisiting the Calibration of Modern Neural Networks",
            "url": "https://arxiv.org/pdf/2106.07998"
          },
          {
            "title": "[PDF] On Calibration of Modern Neural Networks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-Calibration-of-Modern-Neural-Networks-Guo-Pleiss/d65ce2b8300541414bfe51d03906fca72e93523c"
          },
          {
            "title": "On calibration of modern neural networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70",
            "url": "https://dl.acm.org/doi/10.5555/3305381.3305518"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n**Citation Information:**\n\nThe paper \"On Calibration of Modern Neural Networks\" was authored by Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger and published at ICML 2017.\n\n**Available DOI/Identifiers:**\n\n- ArXiv ID: 1706.04599\n- Published in Proceedings of the 34th International Conference on Machine Learning (PMLR 70), 2017\n- ACM DOI reference: Available through the ACM Digital Library for ICML'17\n\n**Paper Summary:**\n\nThe paper addresses confidence calibration – the problem of predicting probability estimates representative of the true correctness likelihood – which is important for classification models in many applications. The authors discovered that modern neural networks, unlike those from a decade ago, are poorly calibrated, with depth, width, weight decay, and Batch Normalization being important factors influencing calibration."
    ],
    "durationSeconds": 4.682660470000003
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T07:38:11.395Z_

<details><summary>↩ Tool result · `toolu_01Cust3T8dYToW51HHGjoHLx`</summary>

```text
Web search results for query: "Conneau "Unsupervised Cross-lingual Representation Learning at Scale" XLM-R ACL 2020 doi"

Links: [{"title":"Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.747/"},{"title":"(PDF) Unsupervised Cross-lingual Representation Learning at Scale (2020) | Alexis Conneau | 6886 Citations","url":"https://scispace.com/papers/unsupervised-cross-lingual-representation-learning-at-scale-2o09354dx5"},{"title":"[1911.02116] Unsupervised Cross-lingual Representation Learning at Scale","url":"https://arxiv.org/abs/1911.02116"},{"title":"ACL2020: Unsupervised Cross-lingual Representation Learning at Scale","url":"https://virtual.acl2020.org/paper_main.747.html"},{"title":"Conneau, A., et al. (2020) Unsupervised Cross-Lingual Representation Learning at Scale. Proceedings of ACL 2020, 5-10 July 2020, 8440-8451. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4031261"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale","url":"https://arxiv.org/pdf/1911.02116"},{"title":"[PDF] Unsupervised Cross-lingual Representation Learning at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Cross-lingual-Representation-Learning-Conneau-Khandelwal/6fec3e579c7cd4f13bdabbee2b6ac2e8ff5941c6"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale","url":"https://www.researchgate.net/publication/343298778_Unsupervised_Cross-lingual_Representation_Learning_at_Scale"},{"title":"Brief Review — XLM-R: Unsupervised Cross-lingual Representation Learning at Scale | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-xlm-r-unsupervised-cross-lingual-representation-learning-at-scale-0a51dc980900"}]

Based on the search results, I found the paper you're looking for:

**Paper:** "Unsupervised Cross-lingual Representation Learning at Scale" by Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov, published in 2020.

**DOI:** 10.18653/V1/2020.ACL-MAIN.747

**Publication Details:** Proceedings of ACL 2020, 5-10 July 2020, pages 8440-8451

**About the Paper:** The paper shows that pretraining multilingual language models at scale leads to significant performance gains for a wide range of cross-lingual transfer tasks, with the model trained on one hundred languages using more than two terabytes of filtered CommonCrawl data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "72826f78-e717-4182-8a15-4e063d223cb3",
  "tool_use_result": {
    "query": "Conneau \"Unsupervised Cross-lingual Representation Learning at Scale\" XLM-R ACL 2020 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DM2tD7z4QVDg86HVVGUvCS",
        "content": [
          {
            "title": "Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.747/"
          },
          {
            "title": "(PDF) Unsupervised Cross-lingual Representation Learning at Scale (2020) | Alexis Conneau | 6886 Citations",
            "url": "https://scispace.com/papers/unsupervised-cross-lingual-representation-learning-at-scale-2o09354dx5"
          },
          {
            "title": "[1911.02116] Unsupervised Cross-lingual Representation Learning at Scale",
            "url": "https://arxiv.org/abs/1911.02116"
          },
          {
            "title": "ACL2020: Unsupervised Cross-lingual Representation Learning at Scale",
            "url": "https://virtual.acl2020.org/paper_main.747.html"
          },
          {
            "title": "Conneau, A., et al. (2020) Unsupervised Cross-Lingual Representation Learning at Scale. Proceedings of ACL 2020, 5-10 July 2020, 8440-8451. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=4031261"
          },
          {
            "title": "Unsupervised Cross-lingual Representation Learning at Scale",
            "url": "https://arxiv.org/pdf/1911.02116"
          },
          {
            "title": "[PDF] Unsupervised Cross-lingual Representation Learning at Scale | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Unsupervised-Cross-lingual-Representation-Learning-Conneau-Khandelwal/6fec3e579c7cd4f13bdabbee2b6ac2e8ff5941c6"
          },
          {
            "title": "Unsupervised Cross-lingual Representation Learning at Scale",
            "url": "https://www.researchgate.net/publication/343298778_Unsupervised_Cross-lingual_Representation_Learning_at_Scale"
          },
          {
            "title": "Brief Review — XLM-R: Unsupervised Cross-lingual Representation Learning at Scale | by Sik-Ho Tsang | Medium",
            "url": "https://sh-tsang.medium.com/brief-review-xlm-r-unsupervised-cross-lingual-representation-learning-at-scale-0a51dc980900"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Paper:** \"Unsupervised Cross-lingual Representation Learning at Scale\" by Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov, published in 2020.\n\n**DOI:** 10.18653/V1/2020.ACL-MAIN.747\n\n**Publication Details:** Proceedings of ACL 2020, 5-10 July 2020, pages 8440-8451\n\n**About the Paper:** The paper shows that pretraining multilingual language models at scale leads to significant performance gains for a wide range of cross-lingual transfer tasks, with the model trained on one hundred languages using more than two terabytes of filtered CommonCrawl data."
    ],
    "durationSeconds": 5.037724103
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-21T07:38:12.532Z_

<details><summary>↩ Tool result · `toolu_01S7ezAmkmZaUbWr1HqQSVz3`</summary>

```text
Web search results for query: "Fedus "Switch Transformers" JMLR 2022 doi trillion parameter"

Links: [{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://jmlr.org/papers/v23/21-0998.html"},{"title":"Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1","url":"https://dl.acm.org/doi/abs/10.5555/3586589.3586709"},{"title":"GitHub - kyegomez/SwitchTransformers: Implementation of Switch Transformers from the paper: \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\" · GitHub","url":"https://github.com/kyegomez/SwitchTransformers"},{"title":"[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity","url":"https://arxiv.org/abs/2101.03961"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Request PDF","url":"https://www.researchgate.net/publication/348403003_Switch_Transformers_Scaling_to_Trillion_Parameter_Models_with_Simple_and_Efficient_Sparsity"},{"title":"Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity","url":"https://alastairreid.github.io/RelatedWork/papers/fedus:arxiv:2021/"},{"title":"[PDF] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Switch-Transformers:-Scaling-to-Trillion-Parameter-Fedus-Zoph/fdacf2a732f55befdc410ea927091cad3b791f13"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec16.pdf"},{"title":"Switch Transformers: Scaling to Trillion Parameter Models ...","url":"https://www.jmlr.org/papers/volume23/21-0998/21-0998.pdf"}]

Based on the search results, I found the paper you're looking for:

**William Fedus, Barret Zoph, Noam Shazeer authored "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity," published in 2022 in JMLR volume 23, issue 120.**

The paper is available at: https://jmlr.org/papers/v23/21-0998.html

**Key details about the paper:**
- The paper introduces Mixture of Experts (MoE) models that select different parameters for each incoming example, resulting in a sparsely-activated model with an outrageous number of parameters but constant computational cost.
- The Switch Transformer simplifies the MoE routing algorithm with reduced communication and computational costs, and introduces training techniques that allow large sparse models to be trained with lower precision (bfloat16) formats.

The paper's arXiv identifier is 2101.03961, and it was originally published on arXiv in January 2021 before being published in the Journal of Machine Learning Research in 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "124c526c-b16b-4e61-9037-330d6c5308b9",
  "tool_use_result": {
    "query": "Fedus \"Switch Transformers\" JMLR 2022 doi trillion parameter",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MExMN6Hzud6DW2b2NcCFkH",
        "content": [
          {
            "title": "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity",
            "url": "https://jmlr.org/papers/v23/21-0998.html"
          },
          {
            "title": "Switch transformers: scaling to trillion parameter models with simple and efficient sparsity: The Journal of Machine Learning Research: Vol 23, No 1",
            "url": "https://dl.acm.org/doi/abs/10.5555/3586589.3586709"
          },
          {
            "title": "GitHub - kyegomez/SwitchTransformers: Implementation of Switch Transformers from the paper: \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity\" · GitHub",
            "url": "https://github.com/kyegomez/SwitchTransformers"
          },
          {
            "title": "[2101.03961] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity",
            "url": "https://arxiv.org/abs/2101.03961"
          },
          {
            "title": "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Request PDF",
            "url": "https://www.researchgate.net/publication/348403003_Switch_Transformers_Scaling_to_Trillion_Parameter_Models_with_Simple_and_Efficient_Sparsity"
          },
          {
            "title": "Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity",
            "url": "https://alastairreid.github.io/RelatedWork/papers/fedus:arxiv:2021/"
          },
          {
            "title": "[PDF] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Switch-Transformers:-Scaling-to-Trillion-Parameter-Fedus-Zoph/fdacf2a732f55befdc410ea927091cad3b791f13"
          },
          {
            "title": "Switch Transformers: Scaling to Trillion Parameter Models ...",
            "url": "https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec16.pdf"
          },
          {
            "title": "Switch Transformers: Scaling to Trillion Parameter Models ...",
            "url": "https://www.jmlr.org/papers/volume23/21-0998/21-0998.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**William Fedus, Barret Zoph, Noam Shazeer authored \"Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity,\" published in 2022 in JMLR volume 23, issue 120.**\n\nThe paper is available at: https://jmlr.org/papers/v23/21-0998.html\n\n**Key details about the paper:**\n- The paper introduces Mixture of Experts (MoE) models that select different parameters for each incoming example, resulting in a sparsely-activated model with an outrageous number of parameters but constant computational cost.\n- The Switch Transformer simplifies the MoE routing algorithm with reduced communication and computational costs, and introduces training techniques that allow large sparse models to be trained with lower precision (bfloat16) formats.\n\nThe paper's arXiv identifier is 2101.03961, and it was originally published on arXiv in January 2021 before being published in the Journal of Machine Learning Research in 2022."
    ],
    "durationSeconds": 5.630723115
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T07:38:12.663Z_

<details><summary>↩ Tool result · `toolu_01S4YcrtxGyQxFBcR9QB5zes`</summary>

```text
Web search results for query: "Lord 1980 "Applications of Item Response Theory to Practical Testing Problems" ISBN Erlbaum"

Links: [{"title":"Boekbesprekingen: Applications of item response theory to practical testing problems / F.M. Lord. - Hillsdale, N.J : Erlbaum Associates, 1980. - ISBN 0-89859-006-X - University of Twente Research Information","url":"https://research.utwente.nl/en/publications/boekbesprekingen-fm-lord-applications-of-item-response-theory-to-/"},{"title":"Applications Of Item Response Theory To Practical Testing Problems 089859006X, 9780898590067 - DOKUMEN.PUB","url":"https://dokumen.pub/applications-of-item-response-theory-to-practical-testing-problems-089859006x-9780898590067.html"},{"title":"Applications of Item Response Theory To Practical Testing Problems: Frederic M. Lord: 9780898590067: Amazon.com: Books","url":"https://www.amazon.com/Applications-Response-Practical-Testing-Problems/dp/089859006X"},{"title":"(PDF) Some Applications of Item Response Theory to Testing","url":"https://www.researchgate.net/publication/265667091_Some_Applications_of_Item_Response_Theory_to_Testing"},{"title":"ERIC - ED312280 - Applications of Item Response Theory to Practical Testing Problems., 1980","url":"https://eric.ed.gov/?id=ED312280"},{"title":"Applications of Item Response Theory To Practical Testing Problems - Frederic M. Lord: 9780898590067 - AbeBooks","url":"https://www.abebooks.com/9780898590067/Applications-Item-Response-Theory-Practical-089859006X/plp"},{"title":"Applications of Item Response Theory to Practical Testing Problems - Frederic M. Lord - Google Books","url":"https://books.google.com/books/about/Applications_of_Item_Response_Theory_to.html?id=_qu8YGkdTvwC"},{"title":"Lord, F. M. (1980). &lt;i>Applications of item response theory to practical testing problems&lt;/i>. Hillsdale, New Jersey: Lawrence Erlbaum Associates.","url":"https://www.sciepub.com/reference/304019"},{"title":"Applications of Item Response Theory To Practical Testing Problems - 1","url":"https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067"},{"title":"Applications of Item Response Theory To Practical Testing Problems | F","url":"https://www.taylorfrancis.com/books/mono/10.4324/9780203056615/applications-item-response-theory-practical-testing-problems-lord"}]

I found the information about the book. Here are the details:

The book "Applications of Item Response Theory To Practical Testing Problems" was published by Lawrence Erlbaum Associates on July 1, 1980, with ISBN-10: 089859006X and ISBN-13: 978-0898590067.

The purpose of the book is to make it possible for measurement specialists to solve practical testing problems through the use of item response theory (IRT). The book is 274 pages long.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b264943e-b932-428a-b7ae-65a96262a1eb",
  "tool_use_result": {
    "query": "Lord 1980 \"Applications of Item Response Theory to Practical Testing Problems\" ISBN Erlbaum",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PytCf22q2AzLMRpaHaEeVx",
        "content": [
          {
            "title": "Boekbesprekingen: Applications of item response theory to practical testing problems / F.M. Lord. - Hillsdale, N.J : Erlbaum Associates, 1980. - ISBN 0-89859-006-X - University of Twente Research Information",
            "url": "https://research.utwente.nl/en/publications/boekbesprekingen-fm-lord-applications-of-item-response-theory-to-/"
          },
          {
            "title": "Applications Of Item Response Theory To Practical Testing Problems 089859006X, 9780898590067 - DOKUMEN.PUB",
            "url": "https://dokumen.pub/applications-of-item-response-theory-to-practical-testing-problems-089859006x-9780898590067.html"
          },
          {
            "title": "Applications of Item Response Theory To Practical Testing Problems: Frederic M. Lord: 9780898590067: Amazon.com: Books",
            "url": "https://www.amazon.com/Applications-Response-Practical-Testing-Problems/dp/089859006X"
          },
          {
            "title": "(PDF) Some Applications of Item Response Theory to Testing",
            "url": "https://www.researchgate.net/publication/265667091_Some_Applications_of_Item_Response_Theory_to_Testing"
          },
          {
            "title": "ERIC - ED312280 - Applications of Item Response Theory to Practical Testing Problems., 1980",
            "url": "https://eric.ed.gov/?id=ED312280"
          },
          {
            "title": "Applications of Item Response Theory To Practical Testing Problems - Frederic M. Lord: 9780898590067 - AbeBooks",
            "url": "https://www.abebooks.com/9780898590067/Applications-Item-Response-Theory-Practical-089859006X/plp"
          },
          {
            "title": "Applications of Item Response Theory to Practical Testing Problems - Frederic M. Lord - Google Books",
            "url": "https://books.google.com/books/about/Applications_of_Item_Response_Theory_to.html?id=_qu8YGkdTvwC"
          },
          {
            "title": "Lord, F. M. (1980). &lt;i>Applications of item response theory to practical testing problems&lt;/i>. Hillsdale, New Jersey: Lawrence Erlbaum Associates.",
            "url": "https://www.sciepub.com/reference/304019"
          },
          {
            "title": "Applications of Item Response Theory To Practical Testing Problems - 1",
            "url": "https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067"
          },
          {
            "title": "Applications of Item Response Theory To Practical Testing Problems | F",
            "url": "https://www.taylorfrancis.com/books/mono/10.4324/9780203056615/applications-item-response-theory-practical-testing-problems-lord"
          }
        ]
      },
      "I found the information about the book. Here are the details:\n\nThe book \"Applications of Item Response Theory To Practical Testing Problems\" was published by Lawrence Erlbaum Associates on July 1, 1980, with ISBN-10: 089859006X and ISBN-13: 978-0898590067.\n\nThe purpose of the book is to make it possible for measurement specialists to solve practical testing problems through the use of item response theory (IRT). The book is 274 pages long."
    ],
    "durationSeconds": 4.724831538999999
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-21T07:38:13.537Z_

<details><summary>↩ Tool result · `toolu_01P1GT3e39kLmnQrFYnuGAvL`</summary>

```text
Web search results for query: "Ben-David "A Theory of Learning from Different Domains" Machine Learning 2010 doi"

Links: [{"title":"A theory of learning from different domains","url":"https://www.mendeley.com/catalogue/8c104c01-e1b3-32e9-a56a-a1f6221c4b31/"},{"title":"A theory of learning from different domains | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-009-5152-4"},{"title":"[PDF] A theory of learning from different domains | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-theory-of-learning-from-different-domains-Ben-David-Blitzer/66d398aeaeb7ec24ededb1adaa4b4f09a6c1bcde"},{"title":"Ben-David 2010 - A Theory of Learning From Different Domains PDF | PDF | Statistical Classification | Bias Of An Estimator","url":"https://www.scribd.com/document/320914333/Ben-David-2010-A-theory-of-learning-from-different-domains-pdf"},{"title":"A theory of learning from different domains","url":"https://escholarship.org/uc/item/2nv1j9sc"},{"title":"Shai Ben-David","url":"https://cs.uwaterloo.ca/~shai/da.html"},{"title":"(PDF) A theory of learning from different domains","url":"https://www.researchgate.net/publication/220343859_A_theory_of_learning_from_different_domains"},{"title":"A theory of learning from different domains","url":"https://research.google/pubs/pub36364/"},{"title":"A theory of learning from different domains | Machine Language","url":"https://dl.acm.org/doi/10.1007/s10994-009-5152-4"}]

Based on the search results, I found the complete citation information for the Ben-David paper:

Ben-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., & Vaughan, J. W. (2010). A theory of learning from different domains. Machine Learning, 79(1–2), 151–175. https://doi.org/10.1007/s10994-009-5152-4

The paper addresses the problem of learning classifiers that generalize across different domains, investigating conditions under which source domain classifiers perform well on target domains and how to optimally combine labeled data from both domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "d7d7eae1-0200-4189-947e-90837790c4b3",
  "tool_use_result": {
    "query": "Ben-David \"A Theory of Learning from Different Domains\" Machine Learning 2010 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ApmYYVoXQfCtcDczRY9itd",
        "content": [
          {
            "title": "A theory of learning from different domains",
            "url": "https://www.mendeley.com/catalogue/8c104c01-e1b3-32e9-a56a-a1f6221c4b31/"
          },
          {
            "title": "A theory of learning from different domains | Machine Learning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10994-009-5152-4"
          },
          {
            "title": "[PDF] A theory of learning from different domains | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-theory-of-learning-from-different-domains-Ben-David-Blitzer/66d398aeaeb7ec24ededb1adaa4b4f09a6c1bcde"
          },
          {
            "title": "Ben-David 2010 - A Theory of Learning From Different Domains PDF | PDF | Statistical Classification | Bias Of An Estimator",
            "url": "https://www.scribd.com/document/320914333/Ben-David-2010-A-theory-of-learning-from-different-domains-pdf"
          },
          {
            "title": "A theory of learning from different domains",
            "url": "https://escholarship.org/uc/item/2nv1j9sc"
          },
          {
            "title": "Shai Ben-David",
            "url": "https://cs.uwaterloo.ca/~shai/da.html"
          },
          {
            "title": "(PDF) A theory of learning from different domains",
            "url": "https://www.researchgate.net/publication/220343859_A_theory_of_learning_from_different_domains"
          },
          {
            "title": "A theory of learning from different domains",
            "url": "https://research.google/pubs/pub36364/"
          },
          {
            "title": "A theory of learning from different domains | Machine Language",
            "url": "https://dl.acm.org/doi/10.1007/s10994-009-5152-4"
          }
        ]
      },
      "Based on the search results, I found the complete citation information for the Ben-David paper:\n\nBen-David, S., Blitzer, J., Crammer, K., Kulesza, A., Pereira, F., & Vaughan, J. W. (2010). A theory of learning from different domains. Machine Learning, 79(1–2), 151–175. https://doi.org/10.1007/s10994-009-5152-4\n\nThe paper addresses the problem of learning classifiers that generalize across different domains, investigating conditions under which source domain classifiers perform well on target domains and how to optimally combine labeled data from both domains."
    ],
    "durationSeconds": 3.819083356000003
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T07:38:15.382Z_

<details><summary>↩ Tool result · `toolu_01KEAUgJ2GBCauA78DQ5ZfuY`</summary>

```text
Web search results for query: "Kornblith "Similarity of Neural Network Representations Revisited" CKA ICML 2019 doi"

Links: [{"title":"Similarity of Neural Network Representations Revisited","url":"https://vitalab.github.io/article/2021/01/28/SimilarityNeuralNets.html"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://cka-similarity.github.io/"},{"title":"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton","url":"https://icml.cc/media/Slides/icml/2019/halla(13-11-00)-13-12-15-4871-similarity_of_n.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://icml.cc/media/icml-2019/Slides/4871.pdf"},{"title":"Similarity of Neural Network Representations Revisited | Request PDF","url":"https://www.researchgate.net/publication/332799564_Similarity_of_Neural_Network_Representations_Revisited"},{"title":"SIMILARITY OF NEURAL NETWORK REPRESENTA","url":"https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_9.pdf"},{"title":"[1905.00414] Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/abs/1905.00414"},{"title":"[PDF] Similarity of Neural Network Representations Revisited | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Similarity-of-Neural-Network-Representations-Kornblith-Norouzi/726320cdbd04804ffa8f3a78c095bd1b55a2a695"},{"title":"Similarity of Neural Network Representations Revisited","url":"http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"},{"title":"Similarity of Neural Network Representations Revisited","url":"https://arxiv.org/pdf/1905.00414"}]

Based on the search results, I found comprehensive information about this paper. The paper is by Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton from ICML 2019.

The paper introduces a similarity index that measures the relationship between representational similarity matrices and does not suffer from limitations of CCA, which is equivalent to centered kernel alignment (CKA). Unlike CCA, CKA can reliably identify correspondences between representations in networks trained from different initializations.

I found the paper available on arXiv (arXiv:1905.00414) and also at the ICML proceedings (proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf). However, the specific DOI was not clearly displayed in the search results. If you need the exact DOI, you may want to check the official ICML proceedings page or the arXiv page directly for the complete citation information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "10f6bce8-1164-4c8a-95ed-a8d160c040af",
  "tool_use_result": {
    "query": "Kornblith \"Similarity of Neural Network Representations Revisited\" CKA ICML 2019 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BAbsJBNZuiC2Ha9WwVLygW",
        "content": [
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "https://vitalab.github.io/article/2021/01/28/SimilarityNeuralNets.html"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "https://cka-similarity.github.io/"
          },
          {
            "title": "Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton",
            "url": "https://icml.cc/media/Slides/icml/2019/halla(13-11-00)-13-12-15-4871-similarity_of_n.pdf"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "https://icml.cc/media/icml-2019/Slides/4871.pdf"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited | Request PDF",
            "url": "https://www.researchgate.net/publication/332799564_Similarity_of_Neural_Network_Representations_Revisited"
          },
          {
            "title": "SIMILARITY OF NEURAL NETWORK REPRESENTA",
            "url": "https://debug-ml-iclr2019.github.io/cameraready/DebugML-19_paper_9.pdf"
          },
          {
            "title": "[1905.00414] Similarity of Neural Network Representations Revisited",
            "url": "https://arxiv.org/abs/1905.00414"
          },
          {
            "title": "[PDF] Similarity of Neural Network Representations Revisited | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Similarity-of-Neural-Network-Representations-Kornblith-Norouzi/726320cdbd04804ffa8f3a78c095bd1b55a2a695"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "http://proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf"
          },
          {
            "title": "Similarity of Neural Network Representations Revisited",
            "url": "https://arxiv.org/pdf/1905.00414"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about this paper. The paper is by Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton from ICML 2019.\n\nThe paper introduces a similarity index that measures the relationship between representational similarity matrices and does not suffer from limitations of CCA, which is equivalent to centered kernel alignment (CKA). Unlike CCA, CKA can reliably identify correspondences between representations in networks trained from different initializations.\n\nI found the paper available on arXiv (arXiv:1905.00414) and also at the ICML proceedings (proceedings.mlr.press/v97/kornblith19a/kornblith19a.pdf). However, the specific DOI was not clearly displayed in the search results. If you need the exact DOI, you may want to check the official ICML proceedings page or the arXiv page directly for the complete citation information."
    ],
    "durationSeconds": 6.563842152999998
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for a few more details I need - Hewitt & Liang 2019, Voita & Titov 2020, Pires 2019, Wu & Dredze 2019, Karandikar 2021, Belinkov 2022, Zhao 2019, Angelopoulos 2023, and the Confidence Manifold authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "a4264728-443f-474d-a577-bb0bef723cb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 58_

Now I need details on the remaining classic papers and the Confidence Manifold authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "79687945-4026-4b07-8b83-887f68557635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QTtXmUdnMYUdZ6PEnpFcGN`</summary>

```json
{
  "query": "Hewitt Liang \"Designing and Interpreting Probes with Control Tasks\" EMNLP 2019 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "9af7edf0-1c78-440b-b4cb-d50acd601efa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Tk4Q6SEoHqnPXJjFmfKpUQ`</summary>

```json
{
  "query": "Voita Titov \"Information-Theoretic Probing with Minimum Description Length\" EMNLP 2020 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "7a95a4e1-707e-4bf6-9cad-e99ec9ca5793",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BQsYTzUomQ4rnZEDFfCdpd`</summary>

```json
{
  "query": "Karandikar \"Soft Calibration Objectives for Neural Networks\" NeurIPS 2021 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "6d10a8a2-be19-4662-ab41-fc6348947b4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SN3rZXwZ9FFNFqLcVxnw6v`</summary>

```json
{
  "query": "Angelopoulos Bates \"Conformal Prediction: A Gentle Introduction\" 2023 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "0f4ed6a6-c2af-4bfe-ac46-b5b97c996de8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WuhuN6VaF6XkQuniv19t6Q`</summary>

```json
{
  "query": "\"Confidence Manifold\" \"Geometric Structure\" correctness representations language models 2026 authors arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "65470e87-06eb-4d6c-84a1-f40d9152c787",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Sv8A9D8vAgXYL5km2VVHZ`</summary>

```json
{
  "query": "Zhao \"On Learning Invariant Representations for Domain Adaptation\" ICML 2019 authors doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8119372f-7f3a-496c-820a-ec86d4b26d74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eyR37QXWcuWRbNFtofG2L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 674,
      "cache_creation_input_tokens": 6423,
      "cache_read_input_tokens": 40993,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6423
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-21T07:38:28.287Z_

<details><summary>↩ Tool result · `toolu_01QTtXmUdnMYUdZ6PEnpFcGN`</summary>

```text
Web search results for query: "Hewitt Liang "Designing and Interpreting Probes with Control Tasks" EMNLP 2019 doi"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"},{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Designing and Interpreting Probes with Control Tasks. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1c7c8f6e4720c00cfb0b395c4827d7155"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/pdf/1909.03368"},{"title":"[1909.03368] Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/abs/1909.03368"},{"title":"Designing and Interpreting Probes with Control Tasks Percy Liang John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/public/hewitt2019control_slides.pdf"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"}]

Based on the search results, here is the information about the paper:

**"Designing and Interpreting Probes with Control Tasks"** by John Hewitt and Percy Liang was published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 2733–2743.

**DOI:** 10.18653/v1/D19-1275

**arXiv ID:** arXiv:1909.03368

The paper proposes control tasks that help identify whether probes used to predict linguistic properties of word representations actually encode linguistic structure or if the probe has learned the task itself. The paper received the Best Paper Runner Up Award at EMNLP 2019.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "cc78fa61-7859-4890-975d-bca1c0c5473e",
  "tool_use_result": {
    "query": "Hewitt Liang \"Designing and Interpreting Probes with Control Tasks\" EMNLP 2019 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Eau5RXbT8ovY68eLG12p7Z",
        "content": [
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks - ACL Anthology",
            "url": "https://aclanthology.org/D19-1275/"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/1c7c8f6e4720c00cfb0b395c4827d7155"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks | papers_we_read",
            "url": "https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"
          },
          {
            "title": "Designing and Interpreting Probes · John Hewitt",
            "url": "https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://arxiv.org/pdf/1909.03368"
          },
          {
            "title": "[1909.03368] Designing and Interpreting Probes with Control Tasks",
            "url": "https://arxiv.org/abs/1909.03368"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks Percy Liang John Hewitt",
            "url": "https://www.cs.columbia.edu/~johnhew/public/hewitt2019control_slides.pdf"
          },
          {
            "title": "[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n**\"Designing and Interpreting Probes with Control Tasks\"** by John Hewitt and Percy Liang was published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 2733–2743.\n\n**DOI:** 10.18653/v1/D19-1275\n\n**arXiv ID:** arXiv:1909.03368\n\nThe paper proposes control tasks that help identify whether probes used to predict linguistic properties of word representations actually encode linguistic structure or if the probe has learned the task itself. The paper received the Best Paper Runner Up Award at EMNLP 2019."
    ],
    "durationSeconds": 5.302304208000002
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-21T07:38:29.312Z_

<details><summary>↩ Tool result · `toolu_01Tk4Q6SEoHqnPXJjFmfKpUQ`</summary>

```text
Web search results for query: "Voita Titov "Information-Theoretic Probing with Minimum Description Length" EMNLP 2020 doi"

Links: [{"title":"Information-Theoretic Probing with Minimum Description Length - ACL Anthology","url":"https://aclanthology.org/2020.emnlp-main.14/"},{"title":"[Quick Review] Information-Theoretic Probing with Minimum Description Length","url":"https://liner.com/review/informationtheoretic-probing-with-minimum-description-length"},{"title":"Information-Theoretic Probing with Minimum Description Length | Request PDF","url":"https://www.researchgate.net/publication/347232984_Information-Theoretic_Probing_with_Minimum_Description_Length"},{"title":"Information-Theoretic Probing with MDL","url":"https://lena-voita.github.io/posts/mdl_probes.html"},{"title":"[PDF] Information-Theoretic Probing with Minimum Description Length | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Information-Theoretic-Probing-with-Minimum-Length-Voita-Titov/f4b585c9a79dfce0807b445a09036ea0f9cbcdce"},{"title":"GitHub - lena-voita/description-length-probing: This is a repository with the code for the EMNLP 2020 paper \"Information-Theoretic Probing with Minimum Description Length\"","url":"https://github.com/lena-voita/description-length-probing"},{"title":"Notes on: Information-Theoretic Probing with Minimum Description Length by Voita, E., & Titov, I. (2020) - Hugo Cisneros","url":"https://hugocisneros.com/notes/voitainformationtheoreticprobingminimum2020/"},{"title":"File Finder · lena-voita/description-length-probing","url":"https://github.com/lena-voita/description-length-probing/find/master"},{"title":"dblp: Elena Voita","url":"https://dblp.org/pid/220/4162.html"},{"title":"description-length-probing/control_tasks/example/config/emnlp19-cluster/error-analysis/ptb-pos-c0-rank1000-1hid-ELMo1-run2.yaml at master · lena-voita/description-length-probing","url":"https://github.com/lena-voita/description-length-probing/blob/master/control_tasks/example/config/emnlp19-cluster/error-analysis/ptb-pos-c0-rank1000-1hid-ELMo1-run2.yaml"}]

Based on the search results, here is the information for the paper:

**Publication Details:**

Elena Voita and Ivan Titov published "Information-Theoretic Probing with Minimum Description Length" in the Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 183–196, Online.

**DOI:** 10.18653/v1/2020.emnlp-main.14

**Paper Overview:**

The paper proposes an alternative to standard probes, information-theoretic probing with minimum description length (MDL), and considers two methods for estimating MDL which can be easily implemented on top of the standard probing pipelines: variational coding and online coding.

The paper is available at the ACL Anthology: https://aclanthology.org/2020.emnlp-main.14/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "4dfc50e0-33be-4c82-8994-bc3452b609d2",
  "tool_use_result": {
    "query": "Voita Titov \"Information-Theoretic Probing with Minimum Description Length\" EMNLP 2020 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PUTPCy22YWMCcDra1BBQYV",
        "content": [
          {
            "title": "Information-Theoretic Probing with Minimum Description Length - ACL Anthology",
            "url": "https://aclanthology.org/2020.emnlp-main.14/"
          },
          {
            "title": "[Quick Review] Information-Theoretic Probing with Minimum Description Length",
            "url": "https://liner.com/review/informationtheoretic-probing-with-minimum-description-length"
          },
          {
            "title": "Information-Theoretic Probing with Minimum Description Length | Request PDF",
            "url": "https://www.researchgate.net/publication/347232984_Information-Theoretic_Probing_with_Minimum_Description_Length"
          },
          {
            "title": "Information-Theoretic Probing with MDL",
            "url": "https://lena-voita.github.io/posts/mdl_probes.html"
          },
          {
            "title": "[PDF] Information-Theoretic Probing with Minimum Description Length | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Information-Theoretic-Probing-with-Minimum-Length-Voita-Titov/f4b585c9a79dfce0807b445a09036ea0f9cbcdce"
          },
          {
            "title": "GitHub - lena-voita/description-length-probing: This is a repository with the code for the EMNLP 2020 paper \"Information-Theoretic Probing with Minimum Description Length\"",
            "url": "https://github.com/lena-voita/description-length-probing"
          },
          {
            "title": "Notes on: Information-Theoretic Probing with Minimum Description Length by Voita, E., & Titov, I. (2020) - Hugo Cisneros",
            "url": "https://hugocisneros.com/notes/voitainformationtheoreticprobingminimum2020/"
          },
          {
            "title": "File Finder · lena-voita/description-length-probing",
            "url": "https://github.com/lena-voita/description-length-probing/find/master"
          },
          {
            "title": "dblp: Elena Voita",
            "url": "https://dblp.org/pid/220/4162.html"
          },
          {
            "title": "description-length-probing/control_tasks/example/config/emnlp19-cluster/error-analysis/ptb-pos-c0-rank1000-1hid-ELMo1-run2.yaml at master · lena-voita/description-length-probing",
            "url": "https://github.com/lena-voita/description-length-probing/blob/master/control_tasks/example/config/emnlp19-cluster/error-analysis/ptb-pos-c0-rank1000-1hid-ELMo1-run2.yaml"
          }
        ]
      },
      "Based on the search results, here is the information for the paper:\n\n**Publication Details:**\n\nElena Voita and Ivan Titov published \"Information-Theoretic Probing with Minimum Description Length\" in the Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 183–196, Online.\n\n**DOI:** 10.18653/v1/2020.emnlp-main.14\n\n**Paper Overview:**\n\nThe paper proposes an alternative to standard probes, information-theoretic probing with minimum description length (MDL), and considers two methods for estimating MDL which can be easily implemented on top of the standard probing pipelines: variational coding and online coding.\n\nThe paper is available at the ACL Anthology: https://aclanthology.org/2020.emnlp-main.14/"
    ],
    "durationSeconds": 5.157730542000005
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T07:38:29.968Z_

<details><summary>↩ Tool result · `toolu_01SN3rZXwZ9FFNFqLcVxnw6v`</summary>

```text
Web search results for query: "Angelopoulos Bates "Conformal Prediction: A Gentle Introduction" 2023 arxiv"

Links: [{"title":"A Gentle Introduction to Conformal Time Series Forecasting","url":"https://arxiv.org/pdf/2511.13608"},{"title":"Conformal Prediction: A Gentle Introduction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Conformal-Prediction:-A-Gentle-Introduction-Angelopoulos-Bates/ed112ef477d496a3b45f79fc5ef466d3fe77d066"},{"title":"Publications - Anastasios Angelopoulos","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/html/2107.07511v6"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://www.researchgate.net/publication/353284898_A_Gentle_Introduction_to_Conformal_Prediction_and_Distribution-Free_Uncertainty_Quantification"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210707511A/abstract"},{"title":"Conformal Prediction: : A Gentle Introduction: Foundations and Trends® in Machine Learning: Vol 16, No 4","url":"https://dl.acm.org/doi/10.1561/2200000101"}]

I found the paper you're looking for. The paper "Conformal Prediction: A Gentle Introduction" by Anastasios N. Angelopoulos and Stephen Bates was published in March 2023. 

It was published in Foundations and Trends in Machine Learning, volume 16, pages 494-591. The paper is available through Now Publishers, Inc.

Additionally, there is an earlier arxiv version of a related work: Angelopoulos and Bates also published "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification" on arxiv (2107.07511), which covers similar content on conformal prediction methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8df71a13-4319-4eef-97e4-9ed0147163f4",
  "tool_use_result": {
    "query": "Angelopoulos Bates \"Conformal Prediction: A Gentle Introduction\" 2023 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ADCwrHHDGDmsHQMThuVPx",
        "content": [
          {
            "title": "A Gentle Introduction to Conformal Time Series Forecasting",
            "url": "https://arxiv.org/pdf/2511.13608"
          },
          {
            "title": "Conformal Prediction: A Gentle Introduction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Conformal-Prediction:-A-Gentle-Introduction-Angelopoulos-Bates/ed112ef477d496a3b45f79fc5ef466d3fe77d066"
          },
          {
            "title": "Publications - Anastasios Angelopoulos",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/publications/"
          },
          {
            "title": "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
            "url": "https://arxiv.org/html/2107.07511v6"
          },
          {
            "title": "[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
            "url": "https://arxiv.org/abs/2107.07511"
          },
          {
            "title": "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
            "url": "https://www.researchgate.net/publication/353284898_A_Gentle_Introduction_to_Conformal_Prediction_and_Distribution-Free_Uncertainty_Quantification"
          },
          {
            "title": "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210707511A/abstract"
          },
          {
            "title": "Conformal Prediction: : A Gentle Introduction: Foundations and Trends® in Machine Learning: Vol 16, No 4",
            "url": "https://dl.acm.org/doi/10.1561/2200000101"
          }
        ]
      },
      "I found the paper you're looking for. The paper \"Conformal Prediction: A Gentle Introduction\" by Anastasios N. Angelopoulos and Stephen Bates was published in March 2023. \n\nIt was published in Foundations and Trends in Machine Learning, volume 16, pages 494-591. The paper is available through Now Publishers, Inc.\n\nAdditionally, there is an earlier arxiv version of a related work: Angelopoulos and Bates also published \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\" on arxiv (2107.07511), which covers similar content on conformal prediction methods."
    ],
    "durationSeconds": 4.583300144999987
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T07:38:30.815Z_

<details><summary>↩ Tool result · `toolu_01BQsYTzUomQ4rnZEDFfCdpd`</summary>

```text
Web search results for query: "Karandikar "Soft Calibration Objectives for Neural Networks" NeurIPS 2021 doi"

Links: [{"title":"[Quick Review] Soft Calibration Objectives for Neural Networks","url":"https://liner.com/review/soft-calibration-objectives-for-neural-networks"},{"title":"Soft Calibration Objectives for Neural Networks - researchr publication","url":"https://researchr.org/publication/KarandikarCTLSM21"},{"title":"Soft Calibration Objectives for Neural Networks","url":"https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html"},{"title":"Soft Calibration Objectives for Neural Networks","url":"https://research.google/pubs/pub50844/"},{"title":"[2108.00106] Soft Calibration Objectives for Neural Networks","url":"https://arxiv.org/abs/2108.00106"},{"title":"Soft Calibration Objectives for Neural Networks Archit Karandikar∗","url":"https://openreview.net/pdf?id=-tVD13hOsQ3"},{"title":"[PDF] Soft Calibration Objectives for Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Soft-Calibration-Objectives-for-Neural-Networks-Karandikar-Cain/7416930f69bec3d0b712b9dd3b5e7aa6d3dfec58"},{"title":"Soft Calibration Objectives for Neural Networks Archit Karandikar∗","url":"https://proceedings.neurips.cc/paper/2021/file/f8905bd3df64ace64a68e154ba72f24c-Paper.pdf"},{"title":"Soft calibration objectives for neural networks | Proceedings of the 35th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3540261.3542539"}]

Based on the search results, here's what I found about this paper:

The paper "Soft Calibration Objectives for Neural Networks" was authored by Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer, and Becca Roelofs, and was published in Advances in Neural Information Processing Systems 34 (NeurIPS 2021) in December 2021.

The paper proposes Soft Calibration Objectives, SB-ECE and S-AvUC, which utilize differentiable soft (continuous) binning to enable direct optimization of calibration during neural network training.

The paper is available through multiple sources including:
- arXiv (2108.00106)
- The official NeurIPS proceedings
- The ACM Digital Library (with DOI 10.5555/3540261.3542539)

However, I was unable to locate the specific DOI in the format typically used (e.g., 10.xxxx/xxxxx) in these search results. You may want to check the NeurIPS proceedings page directly or the arXiv page for the complete DOI information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "2a299b2a-a905-4d61-939d-1347fb731066",
  "tool_use_result": {
    "query": "Karandikar \"Soft Calibration Objectives for Neural Networks\" NeurIPS 2021 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RsJs7FRLFHG5n3qAKJMEEJ",
        "content": [
          {
            "title": "[Quick Review] Soft Calibration Objectives for Neural Networks",
            "url": "https://liner.com/review/soft-calibration-objectives-for-neural-networks"
          },
          {
            "title": "Soft Calibration Objectives for Neural Networks - researchr publication",
            "url": "https://researchr.org/publication/KarandikarCTLSM21"
          },
          {
            "title": "Soft Calibration Objectives for Neural Networks",
            "url": "https://proceedings.neurips.cc/paper/2021/hash/f8905bd3df64ace64a68e154ba72f24c-Abstract.html"
          },
          {
            "title": "Soft Calibration Objectives for Neural Networks",
            "url": "https://research.google/pubs/pub50844/"
          },
          {
            "title": "[2108.00106] Soft Calibration Objectives for Neural Networks",
            "url": "https://arxiv.org/abs/2108.00106"
          },
          {
            "title": "Soft Calibration Objectives for Neural Networks Archit Karandikar∗",
            "url": "https://openreview.net/pdf?id=-tVD13hOsQ3"
          },
          {
            "title": "[PDF] Soft Calibration Objectives for Neural Networks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Soft-Calibration-Objectives-for-Neural-Networks-Karandikar-Cain/7416930f69bec3d0b712b9dd3b5e7aa6d3dfec58"
          },
          {
            "title": "Soft Calibration Objectives for Neural Networks Archit Karandikar∗",
            "url": "https://proceedings.neurips.cc/paper/2021/file/f8905bd3df64ace64a68e154ba72f24c-Paper.pdf"
          },
          {
            "title": "Soft calibration objectives for neural networks | Proceedings of the 35th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3540261.3542539"
          }
        ]
      },
      "Based on the search results, here's what I found about this paper:\n\nThe paper \"Soft Calibration Objectives for Neural Networks\" was authored by Archit Karandikar, Nicholas Cain, Dustin Tran, Balaji Lakshminarayanan, Jonathon Shlens, Michael C. Mozer, and Becca Roelofs, and was published in Advances in Neural Information Processing Systems 34 (NeurIPS 2021) in December 2021.\n\nThe paper proposes Soft Calibration Objectives, SB-ECE and S-AvUC, which utilize differentiable soft (continuous) binning to enable direct optimization of calibration during neural network training.\n\nThe paper is available through multiple sources including:\n- arXiv (2108.00106)\n- The official NeurIPS proceedings\n- The ACM Digital Library (with DOI 10.5555/3540261.3542539)\n\nHowever, I was unable to locate the specific DOI in the format typically used (e.g., 10.xxxx/xxxxx) in these search results. You may want to check the NeurIPS proceedings page directly or the arXiv page for the complete DOI information."
    ],
    "durationSeconds": 6.324002874000013
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-21T07:38:31.357Z_

<details><summary>↩ Tool result · `toolu_019Sv8A9D8vAgXYL5km2VVHZ`</summary>

```text
Web search results for query: "Zhao "On Learning Invariant Representations for Domain Adaptation" ICML 2019 authors doi"

Links: [{"title":"On learning invariant representations for domain adaptation - Illinois Experts","url":"https://experts.illinois.edu/en/publications/on-learning-invariant-representations-for-domain-adaptation/"},{"title":"On Learning Invariant Representations for Domain Adaptation. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/17f7e62074e77e75ad75658cb31495002"},{"title":"dblp: On Learning Invariant Representations for Domain Adaptation.","url":"https://dblp.org/rec/conf/icml/0002CZG19.html"},{"title":"On Learning Invariant Representation for Domain Adaptation","url":"https://arxiv.org/pdf/1901.09453"},{"title":"On Learning Invariant Representations for Domain Adaptation","url":"http://proceedings.mlr.press/v97/zhao19a/zhao19a.pdf"},{"title":"On Learning Invariant Representations for Domain Adaptation","url":"https://hanzhaoml.github.io/papers/ICML2019/poster.pdf"},{"title":"On Learning Invariant Representations for Domain Adaptation – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2019/09/13/on-learning-invariant-representations-for-domain-adaptation/"},{"title":"Class-Imbalanced Domain Adaptation: An Empirical Odyssey | Computer Vision – ECCV 2020 Workshops","url":"https://dl.acm.org/doi/10.1007/978-3-030-66415-2_38"},{"title":"ICML 2019 On Learning Invariant Representations for Domain Adaptation Oral","url":"https://icml.cc/virtual/2019/oral/4357"}]

Based on the search results, here is the information about the paper:

**Authors:** Zhao, H., des Combes, R. T., Zhang, K., & Gordon, G. J.

**Full Citation:** On learning invariant representations for domain adaptation. In 36th International Conference on Machine Learning, ICML 2019 (pp. 12985-12999)

**DOI/Pages:** Pages 7523-7532 in Proceedings of Machine Learning Research, volume 97

**Additional Details:**
- Authors are from Carnegie Mellon University and Microsoft Research Montreal
- The paper is available on arXiv with preprint number 1901.09453

The proceedings can be accessed at: http://proceedings.mlr.press/v97/zhao19a.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8a37777e-a9ec-4762-9387-7ef71491a05e",
  "tool_use_result": {
    "query": "Zhao \"On Learning Invariant Representations for Domain Adaptation\" ICML 2019 authors doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T8vtBNnMpJoec3bV1mnp8i",
        "content": [
          {
            "title": "On learning invariant representations for domain adaptation - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/on-learning-invariant-representations-for-domain-adaptation/"
          },
          {
            "title": "On Learning Invariant Representations for Domain Adaptation. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/17f7e62074e77e75ad75658cb31495002"
          },
          {
            "title": "dblp: On Learning Invariant Representations for Domain Adaptation.",
            "url": "https://dblp.org/rec/conf/icml/0002CZG19.html"
          },
          {
            "title": "On Learning Invariant Representation for Domain Adaptation",
            "url": "https://arxiv.org/pdf/1901.09453"
          },
          {
            "title": "On Learning Invariant Representations for Domain Adaptation",
            "url": "http://proceedings.mlr.press/v97/zhao19a/zhao19a.pdf"
          },
          {
            "title": "On Learning Invariant Representations for Domain Adaptation",
            "url": "https://hanzhaoml.github.io/papers/ICML2019/poster.pdf"
          },
          {
            "title": "On Learning Invariant Representations for Domain Adaptation – Machine Learning Blog | ML@CMU | Carnegie Mellon University",
            "url": "https://blog.ml.cmu.edu/2019/09/13/on-learning-invariant-representations-for-domain-adaptation/"
          },
          {
            "title": "Class-Imbalanced Domain Adaptation: An Empirical Odyssey | Computer Vision – ECCV 2020 Workshops",
            "url": "https://dl.acm.org/doi/10.1007/978-3-030-66415-2_38"
          },
          {
            "title": "ICML 2019 On Learning Invariant Representations for Domain Adaptation Oral",
            "url": "https://icml.cc/virtual/2019/oral/4357"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n**Authors:** Zhao, H., des Combes, R. T., Zhang, K., & Gordon, G. J.\n\n**Full Citation:** On learning invariant representations for domain adaptation. In 36th International Conference on Machine Learning, ICML 2019 (pp. 12985-12999)\n\n**DOI/Pages:** Pages 7523-7532 in Proceedings of Machine Learning Research, volume 97\n\n**Additional Details:**\n- Authors are from Carnegie Mellon University and Microsoft Research Montreal\n- The paper is available on arXiv with preprint number 1901.09453\n\nThe proceedings can be accessed at: http://proceedings.mlr.press/v97/zhao19a.html"
    ],
    "durationSeconds": 4.292733143999998
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T07:38:34.367Z_

<details><summary>↩ Tool result · `toolu_01WuhuN6VaF6XkQuniv19t6Q`</summary>

```text
Web search results for query: ""Confidence Manifold" "Geometric Structure" correctness representations language models 2026 authors arxiv"

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning","url":"https://arxiv.org/html/2605.16824"},{"title":"[2605.16824] Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning","url":"https://arxiv.org/abs/2605.16824"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/html/2602.00977"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/pdf/2602.00977"},{"title":"Latent Trajectory Dynamics in Large Language Models: A Manifold Evolution Framework with Empirical Validation","url":"https://arxiv.org/html/2505.20340"},{"title":"A Geometric Perspective on Next-Token Prediction in Large Language Models: Three Emerging Phases","url":"https://arxiv.org/html/2605.09011v1"}]

I found a paper matching your query! Here are the results:

## Primary Result

The paper "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models" demonstrates that the discriminative signal for correctness concentrates in 3–8 dimensions, substantially lower than the high-dimensional activation space. The paper was published on February 8, 2026.

The research studied 9 models across 5 architecture families, from 124M-parameter GPT-2 to 7B-parameter Mistral. A 7B model with 4096-dimensional hidden states encodes correctness in just 5 dimensions, 0.12% of its representational capacity.

## Key Findings

Internal probes outperform the best output method by 23–37 percentage points, with even the training-free centroid classifier, using just cluster means in 8D PLS space, far exceeding any output signal.

Cross-layer similarity analysis reveals block-diagonal structure with consistent phase boundaries: Phase I (0–30% depth) performs token-level feature extraction with low similarity to later layers; Phase II (30–70%) integrates semantics with gradual probe weight rotation; Phase III (70–100%) encodes stable confidence with high intra-phase coherence.

The paper is available on arXiv at https://arxiv.org/abs/2602.08159


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "060fa741-802f-4bcd-aff5-290e2ede6c9d",
  "tool_use_result": {
    "query": "\"Confidence Manifold\" \"Geometric Structure\" correctness representations language models 2026 authors arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QHfp6ZUxbZtCr2KCQSudGB",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning",
            "url": "https://arxiv.org/html/2605.16824"
          },
          {
            "title": "[2605.16824] Confidence Geometry Reveals Trace-Level Correctness in Large Language Model Reasoning",
            "url": "https://arxiv.org/abs/2605.16824"
          },
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals",
            "url": "https://arxiv.org/html/2602.00977"
          },
          {
            "title": "Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals",
            "url": "https://arxiv.org/pdf/2602.00977"
          },
          {
            "title": "Latent Trajectory Dynamics in Large Language Models: A Manifold Evolution Framework with Empirical Validation",
            "url": "https://arxiv.org/html/2505.20340"
          },
          {
            "title": "A Geometric Perspective on Next-Token Prediction in Large Language Models: Three Emerging Phases",
            "url": "https://arxiv.org/html/2605.09011v1"
          }
        ]
      },
      "I found a paper matching your query! Here are the results:\n\n## Primary Result\n\nThe paper \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\" demonstrates that the discriminative signal for correctness concentrates in 3–8 dimensions, substantially lower than the high-dimensional activation space. The paper was published on February 8, 2026.\n\nThe research studied 9 models across 5 architecture families, from 124M-parameter GPT-2 to 7B-parameter Mistral. A 7B model with 4096-dimensional hidden states encodes correctness in just 5 dimensions, 0.12% of its representational capacity.\n\n## Key Findings\n\nInternal probes outperform the best output method by 23–37 percentage points, with even the training-free centroid classifier, using just cluster means in 8D PLS space, far exceeding any output signal.\n\nCross-layer similarity analysis reveals block-diagonal structure with consistent phase boundaries: Phase I (0–30% depth) performs token-level feature extraction with low similarity to later layers; Phase II (30–70%) integrates semantics with gradual probe weight rotation; Phase III (70–100%) encodes stable confidence with high intra-phase coherence.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2602.08159"
    ],
    "durationSeconds": 8.016153139999995
  }
}
```

</details>

---

### Assistant

_source line 71_

<details><summary>Logged reasoning block</summary>

```text
Let me get a few more details - Confidence Manifold authors, Pires 2019, Wu & Dredze 2019, Belinkov 2022 DOIs. And I need to get author details for the Confidence Manifold paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "cbec0a3d-2ce2-48c1-a76a-40a2a2fee5ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 72_

Let me get the remaining details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "de410cd7-2d71-4bc5-b94c-58742bccfd3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 73_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B7BJF1kry42k3MsXgiaizn`</summary>

```json
{
  "query": "arxiv 2602.08159 \"Confidence Manifold\" authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "21df4142-ff90-494b-821a-ea6cfd38ab1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FezA2Kqk7AfRrSgRM1uRfq`</summary>

```json
{
  "query": "Pires \"How Multilingual is Multilingual BERT\" ACL 2019 doi authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e9777735-bd13-4027-85bf-6fd336187540",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PudNMSFGPUgJGCfuPpPAmS`</summary>

```json
{
  "query": "Wu Dredze \"Beto Bentz Becas\" cross-lingual BERT EMNLP 2019 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "bac62a75-706d-49df-a2dc-6f7cf32c637c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012k31kTPM3e5AVgfnD9WQi9`</summary>

```json
{
  "query": "Belinkov \"Probing Classifiers: Promises Shortcomings Advances\" Computational Linguistics 2022 doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "121e8034-e1a2-456c-86e5-ffd698d66e35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EBWcCSRVbNBwg38rmCLk6m`</summary>

```json
{
  "query": "Xiao 2025 ACL \"knowledge boundary\" multilingual LLM authors full list doi aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "be1bbc37-a55f-48c8-96ff-61ccb44faf9c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T07:38:43.712Z_

<details><summary>↩ Tool result · `toolu_01FezA2Kqk7AfRrSgRM1uRfq`</summary>

```text
Web search results for query: "Pires "How Multilingual is Multilingual BERT" ACL 2019 doi authors"

Links: [{"title":"How Multilingual is Multilingual BERT? - ACL Anthology","url":"https://aclanthology.org/P19-1493/"},{"title":"Machine Translation Weekly 15: How Multilingual is Multiligual BERT? | Jindřich’s blog","url":"https://jlibovicky.github.io/2019/10/18/MT-Weekly-Multilingual-BERT.html"},{"title":"[1906.01502] How multilingual is Multilingual BERT?","url":"https://arxiv.org/abs/1906.01502"},{"title":"[Quick Review] How Multilingual is Multilingual BERT?","url":"https://liner.com/review/how-multilingual-is-multilingual-bert"},{"title":"Multilingual BERT","url":"https://www.summarizepaper.com/en/arxiv-id/1906.01502v1/"},{"title":"Paper page - How multilingual is Multilingual BERT?","url":"https://paperswithcode.com/paper/how-multilingual-is-multilingual-bert"},{"title":"[PDF] How Multilingual is Multilingual BERT? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Multilingual-is-Multilingual-BERT-Pires-Schlinger/809cc93921e4698bde891475254ad6dfba33d03b"},{"title":"How Multilingual is Multilingual BERT? | Request PDF","url":"https://www.researchgate.net/publication/335783767_How_Multilingual_is_Multilingual_BERT"},{"title":"How multilingual is Multilingual BERT? Telmo Pires∗ Eva Schlinger Dan Garrette","url":"http://www.dhgarrette.com/papers/pires_multilingual_bert_acl2019.pdf"},{"title":"How multilingual is Multilingual BERT?","url":"https://arxiv.org/pdf/1906.01502"}]

Based on the search results, here is the information about the paper:

**Title:** How Multilingual is Multilingual BERT?

**Authors:** Telmo Pires, Eva Schlinger, and Dan Garrette

**Conference:** Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, July 2019, Florence, Italy

**DOI:** 10.18653/v1/P19-1493

**Pages:** 4996–5001


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8366aa3b-3582-4d95-b995-f8c3f51c0e6e",
  "tool_use_result": {
    "query": "Pires \"How Multilingual is Multilingual BERT\" ACL 2019 doi authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FxemCqUkCwHtptGFuviiJQ",
        "content": [
          {
            "title": "How Multilingual is Multilingual BERT? - ACL Anthology",
            "url": "https://aclanthology.org/P19-1493/"
          },
          {
            "title": "Machine Translation Weekly 15: How Multilingual is Multiligual BERT? | Jindřich’s blog",
            "url": "https://jlibovicky.github.io/2019/10/18/MT-Weekly-Multilingual-BERT.html"
          },
          {
            "title": "[1906.01502] How multilingual is Multilingual BERT?",
            "url": "https://arxiv.org/abs/1906.01502"
          },
          {
            "title": "[Quick Review] How Multilingual is Multilingual BERT?",
            "url": "https://liner.com/review/how-multilingual-is-multilingual-bert"
          },
          {
            "title": "Multilingual BERT",
            "url": "https://www.summarizepaper.com/en/arxiv-id/1906.01502v1/"
          },
          {
            "title": "Paper page - How multilingual is Multilingual BERT?",
            "url": "https://paperswithcode.com/paper/how-multilingual-is-multilingual-bert"
          },
          {
            "title": "[PDF] How Multilingual is Multilingual BERT? | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/How-Multilingual-is-Multilingual-BERT-Pires-Schlinger/809cc93921e4698bde891475254ad6dfba33d03b"
          },
          {
            "title": "How Multilingual is Multilingual BERT? | Request PDF",
            "url": "https://www.researchgate.net/publication/335783767_How_Multilingual_is_Multilingual_BERT"
          },
          {
            "title": "How multilingual is Multilingual BERT? Telmo Pires∗ Eva Schlinger Dan Garrette",
            "url": "http://www.dhgarrette.com/papers/pires_multilingual_bert_acl2019.pdf"
          },
          {
            "title": "How multilingual is Multilingual BERT?",
            "url": "https://arxiv.org/pdf/1906.01502"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n**Title:** How Multilingual is Multilingual BERT?\n\n**Authors:** Telmo Pires, Eva Schlinger, and Dan Garrette\n\n**Conference:** Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, July 2019, Florence, Italy\n\n**DOI:** 10.18653/v1/P19-1493\n\n**Pages:** 4996–5001"
    ],
    "durationSeconds": 3.7863220759999967
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GxCATPwZRdBZBpkTzLjFvt`</summary>

```json
{
  "query": "Zhou LACE \"Beyond the Final Layer\" arxiv 2510.03136 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b4857fd5-034d-4bdf-a203-cf5d81e7ae34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LqHTPaPAAMVr1C1aUeHRG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 697,
      "cache_creation_input_tokens": 5103,
      "cache_read_input_tokens": 47416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5103
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T07:38:45.459Z_

<details><summary>↩ Tool result · `toolu_01PudNMSFGPUgJGCfuPpPAmS`</summary>

```text
Web search results for query: "Wu Dredze "Beto Bentz Becas" cross-lingual BERT EMNLP 2019 doi"

Links: [{"title":"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT - researchr publication","url":"https://researchr.org/publication/WuD19-8"},{"title":"Beto, Bentz, Becas: The surprising cross-lingual effectiveness of Bert - Johns Hopkins University","url":"https://pure.johnshopkins.edu/en/publications/beto-bentz-becas-the-surprising-cross-lingual-effectiveness-of-be/"},{"title":"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT - ACL Anthology","url":"https://aclanthology.org/D19-1077/"},{"title":"CROSS-LINGUAL ABILITY OF MULTILINGUAL BERT","url":"https://openreview.net/pdf?id=HJeT3yrtDr"},{"title":"dblp: Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT.","url":"https://dblp.org/rec/conf/emnlp/WuD19.html"},{"title":"[PDF] Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beto,-Bentz,-Becas:-The-Surprising-Cross-Lingual-of-Wu-Dredze/2fa3f7ce620a1c7155daef6620dd6bb0e01934f3"},{"title":"(PDF) Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT","url":"https://www.researchgate.net/publication/336997478_Beto_Bentz_Becas_The_Surprising_Cross-Lingual_Effectiveness_of_BERT"},{"title":"GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub","url":"https://github.com/shijie-wu/crosslingual-nlp"},{"title":"[1904.09077] Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT","url":"https://arxiv.org/abs/1904.09077"},{"title":"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT","url":"https://arxiv.org/pdf/1904.09077"}]

Based on the search results, here is the information about the paper:

**Title:** "Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT" by Shijie Wu and Mark Dredze, published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP 2019) in Hong Kong, China, November 3-7, 2019, pages 833-844.

**DOI:** 10.18653/v1/D19-1077

**Summary:** The paper explores the broader cross-lingual potential of multilingual BERT (mBERT) as a zero shot language transfer model on 5 NLP tasks covering a total of 39 languages from various language families: NLI, document classification, NER, POS tagging, and dependency parsing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "903ee391-2106-44e4-914a-f74acbc0b975",
  "tool_use_result": {
    "query": "Wu Dredze \"Beto Bentz Becas\" cross-lingual BERT EMNLP 2019 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RoR2ss6jri8abcG3DtXUpk",
        "content": [
          {
            "title": "Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT - researchr publication",
            "url": "https://researchr.org/publication/WuD19-8"
          },
          {
            "title": "Beto, Bentz, Becas: The surprising cross-lingual effectiveness of Bert - Johns Hopkins University",
            "url": "https://pure.johnshopkins.edu/en/publications/beto-bentz-becas-the-surprising-cross-lingual-effectiveness-of-be/"
          },
          {
            "title": "Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT - ACL Anthology",
            "url": "https://aclanthology.org/D19-1077/"
          },
          {
            "title": "CROSS-LINGUAL ABILITY OF MULTILINGUAL BERT",
            "url": "https://openreview.net/pdf?id=HJeT3yrtDr"
          },
          {
            "title": "dblp: Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT.",
            "url": "https://dblp.org/rec/conf/emnlp/WuD19.html"
          },
          {
            "title": "[PDF] Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Beto,-Bentz,-Becas:-The-Surprising-Cross-Lingual-of-Wu-Dredze/2fa3f7ce620a1c7155daef6620dd6bb0e01934f3"
          },
          {
            "title": "(PDF) Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT",
            "url": "https://www.researchgate.net/publication/336997478_Beto_Bentz_Becas_The_Surprising_Cross-Lingual_Effectiveness_of_BERT"
          },
          {
            "title": "GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub",
            "url": "https://github.com/shijie-wu/crosslingual-nlp"
          },
          {
            "title": "[1904.09077] Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT",
            "url": "https://arxiv.org/abs/1904.09077"
          },
          {
            "title": "Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT",
            "url": "https://arxiv.org/pdf/1904.09077"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n**Title:** \"Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of BERT\" by Shijie Wu and Mark Dredze, published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP 2019) in Hong Kong, China, November 3-7, 2019, pages 833-844.\n\n**DOI:** 10.18653/v1/D19-1077\n\n**Summary:** The paper explores the broader cross-lingual potential of multilingual BERT (mBERT) as a zero shot language transfer model on 5 NLP tasks covering a total of 39 languages from various language families: NLI, document classification, NER, POS tagging, and dependency parsing."
    ],
    "durationSeconds": 4.464472586999997
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-21T07:38:46.233Z_

<details><summary>↩ Tool result · `toolu_012k31kTPM3e5AVgfnD9WQi9`</summary>

```text
Web search results for query: "Belinkov "Probing Classifiers: Promises Shortcomings Advances" Computational Linguistics 2022 doi"

Links: [{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"(PDF) Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"}]

Based on the search results, here is the information for the paper:

**Publication Details:**

Title: "Probing Classifiers: Promises, Shortcomings, and Advances"
Author: Yonatan Belinkov
Journal: Computational Linguistics
Volume: 48, Issue: 1
Month: March
Year: 2022
Pages: 207–219
DOI: 10.1162/coli_a_00422
Publisher: MIT Press

The paper discusses how probing classifiers have emerged as a prominent methodology for interpreting deep neural network models in NLP, with the basic idea being that a classifier is trained to predict linguistic properties from a model's representations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "f81d4a88-8f6a-4ebd-9fa2-8183c6d3a227",
  "tool_use_result": {
    "query": "Belinkov \"Probing Classifiers: Promises Shortcomings Advances\" Computational Linguistics 2022 doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_011YZ6YM7Y6EusAAtakKNtGx",
        "content": [
          {
            "title": "@article{belinkov-2022-probing,",
            "url": "https://aclanthology.org/2022.cl-1.7.bib"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology",
            "url": "https://aclanthology.org/2022.cl-1.7/"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology",
            "url": "https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal",
            "url": "https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"
          },
          {
            "title": "Yonatan Belinkov | publications",
            "url": "https://belinkov.com/publications/publicationstype/"
          },
          {
            "title": "(PDF) Probing Classifiers: Promises, Shortcomings, and Advances",
            "url": "https://www.researchgate.net/publication/355072709_Probing_Classifiers_Promises_Shortcomings_and_Advances"
          },
          {
            "title": "[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances",
            "url": "https://arxiv.org/abs/2102.12452"
          }
        ]
      },
      "Based on the search results, here is the information for the paper:\n\n**Publication Details:**\n\nTitle: \"Probing Classifiers: Promises, Shortcomings, and Advances\"\nAuthor: Yonatan Belinkov\nJournal: Computational Linguistics\nVolume: 48, Issue: 1\nMonth: March\nYear: 2022\nPages: 207–219\nDOI: 10.1162/coli_a_00422\nPublisher: MIT Press\n\nThe paper discusses how probing classifiers have emerged as a prominent methodology for interpreting deep neural network models in NLP, with the basic idea being that a classifier is trained to predict linguistic properties from a model's representations."
    ],
    "durationSeconds": 4.246265857999999
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-21T07:38:48.421Z_

<details><summary>↩ Tool result · `toolu_01GxCATPwZRdBZBpkTzLjFvt`</summary>

```text
Web search results for query: "Zhou LACE "Beyond the Final Layer" arxiv 2510.03136 authors full list"

Links: [{"title":"[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/abs/2510.03136"},{"title":"Layer by Layer: Uncovering Hidden Representations in Language Models","url":"https://arxiv.org/pdf/2502.02013"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/html/2510.03136"},{"title":"Suppressing Final Layer Hidden State Jumps in Transformer Pretraining","url":"https://arxiv.org/pdf/2601.18302"},{"title":"Multimodal Language Models See Better When They Look Shallower","url":"https://arxiv.org/pdf/2504.21447"}]

Based on the search results, the authors of the paper "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models" (arXiv 2510.03136) are: Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "fdf149f5-b755-400b-b192-11839448583a",
  "tool_use_result": {
    "query": "Zhou LACE \"Beyond the Final Layer\" arxiv 2510.03136 authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QPiaLC2BcDZw9XvZAtrLjs",
        "content": [
          {
            "title": "[2510.03136] Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/abs/2510.03136"
          },
          {
            "title": "Layer by Layer: Uncovering Hidden Representations in Language Models",
            "url": "https://arxiv.org/pdf/2502.02013"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/html/2510.03136"
          },
          {
            "title": "Suppressing Final Layer Hidden State Jumps in Transformer Pretraining",
            "url": "https://arxiv.org/pdf/2601.18302"
          },
          {
            "title": "Multimodal Language Models See Better When They Look Shallower",
            "url": "https://arxiv.org/pdf/2504.21447"
          }
        ]
      },
      "Based on the search results, the authors of the paper \"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models\" (arXiv 2510.03136) are: Ej Zhou, Caiqi Zhang, Tiancheng Hu, Chengzu Li, Nigel Collier, Ivan Vulić, and Anna Korhonen."
    ],
    "durationSeconds": 4.561235543000002
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-21T07:38:49.009Z_

<details><summary>↩ Tool result · `toolu_01EBWcCSRVbNBwg38rmCLk6m`</summary>

```text
Web search results for query: "Xiao 2025 ACL "knowledge boundary" multilingual LLM authors full list doi aclanthology"

Links: [{"title":"GitHub - DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries: [ACL 2025] Analyzing LLMs' Multilingual Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations","url":"https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries"},{"title":"Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1174/"},{"title":"Knowledge Boundary of Large Language Models: A Survey - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.256/"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"Analyzing LLMs' Knowledge Boundary Cognition Across ...","url":"https://aclanthology.org/2025.acl-long.1174.pdf"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations

**Full Author List:** Chenghao Xiao, Hou Pong Chan, Hao Zhang, Mahani Aljunied, Lidong Bing, Noura Al Moubayed, and Yu Rong

**DOI:** 10.18653/v1/2025.acl-long.1174

**ACL Anthology URL:** https://aclanthology.org/2025.acl-long.1174/

**Conference:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)

**Year:** 2025

The paper presents the first study to analyze how LLMs recognize knowledge boundaries across different languages by probing their internal representations when processing known and unknown questions in multiple languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "78b68505-8bba-4e52-9f04-d4b9247fc264",
  "tool_use_result": {
    "query": "Xiao 2025 ACL \"knowledge boundary\" multilingual LLM authors full list doi aclanthology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RjaddXFgaP6Pe1jT5Tqy3n",
        "content": [
          {
            "title": "GitHub - DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries: [ACL 2025] Analyzing LLMs' Multilingual Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations",
            "url": "https://github.com/DAMO-NLP-SG/LLM-Multilingual-Knowledge-Boundaries"
          },
          {
            "title": "Analyzing LLMs’ Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1174/"
          },
          {
            "title": "Knowledge Boundary of Large Language Models: A Survey - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.256/"
          },
          {
            "title": "The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology",
            "url": "https://aclanthology.org/events/emnlp-2025/"
          },
          {
            "title": "Accepted Main Conference Papers - ACL 2025",
            "url": "https://2025.aclweb.org/program/main_papers/"
          },
          {
            "title": "Analyzing LLMs' Knowledge Boundary Cognition Across ...",
            "url": "https://aclanthology.org/2025.acl-long.1174.pdf"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2025",
            "url": "https://2025.naacl.org/program/accepted_papers/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Paper Title:** Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations\n\n**Full Author List:** Chenghao Xiao, Hou Pong Chan, Hao Zhang, Mahani Aljunied, Lidong Bing, Noura Al Moubayed, and Yu Rong\n\n**DOI:** 10.18653/v1/2025.acl-long.1174\n\n**ACL Anthology URL:** https://aclanthology.org/2025.acl-long.1174/\n\n**Conference:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)\n\n**Year:** 2025\n\nThe paper presents the first study to analyze how LLMs recognize knowledge boundaries across different languages by probing their internal representations when processing known and unknown questions in multiple languages."
    ],
    "durationSeconds": 5.840364333999998
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-21T07:38:52.003Z_

<details><summary>↩ Tool result · `toolu_01B7BJF1kry42k3MsXgiaizn`</summary>

```text
Web search results for query: "arxiv 2602.08159 "Confidence Manifold" authors list"

Links: [{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.biorxiv.org/content/10.1101/426635.full.pdf"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11299811/"},{"title":"EEG-MACS: Manifold Attention and Confidence Stratification for EEG-based Cross-Center Brain Disease Diagnosis under Unreliable Annotations","url":"https://arxiv.org/html/2405.00734v2"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"}]

I found information about the arxiv paper 2602.08159 titled "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models", but the search results don't include the complete authors list. The PDF and HTML versions are available on arxiv.org, but the search snippets don't display the author names.

Let me search more specifically for the authors:

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals","url":"https://arxiv.org/pdf/2602.00977"},{"title":"Attributing authorship via the perplexity of authorial language models","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12225838/"},{"title":"Confidence Under the Hood: An Investigation into the   Confidence-Probability Alignment in Large Language Models","url":"https://arxiv.org/pdf/2405.16282"},{"title":"On the attribution of confidence to large language models","url":"https://arxiv.org/pdf/2407.08388"},{"title":"From Evidence to Belief: A Bayesian Epistemology Approach to Language   Models","url":"https://arxiv.org/pdf/2504.19622"},{"title":"Manifold of Failure: Behavioral Attraction Basins in Language ModelsThis work was conducted independently and does not reflect the views, policies, or endorsements of the authors’ respective employers. Corresponding author: manish.bhatt13212@gmail.com","url":"https://arxiv.org/html/2602.22291"}]

The search results still don't show the author list in the snippets. Let me try a different approach:

Links: [{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6822779/"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.biorxiv.org/content/10.1101/426635.full.pdf"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"},{"title":"Correction: Biased but in Doubt: Conflict and Decision Confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3048855/"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11299811/"}]

I apologize, but despite multiple search attempts, the search results are not displaying the author list from the arxiv paper 2602.08159 "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models." 

While I was able to confirm that the paper exists and was published on February 8, 2026, and can provide details about its research (examining how language models represent correctness signals across 9 models from 5 architecture families), the author names are not appearing in the search result snippets.

To access the complete author list, I recommend visiting the paper directly at:
- https://arxiv.org/html/2602.08159v1 or
- https://www.arxiv.org/pdf/2602.08159

These pages should display the authors at the beginning of the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "55e7d227-f6af-4055-a85a-07f4714197d4",
  "tool_use_result": {
    "query": "arxiv 2602.08159 \"Confidence Manifold\" authors list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QFV55ndfrFGSibmCC9N6qu",
        "content": [
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "The folded X-pattern is not necessarily a statistical signature of decision confidence",
            "url": "https://www.biorxiv.org/content/10.1101/426635.full.pdf"
          },
          {
            "title": "A low-dimensional approximation of optimal confidence",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11299811/"
          },
          {
            "title": "EEG-MACS: Manifold Attention and Confidence Stratification for EEG-based Cross-Center Brain Disease Diagnosis under Unreliable Annotations",
            "url": "https://arxiv.org/html/2405.00734v2"
          },
          {
            "title": "A low-dimensional approximation of optimal confidence",
            "url": "https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"
          }
        ]
      },
      "I found information about the arxiv paper 2602.08159 titled \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models\", but the search results don't include the complete authors list. The PDF and HTML versions are available on arxiv.org, but the search snippets don't display the author names.\n\nLet me search more specifically for the authors:",
      {
        "tool_use_id": "srvtoolu_019Eb78n6ydoVLQEfbcKnz2k",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "Trust in One Round: Confidence Estimation for Large Language Models via Structural Signals",
            "url": "https://arxiv.org/pdf/2602.00977"
          },
          {
            "title": "Attributing authorship via the perplexity of authorial language models",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12225838/"
          },
          {
            "title": "Confidence Under the Hood: An Investigation into the   Confidence-Probability Alignment in Large Language Models",
            "url": "https://arxiv.org/pdf/2405.16282"
          },
          {
            "title": "On the attribution of confidence to large language models",
            "url": "https://arxiv.org/pdf/2407.08388"
          },
          {
            "title": "From Evidence to Belief: A Bayesian Epistemology Approach to Language   Models",
            "url": "https://arxiv.org/pdf/2504.19622"
          },
          {
            "title": "Manifold of Failure: Behavioral Attraction Basins in Language ModelsThis work was conducted independently and does not reflect the views, policies, or endorsements of the authors’ respective employers. Corresponding author: manish.bhatt13212@gmail.com",
            "url": "https://arxiv.org/html/2602.22291"
          }
        ]
      },
      "The search results still don't show the author list in the snippets. Let me try a different approach:",
      {
        "tool_use_id": "srvtoolu_01NK9dhGWx6y8wKPZS9YcgHD",
        "content": [
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The folded X-pattern is not necessarily a statistical signature of decision confidence",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6822779/"
          },
          {
            "title": "The folded X-pattern is not necessarily a statistical signature of decision confidence",
            "url": "https://www.biorxiv.org/content/10.1101/426635.full.pdf"
          },
          {
            "title": "A low-dimensional approximation of optimal confidence",
            "url": "https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"
          },
          {
            "title": "Correction: Biased but in Doubt: Conflict and Decision Confidence",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3048855/"
          },
          {
            "title": "A low-dimensional approximation of optimal confidence",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11299811/"
          }
        ]
      },
      "I apologize, but despite multiple search attempts, the search results are not displaying the author list from the arxiv paper 2602.08159 \"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models.\" \n\nWhile I was able to confirm that the paper exists and was published on February 8, 2026, and can provide details about its research (examining how language models represent correctness signals across 9 models from 5 architecture families), the author names are not appearing in the search result snippets.\n\nTo access the complete author list, I recommend visiting the paper directly at:\n- https://arxiv.org/html/2602.08159v1 or\n- https://www.arxiv.org/pdf/2602.08159\n\nThese pages should display the authors at the beginning of the paper."
    ],
    "durationSeconds": 12.545657099999996
  }
}
```

</details>

---

### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
Let me get a few more details on the remaining papers. I need the Civelli authors, Ravisankar authors/venue, Miao CORAL details, Ji 2025 details, Joshi 2025 details, and Liu & Niehues details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "9c2e2df6-13f1-45b6-9a6e-14a28aaff3bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 86_

Let me get details on the remaining papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "1c0d12eb-fe9c-41aa-bdd6-e55a6604a921",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MPyKHMUmXKhLaKS1vMFTUM`</summary>

```json
{
  "query": "arxiv 2601.12731 Civelli \"Shared Geometry of Difficulty\" authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "9b690f60-61c9-418e-a0de-ca95c423a065",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012VwNCnjwAjezSvRw7KxSpq`</summary>

```json
{
  "query": "Ravisankar DALI \"Can you map it to English\" EACL 2026 authors full list doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "66567743-c9be-4091-bf51-2a627569e63e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ZrKUGhBY86FeEyMYas3ea`</summary>

```json
{
  "query": "Ji \"Calibrating Verbal Uncertainty as a Linear Feature\" EMNLP 2025 authors doi arxiv 2503.14477"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "4fc1645b-a9ce-4608-94c0-955056288159",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 90_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ic4vcd8ZLDWmwEVU29WjW`</summary>

```json
{
  "query": "Joshi Ahmad Modi \"Calibration Across Layers\" EMNLP 2025 doi arxiv 2511.00280"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "9684ea87-b25d-4ae3-a165-4a7fca40eeeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SCz1Rkjfnsm4ifMEXSFi78`</summary>

```json
{
  "query": "Liu Niehues \"Middle-Layer Representation Alignment\" ACL 2025 doi authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e320acaa-c8bf-4a53-bc43-6b01ae5d1a80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-21T07:39:01.329Z_

<details><summary>↩ Tool result · `toolu_01MPyKHMUmXKhLaKS1vMFTUM`</summary>

```text
Web search results for query: "arxiv 2601.12731 Civelli "Shared Geometry of Difficulty" authors full list"

Links: [{"title":"[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/abs/2601.12731"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/pastweek?skip=1688&show=50"},{"title":"A Shared Geometry of Difficulty in Multilingual Language Models","url":"https://arxiv.org/html/2601.12731"},{"title":"GeoLaux: A Benchmark for Evaluating MLLMs' Geometry Performance on Long-Step Problems Requiring Auxiliary Lines","url":"https://arxiv.org/pdf/2508.06226"},{"title":"Geometrical congruence, greedy navigability and myopic transfer in complex networks and brain connectomes","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9701786/"},{"title":"Guidewire Morphology as a Predictor of Vascular Tortuosity and Advancement Difficulties During Right Upper Limb Coronary Angiography","url":"https://www.medrxiv.org/content/10.64898/2025.12.21.25342793.full.pdf"}]

The full list of authors for arxiv 2601.12731 "A Shared Geometry of Difficulty in Multilingual Language Models" is:

1. Stefano Civelli (The University of Queensland)
2. Pietro Bernardelle (The University of Queensland)
3. Nicolò Brunello (Polytechnic University of Milan)
4. Gianluca Demartini (The University of Queensland)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "a5ab7c04-f971-467d-b027-67919e79bf79",
  "tool_use_result": {
    "query": "arxiv 2601.12731 Civelli \"Shared Geometry of Difficulty\" authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uk4qPHq3Ztts7KMLsydV44",
        "content": [
          {
            "title": "[2601.12731] A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/abs/2601.12731"
          },
          {
            "title": "Computer Science",
            "url": "https://www.arxiv.org/list/cs/pastweek?skip=1688&show=50"
          },
          {
            "title": "A Shared Geometry of Difficulty in Multilingual Language Models",
            "url": "https://arxiv.org/html/2601.12731"
          },
          {
            "title": "GeoLaux: A Benchmark for Evaluating MLLMs' Geometry Performance on Long-Step Problems Requiring Auxiliary Lines",
            "url": "https://arxiv.org/pdf/2508.06226"
          },
          {
            "title": "Geometrical congruence, greedy navigability and myopic transfer in complex networks and brain connectomes",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9701786/"
          },
          {
            "title": "Guidewire Morphology as a Predictor of Vascular Tortuosity and Advancement Difficulties During Right Upper Limb Coronary Angiography",
            "url": "https://www.medrxiv.org/content/10.64898/2025.12.21.25342793.full.pdf"
          }
        ]
      },
      "The full list of authors for arxiv 2601.12731 \"A Shared Geometry of Difficulty in Multilingual Language Models\" is:\n\n1. Stefano Civelli (The University of Queensland)\n2. Pietro Bernardelle (The University of Queensland)\n3. Nicolò Brunello (Polytechnic University of Milan)\n4. Gianluca Demartini (The University of Queensland)"
    ],
    "durationSeconds": 4.08546807599999
  }
}
```

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Faf9amsmmcmXoaDCz9wuz8`</summary>

```json
{
  "query": "Miao CORAL arxiv 2602.06022 authors \"Correctness-Optimized Residual Activation Lens\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8f05cfa5-8e7d-4fdd-8fe7-e8924d082a3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JwwzubiUBtjinuc5HBL1wC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3328,
      "cache_creation_input_tokens": 2666,
      "cache_read_input_tokens": 52519,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2666
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-21T07:39:04.059Z_

<details><summary>↩ Tool result · `toolu_012VwNCnjwAjezSvRw7KxSpq`</summary>

```text
Web search results for query: "Ravisankar DALI "Can you map it to English" EACL 2026 authors full list doi"

Links: [{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.225/"},{"title":"Kartik Ravisankar's research works","url":"https://www.researchgate.net/scientific-contributions/Kartik-Ravisankar-2310395112"},{"title":"[2504.09378] Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/abs/2504.09378"},{"title":"(PDF) Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://www.researchgate.net/publication/390773780_Can_you_map_it_to_English_The_Role_of_Cross-Lingual_Alignment_in_Multilingual_Performance_of_LLMs"},{"title":"Social media text analytics of Malayalam–English code-mixed using deep learning","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041283/"},{"title":"Similar does not mean same: ERP correlates of processing mental and physical experiencer verbs in Malayalam complex constructions","url":"https://www.biorxiv.org/content/10.1101/2025.05.21.655344.full.pdf"},{"title":"System and method for writing Indian languages using English alphabet","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7177794"}]

Based on the search results, I found the paper you're looking for. Here are the details:

**Paper:** "Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs"

**Authors:** Kartik Ravisankar, HyoJung Han, Sarah Wiegreffe, and Marine Carpuat

**Conference:** Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 4854–4872, Rabat, Morocco

**Year:** 2026

**DOI:** The ACL Anthology link is: https://aclanthology.org/2026.eacl-long.225/

**arXiv identifier:** 2504.09378 (available on arXiv)

The paper introduces the Discriminative Alignment Index (DALI) to quantify instance-level alignment across 24 languages other than English and three distinct NLU tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "cf243ec7-858d-46fb-ba3c-ced48d538a4b",
  "tool_use_result": {
    "query": "Ravisankar DALI \"Can you map it to English\" EACL 2026 authors full list doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MZ1WhoCmoj3kWMDE3EEqYq",
        "content": [
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2026.eacl-long.225/"
          },
          {
            "title": "Kartik Ravisankar's research works",
            "url": "https://www.researchgate.net/scientific-contributions/Kartik-Ravisankar-2310395112"
          },
          {
            "title": "[2504.09378] Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/abs/2504.09378"
          },
          {
            "title": "(PDF) Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://www.researchgate.net/publication/390773780_Can_you_map_it_to_English_The_Role_of_Cross-Lingual_Alignment_in_Multilingual_Performance_of_LLMs"
          },
          {
            "title": "Social media text analytics of Malayalam–English code-mixed using deep learning",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041283/"
          },
          {
            "title": "Similar does not mean same: ERP correlates of processing mental and physical experiencer verbs in Malayalam complex constructions",
            "url": "https://www.biorxiv.org/content/10.1101/2025.05.21.655344.full.pdf"
          },
          {
            "title": "System and method for writing Indian languages using English alphabet",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7177794"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here are the details:\n\n**Paper:** \"Can you map it to English? The Role of Cross-Lingual Alignment in the Multilingual Performance of LLMs\"\n\n**Authors:** Kartik Ravisankar, HyoJung Han, Sarah Wiegreffe, and Marine Carpuat\n\n**Conference:** Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers), pages 4854–4872, Rabat, Morocco\n\n**Year:** 2026\n\n**DOI:** The ACL Anthology link is: https://aclanthology.org/2026.eacl-long.225/\n\n**arXiv identifier:** 2504.09378 (available on arXiv)\n\nThe paper introduces the Discriminative Alignment Index (DALI) to quantify instance-level alignment across 24 languages other than English and three distinct NLU tasks."
    ],
    "durationSeconds": 5.809918732999998
  }
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-21T07:39:05.874Z_

<details><summary>↩ Tool result · `toolu_015ZrKUGhBY86FeEyMYas3ea`</summary>

```text
Web search results for query: "Ji "Calibrating Verbal Uncertainty as a Linear Feature" EMNLP 2025 authors doi arxiv 2503.14477"

Links: [{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/pdf/2503.14477"},{"title":"Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.187/"},{"title":"[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://arxiv.org/abs/2503.14477"},{"title":"(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations","url":"https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"},{"title":"arXiv:2505.23854v1 [cs.CL] 29 May 2025","url":"https://arxiv.org/pdf/2505.23854"},{"title":"dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.","url":"https://dblp.org/rec/journals/corr/abs-2503-14477.html"},{"title":"Teaching Language Models to Faithfully Express their Uncertainty","url":"https://arxiv.org/pdf/2510.12587"}]

Based on the search results, here's the information about the paper:

**Paper Title:** Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations

**Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda

**Venue:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 3769–3793, Suzhou, China

**DOI:** 10.18653/v1/2025.emnlp-main.187

**arXiv ID:** 2503.14477

**Main Contribution:** The paper discovers a linear verbal uncertainty feature (VUF) that controls model expression of uncertainty, and applies this insight to: (1) detect hallucinations arising from the miscalibration between high semantic uncertainty (SU) and low verbal uncertainty (VU); (2) mitigate hallucinations by intervening on activations along the VUF direction at inference time to make VU more aligned with model's SU.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "c1238791-bb24-4cef-997e-bda26d195c42",
  "tool_use_result": {
    "query": "Ji \"Calibrating Verbal Uncertainty as a Linear Feature\" EMNLP 2025 authors doi arxiv 2503.14477",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FWK6cDUVh7SZ4GX1xWgcdB",
        "content": [
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/pdf/2503.14477"
          },
          {
            "title": "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.187/"
          },
          {
            "title": "[2503.14477] Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://arxiv.org/abs/2503.14477"
          },
          {
            "title": "(PDF) Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations",
            "url": "https://www.researchgate.net/publication/389947447_Calibrating_Verbal_Uncertainty_as_a_Linear_Feature_to_Reduce_Hallucinations"
          },
          {
            "title": "arXiv:2505.23854v1 [cs.CL] 29 May 2025",
            "url": "https://arxiv.org/pdf/2505.23854"
          },
          {
            "title": "dblp: Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations.",
            "url": "https://dblp.org/rec/journals/corr/abs-2503-14477.html"
          },
          {
            "title": "Teaching Language Models to Faithfully Express their Uncertainty",
            "url": "https://arxiv.org/pdf/2510.12587"
          }
        ]
      },
      "Based on the search results, here's the information about the paper:\n\n**Paper Title:** Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations\n\n**Authors:** Ziwei Ji, Lei Yu, Yeskendir Koishekenov, Yejin Bang, Anthony Hartshorn, Alan Schelten, Cheng Zhang, Pascale Fung, and Nicola Cancedda\n\n**Venue:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 3769–3793, Suzhou, China\n\n**DOI:** 10.18653/v1/2025.emnlp-main.187\n\n**arXiv ID:** 2503.14477\n\n**Main Contribution:** The paper discovers a linear verbal uncertainty feature (VUF) that controls model expression of uncertainty, and applies this insight to: (1) detect hallucinations arising from the miscalibration between high semantic uncertainty (SU) and low verbal uncertainty (VU); (2) mitigate hallucinations by intervening on activations along the VUF direction at inference time to make VU more aligned with model's SU."
    ],
    "durationSeconds": 6.692192648999989
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-21T07:39:06.433Z_

<details><summary>↩ Tool result · `toolu_01SCz1Rkjfnsm4ifMEXSFi78`</summary>

```text
Web search results for query: "Liu Niehues "Middle-Layer Representation Alignment" ACL 2025 doi authors full list"

Links: [{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.778/"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF","url":"https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"},{"title":"[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/abs/2502.14830"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v2"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in","url":"https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"},{"title":"[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/pdf/2502.14830"}]

Based on the search results, here is the information about the paper:

## Paper Details

**Title:** Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs

**Authors:** Danni Liu and Jan Niehues

**Conference:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15979–15996, Vienna, Austria

**Year:** 2025

**DOI/ISBN:** 979-8-89176-251-0

**arXiv Version:** The paper is also available on arXiv as 2502.14830

**Affiliation:** Karlsruhe Institute of Technology, Germany

Note: The search results show this as a 2-author paper with Danni Liu and Jan Niehues as the primary authors. The ACL Anthology entry lists editors (Che, Nabende, Shutova, and Pilehvar) but not additional authors beyond Liu and Niehues.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "52eafbab-28d1-43ec-add7-f058eb904c4d",
  "tool_use_result": {
    "query": "Liu Niehues \"Middle-Layer Representation Alignment\" ACL 2025 doi authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WJdXi52uYKg7nh2dhzWxWY",
        "content": [
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.778/"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/394303200_Middle-Layer_Representation_Alignment_for_Cross-Lingual_Transfer_in_Fine-Tuned_LLMs"
          },
          {
            "title": "[2502.14830] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/abs/2502.14830"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/html/2502.14830v2"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in",
            "url": "https://openreview.net/pdf/165a4c42ede4fa7182ef5ba60ec0669f5606b9b8.pdf"
          },
          {
            "title": "[Literature Review] Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://www.themoonlight.io/en/review/middle-layer-representation-alignment-for-cross-lingual-transfer-in-fine-tuned-llms"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/pdf/2502.14830"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n## Paper Details\n\n**Title:** Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs\n\n**Authors:** Danni Liu and Jan Niehues\n\n**Conference:** Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15979–15996, Vienna, Austria\n\n**Year:** 2025\n\n**DOI/ISBN:** 979-8-89176-251-0\n\n**arXiv Version:** The paper is also available on arXiv as 2502.14830\n\n**Affiliation:** Karlsruhe Institute of Technology, Germany\n\nNote: The search results show this as a 2-author paper with Danni Liu and Jan Niehues as the primary authors. The ACL Anthology entry lists editors (Che, Nabende, Shutova, and Pilehvar) but not additional authors beyond Liu and Niehues."
    ],
    "durationSeconds": 5.28427285600001
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-21T07:39:06.493Z_

<details><summary>↩ Tool result · `toolu_014ic4vcd8ZLDWmwEVU29WjW`</summary>

```text
Web search results for query: "Joshi Ahmad Modi "Calibration Across Layers" EMNLP 2025 doi arxiv 2511.00280"

Links: [{"title":"GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub","url":"https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF","url":"https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/abs/2511.00280"},{"title":"(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"},{"title":"Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models","url":"https://arxiv.org/pdf/2510.03136"},{"title":"Calibration Across Layers: Understanding Calibration Evolution in LLMs","url":"https://arxiv.org/pdf/2511.00280"}]

I found the paper you're looking for. Here are the details:

**Title:** "Calibration Across Layers: Understanding Calibration Evolution in LLMs"

**Authors:** Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi

**Conference:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)

**ArXiv ID:** 2511.00280

**DOI:** 10.18653/v1/2025.emnlp-main.742

**Key Contributions:** The paper analyzes multiple open-weight models on the MMLU benchmark and uncovers a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached. Additionally, the researchers identify a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.

The paper is available on [arXiv](https://arxiv.org/abs/2511.00280) and through the [ACL Anthology](https://aclanthology.org/2025.emnlp-main.742/).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "836e4334-0020-4a9d-a715-5c292d61011f",
  "tool_use_result": {
    "query": "Joshi Ahmad Modi \"Calibration Across Layers\" EMNLP 2025 doi arxiv 2511.00280",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P6M3jMEeJVmbXiGH33eupk",
        "content": [
          {
            "title": "GitHub - Exploration-Lab/LLM-Calibration-Mechanism · GitHub",
            "url": "https://github.com/Exploration-Lab/LLM-Calibration-Mechanism"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs | Request PDF",
            "url": "https://www.researchgate.net/publication/397421796_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"
          },
          {
            "title": "[2511.00280] Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/abs/2511.00280"
          },
          {
            "title": "(PDF) Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://www.researchgate.net/publication/397231243_Calibration_Across_Layers_Understanding_Calibration_Evolution_in_LLMs"
          },
          {
            "title": "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models",
            "url": "https://arxiv.org/pdf/2510.03136"
          },
          {
            "title": "Calibration Across Layers: Understanding Calibration Evolution in LLMs",
            "url": "https://arxiv.org/pdf/2511.00280"
          }
        ]
      },
      "I found the paper you're looking for. Here are the details:\n\n**Title:** \"Calibration Across Layers: Understanding Calibration Evolution in LLMs\"\n\n**Authors:** Abhinav Joshi, Areeb Ahmad, and Ashutosh Modi\n\n**Conference:** Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)\n\n**ArXiv ID:** 2511.00280\n\n**DOI:** 10.18653/v1/2025.emnlp-main.742\n\n**Key Contributions:** The paper analyzes multiple open-weight models on the MMLU benchmark and uncovers a distinct confidence correction phase in the upper/later layers, where model confidence is actively recalibrated after decision certainty has been reached. Additionally, the researchers identify a low-dimensional calibration direction in the residual stream whose perturbation significantly improves calibration metrics (ECE and MCE) without harming accuracy.\n\nThe paper is available on [arXiv](https://arxiv.org/abs/2511.00280) and through the [ACL Anthology](https://aclanthology.org/2025.emnlp-main.742/)."
    ],
    "durationSeconds": 6.356611875000002
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-21T07:39:07.720Z_

<details><summary>↩ Tool result · `toolu_01Faf9amsmmcmXoaDCz9wuz8`</summary>

```text
Web search results for query: "Miao CORAL arxiv 2602.06022 authors "Correctness-Optimized Residual Activation Lens""

Links: [{"title":"[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/abs/2602.06022"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"},{"title":"Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering","url":"http://paperreading.club/page?id=374945"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL):","url":"https://arxiv.org/pdf/2602.06022"},{"title":"[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering","url":"https://arxiv.org/html/2602.06022v1"},{"title":"Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2602.06022"},{"title":"The Reversible Residual Network: Backpropagation Without Storing   Activations","url":"https://arxiv.org/pdf/1707.04585"}]

Based on the search results, here's what I found about the paper:

## CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022)

**Authors:** Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar

**Overview:**
CORAL is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.

**Problem Being Addressed:**
Large language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive.

**Key Results:**
CORAL was evaluated across three 7B-parameter models and consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.

**Methodology:**
The method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.

The paper was published on February 5, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "fbe8a876-703b-4dfa-b8ea-3596751309d5",
  "tool_use_result": {
    "query": "Miao CORAL arxiv 2602.06022 authors \"Correctness-Optimized Residual Activation Lens\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AFf6xbBnLJvVJJbka4qVRc",
        "content": [
          {
            "title": "[2602.06022] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/abs/2602.06022"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.researchgate.net/publication/400505951_Correctness-Optimized_Residual_Activation_Lens_CORAL_Transferrable_and_Calibration-Aware_Inference-Time_Steering"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens : Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "http://paperreading.club/page?id=374945"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL):",
            "url": "https://arxiv.org/pdf/2602.06022"
          },
          {
            "title": "[Literature Review] Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://www.themoonlight.io/en/review/correctness-optimized-residual-activation-lens-coral-transferrable-and-calibration-aware-inference-time-steering"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering",
            "url": "https://arxiv.org/html/2602.06022v1"
          },
          {
            "title": "Correctness-Optimized Residual Activation Lens (CORAL): Transferrable and Calibration-Aware Inference-Time Steering | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2602.06022"
          },
          {
            "title": "The Reversible Residual Network: Backpropagation Without Storing   Activations",
            "url": "https://arxiv.org/pdf/1707.04585"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n## CORAL: Correctness-Optimized Residual Activation Lens (arXiv 2602.06022)\n\n**Authors:** Miranda Muqing Miao, Young-Min Cho, and Lyle Ungar\n\n**Overview:**\nCORAL is a regularized inference-time steering method that captures distributed correctness signals from model internal activations using weight-decay MLP probes.\n\n**Problem Being Addressed:**\nLarge language models (LLMs) exhibit persistent miscalibration, especially after instruction tuning and preference alignment. Modified training objectives can improve calibration, but retraining is expensive.\n\n**Key Results:**\nCORAL was evaluated across three 7B-parameter models and consistently improves accuracy by 10% and expected calibration error (ECE) by 50% on average. These gains transfer without retraining to the complete published test sets of four held-out benchmarks (ARC-Challenge, HellaSwag, Math-MC, OpenBookQA), averaging 14% accuracy improvements and 49% ECE improvements.\n\n**Methodology:**\nThe method trains a regularized probe that predicts correctness directly from frozen residual stream activations, then uses these predictions to steer model behavior at inference time. By jointly optimizing for the accuracy and calibration components of the Brier score, CORAL improves both metrics and transfers its impact successfully to unseen benchmarks without any retraining.\n\nThe paper was published on February 5, 2026."
    ],
    "durationSeconds": 5.867623195000007
  }
}
```

</details>

---

### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text
Now I need to get the Miao & Ungar "Closing the Confidence-Faithfulness Gap" authors and details, and the Khanmohammadi CCPS full author list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "6375c7a2-e8fb-4901-90e9-f823f9992a1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsMYvfpZtzNw66VeADNCWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8051,
      "cache_read_input_tokens": 55185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8051
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 100_

Let me get the last few author details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "7e01ad6b-8531-4cc0-b320-b0b25a9628b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsMYvfpZtzNw66VeADNCWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8051,
      "cache_read_input_tokens": 55185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8051
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014dc9W22gEBWgMmmxJgpBoC`</summary>

```json
{
  "query": "Miao \"Closing the Confidence-Faithfulness Gap\" arxiv 2603.25052 authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "c9151498-1945-4a22-9ca6-453128f8ca2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsMYvfpZtzNw66VeADNCWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8051,
      "cache_read_input_tokens": 55185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8051
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U3uqZJaCUzgARjE2GMQEj1`</summary>

```json
{
  "query": "Khanmohammadi \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" EMNLP 2025 authors doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "cf7890a0-adc8-4c3c-b679-865aaef0e265",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsMYvfpZtzNw66VeADNCWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8051,
      "cache_read_input_tokens": 55185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8051
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 103_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017KkCQrWpG8KJ4fdQUXZExU`</summary>

```json
{
  "query": "Conneau XLM-RoBERTa ACL 2020 full authors list Khandelwal Goyal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "0c3deb91-67be-4b90-871c-76167774baf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsMYvfpZtzNw66VeADNCWf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8051,
      "cache_read_input_tokens": 55185,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8051
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-21T07:39:16.662Z_

<details><summary>↩ Tool result · `toolu_014dc9W22gEBWgMmmxJgpBoC`</summary>

```text
Web search results for query: "Miao "Closing the Confidence-Faithfulness Gap" arxiv 2603.25052 authors full list"

Links: [{"title":"Fugu-MT 論文翻訳(概要): Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://fugumt.com/fugumt/paper_check/2603.25052v1"},{"title":"[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052v1"},{"title":"[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/abs/2603.25052"},{"title":"Closing the Confidence-Faithfulness Gap in Large Language Models","url":"https://arxiv.org/html/2603.25052"},{"title":"Closing the Confidence-Faithfulness Gap in Large ...","url":"https://arxiv.org/pdf/2603.25052"},{"title":"Teaching Language Models to Faithfully Express their Uncertainty","url":"https://arxiv.org/pdf/2510.12587"},{"title":"Closing the Confidence-Faithfulness Gap in Large ...","url":"https://x.com/HEI/status/2037535763399651595"}]

Based on the search results, the authors of "Closing the Confidence-Faithfulness Gap in Large Language Models" (arXiv:2603.25052) are Miranda Muqing Miao and Lyle Ungar from University of Pennsylvania.

The paper appears to have only these two authors listed in the full author list.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "5f125966-5539-4a2d-9d65-6f493e95abd6",
  "tool_use_result": {
    "query": "Miao \"Closing the Confidence-Faithfulness Gap\" arxiv 2603.25052 authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K8y7Mxefs1JmaYxva2WEHi",
        "content": [
          {
            "title": "Fugu-MT 論文翻訳(概要): Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://fugumt.com/fugumt/paper_check/2603.25052v1"
          },
          {
            "title": "[2603.25052v1] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052v1"
          },
          {
            "title": "[2603.25052] Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/abs/2603.25052"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large Language Models",
            "url": "https://arxiv.org/html/2603.25052"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large ...",
            "url": "https://arxiv.org/pdf/2603.25052"
          },
          {
            "title": "Teaching Language Models to Faithfully Express their Uncertainty",
            "url": "https://arxiv.org/pdf/2510.12587"
          },
          {
            "title": "Closing the Confidence-Faithfulness Gap in Large ...",
            "url": "https://x.com/HEI/status/2037535763399651595"
          }
        ]
      },
      "Based on the search results, the authors of \"Closing the Confidence-Faithfulness Gap in Large Language Models\" (arXiv:2603.25052) are Miranda Muqing Miao and Lyle Ungar from University of Pennsylvania.\n\nThe paper appears to have only these two authors listed in the full author list."
    ],
    "durationSeconds": 3.724503171999997
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-21T07:39:18.192Z_

<details><summary>↩ Tool result · `toolu_01U3uqZJaCUzgARjE2GMQEj1`</summary>

```text
Web search results for query: "Khanmohammadi "Calibrating LLM Confidence by Probing Perturbed Representation Stability" EMNLP 2025 authors doi"

Links: [{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF","url":"https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.530/"},{"title":"[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/abs/2505.21772"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/html/2505.21772v1"},{"title":"Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://arxiv.org/pdf/2505.21772"},{"title":"GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://github.com/ledengary/CCPS"},{"title":"Confidence-Guided Probing Methods","url":"https://www.emergentmind.com/topics/confidence-guided-probing-method"},{"title":"(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability","url":"https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"},{"title":"dblp: Kundan Thind","url":"https://dblp.org/pid/359/8694.html"}]

Based on the search results, here is the information for the paper:

**Title:** Calibrating LLM Confidence by Probing Perturbed Representation Stability

**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese Smiley, Kundan S Thind, and Mohammad M. Ghassemi

**Conference:** 2025 Conference on Empirical Methods in Natural Language Processing, pages 10448–10514, Suzhou, China

**DOI:** 10.18653/v1/2025.emnlp-main.530

**arXiv:** 2505.21772


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "82cf2089-ab0a-42e9-b4c7-e95159de592e",
  "tool_use_result": {
    "query": "Khanmohammadi \"Calibrating LLM Confidence by Probing Perturbed Representation Stability\" EMNLP 2025 authors doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y8bzjMuq2PrbErYvfCKbSy",
        "content": [
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability | Request PDF",
            "url": "https://www.researchgate.net/publication/397423860_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.530/"
          },
          {
            "title": "[2505.21772] Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/abs/2505.21772"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/calibrating-llm-confidence-by-probing-perturbed-representation"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/html/2505.21772v1"
          },
          {
            "title": "Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://arxiv.org/pdf/2505.21772"
          },
          {
            "title": "GitHub - Ledengary/CCPS: Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://github.com/ledengary/CCPS"
          },
          {
            "title": "Confidence-Guided Probing Methods",
            "url": "https://www.emergentmind.com/topics/confidence-guided-probing-method"
          },
          {
            "title": "(PDF) Calibrating LLM Confidence by Probing Perturbed Representation Stability",
            "url": "https://www.researchgate.net/publication/392168633_Calibrating_LLM_Confidence_by_Probing_Perturbed_Representation_Stability"
          },
          {
            "title": "dblp: Kundan Thind",
            "url": "https://dblp.org/pid/359/8694.html"
          }
        ]
      },
      "Based on the search results, here is the information for the paper:\n\n**Title:** Calibrating LLM Confidence by Probing Perturbed Representation Stability\n\n**Authors:** Reza Khanmohammadi, Erfan Miahi, Mehrsa Mardikoraem, Simerjot Kaur, Ivan Brugere, Charese Smiley, Kundan S Thind, and Mohammad M. Ghassemi\n\n**Conference:** 2025 Conference on Empirical Methods in Natural Language Processing, pages 10448–10514, Suzhou, China\n\n**DOI:** 10.18653/v1/2025.emnlp-main.530\n\n**arXiv:** 2505.21772"
    ],
    "durationSeconds": 4.2433598439999916
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-21T07:39:19.485Z_

<details><summary>↩ Tool result · `toolu_017KkCQrWpG8KJ4fdQUXZExU`</summary>

```text
Web search results for query: "Conneau XLM-RoBERTa ACL 2020 full authors list Khandelwal Goyal"

Links: [{"title":"XLM-RoBERTa - Hugo Cisneros","url":"https://hugocisneros.com/notes/xlm_roberta/"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.747/"},{"title":"Cross-Language Language Model (XLM) - GM-RKB","url":"https://www.gabormelli.com/RKB/Cross-Language_Language_Model_(XLM)"},{"title":"(PDF) Unsupervised Cross-lingual Representation Learning at Scale (2020) | Alexis Conneau | 6886 Citations","url":"https://scispace.com/papers/unsupervised-cross-lingual-representation-learning-at-scale-2o09354dx5"},{"title":"[PDF] Unsupervised Cross-lingual Representation Learning at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Cross-lingual-Representation-Learning-Conneau-Khandelwal/6fec3e579c7cd4f13bdabbee2b6ac2e8ff5941c6"},{"title":"Unsupervised Cross-lingual Representation Learning at Scale","url":"https://www.researchgate.net/publication/343298778_Unsupervised_Cross-lingual_Representation_Learning_at_Scale"},{"title":"Conneau, A., et al. (2020) Unsupervised Cross-Lingual Representation Learning at Scale. Proceedings of ACL 2020, 5-10 July 2020, 8440-8451. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=4031261"},{"title":"Cross-lingual Inductive Transfer to Detect Offensive Language","url":"https://arxiv.org/pdf/2007.03771"}]

Based on the search results, here is the full authors list for the XLM-RoBERTa paper published at ACL 2020:

Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov.

The paper is titled "Unsupervised Cross-lingual Representation Learning at Scale" and was published in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "43bfbddb-853e-4c6f-b7cf-d4ffb4d6b37a",
  "tool_use_result": {
    "query": "Conneau XLM-RoBERTa ACL 2020 full authors list Khandelwal Goyal",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MbW9sKcoge7KcN8awhwzSx",
        "content": [
          {
            "title": "XLM-RoBERTa - Hugo Cisneros",
            "url": "https://hugocisneros.com/notes/xlm_roberta/"
          },
          {
            "title": "Unsupervised Cross-lingual Representation Learning at Scale - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.747/"
          },
          {
            "title": "Cross-Language Language Model (XLM) - GM-RKB",
            "url": "https://www.gabormelli.com/RKB/Cross-Language_Language_Model_(XLM)"
          },
          {
            "title": "(PDF) Unsupervised Cross-lingual Representation Learning at Scale (2020) | Alexis Conneau | 6886 Citations",
            "url": "https://scispace.com/papers/unsupervised-cross-lingual-representation-learning-at-scale-2o09354dx5"
          },
          {
            "title": "[PDF] Unsupervised Cross-lingual Representation Learning at Scale | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Unsupervised-Cross-lingual-Representation-Learning-Conneau-Khandelwal/6fec3e579c7cd4f13bdabbee2b6ac2e8ff5941c6"
          },
          {
            "title": "Unsupervised Cross-lingual Representation Learning at Scale",
            "url": "https://www.researchgate.net/publication/343298778_Unsupervised_Cross-lingual_Representation_Learning_at_Scale"
          },
          {
            "title": "Conneau, A., et al. (2020) Unsupervised Cross-Lingual Representation Learning at Scale. Proceedings of ACL 2020, 5-10 July 2020, 8440-8451. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=4031261"
          },
          {
            "title": "Cross-lingual Inductive Transfer to Detect Offensive Language",
            "url": "https://arxiv.org/pdf/2007.03771"
          }
        ]
      },
      "Based on the search results, here is the full authors list for the XLM-RoBERTa paper published at ACL 2020:\n\nAlexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov.\n\nThe paper is titled \"Unsupervised Cross-lingual Representation Learning at Scale\" and was published in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics."
    ],
    "durationSeconds": 4.719033212000009
  }
}
```

</details>

---

### Assistant

_source line 107_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also try to get the Confidence Manifold authors by fetching it with WebFetch. Actually, the search wasn't very helpful for the author list. Let me try one more specific search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "fabcb2bb-4399-447c-b906-13178bab9f1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cpDFfK89NEKsw4t943hEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2369,
      "cache_read_input_tokens": 63236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2369
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 108_

Let me get the Confidence Manifold authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "61ae3a4d-9022-4fa4-a584-4ac4e039d9ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cpDFfK89NEKsw4t943hEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2369,
      "cache_read_input_tokens": 63236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2369
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01W2oqv4Lsux62vqEYn7BxVu`</summary>

```json
{
  "query": "site:arxiv.org 2602.08159 \"Confidence Manifold\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "8acea5ae-a493-4074-956a-fd42ea304f56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cpDFfK89NEKsw4t943hEA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2369,
      "cache_read_input_tokens": 63236,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2369
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-21T07:39:29.044Z_

<details><summary>↩ Tool result · `toolu_01W2oqv4Lsux62vqEYn7BxVu`</summary>

```text
Web search results for query: "site:arxiv.org 2602.08159 "Confidence Manifold" authors"

Links: [{"title":"The Confidence Manifold:","url":"https://www.arxiv.org/pdf/2602.08159"},{"title":"The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models","url":"https://arxiv.org/html/2602.08159v1"},{"title":"The Confidence Manifold - Seongland","url":"https://seongland.com/article/confidence-manifold/"},{"title":"Point Mass in the Confidence Distribution: Is it a Drawback or an   Advantage?","url":"https://arxiv.org/pdf/2310.09960"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6822779/"},{"title":"The folded X-pattern is not necessarily a statistical signature of decision confidence","url":"https://www.biorxiv.org/content/10.1101/426635.full.pdf"},{"title":"Oracle complexities of augmented Lagrangian methods for nonsmooth   manifold optimization","url":"https://arxiv.org/pdf/2404.05121"},{"title":"A low-dimensional approximation of optimal confidence","url":"https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"},{"title":"The positive evidence bias in perceptual confidence is not post-decisional","url":"https://www.biorxiv.org/content/10.1101/2020.03.15.991513.full.pdf"}]

Based on the search results, I found information about the paper with arXiv ID 2602.08159, but the author names are not clearly visible in the snippets provided. The search results show that "The Confidence Manifold" characterizes the geometry of correctness representations across 9 models from 5 architecture families, with a structure where the discriminative signal occupies 3–8 dimensions and performance degrades with additional dimensions.

However, the specific author names are not displayed in these search result snippets. You can access the full paper with complete author information directly at arxiv.org/abs/2602.08159 or arxiv.org/pdf/2602.08159.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "f96c3014-c1b0-4095-99dc-d55f5fb043eb",
  "tool_use_result": {
    "query": "site:arxiv.org 2602.08159 \"Confidence Manifold\" authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_019x1xMgECSWgtiZPhisCTUU",
        "content": [
          {
            "title": "The Confidence Manifold:",
            "url": "https://www.arxiv.org/pdf/2602.08159"
          },
          {
            "title": "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models",
            "url": "https://arxiv.org/html/2602.08159v1"
          },
          {
            "title": "The Confidence Manifold - Seongland",
            "url": "https://seongland.com/article/confidence-manifold/"
          },
          {
            "title": "Point Mass in the Confidence Distribution: Is it a Drawback or an   Advantage?",
            "url": "https://arxiv.org/pdf/2310.09960"
          },
          {
            "title": "The folded X-pattern is not necessarily a statistical signature of decision confidence",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6822779/"
          },
          {
            "title": "The folded X-pattern is not necessarily a statistical signature of decision confidence",
            "url": "https://www.biorxiv.org/content/10.1101/426635.full.pdf"
          },
          {
            "title": "Oracle complexities of augmented Lagrangian methods for nonsmooth   manifold optimization",
            "url": "https://arxiv.org/pdf/2404.05121"
          },
          {
            "title": "A low-dimensional approximation of optimal confidence",
            "url": "https://www.biorxiv.org/content/10.1101/2023.03.15.532729.full.pdf"
          },
          {
            "title": "The positive evidence bias in perceptual confidence is not post-decisional",
            "url": "https://www.biorxiv.org/content/10.1101/2020.03.15.991513.full.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the paper with arXiv ID 2602.08159, but the author names are not clearly visible in the snippets provided. The search results show that \"The Confidence Manifold\" characterizes the geometry of correctness representations across 9 models from 5 architecture families, with a structure where the discriminative signal occupies 3–8 dimensions and performance degrades with additional dimensions.\n\nHowever, the specific author names are not displayed in these search result snippets. You can access the full paper with complete author information directly at arxiv.org/abs/2602.08159 or arxiv.org/pdf/2602.08159."
    ],
    "durationSeconds": 4.789261047000007
  }
}
```

</details>

---

### Assistant

_source line 111_

<details><summary>Logged reasoning block</summary>

```text
I can't find the Confidence Manifold authors through web search. Let me try WebFetch to get the actual arXiv page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "7aa96c03-cfbd-4151-8503-bad717136617",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpA6zaYDyyuTL2jhBWPcwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 65605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 112_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KMPzm5Vo9CE1BVB9fj3PYS`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "a1733400-f10d-4965-9b42-05cbc595453c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SpA6zaYDyyuTL2jhBWPcwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 65605,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-21T07:39:32.449Z_

<details><summary>↩ Tool result · `toolu_01KMPzm5Vo9CE1BVB9fj3PYS`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "7dd82efd-abf1-47fe-971d-bcf8b164c1f7",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Tool call

_source line 114_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0166aJbdzHkui4yRPdogDtMu`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.08159",
  "prompt": "What are the full author names of this paper? Return just the author names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "3502ca68-60d7-405e-95bd-bb471b18421f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014cMsvqg2wssuwHcLkhxU5a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 66355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-21T07:39:37.694Z_

<details><summary>↩ Tool result · `toolu_0166aJbdzHkui4yRPdogDtMu`</summary>

```text
Based on the paper, the full author names are:

1. Seonglae Cho
2. Zekun Wu
3. Kleyton Da Costa
4. Adriano Koshiyama
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "663722bc-653b-46e7-a65e-553518666679",
  "tool_use_result": {
    "bytes": 46880,
    "code": 200,
    "codeText": "OK",
    "result": "Based on the paper, the full author names are:\n\n1. Seonglae Cho\n2. Zekun Wu\n3. Kleyton Da Costa\n4. Adriano Koshiyama",
    "durationMs": 2087,
    "url": "https://arxiv.org/abs/2602.08159"
  }
}
```

</details>

---

### Assistant

_source line 116_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile everything and write the bib entries and edit the related_work.tex.

Let me organize the information:

## Part 1: Missing 22 bib entries

### Classic papers (1-11):

1. `guo2017calibration` — Guo et al. "On Calibration of Modern Neural Networks" ICML 2017
   - Authors: Chuan Guo, Geoff Pleiss, Yu Sun, Kilian Q. Weinberger
   - Booktitle: Proceedings of the 34th International Conference on Machine Learning (PMLR 70)
   - Year: 2017
   - URL: https://proceedings.mlr.press/v70/guo17a.html

2. `hewitt2019control` — Hewitt & Liang "Designing and Interpreting Probes with Control Tasks" EMNLP 2019
   - Authors: John Hewitt, Percy Liang
   - Booktitle: Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing
   - Pages: 2733-2743
   - Year: 2019
   - DOI: 10.18653/v1/D19-1275

3. `kornblith2019cka` — Kornblith et al. on similarity metrics for neural networks at ICML 2019, with Hinton and Lee among the authors, published in PMLR volume 97. 4. `pires2019multilingual` — Pires, Schlinger, and Garrette examining multilingual BERT's cross-lingual capabilities at ACL 2019, pages 4996-5001.

Now I'm adding two more papers on cross-lingual BERT effectiveness and information-theoretic probing methods. Wu and Dredze's 2019 EMNLP paper explores how well BERT transfers across languages despite not being explicitly trained for it, while Voita and Titov's 2020 work introduces a minimum description length approach to probing what linguistic information neural networks capture. Continuing with the bibliographic entries, I'm adding the publication details for Belinkov's work on probing classifiers, then moving into Ben-David's foundational theory paper on learning across domains, and starting to catalog Zhao's research on invariant representations for domain adaptation. Now I'm compiling the recent papers from 2025-2026, starting with Xiao et al.'s work on how language models understand knowledge boundaries across different languages through their internal representations, followed by Zhou et al.'s contribution that's still being documented. Continuing with the CORAL paper details and finding the Khanmohammadi et al. work on calibrating LLM confidence through representation stability analysis. I found the complete details for the Ji et al. paper—it's about calibrating verbal uncertainty as a linear feature to reduce hallucinations, published in EMNLP 2025. I'm also locating the Joshi et al. entry on calibration evolution across layers in language models, also from EMNLP 2025, though the DOI appears to be truncated.

Now I'm pulling up the Liu and Niehues paper on middle-layer representation alignment for cross-lingual transfer in fine-tuned LLMs from ACL 2025, and starting to verify the Ravisankar et al. EACL 2026 paper, though that entry seems to cut off mid-title. Now I'm adding the Conneau et al. 2020 paper on cross-lingual representation learning, which includes the full author list, publication details, and DOI, followed by the Lord 1980 reference on item response theory applications.

Compiling bibliography entries...

I've tracked down the authors for the Confidence Manifold paper and confirmed the publication details for the other entries. The Zhou LACE paper is from arXiv 2510.03136 presented at MELT Workshop at COLM 2025, so I'll cite the arXiv version. The CORAL paper was accepted to ICML 2026, so that should use the inproceedings format. For Miao's 2026 closing paper on arXiv 2603.25052, it appears to only have the preprint so far.

Now I'm going through the remaining papers—Civelli's 2026 work on arXiv 2601.12731 also looks like it's just a preprint without a venue yet. I'm ready to construct all the bibliography entries and add them to the end of the existing file after the last entry. Then I need to plan the edits to related_work.tex, starting with integrating the conneau2020xlmr citation into the Cross-Lingual Probing and Transfer section near the existing Pires and Wu&Dredze references. I'm looking more carefully at the related_work.tex to find where IRT is already mentioned in the cross-lingual probing section, so I can add the citation there naturally. For the Switch Transformers paper, the task marks it as optional, and since there's no clear insertion point in related_work.tex and the method only mentions Qwen3-235B-A22B as an MoE model without discussing the architecture itself, I'll skip adding it to the paper but still include the bibliography entry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e36055b8-fa99-4e1c-b968-0c11c62dde55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFR6dTDER5vgJCZPbNiyAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 66995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 117_

All papers verified. Now I'll write the bib entries and edit the tex files. Let me construct the complete addition to custom.bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b3096c41-b910-4642-912c-806fa57e3b5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFR6dTDER5vgJCZPbNiyAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 66995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 118_

<details open><summary>🔧 Tool call — Edit · `toolu_01KDJVYrdXBnH8iZHQzaxDvj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib",
  "old_string": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}",
  "new_string": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}\n\n% ============================================================\n% Missing citations referenced in .tex files\n% ============================================================\n\n@inproceedings{guo2017calibration,\n    title={On Calibration of Modern Neural Networks},\n    author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n    booktitle={Proceedings of the 34th International Conference on Machine Learning},\n    series={PMLR},\n    volume={70},\n    pages={1321--1330},\n    year={2017},\n    url={https://proceedings.mlr.press/v70/guo17a.html}\n}\n\n@inproceedings{hewitt2019control,\n    title={Designing and Interpreting Probes with Control Tasks},\n    author={Hewitt, John and Liang, Percy},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={2733--2743},\n    year={2019},\n    doi={10.18653/v1/D19-1275}\n}\n\n@inproceedings{kornblith2019cka,\n    title={Similarity of Neural Network Representations Revisited},\n    author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={3519--3529},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/kornblith19a.html}\n}\n\n@inproceedings{pires2019multilingual,\n    title={How Multilingual is Multilingual {BERT}?},\n    author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},\n    booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages={4996--5001},\n    year={2019},\n    doi={10.18653/v1/P19-1493}\n}\n\n@inproceedings{wu2019beto,\n    title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},\n    author={Wu, Shijie and Dredze, Mark},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={833--844},\n    year={2019},\n    doi={10.18653/v1/D19-1077}\n}\n\n@inproceedings{voita2020mdl,\n    title={Information-Theoretic Probing with Minimum Description Length},\n    author={Voita, Elena and Titov, Ivan},\n    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages={183--196},\n    year={2020},\n    doi={10.18653/v1/2020.emnlp-main.14}\n}\n\n@inproceedings{karandikar2021sbece,\n    title={Soft Calibration Objectives for Neural Networks},\n    author={Karandikar, Archit and Cain, Nicholas and Tran, Dustin and Lakshminarayanan, Balaji and Shlens, Jonathon and Mozer, Michael C. and Roelofs, Becca},\n    booktitle={Advances in Neural Information Processing Systems},\n    volume={34},\n    pages={29768--29779},\n    year={2021}\n}\n\n@article{belinkov2022probing,\n    title={Probing Classifiers: Promises, Shortcomings, and Advances},\n    author={Belinkov, Yonatan},\n    journal={Computational Linguistics},\n    volume={48},\n    number={1},\n    pages={207--219},\n    year={2022},\n    publisher={MIT Press},\n    doi={10.1162/coli_a_00422}\n}\n\n@article{bendavid2010theory,\n    title={A Theory of Learning from Different Domains},\n    author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n    journal={Machine Learning},\n    volume={79},\n    number={1--2},\n    pages={151--175},\n    year={2010},\n    doi={10.1007/s10994-009-5152-4}\n}\n\n@inproceedings{zhao2019invariant,\n    title={On Learning Invariant Representations for Domain Adaptation},\n    author={Zhao, Han and des Combes, Remi Tachet and Zhang, Kun and Gordon, Geoffrey J.},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={7523--7532},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/zhao19a.html}\n}\n\n@article{angelopoulos2023conformal,\n    title={Conformal Prediction: A Gentle Introduction},\n    author={Angelopoulos, Anastasios N. and Bates, Stephen},\n    journal={Foundations and Trends in Machine Learning},\n    volume={16},\n    number={4},\n    pages={494--591},\n    year={2023},\n    doi={10.1561/2200000101}\n}\n\n@inproceedings{xiao2025knowledge,\n    title={Analyzing {LLMs}' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations},\n    author={Xiao, Chenghao and Chan, Hou Pong and Zhang, Hao and Aljunied, Mahani and Bing, Lidong and Al Moubayed, Noura and Rong, Yu},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    year={2025},\n    doi={10.18653/v1/2025.acl-long.1174}\n}\n\n@article{zhou2025lace,\n    title={Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models},\n    author={Zhou, Ej and Zhang, Caiqi and Hu, Tiancheng and Li, Chengzu and Collier, Nigel and Vuli{\\'c}, Ivan and Korhonen, Anna},\n    journal={arXiv preprint arXiv:2510.03136},\n    year={2025}\n}\n\n@article{miao2026closing,\n    title={Closing the Confidence-Faithfulness Gap in Large Language Models},\n    author={Miao, Miranda Muqing and Ungar, Lyle},\n    journal={arXiv preprint arXiv:2603.25052},\n    year={2026}\n}\n\n@inproceedings{miao2026coral,\n    title={Correctness-Optimized Residual Activation Lens ({CORAL}): Transferrable and Calibration-Aware Inference-Time Steering},\n    author={Miao, Miranda Muqing and Cho, Young-Min and Ungar, Lyle},\n    booktitle={Proceedings of the 43rd International Conference on Machine Learning},\n    year={2026},\n    url={https://arxiv.org/abs/2602.06022}\n}\n\n@inproceedings{khanmohammadi2025ccps,\n    title={Calibrating {LLM} Confidence by Probing Perturbed Representation Stability},\n    author={Khanmohammadi, Reza and Miahi, Erfan and Mardikoraem, Mehrsa and Kaur, Simerjot and Brugere, Ivan and Smiley, Charese and Thind, Kundan S. and Ghassemi, Mohammad M.},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={10448--10514},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.530}\n}\n\n@article{confidence_manifold2026,\n    title={The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models},\n    author={Cho, Seonglae and Wu, Zekun and Da Costa, Kleyton and Koshiyama, Adriano},\n    journal={arXiv preprint arXiv:2602.08159},\n    year={2026}\n}\n\n@inproceedings{ji2025calibrating,\n    title={Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations},\n    author={Ji, Ziwei and Yu, Lei and Koishekenov, Yeskendir and Bang, Yejin and Hartshorn, Anthony and Schelten, Alan and Zhang, Cheng and Fung, Pascale and Cancedda, Nicola},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={3769--3793},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.187}\n}\n\n@inproceedings{joshi2025calibration,\n    title={Calibration Across Layers: Understanding Calibration Evolution in {LLMs}},\n    author={Joshi, Abhinav and Ahmad, Areeb and Modi, Ashutosh},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.742}\n}\n\n@inproceedings{liu2025middle,\n    title={Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned {LLMs}},\n    author={Liu, Danni and Niehues, Jan},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    pages={15979--15996},\n    year={2025},\n    url={https://arxiv.org/abs/2502.14830}\n}\n\n@inproceedings{ravisankar2026dali,\n    title={Can You Map It to {English}? {T}he Role of Cross-Lingual Alignment in the Multilingual Performance of {LLMs}},\n    author={Ravisankar, Kartik and Han, HyoJung and Wiegreffe, Sarah and Carpuat, Marine},\n    booktitle={Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics},\n    pages={4854--4872},\n    year={2026},\n    url={https://arxiv.org/abs/2504.09378}\n}\n\n@article{civelli2026shared,\n    title={A Shared Geometry of Difficulty in Multilingual Language Models},\n    author={Civelli, Stefano and Bernardelle, Pietro and Brunello, Nicol{\\`o} and Demartini, Gianluca},\n    journal={arXiv preprint arXiv:2601.12731},\n    year={2026}\n}\n\n% ============================================================\n% Newly added citations\n% ============================================================\n\n@inproceedings{conneau2020xlmr,\n    title={Unsupervised Cross-lingual Representation Learning at Scale},\n    author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},\n    booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n    pages={8440--8451},\n    year={2020},\n    doi={10.18653/v1/2020.acl-main.747}\n}\n\n@book{lord1980irt,\n    title={Applications of Item Response Theory to Practical Testing Problems},\n    author={Lord, Frederic M.},\n    year={1980},\n    publisher={Lawrence Erlbaum Associates},\n    address={Hillsdale, NJ},\n    isbn={978-0898590067}\n}\n\n@article{fedus2022switch,\n    title={Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},\n    author={Fedus, William and Zoph, Barret and Shazeer, Noam},\n    journal={Journal of Machine Learning Research},\n    volume={23},\n    number={120},\n    pages={1--39},\n    year={2022},\n    url={https://jmlr.org/papers/v23/21-0998.html}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e94e156f-acc3-4586-8961-acbefc3c8183",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KFR6dTDER5vgJCZPbNiyAx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 66995,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 119 · 2026-05-21T07:41:35.774Z_

<details><summary>↩ Tool result · `toolu_01KDJVYrdXBnH8iZHQzaxDvj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "d5f07667-2902-478b-9c21-4c0dc9aba194",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib",
    "oldString": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}",
    "newString": "@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}\n\n% ============================================================\n% Missing citations referenced in .tex files\n% ============================================================\n\n@inproceedings{guo2017calibration,\n    title={On Calibration of Modern Neural Networks},\n    author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n    booktitle={Proceedings of the 34th International Conference on Machine Learning},\n    series={PMLR},\n    volume={70},\n    pages={1321--1330},\n    year={2017},\n    url={https://proceedings.mlr.press/v70/guo17a.html}\n}\n\n@inproceedings{hewitt2019control,\n    title={Designing and Interpreting Probes with Control Tasks},\n    author={Hewitt, John and Liang, Percy},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={2733--2743},\n    year={2019},\n    doi={10.18653/v1/D19-1275}\n}\n\n@inproceedings{kornblith2019cka,\n    title={Similarity of Neural Network Representations Revisited},\n    author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={3519--3529},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/kornblith19a.html}\n}\n\n@inproceedings{pires2019multilingual,\n    title={How Multilingual is Multilingual {BERT}?},\n    author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},\n    booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages={4996--5001},\n    year={2019},\n    doi={10.18653/v1/P19-1493}\n}\n\n@inproceedings{wu2019beto,\n    title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},\n    author={Wu, Shijie and Dredze, Mark},\n    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages={833--844},\n    year={2019},\n    doi={10.18653/v1/D19-1077}\n}\n\n@inproceedings{voita2020mdl,\n    title={Information-Theoretic Probing with Minimum Description Length},\n    author={Voita, Elena and Titov, Ivan},\n    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages={183--196},\n    year={2020},\n    doi={10.18653/v1/2020.emnlp-main.14}\n}\n\n@inproceedings{karandikar2021sbece,\n    title={Soft Calibration Objectives for Neural Networks},\n    author={Karandikar, Archit and Cain, Nicholas and Tran, Dustin and Lakshminarayanan, Balaji and Shlens, Jonathon and Mozer, Michael C. and Roelofs, Becca},\n    booktitle={Advances in Neural Information Processing Systems},\n    volume={34},\n    pages={29768--29779},\n    year={2021}\n}\n\n@article{belinkov2022probing,\n    title={Probing Classifiers: Promises, Shortcomings, and Advances},\n    author={Belinkov, Yonatan},\n    journal={Computational Linguistics},\n    volume={48},\n    number={1},\n    pages={207--219},\n    year={2022},\n    publisher={MIT Press},\n    doi={10.1162/coli_a_00422}\n}\n\n@article{bendavid2010theory,\n    title={A Theory of Learning from Different Domains},\n    author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},\n    journal={Machine Learning},\n    volume={79},\n    number={1--2},\n    pages={151--175},\n    year={2010},\n    doi={10.1007/s10994-009-5152-4}\n}\n\n@inproceedings{zhao2019invariant,\n    title={On Learning Invariant Representations for Domain Adaptation},\n    author={Zhao, Han and des Combes, Remi Tachet and Zhang, Kun and Gordon, Geoffrey J.},\n    booktitle={Proceedings of the 36th International Conference on Machine Learning},\n    series={PMLR},\n    volume={97},\n    pages={7523--7532},\n    year={2019},\n    url={https://proceedings.mlr.press/v97/zhao19a.html}\n}\n\n@article{angelopoulos2023conformal,\n    title={Conformal Prediction: A Gentle Introduction},\n    author={Angelopoulos, Anastasios N. and Bates, Stephen},\n    journal={Foundations and Trends in Machine Learning},\n    volume={16},\n    number={4},\n    pages={494--591},\n    year={2023},\n    doi={10.1561/2200000101}\n}\n\n@inproceedings{xiao2025knowledge,\n    title={Analyzing {LLMs}' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations},\n    author={Xiao, Chenghao and Chan, Hou Pong and Zhang, Hao and Aljunied, Mahani and Bing, Lidong and Al Moubayed, Noura and Rong, Yu},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    year={2025},\n    doi={10.18653/v1/2025.acl-long.1174}\n}\n\n@article{zhou2025lace,\n    title={Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models},\n    author={Zhou, Ej and Zhang, Caiqi and Hu, Tiancheng and Li, Chengzu and Collier, Nigel and Vuli{\\'c}, Ivan and Korhonen, Anna},\n    journal={arXiv preprint arXiv:2510.03136},\n    year={2025}\n}\n\n@article{miao2026closing,\n    title={Closing the Confidence-Faithfulness Gap in Large Language Models},\n    author={Miao, Miranda Muqing and Ungar, Lyle},\n    journal={arXiv preprint arXiv:2603.25052},\n    year={2026}\n}\n\n@inproceedings{miao2026coral,\n    title={Correctness-Optimized Residual Activation Lens ({CORAL}): Transferrable and Calibration-Aware Inference-Time Steering},\n    author={Miao, Miranda Muqing and Cho, Young-Min and Ungar, Lyle},\n    booktitle={Proceedings of the 43rd International Conference on Machine Learning},\n    year={2026},\n    url={https://arxiv.org/abs/2602.06022}\n}\n\n@inproceedings{khanmohammadi2025ccps,\n    title={Calibrating {LLM} Confidence by Probing Perturbed Representation Stability},\n    author={Khanmohammadi, Reza and Miahi, Erfan and Mardikoraem, Mehrsa and Kaur, Simerjot and Brugere, Ivan and Smiley, Charese and Thind, Kundan S. and Ghassemi, Mohammad M.},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={10448--10514},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.530}\n}\n\n@article{confidence_manifold2026,\n    title={The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models},\n    author={Cho, Seonglae and Wu, Zekun and Da Costa, Kleyton and Koshiyama, Adriano},\n    journal={arXiv preprint arXiv:2602.08159},\n    year={2026}\n}\n\n@inproceedings{ji2025calibrating,\n    title={Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations},\n    author={Ji, Ziwei and Yu, Lei and Koishekenov, Yeskendir and Bang, Yejin and Hartshorn, Anthony and Schelten, Alan and Zhang, Cheng and Fung, Pascale and Cancedda, Nicola},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages={3769--3793},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.187}\n}\n\n@inproceedings{joshi2025calibration,\n    title={Calibration Across Layers: Understanding Calibration Evolution in {LLMs}},\n    author={Joshi, Abhinav and Ahmad, Areeb and Modi, Ashutosh},\n    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year={2025},\n    doi={10.18653/v1/2025.emnlp-main.742}\n}\n\n@inproceedings{liu2025middle,\n    title={Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned {LLMs}},\n    author={Liu, Danni and Niehues, Jan},\n    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},\n    pages={15979--15996},\n    year={2025},\n    url={https://arxiv.org/abs/2502.14830}\n}\n\n@inproceedings{ravisankar2026dali,\n    title={Can You Map It to {English}? {T}he Role of Cross-Lingual Alignment in the Multilingual Performance of {LLMs}},\n    author={Ravisankar, Kartik and Han, HyoJung and Wiegreffe, Sarah and Carpuat, Marine},\n    booktitle={Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics},\n    pages={4854--4872},\n    year={2026},\n    url={https://arxiv.org/abs/2504.09378}\n}\n\n@article{civelli2026shared,\n    title={A Shared Geometry of Difficulty in Multilingual Language Models},\n    author={Civelli, Stefano and Bernardelle, Pietro and Brunello, Nicol{\\`o} and Demartini, Gianluca},\n    journal={arXiv preprint arXiv:2601.12731},\n    year={2026}\n}\n\n% ============================================================\n% Newly added citations\n% ============================================================\n\n@inproceedings{conneau2020xlmr,\n    title={Unsupervised Cross-lingual Representation Learning at Scale},\n    author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},\n    booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},\n    pages={8440--8451},\n    year={2020},\n    doi={10.18653/v1/2020.acl-main.747}\n}\n\n@book{lord1980irt,\n    title={Applications of Item Response Theory to Practical Testing Problems},\n    author={Lord, Frederic M.},\n    year={1980},\n    publisher={Lawrence Erlbaum Associates},\n    address={Hillsdale, NJ},\n    isbn={978-0898590067}\n}\n\n@article{fedus2022switch,\n    title={Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},\n    author={Fedus, William and Zoph, Barret and Shazeer, Noam},\n    journal={Journal of Machine Learning Research},\n    volume={23},\n    number={120},\n    pages={1--39},\n    year={2022},\n    url={https://jmlr.org/papers/v23/21-0998.html}\n}",
    "originalFile": "% Use this file for citations not found in the ACL Anthology (contained in \"anthology.bib\").\n\n@book{Aho:72,\n    author  = {Alfred V. Aho and Jeffrey D. Ullman},\n    title   = {The Theory of Parsing, Translation and Compiling},\n    year    = \"1972\",\n    volume  = \"1\",\n    publisher = {Prentice-Hall},\n    address = {Englewood Cliffs, NJ}\n}\n\n@book{APA:83,\n    author  = {{American Psychological Association}},\n    title   = {Publications Manual},\n    year    = \"1983\",\n    publisher = {American Psychological Association},\n    address = {Washington, DC}\n}\n\n@article{Chandra:81,\n\tauthor = {Ashok K. Chandra and Dexter C. Kozen and Larry J. Stockmeyer},\n\tyear = \"1981\",\n\ttitle = {Alternation},\n\tjournal = {Journal of the Association for Computing Machinery},\n\tvolume = \"28\",\n\tnumber = \"1\",\n\tpages = \"114--133\",\n\tdoi = \"10.1145/322234.322243\",\n}\n\n@inproceedings{andrew2007scalable,\n  title={Scalable training of {L1}-regularized log-linear models},\n  author={Andrew, Galen and Gao, Jianfeng},\n  booktitle={Proceedings of the 24th International Conference on Machine Learning},\n  pages={33--40},\n  year={2007},\n}\n\n@book{Gusfield:97,\n    author  = {Dan Gusfield},\n    title   = {Algorithms on Strings, Trees and Sequences},\n    year    = \"1997\",\n    publisher = {Cambridge University Press},\n    address = {Cambridge, UK}\n}\n\n@article{rasooli-tetrault-2015,\n    author    = {Mohammad Sadegh Rasooli and Joel R. Tetreault},\n    title     = {Yara Parser: {A} Fast and Accurate Dependency Parser},\n    journal   = {Computing Research Repository},\n    volume    = {arXiv:1503.06733},\n    year      = {2015},\n    url       = {http://arxiv.org/abs/1503.06733},\n    note    = {version 2}\n}\n\n@article{Ando2005,\n\tAcmid = {1194905},\n\tAuthor = {Ando, Rie Kubota and Zhang, Tong},\n\tIssn = {1532-4435},\n\tIssue_Date = {12/1/2005},\n\tJournal = {Journal of Machine Learning Research},\n\tMonth = dec,\n\tNumpages = {37},\n\tPages = {1817--1853},\n\tPublisher = {JMLR.org},\n\tTitle = {A Framework for Learning Predictive Structures from Multiple Tasks and Unlabeled Data},\n\tVolume = {6},\n\tYear = {2005}\n}\n\n% [TO_ADD_BIB] -- Verified citations added for Related Work section\n\n@article{kadavath2022language,\n    title={Language Models (Mostly) Know What They Know},\n    author={Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DaSilva, Nova and Tran-Johnson, Eli and others},\n    journal={arXiv preprint arXiv:2207.05221},\n    year={2022}\n}\n\n@inproceedings{niculescu2005predicting,\n    title={Predicting Good Probabilities with Supervised Learning},\n    author={Niculescu-Mizil, Alexandru and Caruana, Rich},\n    booktitle={Proceedings of the 22nd International Conference on Machine Learning},\n    pages={625--632},\n    year={2005},\n    doi={10.1145/1102351.1102430}\n}\n\n@inproceedings{conneau2018muse,\n    title={Word Translation Without Parallel Data},\n    author={Conneau, Alexis and Lample, Guillaume and Ranzato, Marc'Aurelio and Denoyer, Ludovic and J{\\'e}gou, Herv{\\'e}},\n    booktitle={International Conference on Learning Representations},\n    year={2018}\n}\n\n@inproceedings{artetxe2018vecmap,\n    title={A Robust Self-Learning Method for Fully Unsupervised Cross-Lingual Mappings of Word Embeddings},\n    author={Artetxe, Mikel and Labaka, Gorka and Agirre, Eneko},\n    booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n    pages={789--798},\n    year={2018}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 101,
        "oldLines": 3,
        "newStart": 101,
        "newLines": 240,
        "lines": [
          "     pages={789--798},",
          "     year={2018}",
          " }",
          "+",
          "+% ============================================================",
          "+% Missing citations referenced in .tex files",
          "+% ============================================================",
          "+",
          "+@inproceedings{guo2017calibration,",
          "+    title={On Calibration of Modern Neural Networks},",
          "+    author={Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},",
          "+    booktitle={Proceedings of the 34th International Conference on Machine Learning},",
          "+    series={PMLR},",
          "+    volume={70},",
          "+    pages={1321--1330},",
          "+    year={2017},",
          "+    url={https://proceedings.mlr.press/v70/guo17a.html}",
          "+}",
          "+",
          "+@inproceedings{hewitt2019control,",
          "+    title={Designing and Interpreting Probes with Control Tasks},",
          "+    author={Hewitt, John and Liang, Percy},",
          "+    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},",
          "+    pages={2733--2743},",
          "+    year={2019},",
          "+    doi={10.18653/v1/D19-1275}",
          "+}",
          "+",
          "+@inproceedings{kornblith2019cka,",
          "+    title={Similarity of Neural Network Representations Revisited},",
          "+    author={Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},",
          "+    booktitle={Proceedings of the 36th International Conference on Machine Learning},",
          "+    series={PMLR},",
          "+    volume={97},",
          "+    pages={3519--3529},",
          "+    year={2019},",
          "+    url={https://proceedings.mlr.press/v97/kornblith19a.html}",
          "+}",
          "+",
          "+@inproceedings{pires2019multilingual,",
          "+    title={How Multilingual is Multilingual {BERT}?},",
          "+    author={Pires, Telmo and Schlinger, Eva and Garrette, Dan},",
          "+    booktitle={Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},",
          "+    pages={4996--5001},",
          "+    year={2019},",
          "+    doi={10.18653/v1/P19-1493}",
          "+}",
          "+",
          "+@inproceedings{wu2019beto,",
          "+    title={Beto, Bentz, Becas: The Surprising Cross-Lingual Effectiveness of {BERT}},",
          "+    author={Wu, Shijie and Dredze, Mark},",
          "+    booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},",
          "+    pages={833--844},",
          "+    year={2019},",
          "+    doi={10.18653/v1/D19-1077}",
          "+}",
          "+",
          "+@inproceedings{voita2020mdl,",
          "+    title={Information-Theoretic Probing with Minimum Description Length},",
          "+    author={Voita, Elena and Titov, Ivan},",
          "+    booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages={183--196},",
          "+    year={2020},",
          "+    doi={10.18653/v1/2020.emnlp-main.14}",
          "+}",
          "+",
          "+@inproceedings{karandikar2021sbece,",
          "+    title={Soft Calibration Objectives for Neural Networks},",
          "+    author={Karandikar, Archit and Cain, Nicholas and Tran, Dustin and Lakshminarayanan, Balaji and Shlens, Jonathon and Mozer, Michael C. and Roelofs, Becca},",
          "+    booktitle={Advances in Neural Information Processing Systems},",
          "+    volume={34},",
          "+    pages={29768--29779},",
          "+    year={2021}",
          "+}",
          "+",
          "+@article{belinkov2022probing,",
          "+    title={Probing Classifiers: Promises, Shortcomings, and Advances},",
          "+    author={Belinkov, Yonatan},",
          "+    journal={Computational Linguistics},",
          "+    volume={48},",
          "+    number={1},",
          "+    pages={207--219},",
          "+    year={2022},",
          "+    publisher={MIT Press},",
          "+    doi={10.1162/coli_a_00422}",
          "+}",
          "+",
          "+@article{bendavid2010theory,",
          "+    title={A Theory of Learning from Different Domains},",
          "+    author={Ben-David, Shai and Blitzer, John and Crammer, Koby and Kulesza, Alex and Pereira, Fernando and Vaughan, Jennifer Wortman},",
          "+    journal={Machine Learning},",
          "+    volume={79},",
          "+    number={1--2},",
          "+    pages={151--175},",
          "+    year={2010},",
          "+    doi={10.1007/s10994-009-5152-4}",
          "+}",
          "+",
          "+@inproceedings{zhao2019invariant,",
          "+    title={On Learning Invariant Representations for Domain Adaptation},",
          "+    author={Zhao, Han and des Combes, Remi Tachet and Zhang, Kun and Gordon, Geoffrey J.},",
          "+    booktitle={Proceedings of the 36th International Conference on Machine Learning},",
          "+    series={PMLR},",
          "+    volume={97},",
          "+    pages={7523--7532},",
          "+    year={2019},",
          "+    url={https://proceedings.mlr.press/v97/zhao19a.html}",
          "+}",
          "+",
          "+@article{angelopoulos2023conformal,",
          "+    title={Conformal Prediction: A Gentle Introduction},",
          "+    author={Angelopoulos, Anastasios N. and Bates, Stephen},",
          "+    journal={Foundations and Trends in Machine Learning},",
          "+    volume={16},",
          "+    number={4},",
          "+    pages={494--591},",
          "+    year={2023},",
          "+    doi={10.1561/2200000101}",
          "+}",
          "+",
          "+@inproceedings{xiao2025knowledge,",
          "+    title={Analyzing {LLMs}' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations},",
          "+    author={Xiao, Chenghao and Chan, Hou Pong and Zhang, Hao and Aljunied, Mahani and Bing, Lidong and Al Moubayed, Noura and Rong, Yu},",
          "+    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},",
          "+    year={2025},",
          "+    doi={10.18653/v1/2025.acl-long.1174}",
          "+}",
          "+",
          "+@article{zhou2025lace,",
          "+    title={Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in Large Language Models},",
          "+    author={Zhou, Ej and Zhang, Caiqi and Hu, Tiancheng and Li, Chengzu and Collier, Nigel and Vuli{\\'c}, Ivan and Korhonen, Anna},",
          "+    journal={arXiv preprint arXiv:2510.03136},",
          "+    year={2025}",
          "+}",
          "+",
          "+@article{miao2026closing,",
          "+    title={Closing the Confidence-Faithfulness Gap in Large Language Models},",
          "+    author={Miao, Miranda Muqing and Ungar, Lyle},",
          "+    journal={arXiv preprint arXiv:2603.25052},",
          "+    year={2026}",
          "+}",
          "+",
          "+@inproceedings{miao2026coral,",
          "+    title={Correctness-Optimized Residual Activation Lens ({CORAL}): Transferrable and Calibration-Aware Inference-Time Steering},",
          "+    author={Miao, Miranda Muqing and Cho, Young-Min and Ungar, Lyle},",
          "+    booktitle={Proceedings of the 43rd International Conference on Machine Learning},",
          "+    year={2026},",
          "+    url={https://arxiv.org/abs/2602.06022}",
          "+}",
          "+",
          "+@inproceedings{khanmohammadi2025ccps,",
          "+    title={Calibrating {LLM} Confidence by Probing Perturbed Representation Stability},",
          "+    author={Khanmohammadi, Reza and Miahi, Erfan and Mardikoraem, Mehrsa and Kaur, Simerjot and Brugere, Ivan and Smiley, Charese and Thind, Kundan S. and Ghassemi, Mohammad M.},",
          "+    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages={10448--10514},",
          "+    year={2025},",
          "+    doi={10.18653/v1/2025.emnlp-main.530}",
          "+}",
          "+",
          "+@article{confidence_manifold2026,",
          "+    title={The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models},",
          "+    author={Cho, Seonglae and Wu, Zekun and Da Costa, Kleyton and Koshiyama, Adriano},",
          "+    journal={arXiv preprint arXiv:2602.08159},",
          "+    year={2026}",
          "+}",
          "+",
          "+@inproceedings{ji2025calibrating,",
          "+    title={Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations},",
          "+    author={Ji, Ziwei and Yu, Lei and Koishekenov, Yeskendir and Bang, Yejin and Hartshorn, Anthony and Schelten, Alan and Zhang, Cheng and Fung, Pascale and Cancedda, Nicola},",
          "+    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages={3769--3793},",
          "+    year={2025},",
          "+    doi={10.18653/v1/2025.emnlp-main.187}",
          "+}",
          "+",
          "+@inproceedings{joshi2025calibration,",
          "+    title={Calibration Across Layers: Understanding Calibration Evolution in {LLMs}},",
          "+    author={Joshi, Abhinav and Ahmad, Areeb and Modi, Ashutosh},",
          "+    booktitle={Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},",
          "+    year={2025},",
          "+    doi={10.18653/v1/2025.emnlp-main.742}",
          "+}",
          "+",
          "+@inproceedings{liu2025middle,",
          "+    title={Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned {LLMs}},",
          "+    author={Liu, Danni and Niehues, Jan},",
          "+    booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},",
          "+    pages={15979--15996},",
          "+    year={2025},",
          "+    url={https://arxiv.org/abs/2502.14830}",
          "+}",
          "+",
          "+@inproceedings{ravisankar2026dali,",
          "+    title={Can You Map It to {English}? {T}he Role of Cross-Lingual Alignment in the Multilingual Performance of {LLMs}},",
          "+    author={Ravisankar, Kartik and Han, HyoJung and Wiegreffe, Sarah and Carpuat, Marine},",
          "+    booktitle={Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics},",
          "+    pages={4854--4872},",
          "+    year={2026},",
          "+    url={https://arxiv.org/abs/2504.09378}",
          "+}",
          "+",
          "+@article{civelli2026shared,",
          "+    title={A Shared Geometry of Difficulty in Multilingual Language Models},",
          "+    author={Civelli, Stefano and Bernardelle, Pietro and Brunello, Nicol{\\`o} and Demartini, Gianluca},",
          "+    journal={arXiv preprint arXiv:2601.12731},",
          "+    year={2026}",
          "+}",
          "+",
          "+% ============================================================",
          "+% Newly added citations",
          "+% ============================================================",
          "+",
          "+@inproceedings{conneau2020xlmr,",
          "+    title={Unsupervised Cross-lingual Representation Learning at Scale},",
          "+    author={Conneau, Alexis and Khandelwal, Kartikay and Goyal, Naman and Chaudhary, Vishrav and Wenzek, Guillaume and Guzm{\\'a}n, Francisco and Grave, Edouard and Ott, Myle and Zettlemoyer, Luke and Stoyanov, Veselin},",
          "+    booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},",
          "+    pages={8440--8451},",
          "+    year={2020},",
          "+    doi={10.18653/v1/2020.acl-main.747}",
          "+}",
          "+",
          "+@book{lord1980irt,",
          "+    title={Applications of Item Response Theory to Practical Testing Problems},",
          "+    author={Lord, Frederic M.},",
          "+    year={1980},",
          "+    publisher={Lawrence Erlbaum Associates},",
          "+    address={Hillsdale, NJ},",
          "+    isbn={978-0898590067}",
          "+}",
          "+",
          "+@article{fedus2022switch,",
          "+    title={Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},",
          "+    author={Fedus, William and Zoph, Barret and Shazeer, Noam},",
          "+    journal={Journal of Machine Learning Research},",
          "+    volume={23},",
          "+    number={120},",
          "+    pages={1--39},",
          "+    year={2022},",
          "+    url={https://jmlr.org/papers/v23/21-0998.html}",
          "+}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 120_

Now editing related_work.tex to insert the new citations. I'll make three targeted edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "18b4eae7-d90c-4afa-a45c-90317b5e80b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTZEY19qenKkh8Zfo191yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8061,
      "cache_read_input_tokens": 67155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8061
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 121_

<details open><summary>🔧 Tool call — Edit · `toolu_01C6LA8tGKh8xmb74Cqxy7B8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
  "old_string": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]",
  "new_string": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "90976007-4754-4017-8342-0cb71a721ac0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DTZEY19qenKkh8Zfo191yW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8061,
      "cache_read_input_tokens": 67155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8061
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-21T07:41:43.812Z_

<details><summary>↩ Tool result · `toolu_01C6LA8tGKh8xmb74Cqxy7B8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "80fc1a2d-f34e-450e-8d7f-0451a039047d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
    "oldString": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]",
    "newString": "Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages.",
    "originalFile": "% Requires: \\usepackage{pifont} \\newcommand{\\cmark}{\\ding{51}} \\newcommand{\\xmark}{\\ding{55}}\n% Requires: \\usepackage{booktabs}\n\n\\section{Related Work}\n\n\\subsection{LLM Calibration and Internal Representations}\n\nPost-hoc calibration methods such as temperature scaling \\cite{guo2017calibration} and Platt scaling \\cite{niculescu2005predicting} treat model confidence as a scalar output to be recalibrated after training. These approaches assume access to a held-out validation set from the target distribution and operate entirely on output logits without inspecting internal representations.\nA complementary line of work examines whether models can self-assess correctness through verbalized confidence. \\citet{kadavath2022language} demonstrate that larger language models produce well-calibrated probability estimates when asked to evaluate their own answers, establishing that calibration information exists within the model prior to output generation.\n\nRecent studies shift attention from output-level calibration to representation-level probing. \\citet{miao2026closing} identify that correctness and verbalized confidence occupy nearly orthogonal subspaces in hidden states (cosine similarity below 0.04), suggesting that standard confidence elicitation fails to capture the full calibration signal. Building on this observation, CORAL \\cite{miao2026coral} trains correctness probes that transfer across tasks within English, achieving approximately 50\\% ECE improvement over verbalized confidence baselines. CCPS \\cite{khanmohammadi2025ccps} takes a complementary approach by measuring representation stability under input perturbations as a proxy for correctness. The Confidence Manifold framework \\cite{confidence_manifold2026} reveals that calibration-relevant information concentrates in a low-dimensional subspace (3 to 8 dimensions), with as few as 25 labeled examples sufficient for 89\\% probing accuracy. \\citet{ji2025calibrating} further demonstrate that verbal uncertainty in LLMs corresponds to a linear direction in representation space, while \\citet{joshi2025calibration} analyze how calibration signals evolve across layers, finding non-monotonic patterns that motivate layer selection.\n\nAll of these studies operate exclusively in English and on a single model architecture. Our work extends correctness probing to 20 languages across 2 model families, revealing that transfer quality varies substantially across languages and architectures.\n\n\\subsection{Cross-Lingual Probing and Transfer}\n\nCross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \\citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \\cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.\n\nThe technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \\cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \\cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]\n\\citet{liu2025middle} show that middle layers of fine-tuned LLMs exhibit stronger cross-lingual alignment than early or late layers, consistent with the depth patterns we observe for correctness probes.\n\nOur work differs in three respects: we probe correctness (an output-dependent signal that requires generating and evaluating answers), we provide systematic depth analysis with Pareto frontier characterization across architectures, and we evaluate 5 transfer methods (including linear projection inspired by MUSE/VecMap) across 20 languages.\n\n\\subsection{Multilingual Calibration}\n\nCalibration quality varies dramatically across languages. \\citet{zhou2025lace} document a 5$\\times$ ECE gap between English and low-resource languages across 100+ languages and propose LACE, an adaptive layer ensemble that selects different layer combinations per language. While effective, LACE requires per-language validation data with correctness labels, limiting applicability to languages where such annotations exist.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison with closely related work on calibration probing and cross-lingual transfer. Target signals: KB = knowledge boundary, Corr.\\ = correctness, Diff.\\ = difficulty. Zero-CL = zero target-language correctness labels required.}\n\\label{tab:related_work}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\textbf{Target} & \\textbf{\\# Langs} & \\textbf{Calib.} & \\textbf{Zero-CL} & \\textbf{Depth} & \\textbf{Transfer} \\\\\n& \\textbf{Signal} & & \\textbf{Metrics} & \\textbf{Labels} & \\textbf{Analysis} & \\textbf{Methods} \\\\\n\\midrule\nXiao et al. & KB & 8 & \\xmark & \\cmark & \\xmark & 1 \\\\\nLACE & -- & 100+ & \\cmark & \\xmark & partial & -- \\\\\nCORAL & Corr. & 1 & \\cmark & -- & \\cmark & 1 \\\\\nMiao \\& Ungar & Corr. & 1 & \\xmark & -- & \\xmark & -- \\\\\nCivelli et al. & Diff. & 7 & \\xmark & \\cmark & \\cmark & 1 \\\\\n\\midrule\n\\textbf{Ours} & \\textbf{Corr.} & \\textbf{20} & \\cmark & \\cmark & \\cmark & \\textbf{5} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe fundamental challenge that LACE addresses (per-language calibration heterogeneity) motivates our investigation, but our approach differs in both goal and mechanism. We analyze \\emph{why} cross-lingual transfer of correctness probes fails (architecture-dependent depth-transferability tradeoffs, geometric divergence measured by CKA) rather than engineering a per-language compensation. Our method requires zero target-language correctness labels, transferring probes trained on English data alone.\n\n\\subsection{Domain Adaptation Theory}\n\nThe theoretical framework of \\citet{bendavid2010theory} bounds target-domain error by source error plus a divergence term ($\\mathcal{H}$-divergence) between source and target distributions, plus a joint ideal error. Applied to cross-lingual probe transfer, this predicts degradation proportional to the representational distance between languages. \\citet{zhao2019invariant} prove a stronger negative result: when conditional distributions $P(Y|X)$ differ between domains, matching marginal distributions of representations can \\emph{increase} target error rather than reduce it.\n\nThis theoretical insight directly explains our empirical finding on CaCLR (Cross-lingual Calibration via Conditional Label-aware Representation matching). CaCLR applies MMD-based distributional matching to align probe logit distributions across languages. If distributional matching proves insufficient (pending experimental validation), this would align with the prediction of \\citet{zhao2019invariant}: because conditional accuracy distributions $P(\\text{correct}|\\mathbf{h})$ differ between languages (due to varying model competence), marginal alignment may destroy the conditional structure that probes rely on. Our CKA partial correlation analysis further reveals a Simpson's Paradox where aggregate cross-lingual similarity masks within-layer divergence, a confounding pattern that naive cross-layer pooling obscures.\n\n\\subsection{Probing Methodology and Evaluation}\n\nThe methodological foundations of representation probing inform our experimental design. \\citet{hewitt2019control} introduce control tasks that establish selectivity baselines, guarding against probes that succeed merely due to high capacity rather than genuine information in representations. \\citet{voita2020mdl} propose minimum description length probes as an information-theoretic alternative, measuring the amount of effort required to extract a property. \\citet{belinkov2022probing} surveys the broader landscape of probing classifiers, identifying best practices and common pitfalls including the capacity-informativeness tradeoff.\n\nWe apply the control task framework of \\citet{hewitt2019control} to cross-lingual correctness probing. English probing controls (Hewitt \\& Liang selectivity) reveal layer-dependent selectivity patterns, with selectivity concentrated in deeper layers (L20+) --- raising concerns that shallow-layer positive results in low-resource languages may partly reflect capacity artifacts rather than genuine correctness signal. Cross-lingual control experiments are planned to quantify this. For measuring representational similarity across languages and layers, we employ CKA \\cite{kornblith2019cka} with partial correlation analysis, revealing geometric structure invisible to standard pairwise comparisons. Conformal prediction \\cite{angelopoulos2023conformal} offers distribution-free coverage guarantees complementary to our probing approach but requires per-language calibration data, which our zero-correctness-label setting explicitly avoids.\n\nOur work contributes the first systematic application of probing controls to cross-lingual transfer evaluation and applies CKA with depth-controlled partial correlation as a diagnostic for understanding transfer failure modes.\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " ",
          " Cross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \\citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \\cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.",
          " ",
          "-The technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \\cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \\cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}. % [TO_ADD_BIB]",
          "+The technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \\cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \\cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages.",
          " \\citet{liu2025middle} show that middle layers of fine-tuned LLMs exhibit stronger cross-lingual alignment than early or late layers, consistent with the depth patterns we observe for correctness probes.",
          " ",
          " Our work differs in three respects: we probe correctness (an output-dependent signal that requires generating and evaluating answers), we provide systematic depth analysis with Pareto frontier characterization across architectures, and we evaluate 5 transfer methods (including linear projection inspired by MUSE/VecMap) across 20 languages."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Edit · `toolu_01P5weSqBW6kMZC56jpUrJQZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
  "old_string": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages;",
  "new_string": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels \\cite{lord1980irt} and report shared geometric structure across 7 languages;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "66bf3e9b-03be-4107-958c-2b53af7a846f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CcpxBtd3kmemgsnYt1U27Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 75216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 397
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-21T07:41:48.135Z_

<details><summary>↩ Tool result · `toolu_01P5weSqBW6kMZC56jpUrJQZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "bfc7d2f7-70ef-437e-8eb3-5d89e825a6cb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex",
    "oldString": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages;",
    "newString": "\\citet{civelli2026shared} probe item difficulty using IRT-derived labels \\cite{lord1980irt} and report shared geometric structure across 7 languages;",
    "originalFile": "% Requires: \\usepackage{pifont} \\newcommand{\\cmark}{\\ding{51}} \\newcommand{\\xmark}{\\ding{55}}\n% Requires: \\usepackage{booktabs}\n\n\\section{Related Work}\n\n\\subsection{LLM Calibration and Internal Representations}\n\nPost-hoc calibration methods such as temperature scaling \\cite{guo2017calibration} and Platt scaling \\cite{niculescu2005predicting} treat model confidence as a scalar output to be recalibrated after training. These approaches assume access to a held-out validation set from the target distribution and operate entirely on output logits without inspecting internal representations.\nA complementary line of work examines whether models can self-assess correctness through verbalized confidence. \\citet{kadavath2022language} demonstrate that larger language models produce well-calibrated probability estimates when asked to evaluate their own answers, establishing that calibration information exists within the model prior to output generation.\n\nRecent studies shift attention from output-level calibration to representation-level probing. \\citet{miao2026closing} identify that correctness and verbalized confidence occupy nearly orthogonal subspaces in hidden states (cosine similarity below 0.04), suggesting that standard confidence elicitation fails to capture the full calibration signal. Building on this observation, CORAL \\cite{miao2026coral} trains correctness probes that transfer across tasks within English, achieving approximately 50\\% ECE improvement over verbalized confidence baselines. CCPS \\cite{khanmohammadi2025ccps} takes a complementary approach by measuring representation stability under input perturbations as a proxy for correctness. The Confidence Manifold framework \\cite{confidence_manifold2026} reveals that calibration-relevant information concentrates in a low-dimensional subspace (3 to 8 dimensions), with as few as 25 labeled examples sufficient for 89\\% probing accuracy. \\citet{ji2025calibrating} further demonstrate that verbal uncertainty in LLMs corresponds to a linear direction in representation space, while \\citet{joshi2025calibration} analyze how calibration signals evolve across layers, finding non-monotonic patterns that motivate layer selection.\n\nAll of these studies operate exclusively in English and on a single model architecture. Our work extends correctness probing to 20 languages across 2 model families, revealing that transfer quality varies substantially across languages and architectures.\n\n\\subsection{Cross-Lingual Probing and Transfer}\n\nCross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \\citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \\cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.\n\nThe technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \\cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \\cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages.\n\\citet{liu2025middle} show that middle layers of fine-tuned LLMs exhibit stronger cross-lingual alignment than early or late layers, consistent with the depth patterns we observe for correctness probes.\n\nOur work differs in three respects: we probe correctness (an output-dependent signal that requires generating and evaluating answers), we provide systematic depth analysis with Pareto frontier characterization across architectures, and we evaluate 5 transfer methods (including linear projection inspired by MUSE/VecMap) across 20 languages.\n\n\\subsection{Multilingual Calibration}\n\nCalibration quality varies dramatically across languages. \\citet{zhou2025lace} document a 5$\\times$ ECE gap between English and low-resource languages across 100+ languages and propose LACE, an adaptive layer ensemble that selects different layer combinations per language. While effective, LACE requires per-language validation data with correctness labels, limiting applicability to languages where such annotations exist.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Comparison with closely related work on calibration probing and cross-lingual transfer. Target signals: KB = knowledge boundary, Corr.\\ = correctness, Diff.\\ = difficulty. Zero-CL = zero target-language correctness labels required.}\n\\label{tab:related_work}\n\\begin{tabular}{lcccccc}\n\\toprule\n& \\textbf{Target} & \\textbf{\\# Langs} & \\textbf{Calib.} & \\textbf{Zero-CL} & \\textbf{Depth} & \\textbf{Transfer} \\\\\n& \\textbf{Signal} & & \\textbf{Metrics} & \\textbf{Labels} & \\textbf{Analysis} & \\textbf{Methods} \\\\\n\\midrule\nXiao et al. & KB & 8 & \\xmark & \\cmark & \\xmark & 1 \\\\\nLACE & -- & 100+ & \\cmark & \\xmark & partial & -- \\\\\nCORAL & Corr. & 1 & \\cmark & -- & \\cmark & 1 \\\\\nMiao \\& Ungar & Corr. & 1 & \\xmark & -- & \\xmark & -- \\\\\nCivelli et al. & Diff. & 7 & \\xmark & \\cmark & \\cmark & 1 \\\\\n\\midrule\n\\textbf{Ours} & \\textbf{Corr.} & \\textbf{20} & \\cmark & \\cmark & \\cmark & \\textbf{5} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe fundamental challenge that LACE addresses (per-language calibration heterogeneity) motivates our investigation, but our approach differs in both goal and mechanism. We analyze \\emph{why} cross-lingual transfer of correctness probes fails (architecture-dependent depth-transferability tradeoffs, geometric divergence measured by CKA) rather than engineering a per-language compensation. Our method requires zero target-language correctness labels, transferring probes trained on English data alone.\n\n\\subsection{Domain Adaptation Theory}\n\nThe theoretical framework of \\citet{bendavid2010theory} bounds target-domain error by source error plus a divergence term ($\\mathcal{H}$-divergence) between source and target distributions, plus a joint ideal error. Applied to cross-lingual probe transfer, this predicts degradation proportional to the representational distance between languages. \\citet{zhao2019invariant} prove a stronger negative result: when conditional distributions $P(Y|X)$ differ between domains, matching marginal distributions of representations can \\emph{increase} target error rather than reduce it.\n\nThis theoretical insight directly explains our empirical finding on CaCLR (Cross-lingual Calibration via Conditional Label-aware Representation matching). CaCLR applies MMD-based distributional matching to align probe logit distributions across languages. If distributional matching proves insufficient (pending experimental validation), this would align with the prediction of \\citet{zhao2019invariant}: because conditional accuracy distributions $P(\\text{correct}|\\mathbf{h})$ differ between languages (due to varying model competence), marginal alignment may destroy the conditional structure that probes rely on. Our CKA partial correlation analysis further reveals a Simpson's Paradox where aggregate cross-lingual similarity masks within-layer divergence, a confounding pattern that naive cross-layer pooling obscures.\n\n\\subsection{Probing Methodology and Evaluation}\n\nThe methodological foundations of representation probing inform our experimental design. \\citet{hewitt2019control} introduce control tasks that establish selectivity baselines, guarding against probes that succeed merely due to high capacity rather than genuine information in representations. \\citet{voita2020mdl} propose minimum description length probes as an information-theoretic alternative, measuring the amount of effort required to extract a property. \\citet{belinkov2022probing} surveys the broader landscape of probing classifiers, identifying best practices and common pitfalls including the capacity-informativeness tradeoff.\n\nWe apply the control task framework of \\citet{hewitt2019control} to cross-lingual correctness probing. English probing controls (Hewitt \\& Liang selectivity) reveal layer-dependent selectivity patterns, with selectivity concentrated in deeper layers (L20+) --- raising concerns that shallow-layer positive results in low-resource languages may partly reflect capacity artifacts rather than genuine correctness signal. Cross-lingual control experiments are planned to quantify this. For measuring representational similarity across languages and layers, we employ CKA \\cite{kornblith2019cka} with partial correlation analysis, revealing geometric structure invisible to standard pairwise comparisons. Conformal prediction \\cite{angelopoulos2023conformal} offers distribution-free coverage guarantees complementary to our probing approach but requires per-language calibration data, which our zero-correctness-label setting explicitly avoids.\n\nOur work contributes the first systematic application of probing controls to cross-lingual transfer evaluation and applies CKA with depth-controlled partial correlation as a diagnostic for understanding transfer failure modes.\n",
    "structuredPatch": [
      {
        "oldStart": 14,
        "oldLines": 7,
        "newStart": 14,
        "newLines": 7,
        "lines": [
          " ",
          " \\subsection{Cross-Lingual Probing and Transfer}",
          " ",
          "-Cross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \\citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \\citet{civelli2026shared} probe item difficulty using IRT-derived labels and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \\cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.",
          "+Cross-lingual probing investigates whether linguistic or behavioral properties encoded in one language's representations generalize to others. \\citet{xiao2025knowledge} probe knowledge boundaries across 8 languages and find partial cross-lingual transfer, but their target signal is answerability (an input-level property) rather than correctness (which depends on the model's actual output). \\citet{civelli2026shared} probe item difficulty using IRT-derived labels \\cite{lord1980irt} and report shared geometric structure across 7 languages; however, difficulty is a property of the question itself, independent of any particular model's response. DALI \\cite{ravisankar2026dali} provides causal evidence through activation patching that English middle-layer representations can repair errors in 24 non-English languages, confirming that transferable correctness information exists but not quantifying when and why transfer fails.",
          " ",
          " The technical foundations for cross-lingual alignment predate LLM-era probing. MUSE \\cite{conneau2018muse} established adversarial training for unsupervised bilingual word embedding alignment, while VecMap \\cite{artetxe2018vecmap} demonstrated that self-learning with structural similarity initialization achieves robust cross-lingual mappings without parallel data. Foundational cross-lingual transfer studies on multilingual BERT established that zero-shot transfer works surprisingly well between typologically similar languages \\cite{pires2019multilingual} and across diverse NLP tasks covering 39 languages \\cite{wu2019beto}, while XLM-RoBERTa \\cite{conneau2020xlmr} demonstrated that scaling unsupervised multilingual pretraining yields strong cross-lingual transfer across 100 languages.",
          " \\citet{liu2025middle} show that middle layers of fine-tuned LLMs exhibit stronger cross-lingual alignment than early or late layers, consistent with the depth patterns we observe for correctness probes."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 125_

Now let me also add the `fedus2022switch` citation. Let me check method.tex for a natural insertion point near the MoE model mention.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "10238657-f96e-4839-91cc-ff96094aa25f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JE9GtXPMtR1Tw9upGKDwC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 75613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 126_

<details open><summary>🔧 Tool call — Read · `toolu_015KaQazdyx1K9LHpHgajVZ3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
  "offset": 17,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "1e7ac1a2-00be-4f39-a926-99189b094109",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JE9GtXPMtR1Tw9upGKDwC7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 270,
      "cache_read_input_tokens": 75613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 270
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-21T07:41:52.394Z_

<details><summary>↩ Tool result · `toolu_015KaQazdyx1K9LHpHgajVZ3`</summary>

```text
17	\label{sec:framework}
18	
19	\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).
20	
21	\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \textsc{med} (ar, id, nl, pl, tr, uk, vi), and \textsc{low} (bn, hi, sw, te).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "5a0eb72c-b641-49e1-b9ea-b1fea042dc6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
      "content": "\\label{sec:framework}\n\n\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).\n\n\\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \\textsc{med} (ar, id, nl, pl, tr, uk, vi), and \\textsc{low} (bn, hi, sw, te).",
      "numLines": 5,
      "startLine": 17,
      "totalLines": 83
    }
  }
}
```

</details>

---

### Assistant

_source line 128_

<details><summary>Logged reasoning block</summary>

```text
Both Qwen3-235B-A22B and Llama 4 Scout 17B-16E are MoE (Mixture of Experts) architectures. The "A22B" in Qwen3-235B-A22B means 22B active parameters out of 235B total, and the "16E" in Llama 4 Scout 17B-16E means 16 experts. I could add a natural citation here. Let me add it to the Models paragraph.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "b3a2782a-c371-4efd-989a-f1873850e8e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLy1LegDB5shxvJx4xkXrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 75883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 129_

The Models paragraph mentions MoE architectures (Qwen3-235B-A22B and Llama 4 Scout 17B-16E). I'll insert the Switch Transformers citation there.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "41e3dad5-764d-4798-83ad-3b43cf18190d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLy1LegDB5shxvJx4xkXrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 75883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 130_

<details open><summary>🔧 Tool call — Edit · `toolu_01M181A1mfM1oqhLK94gYi6g`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
  "old_string": "\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).",
  "new_string": "\\paragraph{Models.} We evaluate two mixture-of-experts (MoE) architectures \\cite{fedus2022switch}: Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct as dense validation models (MVP)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e6b0b4ee-6413-4048-9237-0b22035badbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLy1LegDB5shxvJx4xkXrq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 75883,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-21T07:42:00.255Z_

<details><summary>↩ Tool result · `toolu_01M181A1mfM1oqhLK94gYi6g`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "af0ccf63-4b29-4db7-860e-0b0f53cc0559",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex",
    "oldString": "\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).",
    "newString": "\\paragraph{Models.} We evaluate two mixture-of-experts (MoE) architectures \\cite{fedus2022switch}: Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct as dense validation models (MVP).",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven a multilingual large language model (LLM) and a multiple-choice question-answering (MCQA) instance, we extract the post-layer-norm residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at layer $l$. A \\emph{correctness probe} is a linear classifier\n\\begin{equation}\n  f_l(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)\n  \\label{eq:probe}\n\\end{equation}\ntrained to predict $p(\\text{correct} \\mid \\mathbf{h}_l)$, the probability that the model's selected answer is correct. This target is output-dependent: it reflects the model's actual accuracy on each instance, not an intrinsic property of the input.\n\nWe distinguish correctness probing from two related tasks. \\emph{Knowledge boundary probing} \\citep{xiao2025knowledge} classifies whether a question is answerable, an input-level property independent of model output. \\emph{Difficulty probing} \\citep{civelli2026shared} predicts item difficulty as a language-agnostic question property via Item Response Theory (IRT). Our central question is whether an English-trained probe $f_l$ can transfer zero-shot to a target language $t$ without any target-language correctness labels (zero-correctness-label transfer), and which alignment strategies improve this transfer.\n\n\\subsection{Experimental Framework}\n\\label{sec:framework}\n\n\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).\n\n\\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \\textsc{med} (ar, id, nl, pl, tr, uk, vi), and \\textsc{low} (bn, hi, sw, te).\n\n\\paragraph{Data.} We use the GlobalMMLU test split, partitioned 70/30 via stratified sampling into \\texttt{probe\\_train} and \\texttt{eval} portions. English binary correctness labels come from \\texttt{probe\\_train} only; all reported results use \\texttt{eval} exclusively.\n\n\\paragraph{Activation extraction.} We register forward hooks on post-layer-norm residual stream outputs. Layers are sampled at regular intervals (every 4th layer plus the final layer for all models, yielding 8--25 probed layers depending on architecture depth). We use 4-bit quantization (GPTQ-Int4 for Qwen3, W4A16 for Llama 4 Scout) and include a higher-precision validation ablation at representative layers to control for quantization artifacts.\n\n\\paragraph{Metrics.} We report Area Under the ROC Curve (AUROC) for correctness discrimination, Soft-Binned ECE (SB-ECE) \\citep{karandikar2021sbece} for calibration quality, and selectivity \\citep{hewitt2019control}. Standard ECE (10-bin) and Brier score are reported in the Appendix. % [TO_ADD_BIB]\n\n\\subsection{Transfer Methods}\n\\label{sec:transfer}\n\nWe compare five methods ordered by complexity.\n\n\\paragraph{(a) Zero-shot transfer.} The English-trained probe $f_l$ is applied directly to target language representations without adaptation. This serves as the baseline for all comparisons.\n\n\\paragraph{(b) Mean-shift alignment.} We subtract the cross-lingual mean difference $\\boldsymbol{\\delta} = \\boldsymbol{\\mu}_{\\text{en}} - \\boldsymbol{\\mu}_t$ from target activations before applying the English probe.\n\n\\textbf{Rank-invariance proof.} Under the StandardScaler fitted on English training data, each dimension is normalized as $z_i = (h_i - \\mu_{\\text{en},i}) / \\sigma_{\\text{en},i}$. After mean-shift, the target representation becomes $h_i + \\delta_i$, and the scaled value is\n\\begin{equation}\n  z'_i = \\frac{h_i + \\delta_i - \\mu_{\\text{en},i}}{\\sigma_{\\text{en},i}} = z_i + c_i\n  \\label{eq:meanshift}\n\\end{equation}\nwhere $c_i = \\delta_i / \\sigma_{\\text{en},i}$ is a constant independent of the input sample. The probe logit then shifts by $\\mathbf{w}^\\top \\mathbf{c}$, a scalar applied identically to every sample. Because AUROC depends only on the ranking of predictions, this uniform offset leaves the ranking unchanged: $\\Delta\\text{AUROC} \\equiv 0$. Our MVP experiments confirm this prediction exactly ($\\Delta\\text{AUROC} = 0.000000$ across 5 languages $\\times$ all layers). ECE can change because binned probability values shift after the sigmoid transformation, but these changes are inconsistent across configurations and do not constitute reliable calibration improvement.\n\n\\paragraph{(c) Procrustes alignment.} We learn an orthogonal mapping from a small set of parallel sentence pairs by solving\n\\begin{equation}\n  \\mathbf{R}^* = \\arg\\min_{\\mathbf{R}^\\top\\mathbf{R}=\\mathbf{I}} \\|\\mathbf{X}_t\\mathbf{R} - \\mathbf{X}_{\\text{en}}\\|_F\n  \\label{eq:procrustes}\n\\end{equation}\nfollowing cross-lingual word embedding alignment methods such as MUSE \\citep{conneau2018muse} and VecMap \\citep{artetxe2018vecmap}. % [TO_ADD_BIB]\nApproximately 50 parallel pairs achieve 98\\% of 200-pair performance. Resource tier matters: \\textsc{high}-resource languages saturate at ${\\sim}$20 pairs and \\textsc{low}-resource at ${\\sim}$50. An effect reversal occurs at moderate transfer quality: Procrustes alignment helps when zero-shot AUROC $< 0.50$ but degrades performance when zero-shot AUROC $> 0.60$, which implies that alignment strategy must be conditioned on baseline transfer quality.\n\n\\paragraph{(d) Few-shot probe training.} We combine the full English training data with 25, 50, or 100 target-language labeled examples and retrain the probe. This requires target-language correctness labels and serves as an upper-bound reference.\n\n\\paragraph{(e) CaCLR (Calibration-aware Cross-Lingual Regularization).} CaCLR tests whether joint calibration and distributional matching can improve zero-correctness-label transfer. The objective combines three terms:\n\\begin{equation}\n  \\mathcal{L} = \\mathcal{L}_{\\text{BCE}} + \\alpha \\cdot \\mathcal{L}_{\\text{SB-ECE}} + \\beta \\cdot \\mathcal{L}_{\\text{consistency}}\n  \\label{eq:caclr}\n\\end{equation}\n$\\mathcal{L}_{\\text{BCE}}$ is standard binary cross-entropy on English \\texttt{probe\\_train} labels. $\\mathcal{L}_{\\text{SB-ECE}}$ is the differentiable Soft-Binned ECE (SB-ECE) of \\citet{karandikar2021sbece}, which replaces hard histogram bins with soft assignments to enable gradient-based calibration optimization. $\\mathcal{L}_{\\text{consistency}}$ is Maximum Mean Discrepancy (MMD) computed on \\emph{probe logits} from parallel English and target-language inputs. Operating on probe outputs (rather than raw activations) ensures gradient flow to probe parameters. For linear probes, the logit $\\mathbf{w}^\\top \\mathbf{h} + b$ is one-dimensional, so MMD operates in 1-D space; we discuss this design limitation in \\S\\ref{sec:discussion}. We use a Gaussian RBF kernel with bandwidth selected by the median heuristic. Parallel activations come from the GlobalMMLU \\texttt{probe\\_train} portion (70\\% of test split); no target-language correctness labels are required. The probe is initialized from the standard logistic regression solution (warm start) and optimized with Adam (learning rate $10^{-3}$). We apply early stopping based on English validation ECE. Both $\\alpha$ and $\\beta$ are swept across three orders of magnitude; batch size and epoch count are reported in the Appendix.\n\n\\subsection{Difficulty-Capability Decomposition}\n\\label{sec:decomposition}\n\nWe train IRT-based difficulty probes that predict question difficulty, a language-agnostic property independent of model capability. To isolate the capability-specific component, we project out the difficulty direction from each representation:\n\\begin{equation}\n  \\mathbf{h}_l^{\\text{res}} = \\mathbf{h}_l - (\\mathbf{h}_l \\cdot \\hat{\\mathbf{w}}_{\\text{diff}})\\hat{\\mathbf{w}}_{\\text{diff}}\n  \\label{eq:residual}\n\\end{equation}\nwhere $\\hat{\\mathbf{w}}_{\\text{diff}}$ is the unit-norm difficulty direction. We retrain correctness probes on the residual $\\mathbf{h}_l^{\\text{res}}$ and compare cross-lingual transfer. This decomposition yields a prescriptive signal: when the difficulty component dominates a language-layer combination, transfer should succeed because the underlying structure is shared across languages. When the capability component dominates, transfer should degrade because the encoding is language-specific.\n\n\\subsection{Geometric Analysis}\n\\label{sec:geometric}\n\nWe quantify cross-lingual representational similarity with Centered Kernel Alignment (CKA) \\citep{kornblith2019cka}. % [TO_ADD_BIB]\nThe central analysis applies partial correlation to control for layer depth, which reveals a Simpson's Paradox in the CKA-transfer relationship. The raw correlation between CKA and transfer AUROC across all language-layer pairs is negative, because both quantities covary with depth (deeper layers have lower CKA and, in some architectures, lower transfer AUROC). After controlling for depth, the partial correlation reverses sign: within each layer, higher cross-lingual CKA predicts better probe transfer (Llama pilot: $\\rho = +0.41$, $p = 0.006$; 14 of 17 layer-level correlations are positive (8 layers from Qwen2.5-7B + 9 layers from Llama-3.1-8B pilot models)). We report bootstrap confidence intervals (1000 resamples) for all partial correlations. We supplement CKA with subspace angle analysis that measures the cross-lingual angular distance between correctness directions $\\mathbf{w}_l$ at each layer. These results are framed as geometric and correlational analysis, not mechanistic explanation.\n\n\\subsection{Probing Controls}\n\\label{sec:controls}\n\nWe validate probe quality with the control task framework of \\citet{hewitt2019control}. % [TO_ADD_BIB]\nSelectivity is the gap between AUROC on true correctness labels and AUROC on randomly shuffled labels; higher selectivity indicates that the probe captures genuine task-relevant structure rather than exploiting representational capacity. We reduce activations to 100 dimensions via PCA before probe training to guard against high-dimensional overfitting, and report 5-fold cross-validated estimates. Pilot control task analysis on English (Qwen2.5-7B, 8 probed layers) shows selectivity concentrated in deeper layers: L20+ selectivity $> 0.20$, while shallow layers (L0--L12) show selectivity $< 0.05$, indicating that positive AUROC at shallow layers likely reflects capacity artifacts rather than genuine linguistic signal. Cross-lingual control experiments are planned to determine whether this pattern generalizes across target languages.\n",
    "structuredPatch": [
      {
        "oldStart": 16,
        "oldLines": 7,
        "newStart": 16,
        "newLines": 7,
        "lines": [
          " \\subsection{Experimental Framework}",
          " \\label{sec:framework}",
          " ",
          "-\\paragraph{Models.} We evaluate Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct for validation (MVP).",
          "+\\paragraph{Models.} We evaluate two mixture-of-experts (MoE) architectures \\cite{fedus2022switch}: Qwen3-235B-A22B (GPTQ-Int4) and Llama 4 Scout 17B-16E (W4A16) as primary architectures (P0), with Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct as dense validation models (MVP).",
          " ",
          " \\paragraph{Languages.} We test 20 languages (English as source, plus 19 target languages) spanning three resource tiers based on GlobalMMLU availability: \\textsc{high} (zh, de, es, fr, ja, ko, pt, ru), \\textsc{med} (ar, id, nl, pl, tr, uk, vi), and \\textsc{low} (bn, hi, sw, te).",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 132_

Let me verify the final state of all edited files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "0d3a790c-0979-4f3a-9784-2364141689cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkPJ1tpVHDLXbFzzE3W5Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 76364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 133_

<details open><summary>🔧 Tool call — Bash · `toolu_018DApgeXvmricevCn4rQQEf`</summary>

```json
{
  "command": "grep -c '@' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | head -1",
  "description": "Count bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "93341f35-4041-4b9e-b7f5-089907c80e5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkPJ1tpVHDLXbFzzE3W5Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 76364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-21T07:42:06.351Z_

<details><summary>↩ Tool result · `toolu_018DApgeXvmricevCn4rQQEf`</summary>

```text
36
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "92a15ab9-3ea1-4f1b-88d9-e960a6d426f9",
  "tool_use_result": {
    "stdout": "36",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 135_

<details open><summary>🔧 Tool call — Bash · `toolu_017JhoKuZgWTCwNxgfwRYQck`</summary>

```json
{
  "command": "grep -oP '\\\\cite\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
  "description": "Extract all cite keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "28c36543-d6cb-4204-8883-1647a2525d20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RkPJ1tpVHDLXbFzzE3W5Ce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 580,
      "cache_read_input_tokens": 76364,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 580
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-21T07:42:07.592Z_

<details><summary>↩ Tool result · `toolu_017JhoKuZgWTCwNxgfwRYQck`</summary>

```text
angelopoulos2023conformal
artetxe2018vecmap
confidence_manifold2026
conneau2018muse
conneau2020xlmr
fedus2022switch
guo2017calibration
khanmohammadi2025ccps
kornblith2019cka
lord1980irt
miao2026coral
niculescu2005predicting
pires2019multilingual
ravisankar2026dali
wu2019beto
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "67fec904-9206-4e89-967e-5a93af2c3ff9",
  "tool_use_result": {
    "stdout": "angelopoulos2023conformal\nartetxe2018vecmap\nconfidence_manifold2026\nconneau2018muse\nconneau2020xlmr\nfedus2022switch\nguo2017calibration\nkhanmohammadi2025ccps\nkornblith2019cka\nlord1980irt\nmiao2026coral\nniculescu2005predicting\npires2019multilingual\nravisankar2026dali\nwu2019beto",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 137_

<details><summary>Logged reasoning block</summary>

```text
Wait, that's only showing `\cite{}` references, not `\citet{}` references. Let me also check for `\citet{}` and `\citep{}` patterns.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "002ad0a1-21eb-4e55-b9b8-c9a3efdbffad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XyCJA91SMM9RhihGAk52d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 76944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 492
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 138_

<details open><summary>🔧 Tool call — Bash · `toolu_018SpDu4fbKZmVfJ51GFx5Vs`</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u",
  "description": "Extract all cite/citet/citep keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e6da31e4-8c40-4bc9-b2a8-43b18f80090c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011XyCJA91SMM9RhihGAk52d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 492,
      "cache_read_input_tokens": 76944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 492
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-21T07:42:12.214Z_

<details><summary>↩ Tool result · `toolu_018SpDu4fbKZmVfJ51GFx5Vs`</summary>

```text
angelopoulos2023conformal
artetxe2018vecmap
belinkov2022probing
bendavid2010theory
civelli2026shared
confidence_manifold2026
conneau2018muse
conneau2020xlmr
fedus2022switch
guo2017calibration
hewitt2019control
ji2025calibrating
joshi2025calibration
kadavath2022language
karandikar2021sbece
khanmohammadi2025ccps
kornblith2019cka
liu2025middle
lord1980irt
miao2026closing
miao2026coral
niculescu2005predicting
pires2019multilingual
ravisankar2026dali
voita2020mdl
wu2019beto
xiao2025knowledge
zhao2019invariant
zhou2025lace
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "a17cf05a-6422-431b-8f53-e1f7b38f4f86",
  "tool_use_result": {
    "stdout": "angelopoulos2023conformal\nartetxe2018vecmap\nbelinkov2022probing\nbendavid2010theory\ncivelli2026shared\nconfidence_manifold2026\nconneau2018muse\nconneau2020xlmr\nfedus2022switch\nguo2017calibration\nhewitt2019control\nji2025calibrating\njoshi2025calibration\nkadavath2022language\nkarandikar2021sbece\nkhanmohammadi2025ccps\nkornblith2019cka\nliu2025middle\nlord1980irt\nmiao2026closing\nmiao2026coral\nniculescu2005predicting\npires2019multilingual\nravisankar2026dali\nvoita2020mdl\nwu2019beto\nxiao2025knowledge\nzhao2019invariant\nzhou2025lace",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 140_

<details open><summary>🔧 Tool call — Bash · `toolu_01HxiVqe8ojEhqwUU3pcihCP`</summary>

```json
{
  "command": "grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u",
  "description": "Extract all bib keys from custom.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "4dbf4eeb-7d26-4e2f-b82c-da03be3e5c6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXCAHHfvLwjbvpxwDJeZ3w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 484,
      "cache_read_input_tokens": 77436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 484
      },
      "output_tokens": 44,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-21T07:42:16.063Z_

<details><summary>↩ Tool result · `toolu_01HxiVqe8ojEhqwUU3pcihCP`</summary>

```text
APA:83
Aho:72
Ando2005
Chandra:81
Gusfield:97
andrew2007scalable
angelopoulos2023conformal
artetxe2018vecmap
belinkov2022probing
bendavid2010theory
civelli2026shared
confidence_manifold2026
conneau2018muse
conneau2020xlmr
fedus2022switch
guo2017calibration
hewitt2019control
ji2025calibrating
joshi2025calibration
kadavath2022language
karandikar2021sbece
khanmohammadi2025ccps
kornblith2019cka
liu2025middle
lord1980irt
miao2026closing
miao2026coral
niculescu2005predicting
pires2019multilingual
rasooli-tetrault-2015
ravisankar2026dali
voita2020mdl
wu2019beto
xiao2025knowledge
zhao2019invariant
zhou2025lace
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "84fdf266-d26f-4cac-a1d0-802a1a4820bd",
  "tool_use_result": {
    "stdout": "APA:83\nAho:72\nAndo2005\nChandra:81\nGusfield:97\nandrew2007scalable\nangelopoulos2023conformal\nartetxe2018vecmap\nbelinkov2022probing\nbendavid2010theory\ncivelli2026shared\nconfidence_manifold2026\nconneau2018muse\nconneau2020xlmr\nfedus2022switch\nguo2017calibration\nhewitt2019control\nji2025calibrating\njoshi2025calibration\nkadavath2022language\nkarandikar2021sbece\nkhanmohammadi2025ccps\nkornblith2019cka\nliu2025middle\nlord1980irt\nmiao2026closing\nmiao2026coral\nniculescu2005predicting\npires2019multilingual\nrasooli-tetrault-2015\nravisankar2026dali\nvoita2020mdl\nwu2019beto\nxiao2025knowledge\nzhao2019invariant\nzhou2025lace",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 142_

<details open><summary>🔧 Tool call — Bash · `toolu_01FH4BVuQzJzD6VoBnpESSiV`</summary>

```json
{
  "command": "comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/method.tex 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u) <(grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u)",
  "description": "Find cite keys missing from bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "1489de0f-ca10-4aec-8ca1-cf50b1dc6add",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016QKAPLJ6Vc6x4PwmSkGdtY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 77920,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
      },
      "output_tokens": 56,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-21T07:42:21.144Z_

<details><summary>↩ Tool result · `toolu_01FH4BVuQzJzD6VoBnpESSiV`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "ced54d6e-c2b3-4684-9dbc-abf928e40053",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 144_

No missing cite keys — every `\cite` in `related_work.tex` and `method.tex` has a corresponding bib entry.

Let me also check the other tex files for any remaining missing citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "e34f0161-18ed-481c-b250-b5212e477d2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxbXXDywa5QeGfPHQbKxMg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 78337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 145_

<details open><summary>🔧 Tool call — Bash · `toolu_01BqSDPZPorbVnCEm9KthM7p`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/ -name '*.tex' -exec grep -oP '\\\\cite[tp]?\\{[^}]+\\}' {} + 2>/dev/null | grep -oP '\\{[^}]+\\}' | tr -d '{}' | tr ',' '\\n' | sort -u | comm -23 - <(grep -oP '@\\w+\\{([^,]+),' /home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/xling_calib_direction/docs/paper/custom.bib | grep -oP '\\{[^,]+' | tr -d '{' | sort -u)",
  "description": "Check all tex files for missing bib entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "3f103ebe-79c8-45cc-b69e-57b26ee74512",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxbXXDywa5QeGfPHQbKxMg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 78337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-21T07:42:26.916Z_

<details><summary>↩ Tool result · `toolu_01BqSDPZPorbVnCEm9KthM7p`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "c227db95-5216-44d9-910a-72601a508f2f",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 147_

Zero missing citations across all tex files.

**Summary of changes:**

**custom.bib** — Added 25 BibTeX entries:
- 11 classic papers (guo2017calibration, hewitt2019control, kornblith2019cka, pires2019multilingual, wu2019beto, voita2020mdl, karandikar2021sbece, belinkov2022probing, bendavid2010theory, zhao2019invariant, angelopoulos2023conformal)
- 11 recent 2025-2026 papers (xiao2025knowledge, zhou2025lace, miao2026closing, miao2026coral, khanmohammadi2025ccps, confidence_manifold2026, ji2025calibrating, joshi2025calibration, liu2025middle, ravisankar2026dali, civelli2026shared) — all verified via web search, no [TO_VERIFY] needed
- 3 newly added citations (conneau2020xlmr, lord1980irt, fedus2022switch)

**related_work.tex** — 2 insertions:
- `\cite{conneau2020xlmr}` in §Cross-Lingual Probing, after Pires/Wu&Dredze
- `\cite{lord1980irt}` next to Civelli's IRT-derived labels mention

**method.tex** — 1 insertion:
- `\cite{fedus2022switch}` in §Models paragraph, noting both primary models are MoE architectures

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "uuid": "372255a2-f5cd-4a90-aa8d-f7c3983e9c16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012cfWGPs1czZHbDH3veBwAk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 78647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 431
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 148_

Zero missing citations across all tex files.

**Summary of changes:**

**custom.bib** — Added 25 BibTeX entries:
- 11 classic papers (guo2017calibration, hewitt2019control, kornblith2019cka, pires2019multilingual, wu2019beto, voita2020mdl, karandikar2021sbece, belinkov2022probing, bendavid2010theory, zhao2019invariant, angelopoulos2023conformal)
- 11 recent 2025-2026 papers (xiao2025knowledge, zhou2025lace, miao2026closing, miao2026coral, khanmohammadi2025ccps, confidence_manifold2026, ji2025calibrating, joshi2025calibration, liu2025middle, ravisankar2026dali, civelli2026shared) — all verified via web search, no [TO_VERIFY] needed
- 3 newly added citations (conneau2020xlmr, lord1980irt, fedus2022switch)

**related_work.tex** — 2 insertions:
- `\cite{conneau2020xlmr}` in §Cross-Lingual Probing, after Pires/Wu&Dredze
- `\cite{lord1980irt}` next to Civelli's IRT-derived labels mention

**method.tex** — 1 insertion:
- `\cite{fedus2022switch}` in §Models paragraph, noting both primary models are MoE architectures

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 318593,
  "duration_api_ms": 499285,
  "num_turns": 58,
  "stop_reason": "end_turn",
  "session_id": "8711801c-2ab4-40fb-b538-cca7e7f4cc00",
  "total_cost_usd": 2.43918825,
  "usage": {
    "input_tokens": 6427,
    "cache_creation_input_tokens": 67237,
    "cache_read_input_tokens": 1359782,
    "output_tokens": 14719,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 67237,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 373,
        "cache_read_input_tokens": 78647,
        "cache_creation_input_tokens": 431,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 431
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 449861,
      "outputTokens": 13819,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 42,
      "costUSD": 0.9389559999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6427,
      "outputTokens": 14719,
      "cacheReadInputTokens": 1359782,
      "cacheCreationInputTokens": 67237,
      "webSearchRequests": 0,
      "costUSD": 1.5002322500000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1f3e2922-f23f-4d53-800d-f23e0d5c7d3a"
}
```

</details>

---
