# paper bib verification

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/workers/worker_paper_bib-verification_20260523T165159.log`
- **Structured JSON:** [`5bcd82607235cd9de17c.json`](../../sessions/5b/5bcd82607235cd9de17c.json)

## Before a recorded user message

86 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
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
  "uuid": "417d0dbc-703c-4914-9c92-ce5acd2f926c",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779858000,
    "rateLimitType": "seven_day",
    "utilization": 0.8,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "3865d5e0-2d75-454f-ad83-bc0ad1b7ac65",
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the references.bib file and understanding the current state of the BibTeX entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "8995fd83-e3df-4f52-afeb-c04cb6d52906",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQApNsavES4Nmu2HtTRHnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12692,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12692
      },
      "output_tokens": 23,
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

先读取 bib 文件和 tex 文件，同时搜索 6 条待核对的 BibTeX 条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "561f2a3f-d929-48b7-b6f8-4ce6621f91e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQApNsavES4Nmu2HtTRHnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12692,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12692
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — Read · `toolu_01T5hu5QoFKZqn1BbQVd3vhd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "803ed7bb-8ce5-429b-ad46-0dea537b69bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQApNsavES4Nmu2HtTRHnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12692,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12692
      },
      "output_tokens": 23,
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

_source line 7 · 2026-05-23T16:52:12.554Z_

<details><summary>↩ Tool result · `toolu_01T5hu5QoFKZqn1BbQVd3vhd`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@article{landesberg2026bon,
4	  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},
5	  author = {Landesberg, Eddie},
6	  journal = {arXiv preprint arXiv:2603.12520},
7	  year = {2026},
8	}
9	
10	@inproceedings{min2023factscore,
11	  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},
12	  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},
13	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
14	  year = {2023},
15	  url = {https://aclanthology.org/2023.emnlp-main.741/},
16	}
17	
18	@article{holm1979simple,
19	  title = {A Simple Sequentially Rejective Multiple Test Procedure},
20	  author = {Holm, Sture},
21	  journal = {Scandinavian Journal of Statistics},
22	  volume = {6},
23	  number = {2},
24	  pages = {65--70},
25	  year = {1979},
26	}
27	
28	@inproceedings{xiong2024verbalized,
29	  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},
30	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
31	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},
32	  year = {2024},
33	  url = {https://arxiv.org/abs/2306.13063},
34	}
35	
36	@article{brown2024monkeys,
37	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
38	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
39	  journal = {arXiv preprint arXiv:2407.21787},
40	  year = {2024},
41	  url = {https://arxiv.org/abs/2407.21787}
42	}
43	
44	@inproceedings{chen2024usc,
45	  title = {Universal Self-Consistency for Large Language Model Generation},
46	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
47	  booktitle = {ICML 2024 Workshop on In-Context Learning},
48	  year = {2024},
49	  url = {https://arxiv.org/abs/2311.17311}
50	}
51	
52	@article{cobbe2021verifiers,
53	  title = {Training Verifiers to Solve Math Word Problems},
54	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
55	  journal = {arXiv preprint arXiv:2110.14168},
56	  year = {2021},
57	  url = {https://arxiv.org/abs/2110.14168}
58	}
59	
60	@inproceedings{derczynski2017wnut,
61	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
62	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
63	  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},
64	  year = {2017},
65	  url = {https://aclanthology.org/W17-4418/}
66	}
67	
68	@inproceedings{ding2021fewnerd,
69	  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
70	  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},
71	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
72	  pages = {3198--3213},
73	  year = {2021},
74	  doi = {10.18653/v1/2021.acl-long.248}
75	}
76	
77	@inproceedings{eikema2022sampling,
78	  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},
79	  author = {Eikema, Bryan and Aziz, Wilker},
80	  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},
81	  year = {2022},
82	  pages = {10978--10993},
83	  doi = {10.18653/v1/2022.emnlp-main.754}
84	}
85	
86	@article{freitag2022high,
87	  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},
88	  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},
89	  journal = {Transactions of the Association for Computational Linguistics},
90	  volume = {10},
91	  year = {2022},
92	  pages = {811--825},
93	  doi = {10.1162/tacl_a_00491}
94	}
95	
96	@article{fleiss1971agreement,
97	  title = {Measuring nominal scale agreement among many raters.},
98	  author = {Fleiss, Joseph L.},
99	  journal = {Psychological Bulletin},
100	  year = {1971},
101	  doi = {10.1037/h0031619},
102	  url = {http://dx.doi.org/10.1037/h0031619}
103	}
104	
105	@inproceedings{geng2024confidence,
106	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
107	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
108	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
109	  year = {2024},
110	  doi = {10.18653/v1/2024.naacl-long.366},
111	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
112	}
113	
114	
115	@article{kadavath2022language,
116	  title = {Language Models (Mostly) Know What They Know},
117	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
118	  journal = {arXiv preprint arXiv:2207.05221},
119	  year = {2022},
120	  url = {https://arxiv.org/abs/2207.05221}
121	}
122	
123	@inproceedings{kang2025selfcertainty,
124	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
125	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
126	  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},
127	  year = {2025},
128	  url = {https://arxiv.org/abs/2502.18581}
129	}
130	
131	@inproceedings{kuhn2023semantic,
132	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
133	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
134	  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},
135	  year = {2023},
136	  url = {https://arxiv.org/abs/2302.09664}
137	}
138	
139	@inproceedings{lightman2024verify,
140	  title = {Let's Verify Step by Step},
141	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
142	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},
143	  year = {2024},
144	  url = {https://arxiv.org/abs/2305.20050}
145	}
146	
147	@inproceedings{luan2018scierc,
148	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
149	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
150	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
151	  year = {2018},
152	  doi = {10.18653/v1/D18-1360},
153	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
154	}
155	
156	@inproceedings{manakul2023selfcheckgpt,
157	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
158	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
159	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
160	  year = {2023},
161	  doi = {10.18653/v1/2023.emnlp-main.557},
162	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
163	}
164	
165	@article{yao2026consistency,
166	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
167	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
168	  journal = {Genomics \& Informatics},
169	  year = {2026},
170	  doi = {10.1186/s44342-025-00063-2},
171	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
172	}
173	
174	@inproceedings{sainz2024gollie,
175	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
176	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
177	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},
178	  year = {2024},
179	  url = {https://arxiv.org/abs/2310.03668}
180	}
181	
182	@inproceedings{snell2025scaling,
183	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
184	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
185	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
186	  year = {2025},
187	  url = {https://arxiv.org/abs/2408.03314}
188	}
189	
190	@inproceedings{taubenfeld2025cisc,
191	  title = {Confidence Improves Self-Consistency in LLMs},
192	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
193	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
194	  year = {2025},
195	  doi = {10.18653/v1/2025.findings-acl.1030},
196	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
197	}
198	
199	@inproceedings{thirukovalluru2024atomic,
200	  title = {Atomic Self-Consistency for Better Long Form Generations},
201	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
202	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
203	  year = {2024},
204	  doi = {10.18653/v1/2024.emnlp-main.706},
205	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
206	}
207	
208	@inproceedings{tjongkimsang2003conll,
209	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
210	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
211	  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},
212	  year = {2003},
213	  url = {https://aclanthology.org/W03-0419/}
214	}
215	
216	@inproceedings{wang2023selfconsistency,
217	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
218	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
219	  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},
220	  year = {2023},
221	  url = {https://arxiv.org/abs/2203.11171}
222	}
223	
224	@article{willard2023guided,
225	  title = {Efficient Guided Generation for Large Language Models},
226	  author = {Willard, Brandon T. and Louf, Rémi},
227	  journal = {arXiv preprint arXiv:2307.09702},
228	  year = {2023},
229	  url = {https://arxiv.org/abs/2307.09702}
230	}
231	
232	@inproceedings{xia2025survey,
233	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
234	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
235	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
236	  year = {2025},
237	  url = {https://aclanthology.org/2025.findings-acl.1101/}
238	}
239	
240	@inproceedings{zheng2024llamafactory,
241	  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},
242	  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},
243	  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},
244	  year = {2024},
245	  pages = {400--410},
246	  doi = {10.18653/v1/2024.acl-demos.38}
247	}
248	
249	@inproceedings{zhou2024uniner,
250	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
251	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
252	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
253	  year = {2024},
254	  url = {https://arxiv.org/abs/2308.03279}
255	}
256	
257	@inproceedings{muller2021understanding,
258	  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
259	  author = {M{\"u}ller, Mathias and Sennrich, Rico},
260	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
261	  year = {2021},
262	  url = {https://arxiv.org/abs/2105.08504}
263	}
264	
265	@inproceedings{eikema2025structured,
266	  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},
267	  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},
268	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
269	  year = {2025},
270	  url = {https://arxiv.org/abs/2510.20700}
271	}
272	
273	@inproceedings{jinnai2024mbr,
274	  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},
275	  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},
276	  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},
277	  year = {2024},
278	  url = {https://arxiv.org/abs/2311.05263}
279	}
280	
281	@inproceedings{ratinov2009design,
282	  title = {Design Challenges and Misconceptions in Named Entity Recognition},
283	  author = {Ratinov, Lev and Roth, Dan},
284	  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},
285	  year = {2009},
286	  pages = {147--155},
287	  publisher = {Association for Computational Linguistics}
288	}
289	
290	@inproceedings{bergkirkpatrick2012empirical,
291	  title = {An Empirical Investigation of Statistical Significance in {NLP}},
292	  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},
293	  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},
294	  year = {2012},
295	  pages = {995--1005},
296	  publisher = {Association for Computational Linguistics}
297	}
298	
299	@inproceedings{tian2023calibration,
300	  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},
301	  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},
302	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
303	  year = {2023},
304	  pages = {5433--5442},
305	  publisher = {Association for Computational Linguistics}
306	}
307	
308	@inproceedings{yun2025price,
309	  title = {The Price of Format: Diversity Collapse in {LLMs}},
310	  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},
311	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
312	  year = {2025},
313	  url = {https://aclanthology.org/2025.findings-emnlp.836/}
314	}
315	
316	@inproceedings{gao2023scaling,
317	  title = {Scaling Laws for Reward Model Overoptimization},
318	  author = {Gao, Leo and Schulman, John and Hilton, Jacob},
319	  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
320	  year = {2023},
321	  url = {https://proceedings.mlr.press/v202/gao23h.html}
322	}
323	
324	@inproceedings{kuleshov2015calibrated,
325	  title = {Calibrated Structured Prediction},
326	  author = {Kuleshov, Volodymyr and Liang, Percy},
327	  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},
328	  year = {2015},
329	  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}
330	}
331	
332	@inproceedings{platt1999probabilistic,
333	  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},
334	  author = {Platt, John C.},
335	  booktitle = {Advances in Large Margin Classifiers},
336	  pages = {61--74},
337	  year = {1999},
338	  publisher = {MIT Press}
339	}
340	
341	@inproceedings{guo2017calibration,
342	  title = {On Calibration of Modern Neural Networks},
343	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
344	  booktitle = {Proceedings of the 34th International Conference on Machine Learning},
345	  pages = {1321--1330},
346	  year = {2017}
347	}
348	
349	@inproceedings{geifman2017selective,
350	  title = {Selective Classification for Deep Neural Networks},
351	  author = {Geifman, Yonatan and El-Yaniv, Ran},
352	  booktitle = {Advances in Neural Information Processing Systems},
353	  volume = {30},
354	  year = {2017},
355	  url = {https://arxiv.org/abs/1705.08500}
356	}
357	
358	@article{dong2024xgrammar,
359	  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},
360	  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},
361	  journal = {arXiv preprint arXiv:2411.15100},
362	  year = {2024},
363	  url = {https://arxiv.org/abs/2411.15100}
364	}
365	
366	@article{lin2022teaching,
367	  title = {Teaching Models to Express Their Uncertainty in Words},
368	  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},
369	  journal = {Transactions on Machine Learning Research},
370	  year = {2022},
371	  url = {https://arxiv.org/abs/2205.14334}
372	}
373	
374	@article{farquhar2024detecting,
375	  title = {Detecting hallucinations in large language models using semantic entropy},
376	  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},
377	  journal = {Nature},
378	  volume = {630},
379	  pages = {625--630},
380	  year = {2024},
381	  doi = {10.1038/s41586-024-07421-0}
382	}
383	
384	@article{chen2023twofailures,
385	  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},
386	  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},
387	  journal = {Transactions on Machine Learning Research},
388	  year = {2024},
389	  url = {https://arxiv.org/abs/2305.14279}
390	}
391	
392	@inproceedings{aggarwal2023adaptive,
393	  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},
394	  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},
395	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},
396	  year = {2023},
397	  url = {https://arxiv.org/abs/2305.11860}
398	}
399	
400	@inproceedings{xie2023zeroshot,
401	  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
402	  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
403	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
404	  pages = {7935--7956},
405	  year = {2023},
406	  publisher = {Association for Computational Linguistics},
407	  doi = {10.18653/v1/2023.emnlp-main.493},
408	  url = {https://aclanthology.org/2023.emnlp-main.493/}
409	}
410	
411	@inproceedings{muennighoff2025s1,
412	  title = {s1: Simple Test-Time Scaling},
413	  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\`e}s, Emmanuel and Hashimoto, Tatsunori},
414	  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
415	  year = {2025},
416	  url = {https://arxiv.org/abs/2501.19393}
417	}
418	
419	@inproceedings{eikema2020map,
420	  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},
421	  author = {Eikema, Bryan and Aziz, Wilker},
422	  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},
423	  pages = {4506--4520},
424	  year = {2020},
425	  url = {https://aclanthology.org/2020.coling-main.398/}
426	}
427	
428	@inproceedings{kumar2004minimum,
429	  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},
430	  author = {Kumar, Shankar and Byrne, William},
431	  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},
432	  pages = {169--176},
433	  year = {2004},
434	  url = {https://aclanthology.org/N04-1022/}
435	}
436	
437	@inproceedings{dembczynski2011exact,
438	  title = {An Exact Algorithm for {F}-Measure Maximization},
439	  author = {Dembczy{\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\"u}llermeier, Eyke},
440	  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},
441	  year = {2011},
442	  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}
443	}
444	
445	@inproceedings{denero2009fast,
446	  title = {Fast Consensus Decoding over Translation Forests},
447	  author = {DeNero, John and Chiang, David and Knight, Kevin},
448	  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},
449	  pages = {567--575},
450	  year = {2009},
451	  url = {https://aclanthology.org/P09-1064/}
452	}
453	
454	@inproceedings{desai2020calibration,
455	  title = {Calibration of Pre-trained Transformers},
456	  author = {Desai, Shrey and Durrett, Greg},
457	  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
458	  pages = {295--302},
459	  year = {2020},
460	  url = {https://aclanthology.org/2020.emnlp-main.21/}
461	}
462	
463	@inproceedings{huang2024large,
464	  title = {Large Language Models Cannot Self-Correct Reasoning Yet},
465	  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},
466	  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
467	  year = {2024},
468	  url = {https://openreview.net/forum?id=IkmD3fKBPQ}
469	}
470	
471	@inproceedings{li2024simple,
472	  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},
473	  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},
474	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},
475	  year = {2024},
476	  url = {https://arxiv.org/abs/2402.13364}
477	}
478	
479	@inproceedings{xie2024selfimproving,
480	  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},
481	  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
482	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
483	  year = {2024}
484	}
485	
486	@inproceedings{madaan2023selfrefine,
487	  title = {Self-Refine: Iterative Refinement with Self-Feedback},
488	  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shyam and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},
489	  booktitle = {Advances in Neural Information Processing Systems},
490	  year = {2023}
491	}
492	
493	@article{chen2021codex,
494	  title = {Evaluating Large Language Models Trained on Code},
495	  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
496	  journal = {arXiv preprint arXiv:2107.03374},
497	  year = {2021}
498	}
499	
500	@inproceedings{fisch2021conformal,
501	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
502	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
503	  booktitle = {Proceedings of the 38th International Conference on Machine Learning},
504	  year = {2021}
505	}
506	
507	@article{angelopoulos2023conformal,
508	  title = {Conformal Prediction: A Gentle Introduction},
509	  author = {Angelopoulos, Anastasios N. and Bates, Stephen},
510	  journal = {Foundations and Trends in Machine Learning},
511	  volume = {16},
512	  number = {4},
513	  pages = {494--591},
514	  year = {2023}
515	}
516	
517	@inproceedings{malinin2021uncertainty,
518	  title = {Uncertainty Estimation in Autoregressive Structured Prediction},
519	  author = {Malinin, Andrey and Gales, Mark},
520	  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},
521	  year = {2021}
522	}
523	
524	@inproceedings{varshney2022selective,
525	  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},
526	  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},
527	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
528	  year = {2022}
529	}
530	
531	@inproceedings{vazhentsev2022uncertainty,
532	  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},
533	  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},
534	  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
535	  year = {2022},
536	  url = {https://aclanthology.org/2022.acl-long.566}
537	}
538	
539	@inproceedings{kuleshov2022calibrated,
540	  title = {Calibrated Structured Prediction},
541	  author = {Kuleshov, Volodymyr and Deshpande, Shachi},
542	  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},
543	  year = {2022},
544	  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}
545	}
546	
547	@inproceedings{yee2019noisy,
548	  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},
549	  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},
550	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
551	  year = {2019},
552	  url = {https://arxiv.org/abs/1908.05731}
553	}
554	
555	@inproceedings{li2023stepaware,
556	  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},
557	  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},
558	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
559	  year = {2023},
560	  url = {https://arxiv.org/abs/2206.02336}
561	}
562	
563	@inproceedings{zhang2023ener,
564	  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},
565	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
566	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
567	  year = {2023},
568	  url = {https://arxiv.org/abs/2305.17854}
569	}
570	
571	@inproceedings{he2024uncertainty,
572	  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},
573	  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},
574	  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},
575	  year = {2024},
576	  url = {https://arxiv.org/abs/2311.08726}
577	}
578	
579	@inproceedings{xiao2022uncertainty,
580	  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},
581	  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},
582	  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},
583	  year = {2022},
584	}
585	
586	@article{li2026rewardtail,
587	  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},
588	  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},
589	  journal = {arXiv preprint arXiv:2602.01485},
590	  year = {2026},
591	}
592	
593	@inproceedings{shinn2023reflexion,
594	  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},
595	  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
596	  booktitle = {Advances in Neural Information Processing Systems},
597	  year = {2023}
598	}
599	
600	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "d8dedba0-4c96-4825-a86e-d99d347f7b3a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shyam and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
      "numLines": 600,
      "startLine": 1,
      "totalLines": 600
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01NjrpZUsZ5KUBFaCmm85ZNJ`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "70a88cae-83b8-4a77-8fcb-8d94edd10b01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JQApNsavES4Nmu2HtTRHnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12692,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12692
      },
      "output_tokens": 23,
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

_source line 9 · 2026-05-23T16:52:12.962Z_

<details><summary>↩ Tool result · `toolu_01NjrpZUsZ5KUBFaCmm85ZNJ`</summary>

```text
docs/paper/sections/theoretical.tex
docs/paper/sections/_archived/experiments_OLD.tex
docs/paper/sections/mechanistic.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/diagnostic.tex
docs/paper/sections/checklist.tex
docs/paper/sections/related_work.tex
docs/paper/sections/background.tex
docs/paper/sections/abstract.tex
docs/paper/sections/adaptive.tex
docs/paper/sections/method.tex
docs/paper/sections/discussion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/appendix.tex
docs/paper/main.tex
docs/paper/sections/theory.tex
docs/paper/sections/introduction.tex
docs/paper/sections/single_signal.tex
docs/paper/sections/experiments_main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "04d8e455-3c17-4a65-b12b-18ff365073e7",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/theoretical.tex",
      "docs/paper/sections/_archived/experiments_OLD.tex",
      "docs/paper/sections/mechanistic.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/diagnostic.tex",
      "docs/paper/sections/checklist.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/background.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/adaptive.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/discussion.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/theory.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/single_signal.tex",
      "docs/paper/sections/experiments_main.tex"
    ],
    "durationMs": 14,
    "numFiles": 19,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:
1. Search for all \cite references in the tex files to find which bib keys are actually used
2. WebSearch for the 6 specific entries to verify their accuracy

Let me first extract all bib keys from references.bib, then grep for citations in tex files. I'll also start the web searches for the 6 entries.

Let me extract all bib keys from the bib file first. The keys I can see are:
- landesberg2026bon
- min2023factscore
- holm1979simple
- xiong2024verbalized
- brown2024monkeys


- chen2024usc
- cobbe2021verifiers
- derczynski2017wnut
- ding2021fewnerd
- eikema2022sampling
- freitag2022high
- fleiss1971agreement
- geng2024confidence
- kadavath2022language
- kang2025selfcertainty
- kuhn2023semantic
- lightman2024verify
- luan2018scierc
- manakul2023selfcheckgpt
- yao2026consistency
- sainz2024gollie
- snell2025scaling
- taubenfeld2025cisc
- thirukovalluru2024atomic
- tjongkimsang2003conll
- wang2023selfconsistency
- willard2023guided
- xia2025survey
- zheng2024llamafactory
- zhou2024uniner
- muller2021understanding
- eikema2025structured
- jinnai2024mbr
- ratinov2009design
- bergkirkpatrick2012empirical
- tian2023calibration
- yun2025price
- gao2023scaling
- kuleshov2015calibrated
- platt1999probabilistic
- guo2017calibration
- geifman2017selective
- dong2024xgrammar
- lin2022teaching
- farquhar2024detecting
- chen2023twofailures
- aggarwal2023adaptive
- xie2023zeroshot
- madaan2023selfrefine
- chen2021cod
- fisch2021conformal
- angelopoulos2023conformal
- malinin2021uncertainty
- varshney2022selective
- vazhentsev2022uncertainty
- kuleshov2022calibrated
- yee2019noisy
- li2023stepaware
- zhang2023ener
- he2024uncertainty
- xiao2022uncertainty
- li2026rewardtail
- shinn2023reflexion
- desai2020calibration
- huang2024large
- li2024simple
- xie2024selfimproving
- kumar2004minimum
- dembczynski2011exact
- denero2009fast
- eikema2020map
- muennighoff2025s1

Now I'm searching through the tex files for all citation commands and checking for those six specific entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "accad76c-a88d-4f64-b12d-12027187cbff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YokuTtw7KDU1pZnTFNtEE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11863,
      "cache_read_input_tokens": 24533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11863
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

Now let me grep for all citation commands in the tex files, and search for the 6 entries to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "b4984b66-b8bd-4012-805d-d196db0a3ced",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YokuTtw7KDU1pZnTFNtEE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11863,
      "cache_read_input_tokens": 24533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11863
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

<details open><summary>🔧 Tool call — Grep · `toolu_01XfwDjmtWRzRBbPdySJjVVt`</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "a37031fe-23f3-4619-9a0d-da11c25df7e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YokuTtw7KDU1pZnTFNtEE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11863,
      "cache_read_input_tokens": 24533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11863
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

_source line 13 · 2026-05-23T16:52:39.515Z_

<details><summary>↩ Tool result · `toolu_01XfwDjmtWRzRBbPdySJjVVt`</summary>

```text
docs/paper/sections/related_work.tex:4:Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.
docs/paper/sections/related_work.tex:5:Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.
docs/paper/sections/related_work.tex:9:\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as conditions associated with the failure of this correlation to yield selection gains.
docs/paper/sections/related_work.tex:10:\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.
docs/paper/sections/related_work.tex:11:\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.
docs/paper/sections/related_work.tex:12:Our evaluation builds on generative IE \cite{zhou2024uniner, sainz2024gollie} and constrained decoding \cite{willard2023guided, dong2024xgrammar}.
docs/paper/sections/related_work.tex:15:Our selection strategies instantiate MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.
docs/paper/sections/related_work.tex:16:Semantic uncertainty \cite{kuhn2023semantic} and confidence estimation \cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective prediction \cite{geifman2017selective} and support abstention independent of sample selection.
docs/paper/sections/mechanistic.tex:13:Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
docs/paper/sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
docs/paper/sections/checklist.tex:57:Yes. LLaMA Factory \cite{zheng2024llamafactory} for fine-tuning and XGrammar \cite{dong2024xgrammar} for constrained decoding are cited with version-relevant details in Appendix~\ref{app:training}. Evaluation uses standard span-level micro-F1 (converted to per-instance macro-F1 as described in Section~\ref{sec:evaluation}).
docs/paper/sections/discussion.tex:5:The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter); this persists across families \cite{yun2025price}, scales (4B--72B), and decoding modes (Appendix~\ref{app:freeform_ablation}).
docs/paper/sections/method.tex:5:Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
docs/paper/sections/method.tex:28:We adapt \citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\cup| \times 2$ rating matrix:
docs/paper/sections/method.tex:73:Entity-level construction (\S\ref{sec:selection_method}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
docs/paper/sections/method.tex:84:Set-level F1 admits no closed-form threshold \cite{dembczynski2011exact}; we use $\alpha{=}1$ throughout, which induces similar thresholds for typical NER sizes ($|E_\cup| \leq 30$).
docs/paper/sections/theory.tex:6:Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}), consistent with utility degradation on structured outputs \cite{eikema2025structured}.
docs/paper/sections/theory.tex:11:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
docs/paper/sections/diagnostic.tex:7:Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
docs/paper/sections/diagnostic.tex:34:FK: inter-rater agreement \cite{fleiss1971agreement} adapted to entity sets, treating unique (text, type) tuples as items with binary present/absent labels (Appendix~\ref{app:fk_independence}).
docs/paper/sections/_archived/experiments_OLD.tex:9:\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
docs/paper/sections/_archived/experiments_OLD.tex:10:\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
docs/paper/sections/_archived/experiments_OLD.tex:11:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
docs/paper/sections/_archived/experiments_OLD.tex:12:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
docs/paper/sections/_archived/experiments_OLD.tex:15:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
docs/paper/sections/_archived/experiments_OLD.tex:16:We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\ref{app:n_scaling}).
docs/paper/sections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): FewNERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$); a single stochastic sample underperforms greedy ($N{\geq}4$ needed to match).
docs/paper/sections/background.tex:4:Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \cite{li2026rewardtail}. Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.
docs/paper/sections/background.tex:5:SC can fail when consistent outputs are wrong \cite{chen2023twofailures}; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain. Iterative self-verification \cite{shinn2023reflexion} offers an alternative, but our ESJ and MRSC results (\S\ref{sec:selection_gap}) show such approaches also fail for NER.
docs/paper/sections/background.tex:6:\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\S\ref{sec:selection_gap}).
docs/paper/sections/background.tex:9:\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.
docs/paper/sections/background.tex:11:\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
docs/paper/sections/background.tex:14:Our selection instantiates MBR decoding \cite{eikema2022sampling}; \citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings.
docs/paper/sections/background.tex:15:LP is well-calibrated at population level \cite{kadavath2022language, tian2023calibration} and motivated as a quality signal by noisy channel models \cite{yee2019noisy}, yet too compressed within instances for selection.
docs/paper/sections/background.tex:16:Complementary approaches include uncertainty estimation for autoregressive structured prediction \cite{malinin2021uncertainty}, calibration of pre-trained transformers \cite{desai2020calibration}, large-scale uncertainty quantification \cite{xiao2022uncertainty}, semantic uncertainty \cite{kuhn2023semantic}, selective prediction \cite{geifman2017selective}, and conformal prediction \cite{angelopoulos2023conformal}.
docs/paper/sections/background.tex:26:Dimension & \citet{yao2026consistency} & \citet{yun2025price} & \citet{landesberg2026bon} & Ours \\
docs/paper/sections/background.tex:39:\citet{landesberg2026bon} independently document a correlation-selection gap in best-of-$N$ reasoning: global judge $r{=}0.47$ masks within-prompt $r{=}0.27$ (Table~\ref{tab:novelty_comparison}).
docs/paper/sections/appendix.tex:257:Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
docs/paper/sections/appendix.tex:503:(2) $\delta_{\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \cite{ratinov2009design};
docs/paper/sections/appendix.tex:504:(3) $\delta_{\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \cite{bergkirkpatrick2012empirical}.
docs/paper/sections/appendix.tex:619:Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
docs/paper/sections/appendix.tex:783:Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
docs/paper/sections/appendix.tex:1125:Entity-level construction (\S\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\arg\max_{y \in \{y_1,\ldots,y_N\}}$) to construction over all subsets of $E_\cup{=}\bigcup_i y_i$.
docs/paper/sections/appendix.tex:1136:Set-level F1 is non-linear and admits no closed-form threshold rule \cite{dembczynski2011exact}. We use balanced linear utility ($\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\cup| \leq 30$).
docs/paper/sections/appendix.tex:1145:With F1 utility, the optimal threshold depends on the full probability vector over $E_\cup$ \cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\cup|$ is small (typically 5--15 in our experiments).
docs/paper/sections/appendix.tex:1150:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
docs/paper/sections/appendix.tex:1151:Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.
docs/paper/sections/appendix.tex:1152:\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
docs/paper/sections/appendix.tex:1865:We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \citet{lin2022teaching} and \citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.
docs/paper/sections/appendix.tex:2038:Standard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \cite{platt1999probabilistic} fits a logistic regression $\sigma(a \cdot \text{LP} + b)$, and temperature scaling \cite{guo2017calibration} divides logits by a scalar $\tau$.
docs/paper/sections/appendix.tex:2453:Aspect & \citet{yun2025price} & \citet{chen2023twofailures} & \citet{aggarwal2023adaptive} & \citet{farquhar2024detecting} & \textbf{Ours} \\
docs/paper/sections/appendix.tex:2494:Majority vote \textit{is} MBR decoding under set-overlap utility (Proposition~\ref{prop:construction_mbr}; \S\ref{sec:mbr_theory}). LP-weighted construction is the quality-aware MBR variant (\S\ref{sec:mbr_theory}). This follows directly from \citet{eikema2022sampling}; \citet{eikema2025structured} confirm that MBR utilities degrade on structured outputs, consistent with our LP compression findings.
docs/paper/sections/appendix.tex:2508:\paragraph{O12: Overlap with \citet{yun2025price}.}
docs/paper/sections/experiments_main.tex:7:\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
docs/paper/sections/experiments_main.tex:8:\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
docs/paper/sections/experiments_main.tex:9:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
docs/paper/sections/experiments_main.tex:10:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
docs/paper/sections/experiments_main.tex:13:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
docs/paper/sections/experiments_main.tex:14:$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
docs/paper/sections/experiments_main.tex:105:Under per-family Holm--Bonferroni \cite{holm1979simple} correction ($k{=}10$ entity-construction comparisons), $p_{\text{adj}}{=}0.006$; global ($k{=}57$): $p_{\text{adj}}{=}0.055$; the family partition was not pre-registered (Appendix~\ref{app:holm}).
docs/paper/sections/experiments_main.tex:113:The degeneracy decomposition (\S\ref{sec:theory}) identifies $\alpha$---not degeneracy---as the binding constraint ($8$--$33{\times}$ tighter); this persists across families \cite{yun2025price}, scales (4B--72B), and decoding modes (Appendix~\ref{app:freeform_ablation}).
docs/paper/sections/introduction.tex:3:Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
docs/paper/sections/introduction.tex:4:For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \cite{yao2026consistency} and qualitative diversity collapse \cite{yun2025price} but no instance-level diagnostic framework.
docs/paper/sections/introduction.tex:8:A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
docs/paper/sections/introduction.tex:26:QE signals achieve AUROC up to $0.82$; while \citet{yao2026consistency} report task-level correlation ($\rho$ up to 0.47), our instance-level decomposition reveals why correlation does not yield selection gains.
docs/paper/sections/introduction.tex:28:A diagnostic cascade---degeneracy, LP compression, signal alignment---quantifies failure mechanisms at entity level; \citet{yun2025price} describe diversity collapse qualitatively, we provide quantitative decomposition ($D$, $\alpha$, LP range). A necessary condition bound (\S\ref{sec:theory}) confirms $\alpha$ as the binding constraint (3--12\% recovery ratio). Hidden-state probes reveal an introspection boundary (AUROC $0.63$--$0.88$ vs.\ ESJ $\approx 0.50$; Appendix~\ref{sec:mechanistic}).
docs/paper/sections/introduction.tex:30:Entity-level construction yields $+1.40$\,pp on Few-NERD where the cascade identifies favorable conditions. Unlike \citet{xie2023zeroshot}'s zero-shot entity voting, we aggregate stochastic samples from fine-tuned models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "d983333e-e6cb-4a18-ae1b-19029a52df5b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:4:Self-consistency \\cite{wang2023selfconsistency} and best-of-$N$ with compute-optimal allocation \\cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code tasks.\ndocs/paper/sections/related_work.tex:5:Reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty} and BoN scaling laws \\cite{gao2023scaling} reduce or characterize inference cost, while trained verifiers \\cite{cobbe2021verifiers, lightman2024verify} learn per-sample scoring.\ndocs/paper/sections/related_work.tex:9:\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE; we diagnose degeneracy and LP compression as conditions associated with the failure of this correlation to yield selection gains.\ndocs/paper/sections/related_work.tex:10:\\citet{xie2023zeroshot} propose entity voting for zero-shot NER, the closest prior work to our entity-level construction; our approach aggregates stochastic samples from a single fine-tuned model without prompt engineering.\ndocs/paper/sections/related_work.tex:11:\\citet{yun2025price} show structured formats induce diversity collapse; our LP compression (median range 0.041 nats) corroborates this for NER.\ndocs/paper/sections/related_work.tex:12:Our evaluation builds on generative IE \\cite{zhou2024uniner, sainz2024gollie} and constrained decoding \\cite{willard2023guided, dong2024xgrammar}.\ndocs/paper/sections/related_work.tex:15:Our selection strategies instantiate MBR decoding \\cite{eikema2022sampling}; \\citet{eikema2025structured} find MBR utilities degrade on structured outputs, while our diagnosis identifies degeneracy as the primary bottleneck.\ndocs/paper/sections/related_work.tex:16:Semantic uncertainty \\cite{kuhn2023semantic} and confidence estimation \\cite{geng2024confidence, xia2025survey} provide complementary model-internal alternatives; our QE signals with AUROC up to 0.82 connect to selective prediction \\cite{geifman2017selective} and support abstention independent of sample selection.\ndocs/paper/sections/mechanistic.tex:13:Following iterative self-refinement \\cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\\ $0.4997$).\ndocs/paper/sections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\ndocs/paper/sections/checklist.tex:57:Yes. LLaMA Factory \\cite{zheng2024llamafactory} for fine-tuning and XGrammar \\cite{dong2024xgrammar} for constrained decoding are cited with version-relevant details in Appendix~\\ref{app:training}. Evaluation uses standard span-level micro-F1 (converted to per-instance macro-F1 as described in Section~\\ref{sec:evaluation}).\ndocs/paper/sections/discussion.tex:5:The degeneracy decomposition (\\S\\ref{sec:theory}) identifies $\\alpha$---not degeneracy---as the binding constraint ($8$--$33{\\times}$ tighter); this persists across families \\cite{yun2025price}, scales (4B--72B), and decoding modes (Appendix~\\ref{app:freeform_ablation}).\ndocs/paper/sections/method.tex:5:Given model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\ndocs/paper/sections/method.tex:28:We adapt \\citet{fleiss1971agreement} to entity sets: items are unique (text, type) tuples across all $N$ samples; each sample assigns binary present/absent labels, yielding a $|E_\\cup| \\times 2$ rating matrix:\ndocs/paper/sections/method.tex:73:Entity-level construction (\\S\\ref{sec:selection_method}) is a special case of minimum Bayes risk (MBR) decoding \\cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\\arg\\max_{y \\in \\{y_1,\\ldots,y_N\\}}$) to construction over all subsets of $E_\\cup{=}\\bigcup_i y_i$.\ndocs/paper/sections/method.tex:84:Set-level F1 admits no closed-form threshold \\cite{dembczynski2011exact}; we use $\\alpha{=}1$ throughout, which induces similar thresholds for typical NER sizes ($|E_\\cup| \\leq 30$).\ndocs/paper/sections/theory.tex:6:Signal-derived weights $w_i$ yield quality-weighted MBR: $\\hat{p}_w(e) = \\sum_{i} w_i \\, \\mathbf{1}[e {\\in} y_i] / \\sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\\rho{\\approx}0.2$; \\S\\ref{sec:prescriptive}), consistent with utility degradation on structured outputs \\cite{eikema2025structured}.\ndocs/paper/sections/theory.tex:11:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): Few-NERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, SciERC converges more slowly ($c{\\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\\,pp---a persistent gap.\ndocs/paper/sections/diagnostic.tex:7:Given model $\\mathcal{M}$ and input $x$, we sample $N$ outputs $\\{y_1, \\ldots, y_N\\}$ at temperature $T > 0$ via constrained decoding \\cite{willard2023guided}, where each $y_i$ is an entity set.\ndocs/paper/sections/diagnostic.tex:34:FK: inter-rater agreement \\cite{fleiss1971agreement} adapted to entity sets, treating unique (text, type) tuples as items with binary present/absent labels (Appendix~\\ref{app:fk_independence}).\ndocs/paper/sections/_archived/experiments_OLD.tex:9:\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\ndocs/paper/sections/_archived/experiments_OLD.tex:10:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\ndocs/paper/sections/_archived/experiments_OLD.tex:11:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\ndocs/paper/sections/_archived/experiments_OLD.tex:12:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\ndocs/paper/sections/_archived/experiments_OLD.tex:15:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\ndocs/paper/sections/_archived/experiments_OLD.tex:16:We draw $N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}, with $N{=}16$ for scaling experiments (Appendix~\\ref{app:n_scaling}).\ndocs/paper/sections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): FewNERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, while SciERC converges more slowly ($c{\\approx}0.35$); a single stochastic sample underperforms greedy ($N{\\geq}4$ needed to match).\ndocs/paper/sections/background.tex:4:Self-consistency \\cite{wang2023selfconsistency} and best-of-$N$ with scaling laws \\cite{snell2025scaling, brown2024monkeys, gao2023scaling} yield large gains on reasoning; recent extensions include reward-tail-guided search \\cite{li2026rewardtail}. Reward-free selectors \\cite{taubenfeld2025cisc, kang2025selfcertainty} and trained verifiers \\cite{cobbe2021verifiers, lightman2024verify, li2023stepaware} target discrete-answer settings.\ndocs/paper/sections/background.tex:5:SC can fail when consistent outputs are wrong \\cite{chen2023twofailures}; free-form \\cite{chen2024usc} and atomic \\cite{thirukovalluru2024atomic} variants face limits where sub-output agreement does not yield selection gain. Iterative self-verification \\cite{shinn2023reflexion} offers an alternative, but our ESJ and MRSC results (\\S\\ref{sec:selection_gap}) show such approaches also fail for NER.\ndocs/paper/sections/background.tex:6:\\citet{yun2025price} identify diversity collapse under constrained decoding; we extend their qualitative account with quantitative diagnostics (\\S\\ref{sec:selection_gap}).\ndocs/paper/sections/background.tex:9:\\citet{yao2026consistency} show consistency correlates with accuracy for LLM-based NER/RE ($\\rho$ up to 0.47); we extend to instance-level analysis: (1)~task-level $\\rho$ masks instance-level degeneracy; (2)~we decompose failure into degeneracy and LP compression; (3)~pre-deployment diagnostics that task-level correlation cannot provide.\ndocs/paper/sections/background.tex:11:\\citet{xie2023zeroshot} propose entity voting for zero-shot NER; \\citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.\ndocs/paper/sections/background.tex:14:Our selection instantiates MBR decoding \\cite{eikema2022sampling}; \\citet{eikema2025structured} find MBR utilities degrade on structured outputs, consistent with our LP compression findings.\ndocs/paper/sections/background.tex:15:LP is well-calibrated at population level \\cite{kadavath2022language, tian2023calibration} and motivated as a quality signal by noisy channel models \\cite{yee2019noisy}, yet too compressed within instances for selection.\ndocs/paper/sections/background.tex:16:Complementary approaches include uncertainty estimation for autoregressive structured prediction \\cite{malinin2021uncertainty}, calibration of pre-trained transformers \\cite{desai2020calibration}, large-scale uncertainty quantification \\cite{xiao2022uncertainty}, semantic uncertainty \\cite{kuhn2023semantic}, selective prediction \\cite{geifman2017selective}, and conformal prediction \\cite{angelopoulos2023conformal}.\ndocs/paper/sections/background.tex:26:Dimension & \\citet{yao2026consistency} & \\citet{yun2025price} & \\citet{landesberg2026bon} & Ours \\\\\ndocs/paper/sections/background.tex:39:\\citet{landesberg2026bon} independently document a correlation-selection gap in best-of-$N$ reasoning: global judge $r{=}0.47$ masks within-prompt $r{=}0.27$ (Table~\\ref{tab:novelty_comparison}).\ndocs/paper/sections/appendix.tex:257:Our $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\ndocs/paper/sections/appendix.tex:503:(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\ndocs/paper/sections/appendix.tex:504:(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\ndocs/paper/sections/appendix.tex:619:Following iterative self-refinement \\cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\\ $0.4997$).\ndocs/paper/sections/appendix.tex:783:Inference uses vLLM with XGrammar-based JSON schema enforcement \\cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\ndocs/paper/sections/appendix.tex:1125:Entity-level construction (\\S\\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \\cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\\arg\\max_{y \\in \\{y_1,\\ldots,y_N\\}}$) to construction over all subsets of $E_\\cup{=}\\bigcup_i y_i$.\ndocs/paper/sections/appendix.tex:1136:Set-level F1 is non-linear and admits no closed-form threshold rule \\cite{dembczynski2011exact}. We use balanced linear utility ($\\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\\cup| \\leq 30$).\ndocs/paper/sections/appendix.tex:1145:With F1 utility, the optimal threshold depends on the full probability vector over $E_\\cup$ \\cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\\cup|$ is small (typically 5--15 in our experiments).\ndocs/paper/sections/appendix.tex:1150:Our selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\ndocs/paper/sections/appendix.tex:1151:Despite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\ndocs/paper/sections/appendix.tex:1152:\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\ndocs/paper/sections/appendix.tex:1865:We evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{lin2022teaching} and \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\ndocs/paper/sections/appendix.tex:2038:Standard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \\cite{platt1999probabilistic} fits a logistic regression $\\sigma(a \\cdot \\text{LP} + b)$, and temperature scaling \\cite{guo2017calibration} divides logits by a scalar $\\tau$.\ndocs/paper/sections/appendix.tex:2453:Aspect & \\citet{yun2025price} & \\citet{chen2023twofailures} & \\citet{aggarwal2023adaptive} & \\citet{farquhar2024detecting} & \\textbf{Ours} \\\\\ndocs/paper/sections/appendix.tex:2494:Majority vote \\textit{is} MBR decoding under set-overlap utility (Proposition~\\ref{prop:construction_mbr}; \\S\\ref{sec:mbr_theory}). LP-weighted construction is the quality-aware MBR variant (\\S\\ref{sec:mbr_theory}). This follows directly from \\citet{eikema2022sampling}; \\citet{eikema2025structured} confirm that MBR utilities degrade on structured outputs, consistent with our LP compression findings.\ndocs/paper/sections/appendix.tex:2508:\\paragraph{O12: Overlap with \\citet{yun2025price}.}\ndocs/paper/sections/experiments_main.tex:7:\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\\approx}$65\\% F1).\ndocs/paper/sections/experiments_main.tex:8:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:selection_gap}).\ndocs/paper/sections/experiments_main.tex:9:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control.\ndocs/paper/sections/experiments_main.tex:10:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\\% zero F1) probes the signal-collapse boundary.\ndocs/paper/sections/experiments_main.tex:13:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others; Appendix~\\ref{app:epoch_confound}).\ndocs/paper/sections/experiments_main.tex:14:$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \\cite{willard2023guided}; $N {\\in} \\{16, 32, 64\\}$ for scaling (Figure~\\ref{fig:n_scaling}; Appendix~\\ref{app:n_scaling}).\ndocs/paper/sections/experiments_main.tex:105:Under per-family Holm--Bonferroni \\cite{holm1979simple} correction ($k{=}10$ entity-construction comparisons), $p_{\\text{adj}}{=}0.006$; global ($k{=}57$): $p_{\\text{adj}}{=}0.055$; the family partition was not pre-registered (Appendix~\\ref{app:holm}).\ndocs/paper/sections/experiments_main.tex:113:The degeneracy decomposition (\\S\\ref{sec:theory}) identifies $\\alpha$---not degeneracy---as the binding constraint ($8$--$33{\\times}$ tighter); this persists across families \\cite{yun2025price}, scales (4B--72B), and decoding modes (Appendix~\\ref{app:freeform_ablation}).\ndocs/paper/sections/introduction.tex:3:Test-time compute scaling---self-consistency \\cite{wang2023selfconsistency}, best-of-$N$ \\cite{snell2025scaling, brown2024monkeys}, extended reasoning \\cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.\ndocs/paper/sections/introduction.tex:4:For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \\cite{yao2026consistency} and qualitative diversity collapse \\cite{yun2025price} but no instance-level diagnostic framework.\ndocs/paper/sections/introduction.tex:8:A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\\textendash$0.88$; Appendix~\\ref{sec:mechanistic}), exposing an \\textit{introspection boundary} \\cite{huang2024large}.\ndocs/paper/sections/introduction.tex:26:QE signals achieve AUROC up to $0.82$; while \\citet{yao2026consistency} report task-level correlation ($\\rho$ up to 0.47), our instance-level decomposition reveals why correlation does not yield selection gains.\ndocs/paper/sections/introduction.tex:28:A diagnostic cascade---degeneracy, LP compression, signal alignment---quantifies failure mechanisms at entity level; \\citet{yun2025price} describe diversity collapse qualitatively, we provide quantitative decomposition ($D$, $\\alpha$, LP range). A necessary condition bound (\\S\\ref{sec:theory}) confirms $\\alpha$ as the binding constraint (3--12\\% recovery ratio). Hidden-state probes reveal an introspection boundary (AUROC $0.63$--$0.88$ vs.\\ ESJ $\\approx 0.50$; Appendix~\\ref{sec:mechanistic}).\ndocs/paper/sections/introduction.tex:30:Entity-level construction yields $+1.40$\\,pp on Few-NERD where the cascade identifies favorable conditions. Unlike \\citet{xie2023zeroshot}'s zero-shot entity voting, we aggregate stochastic samples from fine-tuned models.",
    "numLines": 67
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0126wjvoHgytUhxMT6yLbjjL`</summary>

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
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "fa854670-1af2-44e5-acfa-b213b2aa9b0a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YokuTtw7KDU1pZnTFNtEE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11863,
      "cache_read_input_tokens": 24533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11863
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

_source line 15 · 2026-05-23T16:52:39.894Z_

<details><summary>↩ Tool result · `toolu_0126wjvoHgytUhxMT6yLbjjL`</summary>

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
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "b96ea3e5-d8b3-46e0-a530-7efca54d561a",
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

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now let me extract all cited keys from the grep output and compare with bib keys. Let me first collect all cited keys.

From the grep output, the cited keys are:
- wang2023selfconsistency
- snell2025scaling
- brown2024monkeys
- taubenfeld2025cisc
- kang2025selfcertainty
- gao2023scaling
- cobbe2021verifiers
- lightman2024verify
- yao2026consistency
- xie2023zeroshot
- yun2025price
- zhou2024uniner
- sainz2024gollie


- willard2023guided
- dong2024xgrammar
- eikema2022sampling
- eikema2025structured
- kuhn2023semantic
- geng2024confidence
- xia2025survey
- geifman2017selective
- madaan2023selfrefine
- luan2018scierc
- tjongkimsang2003conll
- ding2021fewnerd
- derczynski2017wnut
- zheng2024llamafactory
- fleiss1971agreement
- kumar2004minimum
- eikema2020map
- dembczynski2011exact
- chen2023twofailures
- chen2024usc
- thirukovalluru2024atomic
- shinn2023reflexion
- li2026rewardtail
- ratinov2009design
- bergkirkpatrick2012empirical
- landesberg2026bon
- kadavath2022language
- tian2023calibration
- yee2019noisy
- malinin2021uncertainty
- desai2020calibration
- xiao2022uncertainty
- angelopoulos2023conformal
- holm1979simple
- muennighoff2025s1
- huang2024large
- lin2022teaching
- platt1999probabilistic
- guo2017calibration
- muller2021understanding
- freitag2022high
- jinnai2024mbr
- li2023stepaware
- aggarwal2023adaptive
- farquhar2024detecting
- xie2024selfimproving
- li2024simple

Now I'm updating the bibliography with the new set of keys, incorporating the additional references like min2023factscore, xiong2024verbalized, brown2024monkeys, cobbe2021verifiers, and several others focused on semantic understanding, confidence estimation, and self-improvement approaches. I'm continuing through the bibliography and checking for citations I might have missed, then scanning for any entries that appear in the references but aren't actually cited anywhere in the document—looks like min2023factscore is one that's defined but never used. Now I'm going through the cited references and confirming they all appear in the grep output - these are all properly cited in the paper. Finishing up the citation checklist and noticing there are some orphaned references that aren't cited anywhere in the document. I should double-check the archived file to make sure I'm not missing anything before finalizing which papers actually need to be included.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "2f77c3b5-8e20-48c4-b42f-9de02b3d97f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

_source line 17_

Now let me search for the 6 entries to verify. I'll launch these in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "54aae91c-9959-4454-963e-2f5994467635",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015RTN9SArEaeeg4mB3fVqvr`</summary>

```json
{
  "query": "Müller Sennrich \"Understanding the Properties of Minimum Bayes Risk Decoding\" ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "6be99b9f-e4b0-4b73-b240-5dcbbc64f5c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H2YwTMmW3m1s72WEN4UnvF`</summary>

```json
{
  "query": "Kumar Byrne \"Minimum Bayes-Risk Decoding for Statistical Machine Translation\" HLT-NAACL 2004"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "e01e30ea-304a-42a9-845c-6349565b6771",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KTA29AKnomKeV4VtiHZpK6`</summary>

```json
{
  "query": "Dembczynski Waegeman Cheng Hüllermeier \"exact algorithm F-measure maximization\" NeurIPS 2011"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "601693c1-ab24-40c8-9a2b-beabb6f2f195",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFHiJRRe8m5g9BSXjZBtwN`</summary>

```json
{
  "query": "Madaan Tandon \"Self-Refine Iterative Refinement with Self-Feedback\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "e2135c3b-f7c5-4606-89af-9d96b04fb545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FLJhtNzrRAbSfRqptqkynT`</summary>

```json
{
  "query": "Kuleshov Deshpande \"Calibrated Structured Prediction\" NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "f0d86959-55b3-4894-b5b9-985713ef103f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BUCRqXgTd5Yre8AUw2J7ha`</summary>

```json
{
  "query": "Shinn Cassano Gopinath Narasimhan Yao \"Reflexion language agents verbal reinforcement learning\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "5e04723a-f99c-4e80-b213-c5e82bf98856",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EnTB2ghnJD5TidtZRxT1Ln",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7546,
      "cache_read_input_tokens": 36396,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7546
      },
      "output_tokens": 19,
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

_source line 24 · 2026-05-23T16:53:27.606Z_

<details><summary>↩ Tool result · `toolu_015RTN9SArEaeeg4mB3fVqvr`</summary>

```text
Web search results for query: "Müller Sennrich "Understanding the Properties of Minimum Bayes Risk Decoding" ACL 2021"

Links: [{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.22/"},{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - Zurich Open Repository and Archive","url":"https://www.zora.uzh.ch/id/eprint/208880/"},{"title":"Minimum Bayes Risk Decoding","url":"https://suzyahyah.github.io/bayesian%20inference/machine%20translation/2022/02/15/mbr-decoding.html"},{"title":"GitHub - ZurichNLP/understanding-mbr · GitHub","url":"https://github.com/ZurichNLP/understanding-mbr"},{"title":"[PDF] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Understanding-the-Properties-of-Minimum-Bayes-Risk-M%C3%BCller-Sennrich/af59aeeb46fb5d8412f550f6dd5c5dc99afc9c1a"},{"title":"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210508504M/abstract"},{"title":"(PDF) Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation","url":"https://www.researchgate.net/publication/351686312_Understanding_the_Properties_of_Minimum_Bayes_Risk_Decoding_in_Neural_Machine_Translation"},{"title":"[2105.08504] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation","url":"https://arxiv.org/abs/2105.08504"},{"title":"GitHub - ZurichNLP/mbr: Minimum Bayes Risk Decoding for Hugging Face Transformers","url":"https://github.com/ZurichNLP/mbr"}]

I found the paper for you! Here are the details:

The paper "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation" was authored by Mathias Müller and Rico Sennrich and published at ACL-IJCNLP 2021. It appeared in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 259–272.

The paper addresses the fact that Neural Machine Translation (NMT) currently exhibits biases such as producing translations that are too short and overgenerating frequent words, and shows poor robustness to copy noise in training data or domain shift, with recent work tying these shortcomings to beam search – the de facto standard inference algorithm in NMT – and proposing to use Minimum Bayes Risk (MBR) decoding on unbiased samples instead.

The authors find that MBR still exhibits a length and token frequency bias, owing to the MT metrics used as utility functions, but that MBR also increases robustness against copy noise in the training data and domain shift.

The paper is available at the ACL Anthology (https://aclanthology.org/2021.acl-long.22/) and on arXiv (https://arxiv.org/abs/2105.08504).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "22a8fe77-892b-4e86-aa32-a440661e5b3e",
  "tool_use_result": {
    "query": "Müller Sennrich \"Understanding the Properties of Minimum Bayes Risk Decoding\" ACL 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_011JyfZUteFJYQS3ta2n6ebu",
        "content": [
          {
            "title": "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - ACL Anthology",
            "url": "https://aclanthology.org/2021.acl-long.22/"
          },
          {
            "title": "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - Zurich Open Repository and Archive",
            "url": "https://www.zora.uzh.ch/id/eprint/208880/"
          },
          {
            "title": "Minimum Bayes Risk Decoding",
            "url": "https://suzyahyah.github.io/bayesian%20inference/machine%20translation/2022/02/15/mbr-decoding.html"
          },
          {
            "title": "GitHub - ZurichNLP/understanding-mbr · GitHub",
            "url": "https://github.com/ZurichNLP/understanding-mbr"
          },
          {
            "title": "[PDF] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Understanding-the-Properties-of-Minimum-Bayes-Risk-M%C3%BCller-Sennrich/af59aeeb46fb5d8412f550f6dd5c5dc99afc9c1a"
          },
          {
            "title": "Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210508504M/abstract"
          },
          {
            "title": "(PDF) Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation",
            "url": "https://www.researchgate.net/publication/351686312_Understanding_the_Properties_of_Minimum_Bayes_Risk_Decoding_in_Neural_Machine_Translation"
          },
          {
            "title": "[2105.08504] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation",
            "url": "https://arxiv.org/abs/2105.08504"
          },
          {
            "title": "GitHub - ZurichNLP/mbr: Minimum Bayes Risk Decoding for Hugging Face Transformers",
            "url": "https://github.com/ZurichNLP/mbr"
          }
        ]
      },
      "I found the paper for you! Here are the details:\n\nThe paper \"Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation\" was authored by Mathias Müller and Rico Sennrich and published at ACL-IJCNLP 2021. It appeared in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 259–272.\n\nThe paper addresses the fact that Neural Machine Translation (NMT) currently exhibits biases such as producing translations that are too short and overgenerating frequent words, and shows poor robustness to copy noise in training data or domain shift, with recent work tying these shortcomings to beam search – the de facto standard inference algorithm in NMT – and proposing to use Minimum Bayes Risk (MBR) decoding on unbiased samples instead.\n\nThe authors find that MBR still exhibits a length and token frequency bias, owing to the MT metrics used as utility functions, but that MBR also increases robustness against copy noise in the training data and domain shift.\n\nThe paper is available at the ACL Anthology (https://aclanthology.org/2021.acl-long.22/) and on arXiv (https://arxiv.org/abs/2105.08504)."
    ],
    "durationSeconds": 5.309930198000002
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T16:53:28.460Z_

<details><summary>↩ Tool result · `toolu_01H2YwTMmW3m1s72WEN4UnvF`</summary>

```text
Web search results for query: "Kumar Byrne "Minimum Bayes-Risk Decoding for Statistical Machine Translation" HLT-NAACL 2004"

Links: [{"title":"Minimum Bayes-Risk Decoding for Statistical Machine Translation - ACL Anthology","url":"https://aclanthology.org/N04-1022/"},{"title":"Minimum Bayes Risk","url":"http://www2.statmt.org/survey/Topic/MinimumBayesRisk"},{"title":"Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation","url":"https://research.google.com/pubs/archive/34628.pdf"},{"title":"(PDF) Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation","url":"https://www.academia.edu/6354227/Lattice_Minimum_Bayes_Risk_Decoding_for_Statistical_Machine_Translation"},{"title":"Centroid-Based Efficient Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2402.11197"},{"title":"(PDF) Minimum Bayes risk decoding for BLEU","url":"https://www.researchgate.net/publication/220874406_Minimum_Bayes_risk_decoding_for_BLEU"},{"title":"Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition","url":"https://arxiv.org/html/2510.19471v1"},{"title":"[2105.08504] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation","url":"https://ar5iv.labs.arxiv.org/html/2105.08504"},{"title":"Minimum Bayes-Risk Decoding for Statistical Machine Translation","url":"https://aclanthology.org/N04-1022.pdf"},{"title":"Minimum Bayes Risk Decoding","url":"https://suzyahyah.github.io/bayesian%20inference/machine%20translation/2022/02/15/mbr-decoding.html"}]

I found the paper you're looking for. Here are the key details:

**"Minimum Bayes-Risk Decoding for Statistical Machine Translation"** by Shankar Kumar and William Byrne, published in the Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL 2004), pages 169–176, Boston, Massachusetts, USA.

The paper is available through the ACL Anthology at https://aclanthology.org/N04-1022/, and a PDF version is also available at https://aclanthology.org/N04-1022.pdf.

This seminal work introduced the Minimum Bayes-Risk (MBR) decoding approach for statistical machine translation, which selects the output sentence that maximizes the expected metric score computed from the set of translation hypotheses, and has since become an influential technique in the machine translation field.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "69ee5e55-0200-4bcc-b517-ae7f1d745f5e",
  "tool_use_result": {
    "query": "Kumar Byrne \"Minimum Bayes-Risk Decoding for Statistical Machine Translation\" HLT-NAACL 2004",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EdzePjoamSTh6CGiaebMXX",
        "content": [
          {
            "title": "Minimum Bayes-Risk Decoding for Statistical Machine Translation - ACL Anthology",
            "url": "https://aclanthology.org/N04-1022/"
          },
          {
            "title": "Minimum Bayes Risk",
            "url": "http://www2.statmt.org/survey/Topic/MinimumBayesRisk"
          },
          {
            "title": "Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation",
            "url": "https://research.google.com/pubs/archive/34628.pdf"
          },
          {
            "title": "(PDF) Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation",
            "url": "https://www.academia.edu/6354227/Lattice_Minimum_Bayes_Risk_Decoding_for_Statistical_Machine_Translation"
          },
          {
            "title": "Centroid-Based Efficient Minimum Bayes Risk Decoding",
            "url": "https://arxiv.org/html/2402.11197"
          },
          {
            "title": "(PDF) Minimum Bayes risk decoding for BLEU",
            "url": "https://www.researchgate.net/publication/220874406_Minimum_Bayes_risk_decoding_for_BLEU"
          },
          {
            "title": "Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition",
            "url": "https://arxiv.org/html/2510.19471v1"
          },
          {
            "title": "[2105.08504] Understanding the Properties of Minimum Bayes Risk Decoding in Neural Machine Translation",
            "url": "https://ar5iv.labs.arxiv.org/html/2105.08504"
          },
          {
            "title": "Minimum Bayes-Risk Decoding for Statistical Machine Translation",
            "url": "https://aclanthology.org/N04-1022.pdf"
          },
          {
            "title": "Minimum Bayes Risk Decoding",
            "url": "https://suzyahyah.github.io/bayesian%20inference/machine%20translation/2022/02/15/mbr-decoding.html"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**\"Minimum Bayes-Risk Decoding for Statistical Machine Translation\"** by Shankar Kumar and William Byrne, published in the Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL 2004), pages 169–176, Boston, Massachusetts, USA.\n\nThe paper is available through the ACL Anthology at https://aclanthology.org/N04-1022/, and a PDF version is also available at https://aclanthology.org/N04-1022.pdf.\n\nThis seminal work introduced the Minimum Bayes-Risk (MBR) decoding approach for statistical machine translation, which selects the output sentence that maximizes the expected metric score computed from the set of translation hypotheses, and has since become an influential technique in the machine translation field."
    ],
    "durationSeconds": 5.228940214000002
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T16:53:29.387Z_

<details><summary>↩ Tool result · `toolu_01KTA29AKnomKeV4VtiHZpK6`</summary>

```text
Web search results for query: "Dembczynski Waegeman Cheng Hüllermeier "exact algorithm F-measure maximization" NeurIPS 2011"

Links: [{"title":"An Exact Algorithm for F-Measure Maximization","url":"https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html"},{"title":"An Exact Algorithm for F-Measure Maximization","url":"https://papers.nips.cc/paper/4389-an-exact-algorithm-for-f-measure-maximization"},{"title":"[PDF] An Exact Algorithm for F-Measure Maximization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Exact-Algorithm-for-F-Measure-Maximization-Dembczynski-Waegeman/211229be3e804881118ec8ab95da511df65fb4df"},{"title":"Figure 1 from An Exact Algorithm for F-Measure Maximization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Exact-Algorithm-for-F-Measure-Maximization-Dembczynski-Waegeman/211229be3e804881118ec8ab95da511df65fb4df/figure/0"},{"title":"F-Measure Maximization in Topical Classification | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-642-32115-3_52"},{"title":"GitHub - mrapp-ke/ExampleWiseF1Maximizer: A scikit-learn meta-estimator for multi-label classification that aims to maximize the example-wise F1 measure","url":"https://github.com/mrapp-ke/ExampleWiseF1Maximizer"},{"title":"(PDF) Online and Stochastic Gradient Methods for Non-decomposable Loss Functions","url":"https://www.researchgate.net/publication/267395868_Online_and_Stochastic_Gradient_Methods_for_Non-decomposable_Loss_Functions"},{"title":"Explainable AI in the Medical Field: A Survey on Machine Learning Interpretability and Use Cases | Al-Nahrain Journal of Science","url":"https://www.anjs.edu.iq/index.php/anjs/article/view/2881"},{"title":"(PDF) An Exact Algorithm for F-Measure Maximization","url":"https://www.researchgate.net/publication/228532504_An_Exact_Algorithm_for_F-Measure_Maximization"},{"title":"Advances in Neural Information Processing Systems 24","url":"https://proceedings.neurips.cc/paper/2011"}]

I found the paper you're looking for! This is "An Exact Algorithm for F-Measure Maximization" by Krzysztof J. Dembczynski, Willem Waegeman, Weiwei Cheng, and Eyke Hüllermeier, published in Advances in Neural Information Processing Systems 24 (NIPS 2011).

The paper presents an algorithm which is computationally efficient and exact regardless of the underlying distribution, requiring only a quadratic number of parameters of the joint distribution with respect to the number of binary responses. The research addresses the challenge that optimizing the F-measure has no closed-form maximizer and current algorithms are approximate, typically relying on additional assumptions regarding the statistical distribution of the binary response variables.

The paper is available through multiple sources including the official NeurIPS proceedings at https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "8ecf4e29-857b-4f54-ae66-b56fc354b907",
  "tool_use_result": {
    "query": "Dembczynski Waegeman Cheng Hüllermeier \"exact algorithm F-measure maximization\" NeurIPS 2011",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SP6jmqEmKbLdnT8cQnA3Gv",
        "content": [
          {
            "title": "An Exact Algorithm for F-Measure Maximization",
            "url": "https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html"
          },
          {
            "title": "An Exact Algorithm for F-Measure Maximization",
            "url": "https://papers.nips.cc/paper/4389-an-exact-algorithm-for-f-measure-maximization"
          },
          {
            "title": "[PDF] An Exact Algorithm for F-Measure Maximization | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/An-Exact-Algorithm-for-F-Measure-Maximization-Dembczynski-Waegeman/211229be3e804881118ec8ab95da511df65fb4df"
          },
          {
            "title": "Figure 1 from An Exact Algorithm for F-Measure Maximization | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/An-Exact-Algorithm-for-F-Measure-Maximization-Dembczynski-Waegeman/211229be3e804881118ec8ab95da511df65fb4df/figure/0"
          },
          {
            "title": "F-Measure Maximization in Topical Classification | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-642-32115-3_52"
          },
          {
            "title": "GitHub - mrapp-ke/ExampleWiseF1Maximizer: A scikit-learn meta-estimator for multi-label classification that aims to maximize the example-wise F1 measure",
            "url": "https://github.com/mrapp-ke/ExampleWiseF1Maximizer"
          },
          {
            "title": "(PDF) Online and Stochastic Gradient Methods for Non-decomposable Loss Functions",
            "url": "https://www.researchgate.net/publication/267395868_Online_and_Stochastic_Gradient_Methods_for_Non-decomposable_Loss_Functions"
          },
          {
            "title": "Explainable AI in the Medical Field: A Survey on Machine Learning Interpretability and Use Cases | Al-Nahrain Journal of Science",
            "url": "https://www.anjs.edu.iq/index.php/anjs/article/view/2881"
          },
          {
            "title": "(PDF) An Exact Algorithm for F-Measure Maximization",
            "url": "https://www.researchgate.net/publication/228532504_An_Exact_Algorithm_for_F-Measure_Maximization"
          },
          {
            "title": "Advances in Neural Information Processing Systems 24",
            "url": "https://proceedings.neurips.cc/paper/2011"
          }
        ]
      },
      "I found the paper you're looking for! This is \"An Exact Algorithm for F-Measure Maximization\" by Krzysztof J. Dembczynski, Willem Waegeman, Weiwei Cheng, and Eyke Hüllermeier, published in Advances in Neural Information Processing Systems 24 (NIPS 2011).\n\nThe paper presents an algorithm which is computationally efficient and exact regardless of the underlying distribution, requiring only a quadratic number of parameters of the joint distribution with respect to the number of binary responses. The research addresses the challenge that optimizing the F-measure has no closed-form maximizer and current algorithms are approximate, typically relying on additional assumptions regarding the statistical distribution of the binary response variables.\n\nThe paper is available through multiple sources including the official NeurIPS proceedings at https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html."
    ],
    "durationSeconds": 5.161107923000003
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-23T16:53:31.414Z_

<details><summary>↩ Tool result · `toolu_01BUCRqXgTd5Yre8AUw2J7ha`</summary>

```text
Web search results for query: "Shinn Cassano Gopinath Narasimhan Yao "Reflexion language agents verbal reinforcement learning" NeurIPS 2023"

Links: [{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"},{"title":"NeurIPS Poster Reflexion: language agents with verbal reinforcement learning","url":"https://neurips.cc/virtual/2023/poster/70114"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University","url":"https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning - New Jersey Research Community","url":"https://www.researchwithnj.com/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"},{"title":"[Paper Note] Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, NeurIPS'23, 2023.03 · Issue #512 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/512"},{"title":"[PDF] Reflexion: language agents with verbal reinforcement learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reflexion:-language-agents-with-verbal-learning-Shinn-Cassano/0671fd553dd670a4e820553a974bc48040ba0819"},{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/pdf/2303.11366"}]

I found the research paper you're looking for! Here are the key details:

**Paper Title:** Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao

**Publication:** Published in Advances in Neural Information Processing Systems 36 - 37th Conference on Neural Information Processing Systems, NeurIPS 2023

**Core Concept:** Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.

**Problem Addressed:** It remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.

The paper is available on arXiv (2303.11366) and has an official GitHub repository with code, demos, and experimental results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "8a53d342-b189-4faf-9257-23ddfbfb8365",
  "tool_use_result": {
    "query": "Shinn Cassano Gopinath Narasimhan Yao \"Reflexion language agents verbal reinforcement learning\" NeurIPS 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_014cwcoxS3u3vTi3WtfXiqJW",
        "content": [
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://github.com/noahshinn/reflexion/tree/main"
          },
          {
            "title": "NeurIPS Poster Reflexion: language agents with verbal reinforcement learning",
            "url": "https://neurips.cc/virtual/2023/poster/70114"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub",
            "url": "https://github.com/noahshinn/reflexion"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning - New Jersey Research Community",
            "url": "https://www.researchwithnj.com/en/publications/reflexion-language-agents-with-verbal-reinforcement-learning-2/"
          },
          {
            "title": "[Paper Note] Reflexion: Language Agents with Verbal Reinforcement Learning, Noah Shinn+, NeurIPS'23, 2023.03 · Issue #512 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/512"
          },
          {
            "title": "[PDF] Reflexion: language agents with verbal reinforcement learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Reflexion:-language-agents-with-verbal-learning-Shinn-Cassano/0671fd553dd670a4e820553a974bc48040ba0819"
          },
          {
            "title": "[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2303.11366"
          }
        ]
      },
      "I found the research paper you're looking for! Here are the key details:\n\n**Paper Title:** Reflexion: Language Agents with Verbal Reinforcement Learning\n\n**Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao\n\n**Publication:** Published in Advances in Neural Information Processing Systems 36 - 37th Conference on Neural Information Processing Systems, NeurIPS 2023\n\n**Core Concept:** Reflexion is a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials.\n\n**Problem Addressed:** It remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning.\n\nThe paper is available on arXiv (2303.11366) and has an official GitHub repository with code, demos, and experimental results."
    ],
    "durationSeconds": 4.539099621000001
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T16:53:32.446Z_

<details><summary>↩ Tool result · `toolu_01FLJhtNzrRAbSfRqptqkynT`</summary>

```text
Web search results for query: "Kuleshov Deshpande "Calibrated Structured Prediction" NeurIPS 2022"

Links: [{"title":"Calibrated Structured Prediction","url":"https://www.cs.cornell.edu/~kuleshov/papers/nips2015.pdf"},{"title":"CALIBRATED REGRESSION AGAINST AN ADVERSARY WITHOUT REGRET Shachi Deshpande","url":"https://arxiv.org/pdf/2302.12196"},{"title":"[PDF] Calibrated Structured Prediction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Calibrated-Structured-Prediction-Kuleshov-Liang/a068b2dc837ed925a6f4724467572c05cbeb5f98"},{"title":"Calibrated Structured Prediction","url":"https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html"},{"title":"Calibrated Structured Prediction Volodymyr Kuleshov, Percy Liang","url":"https://ai.stanford.edu/~kuleshov/papers/nips2015-poster.pdf"},{"title":"Online Calibrated and Conformal Prediction Improves Bayesian Optimization - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11482741/"},{"title":"Calibrated Structured Prediction","url":"https://papers.nips.cc/paper/5658-calibrated-structured-prediction"},{"title":"Calibrated structured prediction | Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 2","url":"https://dl.acm.org/citation.cfm?id=2969627"},{"title":"Online Calibrated and Conformal Prediction Improves Bayesian Optimization","url":"https://proceedings.mlr.press/v238/deshpande24a/deshpande24a.pdf"}]

Based on the search results, I found information about papers by Kuleshov and Deshpande, but the "Calibrated Structured Prediction" paper appears to be from NeurIPS 2015, not 2022.

The paper "Calibrated Structured Prediction" by Volodymyr Kuleshov and Percy Liang was published at NIPS 2015.

However, there are related works by Kuleshov and Deshpande from around 2022. Kuleshov and Deshpande published "Calibrated and Sharp Uncertainties in Deep Learning via Density Estimation" at the International Conference on Machine Learning in 2022, and Deshpande and Kuleshov (along with other coauthors) published "Deep Multi-Modal Structural Equations For Causal Effect Estimation With Unstructured Proxies" at Neural Information Processing Systems in 2022.

It's possible you may be looking for one of these 2022 papers, or there may have been a different publication venue or year for the work you're searching for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "e7ad0232-2a94-4fe0-8a0d-357e979e4c9f",
  "tool_use_result": {
    "query": "Kuleshov Deshpande \"Calibrated Structured Prediction\" NeurIPS 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T8aC4zCFw59d28pa7hqh1A",
        "content": [
          {
            "title": "Calibrated Structured Prediction",
            "url": "https://www.cs.cornell.edu/~kuleshov/papers/nips2015.pdf"
          },
          {
            "title": "CALIBRATED REGRESSION AGAINST AN ADVERSARY WITHOUT REGRET Shachi Deshpande",
            "url": "https://arxiv.org/pdf/2302.12196"
          },
          {
            "title": "[PDF] Calibrated Structured Prediction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Calibrated-Structured-Prediction-Kuleshov-Liang/a068b2dc837ed925a6f4724467572c05cbeb5f98"
          },
          {
            "title": "Calibrated Structured Prediction",
            "url": "https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html"
          },
          {
            "title": "Calibrated Structured Prediction Volodymyr Kuleshov, Percy Liang",
            "url": "https://ai.stanford.edu/~kuleshov/papers/nips2015-poster.pdf"
          },
          {
            "title": "Online Calibrated and Conformal Prediction Improves Bayesian Optimization - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11482741/"
          },
          {
            "title": "Calibrated Structured Prediction",
            "url": "https://papers.nips.cc/paper/5658-calibrated-structured-prediction"
          },
          {
            "title": "Calibrated structured prediction | Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 2",
            "url": "https://dl.acm.org/citation.cfm?id=2969627"
          },
          {
            "title": "Online Calibrated and Conformal Prediction Improves Bayesian Optimization",
            "url": "https://proceedings.mlr.press/v238/deshpande24a/deshpande24a.pdf"
          }
        ]
      },
      "Based on the search results, I found information about papers by Kuleshov and Deshpande, but the \"Calibrated Structured Prediction\" paper appears to be from NeurIPS 2015, not 2022.\n\nThe paper \"Calibrated Structured Prediction\" by Volodymyr Kuleshov and Percy Liang was published at NIPS 2015.\n\nHowever, there are related works by Kuleshov and Deshpande from around 2022. Kuleshov and Deshpande published \"Calibrated and Sharp Uncertainties in Deep Learning via Density Estimation\" at the International Conference on Machine Learning in 2022, and Deshpande and Kuleshov (along with other coauthors) published \"Deep Multi-Modal Structural Equations For Causal Effect Estimation With Unstructured Proxies\" at Neural Information Processing Systems in 2022.\n\nIt's possible you may be looking for one of these 2022 papers, or there may have been a different publication venue or year for the work you're searching for."
    ],
    "durationSeconds": 6.805677062999996
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-23T16:53:33.005Z_

<details><summary>↩ Tool result · `toolu_01QFHiJRRe8m5g9BSXjZBtwN`</summary>

```text
Web search results for query: "Madaan Tandon "Self-Refine Iterative Refinement with Self-Feedback" NeurIPS 2023"

Links: [{"title":"Self-Refine: Iterative Refinement with Self-Feedback","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html"},{"title":"[PDF] Self-Refine: Iterative Refinement with Self-Feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Refine:-Iterative-Refinement-with-Madaan-Tandon/3aaf6a2cbad5850ad81ab5c163599cb3d523436f"},{"title":"Self-Refine: Iterative Refinement with Self-Feedback","url":"https://selfrefine.info/"},{"title":"Self-Refine: Iterative Refinement with Self-Feedback","url":"https://github.com/madaan/self-refine"},{"title":"[2303.17651] Self-Refine: Iterative Refinement with Self-Feedback","url":"https://arxiv.org/abs/2303.17651"},{"title":"SELF-REFINE: iterative refinement with self-feedback","url":"https://dl.acm.org/doi/10.5555/3666122.3668141"},{"title":"NeurIPS Poster Self-Refine: Iterative Refinement with Self-Feedback","url":"https://neurips.cc/virtual/2023/poster/71632"},{"title":"SELF-REFINE: Iterative Refinement with Self-Feedback","url":"https://arxiv.org/pdf/2303.17651"},{"title":"SELF-REFINE: Iterative Refinement with Self-Feedback","url":"https://openreview.net/pdf?id=S37hOerQLB"}]

I found the paper you're looking for! Here's the information about "Self-Refine: Iterative Refinement with Self-Feedback":

## Paper Details

The paper is authored by Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark, and was published at Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track.

## Core Contribution

The paper introduces Self-Refine, an approach for improving initial outputs from LLMs through iterative feedback and refinement, motivated by how humans refine their written text. The main idea is to generate an initial output using an LLM; then, the same LLM provides feedback for its output and uses it to refine itself, iteratively.

## Key Features

Unlike prior work, it does not require supervised training data or reinforcement learning, and works with a single LLM. The paper evaluates Self-Refine across 7 diverse tasks ranging from dialog response generation to mathematical reasoning using state-of-the-art LLMs (GPT-3.5, ChatGPT, and GPT-4), with outputs generated using Self-Refine preferred by humans and automatic metrics, improving by approximately 20% on average.

The paper is available on arXiv (2303.17651) and the official NeurIPS proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "86a1c083-a85e-4606-b604-f5e58047de8c",
  "tool_use_result": {
    "query": "Madaan Tandon \"Self-Refine Iterative Refinement with Self-Feedback\" NeurIPS 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CYt5XNsYbux6KjVgWHgwuq",
        "content": [
          {
            "title": "Self-Refine: Iterative Refinement with Self-Feedback",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html"
          },
          {
            "title": "[PDF] Self-Refine: Iterative Refinement with Self-Feedback | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Self-Refine:-Iterative-Refinement-with-Madaan-Tandon/3aaf6a2cbad5850ad81ab5c163599cb3d523436f"
          },
          {
            "title": "Self-Refine: Iterative Refinement with Self-Feedback",
            "url": "https://selfrefine.info/"
          },
          {
            "title": "Self-Refine: Iterative Refinement with Self-Feedback",
            "url": "https://github.com/madaan/self-refine"
          },
          {
            "title": "[2303.17651] Self-Refine: Iterative Refinement with Self-Feedback",
            "url": "https://arxiv.org/abs/2303.17651"
          },
          {
            "title": "SELF-REFINE: iterative refinement with self-feedback",
            "url": "https://dl.acm.org/doi/10.5555/3666122.3668141"
          },
          {
            "title": "NeurIPS Poster Self-Refine: Iterative Refinement with Self-Feedback",
            "url": "https://neurips.cc/virtual/2023/poster/71632"
          },
          {
            "title": "SELF-REFINE: Iterative Refinement with Self-Feedback",
            "url": "https://arxiv.org/pdf/2303.17651"
          },
          {
            "title": "SELF-REFINE: Iterative Refinement with Self-Feedback",
            "url": "https://openreview.net/pdf?id=S37hOerQLB"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about \"Self-Refine: Iterative Refinement with Self-Feedback\":\n\n## Paper Details\n\nThe paper is authored by Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, and Peter Clark, and was published at Advances in Neural Information Processing Systems 36 (NeurIPS 2023) Main Conference Track.\n\n## Core Contribution\n\nThe paper introduces Self-Refine, an approach for improving initial outputs from LLMs through iterative feedback and refinement, motivated by how humans refine their written text. The main idea is to generate an initial output using an LLM; then, the same LLM provides feedback for its output and uses it to refine itself, iteratively.\n\n## Key Features\n\nUnlike prior work, it does not require supervised training data or reinforcement learning, and works with a single LLM. The paper evaluates Self-Refine across 7 diverse tasks ranging from dialog response generation to mathematical reasoning using state-of-the-art LLMs (GPT-3.5, ChatGPT, and GPT-4), with outputs generated using Self-Refine preferred by humans and automatic metrics, improving by approximately 20% on average.\n\nThe paper is available on arXiv (2303.17651) and the official NeurIPS proceedings."
    ],
    "durationSeconds": 7.829938768000007
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

````text
Let me now analyze the search results for each of the 6 entries:

### 1. muller2021understanding
**Current bib:**
```
@inproceedings{muller2021understanding,
  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},
  author = {M{\"u}ller, Mathias and Sennrich, Rico},
  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year = {2021},
  url = {https://arxiv.org/abs/2105.08504}
}
```
**Verified info:**
- Title: correct ✓
- Authors: Mathias Müller and Rico Sennrich ✓
- Year: 2021 ✓
- Venue: ACL-IJCNLP 2021 (technically "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)") — the bib entry is slightly abbreviated but acceptable

. Pages 259-272.

Overall: **No significant issues.** The venue abbreviation is acceptable.

### 2. kumar2004minimum
**Current bib:**
```
@inproceedings{kumar2004minimum,
  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},
  author = {Kumar, Shankar and Byrne, William},
  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL 2004)},
  pages = {169--176},
  year = {2004},
  url = {https://aclanthology.org/N04-1022/}
}
```
**Verified info:**
- Title: Minimum Bayes-Risk Decoding for Statistical Machine Translation ✓
- Authors: Shankar Kumar and William Byrne ✓
- Year: 2004 ✓
- Venue: HLT-NAACL 2004 ✓
- Pages: 169-176 ✓

Overall: **No issues.**

### 3. dembczynski2011exact
**Current bib:**
```
@inproceedings{dembczynski2011exact,
  title = {An Exact Algorithm for {F}-Measure Maximization},
  author = {Dembczy{\'n}ski, Krzysztof and
```

Checking the second entry against the ACL Anthology and verifying all metadata is correct. Moving on to validate the third entry's author names and publication details. The author name discrepancy is minor since middle initials vary across sources—the NeurIPS proceedings page lists it without the "J." while the actual paper includes it, but both refer to the same person. The URL appears to be cut off, but the venue and year are correctly cited as NeurIPS 2011. I'm noticing the URL hash in the bibliography doesn't match what the search results show, but that's a minor issue since the paper metadata itself—title, authors, venue, and year—all check out. The author might need a middle initial added, but overall this entry is solid. I'm noticing a discrepancy in the author names—the bibliography lists "Shyam Gupta" but multiple sources including Semantic Scholar, NeurIPS proceedings, and arXiv all show "Shashank Gupta" as the correct author name. I should update the citation to reflect the accurate author list. I found an author mismatch for the Self-Refine entry—it lists "Gupta, Shyam" but should be "Gupta, Shashank". For the Kuleshov paper, there's a bigger discrepancy: the bib says it's from NeurIPS 2022 by Kuleshov and Deshpande, but the actual "Calibrated Structured Prediction" paper is from NeurIPS 2015 and co-authored with Percy Liang instead. I need to verify what paper that 2022 URL actually points to, since the details don't match up. I've found two separate Kuleshov entries in the bibliography with identical titles but different years and co-authors, which suggests one might be mislabeled. The URL for the 2022 entry points to NeurIPS 2022 proceedings, so I need to verify what paper actually appears there and whether this is a duplicate or attribution error.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "b3149131-739a-4c26-903e-be1c3d46e101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN6tnGzzerx3utKCeZW5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1641,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 43942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6333
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

I found a discrepancy with `kuleshov2022calibrated`. Let me search more specifically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "4d63c1e4-9f9c-42a2-bf2e-b310aa742f5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN6tnGzzerx3utKCeZW5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1641,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 43942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6333
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U7C2moseFhrvSpF15X3Rqg`</summary>

```json
{
  "query": "Kuleshov Deshpande NeurIPS 2022 site:proceedings.neurips.cc"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "24edd1d6-8d75-4553-808d-374435408f51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN6tnGzzerx3utKCeZW5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1641,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 43942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6333
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019MQPm3g5BC8H7Cf811gsrL`</summary>

```json
{
  "query": "proceedings.neurips.cc paper 2022 07a4e20a7bef6ed1c439ace5a3e0a1b5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "e5946abf-3505-4d3e-8f9d-08c5160de74c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN6tnGzzerx3utKCeZW5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1641,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 43942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6333
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LhqFdFE36d8unmn4QFHaof`</summary>

```json
{
  "query": "Shinn Cassano Reflexion NeurIPS 2023 author list \"Edward Berman\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "06e227b3-2c26-4d04-aa94-47041ae4fc10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CN6tnGzzerx3utKCeZW5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1641,
      "cache_creation_input_tokens": 6333,
      "cache_read_input_tokens": 43942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6333
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

_source line 35 · 2026-05-23T16:54:27.709Z_

<details><summary>↩ Tool result · `toolu_01U7C2moseFhrvSpF15X3Rqg`</summary>

```text
Web search results for query: "Kuleshov Deshpande NeurIPS 2022 site:proceedings.neurips.cc"

Links: [{"title":"Deep Multi-Modal Structural Equations For Causal Effect Estimation With Unstructured Proxies","url":"https://proceedings.neurips.cc//paper_files/paper/2022/hash/46e654963ca9f2b9ff05d1bbfce2420c-Abstract-Conference.html"},{"title":"Revisiting the Kuleshov effect with authentic films: A behavioral and fMRI study","url":"https://www.biorxiv.org/content/10.1101/2023.12.04.569135.full.pdf"},{"title":"An analytic theory of creativity in convolutional diffusion models","url":"https://arxiv.org/pdf/2412.20292"},{"title":"Improving Diffusion Models for Inverse Problems using Manifold Constraints","url":"https://proceedings.neurips.cc/paper_files/paper/2022/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf"},{"title":"Active Learning Helps Pretrained Models Learn the Intended Task","url":"https://proceedings.neurips.cc//paper_files/paper/2022/hash/b43a0e8a35b1c044b18cd843b9771915-Abstract-Conference.html"}]

I found the paper you were looking for! The paper is titled "Deep Multi-Modal Structural Equations For Causal Effect Estimation With Unstructured Proxies" by Shachi Deshpande, Kaiwen Wang, Dhruv Sreenivas, Zheng Li, and Volodymyr Kuleshov, published at NeurIPS 2022.

The paper introduces deep multi-modal structural equations, a generative model for causal effect estimation in which confounders are latent variables and unstructured data are proxy variables.

The paper can be found at: https://proceedings.neurips.cc//paper_files/paper/2022/hash/46e654963ca9f2b9ff05d1bbfce2420c-Abstract-Conference.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "e436796e-00b5-479e-8fe5-d1fd5d35e9bf",
  "tool_use_result": {
    "query": "Kuleshov Deshpande NeurIPS 2022 site:proceedings.neurips.cc",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AwTN96BMPPUchabNxuZMfD",
        "content": [
          {
            "title": "Deep Multi-Modal Structural Equations For Causal Effect Estimation With Unstructured Proxies",
            "url": "https://proceedings.neurips.cc//paper_files/paper/2022/hash/46e654963ca9f2b9ff05d1bbfce2420c-Abstract-Conference.html"
          },
          {
            "title": "Revisiting the Kuleshov effect with authentic films: A behavioral and fMRI study",
            "url": "https://www.biorxiv.org/content/10.1101/2023.12.04.569135.full.pdf"
          },
          {
            "title": "An analytic theory of creativity in convolutional diffusion models",
            "url": "https://arxiv.org/pdf/2412.20292"
          },
          {
            "title": "Improving Diffusion Models for Inverse Problems using Manifold Constraints",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2022/file/a48e5877c7bf86a513950ab23b360498-Paper-Conference.pdf"
          },
          {
            "title": "Active Learning Helps Pretrained Models Learn the Intended Task",
            "url": "https://proceedings.neurips.cc//paper_files/paper/2022/hash/b43a0e8a35b1c044b18cd843b9771915-Abstract-Conference.html"
          }
        ]
      },
      "I found the paper you were looking for! The paper is titled \"Deep Multi-Modal Structural Equations For Causal Effect Estimation With Unstructured Proxies\" by Shachi Deshpande, Kaiwen Wang, Dhruv Sreenivas, Zheng Li, and Volodymyr Kuleshov, published at NeurIPS 2022.\n\nThe paper introduces deep multi-modal structural equations, a generative model for causal effect estimation in which confounders are latent variables and unstructured data are proxy variables.\n\nThe paper can be found at: https://proceedings.neurips.cc//paper_files/paper/2022/hash/46e654963ca9f2b9ff05d1bbfce2420c-Abstract-Conference.html"
    ],
    "durationSeconds": 5.271473400999995
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T16:54:30.230Z_

<details><summary>↩ Tool result · `toolu_01LhqFdFE36d8unmn4QFHaof`</summary>

```text
Web search results for query: "Shinn Cassano Reflexion NeurIPS 2023 author list "Edward Berman""

Links: [{"title":"reflexion/README.md at main · noahshinn/reflexion","url":"https://github.com/noahshinn/reflexion/blob/main/README.md"},{"title":"GitHub - RbKomar/reflexion-forked: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/RbKomar/reflexion-forked"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://github.com/noahshinn/reflexion/tree/main"},{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"https://github.com/noahshinn/reflexion | Ecosyste.ms: Awesome","url":"https://awesome.ecosyste.ms/projects/github.com/noahshinn/reflexion"},{"title":"MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs","url":"https://arxiv.org/pdf/2512.20845"},{"title":"[2303.11366v4] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366v4"},{"title":"[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning","url":"https://arxiv.org/abs/2303.11366"},{"title":"Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn","url":"https://arxiv.org/pdf/2303.11366"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Reflexion:+Language+agents+with+verbal+reinforcement+learning&amp=&publication_year=2023&amp=&author=N.+Shinn&amp=&author=F.+Cassano&amp=&author=E.+Berman&amp=&author=A.+Gopinath&amp=&author=K.+Narasimhan&amp=&author=S.+Yao"}]

Based on the search results, I can confirm the author list for the "Reflexion: Language Agents with Verbal Reinforcement Learning" paper presented at NeurIPS 2023:

The authors are Noah Shinn (Northeastern University), Federico Cassano (Northeastern University), Edward Berman (Northeastern University), Ashwin Gopinath (Massachusetts Institute of Technology), Karthik Narasimhan (Princeton University), and Shunyu Yao (Princeton University).

Yes, Edward Berman is confirmed as one of the authors on this NeurIPS 2023 paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "4cb79e56-abec-4744-bcc8-c92f4d62b1ab",
  "tool_use_result": {
    "query": "Shinn Cassano Reflexion NeurIPS 2023 author list \"Edward Berman\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SCv2ZYeDCyx6LAevhpfQZM",
        "content": [
          {
            "title": "reflexion/README.md at main · noahshinn/reflexion",
            "url": "https://github.com/noahshinn/reflexion/blob/main/README.md"
          },
          {
            "title": "GitHub - RbKomar/reflexion-forked: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://github.com/RbKomar/reflexion-forked"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://github.com/noahshinn/reflexion/tree/main"
          },
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub",
            "url": "https://github.com/noahshinn/reflexion"
          },
          {
            "title": "https://github.com/noahshinn/reflexion | Ecosyste.ms: Awesome",
            "url": "https://awesome.ecosyste.ms/projects/github.com/noahshinn/reflexion"
          },
          {
            "title": "MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs",
            "url": "https://arxiv.org/pdf/2512.20845"
          },
          {
            "title": "[2303.11366v4] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366v4"
          },
          {
            "title": "[2303.11366] Reflexion: Language Agents with Verbal Reinforcement Learning",
            "url": "https://arxiv.org/abs/2303.11366"
          },
          {
            "title": "Reflexion: Language Agents with Verbal Reinforcement Learning Noah Shinn",
            "url": "https://arxiv.org/pdf/2303.11366"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=Reflexion:+Language+agents+with+verbal+reinforcement+learning&amp=&publication_year=2023&amp=&author=N.+Shinn&amp=&author=F.+Cassano&amp=&author=E.+Berman&amp=&author=A.+Gopinath&amp=&author=K.+Narasimhan&amp=&author=S.+Yao"
          }
        ]
      },
      "Based on the search results, I can confirm the author list for the \"Reflexion: Language Agents with Verbal Reinforcement Learning\" paper presented at NeurIPS 2023:\n\nThe authors are Noah Shinn (Northeastern University), Federico Cassano (Northeastern University), Edward Berman (Northeastern University), Ashwin Gopinath (Massachusetts Institute of Technology), Karthik Narasimhan (Princeton University), and Shunyu Yao (Princeton University).\n\nYes, Edward Berman is confirmed as one of the authors on this NeurIPS 2023 paper."
    ],
    "durationSeconds": 6.860914756000013
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-23T16:54:31.387Z_

<details><summary>↩ Tool result · `toolu_019MQPm3g5BC8H7Cf811gsrL`</summary>

```text
Web search results for query: "proceedings.neurips.cc paper 2022 07a4e20a7bef6ed1c439ace5a3e0a1b5"

Links: [{"title":"Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal","url":"https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"},{"title":"NeurIPS 2022 Papers","url":"https://neurips.cc/virtual/2022/papers.html"},{"title":"Structured Clinical Reasoning Prompt Enhances LLM’s Diagnostic Capabilities in Diagnosis Please Quiz Cases","url":"https://www.medrxiv.org/content/10.1101/2024.09.01.24312894.full.pdf"},{"title":"Development of meta-prompts for Large Language Models to screen titles and abstracts for diagnostic test accuracy reviews","url":"https://www.medrxiv.org/content/10.1101/2023.10.31.23297818.full.pdf"},{"title":"Vision-Language Models vs Autonomous AI Agents for Anterior Capsular Radial Folds: A Diagnostic Study","url":"https://www.medrxiv.org/content/10.64898/2026.01.15.26344200.full.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"},{"title":"The Predictability of the Necessity for Cardiology Consultation in Patients Scheduled for Non-Cardiac Surgery Using Artificial Intelligence Models in Preoperative Anesthesia Assessment","url":"https://cdn.clinicaltrials.gov/large-docs/13/NCT07395713/SAP_000.pdf"},{"title":"Hybrid rule-based and on-premises LLM pipeline for extracting CMR and CPET metrics from free-text reports in repaired tetralogy of Fallot","url":"https://www.medrxiv.org/content/10.64898/2026.01.21.26344531.full.pdf"}]

The search didn't return direct results for that specific NeurIPS paper. Let me try a more targeted search for that paper ID:

Links: [{"title":"Illusions of Alignment Between Large Language Models and Brains Emerge From Fragile Methods and Overlooked Confounds","url":"https://www.biorxiv.org/content/10.1101/2025.03.09.642245.full.pdf"},{"title":"Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal","url":"https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"},{"title":"Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews","url":"https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"},{"title":"NeurIPS 2022 Call for Papers","url":"https://neurips.cc/Conferences/2022/CallForPapers"},{"title":"Evaluating large language models for natural-language-to-code generation on aggregate Czech public health data analysis","url":"https://www.medrxiv.org/content/10.64898/2025.12.05.25341697.full.pdf"},{"title":"Call for Papers - NeurIPS 2022","url":"https://nips.cc/Conferences/2022/CallForPapers"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"Automated Identification of Heart Failure with Reduced Ejection Fraction using Deep Learning-based Natural Language Processing","url":"https://www.medrxiv.org/content/10.1101/2023.09.10.23295315.full.pdf"}]

I apologize, but the search results did not return the specific NeurIPS 2022 paper you're looking for with that paper ID (07a4e20a7bef6ed1c439ace5a3e0a1b5). The paper hash/ID doesn't appear in the available web search results.

To find this specific NeurIPS 2022 paper, you might want to try:

1. **Visiting the NeurIPS proceedings directly**: Go to https://proceedings.neurips.cc/ and navigate to the 2022 papers
2. **Using the full paper ID in the URL format**: Try accessing it directly at something like `https://proceedings.neurips.cc/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5`
3. **Searching on OpenReview**: NeurIPS papers are often indexed at https://openreview.net/
4. **Trying arXiv**: If the paper was posted on arXiv, you might find it there with a broader search

If you have the paper title or authors, I could help search for it using that information instead.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "d5f983a7-2b32-4f20-ae6a-6546ad8d0985",
  "tool_use_result": {
    "query": "proceedings.neurips.cc paper 2022 07a4e20a7bef6ed1c439ace5a3e0a1b5",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T7ieRzTWWFanUpud9P3fZp",
        "content": [
          {
            "title": "Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal",
            "url": "https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"
          },
          {
            "title": "NeurIPS 2022 Papers",
            "url": "https://neurips.cc/virtual/2022/papers.html"
          },
          {
            "title": "Structured Clinical Reasoning Prompt Enhances LLM’s Diagnostic Capabilities in Diagnosis Please Quiz Cases",
            "url": "https://www.medrxiv.org/content/10.1101/2024.09.01.24312894.full.pdf"
          },
          {
            "title": "Development of meta-prompts for Large Language Models to screen titles and abstracts for diagnostic test accuracy reviews",
            "url": "https://www.medrxiv.org/content/10.1101/2023.10.31.23297818.full.pdf"
          },
          {
            "title": "Vision-Language Models vs Autonomous AI Agents for Anterior Capsular Radial Folds: A Diagnostic Study",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.15.26344200.full.pdf"
          },
          {
            "title": "Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews",
            "url": "https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"
          },
          {
            "title": "The Predictability of the Necessity for Cardiology Consultation in Patients Scheduled for Non-Cardiac Surgery Using Artificial Intelligence Models in Preoperative Anesthesia Assessment",
            "url": "https://cdn.clinicaltrials.gov/large-docs/13/NCT07395713/SAP_000.pdf"
          },
          {
            "title": "Hybrid rule-based and on-premises LLM pipeline for extracting CMR and CPET metrics from free-text reports in repaired tetralogy of Fallot",
            "url": "https://www.medrxiv.org/content/10.64898/2026.01.21.26344531.full.pdf"
          }
        ]
      },
      "The search didn't return direct results for that specific NeurIPS paper. Let me try a more targeted search for that paper ID:",
      {
        "tool_use_id": "srvtoolu_012vPuN7sxz96N9kvbckcCZu",
        "content": [
          {
            "title": "Illusions of Alignment Between Large Language Models and Brains Emerge From Fragile Methods and Overlooked Confounds",
            "url": "https://www.biorxiv.org/content/10.1101/2025.03.09.642245.full.pdf"
          },
          {
            "title": "Performance of o1 pro and GPT-4 in self-assessment questions for nephrology board renewal",
            "url": "https://www.medrxiv.org/content/10.1101/2025.01.14.25320525.full.pdf"
          },
          {
            "title": "Collaborative Large Language Models for Automated Data Extraction in Living Systematic Reviews",
            "url": "https://www.medrxiv.org/content/10.1101/2024.09.20.24314108.full.pdf"
          },
          {
            "title": "NeurIPS 2022 Call for Papers",
            "url": "https://neurips.cc/Conferences/2022/CallForPapers"
          },
          {
            "title": "Evaluating large language models for natural-language-to-code generation on aggregate Czech public health data analysis",
            "url": "https://www.medrxiv.org/content/10.64898/2025.12.05.25341697.full.pdf"
          },
          {
            "title": "Call for Papers - NeurIPS 2022",
            "url": "https://nips.cc/Conferences/2022/CallForPapers"
          },
          {
            "title": "Performance of reasoning large language models on nephrology multiple-choice questions",
            "url": "https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"
          },
          {
            "title": "Automated Identification of Heart Failure with Reduced Ejection Fraction using Deep Learning-based Natural Language Processing",
            "url": "https://www.medrxiv.org/content/10.1101/2023.09.10.23295315.full.pdf"
          }
        ]
      },
      "I apologize, but the search results did not return the specific NeurIPS 2022 paper you're looking for with that paper ID (07a4e20a7bef6ed1c439ace5a3e0a1b5). The paper hash/ID doesn't appear in the available web search results.\n\nTo find this specific NeurIPS 2022 paper, you might want to try:\n\n1. **Visiting the NeurIPS proceedings directly**: Go to https://proceedings.neurips.cc/ and navigate to the 2022 papers\n2. **Using the full paper ID in the URL format**: Try accessing it directly at something like `https://proceedings.neurips.cc/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5`\n3. **Searching on OpenReview**: NeurIPS papers are often indexed at https://openreview.net/\n4. **Trying arXiv**: If the paper was posted on arXiv, you might find it there with a broader search\n\nIf you have the paper title or authors, I could help search for it using that information instead."
    ],
    "durationSeconds": 8.852254471000021
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Now I have more information. Let me look more carefully at the NeurIPS 2022 URL for `kuleshov2022calibrated`. The URL `https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html` — I need to check what paper this is. Let me try to fetch that URL.

Actually, it might not be findable through search. Let me try to search for it differently.

Let me summarize my findings and check what's needed:


- `muller2021understanding` looks good — authors, title, year, and venue are all correct, and the abbreviated booktitle is acceptable
- `kumar2004minimum` has no issues
- `dembczynski2011exact` has a potential URL hash mismatch — the bib entry might be pointing to a different paper than what the search results show
- Now I need to examine `madaan2023selfref`

For entry 4, there's an author name error — it should be "Shashank Gupta" not "Shyam Gupta". Entry 5 is more problematic: the `kuleshov2022calibrated` entry claims to be about "Calibrated Structured Prediction" by Kuleshov and Deshpande at NeurIPS 2022, but that paper doesn't actually exist. The real "Calibrated Structured Prediction" is by Kuleshov and Liang from NeurIPS 2015, which is already in the bibliography as `kuleshov2015calibrated`. This looks like a duplicate or ghost entry with incorrect metadata. Let me verify whether `kuleshov2022calibrated` is actually cited anywhere in the paper, since neither this entry nor the 2015 version appear in my citation search results. Looking at the grep results more carefully, I'm confirming that several entries don't appear in any citations throughout the tex files: both kuleshov entries, min2023factscore, xiong2024verbalized, akul2023selfcheckgpt, chen2021codex, fisch2021conformal, varshney2022selective, vazhentsev2022uncertainty, zhang2023ener, he2024uncertainty, and denero2009fast are all orphans. The grep search already covered the archived directory, so these are definitely unused references.

I'm also noticing an author discrepancy in the inn2023reflexion entry — the bibliography lists Shinn, Cassano, Gopinath, Narasimhan, and Yao, but the actual paper includes Edward Berman as a co-author, so that's a missing name I need to flag. Since kuleshov2022calibrated is an orphan anyway, I'll remove it entirely rather than trying to verify its URL.

Now I'm compiling the full list of cited entries to identify which bibliography items are actually referenced in the document. Adding more bibliography entries... I'm going through the remaining citations and identifying which ones appear in the bibliography but aren't actually referenced in the paper—there are quite a few orphaned entries that should probably be removed.

Now I need to verify these more carefully by checking the actual tex files, including the archived directory, to make sure I haven't missed any citations. Let me look at what's actually being compiled in main.tex and whether those archived files are even included in the build.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "135dbd8c-455c-4795-8e9d-735629d0442e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCstfCaCdVtxYeAGYn3CPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 6520,
      "cache_read_input_tokens": 50275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6520
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

_source line 39_

Let me verify the orphan candidates by grepping specifically for them, and also check main.tex to see which files are compiled.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "67edfee6-d252-4eff-a64c-ce1b535a4ebd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCstfCaCdVtxYeAGYn3CPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 6520,
      "cache_read_input_tokens": 50275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6520
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

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_016tJsgwbMEqustEpwNrCagT`</summary>

```json
{
  "pattern": "kuleshov|min2023|xiong2024|manakul|chen2021codex|fisch2021|varshney|vazhentsev|zhang2023ener|he2024uncertainty|denero2009",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "ce3616e5-499b-433c-9669-8ca64d14e4cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCstfCaCdVtxYeAGYn3CPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 6520,
      "cache_read_input_tokens": 50275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6520
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

_source line 41 · 2026-05-23T16:55:29.853Z_

<details><summary>↩ Tool result · `toolu_016tJsgwbMEqustEpwNrCagT`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "6a67abfb-cb4d-4c14-af10-cf3860a16e01",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01W3ocJVNhUwBqneb3Si3hfX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "0b249923-aa5f-475f-8e90-84f96c300eba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCstfCaCdVtxYeAGYn3CPR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 787,
      "cache_creation_input_tokens": 6520,
      "cache_read_input_tokens": 50275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6520
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

_source line 43 · 2026-05-23T16:55:30.619Z_

<details><summary>↩ Tool result · `toolu_01W3ocJVNhUwBqneb3Si3hfX`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/background}
38	\input{sections/diagnostic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	
44	\section*{Limitations}
45	\input{sections/limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\renewcommand{\thesection}{\alphalph{\value{section}}}
51	\input{sections/appendix}
52	
53	\end{document}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "06d9a90d-f851-490b-bb5d-019ee087851a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{corollary}{Corollary}\n\\newtheorem{definition}{Definition}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{alphalph}\n\\usepackage{enumitem}\n\n\\graphicspath{{figures/}}\n\n\\title{When Self-Consistency Fails for NER:\\\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/background}\n\\input{sections/diagnostic}\n\\input{sections/single_signal}\n\\input{sections/adaptive}\n\\input{sections/theory}\n\\input{sections/experiments_main}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\renewcommand{\\thesection}{\\alphalph{\\value{section}}}\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Good. Confirmed:
1. None of the orphan candidates appear in any .tex file
2. main.tex does NOT input the _archived file (it uses `sections/experiments_main` not `sections/_archived/experiments_OLD`)

So the orphan entries are confirmed:
1. min2023factscore
2. xiong2024verbalized
3. manakul2023selfcheckgpt
4. kuleshov2015calibrated
5. chen2021codex
6. fisch2021conformal
7. varshney2022selective
8. vazhentsev2022uncertainty


9. kuleshov2022calibrated
10. zhang2023ener
11. he2024uncertainty
12. denero2009fast

Now I need to verify the URL for dembczynski2011exact. The bibliography has one URL but the search results indicate a different one, so I should update it to the correct version. I need to add "Berman, Edward" to the shinn2023reflexion entry between "Cassano, Federico" and "Gopinath, Ashwin", fix the URL hash in dembczynski2011exact, remove the kuleshov2022calibrated entry since it's both orphaned and has incorrect metadata, and delete all 12 orphan entries from the file. I'm identifying the specific corrections needed in the bibliography—fixing three entries and removing twelve orphaned citations that are no longer referenced in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "38d9ea26-5f31-481c-a178-ab2874e452a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1FkSd7nrRECwuoniXdiAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 56795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4126
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

_source line 45_

Confirmed 12 orphan entries (not cited in any compiled .tex file). Now applying corrections and deletions.

**Corrections found:**
1. `madaan2023selfrefine`: "Gupta, Shyam" → "Gupta, Shashank"
2. `shinn2023reflexion`: Missing author Edward Berman
3. `dembczynski2011exact`: Wrong URL hash
4. `muller2021understanding`: No issues
5. `kumar2004minimum`: No issues
6. `kuleshov2022calibrated`: Orphan + wrong metadata (conflates 2015 Kuleshov-Liang paper with fake 2022 entry)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "30283258-5c96-446c-a329-8ccce456646f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1FkSd7nrRECwuoniXdiAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 56795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4126
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_012wA26ZAhcVTKmMEwfHL8Z7`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shyam and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},",
  "new_string": "  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "19f0f31e-82b4-4258-bb89-5554d733b28d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1FkSd7nrRECwuoniXdiAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 56795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4126
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

_source line 47 · 2026-05-23T16:55:59.430Z_

<details><summary>↩ Tool result · `toolu_012wA26ZAhcVTKmMEwfHL8Z7`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "7ce87730-d032-43b4-aee2-66bc010f3391",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shyam and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},",
    "newString": "  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shyam and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 485,
        "oldLines": 7,
        "newStart": 485,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{madaan2023selfrefine,",
          "   title = {Self-Refine: Iterative Refinement with Self-Feedback},",
          "-  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shyam and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},",
          "+  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},",
          "   booktitle = {Advances in Neural Information Processing Systems},",
          "   year = {2023}",
          " }"
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_01MXJ3ZSTrPW1J3USxLPRM3j`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},",
  "new_string": "  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "44f206da-aba4-43fa-80f0-8467273980b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1FkSd7nrRECwuoniXdiAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 56795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4126
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

_source line 49 · 2026-05-23T16:56:00.707Z_

<details><summary>↩ Tool result · `toolu_01MXJ3ZSTrPW1J3USxLPRM3j`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "890f23aa-dfba-4978-a89e-a6a0c9d98f6d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},",
    "newString": "  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 592,
        "oldLines": 7,
        "newStart": 592,
        "newLines": 7,
        "lines": [
          " ",
          " @inproceedings{shinn2023reflexion,",
          "   title = {Reflexion: Language Agents with Verbal Reinforcement Learning},",
          "-  author = {Shinn, Noah and Cassano, Federico and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},",
          "+  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},",
          "   booktitle = {Advances in Neural Information Processing Systems},",
          "   year = {2023}",
          " }"
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01U5Vm85C5hu4c1DQFNZjDND`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}",
  "new_string": "  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "d396b45c-8500-4ab9-8dd9-ccfe192f9815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B1FkSd7nrRECwuoniXdiAD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4126,
      "cache_read_input_tokens": 56795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4126
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

_source line 51 · 2026-05-23T16:56:02.570Z_

<details><summary>↩ Tool result · `toolu_01U5Vm85C5hu4c1DQFNZjDND`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "820acef0-1744-49a3-91bb-466d49f56b5f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}",
    "newString": "  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 439,
        "oldLines": 7,
        "newStart": 439,
        "newLines": 7,
        "lines": [
          "   author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},",
          "   booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},",
          "   year = {2011},",
          "-  url = {https://proceedings.neurips.cc/paper/2011/hash/03e0704b5690a2dee1861dc3ad3316c9-Abstract.html}",
          "+  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}",
          " }",
          " ",
          " @inproceedings{denero2009fast,"
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

_source line 52_

Now deleting the 12 orphan entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "0df36e67-1d5a-4062-9a66-53e0344b4e93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 53_

<details open><summary>🔧 Tool call — Edit · `toolu_01TN9HvFhegeQCXdYWJhUuaN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "23135fa0-5a2a-4651-aa55-267fbe2d14f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 54 · 2026-05-23T16:56:08.986Z_

<details><summary>↩ Tool result · `toolu_01TN9HvFhegeQCXdYWJhUuaN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "26b36997-d5c0-4217-87ae-19c84249fa34",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n@inproceedings{min2023factscore,\n  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},\n  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  url = {https://aclanthology.org/2023.emnlp-main.741/},\n}\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 13,
        "newStart": 7,
        "newLines": 6,
        "lines": [
          "   year = {2026},",
          " }",
          " ",
          "-@inproceedings{min2023factscore,",
          "-  title = {{FActScore}: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation},",
          "-  author = {Min, Sewon and Krishna, Kalpesh and Lyu, Xinxi and Lewis, Mike and Yih, Wen-tau and Koh, Pang Wei and Iyyer, Mohit and Zettlemoyer, Luke and Hajishirzi, Hannaneh},",
          "-  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},",
          "-  year = {2023},",
          "-  url = {https://aclanthology.org/2023.emnlp-main.741/},",
          "-}",
          " ",
          " @article{holm1979simple,",
          "   title = {A Simple Sequentially Rejective Multiple Test Procedure},"
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

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_01Ldx1LnwhN9qzYp8JakFVnW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "bf92a4bc-5223-45c3-99d8-2c6aabad50e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 56 · 2026-05-23T16:56:12.620Z_

<details><summary>↩ Tool result · `toolu_01Ldx1LnwhN9qzYp8JakFVnW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "f6ab8609-7572-4bec-9ed5-f3a976886e6e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063},\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 13,
        "newStart": 18,
        "newLines": 6,
        "lines": [
          "   year = {1979},",
          " }",
          " ",
          "-@inproceedings{xiong2024verbalized,",
          "-  title = {Can {LLMs} Express Their Uncertainty? {An} Empirical Evaluation of Confidence Elicitation in {LLMs}},",
          "-  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},",
          "-  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations},",
          "-  year = {2024},",
          "-  url = {https://arxiv.org/abs/2306.13063},",
          "-}",
          " ",
          " @article{brown2024monkeys,",
          "   title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},"
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

_source line 57_

<details open><summary>🔧 Tool call — Edit · `toolu_01TsQbP8gH4DWggtnT5N8dY2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "c8f8fc5d-de4b-4a5c-a74a-42ca4e074167",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 58 · 2026-05-23T16:56:17.178Z_

<details><summary>↩ Tool result · `toolu_01TsQbP8gH4DWggtnT5N8dY2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "dcffc9f3-7031-42e4-b1ee-e01fbb65d959",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 139,
        "oldLines": 14,
        "newStart": 139,
        "newLines": 6,
        "lines": [
          "   url = {http://dx.doi.org/10.18653/v1/D18-1360}",
          " }",
          " ",
          "-@inproceedings{manakul2023selfcheckgpt,",
          "-  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},",
          "-  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},",
          "-  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},",
          "-  year = {2023},",
          "-  doi = {10.18653/v1/2023.emnlp-main.557},",
          "-  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}",
          "-}",
          " ",
          " @article{yao2026consistency,",
          "   title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},"
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

_source line 59_

<details open><summary>🔧 Tool call — Edit · `toolu_01JS2tsyawAzAmS51dEnumHc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "88c50267-9ae0-4984-a185-71664d979805",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 60 · 2026-05-23T16:56:19.195Z_

<details><summary>↩ Tool result · `toolu_01JS2tsyawAzAmS51dEnumHc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "c470b30c-c644-4635-9963-57d6f3388e76",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}\n}\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 299,
        "oldLines": 13,
        "newStart": 299,
        "newLines": 6,
        "lines": [
          "   url = {https://proceedings.mlr.press/v202/gao23h.html}",
          " }",
          " ",
          "-@inproceedings{kuleshov2015calibrated,",
          "-  title = {Calibrated Structured Prediction},",
          "-  author = {Kuleshov, Volodymyr and Liang, Percy},",
          "-  booktitle = {Advances in Neural Information Processing Systems 28 (NeurIPS)},",
          "-  year = {2015},",
          "-  url = {https://proceedings.neurips.cc/paper/2015/hash/b3b4d2dbedc99fe843fd3dedb02f086f-Abstract.html}",
          "-}",
          " ",
          " @inproceedings{platt1999probabilistic,",
          "   title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},"
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

_source line 61_

<details open><summary>🔧 Tool call — Edit · `toolu_018FDrnVeUYAaZp9q6GvFoF2`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "c80ff282-7db8-49df-8341-93321b9f0534",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 62 · 2026-05-23T16:56:21.556Z_

<details><summary>↩ Tool result · `toolu_018FDrnVeUYAaZp9q6GvFoF2`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "749ccdf6-5525-4248-a933-8fc5e747c730",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n@article{chen2021codex,\n  title = {Evaluating Large Language Models Trained on Code},\n  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},\n  journal = {arXiv preprint arXiv:2107.03374},\n  year = {2021}\n}\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 461,
        "oldLines": 12,
        "newStart": 461,
        "newLines": 6,
        "lines": [
          "   year = {2023}",
          " }",
          " ",
          "-@article{chen2021codex,",
          "-  title = {Evaluating Large Language Models Trained on Code},",
          "-  author = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and Pinto, Henrique Ponde de Oliveira and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},",
          "-  journal = {arXiv preprint arXiv:2107.03374},",
          "-  year = {2021}",
          "-}",
          " ",
          " @inproceedings{fisch2021conformal,",
          "   title = {Few-Shot Conformal Prediction with Auxiliary Tasks},"
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

_source line 63_

<details open><summary>🔧 Tool call — Edit · `toolu_01FjjJP1AwaHPMjjBaaZcMic`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "ebcd3a5a-e419-4e7d-a06a-8485f6c2279f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HoSNpesK9FEPCzdLfBLJqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2279,
      "cache_read_input_tokens": 60921,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2279
      },
      "output_tokens": 2,
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

_source line 64 · 2026-05-23T16:56:23.480Z_

<details><summary>↩ Tool result · `toolu_01FjjJP1AwaHPMjjBaaZcMic`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "af9b014a-fad2-4d41-af33-a2cc75f8d29a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {Proceedings of the 38th International Conference on Machine Learning},\n  year = {2021}\n}\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 462,
        "oldLines": 12,
        "newStart": 462,
        "newLines": 6,
        "lines": [
          " }",
          " ",
          " ",
          "-@inproceedings{fisch2021conformal,",
          "-  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},",
          "-  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},",
          "-  booktitle = {Proceedings of the 38th International Conference on Machine Learning},",
          "-  year = {2021}",
          "-}",
          " ",
          " @article{angelopoulos2023conformal,",
          "   title = {Conformal Prediction: A Gentle Introduction},"
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

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_01YUPEfy7BGGU6ZpgBWKsVu5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "bb55779f-3b24-40dd-b1d7-27e35af6d15e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sBxkQDZRQJKvFcWkDLUPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 63200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2094
      },
      "output_tokens": 73,
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

_source line 66 · 2026-05-23T16:56:29.499Z_

<details><summary>↩ Tool result · `toolu_01YUPEfy7BGGU6ZpgBWKsVu5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "8cd9c6f7-6874-4cff-835a-95deed9a9014",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n@inproceedings{varshney2022selective,\n  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},\n  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year = {2022}\n}\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 480,
        "oldLines": 12,
        "newStart": 480,
        "newLines": 6,
        "lines": [
          "   year = {2021}",
          " }",
          " ",
          "-@inproceedings{varshney2022selective,",
          "-  title = {Investigating Selective Prediction Approaches Across Several Tasks in {IID}, {OOD}, and Adversarial Settings},",
          "-  author = {Varshney, Neeraj and Mishra, Swaroop and Baral, Chitta},",
          "-  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},",
          "-  year = {2022}",
          "-}",
          " ",
          " @inproceedings{vazhentsev2022uncertainty,",
          "   title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},"
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

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_01FLc2vzpMYC3WLBjdrxycSC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "a9129b08-892e-4daa-a282-5a966ccadb35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sBxkQDZRQJKvFcWkDLUPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 63200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2094
      },
      "output_tokens": 73,
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

_source line 68 · 2026-05-23T16:56:32.501Z_

<details><summary>↩ Tool result · `toolu_01FLc2vzpMYC3WLBjdrxycSC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "60751cf4-8aa7-4ad8-ac05-485855fddbeb",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n\n@inproceedings{vazhentsev2022uncertainty,\n  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},\n  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},\n  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2022},\n  url = {https://aclanthology.org/2022.acl-long.566}\n}\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 481,
        "oldLines": 13,
        "newStart": 481,
        "newLines": 6,
        "lines": [
          " }",
          " ",
          " ",
          "-@inproceedings{vazhentsev2022uncertainty,",
          "-  title = {Uncertainty Estimation of Transformer Predictions for Misclassification Detection},",
          "-  author = {Vazhentsev, Artem and Tsymbalov, Evgenii and Shelmanov, Artem and Panchenko, Alexander},",
          "-  booktitle = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},",
          "-  year = {2022},",
          "-  url = {https://aclanthology.org/2022.acl-long.566}",
          "-}",
          " ",
          " @inproceedings{kuleshov2022calibrated,",
          "   title = {Calibrated Structured Prediction},"
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

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01ECZrxT5r9SVJmqQq7Hngmm`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "135c0b20-9249-4f21-921b-fd43e1710236",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sBxkQDZRQJKvFcWkDLUPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 63200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2094
      },
      "output_tokens": 73,
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

_source line 70 · 2026-05-23T16:56:35.790Z_

<details><summary>↩ Tool result · `toolu_01ECZrxT5r9SVJmqQq7Hngmm`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "8e4f1f35-a820-46dd-8e71-fa2e9929f9e5",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n\n\n@inproceedings{kuleshov2022calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Deshpande, Shachi},\n  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},\n  year = {2022},\n  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}\n}\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 482,
        "oldLines": 13,
        "newStart": 482,
        "newLines": 6,
        "lines": [
          " ",
          " ",
          " ",
          "-@inproceedings{kuleshov2022calibrated,",
          "-  title = {Calibrated Structured Prediction},",
          "-  author = {Kuleshov, Volodymyr and Deshpande, Shachi},",
          "-  booktitle = {Advances in Neural Information Processing Systems 35 (NeurIPS)},",
          "-  year = {2022},",
          "-  url = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/07a4e20a7bef6ed1c439ace5a3e0a1b5-Abstract-Conference.html}",
          "-}",
          " ",
          " @inproceedings{yee2019noisy,",
          "   title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},"
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

_source line 71_

<details open><summary>🔧 Tool call — Edit · `toolu_0158TekS3VfeTQrsQTeTbTfw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "ef3817ac-2c0b-4527-add4-61b3f65b1f3a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sBxkQDZRQJKvFcWkDLUPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 63200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2094
      },
      "output_tokens": 73,
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

_source line 72 · 2026-05-23T16:56:39.590Z_

<details><summary>↩ Tool result · `toolu_0158TekS3VfeTQrsQTeTbTfw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "0abe854e-5ea0-46ae-9146-6d12b52af615",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n\n\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n@inproceedings{zhang2023ener,\n  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.17854}\n}\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 499,
        "oldLines": 13,
        "newStart": 499,
        "newLines": 6,
        "lines": [
          "   url = {https://arxiv.org/abs/2206.02336}",
          " }",
          " ",
          "-@inproceedings{zhang2023ener,",
          "-  title = {{E-NER}: Evidential Deep Learning for Trustworthy Named Entity Recognition},",
          "-  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},",
          "-  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},",
          "-  year = {2023},",
          "-  url = {https://arxiv.org/abs/2305.17854}",
          "-}",
          " ",
          " @inproceedings{he2024uncertainty,",
          "   title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},"
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

_source line 73_

<details open><summary>🔧 Tool call — Edit · `toolu_0114rYLAX8cyWEt4FvrPjpAJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "f284e6e0-f707-46a4-b36d-4befbc7d49b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sBxkQDZRQJKvFcWkDLUPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 63200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2094
      },
      "output_tokens": 73,
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

_source line 74 · 2026-05-23T16:56:43.004Z_

<details><summary>↩ Tool result · `toolu_0114rYLAX8cyWEt4FvrPjpAJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "20452c48-8737-4aaf-b88d-f07a912aab50",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n\n\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n\n@inproceedings{he2024uncertainty,\n  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},\n  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.08726}\n}\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 500,
        "oldLines": 13,
        "newStart": 500,
        "newLines": 6,
        "lines": [
          " }",
          " ",
          " ",
          "-@inproceedings{he2024uncertainty,",
          "-  title = {Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission},",
          "-  author = {He, Jianfeng and Yu, Linlin and Lei, Shuo and Lu, Chang-Tien and Chen, Feng},",
          "-  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2024},",
          "-  year = {2024},",
          "-  url = {https://arxiv.org/abs/2311.08726}",
          "-}",
          " ",
          " @inproceedings{xiao2022uncertainty,",
          "   title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},"
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_01NuFwvkxFefFp3cmBwKz4NL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n",
  "new_string": "\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "f975775a-f73c-4be7-89f3-1e3a7345cec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017sBxkQDZRQJKvFcWkDLUPG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2094,
      "cache_read_input_tokens": 63200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2094
      },
      "output_tokens": 73,
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

_source line 76 · 2026-05-23T16:56:45.770Z_

<details><summary>↩ Tool result · `toolu_01NuFwvkxFefFp3cmBwKz4NL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "a085d8fa-8dc6-4666-b6f8-4aac240620ee",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n",
    "newString": "\n",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@article{landesberg2026bon,\n  title = {When {LLM} Judge Scores Look Good but Best-of-{N} Decisions Fail},\n  author = {Landesberg, Eddie},\n  journal = {arXiv preprint arXiv:2603.12520},\n  year = {2026},\n}\n\n\n@article{holm1979simple,\n  title = {A Simple Sequentially Rejective Multiple Test Procedure},\n  author = {Holm, Sture},\n  journal = {Scandinavian Journal of Statistics},\n  volume = {6},\n  number = {2},\n  pages = {65--70},\n  year = {1979},\n}\n\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {ICML 2024 Workshop on In-Context Learning},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {Proceedings of the 3rd Workshop on Noisy User-generated Text (W-NUT 2017)},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{ding2021fewnerd,\n  title = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n  author = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Hai-Tao and Liu, Zhiyuan},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages = {3198--3213},\n  year = {2021},\n  doi = {10.18653/v1/2021.acl-long.248}\n}\n\n@inproceedings{eikema2022sampling,\n  title = {Sampling-Based Approximations to Minimum {B}ayes Risk Decoding for Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing},\n  year = {2022},\n  pages = {10978--10993},\n  doi = {10.18653/v1/2022.emnlp-main.754}\n}\n\n@article{freitag2022high,\n  title = {High Quality Rather than High Model Probability: Minimum {B}ayes Risk Decoding with Neural Metrics},\n  author = {Freitag, Markus and Grangier, David and Tan, Qijun and Liang, Bowen},\n  journal = {Transactions of the Association for Computational Linguistics},\n  volume = {10},\n  year = {2022},\n  pages = {811--825},\n  doi = {10.1162/tacl_a_00491}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {Advances in Neural Information Processing Systems 38 (NeurIPS)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n\n@article{yao2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{snell2025scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {Proceedings of the Seventh Conference on Computational Natural Language Learning (CoNLL 2003)},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@inproceedings{zheng2024llamafactory,\n  title = {{L}lama{F}actory: Unified Efficient Fine-Tuning of 100+ Language Models},\n  author = {Zheng, Yaowei and Zhang, Richong and Zhang, Junhao and Ye, Yanhan and Luo, Zheyan},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)},\n  year = {2024},\n  pages = {400--410},\n  doi = {10.18653/v1/2024.acl-demos.38}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n\n@inproceedings{muller2021understanding,\n  title = {Understanding the Properties of Minimum {Bayes} Risk Decoding in Neural Machine Translation},\n  author = {M{\\\"u}ller, Mathias and Sennrich, Rico},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2021},\n  url = {https://arxiv.org/abs/2105.08504}\n}\n\n@inproceedings{eikema2025structured,\n  title = {Structure-Conditional Minimum {B}ayes Risk Decoding},\n  author = {Eikema, Bryan and Rutkiewicz, Anna and Giulianelli, Mario},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20700}\n}\n\n@inproceedings{jinnai2024mbr,\n  title = {Model-Based Minimum {B}ayes Risk Decoding for Text Generation},\n  author = {Jinnai, Yuu and Morimura, Tetsuro and Honda, Ukyo and Ariu, Kaito and Abe, Kenshi},\n  booktitle = {Proceedings of the 41st International Conference on Machine Learning (ICML)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.05263}\n}\n\n@inproceedings{ratinov2009design,\n  title = {Design Challenges and Misconceptions in Named Entity Recognition},\n  author = {Ratinov, Lev and Roth, Dan},\n  booktitle = {Proceedings of the Thirteenth Conference on Computational Natural Language Learning (CoNLL)},\n  year = {2009},\n  pages = {147--155},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{bergkirkpatrick2012empirical,\n  title = {An Empirical Investigation of Statistical Significance in {NLP}},\n  author = {Berg-Kirkpatrick, Taylor and Burkett, David and Klein, Dan},\n  booktitle = {Proceedings of the 2012 Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL)},\n  year = {2012},\n  pages = {995--1005},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{tian2023calibration,\n  title = {Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback},\n  author = {Tian, Katherine and Mitchell, Eric and Zhou, Allan and Sharma, Archit and Rafailov, Rafael and Yao, Huaxiu and Finn, Chelsea and Manning, Christopher D.},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2023},\n  pages = {5433--5442},\n  publisher = {Association for Computational Linguistics}\n}\n\n@inproceedings{yun2025price,\n  title = {The Price of Format: Diversity Collapse in {LLMs}},\n  author = {Yun, Longfei and An, Chenyang and Wang, Zilong and Peng, Letian and Shang, Jingbo},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-emnlp.836/}\n}\n\n@inproceedings{gao2023scaling,\n  title = {Scaling Laws for Reward Model Overoptimization},\n  author = {Gao, Leo and Schulman, John and Hilton, Jacob},\n  booktitle = {Proceedings of the 40th International Conference on Machine Learning (ICML)},\n  year = {2023},\n  url = {https://proceedings.mlr.press/v202/gao23h.html}\n}\n\n\n@inproceedings{platt1999probabilistic,\n  title = {Probabilistic Outputs for Support Vector Machines and Comparisons to Regularized Likelihood Methods},\n  author = {Platt, John C.},\n  booktitle = {Advances in Large Margin Classifiers},\n  pages = {61--74},\n  year = {1999},\n  publisher = {MIT Press}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {Proceedings of the 34th International Conference on Machine Learning},\n  pages = {1321--1330},\n  year = {2017}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume = {30},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@article{dong2024xgrammar,\n  title = {{XGrammar}: Flexible and Efficient Structured Generation Engine for Large Language Models},\n  author = {Dong, Yixin and Ruan, Charlie F. and Cai, Yaxing and Lai, Ruihang and Xu, Ziyi and Zhao, Yilong and Chen, Tianqi},\n  journal = {arXiv preprint arXiv:2411.15100},\n  year = {2024},\n  url = {https://arxiv.org/abs/2411.15100}\n}\n\n@article{lin2022teaching,\n  title = {Teaching Models to Express Their Uncertainty in Words},\n  author = {Lin, Stephanie and Hilton, Jacob and Evans, Owain},\n  journal = {Transactions on Machine Learning Research},\n  year = {2022},\n  url = {https://arxiv.org/abs/2205.14334}\n}\n\n@article{farquhar2024detecting,\n  title = {Detecting hallucinations in large language models using semantic entropy},\n  author = {Farquhar, Sebastian and Kossen, Jannik and Kuhn, Lorenz and Gal, Yarin},\n  journal = {Nature},\n  volume = {630},\n  pages = {625--630},\n  year = {2024},\n  doi = {10.1038/s41586-024-07421-0}\n}\n\n@article{chen2023twofailures,\n  title = {Two Failures of Self-Consistency in the Multi-Step Reasoning of {LLMs}},\n  author = {Chen, Angelica and Phang, Jason and Parrish, Alicia and Padmakumar, Vishakh and Zhao, Chen and Bowman, Samuel R. and Cho, Kyunghyun},\n  journal = {Transactions on Machine Learning Research},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.14279}\n}\n\n@inproceedings{aggarwal2023adaptive,\n  title = {Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with {LLMs}},\n  author = {Aggarwal, Pranjal and Madaan, Aman and Yang, Yiming and Mausam},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2305.11860}\n}\n\n@inproceedings{xie2023zeroshot,\n  title = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {7935--7956},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  doi = {10.18653/v1/2023.emnlp-main.493},\n  url = {https://aclanthology.org/2023.emnlp-main.493/}\n}\n\n@inproceedings{muennighoff2025s1,\n  title = {s1: Simple Test-Time Scaling},\n  author = {Muennighoff, Niklas and Yang, Zitong and Shi, Weijia and Li, Xiang Lisa and Fei-Fei, Li and Hajishirzi, Hannaneh and Zettlemoyer, Luke and Liang, Percy and Cand{\\`e}s, Emmanuel and Hashimoto, Tatsunori},\n  booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2025},\n  url = {https://arxiv.org/abs/2501.19393}\n}\n\n@inproceedings{eikema2020map,\n  title = {Is {MAP} Decoding All You Need? {T}he Inadequacy of the Mode in Neural Machine Translation},\n  author = {Eikema, Bryan and Aziz, Wilker},\n  booktitle = {Proceedings of the 28th International Conference on Computational Linguistics (COLING)},\n  pages = {4506--4520},\n  year = {2020},\n  url = {https://aclanthology.org/2020.coling-main.398/}\n}\n\n@inproceedings{kumar2004minimum,\n  title = {Minimum {B}ayes-Risk Decoding for Statistical Machine Translation},\n  author = {Kumar, Shankar and Byrne, William},\n  booktitle = {Proceedings of the Human Language Technology Conference of the North American Chapter of the Association for Computational Linguistics (HLT-NAACL)},\n  pages = {169--176},\n  year = {2004},\n  url = {https://aclanthology.org/N04-1022/}\n}\n\n@inproceedings{dembczynski2011exact,\n  title = {An Exact Algorithm for {F}-Measure Maximization},\n  author = {Dembczy{\\'n}ski, Krzysztof and Waegeman, Willem and Cheng, Weiwei and H{\\\"u}llermeier, Eyke},\n  booktitle = {Advances in Neural Information Processing Systems 24 (NeurIPS)},\n  year = {2011},\n  url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}\n}\n\n@inproceedings{denero2009fast,\n  title = {Fast Consensus Decoding over Translation Forests},\n  author = {DeNero, John and Chiang, David and Knight, Kevin},\n  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},\n  pages = {567--575},\n  year = {2009},\n  url = {https://aclanthology.org/P09-1064/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  pages = {295--302},\n  year = {2020},\n  url = {https://aclanthology.org/2020.emnlp-main.21/}\n}\n\n@inproceedings{huang2024large,\n  title = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author = {Huang, Jie and Chen, Xinyun and Mishra, Swaroop and Zheng, Huaixiu Steven and Yu, Adams Wei and Song, Xinying and Zhou, Denny},\n  booktitle = {Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://openreview.net/forum?id=IkmD3fKBPQ}\n}\n\n@inproceedings{li2024simple,\n  title = {A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction},\n  author = {Li, Yinghao and Ramprasad, Rampi and Zhang, Chao},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2402.13364}\n}\n\n@inproceedings{xie2024selfimproving,\n  title = {Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models},\n  author = {Xie, Tingyu and Li, Qi and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year = {2024}\n}\n\n@inproceedings{madaan2023selfrefine,\n  title = {Self-Refine: Iterative Refinement with Self-Feedback},\n  author = {Madaan, Aman and Tandon, Niket and Gupta, Prakhar and Hallinan, Skyler and Gao, Luyu and Wiegreffe, Sarah and Alon, Uri and Dziri, Nouha and Prabhumoye, Shrimai and Yang, Yiming and Gupta, Shashank and Majumder, Bodhisattwa Prasad and Hermann, Katherine and Welleck, Sean and Yazdanbakhsh, Amir and Clark, Peter},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n\n\n@article{angelopoulos2023conformal,\n  title = {Conformal Prediction: A Gentle Introduction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen},\n  journal = {Foundations and Trends in Machine Learning},\n  volume = {16},\n  number = {4},\n  pages = {494--591},\n  year = {2023}\n}\n\n@inproceedings{malinin2021uncertainty,\n  title = {Uncertainty Estimation in Autoregressive Structured Prediction},\n  author = {Malinin, Andrey and Gales, Mark},\n  booktitle = {Proceedings of the Ninth International Conference on Learning Representations},\n  year = {2021}\n}\n\n\n\n\n@inproceedings{yee2019noisy,\n  title = {Simple and Effective Noisy Channel Modeling for Neural Machine Translation},\n  author = {Yee, Kyra and Dauphin, Yann and Auli, Michael},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},\n  year = {2019},\n  url = {https://arxiv.org/abs/1908.05731}\n}\n\n@inproceedings{li2023stepaware,\n  title = {Making Large Language Models Better Reasoners with Step-Aware Verifier},\n  author = {Li, Yifei and Lin, Zeqi and Zhang, Shizhuo and Fu, Qiang and Chen, Bei and Lou, Jian-Guang and Chen, Weizhu},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  url = {https://arxiv.org/abs/2206.02336}\n}\n\n\n\n@inproceedings{xiao2022uncertainty,\n  title = {Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis},\n  author = {Xiao, Yuxin and Liang, Paul Pu and Bhatt, Umang and Neiswanger, Willie and Salakhutdinov, Ruslan and Morency, Louis-Philippe},\n  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2022},\n  year = {2022},\n}\n\n@article{li2026rewardtail,\n  title = {Predicting and Improving Test-Time Scaling Laws via Reward Tail-Guided Search},\n  author = {Li, Muheng and Qian, Jian and Mou, Wenlong},\n  journal = {arXiv preprint arXiv:2602.01485},\n  year = {2026},\n}\n\n@inproceedings{shinn2023reflexion,\n  title = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author = {Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 413,
        "oldLines": 14,
        "newStart": 413,
        "newLines": 6,
        "lines": [
          "   url = {https://proceedings.neurips.cc/paper/2011/hash/71ad16ad2c4d81f348082ff6c4b20768-Abstract.html}",
          " }",
          " ",
          "-@inproceedings{denero2009fast,",
          "-  title = {Fast Consensus Decoding over Translation Forests},",
          "-  author = {DeNero, John and Chiang, David and Knight, Kevin},",
          "-  booktitle = {Proceedings of the Joint Conference of the 47th Annual Meeting of the ACL and the 4th International Joint Conference on Natural Language Processing of the AFNLP (ACL-IJCNLP)},",
          "-  pages = {567--575},",
          "-  year = {2009},",
          "-  url = {https://aclanthology.org/P09-1064/}",
          "-}",
          " ",
          " @inproceedings{desai2020calibration,",
          "   title = {Calibration of Pre-trained Transformers},"
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

_source line 77_

All edits applied. Now compiling to verify.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "141a5aec-149a-4926-8f9e-1f09440c0d70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq2UfCC6vcoJryCaN9rV85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 65294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01USSd4kaASDtm4k7jzaFiYh`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && bibtex main 2>&1 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -5",
  "description": "Compile LaTeX with bibtex to verify no warnings",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "3249f5e4-884e-4354-8b2e-5f4ccabb3ca2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq2UfCC6vcoJryCaN9rV85",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2142,
      "cache_read_input_tokens": 65294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2142
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

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b86oo1091",
  "tool_use_id": "toolu_01USSd4kaASDtm4k7jzaFiYh",
  "description": "Compile LaTeX with bibtex to verify no warnings",
  "task_type": "local_bash",
  "uuid": "64e6f2ad-3738-452f-b473-66b1388e9246",
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba"
}
```

---

### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b86oo1091",
  "tool_use_id": "toolu_01USSd4kaASDtm4k7jzaFiYh",
  "status": "completed",
  "output_file": "",
  "summary": "Compile LaTeX with bibtex to verify no warnings",
  "uuid": "2e0df6b4-2c6e-4338-a812-44d6ad2732ad",
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba"
}
```

---

### Tool result

_source line 81 · 2026-05-23T16:56:56.941Z_

<details><summary>↩ Tool result · `toolu_01USSd4kaASDtm4k7jzaFiYh`</summary>

```text
e/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmri8a.pfb>
Output written on main.pdf (46 pages, 956819 bytes).
Transcript written on main.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
e/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmri8a.pfb>
Output written on main.pdf (46 pages, 956830 bytes).
Transcript written on main.log.
e/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t
imes/utmri8a.pfb>
Output written on main.pdf (46 pages, 956830 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "cea89764-8579-4579-9cb9-db6385b2ff47",
  "tool_use_result": {
    "stdout": "e/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmri8a.pfb>\nOutput written on main.pdf (46 pages, 956819 bytes).\nTranscript written on main.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\ne/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmri8a.pfb>\nOutput written on main.pdf (46 pages, 956830 bytes).\nTranscript written on main.log.\ne/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/t\nimes/utmri8a.pfb>\nOutput written on main.pdf (46 pages, 956830 bytes).\nTranscript written on main.log.",
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

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
The bibtex output doesn't show any warnings. Let me verify by checking the bibtex output more carefully - it only shows 3 lines of output, which is good (no warnings). Let me also check the .blg file for any warnings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "2a711c63-3e5e-4dd5-bd76-e878501c5480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRpMRpYexyQgxzhcf9RMrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 67436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 677
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01Whb8JQ3S9TRdXmHGjNUWuW`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.blg",
  "description": "Check bibtex log for warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "a4479ebd-c14f-422d-a60d-2ec4170292af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YRpMRpYexyQgxzhcf9RMrB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 67436,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 677
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

_source line 84 · 2026-05-23T16:57:01.633Z_

<details><summary>↩ Tool result · `toolu_01Whb8JQ3S9TRdXmHGjNUWuW`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
Capacity: max_strings=200000, hash_size=200000, hash_prime=170003
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Reallocated glb_str_ptr (elt_size=4) to 20 items from 10.
Reallocated global_strs (elt_size=200001) to 20 items from 10.
Reallocated glb_str_end (elt_size=4) to 20 items from 10.
Reallocated singl_function (elt_size=4) to 100 items from 50.
Reallocated singl_function (elt_size=4) to 100 items from 50.
Reallocated wiz_functions (elt_size=4) to 6000 items from 3000.
Database file #1: references.bib
You've used 55 entries,
            3764 wiz_defined-function locations,
            1037 strings with 21086 characters,
and the built_in function-call counts, 46140 in all, are:
= -- 3762
> -- 2748
< -- 30
+ -- 1126
- -- 847
* -- 3217
:= -- 6796
add.period$ -- 225
call.type$ -- 55
change.case$ -- 642
chr.to.int$ -- 58
cite$ -- 55
duplicate$ -- 2725
empty$ -- 3062
format.name$ -- 1024
if$ -- 9908
int.to.chr$ -- 2
int.to.str$ -- 2
missing$ -- 648
newline$ -- 279
num.names$ -- 220
pop$ -- 1805
preamble$ -- 1
purify$ -- 507
quote$ -- 0
skip$ -- 2333
stack$ -- 0
substring$ -- 1155
swap$ -- 1495
text.length$ -- 24
text.prefix$ -- 0
top$ -- 0
type$ -- 495
warning$ -- 0
while$ -- 209
width$ -- 0
write$ -- 685
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "d6adb8c3-f77a-45dd-95c2-2dba7e391564",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nCapacity: max_strings=200000, hash_size=200000, hash_prime=170003\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nReallocated glb_str_ptr (elt_size=4) to 20 items from 10.\nReallocated global_strs (elt_size=200001) to 20 items from 10.\nReallocated glb_str_end (elt_size=4) to 20 items from 10.\nReallocated singl_function (elt_size=4) to 100 items from 50.\nReallocated singl_function (elt_size=4) to 100 items from 50.\nReallocated wiz_functions (elt_size=4) to 6000 items from 3000.\nDatabase file #1: references.bib\nYou've used 55 entries,\n            3764 wiz_defined-function locations,\n            1037 strings with 21086 characters,\nand the built_in function-call counts, 46140 in all, are:\n= -- 3762\n> -- 2748\n< -- 30\n+ -- 1126\n- -- 847\n* -- 3217\n:= -- 6796\nadd.period$ -- 225\ncall.type$ -- 55\nchange.case$ -- 642\nchr.to.int$ -- 58\ncite$ -- 55\nduplicate$ -- 2725\nempty$ -- 3062\nformat.name$ -- 1024\nif$ -- 9908\nint.to.chr$ -- 2\nint.to.str$ -- 2\nmissing$ -- 648\nnewline$ -- 279\nnum.names$ -- 220\npop$ -- 1805\npreamble$ -- 1\npurify$ -- 507\nquote$ -- 0\nskip$ -- 2333\nstack$ -- 0\nsubstring$ -- 1155\nswap$ -- 1495\ntext.length$ -- 24\ntext.prefix$ -- 0\ntop$ -- 0\ntype$ -- 495\nwarning$ -- 0\nwhile$ -- 209\nwidth$ -- 0\nwrite$ -- 685",
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

_source line 85_

0 warnings, 55 entries used. 编译完全通过。

---

## 报告

### 1. 六条 BibTeX 条目核对结果

| Key | 修正内容 |
|-----|---------|
| `muller2021understanding` | 无需修改 |
| `kumar2004minimum` | 无需修改 |
| `dembczynski2011exact` | URL hash 修正：`03e0704b...` → `71ad16ad...` |
| `madaan2023selfrefine` | author 修正：`Gupta, Shyam` → `Gupta, Shashank` |
| `kuleshov2022calibrated` | 孤立条目，已删除（该条目元数据错误：标题和作者混合了 Kuleshov-Liang 2015 和 Kuleshov-Deshpande 2022 两篇不同论文） |
| `shinn2023reflexion` | author 补全：添加缺失作者 `Berman, Edward`（位于 Cassano 和 Gopinath 之间） |

### 2. 孤立条目（12 条，已全部删除）

| Key | 论文 |
|-----|------|
| `min2023factscore` | FActScore (EMNLP 2023) |
| `xiong2024verbalized` | Can LLMs Express Their Uncertainty? (ICLR 2024) |
| `manakul2023selfcheckgpt` | SelfCheckGPT (EMNLP 2023) |
| `kuleshov2015calibrated` | Calibrated Structured Prediction (NeurIPS 2015) |
| `kuleshov2022calibrated` | Calibrated Structured Prediction (错误条目) |
| `chen2021codex` | Evaluating LLMs Trained on Code |
| `fisch2021conformal` | Few-Shot Conformal Prediction (ICML 2021) |
| `varshney2022selective` | Investigating Selective Prediction (ACL 2022 Findings) |
| `vazhentsev2022uncertainty` | Uncertainty Estimation of Transformer Predictions (ACL 2022) |
| `zhang2023ener` | E-NER (ACL 2023 Findings) |
| `he2024uncertainty` | Uncertainty Estimation on Sequential Labeling (NAACL 2024 Findings) |
| `denero2009fast` | Fast Consensus Decoding (ACL-IJCNLP 2009) |

### 3. 编译结果

- bibtex: **0 warnings**，55 entries used
- pdflatex: 编译成功，46 页输出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "uuid": "3e465704-e9a0-44b7-ba7b-fe00ac842430",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Nk6Cbnd9rXdjb4KHSxSUR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 68113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 753
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

_source line 86_

0 warnings, 55 entries used. 编译完全通过。

---

## 报告

### 1. 六条 BibTeX 条目核对结果

| Key | 修正内容 |
|-----|---------|
| `muller2021understanding` | 无需修改 |
| `kumar2004minimum` | 无需修改 |
| `dembczynski2011exact` | URL hash 修正：`03e0704b...` → `71ad16ad...` |
| `madaan2023selfrefine` | author 修正：`Gupta, Shyam` → `Gupta, Shashank` |
| `kuleshov2022calibrated` | 孤立条目，已删除（该条目元数据错误：标题和作者混合了 Kuleshov-Liang 2015 和 Kuleshov-Deshpande 2022 两篇不同论文） |
| `shinn2023reflexion` | author 补全：添加缺失作者 `Berman, Edward`（位于 Cassano 和 Gopinath 之间） |

### 2. 孤立条目（12 条，已全部删除）

| Key | 论文 |
|-----|------|
| `min2023factscore` | FActScore (EMNLP 2023) |
| `xiong2024verbalized` | Can LLMs Express Their Uncertainty? (ICLR 2024) |
| `manakul2023selfcheckgpt` | SelfCheckGPT (EMNLP 2023) |
| `kuleshov2015calibrated` | Calibrated Structured Prediction (NeurIPS 2015) |
| `kuleshov2022calibrated` | Calibrated Structured Prediction (错误条目) |
| `chen2021codex` | Evaluating LLMs Trained on Code |
| `fisch2021conformal` | Few-Shot Conformal Prediction (ICML 2021) |
| `varshney2022selective` | Investigating Selective Prediction (ACL 2022 Findings) |
| `vazhentsev2022uncertainty` | Uncertainty Estimation of Transformer Predictions (ACL 2022) |
| `zhang2023ener` | E-NER (ACL 2023 Findings) |
| `he2024uncertainty` | Uncertainty Estimation on Sequential Labeling (NAACL 2024 Findings) |
| `denero2009fast` | Fast Consensus Decoding (ACL-IJCNLP 2009) |

### 3. 编译结果

- bibtex: **0 warnings**，55 entries used
- pdflatex: 编译成功，46 页输出

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 311777,
  "duration_api_ms": 348306,
  "num_turns": 33,
  "stop_reason": "end_turn",
  "session_id": "72bf4408-a79c-4eb5-86b8-c04e34d3afba",
  "total_cost_usd": 1.2730022499999998,
  "usage": {
    "input_tokens": 2440,
    "cache_creation_input_tokens": 57025,
    "cache_read_input_tokens": 548746,
    "output_tokens": 15912,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 57025,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 716,
        "cache_read_input_tokens": 68113,
        "cache_creation_input_tokens": 753,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 753
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 115378,
      "outputTokens": 3369,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 10,
      "costUSD": 0.232223,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2440,
      "outputTokens": 15912,
      "cacheReadInputTokens": 548746,
      "cacheCreationInputTokens": 57025,
      "webSearchRequests": 0,
      "costUSD": 1.04077925,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ffe24b82-201c-4f7d-ab0e-99b8d3e666ff"
}
```

</details>

---
