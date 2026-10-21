# paper ref pages batch — Part 1 of 2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

[Transcript overview](../paper-ref-pages-batch.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/43/439d470e18ee90573f0b.json)

## Before a recorded user message

## Before a recorded user message

21 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
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
  "uuid": "8537e6ba-27f6-4674-8678-e519cec93852",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1779450600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "89e802cc-cf3b-4f79-b200-6a051db251a7",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the references.bib file to understand the entries and classify them by venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "7656e873-e541-46c9-81a0-000906a8b2e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cr6mvwhQy7ppRB2bJfZ2JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12266,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12266
      },
      "output_tokens": 29,
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

先读 bib 文件，按 venue 分类条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "7e243a56-7b2a-444b-9c04-6d9981b66426",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cr6mvwhQy7ppRB2bJfZ2JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12266,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12266
      },
      "output_tokens": 29,
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

<details open><summary>🔧 Tool call — Read · `toolu_01TXT2rp45Dy5ZzmkNYyTaFw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "2df13b38-5111-4f09-8384-dd6c2c294c2d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cr6mvwhQy7ppRB2bJfZ2JE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12266,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12266
      },
      "output_tokens": 29,
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

_source line 7 · 2026-05-22T07:30:35.710Z_

<details><summary>↩ Tool result · reported error · `toolu_01TXT2rp45Dy5ZzmkNYyTaFw`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "1aa7859b-33ef-42e7-b769-8e436c58f924",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---


### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_018HANcP39FB3wrSsjieht7Z`</summary>

```json
{
  "pattern": "paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e4f9c65e-d391-495f-8bcf-e138ba5c8054",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBtwYrdCn3jonLoiYchrKq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 24107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
      },
      "output_tokens": 47,
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

_source line 9 · 2026-05-22T07:30:38.453Z_

<details><summary>↩ Tool result · `toolu_018HANcP39FB3wrSsjieht7Z`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "9627c325-5ad6-46c2-8bf0-4af4b0985c2a",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 71,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_01Co8b95wgFvo9Nui4R1gPZ6`</summary>

```json
{
  "pattern": "**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "346e0197-1e7f-4002-b9c2-7eb27165bcfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzEAwkf4qizxzXSyfiBz6P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 71,
      "cache_read_input_tokens": 24308,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 71
      },
      "output_tokens": 55,
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

_source line 11 · 2026-05-22T07:30:41.088Z_

<details><summary>↩ Tool result · `toolu_01Co8b95wgFvo9Nui4R1gPZ6`</summary>

```text
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "f81040e1-431a-493b-8655-f0ea53228766",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 69,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01W3EDLtJ5MDTcYaYcCuFVSp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "bd3211e4-da98-4751-9557-92aec80819b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AaG8BiigSacTAVCr6EMunK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 75,
      "cache_read_input_tokens": 24379,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 75
      },
      "output_tokens": 66,
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

_source line 13 · 2026-05-22T07:30:43.935Z_

<details><summary>↩ Tool result · `toolu_01W3EDLtJ5MDTcYaYcCuFVSp`</summary>

```text
1	@inproceedings{golde-2025-familiarity,
2	  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},
3	  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},
4	  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},
5	  year      = {2025},
6	  url       = {https://arxiv.org/abs/2412.10121}
7	}
8	
9	@book{cohen-1988-statistical,
10	  author    = {Cohen, Jacob},
11	  title     = {Statistical Power Analysis for the Behavioral Sciences},
12	  edition   = {2nd},
13	  publisher = {Lawrence Erlbaum Associates},
14	  year      = {1988}
15	}
16	
17	@inproceedings{baan-2023-ecological,
18	  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},
19	  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},
20	  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},
21	  year      = {2023}
22	}
23	
24	@inproceedings{josifoski-2022-genie,
25	  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},
26	  title     = {{GenIE}: Generative Information Extraction},
27	  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},
28	  pages     = {4626--4643},
29	  year      = {2022}
30	}
31	
32	@inproceedings{dubey-2018-pairwise-confusion,
33	  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},
34	  title     = {Pairwise Confusion for Fine-Grained Visual Classification},
35	  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},
36	  pages     = {71--88},
37	  year      = {2018}
38	}
39	
40	@inproceedings{collier-2021-correlated-noise,
41	  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},
42	  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},
43	  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
44	  pages     = {1551--1560},
45	  year      = {2021}
46	}
47	
48	@inproceedings{yin-2019-zero-shot-bench,
49	  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},
50	  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},
51	  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
52	  pages     = {3914--3923},
53	  year      = {2019},
54	  url       = {https://arxiv.org/abs/1909.00161}
55	}
56	
57	@article{schuirmann-1987-tost,
58	  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},
59	  author    = {Schuirmann, Donald J.},
60	  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},
61	  volume    = {15},
62	  number    = {6},
63	  pages     = {657--680},
64	  year      = {1987},
65	  doi       = {10.1007/BF01068419}
66	}
67	
68	@article{gemini-2025,
69	  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},
70	  author    = {{Gemini Team}},
71	  journal   = {arXiv preprint arXiv:2507.06261},
72	  year      = {2025},
73	  url       = {https://arxiv.org/abs/2507.06261}
74	}
75	
76	@inproceedings{snell2017prototypical,
77	  title     = {Prototypical Networks for Few-shot Learning},
78	  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},
79	  booktitle = {Advances in Neural Information Processing Systems},
80	  volume    = {30},
81	  year      = {2017}
82	}
83	
84	@inproceedings{muller2019when,
85	  title     = {When Does Label Smoothing Help?},
86	  author    = {M{\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},
87	  booktitle = {Advances in Neural Information Processing Systems},
88	  volume    = {32},
89	  year      = {2019}
90	}
91	
92	@inproceedings{peterson2019human,
93	  title     = {Human Uncertainty Makes Classification More Robust},
94	  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},
95	  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},
96	  pages     = {9617--9626},
97	  year      = {2019}
98	}
99	
100	@article{willard2023efficient,
101	  title     = {Efficient Guided Generation for Large Language Models},
102	  author    = {Willard, Brandon T. and Louf, R{\'e}mi},
103	  journal   = {arXiv preprint arXiv:2307.09702},
104	  year      = {2023},
105	  url       = {https://arxiv.org/abs/2307.09702}
106	}
107	
108	
109	
110	% =============================================================================
111	% DIRECT COMPETITORS
112	% =============================================================================
113	
114	@inproceedings{llm-pee-2025,
115	    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},
116	    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
117	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},
118	    year      = {2025},
119	    url       = {https://aclanthology.org/2025.emnlp-main.1743/},
120	}
121	
122	@inproceedings{parse-2025,
123	    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},
124	    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},
125	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
126	    year      = {2025},
127	    url       = {https://aclanthology.org/2025.emnlp-industry.184/},
128	}
129	
130	@inproceedings{crossagentie-2025,
131	    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},
132	    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},
133	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
134	    year      = {2025},
135	    url       = {https://aclanthology.org/2025.findings-acl.718/},
136	}
137	
138	
139	@inproceedings{cmas-ner-2025,
140	    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},
141	    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},
142	    booktitle = {Proceedings of the ACM Web Conference 2025},
143	    year      = {2025},
144	    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},
145	    doi       = {10.1145/3696410.3714923},
146	}
147	
148	% =============================================================================
149	% METHOD COMPONENTS
150	% =============================================================================
151	
152	@inproceedings{uniner-2024,
153	    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},
154	    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},
155	    booktitle = {International Conference on Learning Representations},
156	    year      = {2024},
157	    url       = {https://arxiv.org/abs/2308.03279},
158	}
159	
160	@inproceedings{gollie-2024,
161	    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},
162	    author    = {Sainz, Oscar and Garc{\'\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},
163	    booktitle = {International Conference on Learning Representations},
164	    year      = {2024},
165	    url       = {https://arxiv.org/abs/2310.03668},
166	}
167	
168	@inproceedings{gliner-2024,
169	    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},
170	    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},
171	    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},
172	    year      = {2024},
173	    url       = {https://arxiv.org/abs/2311.08526},
174	}
175	
176	@inproceedings{gliner2-2025,
177	    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},
178	    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},
179	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},
180	    year      = {2025},
181	    url       = {https://aclanthology.org/2025.emnlp-demos.10/},
182	}
183	
184	
185	@inproceedings{iepile-2024,
186	    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},
187	    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},
188	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
189	    pages     = {127--146},
190	    year      = {2024},
191	    url       = {https://aclanthology.org/2024.acl-short.13/},
192	}
193	
194	
195	@inproceedings{dror-2018-significance,
196	    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},
197	    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},
198	    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},
199	    year      = {2018},
200	    url       = {https://aclanthology.org/P18-1128/},
201	}
202	
203	@article{lost-in-middle-2024,
204	    title   = {Lost in the Middle: How Language Models Use Long Contexts},
205	    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},
206	    journal = {Transactions of the Association for Computational Linguistics},
207	    volume  = {12},
208	    pages   = {157--173},
209	    year    = {2024},
210	    url     = {https://arxiv.org/abs/2307.03172},
211	    doi     = {10.1162/tacl_a_00638},
212	}
213	
214	% =============================================================================
215	% ZERO-SHOT NER / RE BASELINES
216	% =============================================================================
217	
218	@inproceedings{shachar-2025-ner-retriever,
219	    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},
220	    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},
221	    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},
222	    year      = {2025},
223	    pages     = {11175--11186},
224	}
225	
226	
227	
228	% =============================================================================
229	% EVALUATION / BENCHMARKING
230	% =============================================================================
231	
232	% =============================================================================
233	% SURVEYS / BACKGROUND
234	% =============================================================================
235	
236	@article{llm4ie-survey-2024,
237	    title   = {Large Language Models for Generative Information Extraction: A Survey},
238	    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},
239	    journal = {Frontiers of Computer Science},
240	    volume  = {18},
241	    number  = {6},
242	    year    = {2024},
243	    url     = {https://arxiv.org/abs/2312.17617},
244	    doi     = {10.1007/s11704-024-40555-y},
245	}
246	
247	@inproceedings{knowcoder-2024,
248	    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},
249	    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},
250	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
251	    year      = {2024},
252	    url       = {https://arxiv.org/abs/2403.07969},
253	}
254	
255	@inproceedings{slot-2025,
256	    title     = {{SLOT}: Structuring the Output of Large Language Models},
257	    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},
258	    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},
259	    year      = {2025},
260	    url       = {https://aclanthology.org/2025.emnlp-industry.32/},
261	}
262	
263	% =============================================================================
264	% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION
265	% =============================================================================
266	
267	
268	@inproceedings{ethayarajh-contextual-2019,
269	    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},
270	    author    = {Ethayarajh, Kawin},
271	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},
272	    year      = {2019},
273	    url       = {https://aclanthology.org/D19-1006/},
274	}
275	
276	@inproceedings{cai-isotropy-clusters-2021,
277	    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},
278	    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},
279	    booktitle = {International Conference on Learning Representations},
280	    year      = {2021},
281	    url       = {https://openreview.net/forum?id=xYGNO86OWDH},
282	}
283	
284	
285	% =============================================================================
286	% ADDITIONAL REFERENCES (from references_survey.md only)
287	% =============================================================================
288	
289	@article{instructuie-2023,
290	    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},
291	    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},
292	    journal = {arXiv preprint arXiv:2304.08085},
293	    year    = {2023},
294	    url     = {https://arxiv.org/abs/2304.08085},
295	}
296	
297	@inproceedings{codeie-2023,
298	    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},
299	    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},
300	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
301	    year      = {2023},
302	    url       = {https://aclanthology.org/2023.acl-long.855/},
303	}
304	
305	@inproceedings{adelie-2024,
306	    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},
307	    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},
308	    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},
309	    year      = {2024},
310	    url       = {https://aclanthology.org/2024.emnlp-main.419/},
311	}
312	
313	@inproceedings{oneke-2025,
314	    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},
315	    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},
316	    booktitle = {Companion Proceedings of the ACM Web Conference 2025},
317	    year      = {2025},
318	    url       = {https://arxiv.org/abs/2412.20005},
319	    doi       = {10.1145/3701716.3715189},
320	}
321	
322	
323	
324	
325	% =============================================================================
326	% DATASETS
327	% =============================================================================
328	
329	@inproceedings{fewnerd-2021,
330	    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},
331	    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},
332	    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},
333	    year      = {2021},
334	    url       = {https://aclanthology.org/2021.acl-long.248/},
335	}
336	
337	@inproceedings{fewrel-2018,
338	    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},
339	    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},
340	    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},
341	    year      = {2018},
342	    url       = {https://aclanthology.org/D18-1514/},
343	}
344	
345	@inproceedings{maven-2020,
346	    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},
347	    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},
348	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},
349	    year      = {2020},
350	    url       = {https://aclanthology.org/2020.emnlp-main.129/},
351	}
352	
353	@inproceedings{docred-2019,
354	    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},
355	    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},
356	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
357	    year      = {2019},
358	    url       = {https://aclanthology.org/P19-1074/},
359	}
360	
361	% =============================================================================
362	% MODELS AND TOOLS
363	% =============================================================================
364	
365	@article{qwen3-2025,
366	    title   = {Qwen3 Technical Report},
367	    author  = {{Qwen Team}},
368	    journal = {arXiv preprint arXiv:2505.09388},
369	    year    = {2025},
370	    url     = {https://arxiv.org/abs/2505.09388},
371	}
372	
373	@article{llama3-2024,
374	    title   = {The {Llama} 3 Herd of Models},
375	    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},
376	    journal = {arXiv preprint arXiv:2407.21783},
377	    year    = {2024},
378	    url     = {https://arxiv.org/abs/2407.21783},
379	}
380	
381	@inproceedings{sentence-bert-2019,
382	    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
383	    author    = {Reimers, Nils and Gurevych, Iryna},
384	    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
385	    year      = {2019},
386	    url       = {https://aclanthology.org/D19-1410/},
387	}
388	
389	@inproceedings{minilm-2020,
390	    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},
391	    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},
392	    booktitle = {Advances in Neural Information Processing Systems},
393	    volume    = {33},
394	    year      = {2020},
395	    url       = {https://arxiv.org/abs/2002.10957},
396	}
397	
398	@inproceedings{reflect-learn-2026,
399	    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},
400	    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},
401	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
402	    volume    = {40},
403	    pages     = {34923--34931},
404	    year      = {2026},
405	    url       = {https://arxiv.org/abs/2508.10036},
406	    doi       = {10.1609/aaai.v40i41.40796},
407	}
408	
409	@inproceedings{sclar-sensitivity-2024,
410	    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},
411	    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},
412	    booktitle = {International Conference on Learning Representations},
413	    year      = {2024},
414	    url       = {https://arxiv.org/abs/2310.11324},
415	}
416	
417	@inproceedings{vllm-2023,
418	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
419	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
420	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
421	    year      = {2023},
422	    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},
423	}
424	
425	@inproceedings{xie-zeroshot-ner-2023,
426	    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},
427	    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},
428	    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
429	    year      = {2023},
430	    url       = {https://aclanthology.org/2023.emnlp-main.493/},
431	}
432	
433	@inproceedings{wadhwa-re-llm-2023,
434	    title     = {Revisiting Relation Extraction in the era of Large Language Models},
435	    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},
436	    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},
437	    pages     = {15566--15589},
438	    year      = {2023},
439	    url       = {https://aclanthology.org/2023.acl-long.868/},
440	}
441	
442	@inproceedings{relationprompt-2022,
443	    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},
444	    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},
445	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
446	    pages     = {45--57},
447	    year      = {2022},
448	    url       = {https://aclanthology.org/2022.findings-acl.5/},
449	}
450	
451	@article{promptner-2023,
452	    title   = {{PromptNER}: Prompting For Named Entity Recognition},
453	    author  = {Ashok, Dhananjay and Lipton, Zachary C.},
454	    journal = {arXiv preprint arXiv:2305.15444},
455	    year    = {2023},
456	    url     = {https://arxiv.org/abs/2305.15444},
457	}
458	
459	@article{json-schema-bench-2025,
460	    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},
461	    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},
462	    journal = {arXiv preprint arXiv:2501.10868},
463	    year    = {2025},
464	    url     = {https://arxiv.org/abs/2501.10868},
465	}
466	
467	@inproceedings{rastogi2020towards,
468	    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},
469	    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},
470	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
471	    volume    = {34},
472	    pages     = {8689--8696},
473	    year      = {2020},
474	    url       = {https://arxiv.org/abs/1909.05855},
475	}
476	
477	@article{li2023evaluating,
478	    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},
479	    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},
480	    journal = {arXiv preprint arXiv:2304.11633},
481	    year    = {2023},
482	    url     = {https://arxiv.org/abs/2304.11633},
483	}
484	
485	@inproceedings{lee2022sgd,
486	    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},
487	    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},
488	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
489	    volume    = {36},
490	    pages     = {10938--10946},
491	    year      = {2022},
492	    url       = {https://arxiv.org/abs/2110.06800},
493	}
494	
495	@article{haystack-to-needle-2025,
496	    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},
497	    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},
498	    journal = {arXiv preprint arXiv:2502.08436},
499	    year    = {2025},
500	    url     = {https://arxiv.org/abs/2502.08436},
501	}
502	
503	@inproceedings{deng-2010-imagenet,
504	    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},
505	    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},
506	    booktitle = {Proceedings of the 11th European Conference on Computer Vision},
507	    pages     = {71--84},
508	    year      = {2010},
509	    doi       = {10.1007/978-3-642-15555-0\_6},
510	}
511	
512	@article{rothman-1990,
513	    title   = {No Adjustments Are Needed for Multiple Comparisons},
514	    author  = {Rothman, Kenneth J.},
515	    journal = {Epidemiology},
516	    volume  = {1},
517	    number  = {1},
518	    pages   = {43--46},
519	    year    = {1990},
520	    doi     = {10.1097/00001648-199001000-00010},
521	}
522	
523	@article{lakens-2017-equivalence,
524	    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},
525	    author  = {Lakens, Dani{\"e}l},
526	    journal = {Social Psychological and Personality Science},
527	    volume  = {8},
528	    number  = {4},
529	    pages   = {355--362},
530	    year    = {2017},
531	    doi     = {10.1177/1948550617697177},
532	}
533	
534	
535	@inproceedings{guo-2021-label-confusion,
536	    title     = {Label Confusion Learning to Enhance Text Classification Models},
537	    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},
538	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
539	    volume    = {35},
540	    number    = {14},
541	    pages     = {12929--12936},
542	    year      = {2021},
543	    doi       = {10.1609/aaai.v35i14.17529},
544	}
545	
546	
547	@article{dlisc-2025,
548	    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},
549	    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},
550	    journal   = {arXiv preprint arXiv:2505.14992},
551	    year      = {2025},
552	    url       = {https://arxiv.org/abs/2505.14992}
553	}
554	
555	@article{spt-2025,
556	    title     = {Schema as Parameterized Tools for Universal Information Extraction},
557	    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},
558	    journal   = {arXiv preprint arXiv:2506.01276},
559	    year      = {2025},
560	    url       = {https://arxiv.org/abs/2506.01276}
561	}
562	
563	@inproceedings{card-2020-power,
564	    title     = {With Little Power Comes Great Responsibility},
565	    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},
566	    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
567	    pages     = {9263--9274},
568	    year      = {2020},
569	    publisher = {Association for Computational Linguistics},
570	    url       = {https://aclanthology.org/2020.emnlp-main.745}
571	}
572	
573	@article{chen-2026-multi-instance,
574	    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},
575	    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},
576	    journal   = {arXiv preprint arXiv:2603.22608},
577	    year      = {2026},
578	    url       = {https://arxiv.org/abs/2603.22608}
579	}
580	
581	@article{robinson-1950-ecological,
582	    author    = {Robinson, William S.},
583	    title     = {Ecological Correlations and the Behavior of Individuals},
584	    journal   = {American Sociological Review},
585	    volume    = {15},
586	    number    = {3},
587	    pages     = {351--357},
588	    year      = {1950}
589	}
590	
591	@inproceedings{boylan-2025-glirel,
592	    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},
593	    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},
594	    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},
595	    year      = {2025},
596	    address   = {Albuquerque, New Mexico},
597	    publisher = {Association for Computational Linguistics},
598	    pages     = {8230--8245},
599	    url       = {https://aclanthology.org/2025.naacl-long.418/}
600	}
601	
602	
603	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c09997e4-e1bb-4680-80e6-c827edb791e0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
      "content": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
      "numLines": 603,
      "startLine": 1,
      "totalLines": 603
    }
  }
}
```

</details>

---


### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now let me classify the 27 entries by venue:

**ACL Anthology papers** (booktitle contains ACL/EMNLP/NAACL/EACL/COLING/Findings/SemEval):

1. `golde-2025-familiarity` - NAACL 2025 → ACL Anthology
2. `baan-2023-ecological` - ACL 2023 → ACL Anthology
3. `llm-pee-2025` - EMNLP 2025 → ACL Anthology (has URL to aclanthology.org)


4. `parse-2025` - EMNLP 2025 Industry Track → ACL Anthology
5. `crossagentie-2025` - Findings ACL 2025 → ACL Anthology
9. `gliner-2024` - NAACL 2024 → ACL Anthology

Continuing through the rest, I'm filtering out the non-ACL venues like the ACM Web Conference and ICLR papers, then checking the remaining entries to see which ones belong in the ACL Anthology. Continuing through the references—most of the remaining ones map to ACL Anthology venues like ACL and EMNLP conferences with their corresponding URLs, though I'm skipping a few that belong to other conference series like NeurIPS, ICLR, and SOSP. Continuing through the remaining papers to verify: the crossagentie entry completes with its full ACL Anthology URL, then I have several more to track down including gliner-2024, gliner2-2025 with its demos link, dror-2018 on significance testing, knowcoder-2024, slot-2025 for the industry track, and ethayarajh-contextual-2019 which appears to have an incomplete URL. Continuing through the remaining papers from ACL and EMNLP conferences, then filtering out entries from machine learning venues like ICLR and NeurIPS, plus a couple from other conference series that don't fit the criteria.

I notice many of these papers already have ACL Anthology URLs, so I can fetch those pages directly to extract the page numbers rather than searching for them individually. Let me load the WebFetch and WebSearch tools to handle this efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "551fbf81-b236-418f-aef9-6ef391c64391",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSgVJUKhmN1EQdhWy9FBHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10954,
      "cache_read_input_tokens": 24454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10954
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

_source line 15_

19 个条目属于 ACL Anthology，多数已有 URL，可以直接查页码。先加载需要的工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "249ee426-d538-4a02-9410-2b340ae6711e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSgVJUKhmN1EQdhWy9FBHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10954,
      "cache_read_input_tokens": 24454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10954
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

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01K9W2CiF6Rm5jsHkEDNSbmq`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "4686a942-2a14-4f0f-a512-ae6bcd285e18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VSgVJUKhmN1EQdhWy9FBHk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10954,
      "cache_read_input_tokens": 24454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10954
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

_source line 17 · 2026-05-22T07:31:11.234Z_

<details><summary>↩ Tool result · `toolu_01K9W2CiF6Rm5jsHkEDNSbmq`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

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
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "0f904a27-c58a-4826-beb7-4f9646a31ee0",
  "tool_use_result": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 22
  }
}
```

</details>

---


### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have the tools. Let me classify the 27 entries:

**ACL Anthology (19 entries to look up):**
Many already have ACL Anthology URLs. I can fetch those pages directly. Let me batch fetch them.

Entries with ACL Anthology URLs:
1. llm-pee-2025 → https://aclanthology.org/2025.emnlp-main.1743/
2. parse-2025 → https://aclanthology.org/2025.emnlp-industry.184/


3. crossagentie-2025 → https://aclanthology.org/2025.findings-acl.718/
4. gliner2-2025 → https://aclanthology.org/2025.emnlp-demos.10/
5. dror-2018-significance → https://aclanthology.org/P18-1128/
6. slot-2025 → https://aclanthology.org/2025.emnlp-industry.32/
7. ethayarajh-contextual-2019 → https://aclanthology.org/D19-1006/
8. codeie-2025 → https://aclanthology.org/2025.emnlp-main.1234/

Continuing through the remaining entries with their anthology links...

9. adelie-2024 → https://aclanthology.org/2024.emnlp-main.419/
10. fewnerd-2021 → https://aclanthology.org/2021.acl-long.248/
11. fewrel-2018 → https://aclanthology.org/D18-1514/
12. maven-2020 → https://aclanthology.org/2020.emnlp-main.129/
13. docred-2019 → https://aclanthology.org/P19-1074/
14. sentence-bert-2019 → https://aclanthology.org/D19-1410/
15. xie-zeroshot-ner-2023 → https://aclanthology.org/2023.emnlp-main.493/

Now I'm noting which entries don't have ACL Anthology URLs available yet.

I need to skip papers from non-NLP venues like ICLR, NeurIPS, SOSP, and ACM conferences. For the remaining entries that need URLs, I'll parallelize fetching the ACL Anthology pages to extract page numbers efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "2d5ad468-981c-4b56-b8f8-3e57458760ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3opC5CR4E7Qyhj3MSoPKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2897,
      "cache_read_input_tokens": 35408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2897
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

_source line 19_

分类完成。19 个属于 ACL Anthology，其中 15 个已有 ACL Anthology URL 可直接查，4 个需要搜索。8 个跳过（5 个 ICLR/NeurIPS，3 个 ACM/SOSP）。

并行获取页码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "f413ef0d-1ec4-42ed-80b1-7647309ba3da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3opC5CR4E7Qyhj3MSoPKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2897,
      "cache_read_input_tokens": 35408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2897
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

_source line 20_

<details open><summary>🔧 Tool call — Agent · `toolu_01KZbgGqCG64PdHot826gzUX`</summary>

```json
{
  "description": "Fetch ACL pages batch 1",
  "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. llm-pee-2025 → https://aclanthology.org/2025.emnlp-main.1743/\n2. parse-2025 → https://aclanthology.org/2025.emnlp-industry.184/\n3. crossagentie-2025 → https://aclanthology.org/2025.findings-acl.718/\n4. gliner2-2025 → https://aclanthology.org/2025.emnlp-demos.10/\n5. dror-2018-significance → https://aclanthology.org/P18-1128/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "a2a56400-2f0e-4659-b068-108ae37a7b41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3opC5CR4E7Qyhj3MSoPKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2897,
      "cache_read_input_tokens": 35408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2897
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


### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetch ACL pages batch 1",
  "task_type": "local_agent",
  "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. llm-pee-2025 → https://aclanthology.org/2025.emnlp-main.1743/\n2. parse-2025 → https://aclanthology.org/2025.emnlp-industry.184/\n3. crossagentie-2025 → https://aclanthology.org/2025.findings-acl.718/\n4. gliner2-2025 → https://aclanthology.org/2025.emnlp-demos.10/\n5. dror-2018-significance → https://aclanthology.org/P18-1128/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\"",
  "uuid": "c6b5f750-df71-41c1-9ed4-0a6fd3e92489",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


## Round 1

## Round 1

3 recorded events


### User

_source line 22 · 2026-05-22T07:31:31.540Z_

Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for "pages" or "pp." or a pattern like "1234--5678" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.

1. llm-pee-2025 → https://aclanthology.org/2025.emnlp-main.1743/
2. parse-2025 → https://aclanthology.org/2025.emnlp-industry.184/
3. crossagentie-2025 → https://aclanthology.org/2025.findings-acl.718/
4. gliner2-2025 → https://aclanthology.org/2025.emnlp-demos.10/
5. dror-2018-significance → https://aclanthology.org/P18-1128/

For each URL, use WebFetch with prompt: "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "6b3e264f-94f3-43e2-b703-c00b9d6a4075"
}
```

</details>

---


### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Agent · `toolu_01U7XFpuyTLbZMtNpoEDJRTN`</summary>

```json
{
  "description": "Fetch ACL pages batch 2",
  "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. slot-2025 → https://aclanthology.org/2025.emnlp-industry.32/\n2. ethayarajh-contextual-2019 → https://aclanthology.org/D19-1006/\n3. codeie-2023 → https://aclanthology.org/2023.acl-long.855/\n4. adelie-2024 → https://aclanthology.org/2024.emnlp-main.419/\n5. fewnerd-2021 → https://aclanthology.org/2021.acl-long.248/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "4817e124-8432-4ef6-8c81-1f81ad3466bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3opC5CR4E7Qyhj3MSoPKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2897,
      "cache_read_input_tokens": 35408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2897
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


### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetch ACL pages batch 2",
  "task_type": "local_agent",
  "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. slot-2025 → https://aclanthology.org/2025.emnlp-industry.32/\n2. ethayarajh-contextual-2019 → https://aclanthology.org/D19-1006/\n3. codeie-2023 → https://aclanthology.org/2023.acl-long.855/\n4. adelie-2024 → https://aclanthology.org/2024.emnlp-main.419/\n5. fewnerd-2021 → https://aclanthology.org/2021.acl-long.248/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\"",
  "uuid": "99dfb014-74c3-4653-9702-ed6869fe833b",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


## Round 2

## Round 2

6 recorded events


### User

_source line 25 · 2026-05-22T07:31:33.906Z_

Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for "pages" or "pp." or a pattern like "1234--5678" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.

1. slot-2025 → https://aclanthology.org/2025.emnlp-industry.32/
2. ethayarajh-contextual-2019 → https://aclanthology.org/D19-1006/
3. codeie-2023 → https://aclanthology.org/2023.acl-long.855/
4. adelie-2024 → https://aclanthology.org/2024.emnlp-main.419/
5. fewnerd-2021 → https://aclanthology.org/2021.acl-long.248/

For each URL, use WebFetch with prompt: "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "f0d7b04d-94a9-437d-8f9c-e76664f76e81"
}
```

</details>

---


### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetch ACL pages batch 1",
  "usage": {
    "total_tokens": 14893,
    "tool_uses": 1,
    "duration_ms": 3642
  },
  "last_tool_name": "ToolSearch",
  "uuid": "6b23d8f2-4e0f-4414-96b8-4b79d910906f",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01R35JFb1xvirnu53jAYnNij`</summary>

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
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "8194f1df-1655-4fca-89de-a259f0251ae7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCHtMGEsqpfec5vzpCzLsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14886,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14886,
        "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-22T07:31:35.191Z_

<details><summary>↩ Tool result · `toolu_01R35JFb1xvirnu53jAYnNij`</summary>

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
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "1e841c0c-8380-45f8-b25a-71be4de71db5"
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Agent · `toolu_01KnTzoQh1p4RBVoPkXVXVAL`</summary>

```json
{
  "description": "Fetch ACL pages batch 3",
  "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. fewrel-2018 → https://aclanthology.org/D18-1514/\n2. maven-2020 → https://aclanthology.org/2020.emnlp-main.129/\n3. docred-2019 → https://aclanthology.org/P19-1074/\n4. sentence-bert-2019 → https://aclanthology.org/D19-1410/\n5. xie-zeroshot-ner-2023 → https://aclanthology.org/2023.emnlp-main.493/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c57d8986-c831-4db7-843d-42bb23eea207",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3opC5CR4E7Qyhj3MSoPKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2897,
      "cache_read_input_tokens": 35408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2897
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


### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetch ACL pages batch 3",
  "task_type": "local_agent",
  "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. fewrel-2018 → https://aclanthology.org/D18-1514/\n2. maven-2020 → https://aclanthology.org/2020.emnlp-main.129/\n3. docred-2019 → https://aclanthology.org/P19-1074/\n4. sentence-bert-2019 → https://aclanthology.org/D19-1410/\n5. xie-zeroshot-ner-2023 → https://aclanthology.org/2023.emnlp-main.493/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\"",
  "uuid": "8a45ebbe-e558-42ef-8121-92a07b255cb5",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


## Round 3

## Round 3

33 recorded events


### User

_source line 31 · 2026-05-22T07:31:36.423Z_

Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for "pages" or "pp." or a pattern like "1234--5678" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.

1. fewrel-2018 → https://aclanthology.org/D18-1514/
2. maven-2020 → https://aclanthology.org/2020.emnlp-main.129/
3. docred-2019 → https://aclanthology.org/P19-1074/
4. sentence-bert-2019 → https://aclanthology.org/D19-1410/
5. xie-zeroshot-ner-2023 → https://aclanthology.org/2023.emnlp-main.493/

For each URL, use WebFetch with prompt: "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e061f1ba-2758-4914-9b49-dba25dcb7541"
}
```

</details>

---


### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetch ACL pages batch 2",
  "usage": {
    "total_tokens": 14891,
    "tool_uses": 1,
    "duration_ms": 3151
  },
  "last_tool_name": "ToolSearch",
  "uuid": "fc71006a-7c12-4f80-bd9f-03883f98b44e",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 33_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetching https://aclanthology.org/2025.emnlp-main.1743/",
  "usage": {
    "total_tokens": 16342,
    "tool_uses": 2,
    "duration_ms": 7049
  },
  "last_tool_name": "WebFetch",
  "uuid": "ea98cc73-4705-4bde-8440-ebde39341327",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetch ACL pages batch 3",
  "usage": {
    "total_tokens": 14884,
    "tool_uses": 1,
    "duration_ms": 3174
  },
  "last_tool_name": "ToolSearch",
  "uuid": "1c294743-fe63-4131-8c7f-4d5b8f680b44",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetching https://aclanthology.org/2025.emnlp-industry.184/",
  "usage": {
    "total_tokens": 16344,
    "tool_uses": 3,
    "duration_ms": 8081
  },
  "last_tool_name": "WebFetch",
  "uuid": "ec9c2d74-d1a3-4140-b77e-3f656ed33013",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetching https://aclanthology.org/2025.findings-acl.718/",
  "usage": {
    "total_tokens": 16346,
    "tool_uses": 4,
    "duration_ms": 8430
  },
  "last_tool_name": "WebFetch",
  "uuid": "e4f7d5eb-97cf-46d8-89d0-e32b99d6c9fb",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetching https://aclanthology.org/2025.emnlp-industry.32/",
  "usage": {
    "total_tokens": 16339,
    "tool_uses": 2,
    "duration_ms": 6602
  },
  "last_tool_name": "WebFetch",
  "uuid": "1523b9c2-3b05-45f1-91e8-7ab41bb1854b",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetching https://aclanthology.org/2025.emnlp-demos.10/",
  "usage": {
    "total_tokens": 16348,
    "tool_uses": 5,
    "duration_ms": 9382
  },
  "last_tool_name": "WebFetch",
  "uuid": "5e65b03b-aaa3-4d96-9092-db0c42815432",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetching https://aclanthology.org/D19-1006/",
  "usage": {
    "total_tokens": 16341,
    "tool_uses": 3,
    "duration_ms": 7440
  },
  "last_tool_name": "WebFetch",
  "uuid": "bf60061d-07aa-4405-9126-d42141f6cc24",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "description": "Fetching https://aclanthology.org/P18-1128/",
  "usage": {
    "total_tokens": 16350,
    "tool_uses": 6,
    "duration_ms": 9945
  },
  "last_tool_name": "WebFetch",
  "uuid": "6d73e0b6-8a13-4fe7-8433-acc38a65f20b",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetching https://aclanthology.org/2023.acl-long.855/",
  "usage": {
    "total_tokens": 16343,
    "tool_uses": 4,
    "duration_ms": 7928
  },
  "last_tool_name": "WebFetch",
  "uuid": "8796edd5-7cb1-4a6a-ba23-0f6890c31dff",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RNr9au65Cn36B3TwG8mWDw`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.1743/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "86365184-b265-4731-be36-eba35e250549",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN2YK4kPmLtheN4M22akzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 14886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
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

_source line 43_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01U9fJyWDjB8sMHfcGsNZM4g`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-industry.184/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "448ed983-d64b-442a-b1c5-144e714f42c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN2YK4kPmLtheN4M22akzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 14886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
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

_source line 44_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01LGhkWnWHYRNfq5VQjgA1QL`</summary>

```json
{
  "url": "https://aclanthology.org/2025.findings-acl.718/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "18fc283a-f5ea-4596-84aa-52dddd7e640b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN2YK4kPmLtheN4M22akzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 14886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
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

_source line 45 · 2026-05-22T07:31:40.758Z_

<details><summary>↩ Tool result · `toolu_01RNr9au65Cn36B3TwG8mWDw`</summary>

```text
34377--34399
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "3886902a-a702-4e13-951f-26c415903236"
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-22T07:31:40.797Z_

<details><summary>↩ Tool result · `toolu_01U9fJyWDjB8sMHfcGsNZM4g`</summary>

```text
2749--2763
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "ae03ff55-3f0f-4bd8-a9b7-482119908476"
}
```

</details>

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014BTztaxaP2pENFycPhEFre`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-demos.10/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "1ff12f6c-c93c-4e3d-9d52-015c92fc2ce3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN2YK4kPmLtheN4M22akzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 14886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
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

_source line 48 · 2026-05-22T07:31:41.042Z_

<details><summary>↩ Tool result · `toolu_01LGhkWnWHYRNfq5VQjgA1QL`</summary>

```text
13953--13977
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c1deb665-06ff-48a6-9502-78aa64ba0bfd"
}
```

</details>

---


### Tool call

_source line 49_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PbNW5jKfzKqx3SgRaFxfsF`</summary>

```json
{
  "url": "https://aclanthology.org/P18-1128/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "cf10615d-1ce5-44aa-b826-b16fabb676ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LN2YK4kPmLtheN4M22akzi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1445,
      "cache_read_input_tokens": 14886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1445,
        "ephemeral_1h_input_tokens": 0
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

_source line 50 · 2026-05-22T07:31:42.157Z_

<details><summary>↩ Tool result · `toolu_014BTztaxaP2pENFycPhEFre`</summary>

```text
130--140
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "302a5bbd-b658-45f8-bcb8-70a53399eda1"
}
```

</details>

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UztZfbQ5VYyPHb8veG5Zw7`</summary>

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
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "3dc4db93-725c-4375-9649-815e0867bfc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DFEbHj1Phn3yvMkEceLSWg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6635,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6635,
        "ephemeral_1h_input_tokens": 0
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

_source line 52 · 2026-05-22T07:31:37.065Z_

<details><summary>↩ Tool result · `toolu_01UztZfbQ5VYyPHb8veG5Zw7`</summary>

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
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "dea73f1c-fbec-427d-9cfa-93934df3e998"
}
```

</details>

---


### Tool call

_source line 53_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BFXLowmskqbdbzgWe3fCdx`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-industry.32/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "d007fe93-4a1c-4a26-b77f-10a7fef0c208",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tJiQJRuetvxveiYMY44fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 54_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NNenmerCLEgQy782necY9i`</summary>

```json
{
  "url": "https://aclanthology.org/D19-1006/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "f86d6dc4-f6ec-4cc5-ac22-8b99c01d7f07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tJiQJRuetvxveiYMY44fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 55_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015rx8zBSfS6nfY3EEqGh9mL`</summary>

```json
{
  "url": "https://aclanthology.org/2023.acl-long.855/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "be2e10d9-8ea3-463d-9a18-2717d4c590a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tJiQJRuetvxveiYMY44fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 56 · 2026-05-22T07:31:41.920Z_

<details><summary>↩ Tool result · `toolu_01BFXLowmskqbdbzgWe3fCdx`</summary>

```text
472--491
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "6eb9d611-8963-4447-bc31-665eb11e2e38"
}
```

</details>

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01U83hNw9YmMfSubY3jWciD6`</summary>

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
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e73d407e-7537-4b1c-a6e3-7516592669e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAqCQ5UD7cwV4abD1EuYMY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6628,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6628,
        "ephemeral_1h_input_tokens": 0
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

_source line 58 · 2026-05-22T07:31:39.609Z_

<details><summary>↩ Tool result · `toolu_01U83hNw9YmMfSubY3jWciD6`</summary>

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
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "5a1bf119-6860-4a4c-bb06-0331a9cacea1"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetching https://aclanthology.org/2024.emnlp-main.419/",
  "usage": {
    "total_tokens": 16345,
    "tool_uses": 5,
    "duration_ms": 8834
  },
  "last_tool_name": "WebFetch",
  "uuid": "0a908231-fcd9-42d4-9061-1c2ae0ceaceb",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool result

_source line 60 · 2026-05-22T07:31:42.363Z_

<details><summary>↩ Tool result · `toolu_01NNenmerCLEgQy782necY9i`</summary>

```text
55--65
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "0f9ce824-89bf-42c6-9bda-2d5d15871031"
}
```

</details>

---


### Tool call

_source line 61_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016uQavhhupsK7MeV6ketEwe`</summary>

```json
{
  "url": "https://aclanthology.org/2024.emnlp-main.419/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "60466f78-a583-4145-ab6e-67be06805bc4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tJiQJRuetvxveiYMY44fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 62_

<details open><summary>🔧 Tool call — Agent · `toolu_01CRCMF1zzQTAi42oLZYKbTc`</summary>

```json
{
  "description": "Search ACL pages batch 4",
  "prompt": "Search for page numbers of these 4 ACL Anthology papers that don't have direct URLs. For each, search on aclanthology.org, then fetch the page to get the pages field from the BibTeX.\n\n1. golde-2025-familiarity: \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\" (NAACL 2025)\n2. baan-2023-ecological: \"The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics\" (ACL 2023)\n3. gliner-2024: \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\" (NAACL 2024)\n4. knowcoder-2024: \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\" (ACL 2024)\n\nFor each paper:\n- Use WebSearch with query: site:aclanthology.org \"paper title\" \n- Then use WebFetch on the ACL Anthology URL to extract the pages field from the BibTeX\n- Return ONLY: citation_key = pages (or \"not found\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "b1708859-250d-4c16-9b35-0108899db8fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3opC5CR4E7Qyhj3MSoPKs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2897,
      "cache_read_input_tokens": 35408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2897
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


### System

_source line 63_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Search ACL pages batch 4",
  "task_type": "local_agent",
  "prompt": "Search for page numbers of these 4 ACL Anthology papers that don't have direct URLs. For each, search on aclanthology.org, then fetch the page to get the pages field from the BibTeX.\n\n1. golde-2025-familiarity: \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\" (NAACL 2025)\n2. baan-2023-ecological: \"The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics\" (ACL 2023)\n3. gliner-2024: \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\" (NAACL 2024)\n4. knowcoder-2024: \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\" (ACL 2024)\n\nFor each paper:\n- Use WebSearch with query: site:aclanthology.org \"paper title\" \n- Then use WebFetch on the ACL Anthology URL to extract the pages field from the BibTeX\n- Return ONLY: citation_key = pages (or \"not found\")",
  "uuid": "c48e25e2-9c1a-4de9-80ab-a3be6fc4d156",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


## Round 4

## Round 4

99 recorded events


### User

_source line 64 · 2026-05-22T07:31:42.773Z_

Search for page numbers of these 4 ACL Anthology papers that don't have direct URLs. For each, search on aclanthology.org, then fetch the page to get the pages field from the BibTeX.

1. golde-2025-familiarity: "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data" (NAACL 2025)
2. baan-2023-ecological: "The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics" (ACL 2023)
3. gliner-2024: "GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer" (NAACL 2024)
4. knowcoder-2024: "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction" (ACL 2024)

For each paper:
- Use WebSearch with query: site:aclanthology.org "paper title" 
- Then use WebFetch on the ACL Anthology URL to extract the pages field from the BibTeX
- Return ONLY: citation_key = pages (or "not found")

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "33fff731-d4bb-4fbb-b090-4c39d61b35e3"
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-22T07:31:42.915Z_

<details><summary>↩ Tool result · `toolu_01PbNW5jKfzKqx3SgRaFxfsF`</summary>

```text
1383--1392
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "04e017cb-2646-41a1-9611-116a4b71a251"
}
```

</details>

---


### System

_source line 66_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetching https://aclanthology.org/D18-1514/",
  "usage": {
    "total_tokens": 16332,
    "tool_uses": 2,
    "duration_ms": 6573
  },
  "last_tool_name": "WebFetch",
  "uuid": "27cd09a5-6293-408a-8c95-3adb91dbb8d9",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 67_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FAD26dp3tkv5xA48MKP1Da`</summary>

```json
{
  "url": "https://aclanthology.org/D18-1514/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "3f06cbc5-90cd-4b22-bd7b-bfd7a68c63d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HnZX6Mo6ie9PvFFvEFTqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 68 · 2026-05-22T07:31:42.992Z_

<details><summary>↩ Tool result · `toolu_015rx8zBSfS6nfY3EEqGh9mL`</summary>

```text
15339--15353
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e7a86aed-d30f-49e1-8670-54f4eba92f2c"
}
```

</details>

---


### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "description": "Fetching https://aclanthology.org/2021.acl-long.248/",
  "usage": {
    "total_tokens": 16347,
    "tool_uses": 6,
    "duration_ms": 9429
  },
  "last_tool_name": "WebFetch",
  "uuid": "ef398e83-ce02-4a50-bd09-62378d7f7c84",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 70_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BmcK9imqz7F27CvbKKvHQy`</summary>

```json
{
  "url": "https://aclanthology.org/2021.acl-long.248/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "d45dcef9-2743-4cb4-99e6-c6b12bcd4fb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019tJiQJRuetvxveiYMY44fy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 71 · 2026-05-22T07:31:43.933Z_

<details><summary>↩ Tool result · `toolu_016uQavhhupsK7MeV6ketEwe`</summary>

```text
Looking at the BibTeX citation provided on the page, the pages field is:

**7371--7387**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "4f4b7964-7082-4739-b738-6a0ee5479f8d"
}
```

</details>

---


### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetching https://aclanthology.org/2020.emnlp-main.129/",
  "usage": {
    "total_tokens": 16334,
    "tool_uses": 3,
    "duration_ms": 7532
  },
  "last_tool_name": "WebFetch",
  "uuid": "a12dfc9c-bd4a-44b0-980f-aea97522ee64",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 73_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016iJdigsePYb2eN85ESTLA4`</summary>

```json
{
  "url": "https://aclanthology.org/2020.emnlp-main.129/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c2952e27-a973-473e-84a8-a6dcee24c683",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HnZX6Mo6ie9PvFFvEFTqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 74 · 2026-05-22T07:31:44.179Z_

<details><summary>↩ Tool result · `toolu_01FAD26dp3tkv5xA48MKP1Da`</summary>

```text
Based on the BibTeX citation provided on this page, the page numbers are:

**4803--4809**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "303b673b-fd8b-4d1d-b4a0-d224aecee8cb"
}
```

</details>

---


### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetching https://aclanthology.org/P19-1074/",
  "usage": {
    "total_tokens": 16336,
    "tool_uses": 4,
    "duration_ms": 7995
  },
  "last_tool_name": "WebFetch",
  "uuid": "0fda7483-89ad-4e45-8bdc-f50fe3682b8b",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 76_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FvK2NqoLgBbyjS3vSVxJLt`</summary>

```json
{
  "url": "https://aclanthology.org/P19-1074/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "1841bb93-8f8a-4e62-8ada-079280038bfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HnZX6Mo6ie9PvFFvEFTqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 77 · 2026-05-22T07:31:44.588Z_

<details><summary>↩ Tool result · `toolu_01BmcK9imqz7F27CvbKKvHQy`</summary>

```text
3198--3213
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "5f0b2997-9c3b-4298-8dec-dea7bd0a8672"
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-22T07:31:45.069Z_

<details><summary>↩ Tool result · `toolu_016iJdigsePYb2eN85ESTLA4`</summary>

```text
1652--1671
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "b6136595-33eb-4d5a-bcf2-2daae76d628b"
}
```

</details>

---


### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetching https://aclanthology.org/D19-1410/",
  "usage": {
    "total_tokens": 16338,
    "tool_uses": 5,
    "duration_ms": 8896
  },
  "last_tool_name": "WebFetch",
  "uuid": "e5ce7b95-f03e-4b89-9c9c-5c0756c69071",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 80_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XzJzhY68nC1K6TDdJLtjpc`</summary>

```json
{
  "url": "https://aclanthology.org/D19-1410/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "dba92b93-caec-4624-92fe-01aceda19743",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HnZX6Mo6ie9PvFFvEFTqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 81_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a557b1be63bb1d8ca",
  "tool_use_id": "toolu_01KZbgGqCG64PdHot826gzUX",
  "status": "completed",
  "output_file": "",
  "summary": "Fetch ACL pages batch 1",
  "usage": {
    "total_tokens": 17087,
    "tool_uses": 6,
    "duration_ms": 13984
  },
  "uuid": "fc6a54d9-7ba1-4016-8616-a5ba9c756326",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool result

_source line 82 · 2026-05-22T07:31:45.530Z_

<details><summary>↩ Tool result · `toolu_01KZbgGqCG64PdHot826gzUX`</summary>

```text
- llm-pee-2025 = 34377--34399
- parse-2025 = 2749--2763
- crossagentie-2025 = 13953--13977
- gliner2-2025 = 130--140
- dror-2018-significance = 1383--1392

agentId: a557b1be63bb1d8ca (use SendMessage with to: 'a557b1be63bb1d8ca' to continue this agent)
&lt;usage>total_tokens: 17151
tool_uses: 6
duration_ms: 13989&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "1cc98d3e-7720-4a06-89eb-4aae19c235e0",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. llm-pee-2025 → https://aclanthology.org/2025.emnlp-main.1743/\n2. parse-2025 → https://aclanthology.org/2025.emnlp-industry.184/\n3. crossagentie-2025 → https://aclanthology.org/2025.findings-acl.718/\n4. gliner2-2025 → https://aclanthology.org/2025.emnlp-demos.10/\n5. dror-2018-significance → https://aclanthology.org/P18-1128/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\"",
    "agentId": "a557b1be63bb1d8ca",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "- llm-pee-2025 = 34377--34399\n- parse-2025 = 2749--2763\n- crossagentie-2025 = 13953--13977\n- gliner2-2025 = 130--140\n- dror-2018-significance = 1383--1392"
      }
    ],
    "totalDurationMs": 13989,
    "totalTokens": 17151,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 738,
      "cache_read_input_tokens": 16331,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 16331,
          "cache_creation_input_tokens": 738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 738,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  }
}
```

</details>

---


### System

_source line 83_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Search ACL pages batch 4",
  "usage": {
    "total_tokens": 14920,
    "tool_uses": 1,
    "duration_ms": 2915
  },
  "last_tool_name": "ToolSearch",
  "uuid": "ab8d8469-bade-4b80-866d-c87291152def",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 84_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TnCFbWqeBS9ZXhJYsvMjjR`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "7cc0d488-d075-43c5-b176-d67704142c57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013bhF9VvCW73YVS8xaAjf5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6656,
      "cache_read_input_tokens": 8249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6656,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 85 · 2026-05-22T07:31:45.692Z_

<details><summary>↩ Tool result · `toolu_01TnCFbWqeBS9ZXhJYsvMjjR`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

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
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "7debcc26-4cc9-4270-aa6f-0e9396689c07"
}
```

</details>

---


### Tool result

_source line 86 · 2026-05-22T07:31:45.438Z_

<details><summary>↩ Tool result · `toolu_01FvK2NqoLgBbyjS3vSVxJLt`</summary>

```text
764--777
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "462c632b-23df-44c2-bd9c-f7478cc95d02"
}
```

</details>

---


### System

_source line 87_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "description": "Fetching https://aclanthology.org/2023.emnlp-main.493/",
  "usage": {
    "total_tokens": 16340,
    "tool_uses": 6,
    "duration_ms": 9551
  },
  "last_tool_name": "WebFetch",
  "uuid": "20679a63-e4af-4a37-937e-e22007e9a69e",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CgpsKpfyWYmatGoiBDcMdK`</summary>

```json
{
  "url": "https://aclanthology.org/2023.emnlp-main.493/",
  "prompt": "Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "eb4c087a-d138-494d-985f-467484d50630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011HnZX6Mo6ie9PvFFvEFTqm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 14877,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1444,
        "ephemeral_1h_input_tokens": 0
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

_source line 89 · 2026-05-22T07:31:47.002Z_

<details><summary>↩ Tool result · `toolu_01XzJzhY68nC1K6TDdJLtjpc`</summary>

```text
According to the BibTeX citation on this page, the page range is:

**3982--3992**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "ebe846e9-ad15-46fe-8986-fe3391dafa66"
}
```

</details>

---


### Tool result

_source line 90 · 2026-05-22T07:31:47.682Z_

<details><summary>↩ Tool result · `toolu_01CgpsKpfyWYmatGoiBDcMdK`</summary>

```text
7935--7956
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "8ea961d5-4abb-45a0-915e-e6e4bb4e8b1e"
}
```

</details>

---


### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a2d4e0d91d32b7540",
  "tool_use_id": "toolu_01U7XFpuyTLbZMtNpoEDJRTN",
  "status": "completed",
  "output_file": "",
  "summary": "Fetch ACL pages batch 2",
  "usage": {
    "total_tokens": 17099,
    "tool_uses": 6,
    "duration_ms": 14126
  },
  "uuid": "6c98c224-1c2b-4d97-8048-f62e36e46bb5",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool result

_source line 92 · 2026-05-22T07:31:48.035Z_

<details><summary>↩ Tool result · `toolu_01U7XFpuyTLbZMtNpoEDJRTN`</summary>

```text
Results:

1. slot-2025 = 472--491
2. ethayarajh-contextual-2019 = 55--65
3. codeie-2023 = 15339--15353
4. adelie-2024 = 7371--7387
5. fewnerd-2021 = 3198--3213

agentId: a2d4e0d91d32b7540 (use SendMessage with to: 'a2d4e0d91d32b7540' to continue this agent)
&lt;usage>total_tokens: 17170
tool_uses: 6
duration_ms: 14128&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c73da7b1-176e-4ce6-872c-23fbf87b1e77",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. slot-2025 → https://aclanthology.org/2025.emnlp-industry.32/\n2. ethayarajh-contextual-2019 → https://aclanthology.org/D19-1006/\n3. codeie-2023 → https://aclanthology.org/2023.acl-long.855/\n4. adelie-2024 → https://aclanthology.org/2024.emnlp-main.419/\n5. fewnerd-2021 → https://aclanthology.org/2021.acl-long.248/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\"",
    "agentId": "a2d4e0d91d32b7540",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Results:\n\n1. slot-2025 = 472--491\n2. ethayarajh-contextual-2019 = 55--65\n3. codeie-2023 = 15339--15353\n4. adelie-2024 = 7371--7387\n5. fewnerd-2021 = 3198--3213"
      }
    ],
    "totalDurationMs": 14128,
    "totalTokens": 17170,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 16328,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 753
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 16328,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 753,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  }
}
```

</details>

---


### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Searching for site:aclanthology.org \"Familiarity: Better Evalua…",
  "usage": {
    "total_tokens": 16875,
    "tool_uses": 2,
    "duration_ms": 7077
  },
  "last_tool_name": "WebSearch",
  "uuid": "9d81a8e7-c45c-449d-a9a3-7f493303a5a3",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 94_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CYzz36UY4Mod6uHfv1oWZo`</summary>

```json
{
  "query": "site:aclanthology.org \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\"",
  "allowed_domains": [
    "aclanthology.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "06302aea-51ba-478d-842e-199d3afe8cdb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119ZJbpVFLxNRFAqsDmi3XV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 14905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa0a8eab4e6807ba6",
  "tool_use_id": "toolu_01KnTzoQh1p4RBVoPkXVXVAL",
  "status": "completed",
  "output_file": "",
  "summary": "Fetch ACL pages batch 3",
  "usage": {
    "total_tokens": 17105,
    "tool_uses": 6,
    "duration_ms": 13852
  },
  "uuid": "1d807f02-f33a-4024-825d-9b6d2befa893",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool result

_source line 96 · 2026-05-22T07:31:50.280Z_

<details><summary>↩ Tool result · `toolu_01KnTzoQh1p4RBVoPkXVXVAL`</summary>

```text
- fewrel-2018 = 4803--4809
- maven-2020 = 1652--1671
- docred-2019 = 764--777
- sentence-bert-2019 = 3982--3992
- xie-zeroshot-ner-2023 = 7935--7956

agentId: aa0a8eab4e6807ba6 (use SendMessage with to: 'aa0a8eab4e6807ba6' to continue this agent)
&lt;usage>total_tokens: 17171
tool_uses: 6
duration_ms: 13857&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "558918c4-fa71-4e18-aadc-7f2780c7f267",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Fetch the following 5 ACL Anthology URLs and extract the page numbers from each page. Look for \"pages\" or \"pp.\" or a pattern like \"1234--5678\" in the BibTeX or metadata on the page. Return ONLY a simple list: citation_key = pages.\n\n1. fewrel-2018 → https://aclanthology.org/D18-1514/\n2. maven-2020 → https://aclanthology.org/2020.emnlp-main.129/\n3. docred-2019 → https://aclanthology.org/P19-1074/\n4. sentence-bert-2019 → https://aclanthology.org/D19-1410/\n5. xie-zeroshot-ner-2023 → https://aclanthology.org/2023.emnlp-main.493/\n\nFor each URL, use WebFetch with prompt: \"Extract the page numbers (pages field) from the BibTeX citation on this page. Return ONLY the page range like '1234--5678' or 'not found'.\"",
    "agentId": "aa0a8eab4e6807ba6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "- fewrel-2018 = 4803--4809\n- maven-2020 = 1652--1671\n- docred-2019 = 764--777\n- sentence-bert-2019 = 3982--3992\n- xie-zeroshot-ner-2023 = 7935--7956"
      }
    ],
    "totalDurationMs": 13857,
    "totalTokens": 17171,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 766,
      "cache_read_input_tokens": 16321,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 766
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 83,
          "cache_read_input_tokens": 16321,
          "cache_creation_input_tokens": 766,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 766,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  }
}
```

</details>

---


### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Searching for site:aclanthology.org \"The Ecological Fallacy in …",
  "usage": {
    "total_tokens": 16877,
    "tool_uses": 3,
    "duration_ms": 7557
  },
  "last_tool_name": "WebSearch",
  "uuid": "2e5d3a17-6db2-4bb3-936e-4b7550708ed3",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 98_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SE4Kaghmk1Y9aDf5omw7yc`</summary>

```json
{
  "query": "site:aclanthology.org \"The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics\"",
  "allowed_domains": [
    "aclanthology.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "247ddc18-f0ca-41bf-aeac-ddd0a1c26029",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119ZJbpVFLxNRFAqsDmi3XV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 14905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Searching for site:aclanthology.org \"GLiNER: Generalist Model f…",
  "usage": {
    "total_tokens": 16879,
    "tool_uses": 4,
    "duration_ms": 8607
  },
  "last_tool_name": "WebSearch",
  "uuid": "ce8d2038-40a8-496b-a7e1-73f13f0728f2",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 100_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012NPEmhheketKKbPyBTrJd9`</summary>

```json
{
  "query": "site:aclanthology.org \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\"",
  "allowed_domains": [
    "aclanthology.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c2de8ff4-2925-4b35-a7cb-acd4c75dd01b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119ZJbpVFLxNRFAqsDmi3XV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 14905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
        "ephemeral_1h_input_tokens": 0
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


### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Searching for site:aclanthology.org \"KnowCoder: Coding Structur…",
  "usage": {
    "total_tokens": 16881,
    "tool_uses": 5,
    "duration_ms": 8775
  },
  "last_tool_name": "WebSearch",
  "uuid": "ba68be99-57b3-4b19-91d8-2532e0289c6b",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WtRfRUKQu6FFj5rFrmwt2e`</summary>

```json
{
  "query": "site:aclanthology.org \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\"",
  "allowed_domains": [
    "aclanthology.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "9a9a787b-8983-496d-8cc9-99076ec18f50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119ZJbpVFLxNRFAqsDmi3XV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1951,
      "cache_read_input_tokens": 14905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1951,
        "ephemeral_1h_input_tokens": 0
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

_source line 103 · 2026-05-22T07:31:55.533Z_

<details><summary>↩ Tool result · `toolu_01CYzz36UY4Mod6uHfv1oWZo`</summary>

```text
Web search results for query: "site:aclanthology.org "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data""

Links: [{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by   Quantifying Label Shifts in Synthetic Training Data","url":"https://arxiv.org/pdf/2412.10121"},{"title":"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.37/"},{"title":"GuideX: Guided Synthetic Data Generation for Zero-Shot Information Extraction","url":"https://arxiv.org/pdf/2506.00649"},{"title":"Zero-Shot Learning in Named-Entity Recognition with External Knowledge","url":"https://arxiv.org/pdf/2111.07734"},{"title":"GLiNER-BioMed: A Suite of Efficient Models for Open Biomedical Named Entity Recognition","url":"https://arxiv.org/pdf/2504.00676"}]

The search found the paper! The paper "Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data" was published by Jonas Golde, Patrick Haller, Max Ploner, Fabio Barth, Nicolaas Jedema, and Alan Akbik in the Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics (NAACL 2025), pages 820–834.

The paper proposes FAMILIARITY, a novel metric that captures both the semantic similarity between entity types in training and evaluation, as well as their frequency in the training data, to provide an estimate of label shift. The research found that synthetic datasets used for zero-shot NER often contain entity types that are semantically highly similar to those in standard evaluation benchmarks, which causes reported F1 scores to overestimate the true capabilities of these approaches.

The paper is available at: https://aclanthology.org/2025.naacl-long.37/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c937c1a9-4b63-40c6-91a3-f4a5b0315684"
}
```

</details>

---


### Tool result

_source line 104 · 2026-05-22T07:31:55.747Z_

<details><summary>↩ Tool result · `toolu_01SE4Kaghmk1Y9aDf5omw7yc`</summary>

```text
Web search results for query: "site:aclanthology.org "The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics""

Links: [{"title":"The Ecological Fallacy in Annotation: Modelling Human Label Variation   goes beyond Sociodemographics","url":"https://arxiv.org/pdf/2306.11559"},{"title":"The Ecological Fallacy in Annotation: Modelling Human ...","url":"https://aclanthology.org/2023.acl-short.88.pdf"},{"title":"Beyond Demographics: Fine-tuning Large Language Models to Predict   Individuals' Subjective Text Perceptions","url":"https://arxiv.org/pdf/2502.20897"},{"title":"The 'Problem' of Human Label Variation: On Ground Truth in Data,   Modeling and Evaluation","url":"https://arxiv.org/pdf/2211.02570"},{"title":"Fine-grained Fallacy Detection with Human Label Variation","url":"https://arxiv.org/pdf/2502.13853"}]

I found the paper! The paper is titled "The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics" by Matthias Orlikowski, Paul Röttger, Philipp Cimiano, and Dirk Hovy from Bielefeld University, University of Oxford, and Bocconi University.

The paper addresses human label variation in NLP tasks, where different annotators give different labels to the same texts, with this variation known to depend at least in part on the sociodemographics of annotators. The authors introduce group-specific layers to multi-annotator models to account for sociodemographic attributes, but find that explicitly accounting for sociodemographic attributes in this way does not significantly improve model performance. Their findings show that individual annotation behaviour depends on much more than just sociodemographics.

The paper is available on ACL Anthology at: https://aclanthology.org/2023.acl-short.88.pdf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c7ff0b10-43c1-4001-a2ea-48118989ad92"
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-22T07:31:56.856Z_

<details><summary>↩ Tool result · `toolu_012NPEmhheketKKbPyBTrJd9`</summary>

```text
Web search results for query: "site:aclanthology.org "GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer""

Links: [{"title":"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.300/"},{"title":"GLiNER: Generalist Model for Named Entity Recognition using   Bidirectional Transformer","url":"https://arxiv.org/pdf/2311.08526"},{"title":"&lt;modsCollection xmlns=\"http://www.loc.gov/mods/v3\">","url":"https://aclanthology.org/2024.naacl-long.300.xml"},{"title":"GLiNER-BioMed: A Suite of Efficient Models for Open Biomedical Named Entity Recognition","url":"https://arxiv.org/pdf/2504.00676"},{"title":"GLiNER multi-task: Generalist Lightweight Model for Various Information   Extraction Tasks","url":"https://arxiv.org/pdf/2406.12925"}]

I found the paper! Here are the search results:

The paper "GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer" was authored by Urchade Zaratiana, Nadi Tomeh, Pierre Holat, and Thierry Charnois and published in 2024.

It appears in the Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers).

The paper introduces a compact NER model trained to identify any type of entity. Leveraging a bidirectional transformer encoder, GLiNER facilitates parallel entity extraction, an advantage over the slow sequential token generation of LLMs. Through comprehensive testing, GLiNER demonstrates strong performance, outperforming both ChatGPT and fine-tuned LLMs in zero-shot evaluations on various NER benchmarks.

The paper is available at: https://aclanthology.org/2024.naacl-long.300/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "af614ed6-dc2b-4b6e-bc6d-062296c6a46d"
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-22T07:31:57.930Z_

<details><summary>↩ Tool result · `toolu_01WtRfRUKQu6FFj5rFrmwt2e`</summary>

```text
Web search results for query: "site:aclanthology.org "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction""

Links: [{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal   Information Extraction","url":"https://arxiv.org/pdf/2403.07969"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.475/"},{"title":"RUIE: Retrieval-based Unified Information Extraction using ...","url":"https://aclanthology.org/2025.coling-main.645.pdf"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"KnowCoder: Coding Structured Knowledge into LLMs for ...","url":"https://aclanthology.org/2024.acl-long.475.pdf"}]

I found the paper you're looking for on the ACL Anthology. The paper "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction" by Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, and Xueqi Cheng was published in 2024 in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8758–8779, Bangkok, Thailand.

The paper is available at: https://aclanthology.org/2024.acl-long.475/

KnowCoder is a Large Language Model designed to conduct Universal Information Extraction via code generation. It introduces a code-style schema representation method to uniformly transform different schemas into Python classes, with which complex schema information can be captured in an LLM-friendly manner.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "8cad0015-7755-4a9d-a288-1ec73e252b6a"
}
```

</details>

---


### System

_source line 107_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Fetching https://aclanthology.org/2025.naacl-long.37/",
  "usage": {
    "total_tokens": 19514,
    "tool_uses": 6,
    "duration_ms": 19150
  },
  "last_tool_name": "WebFetch",
  "uuid": "0f5c7312-f9ab-4f48-a9f6-0c96aa0ef13d",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016yY5jN7Jd5Zs4BXaSwrHLa`</summary>

```json
{
  "url": "https://aclanthology.org/2025.naacl-long.37/",
  "prompt": "Find the BibTeX entry on this page. Extract ONLY the \"pages\" field value from the BibTeX. Return it exactly as it appears (e.g. \"820--834\")."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "516e3bcd-af2c-4be0-85ad-9535574dea24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RepkSBtxfXee3ZGTtJjeQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2633,
      "cache_read_input_tokens": 16856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2633,
        "ephemeral_1h_input_tokens": 0
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

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Fetching https://aclanthology.org/2023.acl-short.88/",
  "usage": {
    "total_tokens": 19515,
    "tool_uses": 7,
    "duration_ms": 20092
  },
  "last_tool_name": "WebFetch",
  "uuid": "66edff80-1042-4f70-84e9-09fd0911be5f",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V1y6ETAmphH5rexQVRciHE`</summary>

```json
{
  "url": "https://aclanthology.org/2023.acl-short.88/",
  "prompt": "Find the BibTeX entry on this page. Extract ONLY the \"pages\" field value from the BibTeX. Return it exactly as it appears (e.g. \"1023--1035\")."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "abcda28c-78ea-474f-ba39-dad5b7be0709",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RepkSBtxfXee3ZGTtJjeQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2633,
      "cache_read_input_tokens": 16856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2633,
        "ephemeral_1h_input_tokens": 0
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

_source line 111 · 2026-05-22T07:32:03.424Z_

<details><summary>↩ Tool result · `toolu_016yY5jN7Jd5Zs4BXaSwrHLa`</summary>

```text
The "pages" field value from the BibTeX entry is:

**820--834**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "afaa1ff1-e630-43ae-80be-221c177ce1d3"
}
```

</details>

---


### System

_source line 112_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Fetching https://aclanthology.org/2024.naacl-long.300/",
  "usage": {
    "total_tokens": 19516,
    "tool_uses": 8,
    "duration_ms": 21032
  },
  "last_tool_name": "WebFetch",
  "uuid": "56ff005d-30e7-4334-bc54-c35cf3a0bcf4",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 113_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Vmjq5TVZWUSqd3yBLEXDSH`</summary>

```json
{
  "url": "https://aclanthology.org/2024.naacl-long.300/",
  "prompt": "Find the BibTeX entry on this page. Extract ONLY the \"pages\" field value from the BibTeX. Return it exactly as it appears (e.g. \"1023--1035\")."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c35664bf-3722-4c7b-a8f3-f6ef6d7bf79b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RepkSBtxfXee3ZGTtJjeQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2633,
      "cache_read_input_tokens": 16856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2633,
        "ephemeral_1h_input_tokens": 0
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

_source line 114_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "description": "Fetching https://aclanthology.org/2024.acl-long.475/",
  "usage": {
    "total_tokens": 19517,
    "tool_uses": 9,
    "duration_ms": 21538
  },
  "last_tool_name": "WebFetch",
  "uuid": "8901ddfb-d118-4660-a0fc-51715fd25d0a",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool call

_source line 115_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017YQsYKC3bDCkTV6CfJYpmb`</summary>

```json
{
  "url": "https://aclanthology.org/2024.acl-long.475/",
  "prompt": "Find the BibTeX entry on this page. Extract ONLY the \"pages\" field value from the BibTeX. Return it exactly as it appears (e.g. \"8758--8779\")."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "af05206d-4449-4475-961e-a2152accf9b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RepkSBtxfXee3ZGTtJjeQZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2633,
      "cache_read_input_tokens": 16856,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2633,
        "ephemeral_1h_input_tokens": 0
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

_source line 116 · 2026-05-22T07:32:04.764Z_

<details><summary>↩ Tool result · `toolu_01V1y6ETAmphH5rexQVRciHE`</summary>

```text
The pages field value from the BibTeX entry is:

**1017--1029**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "fc7af913-111d-4780-8722-53759fc8dcf2"
}
```

</details>

---


### Tool result

_source line 117 · 2026-05-22T07:32:04.869Z_

<details><summary>↩ Tool result · `toolu_01Vmjq5TVZWUSqd3yBLEXDSH`</summary>

````text
The "pages" field value from the BibTeX entry is:

```
5364--5376
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "8731fb4b-950c-4fe2-a064-599a3961bb5f"
}
```

</details>

---


### Tool result

_source line 118 · 2026-05-22T07:32:05.781Z_

<details><summary>↩ Tool result · `toolu_017YQsYKC3bDCkTV6CfJYpmb`</summary>

````text
The "pages" field value from the BibTeX entry is:

```
8758--8779
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "ad8197dc-fba7-4255-8487-4e443cd89652"
}
```

</details>

---


### System

_source line 119_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a3fb8ef0e51262cb9",
  "tool_use_id": "toolu_01CRCMF1zzQTAi42oLZYKbTc",
  "status": "completed",
  "output_file": "",
  "summary": "Search ACL pages batch 4",
  "usage": {
    "total_tokens": 20316,
    "tool_uses": 9,
    "duration_ms": 26079
  },
  "uuid": "dc1c5788-dcf8-4361-839b-c5cb61ba4dd9",
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae"
}
```

---


### Tool result

_source line 120 · 2026-05-22T07:32:08.855Z_

<details><summary>↩ Tool result · `toolu_01CRCMF1zzQTAi42oLZYKbTc`</summary>

```text
Results:

1. `golde-2025-familiarity` = pages 820--834
2. `baan-2023-ecological` = pages 1017--1029
3. `gliner-2024` = pages 5364--5376
4. `knowcoder-2024` = pages 8758--8779

agentId: a3fb8ef0e51262cb9 (use SendMessage with to: 'a3fb8ef0e51262cb9' to continue this agent)
&lt;usage>total_tokens: 20370
tool_uses: 9
duration_ms: 26081&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e8e749eb-e5ec-428e-a65c-33f0d3dd4698",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for page numbers of these 4 ACL Anthology papers that don't have direct URLs. For each, search on aclanthology.org, then fetch the page to get the pages field from the BibTeX.\n\n1. golde-2025-familiarity: \"Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data\" (NAACL 2025)\n2. baan-2023-ecological: \"The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics\" (ACL 2023)\n3. gliner-2024: \"GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer\" (NAACL 2024)\n4. knowcoder-2024: \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\" (ACL 2024)\n\nFor each paper:\n- Use WebSearch with query: site:aclanthology.org \"paper title\" \n- Then use WebFetch on the ACL Anthology URL to extract the pages field from the BibTeX\n- Return ONLY: citation_key = pages (or \"not found\")",
    "agentId": "a3fb8ef0e51262cb9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Results:\n\n1. `golde-2025-familiarity` = pages 820--834\n2. `baan-2023-ecological` = pages 1017--1029\n3. `gliner-2024` = pages 5364--5376\n4. `knowcoder-2024` = pages 8758--8779"
      }
    ],
    "totalDurationMs": 26081,
    "totalTokens": 20370,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 19489,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 798
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 19489,
          "cache_creation_input_tokens": 798,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 798,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  }
}
```

</details>

---


### Assistant

_source line 121_

<details><summary>Logged reasoning block</summary>

```text
All 19 ACL Anthology entries have been found. Now I need to add the pages field to each entry in the bib file. Let me do the edits.

Here are all 19 entries with pages:

1. golde-2025-familiarity = 820--834
2. baan-2023-ecological = 1017--1029
3. llm-pee-2025 = 34377--34399
4. parse-2025 = 2749--2763
5. crossagentie-2025 = 13953--13977


6. gliner-2024 = 5364--5376
7. gliner2-2025 = 130--140
8. dror-2018-significance = 1383--1392
9. knowcoder-2024 = 8758--8779
10. slot-2025 = 472--491
11. ethayarajh-contextual-2019 = 55--65
12. codeie-2023 = 15339--15353
13. adelie-2024 = 7371--7387
14. fewnerd-2021 = 3198--3213
15. fewrel-2018 = 4803--4809
16. maven-2020 = 1652--1671
17. docred-2019 = 764--777
18. sentence-bert-2019 = 3982--3992
19. xie-zeroshot-ner-2023 = 7935--7956

Now I need to add the pages field to each entry. I'll insert `pages = "xxx--yyy",` before the year line for consistency across all entries.

I'll batch these edits together to handle multiple entries in parallel, making sure each one has a unique identifier so I can target the right location for the insertion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "815038a1-f78c-4577-a70d-ae16b2ca7853",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 122_

全部 19 个 ACL Anthology 条目的页码都找到了。现在批量添加 pages 字段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "d4a4ff7a-fda2-404b-8cde-a4291b255783",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 123_

<details open><summary>🔧 Tool call — Edit · `toolu_01KNN11vSTf8yz1HKgcxWfPy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}",
  "new_string": "  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "61d6f94d-eb2c-4ed1-8e0d-1ffbdc341b49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 124 · 2026-05-22T07:32:22.984Z_

<details><summary>↩ Tool result · `toolu_01KNN11vSTf8yz1HKgcxWfPy`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "bf20a10a-ed7c-4e47-be21-5da6adad9e66",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}",
    "newString": "  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 6,
        "newStart": 2,
        "newLines": 7,
        "lines": [
          "   title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},",
          "   author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},",
          "   booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},",
          "+  pages     = {820--834},",
          "   year      = {2025},",
          "   url       = {https://arxiv.org/abs/2412.10121}",
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

_source line 125_

<details open><summary>🔧 Tool call — Edit · `toolu_01Bo1tehSJU6XPSvZDNcoikc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}",
  "new_string": "  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "895e6279-1c0c-4fd3-836a-504d110447d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 126 · 2026-05-22T07:32:24.315Z_

<details><summary>↩ Tool result · `toolu_01Bo1tehSJU6XPSvZDNcoikc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "b718a1f2-4d63-4be8-895f-5961f1133c2f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}",
    "newString": "  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 6,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          "   author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},",
          "   title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},",
          "   booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},",
          "+  pages     = {1017--1029},",
          "   year      = {2023}",
          " }",
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


### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Edit · `toolu_016ooC3j8FPFcFvGYfgpKTjQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "ddb880ae-25f2-416e-9c1e-324b2067c2f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 128 · 2026-05-22T07:32:26.623Z_

<details><summary>↩ Tool result · `toolu_016ooC3j8FPFcFvGYfgpKTjQ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "f3f234cd-dc62-4b2e-9b9f-464fd11cbf12",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}",
    "newString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 117,
        "oldLines": 6,
        "newStart": 117,
        "newLines": 7,
        "lines": [
          "     title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},",
          "     author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},",
          "     booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages     = {34377--34399},",
          "     year      = {2025},",
          "     url       = {https://aclanthology.org/2025.emnlp-main.1743/},",
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

_source line 129_

<details open><summary>🔧 Tool call — Edit · `toolu_01F5B5uju9yw14L3vZ8tiTbf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "17272629-0d58-4614-8032-c6fde7723751",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 130 · 2026-05-22T07:32:28.432Z_

<details><summary>↩ Tool result · `toolu_01F5B5uju9yw14L3vZ8tiTbf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "4c45db7b-bb00-4cc2-8cfe-1dfed2ca339f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}",
    "newString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 126,
        "oldLines": 6,
        "newStart": 126,
        "newLines": 7,
        "lines": [
          "     title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},",
          "     author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},",
          "     booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},",
          "+    pages     = {2749--2763},",
          "     year      = {2025},",
          "     url       = {https://aclanthology.org/2025.emnlp-industry.184/},",
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

_source line 131_

<details open><summary>🔧 Tool call — Edit · `toolu_01X6BgDmGJ9Yb6XgnKA2cqkA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}",
  "new_string": "    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c9739e1f-4b7f-40bc-8aec-dc4c7b3764a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 132 · 2026-05-22T07:32:30.469Z_

<details><summary>↩ Tool result · `toolu_01X6BgDmGJ9Yb6XgnKA2cqkA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "48922935-d617-4b7c-9823-550f2d242be6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}",
    "newString": "    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 135,
        "oldLines": 6,
        "newStart": 135,
        "newLines": 7,
        "lines": [
          "     title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},",
          "     author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},",
          "     booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},",
          "+    pages     = {13953--13977},",
          "     year      = {2025},",
          "     url       = {https://aclanthology.org/2025.findings-acl.718/},",
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

_source line 133_

<details open><summary>🔧 Tool call — Edit · `toolu_01D8FActQTaqPBxm7nBMm4Qc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}",
  "new_string": "    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "fa2b2117-2403-4ca3-83cb-8657c9dcff43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 134 · 2026-05-22T07:32:32.327Z_

<details><summary>↩ Tool result · `toolu_01D8FActQTaqPBxm7nBMm4Qc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c89ce23c-6176-44b9-b12c-482bbbac6012",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}",
    "newString": "    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 174,
        "oldLines": 6,
        "newStart": 174,
        "newLines": 7,
        "lines": [
          "     title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},",
          "     author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},",
          "     booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},",
          "+    pages     = {5364--5376},",
          "     year      = {2024},",
          "     url       = {https://arxiv.org/abs/2311.08526},",
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

_source line 135_

<details open><summary>🔧 Tool call — Edit · `toolu_01AJkuL36fpa6F9mxephpyp1`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "9603980d-849e-4ba0-8569-7ef1fba8e339",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 136 · 2026-05-22T07:32:34.262Z_

<details><summary>↩ Tool result · `toolu_01AJkuL36fpa6F9mxephpyp1`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e14b828e-b855-4fa6-801c-8eddf2362dfc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}",
    "newString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 183,
        "oldLines": 6,
        "newStart": 183,
        "newLines": 7,
        "lines": [
          "     title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},",
          "     author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},",
          "     booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},",
          "+    pages     = {130--140},",
          "     year      = {2025},",
          "     url       = {https://aclanthology.org/2025.emnlp-demos.10/},",
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

_source line 137_

<details open><summary>🔧 Tool call — Edit · `toolu_018tjoiFivrXXjf1najxU6KB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}",
  "new_string": "    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "5103dbb3-c8e9-4eff-a8bd-65fae7612a7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 138 · 2026-05-22T07:32:36.118Z_

<details><summary>↩ Tool result · `toolu_018tjoiFivrXXjf1najxU6KB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "6c9908ea-fc41-46f8-91c6-4b82cbac6e5b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}",
    "newString": "    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 203,
        "oldLines": 6,
        "newStart": 203,
        "newLines": 7,
        "lines": [
          "     title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},",
          "     author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},",
          "     booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},",
          "+    pages     = {1383--1392},",
          "     year      = {2018},",
          "     url       = {https://aclanthology.org/P18-1128/},",
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

_source line 139_

<details open><summary>🔧 Tool call — Edit · `toolu_01Qx93dfgYuDTjAnxy7ybSEa`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}",
  "new_string": "    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "921d76c9-c62f-4fd8-8c97-501241706485",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J1ae2G8YnJXkF6UsHvoAYK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3190,
      "cache_read_input_tokens": 38305,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3190
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

_source line 140 · 2026-05-22T07:32:37.728Z_

<details><summary>↩ Tool result · `toolu_01Qx93dfgYuDTjAnxy7ybSEa`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "f64238d1-cdb8-45e9-8624-5b1fc54ac5a0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}",
    "newString": "    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 256,
        "oldLines": 6,
        "newStart": 256,
        "newLines": 7,
        "lines": [
          "     title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},",
          "     author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},",
          "     booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},",
          "+    pages     = {8758--8779},",
          "     year      = {2024},",
          "     url       = {https://arxiv.org/abs/2403.07969},",
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

_source line 141_

<details open><summary>🔧 Tool call — Edit · `toolu_01VJN79bn4r7TbpHH1PYCD8F`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "e1e12e7b-57ee-451e-b46c-fcb61a1e2672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 142 · 2026-05-22T07:32:41.893Z_

<details><summary>↩ Tool result · `toolu_01VJN79bn4r7TbpHH1PYCD8F`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "69c140d8-701b-4ea0-99ee-b00c1736d98b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}",
    "newString": "    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 265,
        "oldLines": 6,
        "newStart": 265,
        "newLines": 7,
        "lines": [
          "     title     = {{SLOT}: Structuring the Output of Large Language Models},",
          "     author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},",
          "     booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},",
          "+    pages     = {472--491},",
          "     year      = {2025},",
          "     url       = {https://aclanthology.org/2025.emnlp-industry.32/},",
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

_source line 143_

<details open><summary>🔧 Tool call — Edit · `toolu_01NWfmYFhkD63NQMBRPpijoB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "01301282-ab40-4dca-a249-92b53e849c66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 144 · 2026-05-22T07:32:44.299Z_

<details><summary>↩ Tool result · `toolu_01NWfmYFhkD63NQMBRPpijoB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "01df4d0b-7a33-4fd5-840a-8d541658da50",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}",
    "newString": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 279,
        "oldLines": 6,
        "newStart": 279,
        "newLines": 7,
        "lines": [
          "     title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},",
          "     author    = {Ethayarajh, Kawin},",
          "     booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},",
          "+    pages     = {55--65},",
          "     year      = {2019},",
          "     url       = {https://aclanthology.org/D19-1006/},",
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

_source line 145_

<details open><summary>🔧 Tool call — Edit · `toolu_01B5wCYWBiqgViXtXz1WaGXP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}",
  "new_string": "    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "c4e76e34-f25a-4fe9-87aa-72c11ed80d53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 146 · 2026-05-22T07:32:46.140Z_

<details><summary>↩ Tool result · `toolu_01B5wCYWBiqgViXtXz1WaGXP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "d125b416-0942-4c7a-8dd5-8099abed3b63",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}",
    "newString": "    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 309,
        "oldLines": 6,
        "newStart": 309,
        "newLines": 7,
        "lines": [
          "     title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},",
          "     author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},",
          "     booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},",
          "+    pages     = {15339--15353},",
          "     year      = {2023},",
          "     url       = {https://aclanthology.org/2023.acl-long.855/},",
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

_source line 147_

<details open><summary>🔧 Tool call — Edit · `toolu_01VDMfznMXwpsTVmc7y15xZx`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "27a86ade-f2e9-4eaa-a430-47182084fcff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 148 · 2026-05-22T07:32:48.561Z_

<details><summary>↩ Tool result · `toolu_01VDMfznMXwpsTVmc7y15xZx`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "8963190c-9bd6-43b7-9355-ec646e1c9cea",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}",
    "newString": "    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 318,
        "oldLines": 6,
        "newStart": 318,
        "newLines": 7,
        "lines": [
          "     title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},",
          "     author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},",
          "     booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages     = {7371--7387},",
          "     year      = {2024},",
          "     url       = {https://aclanthology.org/2024.emnlp-main.419/},",
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

_source line 149_

<details open><summary>🔧 Tool call — Edit · `toolu_01MPvNXa3kpVmWXKFg9XGF9m`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}",
  "new_string": "    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {3198--3213},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "68e8c676-82a7-465e-8f31-de06c7867c38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 150 · 2026-05-22T07:32:50.412Z_

<details><summary>↩ Tool result · `toolu_01MPvNXa3kpVmWXKFg9XGF9m`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "07971100-e6d6-4e2b-ab69-ed07c2a60d9d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}",
    "newString": "    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {3198--3213},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 343,
        "oldLines": 6,
        "newStart": 343,
        "newLines": 7,
        "lines": [
          "     title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},",
          "     author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},",
          "     booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},",
          "+    pages     = {3198--3213},",
          "     year      = {2021},",
          "     url       = {https://aclanthology.org/2021.acl-long.248/},",
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

_source line 151_

<details open><summary>🔧 Tool call — Edit · `toolu_01Kg92dVHfXEdhKPqqjdBihz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {4803--4809},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "64c558ce-6fed-4293-a8d2-76247f024e57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 152 · 2026-05-22T07:32:52.850Z_

<details><summary>↩ Tool result · `toolu_01Kg92dVHfXEdhKPqqjdBihz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "9c11634c-7421-47d8-b1bf-28df6eeb840f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}",
    "newString": "    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {4803--4809},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {3198--3213},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 352,
        "oldLines": 6,
        "newStart": 352,
        "newLines": 7,
        "lines": [
          "     title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},",
          "     author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},",
          "     booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages     = {4803--4809},",
          "     year      = {2018},",
          "     url       = {https://aclanthology.org/D18-1514/},",
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

_source line 153_

<details open><summary>🔧 Tool call — Edit · `toolu_014gNuR1nPa9xR5fWUb3iKUG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {1652--1671},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "427d4d33-1e46-47c8-97bb-913f3ea8cafe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 154 · 2026-05-22T07:32:54.682Z_

<details><summary>↩ Tool result · `toolu_014gNuR1nPa9xR5fWUb3iKUG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "9adcfff4-51ff-44a8-9c3b-a08ca0138f03",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}",
    "newString": "    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {1652--1671},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {3198--3213},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {4803--4809},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 361,
        "oldLines": 6,
        "newStart": 361,
        "newLines": 7,
        "lines": [
          "     title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},",
          "     author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},",
          "     booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages     = {1652--1671},",
          "     year      = {2020},",
          "     url       = {https://aclanthology.org/2020.emnlp-main.129/},",
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

_source line 155_

<details open><summary>🔧 Tool call — Edit · `toolu_01HqZkPbYAqGfgFqT31W32qC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}",
  "new_string": "    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {764--777},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "7e8b2873-1b7f-4b87-9fc3-e5e759117727",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 156 · 2026-05-22T07:32:56.547Z_

<details><summary>↩ Tool result · `toolu_01HqZkPbYAqGfgFqT31W32qC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "0e651013-46e4-47dc-b791-9367d20bf170",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}",
    "newString": "    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {764--777},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {3198--3213},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {4803--4809},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {1652--1671},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 370,
        "oldLines": 6,
        "newStart": 370,
        "newLines": 7,
        "lines": [
          "     title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},",
          "     author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},",
          "     booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},",
          "+    pages     = {764--777},",
          "     year      = {2019},",
          "     url       = {https://aclanthology.org/P19-1074/},",
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

_source line 157_

<details open><summary>🔧 Tool call — Edit · `toolu_01G61uWBcgsQxoU7JWxsoC2p`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {3982--3992},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "d138d1fd-c5a4-44b8-aa73-288eb3344ee4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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

_source line 158 · 2026-05-22T07:32:58.411Z_

<details><summary>↩ Tool result · `toolu_01G61uWBcgsQxoU7JWxsoC2p`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "da969c8b-80e2-4e2c-88ee-8918c884a0f9",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
    "oldString": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}",
    "newString": "    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {3982--3992},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}",
    "originalFile": "@inproceedings{golde-2025-familiarity,\n  title     = {Familiarity: Better Evaluation of Zero-Shot Named Entity Recognition by Quantifying Label Shifts in Synthetic Training Data},\n  author    = {Golde, Jonas and Haller, Patrick and Ploner, Max and Barth, Fabio and Jedema, Nicolaas and Akbik, Alan},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  pages     = {820--834},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2412.10121}\n}\n\n@book{cohen-1988-statistical,\n  author    = {Cohen, Jacob},\n  title     = {Statistical Power Analysis for the Behavioral Sciences},\n  edition   = {2nd},\n  publisher = {Lawrence Erlbaum Associates},\n  year      = {1988}\n}\n\n@inproceedings{baan-2023-ecological,\n  author    = {Baan, Joris and Plank, Barbara and Fernandez, Raquel},\n  title     = {The Ecological Fallacy in Annotation: Modelling Human Label Variation goes beyond Sociodemographics},\n  booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL)},\n  pages     = {1017--1029},\n  year      = {2023}\n}\n\n@inproceedings{josifoski-2022-genie,\n  author    = {Josifoski, Martin and De Cao, Nicola and Peyrard, Maxime and Petroni, Fabio and West, Robert},\n  title     = {{GenIE}: Generative Information Extraction},\n  booktitle = {Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL)},\n  pages     = {4626--4643},\n  year      = {2022}\n}\n\n@inproceedings{dubey-2018-pairwise-confusion,\n  author    = {Dubey, Abhimanyu and Gupta, Otkrist and Guo, Pei and Raskar, Ramesh and Farrell, Ryan and Naik, Nikhil},\n  title     = {Pairwise Confusion for Fine-Grained Visual Classification},\n  booktitle = {Proceedings of the European Conference on Computer Vision (ECCV)},\n  pages     = {71--88},\n  year      = {2018}\n}\n\n@inproceedings{collier-2021-correlated-noise,\n  author    = {Collier, Mark and Mustafa, Basil and Kokiopoulou, Efi and Jenatton, Rodolphe and Berent, Jesse},\n  title     = {Correlated Input-Dependent Label Noise in Large-Scale Image Classification},\n  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  pages     = {1551--1560},\n  year      = {2021}\n}\n\n@inproceedings{yin-2019-zero-shot-bench,\n  title     = {Benchmarking Zero-shot Text Classification: Datasets, Evaluation and Entailment Approach},\n  author    = {Yin, Wenpeng and Hay, Jamaal and Roth, Dan},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n  pages     = {3914--3923},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1909.00161}\n}\n\n@article{schuirmann-1987-tost,\n  title     = {A Comparison of the Two One-Sided Tests Procedure and the Power Approach for Assessing the Equivalence of Average Bioavailability},\n  author    = {Schuirmann, Donald J.},\n  journal   = {Journal of Pharmacokinetics and Biopharmaceutics},\n  volume    = {15},\n  number    = {6},\n  pages     = {657--680},\n  year      = {1987},\n  doi       = {10.1007/BF01068419}\n}\n\n@article{gemini-2025,\n  title     = {Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, and Long Context},\n  author    = {{Gemini Team}},\n  journal   = {arXiv preprint arXiv:2507.06261},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2507.06261}\n}\n\n@inproceedings{snell2017prototypical,\n  title     = {Prototypical Networks for Few-shot Learning},\n  author    = {Snell, Jake and Swersky, Kevin and Zemel, Richard},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {30},\n  year      = {2017}\n}\n\n@inproceedings{muller2019when,\n  title     = {When Does Label Smoothing Help?},\n  author    = {M{\\\"u}ller, Rafael and Kornblith, Simon and Hinton, Geoffrey E.},\n  booktitle = {Advances in Neural Information Processing Systems},\n  volume    = {32},\n  year      = {2019}\n}\n\n@inproceedings{peterson2019human,\n  title     = {Human Uncertainty Makes Classification More Robust},\n  author    = {Peterson, Joshua C. and Battleday, Ruairidh M. and Griffiths, Thomas L. and Russakovsky, Olga},\n  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision},\n  pages     = {9617--9626},\n  year      = {2019}\n}\n\n@article{willard2023efficient,\n  title     = {Efficient Guided Generation for Large Language Models},\n  author    = {Willard, Brandon T. and Louf, R{\\'e}mi},\n  journal   = {arXiv preprint arXiv:2307.09702},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2307.09702}\n}\n\n\n\n% =============================================================================\n% DIRECT COMPETITORS\n% =============================================================================\n\n@inproceedings{llm-pee-2025,\n    title     = {Towards Event Extraction with Massive Types: {LLM}-based Collaborative Annotation and Partitioning Extraction},\n    author    = {Liu, Wenxuan and Li, Zixuan and Bai, Long and Zuo, Yuxin and Xu, Daozhu and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {34377--34399},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-main.1743/},\n}\n\n@inproceedings{parse-2025,\n    title     = {{PARSE}: {LLM} Driven Schema Optimization for Reliable Entity Extraction},\n    author    = {Shrimal, Anubhav and Jain, Aryan and Chowdhury, Soumyajit and Yenigalla, Promod},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {2749--2763},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.184/},\n}\n\n@inproceedings{crossagentie-2025,\n    title     = {{CROSSAGENTIE}: Cross-Type and Cross-Task Multi-Agent {LLM} Collaboration for Zero-Shot Information Extraction},\n    author    = {Lu, Meng and Xie, Yuzhang and Bi, Zhenyu and Cao, Shuxiang and Wang, Xuan},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    pages     = {13953--13977},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.findings-acl.718/},\n}\n\n\n@inproceedings{cmas-ner-2025,\n    title     = {A Cooperative Multi-Agent Framework for Zero-Shot Named Entity Recognition},\n    author    = {Wang, Zihan and Zhao, Ziqi and Lyu, Yougang and Chen, Zhumin and de Rijke, Maarten and Ren, Zhaochun},\n    booktitle = {Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://dl.acm.org/doi/10.1145/3696410.3714923},\n    doi       = {10.1145/3696410.3714923},\n}\n\n% =============================================================================\n% METHOD COMPONENTS\n% =============================================================================\n\n@inproceedings{uniner-2024,\n    title     = {{UniversalNER}: Targeted Distillation from Large Language Models for Open Named Entity Recognition},\n    author    = {Zhou, Wenxuan and Zhang, Sheng and Gu, Yu and Chen, Muhao and Poon, Hoifung},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2308.03279},\n}\n\n@inproceedings{gollie-2024,\n    title     = {{GoLLIE}: Annotation Guidelines improve Zero-Shot Information-Extraction},\n    author    = {Sainz, Oscar and Garc{\\'\\i}a-Ferrero, Iker and Agerri, Rodrigo and Lopez de Lacalle, Oier and Rigau, German and Agirre, Eneko},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.03668},\n}\n\n@inproceedings{gliner-2024,\n    title     = {{GLiNER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer},\n    author    = {Zaratiana, Urchade and Tomeh, Nadi and Holat, Pierre and Charnois, Thierry},\n    booktitle = {Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics},\n    pages     = {5364--5376},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2311.08526},\n}\n\n@inproceedings{gliner2-2025,\n    title     = {{GLiNER2}: Schema-Driven Multi-Task Learning for Structured Information Extraction},\n    author    = {Zaratiana, Urchade and Pasternak, Gil and Boyd, Oliver and Hurn-Maloney, George and Lewis, Ash},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations},\n    pages     = {130--140},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-demos.10/},\n}\n\n\n@inproceedings{iepile-2024,\n    title     = {{IEPile}: Unearthing Large Scale Schema-Conditioned Information Extraction Corpus},\n    author    = {Gui, Honghao and Yuan, Lin and Ye, Hongbin and Zhang, Ningyu and Sun, Mengshu and Liang, Lei and Chen, Huajun},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n    pages     = {127--146},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.acl-short.13/},\n}\n\n\n@inproceedings{dror-2018-significance,\n    title     = {The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing},\n    author    = {Dror, Rotem and Baumer, Gili and Shlomov, Segev and Reichart, Roi},\n    booktitle = {Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {1383--1392},\n    year      = {2018},\n    url       = {https://aclanthology.org/P18-1128/},\n}\n\n@article{lost-in-middle-2024,\n    title   = {Lost in the Middle: How Language Models Use Long Contexts},\n    author  = {Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy},\n    journal = {Transactions of the Association for Computational Linguistics},\n    volume  = {12},\n    pages   = {157--173},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2307.03172},\n    doi     = {10.1162/tacl_a_00638},\n}\n\n% =============================================================================\n% ZERO-SHOT NER / RE BASELINES\n% =============================================================================\n\n@inproceedings{shachar-2025-ner-retriever,\n    title     = {{NER} Retriever: Zero-Shot Named Entity Retrieval with Type-Aware Embeddings},\n    author    = {Shachar, Or and Katz, Uri and Goldberg, Yoav and Glickman, Oren},\n    booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2025},\n    year      = {2025},\n    pages     = {11175--11186},\n}\n\n\n\n% =============================================================================\n% EVALUATION / BENCHMARKING\n% =============================================================================\n\n% =============================================================================\n% SURVEYS / BACKGROUND\n% =============================================================================\n\n@article{llm4ie-survey-2024,\n    title   = {Large Language Models for Generative Information Extraction: A Survey},\n    author  = {Xu, Derong and Chen, Wei and Peng, Wenjun and Zhang, Chao and Xu, Tong and Zhao, Xiangyu and Wu, Xian and Zheng, Yefeng and Wang, Yang and Chen, Enhong},\n    journal = {Frontiers of Computer Science},\n    volume  = {18},\n    number  = {6},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2312.17617},\n    doi     = {10.1007/s11704-024-40555-y},\n}\n\n@inproceedings{knowcoder-2024,\n    title     = {{KnowCoder}: Coding Structured Knowledge into {LLM}s for Universal Information Extraction},\n    author    = {Li, Zixuan and Zeng, Yutao and Zuo, Yuxin and Ren, Weicheng and Liu, Wenxuan and Su, Miao and Guo, Yucan and Liu, Yantao and Li, Xiang and Hu, Zhilei and Bai, Long and Li, Wei and Liu, Yidan and Yang, Pan and Jin, Xiaolong and Guo, Jiafeng and Cheng, Xueqi},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    pages     = {8758--8779},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2403.07969},\n}\n\n@inproceedings{slot-2025,\n    title     = {{SLOT}: Structuring the Output of Large Language Models},\n    author    = {Shen, Zhengyuan and Wang, Darren Yow-Bang and Mishra, Soumya Smruti and Xu, Zhichao and Teng, Yifei and Ding, Haibo},\n    booktitle = {Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: Industry Track},\n    pages     = {472--491},\n    year      = {2025},\n    url       = {https://aclanthology.org/2025.emnlp-industry.32/},\n}\n\n% =============================================================================\n% EMBEDDING ANISOTROPY / REPRESENTATION DEGENERATION\n% =============================================================================\n\n\n@inproceedings{ethayarajh-contextual-2019,\n    title     = {How Contextual are Contextualized Word Representations? {C}omparing the Geometry of {BERT}, {ELMo}, and {GPT-2} Embeddings},\n    author    = {Ethayarajh, Kawin},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing},\n    pages     = {55--65},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1006/},\n}\n\n@inproceedings{cai-isotropy-clusters-2021,\n    title     = {Isotropy in the Contextual Embedding Space: Clusters and Manifolds},\n    author    = {Cai, Xingyu and Huang, Jiaji and Bian, Yuchen and Church, Kenneth},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2021},\n    url       = {https://openreview.net/forum?id=xYGNO86OWDH},\n}\n\n\n% =============================================================================\n% ADDITIONAL REFERENCES (from references_survey.md only)\n% =============================================================================\n\n@article{instructuie-2023,\n    title   = {{InstructUIE}: Multi-task Instruction Tuning for Unified Information Extraction},\n    author  = {Wang, Xiao and Zhou, Weikang and Zu, Can and Xia, Han and Chen, Tianze and Zhang, Yuansen and Zheng, Rui and Ye, Junjie and Zhang, Qi and Gui, Tao and Kang, Jihua and Yang, Jingsheng and Li, Siyuan and Du, Chunsai},\n    journal = {arXiv preprint arXiv:2304.08085},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.08085},\n}\n\n@inproceedings{codeie-2023,\n    title     = {{CodeIE}: Large Code Generation Models are Better Few-Shot Information Extractors},\n    author    = {Li, Peng and Sun, Tianxiang and Tang, Qiong and Yan, Hang and Wu, Yuanbin and Huang, Xuanjing and Qiu, Xipeng},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15339--15353},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.855/},\n}\n\n@inproceedings{adelie-2024,\n    title     = {{ADELIE}: Aligning Large Language Models on Information Extraction},\n    author    = {Qi, Yunjia and Peng, Hao and Wang, Xiaozhi and Xu, Bin and Hou, Lei and Li, Juanzi},\n    booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7371--7387},\n    year      = {2024},\n    url       = {https://aclanthology.org/2024.emnlp-main.419/},\n}\n\n@inproceedings{oneke-2025,\n    title     = {{OneKE}: A Dockerized Schema-Guided {LLM} Agent-based Knowledge Extraction System},\n    author    = {Luo, Yujie and Ru, Xiangyuan and Liu, Kangwei and Yuan, Lin and Sun, Mengshu and Zhang, Ningyu and Liang, Lei and Zhang, Zhiqiang and Zhou, Jun and Wei, Lanning and Zheng, Da and Wang, Haofen and Chen, Huajun},\n    booktitle = {Companion Proceedings of the ACM Web Conference 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2412.20005},\n    doi       = {10.1145/3701716.3715189},\n}\n\n\n\n\n% =============================================================================\n% DATASETS\n% =============================================================================\n\n@inproceedings{fewnerd-2021,\n    title     = {Few-{NERD}: A Few-shot Named Entity Recognition Dataset},\n    author    = {Ding, Ning and Xu, Guangwei and Chen, Yulin and Wang, Xiaobin and Han, Xu and Xie, Pengjun and Zheng, Haitao and Liu, Zhiyuan},\n    booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {3198--3213},\n    year      = {2021},\n    url       = {https://aclanthology.org/2021.acl-long.248/},\n}\n\n@inproceedings{fewrel-2018,\n    title     = {{FewRel}: A Large-Scale Supervised Few-Shot Relation Classification Dataset with State-of-the-Art Evaluation},\n    author    = {Han, Xu and Zhu, Hao and Yu, Pengfei and Wang, Ziyun and Yao, Yuan and Liu, Zhiyuan and Sun, Maosong},\n    booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {4803--4809},\n    year      = {2018},\n    url       = {https://aclanthology.org/D18-1514/},\n}\n\n@inproceedings{maven-2020,\n    title     = {{MAVEN}: A Massive General Domain Event Detection Dataset},\n    author    = {Wang, Xiaozhi and Wang, Ziqi and Han, Xu and Jiang, Wangyi and Han, Rong and Liu, Zhiyuan and Li, Juanzi and Li, Peng and Lin, Yankai and Zhou, Jie},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {1652--1671},\n    year      = {2020},\n    url       = {https://aclanthology.org/2020.emnlp-main.129/},\n}\n\n@inproceedings{docred-2019,\n    title     = {{DocRED}: A Large-Scale Document-Level Relation Extraction Dataset},\n    author    = {Yao, Yuan and Ye, Deming and Li, Peng and Han, Xu and Lin, Yankai and Liu, Zhenghao and Liu, Zhiyuan and Huang, Lixin and Zhou, Jie and Sun, Maosong},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    pages     = {764--777},\n    year      = {2019},\n    url       = {https://aclanthology.org/P19-1074/},\n}\n\n% =============================================================================\n% MODELS AND TOOLS\n% =============================================================================\n\n@article{qwen3-2025,\n    title   = {Qwen3 Technical Report},\n    author  = {{Qwen Team}},\n    journal = {arXiv preprint arXiv:2505.09388},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2505.09388},\n}\n\n@article{llama3-2024,\n    title   = {The {Llama} 3 Herd of Models},\n    author  = {Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and Yang, Amy and Fan, Angela},\n    journal = {arXiv preprint arXiv:2407.21783},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2407.21783},\n}\n\n@inproceedings{sentence-bert-2019,\n    title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},\n    author    = {Reimers, Nils and Gurevych, Iryna},\n    booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2019},\n    url       = {https://aclanthology.org/D19-1410/},\n}\n\n@inproceedings{minilm-2020,\n    title     = {{MiniLM}: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers},\n    author    = {Wang, Wenhui and Wei, Furu and Dong, Li and Bao, Hangbo and Yang, Nan and Zhou, Ming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    volume    = {33},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/2002.10957},\n}\n\n@inproceedings{reflect-learn-2026,\n    title     = {Reflect then Learn: Active Prompting for Information Extraction Guided by Introspective Confusion},\n    author    = {Zhao, Dong and Wang, Yadong and Chen, Xiang and Wang, Chenxi and Dai, Hongliang and Geng, Chuanxing and Zhang, Shengzhong and Li, Shaoyuan and Huang, Sheng-Jun},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {40},\n    pages     = {34923--34931},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.10036},\n    doi       = {10.1609/aaai.v40i41.40796},\n}\n\n@inproceedings{sclar-sensitivity-2024,\n    title     = {Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design},\n    author    = {Sclar, Melanie and Choi, Yejin and Tsvetkov, Yulia and Suhr, Alane},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2310.11324},\n}\n\n@inproceedings{vllm-2023,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://dl.acm.org/doi/10.1145/3600006.3613165},\n}\n\n@inproceedings{xie-zeroshot-ner-2023,\n    title     = {Empirical Study of Zero-Shot {NER} with {ChatGPT}},\n    author    = {Xie, Tingyu and Li, Qi and Zhang, Jian and Zhang, Yan and Liu, Zuozhu and Wang, Hongwei},\n    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}\n\n@inproceedings{wadhwa-re-llm-2023,\n    title     = {Revisiting Relation Extraction in the era of Large Language Models},\n    author    = {Wadhwa, Somin and Amir, Silvio and Wallace, Byron C.},\n    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics},\n    pages     = {15566--15589},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.acl-long.868/},\n}\n\n@inproceedings{relationprompt-2022,\n    title     = {{RelationPrompt}: Leveraging Prompts to Generate Synthetic Data for Zero-Shot Relation Triplet Extraction},\n    author    = {Chia, Yew Ken and Bing, Lidong and Poria, Soujanya and Si, Luo},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n    pages     = {45--57},\n    year      = {2022},\n    url       = {https://aclanthology.org/2022.findings-acl.5/},\n}\n\n@article{promptner-2023,\n    title   = {{PromptNER}: Prompting For Named Entity Recognition},\n    author  = {Ashok, Dhananjay and Lipton, Zachary C.},\n    journal = {arXiv preprint arXiv:2305.15444},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2305.15444},\n}\n\n@article{json-schema-bench-2025,\n    title   = {{JSONSchemaBench}: A Rigorous Benchmark of Structured Outputs for Language Models},\n    author  = {Geng, Saibo and Cooper, Hudson and Moskal, Micha{\\l} and Jenkins, Samuel and Berman, Julian and Ranchin, Nathan and West, Robert and Horvitz, Eric and Nori, Harsha},\n    journal = {arXiv preprint arXiv:2501.10868},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.10868},\n}\n\n@inproceedings{rastogi2020towards,\n    title     = {Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset},\n    author    = {Rastogi, Abhinav and Zang, Xiaoxue and Sunkara, Srinivas and Gupta, Raghav and Khaitan, Pranav},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {34},\n    pages     = {8689--8696},\n    year      = {2020},\n    url       = {https://arxiv.org/abs/1909.05855},\n}\n\n@article{li2023evaluating,\n    title   = {Evaluating {ChatGPT}'s Information Extraction Capabilities: An Assessment of Performance, Explainability, Calibration, and Faithfulness},\n    author  = {Li, Bo and Fang, Gexiang and Yang, Yang and Wang, Quansen and Ye, Wei and Zhao, Wen and Zhang, Shikun},\n    journal = {arXiv preprint arXiv:2304.11633},\n    year    = {2023},\n    url     = {https://arxiv.org/abs/2304.11633},\n}\n\n@inproceedings{lee2022sgd,\n    title     = {{SGD-X}: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems},\n    author    = {Lee, Harrison and Gupta, Raghav and Rastogi, Abhinav and Cao, Yuan and Zhang, Bin and Wu, Yonghui},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {36},\n    pages     = {10938--10946},\n    year      = {2022},\n    url       = {https://arxiv.org/abs/2110.06800},\n}\n\n@article{haystack-to-needle-2025,\n    title   = {From Haystack to Needle: Label Space Reduction for Zero-shot Classification},\n    author  = {Vandemoortele, Nathan and Steenwinckel, Bram and Ongenae, Femke and Van Hoecke, Sofie},\n    journal = {arXiv preprint arXiv:2502.08436},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2502.08436},\n}\n\n@inproceedings{deng-2010-imagenet,\n    title     = {What Does Classifying More Than 10,000 Image Categories Tell Us?},\n    author    = {Deng, Jia and Berg, Alexander C. and Li, Kai and Fei-Fei, Li},\n    booktitle = {Proceedings of the 11th European Conference on Computer Vision},\n    pages     = {71--84},\n    year      = {2010},\n    doi       = {10.1007/978-3-642-15555-0\\_6},\n}\n\n@article{rothman-1990,\n    title   = {No Adjustments Are Needed for Multiple Comparisons},\n    author  = {Rothman, Kenneth J.},\n    journal = {Epidemiology},\n    volume  = {1},\n    number  = {1},\n    pages   = {43--46},\n    year    = {1990},\n    doi     = {10.1097/00001648-199001000-00010},\n}\n\n@article{lakens-2017-equivalence,\n    title   = {Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses},\n    author  = {Lakens, Dani{\\\"e}l},\n    journal = {Social Psychological and Personality Science},\n    volume  = {8},\n    number  = {4},\n    pages   = {355--362},\n    year    = {2017},\n    doi     = {10.1177/1948550617697177},\n}\n\n\n@inproceedings{guo-2021-label-confusion,\n    title     = {Label Confusion Learning to Enhance Text Classification Models},\n    author    = {Guo, Biyang and Han, Songqiao and Han, Xiao and Huang, Hailiang and Lu, Ting},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    volume    = {35},\n    number    = {14},\n    pages     = {12929--12936},\n    year      = {2021},\n    doi       = {10.1609/aaai.v35i14.17529},\n}\n\n\n@article{dlisc-2025,\n    title     = {Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models},\n    author    = {Li, Zhuoqun and Wu, Hao and Li, Xinxin and Li, Zhoujun},\n    journal   = {arXiv preprint arXiv:2505.14992},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.14992}\n}\n\n@article{spt-2025,\n    title     = {Schema as Parameterized Tools for Universal Information Extraction},\n    author    = {Liang, Sheng and Zhang, Yongyue and Wu, Yaxiong and Tang, Ruiming and Liu, Yong},\n    journal   = {arXiv preprint arXiv:2506.01276},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2506.01276}\n}\n\n@inproceedings{card-2020-power,\n    title     = {With Little Power Comes Great Responsibility},\n    author    = {Card, Dallas and Henderson, Peter and Khandelwal, Urvashi and Jia, Robin and Mahowald, Kyle and Jurafsky, Dan},\n    booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n    pages     = {9263--9274},\n    year      = {2020},\n    publisher = {Association for Computational Linguistics},\n    url       = {https://aclanthology.org/2020.emnlp-main.745}\n}\n\n@article{chen-2026-multi-instance,\n    title     = {Understanding {LLM} Performance Degradation in Multi-Instance Processing: The Roles of Instance Count and Context Length},\n    author    = {Chen, Jingxuan and Pilehvar, Mohammad Taher and Camacho-Collados, Jose},\n    journal   = {arXiv preprint arXiv:2603.22608},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2603.22608}\n}\n\n@article{robinson-1950-ecological,\n    author    = {Robinson, William S.},\n    title     = {Ecological Correlations and the Behavior of Individuals},\n    journal   = {American Sociological Review},\n    volume    = {15},\n    number    = {3},\n    pages     = {351--357},\n    year      = {1950}\n}\n\n@inproceedings{boylan-2025-glirel,\n    title     = {{GLiREL} -- Generalist Model for Zero-Shot Relation Extraction},\n    author    = {Boylan, Jack and Hokamp, Chris and Gholipour Ghalandari, Demian},\n    booktitle = {Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)},\n    year      = {2025},\n    address   = {Albuquerque, New Mexico},\n    publisher = {Association for Computational Linguistics},\n    pages     = {8230--8245},\n    url       = {https://aclanthology.org/2025.naacl-long.418/}\n}\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 399,
        "oldLines": 6,
        "newStart": 399,
        "newLines": 7,
        "lines": [
          "     title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},",
          "     author    = {Reimers, Nils and Gurevych, Iryna},",
          "     booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},",
          "+    pages     = {3982--3992},",
          "     year      = {2019},",
          "     url       = {https://aclanthology.org/D19-1410/},",
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

_source line 159_

<details open><summary>🔧 Tool call — Edit · `toolu_012nerTpnkfhtqgBf4VJ1JNb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/references.bib",
  "old_string": "    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}",
  "new_string": "    booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n    pages     = {7935--7956},\n    year      = {2023},\n    url       = {https://aclanthology.org/2023.emnlp-main.493/},\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3bad2dee-4ea9-4455-9022-7a0fe772f1ae",
  "uuid": "06945777-e048-48f7-ae48-fd3df45f7809",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DC8eodkxuUYLkrSGL6XiW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3608,
      "cache_read_input_tokens": 41495,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3608
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
