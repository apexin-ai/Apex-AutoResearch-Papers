# paper reference audit

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 13
- **Original source:** `logs/workers/worker_paper_reference-audit_20260515T052222.log`
- **Structured JSON:** [`56ae749f998d97673799.json`](../../sessions/56/56ae749f998d97673799.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "46cd4986-4521-43e8-ad38-4c00cabc8066",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778838600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c06ac92b-415f-4f25-a63f-9478fd0c2cd4",
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the references.bib and all .tex files to perform the citation audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "19a80951-88ea-491f-ae82-a6852c1d333f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vv3ws2A5ZJKSVL8LUMaAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

开始引用审计。先读取 bib 文件和所有 tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "e3ab9c1f-82f2-4973-bbdc-46a89d0f2649",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vv3ws2A5ZJKSVL8LUMaAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01GVrHB94jiKC1kZg2xP7Dsy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "0f89df33-ee4d-4c39-bc08-f6a32e2a4f98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vv3ws2A5ZJKSVL8LUMaAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 7 · 2026-05-15T05:22:31.580Z_

<details><summary>↩ Tool result · `toolu_01GVrHB94jiKC1kZg2xP7Dsy`</summary>

```text
1	% ==============================================================
2	% CATEGORY: direct-competitor
3	% ==============================================================
4	
5	@article{xi2025agentprm,
6	  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},
7	  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},
8	  journal = {arXiv preprint arXiv:2511.08325},
9	  year    = {2025},
10	}
11	
12	@article{choudhury2025prm,
13	  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},
14	  author  = {Sanjiban Choudhury},
15	  journal = {arXiv preprint arXiv:2502.10325},
16	  year    = {2025},
17	}
18	
19	@article{li2026toolprmbench,
20	  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},
21	  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},
22	  journal = {arXiv preprint arXiv:2601.12294},
23	  year    = {2026},
24	}
25	
26	@article{wang2026planrewardbench,
27	  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},
28	  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},
29	  journal = {arXiv preprint arXiv:2604.08178},
30	  year    = {2026},
31	}
32	
33	@inproceedings{chen2025monitoring,
34	  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},
35	  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},
36	  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},
37	  year      = {2025},
38	}
39	
40	@article{kale2025weaktostrong,
41	  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},
42	  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},
43	  journal = {arXiv preprint arXiv:2508.19461},
44	  year    = {2025},
45	}
46	
47	@article{fan2026agentrm,
48	  title   = {Exploring Reasoning Reward Model for Agents},
49	  author  = {Kaixuan Fan and Kaituo Feng and Manyuan Zhang and others},
50	  journal = {arXiv preprint arXiv:2601.22154},
51	  year    = {2026},
52	}
53	
54	@article{qiu2026dataprm,
55	  title   = {Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis},
56	  author  = {Zhisong Qiu and Shuofei Qiao and Kewei Xu and others},
57	  journal = {arXiv preprint arXiv:2604.24198},
58	  year    = {2026},
59	}
60	
61	% ==============================================================
62	% CATEGORY: method-component
63	% ==============================================================
64	
65	@inproceedings{ratner2016dataprogramming,
66	  title     = {Data Programming: Creating Large Training Sets, Quickly},
67	  author    = {Alexander Ratner and Christopher De Sa and Sen Wu and Daniel Selsam and Christopher Re},
68	  booktitle = {Advances in Neural Information Processing Systems},
69	  year      = {2016},
70	}
71	
72	@article{ratner2017snorkel,
73	  title   = {Snorkel: Rapid Training Data Creation with Weak Supervision},
74	  author  = {Alexander Ratner and Stephen H. Bach and Henry Ehrenberg and others},
75	  journal = {Proceedings of the VLDB Endowment},
76	  year    = {2018},
77	}
78	
79	@inproceedings{fu2020flyingsquid,
80	  title     = {Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods},
81	  author    = {Daniel Y. Fu and Mayee F. Chen and Frederic Sala and others},
82	  booktitle = {International Conference on Machine Learning},
83	  year      = {2020},
84	}
85	
86	@inproceedings{ratner2019snorkelmetal,
87	  title     = {Training Complex Models with Multi-Task Weak Supervision},
88	  author    = {Alexander Ratner and Braden Hancock and Jared Dunnmon and others},
89	  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
90	  year      = {2019},
91	}
92	
93	@inproceedings{zhang2021wrench,
94	  title     = {WRENCH: A Comprehensive Benchmark for Weak Supervision},
95	  author    = {Jieyu Zhang and Yue Yu and Yinghao Li and others},
96	  booktitle = {Advances in Neural Information Processing Systems},
97	  year      = {2021},
98	}
99	
100	@inproceedings{safranchik2020linkedhmm,
101	  title     = {Weakly Supervised Sequence Tagging from Noisy Rules},
102	  author    = {Esteban Safranchik and Shiying Luo and Stephen H. Bach},
103	  booktitle = {AAAI Conference on Artificial Intelligence},
104	  year      = {2020},
105	}
106	
107	@inproceedings{sala2019multiresolution,
108	  title     = {Multi-Resolution Weak Supervision for Sequential Data},
109	  author    = {Frederic Sala and Paroma Varma and Jason Fries and others},
110	  booktitle = {Advances in Neural Information Processing Systems},
111	  year      = {2019},
112	}
113	
114	@article{dawid1979em,
115	  title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm},
116	  author  = {A. P. Dawid and A. M. Skene},
117	  journal = {Journal of the Royal Statistical Society, Series C},
118	  year    = {1979},
119	}
120	
121	@inproceedings{lison2021skweak,
122	  title     = {skweak: Weak Supervision Made Easy for NLP},
123	  author    = {Pierre Lison and Jeremy Barnes and Aliaksandr Hubin},
124	  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
125	  year      = {2021},
126	}
127	
128	@inproceedings{li2020dividemix,
129	  title     = {DivideMix: Learning with Noisy Labels as Semi-Supervised Learning},
130	  author    = {Junnan Li and Richard Socher and Steven C.H. Hoi},
131	  booktitle = {International Conference on Learning Representations},
132	  year      = {2020},
133	}
134	
135	@inproceedings{han2018coteaching,
136	  title     = {Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels},
137	  author    = {Bo Han and Quanming Yao and Xingrui Yu and Gang Niu and Miao Xu and Weihua Hu and Ivor W. Tsang and Masashi Sugiyama},
138	  booktitle = {Advances in Neural Information Processing Systems},
139	  year      = {2018},
140	}
141	
142	@article{kaufman2012leakage,
143	  title   = {Leakage in Data Mining: Formulation, Detection, and Avoidance},
144	  author  = {Shachar Kaufman and Saharon Rosset and Claudia Perlich and Ori Stitelman},
145	  journal = {ACM Transactions on Knowledge Discovery from Data},
146	  volume  = {6},
147	  number  = {4},
148	  year    = {2012},
149	}
150	
151	@inproceedings{maheshwari2022spear,
152	  title     = {Learning to Robustly Aggregate Labeling Functions for Semi-supervised Data Programming},
153	  author    = {Ayush Maheshwari and Hewitt Oommen and Nicholas Monath and others},
154	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},
155	  year      = {2022},
156	}
157	
158	@article{manheim2018goodhart,
159	  title   = {Categorizing Variants of Goodhart's Law},
160	  author  = {David Manheim and Scott Garrabrant},
161	  journal = {arXiv preprint arXiv:1803.04585},
162	  year    = {2018},
163	}
164	
165	% ==============================================================
166	% CATEGORY: evaluation
167	% ==============================================================
168	
169	@article{orlanski2026slopcodebench,
170	  title   = {SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks},
171	  author  = {Gabriel Orlanski and Devjeet Roy and Alexander Yun and others},
172	  journal = {arXiv preprint arXiv:2603.24755},
173	  year    = {2026},
174	}
175	
176	@inproceedings{jimenez2024swebench,
177	  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},
178	  author    = {Carlos E. Jimenez and John Yang and Alexander Wettig and others},
179	  booktitle = {International Conference on Learning Representations},
180	  year      = {2024},
181	}
182	
183	@inproceedings{yang2024sweagent,
184	  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},
185	  author    = {John Yang and Carlos E. Jimenez and Alexander Wettig and others},
186	  booktitle = {Advances in Neural Information Processing Systems},
187	  year      = {2024},
188	}
189	
190	@inproceedings{wang2025openhands,
191	  title     = {OpenHands: An Open Platform for AI Software Developers as Generalist Agents},
192	  author    = {Xingyao Wang and Boxuan Li and Yufan Song and others},
193	  booktitle = {International Conference on Learning Representations},
194	  year      = {2025},
195	}
196	
197	% ==============================================================
198	% CATEGORY: background
199	% ==============================================================
200	
201	@inproceedings{shinn2023reflexion,
202	  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},
203	  author    = {Noah Shinn and Federico Cassano and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},
204	  booktitle = {Advances in Neural Information Processing Systems},
205	  year      = {2023},
206	}
207	
208	@inproceedings{zhou2024lats,
209	  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},
210	  author    = {Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},
211	  booktitle = {International Conference on Machine Learning},
212	  year      = {2024},
213	}
214	
215	@inproceedings{yao2023tot,
216	  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
217	  author    = {Shunyu Yao and Dian Yu and Jeffrey Zhao and others},
218	  booktitle = {Advances in Neural Information Processing Systems},
219	  year      = {2023},
220	}
221	
222	@article{cemri2025multiagentfail,
223	  title   = {Why Do Multi-Agent LLM Systems Fail?},
224	  author  = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and others},
225	  journal = {arXiv preprint arXiv:2503.13657},
226	  year    = {2025},
227	}
228	
229	@article{zhu2025agentfail,
230	  title   = {Where LLM Agents Fail and How They Can Learn From Failures},
231	  author  = {Kunlun Zhu and Zijia Liu and Bingxuan Li and others},
232	  journal = {arXiv preprint arXiv:2509.25370},
233	  year    = {2025},
234	}
235	
236	@article{george2025cycledetection,
237	  title   = {Unsupervised Cycle Detection in Agentic Applications},
238	  author  = {Felix George and Harshit Kumar and Divya Pathak and others},
239	  journal = {arXiv preprint arXiv:2511.10650},
240	  year    = {2025},
241	}
242	
243	@article{pipis2025reasoningloop,
244	  title   = {Wait, Wait, Wait... Why Do Reasoning Models Loop?},
245	  author  = {Charilaos Pipis and Shivam Garg and Vasilis Kontonis and others},
246	  journal = {arXiv preprint arXiv:2512.12895},
247	  year    = {2025},
248	}
249	
250	@inproceedings{huang2024selfcorrect,
251	  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},
252	  author    = {Jie Huang and Xinyun Chen and Swaroop Mishra and others},
253	  booktitle = {International Conference on Learning Representations},
254	  year      = {2024},
255	}
256	
257	@article{kamoi2024selfcorrection,
258	  title   = {When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},
259	  author  = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},
260	  journal = {Transactions of the Association for Computational Linguistics},
261	  year    = {2024},
262	}
263	
264	@article{liu2026trajad,
265	  title   = {TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents},
266	  author  = {Yibing Liu and Chong Zhang and Zhongyi Han and others},
267	  journal = {arXiv preprint arXiv:2602.06443},
268	  year    = {2026},
269	}
270	
271	% ==============================================================
272	% CATEGORY: technique
273	% ==============================================================
274	
275	@inproceedings{cho2014gru,
276	  title     = {Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation},
277	  author    = {Kyunghyun Cho and Bart van Merrienboer and Caglar Gulcehre and others},
278	  booktitle = {Conference on Empirical Methods in Natural Language Processing},
279	  year      = {2014},
280	}
281	
282	@inproceedings{bahdanau2015attention,
283	  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},
284	  author    = {Dzmitry Bahdanau and Kyunghyun Cho and Yoshua Bengio},
285	  booktitle = {International Conference on Learning Representations},
286	  year      = {2015},
287	}
288	
289	@article{zhang2025qwen3embedding,
290	  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},
291	  author  = {Yanzhao Zhang and Mingxin Li and Dingkun Long and others},
292	  journal = {arXiv preprint arXiv:2506.05176},
293	  year    = {2025},
294	}
295	
296	@article{wang2024e5,
297	  title   = {Multilingual E5 Text Embeddings: A Technical Report},
298	  author  = {Liang Wang and Nan Yang and Xiaolong Huang and others},
299	  journal = {arXiv preprint arXiv:2402.05672},
300	  year    = {2024},
301	}
302	
303	@article{chen2024bgem3,
304	  title   = {BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},
305	  author  = {Jianlv Chen and Shitao Xiao and Peitian Zhang and others},
306	  journal = {arXiv preprint arXiv:2402.03216},
307	  year    = {2024},
308	}
309	
310	% ==============================================================
311	% CATEGORY: related-work-additions (Round 1 revision)
312	% ==============================================================
313	
314	@book{vanderaalst2016processmining,
315	  title     = {Process Mining: Data Science in Action},
316	  author    = {Wil M. P. van der Aalst},
317	  publisher = {Springer},
318	  year      = {2016},
319	  edition   = {2nd},
320	}
321	
322	@article{ma2024agentboard,
323	  title   = {AgentBoard: An Analytical Evaluation Board of Multi-Turn LLM Agents},
324	  author  = {Chang Ma and Junlei Zhang and Zhihao Zhu and Junjie Wang and others},
325	  journal = {arXiv preprint arXiv:2401.13178},
326	  year    = {2024},
327	}
328	
329	@inproceedings{liu2008isolationforest,
330	  title     = {Isolation Forest},
331	  author    = {Fei Tony Liu and Kai Ming Ting and Zhi-Hua Zhou},
332	  booktitle = {IEEE International Conference on Data Mining},
333	  year      = {2008},
334	}
335	
336	@inproceedings{malhotra2015lstmad,
337	  title     = {Long Short Term Memory Networks for Anomaly Detection in Time Series},
338	  author    = {Pankaj Malhotra and Lovekesh Vig and Gautam Shroff and Puneet Agarwal},
339	  booktitle = {European Symposium on Artificial Neural Networks},
340	  year      = {2015},
341	}
342	
343	@inproceedings{le2022coderl,
344	  title     = {CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning},
345	  author    = {Hung Le and Yue Wang and Akhilesh Deepak Gotmare and Silvio Savarese and Steven C.H. Hoi},
346	  booktitle = {Advances in Neural Information Processing Systems},
347	  year      = {2022},
348	}
349	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "29180cd5-0cd3-4fd3-a730-3d0e03c6883c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/references.bib",
      "content": "% ==============================================================\n% CATEGORY: direct-competitor\n% ==============================================================\n\n@article{xi2025agentprm,\n  title   = {AgentPRM: Process Reward Models for LLM Agents via Step-Wise Promise and Progress},\n  author  = {Zhiheng Xi and Chenyang Liao and Guanyu Li and others},\n  journal = {arXiv preprint arXiv:2511.08325},\n  year    = {2025},\n}\n\n@article{choudhury2025prm,\n  title   = {Process Reward Models for LLM Agents: Practical Framework and Directions},\n  author  = {Sanjiban Choudhury},\n  journal = {arXiv preprint arXiv:2502.10325},\n  year    = {2025},\n}\n\n@article{li2026toolprmbench,\n  title   = {ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents},\n  author  = {Dawei Li and Yuguang Yao and Zhen Tan and Huan Liu and Ruocheng Guo},\n  journal = {arXiv preprint arXiv:2601.12294},\n  year    = {2026},\n}\n\n@article{wang2026planrewardbench,\n  title   = {Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling},\n  author  = {Jiaxuan Wang and Yulan Hu and Wenjin Yang and others},\n  journal = {arXiv preprint arXiv:2604.08178},\n  year    = {2026},\n}\n\n@inproceedings{chen2025monitoring,\n  title     = {Monitoring LLM Agents for Sequentially Contextual Harm},\n  author    = {Yueh-Han Chen and Neelay Joshi and Yulin Chen and He He and Rico Angell},\n  booktitle = {ICLR 2025 Workshop on Building Trust in Language Models and Applications},\n  year      = {2025},\n}\n\n@article{kale2025weaktostrong,\n  title   = {Reliable Weak-to-Strong Monitoring of LLM Agents},\n  author  = {Neil Kale and Chen Bo Calvin Zhang and Kevin Zhu and others},\n  journal = {arXiv preprint arXiv:2508.19461},\n  year    = {2025},\n}\n\n@article{fan2026agentrm,\n  title   = {Exploring Reasoning Reward Model for Agents},\n  author  = {Kaixuan Fan and Kaituo Feng and Manyuan Zhang and others},\n  journal = {arXiv preprint arXiv:2601.22154},\n  year    = {2026},\n}\n\n@article{qiu2026dataprm,\n  title   = {Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis},\n  author  = {Zhisong Qiu and Shuofei Qiao and Kewei Xu and others},\n  journal = {arXiv preprint arXiv:2604.24198},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: method-component\n% ==============================================================\n\n@inproceedings{ratner2016dataprogramming,\n  title     = {Data Programming: Creating Large Training Sets, Quickly},\n  author    = {Alexander Ratner and Christopher De Sa and Sen Wu and Daniel Selsam and Christopher Re},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n}\n\n@article{ratner2017snorkel,\n  title   = {Snorkel: Rapid Training Data Creation with Weak Supervision},\n  author  = {Alexander Ratner and Stephen H. Bach and Henry Ehrenberg and others},\n  journal = {Proceedings of the VLDB Endowment},\n  year    = {2018},\n}\n\n@inproceedings{fu2020flyingsquid,\n  title     = {Fast and Three-rious: Speeding Up Weak Supervision with Triplet Methods},\n  author    = {Daniel Y. Fu and Mayee F. Chen and Frederic Sala and others},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2020},\n}\n\n@inproceedings{ratner2019snorkelmetal,\n  title     = {Training Complex Models with Multi-Task Weak Supervision},\n  author    = {Alexander Ratner and Braden Hancock and Jared Dunnmon and others},\n  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n  year      = {2019},\n}\n\n@inproceedings{zhang2021wrench,\n  title     = {WRENCH: A Comprehensive Benchmark for Weak Supervision},\n  author    = {Jieyu Zhang and Yue Yu and Yinghao Li and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n}\n\n@inproceedings{safranchik2020linkedhmm,\n  title     = {Weakly Supervised Sequence Tagging from Noisy Rules},\n  author    = {Esteban Safranchik and Shiying Luo and Stephen H. Bach},\n  booktitle = {AAAI Conference on Artificial Intelligence},\n  year      = {2020},\n}\n\n@inproceedings{sala2019multiresolution,\n  title     = {Multi-Resolution Weak Supervision for Sequential Data},\n  author    = {Frederic Sala and Paroma Varma and Jason Fries and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2019},\n}\n\n@article{dawid1979em,\n  title   = {Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm},\n  author  = {A. P. Dawid and A. M. Skene},\n  journal = {Journal of the Royal Statistical Society, Series C},\n  year    = {1979},\n}\n\n@inproceedings{lison2021skweak,\n  title     = {skweak: Weak Supervision Made Easy for NLP},\n  author    = {Pierre Lison and Jeremy Barnes and Aliaksandr Hubin},\n  booktitle = {Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year      = {2021},\n}\n\n@inproceedings{li2020dividemix,\n  title     = {DivideMix: Learning with Noisy Labels as Semi-Supervised Learning},\n  author    = {Junnan Li and Richard Socher and Steven C.H. Hoi},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n}\n\n@inproceedings{han2018coteaching,\n  title     = {Co-teaching: Robust Training of Deep Neural Networks with Extremely Noisy Labels},\n  author    = {Bo Han and Quanming Yao and Xingrui Yu and Gang Niu and Miao Xu and Weihua Hu and Ivor W. Tsang and Masashi Sugiyama},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2018},\n}\n\n@article{kaufman2012leakage,\n  title   = {Leakage in Data Mining: Formulation, Detection, and Avoidance},\n  author  = {Shachar Kaufman and Saharon Rosset and Claudia Perlich and Ori Stitelman},\n  journal = {ACM Transactions on Knowledge Discovery from Data},\n  volume  = {6},\n  number  = {4},\n  year    = {2012},\n}\n\n@inproceedings{maheshwari2022spear,\n  title     = {Learning to Robustly Aggregate Labeling Functions for Semi-supervised Data Programming},\n  author    = {Ayush Maheshwari and Hewitt Oommen and Nicholas Monath and others},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2022},\n  year      = {2022},\n}\n\n@article{manheim2018goodhart,\n  title   = {Categorizing Variants of Goodhart's Law},\n  author  = {David Manheim and Scott Garrabrant},\n  journal = {arXiv preprint arXiv:1803.04585},\n  year    = {2018},\n}\n\n% ==============================================================\n% CATEGORY: evaluation\n% ==============================================================\n\n@article{orlanski2026slopcodebench,\n  title   = {SlopCodeBench: Benchmarking How Coding Agents Degrade Over Long-Horizon Iterative Tasks},\n  author  = {Gabriel Orlanski and Devjeet Roy and Alexander Yun and others},\n  journal = {arXiv preprint arXiv:2603.24755},\n  year    = {2026},\n}\n\n@inproceedings{jimenez2024swebench,\n  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},\n  author    = {Carlos E. Jimenez and John Yang and Alexander Wettig and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@inproceedings{yang2024sweagent,\n  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},\n  author    = {John Yang and Carlos E. Jimenez and Alexander Wettig and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2024},\n}\n\n@inproceedings{wang2025openhands,\n  title     = {OpenHands: An Open Platform for AI Software Developers as Generalist Agents},\n  author    = {Xingyao Wang and Boxuan Li and Yufan Song and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n}\n\n% ==============================================================\n% CATEGORY: background\n% ==============================================================\n\n@inproceedings{shinn2023reflexion,\n  title     = {Reflexion: Language Agents with Verbal Reinforcement Learning},\n  author    = {Noah Shinn and Federico Cassano and Ashwin Gopinath and Karthik Narasimhan and Shunyu Yao},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@inproceedings{zhou2024lats,\n  title     = {Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models},\n  author    = {Andy Zhou and Kai Yan and Michal Shlapentokh-Rothman and Haohan Wang and Yu-Xiong Wang},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n}\n\n@inproceedings{yao2023tot,\n  title     = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},\n  author    = {Shunyu Yao and Dian Yu and Jeffrey Zhao and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n}\n\n@article{cemri2025multiagentfail,\n  title   = {Why Do Multi-Agent LLM Systems Fail?},\n  author  = {Mert Cemri and Melissa Z. Pan and Shuyi Yang and others},\n  journal = {arXiv preprint arXiv:2503.13657},\n  year    = {2025},\n}\n\n@article{zhu2025agentfail,\n  title   = {Where LLM Agents Fail and How They Can Learn From Failures},\n  author  = {Kunlun Zhu and Zijia Liu and Bingxuan Li and others},\n  journal = {arXiv preprint arXiv:2509.25370},\n  year    = {2025},\n}\n\n@article{george2025cycledetection,\n  title   = {Unsupervised Cycle Detection in Agentic Applications},\n  author  = {Felix George and Harshit Kumar and Divya Pathak and others},\n  journal = {arXiv preprint arXiv:2511.10650},\n  year    = {2025},\n}\n\n@article{pipis2025reasoningloop,\n  title   = {Wait, Wait, Wait... Why Do Reasoning Models Loop?},\n  author  = {Charilaos Pipis and Shivam Garg and Vasilis Kontonis and others},\n  journal = {arXiv preprint arXiv:2512.12895},\n  year    = {2025},\n}\n\n@inproceedings{huang2024selfcorrect,\n  title     = {Large Language Models Cannot Self-Correct Reasoning Yet},\n  author    = {Jie Huang and Xinyun Chen and Swaroop Mishra and others},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n}\n\n@article{kamoi2024selfcorrection,\n  title   = {When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs},\n  author  = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2024},\n}\n\n@article{liu2026trajad,\n  title   = {TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents},\n  author  = {Yibing Liu and Chong Zhang and Zhongyi Han and others},\n  journal = {arXiv preprint arXiv:2602.06443},\n  year    = {2026},\n}\n\n% ==============================================================\n% CATEGORY: technique\n% ==============================================================\n\n@inproceedings{cho2014gru,\n  title     = {Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation},\n  author    = {Kyunghyun Cho and Bart van Merrienboer and Caglar Gulcehre and others},\n  booktitle = {Conference on Empirical Methods in Natural Language Processing},\n  year      = {2014},\n}\n\n@inproceedings{bahdanau2015attention,\n  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},\n  author    = {Dzmitry Bahdanau and Kyunghyun Cho and Yoshua Bengio},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2015},\n}\n\n@article{zhang2025qwen3embedding,\n  title   = {Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models},\n  author  = {Yanzhao Zhang and Mingxin Li and Dingkun Long and others},\n  journal = {arXiv preprint arXiv:2506.05176},\n  year    = {2025},\n}\n\n@article{wang2024e5,\n  title   = {Multilingual E5 Text Embeddings: A Technical Report},\n  author  = {Liang Wang and Nan Yang and Xiaolong Huang and others},\n  journal = {arXiv preprint arXiv:2402.05672},\n  year    = {2024},\n}\n\n@article{chen2024bgem3,\n  title   = {BGE M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation},\n  author  = {Jianlv Chen and Shitao Xiao and Peitian Zhang and others},\n  journal = {arXiv preprint arXiv:2402.03216},\n  year    = {2024},\n}\n\n% ==============================================================\n% CATEGORY: related-work-additions (Round 1 revision)\n% ==============================================================\n\n@book{vanderaalst2016processmining,\n  title     = {Process Mining: Data Science in Action},\n  author    = {Wil M. P. van der Aalst},\n  publisher = {Springer},\n  year      = {2016},\n  edition   = {2nd},\n}\n\n@article{ma2024agentboard,\n  title   = {AgentBoard: An Analytical Evaluation Board of Multi-Turn LLM Agents},\n  author  = {Chang Ma and Junlei Zhang and Zhihao Zhu and Junjie Wang and others},\n  journal = {arXiv preprint arXiv:2401.13178},\n  year    = {2024},\n}\n\n@inproceedings{liu2008isolationforest,\n  title     = {Isolation Forest},\n  author    = {Fei Tony Liu and Kai Ming Ting and Zhi-Hua Zhou},\n  booktitle = {IEEE International Conference on Data Mining},\n  year      = {2008},\n}\n\n@inproceedings{malhotra2015lstmad,\n  title     = {Long Short Term Memory Networks for Anomaly Detection in Time Series},\n  author    = {Pankaj Malhotra and Lovekesh Vig and Gautam Shroff and Puneet Agarwal},\n  booktitle = {European Symposium on Artificial Neural Networks},\n  year      = {2015},\n}\n\n@inproceedings{le2022coderl,\n  title     = {CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning},\n  author    = {Hung Le and Yue Wang and Akhilesh Deepak Gotmare and Silvio Savarese and Steven C.H. Hoi},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n}\n",
      "numLines": 349,
      "startLine": 1,
      "totalLines": 349
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01Pxc9DHTMMUd9jAoz4okRvY`</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "f3ee3ec7-b700-411a-944e-8b866a83e7bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vv3ws2A5ZJKSVL8LUMaAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 9 · 2026-05-15T05:22:32.014Z_

<details><summary>↩ Tool result · `toolu_01Pxc9DHTMMUd9jAoz4okRvY`</summary>

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
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "28ce6fba-ce10-4b28-a9da-dc376ffe616a",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 6,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_011uiRsivVauUixjgfn2vC5p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "b9b589e1-dc7e-4450-9cbe-dc3617ea7527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012vv3ws2A5ZJKSVL8LUMaAU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 11 · 2026-05-15T05:22:32.414Z_

<details><summary>↩ Tool result · `toolu_011uiRsivVauUixjgfn2vC5p`</summary>

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	\usepackage{enumitem}
19	
20	\newcommand{\todo}[1]{\textcolor{red}{[TODO: #1]}}
21	% \goldset command removed — all placeholders replaced with content
22	
23	\title{Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision}
24	
25	\author{Anonymous}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{sections/abstract}
31	\input{sections/introduction}
32	\input{sections/related_work}
33	\input{sections/method}
34	\input{sections/experiments}
35	\input{sections/analysis}
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{sections/appendix}
45	
46	\end{document}
47	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "f5c88b0b-e05c-4c6f-bda7-30d6ca3a3421",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{enumitem}\n\n\\newcommand{\\todo}[1]{\\textcolor{red}{[TODO: #1]}}\n% \\goldset command removed — all placeholders replaced with content\n\n\\title{Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/analysis}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 47,
      "startLine": 1,
      "totalLines": 47
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The Glob returned no files - probably need to use the full path. Let me get the sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "7115e963-ecf2-4b9b-a75f-5628c49b0686",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bfy7aK4EFFcKLdNxiWLVYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 23962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6055
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WwcVdxZYTW8rEVJbVLnRHb`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "9a02c13a-37bb-4d9a-bd65-9d3f3c6093e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bfy7aK4EFFcKLdNxiWLVYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6055,
      "cache_read_input_tokens": 23962,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6055
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

_source line 14 · 2026-05-15T05:22:36.695Z_

<details><summary>↩ Tool result · `toolu_01WwcVdxZYTW8rEVJbVLnRHb`</summary>

```text
docs/paper/_acl_template/acl_lualatex.tex
docs/paper/_acl_template/acl_latex.tex
docs/paper/sections/method.tex
docs/paper/sections/limitations.tex
docs/paper/sections/related_work.tex
docs/paper/main.tex
docs/paper/sections/abstract.tex
docs/paper/sections/appendix.tex
docs/paper/sections/analysis.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "3f0fe2a7-bf4c-467d-8177-d8d6e202458c",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_acl_template/acl_lualatex.tex",
      "docs/paper/_acl_template/acl_latex.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/experiments.tex"
    ],
    "durationMs": 30,
    "numFiles": 12,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01CL95BnfxSzhqv4sR7DYLGr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "86a6c310-4b33-4652-9020-19041c6c75a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 16 · 2026-05-15T05:22:39.057Z_

<details><summary>↩ Tool result · `toolu_01CL95BnfxSzhqv4sR7DYLGr`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
5	As these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.
6	\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 77\% and quality drops of 75.5\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.
7	Crucially, the dominant failure pattern is not simple repetition but what we term \emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
8	This ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.
9	We observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \citep{yang2024sweagent} and OpenHands \citep{wang2025openhands}---on SWE-bench tasks \citep{jimenez2024swebench}, 28.5\% and 20.9\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.
10	
11	Existing approaches address aspects of this problem but fall short in three ways.
12	First, \emph{repetition detectors} such as cycle detection \citep{george2025cycledetection} and SpecRA \citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.
13	Second, \emph{step-level scoring} via process reward models \citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \citep{chen2025monitoring}.
14	A sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.
15	Third, \emph{LLM self-evaluation} \citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.663 macro-F1 at \$11.66 per test set, well below lightweight feature-based alternatives.
16	More fundamentally, none of these approaches asks the prior question: \emph{what signals actually carry stagnation information?}
17	No systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.
18	
19	We address this question through a systematic empirical study (Figure~\ref{fig:pipeline}).
20	Using a weak supervision framework \citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\% silver-labeled stagnation) and OpenHands (150,652 windows, 20.9\% stagnation).
21	Three labeling functions provide complementary noisy votes: command repetition ($\lambda_1$) targets repetitive behavior, file diff delta ($\lambda_2$) targets output productivity, and outcome backpropagation ($\lambda_3$) propagates task-level outcomes backward through the trajectory.
22	Majority vote aggregation produces window-level binary labels with confidence scores.
23	Our window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.
24	Against these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.
25	
26	Our study yields three principal findings.
27	
28	\textbf{Finding 1: Structural features enable effective zero-data cross-coding-agent transfer, but probes surpass them with fine-tuning.}
29	Thirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \citep{cho2014gru} zero-shot by 36.9\,pp (0.598 on OpenHands, near chance) and the best LLM judge by 16.8\,pp.
30	However, with 100\% target fine-tuning the probe reaches 0.976 macro-F1, surpassing the structural baseline on all windows (0.967)---demonstrating that probe representations recover cross-coding-agent generalization with sufficient adaptation data.
31	We note that in-domain evaluation uses silver labels (\S\ref{sec:circular}); cross-coding-agent transfer and a pending gold set (\S\ref{sec:gold_set}) provide non-circular validation.
32	The structural advantage is encoder-agnostic: three embedding backbones \citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.
33	The in-domain score of 0.995 reflects circular evaluation---structural features overlap with LF inputs---but the cross-coding-agent score of 0.967, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.
34	A feature overlap ablation (\S\ref{sec:feature_overlap}) confirms that the 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1 on all windows---exceeding the full model by 1.0\,pp---while 19 residual features collapse to 0.566: the features that generalize encode universal stagnation signals, and their LF alignment reflects correct LF design rather than circularity.
35	This finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.
36	
37	\textbf{Finding 2: Label quality, not LF selection, is the dominant cross-coding-agent transfer bottleneck.}
38	Labeling functions exhibit systematic temporal dynamics that reverse across agents: command repetition ($\lambda_1$) leads stagnation onset on SWE-Agent by $-1.87$ steps but lags on OpenHands by $+3.32$ steps.
39	A label quality audit reveals that fixing OH label version bias---correcting stagnation rate from 6.56\% to 21.4\%---improves 5\% fine-tuning F1 from 0.570 (under previous label version) to 0.850.
40	Prevalence-matched ablation shows that $\lambda_1$'s core value is coverage ($-29.4$\,pp when removed, $p \approx 0$), not label precision: it fires on only 5.39\% of OH windows with precision 97.91\% (FP rate 2.3\%).
41	
42	\textbf{Finding 3: No label model improves over majority vote.}
43	Five label models---three temporal (TWV, HMM \citep{safranchik2020linkedhmm}, lag-aware HMM) and two generative (FlyingSquid \citep{fu2020flyingsquid}, Snorkel MeTaL \citep{ratner2019snorkelmetal})---all fail to surpass majority vote on downstream detection.
44	TWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\,pp; Snorkel MeTaL collapses catastrophically ($-$63.6\,pp).
45	The bottleneck is LF quantity, not aggregation sophistication: three binary LFs produce too little inter-LF conflict for any method to exploit.
46	
47	Our contributions are:
48	\begin{enumerate}
49	    \item \textbf{Weak supervision methodology for agent monitoring.} We design a silver-labeling pipeline (3 LFs + majority vote) over 205K+ windows from two coding agents, enabling systematic comparison of detection methods without manual annotation.
50	    \item \textbf{Label quality as transfer bottleneck.} We show that labeling functions exhibit agent-specific temporal reversals and that fixing label version bias (stag rate 6.56\%$\to$21.4\% on the embedding subset) is the dominant factor for cross-coding-agent transfer, informing future weak-supervision design on sequential agent data.
51	    \item \textbf{Label model negative finding.} We show that five label models---three temporal and two generative---fail to improve over majority vote for downstream detection. The bottleneck is LF quantity, not aggregation method: the 3-LF regime produces insufficient inter-LF conflict for any approach to add value.
52	    \item \textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\,pp and the best LLM judge by 16.8\,pp on silver labels (no GPU, ${<}$5\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.
53	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "4a56b4ed-03c4-4297-bc39-1cd2f61b9936",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 77\\% and quality drops of 75.5\\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.\nCrucially, the dominant failure pattern is not simple repetition but what we term \\emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nThis ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.\nWe observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \\citep{yang2024sweagent} and OpenHands \\citep{wang2025openhands}---on SWE-bench tasks \\citep{jimenez2024swebench}, 28.5\\% and 20.9\\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.\n\nExisting approaches address aspects of this problem but fall short in three ways.\nFirst, \\emph{repetition detectors} such as cycle detection \\citep{george2025cycledetection} and SpecRA \\citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\nSecond, \\emph{step-level scoring} via process reward models \\citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \\citep{chen2025monitoring}.\nA sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.\nThird, \\emph{LLM self-evaluation} \\citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.663 macro-F1 at \\$11.66 per test set, well below lightweight feature-based alternatives.\nMore fundamentally, none of these approaches asks the prior question: \\emph{what signals actually carry stagnation information?}\nNo systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.\n\nWe address this question through a systematic empirical study (Figure~\\ref{fig:pipeline}).\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\\% silver-labeled stagnation) and OpenHands (150,652 windows, 20.9\\% stagnation).\nThree labeling functions provide complementary noisy votes: command repetition ($\\lambda_1$) targets repetitive behavior, file diff delta ($\\lambda_2$) targets output productivity, and outcome backpropagation ($\\lambda_3$) propagates task-level outcomes backward through the trajectory.\nMajority vote aggregation produces window-level binary labels with confidence scores.\nOur window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \\emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.\nAgainst these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.\n\nOur study yields three principal findings.\n\n\\textbf{Finding 1: Structural features enable effective zero-data cross-coding-agent transfer, but probes surpass them with fine-tuning.}\nThirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.995 macro-F1 in-domain (Random Forest) and 0.967 cross-coding-agent macro-F1 (Gradient Boosting, SWE-Agent $\\to$ OpenHands) with zero target data, outperforming the GRU embedding probe \\citep{cho2014gru} zero-shot by 36.9\\,pp (0.598 on OpenHands, near chance) and the best LLM judge by 16.8\\,pp.\nHowever, with 100\\% target fine-tuning the probe reaches 0.976 macro-F1, surpassing the structural baseline on all windows (0.967)---demonstrating that probe representations recover cross-coding-agent generalization with sufficient adaptation data.\nWe note that in-domain evaluation uses silver labels (\\S\\ref{sec:circular}); cross-coding-agent transfer and a pending gold set (\\S\\ref{sec:gold_set}) provide non-circular validation.\nThe structural advantage is encoder-agnostic: three embedding backbones \\citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.\nThe in-domain score of 0.995 reflects circular evaluation---structural features overlap with LF inputs---but the cross-coding-agent score of 0.967, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.\nA feature overlap ablation (\\S\\ref{sec:feature_overlap}) confirms that the 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1 on all windows---exceeding the full model by 1.0\\,pp---while 19 residual features collapse to 0.566: the features that generalize encode universal stagnation signals, and their LF alignment reflects correct LF design rather than circularity.\nThis finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\n\\textbf{Finding 2: Label quality, not LF selection, is the dominant cross-coding-agent transfer bottleneck.}\nLabeling functions exhibit systematic temporal dynamics that reverse across agents: command repetition ($\\lambda_1$) leads stagnation onset on SWE-Agent by $-1.87$ steps but lags on OpenHands by $+3.32$ steps.\nA label quality audit reveals that fixing OH label version bias---correcting stagnation rate from 6.56\\% to 21.4\\%---improves 5\\% fine-tuning F1 from 0.570 (under previous label version) to 0.850.\nPrevalence-matched ablation shows that $\\lambda_1$'s core value is coverage ($-29.4$\\,pp when removed, $p \\approx 0$), not label precision: it fires on only 5.39\\% of OH windows with precision 97.91\\% (FP rate 2.3\\%).\n\n\\textbf{Finding 3: No label model improves over majority vote.}\nFive label models---three temporal (TWV, HMM \\citep{safranchik2020linkedhmm}, lag-aware HMM) and two generative (FlyingSquid \\citep{fu2020flyingsquid}, Snorkel MeTaL \\citep{ratner2019snorkelmetal})---all fail to surpass majority vote on downstream detection.\nTWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\\,pp; Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp).\nThe bottleneck is LF quantity, not aggregation sophistication: three binary LFs produce too little inter-LF conflict for any method to exploit.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Weak supervision methodology for agent monitoring.} We design a silver-labeling pipeline (3 LFs + majority vote) over 205K+ windows from two coding agents, enabling systematic comparison of detection methods without manual annotation.\n    \\item \\textbf{Label quality as transfer bottleneck.} We show that labeling functions exhibit agent-specific temporal reversals and that fixing label version bias (stag rate 6.56\\%$\\to$21.4\\% on the embedding subset) is the dominant factor for cross-coding-agent transfer, informing future weak-supervision design on sequential agent data.\n    \\item \\textbf{Label model negative finding.} We show that five label models---three temporal and two generative---fail to improve over majority vote for downstream detection. The bottleneck is LF quantity, not aggregation method: the 3-LF regime produces insufficient inter-LF conflict for any approach to add value.\n    \\item \\textbf{Deployment-regime trade-off.} In zero-data settings, 30 structural features outperform the neural probe by 36.9\\,pp and the best LLM judge by 16.8\\,pp on silver labels (no GPU, ${<}$5\\,ms per window). With target-agent fine-tuning, the probe surpasses structural features (0.976 vs.\\ 0.967 macro-F1), delineating when structural monitoring suffices and when fine-tuning is warranted.\n\\end{enumerate}",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_014QD5p2ShSnwDuJU9vyagG4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "a944dab1-5d45-469c-961e-aab336441550",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 18 · 2026-05-15T05:22:39.406Z_

<details><summary>↩ Tool result · `toolu_014QD5p2ShSnwDuJU9vyagG4`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Process Reward Models.}
5	Process reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.
6	\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.
7	\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.
8	Evaluation benchmarks have emerged in parallel: \citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.
9	\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.
10	\citet{le2022coderl} take a value-function approach to code generation, training a critic model to estimate the expected future reward of partial programs---a complementary strategy that operates on program states rather than agent action windows.
11	Our work differs from PRMs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\,ms per window) rather than training signal generation.
12	
13	\paragraph{Agent Self-Reflection and Verification.}
14	Self-reflection methods prompt agents to diagnose and correct their own failures.
15	\citet{shinn2023reflexion} introduce verbal self-reflection loops, \citet{yao2023tot} propose tree-structured deliberation, and \citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.
16	However, \citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.
17	These methods address what to \emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.
18	We address the prior question---\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.
19	Our LLM-as-judge baseline (\S\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.
20	
21	\paragraph{Weak Supervision for Sequential Data.}
22	Data programming \citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.
23	\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\ samples.
24	Extensions to sequential data relax this assumption: \citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\ label models by incorporating span-level linking rules; \citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.
25	More recently, \citet{lison2021skweak} provide skweak, a toolkit for combining heterogeneous labeling functions over token sequences with flexible aggregation, demonstrating that practical WS for sequential data requires careful treatment of abstaining and overlapping LFs.
26	We apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.
27	Unlike \citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\S\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.
28	
29	\paragraph{Learning from Noisy Labels.}
30	Our silver-label pipeline produces labels with systematic noise from LF disagreement, connecting to the broader noisy label learning literature.
31	\citet{han2018coteaching} introduce co-teaching, where two networks train simultaneously and select small-loss samples for each other, mitigating confirmation bias in the presence of label noise.
32	\citet{li2020dividemix} extend this with DivideMix, combining sample selection via a Gaussian mixture model with semi-supervised learning on discarded samples.
33	These methods assume instance-level noise that is approximately class-conditional; our setting differs in that noise is structurally correlated---LFs introduce temporal block noise (entire stagnation episodes may be mislabeled) rather than independent per-sample flips.
34	Our confidence-based stratification (conf${\geq}$2 vs.\ conf${=}$1) serves an analogous role to sample selection: high-confidence windows train the detector, while ambiguous windows are effectively down-weighted.
35	This connection suggests that co-teaching or mixture-model selection over LF agreement patterns could complement majority vote aggregation in future work.
36	
37	\paragraph{Label Leakage and Goodhart Effects.}
38	When evaluation targets are derived from the same signals used as input features, the resulting metric can overstate true performance---a phenomenon formalized as label leakage \citep{kaufman2012leakage}.
39	In our setting, structural features overlap with LF inputs (e.g., repetition ratios feed both the cmd\_rep LF and the structural classifier), producing the 0.995 in-domain F1 that we flag as circular (\S\ref{sec:circular}).
40	This overlap also instantiates a form of Goodhart's Law \citep{manheim2018goodhart}: optimizing a classifier against LF-derived silver labels risks learning to reconstruct LF voting patterns rather than detecting genuine stagnation.
41	We mitigate this through cross-coding-agent transfer evaluation, where the model is tested on a different agent's LF distribution, and through a pending human-annotated gold set (\S\ref{sec:gold_set}).
42	Recent programmatic weak supervision work addresses related concerns: \citet{maheshwari2022spear} propose SPEAR, a semi-supervised data programming framework that jointly learns LF reliability and a downstream model, reducing sensitivity to LF design choices---a direction that could help decouple structural classifiers from their LF-derived training signal.
43	
44	\paragraph{Agent Monitoring and Degradation.}
45	Recent work documents the prevalence and impact of agent failures at scale.
46	\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.
47	\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.
48	\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.
49	\citet{ma2024agentboard} introduce AgentBoard with a fine-grained progress rate metric that tracks partial task completion across sub-goals, providing complementary trajectory-level measurement to our window-level binary classification.
50	\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.
51	These works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across coding agent architectures without requiring another LLM or GPU.
52	
53	\paragraph{Process Mining.}
54	Our structural feature approach draws on the tradition of process mining \citep{vanderaalst2016processmining}, which extracts behavioral patterns from event logs of sequential processes using hand-crafted features such as variant frequencies, conformance metrics, and performance indicators.
55	LLM agent trajectories---sequences of commands, file edits, and outputs---are structurally analogous to business process event logs, and our 30 structural features (repetition ratios, file operation counts, edit distances) can be viewed as process mining features applied to agent action logs.
56	The success of these features in cross-coding-agent transfer (0.967 macro-F1 with no GPU) provides evidence that agent trajectories, like business processes, exhibit sufficiently regular structural signatures for lightweight monitoring.
57	
58	\paragraph{Cycle and Anomaly Detection.}
59	Cycle detection targets structural repetition in agent behavior.
60	\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents.
61	\citet{pipis2025reasoningloop} propose SpecRA, analyzing reasoning loops in language models via speculative decoding and $n$-gram repetition heuristics---a direct competitor that targets a subset of our stagnation definition (repetitive loops) but does not address semantically diverse stagnation where surface behavior varies.
62	\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.
63	In classical sequential anomaly detection, hand-crafted features often outperform learned representations on narrow detection tasks: Isolation Forest \citep{liu2008isolationforest} achieves strong performance with random feature subspaces, and LSTM-based anomaly detectors \citep{malhotra2015lstmad} require substantial training data to surpass feature-based baselines.
64	Our finding that structural features outperform the neural probe in zero-data transfer parallels this pattern.
65	We formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\S\ref{sec:setup}), and our error analysis (\S\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "b1608fb3-9c9f-4339-b895-9c4012690b2c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Process Reward Models.}\nProcess reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.\n\\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \\citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \\citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.\n\\citet{le2022coderl} take a value-function approach to code generation, training a critic model to estimate the expected future reward of partial programs---a complementary strategy that operates on program states rather than agent action windows.\nOur work differs from PRMs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\\,ms per window) rather than training signal generation.\n\n\\paragraph{Agent Self-Reflection and Verification.}\nSelf-reflection methods prompt agents to diagnose and correct their own failures.\n\\citet{shinn2023reflexion} introduce verbal self-reflection loops, \\citet{yao2023tot} propose tree-structured deliberation, and \\citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.\nHowever, \\citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \\citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.\nThese methods address what to \\emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.\nWe address the prior question---\\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.\nOur LLM-as-judge baseline (\\S\\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.\n\n\\paragraph{Weak Supervision for Sequential Data.}\nData programming \\citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \\citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.\n\\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \\citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\\ samples.\nExtensions to sequential data relax this assumption: \\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\\ label models by incorporating span-level linking rules; \\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \\citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.\nMore recently, \\citet{lison2021skweak} provide skweak, a toolkit for combining heterogeneous labeling functions over token sequences with flexible aggregation, demonstrating that practical WS for sequential data requires careful treatment of abstaining and overlapping LFs.\nWe apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.\nUnlike \\citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\\S\\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.\n\n\\paragraph{Learning from Noisy Labels.}\nOur silver-label pipeline produces labels with systematic noise from LF disagreement, connecting to the broader noisy label learning literature.\n\\citet{han2018coteaching} introduce co-teaching, where two networks train simultaneously and select small-loss samples for each other, mitigating confirmation bias in the presence of label noise.\n\\citet{li2020dividemix} extend this with DivideMix, combining sample selection via a Gaussian mixture model with semi-supervised learning on discarded samples.\nThese methods assume instance-level noise that is approximately class-conditional; our setting differs in that noise is structurally correlated---LFs introduce temporal block noise (entire stagnation episodes may be mislabeled) rather than independent per-sample flips.\nOur confidence-based stratification (conf${\\geq}$2 vs.\\ conf${=}$1) serves an analogous role to sample selection: high-confidence windows train the detector, while ambiguous windows are effectively down-weighted.\nThis connection suggests that co-teaching or mixture-model selection over LF agreement patterns could complement majority vote aggregation in future work.\n\n\\paragraph{Label Leakage and Goodhart Effects.}\nWhen evaluation targets are derived from the same signals used as input features, the resulting metric can overstate true performance---a phenomenon formalized as label leakage \\citep{kaufman2012leakage}.\nIn our setting, structural features overlap with LF inputs (e.g., repetition ratios feed both the cmd\\_rep LF and the structural classifier), producing the 0.995 in-domain F1 that we flag as circular (\\S\\ref{sec:circular}).\nThis overlap also instantiates a form of Goodhart's Law \\citep{manheim2018goodhart}: optimizing a classifier against LF-derived silver labels risks learning to reconstruct LF voting patterns rather than detecting genuine stagnation.\nWe mitigate this through cross-coding-agent transfer evaluation, where the model is tested on a different agent's LF distribution, and through a pending human-annotated gold set (\\S\\ref{sec:gold_set}).\nRecent programmatic weak supervision work addresses related concerns: \\citet{maheshwari2022spear} propose SPEAR, a semi-supervised data programming framework that jointly learns LF reliability and a downstream model, reducing sensitivity to LF design choices---a direction that could help decouple structural classifiers from their LF-derived training signal.\n\n\\paragraph{Agent Monitoring and Degradation.}\nRecent work documents the prevalence and impact of agent failures at scale.\n\\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.\n\\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.\n\\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.\n\\citet{ma2024agentboard} introduce AgentBoard with a fine-grained progress rate metric that tracks partial task completion across sub-goals, providing complementary trajectory-level measurement to our window-level binary classification.\n\\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \\citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.\nThese works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across coding agent architectures without requiring another LLM or GPU.\n\n\\paragraph{Process Mining.}\nOur structural feature approach draws on the tradition of process mining \\citep{vanderaalst2016processmining}, which extracts behavioral patterns from event logs of sequential processes using hand-crafted features such as variant frequencies, conformance metrics, and performance indicators.\nLLM agent trajectories---sequences of commands, file edits, and outputs---are structurally analogous to business process event logs, and our 30 structural features (repetition ratios, file operation counts, edit distances) can be viewed as process mining features applied to agent action logs.\nThe success of these features in cross-coding-agent transfer (0.967 macro-F1 with no GPU) provides evidence that agent trajectories, like business processes, exhibit sufficiently regular structural signatures for lightweight monitoring.\n\n\\paragraph{Cycle and Anomaly Detection.}\nCycle detection targets structural repetition in agent behavior.\n\\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents.\n\\citet{pipis2025reasoningloop} propose SpecRA, analyzing reasoning loops in language models via speculative decoding and $n$-gram repetition heuristics---a direct competitor that targets a subset of our stagnation definition (repetitive loops) but does not address semantically diverse stagnation where surface behavior varies.\n\\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.\nIn classical sequential anomaly detection, hand-crafted features often outperform learned representations on narrow detection tasks: Isolation Forest \\citep{liu2008isolationforest} achieves strong performance with random feature subspaces, and LSTM-based anomaly detectors \\citep{malhotra2015lstmad} require substantial training data to surpass feature-based baselines.\nOur finding that structural features outperform the neural probe in zero-data transfer parallels this pattern.\nWe formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\\S\\ref{sec:setup}), and our error analysis (\\S\\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss.",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01Ca8pWweaKbnbbBvi6jm32x`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "3ac14f27-4655-4033-b7f4-18ca153de113",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 20 · 2026-05-15T05:22:39.848Z_

<details><summary>↩ Tool result · `toolu_01Ca8pWweaKbnbbBvi6jm32x`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We frame stagnation detection as window-level binary classification over agent trajectories.
5	Silver labels are generated via weak supervision from three labeling functions, then used to train and evaluate three detection approaches: structural features, a neural embedding probe, and an LLM-as-judge baseline.
6	Figure~\ref{fig:pipeline} provides a system overview.
7	
8	\begin{figure*}[t]
9	\centering
10	\includegraphics[width=\textwidth]{../../figures/paper/fig_pipeline.pdf}
11	\caption{System overview. (Left) Agent trajectories are segmented into overlapping windows of $k{=}5$ steps. (Center) Three labeling functions vote on each window; majority vote produces silver labels with confidence 1--3. (Right) Three detection approaches compared: structural features (30-dim), NL embedding probe (GRU), and LLM-as-judge (eval only, not trained on silver labels).}
12	\label{fig:pipeline}
13	\end{figure*}
14	
15	%-------------------------------------------------------------------
16	\subsection{Problem Formulation}
17	\label{sec:problem}
18	
19	Given an agent trajectory $T = (a_1, a_2, \ldots, a_n)$ where each $a_t$ is an action (e.g., a shell command, file edit, or API call), we partition it into overlapping sliding windows $w_i = (a_i, \ldots, a_{i+k-1})$ with window size $k{=}5$ and stride 1.
20	The task is to assign each window a binary label $y_i \in \{0, 1\}$, where 0 denotes \emph{stagnation} (the agent is stuck or unproductive) and 1 denotes \emph{progress} (the agent is making meaningful headway toward the task goal).
21	
22	The window formulation offers two advantages over alternatives.
23	Compared to step-level scoring, windows capture short-range temporal patterns---such as a sequence of repeated failed attempts---that individual actions cannot express.
24	Compared to trajectory-level labeling, windows provide the granularity needed to pinpoint \emph{when} stagnation begins and ends within a single task attempt, enabling downstream interventions such as early termination or strategy switching.
25	
26	%-------------------------------------------------------------------
27	\subsection{Weak Supervision Pipeline}
28	\label{sec:weak_supervision}
29	
30	No gold-standard annotations exist for agent stagnation at the window level.
31	Manual annotation is expensive: each window requires reviewing $k$ actions with full context (command text, outputs, file diffs), taking an estimated 2--3 minutes per window.
32	We therefore adopt a data programming approach \citep{ratner2016dataprogramming,ratner2017snorkel}: multiple labeling functions (LFs) provide noisy votes that are aggregated into silver labels.
33	Each LF $\lambda_j : w_i \to \{0, 1, \bot\}$ examines a window and emits a vote: stagnation (0), progress (1), or abstain ($\bot$).
34	
35	\subsubsection{Labeling Functions}
36	\label{sec:labeling_functions}
37	
38	We design three LFs that target complementary signals of stagnation (Table~\ref{tab:lf_design}).
39	
40	\paragraph{Command repetition ($\lambda_1$).}
41	Computes the proportion of repeated commands within window $w_i$.
42	A high repetition ratio triggers a stagnation vote, capturing overt repetitive behavior such as re-running failing commands.
43	This LF never abstains: it votes stagnation when the repetition ratio exceeds a threshold and progress otherwise.
44	It votes stagnation on 65.5\% of SWE-Agent windows but only 5.4\% of OpenHands windows; the lower OH rate reflects OH's greater action diversity, which reduces command repetition.
45	On OH, cmd\_rep achieves 97.9\% precision with 26.0\% recall, and shifts from leading stagnation onset ($-1.87$ steps on SWE-Agent) to lagging ($+3.32$ steps), demonstrating agent-specific temporal dynamics (\S\ref{sec:cmd_rep_ablation}).
46	
47	\paragraph{File diff delta ($\lambda_2$).}
48	Measures the fraction of steps within $w_i$ that produce code modifications (file creates, edits, or deletes).
49	A low modification frequency triggers a stagnation vote; windows with more than one edited file receive a progress vote; windows with exactly one or zero edits abstain ($\bot$).
50	On OpenHands, this LF achieves 87.5\% recall on stagnation windows (precision 99.9\%), making it the most reliable cross-coding-agent signal.
51	
52	\paragraph{Outcome backpropagation ($\lambda_3$).}
53	Uses the final task outcome (resolved/unresolved) as distant supervision.
54	For unresolved tasks, the last two windows and any windows following a timeout or stuck signal receive stagnation votes; resolved tasks receive progress votes in the corresponding windows.
55	All other windows abstain ($\bot$).
56	Unlike $\lambda_1$ and $\lambda_2$, which operate on local window content, $\lambda_3$ propagates a global signal backward through time.
57	This makes it a form of distant supervision: individually noisy, but complementary to the real-time signals when aggregated.
58	
59	\begin{table}[t]
60	\centering
61	\small
62	\begin{tabular}{llcc}
63	\toprule
64	\textbf{LF} & \textbf{Signal} & \textbf{SWE Stag\,\%} & \textbf{OH Stag\,\%} \\
65	\midrule
66	$\lambda_1$ (cmd\_rep)    & Repetition & 65.5 & 5.4 \\
67	$\lambda_2$ (file\_diff)  & Output     & 57.3 & 17.8 \\
68	$\lambda_3$ (outcome\_bp) & Outcome    & 23.9 & 16.8 \\
69	\bottomrule
70	\end{tabular}
71	\caption{Labeling function design. Stag\,\% = fire rate, i.e., fraction of windows on which the LF votes stagnation (remaining windows receive progress or abstain). SWE = SWE-Agent; OH = OpenHands. OH values reflect corrected action embeddings (\S\ref{sec:cmd_rep_ablation}).}
72	\label{tab:lf_design}
73	\end{table}
74	
75	\subsubsection{Label Aggregation}
76	\label{sec:label_aggregation}
77	
78	Silver labels are produced by majority vote among non-abstaining LFs:
79	\begin{equation}
80	y_i = \text{MV}\bigl(\{\lambda_j(w_i) : \lambda_j(w_i) \neq \bot\}\bigr)
81	\label{eq:mv}
82	\end{equation}
83	We define the confidence of each label as the number of non-abstaining LFs that agree with the winning label: $\text{conf}_i = |\{j : \lambda_j(w_i) \neq \bot \;\text{and}\; \lambda_j(w_i) = y_i\}| \in \{1, 2, 3\}$.
84	Conf${=}1$ arises when a single non-abstaining LF determines the label---either because only one LF votes or because two LFs disagree with no clear majority---producing the most ambiguous labels.
85	The conf${\geq}$2 subset, where at least two non-abstaining LFs agree on the winning label, serves as the primary evaluation set throughout this work.
86	This stratification allows us to separately analyze model behavior on high-confidence vs.\ ambiguous windows (\S\ref{sec:main_results}).
87	
88	%-------------------------------------------------------------------
89	\subsection{Detection Methods}
90	\label{sec:detection_methods}
91	
92	\subsubsection{Structural Features}
93	\label{sec:structural_features}
94	
95	We extract a 30-dimensional feature vector from each window, requiring no pretrained model or GPU.
96	Features span four categories:
97	(1)~\emph{repetition}: exact command repeat ratio, fuzzy match ratio (Levenshtein-based), and unique command ratio;
98	(2)~\emph{file operations}: counts of file creates, modifications, and deletions within the window;
99	(3)~\emph{edit patterns}: edit distances between consecutive actions, capturing how much the agent's behavior changes step-to-step;
100	(4)~\emph{output statistics}: entropy of command outputs and action type distribution features.
101	These features are fed to three classifiers: Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
102	Because several structural features overlap with the signals used by the labeling functions (e.g., repetition ratios relate to $\lambda_1$), structural classifiers can partially reconstruct the LF voting process.
103	We discuss this circularity and its implications in \S\ref{sec:main_results}.
104	
105	\subsubsection{NL Embedding Probe (ProgressProbe)}
106	\label{sec:progressprobe}
107	
108	Each action $a_t$ is encoded as a natural language description and embedded using Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} into a 1024-dimensional vector.
109	The $k$ embeddings within a window form a sequence that is processed by a 2-layer GRU \citep{cho2014gru} with hidden size 256 and dropout 0.1.
110	An attention mechanism \citep{bahdanau2015attention} computes a weighted combination of the GRU hidden states, yielding a single window-level representation.
111	This representation is passed through a fully connected layer with sigmoid activation for binary classification.
112	Training uses binary cross-entropy loss with early stopping (patience 5) on a validation set.
113	
114	The GRU architecture is motivated by the sequential nature of actions within a window: the order in which commands are issued (e.g., repeated failures followed by a different approach) carries diagnostic information that bag-of-embeddings methods discard.
115	We also evaluate two simpler embedding baselines to isolate the contribution of temporal modeling: (1)~mean-pooled Qwen3 embeddings with logistic regression, and (2)~cosine similarity between consecutive window embeddings with a validation-tuned threshold.
116	
117	\subsubsection{LLM-as-Judge Baseline}
118	\label{sec:llm_judge}
119	
120	We prompt Claude Sonnet 4.6 in zero-shot mode to classify each window as stagnation or progress, given the textual descriptions of actions within the window.\footnote{Extended LLM evaluation including chain-of-thought prompting, few-shot examples, and multi-model comparison is reported in Appendix~\ref{sec:llm_extended}.}
121	The LLM judge establishes a cost-performance reference: at \$11.66 per test set, its zero-shot F1 of 0.663 demonstrates that stagnation detection is non-trivial even for capable LLMs without task-specific adaptation.
122	This baseline is not used in the silver label pipeline.
123	
124	%-------------------------------------------------------------------
125	\subsection{Temporal Label Models}
126	\label{sec:temporal_models}
127	
128	The three LFs occupy distinct temporal niches relative to stagnation onset (\S\ref{sec:lf_temporal}): $\lambda_1$ leads by ${\sim}2$ steps, $\lambda_2$ is near-concurrent, and $\lambda_3$ lags by ${\sim}7$ steps.
129	This motivates exploring whether encoding temporal structure into label aggregation can improve over majority vote.
130	
131	\subsubsection{Time-Varying Weights (TWV)}
132	\label{sec:twv}
133	
134	TWV applies Gaussian kernel smoothing to each LF's activation sequence:
135	\begin{equation}
136	\tilde{\lambda}_j(t) = \sum_{t'} K_\sigma(t - t') \cdot \lambda_j(t')
137	\label{eq:twv}
138	\end{equation}
139	where $K_\sigma$ is a Gaussian kernel with bandwidth $\sigma$.
140	Smoothed activations replace raw votes for conf${=}1$ windows (where exactly one LF disagrees), potentially flipping labels in temporally ambiguous regions.
141	The bandwidth $\sigma$ controls the extent of temporal context: larger values incorporate more distant steps.
142	
143	\subsubsection{Hidden Markov Models}
144	\label{sec:hmm}
145	
146	We model the label sequence as a Hidden Markov Model \citep{safranchik2020linkedhmm} with two hidden states (stagnation, progress) and observations defined by the joint activation pattern of the three LFs.
147	Transition and emission parameters are estimated via Expectation-Maximization (EM).
148	The HMM captures temporal persistence---stagnation episodes tend to span multiple consecutive windows---which majority vote, operating independently per window, cannot model.
149	
150	\subsubsection{Lag-Aware HMM}
151	\label{sec:lag_hmm}
152	
153	The standard HMM treats all LFs as synchronous.
154	Lag-Aware HMM extends this by explicitly modeling each LF's temporal offset: $\lambda_1$ is shifted by $-2$ steps, $\lambda_2$ by $-1$, and $\lambda_3$ by $+7$, estimated from the temporal dynamics analysis (\S\ref{sec:lf_temporal}).
155	To prevent divergence, we apply two regularization strategies: (1)~\emph{confidence anchoring}, which fixes labels for conf${\geq}$2 windows and restricts EM updates to conf${=}1$ windows; and (2)~a prior strength of 5000 on transition parameters.
156	These constraints keep the model close to the majority vote baseline while allowing it to resolve temporally ambiguous labels.
157	The intuition is that aligning each LF's activation to its natural temporal role should produce cleaner emission estimates and, consequently, more accurate Viterbi decodings on ambiguous windows.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "f76fd081-0396-4d76-8d9e-ee2a9037598b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe frame stagnation detection as window-level binary classification over agent trajectories.\nSilver labels are generated via weak supervision from three labeling functions, then used to train and evaluate three detection approaches: structural features, a neural embedding probe, and an LLM-as-judge baseline.\nFigure~\\ref{fig:pipeline} provides a system overview.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_pipeline.pdf}\n\\caption{System overview. (Left) Agent trajectories are segmented into overlapping windows of $k{=}5$ steps. (Center) Three labeling functions vote on each window; majority vote produces silver labels with confidence 1--3. (Right) Three detection approaches compared: structural features (30-dim), NL embedding probe (GRU), and LLM-as-judge (eval only, not trained on silver labels).}\n\\label{fig:pipeline}\n\\end{figure*}\n\n%-------------------------------------------------------------------\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven an agent trajectory $T = (a_1, a_2, \\ldots, a_n)$ where each $a_t$ is an action (e.g., a shell command, file edit, or API call), we partition it into overlapping sliding windows $w_i = (a_i, \\ldots, a_{i+k-1})$ with window size $k{=}5$ and stride 1.\nThe task is to assign each window a binary label $y_i \\in \\{0, 1\\}$, where 0 denotes \\emph{stagnation} (the agent is stuck or unproductive) and 1 denotes \\emph{progress} (the agent is making meaningful headway toward the task goal).\n\nThe window formulation offers two advantages over alternatives.\nCompared to step-level scoring, windows capture short-range temporal patterns---such as a sequence of repeated failed attempts---that individual actions cannot express.\nCompared to trajectory-level labeling, windows provide the granularity needed to pinpoint \\emph{when} stagnation begins and ends within a single task attempt, enabling downstream interventions such as early termination or strategy switching.\n\n%-------------------------------------------------------------------\n\\subsection{Weak Supervision Pipeline}\n\\label{sec:weak_supervision}\n\nNo gold-standard annotations exist for agent stagnation at the window level.\nManual annotation is expensive: each window requires reviewing $k$ actions with full context (command text, outputs, file diffs), taking an estimated 2--3 minutes per window.\nWe therefore adopt a data programming approach \\citep{ratner2016dataprogramming,ratner2017snorkel}: multiple labeling functions (LFs) provide noisy votes that are aggregated into silver labels.\nEach LF $\\lambda_j : w_i \\to \\{0, 1, \\bot\\}$ examines a window and emits a vote: stagnation (0), progress (1), or abstain ($\\bot$).\n\n\\subsubsection{Labeling Functions}\n\\label{sec:labeling_functions}\n\nWe design three LFs that target complementary signals of stagnation (Table~\\ref{tab:lf_design}).\n\n\\paragraph{Command repetition ($\\lambda_1$).}\nComputes the proportion of repeated commands within window $w_i$.\nA high repetition ratio triggers a stagnation vote, capturing overt repetitive behavior such as re-running failing commands.\nThis LF never abstains: it votes stagnation when the repetition ratio exceeds a threshold and progress otherwise.\nIt votes stagnation on 65.5\\% of SWE-Agent windows but only 5.4\\% of OpenHands windows; the lower OH rate reflects OH's greater action diversity, which reduces command repetition.\nOn OH, cmd\\_rep achieves 97.9\\% precision with 26.0\\% recall, and shifts from leading stagnation onset ($-1.87$ steps on SWE-Agent) to lagging ($+3.32$ steps), demonstrating agent-specific temporal dynamics (\\S\\ref{sec:cmd_rep_ablation}).\n\n\\paragraph{File diff delta ($\\lambda_2$).}\nMeasures the fraction of steps within $w_i$ that produce code modifications (file creates, edits, or deletes).\nA low modification frequency triggers a stagnation vote; windows with more than one edited file receive a progress vote; windows with exactly one or zero edits abstain ($\\bot$).\nOn OpenHands, this LF achieves 87.5\\% recall on stagnation windows (precision 99.9\\%), making it the most reliable cross-coding-agent signal.\n\n\\paragraph{Outcome backpropagation ($\\lambda_3$).}\nUses the final task outcome (resolved/unresolved) as distant supervision.\nFor unresolved tasks, the last two windows and any windows following a timeout or stuck signal receive stagnation votes; resolved tasks receive progress votes in the corresponding windows.\nAll other windows abstain ($\\bot$).\nUnlike $\\lambda_1$ and $\\lambda_2$, which operate on local window content, $\\lambda_3$ propagates a global signal backward through time.\nThis makes it a form of distant supervision: individually noisy, but complementary to the real-time signals when aggregated.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{LF} & \\textbf{Signal} & \\textbf{SWE Stag\\,\\%} & \\textbf{OH Stag\\,\\%} \\\\\n\\midrule\n$\\lambda_1$ (cmd\\_rep)    & Repetition & 65.5 & 5.4 \\\\\n$\\lambda_2$ (file\\_diff)  & Output     & 57.3 & 17.8 \\\\\n$\\lambda_3$ (outcome\\_bp) & Outcome    & 23.9 & 16.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Labeling function design. Stag\\,\\% = fire rate, i.e., fraction of windows on which the LF votes stagnation (remaining windows receive progress or abstain). SWE = SWE-Agent; OH = OpenHands. OH values reflect corrected action embeddings (\\S\\ref{sec:cmd_rep_ablation}).}\n\\label{tab:lf_design}\n\\end{table}\n\n\\subsubsection{Label Aggregation}\n\\label{sec:label_aggregation}\n\nSilver labels are produced by majority vote among non-abstaining LFs:\n\\begin{equation}\ny_i = \\text{MV}\\bigl(\\{\\lambda_j(w_i) : \\lambda_j(w_i) \\neq \\bot\\}\\bigr)\n\\label{eq:mv}\n\\end{equation}\nWe define the confidence of each label as the number of non-abstaining LFs that agree with the winning label: $\\text{conf}_i = |\\{j : \\lambda_j(w_i) \\neq \\bot \\;\\text{and}\\; \\lambda_j(w_i) = y_i\\}| \\in \\{1, 2, 3\\}$.\nConf${=}1$ arises when a single non-abstaining LF determines the label---either because only one LF votes or because two LFs disagree with no clear majority---producing the most ambiguous labels.\nThe conf${\\geq}$2 subset, where at least two non-abstaining LFs agree on the winning label, serves as the primary evaluation set throughout this work.\nThis stratification allows us to separately analyze model behavior on high-confidence vs.\\ ambiguous windows (\\S\\ref{sec:main_results}).\n\n%-------------------------------------------------------------------\n\\subsection{Detection Methods}\n\\label{sec:detection_methods}\n\n\\subsubsection{Structural Features}\n\\label{sec:structural_features}\n\nWe extract a 30-dimensional feature vector from each window, requiring no pretrained model or GPU.\nFeatures span four categories:\n(1)~\\emph{repetition}: exact command repeat ratio, fuzzy match ratio (Levenshtein-based), and unique command ratio;\n(2)~\\emph{file operations}: counts of file creates, modifications, and deletions within the window;\n(3)~\\emph{edit patterns}: edit distances between consecutive actions, capturing how much the agent's behavior changes step-to-step;\n(4)~\\emph{output statistics}: entropy of command outputs and action type distribution features.\nThese features are fed to three classifiers: Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\nBecause several structural features overlap with the signals used by the labeling functions (e.g., repetition ratios relate to $\\lambda_1$), structural classifiers can partially reconstruct the LF voting process.\nWe discuss this circularity and its implications in \\S\\ref{sec:main_results}.\n\n\\subsubsection{NL Embedding Probe (ProgressProbe)}\n\\label{sec:progressprobe}\n\nEach action $a_t$ is encoded as a natural language description and embedded using Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} into a 1024-dimensional vector.\nThe $k$ embeddings within a window form a sequence that is processed by a 2-layer GRU \\citep{cho2014gru} with hidden size 256 and dropout 0.1.\nAn attention mechanism \\citep{bahdanau2015attention} computes a weighted combination of the GRU hidden states, yielding a single window-level representation.\nThis representation is passed through a fully connected layer with sigmoid activation for binary classification.\nTraining uses binary cross-entropy loss with early stopping (patience 5) on a validation set.\n\nThe GRU architecture is motivated by the sequential nature of actions within a window: the order in which commands are issued (e.g., repeated failures followed by a different approach) carries diagnostic information that bag-of-embeddings methods discard.\nWe also evaluate two simpler embedding baselines to isolate the contribution of temporal modeling: (1)~mean-pooled Qwen3 embeddings with logistic regression, and (2)~cosine similarity between consecutive window embeddings with a validation-tuned threshold.\n\n\\subsubsection{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\nWe prompt Claude Sonnet 4.6 in zero-shot mode to classify each window as stagnation or progress, given the textual descriptions of actions within the window.\\footnote{Extended LLM evaluation including chain-of-thought prompting, few-shot examples, and multi-model comparison is reported in Appendix~\\ref{sec:llm_extended}.}\nThe LLM judge establishes a cost-performance reference: at \\$11.66 per test set, its zero-shot F1 of 0.663 demonstrates that stagnation detection is non-trivial even for capable LLMs without task-specific adaptation.\nThis baseline is not used in the silver label pipeline.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_models}\n\nThe three LFs occupy distinct temporal niches relative to stagnation onset (\\S\\ref{sec:lf_temporal}): $\\lambda_1$ leads by ${\\sim}2$ steps, $\\lambda_2$ is near-concurrent, and $\\lambda_3$ lags by ${\\sim}7$ steps.\nThis motivates exploring whether encoding temporal structure into label aggregation can improve over majority vote.\n\n\\subsubsection{Time-Varying Weights (TWV)}\n\\label{sec:twv}\n\nTWV applies Gaussian kernel smoothing to each LF's activation sequence:\n\\begin{equation}\n\\tilde{\\lambda}_j(t) = \\sum_{t'} K_\\sigma(t - t') \\cdot \\lambda_j(t')\n\\label{eq:twv}\n\\end{equation}\nwhere $K_\\sigma$ is a Gaussian kernel with bandwidth $\\sigma$.\nSmoothed activations replace raw votes for conf${=}1$ windows (where exactly one LF disagrees), potentially flipping labels in temporally ambiguous regions.\nThe bandwidth $\\sigma$ controls the extent of temporal context: larger values incorporate more distant steps.\n\n\\subsubsection{Hidden Markov Models}\n\\label{sec:hmm}\n\nWe model the label sequence as a Hidden Markov Model \\citep{safranchik2020linkedhmm} with two hidden states (stagnation, progress) and observations defined by the joint activation pattern of the three LFs.\nTransition and emission parameters are estimated via Expectation-Maximization (EM).\nThe HMM captures temporal persistence---stagnation episodes tend to span multiple consecutive windows---which majority vote, operating independently per window, cannot model.\n\n\\subsubsection{Lag-Aware HMM}\n\\label{sec:lag_hmm}\n\nThe standard HMM treats all LFs as synchronous.\nLag-Aware HMM extends this by explicitly modeling each LF's temporal offset: $\\lambda_1$ is shifted by $-2$ steps, $\\lambda_2$ by $-1$, and $\\lambda_3$ by $+7$, estimated from the temporal dynamics analysis (\\S\\ref{sec:lf_temporal}).\nTo prevent divergence, we apply two regularization strategies: (1)~\\emph{confidence anchoring}, which fixes labels for conf${\\geq}$2 windows and restricts EM updates to conf${=}1$ windows; and (2)~a prior strength of 5000 on transition parameters.\nThese constraints keep the model close to the majority vote baseline while allowing it to resolve temporally ambiguous labels.\nThe intuition is that aligning each LF's activation to its natural temporal role should produce cleaner emission estimates and, consequently, more accurate Viterbi decodings on ambiguous windows.",
      "numLines": 157,
      "startLine": 1,
      "totalLines": 157
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01VszC4xZbgkiHPEJfDEtktc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "f9ce73c7-24aa-4812-8e98-0a7362021ade",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 22 · 2026-05-15T05:22:40.353Z_

<details><summary>↩ Tool result · `toolu_01VszC4xZbgkiHPEJfDEtktc`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We organize results around three questions:
5	(1)~which method best detects stagnation across deployment scenarios? (\S\ref{sec:main_results}--\S\ref{sec:robustness});
6	(2)~what drives label quality and cross-coding-agent transfer bottlenecks? (\S\ref{sec:lf_temporal}--\S\ref{sec:cmd_rep_ablation});
7	(3)~can temporal structure in LFs improve labels? (\S\ref{sec:temporal_label_models}).
8	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
9	
10	\paragraph{Circular evaluation caveat.}
11	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
12	Consequently, the in-domain structural F1 of 0.995 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
13	The cross-coding-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
14	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
15	
16	%-------------------------------------------------------------------
17	\subsection{Experimental Setup}
18	\label{sec:setup}
19	
20	\paragraph{Datasets.}
21	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
22	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
23	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 20.9\%.
24	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
25	Train/validation/test splits are constructed at the trajectory level (by SWE-bench instance ID, 70/15/15\%), ensuring no windows from the same task appear across splits.
26	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
27	
28	\begin{table}[t]
29	\centering
30	\small
31	\begin{tabular}{llrrc}
32	\toprule
33	\textbf{Agent} & \textbf{Source} & \textbf{Windows} & \textbf{Stag\,\%} & \textbf{Conf${\geq}$2} \\
34	\midrule
35	SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\
36	OpenHands & CodeAct   & 150,652 & 20.9 & 43,376 \\
37	\bottomrule
38	\end{tabular}
39	\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}
40	\label{tab:dataset_stats}
41	\end{table}
42	
43	\paragraph{Detection methods.}
44	(1)~\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
45	(2)~\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.
46	(3)~\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.
47	(4)~\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\$11.66 API cost for the SWE test set).
48	(5)~\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.
49	
50	\paragraph{Metrics.}
51	Macro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\textsubscript{stag}) and progress (F1\textsubscript{prog}).
52	
53	%-------------------------------------------------------------------
54	\subsection{Main Results}
55	\label{sec:main_results}
56	
57	Table~\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\geq}$2 test set and cross-coding-agent transfer to OpenHands.
58	
59	\begin{table*}[t]
60	\centering
61	\small
62	\begin{tabular}{l ccc cc}
63	\toprule
64	& \multicolumn{3}{c}{\textbf{SWE-Agent In-Domain} (conf${\geq}$2)} & \multicolumn{2}{c}{\textbf{OpenHands Transfer}} \\
65	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
66	\textbf{Method} & Macro-F1 & F1\textsubscript{stag} & F1\textsubscript{prog} & All & Conf${\geq}$2 \\
67	\midrule
68	Structural RF$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \textbf{0.9959} \\
69	Structural GB$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & \textbf{0.9674} & \underline{0.9918} \\
70	Structural LR$^\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\
71	ProgressProbe (GRU)           & \underline{0.9055} & 0.8593 & 0.9518 & 0.598$^a$ & 0.598$^a$ \\
72	\quad + full OH fine-tune      & ---    & ---    & ---    & 0.976$^b$ & 0.976$^b$ \\
73	Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\
74	LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\
75	Cosine Similarity             & 0.5606 & ---    & ---    & 0.447  & 0.393 \\
76	\bottomrule
77	\end{tabular}
78	\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-coding-agent transfer to OpenHands. $^\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). $^a$Probe zero-shot transfer is evaluated on the standard 15\% test split ($N{=}6{,}122$); structural models are evaluated on all OH windows ($N{=}150{,}652$) and the conf${\geq}$2 subset ($N{=}43{,}376$). The structural conf${\geq}$2 numbers provide the most comparable evaluation scope. Probe macro-F1 is identical on all-windows and conf${\geq}$2 subsets (0.598 to three decimal places). For reference, probe zero-shot on the full conf${\geq}$2 set (all 43,376 windows, not just the test split) yields 0.581 macro-F1, consistent with the test-split estimate. $^b$Paired bootstrap on conf${\geq}$2 test split ($N{=}6{,}122$): GB leads fine-tuned probe by 1.65\,pp (95\% CI [1.11, 2.23], $p{<}0.001$); the probe's all-windows advantage (0.976 vs.\ 0.967) reflects stronger performance on conf${=}1$ data. Best in \textbf{bold}, second-best \underline{underlined}.}
79	\label{tab:main_results}
80	\end{table*}
81	
82	In-domain, structural RF achieves 0.995 macro-F1, exceeding the GRU probe by 8.96\,pp (paired bootstrap: 95\% CI [7.44, 10.57]\,pp, $p{<}0.001$).
83	However, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.
84	The more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.
85	The zero-shot LLM judge (0.663) underperforms all learned methods despite substantially higher cost (\$11.66 per test set).
86	Extended evaluation with chain-of-thought and few-shot prompting (Appendix~\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.799 (five-shot-CoT, SWE-Agent in-domain), still 16.8\,pp below structural cross-coding-agent transfer (0.967 on OpenHands)---the structural advantage holds even comparing the harder cross-coding-agent setting against the LLM's easier in-domain regime.
87	CoT alone yields gains comparable to few-shot ($+$8.7\,pp vs.\ $+$8.9\,pp over zero-shot); combining them (five-shot-CoT) adds a further $+$4.8\,pp, suggesting complementary mechanisms.
88	Notably, providing the 30 structural features as additional LLM input degrades performance from 0.751 (few-shot) to 0.688, suggesting the signal resides in engineered feature interactions inaccessible to natural language reasoning (Appendix~\ref{sec:llm_extended}).
89	
90	%-------------------------------------------------------------------
91	\subsection{Cross-Agent Transfer}
92	\label{sec:cross_agent}
93	
94	Table~\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.
95	Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows.
96	RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.
97	Both structural models exceed 0.99 macro-F1 on conf${\geq}$2 OH windows (GB 0.992, RF 0.996), where label noise is lower.
98	
99	The probe's zero-shot transfer (0.598) lags structural GB by 36.9\,pp---cosine similarity collapses further to 0.447 (mean cosine distance between stagnation and progress windows is 0.610 vs.\ 0.613, showing essentially no class separation)---but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.976 macro-F1 on all OH windows, surpassing structural GB (0.967) by 0.9\,pp (\S\ref{sec:cmd_rep_ablation}).
100	The asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\,pp gap); with target-domain fine-tuning, the probe surpasses structural features (+0.9\,pp on all windows).
101	The practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.
102	However, this crossover is scope-dependent: on conf${\geq}$2 windows, where label noise is minimal, GB retains its advantage (0.993 vs.\ 0.976; paired bootstrap $p{<}0.001$, $N{=}6{,}122$), suggesting that the probe's all-windows edge reflects better tolerance of noisy low-confidence labels rather than superior high-confidence detection.
103	
104	Paired bootstrap on the matched conf${\geq}$2 test split ($N{=}6{,}122$, 10K resamples) confirms both gaps as significant.
105	The zero-shot probe lags GB by 39.4\,pp on this subset (95\% CI [37.9, 41.0], $p{<}0.001$).
106	The fine-tuned probe narrows the gap but does not close it on conf${\geq}$2: GB retains a 1.65\,pp edge (95\% CI [1.11, 2.23], $p{<}0.001$; GB 0.993, probe 0.976), whereas the probe's advantage on all windows (0.976 vs.\ 0.967) reflects stronger performance on noisier conf${=}1$ labels.
107	
108	\paragraph{Multi-seed stability.}
109	Structural RF: $0.995{\pm}0.000$ in-domain (3 seeds, zero variance); GB cross-coding-agent: $0.968{\pm}0.002$.
110	The probe shows higher variance: $0.919{\pm}0.011$, though all seeds exceed 0.90.
111	
112	%-------------------------------------------------------------------
113	\subsection{Robustness Analysis}
114	\label{sec:robustness}
115	
116	\paragraph{Encoder ablation.}
117	Replacing Qwen3-0.6B with BGE-M3 \citep{chen2024bgem3} or E5-large-v2 \citep{wang2024e5} yields probe macro-F1 of 0.941 and 0.936, respectively (vs.\ 0.906 for Qwen3).
118	All encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\ref{tab:encoder_ablation}.
119	We use Qwen3-Embedding-0.6B (released May 2025) as our primary encoder for recency; BGE-M3 achieves higher F1 (0.941 vs.\ 0.906), confirming encoder-agnostic findings.
120	
121	\paragraph{Architecture ablation.}
122	Replacing the GRU with a Transformer encoder (2-layer, 4-head, same hidden dimension) yields 0.934 macro-F1 vs.\ 0.933 for GRU ($+$0.18\,pp, not significant under paired bootstrap $p{=}0.82$).
123	The two architectures are functionally equivalent on 5-step windows, suggesting that the sequential inductive bias of the GRU provides no advantage at this window length.
124	
125	\paragraph{Window size.}
126	$k{=}5$ is optimal (0.931 macro-F1); $k{=}3$ drops 5.9\,pp and $k{=}7$ drops 1.8\,pp.
127	Shorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.
128	The 0.931 figure differs from the main table's 0.906 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.
129	Details in Appendix Table~\ref{tab:window_ablation}.
130	
131	\paragraph{Data scaling.}
132	Figure~\ref{fig:data_scaling} compares data efficiency across methods.
133	Structural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\% training data, fully saturating by 50\%.
134	The probe scales monotonically from 0.805 (10\%) to 0.906 (100\%) but has not plateaued---a 10.1\,pp drop that is roughly 20$\times$ the structural degradation (${\sim}$0.4--0.8\,pp).
135	This data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.
136	
137	\begin{figure}[t]
138	\centering
139	\includegraphics[width=\columnwidth]{../../figures/paper/fig_data_scaling.pdf}
140	\caption{Macro-F1 vs.\ training data fraction. Structural classifiers (RF, GB) saturate by 50\% data; the probe scales monotonically but remains 9\,pp below at 100\%.}
141	\label{fig:data_scaling}
142	\end{figure}
143	
144	%-------------------------------------------------------------------
145	\subsection{Labeling Function Temporal Dynamics}
146	\label{sec:lf_temporal}
147	
148	We analyze when each LF first fires relative to the onset of stagnation episodes (Table~\ref{tab:lf_temporal}, Figure~\ref{fig:lf_temporal}).
149	
150	\begin{table}[t]
151	\centering
152	\small
153	\begin{tabular}{lrrrr}
154	\toprule
155	\textbf{LF} & \textbf{Lag} & \textbf{Lead\,\%} & \textbf{Conc.\,\%} & \textbf{Lag\,\%} \\
156	\midrule
157	cmd\_rep      & $-1.87$ & 36.1 & --- & --- \\
158	file\_diff    & $-1.20$ & 17.1 & --- & --- \\
159	outcome\_bp   & $+6.70$ & ---  & --- & 48.4 \\
160	\bottomrule
161	\end{tabular}
162	\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}
163	\label{tab:lf_temporal}
164	\end{table}
165	
166	The three LFs occupy distinct temporal niches.
167	Command repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.
168	File diff is near-concurrent ($-1.20$ steps).
169	Outcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.
170	
171	All pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\_rep vs.\ file\_diff $p{=}1.44{\times}10^{-26}$, cmd\_rep vs.\ outcome\_bp $p{=}6.67{\times}10^{-39}$, file\_diff vs.\ outcome\_bp $p{=}3.47{\times}10^{-47}$).
172	
173	\paragraph{Cross-agent reversal.}
174	On OpenHands, cmd\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).
175	Under corrected OH labels (\S\ref{sec:cmd_rep_ablation}), cmd\_rep fires on only 5.4\% of OH windows with 97.9\% precision---a high-precision, low-recall detector whose temporal role differs fundamentally from its SWE-Agent behavior.
176	
177	\begin{figure}[t]
178	\centering
179	\includegraphics[width=\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}
180	\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\_rep leads ($-1.87$ steps), file\_diff is near-concurrent ($-1.20$), outcome\_bp lags ($+6.70$). Inset: OH reversal where cmd\_rep becomes lagging.}
181	\label{fig:lf_temporal}
182	\end{figure}
183	
184	%-------------------------------------------------------------------
185	\subsection{Label Quality and cmd\_rep Coverage}
186	\label{sec:cmd_rep_ablation}
187	
188	A label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.
189	After correction, the OH stagnation rate on the embedding subset (143,057 windows; short trajectories excluded) shifted from 6.56\% to 21.4\%, with 21,898 window labels flipping.
190	This section quantifies how label quality and cmd\_rep coverage jointly affect probe transfer.
191	
192	\paragraph{Label correction impact on probe transfer.}
193	With corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).
194	The improvement is most dramatic at low data fractions: 5\% fine-tuning reaches 0.850, exceeding the old 50\% result (0.69) by 16.0\,pp.
195	The probe converges rapidly: at 50\% OH data it reaches 0.968, essentially matching structural GB (0.967) and demonstrating that the structural advantage is specific to zero-data deployment (full curve in Appendix Table~\ref{tab:cross_agent_cmdrep}).
196	Label quality, not model capacity, was the transfer bottleneck.
197	
198	\paragraph{Prevalence-matched ablation.}
199	To isolate cmd\_rep's contribution, we compare 3-LF and 2-LF (no cmd\_rep) models on the same test set with matched class prevalence.
200	
201	\begin{table}[t]
202	\centering
203	\small
204	\begin{tabular}{lccc}
205	\toprule
206	\textbf{LF Config} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} \\
207	\midrule
208	3-LF (w/ cmd\_rep) & \textbf{0.9763} & 0.9600 & 0.9930 \\
209	2-LF (no cmd\_rep) & 0.6822 & 0.4810 & 0.8840 \\
210	\midrule
211	$\Delta$ & $-29.4$\,pp & $-47.9$\,pp & $-10.9$\,pp \\
212	\bottomrule
213	\end{tabular}
214	\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\%). Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$).}
215	\label{tab:cmd_rep_ablation}
216	\end{table}
217	
218	Removing cmd\_rep drops macro-F1 by 29.4\,pp (McNemar $\chi^2{=}1551$, $p{\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\,pp F1\textsubscript{stag}).
219	
220	\paragraph{Coverage, not label quality, explains the gap.}
221	The 29.4\,pp drop is not caused by cmd\_rep improving label accuracy.
222	After correction, cmd\_rep fires on only 5.39\% of OH windows (down from the previously reported 92.2\% under corrupted embeddings) with 97.91\% precision---a high-precision, low-recall signal.
223	On the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\% of labels: cmd\_rep does not change any label where the other two LFs already vote.
224	Its contribution is purely \emph{coverage}: including cmd\_rep expands the training set from ${\sim}$4K to ${\sim}$43K windows (a ${\sim}$10$\times$ increase).
225	The 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.
226	
227	\paragraph{Implications for weak supervision.}
228	These results reframe how labeling functions contribute to weak supervision pipelines.
229	A high-precision, low-recall LF like cmd\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.
230	In prevalence-matched evaluation, this data reduction manifests as a 29.4\,pp F1 drop.
231	The core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.
232	
233	%-------------------------------------------------------------------
234	\subsection{Temporal Label Models}
235	\label{sec:temporal_label_models}
236	
237	We investigate whether any label aggregation method---temporal or generative---improves over majority vote (MV).
238	Table~\ref{tab:temporal_models} compares five label models: three temporal (TWV, Lag-HMM, HMM) \citep{ratner2017snorkel,safranchik2020linkedhmm} and two generative i.i.d.\ models (FlyingSquid \citep{fu2020flyingsquid}, Snorkel MeTaL \citep{ratner2019snorkelmetal}).
239	
240	\begin{table}[t]
241	\centering
242	\small
243	\begin{tabular}{lcccc}
244	\toprule
245	\textbf{Method} & \textbf{MV Agr.} & \textbf{Conf${\geq}$2 F1} & \textbf{$\Delta$ vs MV} & \textbf{Probe F1$^\ddagger$} \\
246	\midrule
247	MV (baseline) & 1.000 & 0.8946$^\ast$ & --- & 0.8468 \\
248	\midrule
249	\multicolumn{5}{l}{\emph{Temporal}} \\
250	TWV ($\sigma{=}2$) & 0.885 & \textbf{0.9003} & $+$0.6\,pp & 0.8211 \\
251	Lag-HMM & 0.820 & 0.8936 & $-$0.1\,pp & --- \\
252	HMM & 0.685 & 0.7502 & $-$14.4\,pp & 0.6564 \\
253	\midrule
254	\multicolumn{5}{l}{\emph{Generative (i.i.d.)}} \\
255	FlyingSquid & 0.820 & 0.7820 & $-$11.3\,pp & --- \\
256	Snorkel MeTaL & 0.423 & 0.2580 & $-$63.6\,pp & --- \\
257	\bottomrule
258	\end{tabular}
259	\caption{Label model comparison. Conf${\geq}$2 F1: each model's labels evaluated against MV labels on conf${\geq}$2 windows. $^\ast$MV conf${\geq}$2 F1 (0.8946) reflects downstream probe performance when trained on MV labels, not self-agreement (which would be 1.0). $^\ddagger$Downstream probe trained on each method's full labels, evaluated on the SWE-Agent test set ($N{=}8{,}101$) against MV labels. ``---'' = not evaluated downstream. No model consistently improves over MV.}
260	\label{tab:temporal_models}
261	\end{table}
262	
263	\paragraph{Temporal models.}
264	TWV achieves the highest conf${\geq}$2 F1 (0.900, $+$0.6\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.821 vs.\ 0.847 for MV-trained ($-$2.57\,pp).
265	TWV flips 14.1\% of conf${=}$1 labels, introducing noise that hurts probe training.
266	The Gaussian kernel bandwidth $\sigma$ is critical: $\sigma{=}2$ is optimal; $\sigma{=}1$ drops to 0.811 and $\sigma{=}5$ to 0.808, making TWV impractical as a drop-in MV replacement.
267	HMM overpredicts stagnation (29,176 vs.\ 25,633 progress windows), degrading conf${\geq}$2 F1 by 14.4\,pp and downstream performance to 0.656.
268	Lag-HMM closely tracks MV ($-$0.1\,pp) despite explicitly modeling temporal offsets.
269	
270	\paragraph{Generative (i.i.d.) models.}
271	FlyingSquid \citep{fu2020flyingsquid}, a closed-form triplet-based model, drops 11.3\,pp below MV.
272	On the full dataset, agreement with MV is 82\%; all divergent labels flip progress$\to$stagnation, introducing systematic stagnation bias.
273	Snorkel MeTaL \citep{ratner2019snorkelmetal} fails catastrophically ($-$63.6\,pp), with only 42.3\% MV agreement.
274	Both models assume conditional independence among LFs---an assumption violated by the shared behavioral signals underlying our three LFs---and lack the sequential structure to recover from this misspecification.
275	
276	\paragraph{Root cause: insufficient inter-LF conflict.}
277	These results constitute a negative finding: five label models spanning temporal aggregation and generative modeling all fail to improve over majority vote.
278	Three binary LFs produce at most $2^3{=}8$ voting patterns; conf${\geq}$2 windows dominate the training set, leaving insufficient ambiguity for any aggregation method to exploit.
279	The bottleneck is LF quantity, not aggregation sophistication---scaling to ${>}$10 LFs with higher disagreement rates is needed before advanced label models can add value.
280	In the current 3-LF, low-conflict regime (conf${\geq}$2 agreement rate 95.1\%), temporal alignment gains are offset by noise introduction.
281	With 5--10 LFs generating higher disagreement rates, temporal models may add value---this remains an open question.
282	
283	%-------------------------------------------------------------------
284	\subsection{Gold Set Validation}
285	\label{sec:gold_set}
286	We construct a stratified gold set of 650 windows for non-circular evaluation.
287	Windows are sampled along two axes: \emph{confidence} (balanced across conf${=}1$, conf${=}2$, and conf${=}3$ strata to capture the full ambiguity spectrum) and \emph{trajectory position} (early, middle, and late thirds, since stagnation dynamics differ across trajectory phases; \S\ref{sec:error_analysis}).
288	
289	\paragraph{Annotation protocol.}
290	Two annotators independently label each window as stagnation or progress using an operational definition: \emph{a window is stagnation if the agent's actions within it do not make meaningful progress toward solving the task, regardless of whether the actions appear diverse or purposeful}.
291	Annotators receive the $k{=}5$ action descriptions with full command outputs and file diffs, but \emph{not} the task outcome (resolved/unresolved), preventing information leakage from $\lambda_3$.
292	Disagreements are resolved by a third annotator.
293	Gold validation results are pending; in the interim, cross-coding-agent transfer (\S\ref{sec:cross_agent}) and the feature overlap ablation (\S\ref{sec:feature_overlap}) provide non-circular evidence that structural features encode genuine stagnation signals rather than LF artifacts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "a30a7420-4c7a-44f2-91c0-07b30f70d34e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe organize results around three questions:\n(1)~which method best detects stagnation across deployment scenarios? (\\S\\ref{sec:main_results}--\\S\\ref{sec:robustness});\n(2)~what drives label quality and cross-coding-agent transfer bottlenecks? (\\S\\ref{sec:lf_temporal}--\\S\\ref{sec:cmd_rep_ablation});\n(3)~can temporal structure in LFs improve labels? (\\S\\ref{sec:temporal_label_models}).\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.995 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-coding-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 20.9\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nTrain/validation/test splits are constructed at the trajectory level (by SWE-bench instance ID, 70/15/15\\%), ensuring no windows from the same task appear across splits.\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 20.9 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet 4.6 zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-coding-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9918} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.598$^a$ & 0.598$^a$ \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.976$^b$ & 0.976$^b$ \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & 0.447  & 0.393 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-coding-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). $^a$Probe zero-shot transfer is evaluated on the standard 15\\% test split ($N{=}6{,}122$); structural models are evaluated on all OH windows ($N{=}150{,}652$) and the conf${\\geq}$2 subset ($N{=}43{,}376$). The structural conf${\\geq}$2 numbers provide the most comparable evaluation scope. Probe macro-F1 is identical on all-windows and conf${\\geq}$2 subsets (0.598 to three decimal places). For reference, probe zero-shot on the full conf${\\geq}$2 set (all 43,376 windows, not just the test split) yields 0.581 macro-F1, consistent with the test-split estimate. $^b$Paired bootstrap on conf${\\geq}$2 test split ($N{=}6{,}122$): GB leads fine-tuned probe by 1.65\\,pp (95\\% CI [1.11, 2.23], $p{<}0.001$); the probe's all-windows advantage (0.976 vs.\\ 0.967) reflects stronger performance on conf${=}1$ data. Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.995 macro-F1, exceeding the GRU probe by 8.96\\,pp (paired bootstrap: 95\\% CI [7.44, 10.57]\\,pp, $p{<}0.001$).\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe zero-shot LLM judge (0.663) underperforms all learned methods despite substantially higher cost (\\$11.66 per test set).\nExtended evaluation with chain-of-thought and few-shot prompting (Appendix~\\ref{sec:llm_extended}) yields a best LLM macro-F1 of 0.799 (five-shot-CoT, SWE-Agent in-domain), still 16.8\\,pp below structural cross-coding-agent transfer (0.967 on OpenHands)---the structural advantage holds even comparing the harder cross-coding-agent setting against the LLM's easier in-domain regime.\nCoT alone yields gains comparable to few-shot ($+$8.7\\,pp vs.\\ $+$8.9\\,pp over zero-shot); combining them (five-shot-CoT) adds a further $+$4.8\\,pp, suggesting complementary mechanisms.\nNotably, providing the 30 structural features as additional LLM input degrades performance from 0.751 (few-shot) to 0.688, suggesting the signal resides in engineered feature interactions inaccessible to natural language reasoning (Appendix~\\ref{sec:llm_extended}).\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows.\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models exceed 0.99 macro-F1 on conf${\\geq}$2 OH windows (GB 0.992, RF 0.996), where label noise is lower.\n\nThe probe's zero-shot transfer (0.598) lags structural GB by 36.9\\,pp---cosine similarity collapses further to 0.447 (mean cosine distance between stagnation and progress windows is 0.610 vs.\\ 0.613, showing essentially no class separation)---but full OH fine-tuning closes this gap dramatically: the fine-tuned probe reaches 0.976 macro-F1 on all OH windows, surpassing structural GB (0.967) by 0.9\\,pp (\\S\\ref{sec:cmd_rep_ablation}).\nThe asymmetry between structural and learned methods is thus stage-dependent: in the zero-data regime, structural features transfer naturally while learned embeddings do not (+36.9\\,pp gap); with target-domain fine-tuning, the probe surpasses structural features (+0.9\\,pp on all windows).\nThe practical implication is a deployment trade-off: use structural features when no labeled data is available; invest in probe fine-tuning when annotation budget permits.\nHowever, this crossover is scope-dependent: on conf${\\geq}$2 windows, where label noise is minimal, GB retains its advantage (0.993 vs.\\ 0.976; paired bootstrap $p{<}0.001$, $N{=}6{,}122$), suggesting that the probe's all-windows edge reflects better tolerance of noisy low-confidence labels rather than superior high-confidence detection.\n\nPaired bootstrap on the matched conf${\\geq}$2 test split ($N{=}6{,}122$, 10K resamples) confirms both gaps as significant.\nThe zero-shot probe lags GB by 39.4\\,pp on this subset (95\\% CI [37.9, 41.0], $p{<}0.001$).\nThe fine-tuned probe narrows the gap but does not close it on conf${\\geq}$2: GB retains a 1.65\\,pp edge (95\\% CI [1.11, 2.23], $p{<}0.001$; GB 0.993, probe 0.976), whereas the probe's advantage on all windows (0.976 vs.\\ 0.967) reflects stronger performance on noisier conf${=}1$ labels.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.995{\\pm}0.000$ in-domain (3 seeds, zero variance); GB cross-coding-agent: $0.968{\\pm}0.002$.\nThe probe shows higher variance: $0.919{\\pm}0.011$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.941 and 0.936, respectively (vs.\\ 0.906 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\nWe use Qwen3-Embedding-0.6B (released May 2025) as our primary encoder for recency; BGE-M3 achieves higher F1 (0.941 vs.\\ 0.906), confirming encoder-agnostic findings.\n\n\\paragraph{Architecture ablation.}\nReplacing the GRU with a Transformer encoder (2-layer, 4-head, same hidden dimension) yields 0.934 macro-F1 vs.\\ 0.933 for GRU ($+$0.18\\,pp, not significant under paired bootstrap $p{=}0.82$).\nThe two architectures are functionally equivalent on 5-step windows, suggesting that the sequential inductive bias of the GRU provides no advantage at this window length.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.931 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nThe 0.931 figure differs from the main table's 0.906 because the window ablation uses a separate train/val/test split (seed~42, Qwen3-0.6B encoder) to enable controlled comparison across window sizes; cross-split variance accounts for the gap.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} compares data efficiency across methods.\nStructural classifiers are extremely data-efficient: RF achieves 0.991 and GB 0.987 at just 10\\% training data, fully saturating by 50\\%.\nThe probe scales monotonically from 0.805 (10\\%) to 0.906 (100\\%) but has not plateaued---a 10.1\\,pp drop that is roughly 20$\\times$ the structural degradation (${\\sim}$0.4--0.8\\,pp).\nThis data efficiency further supports the structural signal thesis: the features capture patterns so regular that minimal training data suffices.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Macro-F1 vs.\\ training data fraction. Structural classifiers (RF, GB) saturate by 50\\% data; the probe scales monotonically but remains 9\\,pp below at 100\\%.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nUnder corrected OH labels (\\S\\ref{sec:cmd_rep_ablation}), cmd\\_rep fires on only 5.4\\% of OH windows with 97.9\\% precision---a high-precision, low-recall detector whose temporal role differs fundamentally from its SWE-Agent behavior.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Label Quality and cmd\\_rep Coverage}\n\\label{sec:cmd_rep_ablation}\n\nA label quality audit revealed that the OH embedding vectors used for silver labeling contained a version mismatch, causing systematic label errors.\nAfter correction, the OH stagnation rate on the embedding subset (143,057 windows; short trajectories excluded) shifted from 6.56\\% to 21.4\\%, with 21,898 window labels flipping.\nThis section quantifies how label quality and cmd\\_rep coverage jointly affect probe transfer.\n\n\\paragraph{Label correction impact on probe transfer.}\nWith corrected labels, the 3-LF probe improves from zero-shot 0.598 to fine-tuned 0.976 (previously 0.7512 under corrupted labels).\nThe improvement is most dramatic at low data fractions: 5\\% fine-tuning reaches 0.850, exceeding the old 50\\% result (0.69) by 16.0\\,pp.\nThe probe converges rapidly: at 50\\% OH data it reaches 0.968, essentially matching structural GB (0.967) and demonstrating that the structural advantage is specific to zero-data deployment (full curve in Appendix Table~\\ref{tab:cross_agent_cmdrep}).\nLabel quality, not model capacity, was the transfer bottleneck.\n\n\\paragraph{Prevalence-matched ablation.}\nTo isolate cmd\\_rep's contribution, we compare 3-LF and 2-LF (no cmd\\_rep) models on the same test set with matched class prevalence.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & \\textbf{0.9763} & 0.9600 & 0.9930 \\\\\n2-LF (no cmd\\_rep) & 0.6822 & 0.4810 & 0.8840 \\\\\n\\midrule\n$\\Delta$ & $-29.4$\\,pp & $-47.9$\\,pp & $-10.9$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Prevalence-matched ablation on the same OH test set ($N{=}6{,}122$, stag rate 19.3\\%). Removing cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$).}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep drops macro-F1 by 29.4\\,pp (McNemar $\\chi^2{=}1551$, $p{\\approx}0$), a statistically significant degradation driven primarily by stagnation recall ($-47.9$\\,pp F1\\textsubscript{stag}).\n\n\\paragraph{Coverage, not label quality, explains the gap.}\nThe 29.4\\,pp drop is not caused by cmd\\_rep improving label accuracy.\nAfter correction, cmd\\_rep fires on only 5.39\\% of OH windows (down from the previously reported 92.2\\% under corrupted embeddings) with 97.91\\% precision---a high-precision, low-recall signal.\nOn the 4,070 windows where both 2-LF and 3-LF labels are defined, the two configurations agree on 100\\% of labels: cmd\\_rep does not change any label where the other two LFs already vote.\nIts contribution is purely \\emph{coverage}: including cmd\\_rep expands the training set from ${\\sim}$4K to ${\\sim}$43K windows (a ${\\sim}$10$\\times$ increase).\nThe 2-LF model's low F1 reflects data volume collapse---too few training examples to learn the stagnation distribution---rather than label corruption.\n\n\\paragraph{Implications for weak supervision.}\nThese results reframe how labeling functions contribute to weak supervision pipelines.\nA high-precision, low-recall LF like cmd\\_rep may appear redundant when its labels are a subset of the majority vote, yet removing it causes training data to collapse by an order of magnitude.\nIn prevalence-matched evaluation, this data reduction manifests as a 29.4\\,pp F1 drop.\nThe core contribution of such LFs is coverage provision, not label refinement: they extend the labelable portion of the input space rather than correcting other LFs' errors.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether any label aggregation method---temporal or generative---improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares five label models: three temporal (TWV, Lag-HMM, HMM) \\citep{ratner2017snorkel,safranchik2020linkedhmm} and two generative i.i.d.\\ models (FlyingSquid \\citep{fu2020flyingsquid}, Snorkel MeTaL \\citep{ratner2019snorkelmetal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{MV Agr.} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{$\\Delta$ vs MV} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 1.000 & 0.8946$^\\ast$ & --- & 0.8468 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Temporal}} \\\\\nTWV ($\\sigma{=}2$) & 0.885 & \\textbf{0.9003} & $+$0.6\\,pp & 0.8211 \\\\\nLag-HMM & 0.820 & 0.8936 & $-$0.1\\,pp & --- \\\\\nHMM & 0.685 & 0.7502 & $-$14.4\\,pp & 0.6564 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\emph{Generative (i.i.d.)}} \\\\\nFlyingSquid & 0.820 & 0.7820 & $-$11.3\\,pp & --- \\\\\nSnorkel MeTaL & 0.423 & 0.2580 & $-$63.6\\,pp & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Label model comparison. Conf${\\geq}$2 F1: each model's labels evaluated against MV labels on conf${\\geq}$2 windows. $^\\ast$MV conf${\\geq}$2 F1 (0.8946) reflects downstream probe performance when trained on MV labels, not self-agreement (which would be 1.0). $^\\ddagger$Downstream probe trained on each method's full labels, evaluated on the SWE-Agent test set ($N{=}8{,}101$) against MV labels. ``---'' = not evaluated downstream. No model consistently improves over MV.}\n\\label{tab:temporal_models}\n\\end{table}\n\n\\paragraph{Temporal models.}\nTWV achieves the highest conf${\\geq}$2 F1 (0.900, $+$0.6\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.821 vs.\\ 0.847 for MV-trained ($-$2.57\\,pp).\nTWV flips 14.1\\% of conf${=}$1 labels, introducing noise that hurts probe training.\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal; $\\sigma{=}1$ drops to 0.811 and $\\sigma{=}5$ to 0.808, making TWV impractical as a drop-in MV replacement.\nHMM overpredicts stagnation (29,176 vs.\\ 25,633 progress windows), degrading conf${\\geq}$2 F1 by 14.4\\,pp and downstream performance to 0.656.\nLag-HMM closely tracks MV ($-$0.1\\,pp) despite explicitly modeling temporal offsets.\n\n\\paragraph{Generative (i.i.d.) models.}\nFlyingSquid \\citep{fu2020flyingsquid}, a closed-form triplet-based model, drops 11.3\\,pp below MV.\nOn the full dataset, agreement with MV is 82\\%; all divergent labels flip progress$\\to$stagnation, introducing systematic stagnation bias.\nSnorkel MeTaL \\citep{ratner2019snorkelmetal} fails catastrophically ($-$63.6\\,pp), with only 42.3\\% MV agreement.\nBoth models assume conditional independence among LFs---an assumption violated by the shared behavioral signals underlying our three LFs---and lack the sequential structure to recover from this misspecification.\n\n\\paragraph{Root cause: insufficient inter-LF conflict.}\nThese results constitute a negative finding: five label models spanning temporal aggregation and generative modeling all fail to improve over majority vote.\nThree binary LFs produce at most $2^3{=}8$ voting patterns; conf${\\geq}$2 windows dominate the training set, leaving insufficient ambiguity for any aggregation method to exploit.\nThe bottleneck is LF quantity, not aggregation sophistication---scaling to ${>}$10 LFs with higher disagreement rates is needed before advanced label models can add value.\nIn the current 3-LF, low-conflict regime (conf${\\geq}$2 agreement rate 95.1\\%), temporal alignment gains are offset by noise introduction.\nWith 5--10 LFs generating higher disagreement rates, temporal models may add value---this remains an open question.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\nWe construct a stratified gold set of 650 windows for non-circular evaluation.\nWindows are sampled along two axes: \\emph{confidence} (balanced across conf${=}1$, conf${=}2$, and conf${=}3$ strata to capture the full ambiguity spectrum) and \\emph{trajectory position} (early, middle, and late thirds, since stagnation dynamics differ across trajectory phases; \\S\\ref{sec:error_analysis}).\n\n\\paragraph{Annotation protocol.}\nTwo annotators independently label each window as stagnation or progress using an operational definition: \\emph{a window is stagnation if the agent's actions within it do not make meaningful progress toward solving the task, regardless of whether the actions appear diverse or purposeful}.\nAnnotators receive the $k{=}5$ action descriptions with full command outputs and file diffs, but \\emph{not} the task outcome (resolved/unresolved), preventing information leakage from $\\lambda_3$.\nDisagreements are resolved by a third annotator.\nGold validation results are pending; in the interim, cross-coding-agent transfer (\\S\\ref{sec:cross_agent}) and the feature overlap ablation (\\S\\ref{sec:feature_overlap}) provide non-circular evidence that structural features encode genuine stagnation signals rather than LF artifacts.",
      "numLines": 293,
      "startLine": 1,
      "totalLines": 293
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_012vK1BfRSyDFv7c6BY8rhkk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "30494103-4113-49db-a906-a8ad5a6709e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 24 · 2026-05-15T05:22:40.799Z_

<details><summary>↩ Tool result · `toolu_012vK1BfRSyDFv7c6BY8rhkk`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Circular Evaluation and Its Implications}
5	\label{sec:circular}
6	
7	The structural RF's 0.995 macro-F1 (\S\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.
8	The 30 structural features include repetition ratios and file operation counts---the same signals $\lambda_1$ and $\lambda_2$ consume to produce silver labels.
9	This score therefore represents an upper bound on LF reverse-engineering fidelity (a feature overlap ablation in \S\ref{sec:feature_overlap} quantifies this decomposition).
10	
11	Three evaluation settings break this circularity.
12	First, cross-coding-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.967 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\_rep votes stagnation on 5.4\% vs.\ 65.5\% of windows).
13	The model cannot memorize LF outputs when tested on a different agent's distribution.
14	Second, instance isolation: removing 284 SWE-bench task instances (8.3\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\,pp (Table~\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.
15	Third, a human-annotated gold set (\S\ref{sec:gold_set}) will provide definitive non-circular ground truth.
16	Until then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.
17	
18	\subsection{Feature Overlap Ablation}
19	\label{sec:feature_overlap}
20	
21	To quantify how much of the structural classifier's performance derives from LF-overlapping features versus residual signal, we partition the 30 features into two groups.
22	A feature is classified as \emph{LF-overlapping} if it directly computes the same function as any labeling function: command uniqueness and repetition ratios, adjacent command similarity scores ($\lambda_1$), edit and search command counts and ratios, file display counts ($\lambda_2$), and the short-trajectory indicator ($\lambda_3$).
23	This yields 11 LF-overlapping and 19 residual features (full classification in Appendix Table~\ref{tab:feature_defs}).
24	Table~\ref{tab:feature_overlap} reports GB performance for each subset.
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{lccc}
30	\toprule
31	\textbf{Feature Set} & \textbf{\#Feat} & \textbf{In-Dom.} & \textbf{Cross-Ag.} \\
32	\midrule
33	Full (all 30) & 30 & 0.9951 & 0.9674 \\
34	LF-overlap only & 11 & 0.9937 & \textbf{0.9770} \\
35	Residual only & 19 & 0.9515 & 0.5656 \\
36	\midrule
37	\multicolumn{4}{l}{\emph{Leave-one-group-out (cross-coding-agent)}} \\
38	$-$ cmd\_rep ($\lambda_1$) & 25 & --- & 0.5620 \\
39	$-$ file\_diff ($\lambda_2$) & 25 & --- & 0.6590 \\
40	$-$ outcome\_bp ($\lambda_3$) & 29 & --- & 0.9660 \\
41	\bottomrule
42	\end{tabular}
43	\caption{Feature overlap ablation (GB). In-Dom.\ = SWE-Agent in-domain macro-F1; Cross-Ag.\ = SWE-Agent $\to$ OpenHands zero-shot. Top: on all OH windows, LF-overlap features alone exceed the full model cross-coding-agent ($+$1.0\,pp; on conf${\geq}$2, direction reverses by $-$0.71\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\_rep features account for the largest transfer drop ($-$40.6\,pp).}
44	\label{tab:feature_overlap}
45	\end{table}
46	
47	Three findings emerge.
48	First, on all OH windows ($N{=}150{,}652$), 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\,pp.
49	This is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.
50	The improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.
51	(On the conf${\geq}$2 subset, the direction reverses: the full model leads by 0.71\,pp, indicating that residual features contribute positively when label noise is low; the all-windows advantage of LF-overlap features reflects their robustness to noisy conf${=}1$ labels.)
52	
53	Second, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.
54	However, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\sim}$0.55).
55	
56	Third, LF alignment is evidence of correct LF design, not circularity.
57	The features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.
58	One might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.
59	Two observations counter this.
60	First, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\_rep fires on 65.5\% vs.\ 5.4\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.
61	Second, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.
62	
63	A leave-one-group-out ablation (Table~\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.
64	Removing the five cmd\_rep features ($\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\,pp to 0.562; removing the five file\_diff features ($\lambda_2$: edit/search counts and file display) drops it by 30.8\,pp to 0.659.
65	In contrast, removing the single outcome\_bp feature ($\lambda_3$: is\_short\_trajectory) costs only 0.2\,pp (0.966).
66	Command repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\S\ref{sec:lf_temporal}).
67	
68	\subsection{Why No Label Model Improves Over Majority Vote}
69	\label{sec:why_tlm_fail}
70	
71	Despite clear temporal structure in LF activations (\S\ref{sec:lf_temporal}), no label model---temporal or generative---improves downstream detection over majority vote (\S\ref{sec:temporal_label_models}).
72	The failure spans five models with distinct inductive biases: TWV and Lag-HMM model temporal dynamics, HMM captures latent state transitions, while FlyingSquid and Snorkel MeTaL assume conditional independence.
73	All fail for the same root cause: three binary LFs produce at most $2^3{=}8$ voting patterns, and conf${\geq}$2 windows dominate the training set, leaving insufficient inter-LF conflict for any aggregation method to exploit.
74	
75	The failure modes differ by model class.
76	Temporal models either introduce noise (TWV: $-$2.57\,pp downstream despite $+$0.6\,pp self-evaluated) or overpredict stagnation (HMM: $-$14.4\,pp).
77	Generative models fare worse: FlyingSquid ($-$11.3\,pp) introduces systematic stagnation bias, and Snorkel MeTaL collapses catastrophically ($-$63.6\,pp, 42.3\% MV agreement).
78	Both assume conditional independence among LFs---violated by the shared behavioral signals underlying our three functions---and lack sequential structure to recover from this misspecification.
79	
80	The bottleneck is LF quantity, not aggregation sophistication.
81	Three binary LFs represent a realistic operating point for domain-specific agent monitoring, where each LF requires expert knowledge of agent failure modes.
82	Our finding that temporal label models fail in this low-LF regime has direct implications for practitioners who cannot afford to design ${>}$10 labeling functions: majority vote is not merely a convenient baseline but the recommended aggregation strategy.
83	Scaling to a richer LF set with higher disagreement rates would be needed to create the ambiguity where advanced aggregation could add value \citep{ratner2017snorkel}.
84	
85	\subsection{Error Analysis}
86	\label{sec:error_analysis}
87	
88	We analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).
89	The model misclassifies 131 of 1,824 windows (7.2\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\%).
90	
91	The recall bottleneck is the dominant failure mode: $P_\text{stag}{=}0.897$ vs.\ $R_\text{stag}{=}0.825$.
92	Missed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\% receiving $>$0.9 progress probability.
93	These windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.
94	False positives arise when agents repeat specific command patterns during genuine progress.
95	
96	LF conflict is a strong error predictor: 39.7\% of error windows have at least one LF disagreeing, compared to a 31\% base rate.
97	The cmd\_rep LF contributes the highest per-LF error rate (12.75\%).
98	Errors concentrate in trajectory midpoints (10.2\% error rate vs.\ 6.5\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.
99	Error mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\% of all misclassifications.
100	
101	\subsection{Cross-Agent Error Patterns}
102	\label{sec:cross_agent_errors}
103	
104	We extend error analysis to cross-coding-agent transfer, evaluating the SWE-trained probe and structural GB on the full OH conf${\geq}$2 set (43,376 windows).
105	The probe misclassifies 19.9\% of windows, while structural GB errs on only 0.51\% (223 windows)---a nearly 40$\times$ gap that quantifies the distributional shift penalty for learned embeddings.
106	Of the probe's errors, 80.5\% are false positives (predicting stagnation on progress windows), indicating that the probe systematically misreads OH action patterns as stagnation signals learned from SWE-Agent.
107	
108	The two models' errors are nearly disjoint: only 2.2\% of probe errors overlap with structural errors (192 of 8,643 probe-error windows).
109	Structural features, being agent-agnostic by construction, are immune to the embedding distribution shift that drives probe failures.
110	
111	The probe's cross-coding-agent errors are not borderline: 62\% occur at high confidence ($>$0.9 or $<$0.1), ruling out threshold tuning as a remedy.
112	The embedding space encodes SWE-Agent--specific stagnation patterns that confidently misfire on OH distributions, explaining why even 5\% target fine-tuning (reaching 0.850 macro-F1) dramatically outperforms zero-shot transfer.
113	
114	\subsection{Outcome Backpropagation as Distant Supervision}
115	\label{sec:ob_analysis}
116	
117	Outcome backpropagation ($\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.
118	A 3-seed split-isolated holdout removing $\lambda_3$ yields macro-F1 of $0.770{\pm}0.022$, a 7.7\,pp drop from the 3-LF baseline of 0.847.
119	$\lambda_3$ contributes 33.5\% of conf${\geq}$2 labels (5,158 of 15,401 windows).
120	
121	However, $\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\%.
122	$\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.
123	This suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "4dad9e8c-5c9e-4f05-9c83-21ed0f90a508",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Circular Evaluation and Its Implications}\n\\label{sec:circular}\n\nThe structural RF's 0.995 macro-F1 (\\S\\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.\nThe 30 structural features include repetition ratios and file operation counts---the same signals $\\lambda_1$ and $\\lambda_2$ consume to produce silver labels.\nThis score therefore represents an upper bound on LF reverse-engineering fidelity (a feature overlap ablation in \\S\\ref{sec:feature_overlap} quantifies this decomposition).\n\nThree evaluation settings break this circularity.\nFirst, cross-coding-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.967 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\\_rep votes stagnation on 5.4\\% vs.\\ 65.5\\% of windows).\nThe model cannot memorize LF outputs when tested on a different agent's distribution.\nSecond, instance isolation: removing 284 SWE-bench task instances (8.3\\% of OH test data) that appear in both training and test sets changes all cross-coding-agent macro-F1 by ${<}$0.1\\,pp (Table~\\ref{tab:instance_isolation}), ruling out instance memorization as an explanation for transfer performance.\nThird, a human-annotated gold set (\\S\\ref{sec:gold_set}) will provide definitive non-circular ground truth.\nUntil then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.\n\n\\subsection{Feature Overlap Ablation}\n\\label{sec:feature_overlap}\n\nTo quantify how much of the structural classifier's performance derives from LF-overlapping features versus residual signal, we partition the 30 features into two groups.\nA feature is classified as \\emph{LF-overlapping} if it directly computes the same function as any labeling function: command uniqueness and repetition ratios, adjacent command similarity scores ($\\lambda_1$), edit and search command counts and ratios, file display counts ($\\lambda_2$), and the short-trajectory indicator ($\\lambda_3$).\nThis yields 11 LF-overlapping and 19 residual features (full classification in Appendix Table~\\ref{tab:feature_defs}).\nTable~\\ref{tab:feature_overlap} reports GB performance for each subset.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Feature Set} & \\textbf{\\#Feat} & \\textbf{In-Dom.} & \\textbf{Cross-Ag.} \\\\\n\\midrule\nFull (all 30) & 30 & 0.9951 & 0.9674 \\\\\nLF-overlap only & 11 & 0.9937 & \\textbf{0.9770} \\\\\nResidual only & 19 & 0.9515 & 0.5656 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\emph{Leave-one-group-out (cross-coding-agent)}} \\\\\n$-$ cmd\\_rep ($\\lambda_1$) & 25 & --- & 0.5620 \\\\\n$-$ file\\_diff ($\\lambda_2$) & 25 & --- & 0.6590 \\\\\n$-$ outcome\\_bp ($\\lambda_3$) & 29 & --- & 0.9660 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature overlap ablation (GB). In-Dom.\\ = SWE-Agent in-domain macro-F1; Cross-Ag.\\ = SWE-Agent $\\to$ OpenHands zero-shot. Top: on all OH windows, LF-overlap features alone exceed the full model cross-coding-agent ($+$1.0\\,pp; on conf${\\geq}$2, direction reverses by $-$0.71\\,pp); residual features collapse. Bottom: removing each LF-group individually; cmd\\_rep features account for the largest transfer drop ($-$40.6\\,pp).}\n\\label{tab:feature_overlap}\n\\end{table}\n\nThree findings emerge.\nFirst, on all OH windows ($N{=}150{,}652$), 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1---exceeding the full 30-feature model (0.967) by 1.0\\,pp.\nThis is the opposite of what label leakage would predict: if these features merely reconstructed the labeling pipeline, adding more features could only help or be neutral, not hurt.\nThe improvement under fewer features reflects a regularization effect: the 19 residual features encode agent-specific patterns that introduce noise harmful to cross-coding-agent generalization.\n(On the conf${\\geq}$2 subset, the direction reverses: the full model leads by 0.71\\,pp, indicating that residual features contribute positively when label noise is low; the all-windows advantage of LF-overlap features reflects their robustness to noisy conf${=}1$ labels.)\n\nSecond, residual features retain non-trivial in-domain signal: 19 features achieve 0.952 macro-F1, confirming that stagnation manifests in patterns beyond what the three LFs capture---text length statistics, trajectory counts, and output statistics carry independent diagnostic value.\nHowever, this signal is agent-specific: cross-coding-agent F1 collapses to 0.566, near the majority baseline (${\\sim}$0.55).\n\nThird, LF alignment is evidence of correct LF design, not circularity.\nThe features that generalize across coding agents are precisely those encoding universal stagnation signals---command repetition patterns and file operation dynamics---rather than agent-specific idiosyncrasies captured by residual features.\nOne might object that LF-overlapping features merely reconstruct the label-generation pipeline rather than detecting real stagnation.\nTwo observations counter this.\nFirst, the cross-coding-agent evaluation is itself non-circular: the SWE-Agent LF firing distribution differs drastically from OpenHands (e.g., cmd\\_rep fires on 65.5\\% vs.\\ 5.4\\% of windows), so a model that merely memorizes LF outputs would fail on the target agent---yet structural GB achieves 0.967.\nSecond, if cross-coding-agent success were an artifact of label reconstruction, removing LF-overlapping features should \\emph{not} degrade cross-coding-agent performance (the residual features would reconstruct equally well); instead it collapses to 0.566, confirming that the LF-overlapping features encode genuinely transferable stagnation signals rather than pipeline-specific artifacts.\n\nA leave-one-group-out ablation (Table~\\ref{tab:feature_overlap}, bottom) further localizes the transfer signal.\nRemoving the five cmd\\_rep features ($\\lambda_1$: repetition ratios and adjacent command similarity) drops cross-coding-agent F1 by 40.6\\,pp to 0.562; removing the five file\\_diff features ($\\lambda_2$: edit/search counts and file display) drops it by 30.8\\,pp to 0.659.\nIn contrast, removing the single outcome\\_bp feature ($\\lambda_3$: is\\_short\\_trajectory) costs only 0.2\\,pp (0.966).\nCommand repetition patterns are thus the dominant carrier of cross-coding-agent transfer, consistent with their role as a universal stagnation signal (\\S\\ref{sec:lf_temporal}).\n\n\\subsection{Why No Label Model Improves Over Majority Vote}\n\\label{sec:why_tlm_fail}\n\nDespite clear temporal structure in LF activations (\\S\\ref{sec:lf_temporal}), no label model---temporal or generative---improves downstream detection over majority vote (\\S\\ref{sec:temporal_label_models}).\nThe failure spans five models with distinct inductive biases: TWV and Lag-HMM model temporal dynamics, HMM captures latent state transitions, while FlyingSquid and Snorkel MeTaL assume conditional independence.\nAll fail for the same root cause: three binary LFs produce at most $2^3{=}8$ voting patterns, and conf${\\geq}$2 windows dominate the training set, leaving insufficient inter-LF conflict for any aggregation method to exploit.\n\nThe failure modes differ by model class.\nTemporal models either introduce noise (TWV: $-$2.57\\,pp downstream despite $+$0.6\\,pp self-evaluated) or overpredict stagnation (HMM: $-$14.4\\,pp).\nGenerative models fare worse: FlyingSquid ($-$11.3\\,pp) introduces systematic stagnation bias, and Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp, 42.3\\% MV agreement).\nBoth assume conditional independence among LFs---violated by the shared behavioral signals underlying our three functions---and lack sequential structure to recover from this misspecification.\n\nThe bottleneck is LF quantity, not aggregation sophistication.\nThree binary LFs represent a realistic operating point for domain-specific agent monitoring, where each LF requires expert knowledge of agent failure modes.\nOur finding that temporal label models fail in this low-LF regime has direct implications for practitioners who cannot afford to design ${>}$10 labeling functions: majority vote is not merely a convenient baseline but the recommended aggregation strategy.\nScaling to a richer LF set with higher disagreement rates would be needed to create the ambiguity where advanced aggregation could add value \\citep{ratner2017snorkel}.\n\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).\nThe model misclassifies 131 of 1,824 windows (7.2\\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\\%).\n\nThe recall bottleneck is the dominant failure mode: $P_\\text{stag}{=}0.897$ vs.\\ $R_\\text{stag}{=}0.825$.\nMissed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\\% receiving $>$0.9 progress probability.\nThese windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.\nFalse positives arise when agents repeat specific command patterns during genuine progress.\n\nLF conflict is a strong error predictor: 39.7\\% of error windows have at least one LF disagreeing, compared to a 31\\% base rate.\nThe cmd\\_rep LF contributes the highest per-LF error rate (12.75\\%).\nErrors concentrate in trajectory midpoints (10.2\\% error rate vs.\\ 6.5\\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.\nError mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\\% of all misclassifications.\n\n\\subsection{Cross-Agent Error Patterns}\n\\label{sec:cross_agent_errors}\n\nWe extend error analysis to cross-coding-agent transfer, evaluating the SWE-trained probe and structural GB on the full OH conf${\\geq}$2 set (43,376 windows).\nThe probe misclassifies 19.9\\% of windows, while structural GB errs on only 0.51\\% (223 windows)---a nearly 40$\\times$ gap that quantifies the distributional shift penalty for learned embeddings.\nOf the probe's errors, 80.5\\% are false positives (predicting stagnation on progress windows), indicating that the probe systematically misreads OH action patterns as stagnation signals learned from SWE-Agent.\n\nThe two models' errors are nearly disjoint: only 2.2\\% of probe errors overlap with structural errors (192 of 8,643 probe-error windows).\nStructural features, being agent-agnostic by construction, are immune to the embedding distribution shift that drives probe failures.\n\nThe probe's cross-coding-agent errors are not borderline: 62\\% occur at high confidence ($>$0.9 or $<$0.1), ruling out threshold tuning as a remedy.\nThe embedding space encodes SWE-Agent--specific stagnation patterns that confidently misfire on OH distributions, explaining why even 5\\% target fine-tuning (reaching 0.850 macro-F1) dramatically outperforms zero-shot transfer.\n\n\\subsection{Outcome Backpropagation as Distant Supervision}\n\\label{sec:ob_analysis}\n\nOutcome backpropagation ($\\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.\nA 3-seed split-isolated holdout removing $\\lambda_3$ yields macro-F1 of $0.770{\\pm}0.022$, a 7.7\\,pp drop from the 3-LF baseline of 0.847.\n$\\lambda_3$ contributes 33.5\\% of conf${\\geq}$2 labels (5,158 of 15,401 windows).\n\nHowever, $\\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\\%.\n$\\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.\nThis suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.",
      "numLines": 123,
      "startLine": 1,
      "totalLines": 123
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01LHycGDizUtcpgzGr8mkxCe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "bbf5cc5e-71e5-4890-ad5a-3e6d965ce18b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 26 · 2026-05-15T05:22:41.732Z_

<details><summary>↩ Tool result · `toolu_01LHycGDizUtcpgzGr8mkxCe`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches across deployment regimes using a weak supervision methodology.
5	Three findings emerge.
6	
7	First, a deployment-regime trade-off governs method selection.
8	In zero-data cross-coding-agent transfer (SWE-Agent $\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\,pp and the best LLM judge by 16.8\,pp (cross-coding-agent structural 0.967 vs.\ best LLM 0.799).
9	With target-agent fine-tuning the probe surpasses structural features on all windows (0.976 vs.\ 0.967); on the higher-confidence conf${\geq}$2 subset GB retains its edge (0.993 vs.\ 0.976), confirming that the structural advantage persists where label noise is low.
10	A feature overlap ablation confirms that 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1 on all windows, exceeding the full 30-feature model ($+$1.0\,pp), while 19 residual features collapse to 0.566; LF alignment reflects correct LF design rather than label leakage.
11	
12	Second, labeling functions exhibit agent-specific temporal dynamics.
13	Command repetition leads stagnation onset by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.
14	A label quality audit reveals cmd\_rep is a high-precision detector (97.91\% precision) whose core value is coverage: prevalence-matched ablation shows removing it collapses training data 10$\times$ (43K$\to$4K) and costs $-$29.4\,pp (p$\approx$0).
15	Label version bias---not LF noise---was the dominant transfer bottleneck.
16	
17	Third, no label model improves over majority vote.
18	Five label models---three temporal (TWV, HMM, lag-aware HMM) and two generative (FlyingSquid, Snorkel MeTaL)---all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically ($-$63.6\,pp).
19	The bottleneck is LF quantity, not aggregation method: three binary LFs produce insufficient inter-LF conflict for any approach to exploit.
20	
21	Agent monitoring should therefore prioritize lightweight structural features ({<}5\,ms per window, no GPU) for zero-data deployment; when labeled target-agent data is available, neural probes become competitive and eventually surpass structural baselines.
22	All reported results are evaluated on silver labels derived from our labeling functions; cross-coding-agent transfer and a feature overlap ablation provide non-circular evidence.
23	
24	Future work includes extending evaluation to non-software-engineering agent domains (web navigation, data analysis), online integration with early termination or strategy switching, scaling to ${>}$10 labeling functions to test whether temporal aggregation becomes useful, and human-annotated gold set validation.
25	
26	\paragraph{Reproducibility.}
27	Code, silver labels, and trained models will be released upon acceptance.
28	All agent trajectories are derived from publicly available SWE-bench runs \citep{jimenez2024swebench}; labeling functions and feature extraction are fully deterministic given the trajectory data.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "69e6e12a-f6a4-45da-b56b-fa1bec6b32f5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic study of progress stagnation detection in LLM coding agents, comparing structural features, neural embedding probes, and LLM-as-judge approaches across deployment regimes using a weak supervision methodology.\nThree findings emerge.\n\nFirst, a deployment-regime trade-off governs method selection.\nIn zero-data cross-coding-agent transfer (SWE-Agent $\\to$ OpenHands on SWE-bench), 30 structural features achieve 0.967 macro-F1 on silver labels, outperforming neural probes by 36.9\\,pp and the best LLM judge by 16.8\\,pp (cross-coding-agent structural 0.967 vs.\\ best LLM 0.799).\nWith target-agent fine-tuning the probe surpasses structural features on all windows (0.976 vs.\\ 0.967); on the higher-confidence conf${\\geq}$2 subset GB retains its edge (0.993 vs.\\ 0.976), confirming that the structural advantage persists where label noise is low.\nA feature overlap ablation confirms that 11 LF-overlapping features alone achieve 0.977 cross-coding-agent F1 on all windows, exceeding the full 30-feature model ($+$1.0\\,pp), while 19 residual features collapse to 0.566; LF alignment reflects correct LF design rather than label leakage.\n\nSecond, labeling functions exhibit agent-specific temporal dynamics.\nCommand repetition leads stagnation onset by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.\nA label quality audit reveals cmd\\_rep is a high-precision detector (97.91\\% precision) whose core value is coverage: prevalence-matched ablation shows removing it collapses training data 10$\\times$ (43K$\\to$4K) and costs $-$29.4\\,pp (p$\\approx$0).\nLabel version bias---not LF noise---was the dominant transfer bottleneck.\n\nThird, no label model improves over majority vote.\nFive label models---three temporal (TWV, HMM, lag-aware HMM) and two generative (FlyingSquid, Snorkel MeTaL)---all fail to surpass majority vote; Snorkel MeTaL collapses catastrophically ($-$63.6\\,pp).\nThe bottleneck is LF quantity, not aggregation method: three binary LFs produce insufficient inter-LF conflict for any approach to exploit.\n\nAgent monitoring should therefore prioritize lightweight structural features ({<}5\\,ms per window, no GPU) for zero-data deployment; when labeled target-agent data is available, neural probes become competitive and eventually surpass structural baselines.\nAll reported results are evaluated on silver labels derived from our labeling functions; cross-coding-agent transfer and a feature overlap ablation provide non-circular evidence.\n\nFuture work includes extending evaluation to non-software-engineering agent domains (web navigation, data analysis), online integration with early termination or strategy switching, scaling to ${>}$10 labeling functions to test whether temporal aggregation becomes useful, and human-annotated gold set validation.\n\n\\paragraph{Reproducibility.}\nCode, silver labels, and trained models will be released upon acceptance.\nAll agent trajectories are derived from publicly available SWE-bench runs \\citep{jimenez2024swebench}; labeling functions and feature extraction are fully deterministic given the trajectory data.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_013FTPCpveLEJ2fvB6bn7BJi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "47d06aeb-3643-4371-856b-a55bce0df784",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 28 · 2026-05-15T05:22:42.300Z_

<details><summary>↩ Tool result · `toolu_013FTPCpveLEJ2fvB6bn7BJi`</summary>

```text
1	\label{sec:limitations}
2	
3	\paragraph{Scope.}
4	We evaluate two software engineering coding agents (SWE-Agent and OpenHands) on SWE-bench.
5	Cross-coding-agent transfer is demonstrated between these two agents; generalization to non-coding agent domains---web navigation, data analysis, multi-agent collaboration---remains untested.
6	
7	\paragraph{Silver labels.}
8	All evaluation is against labeling-function-derived silver labels; the structural RF's 0.995 macro-F1 reflects LF-reconstructibility rather than ground-truth detection accuracy.
9	A 650-window gold set with a validated annotation pipeline is prepared but human annotation is pending; see \S\ref{sec:gold_set} for protocol details.
10	
11	\paragraph{Labeling function count.}
12	Three LFs produce insufficient inter-LF conflict (95.1\% agreement at conf${\geq}$2) for any label model---temporal or generative---to demonstrate value; scaling to ${>}$10 LFs with higher disagreement is needed.
13	
14	\paragraph{No online evaluation.}
15	All results are offline; no intervention or real-time deployment evaluation has been conducted.
16	
17	\paragraph{Label version sensitivity.}
18	Cross-coding-agent transfer results are sensitive to label quality: a single embedding version mismatch shifted the OH stagnation rate from 6.56\% to 21.4\% and improved 5\% fine-tuning F1 from 0.570 to 0.850.
19	This sensitivity suggests that deploying the pipeline on new agents requires careful label auditing before conclusions about transfer difficulty can be drawn.
20	
21	\paragraph{Outcome dependence.}
22	The outcome backpropagation labeling function ($\lambda_3$) requires task outcome, which is unavailable during inference.
23	
24	\paragraph{Code and data.}
25	Code, data, and trained models are anonymous during review and will be released upon acceptance.
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "929ea60f-8c45-48aa-b0c0-6dbdeea9fd48",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/limitations.tex",
      "content": "\\label{sec:limitations}\n\n\\paragraph{Scope.}\nWe evaluate two software engineering coding agents (SWE-Agent and OpenHands) on SWE-bench.\nCross-coding-agent transfer is demonstrated between these two agents; generalization to non-coding agent domains---web navigation, data analysis, multi-agent collaboration---remains untested.\n\n\\paragraph{Silver labels.}\nAll evaluation is against labeling-function-derived silver labels; the structural RF's 0.995 macro-F1 reflects LF-reconstructibility rather than ground-truth detection accuracy.\nA 650-window gold set with a validated annotation pipeline is prepared but human annotation is pending; see \\S\\ref{sec:gold_set} for protocol details.\n\n\\paragraph{Labeling function count.}\nThree LFs produce insufficient inter-LF conflict (95.1\\% agreement at conf${\\geq}$2) for any label model---temporal or generative---to demonstrate value; scaling to ${>}$10 LFs with higher disagreement is needed.\n\n\\paragraph{No online evaluation.}\nAll results are offline; no intervention or real-time deployment evaluation has been conducted.\n\n\\paragraph{Label version sensitivity.}\nCross-coding-agent transfer results are sensitive to label quality: a single embedding version mismatch shifted the OH stagnation rate from 6.56\\% to 21.4\\% and improved 5\\% fine-tuning F1 from 0.570 to 0.850.\nThis sensitivity suggests that deploying the pipeline on new agents requires careful label auditing before conclusions about transfer difficulty can be drawn.\n\n\\paragraph{Outcome dependence.}\nThe outcome backpropagation labeling function ($\\lambda_3$) requires task outcome, which is unavailable during inference.\n\n\\paragraph{Code and data.}\nCode, data, and trained models are anonymous during review and will be released upon acceptance.\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01JiMYj1qhk8WQvCzruWYxTU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "ffb51d89-039e-4f66-aeba-29cbca7242ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 30 · 2026-05-15T05:22:42.686Z_

<details><summary>↩ Tool result · `toolu_01JiMYj1qhk8WQvCzruWYxTU`</summary>

```text
1	% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	LLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges.
3	No systematic study has compared detection approaches across deployment scenarios or investigated what signals carry stagnation information.
4	
5	We propose a weak supervision methodology for agent stagnation monitoring: three labeling functions aggregated by majority vote produce silver labels over 205K+ windows from two coding agents (SWE-Agent and OpenHands) on SWE-bench.
6	Against these labels, we compare 30 structural features, a GRU-based neural probe, and LLM-as-judge baselines across zero-data and fine-tuned regimes.
7	
8	We find a deployment-regime trade-off.
9	In zero-data cross-coding-agent transfer, structural features outperform the neural probe by 36.9\,pp and the best LLM judge by 16.8\,pp (cross-coding-agent structural 0.967 vs.\ best LLM 0.799).
10	With target-agent fine-tuning, the probe catches up and surpasses structural features on all evaluation windows (0.976 vs.\ 0.967), demonstrating that the structural advantage is specific to the zero-data regime.
11	Structural features are also data-efficient, exceeding 0.987 F1 at 10\% training data.
12	
13	Labeling functions exhibit agent-specific temporal dynamics: command repetition leads stagnation by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.
14	Label version bias---not LF noise---was the dominant cross-coding-agent transfer bottleneck; fixing it improved 5\% fine-tuning F1 from 0.570 to 0.850.
15	Five label models (three temporal, two generative) all fail to improve over majority vote; the bottleneck is LF quantity, not aggregation sophistication.
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "4cfccd4f-4b12-4018-920e-1a3320ed939a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/abstract.tex",
      "content": "% Abstract: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\nLLM-based agents deployed on software engineering tasks frequently exhibit semantic stagnation---executing diverse yet collectively unproductive action sequences that evade repetition detectors and overwhelm LLM-based judges.\nNo systematic study has compared detection approaches across deployment scenarios or investigated what signals carry stagnation information.\n\nWe propose a weak supervision methodology for agent stagnation monitoring: three labeling functions aggregated by majority vote produce silver labels over 205K+ windows from two coding agents (SWE-Agent and OpenHands) on SWE-bench.\nAgainst these labels, we compare 30 structural features, a GRU-based neural probe, and LLM-as-judge baselines across zero-data and fine-tuned regimes.\n\nWe find a deployment-regime trade-off.\nIn zero-data cross-coding-agent transfer, structural features outperform the neural probe by 36.9\\,pp and the best LLM judge by 16.8\\,pp (cross-coding-agent structural 0.967 vs.\\ best LLM 0.799).\nWith target-agent fine-tuning, the probe catches up and surpasses structural features on all evaluation windows (0.976 vs.\\ 0.967), demonstrating that the structural advantage is specific to the zero-data regime.\nStructural features are also data-efficient, exceeding 0.987 F1 at 10\\% training data.\n\nLabeling functions exhibit agent-specific temporal dynamics: command repetition leads stagnation by 1.87 steps on SWE-Agent but lags by 3.32 steps on OpenHands.\nLabel version bias---not LF noise---was the dominant cross-coding-agent transfer bottleneck; fixing it improved 5\\% fine-tuning F1 from 0.570 to 0.850.\nFive label models (three temporal, two generative) all fail to improve over majority vote; the bottleneck is LF quantity, not aggregation sophistication.\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01PWwvTN2KR9QNeEPDqtdZBm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "4e39b8d8-7e50-49cf-a141-4f604649c25c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NpnfZqiaekGkwhShdVxLpb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 282,
      "cache_read_input_tokens": 30017,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 282
      },
      "output_tokens": 63,
      "service_tier": "standard",
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

_source line 32 · 2026-05-15T05:22:42.907Z_

<details><summary>↩ Tool result · `toolu_01PWwvTN2KR9QNeEPDqtdZBm`</summary>

```text
1	\section{Supplementary Results}
2	\label{sec:appendix}
3	
4	%-------------------------------------------------------------------
5	\subsection{Encoder Ablation}
6	\label{sec:app_encoder}
7	
8	\begin{table}[h]
9	\centering
10	\small
11	\begin{tabular}{lccccc}
12	\toprule
13	\textbf{Encoder} & \textbf{Dim} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{Best Ep.} \\
14	\midrule
15	Qwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\
16	E5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\
17	BGE-M3 & 1024 & \textbf{0.9413} & \textbf{0.9147} & \textbf{0.9679} & 5 \\
18	\bottomrule
19	\end{tabular}
20	\caption{Encoder ablation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\,pp over Qwen3), but the gap between encoders (0.5\,pp) is small relative to the structural--probe gap (8.96\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}
21	\label{tab:encoder_ablation}
22	\end{table}
23	
24	%-------------------------------------------------------------------
25	\subsection{Window Size Ablation}
26	\label{sec:app_window}
27	
28	\begin{table}[h]
29	\centering
30	\small
31	\begin{tabular}{ccccc}
32	\toprule
33	\textbf{Window $k$} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{$\Delta$ vs.\ $k{=}5$} \\
34	\midrule
35	3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\,pp \\
36	\textbf{5} & \textbf{0.9309} & \textbf{0.8917} & \textbf{0.9701} & --- \\
37	7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\,pp \\
38	\bottomrule
39	\end{tabular}
40	\caption{Window size ablation on SWE-Agent conf${\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\textsubscript{stag} drops 11.3\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}
41	\label{tab:window_ablation}
42	\end{table}
43	
44	%-------------------------------------------------------------------
45	\subsection{Multi-Seed Stability}
46	\label{sec:app_multiseed}
47	
48	\begin{table}[h]
49	\centering
50	\small
51	\begin{tabular}{lcccc}
52	\toprule
53	\textbf{Method} & \textbf{In-Domain F1} & \textbf{Seeds} & \textbf{Cross-Agent F1} & \textbf{Seeds} \\
54	\midrule
55	Structural RF & $0.9951 \pm 0.0000$ & 5 & --- & --- \\
56	Structural GB & --- & --- & $0.9678 \pm 0.0015$ & 5 \\
57	ProgressProbe (GRU) & $0.9185 \pm 0.0113$ & 5 & --- & --- \\
58	\bottomrule
59	\end{tabular}
60	\caption{Multi-seed stability (mean $\pm$ std). In-domain: SWE-Agent conf${\geq}$2; cross-coding-agent: SWE-Agent $\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}
61	\label{tab:multiseed}
62	\end{table}
63	
64	%-------------------------------------------------------------------
65	\subsection{Cross-Agent Label Quality and Few-Shot Transfer}
66	\label{sec:app_cmdrep}
67	
68	Table~\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \S\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.
69	
70	\begin{table}[h]
71	\centering
72	\small
73	\begin{tabular}{lc}
74	\toprule
75	\textbf{OH Data Fraction} & \textbf{Probe Macro-F1} \\
76	\midrule
77	0\% (zero-shot) & 0.598 \\
78	5\% & 0.850 \\
79	10\% & 0.918 \\
80	20\% & 0.948 \\
81	50\% & 0.968 \\
82	100\% & 0.976 \\
83	\bottomrule
84	\end{tabular}
85	\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\% jump ($+$25.2\,pp) and rapid convergence toward structural GB (0.992 on conf${\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\% fine-tuning reached only 0.570.}
86	\label{tab:cross_agent_cmdrep}
87	\end{table}
88	
89	The probe reaches 0.948 macro-F1 at 20\% OH data---within 5\,pp of structural GB on conf${\geq}$2 windows (0.992)---and at 50\% (0.968) closes to within 2.5\,pp of structural GB on conf${\geq}$2 (0.992).
90	This rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\% fine-tuning reached only 0.751.
91	The improvement is driven entirely by label quality: the model architecture and training procedure are identical.
92	
93	Under the prevalence-matched ablation (\S\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\% of overlapping windows, confirming that cmd\_rep's contribution is coverage (expanding conf${\geq}$2 training data from ${\sim}$4K to ${\sim}$43K windows) rather than label refinement.
94	The $-29.4$\,pp drop upon removing cmd\_rep (McNemar $\chi^2{=}1{,}551$, $p{\approx}0$) is thus attributable to data volume collapse, not label noise.
95	
96	%-------------------------------------------------------------------
97	\subsection{Structural Feature Definitions}
98	\label{sec:app_features}
99	
100	Table~\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.
101	A feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\S\ref{sec:feature_overlap}).
102	
103	\begin{table*}[h]
104	\centering
105	\small
106	\begin{tabular}{rlll}
107	\toprule
108	\textbf{\#} & \textbf{Feature} & \textbf{Category} & \textbf{LF Overlap} \\
109	\midrule
110	1  & num\_steps             & Trajectory stats    & --- \\
111	2  & num\_actions           & Trajectory stats    & --- \\
112	3  & num\_observations      & Trajectory stats    & --- \\
113	4  & action\_ratio          & Trajectory stats    & --- \\
114	5  & mean\_text\_len        & Text statistics     & --- \\
115	6  & std\_text\_len         & Text statistics     & --- \\
116	7  & max\_text\_len         & Text statistics     & --- \\
117	8  & min\_text\_len         & Text statistics     & --- \\
118	9  & mean\_action\_len      & Text statistics     & --- \\
119	10 & mean\_obs\_len         & Text statistics     & --- \\
120	11 & text\_len\_trend       & Text statistics     & --- \\
121	12 & num\_commands          & Command stats       & --- \\
122	13 & mean\_cmd\_len         & Command stats       & --- \\
123	14 & max\_cmd\_len          & Command stats       & --- \\
124	15 & unique\_cmd\_ratio     & Repetition          & $\lambda_1$ \\
125	16 & max\_repeat\_ratio     & Repetition          & $\lambda_1$ \\
126	17 & num\_edit\_cmds        & File operations     & $\lambda_2$ \\
127	18 & num\_search\_cmds      & File operations     & $\lambda_2$ \\
128	19 & num\_nav\_cmds         & File operations     & --- \\
129	20 & num\_submit\_cmds      & File operations     & --- \\
130	21 & edit\_ratio            & File operations     & $\lambda_2$ \\
131	22 & search\_ratio          & File operations     & $\lambda_2$ \\
132	23 & avg\_adjacent\_cmd\_sim & Edit distance       & $\lambda_1$ \\
133	24 & max\_adjacent\_cmd\_sim & Edit distance       & $\lambda_1$ \\
134	25 & max\_consec\_similar   & Edit distance       & $\lambda_1$ \\
135	26 & num\_errors            & Output statistics   & --- \\
136	27 & num\_test\_outputs     & Output statistics   & --- \\
137	28 & num\_file\_displays    & Output statistics   & $\lambda_2$ \\
138	29 & num\_nonzero\_exits    & Output statistics   & --- \\
139	30 & is\_short\_trajectory  & Trajectory stats    & $\lambda_3$ \\
140	\bottomrule
141	\end{tabular}
142	\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\lambda_1$ (command repetition), $\lambda_2$ (file diff), $\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}
143	\label{tab:feature_defs}
144	\end{table*}
145	
146	%-------------------------------------------------------------------
147	\subsection{Instance Isolation}
148	\label{sec:app_instance_isolation}
149	
150	\begin{table}[h]
151	\centering
152	\small
153	\begin{tabular}{lccc}
154	\toprule
155	\textbf{Model} & \textbf{Full} & \textbf{Unseen-only} & \textbf{$\Delta$} \\
156	\midrule
157	GB all & 0.9674 & 0.9669 & $-$0.05\,pp \\
158	RF all & 0.9123 & 0.9121 & $-$0.01\,pp \\
159	GB conf${\geq}$2 & 0.9919 & 0.9917 & $-$0.02\,pp \\
160	RF conf${\geq}$2 & 0.9959 & 0.9962 & $+$0.03\,pp \\
161	\bottomrule
162	\end{tabular}
163	\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\% of OH). All $|\Delta| < 0.1$\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}
164	\label{tab:instance_isolation}
165	\end{table}
166	
167	%-------------------------------------------------------------------
168	\subsection{Extended LLM-as-Judge Evaluation}
169	\label{sec:llm_extended}
170	
171	Table~\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\ref{tab:main_results}) with chain-of-thought (CoT) prompting, few-shot examples, and an alternative model, all evaluated on the SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$).
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\begin{tabular}{llcccc}
177	\toprule
178	\textbf{Model} & \textbf{Setting} & \textbf{Macro-F1} & \textbf{F1\textsubscript{stag}} & \textbf{F1\textsubscript{prog}} & \textbf{Cost} \\
179	\midrule
180	Claude Sonnet 4.6 & zero-shot & 0.6625 & 0.6055 & 0.7195 & \$11.66 \\
181	Claude Sonnet 4.6 & CoT & 0.7499 & 0.6808 & 0.8189 & \$17.16 \\
182	Claude Sonnet 4.6 & 5-shot & 0.7514 & 0.6828 & 0.8199 & \$36.08 \\
183	Claude Sonnet 4.6 & 5-shot-CoT & \textbf{0.7994} & \textbf{0.7306} & \textbf{0.8681} & \$40.56 \\
184	GPT-5.5$^\dagger$ & zero-shot & 0.7465 & 0.7110 & 0.7819 & \$11.62 \\
185	\midrule
186	\multicolumn{6}{l}{\emph{Structural feature augmentation}} \\
187	Claude Sonnet 4.6 & + structural input$^\ddagger$ & 0.6880 & 0.6270 & 0.7490 & \$14.82 \\
188	\bottomrule
189	\end{tabular}
190	\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\geq}$2 ($N{=}1{,}824$). All Claude rows use the same model; the performance gain comes from prompting strategy. CoT alone yields gains comparable to few-shot ($+$8.7\,pp vs.\ $+$8.9\,pp over zero-shot); combining them (five-shot-CoT) adds a further 4.8\,pp, suggesting complementary mechanisms. $^\ddagger$30 structural features provided as formatted text in the LLM prompt; performance degrades below pure few-shot (0.751), indicating structural signals require engineered classifiers. $^\dagger$GPT-5.5: 22.4\% of responses (408/1,824) failed to parse; macro-F1 is computed over the 1,416 windows with valid outputs. The best LLM configuration (0.799 in-domain) trails structural cross-coding-agent transfer (0.967) by 16.8\,pp. Total API cost across all configurations: \$131.90.}
191	\label{tab:llm_extended}
192	\end{table}
193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e042fa88-d1c2-49b3-81b3-181e8f45e5a5",
  "uuid": "6774bdcd-428a-40fc-9fde-3afb6731bc1a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/appendix.tex",
      "content": "\\section{Supplementary Results}\n\\label{sec:appendix}\n\n%-------------------------------------------------------------------\n\\subsection{Encoder Ablation}\n\\label{sec:app_encoder}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Encoder} & \\textbf{Dim} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{Best Ep.} \\\\\n\\midrule\nQwen3-0.6B & 1024 & 0.9055 & --- & --- & --- \\\\\nE5-large-v2 & 1024 & 0.9363 & 0.9067 & 0.9660 & 4 \\\\\nBGE-M3 & 1024 & \\textbf{0.9413} & \\textbf{0.9147} & \\textbf{0.9679} & 5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Encoder ablation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). All models use the same GRU architecture (2-layer, hidden$=$256, dropout$=$0.1, lr$=$1e-3, batch$=$32, early stopping patience~5). All encoders exceed 0.90 macro-F1, confirming the probe's temporal architecture drives performance rather than a specific encoder. BGE-M3 achieves the highest score ($+$3.6\\,pp over Qwen3), but the gap between encoders (0.5\\,pp) is small relative to the structural--probe gap (8.96\\,pp). ``---'' for Qwen3 indicates per-class scores were not logged in the initial sweep; macro-F1 is computed from the checkpoint with lowest validation loss.}\n\\label{tab:encoder_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Window Size Ablation}\n\\label{sec:app_window}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{ccccc}\n\\toprule\n\\textbf{Window $k$} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{$\\Delta$ vs.\\ $k{=}5$} \\\\\n\\midrule\n3 & 0.8721 & 0.7784 & 0.9659 & $-$5.9\\,pp \\\\\n\\textbf{5} & \\textbf{0.9309} & \\textbf{0.8917} & \\textbf{0.9701} & --- \\\\\n7 & 0.9133 & 0.8791 & 0.9475 & $-$1.8\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Window size ablation on SWE-Agent conf${\\geq}$2 using the Qwen3-0.6B encoder (seed~42). $k{=}5$ is optimal. $k{=}3$ lacks sufficient context for stagnation detection (F1\\textsubscript{stag} drops 11.3\\,pp). $k{=}7$ dilutes signal by spanning both progress and stagnation phases.}\n\\label{tab:window_ablation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Multi-Seed Stability}\n\\label{sec:app_multiseed}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Method} & \\textbf{In-Domain F1} & \\textbf{Seeds} & \\textbf{Cross-Agent F1} & \\textbf{Seeds} \\\\\n\\midrule\nStructural RF & $0.9951 \\pm 0.0000$ & 5 & --- & --- \\\\\nStructural GB & --- & --- & $0.9678 \\pm 0.0015$ & 5 \\\\\nProgressProbe (GRU) & $0.9185 \\pm 0.0113$ & 5 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Multi-seed stability (mean $\\pm$ std). In-domain: SWE-Agent conf${\\geq}$2; cross-coding-agent: SWE-Agent $\\to$ OpenHands zero-shot transfer. Structural classifiers show zero or near-zero variance. The probe exhibits higher variance ($\\sigma{=}0.011$) but all seeds exceed 0.90. ``---'' indicates the setting was not evaluated: RF is evaluated in-domain only, GB cross-coding-agent only, and the probe in-domain only.}\n\\label{tab:multiseed}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Label Quality and Few-Shot Transfer}\n\\label{sec:app_cmdrep}\n\nTable~\\ref{tab:cross_agent_cmdrep} extends the label quality analysis from \\S\\ref{sec:cmd_rep_ablation}, showing probe fine-tuning performance across data fractions under corrected OH labels.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lc}\n\\toprule\n\\textbf{OH Data Fraction} & \\textbf{Probe Macro-F1} \\\\\n\\midrule\n0\\% (zero-shot) & 0.598 \\\\\n5\\% & 0.850 \\\\\n10\\% & 0.918 \\\\\n20\\% & 0.948 \\\\\n50\\% & 0.968 \\\\\n100\\% & 0.976 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Probe fine-tuning on corrected OH labels across data fractions. The zero-shot--to--5\\% jump ($+$25.2\\,pp) and rapid convergence toward structural GB (0.992 on conf${\\geq}$2) demonstrate that label quality, not model capacity, was the transfer bottleneck. Under old (corrupted) labels, 5\\% fine-tuning reached only 0.570.}\n\\label{tab:cross_agent_cmdrep}\n\\end{table}\n\nThe probe reaches 0.948 macro-F1 at 20\\% OH data---within 5\\,pp of structural GB on conf${\\geq}$2 windows (0.992)---and at 50\\% (0.968) closes to within 2.5\\,pp of structural GB on conf${\\geq}$2 (0.992).\nThis rapid convergence under corrected labels contrasts sharply with the old label regime, where even 100\\% fine-tuning reached only 0.751.\nThe improvement is driven entirely by label quality: the model architecture and training procedure are identical.\n\nUnder the prevalence-matched ablation (\\S\\ref{sec:cmd_rep_ablation}), 3-LF and 2-LF label sets agree on 100\\% of overlapping windows, confirming that cmd\\_rep's contribution is coverage (expanding conf${\\geq}$2 training data from ${\\sim}$4K to ${\\sim}$43K windows) rather than label refinement.\nThe $-29.4$\\,pp drop upon removing cmd\\_rep (McNemar $\\chi^2{=}1{,}551$, $p{\\approx}0$) is thus attributable to data volume collapse, not label noise.\n\n%-------------------------------------------------------------------\n\\subsection{Structural Feature Definitions}\n\\label{sec:app_features}\n\nTable~\\ref{tab:feature_defs} lists all 30 structural features with their categories and LF overlap classification.\nA feature is classified as LF-overlapping if it is computed from the same signal space that any labeling function uses as input (\\S\\ref{sec:feature_overlap}).\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\begin{tabular}{rlll}\n\\toprule\n\\textbf{\\#} & \\textbf{Feature} & \\textbf{Category} & \\textbf{LF Overlap} \\\\\n\\midrule\n1  & num\\_steps             & Trajectory stats    & --- \\\\\n2  & num\\_actions           & Trajectory stats    & --- \\\\\n3  & num\\_observations      & Trajectory stats    & --- \\\\\n4  & action\\_ratio          & Trajectory stats    & --- \\\\\n5  & mean\\_text\\_len        & Text statistics     & --- \\\\\n6  & std\\_text\\_len         & Text statistics     & --- \\\\\n7  & max\\_text\\_len         & Text statistics     & --- \\\\\n8  & min\\_text\\_len         & Text statistics     & --- \\\\\n9  & mean\\_action\\_len      & Text statistics     & --- \\\\\n10 & mean\\_obs\\_len         & Text statistics     & --- \\\\\n11 & text\\_len\\_trend       & Text statistics     & --- \\\\\n12 & num\\_commands          & Command stats       & --- \\\\\n13 & mean\\_cmd\\_len         & Command stats       & --- \\\\\n14 & max\\_cmd\\_len          & Command stats       & --- \\\\\n15 & unique\\_cmd\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n16 & max\\_repeat\\_ratio     & Repetition          & $\\lambda_1$ \\\\\n17 & num\\_edit\\_cmds        & File operations     & $\\lambda_2$ \\\\\n18 & num\\_search\\_cmds      & File operations     & $\\lambda_2$ \\\\\n19 & num\\_nav\\_cmds         & File operations     & --- \\\\\n20 & num\\_submit\\_cmds      & File operations     & --- \\\\\n21 & edit\\_ratio            & File operations     & $\\lambda_2$ \\\\\n22 & search\\_ratio          & File operations     & $\\lambda_2$ \\\\\n23 & avg\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n24 & max\\_adjacent\\_cmd\\_sim & Edit distance       & $\\lambda_1$ \\\\\n25 & max\\_consec\\_similar   & Edit distance       & $\\lambda_1$ \\\\\n26 & num\\_errors            & Output statistics   & --- \\\\\n27 & num\\_test\\_outputs     & Output statistics   & --- \\\\\n28 & num\\_file\\_displays    & Output statistics   & $\\lambda_2$ \\\\\n29 & num\\_nonzero\\_exits    & Output statistics   & --- \\\\\n30 & is\\_short\\_trajectory  & Trajectory stats    & $\\lambda_3$ \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Complete structural feature definitions ($N{=}30$). LF Overlap indicates which labeling function's signal space the feature shares: $\\lambda_1$ (command repetition), $\\lambda_2$ (file diff), $\\lambda_3$ (outcome backpropagation), or ``---'' (no overlap). 11 features overlap with at least one LF; 19 are residual.}\n\\label{tab:feature_defs}\n\\end{table*}\n\n%-------------------------------------------------------------------\n\\subsection{Instance Isolation}\n\\label{sec:app_instance_isolation}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Model} & \\textbf{Full} & \\textbf{Unseen-only} & \\textbf{$\\Delta$} \\\\\n\\midrule\nGB all & 0.9674 & 0.9669 & $-$0.05\\,pp \\\\\nRF all & 0.9123 & 0.9121 & $-$0.01\\,pp \\\\\nGB conf${\\geq}$2 & 0.9919 & 0.9917 & $-$0.02\\,pp \\\\\nRF conf${\\geq}$2 & 0.9959 & 0.9962 & $+$0.03\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Instance isolation: cross-coding-agent macro-F1 with and without 284 SWE-bench task instances that overlap between the 1,386 SWE-bench training instances and 3,409 OH test instances (8.3\\% of OH). All $|\\Delta| < 0.1$\\,pp, confirming transfer reflects behavioral pattern generalization rather than instance memorization.}\n\\label{tab:instance_isolation}\n\\end{table}\n\n%-------------------------------------------------------------------\n\\subsection{Extended LLM-as-Judge Evaluation}\n\\label{sec:llm_extended}\n\nTable~\\ref{tab:llm_extended} extends the zero-shot LLM-as-judge baseline (Table~\\ref{tab:main_results}) with chain-of-thought (CoT) prompting, few-shot examples, and an alternative model, all evaluated on the SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Model} & \\textbf{Setting} & \\textbf{Macro-F1} & \\textbf{F1\\textsubscript{stag}} & \\textbf{F1\\textsubscript{prog}} & \\textbf{Cost} \\\\\n\\midrule\nClaude Sonnet 4.6 & zero-shot & 0.6625 & 0.6055 & 0.7195 & \\$11.66 \\\\\nClaude Sonnet 4.6 & CoT & 0.7499 & 0.6808 & 0.8189 & \\$17.16 \\\\\nClaude Sonnet 4.6 & 5-shot & 0.7514 & 0.6828 & 0.8199 & \\$36.08 \\\\\nClaude Sonnet 4.6 & 5-shot-CoT & \\textbf{0.7994} & \\textbf{0.7306} & \\textbf{0.8681} & \\$40.56 \\\\\nGPT-5.5$^\\dagger$ & zero-shot & 0.7465 & 0.7110 & 0.7819 & \\$11.62 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\emph{Structural feature augmentation}} \\\\\nClaude Sonnet 4.6 & + structural input$^\\ddagger$ & 0.6880 & 0.6270 & 0.7490 & \\$14.82 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Extended LLM-as-judge evaluation on SWE-Agent conf${\\geq}$2 ($N{=}1{,}824$). All Claude rows use the same model; the performance gain comes from prompting strategy. CoT alone yields gains comparable to few-shot ($+$8.7\\,pp vs.\\ $+$8.9\\,pp over zero-shot); combining them (five-shot-CoT) adds a further 4.8\\,pp, suggesting complementary mechanisms. $^\\ddagger$30 structural features provided as formatted text in the LLM prompt; performance degrades below pure few-shot (0.751), indicating structural signals require engineered classifiers. $^\\dagger$GPT-5.5: 22.4\\% of responses (408/1,824) failed to parse; macro-F1 is computed over the 1,416 windows with valid outputs. The best LLM configuration (0.799 in-domain) trails structural cross-coding-agent transfer (0.967) by 16.8\\,pp. Total API cost across all configurations: \\$131.90.}\n\\label{tab:llm_extended}\n\\end{table}\n",
      "numLines": 193,
      "startLine": 1,
      "totalLines": 193
    }
  }
}
```

</details>

---
