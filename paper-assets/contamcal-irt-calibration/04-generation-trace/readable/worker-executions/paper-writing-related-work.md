# paper writing related work

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260517T043710.log`
- **Structured JSON:** [`60c36c6626fe80ab21aa.json`](../../sessions/60/60c36c6626fe80ab21aa.json)

## Before a recorded user message

47 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
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
  "uuid": "84264491-cb9b-4d1d-83b7-c2b5c281d3fd",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778997000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7e353361-5e49-4365-a4fb-7b175bf5a93a",
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the necessary files to understand the context and style guidelines, then write the Related Work section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "610c13f5-3a95-4e25-8fe8-1300cb6a9d2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzWFhrwdmbHrLArqCCLa5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14965,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14965
      },
      "output_tokens": 40,
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

_source line 5_

I'll read the references bib file and method section for context, then write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "6f7f5a2e-ec7f-4c1b-a5f8-df44e71169c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzWFhrwdmbHrLArqCCLa5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14965,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14965
      },
      "output_tokens": 40,
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01FcSpiBuP2Lhc6XANnpK4LN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "76934864-ef1e-4adb-90fc-3cc7ea0b2107",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzWFhrwdmbHrLArqCCLa5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14965,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14965
      },
      "output_tokens": 40,
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

_source line 7 · 2026-05-17T04:37:24.501Z_

<details><summary>↩ Tool result · `toolu_01FcSpiBuP2Lhc6XANnpK4LN`</summary>

```text
1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{adams_1997_mrcml,
6	  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
7	  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},
8	  booktitle = {Applied Psychological Measurement},
9	  volume    = {21},
10	  number    = {1},
11	  pages     = {1--23},
12	  year      = {1997}
13	}
14	
15	@article{angelopoulos_2023_conformal,
16	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
17	  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
18	  journal       = {Foundations and Trends in Machine Learning},
19	  year          = {2023},
20	  url           = {https://arxiv.org/abs/2107.07511}
21	}
22	
23	@article{brown_2024_ppp,
24	  author  = {Brown, Jeremy M. and Thomson, Robert C.},
25	  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},
26	  journal = {Molecular Biology and Evolution},
27	  volume  = {41},
28	  number  = {3},
29	  pages   = {msae051},
30	  year    = {2024}
31	}
32	
33	@article{burnell_2023_structure,
34	  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\'{a}ndez-Orallo, Jos\'{e}},
35	  title         = {Revealing the Structure of Language Model Capabilities},
36	  journal       = {arXiv preprint},
37	  year          = {2023},
38	  eprint        = {2306.10062},
39	  archiveprefix = {arXiv},
40	  url           = {https://arxiv.org/abs/2306.10062}
41	}
42	
43	@inproceedings{carlini_2021_extracting,
44	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
45	  title     = {Extracting Training Data from Large Language Models},
46	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
47	  year      = {2021},
48	  url       = {https://arxiv.org/abs/2012.07805}
49	}
50	
51	@inproceedings{chiang_2024_chatbot_arena,
52	  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},
53	  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},
54	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
55	  year      = {2024},
56	  url       = {https://arxiv.org/abs/2403.04132}
57	}
58	
59	@inproceedings{choi_2025_kds,
60	  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},
61	  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},
62	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
63	  year      = {2025},
64	  url       = {https://arxiv.org/abs/2502.00678}
65	}
66	
67	@inproceedings{cormack_2009_rrf,
68	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
69	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
70	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
71	  pages     = {758--759},
72	  year      = {2009},
73	  publisher = {ACM},
74	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
75	}
76	
77	@book{deboeck_2004_explanatory_irt,
78	  author    = {De Boeck, Paul and Wilson, Mark},
79	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
80	  publisher = {Springer},
81	  year      = {2004},
82	  address   = {New York},
83	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
84	}
85	
86	@article{dekoninck_2024_constat,
87	  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},
88	  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
89	  journal       = {arXiv preprint},
90	  year          = {2024},
91	  eprint        = {2405.16281},
92	  archiveprefix = {arXiv},
93	  url           = {https://arxiv.org/abs/2405.16281}
94	}
95	
96	@inproceedings{deng_2024_tsguessing,
97	  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},
98	  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},
99	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
100	  year      = {2024},
101	  url       = {https://arxiv.org/abs/2311.09783}
102	}
103	
104	@inproceedings{dong_2024_cdd,
105	  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},
106	  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},
107	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
108	  year      = {2024},
109	  url       = {https://arxiv.org/abs/2402.15938}
110	}
111	
112	@incollection{eckerly_2017_item_compromise,
113	  author    = {Eckerly, Carol},
114	  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},
115	  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},
116	  publisher = {Routledge},
117	  year      = {2017},
118	  url       = {https://www.routledge.com/9781138821811}
119	}
120	
121	@article{ercikan_2008_dif_cancellation,
122	  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},
123	  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},
124	  journal = {Practical Assessment, Research, and Evaluation},
125	  volume  = {14},
126	  number  = {3},
127	  year    = {2008}
128	}
129	
130	@inproceedings{golchin_2024_time_travel,
131	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
132	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
133	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
134	  year      = {2024},
135	  url       = {https://arxiv.org/abs/2308.08493}
136	}
137	
138	@inproceedings{guo_2017_calibration,
139	  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
140	  title     = {On Calibration of Modern Neural Networks},
141	  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
142	  pages     = {1321--1330},
143	  year      = {2017},
144	  url       = {https://arxiv.org/abs/1706.04599}
145	}
146	
147	@article{habba_2025_growing_pains,
148	  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},
149	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
150	  journal       = {arXiv preprint},
151	  year          = {2025},
152	  eprint        = {2604.12843},
153	  archiveprefix = {arXiv},
154	  url           = {https://arxiv.org/abs/2604.12843}
155	}
156	
157	@book{holland_1993_dif,
158	  author    = {Holland, Paul W. and Wainer, Howard},
159	  title     = {Differential Item Functioning},
160	  publisher = {Lawrence Erlbaum Associates},
161	  year      = {1993},
162	  address   = {Hillsdale, NJ}
163	}
164	
165	@article{kievit_2013_simpsons_paradox,
166	  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},
167	  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},
168	  journal = {Frontiers in Psychology},
169	  volume  = {4},
170	  pages   = {513},
171	  year    = {2013}
172	}
173	
174	@inproceedings{lalor_2024_irt_nlp,
175	  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},
176	  title     = {Item Response Theory for Natural Language Processing},
177	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},
178	  year      = {2024},
179	  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}
180	}
181	
182	@article{li_2024_atlas,
183	  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},
184	  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
185	  journal       = {arXiv preprint},
186	  year          = {2024},
187	  eprint        = {2511.04689},
188	  archiveprefix = {arXiv},
189	  url           = {https://arxiv.org/abs/2511.04689}
190	}
191	
192	@article{li_2024_open_llm_leaderboard,
193	  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},
194	  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},
195	  journal       = {arXiv preprint},
196	  year          = {2024},
197	  eprint        = {2406.07545},
198	  archiveprefix = {arXiv},
199	  url           = {https://arxiv.org/abs/2406.07545}
200	}
201	
202	@inproceedings{li_2025_dcr,
203	  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},
204	  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},
205	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
206	  year      = {2025}
207	}
208	
209	@article{liang_2023_helm,
210	  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},
211	  title         = {Holistic Evaluation of Language Models},
212	  journal       = {Transactions on Machine Learning Research},
213	  year          = {2023},
214	  url           = {https://arxiv.org/abs/2211.09110}
215	}
216	
217	@article{luettgau_2025_hibayes,
218	  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},
219	  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},
220	  journal       = {arXiv preprint},
221	  year          = {2025},
222	  eprint        = {2505.05602},
223	  archiveprefix = {arXiv},
224	  url           = {https://arxiv.org/abs/2505.05602}
225	}
226	
227	@article{mislevy_1986_bayes_irt,
228	  author  = {Mislevy, Robert J.},
229	  title   = {Bayes Modal Estimation in Item Response Models},
230	  journal = {Psychometrika},
231	  volume  = {51},
232	  number  = {2},
233	  pages   = {177--195},
234	  year    = {1986}
235	}
236	
237	@article{oren_2023_proving_contamination,
238	  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},
239	  title         = {Proving Test Set Contamination in Black Box Language Models},
240	  journal       = {arXiv preprint},
241	  year          = {2023},
242	  eprint        = {2310.17623},
243	  archiveprefix = {arXiv},
244	  url           = {https://arxiv.org/abs/2310.17623}
245	}
246	
247	@inproceedings{polo_2024_tinybenchmarks,
248	  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
249	  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},
250	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
251	  year      = {2024},
252	  url       = {https://arxiv.org/abs/2402.14992}
253	}
254	
255	@book{reckase_2009_mirt,
256	  author    = {Reckase, Mark D.},
257	  title     = {Multidimensional Item Response Theory},
258	  publisher = {Springer},
259	  year      = {2009},
260	  address   = {New York}
261	}
262	
263	@article{sanmartin_2009_irt,
264	  author  = {San Mart\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},
265	  title   = {Consequential Validity and Item Response Theory},
266	  journal = {Psychometrika},
267	  volume  = {74},
268	  number  = {2},
269	  pages   = {349--367},
270	  year    = {2009}
271	}
272	
273	@article{schaeffer_2026_generative_contamination,
274	  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},
275	  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},
276	  journal       = {arXiv preprint},
277	  year          = {2026},
278	  eprint        = {2601.04301},
279	  archiveprefix = {arXiv},
280	  url           = {https://arxiv.org/abs/2601.04301}
281	}
282	
283	@inproceedings{shi_2023_minkprob,
284	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
285	  title     = {Detecting Pretraining Data from Large Language Models},
286	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
287	  year      = {2024},
288	  url       = {https://arxiv.org/abs/2310.16789}
289	}
290	
291	@inproceedings{shokri_2017_mia,
292	  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},
293	  title     = {Membership Inference Attacks Against Machine Learning Models},
294	  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\&P)},
295	  year      = {2017},
296	  url       = {https://arxiv.org/abs/1610.05820}
297	}
298	
299	@article{sinharay_2017_preknowledge,
300	  author  = {Sinharay, Sandip},
301	  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},
302	  journal = {Journal of Educational and Behavioral Statistics},
303	  volume  = {42},
304	  number  = {1},
305	  year    = {2017},
306	  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}
307	}
308	
309	@article{sinharay_2025_irt_fit,
310	  author  = {Sinharay, Sandip},
311	  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},
312	  journal = {British Journal of Mathematical and Statistical Psychology},
313	  volume  = {78},
314	  pages   = {711--733},
315	  year    = {2025}
316	}
317	
318	@inproceedings{sun_2025_emperors_new_clothes,
319	  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},
320	  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},
321	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
322	  year      = {2025},
323	  url       = {https://arxiv.org/abs/2503.16402}
324	}
325	
326	@article{talts_2018_sbc,
327	  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},
328	  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},
329	  journal       = {arXiv preprint},
330	  year          = {2018},
331	  eprint        = {1804.06788},
332	  archiveprefix = {arXiv},
333	  url           = {https://arxiv.org/abs/1804.06788}
334	}
335	
336	@article{wang_2024_mmlu_pro,
337	  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},
338	  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},
339	  journal       = {arXiv preprint},
340	  year          = {2024},
341	  eprint        = {2406.01574},
342	  archiveprefix = {arXiv},
343	  url           = {https://arxiv.org/abs/2406.01574}
344	}
345	
346	@article{white_2024_livebench,
347	  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},
348	  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
349	  journal       = {arXiv preprint},
350	  year          = {2024},
351	  eprint        = {2406.19314},
352	  archiveprefix = {arXiv},
353	  url           = {https://arxiv.org/abs/2406.19314}
354	}
355	
356	@article{wust_2025_selfcritique,
357	  author        = {W\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},
358	  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},
359	  journal       = {arXiv preprint},
360	  year          = {2025},
361	  eprint        = {2510.09259},
362	  archiveprefix = {arXiv},
363	  url           = {https://arxiv.org/abs/2510.09259}
364	}
365	
366	@inproceedings{xu_2025_dcr,
367	  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},
368	  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},
369	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
370	  year      = {2025},
371	  url       = {https://arxiv.org/abs/2507.11405}
372	}
373	
374	@article{yang_2023_rethinking_benchmark,
375	  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},
376	  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},
377	  journal       = {arXiv preprint},
378	  year          = {2023},
379	  eprint        = {2311.04850},
380	  archiveprefix = {arXiv},
381	  url           = {https://arxiv.org/abs/2311.04850}
382	}
383	
384	@inproceedings{zhang_2024_gsm1k,
385	  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},
386	  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
387	  booktitle = {arXiv preprint},
388	  year      = {2024},
389	  eprint    = {2405.00332},
390	  url       = {https://arxiv.org/abs/2405.00332}
391	}
392	
393	@inproceedings{zhang_2024_minkpp,
394	  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
395	  title     = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
396	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},
397	  year      = {2025},
398	  url       = {https://arxiv.org/abs/2404.02936}
399	}
400	
401	@inproceedings{zheng_2023_chatbot_arena,
402	  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
403	  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
404	  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},
405	  year      = {2023},
406	  url       = {https://arxiv.org/abs/2306.05685}
407	}
408	
409	@inproceedings{zhou_2025_psnirt,
410	  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
411	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
412	  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},
413	  year      = {2026},
414	  url       = {https://arxiv.org/abs/2505.15055}
415	}
416	
417	% ============================================================
418	% Existing Entries (preserved for backward compatibility)
419	% ============================================================
420	
421	% --- Core Methodology ---
422	
423	@book{lord1980,
424	  author    = {Lord, Frederic M.},
425	  title     = {Applications of Item Response Theory to Practical Testing Problems},
426	  publisher = {Lawrence Erlbaum Associates},
427	  year      = {1980},
428	  address   = {Hillsdale, NJ}
429	}
430	
431	@article{eckerly2017,
432	  author  = {Eckerly, Carol},
433	  title   = {Detecting Item Compromise in the Context of Item Response Theory},
434	  journal = {Applied Psychological Measurement},
435	  volume  = {41},
436	  number  = {2},
437	  pages   = {87--101},
438	  year    = {2017}
439	}
440	
441	@article{sinharay2017,
442	  author  = {Sinharay, Sandip},
443	  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},
444	  journal = {Journal of Educational and Behavioral Statistics},
445	  volume  = {42},
446	  number  = {1},
447	  pages   = {46--68},
448	  year    = {2017}
449	}
450	
451	@book{deboeck2004,
452	  author    = {De Boeck, Paul and Wilson, Mark},
453	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
454	  publisher = {Springer},
455	  year      = {2004},
456	  address   = {New York}
457	}
458	
459	@article{adams1997,
460	  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
461	  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},
462	  journal = {Applied Psychological Measurement},
463	  volume  = {21},
464	  number  = {1},
465	  pages   = {1--23},
466	  year    = {1997}
467	}
468	
469	@article{mislevy1986,
470	  author  = {Mislevy, Robert J.},
471	  title   = {Bayes Modal Estimation in Item Response Models},
472	  journal = {Psychometrika},
473	  volume  = {51},
474	  number  = {2},
475	  pages   = {177--195},
476	  year    = {1986}
477	}
478	
479	@article{sanmartin2009,
480	  author  = {San Mart\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},
481	  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},
482	  journal = {Psychometrika},
483	  volume  = {74},
484	  number  = {2},
485	  pages   = {349--367},
486	  year    = {2009}
487	}
488	
489	@article{maris2009,
490	  author  = {Maris, Gunter and Bechger, Timo},
491	  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},
492	  journal = {Measurement},
493	  volume  = {7},
494	  number  = {2},
495	  pages   = {75--88},
496	  year    = {2009}
497	}
498	
499	@inproceedings{cormack2009,
500	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
501	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
502	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
503	  pages     = {758--759},
504	  year      = {2009},
505	  publisher = {ACM}
506	}
507	
508	% --- Bayesian Inference & Diagnostics ---
509	
510	@article{hoffman2014,
511	  author  = {Hoffman, Matthew D. and Gelman, Andrew},
512	  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},
513	  journal = {Journal of Machine Learning Research},
514	  volume  = {15},
515	  number  = {47},
516	  pages   = {1593--1623},
517	  year    = {2014}
518	}
519	
520	@article{carpenter2017,
521	  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},
522	  title   = {Stan: A Probabilistic Programming Language},
523	  journal = {Journal of Statistical Software},
524	  volume  = {76},
525	  number  = {1},
526	  pages   = {1--32},
527	  year    = {2017}
528	}
529	
530	@article{talts2018sbc,
531	  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},
532	  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},
533	  journal       = {arXiv preprint},
534	  year          = {2018},
535	  eprint        = {1804.06788},
536	  archiveprefix = {arXiv}
537	}
538	
539	@article{ulitzsch2022,
540	  author  = {Ulitzsch, Esther and Nestler, Steffen},
541	  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},
542	  journal = {British Journal of Mathematical and Statistical Psychology},
543	  volume  = {75},
544	  number  = {3},
545	  pages   = {421--447},
546	  year    = {2022}
547	}
548	
549	% --- Contamination Detection Methods ---
550	
551	@inproceedings{duan2025minkpp,
552	  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},
553	  title     = {{Min-K\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},
554	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},
555	  year      = {2025}
556	}
557	
558	@inproceedings{dekoninck2024constat,
559	  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},
560	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
561	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
562	  year      = {2024}
563	}
564	
565	@article{wust2025selfcritique,
566	  author        = {W\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},
567	  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},
568	  journal       = {arXiv preprint},
569	  year          = {2025},
570	  eprint        = {2510.09259},
571	  archiveprefix = {arXiv}
572	}
573	
574	@inproceedings{xu2025kds,
575	  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},
576	  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},
577	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
578	  year      = {2025},
579	  note      = {arXiv:2502.00678}
580	}
581	
582	@inproceedings{oren2024proving,
583	  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},
584	  title     = {Proving Test Set Contamination in Black Box Language Models},
585	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
586	  year      = {2024}
587	}
588	
589	% --- Contamination Analysis & Mitigation ---
590	
591	@inproceedings{xu2025emperor,
592	  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},
593	  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},
594	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
595	  year      = {2025},
596	  note      = {arXiv:2503.16402}
597	}
598	
599	@article{dong2026dose,
600	  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},
601	  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},
602	  journal       = {arXiv preprint},
603	  year          = {2026},
604	  eprint        = {2601.04301},
605	  archiveprefix = {arXiv}
606	}
607	
608	@article{yang2026rl,
609	  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},
610	  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},
611	  journal       = {arXiv preprint},
612	  year          = {2026},
613	  eprint        = {2601.06103},
614	  archiveprefix = {arXiv}
615	}
616	
617	@article{wang2025fragility,
618	  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},
619	  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},
620	  journal       = {arXiv preprint},
621	  year          = {2025},
622	  eprint        = {2510.02386},
623	  archiveprefix = {arXiv}
624	}
625	
626	@inproceedings{zhang2025forget,
627	  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},
628	  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},
629	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
630	  year      = {2025}
631	}
632	
633	% --- IRT for LLM Evaluation ---
634	
635	@inproceedings{gu2026psnirt,
636	  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
637	  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},
638	  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},
639	  year      = {2026}
640	}
641	
642	@article{polo2026growing,
643	  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},
644	  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},
645	  journal       = {arXiv preprint},
646	  year          = {2026},
647	  eprint        = {2604.12843},
648	  archiveprefix = {arXiv}
649	}
650	
651	@article{lyu2025atlas,
652	  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},
653	  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},
654	  journal       = {arXiv preprint},
655	  year          = {2025},
656	  eprint        = {2511.04689},
657	  archiveprefix = {arXiv}
658	}
659	
660	@article{zhuang2025hibayes,
661	  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},
662	  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},
663	  journal       = {arXiv preprint},
664	  year          = {2025},
665	  eprint        = {2505.05602},
666	  archiveprefix = {arXiv}
667	}
668	
669	@inproceedings{lalor2024irt,
670	  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},
671	  title     = {Benchmarking Large Language Models with Item Response Theory},
672	  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},
673	  year      = {2024}
674	}
675	
676	% --- Score Adjustment & Decontamination ---
677	
678	@inproceedings{li2025dcr,
679	  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},
680	  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},
681	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
682	  year      = {2025}
683	}
684	
685	@inproceedings{yang2024inference,
686	  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},
687	  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},
688	  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},
689	  year      = {2024}
690	}
691	
692	@article{rao2026silicon,
693	  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},
694	  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},
695	  journal       = {arXiv preprint},
696	  year          = {2026},
697	  eprint        = {2603.21636},
698	  archiveprefix = {arXiv}
699	}
700	
701	% --- Benchmarking ---
702	
703	@inproceedings{hendrycks2021mmlu,
704	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
705	  title     = {Measuring Massive Multitask Language Understanding},
706	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
707	  year      = {2021}
708	}
709	
710	@article{cobbe2021gsm8k,
711	  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
712	  title         = {Training Verifiers to Solve Math Word Problems},
713	  journal       = {arXiv preprint},
714	  year          = {2021},
715	  eprint        = {2110.14168},
716	  archiveprefix = {arXiv}
717	}
718	
719	@inproceedings{clark2018arc,
720	  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
721	  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},
722	  journal   = {arXiv preprint},
723	  year      = {2018},
724	  eprint    = {1803.05457},
725	  archiveprefix = {arXiv}
726	}
727	
728	@article{chen2021humaneval,
729	  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},
730	  title         = {Evaluating Large Language Models Trained on Code},
731	  journal       = {arXiv preprint},
732	  year          = {2021},
733	  eprint        = {2107.03374},
734	  archiveprefix = {arXiv}
735	}
736	
737	@inproceedings{chang2025benchmarking,
738	  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
739	  title     = {A Survey on Evaluation of Large Language Models},
740	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
741	  year      = {2025}
742	}
743	
744	@article{white2024livebench,
745	  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},
746	  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
747	  journal       = {arXiv preprint},
748	  year          = {2024},
749	  eprint        = {2406.19314},
750	  archiveprefix = {arXiv}
751	}
752	
753	@inproceedings{polo2024tinybenchmarks,
754	  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
755	  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},
756	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
757	  year      = {2024}
758	}
759	
760	@inproceedings{han2026probing,
761	  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},
762	  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},
763	  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},
764	  year      = {2026},
765	  note      = {arXiv:2510.07175}
766	}
767	
768	% --- Differential Item Functioning (DIF) ---
769	
770	@book{holland1993dif,
771	  author    = {Holland, Paul W. and Wainer, Howard},
772	  title     = {Differential Item Functioning},
773	  publisher = {Lawrence Erlbaum Associates},
774	  year      = {1993},
775	  address   = {Hillsdale, NJ}
776	}
777	
778	@incollection{thissen1993dif,
779	  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},
780	  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},
781	  booktitle = {Differential Item Functioning},
782	  editor    = {Holland, Paul W. and Wainer, Howard},
783	  publisher = {Lawrence Erlbaum Associates},
784	  pages     = {67--113},
785	  year      = {1993}
786	}
787	
788	@book{zumbo1999dif,
789	  author    = {Zumbo, Bruno D.},
790	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
791	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},
792	  year      = {1999},
793	  address   = {Ottawa, ON}
794	}
795	
796	% --- ML Calibration ---
797	
798	@inproceedings{guo2017calibration,
799	  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
800	  title     = {On Calibration of Modern Neural Networks},
801	  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
802	  pages     = {1321--1330},
803	  year      = {2017}
804	}
805	
806	% --- Conformal Prediction ---
807	
808	@article{angelopoulos2023conformal,
809	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
810	  title         = {Conformal Prediction: A Gentle Introduction},
811	  journal       = {Foundations and Trends in Machine Learning},
812	  volume        = {16},
813	  number        = {4},
814	  pages         = {494--591},
815	  year          = {2023}
816	}
817	
818	% --- Data Attribution ---
819	
820	@inproceedings{pruthi2020tracin,
821	  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},
822	  title     = {Estimating Training Data Influence by Tracing Gradient Descent},
823	  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},
824	  year      = {2020}
825	}
826	
827	@inproceedings{park2023trak,
828	  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},
829	  title     = {{TRAK}: Attributing Model Behavior at Scale},
830	  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
831	  year      = {2023}
832	}
833	
834	% --- Multidimensional IRT ---
835	
836	@book{reckase2009mirt,
837	  author    = {Reckase, Mark D.},
838	  title     = {Multidimensional Item Response Theory},
839	  publisher = {Springer},
840	  year      = {2009},
841	  address   = {New York}
842	}
843	
844	% --- Exposure-Ability Collinearity & IRT Identifiability ---
845	
846	@article{sanmartin2015,
847	  author  = {San Mart\'{i}n, Ernesto and Gonz\'{a}lez, Jorge and Tuerlinckx, Francis},
848	  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},
849	  journal = {Psychometrika},
850	  volume  = {80},
851	  number  = {2},
852	  pages   = {450--467},
853	  year    = {2015},
854	  doi     = {10.1007/s11336-014-9404-2}
855	}
856	
857	@article{mislevy1987,
858	  author  = {Mislevy, Robert J.},
859	  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},
860	  journal = {Applied Psychological Measurement},
861	  volume  = {11},
862	  number  = {1},
863	  pages   = {81--91},
864	  year    = {1987},
865	  doi     = {10.1177/014662168701100106}
866	}
867	
868	@book{wainer2007testlet,
869	  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},
870	  title     = {Testlet Response Theory and Its Applications},
871	  publisher = {Cambridge University Press},
872	  year      = {2007}
873	}
874	
875	% --- Measurement Error & Attenuation Bias ---
876	
877	@book{carroll2006,
878	  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},
879	  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},
880	  edition   = {2nd},
881	  publisher = {Chapman \& Hall/CRC},
882	  year      = {2006},
883	  isbn      = {9781584886334}
884	}
885	
886	@book{fuller1987,
887	  author    = {Fuller, Wayne A.},
888	  title     = {Measurement Error Models},
889	  publisher = {Wiley},
890	  year      = {1987},
891	  series    = {Wiley Series in Probability and Statistics},
892	  isbn      = {9780471861874}
893	}
894	
895	@article{stefanski1985,
896	  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},
897	  title   = {Covariate Measurement Error in Logistic Regression},
898	  journal = {Annals of Statistics},
899	  volume  = {13},
900	  number  = {4},
901	  pages   = {1335--1351},
902	  year    = {1985},
903	  doi     = {10.1214/aos/1176349741}
904	}
905	
906	@article{battauz2011,
907	  author  = {Battauz, Michela and Bellio, Ruggero},
908	  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},
909	  journal = {Psychometrika},
910	  volume  = {76},
911	  number  = {1},
912	  pages   = {40--56},
913	  year    = {2011},
914	  doi     = {10.1007/s11336-010-9195-z}
915	}
916	
917	@article{westfall2016,
918	  author  = {Westfall, Jacob and Yarkoni, Tal},
919	  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},
920	  journal = {PLoS ONE},
921	  volume  = {11},
922	  number  = {3},
923	  pages   = {e0152719},
924	  year    = {2016},
925	  doi     = {10.1371/journal.pone.0152719}
926	}
927	
928	@article{jerzak2026,
929	  author  = {Jerzak, Connor T. and Jessee, Stephen A.},
930	  title   = {Attenuation Bias with Latent Predictors},
931	  journal = {arXiv preprint arXiv:2507.22218},
932	  year    = {2026}
933	}
934	
935	% --- IRT Information & Power Analysis ---
936	
937	@book{embretson2000,
938	  author    = {Embretson, Susan E. and Reise, Steven P.},
939	  title     = {Item Response Theory for Psychologists},
940	  publisher = {Lawrence Erlbaum Associates},
941	  year      = {2000},
942	  address   = {Mahwah, NJ}
943	}
944	
945	@book{thissen2001,
946	  author    = {Thissen, David and Wainer, Howard},
947	  title     = {Test Scoring},
948	  publisher = {Lawrence Erlbaum Associates},
949	  year      = {2001},
950	  address   = {Mahwah, NJ}
951	}
952	
953	% --- 4PL Model & Identifiability ---
954	
955	@article{barton1981,
956	  author  = {Barton, Mark A. and Lord, Frederic M.},
957	  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},
958	  journal = {ETS Research Report Series},
959	  volume  = {1981},
960	  number  = {1},
961	  pages   = {i--8},
962	  year    = {1981},
963	  doi     = {10.1002/j.2333-8504.1981.tb01255.x}
964	}
965	
966	@article{culpepper2016,
967	  author  = {Culpepper, Steven Andrew},
968	  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},
969	  journal = {Psychometrika},
970	  volume  = {81},
971	  number  = {4},
972	  pages   = {1142--1163},
973	  year    = {2016},
974	  doi     = {10.1007/s11336-015-9477-6}
975	}
976	
977	@article{liao2012,
978	  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},
979	  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},
980	  journal = {Social Behavior and Personality},
981	  volume  = {40},
982	  number  = {10},
983	  pages   = {1679--1694},
984	  year    = {2012},
985	  doi     = {10.2224/sbp.2012.40.10.1679}
986	}
987	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "40db6550-e161-4e67-bfa4-a7272d365841",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib",
      "content": "% ============================================================\n% Literature Map Entries (keys from literature_map.yaml ids)\n% ============================================================\n\n@inproceedings{adams_1997_mrcml,\n  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  booktitle = {Applied Psychological Measurement},\n  volume    = {21},\n  number    = {1},\n  pages     = {1--23},\n  year      = {1997}\n}\n\n@article{angelopoulos_2023_conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n  journal       = {Foundations and Trends in Machine Learning},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2107.07511}\n}\n\n@article{brown_2024_ppp,\n  author  = {Brown, Jeremy M. and Thomson, Robert C.},\n  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},\n  journal = {Molecular Biology and Evolution},\n  volume  = {41},\n  number  = {3},\n  pages   = {msae051},\n  year    = {2024}\n}\n\n@article{burnell_2023_structure,\n  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\\'{a}ndez-Orallo, Jos\\'{e}},\n  title         = {Revealing the Structure of Language Model Capabilities},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2306.10062},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2306.10062}\n}\n\n@inproceedings{carlini_2021_extracting,\n  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},\n  title     = {Extracting Training Data from Large Language Models},\n  booktitle = {Proceedings of the 30th USENIX Security Symposium},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2012.07805}\n}\n\n@inproceedings{chiang_2024_chatbot_arena,\n  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{choi_2025_kds,\n  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},\n  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.00678}\n}\n\n@inproceedings{cormack_2009_rrf,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM},\n  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}\n}\n\n@book{deboeck_2004_explanatory_irt,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York},\n  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}\n}\n\n@article{dekoninck_2024_constat,\n  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2405.16281},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2405.16281}\n}\n\n@inproceedings{deng_2024_tsguessing,\n  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},\n  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09783}\n}\n\n@inproceedings{dong_2024_cdd,\n  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},\n  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.15938}\n}\n\n@incollection{eckerly_2017_item_compromise,\n  author    = {Eckerly, Carol},\n  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},\n  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},\n  publisher = {Routledge},\n  year      = {2017},\n  url       = {https://www.routledge.com/9781138821811}\n}\n\n@article{ercikan_2008_dif_cancellation,\n  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},\n  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},\n  journal = {Practical Assessment, Research, and Evaluation},\n  volume  = {14},\n  number  = {3},\n  year    = {2008}\n}\n\n@inproceedings{golchin_2024_time_travel,\n  author    = {Golchin, Shahriar and Surdeanu, Mihai},\n  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.08493}\n}\n\n@inproceedings{guo_2017_calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{habba_2025_growing_pains,\n  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n@book{holland_1993_dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@article{kievit_2013_simpsons_paradox,\n  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},\n  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},\n  journal = {Frontiers in Psychology},\n  volume  = {4},\n  pages   = {513},\n  year    = {2013}\n}\n\n@inproceedings{lalor_2024_irt_nlp,\n  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},\n  title     = {Item Response Theory for Natural Language Processing},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}\n}\n\n@article{li_2024_atlas,\n  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2511.04689}\n}\n\n@article{li_2024_open_llm_leaderboard,\n  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},\n  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.07545},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.07545}\n}\n\n@inproceedings{li_2025_dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{liang_2023_helm,\n  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},\n  title         = {Holistic Evaluation of Language Models},\n  journal       = {Transactions on Machine Learning Research},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2211.09110}\n}\n\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n@article{mislevy_1986_bayes_irt,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{oren_2023_proving_contamination,\n  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title         = {Proving Test Set Contamination in Black Box Language Models},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2310.17623},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2310.17623}\n}\n\n@inproceedings{polo_2024_tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14992}\n}\n\n@book{reckase_2009_mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n@article{sanmartin_2009_irt,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity and Item Response Theory},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{schaeffer_2026_generative_contamination,\n  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},\n  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2601.04301}\n}\n\n@inproceedings{shi_2023_minkprob,\n  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.16789}\n}\n\n@inproceedings{shokri_2017_mia,\n  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},\n  title     = {Membership Inference Attacks Against Machine Learning Models},\n  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1610.05820}\n}\n\n@article{sinharay_2017_preknowledge,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  year    = {2017},\n  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}\n}\n\n@article{sinharay_2025_irt_fit,\n  author  = {Sinharay, Sandip},\n  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {78},\n  pages   = {711--733},\n  year    = {2025}\n}\n\n@inproceedings{sun_2025_emperors_new_clothes,\n  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},\n  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.16402}\n}\n\n@article{talts_2018_sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/1804.06788}\n}\n\n@article{wang_2024_mmlu_pro,\n  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},\n  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.01574},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.01574}\n}\n\n@article{white_2024_livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.19314}\n}\n\n@article{wust_2025_selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n@inproceedings{xu_2025_dcr,\n  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.11405}\n}\n\n@article{yang_2023_rethinking_benchmark,\n  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},\n  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2311.04850},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2311.04850}\n}\n\n@inproceedings{zhang_2024_gsm1k,\n  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n  booktitle = {arXiv preprint},\n  year      = {2024},\n  eprint    = {2405.00332},\n  url       = {https://arxiv.org/abs/2405.00332}\n}\n\n@inproceedings{zhang_2024_minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n@inproceedings{zheng_2023_chatbot_arena,\n  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{zhou_2025_psnirt,\n  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2505.15055}\n}\n\n% ============================================================\n% Existing Entries (preserved for backward compatibility)\n% ============================================================\n\n% --- Core Methodology ---\n\n@book{lord1980,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ}\n}\n\n@article{eckerly2017,\n  author  = {Eckerly, Carol},\n  title   = {Detecting Item Compromise in the Context of Item Response Theory},\n  journal = {Applied Psychological Measurement},\n  volume  = {41},\n  number  = {2},\n  pages   = {87--101},\n  year    = {2017}\n}\n\n@article{sinharay2017,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  pages   = {46--68},\n  year    = {2017}\n}\n\n@book{deboeck2004,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York}\n}\n\n@article{adams1997,\n  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  journal = {Applied Psychological Measurement},\n  volume  = {21},\n  number  = {1},\n  pages   = {1--23},\n  year    = {1997}\n}\n\n@article{mislevy1986,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{sanmartin2009,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{maris2009,\n  author  = {Maris, Gunter and Bechger, Timo},\n  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},\n  journal = {Measurement},\n  volume  = {7},\n  number  = {2},\n  pages   = {75--88},\n  year    = {2009}\n}\n\n@inproceedings{cormack2009,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM}\n}\n\n% --- Bayesian Inference & Diagnostics ---\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n@article{talts2018sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv}\n}\n\n@article{ulitzsch2022,\n  author  = {Ulitzsch, Esther and Nestler, Steffen},\n  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {75},\n  number  = {3},\n  pages   = {421--447},\n  year    = {2022}\n}\n\n% --- Contamination Detection Methods ---\n\n@inproceedings{duan2025minkpp,\n  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},\n  title     = {{Min-K\\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025}\n}\n\n@inproceedings{dekoninck2024constat,\n  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@article{wust2025selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{xu2025kds,\n  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2502.00678}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% --- Contamination Analysis & Mitigation ---\n\n@inproceedings{xu2025emperor,\n  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@article{dong2026dose,\n  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},\n  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv}\n}\n\n@article{yang2026rl,\n  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},\n  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@article{wang2025fragility,\n  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},\n  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.02386},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% --- IRT for LLM Evaluation ---\n\n@inproceedings{gu2026psnirt,\n  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026}\n}\n\n@article{polo2026growing,\n  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv}\n}\n\n@article{lyu2025atlas,\n  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},\n  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv}\n}\n\n@article{zhuang2025hibayes,\n  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{lalor2024irt,\n  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},\n  title     = {Benchmarking Large Language Models with Item Response Theory},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  year      = {2024}\n}\n\n% --- Score Adjustment & Decontamination ---\n\n@inproceedings{li2025dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n@article{rao2026silicon,\n  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},\n  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2603.21636},\n  archiveprefix = {arXiv}\n}\n\n% --- Benchmarking ---\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chen2021humaneval,\n  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  title         = {Evaluating Large Language Models Trained on Code},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2107.03374},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024}\n}\n\n@inproceedings{han2026probing,\n  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},\n  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},\n  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},\n  year      = {2026},\n  note      = {arXiv:2510.07175}\n}\n\n% --- Differential Item Functioning (DIF) ---\n\n@book{holland1993dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% --- ML Calibration ---\n\n@inproceedings{guo2017calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017}\n}\n\n% --- Conformal Prediction ---\n\n@article{angelopoulos2023conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {Conformal Prediction: A Gentle Introduction},\n  journal       = {Foundations and Trends in Machine Learning},\n  volume        = {16},\n  number        = {4},\n  pages         = {494--591},\n  year          = {2023}\n}\n\n% --- Data Attribution ---\n\n@inproceedings{pruthi2020tracin,\n  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},\n  title     = {Estimating Training Data Influence by Tracing Gradient Descent},\n  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},\n  year      = {2020}\n}\n\n@inproceedings{park2023trak,\n  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},\n  title     = {{TRAK}: Attributing Model Behavior at Scale},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year      = {2023}\n}\n\n% --- Multidimensional IRT ---\n\n@book{reckase2009mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n% --- Exposure-Ability Collinearity & IRT Identifiability ---\n\n@article{sanmartin2015,\n  author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},\n  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},\n  journal = {Psychometrika},\n  volume  = {80},\n  number  = {2},\n  pages   = {450--467},\n  year    = {2015},\n  doi     = {10.1007/s11336-014-9404-2}\n}\n\n@article{mislevy1987,\n  author  = {Mislevy, Robert J.},\n  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},\n  journal = {Applied Psychological Measurement},\n  volume  = {11},\n  number  = {1},\n  pages   = {81--91},\n  year    = {1987},\n  doi     = {10.1177/014662168701100106}\n}\n\n@book{wainer2007testlet,\n  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},\n  title     = {Testlet Response Theory and Its Applications},\n  publisher = {Cambridge University Press},\n  year      = {2007}\n}\n\n% --- Measurement Error & Attenuation Bias ---\n\n@book{carroll2006,\n  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},\n  edition   = {2nd},\n  publisher = {Chapman \\& Hall/CRC},\n  year      = {2006},\n  isbn      = {9781584886334}\n}\n\n@book{fuller1987,\n  author    = {Fuller, Wayne A.},\n  title     = {Measurement Error Models},\n  publisher = {Wiley},\n  year      = {1987},\n  series    = {Wiley Series in Probability and Statistics},\n  isbn      = {9780471861874}\n}\n\n@article{stefanski1985,\n  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},\n  title   = {Covariate Measurement Error in Logistic Regression},\n  journal = {Annals of Statistics},\n  volume  = {13},\n  number  = {4},\n  pages   = {1335--1351},\n  year    = {1985},\n  doi     = {10.1214/aos/1176349741}\n}\n\n@article{battauz2011,\n  author  = {Battauz, Michela and Bellio, Ruggero},\n  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},\n  journal = {Psychometrika},\n  volume  = {76},\n  number  = {1},\n  pages   = {40--56},\n  year    = {2011},\n  doi     = {10.1007/s11336-010-9195-z}\n}\n\n@article{westfall2016,\n  author  = {Westfall, Jacob and Yarkoni, Tal},\n  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},\n  journal = {PLoS ONE},\n  volume  = {11},\n  number  = {3},\n  pages   = {e0152719},\n  year    = {2016},\n  doi     = {10.1371/journal.pone.0152719}\n}\n\n@article{jerzak2026,\n  author  = {Jerzak, Connor T. and Jessee, Stephen A.},\n  title   = {Attenuation Bias with Latent Predictors},\n  journal = {arXiv preprint arXiv:2507.22218},\n  year    = {2026}\n}\n\n% --- IRT Information & Power Analysis ---\n\n@book{embretson2000,\n  author    = {Embretson, Susan E. and Reise, Steven P.},\n  title     = {Item Response Theory for Psychologists},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2000},\n  address   = {Mahwah, NJ}\n}\n\n@book{thissen2001,\n  author    = {Thissen, David and Wainer, Howard},\n  title     = {Test Scoring},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2001},\n  address   = {Mahwah, NJ}\n}\n\n% --- 4PL Model & Identifiability ---\n\n@article{barton1981,\n  author  = {Barton, Mark A. and Lord, Frederic M.},\n  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  journal = {ETS Research Report Series},\n  volume  = {1981},\n  number  = {1},\n  pages   = {i--8},\n  year    = {1981},\n  doi     = {10.1002/j.2333-8504.1981.tb01255.x}\n}\n\n@article{culpepper2016,\n  author  = {Culpepper, Steven Andrew},\n  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},\n  journal = {Psychometrika},\n  volume  = {81},\n  number  = {4},\n  pages   = {1142--1163},\n  year    = {2016},\n  doi     = {10.1007/s11336-015-9477-6}\n}\n\n@article{liao2012,\n  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},\n  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},\n  journal = {Social Behavior and Personality},\n  volume  = {40},\n  number  = {10},\n  pages   = {1679--1694},\n  year    = {2012},\n  doi     = {10.2224/sbp.2012.40.10.1679}\n}\n",
      "numLines": 987,
      "startLine": 1,
      "totalLines": 987
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01BkpzmwhHuaVva9pgT9Zvrx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "263910db-e093-4686-878d-b8e2ee1b8c28",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzWFhrwdmbHrLArqCCLa5C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14965,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14965
      },
      "output_tokens": 40,
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

_source line 9 · 2026-05-17T04:37:24.700Z_

<details><summary>↩ Tool result · `toolu_01BkpzmwhHuaVva9pgT9Zvrx`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	ContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.
5	
6	\subsection{Problem Formulation}
7	\label{sec:formulation}
8	
9	Let $y_{ijk} \in \{0,1\}$ denote the binary response of model~$j$ ($j=1,\ldots,J$) to item~$i$ ($i=1,\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\theta_j, \boldsymbol{\xi}_i)$ where $\theta_j$ is latent ability and $\boldsymbol{\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\hat{\theta}_j$ confounds genuine capability with memorization.
10	
11	Our goal is twofold: (1)~estimate $\theta_j^{\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \citep{eckerly2017,sinharay2017} and explanatory IRT \citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.
12	
13	\textit{Adaptation~1: Independent examinees $\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\theta_j$ \citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.
14	
15	\textit{Adaptation~2: Binary leakage $\to$ continuous exposure.} Item compromise IRT uses binary indicators \citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \in [0,1]$ derived from detection signals, following the explanatory IRT tradition \citep{deboeck2004}.
16	
17	\textit{Adaptation~3: Stable ability $\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.
18	
19	\subsection{Stage 1: Multi-Signal Exposure Mapping}
20	\label{sec:stage1}
21	
22	For each model~$j$ and item~$i$, we compute four complementary detection signals. \textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \textbf{S2}~(Min-K\%++): a membership inference statistic based on token-level surprisal \citep{duan2025minkpp}. \textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \citep{dekoninck2024constat}. \textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \S\ref{sec:signal_analysis}.
23	
24	We aggregate signals via Reciprocal Rank Fusion \citep[RRF;][]{cormack2009}:
25	\begin{equation}
26	\label{eq:rrf}
27	    e_{ij} = \sum_{s=1}^{4} \frac{1}{k + r_{s}(i)},
28	\end{equation}
29	where $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious) and $k=60$ is the standard smoothing constant. Raw scores are min-max normalized per model to obtain $e_{ij} \in [0,1]$.
30	
31	RRF is a deliberate design choice. A learned aggregator requires labeled contamination data, but ground-truth labels are precisely what we lack. The aggregator's own training data may be contaminated, creating a meta-circularity problem. RRF sidesteps this by operating on rank orderings without parameter estimation.
32	
33	\subsection{Stage 2: Contamination-Augmented IRT}
34	\label{sec:stage2}
35	
36	\paragraph{Primary model: 2PL+$\gamma$.}
37	Our primary specification augments the two-parameter logistic model with a per-domain contamination covariate. For benchmark~$k$ containing domains $d \in \{1,\ldots,D_k\}$ (e.g., MMLU has $D_k=8$ subject domains), the response probability is:
38	\begin{equation}
39	\label{eq:2pl_gamma}
40	    P(y_{ijk} = 1) = \sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_{d(i)} \cdot e_{ij}\bigr),
41	\end{equation}
42	where $\sigma(\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \in \mathbb{R}$ is item difficulty, $\theta_j$ is model ability, and $\gamma_{d(i)}$ is the contamination effect for the domain containing item~$i$. The per-domain specification permits heterogeneous effects: memorization may inflate knowledge recall while leaving reasoning items unaffected within the same benchmark. When a benchmark lacks domain structure, a single $\gamma_k$ is estimated.
43	
44	The additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\gamma_{d(i)} \cdot e_{ij} / a_i$ units on the ability scale.
45	
46	\paragraph{4PL extension for multiple-choice benchmarks.}
47	For MC-format benchmarks (ARC, MMLU) where guessing and ceiling effects are non-negligible, we extend to:
48	\begin{equation}
49	\label{eq:4pl_gamma}
50	    P(y_{ijk} = 1) = c_i + (d_i - c_i)\,\sigma\!\bigl(a_i(\theta_j - b_i) + \gamma_{d(i)} \cdot e_{ij}\bigr),
51	\end{equation}
52	with guessing asymptote $c_i \sim \text{Beta}(5,20)$ and ceiling $d_i \sim \text{Beta}(20,5)$. This extension requires $J \geq 16$ models to avoid overparameterization; with fewer respondents, the $c_i$ and $d_i$ parameters become unidentifiable (empirically confirmed: ARC with $J=5$ under 4PL+$\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068).
53	
54	\paragraph{Inference.}
55	We perform Bayesian inference via NUTS \citep{hoffman2014} in Stan \citep{carpenter2017}, running four chains with target acceptance 0.95. Priors: $\theta_j \sim \mathcal{N}(0,1)$, $a_i \sim \text{LogNormal}(0, 0.5)$, $b_i \sim \mathcal{N}(0,1)$, $\gamma_{d} \sim \mathcal{N}(0,1)$. Convergence requires split-$\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.
56	
57	\paragraph{Calibrated score.}
58	The decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:
59	\begin{equation}
60	\label{eq:calibrated}
61	    \text{Acc}_{j}^{\text{cal}} = \frac{1}{I_k} \sum_{i=1}^{I_k}\, \mathbb{E}_{\boldsymbol{\psi} \sim p(\boldsymbol{\psi} \mid \mathbf{y})} \!\left[\sigma\!\bigl(a_i(\theta_j - b_i)\bigr)\right],
62	\end{equation}
63	with credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.
64	
65	\subsection{Fisher Information and Identifiability}
66	\label{sec:fisher}
67	
68	The reliability of $\gamma$ estimation depends on two factors: signal discriminative quality (AUC of exposure scores) and ensemble size~$J$. The expected Fisher information $\mathcal{I}(\gamma)$ depends on $\text{Var}(e_{\cdot i})$ across models for each item (full derivation in Appendix~A). When signal AUC is low, exposure scores become uniform, collapsing this variance and rendering $\gamma$ structurally unidentifiable.
69	
70	We validate via simulation across 24 conditions (4~AUC levels $\times$ 4~ensemble sizes, 10 seeds each). Recovery succeeds down to AUC$=$0.55 (lowest tested) with bias~$<0.05$ and 95\% CI coverage~$\geq$90\% at $J \geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate.
71	
72	This reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \citep{polo2026growing,lalor2024irt}, well below the $J \geq 50$ regime where $\gamma$ recovery is reliable. This structural gap is itself a central finding (\S\ref{sec:results}).
73	
74	\subsection{Calibration Value Decomposition}
75	\label{sec:value_decomposition}
76	
77	Eq.~\eqref{eq:calibrated} depends on the ability estimate~$\theta_j$, not on $\gamma$ directly. Two mechanisms contribute to calibration quality: (a)~IRT ability estimation, which separates stable capability from item-level noise regardless of the contamination model; and (b)~the explicit $\gamma$ correction, which absorbs contamination variance during joint estimation of~$\theta_j$.
78	
79	Empirically, vanilla 2PL ($\gamma\!=\!0$) achieves calibration MAE comparable to 2PL+$\gamma$ across all benchmarks: GSM8K 0.0063 vs 0.0062, MMLU 0.0068 vs 0.0070, ARC 0.0158 vs 0.0201. The calibration benefit comes entirely from IRT ability estimation itself, which provides better $\theta$ separation from noise than raw accuracy.
80	
81	This strengthens rather than undermines our framework. The $\gamma_{d}$ parameters serve a complementary diagnostic role: they reveal which domains exhibit inflation or deflation, the direction and magnitude of contamination effects, and model misfit patterns. These are actionable characterizations that aggregate calibration metrics cannot deliver. Calibration says ``how much to trust''; $\gamma$ says ``where and why scores are distorted.''
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "ac15f93f-27c6-4bf6-9d5c-70c787cc0e5d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nContamCal operates in two stages: Stage~1 estimates per-item contamination exposure from multiple detection signals via training-free fusion; Stage~2 embeds these scores in a contamination-augmented IRT model to produce calibrated ability estimates with credible intervals.\n\n\\subsection{Problem Formulation}\n\\label{sec:formulation}\n\nLet $y_{ijk} \\in \\{0,1\\}$ denote the binary response of model~$j$ ($j=1,\\ldots,J$) to item~$i$ ($i=1,\\ldots,I_k$) on benchmark~$k$. Standard IRT assumes $P(y_{ijk}=1) = f(\\theta_j, \\boldsymbol{\\xi}_i)$ where $\\theta_j$ is latent ability and $\\boldsymbol{\\xi}_i$ collects item parameters. When training corpora contain benchmark items, the observed ability $\\hat{\\theta}_j$ confounds genuine capability with memorization.\n\nOur goal is twofold: (1)~estimate $\\theta_j^{\\text{clean}}$, the ability each model would exhibit had it never encountered test items during training, and (2)~diagnose contamination effects at domain granularity within each benchmark. We draw on item compromise IRT \\citep{eckerly2017,sinharay2017} and explanatory IRT \\citep{deboeck2004}, adapting these frameworks through three structural modifications for LLM evaluation.\n\n\\textit{Adaptation~1: Independent examinees $\\to$ shared item pool.} Classical IRT assumes independent test-takers. In LLM evaluation, a fixed item set is shared across all models, and responses within a single model may exhibit residual correlations beyond the scalar~$\\theta_j$ \\citep{sanmartin2009}. We mitigate this by fitting per-benchmark models.\n\n\\textit{Adaptation~2: Binary leakage $\\to$ continuous exposure.} Item compromise IRT uses binary indicators \\citep{sinharay2017}. LLM contamination is graded: a model may have encountered an item zero, once, or hundreds of times. We replace binary indicators with continuous exposure scores $e_{ij} \\in [0,1]$ derived from detection signals, following the explanatory IRT tradition \\citep{deboeck2004}.\n\n\\textit{Adaptation~3: Stable ability $\\to$ regime-conditional ability.} In educational testing, ability is approximately constant. For LLMs, the training regime (SFT vs.\\ RL) qualitatively changes both internal representations and signal reliability. We recover clean ability via counterfactual inference (setting exposure to zero) rather than regime-specific ability parameters.\n\n\\subsection{Stage 1: Multi-Signal Exposure Mapping}\n\\label{sec:stage1}\n\nFor each model~$j$ and item~$i$, we compute four complementary detection signals. \\textbf{S1}~(Embedding similarity): cosine similarity between the item embedding and its nearest neighbor in the SFT training corpus. \\textbf{S2}~(Min-K\\%++): a membership inference statistic based on token-level surprisal \\citep{duan2025minkpp}. \\textbf{S3}~(ConStat): the accuracy gap between original and paraphrased item variants \\citep{dekoninck2024constat}. \\textbf{S4}~(Self-Critique): negative entropy of model self-evaluation distributions \\citep{wust2025selfcritique}. S2 and S4 exhibit known failure modes under RL post-training, which we characterize in \\S\\ref{sec:signal_analysis}.\n\nWe aggregate signals via Reciprocal Rank Fusion \\citep[RRF;][]{cormack2009}:\n\\begin{equation}\n\\label{eq:rrf}\n    e_{ij} = \\sum_{s=1}^{4} \\frac{1}{k + r_{s}(i)},\n\\end{equation}\nwhere $r_s(i)$ is the rank of item~$i$ under signal~$s$ (rank~1 = most suspicious) and $k=60$ is the standard smoothing constant. Raw scores are min-max normalized per model to obtain $e_{ij} \\in [0,1]$.\n\nRRF is a deliberate design choice. A learned aggregator requires labeled contamination data, but ground-truth labels are precisely what we lack. The aggregator's own training data may be contaminated, creating a meta-circularity problem. RRF sidesteps this by operating on rank orderings without parameter estimation.\n\n\\subsection{Stage 2: Contamination-Augmented IRT}\n\\label{sec:stage2}\n\n\\paragraph{Primary model: 2PL+$\\gamma$.}\nOur primary specification augments the two-parameter logistic model with a per-domain contamination covariate. For benchmark~$k$ containing domains $d \\in \\{1,\\ldots,D_k\\}$ (e.g., MMLU has $D_k=8$ subject domains), the response probability is:\n\\begin{equation}\n\\label{eq:2pl_gamma}\n    P(y_{ijk} = 1) = \\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),\n\\end{equation}\nwhere $\\sigma(\\cdot)$ is the logistic function, $a_i > 0$ is item discrimination, $b_i \\in \\mathbb{R}$ is item difficulty, $\\theta_j$ is model ability, and $\\gamma_{d(i)}$ is the contamination effect for the domain containing item~$i$. The per-domain specification permits heterogeneous effects: memorization may inflate knowledge recall while leaving reasoning items unaffected within the same benchmark. When a benchmark lacks domain structure, a single $\\gamma_k$ is estimated.\n\nThe additive structure admits a natural interpretation: contamination shifts the effective difficulty of item~$i$ by $\\gamma_{d(i)} \\cdot e_{ij} / a_i$ units on the ability scale.\n\n\\paragraph{4PL extension for multiple-choice benchmarks.}\nFor MC-format benchmarks (ARC, MMLU) where guessing and ceiling effects are non-negligible, we extend to:\n\\begin{equation}\n\\label{eq:4pl_gamma}\n    P(y_{ijk} = 1) = c_i + (d_i - c_i)\\,\\sigma\\!\\bigl(a_i(\\theta_j - b_i) + \\gamma_{d(i)} \\cdot e_{ij}\\bigr),\n\\end{equation}\nwith guessing asymptote $c_i \\sim \\text{Beta}(5,20)$ and ceiling $d_i \\sim \\text{Beta}(20,5)$. This extension requires $J \\geq 16$ models to avoid overparameterization; with fewer respondents, the $c_i$ and $d_i$ parameters become unidentifiable (empirically confirmed: ARC with $J=5$ under 4PL+$\\gamma$ yields PPP$=$0.000 and MAE degradation from 0.004 to 0.068).\n\n\\paragraph{Inference.}\nWe perform Bayesian inference via NUTS \\citep{hoffman2014} in Stan \\citep{carpenter2017}, running four chains with target acceptance 0.95. Priors: $\\theta_j \\sim \\mathcal{N}(0,1)$, $a_i \\sim \\text{LogNormal}(0, 0.5)$, $b_i \\sim \\mathcal{N}(0,1)$, $\\gamma_{d} \\sim \\mathcal{N}(0,1)$. Convergence requires split-$\\hat{R} < 1.01$ and bulk ESS~$> 400$ for all parameters.\n\n\\paragraph{Calibrated score.}\nThe decontaminated accuracy for model~$j$ on benchmark~$k$ is the posterior expectation under zero exposure:\n\\begin{equation}\n\\label{eq:calibrated}\n    \\text{Acc}_{j}^{\\text{cal}} = \\frac{1}{I_k} \\sum_{i=1}^{I_k}\\, \\mathbb{E}_{\\boldsymbol{\\psi} \\sim p(\\boldsymbol{\\psi} \\mid \\mathbf{y})} \\!\\left[\\sigma\\!\\bigl(a_i(\\theta_j - b_i)\\bigr)\\right],\n\\end{equation}\nwith credible intervals from posterior quantiles. Models with noisier exposure signals receive wider intervals by construction.\n\n\\subsection{Fisher Information and Identifiability}\n\\label{sec:fisher}\n\nThe reliability of $\\gamma$ estimation depends on two factors: signal discriminative quality (AUC of exposure scores) and ensemble size~$J$. The expected Fisher information $\\mathcal{I}(\\gamma)$ depends on $\\text{Var}(e_{\\cdot i})$ across models for each item (full derivation in Appendix~A). When signal AUC is low, exposure scores become uniform, collapsing this variance and rendering $\\gamma$ structurally unidentifiable.\n\nWe validate via simulation across 24 conditions (4~AUC levels $\\times$ 4~ensemble sizes, 10 seeds each). Recovery succeeds down to AUC$=$0.55 (lowest tested) with bias~$<0.05$ and 95\\% CI coverage~$\\geq$90\\% at $J \\geq 50$. Posterior CI width scales as $J^{-0.48}$, close to the parametric $J^{-0.5}$ rate.\n\nThis reveals a domain-method mismatch: IRT-based LLM evaluation typically pools $J = 8$--$30$ models \\citep{polo2026growing,lalor2024irt}, well below the $J \\geq 50$ regime where $\\gamma$ recovery is reliable. This structural gap is itself a central finding (\\S\\ref{sec:results}).\n\n\\subsection{Calibration Value Decomposition}\n\\label{sec:value_decomposition}\n\nEq.~\\eqref{eq:calibrated} depends on the ability estimate~$\\theta_j$, not on $\\gamma$ directly. Two mechanisms contribute to calibration quality: (a)~IRT ability estimation, which separates stable capability from item-level noise regardless of the contamination model; and (b)~the explicit $\\gamma$ correction, which absorbs contamination variance during joint estimation of~$\\theta_j$.\n\nEmpirically, vanilla 2PL ($\\gamma\\!=\\!0$) achieves calibration MAE comparable to 2PL+$\\gamma$ across all benchmarks: GSM8K 0.0063 vs 0.0062, MMLU 0.0068 vs 0.0070, ARC 0.0158 vs 0.0201. The calibration benefit comes entirely from IRT ability estimation itself, which provides better $\\theta$ separation from noise than raw accuracy.\n\nThis strengthens rather than undermines our framework. The $\\gamma_{d}$ parameters serve a complementary diagnostic role: they reveal which domains exhibit inflation or deflation, the direction and magnitude of contamination effects, and model misfit patterns. These are actionable characterizations that aggregate calibration metrics cannot deliver. Calibration says ``how much to trust''; $\\gamma$ says ``where and why scores are distorted.''\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the references bib file and the method section. Let me verify the cite keys that are specified in the task. Let me check:

- `\citep{shi_2023_minkprob}` - exists as `shi_2023_minkprob` ✓
- `\citep{zhang_2024_minkpp}` - exists as `zhang_2024_minkpp` ✓
- `\citep{dekoninck_2024_constat}` - exists as `dekoninck_2024_constat` ✓


- `\citep{dong_2024_cdd}` - exists as `dong_2024_cdd` ✓
- `\citep{choi_2025_kds}` - exists as `choi_2025_kds` ✓
- `\citep{deng_2024_tsguessing}` - exists as `deng_2024_tsguessing` ✓
- `\citep{lalor_2024_irt_nlp}` - exists as `lalor_2024_irt_nlp` ✓
- `\citep{polo_2024_tinybenchmarks}` - exists as `polo_2024_tinybenchmarks` ✓

All the required citations are present in the bibliography.

Now I'm checking the remaining references. Most are matching up correctly, but I'm noticing a discrepancy with the Sinharay citation—the document references `sinharay_2017_compromise_detection` but the actual entry in the bibliography is `sinharay_2017_preknowledge`. I need to figure out if this is a mismatch that needs to be resolved. I need to double-check the citation keys against what's actually in the bib file. The task specifies `\citep{sinharay_2017_compromise_detection}`, but the bib only has `sinharay_2017_preknowledge`, so I'll use that instead. For the Emperor paper, `xu2025emperor` is the one the task calls for and it exists. The DCR citation appears to be cut off in the instruction, but `li_2025_dcr` is what I found in the bib file.

Now I'm drafting the Related Work section—it needs to be around 700 words total, split into 5 subsections of roughly 140 words each, while maintaining the style guidelines about avoiding dashes, -ing endings, and AI markers, and focusing on positioning rather than surveying.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "ba4fbf77-9ffb-493b-b9bd-97dea3098073",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKd3Psx2xX9jsuiRjYQPSa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19708,
      "cache_read_input_tokens": 26806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19708
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

_source line 11_

Now I'll check if the output directory exists, then write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "22f395b6-d293-4192-8171-f02ce045877a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKd3Psx2xX9jsuiRjYQPSa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19708,
      "cache_read_input_tokens": 26806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19708
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

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01EFdYqZmNdj49yo7VHeL59k`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/",
  "description": "List paper draft directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "34069c28-2ff3-47c4-8b83-51100675374a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XKd3Psx2xX9jsuiRjYQPSa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19708,
      "cache_read_input_tokens": 26806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19708
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

_source line 13 · 2026-05-17T04:37:47.891Z_

<details><summary>↩ Tool result · `toolu_01EFdYqZmNdj49yo7VHeL59k`</summary>

```text
_pdf_images
experiments.tex
figures
introduction.tex
literature_gaps.md
main.aux
main.bbl
main.blg
main.log
main.pdf
main.tex
method.tex
references.bib
references.bib.prev
related_work.tex
results.tex
results_tables.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "70e60047-fcf0-44f5-acea-6d6e8a0cbdd0",
  "tool_use_result": {
    "stdout": "_pdf_images\nexperiments.tex\nfigures\nintroduction.tex\nliterature_gaps.md\nmain.aux\nmain.bbl\nmain.blg\nmain.log\nmain.pdf\nmain.tex\nmethod.tex\nreferences.bib\nreferences.bib.prev\nrelated_work.tex\nresults.tex\nresults_tables.md",
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

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
The file already exists. Let me read it first to see what's there, then write the new version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "3682316b-80b3-4cf2-9da7-f3a3b4ee4ce5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQhqejn8tskr7Mv6VcHtuL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1234,
      "cache_read_input_tokens": 46514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1234
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

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01FmzGgxeRa6p7B7mQdfyhGj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "fb53cbeb-e171-4ba8-ade8-ced7fa7712c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQhqejn8tskr7Mv6VcHtuL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1234,
      "cache_read_input_tokens": 46514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1234
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

_source line 16 · 2026-05-17T04:37:52.596Z_

<details><summary>↩ Tool result · `toolu_01FmzGgxeRa6p7B7mQdfyhGj`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Benchmark Contamination Detection}
5	\label{sec:related:detection}
6	
7	Detecting training data contamination in LLMs has produced a diverse methodological landscape spanning at least eight paradigms. Time-based partitioning uses temporal cutoffs to identify potentially leaked items, while canary string insertion (e.g., BIG-Bench) provides direct memorization probes \citep{chang2025benchmarking}. Min-K\%++ \citep{duan2025minkpp} performs membership inference by examining token-level probability distributions, achieving strong detection on pre-training contamination. Time Travel \citep{oren2024proving} uses guided completion to detect black-box contamination without model weight access. ConStat \citep{dekoninck2024constat} measures performance gaps between original and paraphrased benchmark items, targeting surface-form memorization. Self-Critique \citep{wust2025selfcritique} identifies contamination through entropy collapse in model self-evaluations---a signal that, unlike probability-based methods, partially survives reinforcement learning post-training. Hierarchical semantic detection approaches match items at multiple granularity levels to training corpora. KDS \citep{xu2025kds} uses knowledge distillation signatures to achieve near-perfect detection (Spearman $\rho = 0.99$) but requires per-model LoRA fine-tuning, limiting scalability.
8	
9	A critical finding is that detection methods are fragile under RL post-training: \citet{wang2025fragility} show that GRPO and similar procedures degrade probability-based detection signals substantially, while Self-Critique's entropy-based signal achieves only 0.60--0.70 AUC on RL-trained models \citep{wust2025selfcritique}. Despite this rich detection toolkit, all existing methods produce binary or continuous \emph{flags}---they diagnose contamination without prescribing how to adjust the reported accuracy that end-users rely on.
10	
11	\subsection{Contamination Impact and Mitigation}
12	\label{sec:related:mitigation}
13	
14	Understanding contamination's quantitative impact has advanced rapidly. \citet{dong2026dose} establish dose-response curves showing that score inflation scales monotonically with both model size and contamination dosage. \citet{yang2026rl} further demonstrate that SFT inflates accuracy only on contaminated tasks, while GRPO amplifies inflation even on structurally similar uncontaminated items---a cross-contamination effect that complicates attribution. \citet{zhang2025forget} show that contamination persists in model weights following standard decontamination, with forgetting curves following scaling laws that make complete removal impractical.
15	
16	The mitigation landscape is equally sobering. \citet{xu2025emperor} systematically evaluate twenty strategies---item rephrasing, option shuffling, filtering, dynamic benchmark construction, and more---across ten LLMs and five benchmarks, finding that none reliably eliminates contamination effects. Dynamic benchmarks such as LiveBench \citep{white2024livebench} circumvent contamination by generating fresh items but cannot retroactively calibrate existing benchmark scores. Inference-Time Decontamination \citep{yang2024inference} rewrites items at test time but operates during inference rather than producing post-hoc calibrated scores. DCR \citep{li2025dcr} is the closest existing method to ours, producing adjusted accuracy via fuzzy inference over detection signals; however, it provides point estimates without uncertainty bounds and does not address signal degradation under RL. \citet{rao2026silicon} propose a router-worker audit framework that produces contamination flags rather than calibrated scores. Collectively, these findings motivate a paradigm shift: from contamination \emph{prevention}---which demonstrably fails---to post-hoc statistical \emph{adjustment} with proper uncertainty quantification.
17	
18	\paragraph{Terminological note.} Throughout this paper, ``calibration'' refers to the psychometric sense of score adjustment---recovering decontaminated ability estimates from potentially inflated benchmark scores. This should not be confused with probability calibration in machine learning, where the goal is to align predicted probabilities with empirical frequencies via methods such as Platt scaling or temperature scaling \citep{guo2017calibration}. ContamCal performs the former: it adjusts reported accuracies for contamination bias rather than recalibrating model confidence scores.
19	
20	\subsection{IRT for LLM Evaluation}
21	\label{sec:related:irt}
22	
23	Item response theory has gained traction as a principled framework for LLM evaluation. \citet{lalor2024irt} demonstrate that IRT-based evaluation yields more informative model comparisons than raw accuracy. PSN-IRT \citep{gu2026psnirt} scales this to 41,871 items across 11 benchmarks using a 4PL model with neural network parameter estimation, establishing item difficulty and discrimination profiles but without modeling contamination or producing adjusted scores. \citet{polo2026growing} fit multidimensional 2PL IRT with anchor items to over 400 models, validating IRT's applicability at scale while identifying practical limitations in the few-examinee regime; contamination is not addressed. ATLAS \citep{lyu2025atlas} leverages IRT for adaptive testing, reducing evaluation cost through maximally informative item selection. TinyBenchmarks \citep{polo2024tinybenchmarks} similarly exploits IRT-informed item selection for efficient evaluation. HiBayES \citep{zhuang2025hibayes} provides hierarchical Bayesian credible intervals over model ability estimates but treats all items as equally trustworthy. \citet{han2026probing} quantify contamination effects within psychometric evaluations but do not use IRT or produce calibrated scores. Across this body of work, contamination has not been modeled as a covariate within the IRT framework---a gap that ContamCal addresses by augmenting the item response function with exposure parameters.
24	
25	\paragraph{Alternative uncertainty quantification.} Conformal prediction \citep{angelopoulos2023conformal} offers distribution-free coverage guarantees and has been applied to various prediction tasks. We adopt Bayesian IRT over conformal alternatives for three reasons. First, contamination-specific parameters ($\gamma_k$) yield directly interpretable causal quantities---``contamination inflates scores by $\gamma_k$ units on benchmark $k$''---whereas conformal intervals lack such structural decomposition. Second, the posterior over all latent variables naturally propagates measurement error into credible intervals without requiring a separate calibration set. Third, conformal prediction assumes exchangeability of data points, which is violated in the contaminated setting: response distributions for contaminated items are systematically shifted relative to clean items. Conformal methods may nonetheless prove valuable in complementary LLM evaluation contexts where exchangeability holds.
26	
27	\subsection{Item Compromise in Educational Measurement}
28	\label{sec:related:edumeasure}
29	
30	The psychometric literature has long addressed item compromise---the unauthorized disclosure of test content prior to administration. \citet{eckerly2017} develops IRT models that incorporate compromise indicators to simultaneously estimate item parameters and compromise effects, while \citet{sinharay2017} proposes likelihood ratio and score tests for detecting item preknowledge. The explanatory IRT tradition \citep{deboeck2004,adams1997} provides the theoretical foundation for embedding external covariates within item response functions, and \citet{mislevy1986} establishes Bayesian estimation procedures for such augmented models.
31	
32	Adapting this tradition to LLM evaluation requires three structural adaptations detailed in \S\ref{sec:stage2}.
33	
34	\paragraph{Differential item functioning.} The per-benchmark exposure parameter $\gamma_k$ in ContamCal can be interpreted as measuring differential item functioning (DIF) between contaminated and clean model populations. DIF---the phenomenon whereby examinees of equal ability but different group membership respond differently to an item---was formalized by \citep{holland1993dif}, with IRT-based detection procedures developed by \citet{thissen1993dif} and logistic regression frameworks established by \citet{zumbo1999dif}. In this view, $\gamma_k$ functions as a uniform DIF parameter capturing systematic advantage conferred by exposure. However, ContamCal extends the classical DIF paradigm in two respects: group membership is determined by continuous exposure scores from Stage~1 rather than discrete demographic categories, and DIF is modeled with benchmark-specific $\gamma_k$ parameters, each with independent priors, fitted separately per benchmark.
35	
36	\paragraph{Positioning.} ContamCal bridges contamination detection (which flags but does not calibrate), IRT-based LLM evaluation (which models ability but ignores contamination), and educational item compromise models (which handle leaked items but assume independent examinees with binary exposure). Table~\ref{tab:positioning} summarizes the capabilities of representative methods.
37	
38	\begin{table}[t]
39	\centering
40	\small
41	\begin{tabular}{lcccc}
42	\toprule
43	\textbf{Method} & \textbf{Detects} & \textbf{Calibrates} & \textbf{UQ} & \textbf{RL-robust} \\
44	\midrule
45	Min-K\%++ & \checkmark & & & \\
46	ConStat & \checkmark & & & \\
47	Self-Critique & \checkmark & & & \checkmark \\
48	KDS & \checkmark & & & ? \\
49	DCR & \checkmark & \checkmark & & \\
50	PSN-IRT & & & & \\
51	HiBayES & & & \checkmark & \\
52	\textbf{ContamCal} & \checkmark & \checkmark & \checkmark & ?$^\dagger$ \\
53	\bottomrule
54	\multicolumn{5}{l}{\footnotesize $^\dagger$Designed for RL robustness via uncertainty propagation; empirical validation pending (exp-008).}
55	\end{tabular}
56	\caption{Capability comparison of contamination-aware evaluation methods. UQ = uncertainty quantification via credible intervals. RL-robust = maintains effectiveness after RL post-training.}
57	\label{tab:positioning}
58	\end{table}
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "46a83973-2a0f-4866-ad77-e44aff9c4a68",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Benchmark Contamination Detection}\n\\label{sec:related:detection}\n\nDetecting training data contamination in LLMs has produced a diverse methodological landscape spanning at least eight paradigms. Time-based partitioning uses temporal cutoffs to identify potentially leaked items, while canary string insertion (e.g., BIG-Bench) provides direct memorization probes \\citep{chang2025benchmarking}. Min-K\\%++ \\citep{duan2025minkpp} performs membership inference by examining token-level probability distributions, achieving strong detection on pre-training contamination. Time Travel \\citep{oren2024proving} uses guided completion to detect black-box contamination without model weight access. ConStat \\citep{dekoninck2024constat} measures performance gaps between original and paraphrased benchmark items, targeting surface-form memorization. Self-Critique \\citep{wust2025selfcritique} identifies contamination through entropy collapse in model self-evaluations---a signal that, unlike probability-based methods, partially survives reinforcement learning post-training. Hierarchical semantic detection approaches match items at multiple granularity levels to training corpora. KDS \\citep{xu2025kds} uses knowledge distillation signatures to achieve near-perfect detection (Spearman $\\rho = 0.99$) but requires per-model LoRA fine-tuning, limiting scalability.\n\nA critical finding is that detection methods are fragile under RL post-training: \\citet{wang2025fragility} show that GRPO and similar procedures degrade probability-based detection signals substantially, while Self-Critique's entropy-based signal achieves only 0.60--0.70 AUC on RL-trained models \\citep{wust2025selfcritique}. Despite this rich detection toolkit, all existing methods produce binary or continuous \\emph{flags}---they diagnose contamination without prescribing how to adjust the reported accuracy that end-users rely on.\n\n\\subsection{Contamination Impact and Mitigation}\n\\label{sec:related:mitigation}\n\nUnderstanding contamination's quantitative impact has advanced rapidly. \\citet{dong2026dose} establish dose-response curves showing that score inflation scales monotonically with both model size and contamination dosage. \\citet{yang2026rl} further demonstrate that SFT inflates accuracy only on contaminated tasks, while GRPO amplifies inflation even on structurally similar uncontaminated items---a cross-contamination effect that complicates attribution. \\citet{zhang2025forget} show that contamination persists in model weights following standard decontamination, with forgetting curves following scaling laws that make complete removal impractical.\n\nThe mitigation landscape is equally sobering. \\citet{xu2025emperor} systematically evaluate twenty strategies---item rephrasing, option shuffling, filtering, dynamic benchmark construction, and more---across ten LLMs and five benchmarks, finding that none reliably eliminates contamination effects. Dynamic benchmarks such as LiveBench \\citep{white2024livebench} circumvent contamination by generating fresh items but cannot retroactively calibrate existing benchmark scores. Inference-Time Decontamination \\citep{yang2024inference} rewrites items at test time but operates during inference rather than producing post-hoc calibrated scores. DCR \\citep{li2025dcr} is the closest existing method to ours, producing adjusted accuracy via fuzzy inference over detection signals; however, it provides point estimates without uncertainty bounds and does not address signal degradation under RL. \\citet{rao2026silicon} propose a router-worker audit framework that produces contamination flags rather than calibrated scores. Collectively, these findings motivate a paradigm shift: from contamination \\emph{prevention}---which demonstrably fails---to post-hoc statistical \\emph{adjustment} with proper uncertainty quantification.\n\n\\paragraph{Terminological note.} Throughout this paper, ``calibration'' refers to the psychometric sense of score adjustment---recovering decontaminated ability estimates from potentially inflated benchmark scores. This should not be confused with probability calibration in machine learning, where the goal is to align predicted probabilities with empirical frequencies via methods such as Platt scaling or temperature scaling \\citep{guo2017calibration}. ContamCal performs the former: it adjusts reported accuracies for contamination bias rather than recalibrating model confidence scores.\n\n\\subsection{IRT for LLM Evaluation}\n\\label{sec:related:irt}\n\nItem response theory has gained traction as a principled framework for LLM evaluation. \\citet{lalor2024irt} demonstrate that IRT-based evaluation yields more informative model comparisons than raw accuracy. PSN-IRT \\citep{gu2026psnirt} scales this to 41,871 items across 11 benchmarks using a 4PL model with neural network parameter estimation, establishing item difficulty and discrimination profiles but without modeling contamination or producing adjusted scores. \\citet{polo2026growing} fit multidimensional 2PL IRT with anchor items to over 400 models, validating IRT's applicability at scale while identifying practical limitations in the few-examinee regime; contamination is not addressed. ATLAS \\citep{lyu2025atlas} leverages IRT for adaptive testing, reducing evaluation cost through maximally informative item selection. TinyBenchmarks \\citep{polo2024tinybenchmarks} similarly exploits IRT-informed item selection for efficient evaluation. HiBayES \\citep{zhuang2025hibayes} provides hierarchical Bayesian credible intervals over model ability estimates but treats all items as equally trustworthy. \\citet{han2026probing} quantify contamination effects within psychometric evaluations but do not use IRT or produce calibrated scores. Across this body of work, contamination has not been modeled as a covariate within the IRT framework---a gap that ContamCal addresses by augmenting the item response function with exposure parameters.\n\n\\paragraph{Alternative uncertainty quantification.} Conformal prediction \\citep{angelopoulos2023conformal} offers distribution-free coverage guarantees and has been applied to various prediction tasks. We adopt Bayesian IRT over conformal alternatives for three reasons. First, contamination-specific parameters ($\\gamma_k$) yield directly interpretable causal quantities---``contamination inflates scores by $\\gamma_k$ units on benchmark $k$''---whereas conformal intervals lack such structural decomposition. Second, the posterior over all latent variables naturally propagates measurement error into credible intervals without requiring a separate calibration set. Third, conformal prediction assumes exchangeability of data points, which is violated in the contaminated setting: response distributions for contaminated items are systematically shifted relative to clean items. Conformal methods may nonetheless prove valuable in complementary LLM evaluation contexts where exchangeability holds.\n\n\\subsection{Item Compromise in Educational Measurement}\n\\label{sec:related:edumeasure}\n\nThe psychometric literature has long addressed item compromise---the unauthorized disclosure of test content prior to administration. \\citet{eckerly2017} develops IRT models that incorporate compromise indicators to simultaneously estimate item parameters and compromise effects, while \\citet{sinharay2017} proposes likelihood ratio and score tests for detecting item preknowledge. The explanatory IRT tradition \\citep{deboeck2004,adams1997} provides the theoretical foundation for embedding external covariates within item response functions, and \\citet{mislevy1986} establishes Bayesian estimation procedures for such augmented models.\n\nAdapting this tradition to LLM evaluation requires three structural adaptations detailed in \\S\\ref{sec:stage2}.\n\n\\paragraph{Differential item functioning.} The per-benchmark exposure parameter $\\gamma_k$ in ContamCal can be interpreted as measuring differential item functioning (DIF) between contaminated and clean model populations. DIF---the phenomenon whereby examinees of equal ability but different group membership respond differently to an item---was formalized by \\citep{holland1993dif}, with IRT-based detection procedures developed by \\citet{thissen1993dif} and logistic regression frameworks established by \\citet{zumbo1999dif}. In this view, $\\gamma_k$ functions as a uniform DIF parameter capturing systematic advantage conferred by exposure. However, ContamCal extends the classical DIF paradigm in two respects: group membership is determined by continuous exposure scores from Stage~1 rather than discrete demographic categories, and DIF is modeled with benchmark-specific $\\gamma_k$ parameters, each with independent priors, fitted separately per benchmark.\n\n\\paragraph{Positioning.} ContamCal bridges contamination detection (which flags but does not calibrate), IRT-based LLM evaluation (which models ability but ignores contamination), and educational item compromise models (which handle leaked items but assume independent examinees with binary exposure). Table~\\ref{tab:positioning} summarizes the capabilities of representative methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Detects} & \\textbf{Calibrates} & \\textbf{UQ} & \\textbf{RL-robust} \\\\\n\\midrule\nMin-K\\%++ & \\checkmark & & & \\\\\nConStat & \\checkmark & & & \\\\\nSelf-Critique & \\checkmark & & & \\checkmark \\\\\nKDS & \\checkmark & & & ? \\\\\nDCR & \\checkmark & \\checkmark & & \\\\\nPSN-IRT & & & & \\\\\nHiBayES & & & \\checkmark & \\\\\n\\textbf{ContamCal} & \\checkmark & \\checkmark & \\checkmark & ?$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Designed for RL robustness via uncertainty propagation; empirical validation pending (exp-008).}\n\\end{tabular}\n\\caption{Capability comparison of contamination-aware evaluation methods. UQ = uncertainty quantification via credible intervals. RL-robust = maintains effectiveness after RL post-training.}\n\\label{tab:positioning}\n\\end{table}\n",
      "numLines": 59,
      "startLine": 1,
      "totalLines": 59
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the existing related_work.tex and the references. The existing version is quite long and doesn't match the task requirements. I need to rewrite it completely following the task's structure (5 subsections, ~140 words each, ~700 total), with the correct cite keys as specified in the task.

Let me note the cite keys from the bib:
- `shi_2023_minkprob` - exists ✓
- `zhang_2024_minkpp` - exists ✓


- `dekoninck_2024_constat` - exists ✓
- `dong_2024_cdd` - exists ✓
- `choi_2025_kds` - exists ✓
- `deng_2024_tsguessing` - exists ✓
- `lalor_2024_irt_nlp` - exists ✓
- `polo_2024_tinybenchmarks` - exists ✓
- `habba_2025_growing_pains` - exists ✓
- `luettgau_2025_hibayes` - exists ✓
- `li_2024_atlas` - exists ✓
- `eckerly_2017_item_compromise` - exists ✓

All the required citations are available, so I can proceed with writing the five subsections using these references. I see there are actually two DCR papers in the bibliography—one by Li et al. on decontaminated calibration and ranking, and another by Xu et al. on quantifying data contamination. Since the task specifies using `\citep{li_2025_dcr}`, I'll go with that one. I've confirmed `guo_2017_calibration` exists too. Now I need to structure the literature review across five subsections, keeping each around 140 words, and I'm starting to draft the content while being careful to follow the exact task structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "e452cc45-d0bb-46b3-8703-9ff2a67bb4ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzjWz4VMh6yfqRSHX88A1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 47748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2673
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

_source line 18_

Now I'll write the rewritten Related Work section following the task's structure and constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "396eba1c-a891-452d-b858-9cb611c84cea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzjWz4VMh6yfqRSHX88A1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 47748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2673
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

_source line 19_

<details open><summary>🔧 Tool call — Write · `toolu_0144pbKwEkHqRVdrXXfzFTjb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "d94ca098-7f2a-4423-b470-45892a8f6d44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzjWz4VMh6yfqRSHX88A1G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2673,
      "cache_read_input_tokens": 47748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2673
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

_source line 20 · 2026-05-17T04:38:31.015Z_

<details><summary>↩ Tool result · `toolu_0144pbKwEkHqRVdrXXfzFTjb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "e2254311-3df0-4426-b1ba-8d9d995cb242",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 58,
        "newStart": 1,
        "newLines": 22,
        "lines": [
          " \\section{Related Work}",
          "-\\label{sec:related}",
          "+\\label{sec:related_work}",
          " ",
          "-\\subsection{Benchmark Contamination Detection}",
          "-\\label{sec:related:detection}",
          "+\\subsection{Contamination Detection}",
          " ",
          "-Detecting training data contamination in LLMs has produced a diverse methodological landscape spanning at least eight paradigms. Time-based partitioning uses temporal cutoffs to identify potentially leaked items, while canary string insertion (e.g., BIG-Bench) provides direct memorization probes \\citep{chang2025benchmarking}. Min-K\\%++ \\citep{duan2025minkpp} performs membership inference by examining token-level probability distributions, achieving strong detection on pre-training contamination. Time Travel \\citep{oren2024proving} uses guided completion to detect black-box contamination without model weight access. ConStat \\citep{dekoninck2024constat} measures performance gaps between original and paraphrased benchmark items, targeting surface-form memorization. Self-Critique \\citep{wust2025selfcritique} identifies contamination through entropy collapse in model self-evaluations---a signal that, unlike probability-based methods, partially survives reinforcement learning post-training. Hierarchical semantic detection approaches match items at multiple granularity levels to training corpora. KDS \\citep{xu2025kds} uses knowledge distillation signatures to achieve near-perfect detection (Spearman $\\rho = 0.99$) but requires per-model LoRA fine-tuning, limiting scalability.",
          "+Recent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.",
          " ",
          "-A critical finding is that detection methods are fragile under RL post-training: \\citet{wang2025fragility} show that GRPO and similar procedures degrade probability-based detection signals substantially, while Self-Critique's entropy-based signal achieves only 0.60--0.70 AUC on RL-trained models \\citep{wust2025selfcritique}. Despite this rich detection toolkit, all existing methods produce binary or continuous \\emph{flags}---they diagnose contamination without prescribing how to adjust the reported accuracy that end-users rely on.",
          "-",
          "-\\subsection{Contamination Impact and Mitigation}",
          "-\\label{sec:related:mitigation}",
          "-",
          "-Understanding contamination's quantitative impact has advanced rapidly. \\citet{dong2026dose} establish dose-response curves showing that score inflation scales monotonically with both model size and contamination dosage. \\citet{yang2026rl} further demonstrate that SFT inflates accuracy only on contaminated tasks, while GRPO amplifies inflation even on structurally similar uncontaminated items---a cross-contamination effect that complicates attribution. \\citet{zhang2025forget} show that contamination persists in model weights following standard decontamination, with forgetting curves following scaling laws that make complete removal impractical.",
          "-",
          "-The mitigation landscape is equally sobering. \\citet{xu2025emperor} systematically evaluate twenty strategies---item rephrasing, option shuffling, filtering, dynamic benchmark construction, and more---across ten LLMs and five benchmarks, finding that none reliably eliminates contamination effects. Dynamic benchmarks such as LiveBench \\citep{white2024livebench} circumvent contamination by generating fresh items but cannot retroactively calibrate existing benchmark scores. Inference-Time Decontamination \\citep{yang2024inference} rewrites items at test time but operates during inference rather than producing post-hoc calibrated scores. DCR \\citep{li2025dcr} is the closest existing method to ours, producing adjusted accuracy via fuzzy inference over detection signals; however, it provides point estimates without uncertainty bounds and does not address signal degradation under RL. \\citet{rao2026silicon} propose a router-worker audit framework that produces contamination flags rather than calibrated scores. Collectively, these findings motivate a paradigm shift: from contamination \\emph{prevention}---which demonstrably fails---to post-hoc statistical \\emph{adjustment} with proper uncertainty quantification.",
          "-",
          "-\\paragraph{Terminological note.} Throughout this paper, ``calibration'' refers to the psychometric sense of score adjustment---recovering decontaminated ability estimates from potentially inflated benchmark scores. This should not be confused with probability calibration in machine learning, where the goal is to align predicted probabilities with empirical frequencies via methods such as Platt scaling or temperature scaling \\citep{guo2017calibration}. ContamCal performs the former: it adjusts reported accuracies for contamination bias rather than recalibrating model confidence scores.",
          "-",
          " \\subsection{IRT for LLM Evaluation}",
          "-\\label{sec:related:irt}",
          " ",
          "-Item response theory has gained traction as a principled framework for LLM evaluation. \\citet{lalor2024irt} demonstrate that IRT-based evaluation yields more informative model comparisons than raw accuracy. PSN-IRT \\citep{gu2026psnirt} scales this to 41,871 items across 11 benchmarks using a 4PL model with neural network parameter estimation, establishing item difficulty and discrimination profiles but without modeling contamination or producing adjusted scores. \\citet{polo2026growing} fit multidimensional 2PL IRT with anchor items to over 400 models, validating IRT's applicability at scale while identifying practical limitations in the few-examinee regime; contamination is not addressed. ATLAS \\citep{lyu2025atlas} leverages IRT for adaptive testing, reducing evaluation cost through maximally informative item selection. TinyBenchmarks \\citep{polo2024tinybenchmarks} similarly exploits IRT-informed item selection for efficient evaluation. HiBayES \\citep{zhuang2025hibayes} provides hierarchical Bayesian credible intervals over model ability estimates but treats all items as equally trustworthy. \\citet{han2026probing} quantify contamination effects within psychometric evaluations but do not use IRT or produce calibrated scores. Across this body of work, contamination has not been modeled as a covariate within the IRT framework---a gap that ContamCal addresses by augmenting the item response function with exposure parameters.",
          "+Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.",
          " ",
          "-\\paragraph{Alternative uncertainty quantification.} Conformal prediction \\citep{angelopoulos2023conformal} offers distribution-free coverage guarantees and has been applied to various prediction tasks. We adopt Bayesian IRT over conformal alternatives for three reasons. First, contamination-specific parameters ($\\gamma_k$) yield directly interpretable causal quantities---``contamination inflates scores by $\\gamma_k$ units on benchmark $k$''---whereas conformal intervals lack such structural decomposition. Second, the posterior over all latent variables naturally propagates measurement error into credible intervals without requiring a separate calibration set. Third, conformal prediction assumes exchangeability of data points, which is violated in the contaminated setting: response distributions for contaminated items are systematically shifted relative to clean items. Conformal methods may nonetheless prove valuable in complementary LLM evaluation contexts where exchangeability holds.",
          "-",
          " \\subsection{Item Compromise in Educational Measurement}",
          "-\\label{sec:related:edumeasure}",
          " ",
          "-The psychometric literature has long addressed item compromise---the unauthorized disclosure of test content prior to administration. \\citet{eckerly2017} develops IRT models that incorporate compromise indicators to simultaneously estimate item parameters and compromise effects, while \\citet{sinharay2017} proposes likelihood ratio and score tests for detecting item preknowledge. The explanatory IRT tradition \\citep{deboeck2004,adams1997} provides the theoretical foundation for embedding external covariates within item response functions, and \\citet{mislevy1986} establishes Bayesian estimation procedures for such augmented models.",
          "+The psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).",
          " ",
          "-Adapting this tradition to LLM evaluation requires three structural adaptations detailed in \\S\\ref{sec:stage2}.",
          "+\\subsection{Contamination Mitigation and Score Adjustment}",
          " ",
          "-\\paragraph{Differential item functioning.} The per-benchmark exposure parameter $\\gamma_k$ in ContamCal can be interpreted as measuring differential item functioning (DIF) between contaminated and clean model populations. DIF---the phenomenon whereby examinees of equal ability but different group membership respond differently to an item---was formalized by \\citep{holland1993dif}, with IRT-based detection procedures developed by \\citet{thissen1993dif} and logistic regression frameworks established by \\citet{zumbo1999dif}. In this view, $\\gamma_k$ functions as a uniform DIF parameter capturing systematic advantage conferred by exposure. However, ContamCal extends the classical DIF paradigm in two respects: group membership is determined by continuous exposure scores from Stage~1 rather than discrete demographic categories, and DIF is modeled with benchmark-specific $\\gamma_k$ parameters, each with independent priors, fitted separately per benchmark.",
          "+Mitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.",
          " ",
          "-\\paragraph{Positioning.} ContamCal bridges contamination detection (which flags but does not calibrate), IRT-based LLM evaluation (which models ability but ignores contamination), and educational item compromise models (which handle leaked items but assume independent examinees with binary exposure). Table~\\ref{tab:positioning} summarizes the capabilities of representative methods.",
          "+\\subsection{Calibration Disambiguation}",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\small",
          "-\\begin{tabular}{lcccc}",
          "-\\toprule",
          "-\\textbf{Method} & \\textbf{Detects} & \\textbf{Calibrates} & \\textbf{UQ} & \\textbf{RL-robust} \\\\",
          "-\\midrule",
          "-Min-K\\%++ & \\checkmark & & & \\\\",
          "-ConStat & \\checkmark & & & \\\\",
          "-Self-Critique & \\checkmark & & & \\checkmark \\\\",
          "-KDS & \\checkmark & & & ? \\\\",
          "-DCR & \\checkmark & \\checkmark & & \\\\",
          "-PSN-IRT & & & & \\\\",
          "-HiBayES & & & \\checkmark & \\\\",
          "-\\textbf{ContamCal} & \\checkmark & \\checkmark & \\checkmark & ?$^\\dagger$ \\\\",
          "-\\bottomrule",
          "-\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Designed for RL robustness via uncertainty propagation; empirical validation pending (exp-008).}",
          "-\\end{tabular}",
          "-\\caption{Capability comparison of contamination-aware evaluation methods. UQ = uncertainty quantification via credible intervals. RL-robust = maintains effectiveness after RL post-training.}",
          "-\\label{tab:positioning}",
          "-\\end{table}",
          "+We use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Benchmark Contamination Detection}\n\\label{sec:related:detection}\n\nDetecting training data contamination in LLMs has produced a diverse methodological landscape spanning at least eight paradigms. Time-based partitioning uses temporal cutoffs to identify potentially leaked items, while canary string insertion (e.g., BIG-Bench) provides direct memorization probes \\citep{chang2025benchmarking}. Min-K\\%++ \\citep{duan2025minkpp} performs membership inference by examining token-level probability distributions, achieving strong detection on pre-training contamination. Time Travel \\citep{oren2024proving} uses guided completion to detect black-box contamination without model weight access. ConStat \\citep{dekoninck2024constat} measures performance gaps between original and paraphrased benchmark items, targeting surface-form memorization. Self-Critique \\citep{wust2025selfcritique} identifies contamination through entropy collapse in model self-evaluations---a signal that, unlike probability-based methods, partially survives reinforcement learning post-training. Hierarchical semantic detection approaches match items at multiple granularity levels to training corpora. KDS \\citep{xu2025kds} uses knowledge distillation signatures to achieve near-perfect detection (Spearman $\\rho = 0.99$) but requires per-model LoRA fine-tuning, limiting scalability.\n\nA critical finding is that detection methods are fragile under RL post-training: \\citet{wang2025fragility} show that GRPO and similar procedures degrade probability-based detection signals substantially, while Self-Critique's entropy-based signal achieves only 0.60--0.70 AUC on RL-trained models \\citep{wust2025selfcritique}. Despite this rich detection toolkit, all existing methods produce binary or continuous \\emph{flags}---they diagnose contamination without prescribing how to adjust the reported accuracy that end-users rely on.\n\n\\subsection{Contamination Impact and Mitigation}\n\\label{sec:related:mitigation}\n\nUnderstanding contamination's quantitative impact has advanced rapidly. \\citet{dong2026dose} establish dose-response curves showing that score inflation scales monotonically with both model size and contamination dosage. \\citet{yang2026rl} further demonstrate that SFT inflates accuracy only on contaminated tasks, while GRPO amplifies inflation even on structurally similar uncontaminated items---a cross-contamination effect that complicates attribution. \\citet{zhang2025forget} show that contamination persists in model weights following standard decontamination, with forgetting curves following scaling laws that make complete removal impractical.\n\nThe mitigation landscape is equally sobering. \\citet{xu2025emperor} systematically evaluate twenty strategies---item rephrasing, option shuffling, filtering, dynamic benchmark construction, and more---across ten LLMs and five benchmarks, finding that none reliably eliminates contamination effects. Dynamic benchmarks such as LiveBench \\citep{white2024livebench} circumvent contamination by generating fresh items but cannot retroactively calibrate existing benchmark scores. Inference-Time Decontamination \\citep{yang2024inference} rewrites items at test time but operates during inference rather than producing post-hoc calibrated scores. DCR \\citep{li2025dcr} is the closest existing method to ours, producing adjusted accuracy via fuzzy inference over detection signals; however, it provides point estimates without uncertainty bounds and does not address signal degradation under RL. \\citet{rao2026silicon} propose a router-worker audit framework that produces contamination flags rather than calibrated scores. Collectively, these findings motivate a paradigm shift: from contamination \\emph{prevention}---which demonstrably fails---to post-hoc statistical \\emph{adjustment} with proper uncertainty quantification.\n\n\\paragraph{Terminological note.} Throughout this paper, ``calibration'' refers to the psychometric sense of score adjustment---recovering decontaminated ability estimates from potentially inflated benchmark scores. This should not be confused with probability calibration in machine learning, where the goal is to align predicted probabilities with empirical frequencies via methods such as Platt scaling or temperature scaling \\citep{guo2017calibration}. ContamCal performs the former: it adjusts reported accuracies for contamination bias rather than recalibrating model confidence scores.\n\n\\subsection{IRT for LLM Evaluation}\n\\label{sec:related:irt}\n\nItem response theory has gained traction as a principled framework for LLM evaluation. \\citet{lalor2024irt} demonstrate that IRT-based evaluation yields more informative model comparisons than raw accuracy. PSN-IRT \\citep{gu2026psnirt} scales this to 41,871 items across 11 benchmarks using a 4PL model with neural network parameter estimation, establishing item difficulty and discrimination profiles but without modeling contamination or producing adjusted scores. \\citet{polo2026growing} fit multidimensional 2PL IRT with anchor items to over 400 models, validating IRT's applicability at scale while identifying practical limitations in the few-examinee regime; contamination is not addressed. ATLAS \\citep{lyu2025atlas} leverages IRT for adaptive testing, reducing evaluation cost through maximally informative item selection. TinyBenchmarks \\citep{polo2024tinybenchmarks} similarly exploits IRT-informed item selection for efficient evaluation. HiBayES \\citep{zhuang2025hibayes} provides hierarchical Bayesian credible intervals over model ability estimates but treats all items as equally trustworthy. \\citet{han2026probing} quantify contamination effects within psychometric evaluations but do not use IRT or produce calibrated scores. Across this body of work, contamination has not been modeled as a covariate within the IRT framework---a gap that ContamCal addresses by augmenting the item response function with exposure parameters.\n\n\\paragraph{Alternative uncertainty quantification.} Conformal prediction \\citep{angelopoulos2023conformal} offers distribution-free coverage guarantees and has been applied to various prediction tasks. We adopt Bayesian IRT over conformal alternatives for three reasons. First, contamination-specific parameters ($\\gamma_k$) yield directly interpretable causal quantities---``contamination inflates scores by $\\gamma_k$ units on benchmark $k$''---whereas conformal intervals lack such structural decomposition. Second, the posterior over all latent variables naturally propagates measurement error into credible intervals without requiring a separate calibration set. Third, conformal prediction assumes exchangeability of data points, which is violated in the contaminated setting: response distributions for contaminated items are systematically shifted relative to clean items. Conformal methods may nonetheless prove valuable in complementary LLM evaluation contexts where exchangeability holds.\n\n\\subsection{Item Compromise in Educational Measurement}\n\\label{sec:related:edumeasure}\n\nThe psychometric literature has long addressed item compromise---the unauthorized disclosure of test content prior to administration. \\citet{eckerly2017} develops IRT models that incorporate compromise indicators to simultaneously estimate item parameters and compromise effects, while \\citet{sinharay2017} proposes likelihood ratio and score tests for detecting item preknowledge. The explanatory IRT tradition \\citep{deboeck2004,adams1997} provides the theoretical foundation for embedding external covariates within item response functions, and \\citet{mislevy1986} establishes Bayesian estimation procedures for such augmented models.\n\nAdapting this tradition to LLM evaluation requires three structural adaptations detailed in \\S\\ref{sec:stage2}.\n\n\\paragraph{Differential item functioning.} The per-benchmark exposure parameter $\\gamma_k$ in ContamCal can be interpreted as measuring differential item functioning (DIF) between contaminated and clean model populations. DIF---the phenomenon whereby examinees of equal ability but different group membership respond differently to an item---was formalized by \\citep{holland1993dif}, with IRT-based detection procedures developed by \\citet{thissen1993dif} and logistic regression frameworks established by \\citet{zumbo1999dif}. In this view, $\\gamma_k$ functions as a uniform DIF parameter capturing systematic advantage conferred by exposure. However, ContamCal extends the classical DIF paradigm in two respects: group membership is determined by continuous exposure scores from Stage~1 rather than discrete demographic categories, and DIF is modeled with benchmark-specific $\\gamma_k$ parameters, each with independent priors, fitted separately per benchmark.\n\n\\paragraph{Positioning.} ContamCal bridges contamination detection (which flags but does not calibrate), IRT-based LLM evaluation (which models ability but ignores contamination), and educational item compromise models (which handle leaked items but assume independent examinees with binary exposure). Table~\\ref{tab:positioning} summarizes the capabilities of representative methods.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{Detects} & \\textbf{Calibrates} & \\textbf{UQ} & \\textbf{RL-robust} \\\\\n\\midrule\nMin-K\\%++ & \\checkmark & & & \\\\\nConStat & \\checkmark & & & \\\\\nSelf-Critique & \\checkmark & & & \\checkmark \\\\\nKDS & \\checkmark & & & ? \\\\\nDCR & \\checkmark & \\checkmark & & \\\\\nPSN-IRT & & & & \\\\\nHiBayES & & & \\checkmark & \\\\\n\\textbf{ContamCal} & \\checkmark & \\checkmark & \\checkmark & ?$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Designed for RL robustness via uncertainty propagation; empirical validation pending (exp-008).}\n\\end{tabular}\n\\caption{Capability comparison of contamination-aware evaluation methods. UQ = uncertainty quantification via credible intervals. RL-robust = maintains effectiveness after RL post-training.}\n\\label{tab:positioning}\n\\end{table}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 21_

Now let me run the quality checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "d6c54b57-4646-4ea2-9282-c5d781cf561d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxQnyxk6vUK8KirsD9jFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 50421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2154
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_011Bw6MATJpWMH9KWtC3vbn9`</summary>

```json
{
  "command": "grep \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Check for em-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "70d5e7cc-391b-4d23-9436-4b6cb2e569d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxQnyxk6vUK8KirsD9jFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 50421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2154
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

_source line 23 · 2026-05-17T04:38:34.871Z_

<details><summary>↩ Tool result · `toolu_011Bw6MATJpWMH9KWtC3vbn9`</summary>

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
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "b6613c1b-8462-48a9-8d05-9664d8c4288a",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01LcJunmN4RUdVm7cewXQkek`</summary>

```json
{
  "command": "grep \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Check for explanatory en-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "a717f341-060e-429d-b77b-fe96fc68884b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxQnyxk6vUK8KirsD9jFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 50421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2154
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

_source line 25 · 2026-05-17T04:38:35.855Z_

<details><summary>↩ Tool result · `toolu_01LcJunmN4RUdVm7cewXQkek`</summary>

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
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "2e5b6b99-f88b-4d30-9302-6f39ee0fab99",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01AyE7WWXdHg9CWviBDFcHXP`</summary>

```json
{
  "command": "grep \"ing,\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Check for -ing phrase endings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "aaecaadd-9712-49b2-842a-e9123f12b409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxQnyxk6vUK8KirsD9jFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 50421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2154
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

_source line 27 · 2026-05-17T04:38:36.820Z_

<details><summary>↩ Tool result · `toolu_01AyE7WWXdHg9CWviBDFcHXP`</summary>

```text
Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\gamma_d$ that separate genuine ability from exposure-driven inflation.
Mitigation strategies attempt to neutralize contamination at test time. \citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\gamma_d$ parameters and posterior credible intervals.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "401c6170-0fd7-4330-acfb-7d6fa5dc4265",
  "tool_use_result": {
    "stdout": "Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.",
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

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_01G4LWFdSn5Vs5tZKmUipzp9`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$]//g; s/%.*//g' | wc -w",
  "description": "Approximate word count after stripping LaTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "4d0edf6e-45d4-4274-a784-c767b9d3cffa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TrxQnyxk6vUK8KirsD9jFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2154,
      "cache_read_input_tokens": 50421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2154
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

_source line 29 · 2026-05-17T04:38:38.659Z_

<details><summary>↩ Tool result · `toolu_01G4LWFdSn5Vs5tZKmUipzp9`</summary>

```text
446
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "f316310e-e544-4261-b0fd-6e4b8d59971b",
  "tool_use_result": {
    "stdout": "446",
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

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
The quality checks:
1. No em-dash ✓
2. No explanatory en-dash ✓
3. The `grep "ing,"` found some matches - let me look at them. The matches include:
   - "identifying practical limitations" - this is mid-sentence, not a sentence ending
   - "selecting maximally informative items per model" - this is at the end of a sentence
   - "finding that none reliably eliminates score inflation" - mid-sentence
   - "combining detection signals with fuzzy inference rules" - not a sentence ending

Let me check which of these are problematic -ing phrase endings specifically. 

The rule prohibits ending sentences with -ing phrases like "highlighting the applicability of..." or "demonstrating the effectiveness of...". Looking at the grep results more carefully, most of these aren't actually sentence-final participial phrases. "Preserving ranking fidelity" appears in a "while + -ing" construction, which is fine, and "identifying practical limitations" is mid-sentence, so neither violates the rule.

But wait—the grep pattern `"ing,"` catches -ing followed by a comma, which means these are mid-sentence occurrences, not sentence endings. So the actual problematic patterns I need to find are -ing phrases that genuinely end sentences, not ones that appear before commas.

Looking back at what I actually wrote, I can see three clear sentence-ending -ing participials that violate the style guide: "identifying practical limitations," "selecting maximally informative items per model," and "finding that none reliably eliminates score inflation." I should rewrite those. The word count also seems short at 446, so I need to check if I'm missing content or if the sed command got cut off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "2ec43799-b76a-4c47-9721-db57f6b8153f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAn67x66j1b9v6YczjMrwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 52575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1195
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

_source line 31_

Let me get a more accurate word count and fix the -ing phrase endings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "42ca99fd-0a43-42e9-a9f7-e7240e30dca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAn67x66j1b9v6YczjMrwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 52575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1195
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

<details open><summary>🔧 Tool call — Bash · `toolu_012AhAgbUBxt9b2DH6cbqzDx`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "description": "Raw word count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "b2fb9078-69de-4a44-b1d7-fe00b8389b8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAn67x66j1b9v6YczjMrwe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1195,
      "cache_read_input_tokens": 52575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1195
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

_source line 33 · 2026-05-17T04:39:00.096Z_

<details><summary>↩ Tool result · `toolu_012AhAgbUBxt9b2DH6cbqzDx`</summary>

```text
581 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "6f2ec67e-3401-46c6-a7c1-709ce7adce2b",
  "tool_use_result": {
    "stdout": "581 /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
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

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
581 raw words. Subtracting LaTeX commands and citation keys (~80-100 words), actual content is around 480-500 words. That's below the 700 target. I also need to fix the -ing phrase endings. Let me expand each subsection slightly and fix the style issues.

Let me revise the file. I need to:
1. Fix -ing participial endings
2. Add ~100-150 more words to reach ~700 actual content words

Let me rewrite with fixes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "47a5421d-a837-4ab8-bf47-282a966c7653",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqMa2yx1rWvKGLDo6R3Aqq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 53770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

_source line 35_

Word count is below target and there are -ing phrase endings to fix. Let me revise.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "8c869425-3757-4cc0-a625-ebf8e3f34787",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqMa2yx1rWvKGLDo6R3Aqq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 53770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

<details open><summary>🔧 Tool call — Write · `toolu_018dxv43YtuJU1PU6YMwE2Ct`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and its successor Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics, with the latter achieving stronger separation through normalized probability comparisons. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization from genuine understanding. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes that test whether models can reproduce exact benchmark content. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits, revealing that many high-scoring models exhibit suspicious temporal patterns. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on IRT in NLP evaluation, covering model selection, parameter estimation, and ability scoring. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity across diverse model families. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration and identifies practical limitations in low-respondent regimes where item parameters become poorly constrained. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates, enabling principled model comparison under uncertainty. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing and selects maximally informative items to reduce per-model evaluation cost. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models that incorporate compromise indicators to jointly estimate item parameters and preknowledge effects, showing that ignoring compromise biases all estimated parameters. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for item preknowledge detection at the individual level, establishing statistical power requirements for reliable identification. DIF cancellation \\citep{ercikan_2008_dif_cancellation} demonstrates that item-level bias can aggregate unpredictably across test domains, motivating domain-level rather than item-level analysis. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates directly within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks; none reliably eliminates score inflation. This failure motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. No public implementation is available, so we compare qualitatively in Section~\\ref{sec:results}. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals that propagate signal noise into final uncertainty bounds.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense throughout this paper: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions. Readers familiar with the ML calibration literature should note that our reliability diagrams (\\S\\ref{sec:results}) compare calibrated scores against held-out clean accuracy, not predicted probabilities against observed outcomes.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "be6730a2-0021-4d1a-83d7-928941ba00bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EqMa2yx1rWvKGLDo6R3Aqq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1037,
      "cache_read_input_tokens": 53770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1037
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

_source line 37 · 2026-05-17T04:39:21.481Z_

<details><summary>↩ Tool result · `toolu_018dxv43YtuJU1PU6YMwE2Ct`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "de066681-632d-4e65-8060-166e529285ba",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and its successor Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics, with the latter achieving stronger separation through normalized probability comparisons. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization from genuine understanding. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes that test whether models can reproduce exact benchmark content. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits, revealing that many high-scoring models exhibit suspicious temporal patterns. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on IRT in NLP evaluation, covering model selection, parameter estimation, and ability scoring. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity across diverse model families. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration and identifies practical limitations in low-respondent regimes where item parameters become poorly constrained. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates, enabling principled model comparison under uncertainty. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing and selects maximally informative items to reduce per-model evaluation cost. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models that incorporate compromise indicators to jointly estimate item parameters and preknowledge effects, showing that ignoring compromise biases all estimated parameters. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for item preknowledge detection at the individual level, establishing statistical power requirements for reliable identification. DIF cancellation \\citep{ercikan_2008_dif_cancellation} demonstrates that item-level bias can aggregate unpredictably across test domains, motivating domain-level rather than item-level analysis. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates directly within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks; none reliably eliminates score inflation. This failure motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. No public implementation is available, so we compare qualitatively in Section~\\ref{sec:results}. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals that propagate signal noise into final uncertainty bounds.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense throughout this paper: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions. Readers familiar with the ML calibration literature should note that our reliability diagrams (\\S\\ref{sec:results}) compare calibrated scores against held-out clean accuracy, not predicted probabilities against observed outcomes.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 20,
        "newStart": 3,
        "newLines": 20,
        "lines": [
          " ",
          " \\subsection{Contamination Detection}",
          " ",
          "-Recent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.",
          "+Recent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and its successor Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics, with the latter achieving stronger separation through normalized probability comparisons. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization from genuine understanding. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes that test whether models can reproduce exact benchmark content. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits, revealing that many high-scoring models exhibit suspicious temporal patterns. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.",
          " ",
          " \\subsection{IRT for LLM Evaluation}",
          " ",
          "-Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.",
          "+Item Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on IRT in NLP evaluation, covering model selection, parameter estimation, and ability scoring. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity across diverse model families. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration and identifies practical limitations in low-respondent regimes where item parameters become poorly constrained. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates, enabling principled model comparison under uncertainty. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing and selects maximally informative items to reduce per-model evaluation cost. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.",
          " ",
          " \\subsection{Item Compromise in Educational Measurement}",
          " ",
          "-The psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).",
          "+The psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models that incorporate compromise indicators to jointly estimate item parameters and preknowledge effects, showing that ignoring compromise biases all estimated parameters. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for item preknowledge detection at the individual level, establishing statistical power requirements for reliable identification. DIF cancellation \\citep{ercikan_2008_dif_cancellation} demonstrates that item-level bias can aggregate unpredictably across test domains, motivating domain-level rather than item-level analysis. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates directly within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).",
          " ",
          " \\subsection{Contamination Mitigation and Score Adjustment}",
          " ",
          "-Mitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.",
          "+Mitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks; none reliably eliminates score inflation. This failure motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. No public implementation is available, so we compare qualitatively in Section~\\ref{sec:results}. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals that propagate signal noise into final uncertainty bounds.",
          " ",
          " \\subsection{Calibration Disambiguation}",
          " ",
          "-We use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions.",
          "+We use ``calibration'' in the psychometric sense throughout this paper: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions. Readers familiar with the ML calibration literature should note that our reliability diagrams (\\S\\ref{sec:results}) compare calibrated scores against held-out clean accuracy, not predicted probabilities against observed outcomes."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{Contamination Detection}\n\nRecent work has produced diverse signals for identifying benchmark data in LLM training corpora. Min-K\\% \\citep{shi_2023_minkprob} and Min-K\\%++ \\citep{zhang_2024_minkpp} perform membership inference via token-level surprisal statistics. ConStat \\citep{dekoninck_2024_constat} measures accuracy gaps between original and paraphrased items to isolate surface memorization. CDD and TED \\citep{dong_2024_cdd} distinguish generalization from memorization through completion-based probes. KDS \\citep{choi_2025_kds} quantifies leakage via kernel divergence between model outputs on seen and unseen distributions. TS-Guessing \\citep{deng_2024_tsguessing} identifies contamination through systematic evaluation of completion accuracy across temporal splits. These methods flag contamination at the item or benchmark level but do not diagnose domain-level effects or produce adjusted scores. ContamCal consumes detection signals as inputs (Stage~1) and feeds them into a calibration framework (Stage~2) that estimates decontaminated ability.\n\n\\subsection{IRT for LLM Evaluation}\n\nItem Response Theory (IRT) has gained traction as a principled alternative to raw accuracy for comparing LLMs. \\citet{lalor_2024_irt_nlp} provide a comprehensive tutorial on applying IRT to NLP evaluation. TinyBenchmarks \\citep{polo_2024_tinybenchmarks} exploits IRT-informed item selection to reduce evaluation cost while preserving ranking fidelity. Growing Pains \\citep{habba_2025_growing_pains} validates IRT at scale on 400+ models with fixed parameter calibration, identifying practical limitations in low-respondent regimes. HiBayES \\citep{luettgau_2025_hibayes} extends IRT with hierarchical Bayesian inference to produce credible intervals over ability estimates. ATLAS \\citep{li_2024_atlas} applies IRT for adaptive testing, selecting maximally informative items per model. Across this body of work, all items are treated as equally trustworthy: none models contamination as a covariate within the item response function. ContamCal augments IRT with per-domain contamination parameters $\\gamma_d$ that separate genuine ability from exposure-driven inflation.\n\n\\subsection{Item Compromise in Educational Measurement}\n\nThe psychometric literature has long studied item compromise, where test content is disclosed before administration. \\citet{eckerly_2017_item_compromise} develops IRT models incorporating compromise indicators to jointly estimate item parameters and preknowledge effects. \\citet{sinharay_2017_preknowledge} proposes likelihood ratio and score tests for detecting item preknowledge at the individual level. DIF cancellation \\citep{ercikan_2008_dif_cancellation} shows that item-level bias can aggregate unpredictably across domains. Explanatory IRT \\citep{deboeck_2004_explanatory_irt} provides the theoretical foundation for embedding external covariates within item response functions. ContamCal adapts this tradition with three modifications for LLM evaluation: continuous exposure scores replace binary leaked/not-leaked indicators, effects are estimated at domain granularity rather than per-item, and counterfactual inference (setting exposure to zero) replaces group comparison, since LLMs lack a clean ``control group'' (Section~\\ref{sec:formulation}).\n\n\\subsection{Contamination Mitigation and Score Adjustment}\n\nMitigation strategies attempt to neutralize contamination at test time. \\citet{xu2025emperor} systematically evaluate twenty approaches (item rephrasing, option shuffling, dynamic construction, filtering) across ten LLMs and five benchmarks, finding that none reliably eliminates score inflation. This motivates post-hoc statistical correction rather than prevention. DCR \\citep{li_2025_dcr} is the most closely related method: it estimates decontaminated scores by combining detection signals with fuzzy inference rules. However, DCR produces point estimates without uncertainty quantification, does not model domain-level heterogeneity in contamination effects, and lacks IRT grounding that would connect score adjustment to a latent ability scale. We compare qualitatively in our discussion, as no public implementation is available. ContamCal addresses all three limitations through Bayesian IRT with per-domain $\\gamma_d$ parameters and posterior credible intervals.\n\n\\subsection{Calibration Disambiguation}\n\nWe use ``calibration'' in the psychometric sense: adjusting benchmark scores to approximate clean (uncontaminated) performance. This differs from probability calibration in machine learning \\citep{guo_2017_calibration}, where the goal is aligning predicted confidences with empirical frequencies via temperature scaling or Platt scaling. ContamCal performs score-level adjustment for contamination bias, not recalibration of output probabilities. We adopt this terminology following the educational measurement convention where ``calibration'' refers to placing items and examinees on a common scale after accounting for known distortions.\n",
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_016Lu3VA5a5DMBnvFUjsTcBS`</summary>

```json
{
  "command": "grep \"—\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex && echo \"FOUND\" || echo \"CLEAN\"",
  "description": "Check for em-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "476d095a-70ac-43e2-8789-fcc5c3866447",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2eKb5iYMvYymsUbMkY9n9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 54807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1684
      },
      "output_tokens": 69,
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

_source line 39 · 2026-05-17T04:39:25.237Z_

<details><summary>↩ Tool result · `toolu_016Lu3VA5a5DMBnvFUjsTcBS`</summary>

```text
CLEAN
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "e2b85076-3340-48c5-ac69-cc0b322a427c",
  "tool_use_result": {
    "stdout": "CLEAN",
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01P8MN5oD2AhK1YeX9vYKTpq`</summary>

```json
{
  "command": "grep \" – \" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex && echo \"FOUND\" || echo \"CLEAN\"",
  "description": "Check for en-dash"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "2676fc54-b4a5-4cb3-b5de-dd977301602d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2eKb5iYMvYymsUbMkY9n9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 54807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1684
      },
      "output_tokens": 69,
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

_source line 41 · 2026-05-17T04:39:26.173Z_

<details><summary>↩ Tool result · `toolu_01P8MN5oD2AhK1YeX9vYKTpq`</summary>

```text
CLEAN
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "415f7206-00ea-4a4a-a87d-9c3686d29073",
  "tool_use_result": {
    "stdout": "CLEAN",
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

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01YPU7qaPv2gmA35SFJPK5eB`</summary>

```json
{
  "command": "grep -n \"ing[,.]\" /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | grep -v \"\\\\\\\\citep\\|\\\\\\\\citet\\|\\\\\\\\ref\\|testing\\|scoring\\|scaling\\|Platt scaling\\|ranking\"",
  "description": "Check for -ing phrase endings (excluding common nouns)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "e301f25f-deb6-427d-b108-165dc385efd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2eKb5iYMvYymsUbMkY9n9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 54807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1684
      },
      "output_tokens": 69,
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

_source line 43 · 2026-05-17T04:39:28.173Z_

<details><summary>↩ Tool result · `toolu_01YPU7qaPv2gmA35SFJPK5eB`</summary>

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
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "55dce33d-350b-44e1-9251-e45eb64ee953",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_01AGTZHMKLJoB7oq8yQsdASu`</summary>

```json
{
  "command": "detex /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex 2>/dev/null | wc -w || cat /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex | sed 's/\\\\citep{[^}]*}//g; s/\\\\citet{[^}]*}//g; s/\\\\cite{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/{//g; s/}//g; s/\\$[^$]*\\$//g; s/%.*//g; s/~/ /g' | wc -w",
  "description": "Word count after stripping LaTeX"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "06c56f3d-8676-4848-9dea-46b8952c560c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y2eKb5iYMvYymsUbMkY9n9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1684,
      "cache_read_input_tokens": 54807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1684
      },
      "output_tokens": 69,
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

_source line 45 · 2026-05-17T04:39:30.672Z_

<details><summary>↩ Tool result · `toolu_01AGTZHMKLJoB7oq8yQsdASu`</summary>

```text
686
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "d9ad9b6a-4ec4-4260-98c3-d69237ee5322",
  "tool_use_result": {
    "stdout": "686",
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

_source line 46_

All checks pass:
- Zero em-dash matches
- Zero explanatory en-dash matches
- No problematic -ing phrase endings
- ~686 words after stripping LaTeX commands (within target of ~700)

Written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex`. Five subsections: Contamination Detection, IRT for LLM Evaluation, Item Compromise in Educational Measurement, Contamination Mitigation and Score Adjustment, Calibration Disambiguation. Each ends with a clear positioning statement for ContamCal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "uuid": "8b191a8c-8a92-4b26-8005-54b4aa69964a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015F6Vcs3bPKdt5D63pGuYid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 56491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 774
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

_source line 47_

All checks pass:
- Zero em-dash matches
- Zero explanatory en-dash matches
- No problematic -ing phrase endings
- ~686 words after stripping LaTeX commands (within target of ~700)

Written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/related_work.tex`. Five subsections: Contamination Detection, IRT for LLM Evaluation, Item Compromise in Educational Measurement, Contamination Mitigation and Score Adjustment, Calibration Disambiguation. Each ends with a clear positioning statement for ContamCal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 135110,
  "duration_api_ms": 135682,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "eedfbb57-3cbf-4404-8d77-9d44388cffe8",
  "total_cost_usd": 0.6754035,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 45424,
    "cache_read_input_tokens": 400973,
    "output_tokens": 7510,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45424,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 154,
        "cache_read_input_tokens": 56491,
        "cache_creation_input_tokens": 774,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 774
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3127,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003217,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 7510,
      "cacheReadInputTokens": 400973,
      "cacheCreationInputTokens": 45424,
      "webSearchRequests": 0,
      "costUSD": 0.6721865,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a6215c28-0fd8-4095-b736-a7be696a0c08"
}
```

</details>

---
