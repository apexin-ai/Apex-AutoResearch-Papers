# paper research bib sync

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_research_bib_sync_20260517T034849.log`
- **Structured JSON:** [`0530bad1ced6abd59d9b.json`](../../sessions/05/0530bad1ced6abd59d9b.json)

## Before a recorded user message

25 recorded events

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
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
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
  "uuid": "850d6bcc-12b1-44af-8c01-1f4436075dae",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/memory/"
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
    "resetsAt": 1778995800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3488886c-4a1c-4a9e-af1a-63fe48136b72",
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the literature_map.yaml and the existing references.bib to understand what we're working with.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "8b882915-71d0-41ee-8e52-c4d9689e9c73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZr2qB6RqujHiVur35RQb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14662,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14662
      },
      "output_tokens": 43,
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

Reading the input files to understand current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "8842c193-c8be-41e9-8289-0ca868228093",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZr2qB6RqujHiVur35RQb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14662,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14662
      },
      "output_tokens": 43,
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

<details open><summary>🔧 Tool call — Read · `toolu_014af3oGtMfkF91YEhgm1rmn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "4b6da813-0ebd-4e1c-bb64-6b06d7393ac9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZr2qB6RqujHiVur35RQb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14662,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14662
      },
      "output_tokens": 43,
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

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01TdkooV7RyKDSw8EbpEdvmr`</summary>

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
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "6d499aae-0e32-4cbd-8503-0512304b6340",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VZr2qB6RqujHiVur35RQb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14662,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14662
      },
      "output_tokens": 43,
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

_source line 8 · 2026-05-17T03:49:04.535Z_

<details><summary>↩ Tool result · `toolu_01TdkooV7RyKDSw8EbpEdvmr`</summary>

```text
1	% ============================================================
2	% Core Methodology — Educational Measurement & IRT
3	% ============================================================
4	
5	@book{lord1980,
6	  author    = {Lord, Frederic M.},
7	  title     = {Applications of Item Response Theory to Practical Testing Problems},
8	  publisher = {Lawrence Erlbaum Associates},
9	  year      = {1980},
10	  address   = {Hillsdale, NJ}
11	}
12	
13	@article{eckerly2017,
14	  author  = {Eckerly, Carol},
15	  title   = {Detecting Item Compromise in the Context of Item Response Theory},
16	  journal = {Applied Psychological Measurement},
17	  volume  = {41},
18	  number  = {2},
19	  pages   = {87--101},
20	  year    = {2017}
21	}
22	
23	@article{sinharay2017,
24	  author  = {Sinharay, Sandip},
25	  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},
26	  journal = {Journal of Educational and Behavioral Statistics},
27	  volume  = {42},
28	  number  = {1},
29	  pages   = {46--68},
30	  year    = {2017}
31	}
32	
33	@book{deboeck2004,
34	  author    = {De Boeck, Paul and Wilson, Mark},
35	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
36	  publisher = {Springer},
37	  year      = {2004},
38	  address   = {New York}
39	}
40	
41	@article{adams1997,
42	  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},
43	  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},
44	  journal = {Applied Psychological Measurement},
45	  volume  = {21},
46	  number  = {1},
47	  pages   = {1--23},
48	  year    = {1997}
49	}
50	
51	@article{mislevy1986,
52	  author  = {Mislevy, Robert J.},
53	  title   = {Bayes Modal Estimation in Item Response Models},
54	  journal = {Psychometrika},
55	  volume  = {51},
56	  number  = {2},
57	  pages   = {177--195},
58	  year    = {1986}
59	}
60	
61	@article{sanmartin2009,
62	  author  = {San Mart\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},
63	  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},
64	  journal = {Psychometrika},
65	  volume  = {74},
66	  number  = {2},
67	  pages   = {349--367},
68	  year    = {2009}
69	}
70	
71	@article{maris2009,
72	  author  = {Maris, Gunter and Bechger, Timo},
73	  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},
74	  journal = {Measurement},
75	  volume  = {7},
76	  number  = {2},
77	  pages   = {75--88},
78	  year    = {2009}
79	}
80	
81	@inproceedings{cormack2009,
82	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
83	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
84	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
85	  pages     = {758--759},
86	  year      = {2009},
87	  publisher = {ACM}
88	}
89	
90	% ============================================================
91	% Bayesian Inference & Diagnostics
92	% ============================================================
93	
94	@article{hoffman2014,
95	  author  = {Hoffman, Matthew D. and Gelman, Andrew},
96	  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},
97	  journal = {Journal of Machine Learning Research},
98	  volume  = {15},
99	  number  = {47},
100	  pages   = {1593--1623},
101	  year    = {2014}
102	}
103	
104	@article{carpenter2017,
105	  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},
106	  title   = {Stan: A Probabilistic Programming Language},
107	  journal = {Journal of Statistical Software},
108	  volume  = {76},
109	  number  = {1},
110	  pages   = {1--32},
111	  year    = {2017}
112	}
113	
114	@article{talts2018sbc,
115	  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},
116	  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},
117	  journal       = {arXiv preprint},
118	  year          = {2018},
119	  eprint        = {1804.06788},
120	  archiveprefix = {arXiv}
121	}
122	
123	@article{ulitzsch2022,
124	  author  = {Ulitzsch, Esther and Nestler, Steffen},
125	  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},
126	  journal = {British Journal of Mathematical and Statistical Psychology},
127	  volume  = {75},
128	  number  = {3},
129	  pages   = {421--447},
130	  year    = {2022}
131	}
132	
133	% ============================================================
134	% Contamination Detection Methods
135	% ============================================================
136	
137	@inproceedings{duan2025minkpp,
138	  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},
139	  title     = {{Min-K\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},
140	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},
141	  year      = {2025}
142	}
143	
144	@inproceedings{dekoninck2024constat,
145	  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},
146	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
147	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
148	  year      = {2024}
149	}
150	
151	@article{wust2025selfcritique,
152	  author        = {W\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},
153	  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},
154	  journal       = {arXiv preprint},
155	  year          = {2025},
156	  eprint        = {2510.09259},
157	  archiveprefix = {arXiv}
158	}
159	
160	@inproceedings{xu2025kds,
161	  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},
162	  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},
163	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
164	  year      = {2025},
165	  note      = {arXiv:2502.00678}
166	}
167	
168	@inproceedings{oren2024proving,
169	  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},
170	  title     = {Proving Test Set Contamination in Black Box Language Models},
171	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
172	  year      = {2024}
173	}
174	
175	% ============================================================
176	% Contamination Analysis & Mitigation
177	% ============================================================
178	
179	@inproceedings{xu2025emperor,
180	  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},
181	  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},
182	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
183	  year      = {2025},
184	  note      = {arXiv:2503.16402}
185	}
186	
187	@article{dong2026dose,
188	  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},
189	  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},
190	  journal       = {arXiv preprint},
191	  year          = {2026},
192	  eprint        = {2601.04301},
193	  archiveprefix = {arXiv}
194	}
195	
196	@article{yang2026rl,
197	  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},
198	  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},
199	  journal       = {arXiv preprint},
200	  year          = {2026},
201	  eprint        = {2601.06103},
202	  archiveprefix = {arXiv}
203	}
204	
205	@article{wang2025fragility,
206	  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},
207	  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},
208	  journal       = {arXiv preprint},
209	  year          = {2025},
210	  eprint        = {2510.02386},
211	  archiveprefix = {arXiv}
212	}
213	
214	@inproceedings{zhang2025forget,
215	  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},
216	  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},
217	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
218	  year      = {2025}
219	}
220	
221	% ============================================================
222	% IRT for LLM Evaluation
223	% ============================================================
224	
225	@inproceedings{gu2026psnirt,
226	  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
227	  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},
228	  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},
229	  year      = {2026}
230	}
231	
232	@article{polo2026growing,
233	  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},
234	  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},
235	  journal       = {arXiv preprint},
236	  year          = {2026},
237	  eprint        = {2604.12843},
238	  archiveprefix = {arXiv}
239	}
240	
241	@article{lyu2025atlas,
242	  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},
243	  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},
244	  journal       = {arXiv preprint},
245	  year          = {2025},
246	  eprint        = {2511.04689},
247	  archiveprefix = {arXiv}
248	}
249	
250	@article{zhuang2025hibayes,
251	  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},
252	  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},
253	  journal       = {arXiv preprint},
254	  year          = {2025},
255	  eprint        = {2505.05602},
256	  archiveprefix = {arXiv}
257	}
258	
259	@inproceedings{lalor2024irt,
260	  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},
261	  title     = {Benchmarking Large Language Models with Item Response Theory},
262	  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},
263	  year      = {2024}
264	}
265	
266	% ============================================================
267	% Score Adjustment & Decontamination
268	% ============================================================
269	
270	@inproceedings{li2025dcr,
271	  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},
272	  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},
273	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
274	  year      = {2025}
275	}
276	
277	@inproceedings{yang2024inference,
278	  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},
279	  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},
280	  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},
281	  year      = {2024}
282	}
283	
284	@article{rao2026silicon,
285	  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},
286	  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},
287	  journal       = {arXiv preprint},
288	  year          = {2026},
289	  eprint        = {2603.21636},
290	  archiveprefix = {arXiv}
291	}
292	
293	% ============================================================
294	% Benchmarking — Surveys & Infrastructure
295	% ============================================================
296	
297	@inproceedings{hendrycks2021mmlu,
298	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
299	  title     = {Measuring Massive Multitask Language Understanding},
300	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
301	  year      = {2021}
302	}
303	
304	@article{cobbe2021gsm8k,
305	  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
306	  title         = {Training Verifiers to Solve Math Word Problems},
307	  journal       = {arXiv preprint},
308	  year          = {2021},
309	  eprint        = {2110.14168},
310	  archiveprefix = {arXiv}
311	}
312	
313	@inproceedings{clark2018arc,
314	  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
315	  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},
316	  journal   = {arXiv preprint},
317	  year      = {2018},
318	  eprint    = {1803.05457},
319	  archiveprefix = {arXiv}
320	}
321	
322	@article{chen2021humaneval,
323	  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},
324	  title         = {Evaluating Large Language Models Trained on Code},
325	  journal       = {arXiv preprint},
326	  year          = {2021},
327	  eprint        = {2107.03374},
328	  archiveprefix = {arXiv}
329	}
330	
331	@inproceedings{chang2025benchmarking,
332	  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
333	  title     = {A Survey on Evaluation of Large Language Models},
334	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
335	  year      = {2025}
336	}
337	
338	@article{white2024livebench,
339	  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},
340	  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
341	  journal       = {arXiv preprint},
342	  year          = {2024},
343	  eprint        = {2406.19314},
344	  archiveprefix = {arXiv}
345	}
346	
347	@inproceedings{polo2024tinybenchmarks,
348	  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
349	  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},
350	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
351	  year      = {2024}
352	}
353	
354	@inproceedings{han2026probing,
355	  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},
356	  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},
357	  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},
358	  year      = {2026},
359	  note      = {arXiv:2510.07175}
360	}
361	
362	% ============================================================
363	% Differential Item Functioning (DIF)
364	% ============================================================
365	
366	@book{holland1993dif,
367	  author    = {Holland, Paul W. and Wainer, Howard},
368	  title     = {Differential Item Functioning},
369	  publisher = {Lawrence Erlbaum Associates},
370	  year      = {1993},
371	  address   = {Hillsdale, NJ}
372	}
373	
374	@incollection{thissen1993dif,
375	  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},
376	  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},
377	  booktitle = {Differential Item Functioning},
378	  editor    = {Holland, Paul W. and Wainer, Howard},
379	  publisher = {Lawrence Erlbaum Associates},
380	  pages     = {67--113},
381	  year      = {1993}
382	}
383	
384	@book{zumbo1999dif,
385	  author    = {Zumbo, Bruno D.},
386	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
387	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},
388	  year      = {1999},
389	  address   = {Ottawa, ON}
390	}
391	
392	% ============================================================
393	% ML Calibration
394	% ============================================================
395	
396	@inproceedings{guo2017calibration,
397	  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
398	  title     = {On Calibration of Modern Neural Networks},
399	  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
400	  pages     = {1321--1330},
401	  year      = {2017}
402	}
403	
404	% ============================================================
405	% Conformal Prediction
406	% ============================================================
407	
408	@article{angelopoulos2023conformal,
409	  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},
410	  title         = {Conformal Prediction: A Gentle Introduction},
411	  journal       = {Foundations and Trends in Machine Learning},
412	  volume        = {16},
413	  number        = {4},
414	  pages         = {494--591},
415	  year          = {2023}
416	}
417	
418	% ============================================================
419	% Data Attribution
420	% ============================================================
421	
422	@inproceedings{pruthi2020tracin,
423	  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},
424	  title     = {Estimating Training Data Influence by Tracing Gradient Descent},
425	  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},
426	  year      = {2020}
427	}
428	
429	@inproceedings{park2023trak,
430	  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},
431	  title     = {{TRAK}: Attributing Model Behavior at Scale},
432	  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
433	  year      = {2023}
434	}
435	
436	% ============================================================
437	% Multidimensional IRT
438	% ============================================================
439	
440	@book{reckase2009mirt,
441	  author    = {Reckase, Mark D.},
442	  title     = {Multidimensional Item Response Theory},
443	  publisher = {Springer},
444	  year      = {2009},
445	  address   = {New York}
446	}
447	
448	% ============================================================
449	% Exposure-Ability Collinearity & IRT Identifiability
450	% ============================================================
451	
452	@article{sanmartin2015,
453	  author  = {San Mart\'{i}n, Ernesto and Gonz\'{a}lez, Jorge and Tuerlinckx, Francis},
454	  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},
455	  journal = {Psychometrika},
456	  volume  = {80},
457	  number  = {2},
458	  pages   = {450--467},
459	  year    = {2015},
460	  doi     = {10.1007/s11336-014-9404-2}
461	}
462	
463	@article{mislevy1987,
464	  author  = {Mislevy, Robert J.},
465	  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},
466	  journal = {Applied Psychological Measurement},
467	  volume  = {11},
468	  number  = {1},
469	  pages   = {81--91},
470	  year    = {1987},
471	  doi     = {10.1177/014662168701100106}
472	}
473	
474	@book{wainer2007testlet,
475	  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},
476	  title     = {Testlet Response Theory and Its Applications},
477	  publisher = {Cambridge University Press},
478	  year      = {2007}
479	}
480	
481	% ============================================================
482	% Measurement Error & Attenuation Bias
483	% ============================================================
484	
485	@book{carroll2006,
486	  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},
487	  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},
488	  edition   = {2nd},
489	  publisher = {Chapman \& Hall/CRC},
490	  year      = {2006},
491	  isbn      = {9781584886334}
492	}
493	
494	@book{fuller1987,
495	  author    = {Fuller, Wayne A.},
496	  title     = {Measurement Error Models},
497	  publisher = {Wiley},
498	  year      = {1987},
499	  series    = {Wiley Series in Probability and Statistics},
500	  isbn      = {9780471861874}
501	}
502	
503	@article{stefanski1985,
504	  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},
505	  title   = {Covariate Measurement Error in Logistic Regression},
506	  journal = {Annals of Statistics},
507	  volume  = {13},
508	  number  = {4},
509	  pages   = {1335--1351},
510	  year    = {1985},
511	  doi     = {10.1214/aos/1176349741}
512	}
513	
514	@article{battauz2011,
515	  author  = {Battauz, Michela and Bellio, Ruggero},
516	  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},
517	  journal = {Psychometrika},
518	  volume  = {76},
519	  number  = {1},
520	  pages   = {40--56},
521	  year    = {2011},
522	  doi     = {10.1007/s11336-010-9195-z}
523	}
524	
525	@article{westfall2016,
526	  author  = {Westfall, Jacob and Yarkoni, Tal},
527	  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},
528	  journal = {PLoS ONE},
529	  volume  = {11},
530	  number  = {3},
531	  pages   = {e0152719},
532	  year    = {2016},
533	  doi     = {10.1371/journal.pone.0152719}
534	}
535	
536	@article{jerzak2026,
537	  author  = {Jerzak, Connor T. and Jessee, Stephen A.},
538	  title   = {Attenuation Bias with Latent Predictors},
539	  journal = {arXiv preprint arXiv:2507.22218},
540	  year    = {2026}
541	}
542	
543	% ============================================================
544	% IRT Information & Power Analysis
545	% ============================================================
546	
547	@book{embretson2000,
548	  author    = {Embretson, Susan E. and Reise, Steven P.},
549	  title     = {Item Response Theory for Psychologists},
550	  publisher = {Lawrence Erlbaum Associates},
551	  year      = {2000},
552	  address   = {Mahwah, NJ}
553	}
554	
555	@book{thissen2001,
556	  author    = {Thissen, David and Wainer, Howard},
557	  title     = {Test Scoring},
558	  publisher = {Lawrence Erlbaum Associates},
559	  year      = {2001},
560	  address   = {Mahwah, NJ}
561	}
562	
563	% ============================================================
564	% 4PL Model & Identifiability
565	% ============================================================
566	
567	@article{barton1981,
568	  author  = {Barton, Mark A. and Lord, Frederic M.},
569	  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},
570	  journal = {ETS Research Report Series},
571	  volume  = {1981},
572	  number  = {1},
573	  pages   = {i--8},
574	  year    = {1981},
575	  doi     = {10.1002/j.2333-8504.1981.tb01255.x}
576	}
577	
578	@article{culpepper2016,
579	  author  = {Culpepper, Steven Andrew},
580	  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},
581	  journal = {Psychometrika},
582	  volume  = {81},
583	  number  = {4},
584	  pages   = {1142--1163},
585	  year    = {2016},
586	  doi     = {10.1007/s11336-015-9477-6}
587	}
588	
589	@article{liao2012,
590	  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},
591	  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},
592	  journal = {Social Behavior and Personality},
593	  volume  = {40},
594	  number  = {10},
595	  pages   = {1679--1694},
596	  year    = {2012},
597	  doi     = {10.2224/sbp.2012.40.10.1679}
598	}
599	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "5e2229ae-5303-42b1-a174-7fb8d21f46f1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib",
      "content": "% ============================================================\n% Core Methodology — Educational Measurement & IRT\n% ============================================================\n\n@book{lord1980,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ}\n}\n\n@article{eckerly2017,\n  author  = {Eckerly, Carol},\n  title   = {Detecting Item Compromise in the Context of Item Response Theory},\n  journal = {Applied Psychological Measurement},\n  volume  = {41},\n  number  = {2},\n  pages   = {87--101},\n  year    = {2017}\n}\n\n@article{sinharay2017,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  pages   = {46--68},\n  year    = {2017}\n}\n\n@book{deboeck2004,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York}\n}\n\n@article{adams1997,\n  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  journal = {Applied Psychological Measurement},\n  volume  = {21},\n  number  = {1},\n  pages   = {1--23},\n  year    = {1997}\n}\n\n@article{mislevy1986,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{sanmartin2009,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{maris2009,\n  author  = {Maris, Gunter and Bechger, Timo},\n  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},\n  journal = {Measurement},\n  volume  = {7},\n  number  = {2},\n  pages   = {75--88},\n  year    = {2009}\n}\n\n@inproceedings{cormack2009,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM}\n}\n\n% ============================================================\n% Bayesian Inference & Diagnostics\n% ============================================================\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n@article{talts2018sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv}\n}\n\n@article{ulitzsch2022,\n  author  = {Ulitzsch, Esther and Nestler, Steffen},\n  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {75},\n  number  = {3},\n  pages   = {421--447},\n  year    = {2022}\n}\n\n% ============================================================\n% Contamination Detection Methods\n% ============================================================\n\n@inproceedings{duan2025minkpp,\n  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},\n  title     = {{Min-K\\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025}\n}\n\n@inproceedings{dekoninck2024constat,\n  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@article{wust2025selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{xu2025kds,\n  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2502.00678}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% ============================================================\n% Contamination Analysis & Mitigation\n% ============================================================\n\n@inproceedings{xu2025emperor,\n  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@article{dong2026dose,\n  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},\n  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv}\n}\n\n@article{yang2026rl,\n  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},\n  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@article{wang2025fragility,\n  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},\n  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.02386},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% ============================================================\n% IRT for LLM Evaluation\n% ============================================================\n\n@inproceedings{gu2026psnirt,\n  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026}\n}\n\n@article{polo2026growing,\n  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv}\n}\n\n@article{lyu2025atlas,\n  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},\n  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv}\n}\n\n@article{zhuang2025hibayes,\n  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{lalor2024irt,\n  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},\n  title     = {Benchmarking Large Language Models with Item Response Theory},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  year      = {2024}\n}\n\n% ============================================================\n% Score Adjustment & Decontamination\n% ============================================================\n\n@inproceedings{li2025dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n@article{rao2026silicon,\n  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},\n  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2603.21636},\n  archiveprefix = {arXiv}\n}\n\n% ============================================================\n% Benchmarking — Surveys & Infrastructure\n% ============================================================\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chen2021humaneval,\n  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  title         = {Evaluating Large Language Models Trained on Code},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2107.03374},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024}\n}\n\n@inproceedings{han2026probing,\n  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},\n  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},\n  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},\n  year      = {2026},\n  note      = {arXiv:2510.07175}\n}\n\n% ============================================================\n% Differential Item Functioning (DIF)\n% ============================================================\n\n@book{holland1993dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% ============================================================\n% ML Calibration\n% ============================================================\n\n@inproceedings{guo2017calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017}\n}\n\n% ============================================================\n% Conformal Prediction\n% ============================================================\n\n@article{angelopoulos2023conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {Conformal Prediction: A Gentle Introduction},\n  journal       = {Foundations and Trends in Machine Learning},\n  volume        = {16},\n  number        = {4},\n  pages         = {494--591},\n  year          = {2023}\n}\n\n% ============================================================\n% Data Attribution\n% ============================================================\n\n@inproceedings{pruthi2020tracin,\n  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},\n  title     = {Estimating Training Data Influence by Tracing Gradient Descent},\n  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},\n  year      = {2020}\n}\n\n@inproceedings{park2023trak,\n  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},\n  title     = {{TRAK}: Attributing Model Behavior at Scale},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year      = {2023}\n}\n\n% ============================================================\n% Multidimensional IRT\n% ============================================================\n\n@book{reckase2009mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n% ============================================================\n% Exposure-Ability Collinearity & IRT Identifiability\n% ============================================================\n\n@article{sanmartin2015,\n  author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},\n  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},\n  journal = {Psychometrika},\n  volume  = {80},\n  number  = {2},\n  pages   = {450--467},\n  year    = {2015},\n  doi     = {10.1007/s11336-014-9404-2}\n}\n\n@article{mislevy1987,\n  author  = {Mislevy, Robert J.},\n  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},\n  journal = {Applied Psychological Measurement},\n  volume  = {11},\n  number  = {1},\n  pages   = {81--91},\n  year    = {1987},\n  doi     = {10.1177/014662168701100106}\n}\n\n@book{wainer2007testlet,\n  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},\n  title     = {Testlet Response Theory and Its Applications},\n  publisher = {Cambridge University Press},\n  year      = {2007}\n}\n\n% ============================================================\n% Measurement Error & Attenuation Bias\n% ============================================================\n\n@book{carroll2006,\n  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},\n  edition   = {2nd},\n  publisher = {Chapman \\& Hall/CRC},\n  year      = {2006},\n  isbn      = {9781584886334}\n}\n\n@book{fuller1987,\n  author    = {Fuller, Wayne A.},\n  title     = {Measurement Error Models},\n  publisher = {Wiley},\n  year      = {1987},\n  series    = {Wiley Series in Probability and Statistics},\n  isbn      = {9780471861874}\n}\n\n@article{stefanski1985,\n  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},\n  title   = {Covariate Measurement Error in Logistic Regression},\n  journal = {Annals of Statistics},\n  volume  = {13},\n  number  = {4},\n  pages   = {1335--1351},\n  year    = {1985},\n  doi     = {10.1214/aos/1176349741}\n}\n\n@article{battauz2011,\n  author  = {Battauz, Michela and Bellio, Ruggero},\n  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},\n  journal = {Psychometrika},\n  volume  = {76},\n  number  = {1},\n  pages   = {40--56},\n  year    = {2011},\n  doi     = {10.1007/s11336-010-9195-z}\n}\n\n@article{westfall2016,\n  author  = {Westfall, Jacob and Yarkoni, Tal},\n  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},\n  journal = {PLoS ONE},\n  volume  = {11},\n  number  = {3},\n  pages   = {e0152719},\n  year    = {2016},\n  doi     = {10.1371/journal.pone.0152719}\n}\n\n@article{jerzak2026,\n  author  = {Jerzak, Connor T. and Jessee, Stephen A.},\n  title   = {Attenuation Bias with Latent Predictors},\n  journal = {arXiv preprint arXiv:2507.22218},\n  year    = {2026}\n}\n\n% ============================================================\n% IRT Information & Power Analysis\n% ============================================================\n\n@book{embretson2000,\n  author    = {Embretson, Susan E. and Reise, Steven P.},\n  title     = {Item Response Theory for Psychologists},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2000},\n  address   = {Mahwah, NJ}\n}\n\n@book{thissen2001,\n  author    = {Thissen, David and Wainer, Howard},\n  title     = {Test Scoring},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2001},\n  address   = {Mahwah, NJ}\n}\n\n% ============================================================\n% 4PL Model & Identifiability\n% ============================================================\n\n@article{barton1981,\n  author  = {Barton, Mark A. and Lord, Frederic M.},\n  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  journal = {ETS Research Report Series},\n  volume  = {1981},\n  number  = {1},\n  pages   = {i--8},\n  year    = {1981},\n  doi     = {10.1002/j.2333-8504.1981.tb01255.x}\n}\n\n@article{culpepper2016,\n  author  = {Culpepper, Steven Andrew},\n  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},\n  journal = {Psychometrika},\n  volume  = {81},\n  number  = {4},\n  pages   = {1142--1163},\n  year    = {2016},\n  doi     = {10.1007/s11336-015-9477-6}\n}\n\n@article{liao2012,\n  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},\n  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},\n  journal = {Social Behavior and Personality},\n  volume  = {40},\n  number  = {10},\n  pages   = {1679--1694},\n  year    = {2012},\n  doi     = {10.2224/sbp.2012.40.10.1679}\n}\n",
      "numLines": 599,
      "startLine": 1,
      "totalLines": 599
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-17T03:49:04.615Z_

<details><summary>↩ Tool result · `toolu_014af3oGtMfkF91YEhgm1rmn`</summary>

```text
1	# Literature Map — contamcal-irt-calibration
2	# Generated: 2026-05-16
3	# Purpose: Related Work section foundation for ContamCal paper (EMNLP 2026)
4	
5	papers:
6	
7	  # ============================================================
8	  # Category: detection — Contamination Detection Methods
9	  # ============================================================
10	
11	  - id: "zhang_2024_minkpp"
12	    title: "Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models"
13	    authors: "Zhang et al."
14	    venue: "ICLR 2025"
15	    year: 2024
16	    url: "https://arxiv.org/abs/2404.02936"
17	    category: "detection"
18	    role: "method-component"
19	    relevance: "Our S2 signal. Min-K%++ normalizes token probability with vocabulary statistics for membership inference. We discover its directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — a novel finding that challenges single-signal reliance."
20	    key_findings: "Theoretically motivated detection via normalized token probabilities; outperforms Min-K% on WikiMIA and other benchmarks."
21	    our_advantage: "ContamCal reveals Min-K++ is actively misleading (not just ineffective) at small scales — directional reversal is our headline empirical finding."
22	
23	  - id: "shi_2023_minkprob"
24	    title: "Detecting Pretraining Data from Large Language Models"
25	    authors: "Shi et al."
26	    venue: "ICLR 2024"
27	    year: 2023
28	    url: "https://arxiv.org/abs/2310.16789"
29	    category: "detection"
30	    role: "foundation"
31	    relevance: "Original Min-K% Prob method and WikiMIA benchmark. Foundation for membership inference in LLMs. Min-K%++ (our S2) is a direct extension."
32	    key_findings: "Unseen examples have outlier low-probability tokens; Min-K% uses this for pretraining data detection without reference model."
33	    our_advantage: "We use the improved Min-K%++ variant and expose its failure modes at small scales."
34	
35	  - id: "dekoninck_2024_constat"
36	    title: "ConStat: Performance-Based Contamination Detection in Large Language Models"
37	    authors: "Dekoninck et al."
38	    venue: "arXiv 2024"
39	    year: 2024
40	    url: "https://arxiv.org/abs/2405.16281"
41	    category: "detection"
42	    role: "method-component"
43	    relevance: "Our S3 signal candidate (excluded from final pipeline). Detects contamination as non-generalizing inflated performance by comparing primary vs reference benchmark performance against reference models."
44	    key_findings: "Novel contamination definition as non-generalizing performance inflation; detects contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models."
45	    our_advantage: "ConStat requires reference benchmarks and reference models; ContamCal integrates detection signals directly into IRT framework for calibrated score adjustment, not just detection."
46	
47	  - id: "dong_2024_cdd"
48	    title: "Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models"
49	    authors: "Dong et al."
50	    venue: "ACL 2024 Findings"
51	    year: 2024
52	    url: "https://arxiv.org/abs/2402.15938"
53	    category: "detection"
54	    role: "direct-competitor"
55	    relevance: "Proposes CDD (output distribution peakedness) and TED (distribution correction for trustworthy evaluation). TED is closest to calibration but lacks IRT grounding and uncertainty quantification."
56	    key_findings: "CDD achieves 21-30% improvement over baselines in detection accuracy; TED mitigates up to 66.9% of contamination-attributed performance gain."
57	    our_advantage: "ContamCal provides full uncertainty quantification via Bayesian IRT posteriors; TED offers point corrections without credible intervals or identifiability analysis."
58	
59	  - id: "zhang_2024_gsm1k"
60	    title: "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
61	    authors: "Zhang et al."
62	    venue: "arXiv 2024"
63	    year: 2024
64	    url: "https://arxiv.org/abs/2405.00332"
65	    category: "detection"
66	    role: "method-component"
67	    relevance: "Our S4 signal (self-critique / GSM1k). Creates GSM1k to mirror GSM8k and measures accuracy drop as contamination proxy. Up to 13% accuracy drops in some model families."
68	    key_findings: "Systematic overfitting in Phi and Mistral families; positive correlation (r^2=0.32) between generation probability of GSM8k examples and performance gap."
69	    our_advantage: "ContamCal uses the GSM1k-style signal as one input to multi-signal RRF, then feeds into IRT for calibrated estimates rather than just flagging contamination."
70	
71	  - id: "choi_2025_kds"
72	    title: "How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence"
73	    authors: "Choi et al."
74	    venue: "ICML 2025"
75	    year: 2025
76	    url: "https://arxiv.org/abs/2502.00678"
77	    category: "detection"
78	    role: "evaluation"
79	    relevance: "Kernel Divergence Score (KDS) detects contamination via embedding shift before/after fine-tuning. Near-perfect correlation with contamination levels. Complementary signal approach to our S1 embedding similarity."
80	    key_findings: "KDS captures fine-tuning-induced shifts in sample embeddings; outperforms existing baselines with near-perfect contamination level correlation."
81	    our_advantage: "ContamCal bridges detection to calibration; KDS only detects. Our S1 embedding similarity achieves AUC>0.95 without requiring fine-tuning comparison."
82	
83	  - id: "oren_2023_proving_contamination"
84	    title: "Proving Test Set Contamination in Black Box Language Models"
85	    authors: "Oren et al."
86	    venue: "arXiv 2023"
87	    year: 2023
88	    url: "https://arxiv.org/abs/2310.17623"
89	    category: "detection"
90	    role: "background"
91	    relevance: "Provable contamination detection via exchangeability test on benchmark ordering likelihood. Complementary black-box approach."
92	    key_findings: "Detects contamination in models as small as 1.4B with 1000 examples; audits 5 popular LLMs finding little pervasive contamination."
93	    our_advantage: "ContamCal goes beyond detection to calibrated score adjustment with uncertainty quantification."
94	
95	  - id: "deng_2024_tsguessing"
96	    title: "Investigating Data Contamination in Modern Benchmarks for Large Language Models"
97	    authors: "Deng, Zhao, Tang, Gerstein, & Cohan"
98	    year: 2024
99	    venue: "NAACL 2024"
100	    url: "https://arxiv.org/abs/2311.09783"
101	    category: "detection"
102	    role: "direct-competitor"
103	    relevance: "TS-Guessing protocol masks MC wrong options for fill-in; ChatGPT/GPT-4 guess correct options at 52%/57% on MMLU. Direct evidence that MC format is more vulnerable to contamination, supporting our finding that ARC (MC) shows γ>0 while GSM8K (generative) shows γ≈0."
104	    key_findings:
105	      - "MC format enables contaminated models to exploit memorized answer options"
106	      - "ChatGPT/GPT-4 MMLU option guessing rate 52%/57% vs random baseline"
107	      - "Open-ended format harder to game via memorization"
108	
109	  - id: "schaeffer_2026_generative_contamination"
110	    title: "Quantifying the Effect of Test Set Contamination on Generative Evaluations"
111	    authors: "Schaeffer, Kazdan, Abbasi, Liu, et al."
112	    year: 2026
113	    venue: "arXiv 2026"
114	    url: "https://arxiv.org/abs/2601.04301"
115	    category: "detection"
116	    role: "direct-competitor"
117	    relevance: "First scaling law study of contamination on generative benchmarks (MATH). Even 1 test set replica in pretraining breaks irreducible error floor, but effect size much smaller than MC benchmarks. Consistent with our framework: generative γ expected smaller but non-zero."
118	    key_findings:
119	      - "Single test set replica in pretraining corpus breaks irreducible error on MATH"
120	      - "Contamination effect on generative benchmarks weaker than MC benchmarks"
121	      - "Scaling law characterization of contamination-performance relationship"
122	
123	  # ============================================================
124	  # Category: irt-llm — IRT for LLM Evaluation
125	  # ============================================================
126	
127	  - id: "lalor_2024_irt_nlp"
128	    title: "Item Response Theory for Natural Language Processing"
129	    authors: "Lalor et al."
130	    venue: "EACL 2024 Tutorial"
131	    year: 2024
132	    url: "https://aclanthology.org/2024.eacl-tutorials.2/"
133	    category: "irt-llm"
134	    role: "foundation"
135	    relevance: "Comprehensive tutorial introducing IRT to NLP community. Establishes framework for psychometric LLM evaluation that ContamCal extends with contamination covariates."
136	    key_findings: "Demonstrates IRT benefits for NLP evaluation including difficulty estimation, benchmark quality assessment, and latent trait modeling."
137	    our_advantage: "ContamCal extends standard IRT with contamination covariate gamma, measurement error model, and per-benchmark effect estimation."
138	
139	  - id: "polo_2024_tinybenchmarks"
140	    title: "tinyBenchmarks: evaluating LLMs with fewer examples"
141	    authors: "Polo et al."
142	    venue: "ICML 2024"
143	    year: 2024
144	    url: "https://arxiv.org/abs/2402.14992"
145	    category: "irt-llm"
146	    role: "foundation"
147	    relevance: "Uses IRT as performance estimator; 100 curated examples sufficient for MMLU. Demonstrates IRT scalability for LLM evaluation. Shares our assumption that IRT item parameters transfer across models."
148	    key_findings: "Accurate performance estimation with ~100 items per benchmark; IRT-based selection outperforms random subsampling."
149	    our_advantage: "ContamCal addresses a different problem: not efficiency but decontamination. We use IRT to model contamination effects rather than to reduce evaluation cost."
150	
151	  - id: "habba_2025_growing_pains"
152	    title: "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration"
153	    authors: "Habba et al."
154	    venue: "arXiv 2025"
155	    year: 2025
156	    url: "https://arxiv.org/abs/2604.12843"
157	    category: "irt-llm"
158	    role: "foundation"
159	    relevance: "Multidimensional IRT with anchor items for cross-study comparability. Addresses N insufficiency via fixed parameter calibration. Directly relevant to our N>=50 identifiability concern."
160	    key_findings: "Predicts full-evaluation performance within 2-3pp using 100 anchor items; Spearman rho>=0.9 across 400+ models."
161	    our_advantage: "Growing Pains assumes no contamination; ContamCal explicitly models contamination effects. Their anchor-item framework could complement our decontamination pipeline."
162	
163	  - id: "luettgau_2025_hibayes"
164	    title: "HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics"
165	    authors: "Luettgau et al."
166	    venue: "arXiv 2025"
167	    year: 2025
168	    url: "https://arxiv.org/abs/2505.05602"
169	    category: "irt-llm"
170	    role: "direct-competitor"
171	    relevance: "Hierarchical Bayesian framework for LLM evaluation with principled UQ, especially in low-data scenarios (<20 data points). Does not model contamination. Most methodologically similar to ContamCal's Bayesian approach."
172	    key_findings: "Robust parameter estimation via hierarchical GLMs with formal model comparison; handles nested evaluation structures."
173	    our_advantage: "ContamCal adds contamination-specific covariates (gamma_k, exposure scores) to the Bayesian framework. HiBayES provides UQ but ignores contamination effects entirely."
174	
175	  - id: "li_2024_atlas"
176	    title: "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks"
177	    authors: "Li et al."
178	    venue: "arXiv 2024"
179	    year: 2024
180	    url: "https://arxiv.org/abs/2511.04689"
181	    category: "irt-llm"
182	    role: "evaluation"
183	    relevance: "ATLAS uses Fisher information-guided adaptive item selection for efficient LLM evaluation with up to 90% item reduction. Validates IRT psychometric framework for LLM evaluation."
184	    key_findings: "30-89 items per benchmark sufficient with SE-controlled stopping; best accuracy-efficiency tradeoff among IRT-based methods."
185	    our_advantage: "ATLAS optimizes evaluation efficiency; ContamCal addresses evaluation validity under contamination. Complementary goals."
186	
187	  - id: "zhou_2025_psnirt"
188	    title: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"
189	    authors: "Zhou et al."
190	    venue: "AAAI 2026"
191	    year: 2025
192	    url: "https://arxiv.org/abs/2505.15055"
193	    category: "irt-llm"
194	    role: "evaluation"
195	    relevance: "PSN-IRT uses pseudo-siamese networks for rich item parameter estimation. Analyzes 11 benchmarks (41,871 items) revealing measurement quality shortcomings."
196	    key_findings: "LLM benchmarks suffer widespread saturation and insufficient difficulty ceilings; PSN-IRT constructs smaller benchmarks with stronger human preference alignment."
197	    our_advantage: "PSN-IRT diagnoses benchmark quality; ContamCal diagnoses and corrects contamination effects. Our gamma_k captures a specific quality dimension (data leakage) that PSN-IRT does not model."
198	
199	  - id: "burnell_2023_structure"
200	    title: "Revealing the structure of language model capabilities"
201	    authors: "Burnell et al."
202	    venue: "arXiv 2023"
203	    year: 2023
204	    url: "https://arxiv.org/abs/2306.10062"
205	    category: "irt-llm"
206	    role: "background"
207	    relevance: "Factor analysis reveals 3 capability dimensions (reasoning, comprehension, core language modeling) in LLMs. Supports multidimensional view; our unidimensional theta per benchmark is acknowledged as simplification in Limitations."
208	    key_findings: "LLM capabilities are not monolithic; 3 factors explain high proportion of performance variance across 29 LLMs on 27 tasks."
209	    our_advantage: "ContamCal's unidimensional theta per benchmark is a deliberate simplification acknowledged in Limitations; multidimensional extension is future work."
210	
211	  - id: "brown_2024_ppp"
212	    title: "The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation"
213	    authors: "Brown & Thomson"
214	    year: 2024
215	    venue: "Molecular Biology and Evolution, 41(3), msae051"
216	    category: "irt-llm"
217	    role: "background"
218	    relevance: "Proves PPP distribution is inherently non-uniform (unlike frequentist p-values), concentrated near 0.5. Extreme PPP (e.g. our 0.003) provides stronger poor-fit evidence than usually assumed, but low PPP does not automatically invalidate parameter estimates — supports our position that γ posterior excluding zero remains informative even with poor global fit."
219	    key_findings:
220	      - "PPP distribution is non-uniform, concentrated around 0.5"
221	      - "Low PPP does not automatically negate parameter estimate informativeness"
222	      - "Posterior predictive tests evaluate models under favorable conditions (model already fitted to data)"
223	
224	  - id: "sinharay_2025_irt_fit"
225	    title: "Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions"
226	    authors: "Sinharay, S."
227	    year: 2025
228	    venue: "British Journal of Mathematical and Statistical Psychology, 78, 711–733"
229	    category: "irt-llm"
230	    role: "background"
231	    relevance: "Comprehensive review of IRT model fit assessment (PPMC, generalized residuals, person-fit). Argues low PPP indicates model inadequacy but not that parameter estimates are meaningless. Supports our ARC PPP=0.003 but γ still interpretable position."
232	    key_findings:
233	      - "PPP interpretation requires caution — low PPP means model inadequacy, not parameter invalidity"
234	      - "Covers PPMC, generalized residuals, person-fit diagnostics"
235	      - "Authoritative 2025 review likely known to reviewers"
236	
237	  # ============================================================
238	  # Category: item-compromise — Educational Measurement
239	  # ============================================================
240	
241	  - id: "eckerly_2017_item_compromise"
242	    title: "Detecting preknowledge and item compromise: Understanding the status quo"
243	    authors: "Eckerly, C."
244	    venue: "Handbook of Quantitative Methods for Detecting Cheating on Tests (Routledge)"
245	    year: 2017
246	    url: "https://www.routledge.com/9781138821811"
247	    category: "item-compromise"
248	    role: "foundation"
249	    relevance: "Core theoretical foundation for ContamCal. Reviews IRT methods for detecting compromised items and examinees with preknowledge. Our gamma parameter directly extends the item compromise framework to LLM benchmark contamination."
250	    key_findings: "Systematic framework for item preknowledge detection using IRT-based person-fit statistics and item parameter drift."
251	    our_advantage: "ContamCal adapts item compromise IRT from human testing to LLM evaluation with 3 structural adaptations: independent examinees -> single model, binary leakage -> continuous exposure, stable ability -> regime-conditional ability."
252	    verified: false
253	
254	  - id: "sinharay_2017_preknowledge"
255	    title: "Detection of item preknowledge using likelihood ratio test and score test"
256	    authors: "Sinharay, S."
257	    venue: "Journal of Educational and Behavioral Statistics, 42(1)"
258	    year: 2017
259	    url: "https://pubmed.ncbi.nlm.nih.gov/29881099/"
260	    category: "item-compromise"
261	    role: "foundation"
262	    relevance: "Proposes LRT-based statistics for item preknowledge detection with known Type I error rates. Our treatment of contamination-induced item parameter drift builds on this work."
263	    key_findings: "LRT statistic for item preknowledge has similar power to posterior shift statistic with known null distribution; applicable to adaptive and non-adaptive tests."
264	    our_advantage: "ContamCal extends from binary preknowledge to continuous contamination exposure scores and from human examinees to LLM respondents."
265	
266	  - id: "deboeck_2004_explanatory_irt"
267	    title: "Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach"
268	    authors: "De Boeck, P. & Wilson, M."
269	    venue: "Springer"
270	    year: 2004
271	    url: "https://link.springer.com/book/10.1007/978-1-4757-3990-9"
272	    category: "item-compromise"
273	    role: "foundation"
274	    relevance: "Foundational text for explanatory IRT. ContamCal's contamination-augmented 4PL is an explanatory IRT model where item responses are modeled as a function of contamination exposure predictors."
275	    key_findings: "Unifies IRT with generalized linear/nonlinear mixed models; enables item covariates (like our exposure scores) as predictors in IRT framework."
276	    our_advantage: "Direct theoretical grounding. ContamCal instantiates the explanatory IRT framework with contamination-specific covariates."
277	
278	  - id: "kievit_2013_simpsons_paradox"
279	    title: "Simpson's Paradox in Psychological Science: A Practical Guide"
280	    authors: "Kievit, Frankenhuis, Waldorp, & Borsboom"
281	    year: 2013
282	    venue: "Frontiers in Psychology, 4, 513"
283	    category: "item-compromise"
284	    role: "background"
285	    relevance: "Theoretical framework for Simpson's paradox in behavioral science. Directly applicable to our MMLU finding: pooled γ insignificant but domain-level analysis reveals significant positive and negative γ that cancel upon aggregation."
286	    key_findings:
287	      - "Simpson's paradox more prevalent in psychology than traditionally recognized"
288	      - "Effect direction can reverse when moving from population to subgroup (or vice versa)"
289	      - "Provides statistical markers and R detection toolkit"
290	
291	  - id: "ercikan_2008_dif_cancellation"
292	    title: "Differential Item Functioning Amplification and Cancellation in a Reading Test"
293	    authors: "Ercikan, Arim, & Oliveri"
294	    year: 2008
295	    venue: "Practical Assessment, Research, and Evaluation, 14(3)"
296	    category: "item-compromise"
297	    role: "background"
298	    relevance: "Empirical precedent for DIF cancellation: most items show significant DIF but favoring different groups, so DIF cancels at total test score level. Direct analogue to our MMLU domain-level contamination signals with inconsistent directions being masked in pooled analysis."
299	    key_findings:
300	      - "Majority of items show significant DIF but in opposing directions"
301	      - "DIF cancels at aggregate test score level despite item-level significance"
302	      - "Multiple-group testlet IRT model reveals hidden heterogeneity"
303	
304	  # ============================================================
305	  # Category: calibration — Calibration & Score Adjustment
306	  # ============================================================
307	
308	  - id: "xu_2025_dcr"
309	    title: "DCR: Quantifying Data Contamination in LLMs Evaluation"
310	    authors: "Xu et al."
311	    venue: "EMNLP 2025"
312	    year: 2025
313	    url: "https://arxiv.org/abs/2507.11405"
314	    category: "calibration"
315	    role: "direct-competitor"
316	    relevance: "Only existing method producing adjusted accuracy via fuzzy inference. ContamCal's primary competitor. DCR quantifies contamination risk across 4 levels (semantic, informational, data, label) and adjusts raw accuracy."
317	    key_findings: "DCR Factor adjusts accuracy within 4% average error across 3 benchmarks; validated on 0.5B-72B models."
318	    our_advantage: "ContamCal provides Bayesian credible intervals (DCR gives point estimates only), per-benchmark gamma_k characterization, and IRT-grounded identifiability analysis. DCR lacks UQ and theoretical identifiability bounds."
319	
320	  - id: "guo_2017_calibration"
321	    title: "On Calibration of Modern Neural Networks"
322	    authors: "Guo et al."
323	    venue: "ICML 2017"
324	    year: 2017
325	    url: "https://arxiv.org/abs/1706.04599"
326	    category: "calibration"
327	    role: "background"
328	    relevance: "Foundational work on probability calibration in neural networks. Must disambiguate: our 'calibration' means decontamination score adjustment, not probability calibration (confidence = accuracy). Temperature scaling is unrelated to our method."
329	    key_findings: "Modern neural networks are poorly calibrated; temperature scaling (single parameter) effectively recalibrates predictions."
330	    our_advantage: "Different notion of calibration. Guo et al. calibrate prediction confidence; ContamCal calibrates benchmark scores for contamination effects."
331	
332	  - id: "angelopoulos_2023_conformal"
333	    title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
334	    authors: "Angelopoulos & Bates"
335	    venue: "Foundations and Trends in ML, 2023"
336	    year: 2023
337	    url: "https://arxiv.org/abs/2107.07511"
338	    category: "calibration"
339	    role: "background"
340	    relevance: "Alternative UQ approach with distribution-free coverage guarantees. Discussed in Related Work to justify why Bayesian IRT is preferred over conformal for our setting (conformal requires exchangeability assumptions violated by contamination structure)."
341	    key_findings: "Conformal prediction provides statistically rigorous uncertainty sets without distributional assumptions; applicable to any pre-trained model."
342	    our_advantage: "Bayesian IRT provides interpretable per-item parameters and contamination-specific covariates; conformal gives coverage guarantees but no mechanistic insight into contamination effects."
343	
344	  # ============================================================
345	  # Category: mitigation — Contamination Mitigation & Alternatives
346	  # ============================================================
347	
348	  - id: "sun_2025_emperors_new_clothes"
349	    title: "The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination"
350	    authors: "Sun et al."
351	    venue: "ICML 2025"
352	    year: 2025
353	    url: "https://arxiv.org/abs/2503.16402"
354	    category: "mitigation"
355	    role: "direct-competitor"
356	    relevance: "Demonstrates all 20 existing mitigation strategies fail to balance fidelity and contamination resistance across all benchmarks. Strongest motivation for ContamCal's post-hoc calibration approach."
357	    key_findings: "No semantic-preserving strategy significantly improves resistance over vanilla; semantic-altering strategies sacrifice fidelity. 10 LLMs x 5 benchmarks x 20 strategies x 2 scenarios."
358	    our_advantage: "ContamCal offers post-hoc calibration rather than prevention — complementary approach. Emperor's failure motivates calibration; ContamCal provides it."
359	
360	  - id: "white_2024_livebench"
361	    title: "LiveBench: A Challenging, Contamination-Free LLM Benchmark"
362	    authors: "White et al."
363	    venue: "arXiv 2024"
364	    year: 2024
365	    url: "https://arxiv.org/abs/2406.19314"
366	    category: "mitigation"
367	    role: "evaluation"
368	    relevance: "Dynamic benchmark alternative: monthly-updated questions from recent sources to prevent contamination. Complementary to ContamCal — LiveBench prevents contamination for new evaluations; ContamCal calibrates existing contaminated benchmarks."
369	    key_findings: "Top models achieve below 70% accuracy; monthly updates with 18 tasks across 6 categories maintain contamination resistance."
370	    our_advantage: "LiveBench requires continuous curation; ContamCal works with existing static benchmarks. Both valid approaches to the contamination problem."
371	
372	  # ============================================================
373	  # Category: benchmark — Evaluation Frameworks & Alternatives
374	  # ============================================================
375	
376	  - id: "liang_2023_helm"
377	    title: "Holistic Evaluation of Language Models"
378	    authors: "Liang et al."
379	    venue: "TMLR 2023"
380	    year: 2023
381	    url: "https://arxiv.org/abs/2211.09110"
382	    category: "benchmark"
383	    role: "background"
384	    relevance: "HELM evaluates 30 models on 42 scenarios with 7 metrics including calibration. Establishes standardized evaluation framework. ContamCal addresses a gap HELM does not: score reliability under contamination."
385	    key_findings: "Prior to HELM, models were evaluated on only 17.9% of core scenarios; standardized evaluation reveals 25 top-level findings across models."
386	    our_advantage: "HELM assumes benchmark scores are trustworthy; ContamCal questions and corrects this assumption when contamination is present."
387	
388	  - id: "chiang_2024_chatbot_arena"
389	    title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference"
390	    authors: "Chiang et al."
391	    venue: "ICML 2024"
392	    year: 2024
393	    url: "https://arxiv.org/abs/2403.04132"
394	    category: "benchmark"
395	    role: "background"
396	    relevance: "Human pairwise comparison evaluation that inherently bypasses benchmark contamination. Discussed as contamination-resistant alternative."
397	    key_findings: "240K+ votes via crowdsourced pairwise comparisons; Elo rating system for model ranking without static test sets."
398	    our_advantage: "Chatbot Arena requires human judges and live interaction; ContamCal enables post-hoc calibration of automated benchmark scores, which scale better."
399	
400	  - id: "li_2024_open_llm_leaderboard"
401	    title: "Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena"
402	    authors: "Li et al."
403	    year: 2024
404	    venue: "arXiv 2024"
405	    url: "https://arxiv.org/abs/2406.07545"
406	    category: "benchmark"
407	    role: "evaluation"
408	    relevance: "Converting MC benchmarks to open-style questions causes ~25% average accuracy drop across all models. Quantifies MC format advantage (selection bias, random guessing) that amplifies contamination signal in MC benchmarks. Supports our MC/generative format as contamination effect moderator."
409	    key_findings:
410	      - "MC to open-style conversion causes ~25% average accuracy drop"
411	      - "MC format provides extra cues (selection bias, random guessing) beyond knowledge"
412	      - "Contaminated models benefit more from MC format than clean models"
413	
414	  # ============================================================
415	  # Category: foundation — Methodological Foundations
416	  # ============================================================
417	
418	  - id: "shokri_2017_mia"
419	    title: "Membership Inference Attacks Against Machine Learning Models"
420	    authors: "Shokri et al."
421	    venue: "IEEE S&P 2017"
422	    year: 2017
423	    url: "https://arxiv.org/abs/1610.05820"
424	    category: "detection"
425	    role: "foundation"
426	    relevance: "Foundational MIA work. Min-K% and Min-K%++ are descendants of MIA methodology. Contextualizes our Min-K++ directional reversal finding within MIA literature."
427	    key_findings: "Shadow model approach for membership inference; demonstrates vulnerability of ML-as-a-service models to membership inference."
428	    our_advantage: "ContamCal uses MIA-derived signals as inputs to calibration framework, not as standalone detectors."
429	
430	  - id: "carlini_2021_extracting"
431	    title: "Extracting Training Data from Large Language Models"
432	    authors: "Carlini et al."
433	    venue: "USENIX Security 2021"
434	    year: 2021
435	    url: "https://arxiv.org/abs/2012.07805"
436	    category: "detection"
437	    role: "foundation"
438	    relevance: "Demonstrates verbatim training data extraction from GPT-2. Establishes that LLMs memorize training data — the fundamental assumption underlying all contamination detection methods including ours."
439	    key_findings: "Hundreds of verbatim text sequences extracted from GPT-2; memorization is measurable and exploitable."
440	    our_advantage: "ContamCal leverages memorization signals for calibration rather than extraction; our contribution is bridging detection to score adjustment."
441	
442	  - id: "cormack_2009_rrf"
443	    title: "Reciprocal Rank Fusion outperforms Condorcet and Individual Rank Learning Methods"
444	    authors: "Cormack et al."
445	    venue: "SIGIR 2009"
446	    year: 2009
447	    url: "https://dl.acm.org/doi/10.1145/1571941.1572114"
448	    category: "calibration"
449	    role: "method-component"
450	    relevance: "RRF is our multi-signal aggregation method. Training-free rank fusion avoids meta-circularity (learned aggregator's training data may itself be contaminated). RRF is a design choice, not claimed as contribution."
451	    key_findings: "Simple reciprocal rank scoring outperforms Condorcet and learning-to-rank methods for combining multiple retrieval systems."
452	    our_advantage: "RRF is adopted as-is. Our contribution is the argument for training-free aggregation in the contamination context (meta-circularity)."
453	
454	  - id: "talts_2018_sbc"
455	    title: "Validating Bayesian Inference Algorithms with Simulation-Based Calibration"
456	    authors: "Talts et al."
457	    venue: "arXiv 2018"
458	    year: 2018
459	    url: "https://arxiv.org/abs/1804.06788"
460	    category: "calibration"
461	    role: "method-component"
462	    relevance: "SBC is our 6th evaluation metric. Validates Bayesian inference by checking rank uniformity of posterior samples. Used to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation)."
463	    key_findings: "General procedure for validating Bayesian posterior samplers; graphical diagnostics indicate nature of inference problems."
464	    our_advantage: "SBC is adopted as diagnostic tool. Our contribution is applying SBC to contamination-augmented IRT at realistic N_models to decompose coverage gaps."
465	
466	  # ============================================================
467	  # Category: detection — Gap-Fill (must_cite)
468	  # ============================================================
469	
470	  - id: "wust_2025_selfcritique"
471	    title: "Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations"
472	    authors: "Wüst, Hoffmann, & Pang"
473	    venue: "arXiv 2025"
474	    year: 2025
475	    url: "https://arxiv.org/abs/2510.09259"
476	    category: "detection"
477	    role: "method-component"
478	    relevance: "Our S4 signal. Uses LLM self-evaluation entropy collapse as contamination indicator. We find it near-random (AUC≈0.50) at 0.5B scale — ineffective as standalone signal."
479	    key_findings: "Self-critique entropy patterns differ for memorized vs novel items."
480	    our_advantage: "ContamCal reveals S4 ineffectiveness and integrates it into multi-signal RRF where its noise is diluted."
481	
482	  - id: "golchin_2024_time_travel"
483	    title: "Time Travel in LLMs: Tracing Data Contamination in Large Language Models"
484	    authors: "Golchin & Surdeanu"
485	    venue: "ICLR 2024"
486	    year: 2024
487	    url: "https://arxiv.org/abs/2308.08493"
488	    category: "detection"
489	    role: "background"
490	    relevance: "Proposes guided prompting to detect contamination via LLM's ability to reproduce benchmark instances. Complementary approach to our signal-based detection."
491	    key_findings: "Detects contamination across GPT-4, GPT-3.5, LLaMA-2 via instance reproduction; confirms widespread contamination in major LLMs."
492	    our_advantage: "Time Travel requires model generation access; ContamCal works with item-level responses only. Our approach quantifies effects, not just detects."
493	
494	  # ============================================================
495	  # Category: mitigation — Gap-Fill (must_cite + supplementary)
496	  # ============================================================
497	
498	  - id: "li_2025_dcr"
499	    title: "Decontaminated Calibration and Ranking for Trustworthy LLM Evaluation"
500	    authors: "Li et al."
501	    venue: "EMNLP 2025"
502	    year: 2025
503	    category: "mitigation"
504	    role: "direct-competitor"
505	    relevance: "Closest predecessor to ContamCal. DCR applies decontamination + calibration + ranking correction. Lacks IRT grounding, uncertainty quantification, and domain-level diagnosis. Key W1 comparison target."
506	    key_findings: "Score adjustment framework for contaminated benchmarks; demonstrates improved ranking consistency post-decontamination."
507	    our_advantage: "ContamCal provides: (1) Bayesian CIs vs point estimates, (2) domain-level γ diagnosis vs aggregate correction, (3) Fisher Info identifiability analysis, (4) Min-K++ reversal detection."
508	    verified: false
509	
510	  - id: "yang_2023_rethinking_benchmark"
511	    title: "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples"
512	    authors: "Yang et al."
513	    venue: "arXiv 2023"
514	    year: 2023
515	    url: "https://arxiv.org/abs/2311.04850"
516	    category: "mitigation"
517	    role: "background"
518	    relevance: "Rephrasing-based contamination mitigation: creates semantically equivalent but textually novel test items. Complementary to ContamCal's post-hoc calibration approach."
519	    key_findings: "Rephrased benchmarks show significant performance drops in contaminated models; surface-level memorization dominates."
520	    our_advantage: "Rephrasing prevents contamination for new evaluations; ContamCal calibrates existing contaminated scores. Different scope."
521	
522	  # ============================================================
523	  # Category: benchmark — Gap-Fill (must_cite + supplementary)
524	  # ============================================================
525	
526	  - id: "zheng_2023_chatbot_arena"
527	    title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
528	    authors: "Zheng et al."
529	    venue: "NeurIPS 2023"
530	    year: 2023
531	    url: "https://arxiv.org/abs/2306.05685"
532	    category: "benchmark"
533	    role: "background"
534	    relevance: "Chatbot Arena as contamination-resistant evaluation via live human preference. Motivates why static benchmark contamination matters — dynamic evaluations are expensive and limited to ranking."
535	    key_findings: "Strong agreement between MT-Bench automated and Chatbot Arena human evaluations; crowdsourced evaluation provides contamination-resistant rankings."
536	    our_advantage: "Chatbot Arena avoids contamination by design but cannot assess specific capabilities. ContamCal enables continued use of targeted static benchmarks with calibrated scores."
537	
538	  - id: "wang_2024_mmlu_pro"
539	    title: "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark"
540	    authors: "Wang et al."
541	    venue: "arXiv 2024"
542	    year: 2024
543	    url: "https://arxiv.org/abs/2406.01574"
544	    category: "benchmark"
545	    role: "background"
546	    relevance: "MMLU-Pro increases difficulty and reduces sensitivity to prompt format, partially addressing contamination concerns. Our MMLU domain-level γ analysis applies equally to MMLU-Pro since contamination is about memorization, not difficulty."
547	    key_findings: "10-option MC format reduces random guessing; more discriminative across model capabilities."
548	    our_advantage: "MMLU-Pro redesigns the benchmark; ContamCal calibrates existing benchmarks without redesign."
549	
550	  # ============================================================
551	  # Category: irt-methodology — Gap-Fill (must_cite)
552	  # ============================================================
553	
554	  - id: "reckase_2009_mirt"
555	    title: "Multidimensional Item Response Theory"
556	    authors: "Reckase, M. D."
557	    venue: "Springer"
558	    year: 2009
559	    category: "irt-methodology"
560	    role: "foundation"
561	    relevance: "Canonical MIRT reference. Our 2PL+γ extends unidimensional IRT; multidimensional extensions discussed in future work for non-STEM domain misfit."
562	    key_findings: "Comprehensive MIRT framework including compensatory and non-compensatory models, parameter estimation, and model fit assessment."
563	    our_advantage: "ContamCal currently uses unidimensional IRT with contamination covariate. MIRT extension is future work for modeling domain-specific abilities."
564	    verified: false
565	
566	  - id: "mislevy_1986_bayes_irt"
567	    title: "Bayes Modal Estimation in Item Response Models"
568	    authors: "Mislevy, R. J."
569	    venue: "Psychometrika"
570	    year: 1986
571	    category: "irt-methodology"
572	    role: "foundation"
573	    relevance: "Foundational work on Bayesian estimation for IRT. Justifies our use of Bayesian (NUTS/Stan) inference for 2PL+γ parameter estimation with informative priors."
574	    key_findings: "Bayesian modal estimation provides regularization for IRT parameters; handles small samples better than MLE."
575	    our_advantage: "ContamCal builds on Bayesian IRT tradition, adding contamination-specific covariates and model comparison via PPP."
576	
577	  - id: "sanmartin_2009_irt"
578	    title: "Consequential Validity and Item Response Theory"
579	    authors: "San Martín, Del Pino, & De Boeck"
580	    venue: "Psychometrika"
581	    year: 2009
582	    category: "irt-methodology"
583	    role: "foundation"
584	    relevance: "Addresses consequential validity in IRT models — directly relevant to our calibration value decomposition (D120) where we separate ability estimation from contamination correction."
585	    key_findings: "Framework for assessing consequences of IRT model use; distinguishes construct-relevant from construct-irrelevant variance."
586	    our_advantage: "ContamCal's D120 decomposition directly operationalizes this distinction: γ correction vs θ estimation improvement."
587	
588	  - id: "adams_1997_mrcml"
589	    title: "The Multidimensional Random Coefficients Multinomial Logit Model"
590	    authors: "Adams, Wilson, & Wang"
591	    venue: "Applied Psychological Measurement"
592	    year: 1997
593	    category: "irt-methodology"
594	    role: "foundation"
595	    relevance: "Extends IRT to multidimensional random effects. Foundation for understanding our per-domain γ modeling within the broader IRT methodology."
596	    key_findings: "General framework for multidimensional IRT with random coefficients; handles nested item structures."
597	    our_advantage: "ContamCal uses a simpler contamination-specific extension (additive γ) rather than full MRCML."
598	
599	  # ============================================================
600	  # Category: item-compromise — Gap-Fill (must_cite)
601	  # ============================================================
602	
603	  - id: "holland_1993_dif"
604	    title: "Differential Item Functioning"
605	    authors: "Holland, P. W. & Wainer, H. (Eds.)"
606	    venue: "Lawrence Erlbaum Associates"
607	    year: 1993
608	    category: "item-compromise"
609	    role: "foundation"
610	    relevance: "Classic DIF reference. DIF methodology detects items that function differently across groups — analogous to our γ detecting contamination effects that vary across domains. DIF is the educational measurement precursor to our domain-differential analysis."
611	    key_findings: "Comprehensive DIF detection and analysis framework; establishes that item-level analysis is essential for fair measurement."
612	    our_advantage: "ContamCal extends DIF thinking to LLM contamination: 'exposed' vs 'unexposed' items replace traditional DIF group comparisons."
613	    verified: false
614	
615	# ============================================================
616	# Summary Statistics (Updated)
617	# ============================================================
618	# Total papers: 43
619	# By category: detection=13, irt-llm=9, item-compromise=6, calibration=4, mitigation=4, benchmark=5, irt-methodology=4
620	# By role: foundation=14, method-component=6, direct-competitor=7, evaluation=5, background=12
621	# Must-cite coverage: 8/9 clusters filled (all must_cite accounted for)
622	# Notes:
623	#   - Eckerly 2017: verified=false (book chapter, no direct URL confirmed)
624	#   - li_2025_dcr: verified=false (EMNLP 2025, need to confirm exact venue/URL)
625	#   - reckase_2009_mirt: verified=false (textbook, no arXiv URL)
626	#   - holland_1993_dif: verified=false (textbook, no DOI confirmed)
627	#   - paper_framing.md references "Lalor et al., AAAI 2024" — closest match is EACL 2024 tutorial
628	#   - weller2024selfcritique in writing_plan → actually wust2025selfcritique
629	#   - paper_framing.md references "ATLAS (Baffour et al., 2024)" — actual paper is Li et al., 2024 (arxiv 2511.04689)
630	#   - paper_framing.md references "PSN-IRT (Yao et al., 2024)" — actual paper is Zhou et al., 2025 (AAAI 2026)
631	#   - paper_framing.md references "DCR (Dekoninck et al., EMNLP 2025)" — actual DCR is Xu et al. (Dekoninck authored ConStat)
632	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "c6458267-8af0-4e88-b2c5-5be88578e953",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/literature_map.yaml",
      "content": "# Literature Map — contamcal-irt-calibration\n# Generated: 2026-05-16\n# Purpose: Related Work section foundation for ContamCal paper (EMNLP 2026)\n\npapers:\n\n  # ============================================================\n  # Category: detection — Contamination Detection Methods\n  # ============================================================\n\n  - id: \"zhang_2024_minkpp\"\n    title: \"Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large Language Models\"\n    authors: \"Zhang et al.\"\n    venue: \"ICLR 2025\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2404.02936\"\n    category: \"detection\"\n    role: \"method-component\"\n    relevance: \"Our S2 signal. Min-K%++ normalizes token probability with vocabulary statistics for membership inference. We discover its directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — a novel finding that challenges single-signal reliance.\"\n    key_findings: \"Theoretically motivated detection via normalized token probabilities; outperforms Min-K% on WikiMIA and other benchmarks.\"\n    our_advantage: \"ContamCal reveals Min-K++ is actively misleading (not just ineffective) at small scales — directional reversal is our headline empirical finding.\"\n\n  - id: \"shi_2023_minkprob\"\n    title: \"Detecting Pretraining Data from Large Language Models\"\n    authors: \"Shi et al.\"\n    venue: \"ICLR 2024\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2310.16789\"\n    category: \"detection\"\n    role: \"foundation\"\n    relevance: \"Original Min-K% Prob method and WikiMIA benchmark. Foundation for membership inference in LLMs. Min-K%++ (our S2) is a direct extension.\"\n    key_findings: \"Unseen examples have outlier low-probability tokens; Min-K% uses this for pretraining data detection without reference model.\"\n    our_advantage: \"We use the improved Min-K%++ variant and expose its failure modes at small scales.\"\n\n  - id: \"dekoninck_2024_constat\"\n    title: \"ConStat: Performance-Based Contamination Detection in Large Language Models\"\n    authors: \"Dekoninck et al.\"\n    venue: \"arXiv 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2405.16281\"\n    category: \"detection\"\n    role: \"method-component\"\n    relevance: \"Our S3 signal candidate (excluded from final pipeline). Detects contamination as non-generalizing inflated performance by comparing primary vs reference benchmark performance against reference models.\"\n    key_findings: \"Novel contamination definition as non-generalizing performance inflation; detects contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models.\"\n    our_advantage: \"ConStat requires reference benchmarks and reference models; ContamCal integrates detection signals directly into IRT framework for calibrated score adjustment, not just detection.\"\n\n  - id: \"dong_2024_cdd\"\n    title: \"Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models\"\n    authors: \"Dong et al.\"\n    venue: \"ACL 2024 Findings\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.15938\"\n    category: \"detection\"\n    role: \"direct-competitor\"\n    relevance: \"Proposes CDD (output distribution peakedness) and TED (distribution correction for trustworthy evaluation). TED is closest to calibration but lacks IRT grounding and uncertainty quantification.\"\n    key_findings: \"CDD achieves 21-30% improvement over baselines in detection accuracy; TED mitigates up to 66.9% of contamination-attributed performance gain.\"\n    our_advantage: \"ContamCal provides full uncertainty quantification via Bayesian IRT posteriors; TED offers point corrections without credible intervals or identifiability analysis.\"\n\n  - id: \"zhang_2024_gsm1k\"\n    title: \"A Careful Examination of Large Language Model Performance on Grade School Arithmetic\"\n    authors: \"Zhang et al.\"\n    venue: \"arXiv 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2405.00332\"\n    category: \"detection\"\n    role: \"method-component\"\n    relevance: \"Our S4 signal (self-critique / GSM1k). Creates GSM1k to mirror GSM8k and measures accuracy drop as contamination proxy. Up to 13% accuracy drops in some model families.\"\n    key_findings: \"Systematic overfitting in Phi and Mistral families; positive correlation (r^2=0.32) between generation probability of GSM8k examples and performance gap.\"\n    our_advantage: \"ContamCal uses the GSM1k-style signal as one input to multi-signal RRF, then feeds into IRT for calibrated estimates rather than just flagging contamination.\"\n\n  - id: \"choi_2025_kds\"\n    title: \"How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence\"\n    authors: \"Choi et al.\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2502.00678\"\n    category: \"detection\"\n    role: \"evaluation\"\n    relevance: \"Kernel Divergence Score (KDS) detects contamination via embedding shift before/after fine-tuning. Near-perfect correlation with contamination levels. Complementary signal approach to our S1 embedding similarity.\"\n    key_findings: \"KDS captures fine-tuning-induced shifts in sample embeddings; outperforms existing baselines with near-perfect contamination level correlation.\"\n    our_advantage: \"ContamCal bridges detection to calibration; KDS only detects. Our S1 embedding similarity achieves AUC>0.95 without requiring fine-tuning comparison.\"\n\n  - id: \"oren_2023_proving_contamination\"\n    title: \"Proving Test Set Contamination in Black Box Language Models\"\n    authors: \"Oren et al.\"\n    venue: \"arXiv 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2310.17623\"\n    category: \"detection\"\n    role: \"background\"\n    relevance: \"Provable contamination detection via exchangeability test on benchmark ordering likelihood. Complementary black-box approach.\"\n    key_findings: \"Detects contamination in models as small as 1.4B with 1000 examples; audits 5 popular LLMs finding little pervasive contamination.\"\n    our_advantage: \"ContamCal goes beyond detection to calibrated score adjustment with uncertainty quantification.\"\n\n  - id: \"deng_2024_tsguessing\"\n    title: \"Investigating Data Contamination in Modern Benchmarks for Large Language Models\"\n    authors: \"Deng, Zhao, Tang, Gerstein, & Cohan\"\n    year: 2024\n    venue: \"NAACL 2024\"\n    url: \"https://arxiv.org/abs/2311.09783\"\n    category: \"detection\"\n    role: \"direct-competitor\"\n    relevance: \"TS-Guessing protocol masks MC wrong options for fill-in; ChatGPT/GPT-4 guess correct options at 52%/57% on MMLU. Direct evidence that MC format is more vulnerable to contamination, supporting our finding that ARC (MC) shows γ>0 while GSM8K (generative) shows γ≈0.\"\n    key_findings:\n      - \"MC format enables contaminated models to exploit memorized answer options\"\n      - \"ChatGPT/GPT-4 MMLU option guessing rate 52%/57% vs random baseline\"\n      - \"Open-ended format harder to game via memorization\"\n\n  - id: \"schaeffer_2026_generative_contamination\"\n    title: \"Quantifying the Effect of Test Set Contamination on Generative Evaluations\"\n    authors: \"Schaeffer, Kazdan, Abbasi, Liu, et al.\"\n    year: 2026\n    venue: \"arXiv 2026\"\n    url: \"https://arxiv.org/abs/2601.04301\"\n    category: \"detection\"\n    role: \"direct-competitor\"\n    relevance: \"First scaling law study of contamination on generative benchmarks (MATH). Even 1 test set replica in pretraining breaks irreducible error floor, but effect size much smaller than MC benchmarks. Consistent with our framework: generative γ expected smaller but non-zero.\"\n    key_findings:\n      - \"Single test set replica in pretraining corpus breaks irreducible error on MATH\"\n      - \"Contamination effect on generative benchmarks weaker than MC benchmarks\"\n      - \"Scaling law characterization of contamination-performance relationship\"\n\n  # ============================================================\n  # Category: irt-llm — IRT for LLM Evaluation\n  # ============================================================\n\n  - id: \"lalor_2024_irt_nlp\"\n    title: \"Item Response Theory for Natural Language Processing\"\n    authors: \"Lalor et al.\"\n    venue: \"EACL 2024 Tutorial\"\n    year: 2024\n    url: \"https://aclanthology.org/2024.eacl-tutorials.2/\"\n    category: \"irt-llm\"\n    role: \"foundation\"\n    relevance: \"Comprehensive tutorial introducing IRT to NLP community. Establishes framework for psychometric LLM evaluation that ContamCal extends with contamination covariates.\"\n    key_findings: \"Demonstrates IRT benefits for NLP evaluation including difficulty estimation, benchmark quality assessment, and latent trait modeling.\"\n    our_advantage: \"ContamCal extends standard IRT with contamination covariate gamma, measurement error model, and per-benchmark effect estimation.\"\n\n  - id: \"polo_2024_tinybenchmarks\"\n    title: \"tinyBenchmarks: evaluating LLMs with fewer examples\"\n    authors: \"Polo et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2402.14992\"\n    category: \"irt-llm\"\n    role: \"foundation\"\n    relevance: \"Uses IRT as performance estimator; 100 curated examples sufficient for MMLU. Demonstrates IRT scalability for LLM evaluation. Shares our assumption that IRT item parameters transfer across models.\"\n    key_findings: \"Accurate performance estimation with ~100 items per benchmark; IRT-based selection outperforms random subsampling.\"\n    our_advantage: \"ContamCal addresses a different problem: not efficiency but decontamination. We use IRT to model contamination effects rather than to reduce evaluation cost.\"\n\n  - id: \"habba_2025_growing_pains\"\n    title: \"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\"\n    authors: \"Habba et al.\"\n    venue: \"arXiv 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2604.12843\"\n    category: \"irt-llm\"\n    role: \"foundation\"\n    relevance: \"Multidimensional IRT with anchor items for cross-study comparability. Addresses N insufficiency via fixed parameter calibration. Directly relevant to our N>=50 identifiability concern.\"\n    key_findings: \"Predicts full-evaluation performance within 2-3pp using 100 anchor items; Spearman rho>=0.9 across 400+ models.\"\n    our_advantage: \"Growing Pains assumes no contamination; ContamCal explicitly models contamination effects. Their anchor-item framework could complement our decontamination pipeline.\"\n\n  - id: \"luettgau_2025_hibayes\"\n    title: \"HiBayES: A Hierarchical Bayesian Modeling Framework for AI Evaluation Statistics\"\n    authors: \"Luettgau et al.\"\n    venue: \"arXiv 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.05602\"\n    category: \"irt-llm\"\n    role: \"direct-competitor\"\n    relevance: \"Hierarchical Bayesian framework for LLM evaluation with principled UQ, especially in low-data scenarios (<20 data points). Does not model contamination. Most methodologically similar to ContamCal's Bayesian approach.\"\n    key_findings: \"Robust parameter estimation via hierarchical GLMs with formal model comparison; handles nested evaluation structures.\"\n    our_advantage: \"ContamCal adds contamination-specific covariates (gamma_k, exposure scores) to the Bayesian framework. HiBayES provides UQ but ignores contamination effects entirely.\"\n\n  - id: \"li_2024_atlas\"\n    title: \"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\"\n    authors: \"Li et al.\"\n    venue: \"arXiv 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2511.04689\"\n    category: \"irt-llm\"\n    role: \"evaluation\"\n    relevance: \"ATLAS uses Fisher information-guided adaptive item selection for efficient LLM evaluation with up to 90% item reduction. Validates IRT psychometric framework for LLM evaluation.\"\n    key_findings: \"30-89 items per benchmark sufficient with SE-controlled stopping; best accuracy-efficiency tradeoff among IRT-based methods.\"\n    our_advantage: \"ATLAS optimizes evaluation efficiency; ContamCal addresses evaluation validity under contamination. Complementary goals.\"\n\n  - id: \"zhou_2025_psnirt\"\n    title: \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n    authors: \"Zhou et al.\"\n    venue: \"AAAI 2026\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2505.15055\"\n    category: \"irt-llm\"\n    role: \"evaluation\"\n    relevance: \"PSN-IRT uses pseudo-siamese networks for rich item parameter estimation. Analyzes 11 benchmarks (41,871 items) revealing measurement quality shortcomings.\"\n    key_findings: \"LLM benchmarks suffer widespread saturation and insufficient difficulty ceilings; PSN-IRT constructs smaller benchmarks with stronger human preference alignment.\"\n    our_advantage: \"PSN-IRT diagnoses benchmark quality; ContamCal diagnoses and corrects contamination effects. Our gamma_k captures a specific quality dimension (data leakage) that PSN-IRT does not model.\"\n\n  - id: \"burnell_2023_structure\"\n    title: \"Revealing the structure of language model capabilities\"\n    authors: \"Burnell et al.\"\n    venue: \"arXiv 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2306.10062\"\n    category: \"irt-llm\"\n    role: \"background\"\n    relevance: \"Factor analysis reveals 3 capability dimensions (reasoning, comprehension, core language modeling) in LLMs. Supports multidimensional view; our unidimensional theta per benchmark is acknowledged as simplification in Limitations.\"\n    key_findings: \"LLM capabilities are not monolithic; 3 factors explain high proportion of performance variance across 29 LLMs on 27 tasks.\"\n    our_advantage: \"ContamCal's unidimensional theta per benchmark is a deliberate simplification acknowledged in Limitations; multidimensional extension is future work.\"\n\n  - id: \"brown_2024_ppp\"\n    title: \"The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation\"\n    authors: \"Brown & Thomson\"\n    year: 2024\n    venue: \"Molecular Biology and Evolution, 41(3), msae051\"\n    category: \"irt-llm\"\n    role: \"background\"\n    relevance: \"Proves PPP distribution is inherently non-uniform (unlike frequentist p-values), concentrated near 0.5. Extreme PPP (e.g. our 0.003) provides stronger poor-fit evidence than usually assumed, but low PPP does not automatically invalidate parameter estimates — supports our position that γ posterior excluding zero remains informative even with poor global fit.\"\n    key_findings:\n      - \"PPP distribution is non-uniform, concentrated around 0.5\"\n      - \"Low PPP does not automatically negate parameter estimate informativeness\"\n      - \"Posterior predictive tests evaluate models under favorable conditions (model already fitted to data)\"\n\n  - id: \"sinharay_2025_irt_fit\"\n    title: \"Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions\"\n    authors: \"Sinharay, S.\"\n    year: 2025\n    venue: \"British Journal of Mathematical and Statistical Psychology, 78, 711–733\"\n    category: \"irt-llm\"\n    role: \"background\"\n    relevance: \"Comprehensive review of IRT model fit assessment (PPMC, generalized residuals, person-fit). Argues low PPP indicates model inadequacy but not that parameter estimates are meaningless. Supports our ARC PPP=0.003 but γ still interpretable position.\"\n    key_findings:\n      - \"PPP interpretation requires caution — low PPP means model inadequacy, not parameter invalidity\"\n      - \"Covers PPMC, generalized residuals, person-fit diagnostics\"\n      - \"Authoritative 2025 review likely known to reviewers\"\n\n  # ============================================================\n  # Category: item-compromise — Educational Measurement\n  # ============================================================\n\n  - id: \"eckerly_2017_item_compromise\"\n    title: \"Detecting preknowledge and item compromise: Understanding the status quo\"\n    authors: \"Eckerly, C.\"\n    venue: \"Handbook of Quantitative Methods for Detecting Cheating on Tests (Routledge)\"\n    year: 2017\n    url: \"https://www.routledge.com/9781138821811\"\n    category: \"item-compromise\"\n    role: \"foundation\"\n    relevance: \"Core theoretical foundation for ContamCal. Reviews IRT methods for detecting compromised items and examinees with preknowledge. Our gamma parameter directly extends the item compromise framework to LLM benchmark contamination.\"\n    key_findings: \"Systematic framework for item preknowledge detection using IRT-based person-fit statistics and item parameter drift.\"\n    our_advantage: \"ContamCal adapts item compromise IRT from human testing to LLM evaluation with 3 structural adaptations: independent examinees -> single model, binary leakage -> continuous exposure, stable ability -> regime-conditional ability.\"\n    verified: false\n\n  - id: \"sinharay_2017_preknowledge\"\n    title: \"Detection of item preknowledge using likelihood ratio test and score test\"\n    authors: \"Sinharay, S.\"\n    venue: \"Journal of Educational and Behavioral Statistics, 42(1)\"\n    year: 2017\n    url: \"https://pubmed.ncbi.nlm.nih.gov/29881099/\"\n    category: \"item-compromise\"\n    role: \"foundation\"\n    relevance: \"Proposes LRT-based statistics for item preknowledge detection with known Type I error rates. Our treatment of contamination-induced item parameter drift builds on this work.\"\n    key_findings: \"LRT statistic for item preknowledge has similar power to posterior shift statistic with known null distribution; applicable to adaptive and non-adaptive tests.\"\n    our_advantage: \"ContamCal extends from binary preknowledge to continuous contamination exposure scores and from human examinees to LLM respondents.\"\n\n  - id: \"deboeck_2004_explanatory_irt\"\n    title: \"Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach\"\n    authors: \"De Boeck, P. & Wilson, M.\"\n    venue: \"Springer\"\n    year: 2004\n    url: \"https://link.springer.com/book/10.1007/978-1-4757-3990-9\"\n    category: \"item-compromise\"\n    role: \"foundation\"\n    relevance: \"Foundational text for explanatory IRT. ContamCal's contamination-augmented 4PL is an explanatory IRT model where item responses are modeled as a function of contamination exposure predictors.\"\n    key_findings: \"Unifies IRT with generalized linear/nonlinear mixed models; enables item covariates (like our exposure scores) as predictors in IRT framework.\"\n    our_advantage: \"Direct theoretical grounding. ContamCal instantiates the explanatory IRT framework with contamination-specific covariates.\"\n\n  - id: \"kievit_2013_simpsons_paradox\"\n    title: \"Simpson's Paradox in Psychological Science: A Practical Guide\"\n    authors: \"Kievit, Frankenhuis, Waldorp, & Borsboom\"\n    year: 2013\n    venue: \"Frontiers in Psychology, 4, 513\"\n    category: \"item-compromise\"\n    role: \"background\"\n    relevance: \"Theoretical framework for Simpson's paradox in behavioral science. Directly applicable to our MMLU finding: pooled γ insignificant but domain-level analysis reveals significant positive and negative γ that cancel upon aggregation.\"\n    key_findings:\n      - \"Simpson's paradox more prevalent in psychology than traditionally recognized\"\n      - \"Effect direction can reverse when moving from population to subgroup (or vice versa)\"\n      - \"Provides statistical markers and R detection toolkit\"\n\n  - id: \"ercikan_2008_dif_cancellation\"\n    title: \"Differential Item Functioning Amplification and Cancellation in a Reading Test\"\n    authors: \"Ercikan, Arim, & Oliveri\"\n    year: 2008\n    venue: \"Practical Assessment, Research, and Evaluation, 14(3)\"\n    category: \"item-compromise\"\n    role: \"background\"\n    relevance: \"Empirical precedent for DIF cancellation: most items show significant DIF but favoring different groups, so DIF cancels at total test score level. Direct analogue to our MMLU domain-level contamination signals with inconsistent directions being masked in pooled analysis.\"\n    key_findings:\n      - \"Majority of items show significant DIF but in opposing directions\"\n      - \"DIF cancels at aggregate test score level despite item-level significance\"\n      - \"Multiple-group testlet IRT model reveals hidden heterogeneity\"\n\n  # ============================================================\n  # Category: calibration — Calibration & Score Adjustment\n  # ============================================================\n\n  - id: \"xu_2025_dcr\"\n    title: \"DCR: Quantifying Data Contamination in LLMs Evaluation\"\n    authors: \"Xu et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2507.11405\"\n    category: \"calibration\"\n    role: \"direct-competitor\"\n    relevance: \"Only existing method producing adjusted accuracy via fuzzy inference. ContamCal's primary competitor. DCR quantifies contamination risk across 4 levels (semantic, informational, data, label) and adjusts raw accuracy.\"\n    key_findings: \"DCR Factor adjusts accuracy within 4% average error across 3 benchmarks; validated on 0.5B-72B models.\"\n    our_advantage: \"ContamCal provides Bayesian credible intervals (DCR gives point estimates only), per-benchmark gamma_k characterization, and IRT-grounded identifiability analysis. DCR lacks UQ and theoretical identifiability bounds.\"\n\n  - id: \"guo_2017_calibration\"\n    title: \"On Calibration of Modern Neural Networks\"\n    authors: \"Guo et al.\"\n    venue: \"ICML 2017\"\n    year: 2017\n    url: \"https://arxiv.org/abs/1706.04599\"\n    category: \"calibration\"\n    role: \"background\"\n    relevance: \"Foundational work on probability calibration in neural networks. Must disambiguate: our 'calibration' means decontamination score adjustment, not probability calibration (confidence = accuracy). Temperature scaling is unrelated to our method.\"\n    key_findings: \"Modern neural networks are poorly calibrated; temperature scaling (single parameter) effectively recalibrates predictions.\"\n    our_advantage: \"Different notion of calibration. Guo et al. calibrate prediction confidence; ContamCal calibrates benchmark scores for contamination effects.\"\n\n  - id: \"angelopoulos_2023_conformal\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    venue: \"Foundations and Trends in ML, 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"calibration\"\n    role: \"background\"\n    relevance: \"Alternative UQ approach with distribution-free coverage guarantees. Discussed in Related Work to justify why Bayesian IRT is preferred over conformal for our setting (conformal requires exchangeability assumptions violated by contamination structure).\"\n    key_findings: \"Conformal prediction provides statistically rigorous uncertainty sets without distributional assumptions; applicable to any pre-trained model.\"\n    our_advantage: \"Bayesian IRT provides interpretable per-item parameters and contamination-specific covariates; conformal gives coverage guarantees but no mechanistic insight into contamination effects.\"\n\n  # ============================================================\n  # Category: mitigation — Contamination Mitigation & Alternatives\n  # ============================================================\n\n  - id: \"sun_2025_emperors_new_clothes\"\n    title: \"The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contamination\"\n    authors: \"Sun et al.\"\n    venue: \"ICML 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2503.16402\"\n    category: \"mitigation\"\n    role: \"direct-competitor\"\n    relevance: \"Demonstrates all 20 existing mitigation strategies fail to balance fidelity and contamination resistance across all benchmarks. Strongest motivation for ContamCal's post-hoc calibration approach.\"\n    key_findings: \"No semantic-preserving strategy significantly improves resistance over vanilla; semantic-altering strategies sacrifice fidelity. 10 LLMs x 5 benchmarks x 20 strategies x 2 scenarios.\"\n    our_advantage: \"ContamCal offers post-hoc calibration rather than prevention — complementary approach. Emperor's failure motivates calibration; ContamCal provides it.\"\n\n  - id: \"white_2024_livebench\"\n    title: \"LiveBench: A Challenging, Contamination-Free LLM Benchmark\"\n    authors: \"White et al.\"\n    venue: \"arXiv 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.19314\"\n    category: \"mitigation\"\n    role: \"evaluation\"\n    relevance: \"Dynamic benchmark alternative: monthly-updated questions from recent sources to prevent contamination. Complementary to ContamCal — LiveBench prevents contamination for new evaluations; ContamCal calibrates existing contaminated benchmarks.\"\n    key_findings: \"Top models achieve below 70% accuracy; monthly updates with 18 tasks across 6 categories maintain contamination resistance.\"\n    our_advantage: \"LiveBench requires continuous curation; ContamCal works with existing static benchmarks. Both valid approaches to the contamination problem.\"\n\n  # ============================================================\n  # Category: benchmark — Evaluation Frameworks & Alternatives\n  # ============================================================\n\n  - id: \"liang_2023_helm\"\n    title: \"Holistic Evaluation of Language Models\"\n    authors: \"Liang et al.\"\n    venue: \"TMLR 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2211.09110\"\n    category: \"benchmark\"\n    role: \"background\"\n    relevance: \"HELM evaluates 30 models on 42 scenarios with 7 metrics including calibration. Establishes standardized evaluation framework. ContamCal addresses a gap HELM does not: score reliability under contamination.\"\n    key_findings: \"Prior to HELM, models were evaluated on only 17.9% of core scenarios; standardized evaluation reveals 25 top-level findings across models.\"\n    our_advantage: \"HELM assumes benchmark scores are trustworthy; ContamCal questions and corrects this assumption when contamination is present.\"\n\n  - id: \"chiang_2024_chatbot_arena\"\n    title: \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\"\n    authors: \"Chiang et al.\"\n    venue: \"ICML 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2403.04132\"\n    category: \"benchmark\"\n    role: \"background\"\n    relevance: \"Human pairwise comparison evaluation that inherently bypasses benchmark contamination. Discussed as contamination-resistant alternative.\"\n    key_findings: \"240K+ votes via crowdsourced pairwise comparisons; Elo rating system for model ranking without static test sets.\"\n    our_advantage: \"Chatbot Arena requires human judges and live interaction; ContamCal enables post-hoc calibration of automated benchmark scores, which scale better.\"\n\n  - id: \"li_2024_open_llm_leaderboard\"\n    title: \"Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena\"\n    authors: \"Li et al.\"\n    year: 2024\n    venue: \"arXiv 2024\"\n    url: \"https://arxiv.org/abs/2406.07545\"\n    category: \"benchmark\"\n    role: \"evaluation\"\n    relevance: \"Converting MC benchmarks to open-style questions causes ~25% average accuracy drop across all models. Quantifies MC format advantage (selection bias, random guessing) that amplifies contamination signal in MC benchmarks. Supports our MC/generative format as contamination effect moderator.\"\n    key_findings:\n      - \"MC to open-style conversion causes ~25% average accuracy drop\"\n      - \"MC format provides extra cues (selection bias, random guessing) beyond knowledge\"\n      - \"Contaminated models benefit more from MC format than clean models\"\n\n  # ============================================================\n  # Category: foundation — Methodological Foundations\n  # ============================================================\n\n  - id: \"shokri_2017_mia\"\n    title: \"Membership Inference Attacks Against Machine Learning Models\"\n    authors: \"Shokri et al.\"\n    venue: \"IEEE S&P 2017\"\n    year: 2017\n    url: \"https://arxiv.org/abs/1610.05820\"\n    category: \"detection\"\n    role: \"foundation\"\n    relevance: \"Foundational MIA work. Min-K% and Min-K%++ are descendants of MIA methodology. Contextualizes our Min-K++ directional reversal finding within MIA literature.\"\n    key_findings: \"Shadow model approach for membership inference; demonstrates vulnerability of ML-as-a-service models to membership inference.\"\n    our_advantage: \"ContamCal uses MIA-derived signals as inputs to calibration framework, not as standalone detectors.\"\n\n  - id: \"carlini_2021_extracting\"\n    title: \"Extracting Training Data from Large Language Models\"\n    authors: \"Carlini et al.\"\n    venue: \"USENIX Security 2021\"\n    year: 2021\n    url: \"https://arxiv.org/abs/2012.07805\"\n    category: \"detection\"\n    role: \"foundation\"\n    relevance: \"Demonstrates verbatim training data extraction from GPT-2. Establishes that LLMs memorize training data — the fundamental assumption underlying all contamination detection methods including ours.\"\n    key_findings: \"Hundreds of verbatim text sequences extracted from GPT-2; memorization is measurable and exploitable.\"\n    our_advantage: \"ContamCal leverages memorization signals for calibration rather than extraction; our contribution is bridging detection to score adjustment.\"\n\n  - id: \"cormack_2009_rrf\"\n    title: \"Reciprocal Rank Fusion outperforms Condorcet and Individual Rank Learning Methods\"\n    authors: \"Cormack et al.\"\n    venue: \"SIGIR 2009\"\n    year: 2009\n    url: \"https://dl.acm.org/doi/10.1145/1571941.1572114\"\n    category: \"calibration\"\n    role: \"method-component\"\n    relevance: \"RRF is our multi-signal aggregation method. Training-free rank fusion avoids meta-circularity (learned aggregator's training data may itself be contaminated). RRF is a design choice, not claimed as contribution.\"\n    key_findings: \"Simple reciprocal rank scoring outperforms Condorcet and learning-to-rank methods for combining multiple retrieval systems.\"\n    our_advantage: \"RRF is adopted as-is. Our contribution is the argument for training-free aggregation in the contamination context (meta-circularity).\"\n\n  - id: \"talts_2018_sbc\"\n    title: \"Validating Bayesian Inference Algorithms with Simulation-Based Calibration\"\n    authors: \"Talts et al.\"\n    venue: \"arXiv 2018\"\n    year: 2018\n    url: \"https://arxiv.org/abs/1804.06788\"\n    category: \"calibration\"\n    role: \"method-component\"\n    relevance: \"SBC is our 6th evaluation metric. Validates Bayesian inference by checking rank uniformity of posterior samples. Used to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation).\"\n    key_findings: \"General procedure for validating Bayesian posterior samplers; graphical diagnostics indicate nature of inference problems.\"\n    our_advantage: \"SBC is adopted as diagnostic tool. Our contribution is applying SBC to contamination-augmented IRT at realistic N_models to decompose coverage gaps.\"\n\n  # ============================================================\n  # Category: detection — Gap-Fill (must_cite)\n  # ============================================================\n\n  - id: \"wust_2025_selfcritique\"\n    title: \"Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations\"\n    authors: \"Wüst, Hoffmann, & Pang\"\n    venue: \"arXiv 2025\"\n    year: 2025\n    url: \"https://arxiv.org/abs/2510.09259\"\n    category: \"detection\"\n    role: \"method-component\"\n    relevance: \"Our S4 signal. Uses LLM self-evaluation entropy collapse as contamination indicator. We find it near-random (AUC≈0.50) at 0.5B scale — ineffective as standalone signal.\"\n    key_findings: \"Self-critique entropy patterns differ for memorized vs novel items.\"\n    our_advantage: \"ContamCal reveals S4 ineffectiveness and integrates it into multi-signal RRF where its noise is diluted.\"\n\n  - id: \"golchin_2024_time_travel\"\n    title: \"Time Travel in LLMs: Tracing Data Contamination in Large Language Models\"\n    authors: \"Golchin & Surdeanu\"\n    venue: \"ICLR 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2308.08493\"\n    category: \"detection\"\n    role: \"background\"\n    relevance: \"Proposes guided prompting to detect contamination via LLM's ability to reproduce benchmark instances. Complementary approach to our signal-based detection.\"\n    key_findings: \"Detects contamination across GPT-4, GPT-3.5, LLaMA-2 via instance reproduction; confirms widespread contamination in major LLMs.\"\n    our_advantage: \"Time Travel requires model generation access; ContamCal works with item-level responses only. Our approach quantifies effects, not just detects.\"\n\n  # ============================================================\n  # Category: mitigation — Gap-Fill (must_cite + supplementary)\n  # ============================================================\n\n  - id: \"li_2025_dcr\"\n    title: \"Decontaminated Calibration and Ranking for Trustworthy LLM Evaluation\"\n    authors: \"Li et al.\"\n    venue: \"EMNLP 2025\"\n    year: 2025\n    category: \"mitigation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest predecessor to ContamCal. DCR applies decontamination + calibration + ranking correction. Lacks IRT grounding, uncertainty quantification, and domain-level diagnosis. Key W1 comparison target.\"\n    key_findings: \"Score adjustment framework for contaminated benchmarks; demonstrates improved ranking consistency post-decontamination.\"\n    our_advantage: \"ContamCal provides: (1) Bayesian CIs vs point estimates, (2) domain-level γ diagnosis vs aggregate correction, (3) Fisher Info identifiability analysis, (4) Min-K++ reversal detection.\"\n    verified: false\n\n  - id: \"yang_2023_rethinking_benchmark\"\n    title: \"Rethinking Benchmark and Contamination for Language Models with Rephrased Samples\"\n    authors: \"Yang et al.\"\n    venue: \"arXiv 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2311.04850\"\n    category: \"mitigation\"\n    role: \"background\"\n    relevance: \"Rephrasing-based contamination mitigation: creates semantically equivalent but textually novel test items. Complementary to ContamCal's post-hoc calibration approach.\"\n    key_findings: \"Rephrased benchmarks show significant performance drops in contaminated models; surface-level memorization dominates.\"\n    our_advantage: \"Rephrasing prevents contamination for new evaluations; ContamCal calibrates existing contaminated scores. Different scope.\"\n\n  # ============================================================\n  # Category: benchmark — Gap-Fill (must_cite + supplementary)\n  # ============================================================\n\n  - id: \"zheng_2023_chatbot_arena\"\n    title: \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\"\n    authors: \"Zheng et al.\"\n    venue: \"NeurIPS 2023\"\n    year: 2023\n    url: \"https://arxiv.org/abs/2306.05685\"\n    category: \"benchmark\"\n    role: \"background\"\n    relevance: \"Chatbot Arena as contamination-resistant evaluation via live human preference. Motivates why static benchmark contamination matters — dynamic evaluations are expensive and limited to ranking.\"\n    key_findings: \"Strong agreement between MT-Bench automated and Chatbot Arena human evaluations; crowdsourced evaluation provides contamination-resistant rankings.\"\n    our_advantage: \"Chatbot Arena avoids contamination by design but cannot assess specific capabilities. ContamCal enables continued use of targeted static benchmarks with calibrated scores.\"\n\n  - id: \"wang_2024_mmlu_pro\"\n    title: \"MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\"\n    authors: \"Wang et al.\"\n    venue: \"arXiv 2024\"\n    year: 2024\n    url: \"https://arxiv.org/abs/2406.01574\"\n    category: \"benchmark\"\n    role: \"background\"\n    relevance: \"MMLU-Pro increases difficulty and reduces sensitivity to prompt format, partially addressing contamination concerns. Our MMLU domain-level γ analysis applies equally to MMLU-Pro since contamination is about memorization, not difficulty.\"\n    key_findings: \"10-option MC format reduces random guessing; more discriminative across model capabilities.\"\n    our_advantage: \"MMLU-Pro redesigns the benchmark; ContamCal calibrates existing benchmarks without redesign.\"\n\n  # ============================================================\n  # Category: irt-methodology — Gap-Fill (must_cite)\n  # ============================================================\n\n  - id: \"reckase_2009_mirt\"\n    title: \"Multidimensional Item Response Theory\"\n    authors: \"Reckase, M. D.\"\n    venue: \"Springer\"\n    year: 2009\n    category: \"irt-methodology\"\n    role: \"foundation\"\n    relevance: \"Canonical MIRT reference. Our 2PL+γ extends unidimensional IRT; multidimensional extensions discussed in future work for non-STEM domain misfit.\"\n    key_findings: \"Comprehensive MIRT framework including compensatory and non-compensatory models, parameter estimation, and model fit assessment.\"\n    our_advantage: \"ContamCal currently uses unidimensional IRT with contamination covariate. MIRT extension is future work for modeling domain-specific abilities.\"\n    verified: false\n\n  - id: \"mislevy_1986_bayes_irt\"\n    title: \"Bayes Modal Estimation in Item Response Models\"\n    authors: \"Mislevy, R. J.\"\n    venue: \"Psychometrika\"\n    year: 1986\n    category: \"irt-methodology\"\n    role: \"foundation\"\n    relevance: \"Foundational work on Bayesian estimation for IRT. Justifies our use of Bayesian (NUTS/Stan) inference for 2PL+γ parameter estimation with informative priors.\"\n    key_findings: \"Bayesian modal estimation provides regularization for IRT parameters; handles small samples better than MLE.\"\n    our_advantage: \"ContamCal builds on Bayesian IRT tradition, adding contamination-specific covariates and model comparison via PPP.\"\n\n  - id: \"sanmartin_2009_irt\"\n    title: \"Consequential Validity and Item Response Theory\"\n    authors: \"San Martín, Del Pino, & De Boeck\"\n    venue: \"Psychometrika\"\n    year: 2009\n    category: \"irt-methodology\"\n    role: \"foundation\"\n    relevance: \"Addresses consequential validity in IRT models — directly relevant to our calibration value decomposition (D120) where we separate ability estimation from contamination correction.\"\n    key_findings: \"Framework for assessing consequences of IRT model use; distinguishes construct-relevant from construct-irrelevant variance.\"\n    our_advantage: \"ContamCal's D120 decomposition directly operationalizes this distinction: γ correction vs θ estimation improvement.\"\n\n  - id: \"adams_1997_mrcml\"\n    title: \"The Multidimensional Random Coefficients Multinomial Logit Model\"\n    authors: \"Adams, Wilson, & Wang\"\n    venue: \"Applied Psychological Measurement\"\n    year: 1997\n    category: \"irt-methodology\"\n    role: \"foundation\"\n    relevance: \"Extends IRT to multidimensional random effects. Foundation for understanding our per-domain γ modeling within the broader IRT methodology.\"\n    key_findings: \"General framework for multidimensional IRT with random coefficients; handles nested item structures.\"\n    our_advantage: \"ContamCal uses a simpler contamination-specific extension (additive γ) rather than full MRCML.\"\n\n  # ============================================================\n  # Category: item-compromise — Gap-Fill (must_cite)\n  # ============================================================\n\n  - id: \"holland_1993_dif\"\n    title: \"Differential Item Functioning\"\n    authors: \"Holland, P. W. & Wainer, H. (Eds.)\"\n    venue: \"Lawrence Erlbaum Associates\"\n    year: 1993\n    category: \"item-compromise\"\n    role: \"foundation\"\n    relevance: \"Classic DIF reference. DIF methodology detects items that function differently across groups — analogous to our γ detecting contamination effects that vary across domains. DIF is the educational measurement precursor to our domain-differential analysis.\"\n    key_findings: \"Comprehensive DIF detection and analysis framework; establishes that item-level analysis is essential for fair measurement.\"\n    our_advantage: \"ContamCal extends DIF thinking to LLM contamination: 'exposed' vs 'unexposed' items replace traditional DIF group comparisons.\"\n    verified: false\n\n# ============================================================\n# Summary Statistics (Updated)\n# ============================================================\n# Total papers: 43\n# By category: detection=13, irt-llm=9, item-compromise=6, calibration=4, mitigation=4, benchmark=5, irt-methodology=4\n# By role: foundation=14, method-component=6, direct-competitor=7, evaluation=5, background=12\n# Must-cite coverage: 8/9 clusters filled (all must_cite accounted for)\n# Notes:\n#   - Eckerly 2017: verified=false (book chapter, no direct URL confirmed)\n#   - li_2025_dcr: verified=false (EMNLP 2025, need to confirm exact venue/URL)\n#   - reckase_2009_mirt: verified=false (textbook, no arXiv URL)\n#   - holland_1993_dif: verified=false (textbook, no DOI confirmed)\n#   - paper_framing.md references \"Lalor et al., AAAI 2024\" — closest match is EACL 2024 tutorial\n#   - weller2024selfcritique in writing_plan → actually wust2025selfcritique\n#   - paper_framing.md references \"ATLAS (Baffour et al., 2024)\" — actual paper is Li et al., 2024 (arxiv 2511.04689)\n#   - paper_framing.md references \"PSN-IRT (Yao et al., 2024)\" — actual paper is Zhou et al., 2025 (AAAI 2026)\n#   - paper_framing.md references \"DCR (Dekoninck et al., EMNLP 2025)\" — actual DCR is Xu et al. (Dekoninck authored ConStat)\n",
      "numLines": 632,
      "startLine": 1,
      "totalLines": 632
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

Now I'll back up the existing .bib and generate the merged file. Let me first create the backup.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "7906245d-f063-4d9a-bb48-105fbff31928",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ft53VQMo75yMNp8QkV8zik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9062,
      "cache_creation_input_tokens": 12944,
      "cache_read_input_tokens": 26503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12944
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_011Keee93HCbVMcU1ycy2uRU`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib.prev",
  "description": "Backup existing references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "2df94061-4bf0-4747-b3f4-244cf4f4fe61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ft53VQMo75yMNp8QkV8zik",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9062,
      "cache_creation_input_tokens": 12944,
      "cache_read_input_tokens": 26503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12944
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

_source line 12 · 2026-05-17T03:49:11.622Z_

<details><summary>↩ Tool result · `toolu_011Keee93HCbVMcU1ycy2uRU`</summary>

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
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "54b1af7b-4378-4de1-9520-a12de16db487",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I need to map the literature_map entries to their bibtex keys and check which ones already exist in the .bib file. Let me analyze:

Literature map entries (43 total):
1. zhang_2024_minkpp → existing key: duan2025minkpp (different key)
2. shi_2023_minkprob → not in bib
3. dekoninck_2024_constat → existing: dekoninck2024constat
4. dong_2024_cdd → not in bib
5. zhang_2024_gsm1k → not in bib


6. choi_2025_kds → existing: xu2025kds (different key, might be the same paper)
7. oren_2023_proving_contamination → existing: oren2024proving (year mismatch)
8. deng_2024_tsguessing → not in bib
9. schaeffer_2026_generative_contamination → need to verify against dong2026dose by checking titles and arxiv IDs to confirm they're different papers or duplicates with wrong metadata
10. lalor_2024_irt_nlp → existing: lalor2024irt (conflicting venue info - AAAI 2024 vs EACL 2024 Tutorial)
11. polo_2024_tinybenchmarks → existing: polo2024tinybenchmarks (matches)
12. habba_2025_growing_pains → existing: polo2026growing (different key, same arxiv ID 2604.12843)
13. luettgau_2025_hibayes → existing: zhuang2025hibayes (different key, same arxiv ID 2505.05602)
14. li_2024_atlas → existing: lyu2025atlas (different key, same arxiv ID 2511.04689)
15. zhou_2025 (entry appears incomplete)

Now I'm checking the remaining entries - zhou_2025_psnirt has a matching arxiv ID with gu2026psnirt but the existing entry lacks the arxiv number. Several entries like burnell_2023, brown_2024, and sinharay_2025 aren't in the bibliography at all, while others like eckerly_2017, sinharay_2017, and deboeck_2004 have existing entries that may need verification or updating. I'm also spotting ercikan_2008 which appears to be cut off.

For the DCR papers, I'm finding two distinct entries in the literature map - one by Xu et al. and one by Li et al., both from EMNLP 2025 but with different arxiv IDs and titles, so these should be kept separate even though the existing bibliography only has the Li version. Guo_2017_calibration matches the existing guo2017calibration entry.

Now I'm going through the remaining entries: angelopoulos_2023_conformal is already in the bibliography, sun_2025_emperors_new_clothes corresponds to xu2025emperor (same arxiv ID despite the different key), white_2024_livebench exists, but liang_2023_helm, chiang_2024_chatbot_arena, li_2024_open_llm_leaderboard, shokri_2017_mia, and carlini_2021_extracting are missing from the current bibliography. For the older entries, cormack_2009_rrf matches cormack2009 and talts_2018_sbc is already there.

Continuing down the list, wust_2025_selfcritique exists as expected, golchin_2024_time_travel is missing, li_2025_dcr is a match, but yang_2023_rethinking_benchmark, zheng_2023_chatbot_arena, wang_2024_mmlu_pro, and several others like reckase_2009_mirt, mislevy_1986_bayes_irt, sanmartin_2009_irt, and adams_1997_mrcml are either already present or need to be checked against the existing entries.

Now I'm hitting a key issue: the literature_map uses IDs like `zhang_2024_minkpp` as bibtex keys, but the existing .bib file uses different conventions like `duan2025minkpp`. The instructions say to use literature_map IDs as keys and preserve existing entries if they're complete matches, but these don't align. I need to clarify whether I should standardize all keys to the literature_map format or keep the existing ones when content matches. I'm realizing the merge strategy needs clarification—the goal should be to have entries with literature_map IDs as keys, keeping existing entries that already match those keys, while replacing any duplicates that use different keys but reference the same papers. I'm realizing the safest approach is to keep all existing bib entries since the .tex files reference them by their current keys, and adding new entries with literature_map ids would create duplicates without breaking the documents. The real challenge is that changing keys would require updating all the .tex file references, which isn't part of this task. I need to clarify the format for the literature_map IDs as BibTeX keys—underscores are valid, so I'll use them as-is. Now I'm mapping out each of the 43 literature entries to their appropriate BibTeX entry types based on their publication venues, then I'll merge everything into a single alphabetically sorted bibliography file while preserving all existing entries. Continuing through the bibliography entries, I'm cataloging the remaining references with their publication types and venues—working through items 13 through 22, which include arXiv papers, conference proceedings, journal articles across various fields like psychology and molecular biology, and a handbook chapter. Continuing through the bibliography entries, I'm cataloging more papers on membership inference attacks, data extraction vulnerabilities, and recent benchmark evaluations from major conferences and preprint servers.

Now I'm going back through my literature map to do a proper count of all the entries I've included, starting from the beginning to make sure I have the right total. I'm continuing through the bibliography and noticing a discrepancy—I've counted 46 entries but the header indicates 43, so I need to recount carefully to figure out where the mismatch is. Now I'm verifying the counts for each category against the YAML entries. Detection has 13 papers, IRT-LLM has 9, item-compromise has 6, and I'm checking calibration next which appears to have at least 3 entries so far. I'm tallying up the remaining categories—benchmark gives me 5 entries, irt-methodology has 4, bringing my total to 46 across all categories. The YAML summary claims 43, but I'm going to trust my count and include all the entries I've found.

Now I'm double-checking the categorization more carefully. I notice cormack_2009_rrf and talts_2018_sbc are both marked as calibration entries, which would make 5 in that category rather than the 4 the summary indicates. There's a small discrepancy, but I'll proceed with processing everything I've identified.

Looking at the detection section, I'm counting 9 entries across the main detection area and the specialized subsections like irt-llm and item-compromise, with the item-compromise section still being tallied. Continuing with the benchmark gap-fill section, I'm adding two more papers to reach a total of 2 entries. Now I'm moving into the IRT methodology gap-fill with four foundational papers on item response theory and Bayesian approaches. There's also one paper on item compromise detection. Let me recalculate the total—I'm getting 46 entries across all sections, but the YAML structure shows 43, so I need to recount more carefully by going through the actual entries in the file. Continuing through the bibliography with more recent work on differential item functioning, calibration methods, and various benchmark evaluations including conformal prediction approaches, live benchmarking systems, and membership inference attacks.

Now I'm noticing a discrepancy—the YAML metadata indicates 43 entries but I'm actually counting 46 when I go through them systematically. Let me verify by listing them out to make sure I capture all of them correctly.

Continuing through the rest of the bibliography entries from schaeffer_2026 through white_2024_livebench, bringing the total count to 28 so far.

Now I'm seeing the full list extends to 46 entries, not 43 as the summary indicated. The discrepancy is becoming clear as I work through the complete bibliography.

For the merge strategy, I should generate entries for all 46 papers using their literature_map IDs, preserve any existing entries that don't overlap with these, and remove clear duplicates where the same paper appears under different keys.

Looking at the existing entries, most map to literature_map papers, but a few like lord1980 aren't in the map at all, so those stay. For entries like eckerly2017 and sinharay2017 that do match literature_map papers, I need to check if they're actually the same work or different papers by the same author—if they're duplicates, I'll replace them with the new standardized keys. Carpenter2017 isn't in the literature map either, so I'll keep it. Talts2018sbc matches and needs replacing. For duan2025minkpp, the literature map has the correct authors as Zhang et al., so I'll use that version instead of the existing entry with wrong authors. Dekoninck2024constat matches but has conflicting venue information between NeurIPS 2024 and arXiv 2024 that I need to resolve. Now I'm checking the arxiv IDs more carefully—several entries have the same arxiv numbers but mismatched titles and authors in the existing bibliography. The literature map has the correct metadata for these papers, so I need to replace those entries with the accurate information from the lit map. A few more keys still need to be matched up. Continuing through the rest of the entries, I see that zhuang2025hibayes matches luettgau_2025_hibayes with the same arxiv identifier, so the first author needs updating. For lalor2024irt, there's a potential mismatch—the existing entry is an AAAI 2024 paper while the literature map points to an EACL 2024 tutorial, which could be two different works, so I'll keep both. The li2025dcr entry matches directly, and yang2024inference isn't in the literature map so it stays.

Moving through the benchmarking papers, most of them—including the silicon valley reference, MMLU, GSM8K, ARC, HumanEval, and the recent benchmarking work—don't appear in the literature map, so those remain unchanged. White's LiveBench and Polo's TinyBenchmarks both have matches and should be replaced. Holland's DIF paper matches and needs updating, while Thissen and Zumbo's DIF work aren't in the map. Guo's calibration paper and Angelopoulos' conformal prediction work both have matches to replace.

Continuing down the list, I'm finding that most of the remaining papers—TracIn, TRAK, the IRT and measurement theory papers by Reckase, Sanmartin, Mislevy, Wainer, Carroll, Fuller, Stefanski, Battauz, and Westfall—don't have corresponding entries in the literature map, so they'll stay as is. Reckase's MIRT paper does match and needs replacing.

Now I'm realizing the safest approach is to keep all the existing bibliography entries since they're already referenced in the .tex files, then add all 46 literature map entries as new keys. Even if some papers appear twice under different keys, BibTeX won't complain about unused entries, and this prevents any risk of breaking citations in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "5434aaa0-488e-4a49-a2aa-f19a2d349571",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H94u4HWT8x2FsxwaW4UJLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9264,
      "cache_read_input_tokens": 39447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9264
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

_source line 14_

Now I'll generate the merged references.bib with all 46 literature_map entries added (using their ids as keys) while preserving all existing entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "b96d5d9d-ad15-418a-a449-fa3429a1717f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H94u4HWT8x2FsxwaW4UJLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9264,
      "cache_read_input_tokens": 39447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9264
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

<details open><summary>🔧 Tool call — Write · `toolu_012M2RFvi3PxVwGHCu9coCyK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib",
  "content": "% ============================================================\n% Literature Map Entries (keys from literature_map.yaml ids)\n% ============================================================\n\n@inproceedings{adams_1997_mrcml,\n  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  booktitle = {Applied Psychological Measurement},\n  volume    = {21},\n  number    = {1},\n  pages     = {1--23},\n  year      = {1997}\n}\n\n@article{angelopoulos_2023_conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n  journal       = {Foundations and Trends in Machine Learning},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2107.07511}\n}\n\n@article{brown_2024_ppp,\n  author  = {Brown, Jeremy M. and Thomson, Robert C.},\n  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},\n  journal = {Molecular Biology and Evolution},\n  volume  = {41},\n  number  = {3},\n  pages   = {msae051},\n  year    = {2024}\n}\n\n@article{burnell_2023_structure,\n  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\\'{a}ndez-Orallo, Jos\\'{e}},\n  title         = {Revealing the Structure of Language Model Capabilities},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2306.10062},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2306.10062}\n}\n\n@inproceedings{carlini_2021_extracting,\n  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},\n  title     = {Extracting Training Data from Large Language Models},\n  booktitle = {Proceedings of the 30th USENIX Security Symposium},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2012.07805}\n}\n\n@inproceedings{chiang_2024_chatbot_arena,\n  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{choi_2025_kds,\n  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},\n  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.00678}\n}\n\n@inproceedings{cormack_2009_rrf,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM},\n  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}\n}\n\n@book{deboeck_2004_explanatory_irt,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York},\n  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}\n}\n\n@article{dekoninck_2024_constat,\n  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2405.16281},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2405.16281}\n}\n\n@inproceedings{deng_2024_tsguessing,\n  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},\n  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09783}\n}\n\n@inproceedings{dong_2024_cdd,\n  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},\n  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.15938}\n}\n\n@incollection{eckerly_2017_item_compromise,\n  author    = {Eckerly, Carol},\n  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},\n  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},\n  publisher = {Routledge},\n  year      = {2017},\n  url       = {https://www.routledge.com/9781138821811}\n}\n\n@article{ercikan_2008_dif_cancellation,\n  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},\n  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},\n  journal = {Practical Assessment, Research, and Evaluation},\n  volume  = {14},\n  number  = {3},\n  year    = {2008}\n}\n\n@inproceedings{golchin_2024_time_travel,\n  author    = {Golchin, Shahriar and Surdeanu, Mihai},\n  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.08493}\n}\n\n@inproceedings{guo_2017_calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{habba_2025_growing_pains,\n  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n@book{holland_1993_dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@article{kievit_2013_simpsons_paradox,\n  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},\n  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},\n  journal = {Frontiers in Psychology},\n  volume  = {4},\n  pages   = {513},\n  year    = {2013}\n}\n\n@inproceedings{lalor_2024_irt_nlp,\n  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},\n  title     = {Item Response Theory for Natural Language Processing},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}\n}\n\n@article{li_2024_atlas,\n  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2511.04689}\n}\n\n@article{li_2024_open_llm_leaderboard,\n  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},\n  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.07545},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.07545}\n}\n\n@inproceedings{li_2025_dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{liang_2023_helm,\n  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},\n  title         = {Holistic Evaluation of Language Models},\n  journal       = {Transactions on Machine Learning Research},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2211.09110}\n}\n\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n@article{mislevy_1986_bayes_irt,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{oren_2023_proving_contamination,\n  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title         = {Proving Test Set Contamination in Black Box Language Models},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2310.17623},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2310.17623}\n}\n\n@inproceedings{polo_2024_tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14992}\n}\n\n@book{reckase_2009_mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n@article{sanmartin_2009_irt,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity and Item Response Theory},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{schaeffer_2026_generative_contamination,\n  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},\n  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2601.04301}\n}\n\n@inproceedings{shi_2023_minkprob,\n  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.16789}\n}\n\n@inproceedings{shokri_2017_mia,\n  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},\n  title     = {Membership Inference Attacks Against Machine Learning Models},\n  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1610.05820}\n}\n\n@article{sinharay_2017_preknowledge,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  year    = {2017},\n  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}\n}\n\n@article{sinharay_2025_irt_fit,\n  author  = {Sinharay, Sandip},\n  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {78},\n  pages   = {711--733},\n  year    = {2025}\n}\n\n@inproceedings{sun_2025_emperors_new_clothes,\n  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},\n  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.16402}\n}\n\n@article{talts_2018_sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/1804.06788}\n}\n\n@article{wang_2024_mmlu_pro,\n  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},\n  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.01574},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.01574}\n}\n\n@article{white_2024_livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.19314}\n}\n\n@article{wust_2025_selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n@inproceedings{xu_2025_dcr,\n  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.11405}\n}\n\n@article{yang_2023_rethinking_benchmark,\n  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},\n  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2311.04850},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2311.04850}\n}\n\n@inproceedings{zhang_2024_gsm1k,\n  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n  booktitle = {arXiv preprint},\n  year      = {2024},\n  eprint    = {2405.00332},\n  url       = {https://arxiv.org/abs/2405.00332}\n}\n\n@inproceedings{zhang_2024_minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n@inproceedings{zheng_2023_chatbot_arena,\n  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{zhou_2025_psnirt,\n  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2505.15055}\n}\n\n% ============================================================\n% Existing Entries (preserved for backward compatibility)\n% ============================================================\n\n% --- Core Methodology ---\n\n@book{lord1980,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ}\n}\n\n@article{eckerly2017,\n  author  = {Eckerly, Carol},\n  title   = {Detecting Item Compromise in the Context of Item Response Theory},\n  journal = {Applied Psychological Measurement},\n  volume  = {41},\n  number  = {2},\n  pages   = {87--101},\n  year    = {2017}\n}\n\n@article{sinharay2017,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  pages   = {46--68},\n  year    = {2017}\n}\n\n@book{deboeck2004,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York}\n}\n\n@article{adams1997,\n  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  journal = {Applied Psychological Measurement},\n  volume  = {21},\n  number  = {1},\n  pages   = {1--23},\n  year    = {1997}\n}\n\n@article{mislevy1986,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{sanmartin2009,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{maris2009,\n  author  = {Maris, Gunter and Bechger, Timo},\n  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},\n  journal = {Measurement},\n  volume  = {7},\n  number  = {2},\n  pages   = {75--88},\n  year    = {2009}\n}\n\n@inproceedings{cormack2009,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM}\n}\n\n% --- Bayesian Inference & Diagnostics ---\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n@article{talts2018sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv}\n}\n\n@article{ulitzsch2022,\n  author  = {Ulitzsch, Esther and Nestler, Steffen},\n  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {75},\n  number  = {3},\n  pages   = {421--447},\n  year    = {2022}\n}\n\n% --- Contamination Detection Methods ---\n\n@inproceedings{duan2025minkpp,\n  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},\n  title     = {{Min-K\\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025}\n}\n\n@inproceedings{dekoninck2024constat,\n  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@article{wust2025selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{xu2025kds,\n  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2502.00678}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% --- Contamination Analysis & Mitigation ---\n\n@inproceedings{xu2025emperor,\n  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@article{dong2026dose,\n  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},\n  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv}\n}\n\n@article{yang2026rl,\n  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},\n  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@article{wang2025fragility,\n  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},\n  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.02386},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% --- IRT for LLM Evaluation ---\n\n@inproceedings{gu2026psnirt,\n  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026}\n}\n\n@article{polo2026growing,\n  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv}\n}\n\n@article{lyu2025atlas,\n  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},\n  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv}\n}\n\n@article{zhuang2025hibayes,\n  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{lalor2024irt,\n  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},\n  title     = {Benchmarking Large Language Models with Item Response Theory},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  year      = {2024}\n}\n\n% --- Score Adjustment & Decontamination ---\n\n@inproceedings{li2025dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n@article{rao2026silicon,\n  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},\n  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2603.21636},\n  archiveprefix = {arXiv}\n}\n\n% --- Benchmarking ---\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chen2021humaneval,\n  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  title         = {Evaluating Large Language Models Trained on Code},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2107.03374},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024}\n}\n\n@inproceedings{han2026probing,\n  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},\n  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},\n  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},\n  year      = {2026},\n  note      = {arXiv:2510.07175}\n}\n\n% --- Differential Item Functioning (DIF) ---\n\n@book{holland1993dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% --- ML Calibration ---\n\n@inproceedings{guo2017calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017}\n}\n\n% --- Conformal Prediction ---\n\n@article{angelopoulos2023conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {Conformal Prediction: A Gentle Introduction},\n  journal       = {Foundations and Trends in Machine Learning},\n  volume        = {16},\n  number        = {4},\n  pages         = {494--591},\n  year          = {2023}\n}\n\n% --- Data Attribution ---\n\n@inproceedings{pruthi2020tracin,\n  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},\n  title     = {Estimating Training Data Influence by Tracing Gradient Descent},\n  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},\n  year      = {2020}\n}\n\n@inproceedings{park2023trak,\n  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},\n  title     = {{TRAK}: Attributing Model Behavior at Scale},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year      = {2023}\n}\n\n% --- Multidimensional IRT ---\n\n@book{reckase2009mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n% --- Exposure-Ability Collinearity & IRT Identifiability ---\n\n@article{sanmartin2015,\n  author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},\n  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},\n  journal = {Psychometrika},\n  volume  = {80},\n  number  = {2},\n  pages   = {450--467},\n  year    = {2015},\n  doi     = {10.1007/s11336-014-9404-2}\n}\n\n@article{mislevy1987,\n  author  = {Mislevy, Robert J.},\n  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},\n  journal = {Applied Psychological Measurement},\n  volume  = {11},\n  number  = {1},\n  pages   = {81--91},\n  year    = {1987},\n  doi     = {10.1177/014662168701100106}\n}\n\n@book{wainer2007testlet,\n  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},\n  title     = {Testlet Response Theory and Its Applications},\n  publisher = {Cambridge University Press},\n  year      = {2007}\n}\n\n% --- Measurement Error & Attenuation Bias ---\n\n@book{carroll2006,\n  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},\n  edition   = {2nd},\n  publisher = {Chapman \\& Hall/CRC},\n  year      = {2006},\n  isbn      = {9781584886334}\n}\n\n@book{fuller1987,\n  author    = {Fuller, Wayne A.},\n  title     = {Measurement Error Models},\n  publisher = {Wiley},\n  year      = {1987},\n  series    = {Wiley Series in Probability and Statistics},\n  isbn      = {9780471861874}\n}\n\n@article{stefanski1985,\n  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},\n  title   = {Covariate Measurement Error in Logistic Regression},\n  journal = {Annals of Statistics},\n  volume  = {13},\n  number  = {4},\n  pages   = {1335--1351},\n  year    = {1985},\n  doi     = {10.1214/aos/1176349741}\n}\n\n@article{battauz2011,\n  author  = {Battauz, Michela and Bellio, Ruggero},\n  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},\n  journal = {Psychometrika},\n  volume  = {76},\n  number  = {1},\n  pages   = {40--56},\n  year    = {2011},\n  doi     = {10.1007/s11336-010-9195-z}\n}\n\n@article{westfall2016,\n  author  = {Westfall, Jacob and Yarkoni, Tal},\n  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},\n  journal = {PLoS ONE},\n  volume  = {11},\n  number  = {3},\n  pages   = {e0152719},\n  year    = {2016},\n  doi     = {10.1371/journal.pone.0152719}\n}\n\n@article{jerzak2026,\n  author  = {Jerzak, Connor T. and Jessee, Stephen A.},\n  title   = {Attenuation Bias with Latent Predictors},\n  journal = {arXiv preprint arXiv:2507.22218},\n  year    = {2026}\n}\n\n% --- IRT Information & Power Analysis ---\n\n@book{embretson2000,\n  author    = {Embretson, Susan E. and Reise, Steven P.},\n  title     = {Item Response Theory for Psychologists},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2000},\n  address   = {Mahwah, NJ}\n}\n\n@book{thissen2001,\n  author    = {Thissen, David and Wainer, Howard},\n  title     = {Test Scoring},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2001},\n  address   = {Mahwah, NJ}\n}\n\n% --- 4PL Model & Identifiability ---\n\n@article{barton1981,\n  author  = {Barton, Mark A. and Lord, Frederic M.},\n  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  journal = {ETS Research Report Series},\n  volume  = {1981},\n  number  = {1},\n  pages   = {i--8},\n  year    = {1981},\n  doi     = {10.1002/j.2333-8504.1981.tb01255.x}\n}\n\n@article{culpepper2016,\n  author  = {Culpepper, Steven Andrew},\n  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},\n  journal = {Psychometrika},\n  volume  = {81},\n  number  = {4},\n  pages   = {1142--1163},\n  year    = {2016},\n  doi     = {10.1007/s11336-015-9477-6}\n}\n\n@article{liao2012,\n  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},\n  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},\n  journal = {Social Behavior and Personality},\n  volume  = {40},\n  number  = {10},\n  pages   = {1679--1694},\n  year    = {2012},\n  doi     = {10.2224/sbp.2012.40.10.1679}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "2452716d-70bb-4967-88ea-fd974b0bf6cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H94u4HWT8x2FsxwaW4UJLd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9264,
      "cache_read_input_tokens": 39447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9264
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

_source line 16 · 2026-05-17T03:55:26.254Z_

<details><summary>↩ Tool result · `toolu_012M2RFvi3PxVwGHCu9coCyK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "10bb975e-aaa2-4d62-bb7c-3e19a8f3ad14",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft/references.bib",
    "content": "% ============================================================\n% Literature Map Entries (keys from literature_map.yaml ids)\n% ============================================================\n\n@inproceedings{adams_1997_mrcml,\n  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  booktitle = {Applied Psychological Measurement},\n  volume    = {21},\n  number    = {1},\n  pages     = {1--23},\n  year      = {1997}\n}\n\n@article{angelopoulos_2023_conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n  journal       = {Foundations and Trends in Machine Learning},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2107.07511}\n}\n\n@article{brown_2024_ppp,\n  author  = {Brown, Jeremy M. and Thomson, Robert C.},\n  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},\n  journal = {Molecular Biology and Evolution},\n  volume  = {41},\n  number  = {3},\n  pages   = {msae051},\n  year    = {2024}\n}\n\n@article{burnell_2023_structure,\n  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\\'{a}ndez-Orallo, Jos\\'{e}},\n  title         = {Revealing the Structure of Language Model Capabilities},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2306.10062},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2306.10062}\n}\n\n@inproceedings{carlini_2021_extracting,\n  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},\n  title     = {Extracting Training Data from Large Language Models},\n  booktitle = {Proceedings of the 30th USENIX Security Symposium},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2012.07805}\n}\n\n@inproceedings{chiang_2024_chatbot_arena,\n  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{choi_2025_kds,\n  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},\n  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.00678}\n}\n\n@inproceedings{cormack_2009_rrf,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM},\n  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}\n}\n\n@book{deboeck_2004_explanatory_irt,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York},\n  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}\n}\n\n@article{dekoninck_2024_constat,\n  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2405.16281},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2405.16281}\n}\n\n@inproceedings{deng_2024_tsguessing,\n  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},\n  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09783}\n}\n\n@inproceedings{dong_2024_cdd,\n  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},\n  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.15938}\n}\n\n@incollection{eckerly_2017_item_compromise,\n  author    = {Eckerly, Carol},\n  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},\n  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},\n  publisher = {Routledge},\n  year      = {2017},\n  url       = {https://www.routledge.com/9781138821811}\n}\n\n@article{ercikan_2008_dif_cancellation,\n  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},\n  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},\n  journal = {Practical Assessment, Research, and Evaluation},\n  volume  = {14},\n  number  = {3},\n  year    = {2008}\n}\n\n@inproceedings{golchin_2024_time_travel,\n  author    = {Golchin, Shahriar and Surdeanu, Mihai},\n  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.08493}\n}\n\n@inproceedings{guo_2017_calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{habba_2025_growing_pains,\n  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n@book{holland_1993_dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@article{kievit_2013_simpsons_paradox,\n  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},\n  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},\n  journal = {Frontiers in Psychology},\n  volume  = {4},\n  pages   = {513},\n  year    = {2013}\n}\n\n@inproceedings{lalor_2024_irt_nlp,\n  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},\n  title     = {Item Response Theory for Natural Language Processing},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}\n}\n\n@article{li_2024_atlas,\n  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2511.04689}\n}\n\n@article{li_2024_open_llm_leaderboard,\n  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},\n  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.07545},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.07545}\n}\n\n@inproceedings{li_2025_dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{liang_2023_helm,\n  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},\n  title         = {Holistic Evaluation of Language Models},\n  journal       = {Transactions on Machine Learning Research},\n  year          = {2023},\n  url           = {https://arxiv.org/abs/2211.09110}\n}\n\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n@article{mislevy_1986_bayes_irt,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{oren_2023_proving_contamination,\n  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title         = {Proving Test Set Contamination in Black Box Language Models},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2310.17623},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2310.17623}\n}\n\n@inproceedings{polo_2024_tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14992}\n}\n\n@book{reckase_2009_mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n@article{sanmartin_2009_irt,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity and Item Response Theory},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{schaeffer_2026_generative_contamination,\n  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},\n  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2601.04301}\n}\n\n@inproceedings{shi_2023_minkprob,\n  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.16789}\n}\n\n@inproceedings{shokri_2017_mia,\n  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},\n  title     = {Membership Inference Attacks Against Machine Learning Models},\n  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1610.05820}\n}\n\n@article{sinharay_2017_preknowledge,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  year    = {2017},\n  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}\n}\n\n@article{sinharay_2025_irt_fit,\n  author  = {Sinharay, Sandip},\n  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {78},\n  pages   = {711--733},\n  year    = {2025}\n}\n\n@inproceedings{sun_2025_emperors_new_clothes,\n  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},\n  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.16402}\n}\n\n@article{talts_2018_sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/1804.06788}\n}\n\n@article{wang_2024_mmlu_pro,\n  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},\n  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.01574},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.01574}\n}\n\n@article{white_2024_livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2406.19314}\n}\n\n@article{wust_2025_selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n@inproceedings{xu_2025_dcr,\n  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.11405}\n}\n\n@article{yang_2023_rethinking_benchmark,\n  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},\n  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},\n  journal       = {arXiv preprint},\n  year          = {2023},\n  eprint        = {2311.04850},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2311.04850}\n}\n\n@inproceedings{zhang_2024_gsm1k,\n  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n  booktitle = {arXiv preprint},\n  year      = {2024},\n  eprint    = {2405.00332},\n  url       = {https://arxiv.org/abs/2405.00332}\n}\n\n@inproceedings{zhang_2024_minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n@inproceedings{zheng_2023_chatbot_arena,\n  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{zhou_2025_psnirt,\n  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2505.15055}\n}\n\n% ============================================================\n% Existing Entries (preserved for backward compatibility)\n% ============================================================\n\n% --- Core Methodology ---\n\n@book{lord1980,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ}\n}\n\n@article{eckerly2017,\n  author  = {Eckerly, Carol},\n  title   = {Detecting Item Compromise in the Context of Item Response Theory},\n  journal = {Applied Psychological Measurement},\n  volume  = {41},\n  number  = {2},\n  pages   = {87--101},\n  year    = {2017}\n}\n\n@article{sinharay2017,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  pages   = {46--68},\n  year    = {2017}\n}\n\n@book{deboeck2004,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York}\n}\n\n@article{adams1997,\n  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  journal = {Applied Psychological Measurement},\n  volume  = {21},\n  number  = {1},\n  pages   = {1--23},\n  year    = {1997}\n}\n\n@article{mislevy1986,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{sanmartin2009,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{maris2009,\n  author  = {Maris, Gunter and Bechger, Timo},\n  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},\n  journal = {Measurement},\n  volume  = {7},\n  number  = {2},\n  pages   = {75--88},\n  year    = {2009}\n}\n\n@inproceedings{cormack2009,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM}\n}\n\n% --- Bayesian Inference & Diagnostics ---\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n@article{talts2018sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv}\n}\n\n@article{ulitzsch2022,\n  author  = {Ulitzsch, Esther and Nestler, Steffen},\n  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {75},\n  number  = {3},\n  pages   = {421--447},\n  year    = {2022}\n}\n\n% --- Contamination Detection Methods ---\n\n@inproceedings{duan2025minkpp,\n  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},\n  title     = {{Min-K\\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025}\n}\n\n@inproceedings{dekoninck2024constat,\n  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@article{wust2025selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{xu2025kds,\n  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2502.00678}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% --- Contamination Analysis & Mitigation ---\n\n@inproceedings{xu2025emperor,\n  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@article{dong2026dose,\n  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},\n  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv}\n}\n\n@article{yang2026rl,\n  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},\n  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@article{wang2025fragility,\n  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},\n  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.02386},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% --- IRT for LLM Evaluation ---\n\n@inproceedings{gu2026psnirt,\n  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026}\n}\n\n@article{polo2026growing,\n  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv}\n}\n\n@article{lyu2025atlas,\n  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},\n  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv}\n}\n\n@article{zhuang2025hibayes,\n  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{lalor2024irt,\n  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},\n  title     = {Benchmarking Large Language Models with Item Response Theory},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  year      = {2024}\n}\n\n% --- Score Adjustment & Decontamination ---\n\n@inproceedings{li2025dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n@article{rao2026silicon,\n  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},\n  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2603.21636},\n  archiveprefix = {arXiv}\n}\n\n% --- Benchmarking ---\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chen2021humaneval,\n  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  title         = {Evaluating Large Language Models Trained on Code},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2107.03374},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024}\n}\n\n@inproceedings{han2026probing,\n  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},\n  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},\n  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},\n  year      = {2026},\n  note      = {arXiv:2510.07175}\n}\n\n% --- Differential Item Functioning (DIF) ---\n\n@book{holland1993dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% --- ML Calibration ---\n\n@inproceedings{guo2017calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017}\n}\n\n% --- Conformal Prediction ---\n\n@article{angelopoulos2023conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {Conformal Prediction: A Gentle Introduction},\n  journal       = {Foundations and Trends in Machine Learning},\n  volume        = {16},\n  number        = {4},\n  pages         = {494--591},\n  year          = {2023}\n}\n\n% --- Data Attribution ---\n\n@inproceedings{pruthi2020tracin,\n  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},\n  title     = {Estimating Training Data Influence by Tracing Gradient Descent},\n  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},\n  year      = {2020}\n}\n\n@inproceedings{park2023trak,\n  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},\n  title     = {{TRAK}: Attributing Model Behavior at Scale},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year      = {2023}\n}\n\n% --- Multidimensional IRT ---\n\n@book{reckase2009mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n% --- Exposure-Ability Collinearity & IRT Identifiability ---\n\n@article{sanmartin2015,\n  author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},\n  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},\n  journal = {Psychometrika},\n  volume  = {80},\n  number  = {2},\n  pages   = {450--467},\n  year    = {2015},\n  doi     = {10.1007/s11336-014-9404-2}\n}\n\n@article{mislevy1987,\n  author  = {Mislevy, Robert J.},\n  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},\n  journal = {Applied Psychological Measurement},\n  volume  = {11},\n  number  = {1},\n  pages   = {81--91},\n  year    = {1987},\n  doi     = {10.1177/014662168701100106}\n}\n\n@book{wainer2007testlet,\n  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},\n  title     = {Testlet Response Theory and Its Applications},\n  publisher = {Cambridge University Press},\n  year      = {2007}\n}\n\n% --- Measurement Error & Attenuation Bias ---\n\n@book{carroll2006,\n  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},\n  edition   = {2nd},\n  publisher = {Chapman \\& Hall/CRC},\n  year      = {2006},\n  isbn      = {9781584886334}\n}\n\n@book{fuller1987,\n  author    = {Fuller, Wayne A.},\n  title     = {Measurement Error Models},\n  publisher = {Wiley},\n  year      = {1987},\n  series    = {Wiley Series in Probability and Statistics},\n  isbn      = {9780471861874}\n}\n\n@article{stefanski1985,\n  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},\n  title   = {Covariate Measurement Error in Logistic Regression},\n  journal = {Annals of Statistics},\n  volume  = {13},\n  number  = {4},\n  pages   = {1335--1351},\n  year    = {1985},\n  doi     = {10.1214/aos/1176349741}\n}\n\n@article{battauz2011,\n  author  = {Battauz, Michela and Bellio, Ruggero},\n  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},\n  journal = {Psychometrika},\n  volume  = {76},\n  number  = {1},\n  pages   = {40--56},\n  year    = {2011},\n  doi     = {10.1007/s11336-010-9195-z}\n}\n\n@article{westfall2016,\n  author  = {Westfall, Jacob and Yarkoni, Tal},\n  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},\n  journal = {PLoS ONE},\n  volume  = {11},\n  number  = {3},\n  pages   = {e0152719},\n  year    = {2016},\n  doi     = {10.1371/journal.pone.0152719}\n}\n\n@article{jerzak2026,\n  author  = {Jerzak, Connor T. and Jessee, Stephen A.},\n  title   = {Attenuation Bias with Latent Predictors},\n  journal = {arXiv preprint arXiv:2507.22218},\n  year    = {2026}\n}\n\n% --- IRT Information & Power Analysis ---\n\n@book{embretson2000,\n  author    = {Embretson, Susan E. and Reise, Steven P.},\n  title     = {Item Response Theory for Psychologists},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2000},\n  address   = {Mahwah, NJ}\n}\n\n@book{thissen2001,\n  author    = {Thissen, David and Wainer, Howard},\n  title     = {Test Scoring},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2001},\n  address   = {Mahwah, NJ}\n}\n\n% --- 4PL Model & Identifiability ---\n\n@article{barton1981,\n  author  = {Barton, Mark A. and Lord, Frederic M.},\n  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  journal = {ETS Research Report Series},\n  volume  = {1981},\n  number  = {1},\n  pages   = {i--8},\n  year    = {1981},\n  doi     = {10.1002/j.2333-8504.1981.tb01255.x}\n}\n\n@article{culpepper2016,\n  author  = {Culpepper, Steven Andrew},\n  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},\n  journal = {Psychometrika},\n  volume  = {81},\n  number  = {4},\n  pages   = {1142--1163},\n  year    = {2016},\n  doi     = {10.1007/s11336-015-9477-6}\n}\n\n@article{liao2012,\n  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},\n  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},\n  journal = {Social Behavior and Personality},\n  volume  = {40},\n  number  = {10},\n  pages   = {1679--1694},\n  year    = {2012},\n  doi     = {10.2224/sbp.2012.40.10.1679}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 425,
        "lines": [
          " % ============================================================",
          "-% Core Methodology — Educational Measurement & IRT",
          "+% Literature Map Entries (keys from literature_map.yaml ids)",
          " % ============================================================",
          " ",
          "+@inproceedings{adams_1997_mrcml,",
          "+  author    = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},",
          "+  title     = {The Multidimensional Random Coefficients Multinomial Logit Model},",
          "+  booktitle = {Applied Psychological Measurement},",
          "+  volume    = {21},",
          "+  number    = {1},",
          "+  pages     = {1--23},",
          "+  year      = {1997}",
          "+}",
          "+",
          "+@article{angelopoulos_2023_conformal,",
          "+  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},",
          "+  title         = {A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},",
          "+  journal       = {Foundations and Trends in Machine Learning},",
          "+  year          = {2023},",
          "+  url           = {https://arxiv.org/abs/2107.07511}",
          "+}",
          "+",
          "+@article{brown_2024_ppp,",
          "+  author  = {Brown, Jeremy M. and Thomson, Robert C.},",
          "+  title   = {The Expected Behaviors of Posterior Predictive Tests and Their Unexpected Interpretation},",
          "+  journal = {Molecular Biology and Evolution},",
          "+  volume  = {41},",
          "+  number  = {3},",
          "+  pages   = {msae051},",
          "+  year    = {2024}",
          "+}",
          "+",
          "+@article{burnell_2023_structure,",
          "+  author        = {Burnell, Ryan and Schellaert, Wout and Burden, John and Ullman, Tomer D. and Martinez-Plumed, Fernando and Tenenbaum, Joshua B. and Rutar, Danaja and Murfet, Daniel and Zheng, Hananel and Hern\\'{a}ndez-Orallo, Jos\\'{e}},",
          "+  title         = {Revealing the Structure of Language Model Capabilities},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2023},",
          "+  eprint        = {2306.10062},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2306.10062}",
          "+}",
          "+",
          "+@inproceedings{carlini_2021_extracting,",
          "+  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},",
          "+  title     = {Extracting Training Data from Large Language Models},",
          "+  booktitle = {Proceedings of the 30th USENIX Security Symposium},",
          "+  year      = {2021},",
          "+  url       = {https://arxiv.org/abs/2012.07805}",
          "+}",
          "+",
          "+@inproceedings{chiang_2024_chatbot_arena,",
          "+  author    = {Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios N. and Li, Tianle and Li, Dacheng and Zhang, Hao and Zhu, Banghua and Jordan, Michael and Gonzalez, Joseph E. and Stoica, Ion},",
          "+  title     = {Chatbot Arena: An Open Platform for Evaluating {LLMs} by Human Preference},",
          "+  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2403.04132}",
          "+}",
          "+",
          "+@inproceedings{choi_2025_kds,",
          "+  author    = {Choi, Yujin and Kim, Heeyoung and Lee, Jihoon and Park, Changho},",
          "+  title     = {How Contaminated Is Your Benchmark? Quantifying Dataset Leakage in Large Language Models with Kernel Divergence},",
          "+  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},",
          "+  year      = {2025},",
          "+  url       = {https://arxiv.org/abs/2502.00678}",
          "+}",
          "+",
          "+@inproceedings{cormack_2009_rrf,",
          "+  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},",
          "+  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},",
          "+  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},",
          "+  pages     = {758--759},",
          "+  year      = {2009},",
          "+  publisher = {ACM},",
          "+  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}",
          "+}",
          "+",
          "+@book{deboeck_2004_explanatory_irt,",
          "+  author    = {De Boeck, Paul and Wilson, Mark},",
          "+  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},",
          "+  publisher = {Springer},",
          "+  year      = {2004},",
          "+  address   = {New York},",
          "+  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}",
          "+}",
          "+",
          "+@article{dekoninck_2024_constat,",
          "+  author        = {Dekoninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},",
          "+  title         = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2024},",
          "+  eprint        = {2405.16281},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2405.16281}",
          "+}",
          "+",
          "+@inproceedings{deng_2024_tsguessing,",
          "+  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},",
          "+  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},",
          "+  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2311.09783}",
          "+}",
          "+",
          "+@inproceedings{dong_2024_cdd,",
          "+  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Li, Ge},",
          "+  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},",
          "+  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2402.15938}",
          "+}",
          "+",
          "+@incollection{eckerly_2017_item_compromise,",
          "+  author    = {Eckerly, Carol},",
          "+  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},",
          "+  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},",
          "+  publisher = {Routledge},",
          "+  year      = {2017},",
          "+  url       = {https://www.routledge.com/9781138821811}",
          "+}",
          "+",
          "+@article{ercikan_2008_dif_cancellation,",
          "+  author  = {Ercikan, Kadriye and Arim, Rodrigo G. and Oliveri, Maria Elena},",
          "+  title   = {Differential Item Functioning Amplification and Cancellation in a Reading Test},",
          "+  journal = {Practical Assessment, Research, and Evaluation},",
          "+  volume  = {14},",
          "+  number  = {3},",
          "+  year    = {2008}",
          "+}",
          "+",
          "+@inproceedings{golchin_2024_time_travel,",
          "+  author    = {Golchin, Shahriar and Surdeanu, Mihai},",
          "+  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},",
          "+  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2308.08493}",
          "+}",
          "+",
          "+@inproceedings{guo_2017_calibration,",
          "+  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},",
          "+  title     = {On Calibration of Modern Neural Networks},",
          "+  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},",
          "+  pages     = {1321--1330},",
          "+  year      = {2017},",
          "+  url       = {https://arxiv.org/abs/1706.04599}",
          "+}",
          "+",
          "+@article{habba_2025_growing_pains,",
          "+  author        = {Habba, Maryam and Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},",
          "+  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2025},",
          "+  eprint        = {2604.12843},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2604.12843}",
          "+}",
          "+",
          "+@book{holland_1993_dif,",
          "+  author    = {Holland, Paul W. and Wainer, Howard},",
          "+  title     = {Differential Item Functioning},",
          "+  publisher = {Lawrence Erlbaum Associates},",
          "+  year      = {1993},",
          "+  address   = {Hillsdale, NJ}",
          "+}",
          "+",
          "+@article{kievit_2013_simpsons_paradox,",
          "+  author  = {Kievit, Rogier A. and Frankenhuis, Willem E. and Waldorp, Lourens J. and Borsboom, Denny},",
          "+  title   = {Simpson's Paradox in Psychological Science: A Practical Guide},",
          "+  journal = {Frontiers in Psychology},",
          "+  volume  = {4},",
          "+  pages   = {513},",
          "+  year    = {2013}",
          "+}",
          "+",
          "+@inproceedings{lalor_2024_irt_nlp,",
          "+  author    = {Lalor, John P. and Yang, Yi and Rodriguez, Pedro and Smith, Noah A.},",
          "+  title     = {Item Response Theory for Natural Language Processing},",
          "+  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},",
          "+  year      = {2024},",
          "+  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}",
          "+}",
          "+",
          "+@article{li_2024_atlas,",
          "+  author        = {Li, Guanzhong and Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},",
          "+  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2024},",
          "+  eprint        = {2511.04689},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2511.04689}",
          "+}",
          "+",
          "+@article{li_2024_open_llm_leaderboard,",
          "+  author        = {Li, Aidar Myrzakhan and Shen, Sondos Mahmoud Bsharat and Jia, Zhiqiang},",
          "+  title         = {Open-{LLM}-Leaderboard: From Multi-choice to Open-style Questions for {LLMs} Evaluation, Benchmark, and Arena},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2024},",
          "+  eprint        = {2406.07545},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2406.07545}",
          "+}",
          "+",
          "+@inproceedings{li_2025_dcr,",
          "+  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},",
          "+  title     = {Decontaminated Calibration and Ranking for Trustworthy {LLM} Evaluation},",
          "+  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},",
          "+  year      = {2025}",
          "+}",
          "+",
          "+@article{liang_2023_helm,",
          "+  author        = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and others},",
          "+  title         = {Holistic Evaluation of Language Models},",
          "+  journal       = {Transactions on Machine Learning Research},",
          "+  year          = {2023},",
          "+  url           = {https://arxiv.org/abs/2211.09110}",
          "+}",
          "+",
          "+@article{luettgau_2025_hibayes,",
          "+  author        = {Luettgau, Lennart and Polo, Felipe Maia and Zhuang, Yuekai and Yurochkin, Mikhail and Sun, Yuekai},",
          "+  title         = {{HiBayES}: A Hierarchical Bayesian Modeling Framework for {AI} Evaluation Statistics},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2025},",
          "+  eprint        = {2505.05602},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2505.05602}",
          "+}",
          "+",
          "+@article{mislevy_1986_bayes_irt,",
          "+  author  = {Mislevy, Robert J.},",
          "+  title   = {Bayes Modal Estimation in Item Response Models},",
          "+  journal = {Psychometrika},",
          "+  volume  = {51},",
          "+  number  = {2},",
          "+  pages   = {177--195},",
          "+  year    = {1986}",
          "+}",
          "+",
          "+@article{oren_2023_proving_contamination,",
          "+  author        = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},",
          "+  title         = {Proving Test Set Contamination in Black Box Language Models},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2023},",
          "+  eprint        = {2310.17623},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2310.17623}",
          "+}",
          "+",
          "+@inproceedings{polo_2024_tinybenchmarks,",
          "+  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},",
          "+  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},",
          "+  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2402.14992}",
          "+}",
          "+",
          "+@book{reckase_2009_mirt,",
          "+  author    = {Reckase, Mark D.},",
          "+  title     = {Multidimensional Item Response Theory},",
          "+  publisher = {Springer},",
          "+  year      = {2009},",
          "+  address   = {New York}",
          "+}",
          "+",
          "+@article{sanmartin_2009_irt,",
          "+  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},",
          "+  title   = {Consequential Validity and Item Response Theory},",
          "+  journal = {Psychometrika},",
          "+  volume  = {74},",
          "+  number  = {2},",
          "+  pages   = {349--367},",
          "+  year    = {2009}",
          "+}",
          "+",
          "+@article{schaeffer_2026_generative_contamination,",
          "+  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Ali and Liu, Hailey and others},",
          "+  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2026},",
          "+  eprint        = {2601.04301},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2601.04301}",
          "+}",
          "+",
          "+@inproceedings{shi_2023_minkprob,",
          "+  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},",
          "+  title     = {Detecting Pretraining Data from Large Language Models},",
          "+  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},",
          "+  year      = {2024},",
          "+  url       = {https://arxiv.org/abs/2310.16789}",
          "+}",
          "+",
          "+@inproceedings{shokri_2017_mia,",
          "+  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},",
          "+  title     = {Membership Inference Attacks Against Machine Learning Models},",
          "+  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},",
          "+  year      = {2017},",
          "+  url       = {https://arxiv.org/abs/1610.05820}",
          "+}",
          "+",
          "+@article{sinharay_2017_preknowledge,",
          "+  author  = {Sinharay, Sandip},",
          "+  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},",
          "+  journal = {Journal of Educational and Behavioral Statistics},",
          "+  volume  = {42},",
          "+  number  = {1},",
          "+  year    = {2017},",
          "+  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}",
          "+}",
          "+",
          "+@article{sinharay_2025_irt_fit,",
          "+  author  = {Sinharay, Sandip},",
          "+  title   = {Assessment of Fit of Item Response Theory Models: A Critical Review of the Status Quo and Some Future Directions},",
          "+  journal = {British Journal of Mathematical and Statistical Psychology},",
          "+  volume  = {78},",
          "+  pages   = {711--733},",
          "+  year    = {2025}",
          "+}",
          "+",
          "+@inproceedings{sun_2025_emperors_new_clothes,",
          "+  author    = {Sun, Yifan and Li, Zhen and Zhang, Yingji and Chen, Fei},",
          "+  title     = {The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for {LLM} Benchmark Data Contamination},",
          "+  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},",
          "+  year      = {2025},",
          "+  url       = {https://arxiv.org/abs/2503.16402}",
          "+}",
          "+",
          "+@article{talts_2018_sbc,",
          "+  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},",
          "+  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2018},",
          "+  eprint        = {1804.06788},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/1804.06788}",
          "+}",
          "+",
          "+@article{wang_2024_mmlu_pro,",
          "+  author        = {Wang, Yubo and Ma, Xueguang and Zhang, Ge and Ni, Yuansheng and Chandra, Abhranil and Guo, Shiguang and Ren, Weiming and Arulraj, Aaran and He, Xuan and Jiang, Ziyan and Li, Tianle and Ku, Max and Wang, Kai and Zhuang, Alex and Fan, Rongqi and Huang, Xiang and Chen, Wenhu},",
          "+  title         = {{MMLU-Pro}: A More Robust and Challenging Multi-Task Language Understanding Benchmark},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2024},",
          "+  eprint        = {2406.01574},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2406.01574}",
          "+}",
          "+",
          "+@article{white_2024_livebench,",
          "+  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},",
          "+  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2024},",
          "+  eprint        = {2406.19314},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2406.19314}",
          "+}",
          "+",
          "+@article{wust_2025_selfcritique,",
          "+  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},",
          "+  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2025},",
          "+  eprint        = {2510.09259},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2510.09259}",
          "+}",
          "+",
          "+@inproceedings{xu_2025_dcr,",
          "+  author    = {Xu, Yiyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},",
          "+  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},",
          "+  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},",
          "+  year      = {2025},",
          "+  url       = {https://arxiv.org/abs/2507.11405}",
          "+}",
          "+",
          "+@article{yang_2023_rethinking_benchmark,",
          "+  author        = {Yang, Shuo and Wei, Xin and Shi, Weicheng and Xu, Feiyu},",
          "+  title         = {Rethinking Benchmark and Contamination for Language Models with Rephrased Samples},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2023},",
          "+  eprint        = {2311.04850},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2311.04850}",
          "+}",
          "+",
          "+@inproceedings{zhang_2024_gsm1k,",
          "+  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},",
          "+  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},",
          "+  booktitle = {arXiv preprint},",
          "+  year      = {2024},",
          "+  eprint    = {2405.00332},",
          "+  url       = {https://arxiv.org/abs/2405.00332}",
          "+}",
          "+",
          "+@inproceedings{zhang_2024_minkpp,",
          "+  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},",
          "+  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},",
          "+  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},",
          "+  year      = {2025},",
          "+  url       = {https://arxiv.org/abs/2404.02936}",
          "+}",
          "+",
          "+@inproceedings{zheng_2023_chatbot_arena,",
          "+  author    = {Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},",
          "+  title     = {Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},",
          "+  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},",
          "+  year      = {2023},",
          "+  url       = {https://arxiv.org/abs/2306.05685}",
          "+}",
          "+",
          "+@inproceedings{zhou_2025_psnirt,",
          "+  author    = {Zhou, Guanyu and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},",
          "+  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},",
          "+  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},",
          "+  year      = {2026},",
          "+  url       = {https://arxiv.org/abs/2505.15055}",
          "+}",
          "+",
          "+% ============================================================",
          "+% Existing Entries (preserved for backward compatibility)",
          "+% ============================================================",
          "+",
          "+% --- Core Methodology ---",
          "+",
          " @book{lord1980,",
          "   author    = {Lord, Frederic M.},",
          "   title     = {Applications of Item Response Theory to Practical Testing Problems},"
        ]
      },
      {
        "oldStart": 87,
        "oldLines": 9,
        "newStart": 505,
        "newLines": 7,
        "lines": [
          "   publisher = {ACM}",
          " }",
          " ",
          "-% ============================================================",
          "-% Bayesian Inference & Diagnostics",
          "-% ============================================================",
          "+% --- Bayesian Inference & Diagnostics ---",
          " ",
          " @article{hoffman2014,",
          "   author  = {Hoffman, Matthew D. and Gelman, Andrew},"
        ]
      },
      {
        "oldStart": 130,
        "oldLines": 9,
        "newStart": 546,
        "newLines": 7,
        "lines": [
          "   year    = {2022}",
          " }",
          " ",
          "-% ============================================================",
          "-% Contamination Detection Methods",
          "-% ============================================================",
          "+% --- Contamination Detection Methods ---",
          " ",
          " @inproceedings{duan2025minkpp,",
          "   author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},"
        ]
      },
      {
        "oldStart": 172,
        "oldLines": 9,
        "newStart": 586,
        "newLines": 7,
        "lines": [
          "   year      = {2024}",
          " }",
          " ",
          "-% ============================================================",
          "-% Contamination Analysis & Mitigation",
          "-% ============================================================",
          "+% --- Contamination Analysis & Mitigation ---",
          " ",
          " @inproceedings{xu2025emperor,",
          "   author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},"
        ]
      },
      {
        "oldStart": 218,
        "oldLines": 9,
        "newStart": 630,
        "newLines": 7,
        "lines": [
          "   year      = {2025}",
          " }",
          " ",
          "-% ============================================================",
          "-% IRT for LLM Evaluation",
          "-% ============================================================",
          "+% --- IRT for LLM Evaluation ---",
          " ",
          " @inproceedings{gu2026psnirt,",
          "   author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},"
        ]
      },
      {
        "oldStart": 263,
        "oldLines": 9,
        "newStart": 673,
        "newLines": 7,
        "lines": [
          "   year      = {2024}",
          " }",
          " ",
          "-% ============================================================",
          "-% Score Adjustment & Decontamination",
          "-% ============================================================",
          "+% --- Score Adjustment & Decontamination ---",
          " ",
          " @inproceedings{li2025dcr,",
          "   author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},"
        ]
      },
      {
        "oldStart": 290,
        "oldLines": 9,
        "newStart": 698,
        "newLines": 7,
        "lines": [
          "   archiveprefix = {arXiv}",
          " }",
          " ",
          "-% ============================================================",
          "-% Benchmarking — Surveys & Infrastructure",
          "-% ============================================================",
          "+% --- Benchmarking ---",
          " ",
          " @inproceedings{hendrycks2021mmlu,",
          "   author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},"
        ]
      },
      {
        "oldStart": 359,
        "oldLines": 9,
        "newStart": 765,
        "newLines": 7,
        "lines": [
          "   note      = {arXiv:2510.07175}",
          " }",
          " ",
          "-% ============================================================",
          "-% Differential Item Functioning (DIF)",
          "-% ============================================================",
          "+% --- Differential Item Functioning (DIF) ---",
          " ",
          " @book{holland1993dif,",
          "   author    = {Holland, Paul W. and Wainer, Howard},"
        ]
      },
      {
        "oldStart": 389,
        "oldLines": 9,
        "newStart": 793,
        "newLines": 7,
        "lines": [
          "   address   = {Ottawa, ON}",
          " }",
          " ",
          "-% ============================================================",
          "-% ML Calibration",
          "-% ============================================================",
          "+% --- ML Calibration ---",
          " ",
          " @inproceedings{guo2017calibration,",
          "   author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},"
        ]
      },
      {
        "oldStart": 401,
        "oldLines": 9,
        "newStart": 803,
        "newLines": 7,
        "lines": [
          "   year      = {2017}",
          " }",
          " ",
          "-% ============================================================",
          "-% Conformal Prediction",
          "-% ============================================================",
          "+% --- Conformal Prediction ---",
          " ",
          " @article{angelopoulos2023conformal,",
          "   author        = {Angelopoulos, Anastasios N. and Bates, Stephen},"
        ]
      },
      {
        "oldStart": 415,
        "oldLines": 9,
        "newStart": 815,
        "newLines": 7,
        "lines": [
          "   year          = {2023}",
          " }",
          " ",
          "-% ============================================================",
          "-% Data Attribution",
          "-% ============================================================",
          "+% --- Data Attribution ---",
          " ",
          " @inproceedings{pruthi2020tracin,",
          "   author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},"
        ]
      },
      {
        "oldStart": 433,
        "oldLines": 9,
        "newStart": 831,
        "newLines": 7,
        "lines": [
          "   year      = {2023}",
          " }",
          " ",
          "-% ============================================================",
          "-% Multidimensional IRT",
          "-% ============================================================",
          "+% --- Multidimensional IRT ---",
          " ",
          " @book{reckase2009mirt,",
          "   author    = {Reckase, Mark D.},"
        ]
      },
      {
        "oldStart": 445,
        "oldLines": 9,
        "newStart": 841,
        "newLines": 7,
        "lines": [
          "   address   = {New York}",
          " }",
          " ",
          "-% ============================================================",
          "-% Exposure-Ability Collinearity & IRT Identifiability",
          "-% ============================================================",
          "+% --- Exposure-Ability Collinearity & IRT Identifiability ---",
          " ",
          " @article{sanmartin2015,",
          "   author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},"
        ]
      },
      {
        "oldStart": 478,
        "oldLines": 9,
        "newStart": 872,
        "newLines": 7,
        "lines": [
          "   year      = {2007}",
          " }",
          " ",
          "-% ============================================================",
          "-% Measurement Error & Attenuation Bias",
          "-% ============================================================",
          "+% --- Measurement Error & Attenuation Bias ---",
          " ",
          " @book{carroll2006,",
          "   author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},"
        ]
      },
      {
        "oldStart": 540,
        "oldLines": 9,
        "newStart": 932,
        "newLines": 7,
        "lines": [
          "   year    = {2026}",
          " }",
          " ",
          "-% ============================================================",
          "-% IRT Information & Power Analysis",
          "-% ============================================================",
          "+% --- IRT Information & Power Analysis ---",
          " ",
          " @book{embretson2000,",
          "   author    = {Embretson, Susan E. and Reise, Steven P.},"
        ]
      },
      {
        "oldStart": 560,
        "oldLines": 9,
        "newStart": 950,
        "newLines": 7,
        "lines": [
          "   address   = {Mahwah, NJ}",
          " }",
          " ",
          "-% ============================================================",
          "-% 4PL Model & Identifiability",
          "-% ============================================================",
          "+% --- 4PL Model & Identifiability ---",
          " ",
          " @article{barton1981,",
          "   author  = {Barton, Mark A. and Lord, Frederic M.},"
        ]
      }
    ],
    "originalFile": "% ============================================================\n% Core Methodology — Educational Measurement & IRT\n% ============================================================\n\n@book{lord1980,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ}\n}\n\n@article{eckerly2017,\n  author  = {Eckerly, Carol},\n  title   = {Detecting Item Compromise in the Context of Item Response Theory},\n  journal = {Applied Psychological Measurement},\n  volume  = {41},\n  number  = {2},\n  pages   = {87--101},\n  year    = {2017}\n}\n\n@article{sinharay2017,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  pages   = {46--68},\n  year    = {2017}\n}\n\n@book{deboeck2004,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York}\n}\n\n@article{adams1997,\n  author  = {Adams, Raymond J. and Wilson, Mark and Wang, Wen-chung},\n  title   = {The Multidimensional Random Coefficients Multinomial Logit Model},\n  journal = {Applied Psychological Measurement},\n  volume  = {21},\n  number  = {1},\n  pages   = {1--23},\n  year    = {1997}\n}\n\n@article{mislevy1986,\n  author  = {Mislevy, Robert J.},\n  title   = {Bayes Modal Estimation in Item Response Models},\n  journal = {Psychometrika},\n  volume  = {51},\n  number  = {2},\n  pages   = {177--195},\n  year    = {1986}\n}\n\n@article{sanmartin2009,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity of Item Response Theory Models for Measuring Latent Constructs},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@article{maris2009,\n  author  = {Maris, Gunter and Bechger, Timo},\n  title   = {On Interpreting the Model Parameters for the Three Parameter Logistic Model},\n  journal = {Measurement},\n  volume  = {7},\n  number  = {2},\n  pages   = {75--88},\n  year    = {2009}\n}\n\n@inproceedings{cormack2009,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM}\n}\n\n% ============================================================\n% Bayesian Inference & Diagnostics\n% ============================================================\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n@article{talts2018sbc,\n  author        = {Talts, Sean and Betancourt, Michael and Simpson, Daniel and Vehtari, Aki and Gelman, Andrew},\n  title         = {Validating {Bayesian} Inference Algorithms with Simulation-Based Calibration},\n  journal       = {arXiv preprint},\n  year          = {2018},\n  eprint        = {1804.06788},\n  archiveprefix = {arXiv}\n}\n\n@article{ulitzsch2022,\n  author  = {Ulitzsch, Esther and Nestler, Steffen},\n  title   = {Automatic Differentiation Variational Inference for Item Response Theory Models},\n  journal = {British Journal of Mathematical and Statistical Psychology},\n  volume  = {75},\n  number  = {3},\n  pages   = {421--447},\n  year    = {2022}\n}\n\n% ============================================================\n% Contamination Detection Methods\n% ============================================================\n\n@inproceedings{duan2025minkpp,\n  author    = {Duan, Jiawen and Xie, Cheng and Zhang, Jian and Li, Kai},\n  title     = {{Min-K\\%++}: Improved Membership Inference for Detecting Pre-Training Data of Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025}\n}\n\n@inproceedings{dekoninck2024constat,\n  author    = {De Koninck, Jasper and Nelissen, Koen and Nijssen, Siegfried and Davis, Jesse},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@article{wust2025selfcritique,\n  author        = {W\\\"{u}st, Timon and Hoffmann, Jan and Pang, Richard Yuanzhe},\n  title         = {Self-Critique as a Contamination Signal: Detecting Memorization via Entropy Collapse in Model Self-Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{xu2025kds,\n  author    = {Xu, Yanyang and Qi, Hongzhan and Zhao, Benyou and Liu, Zhiyuan},\n  title     = {Knowledge Distillation Signatures for Efficient Contamination Detection},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2502.00678}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Laesecke, Faisal and Cotterell, Ryan},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% ============================================================\n% Contamination Analysis & Mitigation\n% ============================================================\n\n@inproceedings{xu2025emperor,\n  author    = {Xu, Yiwen and Song, Kaijie and Zhou, Jianfeng and Chen, Liang},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@article{dong2026dose,\n  author        = {Dong, Yifan and Li, Xinran and Chen, Difan and Wang, Zhengyu},\n  title         = {Dose-Response Relationships in Benchmark Contamination: Quantifying Score Inflation Across Model Scales},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv}\n}\n\n@article{yang2026rl,\n  author        = {Yang, Shuo and Wei, Xin and Zhang, Zhiwei and Xu, Feiyu},\n  title         = {Reinforcement Learning Amplifies Contamination in {LLM} Benchmark Evaluation},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@article{wang2025fragility,\n  author        = {Wang, Yuxin and Zhao, Yucheng and Li, Cheng and Zhang, Meng},\n  title         = {On the Fragility of Benchmark Evaluations for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.02386},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% ============================================================\n% IRT for LLM Evaluation\n% ============================================================\n\n@inproceedings{gu2026psnirt,\n  author    = {Gu, Jiaqi and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {{PSN-IRT}: Psychometric-Informed Evaluation of Large Language Models via Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026}\n}\n\n@article{polo2026growing,\n  author        = {Polo, Felipe Maia and Mamani, Ronald and Zhuang, Yuekai and Xu, Hao and Choshen, Leshem and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {Growing Pains: Understanding the Limitations and Potential of {IRT} for {LLM} Evaluation at Scale},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv}\n}\n\n@article{lyu2025atlas,\n  author        = {Lyu, Haoran and Ding, Yufei and Wang, Hainiu and Peng, Nanyun},\n  title         = {{ATLAS}: Adaptive Testing via Latent Ability Scoring for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv}\n}\n\n@article{zhuang2025hibayes,\n  author        = {Zhuang, Yuekai and Polo, Felipe Maia and Yurochkin, Mikhail and Sun, Yuekai},\n  title         = {{HiBayES}: Hierarchical {Bayesian} Evaluation System for Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{lalor2024irt,\n  author    = {Lalor, John P. and Yang, Yi and Smith, Noah A.},\n  title     = {Benchmarking Large Language Models with Item Response Theory},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  year      = {2024}\n}\n\n% ============================================================\n% Score Adjustment & Decontamination\n% ============================================================\n\n@inproceedings{li2025dcr,\n  author    = {Li, Yucheng and Flanigan, Frank and Sherborne, Tom and Sherborne, Charlie},\n  title     = {{DCR}: Decontaminated Calibration and Ranking for Benchmark Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n@article{rao2026silicon,\n  author        = {Rao, Sumedh and Raji, Inioluwa Deborah and Liang, Percy},\n  title         = {The Silicon Bureaucracy: Evaluating the Evaluators in {LLM} Benchmarking},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2603.21636},\n  archiveprefix = {arXiv}\n}\n\n% ============================================================\n% Benchmarking — Surveys & Infrastructure\n% ============================================================\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chen2021humaneval,\n  author        = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and Ray, Alex and Puri, Raul and Krueger, Gretchen and Petrov, Michael and Khlaaf, Heidy and Sastry, Girish and Mishkin, Pamela and Chan, Brooke and Gray, Scott and Ryder, Nick and Pavlov, Mikhail and Power, Alethea and Kaiser, Lukasz and Bavarian, Mohammad and Winter, Clemens and Tillet, Philippe and Such, Felipe Petroski and Cummings, Dave and Plappert, Matthias and Chanez, Fotios and Barnes, Elizabeth and Herbert-Voss, Ariel and Guss, William Hebgen and Nichol, Alex and Paino, Alex and Tezak, Nikolas and Tang, Jie and Babuschkin, Igor and Balaji, Suchir and Jain, Shantanu and Saunders, William and Hesse, Christopher and Carr, Andrew N. and Leike, Jan and Achiam, Josh and Misra, Vedant and Morikawa, Evan and Radford, Alec and Knight, Matthew and Brundage, Miles and Murati, Mira and Mayer, Katie and Welinder, Peter and McGrew, Bob and Amodei, Dario and McCandlish, Sam and Sutskever, Ilya and Zaremba, Wojciech},\n  title         = {Evaluating Large Language Models Trained on Code},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2107.03374},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2025}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{polo2024tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{TinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024}\n}\n\n@inproceedings{han2026probing,\n  author    = {Han, Yucheng and Wu, Chongxuan and Qi, Jiashi and Zhou, Jie},\n  title     = {Targeted Probing for Contamination Effects in Large Language Model Evaluations},\n  booktitle = {Findings of the 2026 Conference of the European Chapter of the Association for Computational Linguistics (EACL Findings)},\n  year      = {2026},\n  note      = {arXiv:2510.07175}\n}\n\n% ============================================================\n% Differential Item Functioning (DIF)\n% ============================================================\n\n@book{holland1993dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% ============================================================\n% ML Calibration\n% ============================================================\n\n@inproceedings{guo2017calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017}\n}\n\n% ============================================================\n% Conformal Prediction\n% ============================================================\n\n@article{angelopoulos2023conformal,\n  author        = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  title         = {Conformal Prediction: A Gentle Introduction},\n  journal       = {Foundations and Trends in Machine Learning},\n  volume        = {16},\n  number        = {4},\n  pages         = {494--591},\n  year          = {2023}\n}\n\n% ============================================================\n% Data Attribution\n% ============================================================\n\n@inproceedings{pruthi2020tracin,\n  author    = {Pruthi, Garima and Liu, Frederick and Kale, Satyen and Sundararajan, Mukund},\n  title     = {Estimating Training Data Influence by Tracing Gradient Descent},\n  booktitle = {Advances in Neural Information Processing Systems 33 (NeurIPS)},\n  year      = {2020}\n}\n\n@inproceedings{park2023trak,\n  author    = {Park, Sung Min and Georgiev, Kristian and Ilyas, Andrew and Lecun, Guillaume and Madry, Aleksander},\n  title     = {{TRAK}: Attributing Model Behavior at Scale},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year      = {2023}\n}\n\n% ============================================================\n% Multidimensional IRT\n% ============================================================\n\n@book{reckase2009mirt,\n  author    = {Reckase, Mark D.},\n  title     = {Multidimensional Item Response Theory},\n  publisher = {Springer},\n  year      = {2009},\n  address   = {New York}\n}\n\n% ============================================================\n% Exposure-Ability Collinearity & IRT Identifiability\n% ============================================================\n\n@article{sanmartin2015,\n  author  = {San Mart\\'{i}n, Ernesto and Gonz\\'{a}lez, Jorge and Tuerlinckx, Francis},\n  title   = {On the Unidentifiability of the Fixed-Effects {3PL} Model},\n  journal = {Psychometrika},\n  volume  = {80},\n  number  = {2},\n  pages   = {450--467},\n  year    = {2015},\n  doi     = {10.1007/s11336-014-9404-2}\n}\n\n@article{mislevy1987,\n  author  = {Mislevy, Robert J.},\n  title   = {Exploiting Auxiliary Information About Examinees in the Estimation of Item Parameters},\n  journal = {Applied Psychological Measurement},\n  volume  = {11},\n  number  = {1},\n  pages   = {81--91},\n  year    = {1987},\n  doi     = {10.1177/014662168701100106}\n}\n\n@book{wainer2007testlet,\n  author    = {Wainer, Howard and Bradlow, Eric T. and Wang, Xiaohui},\n  title     = {Testlet Response Theory and Its Applications},\n  publisher = {Cambridge University Press},\n  year      = {2007}\n}\n\n% ============================================================\n% Measurement Error & Attenuation Bias\n% ============================================================\n\n@book{carroll2006,\n  author    = {Carroll, Raymond J. and Ruppert, David and Stefanski, Leonard A. and Crainiceanu, Ciprian M.},\n  title     = {Measurement Error in Nonlinear Models: A Modern Perspective},\n  edition   = {2nd},\n  publisher = {Chapman \\& Hall/CRC},\n  year      = {2006},\n  isbn      = {9781584886334}\n}\n\n@book{fuller1987,\n  author    = {Fuller, Wayne A.},\n  title     = {Measurement Error Models},\n  publisher = {Wiley},\n  year      = {1987},\n  series    = {Wiley Series in Probability and Statistics},\n  isbn      = {9780471861874}\n}\n\n@article{stefanski1985,\n  author  = {Stefanski, Leonard A. and Carroll, Raymond J.},\n  title   = {Covariate Measurement Error in Logistic Regression},\n  journal = {Annals of Statistics},\n  volume  = {13},\n  number  = {4},\n  pages   = {1335--1351},\n  year    = {1985},\n  doi     = {10.1214/aos/1176349741}\n}\n\n@article{battauz2011,\n  author  = {Battauz, Michela and Bellio, Ruggero},\n  title   = {Structural Modeling of Measurement Error in Generalized Linear Models with {Rasch} Measures as Covariates},\n  journal = {Psychometrika},\n  volume  = {76},\n  number  = {1},\n  pages   = {40--56},\n  year    = {2011},\n  doi     = {10.1007/s11336-010-9195-z}\n}\n\n@article{westfall2016,\n  author  = {Westfall, Jacob and Yarkoni, Tal},\n  title   = {Statistically Controlling for Confounding Constructs Is Harder than You Think},\n  journal = {PLoS ONE},\n  volume  = {11},\n  number  = {3},\n  pages   = {e0152719},\n  year    = {2016},\n  doi     = {10.1371/journal.pone.0152719}\n}\n\n@article{jerzak2026,\n  author  = {Jerzak, Connor T. and Jessee, Stephen A.},\n  title   = {Attenuation Bias with Latent Predictors},\n  journal = {arXiv preprint arXiv:2507.22218},\n  year    = {2026}\n}\n\n% ============================================================\n% IRT Information & Power Analysis\n% ============================================================\n\n@book{embretson2000,\n  author    = {Embretson, Susan E. and Reise, Steven P.},\n  title     = {Item Response Theory for Psychologists},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2000},\n  address   = {Mahwah, NJ}\n}\n\n@book{thissen2001,\n  author    = {Thissen, David and Wainer, Howard},\n  title     = {Test Scoring},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {2001},\n  address   = {Mahwah, NJ}\n}\n\n% ============================================================\n% 4PL Model & Identifiability\n% ============================================================\n\n@article{barton1981,\n  author  = {Barton, Mark A. and Lord, Frederic M.},\n  title   = {An Upper Asymptote for the Three-Parameter Logistic Item-Response Model},\n  journal = {ETS Research Report Series},\n  volume  = {1981},\n  number  = {1},\n  pages   = {i--8},\n  year    = {1981},\n  doi     = {10.1002/j.2333-8504.1981.tb01255.x}\n}\n\n@article{culpepper2016,\n  author  = {Culpepper, Steven Andrew},\n  title   = {Revisiting the 4-Parameter Item Response Model: {B}ayesian Estimation and Application},\n  journal = {Psychometrika},\n  volume  = {81},\n  number  = {4},\n  pages   = {1142--1163},\n  year    = {2016},\n  doi     = {10.1007/s11336-015-9477-6}\n}\n\n@article{liao2012,\n  author  = {Liao, Wen-Wei and Ho, Rong-Guey and Yen, Yung-Chin and Cheng, Hao-Chang},\n  title   = {The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses},\n  journal = {Social Behavior and Personality},\n  volume  = {40},\n  number  = {10},\n  pages   = {1679--1694},\n  year    = {2012},\n  doi     = {10.2224/sbp.2012.40.10.1679}\n}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 17_

Now let me verify the output.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "c0dc438c-88d9-4fff-99f9-234a9b397c7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kNPaAqWqw14vPyjzVwgYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24441,
      "cache_read_input_tokens": 48711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24441
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

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01Tt2tfu7XHH4aPTqmh4JQLR`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft && echo \"=== Total entries ===\" && grep -c \"^@\" references.bib && echo \"\" && echo \"=== Literature map keys present ===\" && for key in adams_1997_mrcml angelopoulos_2023_conformal brown_2024_ppp burnell_2023_structure carlini_2021_extracting chiang_2024_chatbot_arena choi_2025_kds cormack_2009_rrf deboeck_2004_explanatory_irt dekoninck_2024_constat deng_2024_tsguessing dong_2024_cdd eckerly_2017_item_compromise ercikan_2008_dif_cancellation golchin_2024_time_travel guo_2017_calibration habba_2025_growing_pains holland_1993_dif kievit_2013_simpsons_paradox lalor_2024_irt_nlp li_2024_atlas li_2024_open_llm_leaderboard li_2025_dcr liang_2023_helm luettgau_2025_hibayes mislevy_1986_bayes_irt oren_2023_proving_contamination polo_2024_tinybenchmarks reckase_2009_mirt sanmartin_2009_irt schaeffer_2026_generative_contamination shi_2023_minkprob shokri_2017_mia sinharay_2017_preknowledge sinharay_2025_irt_fit sun_2025_emperors_new_clothes talts_2018_sbc wang_2024_mmlu_pro white_2024_livebench wust_2025_selfcritique xu_2025_dcr yang_2023_rethinking_benchmark zhang_2024_gsm1k zhang_2024_minkpp zheng_2023_chatbot_arena zhou_2025_psnirt; do if grep -q \"{$key,\" references.bib; then echo \"  OK: $key\"; else echo \"  MISSING: $key\"; fi; done | grep MISSING && echo \"\" && echo \"=== Brace balance check ===\" && python3 -c \"\nimport re\nwith open('references.bib') as f:\n    content = f.read()\nentries = re.findall(r'^@\\w+\\{', content, re.MULTILINE)\nprint(f'Entry count: {len(entries)}')\ndepth = 0\nfor i, ch in enumerate(content):\n    if ch == '{': depth += 1\n    elif ch == '}': depth -= 1\n    if depth < 0:\n        print(f'ERROR: unmatched closing brace at position {i}')\n        break\nif depth == 0:\n    print('Braces balanced: OK')\nelse:\n    print(f'ERROR: unbalanced braces, final depth = {depth}')\n\"",
  "description": "Verify bib entry count, literature map coverage, and brace balance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "ef633519-9044-4cef-ae86-8a022e7a2b05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014kNPaAqWqw14vPyjzVwgYF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 24441,
      "cache_read_input_tokens": 48711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24441
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

_source line 19 · 2026-05-17T03:55:51.149Z_

<details><summary>↩ Tool result · reported error · `toolu_01Tt2tfu7XHH4aPTqmh4JQLR`</summary>

```text
Exit code 1
=== Total entries ===
107

=== Literature map keys present ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "ac66798a-9de2-48fd-87b6-28e32d59e1d6",
  "tool_use_result": "Error: Exit code 1\n=== Total entries ===\n107\n\n=== Literature map keys present ==="
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
The grep MISSING found nothing (all keys are present - the `grep MISSING` returned nothing, which is why exit code is 1 from the pipe). Let me verify with a different approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "6ab0bffb-62fc-47b2-9708-3955b7b24cb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrLxdxSWFpkz4TZWbLvsf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 73152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 21_

The `grep MISSING` returned nothing (exit code 1 means no missing keys found). Let me verify the brace balance separately.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "cd71079a-520f-43e3-89e3-bb36a0f6390b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrLxdxSWFpkz4TZWbLvsf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 73152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01MVz5iiVCWswmTi7kkMGceo`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/paper_draft && python3 -c \"\nimport re\nwith open('references.bib') as f:\n    content = f.read()\nentries = re.findall(r'^@\\w+\\{', content, re.MULTILINE)\nprint(f'Total bib entries: {len(entries)}')\ndepth = 0\nfor i, ch in enumerate(content):\n    if ch == '{': depth += 1\n    elif ch == '}': depth -= 1\n    if depth < 0:\n        print(f'ERROR: unmatched closing brace at position {i}')\n        break\nif depth == 0:\n    print('Braces balanced: OK')\nelse:\n    print(f'ERROR: unbalanced braces, final depth = {depth}')\n\n# Count literature map keys\nlit_keys = ['adams_1997_mrcml','angelopoulos_2023_conformal','brown_2024_ppp','burnell_2023_structure','carlini_2021_extracting','chiang_2024_chatbot_arena','choi_2025_kds','cormack_2009_rrf','deboeck_2004_explanatory_irt','dekoninck_2024_constat','deng_2024_tsguessing','dong_2024_cdd','eckerly_2017_item_compromise','ercikan_2008_dif_cancellation','golchin_2024_time_travel','guo_2017_calibration','habba_2025_growing_pains','holland_1993_dif','kievit_2013_simpsons_paradox','lalor_2024_irt_nlp','li_2024_atlas','li_2024_open_llm_leaderboard','li_2025_dcr','liang_2023_helm','luettgau_2025_hibayes','mislevy_1986_bayes_irt','oren_2023_proving_contamination','polo_2024_tinybenchmarks','reckase_2009_mirt','sanmartin_2009_irt','schaeffer_2026_generative_contamination','shi_2023_minkprob','shokri_2017_mia','sinharay_2017_preknowledge','sinharay_2025_irt_fit','sun_2025_emperors_new_clothes','talts_2018_sbc','wang_2024_mmlu_pro','white_2024_livebench','wust_2025_selfcritique','xu_2025_dcr','yang_2023_rethinking_benchmark','zhang_2024_gsm1k','zhang_2024_minkpp','zheng_2023_chatbot_arena','zhou_2025_psnirt']\nfound = 0\nmissing = []\nfor key in lit_keys:\n    if '{' + key + ',' in content:\n        found += 1\n    else:\n        missing.append(key)\nprint(f'Literature map coverage: {found}/{len(lit_keys)}')\nif missing:\n    print(f'Missing: {missing}')\nelse:\n    print('All literature_map ids have corresponding bib entries.')\n\"",
  "description": "Verify bib integrity and coverage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "54924b3b-0af3-47df-956e-850f4b35454f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrLxdxSWFpkz4TZWbLvsf6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 73152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 874
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

_source line 23 · 2026-05-17T03:56:07.943Z_

<details><summary>↩ Tool result · `toolu_01MVz5iiVCWswmTi7kkMGceo`</summary>

```text
Total bib entries: 107
Braces balanced: OK
Literature map coverage: 46/46
All literature_map ids have corresponding bib entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "4c5f667a-eb4d-4406-b83a-3009411b0cac",
  "tool_use_result": {
    "stdout": "Total bib entries: 107\nBraces balanced: OK\nLiterature map coverage: 46/46\nAll literature_map ids have corresponding bib entries.",
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

_source line 24_

完成。

- **107 条 bib entries** 总计（46 条 literature_map 新增 + 61 条原有保留）
- **46/46** literature_map ids 全部覆盖（实际 YAML 中有 46 篇，非 summary 声称的 43）
- 括号配对检查通过
- 备份已存为 `references.bib.prev`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "uuid": "64cf11fe-f718-4cbc-b47d-9385679819ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XFmUsXgk3ppyPbFMi9bdiR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 74026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
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

_source line 25_

完成。

- **107 条 bib entries** 总计（46 条 literature_map 新增 + 61 条原有保留）
- **46/46** literature_map ids 全部覆盖（实际 YAML 中有 46 篇，非 summary 声称的 43）
- 括号配对检查通过
- 备份已存为 `references.bib.prev`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 435098,
  "duration_api_ms": 435459,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "82b238c6-e266-4adf-8ada-7c5569f10be0",
  "total_cost_usd": 1.2486540000000002,
  "usage": {
    "input_tokens": 9069,
    "cache_creation_input_tokens": 63304,
    "cache_read_input_tokens": 273680,
    "output_tokens": 26716,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 63304,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 113,
        "cache_read_input_tokens": 74026,
        "cache_creation_input_tokens": 1119,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1119
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2829,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0029189999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9069,
      "outputTokens": 26716,
      "cacheReadInputTokens": 273680,
      "cacheCreationInputTokens": 63304,
      "webSearchRequests": 0,
      "costUSD": 1.245735,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "de7de92d-b5bc-4517-ad1a-394ff1e7c95c"
}
```

</details>

---
