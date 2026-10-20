# review sf8 five bib entries

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_review_sf8-five-bib-entries_20260518T051659.log`
- **Structured JSON:** [`78c0d09a6cf22d70c4ee.json`](../../sessions/78/78c0d09a6cf22d70c4ee.json)

## Before a recorded user message

39 recorded events

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
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
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
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "a100c2d5-ebf2-40e7-ba50-229b9077c072",
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
    "resetsAt": 1779089400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5ef6c333-2d8a-4baf-a678-3e310976f9a0",
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current references.bib to understand the format, then search for each paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "1beff754-a846-4bf3-819b-74b73c9d0564",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRo5JDyD4iRcq2NYrq8czq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14043,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14043
      },
      "output_tokens": 28,
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

读取现有 bib 文件，同时并行搜索 5 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "76631a86-0bb2-4d4b-ba95-7b413d00c92f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRo5JDyD4iRcq2NYrq8czq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14043,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14043
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — Read · `toolu_01EZUqYcuiuugAJJFz8SxzaL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "df3aa767-cb41-4481-82db-f9250086b2f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRo5JDyD4iRcq2NYrq8czq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14043,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14043
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UyVkLbixFC8aLsDcpMxvXq`</summary>

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
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "7dda2aeb-5f0e-46af-aa6f-d1de05b21f58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRo5JDyD4iRcq2NYrq8czq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14043,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14043
      },
      "output_tokens": 28,
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

_source line 8 · 2026-05-18T05:17:11.721Z_

<details><summary>↩ Tool result · `toolu_01EZUqYcuiuugAJJFz8SxzaL`</summary>

```text
1	% ============================================================
2	% Literature Map Entries (keys from literature_map.yaml ids)
3	% ============================================================
4	
5	@inproceedings{carlini_2021_extracting,
6	  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},
7	  title     = {Extracting Training Data from Large Language Models},
8	  booktitle = {Proceedings of the 30th USENIX Security Symposium},
9	  year      = {2021},
10	  url       = {https://arxiv.org/abs/2012.07805}
11	}
12	
13	@inproceedings{choi_2025_kds,
14	  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},
15	  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},
16	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
17	  year      = {2025},
18	  url       = {https://arxiv.org/abs/2502.00678}
19	}
20	
21	@inproceedings{cormack_2009_rrf,
22	  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},
23	  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},
24	  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
25	  pages     = {758--759},
26	  year      = {2009},
27	  publisher = {ACM},
28	  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}
29	}
30	
31	@book{deboeck_2004_explanatory_irt,
32	  author    = {De Boeck, Paul and Wilson, Mark},
33	  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},
34	  publisher = {Springer},
35	  year      = {2004},
36	  address   = {New York},
37	  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}
38	}
39	
40	@inproceedings{deng_2024_tsguessing,
41	  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},
42	  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},
43	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
44	  year      = {2024},
45	  url       = {https://arxiv.org/abs/2311.09783}
46	}
47	
48	@inproceedings{dong_2024_cdd,
49	  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Gu, Bin and Yang, Mengfei and Li, Ge},
50	  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},
51	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},
52	  year      = {2024},
53	  url       = {https://arxiv.org/abs/2402.15938}
54	}
55	
56	@incollection{eckerly_2017_item_compromise,
57	  author    = {Eckerly, Carol A.},
58	  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},
59	  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},
60	  editor    = {Cizek, Gregory J. and Wollack, James A.},
61	  publisher = {Routledge},
62	  year      = {2017},
63	  chapter   = {5},
64	  doi       = {10.4324/9781315743097-5}
65	}
66	
67	@inproceedings{golchin_2024_time_travel,
68	  author    = {Golchin, Shahriar and Surdeanu, Mihai},
69	  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},
70	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
71	  year      = {2024},
72	  url       = {https://arxiv.org/abs/2308.08493}
73	}
74	
75	@inproceedings{guo_2017_calibration,
76	  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
77	  title     = {On Calibration of Modern Neural Networks},
78	  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},
79	  pages     = {1321--1330},
80	  year      = {2017},
81	  url       = {https://arxiv.org/abs/1706.04599}
82	}
83	
84	@article{habba_2025_growing_pains,
85	  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},
86	  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},
87	  journal       = {arXiv preprint},
88	  year          = {2026},
89	  eprint        = {2604.12843},
90	  archiveprefix = {arXiv},
91	  url           = {https://arxiv.org/abs/2604.12843}
92	}
93	
94	@book{holland_1993_dif,
95	  author    = {Holland, Paul W. and Wainer, Howard},
96	  title     = {Differential Item Functioning},
97	  publisher = {Lawrence Erlbaum Associates},
98	  year      = {1993},
99	  address   = {Hillsdale, NJ}
100	}
101	
102	@inproceedings{lalor_2024_irt_nlp,
103	  author    = {Lalor, John P. and Rodriguez, Pedro and Sedoc, Jo\~{a}o and Hernandez-Orallo, Jose},
104	  title     = {Item Response Theory for Natural Language Processing},
105	  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},
106	  year      = {2024},
107	  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}
108	}
109	
110	@article{li_2024_atlas,
111	  author        = {Li, Peiyu and Tang, Xiuxiu and Chen, Si and Cheng, Ying and Metoyer, Ronald and Hua, Ting and Chawla, Nitesh V.},
112	  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},
113	  journal       = {arXiv preprint},
114	  year          = {2025},
115	  eprint        = {2511.04689},
116	  archiveprefix = {arXiv},
117	  url           = {https://arxiv.org/abs/2511.04689}
118	}
119	
120	@inproceedings{xu2025dcr,
121	  author    = {Xu, Cheng and Yan, Nan and Guan, Shuhao and Jin, Changhong and Mei, Yuke and Guo, Yibing and Kechadi, Tahar},
122	  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},
123	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
124	  pages     = {23002--23020},
125	  year      = {2025},
126	  eprint    = {2507.11405},
127	  archiveprefix = {arXiv},
128	  url       = {https://aclanthology.org/2025.emnlp-main.1173/}
129	}
130	
131	@article{luettgau_2025_hibayes,
132	  author        = {Luettgau, Lennart and Coppock, Harry and Dubois, Magda and Summerfield, Christopher and Ududec, Cozmin},
133	  title         = {{HiBayES}: A Hierarchical {Bayesian} Modeling Framework for {AI} Evaluation Statistics},
134	  journal       = {arXiv preprint},
135	  year          = {2025},
136	  eprint        = {2505.05602},
137	  archiveprefix = {arXiv},
138	  url           = {https://arxiv.org/abs/2505.05602}
139	}
140	
141	@inproceedings{polo_2024_tinybenchmarks,
142	  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},
143	  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},
144	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
145	  year      = {2024},
146	  url       = {https://arxiv.org/abs/2402.14992}
147	}
148	
149	@article{sanmartin_2009_irt,
150	  author  = {San Mart\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},
151	  title   = {Consequential Validity and Item Response Theory},
152	  journal = {Psychometrika},
153	  volume  = {74},
154	  number  = {2},
155	  pages   = {349--367},
156	  year    = {2009}
157	}
158	
159	@inproceedings{shi_2023_minkprob,
160	  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
161	  title     = {Detecting Pretraining Data from Large Language Models},
162	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
163	  year      = {2024},
164	  url       = {https://arxiv.org/abs/2310.16789}
165	}
166	
167	@inproceedings{shokri_2017_mia,
168	  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},
169	  title     = {Membership Inference Attacks Against Machine Learning Models},
170	  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\&P)},
171	  year      = {2017},
172	  url       = {https://arxiv.org/abs/1610.05820}
173	}
174	
175	@article{sinharay_2017_preknowledge,
176	  author  = {Sinharay, Sandip},
177	  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},
178	  journal = {Journal of Educational and Behavioral Statistics},
179	  volume  = {42},
180	  number  = {1},
181	  year    = {2017},
182	  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}
183	}
184	
185	@article{tao2025detecting,
186	  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},
187	  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},
188	  journal       = {arXiv preprint},
189	  year          = {2025},
190	  eprint        = {2510.09259},
191	  archiveprefix = {arXiv},
192	  url           = {https://arxiv.org/abs/2510.09259}
193	}
194	
195	@inproceedings{zhang_2024_gsm1k,
196	  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},
197	  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},
198	  booktitle = {arXiv preprint},
199	  year      = {2024},
200	  eprint    = {2405.00332},
201	  url       = {https://arxiv.org/abs/2405.00332}
202	}
203	
204	@inproceedings{zhang_2024_minkpp,
205	  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},
206	  title     = {{Min-K\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},
207	  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},
208	  year      = {2025},
209	  url       = {https://arxiv.org/abs/2404.02936}
210	}
211	
212	@inproceedings{zhou_2025_psnirt,
213	  author    = {Zhou, Hongli and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},
214	  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},
215	  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},
216	  year      = {2026},
217	  url       = {https://arxiv.org/abs/2505.15055}
218	}
219	
220	% ============================================================
221	% Existing Entries (preserved for backward compatibility)
222	% ============================================================
223	
224	% --- Missing References (added D138) ---
225	
226	@book{lord_1980_irt,
227	  author    = {Lord, Frederic M.},
228	  title     = {Applications of Item Response Theory to Practical Testing Problems},
229	  publisher = {Lawrence Erlbaum Associates},
230	  year      = {1980},
231	  address   = {Hillsdale, NJ},
232	  isbn      = {978-0-89859-006-7},
233	  doi       = {10.4324/9780203056615}
234	}
235	
236	@book{hambleton_1991_irt,
237	  author    = {Hambleton, Ronald K. and Swaminathan, Hariharan and Rogers, H. Jane},
238	  title     = {Fundamentals of Item Response Theory},
239	  publisher = {Sage Publications},
240	  year      = {1991},
241	  address   = {Newbury Park, CA},
242	  isbn      = {978-0-8039-3647-8}
243	}
244	
245	@article{liang_2023_helm,
246	  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and Zelikman, Eric and Durmus, Esin and Ladhak, Faisal and Rong, Frieda and Ren, Hongyu and Yao, Huaxiu and Wang, Jue and Santhanam, Keshav and Orr, Laurel and Zheng, Lucia and Y\"{u}ksekg\"{o}n\"{u}l, Mert and Suzgun, Mirac and Kim, Nathan and Guha, Neel and Chatterji, Niladri S. and Khattab, Omar and Henderson, Peter and Huang, Qian and Chi, Ryan A. and Xie, Sang Michael and Santurkar, Shibani and Ganguli, Surya and Hashimoto, Tatsunori and Icard, Thomas and Zhang, Tianyi and Chaudhary, Vishrav and Wang, William and Li, Xuechen and Mai, Yifan and Zhang, Yuhui and Koreeda, Yuta},
247	  title   = {Holistic Evaluation of Language Models},
248	  journal = {Annals of the New York Academy of Sciences},
249	  volume  = {1525},
250	  number  = {1},
251	  pages   = {140--146},
252	  year    = {2023},
253	  doi     = {10.1111/nyas.15007}
254	}
255	
256	@inproceedings{magar_2022_contamination,
257	  author    = {Magar, Inbal and Schwartz, Roy},
258	  title     = {Data Contamination: From Memorization to Exploitation},
259	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
260	  pages     = {157--165},
261	  year      = {2022},
262	  address   = {Dublin, Ireland},
263	  publisher = {Association for Computational Linguistics},
264	  doi       = {10.18653/v1/2022.acl-short.18}
265	}
266	
267	% --- Core Methodology ---
268	
269	@article{kadavath2022,
270	  author        = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
271	  title         = {Language Models (Mostly) Know What They Know},
272	  journal       = {arXiv preprint},
273	  year          = {2022},
274	  eprint        = {2207.05221},
275	  archiveprefix = {arXiv},
276	  url           = {https://arxiv.org/abs/2207.05221}
277	}
278	
279	% --- Bayesian Inference & Diagnostics ---
280	
281	@article{hoffman2014,
282	  author  = {Hoffman, Matthew D. and Gelman, Andrew},
283	  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},
284	  journal = {Journal of Machine Learning Research},
285	  volume  = {15},
286	  number  = {47},
287	  pages   = {1593--1623},
288	  year    = {2014}
289	}
290	
291	@article{carpenter2017,
292	  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},
293	  title   = {Stan: A Probabilistic Programming Language},
294	  journal = {Journal of Statistical Software},
295	  volume  = {76},
296	  number  = {1},
297	  pages   = {1--32},
298	  year    = {2017}
299	}
300	
301	% --- Contamination Detection Methods ---
302	
303	@inproceedings{dekoninck2024constat,
304	  author    = {Dekoninck, Jasper and M\"{u}ller, Mark Niklas and Vechev, Martin},
305	  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},
306	  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},
307	  year      = {2024}
308	}
309	
310	@inproceedings{oren2024proving,
311	  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Ladhak, Faisal and Hashimoto, Tatsunori},
312	  title     = {Proving Test Set Contamination in Black Box Language Models},
313	  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},
314	  year      = {2024}
315	}
316	
317	% --- Contamination Analysis & Mitigation ---
318	
319	@inproceedings{sun2025emperor,
320	  author    = {Sun, Yifan and Wang, Han and Li, Dongbai and Wang, Gang and Zhang, Huan},
321	  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},
322	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
323	  year      = {2025},
324	  note      = {arXiv:2503.16402}
325	}
326	
327	@inproceedings{kocyigit2025impact,
328	  author        = {Kocyigit, Murat Yildirim and Yildirim, Ekin Akyurek},
329	  title         = {The Impact of Post-training on Data Contamination Detection in Large Language Models},
330	  booktitle     = {Advances in Neural Information Processing Systems 38 (NeurIPS)},
331	  year          = {2025},
332	  eprint        = {2601.06103},
333	  archiveprefix = {arXiv}
334	}
335	
336	@inproceedings{zhang2025forget,
337	  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},
338	  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},
339	  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},
340	  year      = {2025}
341	}
342	
343	% --- IRT for LLM Evaluation ---
344	
345	% --- Score Adjustment & Decontamination ---
346	
347	@inproceedings{yang2024inference,
348	  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},
349	  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},
350	  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},
351	  year      = {2024}
352	}
353	
354	% --- Benchmarking ---
355	
356	@inproceedings{hendrycks2021mmlu,
357	  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},
358	  title     = {Measuring Massive Multitask Language Understanding},
359	  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},
360	  year      = {2021}
361	}
362	
363	@article{cobbe2021gsm8k,
364	  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
365	  title         = {Training Verifiers to Solve Math Word Problems},
366	  journal       = {arXiv preprint},
367	  year          = {2021},
368	  eprint        = {2110.14168},
369	  archiveprefix = {arXiv}
370	}
371	
372	@article{clark2018arc,
373	  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},
374	  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},
375	  journal   = {arXiv preprint},
376	  year      = {2018},
377	  eprint    = {1803.05457},
378	  archiveprefix = {arXiv}
379	}
380	
381	@article{chang2025benchmarking,
382	  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},
383	  title     = {A Survey on Evaluation of Large Language Models},
384	  journal   = {ACM Transactions on Intelligent Systems and Technology},
385	  volume    = {15},
386	  number    = {3},
387	  pages     = {1--45},
388	  year      = {2024},
389	  doi       = {10.1145/3641289}
390	}
391	
392	@article{white2024livebench,
393	  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},
394	  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},
395	  journal       = {arXiv preprint},
396	  year          = {2024},
397	  eprint        = {2406.19314},
398	  archiveprefix = {arXiv}
399	}
400	
401	% --- Differential Item Functioning (DIF) ---
402	
403	@incollection{thissen1993dif,
404	  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},
405	  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},
406	  booktitle = {Differential Item Functioning},
407	  editor    = {Holland, Paul W. and Wainer, Howard},
408	  publisher = {Lawrence Erlbaum Associates},
409	  pages     = {67--113},
410	  year      = {1993}
411	}
412	
413	@book{zumbo1999dif,
414	  author    = {Zumbo, Bruno D.},
415	  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},
416	  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},
417	  year      = {1999},
418	  address   = {Ottawa, ON}
419	}
420	
421	% --- ML Calibration ---
422	
423	% --- Conformal Prediction ---
424	
425	% --- Data Attribution ---
426	
427	% --- Multidimensional IRT ---
428	
429	% --- Exposure-Ability Collinearity & IRT Identifiability ---
430	
431	% --- Measurement Error & Attenuation Bias ---
432	
433	% --- IRT Information & Power Analysis ---
434	
435	% --- 4PL Model & Identifiability ---
436	
437	% --- Model Family References ---
438	
439	@article{qwen2024qwen25,
440	  author        = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Lin, Junyang and Zhou, Jingren},
441	  title         = {Qwen2.5 Technical Report},
442	  journal       = {arXiv preprint},
443	  year          = {2024},
444	  eprint        = {2412.15115},
445	  archiveprefix = {arXiv}
446	}
447	
448	@inproceedings{hu2022lora,
449	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
450	  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},
451	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
452	  year      = {2022},
453	  eprint    = {2106.09685},
454	  archiveprefix = {arXiv}
455	}
456	
457	@article{grattafiori2024llama3,
458	  author        = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},
459	  title         = {The {Llama} 3 Herd of Models},
460	  journal       = {arXiv preprint},
461	  year          = {2024},
462	  eprint        = {2407.21783},
463	  archiveprefix = {arXiv}
464	}
465	
466	@article{gelman2012why,
467	  author  = {Gelman, Andrew and Hill, Jennifer and Yajima, Masanao},
468	  title   = {Why We (Usually) Don't Have to Worry About Multiple Comparisons},
469	  journal = {Journal of Research on Educational Effectiveness},
470	  volume  = {5},
471	  number  = {2},
472	  pages   = {189--211},
473	  year    = {2012},
474	  doi     = {10.1080/19345747.2011.618213},
475	  url     = {https://www.tandfonline.com/doi/abs/10.1080/19345747.2011.618213}
476	}
477	
478	@inproceedings{han2026quantifying,
479	  author    = {Han, Jongwook and Song, Woojung and Lee, Jonggeun and Jo, Yohan},
480	  title     = {Quantifying Data Contamination in Psychometric Evaluations of {LLMs}},
481	  booktitle = {Findings of the Association for Computational Linguistics: EACL 2026},
482	  pages     = {6070--6088},
483	  year      = {2026},
484	  url       = {https://aclanthology.org/2026.findings-eacl.319/}
485	}
486	
487	@article{schaeffer2026causally,
488	  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Baber and Liu, Ken Ziyu and Miranda, Brando and Ahmed, Ahmed and Berez, Fazl and Puri, Abhay and Biderman, Stella and Mireshghallah, Niloofar and Koyejo, Sanmi},
489	  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},
490	  journal       = {arXiv preprint},
491	  year          = {2026},
492	  eprint        = {2601.04301},
493	  archiveprefix = {arXiv},
494	  url           = {https://arxiv.org/abs/2601.04301}
495	}
496	
497	@inproceedings{chen2025benchmarking,
498	  author    = {Chen, Simin and Chen, Yiming and Li, Zexin and Jiang, Yifan and Wan, Zhongwei and He, Yixin and Ran, Dezhi and Gu, Tianle and Li, Haizhou and Xie, Tao and Ray, Baishakhi},
499	  title     = {Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation},
500	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
501	  pages     = {10080--10098},
502	  year      = {2025},
503	  url       = {https://aclanthology.org/2025.emnlp-main.511/}
504	}
505	
506	@article{singh2024evaluation,
507	  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},
508	  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},
509	  journal       = {arXiv preprint},
510	  year          = {2024},
511	  eprint        = {2411.03923},
512	  archiveprefix = {arXiv},
513	  url           = {https://arxiv.org/abs/2411.03923}
514	}
515	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "f01a657b-e9c0-4b6a-815b-05d5d83156b6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
      "content": "% ============================================================\n% Literature Map Entries (keys from literature_map.yaml ids)\n% ============================================================\n\n@inproceedings{carlini_2021_extracting,\n  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},\n  title     = {Extracting Training Data from Large Language Models},\n  booktitle = {Proceedings of the 30th USENIX Security Symposium},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2012.07805}\n}\n\n@inproceedings{choi_2025_kds,\n  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},\n  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.00678}\n}\n\n@inproceedings{cormack_2009_rrf,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM},\n  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}\n}\n\n@book{deboeck_2004_explanatory_irt,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York},\n  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}\n}\n\n@inproceedings{deng_2024_tsguessing,\n  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},\n  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09783}\n}\n\n@inproceedings{dong_2024_cdd,\n  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Gu, Bin and Yang, Mengfei and Li, Ge},\n  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.15938}\n}\n\n@incollection{eckerly_2017_item_compromise,\n  author    = {Eckerly, Carol A.},\n  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},\n  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},\n  editor    = {Cizek, Gregory J. and Wollack, James A.},\n  publisher = {Routledge},\n  year      = {2017},\n  chapter   = {5},\n  doi       = {10.4324/9781315743097-5}\n}\n\n@inproceedings{golchin_2024_time_travel,\n  author    = {Golchin, Shahriar and Surdeanu, Mihai},\n  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.08493}\n}\n\n@inproceedings{guo_2017_calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{habba_2025_growing_pains,\n  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n@book{holland_1993_dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@inproceedings{lalor_2024_irt_nlp,\n  author    = {Lalor, John P. and Rodriguez, Pedro and Sedoc, Jo\\~{a}o and Hernandez-Orallo, Jose},\n  title     = {Item Response Theory for Natural Language Processing},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}\n}\n\n@article{li_2024_atlas,\n  author        = {Li, Peiyu and Tang, Xiuxiu and Chen, Si and Cheng, Ying and Metoyer, Ronald and Hua, Ting and Chawla, Nitesh V.},\n  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2511.04689}\n}\n\n@inproceedings{xu2025dcr,\n  author    = {Xu, Cheng and Yan, Nan and Guan, Shuhao and Jin, Changhong and Mei, Yuke and Guo, Yibing and Kechadi, Tahar},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {23002--23020},\n  year      = {2025},\n  eprint    = {2507.11405},\n  archiveprefix = {arXiv},\n  url       = {https://aclanthology.org/2025.emnlp-main.1173/}\n}\n\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Coppock, Harry and Dubois, Magda and Summerfield, Christopher and Ududec, Cozmin},\n  title         = {{HiBayES}: A Hierarchical {Bayesian} Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n@inproceedings{polo_2024_tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14992}\n}\n\n@article{sanmartin_2009_irt,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity and Item Response Theory},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@inproceedings{shi_2023_minkprob,\n  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.16789}\n}\n\n@inproceedings{shokri_2017_mia,\n  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},\n  title     = {Membership Inference Attacks Against Machine Learning Models},\n  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1610.05820}\n}\n\n@article{sinharay_2017_preknowledge,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  year    = {2017},\n  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}\n}\n\n@article{tao2025detecting,\n  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},\n  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n@inproceedings{zhang_2024_gsm1k,\n  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n  booktitle = {arXiv preprint},\n  year      = {2024},\n  eprint    = {2405.00332},\n  url       = {https://arxiv.org/abs/2405.00332}\n}\n\n@inproceedings{zhang_2024_minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n@inproceedings{zhou_2025_psnirt,\n  author    = {Zhou, Hongli and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2505.15055}\n}\n\n% ============================================================\n% Existing Entries (preserved for backward compatibility)\n% ============================================================\n\n% --- Missing References (added D138) ---\n\n@book{lord_1980_irt,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ},\n  isbn      = {978-0-89859-006-7},\n  doi       = {10.4324/9780203056615}\n}\n\n@book{hambleton_1991_irt,\n  author    = {Hambleton, Ronald K. and Swaminathan, Hariharan and Rogers, H. Jane},\n  title     = {Fundamentals of Item Response Theory},\n  publisher = {Sage Publications},\n  year      = {1991},\n  address   = {Newbury Park, CA},\n  isbn      = {978-0-8039-3647-8}\n}\n\n@article{liang_2023_helm,\n  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and Zelikman, Eric and Durmus, Esin and Ladhak, Faisal and Rong, Frieda and Ren, Hongyu and Yao, Huaxiu and Wang, Jue and Santhanam, Keshav and Orr, Laurel and Zheng, Lucia and Y\\\"{u}ksekg\\\"{o}n\\\"{u}l, Mert and Suzgun, Mirac and Kim, Nathan and Guha, Neel and Chatterji, Niladri S. and Khattab, Omar and Henderson, Peter and Huang, Qian and Chi, Ryan A. and Xie, Sang Michael and Santurkar, Shibani and Ganguli, Surya and Hashimoto, Tatsunori and Icard, Thomas and Zhang, Tianyi and Chaudhary, Vishrav and Wang, William and Li, Xuechen and Mai, Yifan and Zhang, Yuhui and Koreeda, Yuta},\n  title   = {Holistic Evaluation of Language Models},\n  journal = {Annals of the New York Academy of Sciences},\n  volume  = {1525},\n  number  = {1},\n  pages   = {140--146},\n  year    = {2023},\n  doi     = {10.1111/nyas.15007}\n}\n\n@inproceedings{magar_2022_contamination,\n  author    = {Magar, Inbal and Schwartz, Roy},\n  title     = {Data Contamination: From Memorization to Exploitation},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages     = {157--165},\n  year      = {2022},\n  address   = {Dublin, Ireland},\n  publisher = {Association for Computational Linguistics},\n  doi       = {10.18653/v1/2022.acl-short.18}\n}\n\n% --- Core Methodology ---\n\n@article{kadavath2022,\n  author        = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  title         = {Language Models (Mostly) Know What They Know},\n  journal       = {arXiv preprint},\n  year          = {2022},\n  eprint        = {2207.05221},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2207.05221}\n}\n\n% --- Bayesian Inference & Diagnostics ---\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n% --- Contamination Detection Methods ---\n\n@inproceedings{dekoninck2024constat,\n  author    = {Dekoninck, Jasper and M\\\"{u}ller, Mark Niklas and Vechev, Martin},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Ladhak, Faisal and Hashimoto, Tatsunori},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% --- Contamination Analysis & Mitigation ---\n\n@inproceedings{sun2025emperor,\n  author    = {Sun, Yifan and Wang, Han and Li, Dongbai and Wang, Gang and Zhang, Huan},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@inproceedings{kocyigit2025impact,\n  author        = {Kocyigit, Murat Yildirim and Yildirim, Ekin Akyurek},\n  title         = {The Impact of Post-training on Data Contamination Detection in Large Language Models},\n  booktitle     = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year          = {2025},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% --- IRT for LLM Evaluation ---\n\n% --- Score Adjustment & Decontamination ---\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n% --- Benchmarking ---\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@article{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  journal   = {ACM Transactions on Intelligent Systems and Technology},\n  volume    = {15},\n  number    = {3},\n  pages     = {1--45},\n  year      = {2024},\n  doi       = {10.1145/3641289}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n% --- Differential Item Functioning (DIF) ---\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% --- ML Calibration ---\n\n% --- Conformal Prediction ---\n\n% --- Data Attribution ---\n\n% --- Multidimensional IRT ---\n\n% --- Exposure-Ability Collinearity & IRT Identifiability ---\n\n% --- Measurement Error & Attenuation Bias ---\n\n% --- IRT Information & Power Analysis ---\n\n% --- 4PL Model & Identifiability ---\n\n% --- Model Family References ---\n\n@article{qwen2024qwen25,\n  author        = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Lin, Junyang and Zhou, Jingren},\n  title         = {Qwen2.5 Technical Report},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2412.15115},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n  eprint    = {2106.09685},\n  archiveprefix = {arXiv}\n}\n\n@article{grattafiori2024llama3,\n  author        = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title         = {The {Llama} 3 Herd of Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2407.21783},\n  archiveprefix = {arXiv}\n}\n\n@article{gelman2012why,\n  author  = {Gelman, Andrew and Hill, Jennifer and Yajima, Masanao},\n  title   = {Why We (Usually) Don't Have to Worry About Multiple Comparisons},\n  journal = {Journal of Research on Educational Effectiveness},\n  volume  = {5},\n  number  = {2},\n  pages   = {189--211},\n  year    = {2012},\n  doi     = {10.1080/19345747.2011.618213},\n  url     = {https://www.tandfonline.com/doi/abs/10.1080/19345747.2011.618213}\n}\n\n@inproceedings{han2026quantifying,\n  author    = {Han, Jongwook and Song, Woojung and Lee, Jonggeun and Jo, Yohan},\n  title     = {Quantifying Data Contamination in Psychometric Evaluations of {LLMs}},\n  booktitle = {Findings of the Association for Computational Linguistics: EACL 2026},\n  pages     = {6070--6088},\n  year      = {2026},\n  url       = {https://aclanthology.org/2026.findings-eacl.319/}\n}\n\n@article{schaeffer2026causally,\n  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Baber and Liu, Ken Ziyu and Miranda, Brando and Ahmed, Ahmed and Berez, Fazl and Puri, Abhay and Biderman, Stella and Mireshghallah, Niloofar and Koyejo, Sanmi},\n  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2601.04301}\n}\n\n@inproceedings{chen2025benchmarking,\n  author    = {Chen, Simin and Chen, Yiming and Li, Zexin and Jiang, Yifan and Wan, Zhongwei and He, Yixin and Ran, Dezhi and Gu, Tianle and Li, Haizhou and Xie, Tao and Ray, Baishakhi},\n  title     = {Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {10080--10098},\n  year      = {2025},\n  url       = {https://aclanthology.org/2025.emnlp-main.511/}\n}\n\n@article{singh2024evaluation,\n  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},\n  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2411.03923},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2411.03923}\n}\n",
      "numLines": 515,
      "startLine": 1,
      "totalLines": 515
    }
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T05:17:11.703Z_

<details><summary>↩ Tool result · `toolu_01UyVkLbixFC8aLsDcpMxvXq`</summary>

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
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "9e3cfd7c-2953-4986-bff0-2daca671f6ca",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the bib file format and WebSearch tool. Let me search for all 5 papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "30fa216c-1e1f-4f32-b62d-82c47fb63ac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

并行搜索 5 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "828102a9-ea02-4f6d-936e-779068bb1ad0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L3zMUn2aWDecWK4kZ7zsvx`</summary>

```json
{
  "query": "Camilli Shepard 1994 DIF differential item functioning book"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "d8e27728-8ea2-4789-be9e-c33e33c5cf31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q7AMk4jY8avgmeNFBAm8xV`</summary>

```json
{
  "query": "Swaminathan Rogers 1990 logistic regression DIF detecting differential item functioning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "0235d78e-e5a5-4a16-8a0c-49553ed46e4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PYGZ1KbzGZErJ7T3UoFBTz`</summary>

```json
{
  "query": "Xu 2024 \"Benchmarking Benchmark Leakage\" LLMs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "4df611f5-fb0f-4ee7-9d30-155856511995",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_017EpeFTVhZmn9zcDZJvwpR5`</summary>

```json
{
  "query": "Li 2024 \"Task Contamination\" \"Language Models May Not Be Few-Shot Anymore\" AAAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "00903650-8ef8-49c3-b3d5-bdb12ccd3215",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MpJjXGJru346PTuqWAtaz8`</summary>

```json
{
  "query": "IRT identifiability small sample size parameter recovery simulation study 2020 2021 2022 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "0b7a5cd2-afaa-4ee8-90fb-4dd732c867b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Ks9XtrSR28riVWQbBL9WB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10315,
      "cache_read_input_tokens": 25884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10315
      },
      "output_tokens": 21,
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

_source line 17 · 2026-05-18T05:17:23.482Z_

<details><summary>↩ Tool result · `toolu_01L3zMUn2aWDecWK4kZ7zsvx`</summary>

```text
Web search results for query: "Camilli Shepard 1994 DIF differential item functioning book"

Links: [{"title":"Methods for Identifying Biased Test Items (Measurement Methods for the Social Science) - Camilli, Gregory; Shepard, Lorrie: 9780803944169 - AbeBooks","url":"https://www.abebooks.com/9780803944169/Methods-Identifying-Biased-Test-Items-0803944160/plp"},{"title":"Sage Research Methods Differential Item Functioning","url":"https://methods.sagepub.com/book/mono/preview/differential-item-functioning.pdf"},{"title":"Statistical Software for Differential Item Functioning Analysis (Appendix) - Cross-Cultural Research Methods in Psychology","url":"https://www.cambridge.org/core/books/abs/crosscultural-research-methods-in-psychology/statistical-software-for-differential-item-functioning-analysis/458B73203D639F3D0A997E134BD2A841"},{"title":"The Theory and Methods of Differential Item Functioning ( ...","url":"https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf"},{"title":"(PDF) Differential item functioning","url":"https://www.academia.edu/3853712/Differential_item_functioning"},{"title":"(PDF) An introduction to Differential Item Functioning","url":"https://www.academia.edu/1030760/An_introduction_to_Differential_Item_Functioning"},{"title":"The Investigation of Differential Item Functioning in Adaptive Tests | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-0-387-85461-8_17"},{"title":"ERIC - EJ598345 - \"Methods for Identifying Biased Test Items\" by Gregory Camilli and Lorrie A. Shepard., Journal of Educational Measurement, 1996","url":"https://eric.ed.gov/?id=EJ598345"},{"title":"Book Review : Differential Item Functioning Edited by Paul W. Holland and Howard Wainer Hillsdale NJ: Erlbaum, 1993, 453 pp - Roger E. Millsap, 1993","url":"https://journals.sagepub.com/doi/10.1177/014662169301700113"},{"title":"Differential Item Functioning: Beyond validity evidence ...","url":"https://www.psicothema.com/pdf/4457.pdf"}]

Based on the search results, I found information about the book you're looking for:

"Methods for Identifying Biased Test Items" by Gregory Camilli and Lorrie A. Shepard was published by Sage Publications in Thousand Oaks, CA in 1994.

The book is aimed at helping researchers understand how item bias methods work and provides practical advice and specific details on the most useful methods for particular testing situations. It begins with a review of early bias methods and fairness issues, and explains the logic of each method in terms of how differential item functioning (DIF) is defined.

The book is designed to be an instructional guide rather than a technical manual and provides a comprehensive and integrated overview of the procedures for detecting differential item functioning with citations to more technically detailed references.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "6b7926be-e1ea-4f60-939b-1e1fbd4253d6",
  "tool_use_result": {
    "query": "Camilli Shepard 1994 DIF differential item functioning book",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YGBgemu966wZDVoRja3Hr7",
        "content": [
          {
            "title": "Methods for Identifying Biased Test Items (Measurement Methods for the Social Science) - Camilli, Gregory; Shepard, Lorrie: 9780803944169 - AbeBooks",
            "url": "https://www.abebooks.com/9780803944169/Methods-Identifying-Biased-Test-Items-0803944160/plp"
          },
          {
            "title": "Sage Research Methods Differential Item Functioning",
            "url": "https://methods.sagepub.com/book/mono/preview/differential-item-functioning.pdf"
          },
          {
            "title": "Statistical Software for Differential Item Functioning Analysis (Appendix) - Cross-Cultural Research Methods in Psychology",
            "url": "https://www.cambridge.org/core/books/abs/crosscultural-research-methods-in-psychology/statistical-software-for-differential-item-functioning-analysis/458B73203D639F3D0A997E134BD2A841"
          },
          {
            "title": "The Theory and Methods of Differential Item Functioning ( ...",
            "url": "https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf"
          },
          {
            "title": "(PDF) Differential item functioning",
            "url": "https://www.academia.edu/3853712/Differential_item_functioning"
          },
          {
            "title": "(PDF) An introduction to Differential Item Functioning",
            "url": "https://www.academia.edu/1030760/An_introduction_to_Differential_Item_Functioning"
          },
          {
            "title": "The Investigation of Differential Item Functioning in Adaptive Tests | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-0-387-85461-8_17"
          },
          {
            "title": "ERIC - EJ598345 - \"Methods for Identifying Biased Test Items\" by Gregory Camilli and Lorrie A. Shepard., Journal of Educational Measurement, 1996",
            "url": "https://eric.ed.gov/?id=EJ598345"
          },
          {
            "title": "Book Review : Differential Item Functioning Edited by Paul W. Holland and Howard Wainer Hillsdale NJ: Erlbaum, 1993, 453 pp - Roger E. Millsap, 1993",
            "url": "https://journals.sagepub.com/doi/10.1177/014662169301700113"
          },
          {
            "title": "Differential Item Functioning: Beyond validity evidence ...",
            "url": "https://www.psicothema.com/pdf/4457.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the book you're looking for:\n\n\"Methods for Identifying Biased Test Items\" by Gregory Camilli and Lorrie A. Shepard was published by Sage Publications in Thousand Oaks, CA in 1994.\n\nThe book is aimed at helping researchers understand how item bias methods work and provides practical advice and specific details on the most useful methods for particular testing situations. It begins with a review of early bias methods and fairness issues, and explains the logic of each method in terms of how differential item functioning (DIF) is defined.\n\nThe book is designed to be an instructional guide rather than a technical manual and provides a comprehensive and integrated overview of the procedures for detecting differential item functioning with citations to more technically detailed references."
    ],
    "durationSeconds": 6.918687852000001
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T05:17:24.462Z_

<details><summary>↩ Tool result · `toolu_01PYGZ1KbzGZErJ7T3UoFBTz`</summary>

```text
Web search results for query: "Xu 2024 "Benchmarking Benchmark Leakage" LLMs"

Links: [{"title":"[2404.18824] Benchmarking Benchmark Leakage in Large Language Models","url":"https://arxiv.org/abs/2404.18824"},{"title":"Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation","url":"https://arxiv.org/html/2505.24263v1"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"GitHub - GAIR-NLP/benbench: Benchmarking Benchmark Leakage in Large Language Models · GitHub","url":"https://github.com/GAIR-NLP/benbench"},{"title":"Evaluation of benchmark data leakage using the method from (Xu et al.,... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Evaluation-of-benchmark-data-leakage-using-the-method-from-Xu-et-al-2024-The-greater_tbl1_381486092"},{"title":"Training on the Benchmark Is Not All You Need","url":"https://arxiv.org/html/2409.01790v1"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"LastingBench: Defend Benchmarks Against Knowledge Leakage","url":"https://arxiv.org/html/2506.21614v2"},{"title":"[Re] Benchmarking LLM Capabilities in Negotiation through Scoreable Games","url":"https://openreview.net/pdf?id=BVH81SAAh2"},{"title":"Benchmarking Benchmark Leakage in Large Langauge Models","url":"https://gair-nlp.github.io/benbench/"}]

I found the research paper you were looking for. Here's what I found:

The paper "Benchmarking Benchmark Leakage in Large Language Models" was submitted on April 29, 2024, by authors Ruijie Xu, Zengzhi Wang, Run-Ze Fan, and Pengfei Liu.

**Main Focus:**
The paper addresses the phenomenon of benchmark dataset leakage, which has become increasingly prominent due to opaque training processes and often undisclosed inclusion of supervised data in contemporary Large Language Models (LLMs).

**Methodology:**
The authors introduce a detection pipeline utilizing Perplexity and N-gram accuracy, two simple and scalable metrics that gauge a model's prediction precision on benchmark, to identify potential data leakages.

**Key Findings:**
By analyzing 31 LLMs under the context of mathematical reasoning, the researchers reveal substantial instances of training even test set misuse, resulting in potentially unfair comparisons.

**Recommendations:**
The paper proposes the "Benchmark Transparency Card" to encourage clear documentation of benchmark utilization, promoting transparency and healthy developments of LLMs.

The paper is available on arXiv (arXiv:2404.18824), and the authors have made their leaderboard, pipeline implementation, and model predictions publicly available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "b42a7f36-1c09-47d2-8a7e-022900ebe03d",
  "tool_use_result": {
    "query": "Xu 2024 \"Benchmarking Benchmark Leakage\" LLMs",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RBanUc3n4iUxW4pkQKhRaH",
        "content": [
          {
            "title": "[2404.18824] Benchmarking Benchmark Leakage in Large Language Models",
            "url": "https://arxiv.org/abs/2404.18824"
          },
          {
            "title": "Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation",
            "url": "https://arxiv.org/html/2505.24263v1"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/html/2601.19334v1"
          },
          {
            "title": "GitHub - GAIR-NLP/benbench: Benchmarking Benchmark Leakage in Large Language Models · GitHub",
            "url": "https://github.com/GAIR-NLP/benbench"
          },
          {
            "title": "Evaluation of benchmark data leakage using the method from (Xu et al.,... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Evaluation-of-benchmark-data-leakage-using-the-method-from-Xu-et-al-2024-The-greater_tbl1_381486092"
          },
          {
            "title": "Training on the Benchmark Is Not All You Need",
            "url": "https://arxiv.org/html/2409.01790v1"
          },
          {
            "title": "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation",
            "url": "https://arxiv.org/html/2502.17521v2"
          },
          {
            "title": "LastingBench: Defend Benchmarks Against Knowledge Leakage",
            "url": "https://arxiv.org/html/2506.21614v2"
          },
          {
            "title": "[Re] Benchmarking LLM Capabilities in Negotiation through Scoreable Games",
            "url": "https://openreview.net/pdf?id=BVH81SAAh2"
          },
          {
            "title": "Benchmarking Benchmark Leakage in Large Langauge Models",
            "url": "https://gair-nlp.github.io/benbench/"
          }
        ]
      },
      "I found the research paper you were looking for. Here's what I found:\n\nThe paper \"Benchmarking Benchmark Leakage in Large Language Models\" was submitted on April 29, 2024, by authors Ruijie Xu, Zengzhi Wang, Run-Ze Fan, and Pengfei Liu.\n\n**Main Focus:**\nThe paper addresses the phenomenon of benchmark dataset leakage, which has become increasingly prominent due to opaque training processes and often undisclosed inclusion of supervised data in contemporary Large Language Models (LLMs).\n\n**Methodology:**\nThe authors introduce a detection pipeline utilizing Perplexity and N-gram accuracy, two simple and scalable metrics that gauge a model's prediction precision on benchmark, to identify potential data leakages.\n\n**Key Findings:**\nBy analyzing 31 LLMs under the context of mathematical reasoning, the researchers reveal substantial instances of training even test set misuse, resulting in potentially unfair comparisons.\n\n**Recommendations:**\nThe paper proposes the \"Benchmark Transparency Card\" to encourage clear documentation of benchmark utilization, promoting transparency and healthy developments of LLMs.\n\nThe paper is available on arXiv (arXiv:2404.18824), and the authors have made their leaderboard, pipeline implementation, and model predictions publicly available."
    ],
    "durationSeconds": 6.351432232000003
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-18T05:17:26.190Z_

<details><summary>↩ Tool result · `toolu_017EpeFTVhZmn9zcDZJvwpR5`</summary>

```text
Web search results for query: "Li 2024 "Task Contamination" "Language Models May Not Be Few-Shot Anymore" AAAI"

Links: [{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29808"},{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29808/31400"},{"title":"Task contamination | Proceedings of the Thirty-Eighth AAAI Conference on Artificial Intelligence and Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence and Fourteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v38i16.29808"},{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://www.researchgate.net/publication/379294383_Task_Contamination_Language_Models_May_Not_Be_Few-Shot_Anymore"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.1609/aaai.v38i16.29808"},{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://arxiv.org/pdf/2312.16337"},{"title":"[2312.16337] Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://arxiv.org/abs/2312.16337"},{"title":"Task Contamination: Language models may not be few-shot anymore (Paper Explained)","url":"https://medium.com/@agnieszkamikolajczyk/task-contamination-language-models-may-not-be-few-shot-anymore-paper-explained-ea09eac078cd"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"[2312.16337v1] Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://arxiv.org/abs/2312.16337v1"}]

I found the paper! Here are the search results for "Task Contamination: Language Models May Not Be Few-Shot Anymore" by Changmao Li and Jeffrey Flanigan from AAAI 2024:

## Paper Summary

Large language models (LLMs) offer impressive performance in various zero-shot and few-shot tasks. However, their success in zero-shot or few-shot settings may be affected by task contamination, a potential limitation that has not been thoroughly examined.

## Key Findings

Utilizing GPT-3 series models and several other recent open-sourced LLMs, and controlling for dataset difficulty, the study found that datasets released prior to the LLM training data creation date perform surprisingly better than datasets released post the LLM training data creation date.

This strongly indicates that, for many LLMs, there exists task contamination on zero-shot and few-shot evaluation for datasets prior to the LLMs' training data creation date.

## Evidence and Methods

The researchers utilized training data inspection, training data extraction, and a membership inference attack, which reveal further evidence of task contamination.

## Critical Finding

For tasks with no possibility of task contamination, LLMs rarely demonstrate statistically significant improvements over simple majority baselines, in both zero and few-shot settings.

The paper is published in the Proceedings of the AAAI Conference on Artificial Intelligence 2024 and is available through both the AAAI conference website and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "106491c8-2a19-4738-b9ee-0bb7c7a32ba2",
  "tool_use_result": {
    "query": "Li 2024 \"Task Contamination\" \"Language Models May Not Be Few-Shot Anymore\" AAAI",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SsAX8Mb6KC4quMvThusH4o",
        "content": [
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/29808"
          },
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/29808/31400"
          },
          {
            "title": "Task contamination | Proceedings of the Thirty-Eighth AAAI Conference on Artificial Intelligence and Thirty-Sixth Conference on Innovative Applications of Artificial Intelligence and Fourteenth Symposium on Educational Advances in Artificial Intelligence",
            "url": "https://dl.acm.org/doi/10.1609/aaai.v38i16.29808"
          },
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://www.researchgate.net/publication/379294383_Task_Contamination_Language_Models_May_Not_Be_Few-Shot_Anymore"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?doi=10.1609/aaai.v38i16.29808"
          },
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://arxiv.org/pdf/2312.16337"
          },
          {
            "title": "[2312.16337] Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://arxiv.org/abs/2312.16337"
          },
          {
            "title": "Task Contamination: Language models may not be few-shot anymore (Paper Explained)",
            "url": "https://medium.com/@agnieszkamikolajczyk/task-contamination-language-models-may-not-be-few-shot-anymore-paper-explained-ea09eac078cd"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "[2312.16337v1] Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://arxiv.org/abs/2312.16337v1"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Task Contamination: Language Models May Not Be Few-Shot Anymore\" by Changmao Li and Jeffrey Flanigan from AAAI 2024:\n\n## Paper Summary\n\nLarge language models (LLMs) offer impressive performance in various zero-shot and few-shot tasks. However, their success in zero-shot or few-shot settings may be affected by task contamination, a potential limitation that has not been thoroughly examined.\n\n## Key Findings\n\nUtilizing GPT-3 series models and several other recent open-sourced LLMs, and controlling for dataset difficulty, the study found that datasets released prior to the LLM training data creation date perform surprisingly better than datasets released post the LLM training data creation date.\n\nThis strongly indicates that, for many LLMs, there exists task contamination on zero-shot and few-shot evaluation for datasets prior to the LLMs' training data creation date.\n\n## Evidence and Methods\n\nThe researchers utilized training data inspection, training data extraction, and a membership inference attack, which reveal further evidence of task contamination.\n\n## Critical Finding\n\nFor tasks with no possibility of task contamination, LLMs rarely demonstrate statistically significant improvements over simple majority baselines, in both zero and few-shot settings.\n\nThe paper is published in the Proceedings of the AAAI Conference on Artificial Intelligence 2024 and is available through both the AAAI conference website and arXiv."
    ],
    "durationSeconds": 6.669982623
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-18T05:17:29.727Z_

<details><summary>↩ Tool result · `toolu_01Q7AMk4jY8avgmeNFBAm8xV`</summary>

```text
Web search results for query: "Swaminathan Rogers 1990 logistic regression DIF detecting differential item functioning"

Links: [{"title":"Detecting Differential Item Functioning Using Logistic Regression Procedures - Swaminathan - 1990 - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x"},{"title":"Detecting Differential Item Functioning Using the Logistic Regression Procedure in Small Samples - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5978487/"},{"title":"Differential Item Functioning | Columbia University Mailman School of Public Health","url":"https://www.publichealth.columbia.edu/research/population-health-methods/differential-item-functioning"},{"title":"Detecting Differential Item Functioning Using Logistic Regression Procedures on JSTOR","url":"https://www.jstor.org/stable/1434855"},{"title":"Detecting differential item functioning using logistic ...","url":"https://psycnet.apa.org/record/1991-13980-001"},{"title":"ERIC - EJ419344 - Detecting Differential Item Functioning Using Logistic Regression Procedures., Journal of Educational Measurement, 1990","url":"https://eric.ed.gov/?id=EJ419344"},{"title":"The Theory and Methods of Differential Item Functioning ( ...","url":"https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Detecting+differential+item+functioning+using+logistic+regression+procedures&amp=&author=H+Swaminathan&amp=&author=HJ+Rogers&amp=&publication_year=1990&amp=&journal=J+Educ+Meas&amp=&volume=27&amp=&pages=361-70"},{"title":"Differential Item Functioning Detection Methods - ijrpr","url":"https://ijrpr.com/uploads/V5ISSUE2/IJRPR22702.pdf"},{"title":"(PDF) A Comparison of Logistic Regression and Mantel-Haenszel Procedures for Detecting Differential Item Functioning","url":"https://www.academia.edu/78078049/A_Comparison_of_Logistic_Regression_and_Mantel_Haenszel_Procedures_for_Detecting_Differential_Item_Functioning"}]

I found the seminal work you're looking for. Here are the key findings about the Swaminathan and Rogers 1990 paper on logistic regression for detecting differential item functioning (DIF):

## Publication Details

The article "Detecting Differential Item Functioning Using Logistic Regression Procedures" was published by Hariharan Swaminathan and H. Jane Rogers in the Journal of Educational Measurement, Volume 27, Number 4 (Winter, 1990), pages 361-370.

## Main Contribution

The work presents a logistic regression model for characterizing differential item functioning (DIF) between two groups. In the logistic regression procedure, an LR is used to model the probability of getting an item correct using a conditioning variable (e.g., observed total test score), a group membership, and an interaction between the conditioning variable and group membership.

## Key Methodological Features

The paper distinguishes between uniform and nonuniform DIF in terms of the model parameters, develops a statistic for testing the hypothesis of no DIF, and through simulation studies shows that the logistic regression procedure is more powerful than the Mantel-Haenszel procedure for detecting nonuniform DIF and as powerful in detecting uniform DIF.

## Impact and Adoption

The logistic regression procedure developed by Swaminathan and Rogers has become a popular method for testing differential item functioning (DIF), and Swaminathan and Rogers pointed out that the asymptotic result of an LR may not be a valid indicator of the presence of DIF in small samples.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "07e2e7c5-ef9d-460b-ae6f-92b0d63fc9d7",
  "tool_use_result": {
    "query": "Swaminathan Rogers 1990 logistic regression DIF detecting differential item functioning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SHsUoqQrGvV5HDYHz5uuH9",
        "content": [
          {
            "title": "Detecting Differential Item Functioning Using Logistic Regression Procedures - Swaminathan - 1990 - Journal of Educational Measurement - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x"
          },
          {
            "title": "Detecting Differential Item Functioning Using the Logistic Regression Procedure in Small Samples - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5978487/"
          },
          {
            "title": "Differential Item Functioning | Columbia University Mailman School of Public Health",
            "url": "https://www.publichealth.columbia.edu/research/population-health-methods/differential-item-functioning"
          },
          {
            "title": "Detecting Differential Item Functioning Using Logistic Regression Procedures on JSTOR",
            "url": "https://www.jstor.org/stable/1434855"
          },
          {
            "title": "Detecting differential item functioning using logistic ...",
            "url": "https://psycnet.apa.org/record/1991-13980-001"
          },
          {
            "title": "ERIC - EJ419344 - Detecting Differential Item Functioning Using Logistic Regression Procedures., Journal of Educational Measurement, 1990",
            "url": "https://eric.ed.gov/?id=EJ419344"
          },
          {
            "title": "The Theory and Methods of Differential Item Functioning ( ...",
            "url": "https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=Detecting+differential+item+functioning+using+logistic+regression+procedures&amp=&author=H+Swaminathan&amp=&author=HJ+Rogers&amp=&publication_year=1990&amp=&journal=J+Educ+Meas&amp=&volume=27&amp=&pages=361-70"
          },
          {
            "title": "Differential Item Functioning Detection Methods - ijrpr",
            "url": "https://ijrpr.com/uploads/V5ISSUE2/IJRPR22702.pdf"
          },
          {
            "title": "(PDF) A Comparison of Logistic Regression and Mantel-Haenszel Procedures for Detecting Differential Item Functioning",
            "url": "https://www.academia.edu/78078049/A_Comparison_of_Logistic_Regression_and_Mantel_Haenszel_Procedures_for_Detecting_Differential_Item_Functioning"
          }
        ]
      },
      "I found the seminal work you're looking for. Here are the key findings about the Swaminathan and Rogers 1990 paper on logistic regression for detecting differential item functioning (DIF):\n\n## Publication Details\n\nThe article \"Detecting Differential Item Functioning Using Logistic Regression Procedures\" was published by Hariharan Swaminathan and H. Jane Rogers in the Journal of Educational Measurement, Volume 27, Number 4 (Winter, 1990), pages 361-370.\n\n## Main Contribution\n\nThe work presents a logistic regression model for characterizing differential item functioning (DIF) between two groups. In the logistic regression procedure, an LR is used to model the probability of getting an item correct using a conditioning variable (e.g., observed total test score), a group membership, and an interaction between the conditioning variable and group membership.\n\n## Key Methodological Features\n\nThe paper distinguishes between uniform and nonuniform DIF in terms of the model parameters, develops a statistic for testing the hypothesis of no DIF, and through simulation studies shows that the logistic regression procedure is more powerful than the Mantel-Haenszel procedure for detecting nonuniform DIF and as powerful in detecting uniform DIF.\n\n## Impact and Adoption\n\nThe logistic regression procedure developed by Swaminathan and Rogers has become a popular method for testing differential item functioning (DIF), and Swaminathan and Rogers pointed out that the asymptotic result of an LR may not be a valid indicator of the presence of DIF in small samples."
    ],
    "durationSeconds": 12.657608617999998
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T05:17:36.215Z_

<details><summary>↩ Tool result · `toolu_01MpJjXGJru346PTuqWAtaz8`</summary>

```text
Web search results for query: "IRT identifiability small sample size parameter recovery simulation study 2020 2021 2022 2023 2024"

Links: [{"title":"(PDF) Improving IRT parameter estimates with small sample sizes: Evaluating the efficacy of a new data augmentation technique","url":"https://www.researchgate.net/publication/228787219_Improving_IRT_parameter_estimates_with_small_sample_sizes_Evaluating_the_efficacy_of_a_new_data_augmentation_technique"},{"title":"IRT Item Parameter Recovery With Marginal Maximum ... - ERIC","url":"https://files.eric.ed.gov/fulltext/EJ1084527.pdf"},{"title":"Sample-Size Planning in Item-Response Theory: A Tutorial - Ulrich Schroeders, Timo Gnambs, 2025","url":"https://journals.sagepub.com/doi/10.1177/25152459251314798"},{"title":"Parameter Estimation Accuracy of the Effort-Moderated Item Response Theory Model Under Multiple Assumption Violations - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8072948/"},{"title":"The Impact of Sample Size and Various Other Factors on Estimation of Dichotomous Mixture IRT Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37187690/"},{"title":"Item Parameter Estimation of the 2PL IRT Model With Fixed ...","url":"https://openpublishing.library.umass.edu/pare/article/2104/galley/2511/view/"},{"title":"Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10700496/"},{"title":"Improving IRT parameter estimates with small sample sizes","url":"https://digitalcommons.unl.edu/cgi/viewcontent.cgi?httpsredir=1&article=1075&context=cehsdiss"},{"title":"Comparison of Scale Identification Methods in Mixture IRT ...","url":"https://digitalcommons.wayne.edu/cgi/viewcontent.cgi?article=2971&context=jmasm"},{"title":"On the Identifiability of 3- and 4-Parameter Item Response Theory Models From the Perspective of Knowledge Space Theory - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/38349597/"}]

I've completed the web search for studies on IRT identifiability, small sample sizes, and parameter recovery in simulation studies from 2020-2024. Here are the relevant findings:

## Key Research Findings

**Sample Size Requirements:**
Several textbooks on IRT provide general recommendations on the required sample size for different models, which often culminate in suggesting at least 250 or 500 respondents or having a sufficient ratio of respondents to model parameters, such as 10:1 or 20:1. However, simulation studies examining the minimum required sample size for IRT analyses have consistently shown that these are context-dependent, and IRT can yield accurate parameter estimates with as few as 100 respondents if prior information is incorporated into the estimation or estimation methods that are robust to missing values are employed.

**Small Sample Solutions:**
Hierarchical Bayesian modeling is beneficial when complex models with many parameters of the same type, such as IRT models, are to be estimated with sparse data, with an optimized hierarchical Bayesian two-parameter logistic model showing how to benefit from this approach in small samples. The optimized hierarchical 2PL in the half-Cauchy or Exponential configuration yields unbiased model parameter estimates in small samples of N = 50.

**Mixture IRT Models:**
Dichotomous mixture IRT models required more than 2,000 examinees to be able to obtain stable results as even shorter tests required such large sample sizes for more precise estimates, with this number increasing as the number of latent classes, the degree of separation, and model complexity increased.

**Identifiability Issues:**
There are identifiability concerns when using the empirical histogram method for the 3PL IRT model, as the number of estimated parameters may be very large depending on test length and the number of quadrature points.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "00a892ed-c004-4da0-b728-0c3f8569316a",
  "tool_use_result": {
    "query": "IRT identifiability small sample size parameter recovery simulation study 2020 2021 2022 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_011iedwXavygzHR436zfWorR",
        "content": [
          {
            "title": "(PDF) Improving IRT parameter estimates with small sample sizes: Evaluating the efficacy of a new data augmentation technique",
            "url": "https://www.researchgate.net/publication/228787219_Improving_IRT_parameter_estimates_with_small_sample_sizes_Evaluating_the_efficacy_of_a_new_data_augmentation_technique"
          },
          {
            "title": "IRT Item Parameter Recovery With Marginal Maximum ... - ERIC",
            "url": "https://files.eric.ed.gov/fulltext/EJ1084527.pdf"
          },
          {
            "title": "Sample-Size Planning in Item-Response Theory: A Tutorial - Ulrich Schroeders, Timo Gnambs, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/25152459251314798"
          },
          {
            "title": "Parameter Estimation Accuracy of the Effort-Moderated Item Response Theory Model Under Multiple Assumption Violations - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8072948/"
          },
          {
            "title": "The Impact of Sample Size and Various Other Factors on Estimation of Dichotomous Mixture IRT Models - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/37187690/"
          },
          {
            "title": "Item Parameter Estimation of the 2PL IRT Model With Fixed ...",
            "url": "https://openpublishing.library.umass.edu/pare/article/2104/galley/2511/view/"
          },
          {
            "title": "Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10700496/"
          },
          {
            "title": "Improving IRT parameter estimates with small sample sizes",
            "url": "https://digitalcommons.unl.edu/cgi/viewcontent.cgi?httpsredir=1&article=1075&context=cehsdiss"
          },
          {
            "title": "Comparison of Scale Identification Methods in Mixture IRT ...",
            "url": "https://digitalcommons.wayne.edu/cgi/viewcontent.cgi?article=2971&context=jmasm"
          },
          {
            "title": "On the Identifiability of 3- and 4-Parameter Item Response Theory Models From the Perspective of Knowledge Space Theory - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/38349597/"
          }
        ]
      },
      "I've completed the web search for studies on IRT identifiability, small sample sizes, and parameter recovery in simulation studies from 2020-2024. Here are the relevant findings:\n\n## Key Research Findings\n\n**Sample Size Requirements:**\nSeveral textbooks on IRT provide general recommendations on the required sample size for different models, which often culminate in suggesting at least 250 or 500 respondents or having a sufficient ratio of respondents to model parameters, such as 10:1 or 20:1. However, simulation studies examining the minimum required sample size for IRT analyses have consistently shown that these are context-dependent, and IRT can yield accurate parameter estimates with as few as 100 respondents if prior information is incorporated into the estimation or estimation methods that are robust to missing values are employed.\n\n**Small Sample Solutions:**\nHierarchical Bayesian modeling is beneficial when complex models with many parameters of the same type, such as IRT models, are to be estimated with sparse data, with an optimized hierarchical Bayesian two-parameter logistic model showing how to benefit from this approach in small samples. The optimized hierarchical 2PL in the half-Cauchy or Exponential configuration yields unbiased model parameter estimates in small samples of N = 50.\n\n**Mixture IRT Models:**\nDichotomous mixture IRT models required more than 2,000 examinees to be able to obtain stable results as even shorter tests required such large sample sizes for more precise estimates, with this number increasing as the number of latent classes, the degree of separation, and model complexity increased.\n\n**Identifiability Issues:**\nThere are identifiability concerns when using the empirical histogram method for the 3PL IRT model, as the number of estimated parameters may be very large depending on test length and the number of quadrature points."
    ],
    "durationSeconds": 16.037372972999997
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Good, I found most papers. Let me get more details on specific ones:

1. **Camilli & Shepard (1994)**: "Methods for Identifying Biased Test Items", Sage Publications, 1994. ISBN: 0803944160. Let me search for more details.

2. **Swaminathan & Rogers (1990)**: "Detecting Differential Item Functioning Using Logistic Regression Procedures", Journal of Educational Measurement, Vol 27, No 4, pp 361-370, 1990. DOI from Wiley.
   
Now looking at the more recent LLM papers—I've got Xu et al.'s 2024 work on benchmark leakage from arXiv, and Li and Flanigan's AAAI 2024 paper on task contamination, though I need to verify the full page numbers for the latter.

For the IRT identifiability angle, I found a 2025 tutorial by Schroeders and Gnambs on sample-size planning, plus a 2024 paper on identifiability of 3- and 4-parameter IRT models from PubMed—I should dig deeper into both of these to see how they connect to the broader contamination issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "73510365-ab51-4781-845a-6e4e71b8605d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 23_

找到前 4 篇的基本信息。第 5 篇需要更精确搜索。补充搜索具体元数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "ad21eb46-c9b4-4091-afce-2c444778590a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014z7WzjJtEXpRBk85Z9dye9`</summary>

```json
{
  "query": "Camilli Shepard 1994 \"Methods for Identifying Biased Test Items\" Sage ISBN DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "5ef7960f-034d-40e3-865b-73836b6d22c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GubrXZg8tdu4Kk5szA8k8N`</summary>

```json
{
  "query": "Swaminathan Rogers 1990 \"Detecting Differential Item Functioning\" DOI 10.1111 journal educational measurement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "c79d8602-dac0-4c13-a49e-74d516a369be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015PxyodKHwWGBf4CYxbHRhU`</summary>

```json
{
  "query": "Xu Wang Fan Liu 2024 \"Benchmarking Benchmark Leakage\" arXiv 2404.18824 conference publication ACL EMNLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "e1e86a98-6c9e-4cb8-aa87-19ca2ae9c6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GRc5Dpdq5uUoYG7xsFAJRH`</summary>

```json
{
  "query": "Changmao Li Jeffrey Flanigan 2024 \"Task Contamination\" AAAI volume 38 pages DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "98a8a621-21a9-4260-babc-0192a9b347b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018x7jYMxGBswtT3zrsrwxHH`</summary>

```json
{
  "query": "Schroeders Gnambs 2025 \"Sample-Size Planning in Item Response Theory\" tutorial DOI journal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "4cc6819e-9921-4c9a-bf4f-586fd7b56a6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gag9nqkPcSroB93BSJpyA9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5047,
      "cache_read_input_tokens": 36199,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5047
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

_source line 29 · 2026-05-18T05:17:49.967Z_

<details><summary>↩ Tool result · `toolu_014z7WzjJtEXpRBk85Z9dye9`</summary>

```text
Web search results for query: "Camilli Shepard 1994 "Methods for Identifying Biased Test Items" Sage ISBN DOI"

Links: [{"title":"Methods for Identifying Biased Test Items | SAGE Publications Inc","url":"https://us.sagepub.com/en-us/nam/methods-for-identifying-biased-test-items/book3416"},{"title":"Methods for Identifying Biased Test Items (Measurement Methods for the Social Science) - Camilli, Gregory; Shepard, Lorrie: 9780803944169 - AbeBooks","url":"https://www.abebooks.com/9780803944169/Methods-Identifying-Biased-Test-Items-0803944160/plp"},{"title":"Methods Identifying Biased Test Items by Gregory Camilli Lorrie Shepard - AbeBooks","url":"https://www.abebooks.com/book-search/title/methods-identifying-biased-test-items/author/gregory-camilli-lorrie-shepard/"},{"title":"ERIC - EJ598345 - \"Methods for Identifying Biased Test Items\" by Gregory Camilli and Lorrie A. Shepard., Journal of Educational Measurement, 1996","url":"https://eric.ed.gov/?id=EJ598345"},{"title":"Methods for Identifying Biased Test Items (Measurement Methods for the Social Science #4) (Paperback) | Greenlight Bookstore","url":"https://www.greenlightbookstore.com/book/9780803944169"},{"title":"Methods for Identifying Biased Test Items (Measurement Methods for the Social Science): Camilli, Gregory, Shepard, Lorrie: 9780803944169: Amazon.com: Books","url":"https://www.amazon.com/Methods-Identifying-Biased-Measurement-Science/dp/0803944160"},{"title":"Methods for Identifying Biased Test Items - Gregory Camilli, Lorrie A. Shepard - كتب Google","url":"https://books.google.com.sa/books/about/Methods_for_Identifying_Biased_Test_Item.html?id=kQOFIKjCILEC&redir_esc=y"},{"title":"Methods for Identifying Biased Test Items - Gregory Camilli, Lorrie A. Shepard - Google Books","url":"https://books.google.com/books?id=kQOFIKjCILEC&printsec=copyright"},{"title":"Methods for Identifying Biased Test Items by Gregory Camilli | Goodreads","url":"https://www.goodreads.com/book/show/5940249-methods-for-identifying-biased-test-items"},{"title":"MMSS: Methods for Identifying Biased Test Items | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MMSS:-Methods-for-Identifying-Biased-Test-Items-Camilli-Shepard/4f5593d3f0043b404d3e730aa5defca7152e5a70"}]

Based on the search results, I found information about this publication:

**Book Details:**

Authors: Gregory Camilli and Lorrie A. Shepard
Publisher: Sage Publications, Thousand Oaks, CA
Year: 1994
ISBN 10: 0803944160
ISBN 13: 9780803944169

The book is part of the Measurement Methods for the Social Sciences series and focuses on methods for detecting item bias in testing.

**Regarding the DOI:** The search results do not contain a DOI (Digital Object Identifier) for this book. DOIs were not commonly assigned to books during the 1994 publication period, and this particular publication does not appear to have a DOI in the search results. If you need a DOI, you may want to check academic databases like WorldCat, Google Scholar, or the SAGE Publications website directly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "ba4026de-da38-44c3-af66-2e641b7ec2ec",
  "tool_use_result": {
    "query": "Camilli Shepard 1994 \"Methods for Identifying Biased Test Items\" Sage ISBN DOI",
    "results": [
      {
        "tool_use_id": "srvtoolu_018X9nkVaHeEpwig2MFJ3xWU",
        "content": [
          {
            "title": "Methods for Identifying Biased Test Items | SAGE Publications Inc",
            "url": "https://us.sagepub.com/en-us/nam/methods-for-identifying-biased-test-items/book3416"
          },
          {
            "title": "Methods for Identifying Biased Test Items (Measurement Methods for the Social Science) - Camilli, Gregory; Shepard, Lorrie: 9780803944169 - AbeBooks",
            "url": "https://www.abebooks.com/9780803944169/Methods-Identifying-Biased-Test-Items-0803944160/plp"
          },
          {
            "title": "Methods Identifying Biased Test Items by Gregory Camilli Lorrie Shepard - AbeBooks",
            "url": "https://www.abebooks.com/book-search/title/methods-identifying-biased-test-items/author/gregory-camilli-lorrie-shepard/"
          },
          {
            "title": "ERIC - EJ598345 - \"Methods for Identifying Biased Test Items\" by Gregory Camilli and Lorrie A. Shepard., Journal of Educational Measurement, 1996",
            "url": "https://eric.ed.gov/?id=EJ598345"
          },
          {
            "title": "Methods for Identifying Biased Test Items (Measurement Methods for the Social Science #4) (Paperback) | Greenlight Bookstore",
            "url": "https://www.greenlightbookstore.com/book/9780803944169"
          },
          {
            "title": "Methods for Identifying Biased Test Items (Measurement Methods for the Social Science): Camilli, Gregory, Shepard, Lorrie: 9780803944169: Amazon.com: Books",
            "url": "https://www.amazon.com/Methods-Identifying-Biased-Measurement-Science/dp/0803944160"
          },
          {
            "title": "Methods for Identifying Biased Test Items - Gregory Camilli, Lorrie A. Shepard - كتب Google",
            "url": "https://books.google.com.sa/books/about/Methods_for_Identifying_Biased_Test_Item.html?id=kQOFIKjCILEC&redir_esc=y"
          },
          {
            "title": "Methods for Identifying Biased Test Items - Gregory Camilli, Lorrie A. Shepard - Google Books",
            "url": "https://books.google.com/books?id=kQOFIKjCILEC&printsec=copyright"
          },
          {
            "title": "Methods for Identifying Biased Test Items by Gregory Camilli | Goodreads",
            "url": "https://www.goodreads.com/book/show/5940249-methods-for-identifying-biased-test-items"
          },
          {
            "title": "MMSS: Methods for Identifying Biased Test Items | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/MMSS:-Methods-for-Identifying-Biased-Test-Items-Camilli-Shepard/4f5593d3f0043b404d3e730aa5defca7152e5a70"
          }
        ]
      },
      "Based on the search results, I found information about this publication:\n\n**Book Details:**\n\nAuthors: Gregory Camilli and Lorrie A. Shepard\nPublisher: Sage Publications, Thousand Oaks, CA\nYear: 1994\nISBN 10: 0803944160\nISBN 13: 9780803944169\n\nThe book is part of the Measurement Methods for the Social Sciences series and focuses on methods for detecting item bias in testing.\n\n**Regarding the DOI:** The search results do not contain a DOI (Digital Object Identifier) for this book. DOIs were not commonly assigned to books during the 1994 publication period, and this particular publication does not appear to have a DOI in the search results. If you need a DOI, you may want to check academic databases like WorldCat, Google Scholar, or the SAGE Publications website directly."
    ],
    "durationSeconds": 4.312919825999997
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T05:17:50.756Z_

<details><summary>↩ Tool result · `toolu_01GubrXZg8tdu4Kk5szA8k8N`</summary>

```text
Web search results for query: "Swaminathan Rogers 1990 "Detecting Differential Item Functioning" DOI 10.1111 journal educational measurement"

Links: [{"title":"Detecting Differential Item Functioning Using Logistic Regression Procedures - Swaminathan - 1990 - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x"},{"title":"Detecting Differential Item Functioning Using Logistic ...","url":"https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1745-3984.1990.tb00754.x"},{"title":"Detecting Differential Item Functioning Using the Logistic Regression Procedure in Small Samples - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC5978487/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.1111/j.1745-3984.1990.tb00754.x"},{"title":"Differential Item Functioning | Columbia University Mailman School of Public Health","url":"https://www.publichealth.columbia.edu/research/population-health-methods/differential-item-functioning"},{"title":"Wiley Online Library | Scientific research articles, journals, books, and reference works","url":"https://onlinelibrary.wiley.com/doi/10.1111/j.1745-3984.1990.tb00754.x/abstract"},{"title":"Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning - Li - 2014 - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/jedm.12058"},{"title":"Detecting Differential Item Functioning Using Logistic Regression Procedures on JSTOR","url":"https://www.jstor.org/stable/1434855"},{"title":"Differential Item Functioning: Beyond validity evidence ...","url":"https://www.psicothema.com/pdf/4457.pdf"},{"title":"difR-package: Collection of methods to detect dichotomous and polytomous... in difR: Collection of Methods to Detect Dichotomous and Polytomous Differential Item Functioning (DIF)","url":"https://rdrr.io/cran/difR/man/difR-package.html"}]

I found the article you're looking for! Here are the details:

**Title:** "Detecting Differential Item Functioning Using Logistic Regression Procedures"
**Authors:** Hariharan Swaminathan and H. Jane Rogers
**Journal:** Journal of Educational Measurement, Volume 27, Issue 4
**Year:** 1990
**Pages:** 361-370
**DOI:** 10.1111/j.1745-3984.1990.tb00754.x

The paper presents a logistic regression model for characterizing differential item functioning (DIF) between two groups. The logistic regression (LR) procedure developed in this work has become a popular method for testing differential item functioning (DIF).

The article is available through multiple sources, including the Wiley Online Library and JSTOR, where you can access the full text.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "51ba8c4d-7f73-4250-b778-7a6d3c689844",
  "tool_use_result": {
    "query": "Swaminathan Rogers 1990 \"Detecting Differential Item Functioning\" DOI 10.1111 journal educational measurement",
    "results": [
      {
        "tool_use_id": "srvtoolu_016tghkn5pnPnNJ8qeXCHAsK",
        "content": [
          {
            "title": "Detecting Differential Item Functioning Using Logistic Regression Procedures - Swaminathan - 1990 - Journal of Educational Measurement - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x"
          },
          {
            "title": "Detecting Differential Item Functioning Using Logistic ...",
            "url": "https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1745-3984.1990.tb00754.x"
          },
          {
            "title": "Detecting Differential Item Functioning Using the Logistic Regression Procedure in Small Samples - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5978487/"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?doi=10.1111/j.1745-3984.1990.tb00754.x"
          },
          {
            "title": "Differential Item Functioning | Columbia University Mailman School of Public Health",
            "url": "https://www.publichealth.columbia.edu/research/population-health-methods/differential-item-functioning"
          },
          {
            "title": "Wiley Online Library | Scientific research articles, journals, books, and reference works",
            "url": "https://onlinelibrary.wiley.com/doi/10.1111/j.1745-3984.1990.tb00754.x/abstract"
          },
          {
            "title": "Power and Sample Size Calculations for Logistic Regression Tests for Differential Item Functioning - Li - 2014 - Journal of Educational Measurement - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1111/jedm.12058"
          },
          {
            "title": "Detecting Differential Item Functioning Using Logistic Regression Procedures on JSTOR",
            "url": "https://www.jstor.org/stable/1434855"
          },
          {
            "title": "Differential Item Functioning: Beyond validity evidence ...",
            "url": "https://www.psicothema.com/pdf/4457.pdf"
          },
          {
            "title": "difR-package: Collection of methods to detect dichotomous and polytomous... in difR: Collection of Methods to Detect Dichotomous and Polytomous Differential Item Functioning (DIF)",
            "url": "https://rdrr.io/cran/difR/man/difR-package.html"
          }
        ]
      },
      "I found the article you're looking for! Here are the details:\n\n**Title:** \"Detecting Differential Item Functioning Using Logistic Regression Procedures\"\n**Authors:** Hariharan Swaminathan and H. Jane Rogers\n**Journal:** Journal of Educational Measurement, Volume 27, Issue 4\n**Year:** 1990\n**Pages:** 361-370\n**DOI:** 10.1111/j.1745-3984.1990.tb00754.x\n\nThe paper presents a logistic regression model for characterizing differential item functioning (DIF) between two groups. The logistic regression (LR) procedure developed in this work has become a popular method for testing differential item functioning (DIF).\n\nThe article is available through multiple sources, including the Wiley Online Library and JSTOR, where you can access the full text."
    ],
    "durationSeconds": 4.633600616999996
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-18T05:17:51.651Z_

<details><summary>↩ Tool result · `toolu_01GRc5Dpdq5uUoYG7xsFAJRH`</summary>

```text
Web search results for query: "Changmao Li Jeffrey Flanigan 2024 "Task Contamination" AAAI volume 38 pages DOI"

Links: [{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29808"},{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://www.researchgate.net/publication/379294383_Task_Contamination_Language_Models_May_Not_Be_Few-Shot_Anymore"},{"title":"Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://ojs.aaai.org/index.php/AAAI/article/view/29808/31400"},{"title":"Jeffrey Flanigan's research works | University of California, Santa Cruz and other places","url":"https://www.researchgate.net/scientific-contributions/Jeffrey-Flanigan-70495420"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"dblp: Jeffrey Flanigan","url":"https://dblp.org/pid/75/9768.html"},{"title":"[2312.16337] Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://arxiv.org/abs/2312.16337"},{"title":"Changmao Li","url":"https://scholar.google.com/citations?user=ssw8dCAAAAAJ&hl=en"},{"title":"[2312.16337v1] Task Contamination: Language Models May Not Be Few-Shot Anymore","url":"https://arxiv.org/abs/2312.16337v1"},{"title":"[PDF] Task Contamination: Language Models May Not Be Few-Shot Anymore | Semantic Scholar","url":"https://www.semanticscholar.org/paper/a7b20c1bba14d4cd2b317138496d35d47142d30f"}]

Based on the search results, here is the publication information for the paper:

**Authors:** Changmao Li and Jeffrey Flanigan

**Title:** Task Contamination: Language Models May Not Be Few-Shot Anymore

**Publication:** Proceedings of the AAAI Conference on Artificial Intelligence, Volume 38, Issue 16, Pages 18471-18480

**Year:** 2024

**DOI:** https://doi.org/10.1609/aaai.v38i16.29808


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "bc59c1c4-37f4-4268-8fa6-56e8db2c5f5b",
  "tool_use_result": {
    "query": "Changmao Li Jeffrey Flanigan 2024 \"Task Contamination\" AAAI volume 38 pages DOI",
    "results": [
      {
        "tool_use_id": "srvtoolu_018QeqTQCVGtiUxbiFmtHrRE",
        "content": [
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/29808"
          },
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://www.researchgate.net/publication/379294383_Task_Contamination_Language_Models_May_Not_Be_Few-Shot_Anymore"
          },
          {
            "title": "Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/29808/31400"
          },
          {
            "title": "Jeffrey Flanigan's research works | University of California, Santa Cruz and other places",
            "url": "https://www.researchgate.net/scientific-contributions/Jeffrey-Flanigan-70495420"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "dblp: Jeffrey Flanigan",
            "url": "https://dblp.org/pid/75/9768.html"
          },
          {
            "title": "[2312.16337] Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://arxiv.org/abs/2312.16337"
          },
          {
            "title": "Changmao Li",
            "url": "https://scholar.google.com/citations?user=ssw8dCAAAAAJ&hl=en"
          },
          {
            "title": "[2312.16337v1] Task Contamination: Language Models May Not Be Few-Shot Anymore",
            "url": "https://arxiv.org/abs/2312.16337v1"
          },
          {
            "title": "[PDF] Task Contamination: Language Models May Not Be Few-Shot Anymore | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/a7b20c1bba14d4cd2b317138496d35d47142d30f"
          }
        ]
      },
      "Based on the search results, here is the publication information for the paper:\n\n**Authors:** Changmao Li and Jeffrey Flanigan\n\n**Title:** Task Contamination: Language Models May Not Be Few-Shot Anymore\n\n**Publication:** Proceedings of the AAAI Conference on Artificial Intelligence, Volume 38, Issue 16, Pages 18471-18480\n\n**Year:** 2024\n\n**DOI:** https://doi.org/10.1609/aaai.v38i16.29808"
    ],
    "durationSeconds": 4.0915886489999975
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-18T05:17:53.736Z_

<details><summary>↩ Tool result · `toolu_015PxyodKHwWGBf4CYxbHRhU`</summary>

```text
Web search results for query: "Xu Wang Fan Liu 2024 "Benchmarking Benchmark Leakage" arXiv 2404.18824 conference publication ACL EMNLP"

Links: [{"title":"[2404.18824] Benchmarking Benchmark Leakage in Large Language Models","url":"https://arxiv.org/abs/2404.18824"},{"title":"[PDF] Benchmarking Benchmark Leakage in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Benchmarking-Benchmark-Leakage-in-Large-Language-Xu-Wang/34c0ac6c012f524e30f083b81b148f65c41c221e"},{"title":"[2404.18824v1] Benchmarking Benchmark Leakage in Large Language Models","url":"http://arxiv.org/abs/2404.18824v1"},{"title":"Benchmarking Benchmark Leakage in Large Language Models","url":"https://arxiv.org/html/2404.18824v1"},{"title":"GitHub - GAIR-NLP/benbench: Benchmarking Benchmark Leakage in Large Language Models · GitHub","url":"https://github.com/GAIR-NLP/benbench"},{"title":"Benchmarking Benchmark Leakage in Large Langauge Models","url":"https://gair-nlp.github.io/benbench/"},{"title":"Generative AI Research Benchmarking Benchmark Leakage in Large Language Models","url":"https://arxiv.org/pdf/2404.18824"},{"title":"Training on the Benchmark Is Not All You Need","url":"https://arxiv.org/html/2409.01790v1"},{"title":"Both Text and Images Leaked! A Systematic Analysis of Multimodal LLM Data Contamination","url":"https://arxiv.org/html/2411.03823v1"},{"title":"Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation","url":"https://arxiv.org/html/2505.24263v1"}]

Based on my search results, I found comprehensive information about this paper:

## Paper Information

The paper "Benchmarking Benchmark Leakage in Large Language Models" was submitted to arXiv on April 29, 2024 with identifier 2404.18824, authored by Ruijie Xu, Zengzhi Wang, Run-Ze Fan, and Pengfei Liu.

## Overview

The paper addresses benchmark dataset leakage in Large Language Models (LLMs) and introduces a detection pipeline utilizing Perplexity and N-gram accuracy to identify potential data leakages.

## Key Findings

By analyzing 31 LLMs under the context of mathematical reasoning, the researchers reveal substantial instances of training even test set misuse, resulting in potentially unfair comparisons.

## Contribution

The paper proposes the "Benchmark Transparency Card" to encourage clear documentation of benchmark utilization.

## Conference Publication Note

Based on the search results, this paper was published as an arXiv preprint in April 2024. The search results do not indicate publication at ACL or EMNLP conferences—it appears to be available as an arXiv preprint rather than at a specific conference venue.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "a284a8b1-8798-4509-ad3f-20605e5a5b28",
  "tool_use_result": {
    "query": "Xu Wang Fan Liu 2024 \"Benchmarking Benchmark Leakage\" arXiv 2404.18824 conference publication ACL EMNLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DBLT1dS8ZzoxH2pgHijzS3",
        "content": [
          {
            "title": "[2404.18824] Benchmarking Benchmark Leakage in Large Language Models",
            "url": "https://arxiv.org/abs/2404.18824"
          },
          {
            "title": "[PDF] Benchmarking Benchmark Leakage in Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Benchmarking-Benchmark-Leakage-in-Large-Language-Xu-Wang/34c0ac6c012f524e30f083b81b148f65c41c221e"
          },
          {
            "title": "[2404.18824v1] Benchmarking Benchmark Leakage in Large Language Models",
            "url": "http://arxiv.org/abs/2404.18824v1"
          },
          {
            "title": "Benchmarking Benchmark Leakage in Large Language Models",
            "url": "https://arxiv.org/html/2404.18824v1"
          },
          {
            "title": "GitHub - GAIR-NLP/benbench: Benchmarking Benchmark Leakage in Large Language Models · GitHub",
            "url": "https://github.com/GAIR-NLP/benbench"
          },
          {
            "title": "Benchmarking Benchmark Leakage in Large Langauge Models",
            "url": "https://gair-nlp.github.io/benbench/"
          },
          {
            "title": "Generative AI Research Benchmarking Benchmark Leakage in Large Language Models",
            "url": "https://arxiv.org/pdf/2404.18824"
          },
          {
            "title": "Training on the Benchmark Is Not All You Need",
            "url": "https://arxiv.org/html/2409.01790v1"
          },
          {
            "title": "Both Text and Images Leaked! A Systematic Analysis of Multimodal LLM Data Contamination",
            "url": "https://arxiv.org/html/2411.03823v1"
          },
          {
            "title": "Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation",
            "url": "https://arxiv.org/html/2505.24263v1"
          }
        ]
      },
      "Based on my search results, I found comprehensive information about this paper:\n\n## Paper Information\n\nThe paper \"Benchmarking Benchmark Leakage in Large Language Models\" was submitted to arXiv on April 29, 2024 with identifier 2404.18824, authored by Ruijie Xu, Zengzhi Wang, Run-Ze Fan, and Pengfei Liu.\n\n## Overview\n\nThe paper addresses benchmark dataset leakage in Large Language Models (LLMs) and introduces a detection pipeline utilizing Perplexity and N-gram accuracy to identify potential data leakages.\n\n## Key Findings\n\nBy analyzing 31 LLMs under the context of mathematical reasoning, the researchers reveal substantial instances of training even test set misuse, resulting in potentially unfair comparisons.\n\n## Contribution\n\nThe paper proposes the \"Benchmark Transparency Card\" to encourage clear documentation of benchmark utilization.\n\n## Conference Publication Note\n\nBased on the search results, this paper was published as an arXiv preprint in April 2024. The search results do not indicate publication at ACL or EMNLP conferences—it appears to be available as an arXiv preprint rather than at a specific conference venue."
    ],
    "durationSeconds": 6.593616980999999
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T05:17:55.265Z_

<details><summary>↩ Tool result · `toolu_018x7jYMxGBswtT3zrsrwxHH`</summary>

```text
Web search results for query: "Schroeders Gnambs 2025 "Sample-Size Planning in Item Response Theory" tutorial DOI journal"

Links: [{"title":"Sample-Size Planning in Item-Response Theory: A Tutorial - Ulrich Schroeders, Timo Gnambs, 2025","url":"https://journals.sagepub.com/doi/10.1177/25152459251314798"},{"title":"Sample-Size Planning in Item-Response Theory - Timo Gnambs","url":"https://timo.gnambs.at/sites/default/files/gnambstimo/publications/schroeders2025.pdf"},{"title":"(PDF) Sample Size Planning in Item Response Theory: A Tutorial","url":"https://www.researchgate.net/publication/382541958_Sample_Size_Planning_in_Item_Response_Theory_A_Tutorial"},{"title":"irtsim: Monte Carlo Simulation-Based Sample-Size Planning for Item Response Theory","url":"https://cran.r-project.org/web/packages/irtsim/index.html"},{"title":"Sample-size planning in item-response theory: A tutorial.","url":"https://psycnet.apa.org/record/2026-02467-001"},{"title":"Method-Toolbox | - Ulrich Schroeders","url":"https://ulrich-schroeders.de/fixed/method-toolbox/"},{"title":"OSF | Sample Size Planning in Item Response Theory: A Tutorial","url":"https://osf.io/9xq7r/"},{"title":"Timo GNAMBS | Head of Research Unit | Doctor of Psychology | Leibniz Institute for Educational Trajectories, Bamberg | Educational Measurement | Research profile","url":"https://www.researchgate.net/profile/Timo-Gnambs"},{"title":"Sample Size and Item Calibration or Person Measure Stability","url":"https://www.rasch.org/rmt/rmt74m.htm"},{"title":"Sample-Size Planning in Item-Response Theory: A Tutorial","url":"https://www.researchgate.net/publication/389286489_Sample-Size_Planning_in_Item-Response_Theory_A_Tutorial"}]

Based on the search results, I found the publication information you're looking for:

**Publication Details:**

The tutorial is authored by Ulrich Schroeders and Timo Gnambs, and it was published in 2025.

**Journal and DOI:**

The article is published in Advances in Methods and Practices in Psychological Science (based on the SAGE publishing URL), with the DOI: 10.1177/25152459251314798.

**Content Overview:**

The main part of this tutorial provides a comprehensive, step-by-step guide to Monte Carlo simulation-based sample-size estimation in IRT, which is essential for obtaining precise estimates of item and person parameters, structural effects, and model fit. The tutorial highlights 10 key decisions, organized into four areas: (a) determining the data-generation model, (b) defining the test design and the process of missing values, (c) selecting the IRT model and parameters of interest, and (d) setting up and running the Monte Carlo simulation, with the procedure illustrated with examples from educational, personality, and clinical psychology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "105e5ff4-79bf-42cd-bc1d-c197f875fe61",
  "tool_use_result": {
    "query": "Schroeders Gnambs 2025 \"Sample-Size Planning in Item Response Theory\" tutorial DOI journal",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xei1W3hHEELSM4jcwHToXq",
        "content": [
          {
            "title": "Sample-Size Planning in Item-Response Theory: A Tutorial - Ulrich Schroeders, Timo Gnambs, 2025",
            "url": "https://journals.sagepub.com/doi/10.1177/25152459251314798"
          },
          {
            "title": "Sample-Size Planning in Item-Response Theory - Timo Gnambs",
            "url": "https://timo.gnambs.at/sites/default/files/gnambstimo/publications/schroeders2025.pdf"
          },
          {
            "title": "(PDF) Sample Size Planning in Item Response Theory: A Tutorial",
            "url": "https://www.researchgate.net/publication/382541958_Sample_Size_Planning_in_Item_Response_Theory_A_Tutorial"
          },
          {
            "title": "irtsim: Monte Carlo Simulation-Based Sample-Size Planning for Item Response Theory",
            "url": "https://cran.r-project.org/web/packages/irtsim/index.html"
          },
          {
            "title": "Sample-size planning in item-response theory: A tutorial.",
            "url": "https://psycnet.apa.org/record/2026-02467-001"
          },
          {
            "title": "Method-Toolbox | - Ulrich Schroeders",
            "url": "https://ulrich-schroeders.de/fixed/method-toolbox/"
          },
          {
            "title": "OSF | Sample Size Planning in Item Response Theory: A Tutorial",
            "url": "https://osf.io/9xq7r/"
          },
          {
            "title": "Timo GNAMBS | Head of Research Unit | Doctor of Psychology | Leibniz Institute for Educational Trajectories, Bamberg | Educational Measurement | Research profile",
            "url": "https://www.researchgate.net/profile/Timo-Gnambs"
          },
          {
            "title": "Sample Size and Item Calibration or Person Measure Stability",
            "url": "https://www.rasch.org/rmt/rmt74m.htm"
          },
          {
            "title": "Sample-Size Planning in Item-Response Theory: A Tutorial",
            "url": "https://www.researchgate.net/publication/389286489_Sample-Size_Planning_in_Item-Response_Theory_A_Tutorial"
          }
        ]
      },
      "Based on the search results, I found the publication information you're looking for:\n\n**Publication Details:**\n\nThe tutorial is authored by Ulrich Schroeders and Timo Gnambs, and it was published in 2025.\n\n**Journal and DOI:**\n\nThe article is published in Advances in Methods and Practices in Psychological Science (based on the SAGE publishing URL), with the DOI: 10.1177/25152459251314798.\n\n**Content Overview:**\n\nThe main part of this tutorial provides a comprehensive, step-by-step guide to Monte Carlo simulation-based sample-size estimation in IRT, which is essential for obtaining precise estimates of item and person parameters, structural effects, and model fit. The tutorial highlights 10 key decisions, organized into four areas: (a) determining the data-generation model, (b) defining the test design and the process of missing values, (c) selecting the IRT model and parameters of interest, and (d) setting up and running the Monte Carlo simulation, with the procedure illustrated with examples from educational, personality, and clinical psychology."
    ],
    "durationSeconds": 7.019077543
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also check if there's a more specific paper for #5 about IRT identifiability with small J (small number of examinees). The Schroeders & Gnambs (2025) paper is about sample-size planning in IRT, which is relevant but not specifically about identifiability. Let me also check the other paper I noticed: "On the Identifiability of 3- and 4-Parameter Item Response Theory Models" from PubMed 2024. But actually, the task says "IRT identifiability with small J" - the Schroeders & Gnambs 2025 tutorial is a good fit since it covers sample-size planning for IRT parameter recovery. Let me also check if there's a more specific paper about identifiability issues.


I should look more carefully at the PubMed paper on 3PL and 4PL identifiability since that directly addresses the C008 constraint issue with 4PL models. The task specifically mentions Roberts et al. (2025) or similar literature on IRT identifiability with small J, and the Schroeders & Gnambs paper on sample-size planning is related but may not be the exact match needed. The core issue here is parameter recovery and identifiability when the number of examinees is very small, particularly for the 4PL model's c and d parameters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "70ebc996-7df0-4224-ad32-ccaf71865802",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP3z65rXMNy5ik4zufH9i8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5091,
      "cache_read_input_tokens": 41246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5091
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

Schroeders & Gnambs 2025 适合作为 IRT 小样本文献。现在整理所有信息并写入 bib 文件。

汇总：
1. **Camilli & Shepard (1994)**: book, Sage, ISBN 978-0-8039-4416-9, no DOI
2. **Swaminathan & Rogers (1990)**: Journal of Educational Measurement, 27(4), 361–370, DOI: 10.1111/j.1745-3984.1990.tb00754.x
3. **Xu et al. (2024)**: arXiv:2404.18824, preprint
4. **Li & Flanigan (2024)**: AAAI 2024, Vol 38(16), pp 18471–18480, DOI: 10.1609/aaai.v38i16.29808
5. **Schroeders & Gnambs (2025)**: Advances in Methods and Practices in Psychological Science, DOI: 10.1177/25152459251314798

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "f7c0e8c2-2f37-4033-b311-2d92753c368e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP3z65rXMNy5ik4zufH9i8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5091,
      "cache_read_input_tokens": 41246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5091
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LGBjQy7QWSnYya8KH1RnB4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
  "old_string": "@article{singh2024evaluation,\n  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},\n  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2411.03923},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2411.03923}\n}",
  "new_string": "@article{singh2024evaluation,\n  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},\n  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2411.03923},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2411.03923}\n}\n\n% --- Added references (SF8) ---\n\n@book{camilli_1994_dif,\n  author    = {Camilli, Gregory and Shepard, Lorrie A.},\n  title     = {Methods for Identifying Biased Test Items},\n  series    = {Measurement Methods for the Social Sciences},\n  publisher = {Sage Publications},\n  year      = {1994},\n  address   = {Thousand Oaks, CA},\n  isbn      = {978-0-8039-4416-9}\n}\n\n@article{swaminathan_1990_dif,\n  author  = {Swaminathan, Hariharan and Rogers, H. Jane},\n  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},\n  journal = {Journal of Educational Measurement},\n  volume  = {27},\n  number  = {4},\n  pages   = {361--370},\n  year    = {1990},\n  doi     = {10.1111/j.1745-3984.1990.tb00754.x}\n}\n\n@article{xu_2024_leakage,\n  author        = {Xu, Ruijie and Wang, Zengzhi and Fan, Run-Ze and Liu, Pengfei},\n  title         = {Benchmarking Benchmark Leakage in Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2404.18824},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2404.18824}\n}\n\n@inproceedings{li_2024_task_contamination,\n  author    = {Li, Changmao and Flanigan, Jeffrey},\n  title     = {Task Contamination: Language Models May Not Be Few-Shot Anymore},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  volume    = {38},\n  number    = {16},\n  pages     = {18471--18480},\n  year      = {2024},\n  doi       = {10.1609/aaai.v38i16.29808}\n}\n\n@article{schroeders_2025_irt_sample_size,\n  author  = {Schroeders, Ulrich and Gnambs, Timo},\n  title   = {Sample-Size Planning in Item-Response Theory: A Tutorial},\n  journal = {Advances in Methods and Practices in Psychological Science},\n  year    = {2025},\n  doi     = {10.1177/25152459251314798}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "666540d9-05c4-4c75-9741-903b1ccb7f91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YP3z65rXMNy5ik4zufH9i8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5091,
      "cache_read_input_tokens": 41246,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5091
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

_source line 37 · 2026-05-18T05:18:24.570Z_

<details><summary>↩ Tool result · `toolu_01LGBjQy7QWSnYya8KH1RnB4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "37d747e0-1d79-47f4-a727-e1b18d330849",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/docs/paper/references.bib",
    "oldString": "@article{singh2024evaluation,\n  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},\n  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2411.03923},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2411.03923}\n}",
    "newString": "@article{singh2024evaluation,\n  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},\n  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2411.03923},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2411.03923}\n}\n\n% --- Added references (SF8) ---\n\n@book{camilli_1994_dif,\n  author    = {Camilli, Gregory and Shepard, Lorrie A.},\n  title     = {Methods for Identifying Biased Test Items},\n  series    = {Measurement Methods for the Social Sciences},\n  publisher = {Sage Publications},\n  year      = {1994},\n  address   = {Thousand Oaks, CA},\n  isbn      = {978-0-8039-4416-9}\n}\n\n@article{swaminathan_1990_dif,\n  author  = {Swaminathan, Hariharan and Rogers, H. Jane},\n  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},\n  journal = {Journal of Educational Measurement},\n  volume  = {27},\n  number  = {4},\n  pages   = {361--370},\n  year    = {1990},\n  doi     = {10.1111/j.1745-3984.1990.tb00754.x}\n}\n\n@article{xu_2024_leakage,\n  author        = {Xu, Ruijie and Wang, Zengzhi and Fan, Run-Ze and Liu, Pengfei},\n  title         = {Benchmarking Benchmark Leakage in Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2404.18824},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2404.18824}\n}\n\n@inproceedings{li_2024_task_contamination,\n  author    = {Li, Changmao and Flanigan, Jeffrey},\n  title     = {Task Contamination: Language Models May Not Be Few-Shot Anymore},\n  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},\n  volume    = {38},\n  number    = {16},\n  pages     = {18471--18480},\n  year      = {2024},\n  doi       = {10.1609/aaai.v38i16.29808}\n}\n\n@article{schroeders_2025_irt_sample_size,\n  author  = {Schroeders, Ulrich and Gnambs, Timo},\n  title   = {Sample-Size Planning in Item-Response Theory: A Tutorial},\n  journal = {Advances in Methods and Practices in Psychological Science},\n  year    = {2025},\n  doi     = {10.1177/25152459251314798}\n}",
    "originalFile": "% ============================================================\n% Literature Map Entries (keys from literature_map.yaml ids)\n% ============================================================\n\n@inproceedings{carlini_2021_extracting,\n  author    = {Carlini, Nicholas and Tramer, Florian and Wallace, Eric and Jagielski, Matthew and Herbert-Voss, Ariel and Lee, Katherine and Roberts, Adam and Brown, Tom and Song, Dawn and Erlingsson, Ulfar and Oprea, Alina and Raffel, Colin},\n  title     = {Extracting Training Data from Large Language Models},\n  booktitle = {Proceedings of the 30th USENIX Security Symposium},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2012.07805}\n}\n\n@inproceedings{choi_2025_kds,\n  author    = {Choi, Hyeong Kyu and Khanov, Maxim and Wei, Hongxin and Li, Yixuan},\n  title     = {How Contaminated Is Your Benchmark? Measuring Dataset Leakage in Large Language Models with Kernel Divergence},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.00678}\n}\n\n@inproceedings{cormack_2009_rrf,\n  author    = {Cormack, Gordon V. and Clarke, Charles L. A. and Buettcher, Stefan},\n  title     = {Reciprocal Rank Fusion Outperforms {Condorcet} and Individual Rank Learning Methods},\n  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},\n  pages     = {758--759},\n  year      = {2009},\n  publisher = {ACM},\n  url       = {https://dl.acm.org/doi/10.1145/1571941.1572114}\n}\n\n@book{deboeck_2004_explanatory_irt,\n  author    = {De Boeck, Paul and Wilson, Mark},\n  title     = {Explanatory Item Response Models: A Generalized Linear and Nonlinear Approach},\n  publisher = {Springer},\n  year      = {2004},\n  address   = {New York},\n  url       = {https://link.springer.com/book/10.1007/978-1-4757-3990-9}\n}\n\n@inproceedings{deng_2024_tsguessing,\n  author    = {Deng, Chunyuan and Zhao, Yilun and Tang, Xiangru and Gerstein, Mark and Cohan, Arman},\n  title     = {Investigating Data Contamination in Modern Benchmarks for Large Language Models},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2311.09783}\n}\n\n@inproceedings{dong_2024_cdd,\n  author    = {Dong, Yihong and Jiang, Xue and Liu, Huanyu and Jin, Zhi and Gu, Bin and Yang, Mengfei and Li, Ge},\n  title     = {Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2024},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.15938}\n}\n\n@incollection{eckerly_2017_item_compromise,\n  author    = {Eckerly, Carol A.},\n  title     = {Detecting Preknowledge and Item Compromise: Understanding the Status Quo},\n  booktitle = {Handbook of Quantitative Methods for Detecting Cheating on Tests},\n  editor    = {Cizek, Gregory J. and Wollack, James A.},\n  publisher = {Routledge},\n  year      = {2017},\n  chapter   = {5},\n  doi       = {10.4324/9781315743097-5}\n}\n\n@inproceedings{golchin_2024_time_travel,\n  author    = {Golchin, Shahriar and Surdeanu, Mihai},\n  title     = {Time Travel in {LLMs}: Tracing Data Contamination in Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.08493}\n}\n\n@inproceedings{guo_2017_calibration,\n  author    = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  title     = {On Calibration of Modern Neural Networks},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning (ICML)},\n  pages     = {1321--1330},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{habba_2025_growing_pains,\n  author        = {Habba, Eliya and Itzhak, Itay and Yehudai, Asaf and Perlitz, Yotam and Bandel, Elron and Shmueli-Scheuer, Michal and Choshen, Leshem and Stanovsky, Gabriel},\n  title         = {Growing Pains: Extensible and Efficient {LLM} Benchmarking Via Fixed Parameter Calibration},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2604.12843},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2604.12843}\n}\n\n@book{holland_1993_dif,\n  author    = {Holland, Paul W. and Wainer, Howard},\n  title     = {Differential Item Functioning},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1993},\n  address   = {Hillsdale, NJ}\n}\n\n@inproceedings{lalor_2024_irt_nlp,\n  author    = {Lalor, John P. and Rodriguez, Pedro and Sedoc, Jo\\~{a}o and Hernandez-Orallo, Jose},\n  title     = {Item Response Theory for Natural Language Processing},\n  booktitle = {Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics: Tutorial Abstracts (EACL)},\n  year      = {2024},\n  url       = {https://aclanthology.org/2024.eacl-tutorials.2/}\n}\n\n@article{li_2024_atlas,\n  author        = {Li, Peiyu and Tang, Xiuxiu and Chen, Si and Cheng, Ying and Metoyer, Ronald and Hua, Ting and Chawla, Nitesh V.},\n  title         = {Adaptive Testing for {LLM} Evaluation: A Psychometric Alternative to Static Benchmarks},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2511.04689},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2511.04689}\n}\n\n@inproceedings{xu2025dcr,\n  author    = {Xu, Cheng and Yan, Nan and Guan, Shuhao and Jin, Changhong and Mei, Yuke and Guo, Yibing and Kechadi, Tahar},\n  title     = {{DCR}: Quantifying Data Contamination in {LLMs} Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {23002--23020},\n  year      = {2025},\n  eprint    = {2507.11405},\n  archiveprefix = {arXiv},\n  url       = {https://aclanthology.org/2025.emnlp-main.1173/}\n}\n\n@article{luettgau_2025_hibayes,\n  author        = {Luettgau, Lennart and Coppock, Harry and Dubois, Magda and Summerfield, Christopher and Ududec, Cozmin},\n  title         = {{HiBayES}: A Hierarchical {Bayesian} Modeling Framework for {AI} Evaluation Statistics},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2505.05602},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2505.05602}\n}\n\n@inproceedings{polo_2024_tinybenchmarks,\n  author    = {Polo, Felipe Maia and Weber, Lucas and Choshen, Leshem and Sun, Yuekai and Xu, Gongjun and Yurochkin, Mikhail},\n  title     = {{tinyBenchmarks}: Evaluating {LLMs} with Fewer Examples},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14992}\n}\n\n@article{sanmartin_2009_irt,\n  author  = {San Mart\\'{i}n, Ernesto and Del Pino, Guido and De Boeck, Paul},\n  title   = {Consequential Validity and Item Response Theory},\n  journal = {Psychometrika},\n  volume  = {74},\n  number  = {2},\n  pages   = {349--367},\n  year    = {2009}\n}\n\n@inproceedings{shi_2023_minkprob,\n  author    = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  title     = {Detecting Pretraining Data from Large Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2310.16789}\n}\n\n@inproceedings{shokri_2017_mia,\n  author    = {Shokri, Reza and Stronati, Marco and Song, Congzheng and Shmatikov, Vitaly},\n  title     = {Membership Inference Attacks Against Machine Learning Models},\n  booktitle = {Proceedings of the 2017 IEEE Symposium on Security and Privacy (S\\&P)},\n  year      = {2017},\n  url       = {https://arxiv.org/abs/1610.05820}\n}\n\n@article{sinharay_2017_preknowledge,\n  author  = {Sinharay, Sandip},\n  title   = {Detection of Item Preknowledge Using Likelihood Ratio Test and Score Test},\n  journal = {Journal of Educational and Behavioral Statistics},\n  volume  = {42},\n  number  = {1},\n  year    = {2017},\n  url     = {https://pubmed.ncbi.nlm.nih.gov/29881099/}\n}\n\n@article{tao2025detecting,\n  author        = {Tao, Yongding and Wang, Tian and Dong, Yihong and Liu, Huanyu and Zhang, Kechi and Hu, Xiaolong and Li, Ge},\n  title         = {Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models},\n  journal       = {arXiv preprint},\n  year          = {2025},\n  eprint        = {2510.09259},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2510.09259}\n}\n\n@inproceedings{zhang_2024_gsm1k,\n  author    = {Zhang, Hugh Mee and Da, Jeff and Lee, Nayeon and Zheng, Lianmin and Sheng, Ying and Gonzalez, Joseph E. and Stoica, Ion},\n  title     = {A Careful Examination of Large Language Model Performance on Grade School Arithmetic},\n  booktitle = {arXiv preprint},\n  year      = {2024},\n  eprint    = {2405.00332},\n  url       = {https://arxiv.org/abs/2405.00332}\n}\n\n@inproceedings{zhang_2024_minkpp,\n  author    = {Zhang, Jingyang and Sun, Jingwei and Yeats, Eric and Ouyang, Yang and Kuo, Martin and Zhang, Jianyi and Yang, Hao and Li, Hai},\n  title     = {{Min-K\\%++}: Improved Baseline for Detecting Pre-Training Data from Large Language Models},\n  booktitle = {Proceedings of the 13th International Conference on Learning Representations (ICLR)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2404.02936}\n}\n\n@inproceedings{zhou_2025_psnirt,\n  author    = {Zhou, Hongli and Wang, Hainiu and Ye, Qingyao and Peng, Nanyun},\n  title     = {Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory},\n  booktitle = {Proceedings of the 40th AAAI Conference on Artificial Intelligence},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2505.15055}\n}\n\n% ============================================================\n% Existing Entries (preserved for backward compatibility)\n% ============================================================\n\n% --- Missing References (added D138) ---\n\n@book{lord_1980_irt,\n  author    = {Lord, Frederic M.},\n  title     = {Applications of Item Response Theory to Practical Testing Problems},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1980},\n  address   = {Hillsdale, NJ},\n  isbn      = {978-0-89859-006-7},\n  doi       = {10.4324/9780203056615}\n}\n\n@book{hambleton_1991_irt,\n  author    = {Hambleton, Ronald K. and Swaminathan, Hariharan and Rogers, H. Jane},\n  title     = {Fundamentals of Item Response Theory},\n  publisher = {Sage Publications},\n  year      = {1991},\n  address   = {Newbury Park, CA},\n  isbn      = {978-0-8039-3647-8}\n}\n\n@article{liang_2023_helm,\n  author  = {Liang, Percy and Bommasani, Rishi and Lee, Tony and Tsipras, Dimitris and Soylu, Dilara and Yasunaga, Michihiro and Zhang, Yian and Narayanan, Deepak and Wu, Yuhuai and Kumar, Ananya and Newman, Benjamin and Yuan, Binhang and Yan, Bobby and Zhang, Ce and Cosgrove, Christian and Manning, Christopher D. and R\\'{e}, Christopher and Acosta-Navas, Diana and Hudson, Drew A. and Zelikman, Eric and Durmus, Esin and Ladhak, Faisal and Rong, Frieda and Ren, Hongyu and Yao, Huaxiu and Wang, Jue and Santhanam, Keshav and Orr, Laurel and Zheng, Lucia and Y\\\"{u}ksekg\\\"{o}n\\\"{u}l, Mert and Suzgun, Mirac and Kim, Nathan and Guha, Neel and Chatterji, Niladri S. and Khattab, Omar and Henderson, Peter and Huang, Qian and Chi, Ryan A. and Xie, Sang Michael and Santurkar, Shibani and Ganguli, Surya and Hashimoto, Tatsunori and Icard, Thomas and Zhang, Tianyi and Chaudhary, Vishrav and Wang, William and Li, Xuechen and Mai, Yifan and Zhang, Yuhui and Koreeda, Yuta},\n  title   = {Holistic Evaluation of Language Models},\n  journal = {Annals of the New York Academy of Sciences},\n  volume  = {1525},\n  number  = {1},\n  pages   = {140--146},\n  year    = {2023},\n  doi     = {10.1111/nyas.15007}\n}\n\n@inproceedings{magar_2022_contamination,\n  author    = {Magar, Inbal and Schwartz, Roy},\n  title     = {Data Contamination: From Memorization to Exploitation},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages     = {157--165},\n  year      = {2022},\n  address   = {Dublin, Ireland},\n  publisher = {Association for Computational Linguistics},\n  doi       = {10.18653/v1/2022.acl-short.18}\n}\n\n% --- Core Methodology ---\n\n@article{kadavath2022,\n  author        = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  title         = {Language Models (Mostly) Know What They Know},\n  journal       = {arXiv preprint},\n  year          = {2022},\n  eprint        = {2207.05221},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2207.05221}\n}\n\n% --- Bayesian Inference & Diagnostics ---\n\n@article{hoffman2014,\n  author  = {Hoffman, Matthew D. and Gelman, Andrew},\n  title   = {The {No-U-Turn} Sampler: Adaptively Setting Path Lengths in {Hamiltonian Monte Carlo}},\n  journal = {Journal of Machine Learning Research},\n  volume  = {15},\n  number  = {47},\n  pages   = {1593--1623},\n  year    = {2014}\n}\n\n@article{carpenter2017,\n  author  = {Carpenter, Bob and Gelman, Andrew and Hoffman, Matthew D. and Lee, Daniel and Goodrich, Ben and Betancourt, Michael and Brubaker, Marcus and Guo, Jiqiang and Li, Peter and Riddell, Allen},\n  title   = {Stan: A Probabilistic Programming Language},\n  journal = {Journal of Statistical Software},\n  volume  = {76},\n  number  = {1},\n  pages   = {1--32},\n  year    = {2017}\n}\n\n% --- Contamination Detection Methods ---\n\n@inproceedings{dekoninck2024constat,\n  author    = {Dekoninck, Jasper and M\\\"{u}ller, Mark Niklas and Vechev, Martin},\n  title     = {{ConStat}: Performance-Based Contamination Detection in Large Language Models},\n  booktitle = {Advances in Neural Information Processing Systems 37 (NeurIPS)},\n  year      = {2024}\n}\n\n@inproceedings{oren2024proving,\n  author    = {Oren, Yonatan and Meister, Nicole and Chatterji, Niladri and Ladhak, Faisal and Hashimoto, Tatsunori},\n  title     = {Proving Test Set Contamination in Black Box Language Models},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024}\n}\n\n% --- Contamination Analysis & Mitigation ---\n\n@inproceedings{sun2025emperor,\n  author    = {Sun, Yifan and Wang, Han and Li, Dongbai and Wang, Gang and Zhang, Huan},\n  title     = {The Emperor's New Clothes: Systematic Evaluation of Contamination Mitigation Strategies for Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  note      = {arXiv:2503.16402}\n}\n\n@inproceedings{kocyigit2025impact,\n  author        = {Kocyigit, Murat Yildirim and Yildirim, Ekin Akyurek},\n  title         = {The Impact of Post-training on Data Contamination Detection in Large Language Models},\n  booktitle     = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year          = {2025},\n  eprint        = {2601.06103},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{zhang2025forget,\n  author    = {Zhang, Yiming and Wang, Yuxin and Dong, Hao and Li, Jiashi},\n  title     = {How Much Can We Forget? Examining Decontamination Effectiveness in Large Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025}\n}\n\n% --- IRT for LLM Evaluation ---\n\n% --- Score Adjustment & Decontamination ---\n\n@inproceedings{yang2024inference,\n  author    = {Yang, Shuo and Wei, Xin and Shi, Weicheng},\n  title     = {Inference-Time Decontamination of Large Language Models for Benchmark Evaluation},\n  booktitle = {Findings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP Findings)},\n  year      = {2024}\n}\n\n% --- Benchmarking ---\n\n@inproceedings{hendrycks2021mmlu,\n  author    = {Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob},\n  title     = {Measuring Massive Multitask Language Understanding},\n  booktitle = {Proceedings of the 9th International Conference on Learning Representations (ICLR)},\n  year      = {2021}\n}\n\n@article{cobbe2021gsm8k,\n  author        = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  title         = {Training Verifiers to Solve Math Word Problems},\n  journal       = {arXiv preprint},\n  year          = {2021},\n  eprint        = {2110.14168},\n  archiveprefix = {arXiv}\n}\n\n@article{clark2018arc,\n  author    = {Clark, Peter and Cowhey, Isaac and Etzioni, Oren and Khot, Tushar and Sabharwal, Ashish and Schoenick, Carissa and Tafjord, Oyvind},\n  title     = {Think you have Solved Question Answering? {Try ARC}, the {AI2} Reasoning Challenge},\n  journal   = {arXiv preprint},\n  year      = {2018},\n  eprint    = {1803.05457},\n  archiveprefix = {arXiv}\n}\n\n@article{chang2025benchmarking,\n  author    = {Chang, Yupeng and Wang, Xu and Wang, Jindong and Wu, Yuan and Yang, Linyi and Zhu, Kaijie and Chen, Hao and Yi, Xiaoyuan and Wang, Cunxiang and Wang, Yidong and Ye, Wei and Zhang, Yue and Chang, Yi and Yu, Philip S. and Yang, Qiang and Xie, Xing},\n  title     = {A Survey on Evaluation of Large Language Models},\n  journal   = {ACM Transactions on Intelligent Systems and Technology},\n  volume    = {15},\n  number    = {3},\n  pages     = {1--45},\n  year      = {2024},\n  doi       = {10.1145/3641289}\n}\n\n@article{white2024livebench,\n  author        = {White, Colin and Dooley, Samuel and Roberts, Manley and Pal, Arka and Feuer, Benjamin and Jain, Siddhartha and Shwartz-Ziv, Ravid and Joshi, Neel and Goldblum, Micah},\n  title         = {{LiveBench}: A Challenging, Contamination-Free {LLM} Benchmark},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2406.19314},\n  archiveprefix = {arXiv}\n}\n\n% --- Differential Item Functioning (DIF) ---\n\n@incollection{thissen1993dif,\n  author    = {Thissen, David and Steinberg, Lynne and Wainer, Howard},\n  title     = {Detection of Differential Item Functioning Using the Parameters of Item Response Models},\n  booktitle = {Differential Item Functioning},\n  editor    = {Holland, Paul W. and Wainer, Howard},\n  publisher = {Lawrence Erlbaum Associates},\n  pages     = {67--113},\n  year      = {1993}\n}\n\n@book{zumbo1999dif,\n  author    = {Zumbo, Bruno D.},\n  title     = {A Handbook on the Theory and Methods of Differential Item Functioning ({DIF}): Logistic Regression Modeling as a Unitary Framework for Binary and {Likert}-Type (Ordinal) Item Scores},\n  publisher = {Directorate of Human Resources Research and Evaluation, Department of National Defence},\n  year      = {1999},\n  address   = {Ottawa, ON}\n}\n\n% --- ML Calibration ---\n\n% --- Conformal Prediction ---\n\n% --- Data Attribution ---\n\n% --- Multidimensional IRT ---\n\n% --- Exposure-Ability Collinearity & IRT Identifiability ---\n\n% --- Measurement Error & Attenuation Bias ---\n\n% --- IRT Information & Power Analysis ---\n\n% --- 4PL Model & Identifiability ---\n\n% --- Model Family References ---\n\n@article{qwen2024qwen25,\n  author        = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Lin, Junyang and Zhou, Jingren},\n  title         = {Qwen2.5 Technical Report},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2412.15115},\n  archiveprefix = {arXiv}\n}\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA}: Low-Rank Adaptation of Large Language Models},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year      = {2022},\n  eprint    = {2106.09685},\n  archiveprefix = {arXiv}\n}\n\n@article{grattafiori2024llama3,\n  author        = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title         = {The {Llama} 3 Herd of Models},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2407.21783},\n  archiveprefix = {arXiv}\n}\n\n@article{gelman2012why,\n  author  = {Gelman, Andrew and Hill, Jennifer and Yajima, Masanao},\n  title   = {Why We (Usually) Don't Have to Worry About Multiple Comparisons},\n  journal = {Journal of Research on Educational Effectiveness},\n  volume  = {5},\n  number  = {2},\n  pages   = {189--211},\n  year    = {2012},\n  doi     = {10.1080/19345747.2011.618213},\n  url     = {https://www.tandfonline.com/doi/abs/10.1080/19345747.2011.618213}\n}\n\n@inproceedings{han2026quantifying,\n  author    = {Han, Jongwook and Song, Woojung and Lee, Jonggeun and Jo, Yohan},\n  title     = {Quantifying Data Contamination in Psychometric Evaluations of {LLMs}},\n  booktitle = {Findings of the Association for Computational Linguistics: EACL 2026},\n  pages     = {6070--6088},\n  year      = {2026},\n  url       = {https://aclanthology.org/2026.findings-eacl.319/}\n}\n\n@article{schaeffer2026causally,\n  author        = {Schaeffer, Rylan and Kazdan, Joshua and Abbasi, Baber and Liu, Ken Ziyu and Miranda, Brando and Ahmed, Ahmed and Berez, Fazl and Puri, Abhay and Biderman, Stella and Mireshghallah, Niloofar and Koyejo, Sanmi},\n  title         = {Quantifying the Effect of Test Set Contamination on Generative Evaluations},\n  journal       = {arXiv preprint},\n  year          = {2026},\n  eprint        = {2601.04301},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2601.04301}\n}\n\n@inproceedings{chen2025benchmarking,\n  author    = {Chen, Simin and Chen, Yiming and Li, Zexin and Jiang, Yifan and Wan, Zhongwei and He, Yixin and Ran, Dezhi and Gu, Tianle and Li, Haizhou and Xie, Tao and Ray, Baishakhi},\n  title     = {Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages     = {10080--10098},\n  year      = {2025},\n  url       = {https://aclanthology.org/2025.emnlp-main.511/}\n}\n\n@article{singh2024evaluation,\n  author        = {Singh, Aaditya K. and Kocyigit, Muhammed Yusuf and Poulton, Andrew and Esiobu, David and Lomeli, Maria and Szilvasy, Gergely and Hupkes, Dieuwke},\n  title         = {Evaluation Data Contamination in {LLMs}: How Do We Measure It and (When) Does It Matter?},\n  journal       = {arXiv preprint},\n  year          = {2024},\n  eprint        = {2411.03923},\n  archiveprefix = {arXiv},\n  url           = {https://arxiv.org/abs/2411.03923}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 512,
        "oldLines": 3,
        "newStart": 512,
        "newLines": 55,
        "lines": [
          "   archiveprefix = {arXiv},",
          "   url           = {https://arxiv.org/abs/2411.03923}",
          " }",
          "+",
          "+% --- Added references (SF8) ---",
          "+",
          "+@book{camilli_1994_dif,",
          "+  author    = {Camilli, Gregory and Shepard, Lorrie A.},",
          "+  title     = {Methods for Identifying Biased Test Items},",
          "+  series    = {Measurement Methods for the Social Sciences},",
          "+  publisher = {Sage Publications},",
          "+  year      = {1994},",
          "+  address   = {Thousand Oaks, CA},",
          "+  isbn      = {978-0-8039-4416-9}",
          "+}",
          "+",
          "+@article{swaminathan_1990_dif,",
          "+  author  = {Swaminathan, Hariharan and Rogers, H. Jane},",
          "+  title   = {Detecting Differential Item Functioning Using Logistic Regression Procedures},",
          "+  journal = {Journal of Educational Measurement},",
          "+  volume  = {27},",
          "+  number  = {4},",
          "+  pages   = {361--370},",
          "+  year    = {1990},",
          "+  doi     = {10.1111/j.1745-3984.1990.tb00754.x}",
          "+}",
          "+",
          "+@article{xu_2024_leakage,",
          "+  author        = {Xu, Ruijie and Wang, Zengzhi and Fan, Run-Ze and Liu, Pengfei},",
          "+  title         = {Benchmarking Benchmark Leakage in Large Language Models},",
          "+  journal       = {arXiv preprint},",
          "+  year          = {2024},",
          "+  eprint        = {2404.18824},",
          "+  archiveprefix = {arXiv},",
          "+  url           = {https://arxiv.org/abs/2404.18824}",
          "+}",
          "+",
          "+@inproceedings{li_2024_task_contamination,",
          "+  author    = {Li, Changmao and Flanigan, Jeffrey},",
          "+  title     = {Task Contamination: Language Models May Not Be Few-Shot Anymore},",
          "+  booktitle = {Proceedings of the 38th AAAI Conference on Artificial Intelligence},",
          "+  volume    = {38},",
          "+  number    = {16},",
          "+  pages     = {18471--18480},",
          "+  year      = {2024},",
          "+  doi       = {10.1609/aaai.v38i16.29808}",
          "+}",
          "+",
          "+@article{schroeders_2025_irt_sample_size,",
          "+  author  = {Schroeders, Ulrich and Gnambs, Timo},",
          "+  title   = {Sample-Size Planning in Item-Response Theory: A Tutorial},",
          "+  journal = {Advances in Methods and Practices in Psychological Science},",
          "+  year    = {2025},",
          "+  doi     = {10.1177/25152459251314798}",
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

_source line 38_

5 条已写入。汇总：

| # | Key | 论文 | 来源 |
|---|-----|------|------|
| 1 | `camilli_1994_dif` | Camilli & Shepard (1994), *Methods for Identifying Biased Test Items*, Sage | book, ISBN 978-0-8039-4416-9, 无 DOI |
| 2 | `swaminathan_1990_dif` | Swaminathan & Rogers (1990), *J. Educational Measurement* 27(4), 361–370 | DOI: 10.1111/j.1745-3984.1990.tb00754.x |
| 3 | `xu_2024_leakage` | Xu et al. (2024), *Benchmarking Benchmark Leakage in LLMs*, arXiv:2404.18824 | 未正式发表于会议，arXiv preprint |
| 4 | `li_2024_task_contamination` | Li & Flanigan (2024), *AAAI-38* 38(16), 18471–18480 | DOI: 10.1609/aaai.v38i16.29808 |
| 5 | `schroeders_2025_irt_sample_size` | Schroeders & Gnambs (2025), *Advances in Methods and Practices in Psychological Science* | DOI: 10.1177/25152459251314798 |

第 5 篇未找到 "Roberts et al. (2025)"，替换为 Schroeders & Gnambs (2025) 的 IRT sample-size planning tutorial，直接讨论 IRT 参数在小样本下的 recovery 问题，与项目 C008 约束（N<16 时 4PL 不可识别）高度相关。bib key 相应调整为 `schroeders_2025_irt_sample_size`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "uuid": "164df028-12ca-4d26-b952-261998d9d377",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014xAo7A1zncxstpBFz1Qf7K",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1937,
      "cache_read_input_tokens": 46337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1937
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

_source line 39_

5 条已写入。汇总：

| # | Key | 论文 | 来源 |
|---|-----|------|------|
| 1 | `camilli_1994_dif` | Camilli & Shepard (1994), *Methods for Identifying Biased Test Items*, Sage | book, ISBN 978-0-8039-4416-9, 无 DOI |
| 2 | `swaminathan_1990_dif` | Swaminathan & Rogers (1990), *J. Educational Measurement* 27(4), 361–370 | DOI: 10.1111/j.1745-3984.1990.tb00754.x |
| 3 | `xu_2024_leakage` | Xu et al. (2024), *Benchmarking Benchmark Leakage in LLMs*, arXiv:2404.18824 | 未正式发表于会议，arXiv preprint |
| 4 | `li_2024_task_contamination` | Li & Flanigan (2024), *AAAI-38* 38(16), 18471–18480 | DOI: 10.1609/aaai.v38i16.29808 |
| 5 | `schroeders_2025_irt_sample_size` | Schroeders & Gnambs (2025), *Advances in Methods and Practices in Psychological Science* | DOI: 10.1177/25152459251314798 |

第 5 篇未找到 "Roberts et al. (2025)"，替换为 Schroeders & Gnambs (2025) 的 IRT sample-size planning tutorial，直接讨论 IRT 参数在小样本下的 recovery 问题，与项目 C008 约束（N<16 时 4PL 不可识别）高度相关。bib key 相应调整为 `schroeders_2025_irt_sample_size`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 86700,
  "duration_api_ms": 140219,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "cf8160c4-3cc3-419e-ac2d-ea4d4eecf881",
  "total_cost_usd": 0.69720375,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 36433,
    "cache_read_input_tokens": 161507,
    "output_tokens": 3731,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36433,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 512,
        "cache_read_input_tokens": 46337,
        "cache_creation_input_tokens": 1937,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1937
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 176294,
      "outputTokens": 3826,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 10,
      "costUSD": 0.295424,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 3731,
      "cacheReadInputTokens": 161507,
      "cacheCreationInputTokens": 36433,
      "webSearchRequests": 0,
      "costUSD": 0.40177975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ab46f6d6-f230-451e-acd5-77715385b3fb"
}
```

</details>

---
