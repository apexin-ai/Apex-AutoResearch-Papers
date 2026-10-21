# audit ref check B 20260526T110655 retry1

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_audit_ref_check_B_20260526T110655_retry1.log`
- **Structured JSON:** [`952e81af65719c24bf64.json`](../../sessions/95/952e81af65719c24bf64.json)

## Before a recorded user message

54 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge",
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "639c4e08-17f4-4caf-b04e-36e71dc83828",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/memory/"
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
    "resetsAt": 1779810000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "865c70c0-14da-438f-bff4-3c482afb551a",
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "6b1a394d-790c-4c9f-a35c-3e1d770eb1ca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UcLVRESJGTHJkq5K6YwDXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17564,
      "cache_read_input_tokens": 15491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17564
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XBeECxwiJySPrh6F1QbmBb`</summary>

```json
{
  "query": "select:WebSearch,TodoWrite",
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
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "33b1da9c-74c4-4102-a9a5-8c6e951e9adb",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01UcLVRESJGTHJkq5K6YwDXM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 17564,
      "cache_read_input_tokens": 15491,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17564
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

_source line 6 · 2026-05-26T11:07:14.631Z_

<details><summary>↩ Tool result · `toolu_01XBeECxwiJySPrh6F1QbmBb`</summary>

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
  "tool_name": "TodoWrite"
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
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "c71647be-e774-4fcd-ac6d-48cc78baf756",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "TodoWrite"
    ],
    "query": "select:WebSearch,TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "ff1cb9d0-e3ae-4232-9ffd-6761ff653913",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QPQhJK2h4c4v32DgooxRGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 21796,
      "cache_read_input_tokens": 15584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21796
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29996
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_018Xdx3DeDjfRLFLc6LyeFe3`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "a6f33583-daf6-4be3-b8f1-489d1ef9bb0c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01QPQhJK2h4c4v32DgooxRGc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 21796,
      "cache_read_input_tokens": 15584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21796
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 29996
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-26T11:07:18.640Z_

<details><summary>↩ Tool result · `toolu_018Xdx3DeDjfRLFLc6LyeFe3`</summary>

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
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "facaf22f-9ec1-44c1-b3fc-b05875bd42d8",
  "tool_use_result": {
    "filenames": [
      "docs/paper/references.bib"
    ],
    "durationMs": 6,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_014PCoZeNP5rj7NsFCD5d82n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "00a57ca4-43f5-4571-b19f-9174554fa1b5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JsyPrtPLetcW8sz5y6S6zu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 37380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 189
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 11 · 2026-05-26T11:07:21.288Z_

<details><summary>↩ Tool result · `toolu_014PCoZeNP5rj7NsFCD5d82n`</summary>

```text
1	@book{cohen1988statistical,
2	  title={Statistical Power Analysis for the Behavioral Sciences},
3	  author={Cohen, Jacob},
4	  edition={2nd},
5	  year={1988},
6	  publisher={Lawrence Erlbaum Associates}
7	}
8	
9	@book{pearl2009causality,
10	  title={Causality: Models, Reasoning, and Inference},
11	  author={Pearl, Judea},
12	  edition={2nd},
13	  year={2009},
14	  publisher={Cambridge University Press}
15	}
16	
17	@inproceedings{tripathi2025pairwise,
18	  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
19	  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
20	  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},
21	  year={2025},
22	  url={https://arxiv.org/abs/2504.14716}
23	}
24	
25	@inproceedings{feuer2025sos,
26	  title={Style Outweighs Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
27	  author={Feuer, Benjamin and Goldblum, Micah and Datta, Teresa and Nambiar, Sanjana and Besaleli, Raz and Dooley, Samuel and Cembalest, Max and Dickerson, John P.},
28	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
29	  year={2025},
30	  url={https://arxiv.org/abs/2409.15268}
31	}
32	
33	@inproceedings{li2026preference,
34	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
35	  author={Li, Dawei and others},
36	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
37	  year={2026},
38	  url={https://arxiv.org/abs/2502.01534}
39	}
40	
41	@article{wang2026fairjudge,
42	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
43	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
44	  journal={arXiv preprint arXiv:2602.06625},
45	  year={2026},
46	  url={https://arxiv.org/abs/2602.06625}
47	}
48	
49	
50	@inproceedings{dubois2025lc,
51	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
52	  author={Dubois, Yann and others},
53	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
54	  year={2025},
55	  url={https://arxiv.org/abs/2404.04475}
56	}
57	
58	@article{casse2026concise,
59	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
60	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
61	  journal={arXiv preprint arXiv:2601.10809},
62	  year={2026},
63	  url={https://arxiv.org/abs/2601.10809}
64	}
65	
66	@article{counterfactual2025rhetorical,
67	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
68	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
69	  journal={arXiv preprint arXiv:2512.19908},
70	  year={2025},
71	  url={https://arxiv.org/abs/2512.19908}
72	}
73	
74	@article{soumik2026judging,
75	  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},
76	  author={Soumik, Sadman Kabir},
77	  journal={arXiv preprint arXiv:2604.23178},
78	  year={2026},
79	  url={https://arxiv.org/abs/2604.23178}
80	}
81	
82	@inproceedings{reber2025rate,
83	  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},
84	  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},
85	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
86	  year={2025},
87	  url={https://arxiv.org/abs/2410.11348}
88	}
89	
90	@inproceedings{novikova2018rankme,
91	  title={{RankME}: Reliable Human Ratings for Natural Language Generation},
92	  author={Novikova, Jekaterina and Du{\v{s}}ek, Ond{\v{r}}ej and Rieser, Verena},
93	  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},
94	  year={2018},
95	  url={https://aclanthology.org/N18-2012/}
96	}
97	
98	@article{nemes2009bias,
99	  title={Bias in odds ratios by logistic regression modelling and sample size},
100	  author={Nemes, Szil{\'a}rd and Jonasson, J{\"o}rgen M and Genell, Anna and Steineck, Gunnar},
101	  journal={BMC Medical Research Methodology},
102	  volume={9},
103	  number={56},
104	  year={2009},
105	  publisher={BioMed Central}
106	}
107	
108	@book{david1988method,
109	  title={The Method of Paired Comparisons},
110	  author={David, Herbert A.},
111	  edition={2nd},
112	  year={1988},
113	  publisher={Oxford University Press}
114	}
115	
116	@article{thurstone1927law,
117	  title={A Law of Comparative Judgment},
118	  author={Thurstone, Louis Leon},
119	  journal={Psychological Review},
120	  volume={34},
121	  number={4},
122	  pages={273--286},
123	  year={1927}
124	}
125	
126	@inproceedings{zheng2023judging,
127	  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
128	  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
129	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
130	  year={2023},
131	  url={https://arxiv.org/abs/2306.05685}
132	}
133	
134	@inproceedings{dubois2023alpacafarm,
135	  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},
136	  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},
137	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
138	  year={2023},
139	  url={https://arxiv.org/abs/2305.14387}
140	}
141	
142	@article{bradley1952rank,
143	  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},
144	  author={Bradley, Ralph Allan and Terry, Milton E.},
145	  journal={Biometrika},
146	  volume={39},
147	  number={3/4},
148	  pages={324--345},
149	  year={1952}
150	}
151	
152	@article{feinstein1990kappa,
153	  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},
154	  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},
155	  journal={Journal of Clinical Epidemiology},
156	  volume={43},
157	  number={6},
158	  pages={543--549},
159	  year={1990}
160	}
161	
162	
163	@inproceedings{wang2023faireval,
164	  title={Large Language Models are not Fair Evaluators},
165	  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},
166	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
167	  year={2024},
168	  url={https://aclanthology.org/2024.acl-long.511/}
169	}
170	
171	@inproceedings{li2024calibraeval,
172	  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},
173	  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},
174	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
175	  year={2025},
176	  url={https://aclanthology.org/2025.acl-long.808/}
177	}
178	
179	@article{hoenig2001abuse,
180	  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},
181	  author={Hoenig, John M. and Heisey, Dennis M.},
182	  journal={The American Statistician},
183	  volume={55},
184	  number={1},
185	  pages={19--24},
186	  year={2001}
187	}
188	
189	@inproceedings{zeng2023llmbar,
190	  title={Evaluating Large Language Models at Evaluating Instruction Following},
191	  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},
192	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
193	  year={2024},
194	  url={https://arxiv.org/abs/2310.07641}
195	}
196	
197	@inproceedings{veitch2020adapting,
198	  title={Adapting Text Embeddings for Causal Inference},
199	  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},
200	  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},
201	  year={2020},
202	  url={https://arxiv.org/abs/1905.12741}
203	}
204	
205	@inproceedings{tan2025judgebench,
206	  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},
207	  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},
208	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
209	  year={2025},
210	  url={https://arxiv.org/abs/2410.12784}
211	}
212	
213	@inproceedings{chiang2024chatbot,
214	  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},
215	  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
216	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
217	  year={2024},
218	  url={https://arxiv.org/abs/2403.04132}
219	}
220	
221	@article{hunter2004mm,
222	  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},
223	  author={Hunter, David R.},
224	  journal={The Annals of Statistics},
225	  volume={32},
226	  number={1},
227	  pages={384--406},
228	  year={2004},
229	  doi={10.1214/aos/1079120141}
230	}
231	
232	@inproceedings{ye2024justice,
233	  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},
234	  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},
235	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
236	  year={2025},
237	  url={https://arxiv.org/abs/2410.02736}
238	}
239	
240	@article{feder2021causalm,
241	  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},
242	  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},
243	  journal={Computational Linguistics},
244	  volume={47},
245	  number={2},
246	  pages={333--386},
247	  year={2021},
248	  url={https://aclanthology.org/2021.cl-2.13/}
249	}
250	
251	@inproceedings{wu2021polyjuice,
252	  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},
253	  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},
254	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
255	  year={2021},
256	  url={https://aclanthology.org/2021.acl-long.523/}
257	}
258	
259	@inproceedings{amidei2019likert,
260	  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},
261	  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},
262	  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},
263	  year={2019},
264	  url={https://aclanthology.org/W19-8648/}
265	}
266	
267	@inproceedings{wu2023style,
268	  title={Style Over Substance: Evaluation Biases for Large Language Models},
269	  author={Wu, Minghao and Aji, Alham Fikri},
270	  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},
271	  year={2025},
272	  url={https://aclanthology.org/2025.coling-main.21/}
273	}
274	
275	@article{feder2022causal,
276	  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},
277	  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},
278	  journal={Transactions of the Association for Computational Linguistics},
279	  volume={10},
280	  pages={1138--1158},
281	  year={2022},
282	  url={https://aclanthology.org/2022.tacl-1.66/}
283	}
284	
285	@inproceedings{koo2024cobbler,
286	  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},
287	  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},
288	  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
289	  year={2024},
290	  url={https://aclanthology.org/2024.findings-acl.29/}
291	}
292	
293	@article{liang1986gee,
294	  title={Longitudinal Data Analysis Using Generalized Linear Models},
295	  author={Liang, Kung-Yee and Zeger, Scott L.},
296	  journal={Biometrika},
297	  volume={73},
298	  number={1},
299	  pages={13--22},
300	  year={1986},
301	  doi={10.1093/biomet/73.1.13}
302	}
303	
304	@article{krosnick1999survey,
305	  title={Survey Research},
306	  author={Krosnick, Jon A.},
307	  journal={Annual Review of Psychology},
308	  volume={50},
309	  number={1},
310	  pages={537--567},
311	  year={1999},
312	  doi={10.1146/annurev.psych.50.1.537}
313	}
314	
315	@article{lakens2017equivalence,
316	  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},
317	  author={Lakens, Dani{\"e}l},
318	  journal={Social Psychological and Personality Science},
319	  volume={8},
320	  number={4},
321	  pages={355--362},
322	  year={2017},
323	  doi={10.1177/1948550617697177}
324	}
325	
326	@article{preston2000scale,
327	  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},
328	  author={Preston, Carolyn C. and Colman, Andrew M.},
329	  journal={Acta Psychologica},
330	  volume={104},
331	  number={1},
332	  pages={1--15},
333	  year={2000},
334	  doi={10.1016/S0001-6918(99)00050-5}
335	}
336	
337	@inproceedings{jeong2025comparative,
338	  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},
339	  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},
340	  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},
341	  pages={79--108},
342	  year={2025},
343	  url={https://aclanthology.org/2025.blackboxnlp-1.5}
344	}
345	
346	@article{stureborg2024inconsistent,
347	  title={Large Language Models are Inconsistent and Biased Evaluators},
348	  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},
349	  journal={arXiv preprint arXiv:2405.01724},
350	  year={2024},
351	  url={https://arxiv.org/abs/2405.01724}
352	}
353	
354	@inproceedings{park2024offsetbias,
355	  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},
356	  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},
357	  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},
358	  pages={1043--1067},
359	  year={2024},
360	  doi={10.18653/v1/2024.findings-emnlp.57},
361	  url={https://aclanthology.org/2024.findings-emnlp.57}
362	}
363	
364	@inproceedings{chen2024humans,
365	  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},
366	  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},
367	  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
368	  year={2024},
369	  url={https://aclanthology.org/2024.emnlp-main.474/}
370	}
371	
372	@inproceedings{he2021debertav3,
373	  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},
374	  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
375	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
376	  year={2023},
377	  url={https://arxiv.org/abs/2111.09543}
378	}
379	
380	@inproceedings{shi2024judging,
381	  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},
382	  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},
383	  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
384	  year={2025},
385	  url={https://aclanthology.org/2025.ijcnlp-long.18/}
386	}
387	
388	@inproceedings{bavaresco2025llms,
389	  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},
390	  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},
391	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
392	  year={2025},
393	  url={https://aclanthology.org/2025.acl-short.20/}
394	}
395	
396	@inproceedings{saito2023verbosity,
397	  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},
398	  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},
399	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
400	  year={2023},
401	  url={https://aclanthology.org/2023.emnlp-main.665/}
402	}
403	
404	@article{simms2019does,
405	  title={Does the Number of Response Options Matter? {P}sychometric Perspectives Using Personality Questionnaire Data},
406	  author={Simms, Leonard J. and Zelazny, Kerry and Williams, Trevor F. and Bernstein, Lee},
407	  journal={Psychological Assessment},
408	  volume={31},
409	  number={4},
410	  pages={557--566},
411	  year={2019},
412	  publisher={American Psychological Association},
413	  doi={10.1037/pas0000648}
414	}
415	
416	@inproceedings{carterette2008here,
417	  author = {Ben Carterette and Paul N. Bennett and David Maxwell Chickering and Susan T. Dumais},
418	  title = {Here or There: Preference Judgments for Relevance},
419	  booktitle = {Advances in Information Retrieval, 30th European Conference on {IR} Research, {ECIR} 2008},
420	  pages = {16--27},
421	  year = {2008},
422	  publisher = {Springer},
423	  series = {Lecture Notes in Computer Science},
424	  volume = {4956},
425	  doi = {10.1007/978-3-540-78646-7_5},
426	  address = {Glasgow, UK}
427	}
428	
429	@inproceedings{deutsch-etal-2023-ties,
430	  author = {Daniel Deutsch and George Foster and Markus Freitag},
431	  title = {Ties Matter: Meta-Evaluating Modern Metrics with Pairwise Accuracy and Tie Calibration},
432	  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
433	  pages = {12914--12929},
434	  year = {2023},
435	  publisher = {Association for Computational Linguistics},
436	  address = {Singapore}
437	}
438	
439	@book{luce1959individual,
440	  title={Individual Choice Behavior: A Theoretical Analysis},
441	  author={Luce, R. Duncan},
442	  year={1959},
443	  publisher={John Wiley \& Sons},
444	  address={New York}
445	}
446	
447	@inproceedings{williams2018broad,
448	  title={A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference},
449	  author={Williams, Adina and Nangia, Nikita and Bowman, Samuel R.},
450	  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
451	  pages={1112--1122},
452	  year={2018},
453	  publisher={Association for Computational Linguistics}
454	}
455	
456	@book{embretson2000irt,
457	  title={Item Response Theory for Psychologists},
458	  author={Embretson, Susan E. and Reise, Steven P.},
459	  year={2000},
460	  publisher={Lawrence Erlbaum Associates},
461	  address={Mahwah, NJ}
462	}
463	
464	@article{gwet2008ac1,
465	  title={Computing inter-rater reliability and its variance in the presence of high agreement},
466	  author={Gwet, Kilem Li},
467	  journal={British Journal of Mathematical and Statistical Psychology},
468	  volume={61},
469	  number={1},
470	  pages={29--48},
471	  year={2008},
472	  publisher={Wiley}
473	}
474	
475	@article{likert1932technique,
476	  title={A Technique for the Measurement of Attitudes},
477	  author={Likert, Rensis},
478	  journal={Archives of Psychology},
479	  volume={22},
480	  number={140},
481	  pages={1--55},
482	  year={1932}
483	}
484	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "9b230634-f1f7-4c97-8b03-3877664c8c21",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
      "content": "@book{cohen1988statistical,\n  title={Statistical Power Analysis for the Behavioral Sciences},\n  author={Cohen, Jacob},\n  edition={2nd},\n  year={1988},\n  publisher={Lawrence Erlbaum Associates}\n}\n\n@book{pearl2009causality,\n  title={Causality: Models, Reasoning, and Inference},\n  author={Pearl, Judea},\n  edition={2nd},\n  year={2009},\n  publisher={Cambridge University Press}\n}\n\n@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{feuer2025sos,\n  title={Style Outweighs Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Feuer, Benjamin and Goldblum, Micah and Datta, Teresa and Nambiar, Sanjana and Besaleli, Raz and Dooley, Samuel and Cembalest, Max and Dickerson, John P.},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Sadman Kabir},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{nemes2009bias,\n  title={Bias in odds ratios by logistic regression modelling and sample size},\n  author={Nemes, Szil{\\'a}rd and Jonasson, J{\\\"o}rgen M and Genell, Anna and Steineck, Gunnar},\n  journal={BMC Medical Research Methodology},\n  volume={9},\n  number={56},\n  year={2009},\n  publisher={BioMed Central}\n}\n\n@book{david1988method,\n  title={The Method of Paired Comparisons},\n  author={David, Herbert A.},\n  edition={2nd},\n  year={1988},\n  publisher={Oxford University Press}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}\n\n@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@inproceedings{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@inproceedings{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2023},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@inproceedings{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.ijcnlp-long.18/}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n\n@article{simms2019does,\n  title={Does the Number of Response Options Matter? {P}sychometric Perspectives Using Personality Questionnaire Data},\n  author={Simms, Leonard J. and Zelazny, Kerry and Williams, Trevor F. and Bernstein, Lee},\n  journal={Psychological Assessment},\n  volume={31},\n  number={4},\n  pages={557--566},\n  year={2019},\n  publisher={American Psychological Association},\n  doi={10.1037/pas0000648}\n}\n\n@inproceedings{carterette2008here,\n  author = {Ben Carterette and Paul N. Bennett and David Maxwell Chickering and Susan T. Dumais},\n  title = {Here or There: Preference Judgments for Relevance},\n  booktitle = {Advances in Information Retrieval, 30th European Conference on {IR} Research, {ECIR} 2008},\n  pages = {16--27},\n  year = {2008},\n  publisher = {Springer},\n  series = {Lecture Notes in Computer Science},\n  volume = {4956},\n  doi = {10.1007/978-3-540-78646-7_5},\n  address = {Glasgow, UK}\n}\n\n@inproceedings{deutsch-etal-2023-ties,\n  author = {Daniel Deutsch and George Foster and Markus Freitag},\n  title = {Ties Matter: Meta-Evaluating Modern Metrics with Pairwise Accuracy and Tie Calibration},\n  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},\n  pages = {12914--12929},\n  year = {2023},\n  publisher = {Association for Computational Linguistics},\n  address = {Singapore}\n}\n\n@book{luce1959individual,\n  title={Individual Choice Behavior: A Theoretical Analysis},\n  author={Luce, R. Duncan},\n  year={1959},\n  publisher={John Wiley \\& Sons},\n  address={New York}\n}\n\n@inproceedings{williams2018broad,\n  title={A Broad-Coverage Challenge Corpus for Sentence Understanding through Inference},\n  author={Williams, Adina and Nangia, Nikita and Bowman, Samuel R.},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},\n  pages={1112--1122},\n  year={2018},\n  publisher={Association for Computational Linguistics}\n}\n\n@book{embretson2000irt,\n  title={Item Response Theory for Psychologists},\n  author={Embretson, Susan E. and Reise, Steven P.},\n  year={2000},\n  publisher={Lawrence Erlbaum Associates},\n  address={Mahwah, NJ}\n}\n\n@article{gwet2008ac1,\n  title={Computing inter-rater reliability and its variance in the presence of high agreement},\n  author={Gwet, Kilem Li},\n  journal={British Journal of Mathematical and Statistical Psychology},\n  volume={61},\n  number={1},\n  pages={29--48},\n  year={2008},\n  publisher={Wiley}\n}\n\n@article{likert1932technique,\n  title={A Technique for the Measurement of Attitudes},\n  author={Likert, Rensis},\n  journal={Archives of Psychology},\n  volume={22},\n  number={140},\n  pages={1--55},\n  year={1932}\n}\n",
      "numLines": 484,
      "startLine": 1,
      "totalLines": 484
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

Now let me search for citation usage in tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "a2fb8f5b-16c7-4085-b812-d9b55a0f0e15",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HoAMvpzK2ThfBqLadPBSxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10044,
      "cache_read_input_tokens": 37569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10044
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Grep · `toolu_01XeTLkCyLKiD79grvXkjf3h`</summary>

```json
{
  "pattern": "dubois2023alpacafarm|bradley1952rank|feinstein1990kappa|wang2023faireval|li2024calibraeval|hoenig2001abuse|zeng2023llmbar|veitch2020adapting|tan2025judgebench|chiang2024chatbot|hunter2004mm|ye2024justice|feder2021causalm|wu2021polyjuice|amidei2019likert|wu2023style|feder2022causal|koo2024cobbler|liang1986gee",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "output_mode": "content",
  "-n": true,
  "head_limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "4f8e5724-d603-4d61-941f-0df422a7ee21",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HoAMvpzK2ThfBqLadPBSxQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10044,
      "cache_read_input_tokens": 37569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10044
      },
      "output_tokens": 5,
      "service_tier": "standard",
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

_source line 14 · 2026-05-26T11:07:29.396Z_

<details><summary>↩ Tool result · `toolu_01XeTLkCyLKiD79grvXkjf3h`</summary>

```text
docs/paper/sections/related_work.tex:5:Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
docs/paper/sections/related_work.tex:11:The foundational LLM-as-judge framework \citep{zheng2023judging} documented position bias; \citet{shi2024judging} study it across 15 judges, and \citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.
docs/paper/sections/related_work.tex:12:Style bias as a separate source has received recent attention \citep{wu2023style,feuer2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \citet{li2026preference} show that style-mediated \emph{preference leakage} propagates through evaluation pipelines.
docs/paper/sections/related_work.tex:19:Within NLP, \citet{amidei2019likert} review Likert scales \citep{likert1932technique} in natural language generation (NLG) evaluation, and \citet{novikova2018rankme} confirm that forced-choice methods detect quality differences that rating scales miss.
docs/paper/sections/related_work.tex:20:The Bradley-Terry model \citep{bradley1952rank} underpins Chatbot Arena \citep{chiang2024chatbot} and AlpacaFarm \citep{dubois2023alpacafarm}; no prior work combines BT with per-axis GEE decomposition to expose confound structures invisible to aggregate scores.
docs/paper/sections/experiments.tex:12:Bradley-Terry parameters \citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the \texttt{choix} Python library's default L2 regularization ($\alpha = 10^{-6}$).
docs/paper/sections/experiments.tex:86:Figure~\ref{fig:power_curve} plots detection probability at observed effect magnitudes (not post-hoc power; cf.\ \citealt{hoenig2001abuse}): across six cells, Likert requires $4$--$206\times$ the current $n$ ($336$--$27{,}159$ pairs; Appendix~\ref{app:power_analysis}) to detect effects BT identifies at $p < 0.001$ with $n \leq 100$.
docs/paper/sections/experiments.tex:109:GEE conditional decomposition \citep{liang1986gee} with exchangeable working correlation and robust standard errors separates style from originality effects (Appendix~\ref{app:direction}; model diagnostics including correlation structure robustness and interaction tests in Appendix~\ref{app:gee_diagnostics}).
docs/paper/sections/method.tex:23:This gating mechanism provides filtering-based confounder control \citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality (validated by human annotation; \S\ref{sec:nli_validation}).
docs/paper/sections/method.tex:50:We evaluate primarily on LLMBar \citep{zeng2023llmbar}, a benchmark of $n = 100$ instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels.
docs/paper/sections/method.tex:52:For cross-benchmark validation, we further evaluate on AlpacaEval \citep{dubois2023alpacafarm} and MT-Bench \citep{zheng2023judging}, targeting the strongest effects from the primary analysis to test whether style sensitivity generalizes beyond a single benchmark's distributional characteristics.
docs/paper/sections/method.tex:53:We select formality and verbosity as primary axes based on prior evidence that these are among the most commonly reported style sensitivities in LLM judges \citep{wu2023style,saito2023verbosity}, with register (academic vs.\ conversational) as an exploratory third axis (implementation details in Appendix~\ref{app:implementation}).
docs/paper/sections/appendix.tex:555:Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm} using the \texttt{choix} Python library (default L2 regularization $\alpha = 10^{-6}$); varying $\alpha$ from $10^{-6}$ to $1.0$ changes all BT probabilities by ${<}0.002$.
docs/paper/sections/appendix.tex:560:LLMBar \citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).
docs/paper/sections/appendix.tex:664:Cohen's $\kappa = {-}0.015$ is misleading here: with ${>}96\%$ positive prevalence, chance agreement is near-ceiling and $\kappa$ is compressed toward zero regardless of actual agreement, the well-documented prevalence paradox \citep{feinstein1990kappa}.
docs/paper/sections/introduction.tex:17:Inspired by interventional text analysis \citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice comparison.
docs/paper/references.bib:134:@inproceedings{dubois2023alpacafarm,
docs/paper/references.bib:142:@article{bradley1952rank,
docs/paper/references.bib:152:@article{feinstein1990kappa,
docs/paper/references.bib:163:@inproceedings{wang2023faireval,
docs/paper/references.bib:171:@inproceedings{li2024calibraeval,
docs/paper/references.bib:179:@article{hoenig2001abuse,
docs/paper/references.bib:189:@inproceedings{zeng2023llmbar,
docs/paper/references.bib:197:@inproceedings{veitch2020adapting,
docs/paper/references.bib:205:@inproceedings{tan2025judgebench,
docs/paper/references.bib:213:@inproceedings{chiang2024chatbot,
docs/paper/references.bib:221:@article{hunter2004mm,
docs/paper/references.bib:232:@inproceedings{ye2024justice,
docs/paper/references.bib:240:@article{feder2021causalm,
docs/paper/references.bib:251:@inproceedings{wu2021polyjuice,
docs/paper/references.bib:259:@inproceedings{amidei2019likert,
docs/paper/references.bib:267:@inproceedings{wu2023style,
docs/paper/references.bib:275:@article{feder2022causal,
docs/paper/references.bib:285:@inproceedings{koo2024cobbler,
docs/paper/references.bib:293:@article{liang1986gee,
docs/paper/main.aux:13:\citation{veitch2020adapting}
docs/paper/main.aux:98:\citation{feder2021causalm,wu2021polyjuice,feder2022causal}
docs/paper/main.aux:103:\citation{ye2024justice}
docs/paper/main.aux:104:\citation{wu2023style,feuer2025sos,saito2023verbosity,li2026preference,soumik2026judging}
docs/paper/main.aux:112:\citation{amidei2019likert}
docs/paper/main.aux:115:\citation{bradley1952rank}
docs/paper/main.aux:116:\citation{chiang2024chatbot}
docs/paper/main.aux:117:\citation{dubois2023alpacafarm}
docs/paper/main.aux:229:\citation{veitch2020adapting}
docs/paper/main.aux:295:\citation{zeng2023llmbar}
docs/paper/main.aux:296:\citation{dubois2023alpacafarm}
docs/paper/main.aux:298:\citation{wu2023style,saito2023verbosity}
docs/paper/main.aux:299:\citation{bradley1952rank,luce1959individual}
docs/paper/main.aux:300:\citation{hunter2004mm}
docs/paper/main.aux:476:\citation{hoenig2001abuse}
docs/paper/main.aux:479:\citation{liang1986gee}
docs/paper/main.aux:745:\bibcite{amidei2019likert}{{1}{2019}{{Amidei et~al.}}{{Amidei, Piwek, and Willis}}}
docs/paper/main.aux:746:\bibcite{bradley1952rank}{{2}{1952}{{Bradley and Terry}}{{}}}
docs/paper/main.aux:748:\bibcite{chiang2024chatbot}{{4}{2024}{{Chiang et~al.}}{{Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhu, Zhang, Jordan, Gonzalez, and Stoica}}}
docs/paper/main.aux:752:\bibcite{dubois2023alpacafarm}{{8}{2023}{{Dubois et~al.}}{{Dubois, Li, Taori, Zhang, Gulrajani, Ba, Guestrin, Liang, and Hashimoto}}}
docs/paper/main.aux:754:\bibcite{feder2022causal}{{10}{2022}{{Feder et~al.}}{{Feder, Keith, Manzoor, Pryzant, Sridhar, Wood-Doughty, Eisenstein, Grimmer, Reichart, Roberts, Stewart, Veitch, and Yang}}}
docs/paper/main.aux:755:\bibcite{feder2021causalm}{{11}{2021}{{Feder et~al.}}{{Feder, Oved, Shalit, and Reichart}}}
docs/paper/main.aux:756:\bibcite{feinstein1990kappa}{{12}{1990}{{Feinstein and Cicchetti}}{{}}}
docs/paper/main.aux:760:\bibcite{hoenig2001abuse}{{16}{2001}{{Hoenig and Heisey}}{{}}}
docs/paper/main.aux:761:\bibcite{hunter2004mm}{{17}{2004}{{Hunter}}{{}}}
docs/paper/main.aux:875:\bibcite{liang1986gee}{{22}{1986}{{Liang and Zeger}}{{}}}
docs/paper/main.aux:889:\bibcite{veitch2020adapting}{{36}{2020}{{Veitch et~al.}}{{Veitch, Sridhar, and Blei}}}
docs/paper/main.aux:891:\bibcite{wu2023style}{{38}{2025}{{Wu and Aji}}{{}}}
docs/paper/main.aux:892:\bibcite{wu2021polyjuice}{{39}{2021}{{Wu et~al.}}{{Wu, Ribeiro, Heer, and Weld}}}
docs/paper/main.aux:894:\bibcite{ye2024justice}{{41}{2025}{{Ye et~al.}}{{Ye, Wang, Huang, Chen, Zhang, Moniz, Gao, Geyer, Huang, Chen, Chawla, and Zhang}}}
docs/paper/main.aux:895:\bibcite{zeng2023llmbar}{{42}{2024}{{Zeng et~al.}}{{Zeng, Yu, Gao, Meng, Goyal, and Chen}}}
docs/paper/main.aux:1485:\citation{hunter2004mm}
docs/paper/main.aux:1486:\citation{zeng2023llmbar}
docs/paper/main.aux:1583:\citation{feinstein1990kappa}
docs/paper/main.bbl:4:\bibitem[{Amidei et~al.(2019)Amidei, Piwek, and Willis}]{amidei2019likert}
docs/paper/main.bbl:12:\bibitem[{Bradley and Terry(1952)}]{bradley1952rank}
docs/paper/main.bbl:29:  Zhang, Jordan, Gonzalez, and Stoica}]{chiang2024chatbot}
docs/paper/main.bbl:57:  Liang, and Hashimoto}]{dubois2023alpacafarm}
docs/paper/main.bbl:74:  Yang}]{feder2022causal}
docs/paper/main.bbl:85:  Reichart}]{feder2021causalm}
docs/paper/main.bbl:91:\bibitem[{Feinstein and Cicchetti(1990)}]{feinstein1990kappa}
docs/paper/main.bbl:120:\bibitem[{Hoenig and Heisey(2001)}]{hoenig2001abuse}
docs/paper/main.bbl:126:\bibitem[{Hunter(2004)}]{hunter2004mm}
docs/paper/main.bbl:160:\bibitem[{Liang and Zeger(1986)}]{liang1986gee}
docs/paper/main.bbl:257:\bibitem[{Veitch et~al.(2020)Veitch, Sridhar, and Blei}]{veitch2020adapting}
docs/paper/main.bbl:273:\bibitem[{Wu and Aji(2025)}]{wu2023style}
docs/paper/main.bbl:280:\bibitem[{Wu et~al.(2021)Wu, Ribeiro, Heer, and Weld}]{wu2021polyjuice}
docs/paper/main.bbl:296:  Huang, Chen, Chawla, and Zhang}]{ye2024justice}
docs/paper/main.bbl:306:  Chen}]{zeng2023llmbar}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "4ac2da21-8c06-4ce2-9cc0-090511e03c5d",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/related_work.tex:5:Text-based interventional methods have a growing methodological foundation \\citep{feder2021causalm,wu2021polyjuice,feder2022causal}.\ndocs/paper/sections/related_work.tex:11:The foundational LLM-as-judge framework \\citep{zheng2023judging} documented position bias; \\citet{shi2024judging} study it across 15 judges, and \\citet{ye2024justice} quantify 12 bias types, though neither isolates individual style effects.\ndocs/paper/sections/related_work.tex:12:Style bias as a separate source has received recent attention \\citep{wu2023style,feuer2025sos,saito2023verbosity,li2026preference,soumik2026judging}; \\citet{li2026preference} show that style-mediated \\emph{preference leakage} propagates through evaluation pipelines.\ndocs/paper/sections/related_work.tex:19:Within NLP, \\citet{amidei2019likert} review Likert scales \\citep{likert1932technique} in natural language generation (NLG) evaluation, and \\citet{novikova2018rankme} confirm that forced-choice methods detect quality differences that rating scales miss.\ndocs/paper/sections/related_work.tex:20:The Bradley-Terry model \\citep{bradley1952rank} underpins Chatbot Arena \\citep{chiang2024chatbot} and AlpacaFarm \\citep{dubois2023alpacafarm}; no prior work combines BT with per-axis GEE decomposition to expose confound structures invisible to aggregate scores.\ndocs/paper/sections/experiments.tex:12:Bradley-Terry parameters \\citep{bradley1952rank,luce1959individual} are estimated via spectral initialization followed by minorization-maximization \\citep{hunter2004mm}, using the \\texttt{choix} Python library's default L2 regularization ($\\alpha = 10^{-6}$).\ndocs/paper/sections/experiments.tex:86:Figure~\\ref{fig:power_curve} plots detection probability at observed effect magnitudes (not post-hoc power; cf.\\ \\citealt{hoenig2001abuse}): across six cells, Likert requires $4$--$206\\times$ the current $n$ ($336$--$27{,}159$ pairs; Appendix~\\ref{app:power_analysis}) to detect effects BT identifies at $p < 0.001$ with $n \\leq 100$.\ndocs/paper/sections/experiments.tex:109:GEE conditional decomposition \\citep{liang1986gee} with exchangeable working correlation and robust standard errors separates style from originality effects (Appendix~\\ref{app:direction}; model diagnostics including correlation structure robustness and interaction tests in Appendix~\\ref{app:gee_diagnostics}).\ndocs/paper/sections/method.tex:23:This gating mechanism provides filtering-based confounder control \\citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality (validated by human annotation; \\S\\ref{sec:nli_validation}).\ndocs/paper/sections/method.tex:50:We evaluate primarily on LLMBar \\citep{zeng2023llmbar}, a benchmark of $n = 100$ instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels.\ndocs/paper/sections/method.tex:52:For cross-benchmark validation, we further evaluate on AlpacaEval \\citep{dubois2023alpacafarm} and MT-Bench \\citep{zheng2023judging}, targeting the strongest effects from the primary analysis to test whether style sensitivity generalizes beyond a single benchmark's distributional characteristics.\ndocs/paper/sections/method.tex:53:We select formality and verbosity as primary axes based on prior evidence that these are among the most commonly reported style sensitivities in LLM judges \\citep{wu2023style,saito2023verbosity}, with register (academic vs.\\ conversational) as an exploratory third axis (implementation details in Appendix~\\ref{app:implementation}).\ndocs/paper/sections/appendix.tex:555:Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \\citep{hunter2004mm} using the \\texttt{choix} Python library (default L2 regularization $\\alpha = 10^{-6}$); varying $\\alpha$ from $10^{-6}$ to $1.0$ changes all BT probabilities by ${<}0.002$.\ndocs/paper/sections/appendix.tex:560:LLMBar \\citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).\ndocs/paper/sections/appendix.tex:664:Cohen's $\\kappa = {-}0.015$ is misleading here: with ${>}96\\%$ positive prevalence, chance agreement is near-ceiling and $\\kappa$ is compressed toward zero regardless of actual agreement, the well-documented prevalence paradox \\citep{feinstein1990kappa}.\ndocs/paper/sections/introduction.tex:17:Inspired by interventional text analysis \\citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice comparison.\ndocs/paper/references.bib:134:@inproceedings{dubois2023alpacafarm,\ndocs/paper/references.bib:142:@article{bradley1952rank,\ndocs/paper/references.bib:152:@article{feinstein1990kappa,\ndocs/paper/references.bib:163:@inproceedings{wang2023faireval,\ndocs/paper/references.bib:171:@inproceedings{li2024calibraeval,\ndocs/paper/references.bib:179:@article{hoenig2001abuse,\ndocs/paper/references.bib:189:@inproceedings{zeng2023llmbar,\ndocs/paper/references.bib:197:@inproceedings{veitch2020adapting,\ndocs/paper/references.bib:205:@inproceedings{tan2025judgebench,\ndocs/paper/references.bib:213:@inproceedings{chiang2024chatbot,\ndocs/paper/references.bib:221:@article{hunter2004mm,\ndocs/paper/references.bib:232:@inproceedings{ye2024justice,\ndocs/paper/references.bib:240:@article{feder2021causalm,\ndocs/paper/references.bib:251:@inproceedings{wu2021polyjuice,\ndocs/paper/references.bib:259:@inproceedings{amidei2019likert,\ndocs/paper/references.bib:267:@inproceedings{wu2023style,\ndocs/paper/references.bib:275:@article{feder2022causal,\ndocs/paper/references.bib:285:@inproceedings{koo2024cobbler,\ndocs/paper/references.bib:293:@article{liang1986gee,\ndocs/paper/main.aux:13:\\citation{veitch2020adapting}\ndocs/paper/main.aux:98:\\citation{feder2021causalm,wu2021polyjuice,feder2022causal}\ndocs/paper/main.aux:103:\\citation{ye2024justice}\ndocs/paper/main.aux:104:\\citation{wu2023style,feuer2025sos,saito2023verbosity,li2026preference,soumik2026judging}\ndocs/paper/main.aux:112:\\citation{amidei2019likert}\ndocs/paper/main.aux:115:\\citation{bradley1952rank}\ndocs/paper/main.aux:116:\\citation{chiang2024chatbot}\ndocs/paper/main.aux:117:\\citation{dubois2023alpacafarm}\ndocs/paper/main.aux:229:\\citation{veitch2020adapting}\ndocs/paper/main.aux:295:\\citation{zeng2023llmbar}\ndocs/paper/main.aux:296:\\citation{dubois2023alpacafarm}\ndocs/paper/main.aux:298:\\citation{wu2023style,saito2023verbosity}\ndocs/paper/main.aux:299:\\citation{bradley1952rank,luce1959individual}\ndocs/paper/main.aux:300:\\citation{hunter2004mm}\ndocs/paper/main.aux:476:\\citation{hoenig2001abuse}\ndocs/paper/main.aux:479:\\citation{liang1986gee}\ndocs/paper/main.aux:745:\\bibcite{amidei2019likert}{{1}{2019}{{Amidei et~al.}}{{Amidei, Piwek, and Willis}}}\ndocs/paper/main.aux:746:\\bibcite{bradley1952rank}{{2}{1952}{{Bradley and Terry}}{{}}}\ndocs/paper/main.aux:748:\\bibcite{chiang2024chatbot}{{4}{2024}{{Chiang et~al.}}{{Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhu, Zhang, Jordan, Gonzalez, and Stoica}}}\ndocs/paper/main.aux:752:\\bibcite{dubois2023alpacafarm}{{8}{2023}{{Dubois et~al.}}{{Dubois, Li, Taori, Zhang, Gulrajani, Ba, Guestrin, Liang, and Hashimoto}}}\ndocs/paper/main.aux:754:\\bibcite{feder2022causal}{{10}{2022}{{Feder et~al.}}{{Feder, Keith, Manzoor, Pryzant, Sridhar, Wood-Doughty, Eisenstein, Grimmer, Reichart, Roberts, Stewart, Veitch, and Yang}}}\ndocs/paper/main.aux:755:\\bibcite{feder2021causalm}{{11}{2021}{{Feder et~al.}}{{Feder, Oved, Shalit, and Reichart}}}\ndocs/paper/main.aux:756:\\bibcite{feinstein1990kappa}{{12}{1990}{{Feinstein and Cicchetti}}{{}}}\ndocs/paper/main.aux:760:\\bibcite{hoenig2001abuse}{{16}{2001}{{Hoenig and Heisey}}{{}}}\ndocs/paper/main.aux:761:\\bibcite{hunter2004mm}{{17}{2004}{{Hunter}}{{}}}\ndocs/paper/main.aux:875:\\bibcite{liang1986gee}{{22}{1986}{{Liang and Zeger}}{{}}}\ndocs/paper/main.aux:889:\\bibcite{veitch2020adapting}{{36}{2020}{{Veitch et~al.}}{{Veitch, Sridhar, and Blei}}}\ndocs/paper/main.aux:891:\\bibcite{wu2023style}{{38}{2025}{{Wu and Aji}}{{}}}\ndocs/paper/main.aux:892:\\bibcite{wu2021polyjuice}{{39}{2021}{{Wu et~al.}}{{Wu, Ribeiro, Heer, and Weld}}}\ndocs/paper/main.aux:894:\\bibcite{ye2024justice}{{41}{2025}{{Ye et~al.}}{{Ye, Wang, Huang, Chen, Zhang, Moniz, Gao, Geyer, Huang, Chen, Chawla, and Zhang}}}\ndocs/paper/main.aux:895:\\bibcite{zeng2023llmbar}{{42}{2024}{{Zeng et~al.}}{{Zeng, Yu, Gao, Meng, Goyal, and Chen}}}\ndocs/paper/main.aux:1485:\\citation{hunter2004mm}\ndocs/paper/main.aux:1486:\\citation{zeng2023llmbar}\ndocs/paper/main.aux:1583:\\citation{feinstein1990kappa}\ndocs/paper/main.bbl:4:\\bibitem[{Amidei et~al.(2019)Amidei, Piwek, and Willis}]{amidei2019likert}\ndocs/paper/main.bbl:12:\\bibitem[{Bradley and Terry(1952)}]{bradley1952rank}\ndocs/paper/main.bbl:29:  Zhang, Jordan, Gonzalez, and Stoica}]{chiang2024chatbot}\ndocs/paper/main.bbl:57:  Liang, and Hashimoto}]{dubois2023alpacafarm}\ndocs/paper/main.bbl:74:  Yang}]{feder2022causal}\ndocs/paper/main.bbl:85:  Reichart}]{feder2021causalm}\ndocs/paper/main.bbl:91:\\bibitem[{Feinstein and Cicchetti(1990)}]{feinstein1990kappa}\ndocs/paper/main.bbl:120:\\bibitem[{Hoenig and Heisey(2001)}]{hoenig2001abuse}\ndocs/paper/main.bbl:126:\\bibitem[{Hunter(2004)}]{hunter2004mm}\ndocs/paper/main.bbl:160:\\bibitem[{Liang and Zeger(1986)}]{liang1986gee}\ndocs/paper/main.bbl:257:\\bibitem[{Veitch et~al.(2020)Veitch, Sridhar, and Blei}]{veitch2020adapting}\ndocs/paper/main.bbl:273:\\bibitem[{Wu and Aji(2025)}]{wu2023style}\ndocs/paper/main.bbl:280:\\bibitem[{Wu et~al.(2021)Wu, Ribeiro, Heer, and Weld}]{wu2021polyjuice}\ndocs/paper/main.bbl:296:  Huang, Chen, Chawla, and Zhang}]{ye2024justice}\ndocs/paper/main.bbl:306:  Chen}]{zeng2023llmbar}",
    "numLines": 84
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "d57199b0-a20b-407c-85f2-82ba73aaf5b4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014Qmv1AaSt5fw2aHtHav7XC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5152,
      "cache_read_input_tokens": 47613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5152
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

Let me check which of these are not cited in any tex files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "eb03a393-7693-415d-bc5e-79c2ce617d43",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014Qmv1AaSt5fw2aHtHav7XC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5152,
      "cache_read_input_tokens": 47613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5152
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Grep · `toolu_01JRvuNDgsiZUkj3CfBAHiRw`</summary>

```json
{
  "pattern": "wang2023faireval|li2024calibraeval|tan2025judgebench|koo2024cobbler",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "38484e0f-041d-4df3-b4a7-48d4ea29c52c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014Qmv1AaSt5fw2aHtHav7XC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5152,
      "cache_read_input_tokens": 47613,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5152
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 18 · 2026-05-26T11:07:37.451Z_

<details><summary>↩ Tool result · `toolu_01JRvuNDgsiZUkj3CfBAHiRw`</summary>

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
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "acd25ba6-a889-4823-9a43-b33f4eaa12ba",
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

_source line 19_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ut6p1uLaL2tYmoJpq83ym7`</summary>

```json
{
  "pattern": "wang2023faireval|li2024calibraeval|tan2025judgebench|koo2024cobbler",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "954d9023-86af-4594-ba31-443daf3c0b9c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BuYYnufiZgoEDzyuGvEgRS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 330,
      "cache_read_input_tokens": 52765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 330
      },
      "output_tokens": 71,
      "service_tier": "standard",
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

_source line 20 · 2026-05-26T11:07:40.648Z_

<details><summary>↩ Tool result · `toolu_01Ut6p1uLaL2tYmoJpq83ym7`</summary>

```text
docs/paper/references.bib:163:@inproceedings{wang2023faireval,
docs/paper/references.bib:171:@inproceedings{li2024calibraeval,
docs/paper/references.bib:205:@inproceedings{tan2025judgebench,
docs/paper/references.bib:285:@inproceedings{koo2024cobbler,
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "7183b51b-0c48-446b-b630-fa5d70980229",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/references.bib:163:@inproceedings{wang2023faireval,\ndocs/paper/references.bib:171:@inproceedings{li2024calibraeval,\ndocs/paper/references.bib:205:@inproceedings{tan2025judgebench,\ndocs/paper/references.bib:285:@inproceedings{koo2024cobbler,",
    "numLines": 4
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "b16c889c-40ef-4f57-a07c-0f933353db0c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EnK1rXGXzR46zEeagGbCy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 53095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 22_

Now let me verify the modern ML papers via WebSearch. Running in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "fbdc89a5-f531-4972-8822-361fb381e789",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EnK1rXGXzR46zEeagGbCy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 53095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WCWF4ZXJKYXZYmhy8afsD5`</summary>

```json
{
  "query": "\"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback\" Dubois NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "9751dafa-77bd-4662-abc9-8dd02df0c38b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EnK1rXGXzR46zEeagGbCy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 53095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JhYt5RX9seXrrbs3mN1sGu`</summary>

```json
{
  "query": "\"Large Language Models are not Fair Evaluators\" Wang Peiyi ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "a27aca74-369c-4828-95df-eca9a9fd8940",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EnK1rXGXzR46zEeagGbCy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 53095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019FvJtDhPPAKg4ghdgYeWEN`</summary>

```json
{
  "query": "\"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias\" Li Haitao ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "ee8ee1ee-5cab-4e92-ad4d-dfcd28bb59f4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EnK1rXGXzR46zEeagGbCy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 53095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019cxnxCU8wUX7hFKGDF7Zqu`</summary>

```json
{
  "query": "\"Evaluating Large Language Models at Evaluating Instruction Following\" Zeng LLMBar ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "d32d010a-ac6f-433a-a79c-aa627c8458d5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EnK1rXGXzR46zEeagGbCy7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 343,
      "cache_read_input_tokens": 53095,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 343
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 27 · 2026-05-26T11:07:55.572Z_

<details><summary>↩ Tool result · `toolu_01JhYt5RX9seXrrbs3mN1sGu`</summary>

```text
Web search results for query: ""Large Language Models are not Fair Evaluators" Wang Peiyi ACL 2024"

Links: [{"title":"Large Language Models are not Fair Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.511/"},{"title":"Large Language Models are not Fair Evaluators | Request PDF","url":"https://www.researchgate.net/publication/384214634_Large_Language_Models_are_not_Fair_Evaluators"},{"title":"[2305.17926] Large Language Models are not Fair Evaluators","url":"https://arxiv.org/abs/2305.17926"},{"title":"Large Language Models are not Fair Evaluators","url":"https://aclanthology.org/2024.acl-long.511.pdf"},{"title":"Large Language Models are not Fair Evaluators - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2305.17926"},{"title":"[PDF] Large Language Models are not Fair Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-are-not-Fair-Evaluators-Wang-Li/38d64919ba526868a850a0e5f6239d4c474b7e7e"},{"title":"Large Language Models are not Fair Evaluators Peiyi Wang1 Lei Li1 Liang Chen1","url":"https://arxiv.org/pdf/2305.17926"},{"title":"[Quick Review] Large Language Models are not Fair Evaluators","url":"https://liner.com/review/large-language-models-are-not-fair-evaluators"},{"title":"Model grading • evalthat","url":"https://simonpcouch.github.io/evalthat/articles/model-grading.html"}]

I found the paper you're looking for! "Large Language Models are not Fair Evaluators" is a paper by Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu, Tianyu Liu, and Zhifang Sui, published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 9440–9450, Bangkok, Thailand in 2024.

The paper uncovers a positional bias in the evaluation paradigm of adopting large language models (LLMs), such as GPT-4, as a referee to score and compare the quality of responses generated by candidate models. The researchers find that the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context. As a demonstration, Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator.

To address this issue, the paper proposes a calibration framework with three strategies including Multiple Evidence Calibration, which successfully mitigates evaluation bias and results in closer alignment with human judgments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "aae41858-4796-4b46-a075-6a237235a23b",
  "tool_use_result": {
    "query": "\"Large Language Models are not Fair Evaluators\" Wang Peiyi ACL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jv3eUb7kK75yrMPW6gPGQC",
        "content": [
          {
            "title": "Large Language Models are not Fair Evaluators - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.511/"
          },
          {
            "title": "Large Language Models are not Fair Evaluators | Request PDF",
            "url": "https://www.researchgate.net/publication/384214634_Large_Language_Models_are_not_Fair_Evaluators"
          },
          {
            "title": "[2305.17926] Large Language Models are not Fair Evaluators",
            "url": "https://arxiv.org/abs/2305.17926"
          },
          {
            "title": "Large Language Models are not Fair Evaluators",
            "url": "https://aclanthology.org/2024.acl-long.511.pdf"
          },
          {
            "title": "Large Language Models are not Fair Evaluators - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/2305.17926"
          },
          {
            "title": "[PDF] Large Language Models are not Fair Evaluators | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Large-Language-Models-are-not-Fair-Evaluators-Wang-Li/38d64919ba526868a850a0e5f6239d4c474b7e7e"
          },
          {
            "title": "Large Language Models are not Fair Evaluators Peiyi Wang1 Lei Li1 Liang Chen1",
            "url": "https://arxiv.org/pdf/2305.17926"
          },
          {
            "title": "[Quick Review] Large Language Models are not Fair Evaluators",
            "url": "https://liner.com/review/large-language-models-are-not-fair-evaluators"
          },
          {
            "title": "Model grading • evalthat",
            "url": "https://simonpcouch.github.io/evalthat/articles/model-grading.html"
          }
        ]
      },
      "I found the paper you're looking for! \"Large Language Models are not Fair Evaluators\" is a paper by Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu, Tianyu Liu, and Zhifang Sui, published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 9440–9450, Bangkok, Thailand in 2024.\n\nThe paper uncovers a positional bias in the evaluation paradigm of adopting large language models (LLMs), such as GPT-4, as a referee to score and compare the quality of responses generated by candidate models. The researchers find that the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context. As a demonstration, Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator.\n\nTo address this issue, the paper proposes a calibration framework with three strategies including Multiple Evidence Calibration, which successfully mitigates evaluation bias and results in closer alignment with human judgments."
    ],
    "durationSeconds": 8.725284779
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T11:07:56.065Z_

<details><summary>↩ Tool result · `toolu_01WCWF4ZXJKYXZYmhy8afsD5`</summary>

```text
Web search results for query: ""AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback" Dubois NeurIPS 2023"

Links: [{"title":"NeurIPS Poster AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback","url":"https://neurips.cc/virtual/2023/poster/72842"},{"title":"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback","url":"https://proceedings.neurips.cc//paper_files/paper/2023/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html"},{"title":"[2305.14387] AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback","url":"https://arxiv.org/abs/2305.14387"},{"title":"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | OpenReview","url":"https://openreview.net/forum?id=4hturzLcKX"},{"title":"[PDF] AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AlpacaFarm:-A-Simulation-Framework-for-Methods-that-Dubois-Li/cb6cc7d28d06a0d7c0d3f0d7ee551bbc86dbc3aa"},{"title":"Xuechen Li, 10/05/23 AlpacaFarm A Simulation Framework for Methods that","url":"https://nips.cc/media/neurips-2023/Slides/72842_eQCLdQJ.pdf"},{"title":"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | Request PDF","url":"https://www.researchgate.net/publication/371009706_AlpacaFarm_A_Simulation_Framework_for_Methods_that_Learn_from_Human_Feedback"},{"title":"Xuechen Li, 10/05/23 AlpacaFarm A Simulation Framework for Methods that","url":"https://neurips.cc/media/neurips-2023/Slides/72842_eQCLdQJ.pdf"},{"title":"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback","url":"https://arxiv.org/html/2305.14387v4"}]

I found detailed information about the paper "AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback" by Dubois et al. from NeurIPS 2023.

## Summary

AlpacaFarm is a simulator that enables research and development for learning from feedback at a low cost. The research addresses three major challenges: the high cost of data collection, the lack of trustworthy evaluation, and the absence of reference method implementations.

## Key Components

The paper makes several contributions:

1. **Human Feedback Simulator**: The authors design an LLM-based simulator for human feedback that is 45x cheaper than crowdworkers and displays high agreement with humans.

2. **Evaluation Framework**: They identify an evaluation dataset representative of real-world instructions and propose an automatic evaluation procedure.

3. **Reference Implementations**: They contribute reference implementations for several methods (PPO, best-of-n, expert iteration, among others) that learn from pairwise feedback.

## Results and Impact

The authors train and evaluate eleven models on 10k pairs of human feedback and show that rankings of models trained in AlpacaFarm match rankings of models trained on human data. Methods that use a reward model can substantially improve over supervised fine-tuning and their reference PPO implementation leads to a +10% win-rate improvement against Davinci003.

The paper was published at NeurIPS 2023 and all components are available at https://github.com/tatsu-lab/alpaca_farm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "258d507b-963e-4856-8491-775bc60c0e46",
  "tool_use_result": {
    "query": "\"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback\" Dubois NeurIPS 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_016D4GpwWwGaZGyxn46nKoZx",
        "content": [
          {
            "title": "NeurIPS Poster AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback",
            "url": "https://neurips.cc/virtual/2023/poster/72842"
          },
          {
            "title": "AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback",
            "url": "https://proceedings.neurips.cc//paper_files/paper/2023/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html"
          },
          {
            "title": "[2305.14387] AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback",
            "url": "https://arxiv.org/abs/2305.14387"
          },
          {
            "title": "AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | OpenReview",
            "url": "https://openreview.net/forum?id=4hturzLcKX"
          },
          {
            "title": "[PDF] AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/AlpacaFarm:-A-Simulation-Framework-for-Methods-that-Dubois-Li/cb6cc7d28d06a0d7c0d3f0d7ee551bbc86dbc3aa"
          },
          {
            "title": "Xuechen Li, 10/05/23 AlpacaFarm A Simulation Framework for Methods that",
            "url": "https://nips.cc/media/neurips-2023/Slides/72842_eQCLdQJ.pdf"
          },
          {
            "title": "AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | Request PDF",
            "url": "https://www.researchgate.net/publication/371009706_AlpacaFarm_A_Simulation_Framework_for_Methods_that_Learn_from_Human_Feedback"
          },
          {
            "title": "Xuechen Li, 10/05/23 AlpacaFarm A Simulation Framework for Methods that",
            "url": "https://neurips.cc/media/neurips-2023/Slides/72842_eQCLdQJ.pdf"
          },
          {
            "title": "AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback",
            "url": "https://arxiv.org/html/2305.14387v4"
          }
        ]
      },
      "I found detailed information about the paper \"AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback\" by Dubois et al. from NeurIPS 2023.\n\n## Summary\n\nAlpacaFarm is a simulator that enables research and development for learning from feedback at a low cost. The research addresses three major challenges: the high cost of data collection, the lack of trustworthy evaluation, and the absence of reference method implementations.\n\n## Key Components\n\nThe paper makes several contributions:\n\n1. **Human Feedback Simulator**: The authors design an LLM-based simulator for human feedback that is 45x cheaper than crowdworkers and displays high agreement with humans.\n\n2. **Evaluation Framework**: They identify an evaluation dataset representative of real-world instructions and propose an automatic evaluation procedure.\n\n3. **Reference Implementations**: They contribute reference implementations for several methods (PPO, best-of-n, expert iteration, among others) that learn from pairwise feedback.\n\n## Results and Impact\n\nThe authors train and evaluate eleven models on 10k pairs of human feedback and show that rankings of models trained in AlpacaFarm match rankings of models trained on human data. Methods that use a reward model can substantially improve over supervised fine-tuning and their reference PPO implementation leads to a +10% win-rate improvement against Davinci003.\n\nThe paper was published at NeurIPS 2023 and all components are available at https://github.com/tatsu-lab/alpaca_farm."
    ],
    "durationSeconds": 9.653386271999995
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-26T11:07:57.898Z_

<details><summary>↩ Tool result · `toolu_019cxnxCU8wUX7hFKGDF7Zqu`</summary>

```text
Web search results for query: ""Evaluating Large Language Models at Evaluating Instruction Following" Zeng LLMBar ICLR 2024"

Links: [{"title":"GitHub - princeton-nlp/LLMBar: [ICLR 2024] Evaluating Large Language Models at Evaluating Instruction Following · GitHub","url":"https://github.com/princeton-nlp/LLMBar"},{"title":"ICLR Poster Evaluating Large Language Models at Evaluating Instruction Following","url":"https://iclr.cc/virtual/2024/poster/17598"},{"title":"EVALUATING LARGE LANGUAGE MODELS AT EVALUATING INSTRUCTION FOLLOWING - Princeton University","url":"https://collaborate.princeton.edu/en/publications/evaluating-large-language-models-at-evaluating-instruction-follow/"},{"title":"EVALUATING LARGE LANGUAGE MODELS AT ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf"},{"title":"[2310.07641] Evaluating Large Language Models at Evaluating Instruction Following","url":"https://arxiv.org/abs/2310.07641"},{"title":"Evaluating Large Language Models at Evaluating Instruction Following | OpenReview","url":"https://openreview.net/forum?id=tr0KidwPLc"},{"title":"LLMBar/LLMEvaluator/evaluators/prompts/comparison/Vanilla.txt at main · princeton-nlp/LLMBar","url":"https://github.com/princeton-nlp/LLMBar/blob/main/LLMEvaluator/evaluators/prompts/comparison/Vanilla.txt"},{"title":"EVALUATING THE INSTRUCTION-FOLLOWING ABIL","url":"https://openreview.net/pdf?id=qit4pa6PpY"},{"title":"Evaluating Large Language Models at Evaluating Instruction Following | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/evaluating-large-language-models-at-evaluating-instruction"},{"title":"dblp: Evaluating Large Language Models at Evaluating Instruction Following.","url":"https://dblp.org/rec/conf/iclr/ZengYG0G024.html"}]

I found comprehensive information about this paper. Here's what I found:

## Paper Overview

This is a paper by Zhiyuan Zeng, Jiatong Yu, Tianyu Gao, Yu Meng, Tanya Goyal, and Danqi Chen, published at ICLR 2024, titled "Evaluating Large Language Models at Evaluating Instruction Following."

## Research Focus

The paper investigates the efficacy of "LLM evaluators", particularly in using them to assess instruction following, a metric that gauges how closely generated text adheres to the given instruction.

## The LLMBar Benchmark

The paper introduces a challenging meta-evaluation benchmark called LLMBar, designed to test the ability of an LLM evaluator in discerning instruction-following outputs. LLMBar consists of 419 instances, where each entry contains an instruction paired with two outputs: one faithfully and correctly follows the instruction and the other deviates from it.

The authors manually curated 419 pairs of outputs, one adhering to instructions while the other diverging, yet may possess deceptive qualities that mislead an LLM evaluator, e.g., a more engaging tone.

## Key Findings

The paper discovers that different evaluators (combinations of LLMs and prompts) exhibit distinct performance on LLMBar and even the highest-scoring ones have substantial room for improvement.

## Resources

The data and code for this paper are available at a public repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "0416bddf-b4a0-44bf-b6ff-f770a0c6d059",
  "tool_use_result": {
    "query": "\"Evaluating Large Language Models at Evaluating Instruction Following\" Zeng LLMBar ICLR 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_012eAtVtPLoebzhVgDZD4uok",
        "content": [
          {
            "title": "GitHub - princeton-nlp/LLMBar: [ICLR 2024] Evaluating Large Language Models at Evaluating Instruction Following · GitHub",
            "url": "https://github.com/princeton-nlp/LLMBar"
          },
          {
            "title": "ICLR Poster Evaluating Large Language Models at Evaluating Instruction Following",
            "url": "https://iclr.cc/virtual/2024/poster/17598"
          },
          {
            "title": "EVALUATING LARGE LANGUAGE MODELS AT EVALUATING INSTRUCTION FOLLOWING - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/evaluating-large-language-models-at-evaluating-instruction-follow/"
          },
          {
            "title": "EVALUATING LARGE LANGUAGE MODELS AT ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/afc8b034823271816d14f7c1aefe1dff-Paper-Conference.pdf"
          },
          {
            "title": "[2310.07641] Evaluating Large Language Models at Evaluating Instruction Following",
            "url": "https://arxiv.org/abs/2310.07641"
          },
          {
            "title": "Evaluating Large Language Models at Evaluating Instruction Following | OpenReview",
            "url": "https://openreview.net/forum?id=tr0KidwPLc"
          },
          {
            "title": "LLMBar/LLMEvaluator/evaluators/prompts/comparison/Vanilla.txt at main · princeton-nlp/LLMBar",
            "url": "https://github.com/princeton-nlp/LLMBar/blob/main/LLMEvaluator/evaluators/prompts/comparison/Vanilla.txt"
          },
          {
            "title": "EVALUATING THE INSTRUCTION-FOLLOWING ABIL",
            "url": "https://openreview.net/pdf?id=qit4pa6PpY"
          },
          {
            "title": "Evaluating Large Language Models at Evaluating Instruction Following | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/evaluating-large-language-models-at-evaluating-instruction"
          },
          {
            "title": "dblp: Evaluating Large Language Models at Evaluating Instruction Following.",
            "url": "https://dblp.org/rec/conf/iclr/ZengYG0G024.html"
          }
        ]
      },
      "I found comprehensive information about this paper. Here's what I found:\n\n## Paper Overview\n\nThis is a paper by Zhiyuan Zeng, Jiatong Yu, Tianyu Gao, Yu Meng, Tanya Goyal, and Danqi Chen, published at ICLR 2024, titled \"Evaluating Large Language Models at Evaluating Instruction Following.\"\n\n## Research Focus\n\nThe paper investigates the efficacy of \"LLM evaluators\", particularly in using them to assess instruction following, a metric that gauges how closely generated text adheres to the given instruction.\n\n## The LLMBar Benchmark\n\nThe paper introduces a challenging meta-evaluation benchmark called LLMBar, designed to test the ability of an LLM evaluator in discerning instruction-following outputs. LLMBar consists of 419 instances, where each entry contains an instruction paired with two outputs: one faithfully and correctly follows the instruction and the other deviates from it.\n\nThe authors manually curated 419 pairs of outputs, one adhering to instructions while the other diverging, yet may possess deceptive qualities that mislead an LLM evaluator, e.g., a more engaging tone.\n\n## Key Findings\n\nThe paper discovers that different evaluators (combinations of LLMs and prompts) exhibit distinct performance on LLMBar and even the highest-scoring ones have substantial room for improvement.\n\n## Resources\n\nThe data and code for this paper are available at a public repository."
    ],
    "durationSeconds": 9.84486348
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T11:07:58.631Z_

<details><summary>↩ Tool result · `toolu_019FvJtDhPPAKg4ghdgYeWEN`</summary>

```text
Web search results for query: ""CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias" Li Haitao ACL 2025"

Links: [{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.808/"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate ...","url":"https://aclanthology.org/2025.acl-long.808.pdf"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges | Request PDF","url":"https://www.researchgate.net/publication/394299911_CalibraEval_Calibrating_Prediction_Distribution_to_Mitigate_Selection_Bias_in_LLMs-as-Judges"},{"title":"dblp: CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges.","url":"https://dblp.org/rec/conf/acl/0006CAC0D025.html"},{"title":"‪Calibraeval: Calibrating prediction distribution to mitigate selection bias in llms-as-judges‬","url":"https://scholar.google.com/citations?view_op=view_citation&hl=en&user=m88SZGgAAAAJ&citation_for_view=m88SZGgAAAAJ:f2IySw72cVMC"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges","url":"https://arxiv.org/html/2410.15393v1"},{"title":"[2410.15393] CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges","url":"https://arxiv.org/abs/2410.15393"},{"title":"GitHub - CSHaitao/CalibraEval: The official repo for CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges","url":"https://github.com/CSHaitao/CalibraEval"}]

I found the paper! Here are the key details:

**CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges** was authored by Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, Qian Dong, and Yiqun Liu, and published at ACL 2025. The paper appears in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 16537–16552, Vienna, Austria.

**Overview:**
Large language models (LLMs) are increasingly used as automated evaluation tools to assess the quality of generated natural language (known as LLMs-as-Judges), but when applied to pairwise comparisons, LLM-based evaluators often exhibit selection bias. Specifically, their judgments may become inconsistent when the option positions or ID tokens are swapped, compromising the effectiveness and fairness of the evaluation result.

**The Approach:**
CalibraEval is a label-free, inference-time method for mitigating selection bias that reformulates the debiasing problem as an optimization task to build a projection function that maps the original prediction distribution to an unbiased distribution. The authors propose a non-parametric order-preserving algorithm (NOA) that leverages the partial order relationships between model prediction distributions, thereby eliminating the need for explicit labels and precise mathematical function modeling.

**Results:**
Empirical evaluations of LLMs in multiple representative benchmarks demonstrate that CalibraEval effectively mitigates selection bias and improves performance compared to existing debiasing methods.

The code is available at https://github.com/CSHaitao/CalibraEval.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "c97965bd-dcfc-4d7f-ae9b-5b8a22bf8dc9",
  "tool_use_result": {
    "query": "\"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias\" Li Haitao ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013TZgqhmDeAsQsfPqFnmTkm",
        "content": [
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.808/"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate ...",
            "url": "https://aclanthology.org/2025.acl-long.808.pdf"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges | Request PDF",
            "url": "https://www.researchgate.net/publication/394299911_CalibraEval_Calibrating_Prediction_Distribution_to_Mitigate_Selection_Bias_in_LLMs-as-Judges"
          },
          {
            "title": "dblp: CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges.",
            "url": "https://dblp.org/rec/conf/acl/0006CAC0D025.html"
          },
          {
            "title": "‪Calibraeval: Calibrating prediction distribution to mitigate selection bias in llms-as-judges‬",
            "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=m88SZGgAAAAJ&citation_for_view=m88SZGgAAAAJ:f2IySw72cVMC"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges",
            "url": "https://arxiv.org/html/2410.15393v1"
          },
          {
            "title": "[2410.15393] CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges",
            "url": "https://arxiv.org/abs/2410.15393"
          },
          {
            "title": "GitHub - CSHaitao/CalibraEval: The official repo for CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges",
            "url": "https://github.com/CSHaitao/CalibraEval"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\n**CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges** was authored by Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, Qian Dong, and Yiqun Liu, and published at ACL 2025. The paper appears in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 16537–16552, Vienna, Austria.\n\n**Overview:**\nLarge language models (LLMs) are increasingly used as automated evaluation tools to assess the quality of generated natural language (known as LLMs-as-Judges), but when applied to pairwise comparisons, LLM-based evaluators often exhibit selection bias. Specifically, their judgments may become inconsistent when the option positions or ID tokens are swapped, compromising the effectiveness and fairness of the evaluation result.\n\n**The Approach:**\nCalibraEval is a label-free, inference-time method for mitigating selection bias that reformulates the debiasing problem as an optimization task to build a projection function that maps the original prediction distribution to an unbiased distribution. The authors propose a non-parametric order-preserving algorithm (NOA) that leverages the partial order relationships between model prediction distributions, thereby eliminating the need for explicit labels and precise mathematical function modeling.\n\n**Results:**\nEmpirical evaluations of LLMs in multiple representative benchmarks demonstrate that CalibraEval effectively mitigates selection bias and improves performance compared to existing debiasing methods.\n\nThe code is available at https://github.com/CSHaitao/CalibraEval."
    ],
    "durationSeconds": 11.285794953999996
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "2cad9885-27a3-4a86-aba7-8e37443ce318",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015hpGfpBTDSajNxC3UkUZMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1408,
      "cache_creation_input_tokens": 4718,
      "cache_read_input_tokens": 53438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4718
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X3c4ebKHaoy5vSCTDL4AMD`</summary>

```json
{
  "query": "\"Adapting Text Embeddings for Causal Inference\" Veitch UAI 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "8ea1483a-1855-4ee6-984f-8e7502541b7b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015hpGfpBTDSajNxC3UkUZMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1408,
      "cache_creation_input_tokens": 4718,
      "cache_read_input_tokens": 53438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4718
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DHDSJ3q4riSD7ieewZPjQ6`</summary>

```json
{
  "query": "\"JudgeBench: A Benchmark for Evaluating LLM-based Judges\" Tan ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "01782f3c-cda0-4ab2-9e6c-35dbb8b854dd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015hpGfpBTDSajNxC3UkUZMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1408,
      "cache_creation_input_tokens": 4718,
      "cache_read_input_tokens": 53438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4718
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S2GifQWRQXC97Bm3s5UdHi`</summary>

```json
{
  "query": "\"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\" Chiang ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "5e41ce1a-61a2-41f4-9f4f-c9d921b74d4a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015hpGfpBTDSajNxC3UkUZMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1408,
      "cache_creation_input_tokens": 4718,
      "cache_read_input_tokens": 53438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4718
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013LifdwMPcpRVkvBdzyHgFx`</summary>

```json
{
  "query": "\"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" Ye ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "443d3c36-ef52-4abc-82aa-6de4b570db64",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_015hpGfpBTDSajNxC3UkUZMm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1408,
      "cache_creation_input_tokens": 4718,
      "cache_read_input_tokens": 53438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4718
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 36 · 2026-05-26T11:08:12.942Z_

<details><summary>↩ Tool result · `toolu_01X3c4ebKHaoy5vSCTDL4AMD`</summary>

```text
Web search results for query: ""Adapting Text Embeddings for Causal Inference" Veitch UAI 2020"

Links: [{"title":"Adapting Text Embeddings for Causal Inference","url":"https://proceedings.mlr.press/v124/veitch20a.html"},{"title":"Adapting Text Embeddings for Causal Inference Victor Veitch∗ Dhanya Sridhar∗","url":"http://www.cs.columbia.edu/~blei/papers/VeitchSridharBlei2020.pdf"},{"title":"Adapting Text Embeddings for Causal Inference | Dhanya Sridhar","url":"https://dsridhar91.github.io/publication/uai-20/"},{"title":"[1905.12741] Adapting Text Embeddings for Causal Inference","url":"https://arxiv.org/abs/1905.12741"},{"title":"Adapting Text Embeddings for Causal Inference","url":"https://papertalk.org/papertalks/13750"},{"title":"[PDF] Adapting Text Embeddings for Causal Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adapting-Text-Embeddings-for-Causal-Inference-Veitch-Sridhar/09428af106c378616d7767a37c4f4070a2664e5a"},{"title":"Dhanya Sridhar - Adapting Text Embeddings for Causal Inference","url":"https://www.dsridhar.com/publications/6361-adapting-text-embeddings-for-causal-inference"},{"title":"[PDF] Using Text Embeddings for Causal Inference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Using-Text-Embeddings-for-Causal-Inference-Veitch-Sridhar/298b72096b8a770b0cdb263dd53cf2463b8a1a1d"},{"title":"Using Text Embeddings for Causal Inference","url":"https://www.arxiv.org/pdf/1905.12741v1"},{"title":"Adapting Text Embeddings for Causal Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190512741V/abstract"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Adapting Text Embeddings for Causal Inference

**Authors:** Victor Veitch, Dhanya Sridhar, and David Blei

**Publication:** Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI), PMLR 124:919-928, 2020

**Summary:** The paper develops a method to estimate causal effects from observational text data, adjusting for confounding features of the text such as the subject or writing quality. The authors develop causally sufficient embeddings, low-dimensional document representations that preserve sufficient information for causal identification and allow for efficient estimation of causal effects.

**Methodology:** The approach combines supervised dimensionality reduction (causal adjustment requires only the aspects of text that are predictive of both treatment and outcome) and efficient language modeling (representations of text are designed to dispose of linguistically irrelevant information). The method adapts language models (specifically, word embeddings and topic models) to learn document embeddings that are able to predict both treatment and outcome.

**Applications:** The methods are illustrated by answering questions about the effect of a theorem on paper acceptance and the effect of a gender label on post popularity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "c73b12b1-f79b-4a13-8573-227c812334d5",
  "tool_use_result": {
    "query": "\"Adapting Text Embeddings for Causal Inference\" Veitch UAI 2020",
    "results": [
      {
        "tool_use_id": "srvtoolu_017D8uGzWsHz9KNYFaoqCYYf",
        "content": [
          {
            "title": "Adapting Text Embeddings for Causal Inference",
            "url": "https://proceedings.mlr.press/v124/veitch20a.html"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference Victor Veitch∗ Dhanya Sridhar∗",
            "url": "http://www.cs.columbia.edu/~blei/papers/VeitchSridharBlei2020.pdf"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference | Dhanya Sridhar",
            "url": "https://dsridhar91.github.io/publication/uai-20/"
          },
          {
            "title": "[1905.12741] Adapting Text Embeddings for Causal Inference",
            "url": "https://arxiv.org/abs/1905.12741"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference",
            "url": "https://papertalk.org/papertalks/13750"
          },
          {
            "title": "[PDF] Adapting Text Embeddings for Causal Inference | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Adapting-Text-Embeddings-for-Causal-Inference-Veitch-Sridhar/09428af106c378616d7767a37c4f4070a2664e5a"
          },
          {
            "title": "Dhanya Sridhar - Adapting Text Embeddings for Causal Inference",
            "url": "https://www.dsridhar.com/publications/6361-adapting-text-embeddings-for-causal-inference"
          },
          {
            "title": "[PDF] Using Text Embeddings for Causal Inference | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Using-Text-Embeddings-for-Causal-Inference-Veitch-Sridhar/298b72096b8a770b0cdb263dd53cf2463b8a1a1d"
          },
          {
            "title": "Using Text Embeddings for Causal Inference",
            "url": "https://www.arxiv.org/pdf/1905.12741v1"
          },
          {
            "title": "Adapting Text Embeddings for Causal Inference - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2019arXiv190512741V/abstract"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Paper Title:** Adapting Text Embeddings for Causal Inference\n\n**Authors:** Victor Veitch, Dhanya Sridhar, and David Blei\n\n**Publication:** Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI), PMLR 124:919-928, 2020\n\n**Summary:** The paper develops a method to estimate causal effects from observational text data, adjusting for confounding features of the text such as the subject or writing quality. The authors develop causally sufficient embeddings, low-dimensional document representations that preserve sufficient information for causal identification and allow for efficient estimation of causal effects.\n\n**Methodology:** The approach combines supervised dimensionality reduction (causal adjustment requires only the aspects of text that are predictive of both treatment and outcome) and efficient language modeling (representations of text are designed to dispose of linguistically irrelevant information). The method adapts language models (specifically, word embeddings and topic models) to learn document embeddings that are able to predict both treatment and outcome.\n\n**Applications:** The methods are illustrated by answering questions about the effect of a theorem on paper acceptance and the effect of a gender label on post popularity."
    ],
    "durationSeconds": 8.603801214999999
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-26T11:08:13.495Z_

<details><summary>↩ Tool result · `toolu_01S2GifQWRQXC97Bm3s5UdHi`</summary>

```text
Web search results for query: ""Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference" Chiang ICML 2024"

Links: [{"title":"[2403.04132] Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference","url":"https://arxiv.org/abs/2403.04132"},{"title":"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference","url":"https://proceedings.mlr.press/v235/chiang24b.html"},{"title":"Chatbot arena: an open platform for evaluating LLMs ...","url":"https://dl.acm.org/doi/abs/10.5555/3692070.3692401"},{"title":"[PDF] Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Chatbot-Arena:-An-Open-Platform-for-Evaluating-LLMs-Chiang-Zheng/53f4fb0e9972989194368faf288ff8e3cba5bd60"},{"title":"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference","url":"https://arxiv.org/html/2403.04132v1"},{"title":"ICML Poster Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference","url":"https://icml.cc/virtual/2024/poster/35068"},{"title":"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | OpenReview","url":"https://openreview.net/forum?id=3MW8GKNyzI"},{"title":"Chatbot Arena An Open Platform for Evaluating LLMs by Human Preference","url":"https://icml.cc/media/icml-2024/Slides/35068.pdf"},{"title":"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference - researchr publication","url":"https://researchr.org/publication/ChiangZ0ALLZ0JG24"}]

I found the paper you're looking for! Here's the information:

"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference" was published by Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E. Gonzalez, and Ion Stoica in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024).

The paper addresses the challenge of evaluating large language models' alignment with human preferences by introducing Chatbot Arena, which employs a pairwise comparison approach and leverages input from a diverse user base through crowdsourcing. The platform has amassed over 240K votes, and the paper describes the platform, analyzes the collected data, and explains the statistical methods used for efficient and accurate evaluation and ranking of models.

The platform is publicly available at https://chat.lmsys.org.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "237ebaf3-aa88-4ccb-8bd6-7028501f2857",
  "tool_use_result": {
    "query": "\"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\" Chiang ICML 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_015f5gWdP3oDJcxFBKmfVcSc",
        "content": [
          {
            "title": "[2403.04132] Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference",
            "url": "https://arxiv.org/abs/2403.04132"
          },
          {
            "title": "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference",
            "url": "https://proceedings.mlr.press/v235/chiang24b.html"
          },
          {
            "title": "Chatbot arena: an open platform for evaluating LLMs ...",
            "url": "https://dl.acm.org/doi/abs/10.5555/3692070.3692401"
          },
          {
            "title": "[PDF] Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Chatbot-Arena:-An-Open-Platform-for-Evaluating-LLMs-Chiang-Zheng/53f4fb0e9972989194368faf288ff8e3cba5bd60"
          },
          {
            "title": "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference",
            "url": "https://arxiv.org/html/2403.04132v1"
          },
          {
            "title": "ICML Poster Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference",
            "url": "https://icml.cc/virtual/2024/poster/35068"
          },
          {
            "title": "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | OpenReview",
            "url": "https://openreview.net/forum?id=3MW8GKNyzI"
          },
          {
            "title": "Chatbot Arena An Open Platform for Evaluating LLMs by Human Preference",
            "url": "https://icml.cc/media/icml-2024/Slides/35068.pdf"
          },
          {
            "title": "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference - researchr publication",
            "url": "https://researchr.org/publication/ChiangZ0ALLZ0JG24"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information:\n\n\"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\" was published by Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E. Gonzalez, and Ion Stoica in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024).\n\nThe paper addresses the challenge of evaluating large language models' alignment with human preferences by introducing Chatbot Arena, which employs a pairwise comparison approach and leverages input from a diverse user base through crowdsourcing. The platform has amassed over 240K votes, and the paper describes the platform, analyzes the collected data, and explains the statistical methods used for efficient and accurate evaluation and ranking of models.\n\nThe platform is publicly available at https://chat.lmsys.org."
    ],
    "durationSeconds": 7.417350656999996
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-26T11:08:13.850Z_

<details><summary>↩ Tool result · `toolu_01DHDSJ3q4riSD7ieewZPjQ6`</summary>

```text
Web search results for query: ""JudgeBench: A Benchmark for Evaluating LLM-based Judges" Tan ICLR 2025"

Links: [{"title":"[2410.12784] JudgeBench: A Benchmark for Evaluating LLM-based Judges","url":"https://arxiv.org/abs/2410.12784"},{"title":"Published as a conference paper at ICLR 2025 JUDGEBENCH: A BENCHMARK","url":"https://arxiv.org/pdf/2410.12784"},{"title":"JudgeBench: A Benchmark for Evaluating LLM-Based Judges","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/9e720fce64f91114c49cfd640d821da3-Abstract-Conference.html"},{"title":"JudgeBench: A Benchmark for Evaluating LLM-Based Judges | OpenReview","url":"https://openreview.net/forum?id=G0dksFayVq"},{"title":"dblp: JudgeBench: A Benchmark for Evaluating LLM-Based Judges.","url":"https://dblp.org/rec/conf/iclr/TanZMTC0PS25.html"},{"title":"JUDGEBENCH: A BENCHMARK FOR EVALUATING LLM-BASED JUDGES - WashU Medicine Research Profiles","url":"https://profiles.wustl.edu/en/publications/judgebench-a-benchmark-for-evaluating-llm-based-judges/"},{"title":"JudgeBench: Evaluating LLM Judges","url":"https://www.emergentmind.com/topics/judgebench-dataset"},{"title":"[2410.12784v1] JudgeBench: A Benchmark for Evaluating LLM-based Judges","url":"https://arxiv.org/abs/2410.12784v1"},{"title":"[PDF] JudgeBench: A Benchmark for Evaluating LLM-based Judges | Semantic Scholar","url":"https://www.semanticscholar.org/paper/JudgeBench:-A-Benchmark-for-Evaluating-LLM-based-Tan-Zhuang/088ab579bf490691eea7ac92e122ee11c9b9d131"}]

I found information about "JudgeBench: A Benchmark for Evaluating LLM-based Judges" by Tan and colleagues, which was published at ICLR 2025.

## Overview

JudgeBench is a benchmark for evaluating LLM-based judges on challenging response pairs spanning knowledge, reasoning, math, and coding. LLM-based judges have emerged as a scalable alternative to human evaluation and are increasingly used to assess, compare, and improve models, but the reliability of LLM-based judges themselves is rarely scrutinized.

## Key Methodology

JudgeBench leverages a novel pipeline for converting existing difficult datasets into challenging response pairs with preference labels reflecting objective correctness. Labeling strictly uses dataset ground-truth and dual-verification: correctness requires the candidate to pass both the automated check and LLM-based secondary verification, eliminating reliance on subjective human preference labels.

## Key Findings

Comprehensive evaluation on a collection of prompted judges, fine-tuned judges, multi-agent judges, and reward models shows that JudgeBench poses a significantly greater challenge than previous benchmarks, with many strong models (e.g., GPT-4o) performing just slightly better than random guessing. More specifically, the strongest model on JudgeBench achieves only 64% accuracy, the lowest among all five datasets.

## Publication Details

The paper was published at ICLR 2025 (April 24-28, 2025 in Singapore). Data and code are available at https://github.com/ScalerLab/JudgeBench.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "076890b2-e95e-40b7-b591-6be978be58ee",
  "tool_use_result": {
    "query": "\"JudgeBench: A Benchmark for Evaluating LLM-based Judges\" Tan ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sb2LACapPGFR62EQL3gVya",
        "content": [
          {
            "title": "[2410.12784] JudgeBench: A Benchmark for Evaluating LLM-based Judges",
            "url": "https://arxiv.org/abs/2410.12784"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 JUDGEBENCH: A BENCHMARK",
            "url": "https://arxiv.org/pdf/2410.12784"
          },
          {
            "title": "JudgeBench: A Benchmark for Evaluating LLM-Based Judges",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/9e720fce64f91114c49cfd640d821da3-Abstract-Conference.html"
          },
          {
            "title": "JudgeBench: A Benchmark for Evaluating LLM-Based Judges | OpenReview",
            "url": "https://openreview.net/forum?id=G0dksFayVq"
          },
          {
            "title": "dblp: JudgeBench: A Benchmark for Evaluating LLM-Based Judges.",
            "url": "https://dblp.org/rec/conf/iclr/TanZMTC0PS25.html"
          },
          {
            "title": "JUDGEBENCH: A BENCHMARK FOR EVALUATING LLM-BASED JUDGES - WashU Medicine Research Profiles",
            "url": "https://profiles.wustl.edu/en/publications/judgebench-a-benchmark-for-evaluating-llm-based-judges/"
          },
          {
            "title": "JudgeBench: Evaluating LLM Judges",
            "url": "https://www.emergentmind.com/topics/judgebench-dataset"
          },
          {
            "title": "[2410.12784v1] JudgeBench: A Benchmark for Evaluating LLM-based Judges",
            "url": "https://arxiv.org/abs/2410.12784v1"
          },
          {
            "title": "[PDF] JudgeBench: A Benchmark for Evaluating LLM-based Judges | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/JudgeBench:-A-Benchmark-for-Evaluating-LLM-based-Tan-Zhuang/088ab579bf490691eea7ac92e122ee11c9b9d131"
          }
        ]
      },
      "I found information about \"JudgeBench: A Benchmark for Evaluating LLM-based Judges\" by Tan and colleagues, which was published at ICLR 2025.\n\n## Overview\n\nJudgeBench is a benchmark for evaluating LLM-based judges on challenging response pairs spanning knowledge, reasoning, math, and coding. LLM-based judges have emerged as a scalable alternative to human evaluation and are increasingly used to assess, compare, and improve models, but the reliability of LLM-based judges themselves is rarely scrutinized.\n\n## Key Methodology\n\nJudgeBench leverages a novel pipeline for converting existing difficult datasets into challenging response pairs with preference labels reflecting objective correctness. Labeling strictly uses dataset ground-truth and dual-verification: correctness requires the candidate to pass both the automated check and LLM-based secondary verification, eliminating reliance on subjective human preference labels.\n\n## Key Findings\n\nComprehensive evaluation on a collection of prompted judges, fine-tuned judges, multi-agent judges, and reward models shows that JudgeBench poses a significantly greater challenge than previous benchmarks, with many strong models (e.g., GPT-4o) performing just slightly better than random guessing. More specifically, the strongest model on JudgeBench achieves only 64% accuracy, the lowest among all five datasets.\n\n## Publication Details\n\nThe paper was published at ICLR 2025 (April 24-28, 2025 in Singapore). Data and code are available at https://github.com/ScalerLab/JudgeBench."
    ],
    "durationSeconds": 9.043567352999998
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-26T11:08:17.137Z_

<details><summary>↩ Tool result · `toolu_013LifdwMPcpRVkvBdzyHgFx`</summary>

```text
Web search results for query: ""Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" Ye ICLR 2025"

Links: [{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge | OpenReview","url":"https://openreview.net/forum?id=3GTtZFiajM"},{"title":"JUSTICE OR PREJUDICE? QUANTIFYING BIASES IN LLM-AS-A-JUDGE for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge - Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang - ICLR, 2025 | Publications | News & Events | Ethics and the Common Good | University of Notre Dame","url":"https://ethics.nd.edu/news-and-events/publications/jiayi-ye-yanbo-wang-yue-huang-dongping-chen-qihui-zhang-nuno-moniz-tian-gao-werner-geyer-chao-huang-pin-yu-chen-nitesh-v-chawla-xiangliang-zhang-iclr-2025-justice-or-prejudice-quantifying-biases-in-llm-as-a-judge/"},{"title":"[2410.02736] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.02736"},{"title":"ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://iclr.cc/virtual/2025/poster/31088"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://llm-judge-bias.github.io/"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html"},{"title":"(PDF) Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://www.researchgate.net/publication/384630680_Justice_or_Prejudice_Quantifying_Biases_in_LLM-as-a-Judge"}]

I found the paper you're looking for! Here's what the search reveals:

## Overview

"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" is a paper by Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh Chawla, and Xiangliang Zhang presented at ICLR 2025.

## Key Contributions

The paper identifies 12 key potential biases and proposes a new automated bias quantification framework called CALM, which systematically quantifies and analyzes each type of bias in LLM-as-a-Judge by using automated and principle-guided modification.

## Main Findings

While LLM-as-a-Judge has been widely utilized as an evaluation method in various benchmarks and served as supervised rewards in model training, despite their excellence in many domains, potential issues are under-explored, undermining their reliability and the scope of their utility.

The experiments cover multiple popular language models, and the results indicate that while advanced models have achieved commendable overall performance, significant biases persist in certain specific tasks.

The paper is available on multiple platforms including OpenReview, arXiv (2410.02736), the ICLR proceedings, and a dedicated project website at llm-judge-bias.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "ad0991fd-61a6-4c67-8ae8-5f0f2a0f3dc3",
  "tool_use_result": {
    "query": "\"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" Ye ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011Xha4fAszGuogqmG78KHDW",
        "content": [
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge | OpenReview",
            "url": "https://openreview.net/forum?id=3GTtZFiajM"
          },
          {
            "title": "JUSTICE OR PREJUDICE? QUANTIFYING BIASES IN LLM-AS-A-JUDGE for ICLR 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge - Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang - ICLR, 2025 | Publications | News & Events | Ethics and the Common Good | University of Notre Dame",
            "url": "https://ethics.nd.edu/news-and-events/publications/jiayi-ye-yanbo-wang-yue-huang-dongping-chen-qihui-zhang-nuno-moniz-tian-gao-werner-geyer-chao-huang-pin-yu-chen-nitesh-v-chawla-xiangliang-zhang-iclr-2025-justice-or-prejudice-quantifying-biases-in-llm-as-a-judge/"
          },
          {
            "title": "[2410.02736] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2410.02736"
          },
          {
            "title": "ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://iclr.cc/virtual/2025/poster/31088"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2410.02736v1"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://llm-judge-bias.github.io/"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html"
          },
          {
            "title": "(PDF) Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/384630680_Justice_or_Prejudice_Quantifying_Biases_in_LLM-as-a-Judge"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search reveals:\n\n## Overview\n\n\"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" is a paper by Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh Chawla, and Xiangliang Zhang presented at ICLR 2025.\n\n## Key Contributions\n\nThe paper identifies 12 key potential biases and proposes a new automated bias quantification framework called CALM, which systematically quantifies and analyzes each type of bias in LLM-as-a-Judge by using automated and principle-guided modification.\n\n## Main Findings\n\nWhile LLM-as-a-Judge has been widely utilized as an evaluation method in various benchmarks and served as supervised rewards in model training, despite their excellence in many domains, potential issues are under-explored, undermining their reliability and the scope of their utility.\n\nThe experiments cover multiple popular language models, and the results indicate that while advanced models have achieved commendable overall performance, significant biases persist in certain specific tasks.\n\nThe paper is available on multiple platforms including OpenReview, arXiv (2410.02736), the ICLR proceedings, and a dedicated project website at llm-judge-bias.github.io."
    ],
    "durationSeconds": 10.855399611000001
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TMCnrsKdsRA6NqcTCMQdaD`</summary>

```json
{
  "query": "\"CausaLM: Causal Model Explanation Through Counterfactual Language Models\" Feder Computational Linguistics 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "2e2a8b5f-53da-4188-a372-fc73babda679",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011ZUT7e61vTcVXMutMv7RW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7325,
      "cache_read_input_tokens": 58156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7325
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E15sM1kkNYX9qxBVFpVwon`</summary>

```json
{
  "query": "\"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models\" Wu Ribeiro ACL 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "44099321-df49-4fc7-80c2-4e4a6f0bc7b5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011ZUT7e61vTcVXMutMv7RW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7325,
      "cache_read_input_tokens": 58156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7325
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FGzRwVFJroHrVWoGmSUUTw`</summary>

```json
{
  "query": "\"The Use of Rating and Likert Scales in Natural Language Generation Human Evaluation Tasks\" Amidei INLG 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "044efbe1-c954-46fb-a4ea-5de73b2dbc1a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011ZUT7e61vTcVXMutMv7RW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7325,
      "cache_read_input_tokens": 58156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7325
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U6eHzUpbHNH2uzJaiNe3My`</summary>

```json
{
  "query": "\"Style Over Substance: Evaluation Biases for Large Language Models\" Wu Aji COLING 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "7fab5b71-0d7a-4375-a18b-52c04847e9f8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011ZUT7e61vTcVXMutMv7RW6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7325,
      "cache_read_input_tokens": 58156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7325
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 44 · 2026-05-26T11:08:28.522Z_

<details><summary>↩ Tool result · `toolu_01E15sM1kkNYX9qxBVFpVwon`</summary>

```text
Web search results for query: ""Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models" Wu Ribeiro ACL 2021"

Links: [{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models - ACL Anthology","url":"https://aclanthology.org/2021.acl-long.523/"},{"title":"[PDF] Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Polyjuice:-Generating-Counterfactuals-for-and-Wu-Ribeiro/15e71e497a67423bfedd0d63efe423c4660e5053"},{"title":"[2101.00288] Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models","url":"https://arxiv.org/abs/2101.00288"},{"title":"GitHub - tongshuangwu/polyjuice · GitHub","url":"https://github.com/tongshuangwu/polyjuice"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10293092"},{"title":"Polyjuice: Automated, General-purpose Counterfactual Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Polyjuice:-Automated,-General-purpose-Generation-Wu-Ribeiro/7bc6eac5e11764204711169f36ab71631a8cd998"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models (Conference Paper) | NSF PAGES","url":"https://par.nsf.gov/biblio/10302716"},{"title":"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models","url":"https://idl.uw.edu/papers/polyjuice"}]

I found the paper you're looking for! Here are the key details:

Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models was authored by Tongshuang Wu, Marco Tulio Ribeiro, Jeffrey Heer, and Daniel Weld and published at ACL-IJCNLP 2021.

**Summary:**
Polyjuice is a general-purpose counterfactual generator that allows for control over perturbation types and locations, trained by finetuning GPT-2 on multiple datasets of paired sentences.

**Key Contributions:**
Polyjuice produces diverse sets of realistic counterfactuals, which are useful in various applications including improving training and evaluation on three different tasks (with around 70% less annotation effort than manual generation) and augmenting state-of-the-art explanation techniques.

**Publication Details:**
The paper was published in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 6707–6723.

You can access the paper through the ACL Anthology at https://aclanthology.org/2021.acl-long.523/ or on arXiv at https://arxiv.org/abs/2101.00288.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "ce697c5b-a30a-4189-a34f-e6ab30dad4af",
  "tool_use_result": {
    "query": "\"Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models\" Wu Ribeiro ACL 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_0134TPcGtEPJwrSiKNHzXXo2",
        "content": [
          {
            "title": "Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models - ACL Anthology",
            "url": "https://aclanthology.org/2021.acl-long.523/"
          },
          {
            "title": "[PDF] Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Polyjuice:-Generating-Counterfactuals-for-and-Wu-Ribeiro/15e71e497a67423bfedd0d63efe423c4660e5053"
          },
          {
            "title": "[2101.00288] Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models",
            "url": "https://arxiv.org/abs/2101.00288"
          },
          {
            "title": "GitHub - tongshuangwu/polyjuice · GitHub",
            "url": "https://github.com/tongshuangwu/polyjuice"
          },
          {
            "title": "Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models | NSF Public Access Repository",
            "url": "https://par.nsf.gov/biblio/10293092"
          },
          {
            "title": "Polyjuice: Automated, General-purpose Counterfactual Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Polyjuice:-Automated,-General-purpose-Generation-Wu-Ribeiro/7bc6eac5e11764204711169f36ab71631a8cd998"
          },
          {
            "title": "Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models (Conference Paper) | NSF PAGES",
            "url": "https://par.nsf.gov/biblio/10302716"
          },
          {
            "title": "Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models",
            "url": "https://idl.uw.edu/papers/polyjuice"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\nPolyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models was authored by Tongshuang Wu, Marco Tulio Ribeiro, Jeffrey Heer, and Daniel Weld and published at ACL-IJCNLP 2021.\n\n**Summary:**\nPolyjuice is a general-purpose counterfactual generator that allows for control over perturbation types and locations, trained by finetuning GPT-2 on multiple datasets of paired sentences.\n\n**Key Contributions:**\nPolyjuice produces diverse sets of realistic counterfactuals, which are useful in various applications including improving training and evaluation on three different tasks (with around 70% less annotation effort than manual generation) and augmenting state-of-the-art explanation techniques.\n\n**Publication Details:**\nThe paper was published in the Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 6707–6723.\n\nYou can access the paper through the ACL Anthology at https://aclanthology.org/2021.acl-long.523/ or on arXiv at https://arxiv.org/abs/2101.00288."
    ],
    "durationSeconds": 7.842290894999998
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T11:08:29.592Z_

<details><summary>↩ Tool result · `toolu_01TMCnrsKdsRA6NqcTCMQdaD`</summary>

```text
Web search results for query: ""CausaLM: Causal Model Explanation Through Counterfactual Language Models" Feder Computational Linguistics 2021"

Links: [{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models - ACL Anthology","url":"https://aclanthology.org/2021.cl-2.13/"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/47/2/333/98518/CausaLM-Causal-Model-Explanation-Through"},{"title":"[PDF] CausaLM: Causal Model Explanation Through Counterfactual Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CausaLM:-Causal-Model-Explanation-Through-Language-Feder-Oved/4f0318290bc75294338fdeb450e4365929b3aa0c"},{"title":"dblp: CausaLM: Causal Model Explanation Through Counterfactual Language Models.","url":"https://dblp.org/rec/journals/coling/FederOSR21.html"},{"title":"(PDF) CausaLM: Causal Model Explanation Through Counterfactual Language Models","url":"https://www.researchgate.net/publication/341699788_CausaLM_Causal_Model_Explanation_Through_Counterfactual_Language_Models"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models - Paper Detail","url":"https://deeplearn.org/arxiv/206142/causalm:-causal-model-explanation-through-counterfactual-language-models"},{"title":"Causalm: Causal model explanation through counterfactual language models - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"},{"title":"Causalm: Causal model explanation through counterfactual language models - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"},{"title":"CausaLM: Causal Model Explanation Through Counterfactual Language Models - Amir Feder","url":"https://amirfeder.github.io/publication/2020-10-01-CausaLM"}]

I found the paper you're looking for. Here are the key details:

**Publication Information:**
The paper "CausaLM: Causal Model Explanation Through Counterfactual Language Models" by Amir Feder, Nadav Oved, Uri Shalit, and Roi Reichart was published in Computational Linguistics, Volume 47, Issue 2 in June 2021.

**Main Contribution:**
CausaLM is a framework for producing causal model explanations using counterfactual language representation models based on fine-tuning of deep contextualized embedding models with auxiliary adversarial tasks derived from the causal graph of the problem.

**Key Method:**
By carefully choosing auxiliary adversarial pre-training tasks, language representation models such as BERT can effectively learn a counterfactual representation for a given concept of interest, and be used to estimate its true causal effect on model performance.

**Research Problem:**
While there are tools that can help understand whether biases exist, they do not distinguish between correlation and causation, and might be ill-suited for text-based models and for reasoning about high-level language concepts. A key problem of estimating the causal effect of a concept of interest on a given model is that this estimation requires the generation of counterfactual examples, which is challenging with existing generation technology.

The paper can be accessed through the ACL Anthology at https://aclanthology.org/2021.cl-2.13/ and MIT Press at https://direct.mit.edu/coli/article/47/2/333/98518/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "c4fac5fe-ad63-4e02-bae2-3f725dbb35a6",
  "tool_use_result": {
    "query": "\"CausaLM: Causal Model Explanation Through Counterfactual Language Models\" Feder Computational Linguistics 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PeM5qZ5E49EQCHJrMf8t88",
        "content": [
          {
            "title": "CausaLM: Causal Model Explanation Through Counterfactual Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2021.cl-2.13/"
          },
          {
            "title": "CausaLM: Causal Model Explanation Through Counterfactual Language Models | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/47/2/333/98518/CausaLM-Causal-Model-Explanation-Through"
          },
          {
            "title": "[PDF] CausaLM: Causal Model Explanation Through Counterfactual Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CausaLM:-Causal-Model-Explanation-Through-Language-Feder-Oved/4f0318290bc75294338fdeb450e4365929b3aa0c"
          },
          {
            "title": "dblp: CausaLM: Causal Model Explanation Through Counterfactual Language Models.",
            "url": "https://dblp.org/rec/journals/coling/FederOSR21.html"
          },
          {
            "title": "(PDF) CausaLM: Causal Model Explanation Through Counterfactual Language Models",
            "url": "https://www.researchgate.net/publication/341699788_CausaLM_Causal_Model_Explanation_Through_Counterfactual_Language_Models"
          },
          {
            "title": "CausaLM: Causal Model Explanation Through Counterfactual Language Models - Paper Detail",
            "url": "https://deeplearn.org/arxiv/206142/causalm:-causal-model-explanation-through-counterfactual-language-models"
          },
          {
            "title": "Causalm: Causal model explanation through counterfactual language models - Tel Aviv University",
            "url": "https://cris.tau.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"
          },
          {
            "title": "Causalm: Causal model explanation through counterfactual language models - Technion - Israel Institute of Technology",
            "url": "https://cris.technion.ac.il/en/publications/causalm-causal-model-explanation-through-counterfactual-language-/"
          },
          {
            "title": "CausaLM: Causal Model Explanation Through Counterfactual Language Models - Amir Feder",
            "url": "https://amirfeder.github.io/publication/2020-10-01-CausaLM"
          }
        ]
      },
      "I found the paper you're looking for. Here are the key details:\n\n**Publication Information:**\nThe paper \"CausaLM: Causal Model Explanation Through Counterfactual Language Models\" by Amir Feder, Nadav Oved, Uri Shalit, and Roi Reichart was published in Computational Linguistics, Volume 47, Issue 2 in June 2021.\n\n**Main Contribution:**\nCausaLM is a framework for producing causal model explanations using counterfactual language representation models based on fine-tuning of deep contextualized embedding models with auxiliary adversarial tasks derived from the causal graph of the problem.\n\n**Key Method:**\nBy carefully choosing auxiliary adversarial pre-training tasks, language representation models such as BERT can effectively learn a counterfactual representation for a given concept of interest, and be used to estimate its true causal effect on model performance.\n\n**Research Problem:**\nWhile there are tools that can help understand whether biases exist, they do not distinguish between correlation and causation, and might be ill-suited for text-based models and for reasoning about high-level language concepts. A key problem of estimating the causal effect of a concept of interest on a given model is that this estimation requires the generation of counterfactual examples, which is challenging with existing generation technology.\n\nThe paper can be accessed through the ACL Anthology at https://aclanthology.org/2021.cl-2.13/ and MIT Press at https://direct.mit.edu/coli/article/47/2/333/98518/."
    ],
    "durationSeconds": 9.423182843999996
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T11:08:30.260Z_

<details><summary>↩ Tool result · `toolu_01FGzRwVFJroHrVWoGmSUUTw`</summary>

```text
Web search results for query: ""The Use of Rating and Likert Scales in Natural Language Generation Human Evaluation Tasks" Amidei INLG 2019"

Links: [{"title":"The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations - ACL Anthology","url":"https://aclanthology.org/W19-8648/"},{"title":"[PDF] The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-use-of-rating-and-Likert-scales-in-Natural-A-Amidei-Piwek/73b6a65b283c9c0602822420b11b260925a4cff1"},{"title":"The use of rating and Likert scales in Natural Language","url":"https://oro.open.ac.uk/67963/"},{"title":"The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations | Request PDF","url":"https://www.researchgate.net/publication/338053074_The_use_of_rating_and_Likert_scales_in_Natural_Language_Generation_human_evaluation_tasks_A_review_and_some_recommendations"},{"title":"Best practices for the human evaluation of automatically generated text","url":"https://www.inlg2019.com/assets/papers/98_Paper.pdf"},{"title":"The use of rating and Likert scales in Natural Language ...","url":"https://www.inlg2019.com/assets/papers/57_Paper.pdf"},{"title":"Best practices for the human evaluation of automatically ...","url":"https://aclanthology.org/W19-8643.pdf"},{"title":"Jacopo Amidei | Semantic Scholar","url":"https://www.semanticscholar.org/author/Jacopo-Amidei/3481955"}]

I found the paper you're looking for! Here are the details:

**Title:** The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations

**Authors:** Jacopo Amidei, Paul Piwek, and Alistair Willis

**Publication:** Proceedings of the 12th International Conference on Natural Language Generation, pages 397–402, Tokyo, Japan (INLG 2019)

**Summary:** Rating and Likert scales are widely used in evaluation experiments to measure the quality of Natural Language Generation (NLG) systems. The authors reviewed the use of rating and Likert scales for NLG evaluation tasks published in NLG specialized conferences over the last ten years (135 papers in total). Their analysis reveals a number of deviations from good practice in their use, and they conclude with some recommendations about the use of such scales.

The paper is available at the ACL Anthology: https://aclanthology.org/W19-8648/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "d8a58dbf-8c24-4066-8396-a9a9c0950167",
  "tool_use_result": {
    "query": "\"The Use of Rating and Likert Scales in Natural Language Generation Human Evaluation Tasks\" Amidei INLG 2019",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JerU3pdSzTiRGsv5GE6PTZ",
        "content": [
          {
            "title": "The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations - ACL Anthology",
            "url": "https://aclanthology.org/W19-8648/"
          },
          {
            "title": "[PDF] The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/The-use-of-rating-and-Likert-scales-in-Natural-A-Amidei-Piwek/73b6a65b283c9c0602822420b11b260925a4cff1"
          },
          {
            "title": "The use of rating and Likert scales in Natural Language",
            "url": "https://oro.open.ac.uk/67963/"
          },
          {
            "title": "The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations | Request PDF",
            "url": "https://www.researchgate.net/publication/338053074_The_use_of_rating_and_Likert_scales_in_Natural_Language_Generation_human_evaluation_tasks_A_review_and_some_recommendations"
          },
          {
            "title": "Best practices for the human evaluation of automatically generated text",
            "url": "https://www.inlg2019.com/assets/papers/98_Paper.pdf"
          },
          {
            "title": "The use of rating and Likert scales in Natural Language ...",
            "url": "https://www.inlg2019.com/assets/papers/57_Paper.pdf"
          },
          {
            "title": "Best practices for the human evaluation of automatically ...",
            "url": "https://aclanthology.org/W19-8643.pdf"
          },
          {
            "title": "Jacopo Amidei | Semantic Scholar",
            "url": "https://www.semanticscholar.org/author/Jacopo-Amidei/3481955"
          }
        ]
      },
      "I found the paper you're looking for! Here are the details:\n\n**Title:** The use of rating and Likert scales in Natural Language Generation human evaluation tasks: A review and some recommendations\n\n**Authors:** Jacopo Amidei, Paul Piwek, and Alistair Willis\n\n**Publication:** Proceedings of the 12th International Conference on Natural Language Generation, pages 397–402, Tokyo, Japan (INLG 2019)\n\n**Summary:** Rating and Likert scales are widely used in evaluation experiments to measure the quality of Natural Language Generation (NLG) systems. The authors reviewed the use of rating and Likert scales for NLG evaluation tasks published in NLG specialized conferences over the last ten years (135 papers in total). Their analysis reveals a number of deviations from good practice in their use, and they conclude with some recommendations about the use of such scales.\n\nThe paper is available at the ACL Anthology: https://aclanthology.org/W19-8648/"
    ],
    "durationSeconds": 8.236068425999997
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-26T11:08:30.910Z_

<details><summary>↩ Tool result · `toolu_01U6eHzUpbHNH2uzJaiNe3My`</summary>

```text
Web search results for query: ""Style Over Substance: Evaluation Biases for Large Language Models" Wu Aji COLING 2025"

Links: [{"title":"Style Over Substance: Evaluation Biases for Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.21/"},{"title":"[2307.03025] Style Over Substance: Evaluation Biases for Large Language Models","url":"https://arxiv.org/abs/2307.03025"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=UnstiBOfnv"},{"title":"Evaluation Biases for Large Language Models","url":"https://aclanthology.org/2025.coling-main.21.pdf"},{"title":"Accepted Main Conference Papers - COLING 2025","url":"https://coling2025.org/program/main_conference_papers/"},{"title":"[PDF] Style Over Substance: Evaluation Biases for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Style-Over-Substance:-Evaluation-Biases-for-Large-Wu-Aji/7ace46ab8e71c4304682ab126b1212deb54b9b03"},{"title":"Style Over Substance: Evaluation Biases for Large Language Models","url":"https://www.researchgate.net/publication/372163436_Style_Over_Substance_Evaluation_Biases_for_Large_Language_Models"},{"title":"LLMs are Biased Evaluators But Not Biased for Fact- ...","url":"https://aclanthology.org/2025.findings-acl.1369.pdf"}]

I found the paper! Here's what I found about "Style Over Substance: Evaluation Biases for Large Language Models":

The paper is authored by Minghao Wu and Alham Fikri Aji and was published in the Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025) in Abu Dhabi, UAE on pages 297–312.

**Key findings from the research:**

The study investigates the behavior of crowd-sourced and expert annotators, as well as LLMs, when comparing outputs from different models, using a dataset of intentionally flawed machine-generated answers.

The findings reveal a concerning bias in the evaluation process, as answers with factual errors are rated more favorably than answers that are too short or contained grammatical errors.

To address this issue, the authors propose independently evaluating machine-generated text across multiple dimensions, rather than merging all the evaluation aspects into a single score.

The paper is available at the ACL Anthology (https://aclanthology.org/2025.coling-main.21/) and also appears to have been on arXiv as a preprint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "c3ac811c-b804-4ddb-a4f1-4a4452d7616b",
  "tool_use_result": {
    "query": "\"Style Over Substance: Evaluation Biases for Large Language Models\" Wu Aji COLING 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QiSg4AnX8MaUGrJ5XyJSss",
        "content": [
          {
            "title": "Style Over Substance: Evaluation Biases for Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.coling-main.21/"
          },
          {
            "title": "[2307.03025] Style Over Substance: Evaluation Biases for Large Language Models",
            "url": "https://arxiv.org/abs/2307.03025"
          },
          {
            "title": "Style Over Substance: Evaluation Biases for Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=UnstiBOfnv"
          },
          {
            "title": "Evaluation Biases for Large Language Models",
            "url": "https://aclanthology.org/2025.coling-main.21.pdf"
          },
          {
            "title": "Accepted Main Conference Papers - COLING 2025",
            "url": "https://coling2025.org/program/main_conference_papers/"
          },
          {
            "title": "[PDF] Style Over Substance: Evaluation Biases for Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Style-Over-Substance:-Evaluation-Biases-for-Large-Wu-Aji/7ace46ab8e71c4304682ab126b1212deb54b9b03"
          },
          {
            "title": "Style Over Substance: Evaluation Biases for Large Language Models",
            "url": "https://www.researchgate.net/publication/372163436_Style_Over_Substance_Evaluation_Biases_for_Large_Language_Models"
          },
          {
            "title": "LLMs are Biased Evaluators But Not Biased for Fact- ...",
            "url": "https://aclanthology.org/2025.findings-acl.1369.pdf"
          }
        ]
      },
      "I found the paper! Here's what I found about \"Style Over Substance: Evaluation Biases for Large Language Models\":\n\nThe paper is authored by Minghao Wu and Alham Fikri Aji and was published in the Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025) in Abu Dhabi, UAE on pages 297–312.\n\n**Key findings from the research:**\n\nThe study investigates the behavior of crowd-sourced and expert annotators, as well as LLMs, when comparing outputs from different models, using a dataset of intentionally flawed machine-generated answers.\n\nThe findings reveal a concerning bias in the evaluation process, as answers with factual errors are rated more favorably than answers that are too short or contained grammatical errors.\n\nTo address this issue, the authors propose independently evaluating machine-generated text across multiple dimensions, rather than merging all the evaluation aspects into a single score.\n\nThe paper is available at the ACL Anthology (https://aclanthology.org/2025.coling-main.21/) and also appears to have been on arXiv as a preprint."
    ],
    "durationSeconds": 8.716711282999997
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XpEcWrTCoPFMpUxzrg5kRD`</summary>

```json
{
  "query": "\"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\" Feder TACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "adc10d41-aca6-4eab-969a-ed8cbc29a255",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Hvnd9EqWdp8Gj6GE4Pa8sa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5078,
      "cache_read_input_tokens": 65481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5078
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RM2DtpMV3mmMn3468iGwGV`</summary>

```json
{
  "query": "\"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" Koo Findings ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "a7bfc847-ba50-4d2b-9a16-7b7b31e2c826",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Hvnd9EqWdp8Gj6GE4Pa8sa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5078,
      "cache_read_input_tokens": 65481,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5078
      },
      "output_tokens": 64,
      "service_tier": "standard",
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

_source line 50 · 2026-05-26T11:08:43.271Z_

<details><summary>↩ Tool result · `toolu_01XpEcWrTCoPFMpUxzrg5kRD`</summary>

```text
Web search results for query: ""Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond" Feder TACL 2022"

Links: [{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/4005"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - ACL Anthology","url":"https://aclanthology.org/2022.tacl-1.66/"},{"title":"dblp: Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond.","url":"https://dblp.org/rec/journals/tacl/FederKMPSWEGRRS22.html"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00511/113490/Causal-Inference-in-Natural-Language-Processing"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - Princeton University","url":"https://collaborate.princeton.edu/en/publications/causal-inference-in-natural-language-processing-estimation-predic/"},{"title":"(PDF) Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond","url":"https://www.researchgate.net/publication/364593870_Causal_Inference_in_Natural_Language_Processing_Estimation_Prediction_Interpretation_and_Beyond"},{"title":"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - Wikidata","url":"https://www.wikidata.org/wiki/Q130420656"},{"title":"(PDF) Causal Inference in Natural Language Processing: Application Status and Future Outlook","url":"https://www.researchgate.net/publication/385726030_Causal_Inference_in_Natural_Language_Processing_Application_Status_and_Future_Outlook"}]

I found the paper you were searching for. Here are the key details:

The paper "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond" was authored by Amir Feder, Katherine A. Keith, Emaad Manzoor, Reid Pryzant, Dhanya Sridhar, Zach Wood-Doughty, Jacob Eisenstein, Justin Grimmer, Roi Reichart, Margaret E. Roberts, Brandon M. Stewart, Victor Veitch, and Diyi Yang, and was published in TACL in 2022.

The paper was published in Transactions of the Association for Computational Linguistics, volume 10, pages 1138–1158 in 2022.

The paper introduces the statistical challenge of estimating causal effects with text in settings where text is used as an outcome, treatment, or to address confounding, and explores potential uses of causal inference to improve the robustness, fairness, and interpretability of NLP models.

The paper is available through multiple sources including:
- The ACL Anthology: https://aclanthology.org/2022.tacl-1.66/
- MIT Press Direct: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00511/113490/
- Transactions of the ACL: https://transacl.org/index.php/tacl/article/view/4005


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "bec5d137-142f-4e9d-abbb-52d2e02222d4",
  "tool_use_result": {
    "query": "\"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\" Feder TACL 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Prv6LqLCeftJJw7GEDbD6",
        "content": [
          {
            "title": "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond | Transactions of the Association for Computational Linguistics",
            "url": "https://transacl.org/index.php/tacl/article/view/4005"
          },
          {
            "title": "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - ACL Anthology",
            "url": "https://aclanthology.org/2022.tacl-1.66/"
          },
          {
            "title": "dblp: Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond.",
            "url": "https://dblp.org/rec/journals/tacl/FederKMPSWEGRRS22.html"
          },
          {
            "title": "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00511/113490/Causal-Inference-in-Natural-Language-Processing"
          },
          {
            "title": "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - Princeton University",
            "url": "https://collaborate.princeton.edu/en/publications/causal-inference-in-natural-language-processing-estimation-predic/"
          },
          {
            "title": "(PDF) Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond",
            "url": "https://www.researchgate.net/publication/364593870_Causal_Inference_in_Natural_Language_Processing_Estimation_Prediction_Interpretation_and_Beyond"
          },
          {
            "title": "Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond - Wikidata",
            "url": "https://www.wikidata.org/wiki/Q130420656"
          },
          {
            "title": "(PDF) Causal Inference in Natural Language Processing: Application Status and Future Outlook",
            "url": "https://www.researchgate.net/publication/385726030_Causal_Inference_in_Natural_Language_Processing_Application_Status_and_Future_Outlook"
          }
        ]
      },
      "I found the paper you were searching for. Here are the key details:\n\nThe paper \"Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond\" was authored by Amir Feder, Katherine A. Keith, Emaad Manzoor, Reid Pryzant, Dhanya Sridhar, Zach Wood-Doughty, Jacob Eisenstein, Justin Grimmer, Roi Reichart, Margaret E. Roberts, Brandon M. Stewart, Victor Veitch, and Diyi Yang, and was published in TACL in 2022.\n\nThe paper was published in Transactions of the Association for Computational Linguistics, volume 10, pages 1138–1158 in 2022.\n\nThe paper introduces the statistical challenge of estimating causal effects with text in settings where text is used as an outcome, treatment, or to address confounding, and explores potential uses of causal inference to improve the robustness, fairness, and interpretability of NLP models.\n\nThe paper is available through multiple sources including:\n- The ACL Anthology: https://aclanthology.org/2022.tacl-1.66/\n- MIT Press Direct: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00511/113490/\n- Transactions of the ACL: https://transacl.org/index.php/tacl/article/view/4005"
    ],
    "durationSeconds": 9.309175932999992
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-26T11:08:44.909Z_

<details><summary>↩ Tool result · `toolu_01RM2DtpMV3mmMn3468iGwGV`</summary>

```text
Web search results for query: ""Benchmarking Cognitive Biases in Large Language Models as Evaluators" Koo Findings ACL 2024"

Links: [{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.29/"},{"title":"Benchmarking Cognitive Biases in Large Language ...","url":"https://aclanthology.org/2024.findings-acl.29.pdf"},{"title":"GitHub - minnesotanlp/cobbler: Code and data for Koo et al's ACL 2024 paper \"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" · GitHub","url":"https://github.com/minnesotanlp/cobbler"},{"title":"[2309.17012] Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/abs/2309.17012"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - Experts@Minnesota","url":"https://experts.umn.edu/en/publications/benchmarking-cognitive-biases-in-large-language-models-as-evaluat/"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://aclanthology.org/2024.findings-acl.29.xml"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators","url":"https://arxiv.org/html/2309.17012v3"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators | Request PDF","url":"https://www.researchgate.net/publication/384209612_Benchmarking_Cognitive_Biases_in_Large_Language_Models_as_Evaluators"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators | OpenReview","url":"https://openreview.net/forum?id=AWeBlBQBJu"},{"title":"Benchmarking Cognitive Biases in Large Language Models as Evaluators - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230917012K/abstract"}]

I found the paper you were looking for! Here's information about the study:

**Paper Details:**
The paper "Benchmarking Cognitive Biases in Large Language Models as Evaluators" was authored by Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park, Zae Myung Kim, and Dongyeop Kang, and published in the Findings of the Association for Computational Linguistics: ACL 2024 in Bangkok, Thailand.

**Key Methodology:**
The researchers assembled 16 LLMs encompassing four different size ranges and evaluated their output responses by preference ranking from the other LLMs as evaluators.

**Main Findings:**
LLMs are biased text quality evaluators, exhibiting strong indications on their bias benchmark (average of 40% of comparisons across all models) within each of their evaluations that question their robustness as evaluators.

**Benchmark:**
The researchers introduced the Cognitive Bias Benchmark for LLMs as Evaluators (CoBBLEr), a benchmark to measure six different cognitive biases in LLM evaluation outputs, such as the Egocentric bias where a model prefers to rank its own outputs highly in evaluation.

The paper is available through the ACL Anthology at: https://aclanthology.org/2024.findings-acl.29/, and the code and data are available on GitHub at the minnesotanlp/cobbler repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "828e33fa-12b9-48a9-91bc-e5d4c5968cb0",
  "tool_use_result": {
    "query": "\"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" Koo Findings ACL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_0135MNXpDegUAUyKaKSTN56i",
        "content": [
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-acl.29/"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language ...",
            "url": "https://aclanthology.org/2024.findings-acl.29.pdf"
          },
          {
            "title": "GitHub - minnesotanlp/cobbler: Code and data for Koo et al's ACL 2024 paper \"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" · GitHub",
            "url": "https://github.com/minnesotanlp/cobbler"
          },
          {
            "title": "[2309.17012] Benchmarking Cognitive Biases in Large Language Models as Evaluators",
            "url": "https://arxiv.org/abs/2309.17012"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators - Experts@Minnesota",
            "url": "https://experts.umn.edu/en/publications/benchmarking-cognitive-biases-in-large-language-models-as-evaluat/"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators",
            "url": "https://aclanthology.org/2024.findings-acl.29.xml"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators",
            "url": "https://arxiv.org/html/2309.17012v3"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators | Request PDF",
            "url": "https://www.researchgate.net/publication/384209612_Benchmarking_Cognitive_Biases_in_Large_Language_Models_as_Evaluators"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators | OpenReview",
            "url": "https://openreview.net/forum?id=AWeBlBQBJu"
          },
          {
            "title": "Benchmarking Cognitive Biases in Large Language Models as Evaluators - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230917012K/abstract"
          }
        ]
      },
      "I found the paper you were looking for! Here's information about the study:\n\n**Paper Details:**\nThe paper \"Benchmarking Cognitive Biases in Large Language Models as Evaluators\" was authored by Ryan Koo, Minhwa Lee, Vipul Raheja, Jong Inn Park, Zae Myung Kim, and Dongyeop Kang, and published in the Findings of the Association for Computational Linguistics: ACL 2024 in Bangkok, Thailand.\n\n**Key Methodology:**\nThe researchers assembled 16 LLMs encompassing four different size ranges and evaluated their output responses by preference ranking from the other LLMs as evaluators.\n\n**Main Findings:**\nLLMs are biased text quality evaluators, exhibiting strong indications on their bias benchmark (average of 40% of comparisons across all models) within each of their evaluations that question their robustness as evaluators.\n\n**Benchmark:**\nThe researchers introduced the Cognitive Bias Benchmark for LLMs as Evaluators (CoBBLEr), a benchmark to measure six different cognitive biases in LLM evaluation outputs, such as the Egocentric bias where a model prefers to rank its own outputs highly in evaluation.\n\nThe paper is available through the ACL Anthology at: https://aclanthology.org/2024.findings-acl.29/, and the code and data are available on GitHub at the minnesotanlp/cobbler repository."
    ],
    "durationSeconds": 10.467466891000004
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "9d2afefd-a042-4794-b7ff-15b8be317475",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Qq51MEfFkpEbxwm33gLXLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 70559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3034
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

### Assistant

_source line 53_

Verification complete. Drafting the report.

## 20. dubois2023alpacafarm
- 真实性：✓ 存在
- 作者：✓ 正确（Dubois, Li, Taori, Zhang, Gulrajani, Ba, Guestrin, Liang, Hashimoto）
- 年份：✓ 正确（2023）
- 标题：✓ 正确
- Venue：✓ 正确（NeurIPS 2023）
- 正文引用上下文：✓ 正确（related_work.tex:20 说 BT 用于 AlpacaFarm；method.tex:52 用 AlpacaEval 做跨基准验证——AlpacaEval 出自 AlpacaFarm，引用合理）

## 21. bradley1952rank
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（related_work.tex:20 与 experiments.tex:12 均指 BT model 出处）

## 22. feinstein1990kappa
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（appendix.tex:664 引用其"prevalence paradox"——正是该论文核心论点）

## 23. wang2023faireval
- 真实性：✓ 存在
- 作者：✓ 正确（Wang, Li, Chen, Cai, Zhu, Lin, Cao, Kong, Liu, Liu, Sui）
- 年份：✓ 正确（bib key 写 2023 是 arXiv 时间，实际发表 2024 ACL，bib `year=2024` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（ACL 2024 Long Papers, aclanthology.org/2024.acl-long.511/）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**（bib 中有定义但正文从未 \cite）

## 24. li2024calibraeval
- 真实性：✓ 存在
- 作者：✓ 正确（Li, Chen, Ai, Chu, Zhou, Dong, Liu）
- 年份：✓ 正确（bib key 写 2024 是 arXiv 时间 2410.15393，实际 ACL 2025，bib `year=2025` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（ACL 2025 Long Papers, aclanthology.org/2025.acl-long.808/）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**

## 25. hoenig2001abuse
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（experiments.tex:86 "post-hoc power; cf. Hoenig"——精准引用该论文核心论点）

## 26. zeng2023llmbar
- 真实性：✓ 存在
- 作者：✓ 正确（Zeng, Yu, Gao, Meng, Goyal, Chen）
- 年份：✓ 正确（bib key 2023 是 arXiv 时间 2310.07641，实际 ICLR 2024，bib `year=2024` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2024）
- 正文引用上下文：✓ 正确（method.tex:50 说 LLMBar n=100。LLMBar 总共 419 条，Natural 子集 100 条，与项目用法一致；appendix.tex:560 也明确"100 instruction-response pairs"）

## 27. veitch2020adapting
- 真实性：✓ 存在
- 作者：✓ 正确（Veitch, Sridhar, Blei）
- 年份：✓ 正确（2020）
- 标题：✓ 正确
- Venue：✓ 正确（UAI 2020, PMLR 124:919-928）
- 正文引用上下文：✓ 正确（introduction.tex:17 "interventional text analysis"；method.tex:23 "filtering-based confounder control"——均对应论文 causally sufficient embeddings 思路）

## 28. tan2025judgebench
- 真实性：✓ 存在
- 作者：✓ 正确（Tan, Zhuang, Montgomery, Tang, ...；bib 用 "and others"）
- 年份：✓ 正确（2025）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**

## 29. chiang2024chatbot
- 真实性：✓ 存在
- 作者：✓ 正确（Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhu, Zhang, Jordan, Gonzalez, Stoica）
- 年份：✓ 正确（2024）
- 标题：✓ 正确
- Venue：✓ 正确（ICML 2024）
- 正文引用上下文：✓ 正确（related_work.tex:20 说 BT 用于 Chatbot Arena——Arena 排名确实基于 BT）

## 30. hunter2004mm
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（experiments.tex:12 与 appendix.tex:555 引用其 MM 算法用于 BT 参数估计——正是该论文主题）

## 31. ye2024justice
- 真实性：✓ 存在
- 作者：✓ 正确（Ye, Wang, Huang, Chen, Zhang, Moniz, Gao, Geyer, Huang, Chen, Chawla, Zhang）
- 年份：✓ 正确（2025 ICLR）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：✓ 正确（related_work.tex:11 "quantify 12 bias types"——论文确为 12 种 bias）

## 32. feder2021causalm
- 真实性：✓ 存在
- 作者：✓ 正确（Feder, Oved, Shalit, Reichart）
- 年份：✓ 正确（2021）
- 标题：✓ 正确
- Venue：✓ 正确（Computational Linguistics 47(2): 333–386）
- 正文引用上下文：✓ 正确（related_work.tex:5 列为"text-based interventional methods"基础——CausaLM 正是反事实语言模型）

## 33. wu2021polyjuice
- 真实性：✓ 存在
- 作者：✓ 正确（Wu, Ribeiro, Heer, Weld）
- 年份：✓ 正确（2021）
- 标题：✓ 正确
- Venue：✓ 正确（ACL-IJCNLP 2021 Long Papers）
- 正文引用上下文：✓ 正确（related_work.tex:5 与 CausaLM/causal NLP 同列为反事实文本生成基础工作）

## 34. amidei2019likert
- 真实性：✓ 存在
- 作者：✓ 正确（Amidei, Piwek, Willis）
- 年份：✓ 正确（2019）
- 标题：✓ 正确（bib 含完整副标题 "A Review and Some Recommendations"）
- Venue：✓ 正确（INLG 2019）
- 正文引用上下文：✓ 正确（related_work.tex:19 "review Likert scales in NLG evaluation"——精准对应论文）

## 35. wu2023style
- 真实性：✓ 存在
- 作者：✓ 正确（Wu Minghao, Aji Alham Fikri）
- 年份：✓ 正确（bib key 2023 是 arXiv 2307.03025 时间；正式发表 COLING 2025，bib `year=2025` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（COLING 2025, aclanthology.org/2025.coling-main.21/）
- 正文引用上下文：✓ 正确（related_work.tex:12 与 method.tex:53 均对应"style bias / formality & verbosity sensitivities"——与论文主题一致）

## 36. feder2022causal
- 真实性：✓ 存在
- 作者：✓ 正确（Feder, Keith, Manzoor, Pryzant, Sridhar, Wood-Doughty, Eisenstein, Grimmer, Reichart, Roberts, Stewart, Veitch, Yang）
- 年份：✓ 正确（2022）
- 标题：✓ 正确
- Venue：✓ 正确（TACL vol.10, pp.1138–1158）
- 正文引用上下文：✓ 正确（related_work.tex:5 列为 causal NLP 综述）

## 37. koo2024cobbler
- 真实性：✓ 存在
- 作者：✓ 正确（Koo, Lee, Raheja, Park, Kim, Kang）
- 年份：✓ 正确（2024）
- 标题：✓ 正确
- Venue：✓ 正确（Findings of ACL 2024）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**

## 38. liang1986gee
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（experiments.tex:109 引用其 GEE 框架——该论文正是 GEE 提出之作）

---

## 汇总

总共 **19 条**，引用元数据全部 ✓ **19 条**，hallucinated ✗ **0 条**。

**额外发现（4 条 bib 条目存在但正文从未引用）**：
- `wang2023faireval`（位置偏置经典论文）
- `li2024calibraeval`（selection bias 缓解）
- `tan2025judgebench`（judge benchmark）
- `koo2024cobbler`（认知偏见 benchmark）

这些条目元数据均正确，但在所有 tex 文件中无 `\cite` 使用。建议：要么补充正文引用（这 4 篇与论文主题高度相关，自然适合 Related Work），要么从 bib 中删除以避免 LaTeX 编译时未使用引用的污染。

**年份 key 与实际发表年差异（合理且 bib `year` 字段已修正）**：
- `wang2023faireval` → 实际 ACL 2024（bib year=2024 ✓）
- `li2024calibraeval` → 实际 ACL 2025（bib year=2025 ✓）
- `zeng2023llmbar` → 实际 ICLR 2024（bib year=2024 ✓）
- `wu2023style` → 实际 COLING 2025（bib year=2025 ✓）

Sources:
- [AlpacaFarm NeurIPS 2023](https://proceedings.neurips.cc//paper_files/paper/2023/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html)
- [Wang FairEval ACL 2024](https://aclanthology.org/2024.acl-long.511/)
- [Li CalibraEval ACL 2025](https://aclanthology.org/2025.acl-long.808/)
- [Zeng LLMBar ICLR 2024](https://openreview.net/forum?id=tr0KidwPLc)
- [Veitch Adapting Text Embeddings UAI 2020](https://proceedings.mlr.press/v124/veitch20a.html)
- [Tan JudgeBench ICLR 2025](https://openreview.net/forum?id=G0dksFayVq)
- [Chiang Chatbot Arena ICML 2024](https://proceedings.mlr.press/v235/chiang24b.html)
- [Ye Justice or Prejudice ICLR 2025](https://openreview.net/forum?id=3GTtZFiajM)
- [Feder CausaLM CL 2021](https://aclanthology.org/2021.cl-2.13/)
- [Wu Polyjuice ACL 2021](https://aclanthology.org/2021.acl-long.523/)
- [Amidei Likert INLG 2019](https://aclanthology.org/W19-8648/)
- [Wu&Aji Style Over Substance COLING 2025](https://aclanthology.org/2025.coling-main.21/)
- [Feder Causal NLP TACL 2022](https://aclanthology.org/2022.tacl-1.66/)
- [Koo CoBBLEr Findings ACL 2024](https://aclanthology.org/2024.findings-acl.29/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "uuid": "354b2846-c1f2-4b41-989b-2c07d691c147",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Qq51MEfFkpEbxwm33gLXLV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 70559,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3034
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

### Task result

_source line 54_

Verification complete. Drafting the report.

## 20. dubois2023alpacafarm
- 真实性：✓ 存在
- 作者：✓ 正确（Dubois, Li, Taori, Zhang, Gulrajani, Ba, Guestrin, Liang, Hashimoto）
- 年份：✓ 正确（2023）
- 标题：✓ 正确
- Venue：✓ 正确（NeurIPS 2023）
- 正文引用上下文：✓ 正确（related_work.tex:20 说 BT 用于 AlpacaFarm；method.tex:52 用 AlpacaEval 做跨基准验证——AlpacaEval 出自 AlpacaFarm，引用合理）

## 21. bradley1952rank
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（related_work.tex:20 与 experiments.tex:12 均指 BT model 出处）

## 22. feinstein1990kappa
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（appendix.tex:664 引用其"prevalence paradox"——正是该论文核心论点）

## 23. wang2023faireval
- 真实性：✓ 存在
- 作者：✓ 正确（Wang, Li, Chen, Cai, Zhu, Lin, Cao, Kong, Liu, Liu, Sui）
- 年份：✓ 正确（bib key 写 2023 是 arXiv 时间，实际发表 2024 ACL，bib `year=2024` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（ACL 2024 Long Papers, aclanthology.org/2024.acl-long.511/）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**（bib 中有定义但正文从未 \cite）

## 24. li2024calibraeval
- 真实性：✓ 存在
- 作者：✓ 正确（Li, Chen, Ai, Chu, Zhou, Dong, Liu）
- 年份：✓ 正确（bib key 写 2024 是 arXiv 时间 2410.15393，实际 ACL 2025，bib `year=2025` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（ACL 2025 Long Papers, aclanthology.org/2025.acl-long.808/）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**

## 25. hoenig2001abuse
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（experiments.tex:86 "post-hoc power; cf. Hoenig"——精准引用该论文核心论点）

## 26. zeng2023llmbar
- 真实性：✓ 存在
- 作者：✓ 正确（Zeng, Yu, Gao, Meng, Goyal, Chen）
- 年份：✓ 正确（bib key 2023 是 arXiv 时间 2310.07641，实际 ICLR 2024，bib `year=2024` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2024）
- 正文引用上下文：✓ 正确（method.tex:50 说 LLMBar n=100。LLMBar 总共 419 条，Natural 子集 100 条，与项目用法一致；appendix.tex:560 也明确"100 instruction-response pairs"）

## 27. veitch2020adapting
- 真实性：✓ 存在
- 作者：✓ 正确（Veitch, Sridhar, Blei）
- 年份：✓ 正确（2020）
- 标题：✓ 正确
- Venue：✓ 正确（UAI 2020, PMLR 124:919-928）
- 正文引用上下文：✓ 正确（introduction.tex:17 "interventional text analysis"；method.tex:23 "filtering-based confounder control"——均对应论文 causally sufficient embeddings 思路）

## 28. tan2025judgebench
- 真实性：✓ 存在
- 作者：✓ 正确（Tan, Zhuang, Montgomery, Tang, ...；bib 用 "and others"）
- 年份：✓ 正确（2025）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**

## 29. chiang2024chatbot
- 真实性：✓ 存在
- 作者：✓ 正确（Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhu, Zhang, Jordan, Gonzalez, Stoica）
- 年份：✓ 正确（2024）
- 标题：✓ 正确
- Venue：✓ 正确（ICML 2024）
- 正文引用上下文：✓ 正确（related_work.tex:20 说 BT 用于 Chatbot Arena——Arena 排名确实基于 BT）

## 30. hunter2004mm
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（experiments.tex:12 与 appendix.tex:555 引用其 MM 算法用于 BT 参数估计——正是该论文主题）

## 31. ye2024justice
- 真实性：✓ 存在
- 作者：✓ 正确（Ye, Wang, Huang, Chen, Zhang, Moniz, Gao, Geyer, Huang, Chen, Chawla, Zhang）
- 年份：✓ 正确（2025 ICLR）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2025）
- 正文引用上下文：✓ 正确（related_work.tex:11 "quantify 12 bias types"——论文确为 12 种 bias）

## 32. feder2021causalm
- 真实性：✓ 存在
- 作者：✓ 正确（Feder, Oved, Shalit, Reichart）
- 年份：✓ 正确（2021）
- 标题：✓ 正确
- Venue：✓ 正确（Computational Linguistics 47(2): 333–386）
- 正文引用上下文：✓ 正确（related_work.tex:5 列为"text-based interventional methods"基础——CausaLM 正是反事实语言模型）

## 33. wu2021polyjuice
- 真实性：✓ 存在
- 作者：✓ 正确（Wu, Ribeiro, Heer, Weld）
- 年份：✓ 正确（2021）
- 标题：✓ 正确
- Venue：✓ 正确（ACL-IJCNLP 2021 Long Papers）
- 正文引用上下文：✓ 正确（related_work.tex:5 与 CausaLM/causal NLP 同列为反事实文本生成基础工作）

## 34. amidei2019likert
- 真实性：✓ 存在
- 作者：✓ 正确（Amidei, Piwek, Willis）
- 年份：✓ 正确（2019）
- 标题：✓ 正确（bib 含完整副标题 "A Review and Some Recommendations"）
- Venue：✓ 正确（INLG 2019）
- 正文引用上下文：✓ 正确（related_work.tex:19 "review Likert scales in NLG evaluation"——精准对应论文）

## 35. wu2023style
- 真实性：✓ 存在
- 作者：✓ 正确（Wu Minghao, Aji Alham Fikri）
- 年份：✓ 正确（bib key 2023 是 arXiv 2307.03025 时间；正式发表 COLING 2025，bib `year=2025` 正确）
- 标题：✓ 正确
- Venue：✓ 正确（COLING 2025, aclanthology.org/2025.coling-main.21/）
- 正文引用上下文：✓ 正确（related_work.tex:12 与 method.tex:53 均对应"style bias / formality & verbosity sensitivities"——与论文主题一致）

## 36. feder2022causal
- 真实性：✓ 存在
- 作者：✓ 正确（Feder, Keith, Manzoor, Pryzant, Sridhar, Wood-Doughty, Eisenstein, Grimmer, Reichart, Roberts, Stewart, Veitch, Yang）
- 年份：✓ 正确（2022）
- 标题：✓ 正确
- Venue：✓ 正确（TACL vol.10, pp.1138–1158）
- 正文引用上下文：✓ 正确（related_work.tex:5 列为 causal NLP 综述）

## 37. koo2024cobbler
- 真实性：✓ 存在
- 作者：✓ 正确（Koo, Lee, Raheja, Park, Kim, Kang）
- 年份：✓ 正确（2024）
- 标题：✓ 正确
- Venue：✓ 正确（Findings of ACL 2024）
- 正文引用上下文：⚠ **未在任何 tex 文件中引用**

## 38. liang1986gee
- ✓ 经典文献，跳过 web 验证
- 正文引用上下文：✓ 正确（experiments.tex:109 引用其 GEE 框架——该论文正是 GEE 提出之作）

---

## 汇总

总共 **19 条**，引用元数据全部 ✓ **19 条**，hallucinated ✗ **0 条**。

**额外发现（4 条 bib 条目存在但正文从未引用）**：
- `wang2023faireval`（位置偏置经典论文）
- `li2024calibraeval`（selection bias 缓解）
- `tan2025judgebench`（judge benchmark）
- `koo2024cobbler`（认知偏见 benchmark）

这些条目元数据均正确，但在所有 tex 文件中无 `\cite` 使用。建议：要么补充正文引用（这 4 篇与论文主题高度相关，自然适合 Related Work），要么从 bib 中删除以避免 LaTeX 编译时未使用引用的污染。

**年份 key 与实际发表年差异（合理且 bib `year` 字段已修正）**：
- `wang2023faireval` → 实际 ACL 2024（bib year=2024 ✓）
- `li2024calibraeval` → 实际 ACL 2025（bib year=2025 ✓）
- `zeng2023llmbar` → 实际 ICLR 2024（bib year=2024 ✓）
- `wu2023style` → 实际 COLING 2025（bib year=2025 ✓）

Sources:
- [AlpacaFarm NeurIPS 2023](https://proceedings.neurips.cc//paper_files/paper/2023/hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html)
- [Wang FairEval ACL 2024](https://aclanthology.org/2024.acl-long.511/)
- [Li CalibraEval ACL 2025](https://aclanthology.org/2025.acl-long.808/)
- [Zeng LLMBar ICLR 2024](https://openreview.net/forum?id=tr0KidwPLc)
- [Veitch Adapting Text Embeddings UAI 2020](https://proceedings.mlr.press/v124/veitch20a.html)
- [Tan JudgeBench ICLR 2025](https://openreview.net/forum?id=G0dksFayVq)
- [Chiang Chatbot Arena ICML 2024](https://proceedings.mlr.press/v235/chiang24b.html)
- [Ye Justice or Prejudice ICLR 2025](https://openreview.net/forum?id=3GTtZFiajM)
- [Feder CausaLM CL 2021](https://aclanthology.org/2021.cl-2.13/)
- [Wu Polyjuice ACL 2021](https://aclanthology.org/2021.acl-long.523/)
- [Amidei Likert INLG 2019](https://aclanthology.org/W19-8648/)
- [Wu&Aji Style Over Substance COLING 2025](https://aclanthology.org/2025.coling-main.21/)
- [Feder Causal NLP TACL 2022](https://aclanthology.org/2022.tacl-1.66/)
- [Koo CoBBLEr Findings ACL 2024](https://aclanthology.org/2024.findings-acl.29/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 171301,
  "duration_api_ms": 261413,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "0f4207de-b441-4732-8296-dc8abcc98c00",
  "total_cost_usd": 1.2904897499999999,
  "usage": {
    "input_tokens": 1427,
    "cache_creation_input_tokens": 75573,
    "cache_read_input_tokens": 507131,
    "output_tokens": 9062,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 75573,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 5980,
        "cache_read_input_tokens": 70559,
        "cache_creation_input_tokens": 3034,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3034
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 158413,
      "outputTokens": 6499,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.330908,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 1427,
      "outputTokens": 9062,
      "cacheReadInputTokens": 507131,
      "cacheCreationInputTokens": 75573,
      "webSearchRequests": 0,
      "costUSD": 0.95958175,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5c4a96ee-d0f6-4424-ba9b-710928b52860"
}
```

</details>

---
