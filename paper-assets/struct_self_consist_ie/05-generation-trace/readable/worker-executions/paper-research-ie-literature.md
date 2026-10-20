# paper research ie literature

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 59
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_research_ie_literature_20260514T194843.log`
- **Structured JSON:** [`88715ae1d2541b4cc49b.json`](../../sessions/88/88715ae1d2541b4cc49b.json)

## Before a recorded user message

59 recorded events

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
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
  "uuid": "58510d42-a410-4658-8627-532904de2c61",
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
    "status": "allowed",
    "resetsAt": 1778800800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7e0cb2e8-93dd-41ec-b95e-c37b8da68998",
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current references.bib and literature_map.yaml to understand the existing format and content, then search for the papers to verify their information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "899669b0-bc1b-4c35-8fd9-5606e81ecbbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXHt1nTX1eCoYQCMZqPYdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
      },
      "output_tokens": 31,
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

Let me read the current files and search for the papers' information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "de8544fc-82bd-4274-abc2-64383ae86b57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXHt1nTX1eCoYQCMZqPYdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — Read · `toolu_017btJ9RnfrhbJ7o6hg69eXS`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "267c608f-365e-42e9-998e-be0ea627585e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXHt1nTX1eCoYQCMZqPYdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
      },
      "output_tokens": 31,
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

_source line 7 · 2026-05-14T19:48:57.910Z_

<details><summary>↩ Tool result · `toolu_017btJ9RnfrhbJ7o6hg69eXS`</summary>

```text
1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	% SUPPLEMENTARY — not cited in main text
12	@article{bates2021rcps,
13	  title = {Distribution-free, Risk-controlling Prediction Sets},
14	  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},
15	  journal = {Journal of the ACM},
16	  year = {2021},
17	  doi = {10.1145/3478535},
18	  url = {http://dx.doi.org/10.1145/3478535}
19	}
20	
21	@article{brown2024monkeys,
22	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
23	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
24	  journal = {arXiv preprint arXiv:2407.21787},
25	  year = {2024},
26	  url = {https://arxiv.org/abs/2407.21787}
27	}
28	
29	@inproceedings{chen2024usc,
30	  title = {Universal Self-Consistency for Large Language Model Generation},
31	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
32	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
33	  year = {2024},
34	  url = {https://arxiv.org/abs/2311.17311}
35	}
36	
37	@article{cobbe2021verifiers,
38	  title = {Training Verifiers to Solve Math Word Problems},
39	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
40	  journal = {arXiv preprint arXiv:2110.14168},
41	  year = {2021},
42	  url = {https://arxiv.org/abs/2110.14168}
43	}
44	
45	@inproceedings{culotta2004confidence,
46	  title = {Confidence Estimation for Information Extraction},
47	  author = {Culotta, Aron and McCallum, Andrew},
48	  booktitle = {HLT-NAACL 2004},
49	  year = {2004},
50	  url = {https://aclanthology.org/N04-4028/}
51	}
52	
53	@inproceedings{derczynski2017wnut,
54	  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},
55	  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},
56	  booktitle = {W-NUT Workshop at EMNLP 2017},
57	  year = {2017},
58	  url = {https://aclanthology.org/W17-4418/}
59	}
60	
61	@inproceedings{desai2020calibration,
62	  title = {Calibration of Pre-trained Transformers},
63	  author = {Desai, Shrey and Durrett, Greg},
64	  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
65	  year = {2020},
66	  doi = {10.18653/v1/2020.emnlp-main.21},
67	  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}
68	}
69	
70	% SUPPLEMENTARY — not cited in main text
71	@inproceedings{fisch2021conformal,
72	  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},
73	  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},
74	  booktitle = {ICML 2021},
75	  year = {2021},
76	  doi = {10.5555/3524938.3525234},
77	  url = {https://arxiv.org/abs/2102.08898}
78	}
79	
80	@article{fleiss1971agreement,
81	  title = {Measuring nominal scale agreement among many raters.},
82	  author = {Fleiss, Joseph L.},
83	  journal = {Psychological Bulletin},
84	  year = {1971},
85	  doi = {10.1037/h0031619},
86	  url = {http://dx.doi.org/10.1037/h0031619}
87	}
88	
89	@article{fomicheva2020unsupervised,
90	  title = {Unsupervised Quality Estimation for Neural Machine Translation},
91	  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Frédéric and Guzmán, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},
92	  journal = {Transactions of the Association for Computational Linguistics},
93	  year = {2020},
94	  doi = {10.1162/tacl_a_00330},
95	  url = {http://dx.doi.org/10.1162/tacl_a_00330}
96	}
97	
98	@inproceedings{gal2016dropout,
99	  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
100	  author = {Gal, Yarin and Ghahramani, Zoubin},
101	  booktitle = {ICML 2016},
102	  year = {2016},
103	  url = {https://arxiv.org/abs/1506.02142}
104	}
105	
106	@inproceedings{geifman2017selective,
107	  title = {Selective Classification for Deep Neural Networks},
108	  author = {Geifman, Yonatan and El-Yaniv, Ran},
109	  booktitle = {NeurIPS 2017},
110	  year = {2017},
111	  url = {https://arxiv.org/abs/1705.08500}
112	}
113	
114	@inproceedings{geng2024confidence,
115	  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},
116	  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},
117	  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
118	  year = {2024},
119	  doi = {10.18653/v1/2024.naacl-long.366},
120	  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}
121	}
122	
123	@inproceedings{guo2017calibration,
124	  title = {On Calibration of Modern Neural Networks},
125	  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},
126	  booktitle = {ICML 2017},
127	  year = {2017},
128	  url = {https://arxiv.org/abs/1706.04599}
129	}
130	
131	@article{hobelsberger2025systematic,
132	  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},
133	  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},
134	  journal = {arXiv preprint arXiv:2510.20460},
135	  year = {2025},
136	  url = {https://arxiv.org/abs/2510.20460}
137	}
138	
139	@article{jaccard1901distribution,
140	  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},
141	  author = {Jaccard, Paul},
142	  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},
143	  year = {1901},
144	  url = {https://www.researchgate.net/publication/225035806}
145	}
146	
147	@inproceedings{jagannatha2020calibrating,
148	  title = {Calibrating Structured Output Predictors for Natural Language Processing},
149	  author = {Jagannatha, Abhyuday and Yu, Hong},
150	  booktitle = {ACL 2020},
151	  year = {2020},
152	  url = {https://aclanthology.org/2020.acl-main.188/}
153	}
154	
155	@article{kadavath2022language,
156	  title = {Language Models (Mostly) Know What They Know},
157	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
158	  journal = {arXiv preprint arXiv:2207.05221},
159	  year = {2022},
160	  url = {https://arxiv.org/abs/2207.05221}
161	}
162	
163	@inproceedings{kang2025selfcertainty,
164	  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},
165	  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},
166	  booktitle = {NeurIPS 2025},
167	  year = {2025},
168	  url = {https://arxiv.org/abs/2502.18581}
169	}
170	
171	@inproceedings{kim2026reasc,
172	  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},
173	  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},
174	  booktitle = {ACL 2026},
175	  year = {2026},
176	  url = {https://arxiv.org/abs/2601.02970}
177	}
178	
179	@article{kossen2024semantic,
180	  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},
181	  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},
182	  journal = {arXiv preprint arXiv:2406.15927},
183	  year = {2024},
184	  url = {https://arxiv.org/abs/2406.15927}
185	}
186	
187	@inproceedings{kuhn2023semantic,
188	  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},
189	  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},
190	  booktitle = {ICLR 2023},
191	  year = {2023},
192	  url = {https://arxiv.org/abs/2302.09664}
193	}
194	
195	@inproceedings{kuleshov2015calibrated,
196	  title = {Calibrated Structured Prediction},
197	  author = {Kuleshov, Volodymyr and Liang, Percy},
198	  booktitle = {NeurIPS 2015},
199	  year = {2015},
200	  url = {https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html}
201	}
202	
203	@inproceedings{lakshminarayanan2017ensembles,
204	  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
205	  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},
206	  booktitle = {NeurIPS 2017},
207	  year = {2017},
208	  url = {https://arxiv.org/abs/1612.01474}
209	}
210	
211	@inproceedings{lightman2024verify,
212	  title = {Let's Verify Step by Step},
213	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
214	  booktitle = {ICLR 2024},
215	  year = {2024},
216	  url = {https://arxiv.org/abs/2305.20050}
217	}
218	
219	% SUPPLEMENTARY — not cited in main text
220	@inproceedings{liu2025uqcalibration,
221	  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},
222	  author = {Liu, Xiaoou and Chen, Tiejin and Da, Longchao and Chen, Chacha and Lin, Zhen and Wei, Hua},
223	  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},
224	  year = {2025},
225	  doi = {10.1145/3711896.3736569},
226	  url = {http://dx.doi.org/10.1145/3711896.3736569}
227	}
228	
229	@inproceedings{luan2018scierc,
230	  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},
231	  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},
232	  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
233	  year = {2018},
234	  doi = {10.18653/v1/D18-1360},
235	  url = {http://dx.doi.org/10.18653/v1/D18-1360}
236	}
237	
238	@inproceedings{manakul2023selfcheckgpt,
239	  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},
240	  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},
241	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
242	  year = {2023},
243	  doi = {10.18653/v1/2023.emnlp-main.557},
244	  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}
245	}
246	
247	@article{nedellec2026consistency,
248	  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},
249	  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},
250	  journal = {Genomics \& Informatics},
251	  year = {2026},
252	  doi = {10.1186/s44342-025-00063-2},
253	  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}
254	}
255	
256	@article{oh2025latentsc,
257	  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},
258	  author = {Oh, Jungsuk and Lee, Jay-Yoon},
259	  journal = {arXiv preprint arXiv:2508.18395},
260	  year = {2025},
261	  url = {https://arxiv.org/abs/2508.18395}
262	}
263	
264	@inproceedings{ren2023selfevaluation,
265	  title = {Self-Evaluation Improves Selective Generation in Large Language Models},
266	  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji},
267	  booktitle = {NeurIPS 2023 Workshop},
268	  year = {2023},
269	  url = {https://arxiv.org/abs/2312.09300}
270	}
271	
272	@inproceedings{sainz2024gollie,
273	  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
274	  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},
275	  booktitle = {ICLR 2024},
276	  year = {2024},
277	  url = {https://arxiv.org/abs/2310.03668}
278	}
279	
280	@inproceedings{shelmanov2021active,
281	  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},
282	  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},
283	  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},
284	  year = {2021},
285	  doi = {10.18653/v1/2021.eacl-main.145},
286	  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}
287	}
288	
289	@inproceedings{snell2024scaling,
290	  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
291	  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
292	  booktitle = {ICLR 2025},
293	  year = {2024},
294	  url = {https://arxiv.org/abs/2408.03314}
295	}
296	
297	@inproceedings{taubenfeld2025cisc,
298	  title = {Confidence Improves Self-Consistency in LLMs},
299	  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},
300	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
301	  year = {2025},
302	  doi = {10.18653/v1/2025.findings-acl.1030},
303	  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}
304	}
305	
306	@inproceedings{thirukovalluru2024atomic,
307	  title = {Atomic Self-Consistency for Better Long Form Generations},
308	  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},
309	  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
310	  year = {2024},
311	  doi = {10.18653/v1/2024.emnlp-main.706},
312	  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}
313	}
314	
315	@inproceedings{tjongkimsang2003conll,
316	  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},
317	  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},
318	  booktitle = {CoNLL 2003},
319	  year = {2003},
320	  url = {https://aclanthology.org/W03-0419/}
321	}
322	
323	@inproceedings{vashurin2025cocoa,
324	  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},
325	  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},
326	  booktitle = {NeurIPS 2025},
327	  year = {2025},
328	  url = {https://arxiv.org/abs/2502.04964}
329	}
330	
331	@inproceedings{wadhwa2023revisiting,
332	  title = {Revisiting Relation Extraction in the era of Large Language Models},
333	  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},
334	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
335	  year = {2023},
336	  doi = {10.18653/v1/2023.acl-long.868},
337	  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}
338	}
339	
340	@inproceedings{wan2025rasc,
341	  title = {Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling},
342	  author = {Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},
343	  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
344	  year = {2025},
345	  doi = {10.18653/v1/2025.naacl-long.184},
346	  url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}
347	}
348	
349	@inproceedings{wang2023selfconsistency,
350	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
351	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
352	  booktitle = {ICLR 2023},
353	  year = {2023},
354	  url = {https://arxiv.org/abs/2203.11171}
355	}
356	
357	@inproceedings{wang2024mathshepherd,
358	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
359	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
360	  booktitle = {ACL 2024},
361	  year = {2024},
362	  url = {https://arxiv.org/abs/2312.08935}
363	}
364	
365	@inproceedings{wang2025rankedvoting,
366	  title = {Ranked Voting based Self-Consistency of Large Language Models},
367	  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},
368	  booktitle = {ACL Findings 2025},
369	  year = {2025},
370	  url = {https://arxiv.org/abs/2505.10772}
371	}
372	
373	% SUPPLEMENTARY — not cited in main text
374	@article{wen2025know,
375	  title = {Know Your Limits: A Survey of Abstention in Large Language Models},
376	  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},
377	  journal = {Transactions of the Association for Computational Linguistics},
378	  year = {2025},
379	  doi = {10.1162/tacl_a_00754},
380	  url = {http://dx.doi.org/10.1162/tacl_a_00754}
381	}
382	
383	@article{willard2023guided,
384	  title = {Efficient Guided Generation for Large Language Models},
385	  author = {Willard, Brandon T. and Louf, Rémi},
386	  journal = {arXiv preprint arXiv:2307.09702},
387	  year = {2023},
388	  url = {https://arxiv.org/abs/2307.09702}
389	}
390	
391	@article{wu2024inference,
392	  title = {Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models},
393	  author = {Wu, Yangzhen and Sun, Zhiqing and Li, Shanda and Welleck, Sean and Yang, Yiming},
394	  journal = {arXiv preprint arXiv:2408.00724},
395	  year = {2024},
396	  url = {https://arxiv.org/abs/2408.00724}
397	}
398	
399	% SUPPLEMENTARY — not cited in main text
400	@inproceedings{xia2025survey,
401	  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},
402	  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},
403	  booktitle = {ACL Findings 2025},
404	  year = {2025},
405	  url = {https://aclanthology.org/2025.findings-acl.1101/}
406	}
407	
408	@article{xiao2019uncertainty,
409	  title = {Quantifying Uncertainties in Natural Language Processing Tasks},
410	  author = {Xiao, Yijun and Wang, William Yang},
411	  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
412	  year = {2019},
413	  doi = {10.1609/aaai.v33i01.33017322},
414	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
415	}
416	
417	@inproceedings{xiong2024verbalized,
418	  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},
419	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
420	  booktitle = {ICLR 2024},
421	  year = {2024},
422	  url = {https://arxiv.org/abs/2306.13063}
423	}
424	
425	@inproceedings{zhang2023ener,
426	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
427	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
428	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
429	  year = {2023},
430	  doi = {10.18653/v1/2023.findings-acl.103},
431	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
432	}
433	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "141de283-3319-436e-8cde-c0f36ef822e2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{bates2021rcps,\n  title = {Distribution-free, Risk-controlling Prediction Sets},\n  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},\n  journal = {Journal of the ACM},\n  year = {2021},\n  doi = {10.1145/3478535},\n  url = {http://dx.doi.org/10.1145/3478535}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Frédéric and Guzmán, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330},\n  url = {http://dx.doi.org/10.1162/tacl_a_00330}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{jagannatha2020calibrating,\n  title = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {ACL 2020},\n  year = {2020},\n  url = {https://aclanthology.org/2020.acl-main.188/}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {NeurIPS 2015},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{liu2025uqcalibration,\n  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},\n  author = {Liu, Xiaoou and Chen, Tiejin and Da, Longchao and Chen, Chacha and Lin, Zhen and Wei, Hua},\n  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},\n  year = {2025},\n  doi = {10.1145/3711896.3736569},\n  url = {http://dx.doi.org/10.1145/3711896.3736569}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{ren2023selfevaluation,\n  title = {Self-Evaluation Improves Selective Generation in Large Language Models},\n  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji},\n  booktitle = {NeurIPS 2023 Workshop},\n  year = {2023},\n  url = {https://arxiv.org/abs/2312.09300}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wan2025rasc,\n  title = {Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling},\n  author = {Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},\n  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2025},\n  doi = {10.18653/v1/2025.naacl-long.184},\n  url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@article{wu2024inference,\n  title = {Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models},\n  author = {Wu, Yangzhen and Sun, Zhiqing and Li, Shanda and Welleck, Sean and Yang, Yiming},\n  journal = {arXiv preprint arXiv:2408.00724},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.00724}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n",
      "numLines": 433,
      "startLine": 1,
      "totalLines": 433
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01Jde2J1c6G96PCqwAvfxqxk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "ed3c894a-4e7a-4840-8c93-9da4d61c0374",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXHt1nTX1eCoYQCMZqPYdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
      },
      "output_tokens": 31,
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

_source line 9 · 2026-05-14T19:48:58.712Z_

<details><summary>↩ Tool result · `toolu_01Jde2J1c6G96PCqwAvfxqxk`</summary>

```text
1	meta:
2	  last_updated: '2026-05-14T21:00:00.000Z'
3	  total_papers: 52
4	categories: []
5	papers:
6	  wang2023selfconsistency:
7	    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models
8	    authors:
9	    - Xuezhi Wang
10	    - Jason Wei
11	    - Dale Schuurmans
12	    - Quoc Le
13	    - Ed Chi
14	    - Sharan Narang
15	    - Aakanksha Chowdhery
16	    - Denny Zhou
17	    year: 2023
18	    venue: ICLR 2023
19	    url: https://arxiv.org/abs/2203.11171
20	    doi: ''
21	    bibtex_key: wang2023selfconsistency
22	    category: self_consistency_reasoning
23	    role: foundation
24	    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm
25	      from closed-form answers to structured IE outputs.'
26	    abstract: ''
27	    semantic_scholar_id: ''
28	    verified: true
29	    added_by: paper-research:cluster1
30	    added_at: '2026-05-14T15:47:22.188Z'
31	  taubenfeld2025cisc:
32	    title: Confidence Improves Self-Consistency in LLMs
33	    authors:
34	    - Amir Taubenfeld
35	    - Tom Sheffer
36	    - Eran Ofek
37	    - Amir Feder
38	    - Ariel Goldstein
39	    - Zorik Gekhman
40	    - Gal Yona
41	    year: 2025
42	    venue: ACL Findings 2025
43	    url: https://arxiv.org/abs/2502.06233
44	    doi: 10.18653/v1/2025.findings-acl.1030
45	    bibtex_key: taubenfeld2025cisc
46	    category: self_consistency_reasoning
47	    role: direct-competitor
48	    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the
49	      same "strong predictor, weak selector" gap but for structured outputs.'
50	    abstract: ''
51	    semantic_scholar_id: ''
52	    verified: true
53	    added_by: paper-research:cluster1
54	    added_at: '2026-05-14T15:47:22.188Z'
55	  kang2025selfcertainty:
56	    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty
57	    authors:
58	    - Zhewei Kang
59	    - Xuandong Zhao
60	    - Dawn Song
61	    year: 2025
62	    venue: NeurIPS 2025
63	    url: https://arxiv.org/abs/2502.18581
64	    doi: ''
65	    bibtex_key: kang2025selfcertainty
66	    category: self_consistency_reasoning
67	    role: direct-competitor
68	    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free
69	      quality estimation that we compare against for structured IE.
70	    abstract: ''
71	    semantic_scholar_id: ''
72	    verified: true
73	    added_by: paper-research:cluster1
74	    added_at: '2026-05-14T15:47:22.188Z'
75	  kim2026reasc:
76	    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning
77	    authors:
78	    - Junseok Kim
79	    - Nakyeong Yang
80	    - Kyungmin Min
81	    - Kyomin Jung
82	    year: 2026
83	    venue: ACL 2026
84	    url: https://arxiv.org/abs/2601.02970
85	    doi: ''
86	    bibtex_key: kim2026reasc
87	    category: self_consistency_reasoning
88	    role: direct-competitor
89	    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost
90	      by 70% on GSM8K. Directly relevant to our efficiency analysis.'
91	    abstract: ''
92	    semantic_scholar_id: ''
93	    verified: true
94	    added_by: paper-research:cluster1
95	    added_at: '2026-05-14T15:47:22.188Z'
96	  thirukovalluru2024atomic:
97	    title: Atomic Self-Consistency for Better Long Form Generations
98	    authors:
99	    - Raghuveer Thirukovalluru
100	    - Yukun Huang
101	    - Bhuwan Dhingra
102	    year: 2024
103	    venue: EMNLP 2024
104	    url: https://aclanthology.org/2024.emnlp-main.706/
105	    doi: 10.18653/v1/2024.emnlp-main.706
106	    bibtex_key: thirukovalluru2024atomic
107	    category: self_consistency_reasoning
108	    role: background
109	    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related
110	      to our structured output aggregation approach.
111	    abstract: ''
112	    semantic_scholar_id: ''
113	    verified: true
114	    added_by: paper-research:cluster1
115	    added_at: '2026-05-14T15:47:22.188Z'
116	  chen2024usc:
117	    title: Universal Self-Consistency for Large Language Model Generation
118	    authors:
119	    - Xinyun Chen
120	    - Renat Aksitov
121	    - Uri Alon
122	    - Jie Ren
123	    - Kefan Xiao
124	    - Pengcheng Yin
125	    - Sushant Prakash
126	    - Charles Sutton
127	    - Xuezhi Wang
128	    - Denny Zhou
129	    year: 2024
130	    venue: arXiv preprint (ICML 2024 Workshop ICL)
131	    url: https://arxiv.org/abs/2311.17311
132	    doi: ''
133	    bibtex_key: chen2024usc
134	    category: self_consistency_reasoning
135	    role: background
136	    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers
137	      to free-form generation. Precursor to our structured consistency approach.'
138	    abstract: ''
139	    semantic_scholar_id: ''
140	    verified: true
141	    added_by: paper-research:cluster1
142	    added_at: '2026-05-14T15:47:22.188Z'
143	  manakul2023selfcheckgpt:
144	    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'
145	    authors:
146	    - Potsawee Manakul
147	    - Adian Liusie
148	    - Mark Gales
149	    year: 2023
150	    venue: EMNLP 2023
151	    url: https://aclanthology.org/2023.emnlp-main.557/
152	    doi: 10.18653/v1/2023.emnlp-main.557
153	    bibtex_key: manakul2023selfcheckgpt
154	    category: self_consistency_reasoning
155	    role: background
156	    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations
157	      diverge. Motivates our consistency-based quality signal for IE.
158	    abstract: ''
159	    semantic_scholar_id: ''
160	    verified: true
161	    added_by: paper-research:cluster1
162	    added_at: '2026-05-14T15:47:22.188Z'
163	  wan2025rasc:
164	    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'
165	    authors:
166	    - Guangya Wan
167	    - Yuqi Wu
168	    - Jie Chen
169	    - Sheng Li
170	    year: 2025
171	    venue: NAACL 2025
172	    url: https://aclanthology.org/2025.naacl-long.184/
173	    doi: 10.18653/v1/2025.naacl-long.184
174	    bibtex_key: wan2025rasc
175	    category: self_consistency_reasoning
176	    role: background
177	    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples
178	      by ~70%. Complements our approach of structured quality-aware aggregation.'
179	    abstract: ''
180	    semantic_scholar_id: ''
181	    verified: true
182	    added_by: paper-research:cluster1
183	    added_at: '2026-05-14T15:47:22.188Z'
184	  nedellec2026consistency:
185	    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings
186	      from plant-health data'
187	    authors:
188	    - Claire Nédellec
189	    - Jingbo Xia
190	    year: 2026
191	    venue: Genomics & Informatics
192	    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/
193	    doi: 10.1186/s44342-025-00063-2
194	    bibtex_key: nedellec2026consistency
195	    category: consistency_structured_ie
196	    role: direct-competitor
197	    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and
198	      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'
199	    abstract: ''
200	    semantic_scholar_id: ''
201	    verified: true
202	    added_by: paper-research:lit_batch1
203	    added_at: '2026-05-14T17:52:10.000Z'
204	  vashurin2025cocoa:
205	    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'
206	    authors:
207	    - Roman Vashurin
208	    - Maiya Goloburda
209	    - Albina Ilina
210	    - Aleksandr Rubashevskii
211	    - Preslav Nakov
212	    - Artem Shelmanov
213	    - Maxim Panov
214	    year: 2025
215	    venue: NeurIPS 2025
216	    url: https://arxiv.org/abs/2502.04964
217	    doi: ''
218	    bibtex_key: vashurin2025cocoa
219	    category: consistency_structured_ie
220	    role: background
221	    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.
222	      Provides theoretical grounding for our dual-signal approach in structured IE.
223	    abstract: ''
224	    semantic_scholar_id: ''
225	    verified: true
226	    added_by: paper-research:lit_batch1
227	    added_at: '2026-05-14T17:52:10.000Z'
228	  hobelsberger2025systematic:
229	    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models
230	    authors:
231	    - Christian Hobelsberger
232	    - Theresa Winner
233	    - Andreas Nawroth
234	    - Oliver Mitevski
235	    - Anna-Carolina Haensch
236	    year: 2025
237	    venue: arXiv preprint
238	    url: https://arxiv.org/abs/2510.20460
239	    doi: ''
240	    bibtex_key: hobelsberger2025systematic
241	    category: consistency_structured_ie
242	    role: background
243	    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid
244	      CoCoA yields best calibration, supporting our multi-signal aggregation design.
245	    abstract: ''
246	    semantic_scholar_id: ''
247	    verified: true
248	    added_by: paper-research:lit_batch1
249	    added_at: '2026-05-14T17:52:10.000Z'
250	  geng2024confidence:
251	    title: A Survey of Confidence Estimation and Calibration in Large Language Models
252	    authors:
253	    - Jiahui Geng
254	    - Fengyu Cai
255	    - Yuxia Wang
256	    - Heinz Koeppl
257	    - Preslav Nakov
258	    - Iryna Gurevych
259	    year: 2024
260	    venue: NAACL 2024
261	    url: https://arxiv.org/abs/2311.08298
262	    doi: 10.18653/v1/2024.naacl-long.366
263	    bibtex_key: geng2024confidence
264	    category: confidence_surveys
265	    role: survey
266	    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for
267	      positioning our consistency-based confidence approach within the broader landscape.
268	    abstract: ''
269	    semantic_scholar_id: ''
270	    verified: true
271	    added_by: paper-research:lit_batch1
272	    added_at: '2026-05-14T17:52:10.000Z'
273	  wen2025know:
274	    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'
275	    authors:
276	    - Bingbing Wen
277	    - Jihan Yao
278	    - Shangbin Feng
279	    - Chenjun Xu
280	    - Yulia Tsvetkov
281	    - Bill Howe
282	    - Lucy Lu Wang
283	    year: 2025
284	    venue: TACL 2025
285	    url: https://arxiv.org/abs/2407.18418
286	    doi: 10.1162/tacl_a_00754
287	    bibtex_key: wen2025know
288	    category: confidence_surveys
289	    role: supplementary
290	    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering
291	      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'
292	    abstract: ''
293	    semantic_scholar_id: ''
294	    verified: true
295	    added_by: paper-research:lit_batch1
296	    added_at: '2026-05-14T17:52:10.000Z'
297	  xia2025survey:
298	    title: A Survey of Uncertainty Estimation Methods on Large Language Models
299	    authors:
300	    - Zhiqiu Xia
301	    - Jinxuan Xu
302	    - Yuqian Zhang
303	    - Hang Liu
304	    year: 2025
305	    venue: ACL Findings 2025
306	    url: https://aclanthology.org/2025.findings-acl.1101/
307	    doi: ''
308	    bibtex_key: xia2025survey
309	    category: confidence_surveys
310	    role: supplementary
311	    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,
312	      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps
313	      with geng2024 main survey]'
314	    abstract: ''
315	    semantic_scholar_id: ''
316	    verified: true
317	    added_by: paper-research:lit_batch1
318	    added_at: '2026-05-14T17:52:10.000Z'
319	  liu2025uqcalibration:
320	    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'
321	    authors:
322	    - Xiaoou Liu
323	    - Tiejin Chen
324	    - Longchao Da
325	    - Chacha Chen
326	    - Zhen Lin
327	    - Hua Wei
328	    year: 2025
329	    venue: KDD 2025
330	    url: https://arxiv.org/abs/2503.15850
331	    doi: 10.1145/3711896.3736569
332	    bibtex_key: liu2025uqcalibration
333	    category: confidence_surveys
334	    role: supplementary
335	    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements
336	      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps
337	      with geng2024 main survey]'
338	    abstract: ''
339	    semantic_scholar_id: ''
340	    verified: true
341	    added_by: paper-research:lit_batch1
342	    added_at: '2026-05-14T17:52:10.000Z'
343	  kuhn2023semantic:
344	    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'
345	    authors:
346	    - Lorenz Kuhn
347	    - Yarin Gal
348	    - Sebastian Farquhar
349	    year: 2023
350	    venue: ICLR 2023
351	    url: https://arxiv.org/abs/2302.09664
352	    doi: ''
353	    bibtex_key: kuhn2023semantic
354	    category: uncertainty_calibration
355	    role: foundation
356	    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation
357	      for our structured consistency metric that operates at the semantic level of IE triples.
358	    abstract: ''
359	    semantic_scholar_id: ''
360	    verified: true
361	    added_by: paper-research:lit_batch1
362	    added_at: '2026-05-14T17:52:10.000Z'
363	  kadavath2022language:
364	    title: Language Models (Mostly) Know What They Know
365	    authors:
366	    - Saurav Kadavath
367	    - Tom Conerly
368	    - Amanda Askell
369	    - Tom Henighan
370	    - Dawn Drain
371	    - Ethan Perez
372	    - Nicholas Schiefer
373	    - Zac Hatfield-Dodds
374	    - Nova DasSarma
375	    - Eli Tran-Johnson
376	    - Scott Johnston
377	    - Sheer El-Showk
378	    - Andy Jones
379	    - Nelson Elhage
380	    - Tristan Hume
381	    - Anna Chen
382	    - Yuntao Bai
383	    - Sam Bowman
384	    - Stanislav Fort
385	    - Deep Ganguli
386	    - Danny Hernandez
387	    - Josh Jacobson
388	    - Jackson Kernion
389	    - Shauna Kravec
390	    - Liane Lovitt
391	    - Kamal Ndousse
392	    - Catherine Olsson
393	    - Sam Ringer
394	    - Dario Amodei
395	    - Tom Brown
396	    - Jack Clark
397	    - Nicholas Joseph
398	    - Ben Mann
399	    - Sam McCandlish
400	    - Chris Olah
401	    - Jared Kaplan
402	    year: 2022
403	    venue: arXiv preprint
404	    url: https://arxiv.org/abs/2207.05221
405	    doi: ''
406	    bibtex_key: kadavath2022language
407	    category: uncertainty_calibration
408	    role: foundation
409	    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge
410	      as a confidence signal, which we extend to structured IE output quality estimation.
411	    abstract: ''
412	    semantic_scholar_id: ''
413	    verified: true
414	    added_by: paper-research:lit_batch1
415	    added_at: '2026-05-14T17:52:10.000Z'
416	  guo2017calibration:
417	    title: On Calibration of Modern Neural Networks
418	    authors:
419	    - Chuan Guo
420	    - Geoff Pleiss
421	    - Yu Sun
422	    - Kilian Q. Weinberger
423	    year: 2017
424	    venue: ICML 2017
425	    url: https://arxiv.org/abs/1706.04599
426	    doi: ''
427	    bibtex_key: guo2017calibration
428	    category: uncertainty_calibration
429	    role: foundation
430	    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational
431	      reference for all calibration work including our LLM confidence calibration for IE.
432	    abstract: ''
433	    semantic_scholar_id: ''
434	    verified: true
435	    added_by: paper-research:lit_batch1
436	    added_at: '2026-05-14T17:52:10.000Z'
437	  desai2020calibration:
438	    title: Calibration of Pre-trained Transformers
439	    authors:
440	    - Shrey Desai
441	    - Greg Durrett
442	    year: 2020
443	    venue: EMNLP 2020
444	    url: https://arxiv.org/abs/2003.07892
445	    doi: 10.18653/v1/2020.emnlp-main.21
446	    bibtex_key: desai2020calibration
447	    category: uncertainty_calibration
448	    role: foundation
449	    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical
450	      calibration to the transformer era, motivating our LLM-specific calibration analysis.
451	    abstract: ''
452	    semantic_scholar_id: ''
453	    verified: true
454	    added_by: paper-research:lit_batch1
455	    added_at: '2026-05-14T17:52:10.000Z'
456	  kossen2024semantic:
457	    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'
458	    authors:
459	    - Jannik Kossen
460	    - Jiatong Han
461	    - Muhammed Razzak
462	    - Lisa Schut
463	    - Shreshth Malik
464	    - Yarin Gal
465	    year: 2024
466	    venue: arXiv preprint
467	    url: https://arxiv.org/abs/2406.15927
468	    doi: ''
469	    bibtex_key: kossen2024semantic
470	    category: uncertainty_calibration
471	    role: background
472	    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing
473	      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.
474	    abstract: ''
475	    semantic_scholar_id: ''
476	    verified: true
477	    added_by: paper-research:lit_batch1
478	    added_at: '2026-05-14T17:52:10.000Z'
479	  xiong2024verbalized:
480	    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs
481	    authors:
482	    - Miao Xiong
483	    - Zhiyuan Hu
484	    - Xinyang Lu
485	    - Yifei Li
486	    - Jie Fu
487	    - Junxian He
488	    - Bryan Hooi
489	    year: 2024
490	    venue: ICLR 2024
491	    url: https://arxiv.org/abs/2306.13063
492	    doi: ''
493	    bibtex_key: xiong2024verbalized
494	    category: uncertainty_calibration
495	    role: background
496	    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly
497	      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.
498	    abstract: ''
499	    semantic_scholar_id: ''
500	    verified: true
501	    added_by: paper-research:lit_batch1
502	    added_at: '2026-05-14T17:52:10.000Z'
503	  fisch2021conformal:
504	    title: Few-Shot Conformal Prediction with Auxiliary Tasks
505	    authors:
506	    - Adam Fisch
507	    - Tal Schuster
508	    - Tommi Jaakkola
509	    - Regina Barzilay
510	    year: 2021
511	    venue: ICML 2021
512	    url: https://arxiv.org/abs/2102.08898
513	    doi: 10.5555/3524938.3525234
514	    bibtex_key: fisch2021conformal
515	    category: conformal_prediction
516	    role: supplementary
517	    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter
518	      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'
519	    abstract: ''
520	    semantic_scholar_id: ''
521	    verified: true
522	    added_by: paper-research:lit_batch2
523	    added_at: '2026-05-14T18:10:52.000Z'
524	  angelopoulos2021conformal:
525	    title: Uncertainty Sets for Image Classifiers using Conformal Prediction
526	    authors:
527	    - Anastasios N. Angelopoulos
528	    - Stephen Bates
529	    - Jitendra Malik
530	    - Michael I. Jordan
531	    year: 2021
532	    venue: ICLR 2021
533	    url: https://arxiv.org/abs/2009.14193
534	    doi: ''
535	    bibtex_key: angelopoulos2021conformal
536	    category: conformal_prediction
537	    role: foundation
538	    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for
539	      conformal prediction methodology we adapt to structured IE output sets.
540	    abstract: ''
541	    semantic_scholar_id: ''
542	    verified: true
543	    added_by: paper-research:lit_batch2
544	    added_at: '2026-05-14T18:10:52.000Z'
545	  bates2021rcps:
546	    title: Distribution-Free, Risk-Controlling Prediction Sets
547	    authors:
548	    - Stephen Bates
549	    - Anastasios Angelopoulos
550	    - Lihua Lei
551	    - Jitendra Malik
552	    - Michael I. Jordan
553	    year: 2021
554	    venue: Journal of the ACM 2021
555	    url: https://arxiv.org/abs/2101.02703
556	    doi: 10.1145/3478535
557	    bibtex_key: bates2021rcps
558	    category: conformal_prediction
559	    role: supplementary
560	    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample
561	      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'
562	    abstract: ''
563	    semantic_scholar_id: ''
564	    verified: true
565	    added_by: paper-research:lit_batch2
566	    added_at: '2026-05-14T18:10:52.000Z'
567	  xiao2019uncertainty:
568	    title: Quantifying Uncertainties in Natural Language Processing Tasks
569	    authors:
570	    - Yijun Xiao
571	    - William Yang Wang
572	    year: 2019
573	    venue: AAAI 2019
574	    url: https://arxiv.org/abs/1811.07253
575	    doi: 10.1609/aaai.v33i01.33017322
576	    bibtex_key: xiao2019uncertainty
577	    category: token_span_uncertainty_ner
578	    role: foundation
579	    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model
580	      uncertainty improves both performance and reliability for token-level predictions.
581	    abstract: ''
582	    semantic_scholar_id: ''
583	    verified: true
584	    added_by: paper-research:lit_batch2
585	    added_at: '2026-05-14T18:10:52.000Z'
586	  shelmanov2021active:
587	    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates
588	    authors:
589	    - Artem Shelmanov
590	    - Dmitri Puzyrev
591	    - Lyubov Kupriyanova
592	    - Denis Belyakov
593	    - Daniil Larionov
594	    - Nikita Khromov
595	    - Olga Kozlova
596	    - Ekaterina Artemova
597	    - Dmitry V. Dylov
598	    - Alexander Panchenko
599	    year: 2021
600	    venue: EACL 2021
601	    url: https://arxiv.org/abs/2101.08133
602	    doi: 10.18653/v1/2021.eacl-main.145
603	    bibtex_key: shelmanov2021active
604	    category: token_span_uncertainty_ner
605	    role: foundation
606	    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with
607	      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.
608	    abstract: ''
609	    semantic_scholar_id: ''
610	    verified: true
611	    added_by: paper-research:lit_batch2
612	    added_at: '2026-05-14T18:10:52.000Z'
613	  zhang2023ener:
614	    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'
615	    authors:
616	    - Zhen Zhang
617	    - Mengting Hu
618	    - Shiwan Zhao
619	    - Minlie Huang
620	    - Haotian Wang
621	    - Lemao Liu
622	    - Zhirui Zhang
623	    - Zhe Liu
624	    - Bingzhe Wu
625	    year: 2023
626	    venue: ACL Findings 2023
627	    url: https://arxiv.org/abs/2305.17854
628	    doi: 10.18653/v1/2023.findings-acl.103
629	    bibtex_key: zhang2023ener
630	    category: token_span_uncertainty_ner
631	    role: background
632	    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and
633	      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.
634	    abstract: ''
635	    semantic_scholar_id: ''
636	    verified: true
637	    added_by: paper-research:lit_batch2
638	    added_at: '2026-05-14T18:10:52.000Z'
639	  lakshminarayanan2017ensembles:
640	    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles
641	    authors:
642	    - Balaji Lakshminarayanan
643	    - Alexander Pritzel
644	    - Charles Blundell
645	    year: 2017
646	    venue: NeurIPS 2017
647	    url: https://arxiv.org/abs/1612.01474
648	    doi: ''
649	    bibtex_key: lakshminarayanan2017ensembles
650	    category: ensemble_mc_dropout
651	    role: foundation
652	    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.
653	      Foundational baseline for ensemble-based uncertainty quantification we compare against.
654	    abstract: ''
655	    semantic_scholar_id: ''
656	    verified: true
657	    added_by: paper-research:lit_batch2
658	    added_at: '2026-05-14T18:10:52.000Z'
659	  gal2016dropout:
660	    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'
661	    authors:
662	    - Yarin Gal
663	    - Zoubin Ghahramani
664	    year: 2016
665	    venue: ICML 2016
666	    url: https://arxiv.org/abs/1506.02142
667	    doi: ''
668	    bibtex_key: gal2016dropout
669	    category: ensemble_mc_dropout
670	    role: foundation
671	    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for
672	      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.
673	    abstract: ''
674	    semantic_scholar_id: ''
675	    verified: true
676	    added_by: paper-research:lit_batch2
677	    added_at: '2026-05-14T18:10:52.000Z'
678	  fomicheva2020unsupervised:
679	    title: Unsupervised Quality Estimation for Neural Machine Translation
680	    authors:
681	    - Marina Fomicheva
682	    - Shuo Sun
683	    - Lisa Yankovskaya
684	    - Frédéric Blain
685	    - Francisco Guzmán
686	    - Mark Fishel
687	    - Nikolaos Aletras
688	    - Vishrav Chaudhary
689	    - Lucia Specia
690	    year: 2020
691	    venue: TACL 2020
692	    url: https://arxiv.org/abs/2005.10608
693	    doi: 10.1162/tacl_a_00330
694	    bibtex_key: fomicheva2020unsupervised
695	    category: ensemble_mc_dropout
696	    role: background
697	    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving
698	      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.
699	    abstract: ''
700	    semantic_scholar_id: ''
701	    verified: true
702	    added_by: paper-research:lit_batch2
703	    added_at: '2026-05-14T18:10:52.000Z'
704	  cobbe2021verifiers:
705	    title: Training Verifiers to Solve Math Word Problems
706	    authors:
707	    - Karl Cobbe
708	    - Vineet Kosaraju
709	    - Mohammad Bavarian
710	    - Mark Chen
711	    - Heewoo Jun
712	    - Lukasz Kaiser
713	    - Matthias Plappert
714	    - Jerry Tworek
715	    - Jacob Hilton
716	    - Reiichiro Nakano
717	    - Christopher Hesse
718	    - John Schulman
719	    year: 2021
720	    venue: arXiv preprint
721	    url: https://arxiv.org/abs/2110.14168
722	    doi: ''
723	    bibtex_key: cobbe2021verifiers
724	    category: verifier_reward_models
725	    role: foundation
726	    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.
727	      Establishes the verify-then-select paradigm our method builds upon.'
728	    abstract: ''
729	    semantic_scholar_id: ''
730	    verified: true
731	    added_by: paper-research:lit_batch3
732	    added_at: '2026-05-14T19:30:00.000Z'
733	  lightman2024verify:
734	    title: Let's Verify Step by Step
735	    authors:
736	    - Hunter Lightman
737	    - Vineet Kosaraju
738	    - Yura Burda
739	    - Harri Edwards
740	    - Bowen Baker
741	    - Teddy Lee
742	    - Jan Leike
743	    - John Schulman
744	    - Ilya Sutskever
745	    - Karl Cobbe
746	    year: 2024
747	    venue: ICLR 2024
748	    url: https://arxiv.org/abs/2305.20050
749	    doi: ''
750	    bibtex_key: lightman2024verify
751	    category: verifier_reward_models
752	    role: foundation
753	    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based
754	      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'
755	    abstract: ''
756	    semantic_scholar_id: ''
757	    verified: true
758	    added_by: paper-research:lit_batch3
759	    added_at: '2026-05-14T19:30:00.000Z'
760	  wang2024mathshepherd:
761	    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'
762	    authors:
763	    - Peiyi Wang
764	    - Lei Li
765	    - Zhihong Shao
766	    - Runxin Xu
767	    - Damai Dai
768	    - Yifei Li
769	    - Deli Chen
770	    - Yu Wu
771	    - Zhifang Sui
772	    year: 2024
773	    venue: ACL 2024
774	    url: https://arxiv.org/abs/2312.08935
775	    doi: ''
776	    bibtex_key: wang2024mathshepherd
777	    category: verifier_reward_models
778	    role: background
779	    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.
780	      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.
781	    abstract: ''
782	    semantic_scholar_id: ''
783	    verified: true
784	    added_by: paper-research:lit_batch3
785	    added_at: '2026-05-14T19:30:00.000Z'
786	  snell2024scaling:
787	    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters
788	    authors:
789	    - Charlie Snell
790	    - Jaehoon Lee
791	    - Kelvin Xu
792	    - Aviral Kumar
793	    year: 2024
794	    venue: ICLR 2025
795	    url: https://arxiv.org/abs/2408.03314
796	    doi: ''
797	    bibtex_key: snell2024scaling
798	    category: tts_scaling
799	    role: foundation
800	    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation
801	      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'
802	    abstract: ''
803	    semantic_scholar_id: ''
804	    verified: true
805	    added_by: paper-research:lit_batch3
806	    added_at: '2026-05-14T19:30:00.000Z'
807	  brown2024monkeys:
808	    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'
809	    authors:
810	    - Bradley Brown
811	    - Jordan Juravsky
812	    - Ryan Ehrlich
813	    - Ronald Clark
814	    - Quoc V. Le
815	    - Christopher Ré
816	    - Azalia Mirhoseini
817	    year: 2024
818	    venue: arXiv preprint
819	    url: https://arxiv.org/abs/2407.21787
820	    doi: ''
821	    bibtex_key: brown2024monkeys
822	    category: tts_scaling
823	    role: foundation
824	    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing
825	      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'
826	    abstract: ''
827	    semantic_scholar_id: ''
828	    verified: true
829	    added_by: paper-research:lit_batch3
830	    added_at: '2026-05-14T19:30:00.000Z'
831	  wu2024inference:
832	    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'
833	    authors:
834	    - Yangzhen Wu
835	    - Zhiqing Sun
836	    - Shanda Li
837	    - Sean Welleck
838	    - Yiming Yang
839	    year: 2024
840	    venue: arXiv preprint
841	    url: https://arxiv.org/abs/2408.00724
842	    doi: ''
843	    bibtex_key: wu2024inference
844	    category: tts_scaling
845	    role: background
846	    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms
847	      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.
848	    abstract: ''
849	    semantic_scholar_id: ''
850	    verified: true
851	    added_by: paper-research:lit_batch3
852	    added_at: '2026-05-14T19:30:00.000Z'
853	  kuleshov2015calibrated:
854	    title: Calibrated Structured Prediction
855	    authors:
856	    - Volodymyr Kuleshov
857	    - Percy Liang
858	    year: 2015
859	    venue: NeurIPS 2015
860	    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html
861	    doi: ''
862	    bibtex_key: kuleshov2015calibrated
863	    category: structured_calibration_ie
864	    role: foundation
865	    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration
866	      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'
867	    abstract: ''
868	    semantic_scholar_id: ''
869	    verified: true
870	    added_by: paper-research:lit_batch3
871	    added_at: '2026-05-14T19:30:00.000Z'
872	  culotta2004confidence:
873	    title: Confidence Estimation for Information Extraction
874	    authors:
875	    - Aron Culotta
876	    - Andrew McCallum
877	    year: 2004
878	    venue: HLT-NAACL 2004
879	    url: https://aclanthology.org/N04-4028/
880	    doi: ''
881	    bibtex_key: culotta2004confidence
882	    category: structured_calibration_ie
883	    role: foundation
884	    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record
885	      levels. Establishes the problem setting our LLM-based approach addresses.'
886	    abstract: ''
887	    semantic_scholar_id: ''
888	    verified: true
889	    added_by: paper-research:lit_batch3
890	    added_at: '2026-05-14T19:30:00.000Z'
891	  jagannatha2020calibrating:
892	    title: Calibrating Structured Output Predictors for Natural Language Processing
893	    authors:
894	    - Abhyuday Jagannatha
895	    - Hong Yu
896	    year: 2020
897	    venue: ACL 2020
898	    url: https://aclanthology.org/2020.acl-main.188/
899	    doi: ''
900	    bibtex_key: jagannatha2020calibrating
901	    category: structured_calibration_ie
902	    role: background
903	    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges
904	      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.
905	    abstract: ''
906	    semantic_scholar_id: ''
907	    verified: true
908	    added_by: paper-research:lit_batch3
909	    added_at: '2026-05-14T19:30:00.000Z'
910	  geifman2017selective:
911	    title: Selective Classification for Deep Neural Networks
912	    authors:
913	    - Yonatan Geifman
914	    - Ran El-Yaniv
915	    year: 2017
916	    venue: NeurIPS 2017
917	    url: https://arxiv.org/abs/1705.08500
918	    doi: ''
919	    bibtex_key: geifman2017selective
920	    category: selective_prediction
921	    role: foundation
922	    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified
923	      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'
924	    abstract: ''
925	    semantic_scholar_id: ''
926	    verified: true
927	    added_by: paper-research:lit_batch3
928	    added_at: '2026-05-14T19:30:00.000Z'
929	  ren2023selfevaluation:
930	    title: Self-Evaluation Improves Selective Generation in Large Language Models
931	    authors:
932	    - Jie Ren
933	    - Yao Zhao
934	    - Tu Vu
935	    - Peter J. Liu
936	    - Balaji Lakshminarayanan
937	    year: 2023
938	    venue: NeurIPS 2023 Workshop
939	    url: https://arxiv.org/abs/2312.09300
940	    doi: ''
941	    bibtex_key: ren2023selfevaluation
942	    category: selective_prediction
943	    role: background
944	    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions
945	      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.
946	    abstract: ''
947	    semantic_scholar_id: ''
948	    verified: true
949	    added_by: paper-research:lit_batch3
950	    added_at: '2026-05-14T19:30:00.000Z'
951	  wadhwa2023revisiting:
952	    title: Revisiting Relation Extraction in the era of Large Language Models
953	    authors:
954	    - Somin Wadhwa
955	    - Silvio Amir
956	    - Byron Wallace
957	    year: 2023
958	    venue: ACL 2023
959	    url: https://aclanthology.org/2023.acl-long.868/
960	    doi: 10.18653/v1/2023.acl-long.868
961	    bibtex_key: wadhwa2023revisiting
962	    category: generative_ie
963	    role: foundation
964	    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting
965	      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'
966	    abstract: ''
967	    semantic_scholar_id: ''
968	    verified: true
969	    added_by: paper-research:lit_batch4
970	    added_at: '2026-05-14T21:00:00.000Z'
971	  sainz2024gollie:
972	    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'
973	    authors:
974	    - Oscar Sainz
975	    - Iker García-Ferrero
976	    - Rodrigo Agerri
977	    - Oier Lopez de Lacalle
978	    - German Rigau
979	    - Eneko Agirre
980	    year: 2024
981	    venue: ICLR 2024
982	    url: https://arxiv.org/abs/2310.03668
983	    doi: ''
984	    bibtex_key: sainz2024gollie
985	    category: generative_ie
986	    role: foundation
987	    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization
988	      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'
989	    abstract: ''
990	    semantic_scholar_id: ''
991	    verified: true
992	    added_by: paper-research:lit_batch4
993	    added_at: '2026-05-14T21:00:00.000Z'
994	  luan2018scierc:
995	    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction
996	    authors:
997	    - Yi Luan
998	    - Luheng He
999	    - Mari Ostendorf
1000	    - Hannaneh Hajishirzi
1001	    year: 2018
1002	    venue: EMNLP 2018
1003	    url: https://aclanthology.org/D18-1360/
1004	    doi: 10.18653/v1/D18-1360
1005	    bibtex_key: luan2018scierc
1006	    category: generative_ie
1007	    role: dataset
1008	    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation
1009	      benchmark for our structured IE experiments.'
1010	    abstract: ''
1011	    semantic_scholar_id: ''
1012	    verified: true
1013	    added_by: paper-research:lit_batch4
1014	    added_at: '2026-05-14T21:00:00.000Z'
1015	  tjongkimsang2003conll:
1016	    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'
1017	    authors:
1018	    - Erik F. Tjong Kim Sang
1019	    - Fien De Meulder
1020	    year: 2003
1021	    venue: CoNLL 2003
1022	    url: https://aclanthology.org/W03-0419/
1023	    doi: ''
1024	    bibtex_key: tjongkimsang2003conll
1025	    category: generative_ie
1026	    role: dataset
1027	    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset
1028	      for our NER consistency experiments.'
1029	    abstract: ''
1030	    semantic_scholar_id: ''
1031	    verified: true
1032	    added_by: paper-research:lit_batch4
1033	    added_at: '2026-05-14T21:00:00.000Z'
1034	  derczynski2017wnut:
1035	    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition
1036	    authors:
1037	    - Leon Derczynski
1038	    - Eric Nichols
1039	    - Marieke van Erp
1040	    - Nut Limsopatham
1041	    year: 2017
1042	    venue: W-NUT Workshop at EMNLP 2017
1043	    url: https://aclanthology.org/W17-4418/
1044	    doi: ''
1045	    bibtex_key: derczynski2017wnut
1046	    category: generative_ie
1047	    role: dataset
1048	    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness
1049	      on harder, low-resource NER scenarios.'
1050	    abstract: ''
1051	    semantic_scholar_id: ''
1052	    verified: true
1053	    added_by: paper-research:lit_batch4
1054	    added_at: '2026-05-14T21:00:00.000Z'
1055	  willard2023guided:
1056	    title: Efficient Guided Generation for Large Language Models
1057	    authors:
1058	    - Brandon T. Willard
1059	    - Rémi Louf
1060	    year: 2023
1061	    venue: arXiv preprint
1062	    url: https://arxiv.org/abs/2307.09702
1063	    doi: ''
1064	    bibtex_key: willard2023guided
1065	    category: generative_ie
1066	    role: background
1067	    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and
1068	      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'
1069	    abstract: ''
1070	    semantic_scholar_id: ''
1071	    verified: true
1072	    added_by: paper-research:lit_batch4
1073	    added_at: '2026-05-14T21:00:00.000Z'
1074	  fleiss1971agreement:
1075	    title: Measuring Nominal Scale Agreement Among Many Raters
1076	    authors:
1077	    - Joseph L. Fleiss
1078	    year: 1971
1079	    venue: Psychological Bulletin
1080	    url: https://psycnet.apa.org/record/1972-05083-001
1081	    doi: 10.1037/h0031619
1082	    bibtex_key: fleiss1971agreement
1083	    category: agreement_metrics
1084	    role: foundation
1085	    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation
1086	      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'
1087	    abstract: ''
1088	    semantic_scholar_id: ''
1089	    verified: true
1090	    added_by: paper-research:lit_batch4
1091	    added_at: '2026-05-14T21:00:00.000Z'
1092	  jaccard1901distribution:
1093	    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura
1094	    authors:
1095	    - Paul Jaccard
1096	    year: 1901
1097	    venue: Bulletin de la Société Vaudoise des Sciences Naturelles
1098	    url: https://www.researchgate.net/publication/225035806
1099	    doi: ''
1100	    bibtex_key: jaccard1901distribution
1101	    category: agreement_metrics
1102	    role: foundation
1103	    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap
1104	      between extracted entity/relation sets across multiple LLM samples.'
1105	    abstract: ''
1106	    semantic_scholar_id: ''
1107	    verified: true
1108	    added_by: paper-research:lit_batch4
1109	    added_at: '2026-05-14T21:00:00.000Z'
1110	  wang2025rankedvoting:
1111	    title: Ranked Voting based Self-Consistency of Large Language Models
1112	    authors:
1113	    - Weiqin Wang
1114	    - Yile Wang
1115	    - Hui Huang
1116	    year: 2025
1117	    venue: ACL Findings 2025
1118	    url: https://arxiv.org/abs/2505.10772
1119	    doi: ''
1120	    bibtex_key: wang2025rankedvoting
1121	    category: self_consistency_reasoning
1122	    role: background
1123	    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.
1124	      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'
1125	    abstract: ''
1126	    semantic_scholar_id: ''
1127	    verified: true
1128	    added_by: paper-research:lit_batch4
1129	    added_at: '2026-05-14T21:00:00.000Z'
1130	  oh2025latentsc:
1131	    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'
1132	    authors:
1133	    - Jungsuk Oh
1134	    - Jay-Yoon Lee
1135	    year: 2025
1136	    venue: arXiv preprint
1137	    url: https://arxiv.org/abs/2508.18395
1138	    doi: ''
1139	    bibtex_key: oh2025latentsc
1140	    category: self_consistency_reasoning
1141	    role: background
1142	    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.
1143	      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'
1144	    abstract: ''
1145	    semantic_scholar_id: ''
1146	    verified: true
1147	    added_by: paper-research:lit_batch4
1148	    added_at: '2026-05-14T21:00:00.000Z'
1149	  zhou2024uniner:
1150	    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'
1151	    authors:
1152	    - Wenxuan Zhou
1153	    - Sheng Zhang
1154	    - Yu Gu
1155	    - Muhao Chen
1156	    - Hoifung Poon
1157	    year: 2024
1158	    venue: ICLR 2024
1159	    url: https://arxiv.org/abs/2308.03279
1160	    doi: ''
1161	    bibtex_key: zhou2024uniner
1162	    category: generative_ie
1163	    role: foundation
1164	    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.
1165	      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'
1166	    abstract: ''
1167	    semantic_scholar_id: ''
1168	    verified: false
1169	    added_by: paper-agent:manual
1170	    added_at: '2026-05-14T21:05:00.000Z'
1171	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "9aa8a472-b764-46f1-965e-6102ce68db1c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
      "content": "meta:\n  last_updated: '2026-05-14T21:00:00.000Z'\n  total_papers: 52\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\n      for our structured consistency metric that operates at the semantic level of IE triples.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  fisch2021conformal:\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\n    authors:\n    - Adam Fisch\n    - Tal Schuster\n    - Tommi Jaakkola\n    - Regina Barzilay\n    year: 2021\n    venue: ICML 2021\n    url: https://arxiv.org/abs/2102.08898\n    doi: 10.5555/3524938.3525234\n    bibtex_key: fisch2021conformal\n    category: conformal_prediction\n    role: supplementary\n    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\n      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  angelopoulos2021conformal:\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\n    authors:\n    - Anastasios N. Angelopoulos\n    - Stephen Bates\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.14193\n    doi: ''\n    bibtex_key: angelopoulos2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\n      conformal prediction methodology we adapt to structured IE output sets.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  bates2021rcps:\n    title: Distribution-Free, Risk-Controlling Prediction Sets\n    authors:\n    - Stephen Bates\n    - Anastasios Angelopoulos\n    - Lihua Lei\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: Journal of the ACM 2021\n    url: https://arxiv.org/abs/2101.02703\n    doi: 10.1145/3478535\n    bibtex_key: bates2021rcps\n    category: conformal_prediction\n    role: supplementary\n    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\n      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  xiao2019uncertainty:\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\n    authors:\n    - Yijun Xiao\n    - William Yang Wang\n    year: 2019\n    venue: AAAI 2019\n    url: https://arxiv.org/abs/1811.07253\n    doi: 10.1609/aaai.v33i01.33017322\n    bibtex_key: xiao2019uncertainty\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\n      uncertainty improves both performance and reliability for token-level predictions.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  shelmanov2021active:\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\n    authors:\n    - Artem Shelmanov\n    - Dmitri Puzyrev\n    - Lyubov Kupriyanova\n    - Denis Belyakov\n    - Daniil Larionov\n    - Nikita Khromov\n    - Olga Kozlova\n    - Ekaterina Artemova\n    - Dmitry V. Dylov\n    - Alexander Panchenko\n    year: 2021\n    venue: EACL 2021\n    url: https://arxiv.org/abs/2101.08133\n    doi: 10.18653/v1/2021.eacl-main.145\n    bibtex_key: shelmanov2021active\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  zhang2023ener:\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\n    authors:\n    - Zhen Zhang\n    - Mengting Hu\n    - Shiwan Zhao\n    - Minlie Huang\n    - Haotian Wang\n    - Lemao Liu\n    - Zhirui Zhang\n    - Zhe Liu\n    - Bingzhe Wu\n    year: 2023\n    venue: ACL Findings 2023\n    url: https://arxiv.org/abs/2305.17854\n    doi: 10.18653/v1/2023.findings-acl.103\n    bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  lakshminarayanan2017ensembles:\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\n    authors:\n    - Balaji Lakshminarayanan\n    - Alexander Pritzel\n    - Charles Blundell\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1612.01474\n    doi: ''\n    bibtex_key: lakshminarayanan2017ensembles\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  gal2016dropout:\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\n    authors:\n    - Yarin Gal\n    - Zoubin Ghahramani\n    year: 2016\n    venue: ICML 2016\n    url: https://arxiv.org/abs/1506.02142\n    doi: ''\n    bibtex_key: gal2016dropout\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  fomicheva2020unsupervised:\n    title: Unsupervised Quality Estimation for Neural Machine Translation\n    authors:\n    - Marina Fomicheva\n    - Shuo Sun\n    - Lisa Yankovskaya\n    - Frédéric Blain\n    - Francisco Guzmán\n    - Mark Fishel\n    - Nikolaos Aletras\n    - Vishrav Chaudhary\n    - Lucia Specia\n    year: 2020\n    venue: TACL 2020\n    url: https://arxiv.org/abs/2005.10608\n    doi: 10.1162/tacl_a_00330\n    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wadhwa2023revisiting:\n    title: Revisiting Relation Extraction in the era of Large Language Models\n    authors:\n    - Somin Wadhwa\n    - Silvio Amir\n    - Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    doi: 10.18653/v1/2023.acl-long.868\n    bibtex_key: wadhwa2023revisiting\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  sainz2024gollie:\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\n    authors:\n    - Oscar Sainz\n    - Iker García-Ferrero\n    - Rodrigo Agerri\n    - Oier Lopez de Lacalle\n    - German Rigau\n    - Eneko Agirre\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2310.03668\n    doi: ''\n    bibtex_key: sainz2024gollie\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  luan2018scierc:\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\n    authors:\n    - Yi Luan\n    - Luheng He\n    - Mari Ostendorf\n    - Hannaneh Hajishirzi\n    year: 2018\n    venue: EMNLP 2018\n    url: https://aclanthology.org/D18-1360/\n    doi: 10.18653/v1/D18-1360\n    bibtex_key: luan2018scierc\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\n      benchmark for our structured IE experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  tjongkimsang2003conll:\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\n    authors:\n    - Erik F. Tjong Kim Sang\n    - Fien De Meulder\n    year: 2003\n    venue: CoNLL 2003\n    url: https://aclanthology.org/W03-0419/\n    doi: ''\n    bibtex_key: tjongkimsang2003conll\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\n      for our NER consistency experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  derczynski2017wnut:\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\n    authors:\n    - Leon Derczynski\n    - Eric Nichols\n    - Marieke van Erp\n    - Nut Limsopatham\n    year: 2017\n    venue: W-NUT Workshop at EMNLP 2017\n    url: https://aclanthology.org/W17-4418/\n    doi: ''\n    bibtex_key: derczynski2017wnut\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\n      on harder, low-resource NER scenarios.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  willard2023guided:\n    title: Efficient Guided Generation for Large Language Models\n    authors:\n    - Brandon T. Willard\n    - Rémi Louf\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2307.09702\n    doi: ''\n    bibtex_key: willard2023guided\n    category: generative_ie\n    role: background\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  fleiss1971agreement:\n    title: Measuring Nominal Scale Agreement Among Many Raters\n    authors:\n    - Joseph L. Fleiss\n    year: 1971\n    venue: Psychological Bulletin\n    url: https://psycnet.apa.org/record/1972-05083-001\n    doi: 10.1037/h0031619\n    bibtex_key: fleiss1971agreement\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  jaccard1901distribution:\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\n    authors:\n    - Paul Jaccard\n    year: 1901\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\n    url: https://www.researchgate.net/publication/225035806\n    doi: ''\n    bibtex_key: jaccard1901distribution\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\n      between extracted entity/relation sets across multiple LLM samples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  wang2025rankedvoting:\n    title: Ranked Voting based Self-Consistency of Large Language Models\n    authors:\n    - Weiqin Wang\n    - Yile Wang\n    - Hui Huang\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2505.10772\n    doi: ''\n    bibtex_key: wang2025rankedvoting\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  oh2025latentsc:\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\n    authors:\n    - Jungsuk Oh\n    - Jay-Yoon Lee\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2508.18395\n    doi: ''\n    bibtex_key: oh2025latentsc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: false\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'\n",
      "numLines": 1171,
      "startLine": 1,
      "totalLines": 1171
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015HXiiPjGKUAvBQAQFMzFeQ`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "d817b9af-9d73-4eec-b40c-93c66cfcda3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GXHt1nTX1eCoYQCMZqPYdd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12259,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12259
      },
      "output_tokens": 31,
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

_source line 11 · 2026-05-14T19:48:58.865Z_

<details><summary>↩ Tool result · `toolu_015HXiiPjGKUAvBQAQFMzFeQ`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "c0489ac5-0dfd-42e7-b743-9fd66c576f1d",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Assistant

_source line 12_

Now let me search for the papers to verify their exact information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "c1555436-2861-474e-8140-8b63b207ac02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtiH2aKL3v9G4rQuvfDEoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25165,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25165
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VjAZkTgrFFpvicPqyGg1fe`</summary>

```json
{
  "query": "InstructUIE Multi-task Instruction Tuning Unified Information Extraction Wang 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "de2c1111-ea86-408e-97a7-855e1412938f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtiH2aKL3v9G4rQuvfDEoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25165,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25165
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WwtdLduMSpi3gvtD4QaShi`</summary>

```json
{
  "query": "GenIE autoregressive information extraction constrained decoding Josifoski 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "cce15124-2933-45df-9958-f3f28d89256e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtiH2aKL3v9G4rQuvfDEoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25165,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25165
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKiArzgRiB4xcaoLGtdWDu`</summary>

```json
{
  "query": "CodeIE code generation information extraction Li 2023 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "6f4bcb2b-90ff-4f32-9f8a-7369080ac5ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtiH2aKL3v9G4rQuvfDEoJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25165,
      "cache_read_input_tokens": 24100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25165
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

_source line 16 · 2026-05-14T19:49:09.475Z_

<details><summary>↩ Tool result · `toolu_01WwtdLduMSpi3gvtD4QaShi`</summary>

```text
Web search results for query: "GenIE autoregressive information extraction constrained decoding Josifoski 2022"

Links: [{"title":"GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub","url":"https://github.com/epfl-dlab/GenIE"},{"title":"GenIE: Generative Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.342/"},{"title":"[2112.08340] GenIE: Generative Information Extraction","url":"https://arxiv.org/abs/2112.08340"},{"title":"GenIE: Generative Information Extraction","url":"https://dlab.epfl.ch/people/west/pub/Josifoski-DeCao-Peyrard-Petroni-West_NAACL-22.pdf"},{"title":"(PDF) GenIE: Generative Information Extraction","url":"https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"},{"title":"Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction","url":"https://arxiv.org/html/2506.14901"},{"title":"GenIE: Generative Information Extraction | OpenReview","url":"https://openreview.net/forum?id=HxxjO7zS-c"},{"title":"GitHub - JanKalo/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub","url":"https://github.com/JanKalo/GenIE"},{"title":"GenIE: Generative Information Extraction | Request PDF","url":"https://www.researchgate.net/publication/357069468_GenIE_Generative_Information_Extraction"},{"title":"[2112.08340] GenIE: Generative Information Extraction - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2112.08340"}]

I've found comprehensive information about GenIE. Here's what the search results reveal:

## GenIE: Generative Information Extraction

GenIE is the first end-to-end autoregressive formulation of closed information extraction. The paper by Josifoski et al. was published in July 2022 at the NAACL conference (Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies).

### Key Approach

GenIE uses a sequence-to-sequence model that takes unstructured text as input and autoregressively generates a structured semantic representation of the information expressed in it, in the form of (subject, relation, object) triplets, as output.

### Constrained Decoding

GenIE employs constrained beam search with: (i) a high-level constraint which asserts that the output corresponds to a set of triplets; (ii) lower-level constraints which use prefix tries to force the model to only generate valid entity or relation identifiers (from a predefined schema).

### Advantages

Thanks to a bi-level constrained generation strategy, only triplets consistent with the predefined knowledge base schema are produced, and GenIE is state-of-the-art on closed information extraction, generalizes from fewer training data points than baselines, and scales to a previously unmanageable number of entities and relations.

The GitHub repository and paper are available, and the work has been influential in demonstrating how constrained decoding can enable autoregressive approaches to information extraction tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "35d32e0f-74fa-4c08-8616-308c5f584e9e",
  "tool_use_result": {
    "query": "GenIE autoregressive information extraction constrained decoding Josifoski 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PP92hSpvxau594TPRQKBo7",
        "content": [
          {
            "title": "GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub",
            "url": "https://github.com/epfl-dlab/GenIE"
          },
          {
            "title": "GenIE: Generative Information Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2022.naacl-main.342/"
          },
          {
            "title": "[2112.08340] GenIE: Generative Information Extraction",
            "url": "https://arxiv.org/abs/2112.08340"
          },
          {
            "title": "GenIE: Generative Information Extraction",
            "url": "https://dlab.epfl.ch/people/west/pub/Josifoski-DeCao-Peyrard-Petroni-West_NAACL-22.pdf"
          },
          {
            "title": "(PDF) GenIE: Generative Information Extraction",
            "url": "https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"
          },
          {
            "title": "Combining Constrained and Unconstrained Decoding via Boosting: BoostCD and Its Application to Information Extraction",
            "url": "https://arxiv.org/html/2506.14901"
          },
          {
            "title": "GenIE: Generative Information Extraction | OpenReview",
            "url": "https://openreview.net/forum?id=HxxjO7zS-c"
          },
          {
            "title": "GitHub - JanKalo/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub",
            "url": "https://github.com/JanKalo/GenIE"
          },
          {
            "title": "GenIE: Generative Information Extraction | Request PDF",
            "url": "https://www.researchgate.net/publication/357069468_GenIE_Generative_Information_Extraction"
          },
          {
            "title": "[2112.08340] GenIE: Generative Information Extraction - ar5iv",
            "url": "https://ar5iv.labs.arxiv.org/html/2112.08340"
          }
        ]
      },
      "I've found comprehensive information about GenIE. Here's what the search results reveal:\n\n## GenIE: Generative Information Extraction\n\nGenIE is the first end-to-end autoregressive formulation of closed information extraction. The paper by Josifoski et al. was published in July 2022 at the NAACL conference (Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies).\n\n### Key Approach\n\nGenIE uses a sequence-to-sequence model that takes unstructured text as input and autoregressively generates a structured semantic representation of the information expressed in it, in the form of (subject, relation, object) triplets, as output.\n\n### Constrained Decoding\n\nGenIE employs constrained beam search with: (i) a high-level constraint which asserts that the output corresponds to a set of triplets; (ii) lower-level constraints which use prefix tries to force the model to only generate valid entity or relation identifiers (from a predefined schema).\n\n### Advantages\n\nThanks to a bi-level constrained generation strategy, only triplets consistent with the predefined knowledge base schema are produced, and GenIE is state-of-the-art on closed information extraction, generalizes from fewer training data points than baselines, and scales to a previously unmanageable number of entities and relations.\n\nThe GitHub repository and paper are available, and the work has been influential in demonstrating how constrained decoding can enable autoregressive approaches to information extraction tasks."
    ],
    "durationSeconds": 5.447033479999998
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T19:49:09.875Z_

<details><summary>↩ Tool result · `toolu_01VjAZkTgrFFpvicPqyGg1fe`</summary>

```text
Web search results for query: "InstructUIE Multi-task Instruction Tuning Unified Information Extraction Wang 2023"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub","url":"https://github.com/BeyonderXX/InstructUIE"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"},{"title":"Unified Instruction Tuning (UIT)","url":"https://www.emergentmind.com/topics/unified-instruction-tuning-uit"},{"title":"InstructUIE: Unified Info Extraction Framework | PDF | Conceptual Model | Information","url":"https://www.scribd.com/document/797504751/2304-08085v1"},{"title":"InstructUIE: Multi-task Instruction Tuning for Uniﬁed Information Extraction","url":"https://arxiv.org/pdf/2304.08085"}]

Based on the search results, here's information about the InstructUIE paper:

## Overview

InstructUIE is a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency.

## Key Details

**Authors and Publication:** The paper was authored by Wang, Xiao and Zhou, Weikang and others, published on arXiv as preprint 2304.08085 in 2023

**Motivation:** Existing large models have difficulty with information extraction tasks - for example, gpt-3.5-turbo achieved an F1 score of 18.22 on the Ontonotes dataset, which is significantly lower than the state-of-the-art performance.

## Benchmark and Results

The paper introduces IE INSTRUCTIONS, a benchmark of 32 diverse information extraction datasets in a unified text-to-text format with expert-written instructions.

Experimental results demonstrate that the method achieves comparable performance to Bert in supervised settings and significantly outperforms the state-of-the-art and gpt3.5 in zero-shot settings.

## Framework Components

In the InstructUIE framework, auxiliary objectives cover entity span extraction, typing, pairing, relation classification, trigger, and argument extraction, in addition to the main tasks, to encourage the model to internalize structural phenomena generalizable across data sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "0f1526a3-dd8a-430f-a268-900615164455",
  "tool_use_result": {
    "query": "InstructUIE Multi-task Instruction Tuning Unified Information Extraction Wang 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UBmPMFoGjpjozP5rAsxDWJ",
        "content": [
          {
            "title": "[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://arxiv.org/abs/2304.08085"
          },
          {
            "title": "(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations",
            "url": "https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"
          },
          {
            "title": "GitHub - BeyonderXX/InstructUIE: Universal information extraction with instruction learning · GitHub",
            "url": "https://github.com/BeyonderXX/InstructUIE"
          },
          {
            "title": "[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"
          },
          {
            "title": "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"
          },
          {
            "title": "[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://arxiv.org/abs/2304.08085v1"
          },
          {
            "title": "Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://huggingface.co/papers/2304.08085"
          },
          {
            "title": "Unified Instruction Tuning (UIT)",
            "url": "https://www.emergentmind.com/topics/unified-instruction-tuning-uit"
          },
          {
            "title": "InstructUIE: Unified Info Extraction Framework | PDF | Conceptual Model | Information",
            "url": "https://www.scribd.com/document/797504751/2304-08085v1"
          },
          {
            "title": "InstructUIE: Multi-task Instruction Tuning for Uniﬁed Information Extraction",
            "url": "https://arxiv.org/pdf/2304.08085"
          }
        ]
      },
      "Based on the search results, here's information about the InstructUIE paper:\n\n## Overview\n\nInstructUIE is a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency.\n\n## Key Details\n\n**Authors and Publication:** The paper was authored by Wang, Xiao and Zhou, Weikang and others, published on arXiv as preprint 2304.08085 in 2023\n\n**Motivation:** Existing large models have difficulty with information extraction tasks - for example, gpt-3.5-turbo achieved an F1 score of 18.22 on the Ontonotes dataset, which is significantly lower than the state-of-the-art performance.\n\n## Benchmark and Results\n\nThe paper introduces IE INSTRUCTIONS, a benchmark of 32 diverse information extraction datasets in a unified text-to-text format with expert-written instructions.\n\nExperimental results demonstrate that the method achieves comparable performance to Bert in supervised settings and significantly outperforms the state-of-the-art and gpt3.5 in zero-shot settings.\n\n## Framework Components\n\nIn the InstructUIE framework, auxiliary objectives cover entity span extraction, typing, pairing, relation classification, trigger, and argument extraction, in addition to the main tasks, to encourage the model to internalize structural phenomena generalizable across data sources."
    ],
    "durationSeconds": 6.3154351349999995
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T19:49:11.416Z_

<details><summary>↩ Tool result · `toolu_01BKiArzgRiB4xcaoLGtdWDu`</summary>

```text
Web search results for query: "CodeIE code generation information extraction Li 2023 ACL"

Links: [{"title":"GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub","url":"https://github.com/artpli/CodeIE"},{"title":"CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.855/"},{"title":"[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711"},{"title":"[Quick Review] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://liner.com/review/codeie-large-code-generation-models-are-better-fewshot-information-extractors"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"c-ICL: Contrastive In-context Learning for Information Extraction","url":"https://arxiv.org/html/2402.11254v2"},{"title":"CODEIE: Large Code Generation Models are Better Few- ...","url":"https://aclanthology.org/2023.acl-long.855.pdf"},{"title":"[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors","url":"https://arxiv.org/abs/2305.05711v2"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://openreview.net/pdf/f43b52efa860ab47fd73ce13ebc5406b0838b585.pdf"}]

I found comprehensive information about CodeIE. Here's a summary:

## CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors

CodeIE is a paper published at ACL 2023 titled "Large Code Generation Models are Better Few-Shot Information Extractors". The paper was authored by Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu.

### Main Contribution

The paper proposes to recast structured output in the form of code instead of natural language and utilize generative LLMs of code (Code-LLMs) such as Codex to perform IE tasks, particularly named entity recognition and relation extraction. Code-LLMs can be well-aligned with these IE tasks by designing code-style prompts and formulating these IE tasks as code generation tasks.

### Key Results

Experiment results on seven benchmarks show that the method consistently outperforms fine-tuning moderate-size pre-trained models specially designed for IE tasks (e.g., UIE) and prompting NL-LLMs under few-shot settings. CodeIE formulates structured outputs as Python code elements like dictionaries and lists, which aligns well with Code-LLM pre-training data distribution.

### Official Resources

The official repository for CodeIE is available, and the paper is available through the ACL Anthology and on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "c8e1e75c-3d11-4ff3-b9d4-40a5a63c7263",
  "tool_use_result": {
    "query": "CodeIE code generation information extraction Li 2023 ACL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BujVpZ62Pgx1Hd1YCRo5Bj",
        "content": [
          {
            "title": "GitHub - artpli/CodeIE: [ACL 23] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors · GitHub",
            "url": "https://github.com/artpli/CodeIE"
          },
          {
            "title": "CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors - ACL Anthology",
            "url": "https://aclanthology.org/2023.acl-long.855/"
          },
          {
            "title": "[2305.05711] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors",
            "url": "https://arxiv.org/abs/2305.05711"
          },
          {
            "title": "[Quick Review] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors",
            "url": "https://liner.com/review/codeie-large-code-generation-models-are-better-fewshot-information-extractors"
          },
          {
            "title": "GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction",
            "url": "https://github.com/zjunlp/Low-resource-KEPapers"
          },
          {
            "title": "c-ICL: Contrastive In-context Learning for Information Extraction",
            "url": "https://arxiv.org/html/2402.11254v2"
          },
          {
            "title": "CODEIE: Large Code Generation Models are Better Few- ...",
            "url": "https://aclanthology.org/2023.acl-long.855.pdf"
          },
          {
            "title": "[2305.05711v2] CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors",
            "url": "https://arxiv.org/abs/2305.05711v2"
          },
          {
            "title": "Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Large Language Models for Generative Information Extraction: A Survey",
            "url": "https://openreview.net/pdf/f43b52efa860ab47fd73ce13ebc5406b0838b585.pdf"
          }
        ]
      },
      "I found comprehensive information about CodeIE. Here's a summary:\n\n## CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors\n\nCodeIE is a paper published at ACL 2023 titled \"Large Code Generation Models are Better Few-Shot Information Extractors\". The paper was authored by Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu.\n\n### Main Contribution\n\nThe paper proposes to recast structured output in the form of code instead of natural language and utilize generative LLMs of code (Code-LLMs) such as Codex to perform IE tasks, particularly named entity recognition and relation extraction. Code-LLMs can be well-aligned with these IE tasks by designing code-style prompts and formulating these IE tasks as code generation tasks.\n\n### Key Results\n\nExperiment results on seven benchmarks show that the method consistently outperforms fine-tuning moderate-size pre-trained models specially designed for IE tasks (e.g., UIE) and prompting NL-LLMs under few-shot settings. CodeIE formulates structured outputs as Python code elements like dictionaries and lists, which aligns well with Code-LLM pre-training data distribution.\n\n### Official Resources\n\nThe official repository for CodeIE is available, and the paper is available through the ACL Anthology and on arXiv."
    ],
    "durationSeconds": 6.990389415000002
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have information on all the papers. Let me verify the details:

1. **UniNER (Zhou et al. 2024)** - Already in literature_map with verified: false. Info matches: ICLR 2024, arXiv 2308.03279, authors: Wenxuan Zhou, Sheng Zhang, Yu Gu, Muhao Chen, Hoifung Poon.

2. **InstructUIE (Wang et al. 2023)** - 
   - Title: "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction"
   - arXiv: 2304.08085
   - Need to track down the complete author list

3. **GenIE (Josifoski et al. 2022)** - NAACL 2022, with authors Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, and Robert West.

4. **CodeIE (Li et al. 2023)** - ACL 2023, authored by Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, and Xipeng Qiu, showing how large code generation models can be effective few-shot information extractors. I should verify the author details for InstructUIE and GenIE to make sure I have them complete.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "606450d2-6ad4-49ca-9a8b-f13a72359a7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMT7yCg3duscn7CmVcpqH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 49265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 20_

Let me get the exact author lists for InstructUIE and GenIE.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "d0384d60-005c-4872-bcd6-208931a23823",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMT7yCg3duscn7CmVcpqH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 49265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015K42SWJUGB7G5yAh7mmVJ1`</summary>

```json
{
  "query": "arxiv 2304.08085 InstructUIE authors Xiao Wang Weikang Zhou"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "12604400-9e03-41be-86b1-64712b84eecf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMT7yCg3duscn7CmVcpqH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 49265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BWu4eciJcjU7AvegRCMxgU`</summary>

```json
{
  "query": "GenIE Generative Information Extraction Josifoski De Cao Peyrard NAACL 2022 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "e71a6f57-f000-4f34-ad81-70dc5d9267c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SMT7yCg3duscn7CmVcpqH9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2936,
      "cache_read_input_tokens": 49265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2936
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

_source line 23 · 2026-05-14T19:49:38.568Z_

<details><summary>↩ Tool result · `toolu_01BWu4eciJcjU7AvegRCMxgU`</summary>

```text
Web search results for query: "GenIE Generative Information Extraction Josifoski De Cao Peyrard NAACL 2022 authors"

Links: [{"title":"GenIE: Generative Information Extraction - ACL Anthology","url":"https://aclanthology.org/2022.naacl-main.342/"},{"title":"GenIE: Generative Information Extraction","url":"https://aclanthology.org/2022.naacl-main.342.pdf"},{"title":"GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub","url":"https://github.com/epfl-dlab/GenIE"},{"title":"GenIE: Generative Information Extraction","url":"https://infoscience.epfl.ch/entities/publication/ac96118e-64f4-4d05-8461-aa27321afaeb"},{"title":"[2112.08340] GenIE: Generative Information Extraction","url":"https://arxiv.org/abs/2112.08340"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=GenIE:+Generative+information+extraction&amp=&author=Martin+Josifoski&amp=&author=Nicola+De+Cao&amp=&author=Maxime+Peyrard&amp=&author=Fabio+Petroni&amp=&author=Robert+West&amp=&publication_year=2022&amp=&pages=4626-4643&amp=&doi=10.18653/v1/2022.naacl-main.342"},{"title":"(PDF) GenIE: Generative Information Extraction","url":"https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"},{"title":"Accepted Papers - NAACL-HLT 2022","url":"https://2022.naacl.org/program/accepted_papers/"},{"title":"[2112.08340] GenIE: Generative Information Extraction - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2112.08340"},{"title":"GenIE: Generative Information Extraction - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2112.08340"}]

Based on the web search results, here is information about the GenIE paper and its authors:

## Paper Details

GenIE: Generative Information Extraction was published by Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, and Robert West at NAACL 2022.

## Authors and Affiliations

The authors are affiliated with EPFL, the University of Amsterdam, the University of Edinburgh, and Meta AI.

## Paper Summary

GenIE introduces the first end-to-end autoregressive formulation of closed information extraction and naturally exploits the language knowledge from the pre-trained transformer by autoregressively generating relations and entities in textual form.

## Publication Information

The paper was published in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4626–4643, in Seattle, United States.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "290e5d08-797a-49af-befd-a5db618dbb90",
  "tool_use_result": {
    "query": "GenIE Generative Information Extraction Josifoski De Cao Peyrard NAACL 2022 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_0156wAUK9rdUokyD8obU8svE",
        "content": [
          {
            "title": "GenIE: Generative Information Extraction - ACL Anthology",
            "url": "https://aclanthology.org/2022.naacl-main.342/"
          },
          {
            "title": "GenIE: Generative Information Extraction",
            "url": "https://aclanthology.org/2022.naacl-main.342.pdf"
          },
          {
            "title": "GitHub - epfl-dlab/GenIE: The autoregressive information extraction system GenIE (Generative Information Extraction) implemented in PyTorch. · GitHub",
            "url": "https://github.com/epfl-dlab/GenIE"
          },
          {
            "title": "GenIE: Generative Information Extraction",
            "url": "https://infoscience.epfl.ch/entities/publication/ac96118e-64f4-4d05-8461-aa27321afaeb"
          },
          {
            "title": "[2112.08340] GenIE: Generative Information Extraction",
            "url": "https://arxiv.org/abs/2112.08340"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=GenIE:+Generative+information+extraction&amp=&author=Martin+Josifoski&amp=&author=Nicola+De+Cao&amp=&author=Maxime+Peyrard&amp=&author=Fabio+Petroni&amp=&author=Robert+West&amp=&publication_year=2022&amp=&pages=4626-4643&amp=&doi=10.18653/v1/2022.naacl-main.342"
          },
          {
            "title": "(PDF) GenIE: Generative Information Extraction",
            "url": "https://www.researchgate.net/publication/362262820_GenIE_Generative_Information_Extraction"
          },
          {
            "title": "Accepted Papers - NAACL-HLT 2022",
            "url": "https://2022.naacl.org/program/accepted_papers/"
          },
          {
            "title": "[2112.08340] GenIE: Generative Information Extraction - ar5iv",
            "url": "https://ar5iv.labs.arxiv.org/html/2112.08340"
          },
          {
            "title": "GenIE: Generative Information Extraction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2112.08340"
          }
        ]
      },
      "Based on the web search results, here is information about the GenIE paper and its authors:\n\n## Paper Details\n\nGenIE: Generative Information Extraction was published by Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, and Robert West at NAACL 2022.\n\n## Authors and Affiliations\n\nThe authors are affiliated with EPFL, the University of Amsterdam, the University of Edinburgh, and Meta AI.\n\n## Paper Summary\n\nGenIE introduces the first end-to-end autoregressive formulation of closed information extraction and naturally exploits the language knowledge from the pre-trained transformer by autoregressively generating relations and entities in textual form.\n\n## Publication Information\n\nThe paper was published in the Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages 4626–4643, in Seattle, United States."
    ],
    "durationSeconds": 4.352979645
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T19:49:40.132Z_

<details><summary>↩ Tool result · `toolu_015K42SWJUGB7G5yAh7mmVJ1`</summary>

```text
Web search results for query: "arxiv 2304.08085 InstructUIE authors Xiao Wang Weikang Zhou"

Links: [{"title":"[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085"},{"title":"arXiv:2304.08085v1 [cs.CL] 17 Apr 2023","url":"https://arxiv.org/pdf/2304.08085"},{"title":"[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://arxiv.org/abs/2304.08085v1"},{"title":"Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://huggingface.co/papers/2304.08085"},{"title":"InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction","url":"https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"},{"title":"(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations","url":"https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"},{"title":"[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/InstructUIE:-Multi-task-Instruction-Tuning-for-Wang-Zhou/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"},{"title":"Computation and Language Apr 2023","url":"https://web3.arxiv.org/list/cs.CL/2023-04?skip=275&show=25"},{"title":"weikang zhou - Google 学术搜索","url":"https://scholar.google.com/citations?user=_ypk7UkAAAAJ&hl=zh-CN"},{"title":"SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning","url":"https://arxiv.org/html/2602.13515v1"}]

The search results successfully locate the paper arxiv 2304.08085 on InstructUIE. Here's what I found:

## Paper Details

**Title:** InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction

**Authors:** Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du

**Published:** April 17, 2023

**ArXiv ID:** 2304.08085

## Summary

The paper proposes InstructUIE, a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency. The authors introduce IE INSTRUCTIONS, a benchmark of 32 diverse information extraction datasets in a unified text-to-text format with expert-written instructions.

InstructUIE achieves superior zero-shot performance compared to state-of-the-art models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "6abe5021-7bfd-4224-aa73-13f03a7a04d7",
  "tool_use_result": {
    "query": "arxiv 2304.08085 InstructUIE authors Xiao Wang Weikang Zhou",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NDiQtJkhvUfVcQy2jhpwbC",
        "content": [
          {
            "title": "[2304.08085] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://arxiv.org/abs/2304.08085"
          },
          {
            "title": "arXiv:2304.08085v1 [cs.CL] 17 Apr 2023",
            "url": "https://arxiv.org/pdf/2304.08085"
          },
          {
            "title": "[2304.08085v1] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://arxiv.org/abs/2304.08085v1"
          },
          {
            "title": "Paper page - InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://huggingface.co/papers/2304.08085"
          },
          {
            "title": "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction",
            "url": "https://www.researchgate.net/publication/370071546_InstructUIE_Multi-task_Instruction_Tuning_for_Unified_Information_Extraction"
          },
          {
            "title": "(PDF) InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction (2023) | Xiao Wang | 81 Citations",
            "url": "https://scispace.com/papers/instructuie-multi-task-instruction-tuning-for-unified-qe70ci1r"
          },
          {
            "title": "[PDF] InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/InstructUIE:-Multi-task-Instruction-Tuning-for-Wang-Zhou/bbb2fc6e95d24fb58ab6c25b216b14ac49a32fbe"
          },
          {
            "title": "Computation and Language Apr 2023",
            "url": "https://web3.arxiv.org/list/cs.CL/2023-04?skip=275&show=25"
          },
          {
            "title": "weikang zhou - Google 学术搜索",
            "url": "https://scholar.google.com/citations?user=_ypk7UkAAAAJ&hl=zh-CN"
          },
          {
            "title": "SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning",
            "url": "https://arxiv.org/html/2602.13515v1"
          }
        ]
      },
      "The search results successfully locate the paper arxiv 2304.08085 on InstructUIE. Here's what I found:\n\n## Paper Details\n\n**Title:** InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction\n\n**Authors:** Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du\n\n**Published:** April 17, 2023\n\n**ArXiv ID:** 2304.08085\n\n## Summary\n\nThe paper proposes InstructUIE, a unified information extraction framework based on instruction tuning, which can uniformly model various information extraction tasks and capture the inter-task dependency. The authors introduce IE INSTRUCTIONS, a benchmark of 32 diverse information extraction datasets in a unified text-to-text format with expert-written instructions.\n\nInstructUIE achieves superior zero-shot performance compared to state-of-the-art models."
    ],
    "durationSeconds": 6.143476103000001
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile:

1. **UniNER (Zhou et al. 2024)** - Already in literature_map. I need to:
   - Add bib entry to references.bib
   - Change verified to true in literature_map.yaml

2. **InstructUIE (Wang et al. 2023)**
   - Title: "InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction"
   - Authors: Xiao Wang, Weikang Zhou, Can Zu, Han Xia, Tianze Chen, Yuansen Zhang, Rui Zheng, Junjie Ye, Qi Zhang, Tao Gui, Jihua Kang, Jingsheng Yang, Siyuan Li, Chunsai Du
   - arXiv: 2304.08085, published in 2023 as a preprint
   - bibtex_key: wang2023instructuie

3. **GenIE (Josifoski et al. 2022)** - NAACL 2022
   - Title: "GenIE: Generative Information Extraction"
   - Authors: Martin Josifoski, Nicola De Cao, Maxime Peyrard, Fabio Petroni, Robert West
   - arXiv: 2112.08340
   - DOI: 10.18653/v1/2022.naacl-main.342
   - bibtex_key: josifoski2022genie

4. **CodeIE (Li et al. 2023)** - ACL 2023
   - Title: "CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors"
   - Authors: Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuanbin Wu, Xuanjing Huang, Xipeng Qiu
   - arXiv: 2305.05711
   - bibtex_key: li2023codeie

Both papers fit the requirement for structured generation and constrained decoding in IE—GenIE pioneered constrained decoding for closed IE while CodeIE leverages code generation for the task. Now I need to figure out where these entries go alphabetically in the references file, looking at the existing entries starting with angelopoulos through desai. I'm continuing through the bibliography, adding the three new entries in their alphabetical positions within the existing list.

Now I need to verify the alphabetical ordering more carefully for the entries I'm inserting. Looking at the bibtex keys character by character: josifoski comes after jagannatha but before kadavath, that checks out. For li2023codeie, it slots between lakshminarayanan and lightman correctly. But for wang2023instructuie versus wang2023selfconsistency, I need to compare the keywords after the year — "instructuie" starts with 'i' while "selfconsistency" starts with 's', so instructuie should come first alphabetically.

I also notice zhou2024uniner needs to be added at the end after zhang2023ener. I need to make three main changes: add the four bibliography entries in the right alphabetical spots, update the literature map with the new IE papers, and mark zhou2024uniner as verified. Let me verify InstructUIE's publication status since the search results are a bit unclear—it looks like it's been on arXiv since April 2023, and I should confirm whether it was published in a venue or remains a preprint.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "edb2cd4d-1f39-407d-b008-6d9ec36a5895",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA7Cxt5fZHxFLAmwLtT4WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
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

_source line 26_

I have all the verified information. Now I'll add the BibTeX entries and update the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "e680cd04-f60e-4f70-8452-d64f6ccf85a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA7Cxt5fZHxFLAmwLtT4WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
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

<details open><summary>🔧 Tool call — Edit · `toolu_01U5Ken6yTAk4BcPE8ngAB2d`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@article{kadavath2022language,",
  "new_string": "@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "a9a0dc10-b61c-41b6-884e-caeacbe24164",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA7Cxt5fZHxFLAmwLtT4WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
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

_source line 28 · 2026-05-14T19:50:21.566Z_

<details><summary>↩ Tool result · `toolu_01U5Ken6yTAk4BcPE8ngAB2d`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "15838dfd-db6d-4a15-a1fe-0bda301ce84c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@article{kadavath2022language,",
    "newString": "@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{bates2021rcps,\n  title = {Distribution-free, Risk-controlling Prediction Sets},\n  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},\n  journal = {Journal of the ACM},\n  year = {2021},\n  doi = {10.1145/3478535},\n  url = {http://dx.doi.org/10.1145/3478535}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Frédéric and Guzmán, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330},\n  url = {http://dx.doi.org/10.1162/tacl_a_00330}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{jagannatha2020calibrating,\n  title = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {ACL 2020},\n  year = {2020},\n  url = {https://aclanthology.org/2020.acl-main.188/}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {NeurIPS 2015},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{liu2025uqcalibration,\n  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},\n  author = {Liu, Xiaoou and Chen, Tiejin and Da, Longchao and Chen, Chacha and Lin, Zhen and Wei, Hua},\n  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},\n  year = {2025},\n  doi = {10.1145/3711896.3736569},\n  url = {http://dx.doi.org/10.1145/3711896.3736569}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{ren2023selfevaluation,\n  title = {Self-Evaluation Improves Selective Generation in Large Language Models},\n  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji},\n  booktitle = {NeurIPS 2023 Workshop},\n  year = {2023},\n  url = {https://arxiv.org/abs/2312.09300}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wan2025rasc,\n  title = {Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling},\n  author = {Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},\n  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2025},\n  doi = {10.18653/v1/2025.naacl-long.184},\n  url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@article{wu2024inference,\n  title = {Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models},\n  author = {Wu, Yangzhen and Sun, Zhiqing and Li, Shanda and Welleck, Sean and Yang, Yiming},\n  journal = {arXiv preprint arXiv:2408.00724},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.00724}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 152,
        "oldLines": 6,
        "newStart": 152,
        "newLines": 15,
        "lines": [
          "   url = {https://aclanthology.org/2020.acl-main.188/}",
          " }",
          " ",
          "+@inproceedings{josifoski2022genie,",
          "+  title = {{GenIE}: Generative Information Extraction},",
          "+  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},",
          "+  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},",
          "+  year = {2022},",
          "+  doi = {10.18653/v1/2022.naacl-main.342},",
          "+  url = {https://arxiv.org/abs/2112.08340}",
          "+}",
          "+",
          " @article{kadavath2022language,",
          "   title = {Language Models (Mostly) Know What They Know},",
          "   author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},"
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_011VQCQ4onLzU359BSQDQjbS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{lightman2024verify,",
  "new_string": "@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "b17526af-3f84-491d-82be-d3d10dcc2555",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA7Cxt5fZHxFLAmwLtT4WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
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

_source line 30 · 2026-05-14T19:50:23.916Z_

<details><summary>↩ Tool result · `toolu_011VQCQ4onLzU359BSQDQjbS`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "efa46643-ad1c-4cf0-8a17-1101f6f222fc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{lightman2024verify,",
    "newString": "@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{bates2021rcps,\n  title = {Distribution-free, Risk-controlling Prediction Sets},\n  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},\n  journal = {Journal of the ACM},\n  year = {2021},\n  doi = {10.1145/3478535},\n  url = {http://dx.doi.org/10.1145/3478535}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Frédéric and Guzmán, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330},\n  url = {http://dx.doi.org/10.1162/tacl_a_00330}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{jagannatha2020calibrating,\n  title = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {ACL 2020},\n  year = {2020},\n  url = {https://aclanthology.org/2020.acl-main.188/}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {NeurIPS 2015},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{liu2025uqcalibration,\n  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},\n  author = {Liu, Xiaoou and Chen, Tiejin and Da, Longchao and Chen, Chacha and Lin, Zhen and Wei, Hua},\n  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},\n  year = {2025},\n  doi = {10.1145/3711896.3736569},\n  url = {http://dx.doi.org/10.1145/3711896.3736569}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{ren2023selfevaluation,\n  title = {Self-Evaluation Improves Selective Generation in Large Language Models},\n  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji},\n  booktitle = {NeurIPS 2023 Workshop},\n  year = {2023},\n  url = {https://arxiv.org/abs/2312.09300}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wan2025rasc,\n  title = {Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling},\n  author = {Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},\n  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2025},\n  doi = {10.18653/v1/2025.naacl-long.184},\n  url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@article{wu2024inference,\n  title = {Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models},\n  author = {Wu, Yangzhen and Sun, Zhiqing and Li, Shanda and Welleck, Sean and Yang, Yiming},\n  journal = {arXiv preprint arXiv:2408.00724},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.00724}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 217,
        "oldLines": 6,
        "newStart": 217,
        "newLines": 15,
        "lines": [
          "   url = {https://arxiv.org/abs/1612.01474}",
          " }",
          " ",
          "+@inproceedings{li2023codeie,",
          "+  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},",
          "+  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},",
          "+  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},",
          "+  year = {2023},",
          "+  doi = {10.18653/v1/2023.acl-long.855},",
          "+  url = {https://arxiv.org/abs/2305.05711}",
          "+}",
          "+",
          " @inproceedings{lightman2024verify,",
          "   title = {Let's Verify Step by Step},",
          "   author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},"
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

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01GTz6cGA5DxBneV1gufAX5P`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{wang2023selfconsistency,",
  "new_string": "@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "e9ec6ef6-36d4-42c6-bfa6-affea6ab26a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA7Cxt5fZHxFLAmwLtT4WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
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

_source line 32 · 2026-05-14T19:50:26.739Z_

<details><summary>↩ Tool result · `toolu_01GTz6cGA5DxBneV1gufAX5P`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "c2d8c29f-a520-4092-82b5-001d7bd6ccaf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{wang2023selfconsistency,",
    "newString": "@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{bates2021rcps,\n  title = {Distribution-free, Risk-controlling Prediction Sets},\n  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},\n  journal = {Journal of the ACM},\n  year = {2021},\n  doi = {10.1145/3478535},\n  url = {http://dx.doi.org/10.1145/3478535}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Frédéric and Guzmán, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330},\n  url = {http://dx.doi.org/10.1162/tacl_a_00330}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{jagannatha2020calibrating,\n  title = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {ACL 2020},\n  year = {2020},\n  url = {https://aclanthology.org/2020.acl-main.188/}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {NeurIPS 2015},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{liu2025uqcalibration,\n  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},\n  author = {Liu, Xiaoou and Chen, Tiejin and Da, Longchao and Chen, Chacha and Lin, Zhen and Wei, Hua},\n  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},\n  year = {2025},\n  doi = {10.1145/3711896.3736569},\n  url = {http://dx.doi.org/10.1145/3711896.3736569}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{ren2023selfevaluation,\n  title = {Self-Evaluation Improves Selective Generation in Large Language Models},\n  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji},\n  booktitle = {NeurIPS 2023 Workshop},\n  year = {2023},\n  url = {https://arxiv.org/abs/2312.09300}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wan2025rasc,\n  title = {Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling},\n  author = {Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},\n  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2025},\n  doi = {10.18653/v1/2025.naacl-long.184},\n  url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@article{wu2024inference,\n  title = {Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models},\n  author = {Wu, Yangzhen and Sun, Zhiqing and Li, Shanda and Welleck, Sean and Yang, Yiming},\n  journal = {arXiv preprint arXiv:2408.00724},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.00724}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 364,
        "oldLines": 6,
        "newStart": 364,
        "newLines": 14,
        "lines": [
          "   url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}",
          " }",
          " ",
          "+@article{wang2023instructuie,",
          "+  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},",
          "+  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},",
          "+  journal = {arXiv preprint arXiv:2304.08085},",
          "+  year = {2023},",
          "+  url = {https://arxiv.org/abs/2304.08085}",
          "+}",
          "+",
          " @inproceedings{wang2023selfconsistency,",
          "   title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},",
          "   author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},"
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01YVNCz16YV1jzcwi6QUYQJ4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "  bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'",
  "new_string": "  bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  josifoski2022genie:\n    title: 'GenIE: Generative Information Extraction'\n    authors:\n    - Martin Josifoski\n    - Nicola De Cao\n    - Maxime Peyrard\n    - Fabio Petroni\n    - Robert West\n    year: 2022\n    venue: NAACL 2022\n    url: https://arxiv.org/abs/2112.08340\n    doi: 10.18653/v1/2022.naacl-main.342\n    bibtex_key: josifoski2022genie\n    category: generative_ie\n    role: foundation\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  li2023codeie:\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\n    authors:\n    - Peng Li\n    - Tianxiang Sun\n    - Qiong Tang\n    - Hang Yan\n    - Yuanbin Wu\n    - Xuanjing Huang\n    - Xipeng Qiu\n    year: 2023\n    venue: ACL 2023\n    url: https://arxiv.org/abs/2305.05711\n    doi: 10.18653/v1/2023.acl-long.855\n    bibtex_key: li2023codeie\n    category: generative_ie\n    role: background\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\n      alternative structured generation approach complementary to constrained decoding.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  wang2023instructuie:\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\n    authors:\n    - Xiao Wang\n    - Weikang Zhou\n    - Can Zu\n    - Han Xia\n    - Tianze Chen\n    - Yuansen Zhang\n    - Rui Zheng\n    - Junjie Ye\n    - Qi Zhang\n    - Tao Gui\n    - Jihua Kang\n    - Jingsheng Yang\n    - Siyuan Li\n    - Chunsai Du\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2304.08085\n    doi: ''\n    bibtex_key: wang2023instructuie\n    category: generative_ie\n    role: foundation\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "87653fe5-6c11-4e53-9dc2-b306f37e0d04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MA7Cxt5fZHxFLAmwLtT4WL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 860,
      "cache_creation_input_tokens": 1612,
      "cache_read_input_tokens": 52201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1612
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

_source line 34 · 2026-05-14T19:50:43.071Z_

<details><summary>↩ Tool result · reported error · `toolu_01YVNCz16YV1jzcwi6QUYQJ4`</summary>

```text
&lt;tool_use_error>String to replace not found in file.
String:   bibtex_key: zhang2023ener
    category: token_span_uncertainty_ner
    role: background
    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and
      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.
    abstract: ''
    semantic_scholar_id: ''
    verified: true
    added_by: paper-research:lit_batch2
    added_at: '2026-05-14T18:10:52.000Z'&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "14b99868-9d4e-4b8b-993b-089e8105e66a",
  "tool_use_result": "Error: String to replace not found in file.\nString:   bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'"
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
I made the error because I was trying to edit the literature_map.yaml but wrote references.bib as the file_path. Let me now do the edits on literature_map.yaml. Also I need to add the zhou2024uniner bib entry to references.bib and change verified to true in literature_map.yaml.

Let me first add the zhou2024uniner entry to references.bib (at the end, after zhang2023ener), then edit the literature_map.yaml.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "bfca9a48-d419-49e0-a938-ac917909bf5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2e5A4umK5A1QLNyEeaYzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
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

_source line 36_

Now let me add the zhou2024uniner bib entry at the end of references.bib and update literature_map.yaml.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "ba59f421-fc10-4bb6-846f-c56804b6bce0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2e5A4umK5A1QLNyEeaYzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01BFEMfPvPpoxNwwVuMLjLTd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 440,
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "b21262e5-e752-4197-8c6c-cbbb3197f525",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K2e5A4umK5A1QLNyEeaYzY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5449,
      "cache_read_input_tokens": 53813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5449
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

_source line 38 · 2026-05-14T19:50:51.400Z_

<details><summary>↩ Tool result · `toolu_01BFEMfPvPpoxNwwVuMLjLTd`</summary>

```text
440	  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}
441	}
442	
443	@inproceedings{xiong2024verbalized,
444	  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},
445	  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},
446	  booktitle = {ICLR 2024},
447	  year = {2024},
448	  url = {https://arxiv.org/abs/2306.13063}
449	}
450	
451	@inproceedings{zhang2023ener,
452	  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},
453	  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},
454	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},
455	  year = {2023},
456	  doi = {10.18653/v1/2023.findings-acl.103},
457	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
458	}
459	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "27454065-f2d5-43df-bfef-f1238bccf20c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n",
      "numLines": 20,
      "startLine": 440,
      "totalLines": 459
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01Eabg1CuT1HpY99sfTgezhr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "old_string": "@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}",
  "new_string": "@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "ab6827b0-0bc4-4088-bf6a-d52281a617d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KCHsGr64SM84vKWrbdMSFY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 706,
      "cache_read_input_tokens": 59262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 706
      },
      "output_tokens": 67,
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

_source line 40 · 2026-05-14T19:51:01.727Z_

<details><summary>↩ Tool result · `toolu_01Eabg1CuT1HpY99sfTgezhr`</summary>

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
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "607e4927-9095-4a24-8bc4-f504aa3e153c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "oldString": "@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}",
    "newString": "@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}",
    "originalFile": "% Auto-generated from literature_map.yaml — do not edit manually\n\n@inproceedings{angelopoulos2021conformal,\n  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},\n  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},\n  booktitle = {ICLR 2021},\n  year = {2021},\n  url = {https://arxiv.org/abs/2009.14193}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{bates2021rcps,\n  title = {Distribution-free, Risk-controlling Prediction Sets},\n  author = {Bates, Stephen and Angelopoulos, Anastasios and Lei, Lihua and Malik, Jitendra and Jordan, Michael},\n  journal = {Journal of the ACM},\n  year = {2021},\n  doi = {10.1145/3478535},\n  url = {http://dx.doi.org/10.1145/3478535}\n}\n\n@article{brown2024monkeys,\n  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},\n  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},\n  journal = {arXiv preprint arXiv:2407.21787},\n  year = {2024},\n  url = {https://arxiv.org/abs/2407.21787}\n}\n\n@inproceedings{chen2024usc,\n  title = {Universal Self-Consistency for Large Language Model Generation},\n  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},\n  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2311.17311}\n}\n\n@article{cobbe2021verifiers,\n  title = {Training Verifiers to Solve Math Word Problems},\n  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},\n  journal = {arXiv preprint arXiv:2110.14168},\n  year = {2021},\n  url = {https://arxiv.org/abs/2110.14168}\n}\n\n@inproceedings{culotta2004confidence,\n  title = {Confidence Estimation for Information Extraction},\n  author = {Culotta, Aron and McCallum, Andrew},\n  booktitle = {HLT-NAACL 2004},\n  year = {2004},\n  url = {https://aclanthology.org/N04-4028/}\n}\n\n@inproceedings{derczynski2017wnut,\n  title = {Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition},\n  author = {Derczynski, Leon and Nichols, Eric and Erp, Marieke van and Limsopatham, Nut},\n  booktitle = {W-NUT Workshop at EMNLP 2017},\n  year = {2017},\n  url = {https://aclanthology.org/W17-4418/}\n}\n\n@inproceedings{desai2020calibration,\n  title = {Calibration of Pre-trained Transformers},\n  author = {Desai, Shrey and Durrett, Greg},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year = {2020},\n  doi = {10.18653/v1/2020.emnlp-main.21},\n  url = {http://dx.doi.org/10.18653/v1/2020.emnlp-main.21}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{fisch2021conformal,\n  title = {Few-Shot Conformal Prediction with Auxiliary Tasks},\n  author = {Fisch, Adam and Schuster, Tal and Jaakkola, Tommi and Barzilay, Regina},\n  booktitle = {ICML 2021},\n  year = {2021},\n  doi = {10.5555/3524938.3525234},\n  url = {https://arxiv.org/abs/2102.08898}\n}\n\n@article{fleiss1971agreement,\n  title = {Measuring nominal scale agreement among many raters.},\n  author = {Fleiss, Joseph L.},\n  journal = {Psychological Bulletin},\n  year = {1971},\n  doi = {10.1037/h0031619},\n  url = {http://dx.doi.org/10.1037/h0031619}\n}\n\n@article{fomicheva2020unsupervised,\n  title = {Unsupervised Quality Estimation for Neural Machine Translation},\n  author = {Fomicheva, Marina and Sun, Shuo and Yankovskaya, Lisa and Blain, Frédéric and Guzmán, Francisco and Fishel, Mark and Aletras, Nikolaos and Chaudhary, Vishrav and Specia, Lucia},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2020},\n  doi = {10.1162/tacl_a_00330},\n  url = {http://dx.doi.org/10.1162/tacl_a_00330}\n}\n\n@inproceedings{gal2016dropout,\n  title = {Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n  author = {Gal, Yarin and Ghahramani, Zoubin},\n  booktitle = {ICML 2016},\n  year = {2016},\n  url = {https://arxiv.org/abs/1506.02142}\n}\n\n@inproceedings{geifman2017selective,\n  title = {Selective Classification for Deep Neural Networks},\n  author = {Geifman, Yonatan and El-Yaniv, Ran},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1705.08500}\n}\n\n@inproceedings{geng2024confidence,\n  title = {A Survey of Confidence Estimation and Calibration in Large Language Models},\n  author = {Geng, Jiahui and Cai, Fengyu and Wang, Yuxia and Koeppl, Heinz and Nakov, Preslav and Gurevych, Iryna},\n  booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2024},\n  doi = {10.18653/v1/2024.naacl-long.366},\n  url = {http://dx.doi.org/10.18653/v1/2024.naacl-long.366}\n}\n\n@inproceedings{guo2017calibration,\n  title = {On Calibration of Modern Neural Networks},\n  author = {Guo, Chuan and Pleiss, Geoff and Sun, Yu and Weinberger, Kilian Q.},\n  booktitle = {ICML 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1706.04599}\n}\n\n@article{hobelsberger2025systematic,\n  title = {Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models},\n  author = {Hobelsberger, Christian and Winner, Theresa and Nawroth, Andreas and Mitevski, Oliver and Haensch, Anna-Carolina},\n  journal = {arXiv preprint arXiv:2510.20460},\n  year = {2025},\n  url = {https://arxiv.org/abs/2510.20460}\n}\n\n@article{jaccard1901distribution,\n  title = {Étude comparative de la distribution florale dans une portion des Alpes et du Jura},\n  author = {Jaccard, Paul},\n  journal = {Bulletin de la Société Vaudoise des Sciences Naturelles},\n  year = {1901},\n  url = {https://www.researchgate.net/publication/225035806}\n}\n\n@inproceedings{jagannatha2020calibrating,\n  title = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {ACL 2020},\n  year = {2020},\n  url = {https://aclanthology.org/2020.acl-main.188/}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},\n  year = {2022},\n  url = {https://arxiv.org/abs/2207.05221}\n}\n\n@inproceedings{kang2025selfcertainty,\n  title = {Scalable Best-of-N Selection for Large Language Models via Self-Certainty},\n  author = {Kang, Zhewei and Zhao, Xuandong and Song, Dawn},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.18581}\n}\n\n@inproceedings{kim2026reasc,\n  title = {Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in {LLM} Reasoning},\n  author = {Kim, Junseok and Yang, Nakyeong and Min, Kyungmin and Jung, Kyomin},\n  booktitle = {ACL 2026},\n  year = {2026},\n  url = {https://arxiv.org/abs/2601.02970}\n}\n\n@article{kossen2024semantic,\n  title = {Semantic Entropy Probes: Robust and Cheap Hallucination Detection in {LLMs}},\n  author = {Kossen, Jannik and Han, Jiatong and Razzak, Muhammed and Schut, Lisa and Malik, Shreshth and Gal, Yarin},\n  journal = {arXiv preprint arXiv:2406.15927},\n  year = {2024},\n  url = {https://arxiv.org/abs/2406.15927}\n}\n\n@inproceedings{kuhn2023semantic,\n  title = {Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation},\n  author = {Kuhn, Lorenz and Gal, Yarin and Farquhar, Sebastian},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2302.09664}\n}\n\n@inproceedings{kuleshov2015calibrated,\n  title = {Calibrated Structured Prediction},\n  author = {Kuleshov, Volodymyr and Liang, Percy},\n  booktitle = {NeurIPS 2015},\n  year = {2015},\n  url = {https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n  title = {Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n  author = {Lakshminarayanan, Balaji and Pritzel, Alexander and Blundell, Charles},\n  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{liu2025uqcalibration,\n  title = {Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey},\n  author = {Liu, Xiaoou and Chen, Tiejin and Da, Longchao and Chen, Chacha and Lin, Zhen and Wei, Hua},\n  booktitle = {Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V.2},\n  year = {2025},\n  doi = {10.1145/3711896.3736569},\n  url = {http://dx.doi.org/10.1145/3711896.3736569}\n}\n\n@inproceedings{luan2018scierc,\n  title = {Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction},\n  author = {Luan, Yi and He, Luheng and Ostendorf, Mari and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n  year = {2018},\n  doi = {10.18653/v1/D18-1360},\n  url = {http://dx.doi.org/10.18653/v1/D18-1360}\n}\n\n@inproceedings{manakul2023selfcheckgpt,\n  title = {SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models},\n  author = {Manakul, Potsawee and Liusie, Adian and Gales, Mark},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  year = {2023},\n  doi = {10.18653/v1/2023.emnlp-main.557},\n  url = {http://dx.doi.org/10.18653/v1/2023.emnlp-main.557}\n}\n\n@article{nedellec2026consistency,\n  title = {Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data},\n  author = {Yao, Xinzhi and Nédellec, Claire and Xia, Jingbo and Bossy, Robert},\n  journal = {Genomics \\& Informatics},\n  year = {2026},\n  doi = {10.1186/s44342-025-00063-2},\n  url = {http://dx.doi.org/10.1186/s44342-025-00063-2}\n}\n\n@article{oh2025latentsc,\n  title = {Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning},\n  author = {Oh, Jungsuk and Lee, Jay-Yoon},\n  journal = {arXiv preprint arXiv:2508.18395},\n  year = {2025},\n  url = {https://arxiv.org/abs/2508.18395}\n}\n\n@inproceedings{ren2023selfevaluation,\n  title = {Self-Evaluation Improves Selective Generation in Large Language Models},\n  author = {Ren, Jie and Zhao, Yao and Vu, Tu and Liu, Peter J. and Lakshminarayanan, Balaji},\n  booktitle = {NeurIPS 2023 Workshop},\n  year = {2023},\n  url = {https://arxiv.org/abs/2312.09300}\n}\n\n@inproceedings{sainz2024gollie,\n  title = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n  author = {Sainz, Oscar and García-Ferrero, Iker and Agerri, Rodrigo and Lacalle, Oier Lopez de and Rigau, German and Agirre, Eneko},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2310.03668}\n}\n\n@inproceedings{shelmanov2021active,\n  title = {Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates},\n  author = {Shelmanov, Artem and Puzyrev, Dmitri and Kupriyanova, Lyubov and Belyakov, Denis and Larionov, Daniil and Khromov, Nikita and Kozlova, Olga and Artemova, Ekaterina and Dylov, Dmitry V. and Panchenko, Alexander},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.145},\n  url = {http://dx.doi.org/10.18653/v1/2021.eacl-main.145}\n}\n\n@inproceedings{snell2024scaling,\n  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},\n  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},\n  booktitle = {ICLR 2025},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.03314}\n}\n\n@inproceedings{taubenfeld2025cisc,\n  title = {Confidence Improves Self-Consistency in LLMs},\n  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year = {2025},\n  doi = {10.18653/v1/2025.findings-acl.1030},\n  url = {http://dx.doi.org/10.18653/v1/2025.findings-acl.1030}\n}\n\n@inproceedings{thirukovalluru2024atomic,\n  title = {Atomic Self-Consistency for Better Long Form Generations},\n  author = {Thirukovalluru, Raghuveer and Huang, Yukun and Dhingra, Bhuwan},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n  year = {2024},\n  doi = {10.18653/v1/2024.emnlp-main.706},\n  url = {http://dx.doi.org/10.18653/v1/2024.emnlp-main.706}\n}\n\n@inproceedings{tjongkimsang2003conll,\n  title = {Introduction to the {CoNLL}-2003 Shared Task: Language-Independent Named Entity Recognition},\n  author = {Sang, Erik F. Tjong Kim and Meulder, Fien De},\n  booktitle = {CoNLL 2003},\n  year = {2003},\n  url = {https://aclanthology.org/W03-0419/}\n}\n\n@inproceedings{vashurin2025cocoa,\n  title = {Uncertainty Quantification for {LLMs} through Minimum Bayes Risk: Bridging Confidence and Consistency},\n  author = {Vashurin, Roman and Goloburda, Maiya and Ilina, Albina and Rubashevskii, Aleksandr and Nakov, Preslav and Shelmanov, Artem and Panov, Maxim},\n  booktitle = {NeurIPS 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2502.04964}\n}\n\n@inproceedings{wadhwa2023revisiting,\n  title = {Revisiting Relation Extraction in the era of Large Language Models},\n  author = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.868},\n  url = {http://dx.doi.org/10.18653/v1/2023.acl-long.868}\n}\n\n@inproceedings{wan2025rasc,\n  title = {Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling},\n  author = {Wan, Guangya and Wu, Yuqi and Chen, Jie and Li, Sheng},\n  booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n  year = {2025},\n  doi = {10.18653/v1/2025.naacl-long.184},\n  url = {http://dx.doi.org/10.18653/v1/2025.naacl-long.184}\n}\n\n@article{wang2023instructuie,\n  title = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n  author = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}\n\n@inproceedings{wang2025rankedvoting,\n  title = {Ranked Voting based Self-Consistency of Large Language Models},\n  author = {Wang, Weiqin and Wang, Yile and Huang, Hui},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://arxiv.org/abs/2505.10772}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@article{wen2025know,\n  title = {Know Your Limits: A Survey of Abstention in Large Language Models},\n  author = {Wen, Bingbing and Yao, Jihan and Feng, Shangbin and Xu, Chenjun and Tsvetkov, Yulia and Howe, Bill and Wang, Lucy Lu},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year = {2025},\n  doi = {10.1162/tacl_a_00754},\n  url = {http://dx.doi.org/10.1162/tacl_a_00754}\n}\n\n@article{willard2023guided,\n  title = {Efficient Guided Generation for Large Language Models},\n  author = {Willard, Brandon T. and Louf, Rémi},\n  journal = {arXiv preprint arXiv:2307.09702},\n  year = {2023},\n  url = {https://arxiv.org/abs/2307.09702}\n}\n\n@article{wu2024inference,\n  title = {Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models},\n  author = {Wu, Yangzhen and Sun, Zhiqing and Li, Shanda and Welleck, Sean and Yang, Yiming},\n  journal = {arXiv preprint arXiv:2408.00724},\n  year = {2024},\n  url = {https://arxiv.org/abs/2408.00724}\n}\n\n% SUPPLEMENTARY — not cited in main text\n@inproceedings{xia2025survey,\n  title = {A Survey of Uncertainty Estimation Methods on Large Language Models},\n  author = {Xia, Zhiqiu and Xu, Jinxuan and Zhang, Yuqian and Liu, Hang},\n  booktitle = {ACL Findings 2025},\n  year = {2025},\n  url = {https://aclanthology.org/2025.findings-acl.1101/}\n}\n\n@article{xiao2019uncertainty,\n  title = {Quantifying Uncertainties in Natural Language Processing Tasks},\n  author = {Xiao, Yijun and Wang, William Yang},\n  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year = {2019},\n  doi = {10.1609/aaai.v33i01.33017322},\n  url = {http://dx.doi.org/10.1609/aaai.v33i01.33017322}\n}\n\n@inproceedings{xiong2024verbalized,\n  title = {Can {LLMs} Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in {LLMs}},\n  author = {Xiong, Miao and Hu, Zhiyuan and Lu, Xinyang and Li, Yifei and Fu, Jie and He, Junxian and Hooi, Bryan},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2306.13063}\n}\n\n@inproceedings{zhang2023ener,\n  title = {E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition},\n  author = {Zhang, Zhen and Hu, Mengting and Zhao, Shiwan and Huang, Minlie and Wang, Haotian and Liu, Lemao and Zhang, Zhirui and Liu, Zhe and Wu, Bingzhe},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2023},\n  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 456,
        "oldLines": 3,
        "newStart": 456,
        "newLines": 11,
        "lines": [
          "   doi = {10.18653/v1/2023.findings-acl.103},",
          "   url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}",
          " }",
          "+",
          "+@inproceedings{zhou2024uniner,",
          "+  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},",
          "+  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},",
          "+  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},",
          "+  year = {2024},",
          "+  url = {https://arxiv.org/abs/2308.03279}",
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

_source line 41_

Now let me update the literature_map.yaml — change zhou2024uniner's verified to true and add the 3 new papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "1a1c1e1f-36cc-4c17-aef4-2bc97c3d98dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6xu8JgeMdpWQFRoqsQYd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 59968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01LdHJNe25EA9XuB5PMWfoZW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: false\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'",
  "new_string": "  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'\n  josifoski2022genie:\n    title: 'GenIE: Generative Information Extraction'\n    authors:\n    - Martin Josifoski\n    - Nicola De Cao\n    - Maxime Peyrard\n    - Fabio Petroni\n    - Robert West\n    year: 2022\n    venue: NAACL 2022\n    url: https://arxiv.org/abs/2112.08340\n    doi: 10.18653/v1/2022.naacl-main.342\n    bibtex_key: josifoski2022genie\n    category: generative_ie\n    role: foundation\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  li2023codeie:\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\n    authors:\n    - Peng Li\n    - Tianxiang Sun\n    - Qiong Tang\n    - Hang Yan\n    - Yuanbin Wu\n    - Xuanjing Huang\n    - Xipeng Qiu\n    year: 2023\n    venue: ACL 2023\n    url: https://arxiv.org/abs/2305.05711\n    doi: 10.18653/v1/2023.acl-long.855\n    bibtex_key: li2023codeie\n    category: generative_ie\n    role: background\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\n      alternative structured generation approach complementary to constrained decoding.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  wang2023instructuie:\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\n    authors:\n    - Xiao Wang\n    - Weikang Zhou\n    - Can Zu\n    - Han Xia\n    - Tianze Chen\n    - Yuansen Zhang\n    - Rui Zheng\n    - Junjie Ye\n    - Qi Zhang\n    - Tao Gui\n    - Jihua Kang\n    - Jingsheng Yang\n    - Siyuan Li\n    - Chunsai Du\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2304.08085\n    doi: ''\n    bibtex_key: wang2023instructuie\n    category: generative_ie\n    role: foundation\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "208f3237-b06c-48c7-883f-30c66d7f0356",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U6xu8JgeMdpWQFRoqsQYd9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 59968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
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

_source line 43 · 2026-05-14T19:51:17.205Z_

<details><summary>↩ Tool result · `toolu_01LdHJNe25EA9XuB5PMWfoZW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "8955b1e6-b8a8-4763-adc8-4f5b458c8ff6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "oldString": "  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: false\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'",
    "newString": "  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'\n  josifoski2022genie:\n    title: 'GenIE: Generative Information Extraction'\n    authors:\n    - Martin Josifoski\n    - Nicola De Cao\n    - Maxime Peyrard\n    - Fabio Petroni\n    - Robert West\n    year: 2022\n    venue: NAACL 2022\n    url: https://arxiv.org/abs/2112.08340\n    doi: 10.18653/v1/2022.naacl-main.342\n    bibtex_key: josifoski2022genie\n    category: generative_ie\n    role: foundation\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  li2023codeie:\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\n    authors:\n    - Peng Li\n    - Tianxiang Sun\n    - Qiong Tang\n    - Hang Yan\n    - Yuanbin Wu\n    - Xuanjing Huang\n    - Xipeng Qiu\n    year: 2023\n    venue: ACL 2023\n    url: https://arxiv.org/abs/2305.05711\n    doi: 10.18653/v1/2023.acl-long.855\n    bibtex_key: li2023codeie\n    category: generative_ie\n    role: background\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\n      alternative structured generation approach complementary to constrained decoding.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  wang2023instructuie:\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\n    authors:\n    - Xiao Wang\n    - Weikang Zhou\n    - Can Zu\n    - Han Xia\n    - Tianze Chen\n    - Yuansen Zhang\n    - Rui Zheng\n    - Junjie Ye\n    - Qi Zhang\n    - Tao Gui\n    - Jihua Kang\n    - Jingsheng Yang\n    - Siyuan Li\n    - Chunsai Du\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2304.08085\n    doi: ''\n    bibtex_key: wang2023instructuie\n    category: generative_ie\n    role: foundation\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'",
    "originalFile": "meta:\n  last_updated: '2026-05-14T21:00:00.000Z'\n  total_papers: 52\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\n      for our structured consistency metric that operates at the semantic level of IE triples.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  fisch2021conformal:\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\n    authors:\n    - Adam Fisch\n    - Tal Schuster\n    - Tommi Jaakkola\n    - Regina Barzilay\n    year: 2021\n    venue: ICML 2021\n    url: https://arxiv.org/abs/2102.08898\n    doi: 10.5555/3524938.3525234\n    bibtex_key: fisch2021conformal\n    category: conformal_prediction\n    role: supplementary\n    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\n      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  angelopoulos2021conformal:\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\n    authors:\n    - Anastasios N. Angelopoulos\n    - Stephen Bates\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.14193\n    doi: ''\n    bibtex_key: angelopoulos2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\n      conformal prediction methodology we adapt to structured IE output sets.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  bates2021rcps:\n    title: Distribution-Free, Risk-Controlling Prediction Sets\n    authors:\n    - Stephen Bates\n    - Anastasios Angelopoulos\n    - Lihua Lei\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: Journal of the ACM 2021\n    url: https://arxiv.org/abs/2101.02703\n    doi: 10.1145/3478535\n    bibtex_key: bates2021rcps\n    category: conformal_prediction\n    role: supplementary\n    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\n      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  xiao2019uncertainty:\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\n    authors:\n    - Yijun Xiao\n    - William Yang Wang\n    year: 2019\n    venue: AAAI 2019\n    url: https://arxiv.org/abs/1811.07253\n    doi: 10.1609/aaai.v33i01.33017322\n    bibtex_key: xiao2019uncertainty\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\n      uncertainty improves both performance and reliability for token-level predictions.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  shelmanov2021active:\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\n    authors:\n    - Artem Shelmanov\n    - Dmitri Puzyrev\n    - Lyubov Kupriyanova\n    - Denis Belyakov\n    - Daniil Larionov\n    - Nikita Khromov\n    - Olga Kozlova\n    - Ekaterina Artemova\n    - Dmitry V. Dylov\n    - Alexander Panchenko\n    year: 2021\n    venue: EACL 2021\n    url: https://arxiv.org/abs/2101.08133\n    doi: 10.18653/v1/2021.eacl-main.145\n    bibtex_key: shelmanov2021active\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  zhang2023ener:\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\n    authors:\n    - Zhen Zhang\n    - Mengting Hu\n    - Shiwan Zhao\n    - Minlie Huang\n    - Haotian Wang\n    - Lemao Liu\n    - Zhirui Zhang\n    - Zhe Liu\n    - Bingzhe Wu\n    year: 2023\n    venue: ACL Findings 2023\n    url: https://arxiv.org/abs/2305.17854\n    doi: 10.18653/v1/2023.findings-acl.103\n    bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  lakshminarayanan2017ensembles:\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\n    authors:\n    - Balaji Lakshminarayanan\n    - Alexander Pritzel\n    - Charles Blundell\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1612.01474\n    doi: ''\n    bibtex_key: lakshminarayanan2017ensembles\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  gal2016dropout:\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\n    authors:\n    - Yarin Gal\n    - Zoubin Ghahramani\n    year: 2016\n    venue: ICML 2016\n    url: https://arxiv.org/abs/1506.02142\n    doi: ''\n    bibtex_key: gal2016dropout\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  fomicheva2020unsupervised:\n    title: Unsupervised Quality Estimation for Neural Machine Translation\n    authors:\n    - Marina Fomicheva\n    - Shuo Sun\n    - Lisa Yankovskaya\n    - Frédéric Blain\n    - Francisco Guzmán\n    - Mark Fishel\n    - Nikolaos Aletras\n    - Vishrav Chaudhary\n    - Lucia Specia\n    year: 2020\n    venue: TACL 2020\n    url: https://arxiv.org/abs/2005.10608\n    doi: 10.1162/tacl_a_00330\n    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wadhwa2023revisiting:\n    title: Revisiting Relation Extraction in the era of Large Language Models\n    authors:\n    - Somin Wadhwa\n    - Silvio Amir\n    - Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    doi: 10.18653/v1/2023.acl-long.868\n    bibtex_key: wadhwa2023revisiting\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  sainz2024gollie:\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\n    authors:\n    - Oscar Sainz\n    - Iker García-Ferrero\n    - Rodrigo Agerri\n    - Oier Lopez de Lacalle\n    - German Rigau\n    - Eneko Agirre\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2310.03668\n    doi: ''\n    bibtex_key: sainz2024gollie\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  luan2018scierc:\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\n    authors:\n    - Yi Luan\n    - Luheng He\n    - Mari Ostendorf\n    - Hannaneh Hajishirzi\n    year: 2018\n    venue: EMNLP 2018\n    url: https://aclanthology.org/D18-1360/\n    doi: 10.18653/v1/D18-1360\n    bibtex_key: luan2018scierc\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\n      benchmark for our structured IE experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  tjongkimsang2003conll:\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\n    authors:\n    - Erik F. Tjong Kim Sang\n    - Fien De Meulder\n    year: 2003\n    venue: CoNLL 2003\n    url: https://aclanthology.org/W03-0419/\n    doi: ''\n    bibtex_key: tjongkimsang2003conll\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\n      for our NER consistency experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  derczynski2017wnut:\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\n    authors:\n    - Leon Derczynski\n    - Eric Nichols\n    - Marieke van Erp\n    - Nut Limsopatham\n    year: 2017\n    venue: W-NUT Workshop at EMNLP 2017\n    url: https://aclanthology.org/W17-4418/\n    doi: ''\n    bibtex_key: derczynski2017wnut\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\n      on harder, low-resource NER scenarios.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  willard2023guided:\n    title: Efficient Guided Generation for Large Language Models\n    authors:\n    - Brandon T. Willard\n    - Rémi Louf\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2307.09702\n    doi: ''\n    bibtex_key: willard2023guided\n    category: generative_ie\n    role: background\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  fleiss1971agreement:\n    title: Measuring Nominal Scale Agreement Among Many Raters\n    authors:\n    - Joseph L. Fleiss\n    year: 1971\n    venue: Psychological Bulletin\n    url: https://psycnet.apa.org/record/1972-05083-001\n    doi: 10.1037/h0031619\n    bibtex_key: fleiss1971agreement\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  jaccard1901distribution:\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\n    authors:\n    - Paul Jaccard\n    year: 1901\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\n    url: https://www.researchgate.net/publication/225035806\n    doi: ''\n    bibtex_key: jaccard1901distribution\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\n      between extracted entity/relation sets across multiple LLM samples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  wang2025rankedvoting:\n    title: Ranked Voting based Self-Consistency of Large Language Models\n    authors:\n    - Weiqin Wang\n    - Yile Wang\n    - Hui Huang\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2505.10772\n    doi: ''\n    bibtex_key: wang2025rankedvoting\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  oh2025latentsc:\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\n    authors:\n    - Jungsuk Oh\n    - Jay-Yoon Lee\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2508.18395\n    doi: ''\n    bibtex_key: oh2025latentsc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: false\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'\n",
    "structuredPatch": [
      {
        "oldStart": 1165,
        "oldLines": 6,
        "newStart": 1165,
        "newLines": 83,
        "lines": [
          "       Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'",
          "     abstract: ''",
          "     semantic_scholar_id: ''",
          "-    verified: false",
          "+    verified: true",
          "     added_by: paper-agent:manual",
          "     added_at: '2026-05-14T21:05:00.000Z'",
          "+  josifoski2022genie:",
          "+    title: 'GenIE: Generative Information Extraction'",
          "+    authors:",
          "+    - Martin Josifoski",
          "+    - Nicola De Cao",
          "+    - Maxime Peyrard",
          "+    - Fabio Petroni",
          "+    - Robert West",
          "+    year: 2022",
          "+    venue: NAACL 2022",
          "+    url: https://arxiv.org/abs/2112.08340",
          "+    doi: 10.18653/v1/2022.naacl-main.342",
          "+    bibtex_key: josifoski2022genie",
          "+    category: generative_ie",
          "+    role: foundation",
          "+    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet",
          "+      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-agent:manual",
          "+    added_at: '2026-05-14T22:00:00.000Z'",
          "+  li2023codeie:",
          "+    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'",
          "+    authors:",
          "+    - Peng Li",
          "+    - Tianxiang Sun",
          "+    - Qiong Tang",
          "+    - Hang Yan",
          "+    - Yuanbin Wu",
          "+    - Xuanjing Huang",
          "+    - Xipeng Qiu",
          "+    year: 2023",
          "+    venue: ACL 2023",
          "+    url: https://arxiv.org/abs/2305.05711",
          "+    doi: 10.18653/v1/2023.acl-long.855",
          "+    bibtex_key: li2023codeie",
          "+    category: generative_ie",
          "+    role: background",
          "+    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates",
          "+      alternative structured generation approach complementary to constrained decoding.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-agent:manual",
          "+    added_at: '2026-05-14T22:00:00.000Z'",
          "+  wang2023instructuie:",
          "+    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'",
          "+    authors:",
          "+    - Xiao Wang",
          "+    - Weikang Zhou",
          "+    - Can Zu",
          "+    - Han Xia",
          "+    - Tianze Chen",
          "+    - Yuansen Zhang",
          "+    - Rui Zheng",
          "+    - Junjie Ye",
          "+    - Qi Zhang",
          "+    - Tao Gui",
          "+    - Jihua Kang",
          "+    - Jingsheng Yang",
          "+    - Siyuan Li",
          "+    - Chunsai Du",
          "+    year: 2023",
          "+    venue: arXiv preprint",
          "+    url: https://arxiv.org/abs/2304.08085",
          "+    doi: ''",
          "+    bibtex_key: wang2023instructuie",
          "+    category: generative_ie",
          "+    role: foundation",
          "+    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative",
          "+      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-agent:manual",
          "+    added_at: '2026-05-14T22:00:00.000Z'"
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

_source line 44_

Now let me update the `total_papers` count in literature_map.yaml metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "3f0a7429-b5d0-4068-8ee6-1e362a446993",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAJoqycdU6c56w97SyJTaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 60680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1728
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

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01CJD63cR2qdx8YGV2dz8T3K`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "  total_papers: 52",
  "new_string": "  total_papers: 55"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "3dc92da5-4b09-463e-b817-25e4f8793f15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAJoqycdU6c56w97SyJTaV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1728,
      "cache_read_input_tokens": 60680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1728
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

_source line 46 · 2026-05-14T19:51:23.463Z_

<details><summary>↩ Tool result · `toolu_01CJD63cR2qdx8YGV2dz8T3K`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "8035af3f-e446-4a29-aa69-588f320f4176",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "oldString": "  total_papers: 52",
    "newString": "  total_papers: 55",
    "originalFile": "meta:\n  last_updated: '2026-05-14T21:00:00.000Z'\n  total_papers: 52\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\n      for our structured consistency metric that operates at the semantic level of IE triples.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  fisch2021conformal:\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\n    authors:\n    - Adam Fisch\n    - Tal Schuster\n    - Tommi Jaakkola\n    - Regina Barzilay\n    year: 2021\n    venue: ICML 2021\n    url: https://arxiv.org/abs/2102.08898\n    doi: 10.5555/3524938.3525234\n    bibtex_key: fisch2021conformal\n    category: conformal_prediction\n    role: supplementary\n    relevance: 'Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\n      prediction sets with formal coverage guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  angelopoulos2021conformal:\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\n    authors:\n    - Anastasios N. Angelopoulos\n    - Stephen Bates\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.14193\n    doi: ''\n    bibtex_key: angelopoulos2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\n      conformal prediction methodology we adapt to structured IE output sets.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  bates2021rcps:\n    title: Distribution-Free, Risk-Controlling Prediction Sets\n    authors:\n    - Stephen Bates\n    - Anastasios Angelopoulos\n    - Lihua Lei\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: Journal of the ACM 2021\n    url: https://arxiv.org/abs/2101.02703\n    doi: 10.1145/3478535\n    bibtex_key: bates2021rcps\n    category: conformal_prediction\n    role: supplementary\n    relevance: 'Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\n      guarantees. SUPPLEMENTARY - CP not a method component, angelopoulos2021 retained as main CP reference.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  xiao2019uncertainty:\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\n    authors:\n    - Yijun Xiao\n    - William Yang Wang\n    year: 2019\n    venue: AAAI 2019\n    url: https://arxiv.org/abs/1811.07253\n    doi: 10.1609/aaai.v33i01.33017322\n    bibtex_key: xiao2019uncertainty\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\n      uncertainty improves both performance and reliability for token-level predictions.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  shelmanov2021active:\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\n    authors:\n    - Artem Shelmanov\n    - Dmitri Puzyrev\n    - Lyubov Kupriyanova\n    - Denis Belyakov\n    - Daniil Larionov\n    - Nikita Khromov\n    - Olga Kozlova\n    - Ekaterina Artemova\n    - Dmitry V. Dylov\n    - Alexander Panchenko\n    year: 2021\n    venue: EACL 2021\n    url: https://arxiv.org/abs/2101.08133\n    doi: 10.18653/v1/2021.eacl-main.145\n    bibtex_key: shelmanov2021active\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  zhang2023ener:\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\n    authors:\n    - Zhen Zhang\n    - Mengting Hu\n    - Shiwan Zhao\n    - Minlie Huang\n    - Haotian Wang\n    - Lemao Liu\n    - Zhirui Zhang\n    - Zhe Liu\n    - Bingzhe Wu\n    year: 2023\n    venue: ACL Findings 2023\n    url: https://arxiv.org/abs/2305.17854\n    doi: 10.18653/v1/2023.findings-acl.103\n    bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  lakshminarayanan2017ensembles:\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\n    authors:\n    - Balaji Lakshminarayanan\n    - Alexander Pritzel\n    - Charles Blundell\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1612.01474\n    doi: ''\n    bibtex_key: lakshminarayanan2017ensembles\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  gal2016dropout:\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\n    authors:\n    - Yarin Gal\n    - Zoubin Ghahramani\n    year: 2016\n    venue: ICML 2016\n    url: https://arxiv.org/abs/1506.02142\n    doi: ''\n    bibtex_key: gal2016dropout\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  fomicheva2020unsupervised:\n    title: Unsupervised Quality Estimation for Neural Machine Translation\n    authors:\n    - Marina Fomicheva\n    - Shuo Sun\n    - Lisa Yankovskaya\n    - Frédéric Blain\n    - Francisco Guzmán\n    - Mark Fishel\n    - Nikolaos Aletras\n    - Vishrav Chaudhary\n    - Lucia Specia\n    year: 2020\n    venue: TACL 2020\n    url: https://arxiv.org/abs/2005.10608\n    doi: 10.1162/tacl_a_00330\n    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wadhwa2023revisiting:\n    title: Revisiting Relation Extraction in the era of Large Language Models\n    authors:\n    - Somin Wadhwa\n    - Silvio Amir\n    - Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    doi: 10.18653/v1/2023.acl-long.868\n    bibtex_key: wadhwa2023revisiting\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  sainz2024gollie:\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\n    authors:\n    - Oscar Sainz\n    - Iker García-Ferrero\n    - Rodrigo Agerri\n    - Oier Lopez de Lacalle\n    - German Rigau\n    - Eneko Agirre\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2310.03668\n    doi: ''\n    bibtex_key: sainz2024gollie\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  luan2018scierc:\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\n    authors:\n    - Yi Luan\n    - Luheng He\n    - Mari Ostendorf\n    - Hannaneh Hajishirzi\n    year: 2018\n    venue: EMNLP 2018\n    url: https://aclanthology.org/D18-1360/\n    doi: 10.18653/v1/D18-1360\n    bibtex_key: luan2018scierc\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\n      benchmark for our structured IE experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  tjongkimsang2003conll:\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\n    authors:\n    - Erik F. Tjong Kim Sang\n    - Fien De Meulder\n    year: 2003\n    venue: CoNLL 2003\n    url: https://aclanthology.org/W03-0419/\n    doi: ''\n    bibtex_key: tjongkimsang2003conll\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\n      for our NER consistency experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  derczynski2017wnut:\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\n    authors:\n    - Leon Derczynski\n    - Eric Nichols\n    - Marieke van Erp\n    - Nut Limsopatham\n    year: 2017\n    venue: W-NUT Workshop at EMNLP 2017\n    url: https://aclanthology.org/W17-4418/\n    doi: ''\n    bibtex_key: derczynski2017wnut\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\n      on harder, low-resource NER scenarios.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  willard2023guided:\n    title: Efficient Guided Generation for Large Language Models\n    authors:\n    - Brandon T. Willard\n    - Rémi Louf\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2307.09702\n    doi: ''\n    bibtex_key: willard2023guided\n    category: generative_ie\n    role: background\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  fleiss1971agreement:\n    title: Measuring Nominal Scale Agreement Among Many Raters\n    authors:\n    - Joseph L. Fleiss\n    year: 1971\n    venue: Psychological Bulletin\n    url: https://psycnet.apa.org/record/1972-05083-001\n    doi: 10.1037/h0031619\n    bibtex_key: fleiss1971agreement\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  jaccard1901distribution:\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\n    authors:\n    - Paul Jaccard\n    year: 1901\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\n    url: https://www.researchgate.net/publication/225035806\n    doi: ''\n    bibtex_key: jaccard1901distribution\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\n      between extracted entity/relation sets across multiple LLM samples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  wang2025rankedvoting:\n    title: Ranked Voting based Self-Consistency of Large Language Models\n    authors:\n    - Weiqin Wang\n    - Yile Wang\n    - Hui Huang\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2505.10772\n    doi: ''\n    bibtex_key: wang2025rankedvoting\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  oh2025latentsc:\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\n    authors:\n    - Jungsuk Oh\n    - Jay-Yoon Lee\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2508.18395\n    doi: ''\n    bibtex_key: oh2025latentsc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  zhou2024uniner:\n    title: 'UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition'\n    authors:\n    - Wenxuan Zhou\n    - Sheng Zhang\n    - Yu Gu\n    - Muhao Chen\n    - Hoifung Poon\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2308.03279\n    doi: ''\n    bibtex_key: zhou2024uniner\n    category: generative_ie\n    role: foundation\n    relevance: 'UniNER: distills ChatGPT NER capabilities into smaller models via targeted distillation on diverse entity types.\n      Demonstrates LLM-based generative NER at scale. Directly relevant as representative LLM-based NER baseline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T21:05:00.000Z'\n  josifoski2022genie:\n    title: 'GenIE: Generative Information Extraction'\n    authors:\n    - Martin Josifoski\n    - Nicola De Cao\n    - Maxime Peyrard\n    - Fabio Petroni\n    - Robert West\n    year: 2022\n    venue: NAACL 2022\n    url: https://arxiv.org/abs/2112.08340\n    doi: 10.18653/v1/2022.naacl-main.342\n    bibtex_key: josifoski2022genie\n    category: generative_ie\n    role: foundation\n    relevance: 'First end-to-end autoregressive formulation of closed IE with bi-level constrained decoding (high-level triplet\n      structure + prefix-trie entity/relation constraints). Directly relevant as the foundational constrained decoding approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  li2023codeie:\n    title: 'CodeIE: Large Code Generation Models are Better Few-Shot Information Extractors'\n    authors:\n    - Peng Li\n    - Tianxiang Sun\n    - Qiong Tang\n    - Hang Yan\n    - Yuanbin Wu\n    - Xuanjing Huang\n    - Xipeng Qiu\n    year: 2023\n    venue: ACL 2023\n    url: https://arxiv.org/abs/2305.05711\n    doi: 10.18653/v1/2023.acl-long.855\n    bibtex_key: li2023codeie\n    category: generative_ie\n    role: background\n    relevance: 'Recasts IE as code generation, leveraging Code-LLMs structural output capabilities for NER and RE. Demonstrates\n      alternative structured generation approach complementary to constrained decoding.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n  wang2023instructuie:\n    title: 'InstructUIE: Multi-task Instruction Tuning for Unified Information Extraction'\n    authors:\n    - Xiao Wang\n    - Weikang Zhou\n    - Can Zu\n    - Han Xia\n    - Tianze Chen\n    - Yuansen Zhang\n    - Rui Zheng\n    - Junjie Ye\n    - Qi Zhang\n    - Tao Gui\n    - Jihua Kang\n    - Jingsheng Yang\n    - Siyuan Li\n    - Chunsai Du\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2304.08085\n    doi: ''\n    bibtex_key: wang2023instructuie\n    category: generative_ie\n    role: foundation\n    relevance: 'Unified instruction-tuned IE framework covering NER, RE, EE across 32 datasets. Demonstrates multi-task generative\n      IE with instruction tuning, directly relevant as representative LLM-based unified IE system.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-agent:manual\n    added_at: '2026-05-14T22:00:00.000Z'\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " meta:",
          "   last_updated: '2026-05-14T21:00:00.000Z'",
          "-  total_papers: 52",
          "+  total_papers: 55",
          " categories: []",
          " papers:",
          "   wang2023selfconsistency:"
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

_source line 47_

Let me verify the final state of references.bib around the new entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "2bbf3ef8-32b5-4869-8171-89b0fcccb971",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uiHSdXY1fNBoLaF6dXt8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 62408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_01SXCe1FUwVbDBECZJkAhnsR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 148,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "8d10b17e-50c4-4553-95a1-60ff5b2ffcef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uiHSdXY1fNBoLaF6dXt8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 62408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 49 · 2026-05-14T19:51:27.592Z_

<details><summary>↩ Tool result · `toolu_01SXCe1FUwVbDBECZJkAhnsR`</summary>

```text
148	  title = {Calibrating Structured Output Predictors for Natural Language Processing},
149	  author = {Jagannatha, Abhyuday and Yu, Hong},
150	  booktitle = {ACL 2020},
151	  year = {2020},
152	  url = {https://aclanthology.org/2020.acl-main.188/}
153	}
154	
155	@inproceedings{josifoski2022genie,
156	  title = {{GenIE}: Generative Information Extraction},
157	  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
158	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
159	  year = {2022},
160	  doi = {10.18653/v1/2022.naacl-main.342},
161	  url = {https://arxiv.org/abs/2112.08340}
162	}
163	
164	@article{kadavath2022language,
165	  title = {Language Models (Mostly) Know What They Know},
166	  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},
167	  journal = {arXiv preprint arXiv:2207.05221},
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "d48db661-86dc-4b40-8063-5db5a83f6ee3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "  title = {Calibrating Structured Output Predictors for Natural Language Processing},\n  author = {Jagannatha, Abhyuday and Yu, Hong},\n  booktitle = {ACL 2020},\n  year = {2020},\n  url = {https://aclanthology.org/2020.acl-main.188/}\n}\n\n@inproceedings{josifoski2022genie,\n  title = {{GenIE}: Generative Information Extraction},\n  author = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  year = {2022},\n  doi = {10.18653/v1/2022.naacl-main.342},\n  url = {https://arxiv.org/abs/2112.08340}\n}\n\n@article{kadavath2022language,\n  title = {Language Models (Mostly) Know What They Know},\n  author = {Kadavath, Saurav and Conerly, Tom and Askell, Amanda and Henighan, Tom and Drain, Dawn and Perez, Ethan and Schiefer, Nicholas and Hatfield-Dodds, Zac and DasSarma, Nova and Tran-Johnson, Eli and Johnston, Scott and El-Showk, Sheer and Jones, Andy and Elhage, Nelson and Hume, Tristan and Chen, Anna and Bai, Yuntao and Bowman, Sam and Fort, Stanislav and Ganguli, Deep and Hernandez, Danny and Jacobson, Josh and Kernion, Jackson and Kravec, Shauna and Lovitt, Liane and Ndousse, Kamal and Olsson, Catherine and Ringer, Sam and Amodei, Dario and Brown, Tom and Clark, Jack and Joseph, Nicholas and Mann, Ben and McCandlish, Sam and Olah, Chris and Kaplan, Jared},\n  journal = {arXiv preprint arXiv:2207.05221},",
      "numLines": 20,
      "startLine": 148,
      "totalLines": 467
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01C2FXgDZ4CEgTZEPxaEbMu6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 215,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "09f2ff9a-5ecc-4e68-8f68-ff129c611023",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uiHSdXY1fNBoLaF6dXt8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 62408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 51 · 2026-05-14T19:51:28.526Z_

<details><summary>↩ Tool result · `toolu_01C2FXgDZ4CEgTZEPxaEbMu6`</summary>

```text
215	  booktitle = {NeurIPS 2017},
216	  year = {2017},
217	  url = {https://arxiv.org/abs/1612.01474}
218	}
219	
220	@inproceedings{li2023codeie,
221	  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
222	  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
223	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
224	  year = {2023},
225	  doi = {10.18653/v1/2023.acl-long.855},
226	  url = {https://arxiv.org/abs/2305.05711}
227	}
228	
229	@inproceedings{lightman2024verify,
230	  title = {Let's Verify Step by Step},
231	  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},
232	  booktitle = {ICLR 2024},
233	  year = {2024},
234	  url = {https://arxiv.org/abs/2305.20050}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "318e9230-9306-44a2-9eb8-408e07c72cfd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "  booktitle = {NeurIPS 2017},\n  year = {2017},\n  url = {https://arxiv.org/abs/1612.01474}\n}\n\n@inproceedings{li2023codeie,\n  title = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n  author = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year = {2023},\n  doi = {10.18653/v1/2023.acl-long.855},\n  url = {https://arxiv.org/abs/2305.05711}\n}\n\n@inproceedings{lightman2024verify,\n  title = {Let's Verify Step by Step},\n  author = {Lightman, Hunter and Kosaraju, Vineet and Burda, Yura and Edwards, Harri and Baker, Bowen and Lee, Teddy and Leike, Jan and Schulman, John and Sutskever, Ilya and Cobbe, Karl},\n  booktitle = {ICLR 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2305.20050}",
      "numLines": 20,
      "startLine": 215,
      "totalLines": 467
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01GUgueYw3UgmdLpbvvN9XGi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 370,
  "limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "8aabea3a-f7a4-4243-8b77-65c481ec24c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uiHSdXY1fNBoLaF6dXt8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 62408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 53 · 2026-05-14T19:51:29.463Z_

<details><summary>↩ Tool result · `toolu_01GUgueYw3UgmdLpbvvN9XGi`</summary>

```text
370	  journal = {arXiv preprint arXiv:2304.08085},
371	  year = {2023},
372	  url = {https://arxiv.org/abs/2304.08085}
373	}
374	
375	@inproceedings{wang2023selfconsistency,
376	  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},
377	  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},
378	  booktitle = {ICLR 2023},
379	  year = {2023},
380	  url = {https://arxiv.org/abs/2203.11171}
381	}
382	
383	@inproceedings{wang2024mathshepherd,
384	  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},
385	  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},
386	  booktitle = {ACL 2024},
387	  year = {2024},
388	  url = {https://arxiv.org/abs/2312.08935}
389	}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "02171587-b575-4b49-abb2-ab5d49876016",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "  journal = {arXiv preprint arXiv:2304.08085},\n  year = {2023},\n  url = {https://arxiv.org/abs/2304.08085}\n}\n\n@inproceedings{wang2023selfconsistency,\n  title = {Self-Consistency Improves Chain of Thought Reasoning in Language Models},\n  author = {Wang, Xuezhi and Wei, Jason and Schuurmans, Dale and Le, Quoc and Chi, Ed and Narang, Sharan and Chowdhery, Aakanksha and Zhou, Denny},\n  booktitle = {ICLR 2023},\n  year = {2023},\n  url = {https://arxiv.org/abs/2203.11171}\n}\n\n@inproceedings{wang2024mathshepherd,\n  title = {Math-Shepherd: Verify and Reinforce {LLMs} Step-by-step without Human Annotations},\n  author = {Wang, Peiyi and Li, Lei and Shao, Zhihong and Xu, Runxin and Dai, Damai and Li, Yifei and Chen, Deli and Wu, Yu and Sui, Zhifang},\n  booktitle = {ACL 2024},\n  year = {2024},\n  url = {https://arxiv.org/abs/2312.08935}\n}",
      "numLines": 20,
      "startLine": 370,
      "totalLines": 467
    }
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_01Btt6DkbR5QpYD4q94vPGE1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 470,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "0733df0b-32f2-46a4-9db5-48ae7bff05e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uiHSdXY1fNBoLaF6dXt8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 62408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 55 · 2026-05-14T19:51:30.046Z_

<details><summary>↩ Tool result · `toolu_01Btt6DkbR5QpYD4q94vPGE1`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (470). The file has 467 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "e5e2d013-d1d0-4167-bc9b-e60493b6ae0a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "",
      "numLines": 0,
      "startLine": 470,
      "totalLines": 467
    }
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Read · `toolu_01GTZisTFA5cdvn4HUVP9gad`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "offset": 455,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "71245b0b-b0bf-49ef-bd67-a7dff39f802c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q94TE9rSQB3eqnBwj5X2MP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1975,
      "cache_read_input_tokens": 62637,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1975
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

_source line 57 · 2026-05-14T19:51:34.025Z_

<details><summary>↩ Tool result · `toolu_01GTZisTFA5cdvn4HUVP9gad`</summary>

```text
455	  year = {2023},
456	  doi = {10.18653/v1/2023.findings-acl.103},
457	  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}
458	}
459	
460	@inproceedings{zhou2024uniner,
461	  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
462	  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
463	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
464	  year = {2024},
465	  url = {https://arxiv.org/abs/2308.03279}
466	}
467	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "3a45e06a-b3d7-4c23-a6d5-7ca0975a2f4e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
      "content": "  year = {2023},\n  doi = {10.18653/v1/2023.findings-acl.103},\n  url = {http://dx.doi.org/10.18653/v1/2023.findings-acl.103}\n}\n\n@inproceedings{zhou2024uniner,\n  title = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n  author = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year = {2024},\n  url = {https://arxiv.org/abs/2308.03279}\n}\n",
      "numLines": 13,
      "startLine": 455,
      "totalLines": 467
    }
  }
}
```

</details>

---

### Assistant

_source line 58_

All entries are correctly placed in alphabetical order. Summary of changes:

**references.bib** — 4 new BibTeX entries added:
- `josifoski2022genie` — GenIE: constrained decoding for IE (NAACL 2022)
- `li2023codeie` — CodeIE: code generation for IE (ACL 2023)
- `wang2023instructuie` — InstructUIE: unified instruction-tuned IE (arXiv 2023)
- `zhou2024uniner` — UniversalNER: distilled open NER (ICLR 2024)

**literature_map.yaml** — 3 new entries added (`josifoski2022genie`, `li2023codeie`, `wang2023instructuie`), `zhou2024uniner` verified changed from `false` to `true`, `total_papers` updated to 55.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "uuid": "ae89f137-0766-438e-b919-d22bcf34d8ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017S16QteJG3t79eCkdgKLFE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 64612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 360
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

_source line 59_

All entries are correctly placed in alphabetical order. Summary of changes:

**references.bib** — 4 new BibTeX entries added:
- `josifoski2022genie` — GenIE: constrained decoding for IE (NAACL 2022)
- `li2023codeie` — CodeIE: code generation for IE (ACL 2023)
- `wang2023instructuie` — InstructUIE: unified instruction-tuned IE (arXiv 2023)
- `zhou2024uniner` — UniversalNER: distilled open NER (ICLR 2024)

**literature_map.yaml** — 3 new entries added (`josifoski2022genie`, `li2023codeie`, `wang2023instructuie`), `zhou2024uniner` verified changed from `false` to `true`, `total_papers` updated to 55.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 167572,
  "duration_api_ms": 184862,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "feeed4ce-16ae-46a9-8cad-d8d2d10704c9",
  "total_cost_usd": 0.9868022499999999,
  "usage": {
    "input_tokens": 873,
    "cache_creation_input_tokens": 53131,
    "cache_read_input_tokens": 560787,
    "output_tokens": 8655,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 53131,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 220,
        "cache_read_input_tokens": 64612,
        "cache_creation_input_tokens": 360,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 360
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 92610,
      "outputTokens": 2198,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.15360000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 873,
      "outputTokens": 8655,
      "cacheReadInputTokens": 560787,
      "cacheCreationInputTokens": 53131,
      "webSearchRequests": 0,
      "costUSD": 0.8332022499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a90a33f9-ae7c-4f73-97c0-655bc4743503"
}
```

</details>

---
