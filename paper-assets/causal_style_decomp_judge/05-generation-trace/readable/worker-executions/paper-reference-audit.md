# paper reference audit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 104
- **Recorded user turns:** 0
- **Tool calls:** 39
- **Original source:** `logs/workers/worker_paper_reference-audit_20260522T010830.log`
- **Structured JSON:** [`c2676f923569235ff565.json`](../../sessions/c2/c2676f923569235ff565.json)

## Before a recorded user message

104 recorded events

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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
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
  "uuid": "4abc4a94-1632-4f6a-b4fe-e665e592edcb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-5-projects-causal-style-decomp-judge/memory/"
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
    "resetsAt": 1779933600,
    "rateLimitType": "seven_day",
    "utilization": 0.47,
    "isUsingOverage": false
  },
  "uuid": "850aa2ac-9f85-473d-b18b-04913da9b63f",
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9"
}
```

---

### Assistant

_source line 4_

I'll start by reading the bib file and scanning all tex files for citations, plus loading the reference-audit skill for best practices.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "de15b77e-67e8-4abe-adf9-fdc43c5ba948",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMyLuHphoukBWh73EwNARv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12707,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12707
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

<details open><summary>🔧 Tool call — Read · `toolu_01LPBetPeoXUZwofJSSNUCSs`</summary>

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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "90d39ed8-ad9e-4c7a-b4bc-fd013c3b6f08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMyLuHphoukBWh73EwNARv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12707,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12707
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

_source line 6 · 2026-05-22T01:08:42.760Z_

<details><summary>↩ Tool result · `toolu_01LPBetPeoXUZwofJSSNUCSs`</summary>

```text
1	@article{tripathi2025pairwise,
2	  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
3	  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
4	  journal={arXiv preprint arXiv:2504.14716},
5	  year={2025}
6	}
7	
8	@inproceedings{murugadoss2025sos,
9	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
10	  author={Murugadoss, Aakanksha and others},
11	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
12	  year={2025},
13	  url={https://arxiv.org/abs/2409.15268}
14	}
15	
16	@inproceedings{li2026preference,
17	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
18	  author={Li, Dawei and others},
19	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
20	  year={2026},
21	  url={https://arxiv.org/abs/2502.01534}
22	}
23	
24	@article{wang2026fairjudge,
25	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
26	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
27	  journal={arXiv preprint arXiv:2602.06625},
28	  year={2026},
29	  url={https://arxiv.org/abs/2602.06625}
30	}
31	
32	
33	@inproceedings{dubois2025lc,
34	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
35	  author={Dubois, Yann and others},
36	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
37	  year={2025},
38	  url={https://arxiv.org/abs/2404.04475}
39	}
40	
41	@article{casse2026concise,
42	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
43	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
44	  journal={arXiv preprint arXiv:2601.10809},
45	  year={2026},
46	  url={https://arxiv.org/abs/2601.10809}
47	}
48	
49	@article{counterfactual2025rhetorical,
50	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
51	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
52	  journal={arXiv preprint arXiv:2512.19908},
53	  year={2025},
54	  url={https://arxiv.org/abs/2512.19908}
55	}
56	
57	@article{soumik2026judging,
58	  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},
59	  author={Soumik, Mohammad and others},
60	  journal={arXiv preprint arXiv:2604.23178},
61	  year={2026},
62	  url={https://arxiv.org/abs/2604.23178}
63	}
64	
65	@inproceedings{reber2025rate,
66	  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},
67	  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},
68	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
69	  year={2025},
70	  url={https://arxiv.org/abs/2410.11348}
71	}
72	
73	@inproceedings{kiritchenko2017bws,
74	  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},
75	  author={Kiritchenko, Svetlana and Mohammad, Saif},
76	  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
77	  pages={465--470},
78	  year={2017},
79	  url={https://aclanthology.org/P17-2074/}
80	}
81	
82	@inproceedings{novikova2018rankme,
83	  title={{RankME}: Reliable Human Ratings for Natural Language Generation},
84	  author={Novikova, Jekaterina and Du{\v{s}}ek, Ond{\v{r}}ej and Rieser, Verena},
85	  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},
86	  year={2018},
87	  url={https://aclanthology.org/N18-2012/}
88	}
89	
90	@article{stevens1946theory,
91	  title={On the Theory of Scales of Measurement},
92	  author={Stevens, Stanley Smith},
93	  journal={Science},
94	  volume={103},
95	  number={2684},
96	  pages={677--680},
97	  year={1946}
98	}
99	
100	@article{thurstone1927law,
101	  title={A Law of Comparative Judgment},
102	  author={Thurstone, Louis Leon},
103	  journal={Psychological Review},
104	  volume={34},
105	  number={4},
106	  pages={273--286},
107	  year={1927}
108	}
109	
110	@article{decoster2011median,
111	  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},
112	  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},
113	  journal={Journal of Experimental Psychopathology},
114	  volume={2},
115	  number={2},
116	  pages={197--209},
117	  year={2011},
118	  doi={10.5127/jep.008310}
119	}
120	
121	@inproceedings{zheng2023judging,
122	  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
123	  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
124	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
125	  year={2023},
126	  url={https://arxiv.org/abs/2306.05685}
127	}
128	
129	@inproceedings{dubois2023alpacafarm,
130	  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},
131	  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},
132	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
133	  year={2023},
134	  url={https://arxiv.org/abs/2305.14387}
135	}
136	
137	@article{bradley1952rank,
138	  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},
139	  author={Bradley, Ralph Allan and Terry, Milton E.},
140	  journal={Biometrika},
141	  volume={39},
142	  number={3/4},
143	  pages={324--345},
144	  year={1952}
145	}
146	
147	@article{feinstein1990kappa,
148	  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},
149	  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},
150	  journal={Journal of Clinical Epidemiology},
151	  volume={43},
152	  number={6},
153	  pages={543--549},
154	  year={1990}
155	}
156	
157	
158	@article{wang2023faireval,
159	  title={Large Language Models are not Fair Evaluators},
160	  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},
161	  journal={arXiv preprint arXiv:2305.17926},
162	  year={2023},
163	  url={https://arxiv.org/abs/2305.17926}
164	}
165	
166	@article{li2024calibraeval,
167	  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},
168	  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},
169	  journal={arXiv preprint arXiv:2410.15393},
170	  year={2024},
171	  url={https://arxiv.org/abs/2410.15393}
172	}
173	
174	@article{hoenig2001abuse,
175	  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},
176	  author={Hoenig, John M. and Heisey, Dennis M.},
177	  journal={The American Statistician},
178	  volume={55},
179	  number={1},
180	  pages={19--24},
181	  year={2001}
182	}
183	
184	@inproceedings{zeng2023llmbar,
185	  title={Evaluating Large Language Models at Evaluating Instruction Following},
186	  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},
187	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
188	  year={2024},
189	  url={https://arxiv.org/abs/2310.07641}
190	}
191	
192	@inproceedings{veitch2020adapting,
193	  title={Adapting Text Embeddings for Causal Inference},
194	  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},
195	  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},
196	  year={2020},
197	  url={https://arxiv.org/abs/1905.12741}
198	}
199	
200	@inproceedings{tan2025judgebench,
201	  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},
202	  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},
203	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
204	  year={2025},
205	  url={https://arxiv.org/abs/2410.12784}
206	}
207	
208	@book{louviere2015bws,
209	  title={Best-Worst Scaling: Theory, Methods and Applications},
210	  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},
211	  publisher={Cambridge University Press},
212	  year={2015},
213	  isbn={9781107043152}
214	}
215	
216	@inproceedings{chiang2024chatbot,
217	  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},
218	  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
219	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
220	  year={2024},
221	  url={https://arxiv.org/abs/2403.04132}
222	}
223	
224	@article{hunter2004mm,
225	  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},
226	  author={Hunter, David R.},
227	  journal={The Annals of Statistics},
228	  volume={32},
229	  number={1},
230	  pages={384--406},
231	  year={2004},
232	  doi={10.1214/aos/1079120141}
233	}
234	
235	@article{ye2024justice,
236	  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},
237	  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},
238	  journal={arXiv preprint arXiv:2410.02736},
239	  year={2024},
240	  url={https://arxiv.org/abs/2410.02736}
241	}
242	
243	@article{feder2021causalm,
244	  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},
245	  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},
246	  journal={Computational Linguistics},
247	  volume={47},
248	  number={2},
249	  pages={333--386},
250	  year={2021},
251	  url={https://aclanthology.org/2021.cl-2.13/}
252	}
253	
254	@inproceedings{wu2021polyjuice,
255	  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},
256	  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},
257	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
258	  year={2021},
259	  url={https://aclanthology.org/2021.acl-long.523/}
260	}
261	
262	@inproceedings{clark2021human,
263	  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},
264	  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},
265	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
266	  pages={7282--7296},
267	  year={2021},
268	  url={https://aclanthology.org/2021.acl-long.565/}
269	}
270	
271	@inproceedings{amidei2019likert,
272	  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},
273	  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},
274	  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},
275	  year={2019},
276	  url={https://aclanthology.org/W19-8648/}
277	}
278	
279	@inproceedings{boubdir2023elo,
280	  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},
281	  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},
282	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
283	  year={2024},
284	  url={https://arxiv.org/abs/2311.17295}
285	}
286	
287	@inproceedings{wu2023style,
288	  title={Style Over Substance: Evaluation Biases for Large Language Models},
289	  author={Wu, Minghao and Aji, Alham Fikri},
290	  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},
291	  year={2025},
292	  url={https://aclanthology.org/2025.coling-main.21/}
293	}
294	
295	@inproceedings{liusie2024comparative,
296	  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},
297	  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},
298	  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
299	  pages={139--151},
300	  year={2024},
301	  url={https://aclanthology.org/2024.eacl-long.8/}
302	}
303	
304	@article{feder2022causal,
305	  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},
306	  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},
307	  journal={Transactions of the Association for Computational Linguistics},
308	  volume={10},
309	  pages={1138--1158},
310	  year={2022},
311	  url={https://aclanthology.org/2022.tacl-1.66/}
312	}
313	
314	@inproceedings{koo2024cobbler,
315	  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},
316	  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},
317	  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
318	  year={2024},
319	  url={https://aclanthology.org/2024.findings-acl.29/}
320	}
321	
322	@article{liang1986gee,
323	  title={Longitudinal Data Analysis Using Generalized Linear Models},
324	  author={Liang, Kung-Yee and Zeger, Scott L.},
325	  journal={Biometrika},
326	  volume={73},
327	  number={1},
328	  pages={13--22},
329	  year={1986},
330	  doi={10.1093/biomet/73.1.13}
331	}
332	
333	@article{krosnick1999survey,
334	  title={Survey Research},
335	  author={Krosnick, Jon A.},
336	  journal={Annual Review of Psychology},
337	  volume={50},
338	  number={1},
339	  pages={537--567},
340	  year={1999},
341	  doi={10.1146/annurev.psych.50.1.537}
342	}
343	
344	@article{lakens2017equivalence,
345	  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},
346	  author={Lakens, Dani{\"e}l},
347	  journal={Social Psychological and Personality Science},
348	  volume={8},
349	  number={4},
350	  pages={355--362},
351	  year={2017},
352	  doi={10.1177/1948550617697177}
353	}
354	
355	@article{preston2000scale,
356	  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},
357	  author={Preston, Carolyn C. and Colman, Andrew M.},
358	  journal={Acta Psychologica},
359	  volume={104},
360	  number={1},
361	  pages={1--15},
362	  year={2000},
363	  doi={10.1016/S0001-6918(99)00050-5}
364	}
365	
366	@inproceedings{vanderlee2019best,
367	  title={Best Practices for the Human Evaluation of Automatically Generated Text},
368	  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},
369	  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},
370	  pages={355--368},
371	  year={2019},
372	  url={https://aclanthology.org/W19-8643/}
373	}
374	
375	@article{vanderlee2021human,
376	  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},
377	  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},
378	  journal={Computer Speech \& Language},
379	  volume={67},
380	  pages={101151},
381	  year={2021},
382	  doi={10.1016/j.csl.2020.101151}
383	}
384	
385	@article{celikyilmaz2020evaluation,
386	  title={Evaluation of Text Generation: A Survey},
387	  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},
388	  journal={arXiv preprint arXiv:2006.14799},
389	  year={2020},
390	  url={https://arxiv.org/abs/2006.14799}
391	}
392	
393	@inproceedings{jeong2025comparative,
394	  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},
395	  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},
396	  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},
397	  pages={79--108},
398	  year={2025},
399	  url={https://aclanthology.org/2025.blackboxnlp-1.5}
400	}
401	
402	@article{stureborg2024inconsistent,
403	  title={Large Language Models are Inconsistent and Biased Evaluators},
404	  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},
405	  journal={arXiv preprint arXiv:2405.01724},
406	  year={2024},
407	  url={https://arxiv.org/abs/2405.01724}
408	}
409	
410	@inproceedings{park2024offsetbias,
411	  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},
412	  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},
413	  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},
414	  pages={1043--1067},
415	  year={2024},
416	  doi={10.18653/v1/2024.findings-emnlp.57},
417	  url={https://aclanthology.org/2024.findings-emnlp.57}
418	}
419	
420	@inproceedings{panickssery2024selfpreference,
421	  title={{LLM} Evaluators Recognize and Favor Their Own Generations},
422	  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},
423	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
424	  year={2024},
425	  url={https://arxiv.org/abs/2404.13076}
426	}
427	
428	@inproceedings{chen2024humans,
429	  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},
430	  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},
431	  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
432	  year={2024},
433	  url={https://aclanthology.org/2024.emnlp-main.474/}
434	}
435	
436	@article{he2021debertav3,
437	  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},
438	  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
439	  journal={arXiv preprint arXiv:2111.09543},
440	  year={2021},
441	  url={https://arxiv.org/abs/2111.09543}
442	}
443	
444	@article{shi2024judging,
445	  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},
446	  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},
447	  journal={arXiv preprint arXiv:2406.07791},
448	  year={2024},
449	  url={https://arxiv.org/abs/2406.07791}
450	}
451	
452	@inproceedings{bavaresco2025llms,
453	  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},
454	  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},
455	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
456	  year={2025},
457	  url={https://aclanthology.org/2025.acl-short.20/}
458	}
459	
460	@inproceedings{saito2023verbosity,
461	  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},
462	  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},
463	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
464	  year={2023},
465	  url={https://aclanthology.org/2023.emnlp-main.665/}
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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "61c0e849-9001-41b0-9c15-fa84bb3f3471",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
      "content": "@article{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  journal={arXiv preprint arXiv:2504.14716},\n  year={2025}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@article{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  journal={arXiv preprint arXiv:2305.17926},\n  year={2023},\n  url={https://arxiv.org/abs/2305.17926}\n}\n\n@article{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  journal={arXiv preprint arXiv:2410.15393},\n  year={2024},\n  url={https://arxiv.org/abs/2410.15393}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
      "numLines": 467,
      "startLine": 1,
      "totalLines": 467
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tc2WsnGXeoTDvi6GAiXQz2`</summary>

```json
{
  "pattern": "docs/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0dd652b9-12c3-4404-982c-aa916c009aa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMyLuHphoukBWh73EwNARv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12707,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12707
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

_source line 8 · 2026-05-22T01:08:43.813Z_

<details><summary>↩ Tool result · `toolu_01Tc2WsnGXeoTDvi6GAiXQz2`</summary>

```text
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "6554f282-daf1-4046-bf69-722f4e5889ad",
  "tool_use_result": {
    "filenames": [
      "docs/paper/main.tex"
    ],
    "durationMs": 51,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01Fc57XbuyB66SJZM8BWFcGa`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "7d945e6f-e20a-49d0-9113-52759874784a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HMyLuHphoukBWh73EwNARv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12707,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12707
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

_source line 10 · 2026-05-22T01:08:43.931Z_

<details><summary>↩ Tool result · `toolu_01Fc57XbuyB66SJZM8BWFcGa`</summary>

````text
1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
89	
90	## 常见引用问题模式
91	
92	| 问题类型 | 特征 | 风险 |
93	|---------|------|------|
94	| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |
95	| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |
96	| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |
97	| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |
98	| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |
99	
100	## 输出格式
101	
102	审计完成后，生成结构化报告：
103	
104	```
105	## 引用审计报告
106	
107	**总数**: X 条引用
108	**已验证**: Y 条（OpenAlex confirmed）
109	**问题**: Z 条
110	
111	### 问题列表
112	
113	1. [severity: critical] `\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用
114	   - 建议：删除或替换为已验证的替代引用
115	
116	2. [severity: warning] `\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）
117	   - 建议：更新为正确年份
118	
119	3. [severity: info] `\cite{zzz}` — bib 中存在但正文未引用
120	   - 建议：删除或在相关段落补充引用
121	```
122	
123	## 设计参考
124	
125	本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。
126	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "2b13bb15-d8e4-49ce-a8c0-4c61b0b2ad76",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md",
      "content": "---\nname: reference-audit\ndescription: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。\nscope: global\ntags:\n- workflow\n- submission\n- writing\n- quality\npriority: 6\nversion: 2\nroles:\n- agent\n- paper_agent\n- review_reviewer\n- worker\n---\n\n# 引用验证与审计（Reference Audit）\n\n## 核心原则\n\n**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。\n\n## 触发条件\n\n- 写论文时添加引用\n- Review Reviewer 审查论文引用质量\n- 提交前最终检查\n- 发现可疑引用（年份不对、作者不存在、找不到原文）\n\n## 验证流程\n\n### 1. 单条引用验证（写论文时）\n\n每次需要引用时：\n\n1. **WebSearch 查找**：搜索论文标题 + 第一作者\n2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`\n3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue\n4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式\n5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中\n\n### 2. 全文引用审计（批量检查）\n\n**Step 1：调用 `verify_references(paper_dir)`**\n\n这是首选方式。该工具自动完成：\n- 解析所有 .bib 文件，提取结构化条目\n- 解析所有 .tex 文件，提取 `\\cite{}`/`\\citep{}`/`\\citet{}` 引用\n- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）\n- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）\n\n如果只需快速离线检查，传 `skip_online=True`。\n\n**Step 2：人工复核工具报告中的问题条目**\n\n重点关注：\n- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证\n- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本\n- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错\n- `orphan_bib` — .bib 中有但正文未引用，清理或补引用\n\n**Step 3：语义验证**（优先级排序）\n1. 首先验证 Introduction 和 Related Work 中的高频引用\n2. 然后验证 Method 中支撑技术 claim 的引用\n3. 最后验证其余引用\n\n对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。\n\n### 3. 验证失败处理\n\n**找不到论文时**：\n1. 检查拼写——标题或作者名是否有误？\n2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）\n3. 标记为 `[CITATION NEEDED]`\n4. 明确告知——说明哪条引用无法验证\n\n**信息不匹配时**：\n1. 确认是否找对了论文\n2. 检查版本——preprint vs published 版本\n3. 用最准确的版本更新信息\n\n**绝不做的事**：\n- 从记忆生成 BibTeX——AI 生成引用 40% 错误率\n- 跳过验证步骤\n- 假设论文存在\n- 对无法验证的引用不做标记\n\n## 常见引用问题模式\n\n| 问题类型 | 特征 | 风险 |\n|---------|------|------|\n| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |\n| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |\n| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |\n| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |\n| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |\n\n## 输出格式\n\n审计完成后，生成结构化报告：\n\n```\n## 引用审计报告\n\n**总数**: X 条引用\n**已验证**: Y 条（OpenAlex confirmed）\n**问题**: Z 条\n\n### 问题列表\n\n1. [severity: critical] `\\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用\n   - 建议：删除或替换为已验证的替代引用\n\n2. [severity: warning] `\\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）\n   - 建议：更新为正确年份\n\n3. [severity: info] `\\cite{zzz}` — bib 中存在但正文未引用\n   - 建议：删除或在相关段落补充引用\n```\n\n## 设计参考\n\n本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  }
}
````

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:
1. Read all tex files to extract citation keys
2. Check for Tripathi references
3. Analyze the bib file for completeness issues

Let me read the main.tex file and extract all citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "ee71457d-6d46-41f9-acd4-92310ef27251",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t4u6BiMJt5GEPegYDQNze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10170,
      "cache_read_input_tokens": 24154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10170
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

Now let me read the main.tex file to extract all citation keys, and search for any additional tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "af6462c5-6556-4b72-aa26-bccf4c236468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t4u6BiMJt5GEPegYDQNze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10170,
      "cache_read_input_tokens": 24154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10170
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

<details open><summary>🔧 Tool call — Read · `toolu_01AfKQoZSjA9F5YNpxHU8drB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "b2e5a92e-f53f-4074-b542-343b3cd75a6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t4u6BiMJt5GEPegYDQNze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10170,
      "cache_read_input_tokens": 24154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10170
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

_source line 14 · 2026-05-22T01:08:51.336Z_

<details><summary>↩ Tool result · `toolu_01AfKQoZSjA9F5YNpxHU8drB`</summary>

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
10	% \usepackage{inconsolata} % unavailable locally; re-enable for submission
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath,amssymb}
14	\usepackage{xcolor}
15	\usepackage{subcaption}
16	\usepackage{tikz}
17	\usetikzlibrary{arrows.meta,positioning}
18	
19	\title{The Likert Blindspot: Detecting Hidden Style Bias\\in LLM Judges via Controlled Style Decomposition}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\input{sections/abstract}
27	
28	\input{sections/introduction}
29	
30	\input{sections/related_work}
31	
32	\input{sections/method}
33	
34	\input{sections/experiments}
35	
36	\input{sections/conclusion}
37	
38	\section*{Limitations}
39	\label{sec:limitations}
40	
41	\paragraph{Quality--style confounding and construct validity.}
42	The NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.
43	Although the formality effect survives logistic adjustment for original preference ($\text{OR} = 2.32$, $p = 0.006$; Appendix~\ref{app:direction}), residual confounding is not fully eliminated.
44	An alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\S\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.
45	
46	\paragraph{Evaluator-producer bias and generalizability.}
47	Qwen3-32B serves as both rewriter and judge, raising self-preference concerns \citep{panickssery2024selfpreference}; an independent GPT-4o rewriter bounds this to a 22\% Style OR reduction (Appendix~\ref{app:rewriter_indep}).
48	GPT-4o, Llama-3.3-70B, and Gemini-2.5-Flash use a separate rewriter and are not subject to evaluator-producer overlap; all three independently confirm the Blindspot across four architectures, though cross-judge effect-size comparisons are not valid.
49	Register results carry the highest evaluator-producer risk---all register rewrites use the same Qwen3-32B rewriter without the cross-rewriter validation applied to formality and verbosity---and register conclusions remain tentative pending independent rewriter validation.
50	All experiments use LLMBar ($n = 100$); additional axes, larger benchmarks, and further judges are needed.
51	A fourth axis---tone (assertive vs.\ hedging)---was explored but abandoned: epistemic commitment changes caused the NLI gate to correctly reject most counterfactuals (pass rate ${<}50\%$), confirming that the quality gate prevents content-altering manipulations from entering the pipeline.
52	Our per-axis decomposition treats each style axis independently; in practice, axes may interact (e.g., formality shifts may co-vary with register), and such confounds are not isolated by the current design.
53	
54	\paragraph{Validation methodology and scale design.}
55	NLI validation uses Qwen3-32B as annotator (GPT-4o cross-validation on all 200 pairs confirms 92.1\% formality / 82.6\% verbosity pass precision); human evaluation of both original and rewritten texts would strengthen content-preservation claims.
56	A 100-point continuous scale does not resolve the Blindspot (Appendix~\ref{app:likert100}), suggesting the gap reflects measurement mode rather than granularity \citep{preston2000scale}; equivalence testing \citep{lakens2017equivalence} could formalize whether the Likert effect size is practically zero.
57	
58	\section*{Code and Data}
59	Code and data will be released upon acceptance.
60	
61	\input{sections/appendix}
62	
63	\bibliography{references}
64	
65	\end{document}
66	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "1ed1a09b-44e2-43ad-8759-c678698232ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n% \\usepackage{inconsolata} % unavailable locally; re-enable for submission\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath,amssymb}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{tikz}\n\\usetikzlibrary{arrows.meta,positioning}\n\n\\title{The Likert Blindspot: Detecting Hidden Style Bias\\\\in LLM Judges via Controlled Style Decomposition}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\n\\input{sections/introduction}\n\n\\input{sections/related_work}\n\n\\input{sections/method}\n\n\\input{sections/experiments}\n\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Quality--style confounding and construct validity.}\nThe NLI gate blocks content changes but cannot block quality perception shifts mediated by style itself---a fundamental identifiability limit of text-rewriting approaches.\nAlthough the formality effect survives logistic adjustment for original preference ($\\text{OR} = 2.32$, $p = 0.006$; Appendix~\\ref{app:direction}), residual confounding is not fully eliminated.\nAn alternative interpretation of the Blindspot is that Likert and pairwise modes measure different constructs: Likert captures absolute quality difference while pairwise captures ordinal preference. Under this view, the divergence reflects construct difference rather than measurement failure. The Comparative Trap \\citep{jeong2025comparative} lends support to this alternative; six experimental controls bound this risk (\\S\\ref{sec:amplification}), though definitive separation would require human ground-truth ratings.\n\n\\paragraph{Evaluator-producer bias and generalizability.}\nQwen3-32B serves as both rewriter and judge, raising self-preference concerns \\citep{panickssery2024selfpreference}; an independent GPT-4o rewriter bounds this to a 22\\% Style OR reduction (Appendix~\\ref{app:rewriter_indep}).\nGPT-4o, Llama-3.3-70B, and Gemini-2.5-Flash use a separate rewriter and are not subject to evaluator-producer overlap; all three independently confirm the Blindspot across four architectures, though cross-judge effect-size comparisons are not valid.\nRegister results carry the highest evaluator-producer risk---all register rewrites use the same Qwen3-32B rewriter without the cross-rewriter validation applied to formality and verbosity---and register conclusions remain tentative pending independent rewriter validation.\nAll experiments use LLMBar ($n = 100$); additional axes, larger benchmarks, and further judges are needed.\nA fourth axis---tone (assertive vs.\\ hedging)---was explored but abandoned: epistemic commitment changes caused the NLI gate to correctly reject most counterfactuals (pass rate ${<}50\\%$), confirming that the quality gate prevents content-altering manipulations from entering the pipeline.\nOur per-axis decomposition treats each style axis independently; in practice, axes may interact (e.g., formality shifts may co-vary with register), and such confounds are not isolated by the current design.\n\n\\paragraph{Validation methodology and scale design.}\nNLI validation uses Qwen3-32B as annotator (GPT-4o cross-validation on all 200 pairs confirms 92.1\\% formality / 82.6\\% verbosity pass precision); human evaluation of both original and rewritten texts would strengthen content-preservation claims.\nA 100-point continuous scale does not resolve the Blindspot (Appendix~\\ref{app:likert100}), suggesting the gap reflects measurement mode rather than granularity \\citep{preston2000scale}; equivalence testing \\citep{lakens2017equivalence} could formalize whether the Likert effect size is practically zero.\n\n\\section*{Code and Data}\nCode and data will be released upon acceptance.\n\n\\input{sections/appendix}\n\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01JrWnrGSEkoLZsiRCMZVs8j`</summary>

```json
{
  "pattern": "docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "be841a02-6453-4fc4-a722-b4221256ebea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016t4u6BiMJt5GEPegYDQNze",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10170,
      "cache_read_input_tokens": 24154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10170
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

_source line 16 · 2026-05-22T01:08:51.821Z_

<details><summary>↩ Tool result · `toolu_01JrWnrGSEkoLZsiRCMZVs8j`</summary>

```text
docs/paper/sections/related_work.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
docs/paper/sections/abstract.tex
docs/paper/main.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "a0100f45-206a-4267-be91-7a65b5931531",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/main.tex"
    ],
    "durationMs": 82,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
I need to read all the section tex files to extract all citation keys. Let me do this in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "571a3ee4-9c78-4033-9fed-10d66a278e8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

Let me read all the section files to extract citations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "9f808c58-a4d3-47f9-8ef3-0e022b4741cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Dj1mUbkLeRNjGP8AQedssh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0e90eda2-0c51-4a19-891c-9a824e47847a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 20 · 2026-05-22T01:08:59.511Z_

<details><summary>↩ Tool result · `toolu_01Dj1mUbkLeRNjGP8AQedssh`</summary>

```text
1	\begin{abstract}
2	LLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.
3	We introduce Controlled Style Decomposition (CSD), a unified framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.
4	Across four target judges, one negative control, three benchmarks, and three style axes, CSD demonstrates the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects, following a severity spectrum from complete attenuation at moderate bias to over 60\% signal loss at stronger effects, confirmed by seven statistical methods.
5	GEE conditional decomposition reveals a per-axis confound structure consistent across all four target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality, and register is judge-dependent---determining which estimates are directly interpretable and which require conditional analysis.
6	A negative-control judge shows no detectable bias on either primary axis, supporting discriminative validity.
7	Whether measurement attenuation or construct divergence, the operational conclusion is the same: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "4ec32f79-1c85-4e6f-9692-ddcf4e11d6a6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nLLM judges are widely deployed for evaluation and alignment, yet style features alone explain judge scores with near-perfect correlation.\nWe introduce Controlled Style Decomposition (CSD), a unified framework combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison to systematically quantify style bias in LLM judges.\nAcross four target judges, one negative control, three benchmarks, and three style axes, CSD demonstrates the Likert Blindspot: Likert scoring systematically misses style biases that pairwise comparison detects, following a severity spectrum from complete attenuation at moderate bias to over 60\\% signal loss at stronger effects, confirmed by seven statistical methods.\nGEE conditional decomposition reveals a per-axis confound structure consistent across all four target judges: verbosity bias is style-dominated, formality exhibits a conditional effect moderated by content quality, and register is judge-dependent---determining which estimates are directly interpretable and which require conditional analysis.\nA negative-control judge shows no detectable bias on either primary axis, supporting discriminative validity.\nWhether measurement attenuation or construct divergence, the operational conclusion is the same: Likert-only evaluation systematically misses style-driven preferences that propagate through pairwise-based alignment pipelines.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_015yrm2ZSqLg3GXaqFbZGoza`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "c9eb06b4-611d-4c9c-8698-9702c3413935",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 22 · 2026-05-22T01:09:00.426Z_

<details><summary>↩ Tool result · `toolu_015yrm2ZSqLg3GXaqFbZGoza`</summary>

```text
1	\section{Introduction}
2	
3	\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \emph{higher} on a 1--10 Likert scale (8 vs.\ 5), yet consistently selects the formal variant in pairwise comparison.
4	Same judge, same texts, opposite conclusions.
5	This is the \emph{Likert Blindspot}.
6	
7	LLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.
8	Style features alone explain most of the variance in judge scores \citep{murugadoss2025sos}: 76--92\% of observed preferences originate from surface-level style cues \citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \citep{soumik2026judging}.
9	Despite this consensus, existing approaches each address individual requirements---multi-dimensional style analysis \citep{casse2026concise,wang2026fairjudge}, interventional design \citep{reber2025rate}, population-level correction \citep{dubois2025lc}---but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.
10	A further concern: standard Likert scoring produces ${\sim}60\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \citep{thurstone1927law} but previously unquantified for LLM judges.
11	
12	We propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.
13	Inspired by interventional text analysis \citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice comparison.
14	CSD requires no access to judge internals and applies post-hoc to any black-box judge.
15	Our experiments reveal the \emph{Likert Blindspot} across four target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash), one negative control (Claude Sonnet 4), three benchmarks, and two primary style axes, with exploratory register evidence.
16	On formality data, Likert yields non-significant ATE ($p = 0.332$, $0.908$), while BT detects 63.0\% (GPT-4o, $p = 0.0004$) and 66.5\% (Qwen3-32B, $p < 0.0001$) formal preferences; verbosity shows 77.3\% BT ($p < 0.0001$) invisible to Likert ($p = 0.179$; Figure~\ref{fig:forest_plot}).
17	
18	Our contributions:
19	\begin{itemize}
20	    \item \textbf{A black-box controlled framework} for per-axis style bias detection via style-controlled rewriting and position-controlled pairwise comparison (\S\ref{sec:method}).
21	    \item \textbf{The Likert Blindspot:} Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ attenuation at stronger effects---across six judge$\times$axis configurations ($p < 0.001$ pairwise vs.\ $p > 0.17$ Likert), confirmed by seven statistical methods (Tables~\ref{tab:main_results}--\ref{tab:sensitivity}).
22	    \item \textbf{Per-axis confound structure:} GEE decomposition shows verbosity is style-dominated (Style OR $8$--$13$, Orig OR ${<}1$), formality conditional, register judge-dependent---determining which estimates require conditional analysis (Table~\ref{tab:gee}).
23	    \item \textbf{Practical implications:} audits require pairwise comparison \emph{and} per-axis decomposition; Likert-based findings may systematically underestimate bias (\S\ref{sec:conclusion}).
24	\end{itemize}
25	
26	\begin{figure}[t]
27	\centering
28	\includegraphics[width=\columnwidth]{figures/pipeline_diagram.pdf}
29	\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}
30	\label{fig:pipeline}
31	\end{figure}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "4cdf80ec-438e-409f-9736-4621cc2ab19d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\n\\emph{``What is the average height for a male?''} --- given a formal and a casual answer with verified identical content (NLI entailment $= 0.993$), GPT-4o rates the casual variant \\emph{higher} on a 1--10 Likert scale (8 vs.\\ 5), yet consistently selects the formal variant in pairwise comparison.\nSame judge, same texts, opposite conclusions.\nThis is the \\emph{Likert Blindspot}.\n\nLLM judges are central infrastructure for NLP evaluation and alignment training (RLHF, DPO), where judge preferences serve as reward signals; any systematic bias propagates through both evaluation leaderboards and model development pipelines.\nStyle features alone explain most of the variance in judge scores \\citep{murugadoss2025sos}: 76--92\\% of observed preferences originate from surface-level style cues \\citep{li2026preference}, with bias scores of 0.76--0.92 across five judges \\citep{soumik2026judging}.\nDespite this consensus, existing approaches each address individual requirements---multi-dimensional style analysis \\citep{casse2026concise,wang2026fairjudge}, interventional design \\citep{reber2025rate}, population-level correction \\citep{dubois2025lc}---but no single framework integrates per-axis decomposition, interventional identification, per-instance diagnostics, and black-box applicability.\nA further concern: standard Likert scoring produces ${\\sim}60\\%$ uninformative ties, and even non-tied pairs carry weaker signal than pairwise comparison---a limitation predicted by measurement theory \\citep{thurstone1927law} but previously unquantified for LLM judges.\n\nWe propose Controlled Style Decomposition (CSD), combining NLI-gated content control, per-axis style decomposition, and position-controlled pairwise comparison.\nInspired by interventional text analysis \\citep{veitch2020adapting}, CSD operates in three stages: style-controlled rewriting along a single axis, NLI entailment verification, and bias measurement via forced-choice comparison.\nCSD requires no access to judge internals and applies post-hoc to any black-box judge.\nOur experiments reveal the \\emph{Likert Blindspot} across four target judges (GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash), one negative control (Claude Sonnet 4), three benchmarks, and two primary style axes, with exploratory register evidence.\nOn formality data, Likert yields non-significant ATE ($p = 0.332$, $0.908$), while BT detects 63.0\\% (GPT-4o, $p = 0.0004$) and 66.5\\% (Qwen3-32B, $p < 0.0001$) formal preferences; verbosity shows 77.3\\% BT ($p < 0.0001$) invisible to Likert ($p = 0.179$; Figure~\\ref{fig:forest_plot}).\n\nOur contributions:\n\\begin{itemize}\n    \\item \\textbf{A black-box controlled framework} for per-axis style bias detection via style-controlled rewriting and position-controlled pairwise comparison (\\S\\ref{sec:method}).\n    \\item \\textbf{The Likert Blindspot:} Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \\to 0$ at $n = 355$), ${>}60\\%$ attenuation at stronger effects---across six judge$\\times$axis configurations ($p < 0.001$ pairwise vs.\\ $p > 0.17$ Likert), confirmed by seven statistical methods (Tables~\\ref{tab:main_results}--\\ref{tab:sensitivity}).\n    \\item \\textbf{Per-axis confound structure:} GEE decomposition shows verbosity is style-dominated (Style OR $8$--$13$, Orig OR ${<}1$), formality conditional, register judge-dependent---determining which estimates require conditional analysis (Table~\\ref{tab:gee}).\n    \\item \\textbf{Practical implications:} audits require pairwise comparison \\emph{and} per-axis decomposition; Likert-based findings may systematically underestimate bias (\\S\\ref{sec:conclusion}).\n\\end{itemize}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/pipeline_diagram.pdf}\n\\caption{CSD pipeline overview. Numbers indicate sample attrition at each stage.}\n\\label{fig:pipeline}\n\\end{figure}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01A2QsPLNj4rpR2nTbTHY3sb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "6a6735dd-db71-4130-bfe5-f98c89d28154",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 24 · 2026-05-22T01:09:00.974Z_

<details><summary>↩ Tool result · `toolu_01A2QsPLNj4rpR2nTbTHY3sb`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	Two lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.
5	
6	\paragraph{Interventional Approaches to Judge Bias}
7	Text-based interventional methods have a growing methodological foundation \citep{feder2021causalm,wu2021polyjuice,feder2022causal}.
8	\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).
9	RATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.
10	If this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.
11	CSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.
12	\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.
13	Their framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.
14	
15	\paragraph{Measurement Sensitivity in NLG Evaluation}
16	The distinction between ordinal and interval measurement dates to \citet{stevens1946theory}, whose taxonomy of scales remains foundational.
17	The superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since \citet{thurstone1927law}, whose Law of Comparative Judgment formalizes why forced-choice comparisons yield finer discriminability than absolute ratings.
18	\citet{preston2000scale} show that scale granularity affects reliability, while \citet{krosnick1999survey} documents satisficing behavior that may compound the tie inflation we observe.
19	\citet{decoster2011median} show that artificial categorization of continuous variables discards variance and reduces statistical power, directly relevant to the Likert Blindspot mechanism.
20	Within NLP, \citet{amidei2019likert} review the use of rating and Likert scales in NLG evaluation, identifying inconsistencies in scale design and reporting that compromise cross-study comparability.
21	\citet{clark2021human} demonstrate systematic flaws in human evaluation; \citet{celikyilmaz2020evaluation} survey evaluation methods, and \citet{vanderlee2019best,vanderlee2021human} establish best practices for human NLG evaluation.
22	\citet{kiritchenko2017bws} and \citet{novikova2018rankme} confirm that forced-choice methods (best-worst scaling, ranking) detect quality differences that rating scales miss; \citet{louviere2015bws} provide the theoretical foundation.
23	Our contribution provides a systematic quantification of this gap for LLM judge style bias via controlled per-axis style decomposition, identifying the two-layer mechanism (tie inflation plus residual signal attenuation) that explains it.
24	
25	\paragraph{Style Bias Detection and Mitigation}
26	The foundational LLM-as-judge framework was established by \citet{zheng2023judging}, who introduced MT-Bench and Chatbot Arena and documented position bias in pairwise evaluation.
27	\citet{wang2023faireval} further showed that preference rankings can be manipulated by swapping option order, proposing a win/tie/lose annotation scheme, and \citet{shi2024judging} systematically study position bias across 15 judges, showing it varies by model and quality gap.
28	\citet{li2024calibraeval} address selection bias through calibration of prediction distributions during inference.
29	These works focus on \emph{position} bias and calibration; \citet{ye2024justice} systematically quantify 12 bias types using automated counterfactual modifications, and \citet{koo2024cobbler} benchmark cognitive biases in LLM evaluators, though neither provides per-axis isolation of individual style effects.
30	Style bias as a separate, dominant bias source has received attention only recently \citep{wu2023style,murugadoss2025sos,li2026preference,soumik2026judging}; \citet{saito2023verbosity} specifically quantify verbosity bias in multi-turn chatbot evaluation, and \citet{chen2024humans} compare human and LLM judge biases, finding partially overlapping but distinct bias profiles; \citet{bavaresco2025llms} show that LLM--human agreement varies substantially across tasks.
31	\citet{li2026preference} further show that style-mediated \emph{preference leakage} propagates through the evaluation pipeline, motivating per-axis isolation of style effects.
32	\citet{tan2025judgebench} provide JudgeBench, a benchmark revealing that even strong judges perform near chance on challenging pairs, underscoring the need for controlled experimental designs rather than aggregate accuracy metrics.
33	Multi-feature frameworks such as CASSE \citep{casse2026concise} and FairJudge \citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses without interventional controls.
34	\citet{stureborg2024inconsistent} demonstrate inconsistency and bias across evaluation formats, and \citet{park2024offsetbias} show that verbosity and other surface features systematically inflate judge scores.
35	Crucially, \citet{jeong2025comparative} identify the Comparative Trap: pairwise comparison amplifies style biases relative to pointwise scoring, raising the concern that our pairwise-based detection may partly reflect format-level amplification rather than pure detection.
36	We address this directly in \S\ref{sec:amplification}.
37	
38	\paragraph{Bradley-Terry Models in Evaluation}
39	The Bradley-Terry model \citep{bradley1952rank} underpins Chatbot Arena \citep{zheng2023judging,chiang2024chatbot} and AlpacaFarm \citep{dubois2023alpacafarm}; \citet{boubdir2023elo} establish best practices, and \citet{liusie2024comparative} show zero-shot LLM pairwise comparison matches pointwise evaluation.
40	We adopt BT because it uses all comparison data including inconsistent pairs, yielding proper effect-size CIs; our contribution is to measure the Likert--pairwise sensitivity gap for style bias and show that per-axis GEE decomposition reveals confound structures invisible to aggregate scores.
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "7c092c8c-3e63-421b-9387-68a4affc41d6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\nTwo lines of work motivate our approach: interventional methods for diagnosing judge bias, and measurement theory on the sensitivity of different elicitation formats.\n\n\\paragraph{Interventional Approaches to Judge Bias}\nText-based interventional methods have a growing methodological foundation \\citep{feder2021causalm,wu2021polyjuice,feder2022causal}.\n\\citet{reber2025rate} propose RATE, a framework that rewrites model outputs along style attributes using imperfect counterfactuals and measures the causal effect on reward model scores via Likert-scale Average Treatment Effect (ATE).\nRATE applies a correction term to account for rewriting imperfections, but its reliance on Likert ATE as the primary metric is a vulnerability: our experiments show that Likert scoring exhibits a ceiling effect in which 60\\% of style-transformed pairs receive identical integer scores, yielding non-significant ATE estimates ($p = 0.332$) for the same interventions that pairwise comparison detects at $p = 0.006$.\nIf this Likert Blindspot generalizes beyond our setting, RATE's own style-related findings may underestimate the true magnitude of attribute effects.\nCSD differs from RATE in three respects: it targets individual style axes rather than general attributes, it measures bias through position-controlled pairwise comparison rather than Likert ATE, and it enforces content preservation via NLI entailment gating rather than post-hoc correction for imperfect rewrites.\n\\citet{counterfactual2025rhetorical} also adopt an interventional LLM-based design, rewriting texts to measure rhetorical style effects and aggregating preferences with a Bradley-Terry model.\nTheir framework operates at persona-level granularity (e.g., ``writes like a professor''), whereas CSD intervenes on specific style axes (e.g., formality, conciseness) and uses a sign test with position control rather than parametric aggregation.\n\n\\paragraph{Measurement Sensitivity in NLG Evaluation}\nThe distinction between ordinal and interval measurement dates to \\citet{stevens1946theory}, whose taxonomy of scales remains foundational.\nThe superiority of pairwise comparison over rating scales for eliciting reliable human judgments has been established since \\citet{thurstone1927law}, whose Law of Comparative Judgment formalizes why forced-choice comparisons yield finer discriminability than absolute ratings.\n\\citet{preston2000scale} show that scale granularity affects reliability, while \\citet{krosnick1999survey} documents satisficing behavior that may compound the tie inflation we observe.\n\\citet{decoster2011median} show that artificial categorization of continuous variables discards variance and reduces statistical power, directly relevant to the Likert Blindspot mechanism.\nWithin NLP, \\citet{amidei2019likert} review the use of rating and Likert scales in NLG evaluation, identifying inconsistencies in scale design and reporting that compromise cross-study comparability.\n\\citet{clark2021human} demonstrate systematic flaws in human evaluation; \\citet{celikyilmaz2020evaluation} survey evaluation methods, and \\citet{vanderlee2019best,vanderlee2021human} establish best practices for human NLG evaluation.\n\\citet{kiritchenko2017bws} and \\citet{novikova2018rankme} confirm that forced-choice methods (best-worst scaling, ranking) detect quality differences that rating scales miss; \\citet{louviere2015bws} provide the theoretical foundation.\nOur contribution provides a systematic quantification of this gap for LLM judge style bias via controlled per-axis style decomposition, identifying the two-layer mechanism (tie inflation plus residual signal attenuation) that explains it.\n\n\\paragraph{Style Bias Detection and Mitigation}\nThe foundational LLM-as-judge framework was established by \\citet{zheng2023judging}, who introduced MT-Bench and Chatbot Arena and documented position bias in pairwise evaluation.\n\\citet{wang2023faireval} further showed that preference rankings can be manipulated by swapping option order, proposing a win/tie/lose annotation scheme, and \\citet{shi2024judging} systematically study position bias across 15 judges, showing it varies by model and quality gap.\n\\citet{li2024calibraeval} address selection bias through calibration of prediction distributions during inference.\nThese works focus on \\emph{position} bias and calibration; \\citet{ye2024justice} systematically quantify 12 bias types using automated counterfactual modifications, and \\citet{koo2024cobbler} benchmark cognitive biases in LLM evaluators, though neither provides per-axis isolation of individual style effects.\nStyle bias as a separate, dominant bias source has received attention only recently \\citep{wu2023style,murugadoss2025sos,li2026preference,soumik2026judging}; \\citet{saito2023verbosity} specifically quantify verbosity bias in multi-turn chatbot evaluation, and \\citet{chen2024humans} compare human and LLM judge biases, finding partially overlapping but distinct bias profiles; \\citet{bavaresco2025llms} show that LLM--human agreement varies substantially across tasks.\n\\citet{li2026preference} further show that style-mediated \\emph{preference leakage} propagates through the evaluation pipeline, motivating per-axis isolation of style effects.\n\\citet{tan2025judgebench} provide JudgeBench, a benchmark revealing that even strong judges perform near chance on challenging pairs, underscoring the need for controlled experimental designs rather than aggregate accuracy metrics.\nMulti-feature frameworks such as CASSE \\citep{casse2026concise} and FairJudge \\citep{wang2026fairjudge} decompose style into finer dimensions but rely on correlational analyses without interventional controls.\n\\citet{stureborg2024inconsistent} demonstrate inconsistency and bias across evaluation formats, and \\citet{park2024offsetbias} show that verbosity and other surface features systematically inflate judge scores.\nCrucially, \\citet{jeong2025comparative} identify the Comparative Trap: pairwise comparison amplifies style biases relative to pointwise scoring, raising the concern that our pairwise-based detection may partly reflect format-level amplification rather than pure detection.\nWe address this directly in \\S\\ref{sec:amplification}.\n\n\\paragraph{Bradley-Terry Models in Evaluation}\nThe Bradley-Terry model \\citep{bradley1952rank} underpins Chatbot Arena \\citep{zheng2023judging,chiang2024chatbot} and AlpacaFarm \\citep{dubois2023alpacafarm}; \\citet{boubdir2023elo} establish best practices, and \\citet{liusie2024comparative} show zero-shot LLM pairwise comparison matches pointwise evaluation.\nWe adopt BT because it uses all comparison data including inconsistent pairs, yielding proper effect-size CIs; our contribution is to measure the Likert--pairwise sensitivity gap for style bias and show that per-axis GEE decomposition reveals confound structures invisible to aggregate scores.\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01SN4RgJtoHeUULRxmUBpFuK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "90c0de24-225e-4892-85a1-3102cea83471",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 26 · 2026-05-22T01:09:01.297Z_

<details><summary>↩ Tool result · `toolu_01SN4RgJtoHeUULRxmUBpFuK`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Style-Controlled Rewriting}
5	\label{sec:rewriting}
6	
7	We isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.
8	For each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').
9	This produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.
10	Each operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\ref{sec:causal_framework}).
11	To control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \citep{reber2025rate}.
12	
13	\subsection{Content Preservation Verification}
14	\label{sec:nli_gate}
15	
16	Style-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \to Q$ path in Figure~\ref{fig:dag}).
17	To block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.
18	For axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\to$ rewrite) and NLI(rewrite $\to$ original) must exceed this value.
19	For axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate---expansion necessarily introduces new content that the original cannot entail.
20	We instead apply direction-aware verification: for expansions, only backward entailment (rewrite entails original); for compressions, only forward entailment (original entails rewrite).
21	This recovered verbosity from 65\% to 86\% pass rate without inflating the effect estimate; for formality, strict bidirectional gating is necessary (Appendix~\ref{app:gate_validation}).
22	This gating mechanism provides filtering-based confounder control \citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality.
23	BERTScore serves as a supplementary monitor but does not participate in gating.
24	
25	\subsection{Measurement Protocol}
26	\label{sec:measurement}
27	
28	Each pair that passes the NLI gate is evaluated by four target judges---GPT-4o (\texttt{gpt-4o-2024-08-06}), Qwen3-32B, Llama-3.3-70B, and Gemini-2.5-Flash---under two complementary scoring modes.
29	In Likert mode, the judge assigns an integer score from 1 to 10 for overall quality to each text independently.
30	In pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better.
31	
32	To control for position bias, each pairwise comparison is evaluated twice with the presentation order swapped, which produces $n_{\text{pairs}} \times 2$ observations.
33	We apply two analysis strategies to these data.
34	For the nonparametric sign test, we retain only \emph{consistent} pairs where the judge selected the same text in both orderings.
35	For the Bradley-Terry model, we use all observations including inconsistent pairs, as the model naturally accommodates noise in individual comparisons.
36	
37	\subsection{Experimental Setup}
38	\label{sec:setup}
39	
40	We evaluate on LLMBar \citep{zeng2023llmbar}, a benchmark of $n = 100$ instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels.
41	LLMBar is well-suited for style bias detection because its human-verified labels provide ground truth against which judge deviations can be measured, and its moderate size permits exhaustive pairwise evaluation with position control.
42	
43	\subsection{Design Rationale}
44	\label{sec:causal_framework}
45	
46	Figure~\ref{fig:dag} presents the assumed data-generating process.
47	Three variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.
48	Both $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \to Y$ while blocking confounding through $Q$.
49	Style-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \to Q$).
50	The NLI entailment gate provides filtering-based confounder control by removing pairs where the rewrite changed semantic content, thereby blocking the $R \to Q$ path and yielding a controlled estimate of the $S \to Y$ effect.
51	Our approach provides interventional rather than formal causal evidence: we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.
52	Our identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.
53	
54	\begin{figure}[t]
55	\centering
56	\begin{tikzpicture}[
57	    node distance=2.5cm and 3cm,
58	    every node/.style={font=\small},
59	    obs/.style={draw, circle, minimum size=1.1cm, thick},
60	    mech/.style={draw, rectangle, rounded corners, minimum size=0.9cm, thick, fill=gray!10},
61	    gate/.style={draw, rectangle, dashed, thick, fill=blue!8, font=\footnotesize},
62	    arr/.style={-{Stealth[length=5pt]}, thick},
63	    blocked/.style={-{Stealth[length=5pt]}, thick, dotted, red!60},
64	  ]
65	  \node[obs] (S) {$S$};
66	  \node[obs, right=of S] (Y) {$Y$};
67	  \node[obs, above=1.8cm of Y] (Q) {$Q$};
68	  \node[mech, left=2cm of Q] (R) {Rewrite};
69	  \node[gate, below=0.5cm of R] (NLI) {NLI gate};
70	  \node[obs, below=1.2cm of Y] (P) {$P$};
71	
72	  \draw[arr] (S) -- node[below, font=\footnotesize] {style bias} (Y);
73	  \draw[arr] (Q) -- node[right, font=\footnotesize] {quality} (Y);
74	  \draw[arr] (R) -- node[above, font=\footnotesize] {} (S);
75	  \draw[blocked] (R) -- node[above, font=\footnotesize, black] {\texttimes} (Q);
76	  \draw[blocked] (R) to[bend left=25] node[pos=0.6, right, font=\scriptsize, black] {\texttimes\ artifact} (Y);
77	  \draw[blocked] (P) -- node[right, font=\scriptsize, black] {pos.\ swap} (Y);
78	  \draw[arr, dashed, orange!70!black] (S) to[bend left=30] node[pos=0.5, above left, font=\scriptsize] {residual confound.} (Q);
79	
80	  \draw[arr, gray] (NLI) -- (R);
81	
82	\end{tikzpicture}
83	\caption{Assumed data-generating process (design rationale, not a claim of perfect identification). The rewriting mechanism $R$ targets style $S$ but may inadvertently alter content quality $Q$ (dotted red, blocked by NLI gate) or introduce rewriting artifacts ($R \to Y$, blocked by double-rewrite control). Position bias $P \to Y$ is controlled by order swapping. The dashed orange $S \to Q$ path represents residual confounding: style may influence perceived quality through channels the NLI gate cannot block (Limitations). $Y$: judge score.}
84	\label{fig:dag}
85	\end{figure}
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "9c735739-9db0-40e9-9c93-ad4193274368",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Style-Controlled Rewriting}\n\\label{sec:rewriting}\n\nWe isolate the effect of individual style attributes on judge scores by generating text pairs that differ along exactly one style axis.\nFor each text, an instruction-tuned LLM (Qwen3-32B) first classifies its current style along the target axis (e.g., formal vs.\\ casual via binary classification), then rewrites it toward the opposite pole (temperature 0.7) according to an axis-specific prompt (e.g., ``Rewrite the following text to be more formal/casual while preserving the exact same content and meaning'').\nThis produces a dataset balanced across both directions at the dataset level: texts detected as formal are rewritten to casual, and vice versa.\nEach operation constitutes a binary intervention on a single style variable while all other axes remain fixed (Section~\\ref{sec:causal_framework}).\nTo control for rewriting artifact bias---the possibility that the judge prefers original text over any rewrite regardless of style---we additionally generate a same-style double-rewrite for each text (e.g., formal $\\to$ formal) to form an original-vs-double-rewrite control pair, following the RATE bias correction protocol \\citep{reber2025rate}.\n\n\\subsection{Content Preservation Verification}\n\\label{sec:nli_gate}\n\nStyle-controlled rewriting risks altering semantic content, which would confound the style effect with a content quality effect (the $R \\to Q$ path in Figure~\\ref{fig:dag}).\nTo block this path, we apply a natural language inference (NLI) gate using DeBERTa-v3-large with an entailment threshold of 0.90.\nFor axes that preserve information density (formality, register), we apply standard bidirectional entailment: both NLI(original $\\to$ rewrite) and NLI(rewrite $\\to$ original) must exceed this value.\nFor axes that inherently change information density (e.g., verbosity), bidirectional verification is inappropriate---expansion necessarily introduces new content that the original cannot entail.\nWe instead apply direction-aware verification: for expansions, only backward entailment (rewrite entails original); for compressions, only forward entailment (original entails rewrite).\nThis recovered verbosity from 65\\% to 86\\% pass rate without inflating the effect estimate; for formality, strict bidirectional gating is necessary (Appendix~\\ref{app:gate_validation}).\nThis gating mechanism provides filtering-based confounder control \\citep{veitch2020adapting} by ensuring that retained pairs differ only in style, not in content quality.\nBERTScore serves as a supplementary monitor but does not participate in gating.\n\n\\subsection{Measurement Protocol}\n\\label{sec:measurement}\n\nEach pair that passes the NLI gate is evaluated by four target judges---GPT-4o (\\texttt{gpt-4o-2024-08-06}), Qwen3-32B, Llama-3.3-70B, and Gemini-2.5-Flash---under two complementary scoring modes.\nIn Likert mode, the judge assigns an integer score from 1 to 10 for overall quality to each text independently.\nIn pairwise mode, the judge receives both texts as candidates A and B and makes a forced choice of which response is better.\n\nTo control for position bias, each pairwise comparison is evaluated twice with the presentation order swapped, which produces $n_{\\text{pairs}} \\times 2$ observations.\nWe apply two analysis strategies to these data.\nFor the nonparametric sign test, we retain only \\emph{consistent} pairs where the judge selected the same text in both orderings.\nFor the Bradley-Terry model, we use all observations including inconsistent pairs, as the model naturally accommodates noise in individual comparisons.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate on LLMBar \\citep{zeng2023llmbar}, a benchmark of $n = 100$ instruction-response pairs spanning diverse task types, designed to test LLM judges' ability to distinguish response quality with human-verified quality labels.\nLLMBar is well-suited for style bias detection because its human-verified labels provide ground truth against which judge deviations can be measured, and its moderate size permits exhaustive pairwise evaluation with position control.\n\n\\subsection{Design Rationale}\n\\label{sec:causal_framework}\n\nFigure~\\ref{fig:dag} presents the assumed data-generating process.\nThree variables govern the observed judge score $Y$: the style attribute $S$ (e.g., formality), the original content quality $Q$, and the judge's internal scoring function.\nBoth $S$ and $Q$ causally influence $Y$; the goal of CSD is to approximate the effect $S \\to Y$ while blocking confounding through $Q$.\nStyle-controlled rewriting generates a text pair that differs along a single style axis, but any rewriting operation risks inadvertently altering content quality ($R \\to Q$).\nThe NLI entailment gate provides filtering-based confounder control by removing pairs where the rewrite changed semantic content, thereby blocking the $R \\to Q$ path and yielding a controlled estimate of the $S \\to Y$ effect.\nOur approach provides interventional rather than formal causal evidence: we do not claim that this DAG is a complete structural causal model, nor do we invoke SUTVA or consistency assumptions from the potential outcomes framework.\nOur identification rests on three operational assumptions: (i)~the NLI gate approximates content preservation, blocking the $R \\to Q$ path; (ii)~position swapping controls for presentation-order effects; and (iii)~the style rewrite introduces no systematic differences beyond the target axis.\n\n\\begin{figure}[t]\n\\centering\n\\begin{tikzpicture}[\n    node distance=2.5cm and 3cm,\n    every node/.style={font=\\small},\n    obs/.style={draw, circle, minimum size=1.1cm, thick},\n    mech/.style={draw, rectangle, rounded corners, minimum size=0.9cm, thick, fill=gray!10},\n    gate/.style={draw, rectangle, dashed, thick, fill=blue!8, font=\\footnotesize},\n    arr/.style={-{Stealth[length=5pt]}, thick},\n    blocked/.style={-{Stealth[length=5pt]}, thick, dotted, red!60},\n  ]\n  \\node[obs] (S) {$S$};\n  \\node[obs, right=of S] (Y) {$Y$};\n  \\node[obs, above=1.8cm of Y] (Q) {$Q$};\n  \\node[mech, left=2cm of Q] (R) {Rewrite};\n  \\node[gate, below=0.5cm of R] (NLI) {NLI gate};\n  \\node[obs, below=1.2cm of Y] (P) {$P$};\n\n  \\draw[arr] (S) -- node[below, font=\\footnotesize] {style bias} (Y);\n  \\draw[arr] (Q) -- node[right, font=\\footnotesize] {quality} (Y);\n  \\draw[arr] (R) -- node[above, font=\\footnotesize] {} (S);\n  \\draw[blocked] (R) -- node[above, font=\\footnotesize, black] {\\texttimes} (Q);\n  \\draw[blocked] (R) to[bend left=25] node[pos=0.6, right, font=\\scriptsize, black] {\\texttimes\\ artifact} (Y);\n  \\draw[blocked] (P) -- node[right, font=\\scriptsize, black] {pos.\\ swap} (Y);\n  \\draw[arr, dashed, orange!70!black] (S) to[bend left=30] node[pos=0.5, above left, font=\\scriptsize] {residual confound.} (Q);\n\n  \\draw[arr, gray] (NLI) -- (R);\n\n\\end{tikzpicture}\n\\caption{Assumed data-generating process (design rationale, not a claim of perfect identification). The rewriting mechanism $R$ targets style $S$ but may inadvertently alter content quality $Q$ (dotted red, blocked by NLI gate) or introduce rewriting artifacts ($R \\to Y$, blocked by double-rewrite control). Position bias $P \\to Y$ is controlled by order swapping. The dashed orange $S \\to Q$ path represents residual confounding: style may influence perceived quality through channels the NLI gate cannot block (Limitations). $Y$: judge score.}\n\\label{fig:dag}\n\\end{figure}\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01ECbyJKbpHiNcFymqNQL5zB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "a5efd4a1-e6b4-43e5-9f60-78247d472131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 28 · 2026-05-22T01:09:01.798Z_

<details><summary>↩ Tool result · `toolu_01ECbyJKbpHiNcFymqNQL5zB`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	
5	\subsection{Statistical Framework}
6	\label{sec:stat_framework}
7	
8	We designate a primary family of six hypothesis tests (three judges $\times$ two axes: formality and verbosity) and control the family-wise error rate with Holm-Bonferroni correction at $\alpha = 0.05$.
9	Table~\ref{tab:main_results} reports both raw and adjusted $p$-values.
10	Analyses outside this grid are classified as either \emph{exploratory} (NLI threshold sensitivity sweep, \S\ref{sec:nli_threshold}) or \emph{confirmatory} (consistency filter validation, \S\ref{sec:consistency}).
11	Exploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.
12	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm}, using the default regularization of the \texttt{choix} Python library.
13	All bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.
14	
15	\paragraph{Model selection.}
16	Target judges span four architectures: GPT-4o (2024-08-06), the dominant judge powering AlpacaEval and MT-Bench leaderboards; Qwen3-32B-Instruct, also serving as rewriter for methodological consistency; Llama-3.3-70B-Instruct, the latest dense Llama model (Llama~4's MoE architecture introduces an additional confound); and Gemini-2.5-Flash as a confirmatory fourth architecture. Claude Sonnet~4 serves as negative control.
17	We pin versions for reproducibility; CSD applies to any black-box judge.
18	
19	\begin{table}[t]
20	\centering
21	\small
22	\caption{Main results across five judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\% CIs in Appendix~\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}
23	\label{tab:main_results}
24	\begin{tabular}{@{}lllccc@{}}
25	\toprule
26	Bench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\ \\
27	\midrule
28	LLMBar & GPT-4o & Form.\ & .630$^{***}$ & .102 (.332) & $\dagger$ \\
29	 & GPT-4o & Verb.\ & .760$^{***}$ & $-$.095 (.403) & $\dagger$ \\
30	 & GPT-4o & Reg.\ & .570$^{\dagger}$ & $-$.031 (.785) & $\dagger_{\text{e}}$ \\
31	\cmidrule{2-6}
32	 & Qwen3 & Form.\ & .665$^{***}$ & .011 (.908) & $\dagger$ \\
33	 & Qwen3 & Form.$^b$ & .675$^{***}$ & $-$.025 (.600) & $\dagger$ \\
34	 & Qwen3 & Verb.\ & .773$^{***}$ & $-$.151 (.179) & $\dagger$ \\
35	 & Qwen3 & Reg.\ & .553 & $-$.073 (.505) & $\dagger_{\text{e}}$ \\
36	\cmidrule{2-6}
37	 & Llama-70B & Form.\ & .695$^{***}$ & .010 (.846) & $\dagger$ \\
38	 & Llama-70B & Verb.\ & .735$^{***}$ & .020 (.752) & $\dagger$ \\
39	 & Llama-70B & Reg.\ & .635$^{\dagger}$ & .024 (.690) & $\dagger_{\text{e}}$ \\
40	\cmidrule{2-6}
41	 & Gemini & Form.\ & .574$^{*}$ & $-$.082 (.309) & $\dagger_{\text{c}}$ \\
42	 & Gemini & Verb.\ & .708$^{***}$ & .051 (.370) & $\dagger_{\text{c}}$ \\
43	\cmidrule{2-6}
44	 & Claude & Form.\ & .562 & $-$.021 (.721) & --- \\
45	 & Claude & Verb.\ & .541 & $-$.039 (.743) & --- \\
46	\midrule
47	AEval & GPT-4o & Form.\ & .727$^{***}$ & .148 (.170) & $\dagger$ \\
48	 & Qwen3 & Form.\ & .657$^{***}$ & .081 (.198) & $\dagger$ \\
49	 & Qwen3 & Verb.\ & .841$^{***}$ & .375 (.0003) & $\ddagger$ \\
50	\midrule
51	MTB & GPT-4o & Form.\ & .692$^{***}$ & .167 (.016) & $\ddagger$ \\
52	 & Qwen3 & Form.\ & .712$^{***}$ & .149 (.007) & $\ddagger$ \\
53	\bottomrule
54	\multicolumn{6}{l}{\footnotesize $^{***}$ $p < 0.001$;\; $^{*}$ $p < 0.05$ (Holm-adj.\ for primary; raw for $\dagger_{\text{c}}$).}\\
55	\multicolumn{6}{l}{\footnotesize $\dagger$: Blindspot;\; $\ddagger$: both sig.;\; ---: neither;\; $\dagger_{\text{e}}$: expl.;\; $\dagger_{\text{c}}$: confirmatory.}\\
56	\multicolumn{6}{l}{\footnotesize $^b$ Scaled replication ($n = 355$); other LLMBar: $n = 88$.}\\
57	\multicolumn{6}{l}{\footnotesize Negative $d$: judge rates style-manipulated variants lower on Likert.}\\
58	\multicolumn{6}{l}{\footnotesize Empty cells: benchmark--axis combinations not tested; cross-benchmark}\\
59	\multicolumn{6}{l}{\footnotesize validation focuses on strongest-evidence configurations.}
60	\end{tabular}
61	\end{table}
62	
63	
64	\begin{figure}[t]
65	\centering
66	\includegraphics[width=\columnwidth]{figures/forest_plot.pdf}
67	\caption{Bradley-Terry win probabilities across four target judges and three style axes. Filled diamonds: significant ($p < 0.05$); open diamonds: non-significant. Error bars: 95\% bootstrap CI. The dashed line at 0.50 indicates no style preference. Verbosity shows the strongest and most consistent bias across all four judges.}
68	\label{fig:forest_plot}
69	\end{figure}
70	
71	\section{Analysis}
72	\label{sec:analysis}
73	
74	
75	\subsection{NLI Gate Validation}
76	\label{sec:nli_validation}
77	
78	\paragraph{False negative rate.}
79	Validating all 100 NLI decisions against an LLM annotator (Qwen3-32B) yields 91/100 agreement (Gwet's AC1 $= 0.89$; Cohen's $\kappa = 0.43$, depressed by prevalence skew \citep{feinstein1990kappa}), with FNR $= 8.4\%$ (8 of 12 rejected pairs judged content-preserving).
80	Since this annotator shares the rewriter model, the FNR may be optimistic; GPT-4o cross-validation below provides model-independent verification.
81	Three robustness checks confirm these do not compromise conclusions: BT stable across 11 NLI thresholds (${\leq}3$pp variation; \S\ref{sec:nli_threshold}), no covariate differences between retained and discarded pairs ($p > 0.12$; \S\ref{sec:consistency}), and no directional bias in false negatives (Fisher $p = 0.35$).
82	The gate operates as a precision-oriented filter (precision $= 98.9\%$); verbosity-rejected pairs have larger edit distances (Cliff's $\delta = +0.45$, $p < 0.001$), making estimates lower bounds.
83	Full-scale GPT-4o validation on all 200 decisions yields 92.1\% formality / 82.6\% verbosity pass precision, the lower verbosity figure reflecting direction-aware gating permissiveness (17.4\% vs.\ 7.9\% FPR).
84	Admitted false positives would inflate verbosity BT only if content-leaked pairs systematically favor the styled variant; the GEE originality OR ${<}1$ indicates the opposite direction, making the estimate a conservative lower bound.
85	
86	\paragraph{Threshold sensitivity.}
87	\label{sec:nli_threshold}
88	A sweep across 11 NLI thresholds (0.50--0.98) confirms robustness: all 44 judge$\times$axis$\times$threshold combinations are significant (${\leq}3$pp variation; Appendix~\ref{app:nli_sweep}), and the bimodal NLI score distribution places the 0.90 threshold on a plateau.
89	
90	
91	\subsection{Measurement Sensitivity: Likert vs.\ Pairwise}
92	\label{sec:likert_pairwise}
93	
94	\paragraph{Head-to-head comparison with RATE.}
95	Applying RATE's Likert ATE methodology \citep{reber2025rate} to our formality style-transformed pairs yields Cohen's $d = 0.10$, $p = 0.33$ (non-significant, $n = 88$); pairwise comparison on identical data reveals a 63.0\% formal preference ($p = 0.0004$, Bradley-Terry on all 173 comparisons), confirmed by a consistency-filtered sign test (73.9\%, $p = 0.006$, $n = 46$ consistent pairs).
96	This is the Likert Blindspot: the same data, the same style intervention, two measurement instruments---one detects bias, the other does not.
97	A $4\times$ scaled replication ($n = 355$) distinguishes measurement attenuation from insufficient power: the Likert effect size shrinks to $d = {-}0.025$ (near zero) while BT remains stable at $67.5\%$ ($p < 0.0001$)---if the gap were merely statistical power, $d$ would remain non-zero at larger $n$.
98	Bootstrap subsampling confirms: $d$ remains flat near zero ($d_{\text{median}} = {-}0.017$) as CIs narrow from ${\pm}0.3$ to ${\pm}0.1$, never excluding zero (Appendix~\ref{app:bootstrap_attenuation}).
99	Attenuation follows a severity spectrum: at moderate bias (BT 63--67\%), it is complete ($d \to 0$ at $n = 355$); at stronger effects (BT ${>}70\%$), Likert partially detects but attenuates ${>}60\%$ (MT-Bench $d \approx 0.15$ for BT ${\sim}70\%$)---explaining why three of eleven bias-positive cells escape the Blindspot (Table~\ref{tab:main_results}, $\ddagger$ rows).
100	
101	The frameworks are complementary: RATE measures aggregate quality via Likert ATE; CSD targets per-axis style preference via forced-choice comparison, eliminating ties.
102	The Blindspot arises because Likert tie rates cluster at 58--73\% across all nine configurations; a 100-point continuous scale does not resolve this ($p = 0.725$/$0.117$; Appendix~\ref{app:likert100}), confirming a paradigm difference rather than granularity limitation.
103	
104	
105	\paragraph{Sensitivity hierarchy across measurement methods.}
106	To confirm that the Likert Blindspot is not an artifact of a particular statistical test, we apply seven measurement methods to the same formality data and rank them by sensitivity (Table~\ref{tab:sensitivity}).
107	Both pairwise methods detect the formality preference; all Likert-based methods fail regardless of whether they assume interval scaling (ATE $t$-test), ordinal scaling (ordinal logistic regression), or nonparametric ranking (Wilcoxon signed-rank).
108	The same attenuation pattern replicates on verbosity (Appendix~\ref{app:verb_sensitivity}), where all six Likert methods remain non-significant despite a stronger pairwise signal (BT 77.3\%, $p < 0.001$).
109	
110	\begin{table}[t]
111	\centering
112	\small
113	\caption{Sensitivity hierarchy: seven measurement methods applied to the same formality style-transformed data. Only pairwise methods (top two rows) reach significance. All Likert-based methods fail.}
114	\label{tab:sensitivity}
115	\begin{tabular}{lccc}
116	\toprule
117	Method & Statistic & $p$ & Data \\
118	\midrule
119	BT model & 63.0\% $[55.7, 70.3]$ & $0.0004$ & All 173 comp. \\
120	Sign test (filtered) & 73.9\% (34/46) & 0.006 & Consistent \\
121	\midrule
122	Likert ATE ($t$-test) & $d = 0.102$ & 0.332 & NLI$\geq$0.90 \\
123	Binarized Likert & 60.6\% & 0.296 & Non-tied \\
124	Ordinal reg.\ (prop.\ odds) & $\beta = {-}0.079$ & 0.769 & NLI$\geq$0.90 \\
125	GEE (exchangeable) & $\beta = {-}0.084$ & 0.587 & NLI$\geq$0.90 \\
126	Wilcoxon signed-rank & $W = 274$ & 0.905 & NLI$\geq$0.90 \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	Figure~\ref{fig:power_curve} plots detection probability curves at observed effect magnitudes (not post-hoc power; cf.\ \citealt{hoenig2001abuse}): Likert requires ${\approx}4.5\times$ more data to detect the same bias.
132	Formal power analysis across all six judge$\times$axis cells confirms: Likert would require $4$--$206\times$ the current sample size ($336$--$27{,}159$ pairs) to detect effects that BT identifies at $p < 0.001$ with $n \leq 100$; for formality, the required samples exceed $18{,}000$ pairs---orders of magnitude beyond typical evaluation budgets (Appendix~\ref{app:power_analysis}).
133	\paragraph{Measurement attenuation vs.\ construct divergence.}
134	An alternative interpretation is that Likert and pairwise modes measure different constructs---absolute quality vs.\ ordinal preference---making the divergence a construct difference rather than measurement failure.
135	\citet{tripathi2025pairwise} independently confirm that pairwise and pointwise protocols exhibit distinct sensitivity profiles, with pairwise preferences being more volatile---consistent with this construct divergence interpretation.
136	Both interpretations lead to the same conclusion: Likert audits miss style preferences that drive pairwise-based alignment pipelines (RLHF, DPO).
137	
138	\paragraph{Detection vs.\ amplification.}
139	\label{sec:amplification}
140	\citet{jeong2025comparative} show that pairwise comparison amplifies style biases (the Comparative Trap).
141	Format-level amplification cannot be fully excluded, but six independent controls bound this risk: (i)~NLI gate ablation reverses NLI-fail pairs to BT 41.7\% (Appendix~\ref{app:nli_ablation}); (ii)~Claude Sonnet 4 shows no bias with the identical pairwise format (BT 56.2\%/54.1\%, n.s.); (iii)~cross-axis BT variation (register 55\% $<$ formality 67\% $<$ verbosity 77\%) is inconsistent with uniform format amplification; (iv)~rewriting artifact absorbed by GEE decomposition (Appendix~\ref{app:artifact_control}); (v)~debiased prompting partially reduces bias (verbosity $-13.1$pp; formality $-5.7$/$-0.4$pp); (vi)~four independent architectures all confirm the Blindspot with consistent GEE confound structure (\S\ref{sec:cross_judge}).
142	
143	\begin{figure}[t]
144	\centering
145	\includegraphics[width=\columnwidth]{figures/power_curve.pdf}
146	\caption{Detection probability at observed effect magnitudes. 80\% power crossings: sign test $n \approx 62$, BT $n \approx 114$, binarized Likert $n \approx 462$, Likert ATE $n \approx 1{,}473$. At typical scales ($n = 50$--$200$, shaded), pairwise methods reach 80\% power while Likert methods remain far below. At $n = 355$, Likert $d = {-}0.025$ confirms the gap is structural, not merely a power issue.}
147	\label{fig:power_curve}
148	\end{figure}
149	
150	\subsection{Cross-Judge Replication}
151	\label{sec:cross_judge}
152	
153	Three independent judges replicate the Blindspot: Qwen3-32B (BT 66.5\%, $p < 0.0001$; Likert $p = 0.908$), Llama-3.3-70B (BT 69.5\%, $p = 0.0001$; Likert $p = 0.846$), and Gemini-2.5-Flash (confirmatory: BT 70.8\%, $p < 0.0001$; Likert $d = 0.05$, n.s.).
154	Gemini's formality confound is originality-dominated (Style OR $= 1.64$, n.s.; Orig OR $= 2.51$, $p = 0.002$), unlike the other three judges (\S\ref{sec:direction}).
155	
156	\subsection{Cross-Axis Replication: Verbosity}
157	\label{sec:cross_axis}
158	
159	Verbosity provides the strongest Blindspot: all four target judges show consistent preference (GPT-4o 76.0\%, Qwen3-32B 77.3\%, Llama-70B 73.5\%, Gemini 70.8\%; all $p \leq 0.0001$), while Likert ATE remains non-significant for all ($p = 0.179$--$0.752$).
160	GEE confirms massive style effects (OR $8.2$--$13.1$, all $p < .0001$) with originality ORs below 1 ($0.38$--$0.49$), indicating artifacts favor rewrites rather than reflecting quality confounding (Table~\ref{tab:gee}).
161	Both rewriting directions favor verbose responses (90.7\%/80.6\%); controlling for length leaves the style OR unchanged ($<$2\%).
162	Evaluator-producer overlap applies only to Qwen3-32B; an independent GPT-4o rewriter bounds this to a $22\%$ Style OR reduction ($13.10 \to 10.17$; Appendix~\ref{app:rewriter_indep}).
163	
164	\subsection{Register: Judge-Dependent Confound Structure}
165	\label{sec:negative_control}
166	
167	Register shows judge-dependent heterogeneity (Llama-70B BT 63.5\%, GPT-4o 57.0\%, Qwen3-32B n.s.; all Likert n.s.) with varying GEE confound structure (Table~\ref{tab:gee}); classified as exploratory outside the primary family.
168	
169	\subsection{GEE Conditional Decomposition and Confound Structure}
170	\label{sec:direction}
171	
172	GEE conditional decomposition \citep{liang1986gee} with exchangeable working correlation and robust standard errors separates style from originality effects (Appendix~\ref{app:direction}; model diagnostics including correlation structure robustness and interaction tests in Appendix~\ref{app:gee_diagnostics}).
173	After controlling for original preference, the formality effect remains significant (GPT-4o: OR $= 2.58$, $p = 0.002$; Qwen3-32B: OR $= 2.15$, $p < 0.0001$, $n = 355$; Llama-70B: OR $= 4.81$, $p < 0.0001$; Table~\ref{tab:gee}); the significant originality ORs confirm residual confounding.
174	The $4\times$ replication ($n = 355$) confirms the Blindspot: BT $67.5\%$ (halved CI), Likert n.s.\ ($p = 0.60$).
175	
176	\begin{table}[t]
177	\centering
178	\small
179	\caption{GEE conditional decomposition (exchangeable correlation) of style and originality effects. Verbosity is style-dominated across all four target judges; formality shows varying confound structure.}
180	\label{tab:gee}
181	\begin{tabular}{@{}llclc@{}}
182	\toprule
183	 & \multicolumn{2}{c}{Style OR} & \multicolumn{2}{c}{Originality OR} \\
184	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
185	Config & OR & $p$ & OR & $p$ \\
186	\midrule
187	Qwen3 verb.\ & 13.10 & ${<}.0001$ & 0.49 & .096 \\
188	GPT-4o verb.\ & 11.34 & ${<}.0001$ & 0.45 & .062 \\
189	Llama-70B verb.\ & 8.21 & ${<}.0001$ & 0.38 & .020 \\
190	Gemini verb.\ & 8.98 & ${<}.0001$ & 0.46 & .061 \\
191	\midrule
192	GPT-4o form.\ & 2.58 & .002 & 2.32 & .006 \\
193	Qwen3 form.\ & 4.20 & .0002 & 4.70 & .0001 \\
194	Qwen3 form.$^a$ & 2.15 & ${<}.0001$ & 4.99 & ${<}.0001$ \\
195	Llama-70B form.\ & 4.81 & ${<}.0001$ & 3.12 & .0007 \\
196	Gemini form.\ & 1.64 & .101 & 2.51 & .002 \\
197	\midrule
198	GPT-4o reg.\ & 1.88 & .029 & 2.21 & .006 \\
199	Qwen3 reg.\ & 1.91 & .046 & 5.72 & ${<}.0001$ \\
200	Llama-70B reg.\ & 3.33 & .0003 & 3.07 & .0008 \\
201	\bottomrule
202	\multicolumn{5}{l}{\footnotesize $^a$ $n = 355$; other rows: $n = 88$. 95\% CIs in Appendix.}
203	\end{tabular}
204	\end{table}
205	
206	The confound structure is consistent across all four target judges for verbosity (style-dominated: Style OR $8.2$--$13.1$, Orig OR $0.38$--$0.49$); formality is conditionally style-driven in three judges but originality-dominated in Gemini; register is judge-dependent.
207	Cross-benchmark replication confirms formality bias across all six benchmark$\times$judge configurations (BT 63--73\%, all $p < 0.001$); Claude Sonnet 4 shows no detectable bias (BT 56.2\%/54.1\%, n.s.; TOST equivalence at $\Delta = 15$pp, Appendix~\ref{app:claude_tost}).
208	The Blindspot manifests in eight of eleven bias-positive cells; three exceptions (BT ${>}69\%$, $d \geq 0.14$) confirm it is effect-size dependent.
209	Same-style double-rewrite controls confirm a rewriting artifact (Appendix~\ref{app:artifact_control}), absorbed by GEE's originality term.
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "e3b26a29-5f47-466b-a993-512c5a16e798",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\n\\subsection{Statistical Framework}\n\\label{sec:stat_framework}\n\nWe designate a primary family of six hypothesis tests (three judges $\\times$ two axes: formality and verbosity) and control the family-wise error rate with Holm-Bonferroni correction at $\\alpha = 0.05$.\nTable~\\ref{tab:main_results} reports both raw and adjusted $p$-values.\nAnalyses outside this grid are classified as either \\emph{exploratory} (NLI threshold sensitivity sweep, \\S\\ref{sec:nli_threshold}) or \\emph{confirmatory} (consistency filter validation, \\S\\ref{sec:consistency}).\nExploratory analyses are reported with uncorrected $p$-values and interpreted as hypothesis-generating; confirmatory analyses test specific hypotheses about pipeline validity and are evaluated at the nominal $\\alpha = 0.05$ level without additional correction, as they address orthogonal questions about measurement reliability rather than the primary style-bias family.\nBradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \\citep{hunter2004mm}, using the default regularization of the \\texttt{choix} Python library.\nAll bootstrap confidence intervals use 10{,}000 pair-level resamples with seed 42.\n\n\\paragraph{Model selection.}\nTarget judges span four architectures: GPT-4o (2024-08-06), the dominant judge powering AlpacaEval and MT-Bench leaderboards; Qwen3-32B-Instruct, also serving as rewriter for methodological consistency; Llama-3.3-70B-Instruct, the latest dense Llama model (Llama~4's MoE architecture introduces an additional confound); and Gemini-2.5-Flash as a confirmatory fourth architecture. Claude Sonnet~4 serves as negative control.\nWe pin versions for reproducibility; CSD applies to any black-box judge.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Main results across five judges, three style axes, and three benchmarks. BT: Bradley-Terry win probability (10{,}000 pair-level bootstrap resamples; 95\\% CIs in Appendix~\\ref{app:bt_ci}). AEval: AlpacaEval; MTB: MT-Bench. Claude Sonnet 4 serves as negative control.}\n\\label{tab:main_results}\n\\begin{tabular}{@{}lllccc@{}}\n\\toprule\nBench & Judge & Axis & BT $P$ & Likert $d$ ($p$) & Cat.\\ \\\\\n\\midrule\nLLMBar & GPT-4o & Form.\\ & .630$^{***}$ & .102 (.332) & $\\dagger$ \\\\\n & GPT-4o & Verb.\\ & .760$^{***}$ & $-$.095 (.403) & $\\dagger$ \\\\\n & GPT-4o & Reg.\\ & .570$^{\\dagger}$ & $-$.031 (.785) & $\\dagger_{\\text{e}}$ \\\\\n\\cmidrule{2-6}\n & Qwen3 & Form.\\ & .665$^{***}$ & .011 (.908) & $\\dagger$ \\\\\n & Qwen3 & Form.$^b$ & .675$^{***}$ & $-$.025 (.600) & $\\dagger$ \\\\\n & Qwen3 & Verb.\\ & .773$^{***}$ & $-$.151 (.179) & $\\dagger$ \\\\\n & Qwen3 & Reg.\\ & .553 & $-$.073 (.505) & $\\dagger_{\\text{e}}$ \\\\\n\\cmidrule{2-6}\n & Llama-70B & Form.\\ & .695$^{***}$ & .010 (.846) & $\\dagger$ \\\\\n & Llama-70B & Verb.\\ & .735$^{***}$ & .020 (.752) & $\\dagger$ \\\\\n & Llama-70B & Reg.\\ & .635$^{\\dagger}$ & .024 (.690) & $\\dagger_{\\text{e}}$ \\\\\n\\cmidrule{2-6}\n & Gemini & Form.\\ & .574$^{*}$ & $-$.082 (.309) & $\\dagger_{\\text{c}}$ \\\\\n & Gemini & Verb.\\ & .708$^{***}$ & .051 (.370) & $\\dagger_{\\text{c}}$ \\\\\n\\cmidrule{2-6}\n & Claude & Form.\\ & .562 & $-$.021 (.721) & --- \\\\\n & Claude & Verb.\\ & .541 & $-$.039 (.743) & --- \\\\\n\\midrule\nAEval & GPT-4o & Form.\\ & .727$^{***}$ & .148 (.170) & $\\dagger$ \\\\\n & Qwen3 & Form.\\ & .657$^{***}$ & .081 (.198) & $\\dagger$ \\\\\n & Qwen3 & Verb.\\ & .841$^{***}$ & .375 (.0003) & $\\ddagger$ \\\\\n\\midrule\nMTB & GPT-4o & Form.\\ & .692$^{***}$ & .167 (.016) & $\\ddagger$ \\\\\n & Qwen3 & Form.\\ & .712$^{***}$ & .149 (.007) & $\\ddagger$ \\\\\n\\bottomrule\n\\multicolumn{6}{l}{\\footnotesize $^{***}$ $p < 0.001$;\\; $^{*}$ $p < 0.05$ (Holm-adj.\\ for primary; raw for $\\dagger_{\\text{c}}$).}\\\\\n\\multicolumn{6}{l}{\\footnotesize $\\dagger$: Blindspot;\\; $\\ddagger$: both sig.;\\; ---: neither;\\; $\\dagger_{\\text{e}}$: expl.;\\; $\\dagger_{\\text{c}}$: confirmatory.}\\\\\n\\multicolumn{6}{l}{\\footnotesize $^b$ Scaled replication ($n = 355$); other LLMBar: $n = 88$.}\\\\\n\\multicolumn{6}{l}{\\footnotesize Negative $d$: judge rates style-manipulated variants lower on Likert.}\\\\\n\\multicolumn{6}{l}{\\footnotesize Empty cells: benchmark--axis combinations not tested; cross-benchmark}\\\\\n\\multicolumn{6}{l}{\\footnotesize validation focuses on strongest-evidence configurations.}\n\\end{tabular}\n\\end{table}\n\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/forest_plot.pdf}\n\\caption{Bradley-Terry win probabilities across four target judges and three style axes. Filled diamonds: significant ($p < 0.05$); open diamonds: non-significant. Error bars: 95\\% bootstrap CI. The dashed line at 0.50 indicates no style preference. Verbosity shows the strongest and most consistent bias across all four judges.}\n\\label{fig:forest_plot}\n\\end{figure}\n\n\\section{Analysis}\n\\label{sec:analysis}\n\n\n\\subsection{NLI Gate Validation}\n\\label{sec:nli_validation}\n\n\\paragraph{False negative rate.}\nValidating all 100 NLI decisions against an LLM annotator (Qwen3-32B) yields 91/100 agreement (Gwet's AC1 $= 0.89$; Cohen's $\\kappa = 0.43$, depressed by prevalence skew \\citep{feinstein1990kappa}), with FNR $= 8.4\\%$ (8 of 12 rejected pairs judged content-preserving).\nSince this annotator shares the rewriter model, the FNR may be optimistic; GPT-4o cross-validation below provides model-independent verification.\nThree robustness checks confirm these do not compromise conclusions: BT stable across 11 NLI thresholds (${\\leq}3$pp variation; \\S\\ref{sec:nli_threshold}), no covariate differences between retained and discarded pairs ($p > 0.12$; \\S\\ref{sec:consistency}), and no directional bias in false negatives (Fisher $p = 0.35$).\nThe gate operates as a precision-oriented filter (precision $= 98.9\\%$); verbosity-rejected pairs have larger edit distances (Cliff's $\\delta = +0.45$, $p < 0.001$), making estimates lower bounds.\nFull-scale GPT-4o validation on all 200 decisions yields 92.1\\% formality / 82.6\\% verbosity pass precision, the lower verbosity figure reflecting direction-aware gating permissiveness (17.4\\% vs.\\ 7.9\\% FPR).\nAdmitted false positives would inflate verbosity BT only if content-leaked pairs systematically favor the styled variant; the GEE originality OR ${<}1$ indicates the opposite direction, making the estimate a conservative lower bound.\n\n\\paragraph{Threshold sensitivity.}\n\\label{sec:nli_threshold}\nA sweep across 11 NLI thresholds (0.50--0.98) confirms robustness: all 44 judge$\\times$axis$\\times$threshold combinations are significant (${\\leq}3$pp variation; Appendix~\\ref{app:nli_sweep}), and the bimodal NLI score distribution places the 0.90 threshold on a plateau.\n\n\n\\subsection{Measurement Sensitivity: Likert vs.\\ Pairwise}\n\\label{sec:likert_pairwise}\n\n\\paragraph{Head-to-head comparison with RATE.}\nApplying RATE's Likert ATE methodology \\citep{reber2025rate} to our formality style-transformed pairs yields Cohen's $d = 0.10$, $p = 0.33$ (non-significant, $n = 88$); pairwise comparison on identical data reveals a 63.0\\% formal preference ($p = 0.0004$, Bradley-Terry on all 173 comparisons), confirmed by a consistency-filtered sign test (73.9\\%, $p = 0.006$, $n = 46$ consistent pairs).\nThis is the Likert Blindspot: the same data, the same style intervention, two measurement instruments---one detects bias, the other does not.\nA $4\\times$ scaled replication ($n = 355$) distinguishes measurement attenuation from insufficient power: the Likert effect size shrinks to $d = {-}0.025$ (near zero) while BT remains stable at $67.5\\%$ ($p < 0.0001$)---if the gap were merely statistical power, $d$ would remain non-zero at larger $n$.\nBootstrap subsampling confirms: $d$ remains flat near zero ($d_{\\text{median}} = {-}0.017$) as CIs narrow from ${\\pm}0.3$ to ${\\pm}0.1$, never excluding zero (Appendix~\\ref{app:bootstrap_attenuation}).\nAttenuation follows a severity spectrum: at moderate bias (BT 63--67\\%), it is complete ($d \\to 0$ at $n = 355$); at stronger effects (BT ${>}70\\%$), Likert partially detects but attenuates ${>}60\\%$ (MT-Bench $d \\approx 0.15$ for BT ${\\sim}70\\%$)---explaining why three of eleven bias-positive cells escape the Blindspot (Table~\\ref{tab:main_results}, $\\ddagger$ rows).\n\nThe frameworks are complementary: RATE measures aggregate quality via Likert ATE; CSD targets per-axis style preference via forced-choice comparison, eliminating ties.\nThe Blindspot arises because Likert tie rates cluster at 58--73\\% across all nine configurations; a 100-point continuous scale does not resolve this ($p = 0.725$/$0.117$; Appendix~\\ref{app:likert100}), confirming a paradigm difference rather than granularity limitation.\n\n\n\\paragraph{Sensitivity hierarchy across measurement methods.}\nTo confirm that the Likert Blindspot is not an artifact of a particular statistical test, we apply seven measurement methods to the same formality data and rank them by sensitivity (Table~\\ref{tab:sensitivity}).\nBoth pairwise methods detect the formality preference; all Likert-based methods fail regardless of whether they assume interval scaling (ATE $t$-test), ordinal scaling (ordinal logistic regression), or nonparametric ranking (Wilcoxon signed-rank).\nThe same attenuation pattern replicates on verbosity (Appendix~\\ref{app:verb_sensitivity}), where all six Likert methods remain non-significant despite a stronger pairwise signal (BT 77.3\\%, $p < 0.001$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Sensitivity hierarchy: seven measurement methods applied to the same formality style-transformed data. Only pairwise methods (top two rows) reach significance. All Likert-based methods fail.}\n\\label{tab:sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Statistic & $p$ & Data \\\\\n\\midrule\nBT model & 63.0\\% $[55.7, 70.3]$ & $0.0004$ & All 173 comp. \\\\\nSign test (filtered) & 73.9\\% (34/46) & 0.006 & Consistent \\\\\n\\midrule\nLikert ATE ($t$-test) & $d = 0.102$ & 0.332 & NLI$\\geq$0.90 \\\\\nBinarized Likert & 60.6\\% & 0.296 & Non-tied \\\\\nOrdinal reg.\\ (prop.\\ odds) & $\\beta = {-}0.079$ & 0.769 & NLI$\\geq$0.90 \\\\\nGEE (exchangeable) & $\\beta = {-}0.084$ & 0.587 & NLI$\\geq$0.90 \\\\\nWilcoxon signed-rank & $W = 274$ & 0.905 & NLI$\\geq$0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nFigure~\\ref{fig:power_curve} plots detection probability curves at observed effect magnitudes (not post-hoc power; cf.\\ \\citealt{hoenig2001abuse}): Likert requires ${\\approx}4.5\\times$ more data to detect the same bias.\nFormal power analysis across all six judge$\\times$axis cells confirms: Likert would require $4$--$206\\times$ the current sample size ($336$--$27{,}159$ pairs) to detect effects that BT identifies at $p < 0.001$ with $n \\leq 100$; for formality, the required samples exceed $18{,}000$ pairs---orders of magnitude beyond typical evaluation budgets (Appendix~\\ref{app:power_analysis}).\n\\paragraph{Measurement attenuation vs.\\ construct divergence.}\nAn alternative interpretation is that Likert and pairwise modes measure different constructs---absolute quality vs.\\ ordinal preference---making the divergence a construct difference rather than measurement failure.\n\\citet{tripathi2025pairwise} independently confirm that pairwise and pointwise protocols exhibit distinct sensitivity profiles, with pairwise preferences being more volatile---consistent with this construct divergence interpretation.\nBoth interpretations lead to the same conclusion: Likert audits miss style preferences that drive pairwise-based alignment pipelines (RLHF, DPO).\n\n\\paragraph{Detection vs.\\ amplification.}\n\\label{sec:amplification}\n\\citet{jeong2025comparative} show that pairwise comparison amplifies style biases (the Comparative Trap).\nFormat-level amplification cannot be fully excluded, but six independent controls bound this risk: (i)~NLI gate ablation reverses NLI-fail pairs to BT 41.7\\% (Appendix~\\ref{app:nli_ablation}); (ii)~Claude Sonnet 4 shows no bias with the identical pairwise format (BT 56.2\\%/54.1\\%, n.s.); (iii)~cross-axis BT variation (register 55\\% $<$ formality 67\\% $<$ verbosity 77\\%) is inconsistent with uniform format amplification; (iv)~rewriting artifact absorbed by GEE decomposition (Appendix~\\ref{app:artifact_control}); (v)~debiased prompting partially reduces bias (verbosity $-13.1$pp; formality $-5.7$/$-0.4$pp); (vi)~four independent architectures all confirm the Blindspot with consistent GEE confound structure (\\S\\ref{sec:cross_judge}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/power_curve.pdf}\n\\caption{Detection probability at observed effect magnitudes. 80\\% power crossings: sign test $n \\approx 62$, BT $n \\approx 114$, binarized Likert $n \\approx 462$, Likert ATE $n \\approx 1{,}473$. At typical scales ($n = 50$--$200$, shaded), pairwise methods reach 80\\% power while Likert methods remain far below. At $n = 355$, Likert $d = {-}0.025$ confirms the gap is structural, not merely a power issue.}\n\\label{fig:power_curve}\n\\end{figure}\n\n\\subsection{Cross-Judge Replication}\n\\label{sec:cross_judge}\n\nThree independent judges replicate the Blindspot: Qwen3-32B (BT 66.5\\%, $p < 0.0001$; Likert $p = 0.908$), Llama-3.3-70B (BT 69.5\\%, $p = 0.0001$; Likert $p = 0.846$), and Gemini-2.5-Flash (confirmatory: BT 70.8\\%, $p < 0.0001$; Likert $d = 0.05$, n.s.).\nGemini's formality confound is originality-dominated (Style OR $= 1.64$, n.s.; Orig OR $= 2.51$, $p = 0.002$), unlike the other three judges (\\S\\ref{sec:direction}).\n\n\\subsection{Cross-Axis Replication: Verbosity}\n\\label{sec:cross_axis}\n\nVerbosity provides the strongest Blindspot: all four target judges show consistent preference (GPT-4o 76.0\\%, Qwen3-32B 77.3\\%, Llama-70B 73.5\\%, Gemini 70.8\\%; all $p \\leq 0.0001$), while Likert ATE remains non-significant for all ($p = 0.179$--$0.752$).\nGEE confirms massive style effects (OR $8.2$--$13.1$, all $p < .0001$) with originality ORs below 1 ($0.38$--$0.49$), indicating artifacts favor rewrites rather than reflecting quality confounding (Table~\\ref{tab:gee}).\nBoth rewriting directions favor verbose responses (90.7\\%/80.6\\%); controlling for length leaves the style OR unchanged ($<$2\\%).\nEvaluator-producer overlap applies only to Qwen3-32B; an independent GPT-4o rewriter bounds this to a $22\\%$ Style OR reduction ($13.10 \\to 10.17$; Appendix~\\ref{app:rewriter_indep}).\n\n\\subsection{Register: Judge-Dependent Confound Structure}\n\\label{sec:negative_control}\n\nRegister shows judge-dependent heterogeneity (Llama-70B BT 63.5\\%, GPT-4o 57.0\\%, Qwen3-32B n.s.; all Likert n.s.) with varying GEE confound structure (Table~\\ref{tab:gee}); classified as exploratory outside the primary family.\n\n\\subsection{GEE Conditional Decomposition and Confound Structure}\n\\label{sec:direction}\n\nGEE conditional decomposition \\citep{liang1986gee} with exchangeable working correlation and robust standard errors separates style from originality effects (Appendix~\\ref{app:direction}; model diagnostics including correlation structure robustness and interaction tests in Appendix~\\ref{app:gee_diagnostics}).\nAfter controlling for original preference, the formality effect remains significant (GPT-4o: OR $= 2.58$, $p = 0.002$; Qwen3-32B: OR $= 2.15$, $p < 0.0001$, $n = 355$; Llama-70B: OR $= 4.81$, $p < 0.0001$; Table~\\ref{tab:gee}); the significant originality ORs confirm residual confounding.\nThe $4\\times$ replication ($n = 355$) confirms the Blindspot: BT $67.5\\%$ (halved CI), Likert n.s.\\ ($p = 0.60$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{GEE conditional decomposition (exchangeable correlation) of style and originality effects. Verbosity is style-dominated across all four target judges; formality shows varying confound structure.}\n\\label{tab:gee}\n\\begin{tabular}{@{}llclc@{}}\n\\toprule\n & \\multicolumn{2}{c}{Style OR} & \\multicolumn{2}{c}{Originality OR} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nConfig & OR & $p$ & OR & $p$ \\\\\n\\midrule\nQwen3 verb.\\ & 13.10 & ${<}.0001$ & 0.49 & .096 \\\\\nGPT-4o verb.\\ & 11.34 & ${<}.0001$ & 0.45 & .062 \\\\\nLlama-70B verb.\\ & 8.21 & ${<}.0001$ & 0.38 & .020 \\\\\nGemini verb.\\ & 8.98 & ${<}.0001$ & 0.46 & .061 \\\\\n\\midrule\nGPT-4o form.\\ & 2.58 & .002 & 2.32 & .006 \\\\\nQwen3 form.\\ & 4.20 & .0002 & 4.70 & .0001 \\\\\nQwen3 form.$^a$ & 2.15 & ${<}.0001$ & 4.99 & ${<}.0001$ \\\\\nLlama-70B form.\\ & 4.81 & ${<}.0001$ & 3.12 & .0007 \\\\\nGemini form.\\ & 1.64 & .101 & 2.51 & .002 \\\\\n\\midrule\nGPT-4o reg.\\ & 1.88 & .029 & 2.21 & .006 \\\\\nQwen3 reg.\\ & 1.91 & .046 & 5.72 & ${<}.0001$ \\\\\nLlama-70B reg.\\ & 3.33 & .0003 & 3.07 & .0008 \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^a$ $n = 355$; other rows: $n = 88$. 95\\% CIs in Appendix.}\n\\end{tabular}\n\\end{table}\n\nThe confound structure is consistent across all four target judges for verbosity (style-dominated: Style OR $8.2$--$13.1$, Orig OR $0.38$--$0.49$); formality is conditionally style-driven in three judges but originality-dominated in Gemini; register is judge-dependent.\nCross-benchmark replication confirms formality bias across all six benchmark$\\times$judge configurations (BT 63--73\\%, all $p < 0.001$); Claude Sonnet 4 shows no detectable bias (BT 56.2\\%/54.1\\%, n.s.; TOST equivalence at $\\Delta = 15$pp, Appendix~\\ref{app:claude_tost}).\nThe Blindspot manifests in eight of eleven bias-positive cells; three exceptions (BT ${>}69\\%$, $d \\geq 0.14$) confirm it is effect-size dependent.\nSame-style double-rewrite controls confirm a rewriting artifact (Appendix~\\ref{app:artifact_control}), absorbed by GEE's originality term.\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01VcyqMV5YadiYPxabAzjJ1d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "3a65e03a-ec82-4090-b4f2-0d86c52ee3ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 30 · 2026-05-22T01:09:02.245Z_

<details><summary>↩ Tool result · `toolu_01VcyqMV5YadiYPxabAzjJ1d`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	CSD, a black-box framework, yields two findings across five judges, three benchmarks, and three style axes.
5	First, the \emph{Likert Blindspot}: Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \to 0$ at $n = 355$), ${>}60\%$ attenuation at stronger effects---confirmed by seven statistical methods; whether this reflects measurement attenuation or construct divergence, Likert-only audits miss style-driven preferences that propagate through alignment pipelines.
6	Second, GEE conditional decomposition reveals per-axis confound structure---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis.
7	Existing Likert-based null findings may reflect measurement insensitivity; pairwise comparison with amplification controls (\S\ref{sec:amplification}) offers superior detection sensitivity.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "01e849b6-dec7-4027-80da-92995834213b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nCSD, a black-box framework, yields two findings across five judges, three benchmarks, and three style axes.\nFirst, the \\emph{Likert Blindspot}: Likert scoring systematically misses style biases that pairwise comparison detects---complete at moderate bias ($d \\to 0$ at $n = 355$), ${>}60\\%$ attenuation at stronger effects---confirmed by seven statistical methods; whether this reflects measurement attenuation or construct divergence, Likert-only audits miss style-driven preferences that propagate through alignment pipelines.\nSecond, GEE conditional decomposition reveals per-axis confound structure---verbosity style-dominated, formality conditional, register judge-dependent---determining which estimates require conditional analysis.\nExisting Likert-based null findings may reflect measurement insensitivity; pairwise comparison with amplification controls (\\S\\ref{sec:amplification}) offers superior detection sensitivity.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_015SneGjwQFRv9oX1hyWHf8h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "5426df2a-0236-48d4-9a23-7a521934376b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HXiv7FrcXKwCRD98p54QFC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1616,
      "cache_read_input_tokens": 34324,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1616
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 32 · 2026-05-22T01:09:02.782Z_

<details><summary>↩ Tool result · `toolu_015SneGjwQFRv9oX1hyWHf8h`</summary>

```text
1	\appendix
2	
3	\section{Direction Asymmetry and Quality Confounding}
4	\label{app:direction}
5	
6	The formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\% of casual-is-rewrite pairs ($p = 0.83$).
7	This asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.
8	To quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.
9	After controlling for original preference, the formality effect remains significant ($\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\text{OR} = 2.32$, $p = 0.006$).
10	The formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.
11	
12	At $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.
13	The originality confound remains stronger ($4.99$ vs.\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).
14	The directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.
15	
16	The NLI gate blocks \emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.
17	
18	\section{Consistency Filter Robustness}
19	\label{sec:consistency}
20	
21	The position-consistency filter retains 55 of 98 valid pairs (56.1\%); consistent and inconsistent groups show no significant differences across four covariates (NLI score $p = 0.824$, BERTScore $p = 0.12$, text length $p = 0.137$, length diff $p = 0.715$), indicating selection on judge decisiveness rather than text properties.
22	The BT model using all 173 comparisons including inconsistent pairs yields 63.0\% ($p = 0.0004$), consistent with the filtered sign test (73.9\%, $p = 0.006$), confirming no systematic bias from the filter.
23	
24	\section{GEE Model Diagnostics}
25	\label{app:gee_diagnostics}
26	
27	\paragraph{Correlation structure robustness.}
28	Table~\ref{tab:gee_corr} compares exchangeable and independence working correlation structures across all nine judge$\times$axis cells.
29	The two structures yield virtually identical results: $|\Delta\text{QIC}| < 0.001$ and maximum coefficient change ${<}0.02$ in every cell, with estimated within-pair correlations $\hat{\alpha} \in [-0.25, +0.11]$.
30	All GEE results reported in the main text are therefore robust to correlation structure specification.
31	
32	\begin{table}[h]
33	\centering
34	\small
35	\caption{GEE correlation structure comparison across nine judge$\times$axis cells.}
36	\label{tab:gee_corr}
37	\begin{tabular}{lcccc}
38	\toprule
39	Config & Exch.\ QIC & Indep.\ QIC & $|\Delta\text{QIC}|$ & Max$|\Delta\text{Coef}|$ \\
40	\midrule
41	GPT-4o form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
42	Qwen3 form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
43	Llama-70B form.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
44	GPT-4o verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
45	Qwen3 verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
46	Llama-70B verb.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
47	GPT-4o reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
48	Qwen3 reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
49	Llama-70B reg.\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\
50	\bottomrule
51	\end{tabular}
52	\end{table}
53	
54	\paragraph{Interaction test.}
55	Adding a Style$\times$Originality interaction term to the additive GEE specification yields no significant interactions in any of the nine judge$\times$axis cells (all $p > 0.13$, range $0.14$--$0.96$), confirming that the additive model is the correct specification and that regime classifications are robust to model specification.
56	
57	\paragraph{95\% confidence intervals.}
58	Table~\ref{tab:gee_ci} reports 95\% CIs for all GEE odds ratios in Table~\ref{tab:gee}.
59	
60	\begin{table}[h]
61	\centering
62	\small
63	\caption{95\% CIs for GEE conditional decomposition (Table~\ref{tab:gee}).}
64	\label{tab:gee_ci}
65	\begin{tabular}{@{}lcc@{}}
66	\toprule
67	Config & Style OR [CI] & Orig OR [CI] \\
68	\midrule
69	Qwen3 verb.\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.14] \\
70	GPT-4o verb.\ & 11.34 [4.93, 26.10] & 0.45 [0.20, 1.04] \\
71	Llama-70B verb.\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\
72	Gemini verb.\ & 8.98 [3.68, 21.94] & 0.46 [0.20, 1.04] \\
73	GPT-4o form.\ & 2.58 [1.41, 4.73] & 2.32 [1.27, 4.26] \\
74	Qwen3 form.\ & 4.20 [1.99, 8.87] & 4.70 [2.22, 9.96] \\
75	Qwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\
76	Llama-70B form.\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\
77	Gemini form.\ & 1.64 [0.91, 2.98] & 2.51 [1.39, 4.54] \\
78	GPT-4o reg.\ & 1.88 [1.08, 3.28] & 2.21 [1.26, 3.86] \\
79	Qwen3 reg.\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\
80	Llama-70B reg.\ & 3.33 [1.73, 6.42] & 3.07 [1.60, 5.92] \\
81	\bottomrule
82	\multicolumn{3}{l}{\footnotesize $^a$ $n = 355$; other rows: $n = 88$.}
83	\end{tabular}
84	\end{table}
85	
86	\section{Rewriter Independence}
87	\label{app:rewriter_indep}
88	
89	To test whether the Blindspot depends on the rewriter's identity, we replace Qwen3-32B with GPT-4o as rewriter while keeping Qwen3-32B as judge.
90	
91	\paragraph{Verbosity (Table~\ref{tab:rewriter_indep}).}
92	The Style OR decreases by $22\%$ ($13.10 \to 10.17$), bounding evaluator-producer inflation of the style effect; the pure-style pattern (Originality n.s.) and Blindspot (BT significant, Likert n.s.) both persist.
93	
94	\begin{table}[h]
95	\centering
96	\small
97	\caption{Rewriter independence test: verbosity axis, Qwen3-32B judge. GPT-4o rewriter eliminates evaluator-producer overlap while preserving the Blindspot.}
98	\label{tab:rewriter_indep}
99	\begin{tabular}{lcc}
100	\toprule
101	 & GPT-4o Rewriter & Qwen3 Rewriter \\
102	\midrule
103	NLI pass rate & 81/100 (81\%) & 86/100 (86\%) \\
104	BT $P$ [95\% CI] & .735 [.654, .809] & .773 [.703, .843] \\
105	Likert ATE ($p$) & .000 (.838) & ${\sim}$0 (.179) \\
106	Blindspot & Yes & Yes \\
107	GEE Style OR ($p$) & 10.17 (${<}.0001$) & 13.10 (${<}.0001$) \\
108	GEE Orig OR ($p$) & 1.61 (n.s.) & 0.49 (n.s.) \\
109	\bottomrule
110	\end{tabular}
111	\end{table}
112	
113	\paragraph{Formality (Table~\ref{tab:rewriter_indep_form}).}
114	GPT-4o rewriter produces formality-manipulated pairs yielding BT $64.4\%$ $[56.1, 72.8]$, statistically indistinguishable from the Qwen3-32B baseline ($66.5\%$ $[58.5, 73.9]$; $\Delta = -2.1$pp).
115	The Likert Blindspot replicates with the independent rewriter ($p = 0.184$, n.s.).
116	
117	\begin{table}[h]
118	\centering
119	\small
120	\caption{Rewriter independence test: formality axis, Qwen3-32B judge.}
121	\label{tab:rewriter_indep_form}
122	\begin{tabular}{lcc}
123	\toprule
124	 & GPT-4o Rewriter & Qwen3 Rewriter \\
125	\midrule
126	NLI pass rate & 90/100 (90\%) & 88/100 (88\%) \\
127	BT $P$ [95\% CI] & .644 [.561, .728] & .665 [.585, .739] \\
128	Likert $d$ ($p$) & $-$.081 (.184) & .011 (.908) \\
129	Blindspot & Yes & Yes \\
130	\bottomrule
131	\end{tabular}
132	\end{table}
133	
134	\section{NLI Threshold Sensitivity Sweep}
135	\label{app:nli_sweep}
136	
137	Table~\ref{tab:nli_sweep} reports BT win probabilities across 11 NLI entailment thresholds for all four judge$\times$axis configurations.
138	All 44 combinations are significant ($p < 0.05$), and within each configuration BT varies by at most 3pp, ruling out threshold selection bias.
139	The stability reflects the bimodal NLI score distribution: most pairs score above 0.95 or below 0.30, so thresholds between 0.50 and 0.95 admit nearly identical pair sets.
140	
141	\begin{table}[h]
142	\centering
143	\small
144	\caption{BT win probability across NLI thresholds. All 44 cells significant ($p < 0.05$). $n$: pairs passing threshold.}
145	\label{tab:nli_sweep}
146	\begin{tabular}{@{}rcccc@{}}
147	\toprule
148	Thresh & \multicolumn{2}{c}{Formality BT} & \multicolumn{2}{c}{Verbosity BT} \\
149	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
150	 & Qwen3 & GPT-4o & Qwen3 & GPT-4o \\
151	\midrule
152	.50 & .648 & .615 & .770 & .768 \\
153	.55 & .648 & .615 & .770 & .768 \\
154	.60 & .656 & .621 & .770 & .768 \\
155	.65 & .656 & .621 & .767 & .766 \\
156	.70 & .657 & .623 & .767 & .766 \\
157	.75 & .657 & .623 & .773 & .760 \\
158	.80 & .657 & .623 & .773 & .760 \\
159	.85 & .657 & .623 & .773 & .760 \\
160	.90 & .665 & .630 & .773 & .760 \\
161	.95 & .653 & .629 & .765 & .752 \\
162	.98 & .649 & .642 & .771 & .769 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\section{Direction-Aware Gate Validation}
168	\label{app:gate_validation}
169	
170	For verbosity, the direction-aware NLI gate admits 21 additional pairs (32\%) compared to strict bidirectional verification.
171	These pairs show consistent preference direction (BT 73.8\% vs.\ 78.5\% for bidirectional-pass pairs), and overall BT estimates are statistically indistinguishable ($\Delta = {-}1.1$pp, 95\% CI $[{-}5.6, {+}3.0]$), confirming that direction-aware gating recovers valid pairs without inflating the effect.
172	For formality, strict bidirectional verification is appropriate: a relaxed (direction-aware) gate would admit 9 additional pairs with reversed preference (BT 33.4\%), indicating content preservation failure rather than genuine style preference.
173	This asymmetry empirically justifies the axis-dependent gating strategy described in Section~\ref{sec:nli_gate}.
174	
175	\section{Claude Sonnet 4 Equivalence Testing}
176	\label{app:claude_tost}
177	
178	We failed to detect style bias for Claude at the current sample size ($n = 87$; BT $p = 0.091$, $p = 0.284$).
179	Formal equivalence testing \citep[TOST;][]{lakens2017equivalence} at $\Delta = 10$pp is underpowered at $n = 87$; at $\Delta = 15$pp both axes fall within the equivalence zone, bounding any undetected Claude style preference to ${<}15$pp---substantively distinct from GPT-4o ($13$--$23$pp) and Qwen3-32B ($17$--$27$pp).
180	The $\Delta = 15$pp margin represents a conservative upper bound: it exceeds all observed negative-control deviations from 50\% (Claude: $+6.2$/$+4.1$pp) while remaining below the smallest confirmed bias ($+13$pp for GPT-4o formality), ensuring the equivalence zone excludes effects we would classify as genuine bias.
181	
182	\section{Bradley-Terry Goodness of Fit and Stratified Analysis}
183	\label{app:bt_gof}
184	
185	Bradley-Terry goodness-of-fit tests confirm adequate model fit for both axes (formality: deviance $= 52.80$, $\text{df} = 45$, $p = 0.198$; verbosity: $p = 0.905$).
186	Stratified analysis of consistent pairs by original-text direction reveals no preference heterogeneity for verbosity (Fisher $p = 0.453$) but significant direction asymmetry for formality ($88.9\%$ vs.\ $52.6\%$, Fisher $p = 0.015$), independently confirming the originality confound structure identified by GEE (Table~\ref{tab:gee}).
187	
188	To assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).
189	Style preference persists: formality BT $= 67.3\%$ ($n = 55$, $\Delta = {+}0.8$pp from full sample, 95\% CI $[{-}11.0, {+}12.6]$); verbosity BT $= 76.0\%$ ($n = 50$, $\Delta = {-}1.3$pp, 95\% CI $[{-}13.3, {+}10.3]$).
190	In the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\%$, verbosity $86.1\%$), confirming that style preference is not an artifact of originality confounding.
191	
192	\section{Bradley-Terry Confidence Intervals}
193	\label{app:bt_ci}
194	
195	Table~\ref{tab:bt_ci} reports bootstrap 95\% confidence intervals for all Bradley-Terry estimates in Table~\ref{tab:main_results}.
196	
197	\begin{table}[h]
198	\centering
199	\small
200	\caption{Bootstrap 95\% CIs for BT win probabilities (10{,}000 pair-level resamples).}
201	\label{tab:bt_ci}
202	\begin{tabular}{lllc}
203	\toprule
204	Bench & Judge & Axis & BT $P$ [95\% CI] \\
205	\midrule
206	LLMBar & GPT-4o & Form.\ & .630 [.557, .703] \\
207	 & GPT-4o & Verb.\ & .760 [.667, .853] \\
208	 & GPT-4o & Reg.\ & .570 [.468, .673] \\
209	\cmidrule{2-4}
210	 & Qwen3 & Form.\ & .665 [.585, .739] \\
211	 & Qwen3 & Verb.\ & .773 [.703, .843] \\
212	 & Qwen3 & Reg.\ & .553 [.479, .628] \\
213	\cmidrule{2-4}
214	 & Llama-70B & Form.\ & .695 [.619, .765] \\
215	 & Llama-70B & Verb.\ & .735 [.655, .809] \\
216	 & Llama-70B & Reg.\ & .635 [.555, .712] \\
217	\cmidrule{2-4}
218	 & Claude & Form.\ & .562 [.489, .636] \\
219	 & Claude & Verb.\ & .541 [.459, .616] \\
220	\midrule
221	AEval & GPT-4o & Form.\ & .727 [.663, .785] \\
222	 & Qwen3 & Form.\ & .657 [.581, .733] \\
223	 & Qwen3 & Verb.\ & .841 [.774, .902] \\
224	\midrule
225	MTB & GPT-4o & Form.\ & .692 [.623, .753] \\
226	 & Qwen3 & Form.\ & .712 [.630, .788] \\
227	\bottomrule
228	\end{tabular}
229	\end{table}
230	
231	\section{Bootstrap Attenuation Analysis}
232	\label{app:bootstrap_attenuation}
233	
234	To distinguish measurement attenuation from insufficient statistical power, we subsample the $n = 355$ formality replication (Qwen3-32B) at seven sample sizes and compute Likert Cohen's $d$ with bootstrap 95\% CIs at each (Table~\ref{tab:attenuation}).
235	Under a power limitation, $d$ would remain constant while only $p$-values improve with larger $n$; under measurement attenuation, $d$ itself converges to zero.
236	The data support attenuation: $d_{\text{median}} = {-}0.017$ across all sample sizes, with CIs narrowing from ${\pm}0.3$ to ${\pm}0.1$ but never excluding zero.
237	The same data yield BT $= 66.5\%$ ($p < 0.0001$), confirming that the pairwise signal is robust.
238	Verbosity shows a similar pattern ($d \approx 0.15$--$0.19$, stable, CIs always containing zero; BT $= 76$--$77\%$, $p < 0.0001$).
239	Within the agnostic framework of \S\ref{sec:likert_pairwise}, this evidence favors the measurement attenuation interpretation but does not exclude construct divergence.
240	
241	\begin{table}[h]
242	\centering
243	\small
244	\caption{Bootstrap attenuation analysis: formality $\times$ Qwen3-32B. Likert $d$ remains flat near zero across sample sizes while BT is stable at 66.5\%.}
245	\label{tab:attenuation}
246	\begin{tabular}{@{}rccc@{}}
247	\toprule
248	$n$ & Likert $d$ & 95\% CI & Contains 0? \\
249	\midrule
250	50 & $-$0.017 & [$-$0.308, 0.262] & Yes \\
251	100 & $-$0.015 & [$-$0.219, 0.176] & Yes \\
252	150 & $-$0.019 & [$-$0.179, 0.145] & Yes \\
253	200 & $-$0.016 & [$-$0.157, 0.119] & Yes \\
254	250 & $-$0.018 & [$-$0.144, 0.107] & Yes \\
255	300 & $-$0.018 & [$-$0.131, 0.095] & Yes \\
256	355 & $-$0.017 & [$-$0.123, 0.087] & Yes \\
257	\bottomrule
258	\end{tabular}
259	\end{table}
260	
261	\section{Formal Power Analysis}
262	\label{app:power_analysis}
263	
264	Table~\ref{tab:power} reports the sample size required for Likert ATE to achieve 80\% power at observed effect sizes across all six judge$\times$axis cells.
265	Required sample sizes range from $336$ (Qwen3-32B verbosity, $d = 0.153$) to $27{,}159$ (Qwen3-32B formality, $d = {-}0.017$), representing $4$--$206\times$ the current $n$.
266	For five of six cells, the required $n$ exceeds $1{,}200$---far beyond typical evaluation budgets---converging with the bootstrap attenuation curve (Appendix~\ref{app:bootstrap_attenuation}) to confirm the Blindspot as a structural measurement limitation.
267	
268	\begin{table}[h]
269	\centering
270	\small
271	\caption{Required Likert sample size for 80\% power at observed $d$. BT detects all six effects at $p < 0.001$ with $n \leq 100$.}
272	\label{tab:power}
273	\begin{tabular}{@{}llcrc@{}}
274	\toprule
275	Judge & Axis & Observed $d$ & Required $n$ & Ratio \\
276	\midrule
277	GPT-4o & Form.\ & 0.073 & 1{,}473 & 16.7$\times$ \\
278	GPT-4o & Verb.\ & 0.080 & 1{,}227 & 14.3$\times$ \\
279	Qwen3 & Form.\ & $-$0.017 & 27{,}159 & 76.5$\times$ \\
280	Qwen3 & Verb.\ & 0.153 & 336 & 3.9$\times$ \\
281	Llama-70B & Form.\ & 0.021 & 18{,}157 & 206.3$\times$ \\
282	Llama-70B & Verb.\ & 0.034 & 6{,}737 & 78.3$\times$ \\
283	\bottomrule
284	\end{tabular}
285	\end{table}
286	
287	\section{Verbosity Sensitivity Hierarchy}
288	\label{app:verb_sensitivity}
289	
290	Table~\ref{tab:verb_sensitivity} replicates the seven-method sensitivity analysis (Table~\ref{tab:sensitivity}) on the verbosity axis ($n = 86$ NLI-filtered pairs, Qwen3-32B judge, LLMBar).
291	The attenuation pattern is more extreme than formality: all six Likert-based methods remain non-significant (lowest $p = 0.213$) despite a stronger pairwise signal (BT 77.3\% vs.\ 66.5\% for formality), and Likert effect sizes ($d = 0.036$--$0.056$) are near zero.
292	
293	\begin{table}[h]
294	\centering
295	\small
296	\caption{Sensitivity hierarchy for verbosity ($n = 86$, Qwen3-32B, LLMBar). All Likert methods fail; only BT reaches significance.}
297	\label{tab:verb_sensitivity}
298	\begin{tabular}{lccc}
299	\toprule
300	Method & Statistic & $p$ & Sig? \\
301	\midrule
302	BT model & 77.3\% $[70.3, 84.3]$ & ${<}0.001$ & Yes \\
303	\midrule
304	Likert ATE & $d = 0.056$ & 0.691 & No \\
305	Binarized $\chi^2$ & OR $= 2.16$ & 0.213 & No \\
306	Ordinal reg.\ & $\beta = 0.159$ & 0.575 & No \\
307	Paired $t$-test & $d = 0.056$ & 0.607 & No \\
308	Mann-Whitney $U$ & $r = {-}0.046$ & 0.578 & No \\
309	Cohen's $d$ & $d = 0.036$ & --- & No \\
310	\bottomrule
311	\multicolumn{4}{p{0.9\columnwidth}}{\footnotesize Effect sizes use style-aligned scoring (verbose $-$ concise), isolating style preference direction. Table~\ref{tab:main_results} reports RATE-compatible ATE (counterfactual $-$ original), which conflates style and originality effects.}
312	\end{tabular}
313	\end{table}
314	
315	\section{100-Point Continuous Likert Scale}
316	\label{app:likert100}
317	
318	To test whether the Blindspot reflects integer-scale granularity rather than a paradigm difference between absolute and relative evaluation, we replicate the formality and verbosity experiments using a 100-point continuous scale ($0$--$100$) with Qwen3-32B as judge (Table~\ref{tab:likert100}).
319	Both axes remain non-significant: formality $p = 0.725$ (tie rate $65.9\%$) and verbosity $p = 0.117$ (tie rate $51.2\%$), while the same data yield BT $66.5\%$ ($p < 0.0001$) and $77.3\%$ ($p < 0.0001$) respectively.
320	The persistence of high tie rates even with 101 possible values confirms that LLM judges do not exploit finer granularity to express style preferences; the Blindspot arises from absolute-vs-relative evaluation paradigms, not scale resolution.
321	
322	\begin{table}[h]
323	\centering
324	\small
325	\caption{100-point continuous Likert vs.\ pairwise (BT). The Blindspot persists despite 101 possible score values.}
326	\label{tab:likert100}
327	\begin{tabular}{@{}lccccc@{}}
328	\toprule
329	Axis & Likert $p$ & Tie rate & BT $P$ & BT $p$ \\
330	\midrule
331	Formality & .725 & 65.9\% & .665 & ${<}.0001$ \\
332	Verbosity & .117 & 51.2\% & .773 & ${<}.0001$ \\
333	\bottomrule
334	\end{tabular}
335	\end{table}
336	
337	\section{NLI Gate Ablation}
338	\label{app:nli_ablation}
339	
340	Table~\ref{tab:nli_ablation} compares BT estimates across NLI-pass, NLI-fail, and all pairs.
341	For formality, NLI-fail pairs reverse to 41.7\% (preferring casual over formal), demonstrating that the gate removes content-confounded pairs rather than amplifying style signal.
342	The small NLI-fail sample ($n \approx 12$) limits precision; this serves as a bounding analysis.
343	For verbosity, NLI-fail pairs remain at 75.0\%, consistent with the dominant style effect (OR $= 13.10$) overwhelming content noise.
344	
345	\begin{table}[h]
346	\centering
347	\small
348	\caption{NLI gate ablation: BT win probability by NLI subset.}
349	\label{tab:nli_ablation}
350	\begin{tabular}{lccc}
351	\toprule
352	Axis & NLI-pass & NLI-fail & All \\
353	\midrule
354	Formality & 66.5\% & 41.7\% & 63.0\% \\
355	Verbosity & 77.3\% & 75.0\% & 76.0\% \\
356	\bottomrule
357	\end{tabular}
358	\end{table}
359	
360	\section{Rewriting Artifact Control}
361	\label{app:artifact_control}
362	
363	Same-style double-rewrite (DR) controls quantify the rewriting artifact using BT models (consistent with all other pairwise analyses).
364	Table~\ref{tab:artifact} reports BT $P(\text{original})$---the probability the judge prefers the original over its same-style DR.
365	Both judges systematically prefer LLM-polished text across axes; for verbosity, BT $P(\text{original}) < 0.17$ indicates that rewriting quality dominates when content is held constant, validating the GEE decomposition that separates style from artifact effects.
366	
367	\begin{table}[h]
368	\centering
369	\small
370	\caption{Rewriting artifact: BT $P(\text{orig})$ vs.\ same-style double-rewrite (bootstrap 95\% CI, 10{,}000 resamples). Values ${<}0.5$: judges prefer LLM-polished text.}
371	\label{tab:artifact}
372	\begin{tabular}{@{}llcc@{}}
373	\toprule
374	Axis & Judge & BT $P(\text{orig})$ [CI] & $p$ \\
375	\midrule
376	Form.\ & GPT-4o & .418 [.342, .500] & .037 \\
377	 & Qwen3 & .377 [.303, .451] & .0006 \\
378	\midrule
379	Verb.\ & GPT-4o & .167 [.084, .262] & ${<}.0001$ \\
380	 & Qwen3 & .082 [.035, .140] & ${<}.0001$ \\
381	\bottomrule
382	\end{tabular}
383	\end{table}
384	
385	\section{Implementation Details}
386	\label{app:implementation}
387	
388	\paragraph{Models and APIs.}
389	Style-controlled rewriting uses Qwen3-32B (temperature $0.7$, top-$p$ $0.9$).
390	Target judges: GPT-4o (\texttt{gpt-4o-2024-08-06}, accessed April--May 2026), Qwen3-32B (locally hosted), Llama-3.3-70B (locally hosted via vLLM).
391	Negative control: Claude Sonnet 4 (\texttt{claude-sonnet-4-20250514}, accessed May 2026).
392	All judge calls use temperature $0$ and $\texttt{max\_tokens} = 2048$.
393	
394	\paragraph{NLI gate.}
395	Content preservation is verified using DeBERTa-v3-large \citep{he2021debertav3} fine-tuned on MNLI, with entailment threshold $\tau = 0.90$.
396	Bidirectional entailment is applied for formality and register; direction-aware entailment for verbosity (Section~\ref{sec:nli_gate}).
397	
398	\paragraph{Statistical methods.}
399	Bradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \citep{hunter2004mm} using the \texttt{choix} Python library (default regularization).
400	All bootstrap CIs use 10{,}000 pair-level resamples with seed $42$.
401	GEE models use exchangeable working correlation with robust (sandwich) standard errors via \texttt{statsmodels} (Section~\ref{sec:direction}; diagnostics in Appendix~\ref{app:gee_diagnostics}).
402	
403	\paragraph{Benchmarks.}
404	LLMBar \citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).
405	AlpacaEval \citep{dubois2025lc}: 100 sampled pairs.
406	MT-Bench \citep{zheng2023judging}: 80 multi-turn pairs.
407	
408	\paragraph{Code and data.}
409	All code, prompts, and experimental data will be released upon acceptance under an open-source license.
410	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0fccb35f-b1a1-493e-bf57-c6bae406cb19",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/sections/appendix.tex",
      "content": "\\appendix\n\n\\section{Direction Asymmetry and Quality Confounding}\n\\label{app:direction}\n\nThe formality axis exhibits a pronounced direction asymmetry: the judge selects the formal variant in 78.8\\% of formal-is-rewrite pairs ($p = 0.001$) but only 54.5\\% of casual-is-rewrite pairs ($p = 0.83$).\nThis asymmetry suggests that original quality $Q$ and formality $S$ are partially confounded---formally written texts may be inherently perceived as higher quality.\nTo quantify this, we fit a GEE logistic model (exchangeable correlation) with both formality and original-preference as predictors.\nAfter controlling for original preference, the formality effect remains significant ($\\text{OR} = 2.58$, $p = 0.002$), and the original-preference effect is also significant ($\\text{OR} = 2.32$, $p = 0.006$).\nThe formality preference thus survives adjustment for original-preference confounding, though the significant original-preference effect indicates that quality--style confounding is present and non-negligible.\n\nAt $n = 88$, the Qwen3-32B formality Style OR ($4.20$) exceeded the GPT-4o estimate ($2.58$), but a scaled replication ($n = 355$) corrects this to $2.15$ ($p < 0.0001$), comparable to GPT-4o and consistent with small-sample upward bias rather than evaluator-producer inflation of the style effect.\nThe originality confound remains stronger ($4.99$ vs.\\ $2.32$), consistent with evaluator-producer bias inflating the originality component (Limitations).\nThe directional agreement between judges---both favor formal text after controlling for originality---supports the existence of formality bias, but the effect magnitude from Qwen3-32B should not be directly compared with GPT-4o.\n\nThe NLI gate blocks \\emph{content} changes but cannot block quality perception shifts that are themselves mediated by style---a fundamental identifiability limit of any text-rewriting approach.\n\n\\section{Consistency Filter Robustness}\n\\label{sec:consistency}\n\nThe position-consistency filter retains 55 of 98 valid pairs (56.1\\%); consistent and inconsistent groups show no significant differences across four covariates (NLI score $p = 0.824$, BERTScore $p = 0.12$, text length $p = 0.137$, length diff $p = 0.715$), indicating selection on judge decisiveness rather than text properties.\nThe BT model using all 173 comparisons including inconsistent pairs yields 63.0\\% ($p = 0.0004$), consistent with the filtered sign test (73.9\\%, $p = 0.006$), confirming no systematic bias from the filter.\n\n\\section{GEE Model Diagnostics}\n\\label{app:gee_diagnostics}\n\n\\paragraph{Correlation structure robustness.}\nTable~\\ref{tab:gee_corr} compares exchangeable and independence working correlation structures across all nine judge$\\times$axis cells.\nThe two structures yield virtually identical results: $|\\Delta\\text{QIC}| < 0.001$ and maximum coefficient change ${<}0.02$ in every cell, with estimated within-pair correlations $\\hat{\\alpha} \\in [-0.25, +0.11]$.\nAll GEE results reported in the main text are therefore robust to correlation structure specification.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{GEE correlation structure comparison across nine judge$\\times$axis cells.}\n\\label{tab:gee_corr}\n\\begin{tabular}{lcccc}\n\\toprule\nConfig & Exch.\\ QIC & Indep.\\ QIC & $|\\Delta\\text{QIC}|$ & Max$|\\Delta\\text{Coef}|$ \\\\\n\\midrule\nGPT-4o form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nQwen3 form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nLlama-70B form.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nGPT-4o verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nQwen3 verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nLlama-70B verb.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nGPT-4o reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nQwen3 reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\nLlama-70B reg.\\ & --- & --- & ${<}0.001$ & ${<}0.02$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Interaction test.}\nAdding a Style$\\times$Originality interaction term to the additive GEE specification yields no significant interactions in any of the nine judge$\\times$axis cells (all $p > 0.13$, range $0.14$--$0.96$), confirming that the additive model is the correct specification and that regime classifications are robust to model specification.\n\n\\paragraph{95\\% confidence intervals.}\nTable~\\ref{tab:gee_ci} reports 95\\% CIs for all GEE odds ratios in Table~\\ref{tab:gee}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{95\\% CIs for GEE conditional decomposition (Table~\\ref{tab:gee}).}\n\\label{tab:gee_ci}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nConfig & Style OR [CI] & Orig OR [CI] \\\\\n\\midrule\nQwen3 verb.\\ & 13.10 [5.62, 30.55] & 0.49 [0.21, 1.14] \\\\\nGPT-4o verb.\\ & 11.34 [4.93, 26.10] & 0.45 [0.20, 1.04] \\\\\nLlama-70B verb.\\ & 8.21 [3.62, 18.65] & 0.38 [0.17, 0.86] \\\\\nGemini verb.\\ & 8.98 [3.68, 21.94] & 0.46 [0.20, 1.04] \\\\\nGPT-4o form.\\ & 2.58 [1.41, 4.73] & 2.32 [1.27, 4.26] \\\\\nQwen3 form.\\ & 4.20 [1.99, 8.87] & 4.70 [2.22, 9.96] \\\\\nQwen3 form.$^a$ & 2.15 [1.46, 3.16] & 4.99 [3.40, 7.34] \\\\\nLlama-70B form.\\ & 4.81 [2.48, 9.33] & 3.12 [1.61, 6.04] \\\\\nGemini form.\\ & 1.64 [0.91, 2.98] & 2.51 [1.39, 4.54] \\\\\nGPT-4o reg.\\ & 1.88 [1.08, 3.28] & 2.21 [1.26, 3.86] \\\\\nQwen3 reg.\\ & 1.91 [1.01, 3.58] & 5.72 [3.02, 10.82] \\\\\nLlama-70B reg.\\ & 3.33 [1.73, 6.42] & 3.07 [1.60, 5.92] \\\\\n\\bottomrule\n\\multicolumn{3}{l}{\\footnotesize $^a$ $n = 355$; other rows: $n = 88$.}\n\\end{tabular}\n\\end{table}\n\n\\section{Rewriter Independence}\n\\label{app:rewriter_indep}\n\nTo test whether the Blindspot depends on the rewriter's identity, we replace Qwen3-32B with GPT-4o as rewriter while keeping Qwen3-32B as judge.\n\n\\paragraph{Verbosity (Table~\\ref{tab:rewriter_indep}).}\nThe Style OR decreases by $22\\%$ ($13.10 \\to 10.17$), bounding evaluator-producer inflation of the style effect; the pure-style pattern (Originality n.s.) and Blindspot (BT significant, Likert n.s.) both persist.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Rewriter independence test: verbosity axis, Qwen3-32B judge. GPT-4o rewriter eliminates evaluator-producer overlap while preserving the Blindspot.}\n\\label{tab:rewriter_indep}\n\\begin{tabular}{lcc}\n\\toprule\n & GPT-4o Rewriter & Qwen3 Rewriter \\\\\n\\midrule\nNLI pass rate & 81/100 (81\\%) & 86/100 (86\\%) \\\\\nBT $P$ [95\\% CI] & .735 [.654, .809] & .773 [.703, .843] \\\\\nLikert ATE ($p$) & .000 (.838) & ${\\sim}$0 (.179) \\\\\nBlindspot & Yes & Yes \\\\\nGEE Style OR ($p$) & 10.17 (${<}.0001$) & 13.10 (${<}.0001$) \\\\\nGEE Orig OR ($p$) & 1.61 (n.s.) & 0.49 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Formality (Table~\\ref{tab:rewriter_indep_form}).}\nGPT-4o rewriter produces formality-manipulated pairs yielding BT $64.4\\%$ $[56.1, 72.8]$, statistically indistinguishable from the Qwen3-32B baseline ($66.5\\%$ $[58.5, 73.9]$; $\\Delta = -2.1$pp).\nThe Likert Blindspot replicates with the independent rewriter ($p = 0.184$, n.s.).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Rewriter independence test: formality axis, Qwen3-32B judge.}\n\\label{tab:rewriter_indep_form}\n\\begin{tabular}{lcc}\n\\toprule\n & GPT-4o Rewriter & Qwen3 Rewriter \\\\\n\\midrule\nNLI pass rate & 90/100 (90\\%) & 88/100 (88\\%) \\\\\nBT $P$ [95\\% CI] & .644 [.561, .728] & .665 [.585, .739] \\\\\nLikert $d$ ($p$) & $-$.081 (.184) & .011 (.908) \\\\\nBlindspot & Yes & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NLI Threshold Sensitivity Sweep}\n\\label{app:nli_sweep}\n\nTable~\\ref{tab:nli_sweep} reports BT win probabilities across 11 NLI entailment thresholds for all four judge$\\times$axis configurations.\nAll 44 combinations are significant ($p < 0.05$), and within each configuration BT varies by at most 3pp, ruling out threshold selection bias.\nThe stability reflects the bimodal NLI score distribution: most pairs score above 0.95 or below 0.30, so thresholds between 0.50 and 0.95 admit nearly identical pair sets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BT win probability across NLI thresholds. All 44 cells significant ($p < 0.05$). $n$: pairs passing threshold.}\n\\label{tab:nli_sweep}\n\\begin{tabular}{@{}rcccc@{}}\n\\toprule\nThresh & \\multicolumn{2}{c}{Formality BT} & \\multicolumn{2}{c}{Verbosity BT} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Qwen3 & GPT-4o & Qwen3 & GPT-4o \\\\\n\\midrule\n.50 & .648 & .615 & .770 & .768 \\\\\n.55 & .648 & .615 & .770 & .768 \\\\\n.60 & .656 & .621 & .770 & .768 \\\\\n.65 & .656 & .621 & .767 & .766 \\\\\n.70 & .657 & .623 & .767 & .766 \\\\\n.75 & .657 & .623 & .773 & .760 \\\\\n.80 & .657 & .623 & .773 & .760 \\\\\n.85 & .657 & .623 & .773 & .760 \\\\\n.90 & .665 & .630 & .773 & .760 \\\\\n.95 & .653 & .629 & .765 & .752 \\\\\n.98 & .649 & .642 & .771 & .769 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Direction-Aware Gate Validation}\n\\label{app:gate_validation}\n\nFor verbosity, the direction-aware NLI gate admits 21 additional pairs (32\\%) compared to strict bidirectional verification.\nThese pairs show consistent preference direction (BT 73.8\\% vs.\\ 78.5\\% for bidirectional-pass pairs), and overall BT estimates are statistically indistinguishable ($\\Delta = {-}1.1$pp, 95\\% CI $[{-}5.6, {+}3.0]$), confirming that direction-aware gating recovers valid pairs without inflating the effect.\nFor formality, strict bidirectional verification is appropriate: a relaxed (direction-aware) gate would admit 9 additional pairs with reversed preference (BT 33.4\\%), indicating content preservation failure rather than genuine style preference.\nThis asymmetry empirically justifies the axis-dependent gating strategy described in Section~\\ref{sec:nli_gate}.\n\n\\section{Claude Sonnet 4 Equivalence Testing}\n\\label{app:claude_tost}\n\nWe failed to detect style bias for Claude at the current sample size ($n = 87$; BT $p = 0.091$, $p = 0.284$).\nFormal equivalence testing \\citep[TOST;][]{lakens2017equivalence} at $\\Delta = 10$pp is underpowered at $n = 87$; at $\\Delta = 15$pp both axes fall within the equivalence zone, bounding any undetected Claude style preference to ${<}15$pp---substantively distinct from GPT-4o ($13$--$23$pp) and Qwen3-32B ($17$--$27$pp).\nThe $\\Delta = 15$pp margin represents a conservative upper bound: it exceeds all observed negative-control deviations from 50\\% (Claude: $+6.2$/$+4.1$pp) while remaining below the smallest confirmed bias ($+13$pp for GPT-4o formality), ensuring the equivalence zone excludes effects we would classify as genuine bias.\n\n\\section{Bradley-Terry Goodness of Fit and Stratified Analysis}\n\\label{app:bt_gof}\n\nBradley-Terry goodness-of-fit tests confirm adequate model fit for both axes (formality: deviance $= 52.80$, $\\text{df} = 45$, $p = 0.198$; verbosity: $p = 0.905$).\nStratified analysis of consistent pairs by original-text direction reveals no preference heterogeneity for verbosity (Fisher $p = 0.453$) but significant direction asymmetry for formality ($88.9\\%$ vs.\\ $52.6\\%$, Fisher $p = 0.015$), independently confirming the originality confound structure identified by GEE (Table~\\ref{tab:gee}).\n\nTo assess robustness to originality confounding, we restrict to pairs where the judge assigned equal Likert scores to original and counterfactual texts (eliminating detectable quality differences).\nStyle preference persists: formality BT $= 67.3\\%$ ($n = 55$, $\\Delta = {+}0.8$pp from full sample, 95\\% CI $[{-}11.0, {+}12.6]$); verbosity BT $= 76.0\\%$ ($n = 50$, $\\Delta = {-}1.3$pp, 95\\% CI $[{-}13.3, {+}10.3]$).\nIn the anti-originality subset (pairs where the original never wins), effects strengthen (formality $75.0\\%$, verbosity $86.1\\%$), confirming that style preference is not an artifact of originality confounding.\n\n\\section{Bradley-Terry Confidence Intervals}\n\\label{app:bt_ci}\n\nTable~\\ref{tab:bt_ci} reports bootstrap 95\\% confidence intervals for all Bradley-Terry estimates in Table~\\ref{tab:main_results}.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for BT win probabilities (10{,}000 pair-level resamples).}\n\\label{tab:bt_ci}\n\\begin{tabular}{lllc}\n\\toprule\nBench & Judge & Axis & BT $P$ [95\\% CI] \\\\\n\\midrule\nLLMBar & GPT-4o & Form.\\ & .630 [.557, .703] \\\\\n & GPT-4o & Verb.\\ & .760 [.667, .853] \\\\\n & GPT-4o & Reg.\\ & .570 [.468, .673] \\\\\n\\cmidrule{2-4}\n & Qwen3 & Form.\\ & .665 [.585, .739] \\\\\n & Qwen3 & Verb.\\ & .773 [.703, .843] \\\\\n & Qwen3 & Reg.\\ & .553 [.479, .628] \\\\\n\\cmidrule{2-4}\n & Llama-70B & Form.\\ & .695 [.619, .765] \\\\\n & Llama-70B & Verb.\\ & .735 [.655, .809] \\\\\n & Llama-70B & Reg.\\ & .635 [.555, .712] \\\\\n\\cmidrule{2-4}\n & Claude & Form.\\ & .562 [.489, .636] \\\\\n & Claude & Verb.\\ & .541 [.459, .616] \\\\\n\\midrule\nAEval & GPT-4o & Form.\\ & .727 [.663, .785] \\\\\n & Qwen3 & Form.\\ & .657 [.581, .733] \\\\\n & Qwen3 & Verb.\\ & .841 [.774, .902] \\\\\n\\midrule\nMTB & GPT-4o & Form.\\ & .692 [.623, .753] \\\\\n & Qwen3 & Form.\\ & .712 [.630, .788] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Bootstrap Attenuation Analysis}\n\\label{app:bootstrap_attenuation}\n\nTo distinguish measurement attenuation from insufficient statistical power, we subsample the $n = 355$ formality replication (Qwen3-32B) at seven sample sizes and compute Likert Cohen's $d$ with bootstrap 95\\% CIs at each (Table~\\ref{tab:attenuation}).\nUnder a power limitation, $d$ would remain constant while only $p$-values improve with larger $n$; under measurement attenuation, $d$ itself converges to zero.\nThe data support attenuation: $d_{\\text{median}} = {-}0.017$ across all sample sizes, with CIs narrowing from ${\\pm}0.3$ to ${\\pm}0.1$ but never excluding zero.\nThe same data yield BT $= 66.5\\%$ ($p < 0.0001$), confirming that the pairwise signal is robust.\nVerbosity shows a similar pattern ($d \\approx 0.15$--$0.19$, stable, CIs always containing zero; BT $= 76$--$77\\%$, $p < 0.0001$).\nWithin the agnostic framework of \\S\\ref{sec:likert_pairwise}, this evidence favors the measurement attenuation interpretation but does not exclude construct divergence.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Bootstrap attenuation analysis: formality $\\times$ Qwen3-32B. Likert $d$ remains flat near zero across sample sizes while BT is stable at 66.5\\%.}\n\\label{tab:attenuation}\n\\begin{tabular}{@{}rccc@{}}\n\\toprule\n$n$ & Likert $d$ & 95\\% CI & Contains 0? \\\\\n\\midrule\n50 & $-$0.017 & [$-$0.308, 0.262] & Yes \\\\\n100 & $-$0.015 & [$-$0.219, 0.176] & Yes \\\\\n150 & $-$0.019 & [$-$0.179, 0.145] & Yes \\\\\n200 & $-$0.016 & [$-$0.157, 0.119] & Yes \\\\\n250 & $-$0.018 & [$-$0.144, 0.107] & Yes \\\\\n300 & $-$0.018 & [$-$0.131, 0.095] & Yes \\\\\n355 & $-$0.017 & [$-$0.123, 0.087] & Yes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Formal Power Analysis}\n\\label{app:power_analysis}\n\nTable~\\ref{tab:power} reports the sample size required for Likert ATE to achieve 80\\% power at observed effect sizes across all six judge$\\times$axis cells.\nRequired sample sizes range from $336$ (Qwen3-32B verbosity, $d = 0.153$) to $27{,}159$ (Qwen3-32B formality, $d = {-}0.017$), representing $4$--$206\\times$ the current $n$.\nFor five of six cells, the required $n$ exceeds $1{,}200$---far beyond typical evaluation budgets---converging with the bootstrap attenuation curve (Appendix~\\ref{app:bootstrap_attenuation}) to confirm the Blindspot as a structural measurement limitation.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Required Likert sample size for 80\\% power at observed $d$. BT detects all six effects at $p < 0.001$ with $n \\leq 100$.}\n\\label{tab:power}\n\\begin{tabular}{@{}llcrc@{}}\n\\toprule\nJudge & Axis & Observed $d$ & Required $n$ & Ratio \\\\\n\\midrule\nGPT-4o & Form.\\ & 0.073 & 1{,}473 & 16.7$\\times$ \\\\\nGPT-4o & Verb.\\ & 0.080 & 1{,}227 & 14.3$\\times$ \\\\\nQwen3 & Form.\\ & $-$0.017 & 27{,}159 & 76.5$\\times$ \\\\\nQwen3 & Verb.\\ & 0.153 & 336 & 3.9$\\times$ \\\\\nLlama-70B & Form.\\ & 0.021 & 18{,}157 & 206.3$\\times$ \\\\\nLlama-70B & Verb.\\ & 0.034 & 6{,}737 & 78.3$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Verbosity Sensitivity Hierarchy}\n\\label{app:verb_sensitivity}\n\nTable~\\ref{tab:verb_sensitivity} replicates the seven-method sensitivity analysis (Table~\\ref{tab:sensitivity}) on the verbosity axis ($n = 86$ NLI-filtered pairs, Qwen3-32B judge, LLMBar).\nThe attenuation pattern is more extreme than formality: all six Likert-based methods remain non-significant (lowest $p = 0.213$) despite a stronger pairwise signal (BT 77.3\\% vs.\\ 66.5\\% for formality), and Likert effect sizes ($d = 0.036$--$0.056$) are near zero.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Sensitivity hierarchy for verbosity ($n = 86$, Qwen3-32B, LLMBar). All Likert methods fail; only BT reaches significance.}\n\\label{tab:verb_sensitivity}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Statistic & $p$ & Sig? \\\\\n\\midrule\nBT model & 77.3\\% $[70.3, 84.3]$ & ${<}0.001$ & Yes \\\\\n\\midrule\nLikert ATE & $d = 0.056$ & 0.691 & No \\\\\nBinarized $\\chi^2$ & OR $= 2.16$ & 0.213 & No \\\\\nOrdinal reg.\\ & $\\beta = 0.159$ & 0.575 & No \\\\\nPaired $t$-test & $d = 0.056$ & 0.607 & No \\\\\nMann-Whitney $U$ & $r = {-}0.046$ & 0.578 & No \\\\\nCohen's $d$ & $d = 0.036$ & --- & No \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.9\\columnwidth}}{\\footnotesize Effect sizes use style-aligned scoring (verbose $-$ concise), isolating style preference direction. Table~\\ref{tab:main_results} reports RATE-compatible ATE (counterfactual $-$ original), which conflates style and originality effects.}\n\\end{tabular}\n\\end{table}\n\n\\section{100-Point Continuous Likert Scale}\n\\label{app:likert100}\n\nTo test whether the Blindspot reflects integer-scale granularity rather than a paradigm difference between absolute and relative evaluation, we replicate the formality and verbosity experiments using a 100-point continuous scale ($0$--$100$) with Qwen3-32B as judge (Table~\\ref{tab:likert100}).\nBoth axes remain non-significant: formality $p = 0.725$ (tie rate $65.9\\%$) and verbosity $p = 0.117$ (tie rate $51.2\\%$), while the same data yield BT $66.5\\%$ ($p < 0.0001$) and $77.3\\%$ ($p < 0.0001$) respectively.\nThe persistence of high tie rates even with 101 possible values confirms that LLM judges do not exploit finer granularity to express style preferences; the Blindspot arises from absolute-vs-relative evaluation paradigms, not scale resolution.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{100-point continuous Likert vs.\\ pairwise (BT). The Blindspot persists despite 101 possible score values.}\n\\label{tab:likert100}\n\\begin{tabular}{@{}lccccc@{}}\n\\toprule\nAxis & Likert $p$ & Tie rate & BT $P$ & BT $p$ \\\\\n\\midrule\nFormality & .725 & 65.9\\% & .665 & ${<}.0001$ \\\\\nVerbosity & .117 & 51.2\\% & .773 & ${<}.0001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NLI Gate Ablation}\n\\label{app:nli_ablation}\n\nTable~\\ref{tab:nli_ablation} compares BT estimates across NLI-pass, NLI-fail, and all pairs.\nFor formality, NLI-fail pairs reverse to 41.7\\% (preferring casual over formal), demonstrating that the gate removes content-confounded pairs rather than amplifying style signal.\nThe small NLI-fail sample ($n \\approx 12$) limits precision; this serves as a bounding analysis.\nFor verbosity, NLI-fail pairs remain at 75.0\\%, consistent with the dominant style effect (OR $= 13.10$) overwhelming content noise.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NLI gate ablation: BT win probability by NLI subset.}\n\\label{tab:nli_ablation}\n\\begin{tabular}{lccc}\n\\toprule\nAxis & NLI-pass & NLI-fail & All \\\\\n\\midrule\nFormality & 66.5\\% & 41.7\\% & 63.0\\% \\\\\nVerbosity & 77.3\\% & 75.0\\% & 76.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Rewriting Artifact Control}\n\\label{app:artifact_control}\n\nSame-style double-rewrite (DR) controls quantify the rewriting artifact using BT models (consistent with all other pairwise analyses).\nTable~\\ref{tab:artifact} reports BT $P(\\text{original})$---the probability the judge prefers the original over its same-style DR.\nBoth judges systematically prefer LLM-polished text across axes; for verbosity, BT $P(\\text{original}) < 0.17$ indicates that rewriting quality dominates when content is held constant, validating the GEE decomposition that separates style from artifact effects.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Rewriting artifact: BT $P(\\text{orig})$ vs.\\ same-style double-rewrite (bootstrap 95\\% CI, 10{,}000 resamples). Values ${<}0.5$: judges prefer LLM-polished text.}\n\\label{tab:artifact}\n\\begin{tabular}{@{}llcc@{}}\n\\toprule\nAxis & Judge & BT $P(\\text{orig})$ [CI] & $p$ \\\\\n\\midrule\nForm.\\ & GPT-4o & .418 [.342, .500] & .037 \\\\\n & Qwen3 & .377 [.303, .451] & .0006 \\\\\n\\midrule\nVerb.\\ & GPT-4o & .167 [.084, .262] & ${<}.0001$ \\\\\n & Qwen3 & .082 [.035, .140] & ${<}.0001$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Implementation Details}\n\\label{app:implementation}\n\n\\paragraph{Models and APIs.}\nStyle-controlled rewriting uses Qwen3-32B (temperature $0.7$, top-$p$ $0.9$).\nTarget judges: GPT-4o (\\texttt{gpt-4o-2024-08-06}, accessed April--May 2026), Qwen3-32B (locally hosted), Llama-3.3-70B (locally hosted via vLLM).\nNegative control: Claude Sonnet 4 (\\texttt{claude-sonnet-4-20250514}, accessed May 2026).\nAll judge calls use temperature $0$ and $\\texttt{max\\_tokens} = 2048$.\n\n\\paragraph{NLI gate.}\nContent preservation is verified using DeBERTa-v3-large \\citep{he2021debertav3} fine-tuned on MNLI, with entailment threshold $\\tau = 0.90$.\nBidirectional entailment is applied for formality and register; direction-aware entailment for verbosity (Section~\\ref{sec:nli_gate}).\n\n\\paragraph{Statistical methods.}\nBradley-Terry parameters are estimated via spectral initialization followed by minorization-maximization \\citep{hunter2004mm} using the \\texttt{choix} Python library (default regularization).\nAll bootstrap CIs use 10{,}000 pair-level resamples with seed $42$.\nGEE models use exchangeable working correlation with robust (sandwich) standard errors via \\texttt{statsmodels} (Section~\\ref{sec:direction}; diagnostics in Appendix~\\ref{app:gee_diagnostics}).\n\n\\paragraph{Benchmarks.}\nLLMBar \\citep{zeng2023llmbar}: 100 instruction-response pairs ($n = 88$ after NLI gate, $n = 355$ for scaled replication).\nAlpacaEval \\citep{dubois2025lc}: 100 sampled pairs.\nMT-Bench \\citep{zheng2023judging}: 80 multi-turn pairs.\n\n\\paragraph{Code and data.}\nAll code, prompts, and experimental data will be released upon acceptance under an open-source license.\n",
      "numLines": 410,
      "startLine": 1,
      "totalLines": 410
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me extract all citation keys from the tex files and compare them against the bib entries.

**Citation keys in tex files:**

From main.tex:
- jeong2025comparative
- panickssery2024selfpreference
- preston2000scale
- lakens2017equivalence

From introduction.tex:
- murugadoss2025sos
- li2026preference
- soumik2026judging
- casse2026concise
- wang2026fairjudge
- reber2025rate


- dubois2025lc
- thurstone1927law
- veitch2020adapting
- zeng2023llmbar

From related_work.tex:
- feder2021causalm
- wu2021polyjuice
- feder2022causal
- reber2025rate
- counterfactual2025rhetorical
- stevens1946theory
- thurstone1927law
- preston2000scale
- krosnick1999survey
- decoster2011median
- amidei2019likert
- clark2021human
- celikyilmaz2020evaluation
- vanderlee2019

Now I'm pulling in a much larger set of references focused on human evaluation methodologies, ranking-based approaches, and bias in LLM judgments. These cover best practices for collecting human judgments, various ranking and preference elicitation techniques, and recent work examining inconsistencies and fairness issues in how language models evaluate text. I'm now going through the conclusion section, which doesn't have any citations, then compiling the complete list of unique citation keys found across all the tex files to ensure nothing's been missed. Continuing with the bibliography entries and now cross-referencing against the new list to ensure I'm capturing all the relevant citations in the right order. Continuing through the bibliography entries, then cross-referencing to make sure all the citations in the tex file match what's in the bib file and vice versa. Everything checks out so far—no orphaned entries and no missing references. Now I'm verifying that each bib entry has all the required fields. The key for wang2026fairjudge doesn't match the first author Yang, Bo. Similarly, casse2026concise has a key that doesn't align with the actual first author Cho, Young-Min. And counterfactual2025rhetorical's key doesn't correspond to any of the authors either. I'm also noticing that several entries marked as arXiv preprints need verification to see if they've been published elsewhere.

Continuing through the remaining entries, I see soumik2026judging is another arXiv preprint, while reber2025rate appears complete. The older foundational works like kiritchenko2017bws, novikova2018rankme, stevens1946theory, thurstone1927law, and decoster2011median all look properly formatted. For zheng2023judging, the booktitle field should use the full conference name rather than the abbreviated version.

Moving forward, dubois2023alpacafarm has the same booktitle issue, while bradley1952rank, feinstein1990kappa, and hoenig2001abuse are complete. I need to verify whether wang2023faireval and li2024calibraeval have been published beyond their arXiv versions. Zeng2023llmbar is listed as 2024 with ICLR as the booktitle, and veitch2020adapting has all required fields.

Continuing through the list, tan2025judgebench is an inproceedings entry with full details including "and others" for authors, louviere2015bws is a complete book entry, and chiang2024chatbot is a finished inproceedings. Hunter2004mm is complete as an article, while ye2024justice needs verification on its arXiv status. The remaining entries—feder2021causalm, wu2021polyjuice, clark2021human, and amidei2019likert—appear to be complete inproceedings or article entries.

Moving forward, I'm noticing some key-year mismatches: boubdir2023elo is actually from NeurIPS 2024 despite the key saying 2023, and wu2023style is from COLING 2025 even though the key indicates 2023. The rest of the entries from liusie2024comparative through vanderlee2021human are marked as complete, covering a mix of inproceedings and article types across various publication years.

Continuing through the remaining entries, I need to verify a few arXiv preprints: celikyilmaz2020evaluation with arXiv:2006.14799, stureborg2024inconsistent with arXiv:2405.01724, and he2021debertav3 with arXiv:2111.09543 since DeBERTaV3 is widely cited. The entries for jeong2025comparative, park2024offsetbias, panickssery2024selfpreference, and chen2024humans are all marked complete.

Moving forward with entries 51-53, I see shi2024judging needs verification for its arXiv preprint arXiv:2406.07791, while bavaresco2025llms and saito2023verbosity are complete. I'm also tracking a growing list of arXiv preprints that likely have published versions now, including several from 2025 and 2026 that need checking for their final publication status.

Beyond the arXiv issues, I'm noticing some critical metadata problems: wang2026fairjudge's first author is actually Yang, Bo, casse2026concise should be keyed as cho2026concise under the actual first author Cho, Young-Min, and counterfactual2025rhetorical doesn't match any author name in the key. There are also year mismatches where boubdir2023elo claims 2023 in the key but lists 2024 as the publication year, and wu2023style has a similar discrepancy. but year=2025
   - zeng2023llmbar: key says 2023 but year=2024

4. **"and others" usage:** Several entries use "and others" instead of the full author list.

5. **Venue abbreviation check:** I'm noticing that several conference venues include informal parenthetical abbreviations like "(NeurIPS)", "(ICLR)", "(ICML)", and "(UAI)" appended to their official names, which isn't strictly necessary since the series names alone are standard in BibTeX citations.

6. **Tripathi citation verification:** The entry `tripathi2025pairwise` is present in the bibliography and correctly cited in the experiments section.

Now I need to search for the arXiv preprints to determine if any have been published in peer-reviewed venues.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "555ab7ad-44df-46d0-8c92-814f0f9fc8c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ckw4qkqQnHfLCMUQpR3HNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22874,
      "cache_read_input_tokens": 35940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22874
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

_source line 34_

Now I need to check arXiv preprints for published versions. Let me search for the key ones in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "9f3385cf-0a77-4c20-9626-12ea70f04011",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ckw4qkqQnHfLCMUQpR3HNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22874,
      "cache_read_input_tokens": 35940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22874
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013fdnjSG8fCapGTTCDgFosP`</summary>

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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "9850aa14-f2d0-41db-9741-d246fa8eaf80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ckw4qkqQnHfLCMUQpR3HNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22874,
      "cache_read_input_tokens": 35940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 22874
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

_source line 36 · 2026-05-22T01:10:14.240Z_

<details><summary>↩ Tool result · `toolu_013fdnjSG8fCapGTTCDgFosP`</summary>

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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "7a09a994-f840-4f54-9794-ba77ee318ef5",
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

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for the arXiv preprints to check if they have published versions. I'll do multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "76f74161-5c72-4c2a-96b7-5a176c5b9c8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 38_

Let me search for published versions of the arXiv preprints in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "67f27781-6e2f-4354-8a03-45dc9ec77b16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFsczuH8DStfXF7BmAxhnY`</summary>

```json
{
  "query": "Tripathi \"Pairwise or Pointwise\" LLM evaluation bias 2025 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "a7b85b96-79af-498e-a164-a01e0b1e6a0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MeAdqpBp1pu5x6kxchKyWf`</summary>

```json
{
  "query": "FairJudge \"Adaptive Debiased Consistent\" LLM-as-a-Judge Yang Bo 2026 published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "fff0df15-a3f6-4107-98df-13be272161a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjcH5Fzgt62tdXDzo6YeKE`</summary>

```json
{
  "query": "\"A Concise Agent is Less Expert\" Cho Young-Min style features conversational agents 2026 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "443815bc-a975-4628-8b96-bdaeabada539",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PYvndNRUJGVjrr7LztMLNC`</summary>

```json
{
  "query": "\"Counterfactual LLM-based Framework\" \"Measuring Rhetorical Style\" Qiu Jingyi 2025 published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "b7594b8f-26bc-4cfb-a635-43fd9817fdfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 43 · 2026-05-22T01:10:25.225Z_

<details><summary>↩ Tool result · `toolu_01QFsczuH8DStfXF7BmAxhnY`</summary>

```text
Web search results for query: "Tripathi "Pairwise or Pointwise" LLM evaluation bias 2025 published venue"

Links: [{"title":"[2504.14716v1] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716v1"},{"title":"[2504.14716v2] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716v2"},{"title":"[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716"},{"title":"Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge","url":"https://arxiv.org/html/2602.02219"},{"title":"LLM Judges Are Unreliable — The Collective Intelligence Project","url":"https://www.cip.org/blog/llm-judges-are-unreliable"},{"title":"CodeRankEval: Benchmarking and Analyzing LLM Performance for Code Ranking","url":"https://www.researchgate.net/publication/397827093_CodeRankEval_Benchmarking_and_Analyzing_LLM_Performance_for_Code_Ranking"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for ...","url":"https://arxiv.org/pdf/2504.14716"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.emergentmind.com/papers/2504.14716"},{"title":"The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators","url":"https://arxiv.org/pdf/2406.12319"}]

Based on the search results, I found the paper you're looking for:

"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation" by T. Tripathi, M. Wadhwa, G. Durrett, and S. Niekum was published in the Second Conference on Language Modeling in 2025.

The paper is also available on arXiv as paper 2504.14716, with versions dated April 20, 2025 and August 21, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "656a2770-ffc3-4548-8a18-f64fb07bb1f6",
  "tool_use_result": {
    "query": "Tripathi \"Pairwise or Pointwise\" LLM evaluation bias 2025 published venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VaFwjEWqwFyY5x9B5xaXDH",
        "content": [
          {
            "title": "[2504.14716v1] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation",
            "url": "https://arxiv.org/abs/2504.14716v1"
          },
          {
            "title": "[2504.14716v2] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation",
            "url": "https://arxiv.org/abs/2504.14716v2"
          },
          {
            "title": "[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation",
            "url": "https://arxiv.org/abs/2504.14716"
          },
          {
            "title": "Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2602.02219"
          },
          {
            "title": "LLM Judges Are Unreliable — The Collective Intelligence Project",
            "url": "https://www.cip.org/blog/llm-judges-are-unreliable"
          },
          {
            "title": "CodeRankEval: Benchmarking and Analyzing LLM Performance for Code Ranking",
            "url": "https://www.researchgate.net/publication/397827093_CodeRankEval_Benchmarking_and_Analyzing_LLM_Performance_for_Code_Ranking"
          },
          {
            "title": "Pairwise or Pointwise? Evaluating Feedback Protocols for ...",
            "url": "https://arxiv.org/pdf/2504.14716"
          },
          {
            "title": "Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation",
            "url": "https://www.emergentmind.com/papers/2504.14716"
          },
          {
            "title": "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences   of LLM Evaluators",
            "url": "https://arxiv.org/pdf/2406.12319"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation\" by T. Tripathi, M. Wadhwa, G. Durrett, and S. Niekum was published in the Second Conference on Language Modeling in 2025.\n\nThe paper is also available on arXiv as paper 2504.14716, with versions dated April 20, 2025 and August 21, 2025."
    ],
    "durationSeconds": 4.220743426000001
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HoXLPe2cLBW25qbUkwdYL5`</summary>

```json
{
  "query": "\"Judging the Judges Systematic Evaluation\" bias mitigation LLM-as-a-Judge Soumik 2026 published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "72fcb239-1698-441b-bdfb-8ebb0d855d7a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CfoinyzaT3f6bdbKgBALor`</summary>

```json
{
  "query": "\"Large Language Models are not Fair Evaluators\" Wang Peiyi 2023 published venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "77427c2d-67cc-4172-9785-affa44fa2d20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHvfCJjfuRmmE83TC6sCvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5037,
      "cache_read_input_tokens": 58814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5037
      },
      "output_tokens": 32,
      "service_tier": "standard",
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

_source line 46 · 2026-05-22T01:10:29.081Z_

<details><summary>↩ Tool result · `toolu_01TjcH5Fzgt62tdXDzo6YeKE`</summary>

```text
Web search results for query: ""A Concise Agent is Less Expert" Cho Young-Min style features conversational agents 2026 published venue"

Links: [{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://www.catalyzex.com/paper/a-concise-agent-is-less-expert-revealing-side"},{"title":"[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/abs/2601.10809"},{"title":"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents","url":"https://arxiv.org/html/2601.10809"},{"title":"What’s Next for Conversational AI Agents: Trends and Future Outlook in 2026 • QuickBlox","url":"https://quickblox.com/blog/conversational-ai-agents-emerging-trends/"},{"title":"How to Become an Agentic AI Expert in 2026?","url":"https://www.analyticsvidhya.com/blog/2026/01/agentic-ai-expert-learning-path/"},{"title":"The Future of AI Agents: Top Predictions and Trends to Watch in 2026 - Salesforce","url":"https://www.salesforce.com/uk/news/stories/the-future-of-ai-agents-top-predictions-trends-to-watch-in-2026/"},{"title":"How Conversational AI Agents Work in 2026 | Worktual","url":"https://worktual.in/blog/how-conversational-ai-agents-work/"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents"

**Authors:** Young-Min Cho, Yuan Yuan, Sharath Chandra Guntuku, Lyle Ungar

**Publication Date:** January 15, 2026

**Published Venue:** The paper appears to be available on arXiv (paper 2601.10809)

**Key Findings:** The results reveal consistent and structured side effects, such as prompting for conciseness significantly reduces perceived expertise. The study identified 12 frequently used style features through a survey of 127 conversational agent papers from ACL Anthology, and used controlled, synthetic dialogues across task-oriented and open domain settings to quantify how prompting for one style feature causally affects others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "343eadff-c8d5-454e-bd00-19ffdda452f5",
  "tool_use_result": {
    "query": "\"A Concise Agent is Less Expert\" Cho Young-Min style features conversational agents 2026 published venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_016rGEhsCER2Sse7p65L3LbK",
        "content": [
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://www.catalyzex.com/paper/a-concise-agent-is-less-expert-revealing-side"
          },
          {
            "title": "[2601.10809] A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/abs/2601.10809"
          },
          {
            "title": "A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents",
            "url": "https://arxiv.org/html/2601.10809"
          },
          {
            "title": "What’s Next for Conversational AI Agents: Trends and Future Outlook in 2026 • QuickBlox",
            "url": "https://quickblox.com/blog/conversational-ai-agents-emerging-trends/"
          },
          {
            "title": "How to Become an Agentic AI Expert in 2026?",
            "url": "https://www.analyticsvidhya.com/blog/2026/01/agentic-ai-expert-learning-path/"
          },
          {
            "title": "The Future of AI Agents: Top Predictions and Trends to Watch in 2026 - Salesforce",
            "url": "https://www.salesforce.com/uk/news/stories/the-future-of-ai-agents-top-predictions-trends-to-watch-in-2026/"
          },
          {
            "title": "How Conversational AI Agents Work in 2026 | Worktual",
            "url": "https://worktual.in/blog/how-conversational-ai-agents-work/"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Paper Title:** \"A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents\"\n\n**Authors:** Young-Min Cho, Yuan Yuan, Sharath Chandra Guntuku, Lyle Ungar\n\n**Publication Date:** January 15, 2026\n\n**Published Venue:** The paper appears to be available on arXiv (paper 2601.10809)\n\n**Key Findings:** The results reveal consistent and structured side effects, such as prompting for conciseness significantly reduces perceived expertise. The study identified 12 frequently used style features through a survey of 127 conversational agent papers from ACL Anthology, and used controlled, synthetic dialogues across task-oriented and open domain settings to quantify how prompting for one style feature causally affects others."
    ],
    "durationSeconds": 5.681244913000002
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-22T01:10:30.979Z_

<details><summary>↩ Tool result · `toolu_01PYvndNRUJGVjrr7LztMLNC`</summary>

```text
Web search results for query: ""Counterfactual LLM-based Framework" "Measuring Rhetorical Style" Qiu Jingyi 2025 published"

Links: [{"title":"[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/abs/2512.19908"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/html/2512.19908v1"},{"title":"Jingyi Qiu (@JingyiQiu4) / Posts / X","url":"https://x.com/JingyiQiu4"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/pdf/2512.19908"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview","url":"https://openreview.net/forum?id=fiohEI16sf"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"},{"title":"Rhetorical Questions in LLM Representations: A Linear Probing Study","url":"https://arxiv.org/html/2604.14128v1"},{"title":"[Literature Review] Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://www.themoonlight.io/en/review/counterfactual-llm-based-framework-for-measuring-rhetorical-style"},{"title":"COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...","url":"https://openreview.net/pdf/e194fe1dda6ea2aff401bf0f16650a9c7d414fd9.pdf"}]

Based on the search results, I found the paper you're looking for:

"Counterfactual LLM-based Framework for Measuring Rhetorical Style" by Jingyi Qiu and 2 other authors (Hong Chen and Zongyi Li) has been published on arXiv.

**Key Details:**

- **Publication Date:** December 22, 2025
- **ArXiv ID:** 2512.19908
- **Authors:** Jingyi Qiu (School of Information, University of Michigan, Ann Arbor), Hong Chen (School of Information, University of Michigan, Ann Arbor), and Zongyi Li (CSAIL, MIT)

**Paper Summary:**

The framework uses multiple LLM rhetorical personas to generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley–Terry model. The method was applied to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings.

**Key Findings:** The research found that visionary framing significantly predicts downstream attention including citations and media attention, and observed a sharp rise in rhetorical strength after 2023, largely driven by the adoption of LLM-based writing assistance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "4697926f-4126-4622-9abc-ab5ecbde09ec",
  "tool_use_result": {
    "query": "\"Counterfactual LLM-based Framework\" \"Measuring Rhetorical Style\" Qiu Jingyi 2025 published",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mn53BzjuyD3i5fJFMGZ1kh",
        "content": [
          {
            "title": "[2512.19908] Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/abs/2512.19908"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/html/2512.19908v1"
          },
          {
            "title": "Jingyi Qiu (@JingyiQiu4) / Posts / X",
            "url": "https://x.com/JingyiQiu4"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/pdf/2512.19908"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview",
            "url": "https://openreview.net/forum?id=fiohEI16sf"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://www.researchgate.net/publication/399026376_Counterfactual_LLM-based_Framework_for_Measuring_Rhetorical_Style"
          },
          {
            "title": "Rhetorical Questions in LLM Representations: A Linear Probing Study",
            "url": "https://arxiv.org/html/2604.14128v1"
          },
          {
            "title": "[Literature Review] Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://www.themoonlight.io/en/review/counterfactual-llm-based-framework-for-measuring-rhetorical-style"
          },
          {
            "title": "COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...",
            "url": "https://openreview.net/pdf/e194fe1dda6ea2aff401bf0f16650a9c7d414fd9.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Counterfactual LLM-based Framework for Measuring Rhetorical Style\" by Jingyi Qiu and 2 other authors (Hong Chen and Zongyi Li) has been published on arXiv.\n\n**Key Details:**\n\n- **Publication Date:** December 22, 2025\n- **ArXiv ID:** 2512.19908\n- **Authors:** Jingyi Qiu (School of Information, University of Michigan, Ann Arbor), Hong Chen (School of Information, University of Michigan, Ann Arbor), and Zongyi Li (CSAIL, MIT)\n\n**Paper Summary:**\n\nThe framework uses multiple LLM rhetorical personas to generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and the outcomes are aggregated using a Bradley–Terry model. The method was applied to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings.\n\n**Key Findings:** The research found that visionary framing significantly predicts downstream attention including citations and media attention, and observed a sharp rise in rhetorical strength after 2023, largely driven by the adoption of LLM-based writing assistance."
    ],
    "durationSeconds": 6.5067116360000075
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-22T01:10:31.016Z_

<details><summary>↩ Tool result · `toolu_01CfoinyzaT3f6bdbKgBALor`</summary>

```text
Web search results for query: ""Large Language Models are not Fair Evaluators" Wang Peiyi 2023 published venue conference"

Links: [{"title":"[2305.17926v1] Large Language Models are not Fair Evaluators","url":"https://arxiv.org/abs/2305.17926v1"},{"title":"[2305.17926] Large Language Models are not Fair Evaluators","url":"https://arxiv.org/abs/2305.17926"},{"title":"[2305.17926v2] Large Language Models are not Fair Evaluators","url":"https://arxiv.org/abs/2305.17926v2"},{"title":"[PDF] Large Language Models are not Fair Evaluators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Large-Language-Models-are-not-Fair-Evaluators-Wang-Li/38d64919ba526868a850a0e5f6239d4c474b7e7e"},{"title":"Large Language Models are not Fair Evaluators | DeepAI","url":"https://deepai.org/publication/large-language-models-are-not-fair-evaluators"},{"title":"Large Language Models are not Fair Evaluators","url":"https://arxiv.org/pdf/2305.17926"},{"title":"Large Language Models are not Fair Evaluators - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.511/"},{"title":"Paper page - Large Language Models are not Fair Evaluators","url":"https://huggingface.co/papers/2305.17926"},{"title":"Large Language Models are not Fair Evaluators - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230517926W/abstract"}]

Based on the search results, here's the information about the paper "Large Language Models are not Fair Evaluators" by Wang Peiyi and colleagues:

**Published Venue/Conference:** The paper was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024), though it was initially published on May 29, 2023.

**Key Details:**

- **Authors:** Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu, Tianyu Liu, and Zhifang Sui

- **Main Finding:** The paper uncovers a positional bias in the evaluation paradigm of adopting large language models (LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models.

- **Contribution:** The paper proposes a simple yet effective calibration framework to address the discovered positional bias, with extensive experiments demonstrating that the approach successfully alleviates evaluation bias, resulting in closer alignment with human judgments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "42236655-ede5-427c-931c-617251645d03",
  "tool_use_result": {
    "query": "\"Large Language Models are not Fair Evaluators\" Wang Peiyi 2023 published venue conference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TxxkACidyYHySWMq9ZjWrG",
        "content": [
          {
            "title": "[2305.17926v1] Large Language Models are not Fair Evaluators",
            "url": "https://arxiv.org/abs/2305.17926v1"
          },
          {
            "title": "[2305.17926] Large Language Models are not Fair Evaluators",
            "url": "https://arxiv.org/abs/2305.17926"
          },
          {
            "title": "[2305.17926v2] Large Language Models are not Fair Evaluators",
            "url": "https://arxiv.org/abs/2305.17926v2"
          },
          {
            "title": "[PDF] Large Language Models are not Fair Evaluators | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Large-Language-Models-are-not-Fair-Evaluators-Wang-Li/38d64919ba526868a850a0e5f6239d4c474b7e7e"
          },
          {
            "title": "Large Language Models are not Fair Evaluators | DeepAI",
            "url": "https://deepai.org/publication/large-language-models-are-not-fair-evaluators"
          },
          {
            "title": "Large Language Models are not Fair Evaluators",
            "url": "https://arxiv.org/pdf/2305.17926"
          },
          {
            "title": "Large Language Models are not Fair Evaluators - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.511/"
          },
          {
            "title": "Paper page - Large Language Models are not Fair Evaluators",
            "url": "https://huggingface.co/papers/2305.17926"
          },
          {
            "title": "Large Language Models are not Fair Evaluators - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230517926W/abstract"
          }
        ]
      },
      "Based on the search results, here's the information about the paper \"Large Language Models are not Fair Evaluators\" by Wang Peiyi and colleagues:\n\n**Published Venue/Conference:** The paper was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024), though it was initially published on May 29, 2023.\n\n**Key Details:**\n\n- **Authors:** Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu, Tianyu Liu, and Zhifang Sui\n\n- **Main Finding:** The paper uncovers a positional bias in the evaluation paradigm of adopting large language models (LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models.\n\n- **Contribution:** The paper proposes a simple yet effective calibration framework to address the discovered positional bias, with extensive experiments demonstrating that the approach successfully alleviates evaluation bias, resulting in closer alignment with human judgments."
    ],
    "durationSeconds": 4.783466193000001
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-22T01:10:32.360Z_

<details><summary>↩ Tool result · `toolu_01HoXLPe2cLBW25qbUkwdYL5`</summary>

```text
Web search results for query: ""Judging the Judges Systematic Evaluation" bias mitigation LLM-as-a-Judge Soumik 2026 published"

Links: [{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178"},{"title":"LLM Evaluators Recognize and Favor Their Own Generations","url":"https://www.researchgate.net/publication/397200002_LLM_Evaluators_Recognize_and_Favor_Their_Own_Generations"},{"title":"GitHub - sksoumik/llm-as-judge: Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines · GitHub","url":"https://github.com/sksoumik/llm-as-judge"},{"title":"Judging the Judges: A Systematic Evaluation of Bi… - arXiv","url":"https://arxiv-troller.com/paper/3154455/"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Miti- gation Strategies in LLM-as-a-Judge Pipelines | OpenReview","url":"https://openreview.net/forum?id=QF4lAmG4zc"},{"title":"[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/abs/2604.23178"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Miti-","url":"https://arxiv.org/pdf/2604.23178"},{"title":"Mitigating the Bias of Large Language Model Evaluation","url":"https://arxiv.org/pdf/2409.16788"}]

I found the paper! Here are the key details about "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines":

**Publication Details:**
The paper was published on arXiv on April 25, 2026 (arXiv:2604.23178v1) by Sadman Kabir Soumik, an independent researcher.

**Research Overview:**
LLM-as-a-Judge has become the dominant paradigm for evaluating language model outputs, yet LLM judges exhibit systematic biases that compromise evaluation reliability.

**Study Scope:**
The study compares nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta), three benchmarks (MT-Bench n=400, LLMBar n=200, custom n=225), and four bias types.

**Key Findings:**
Style bias is the dominant bias (0.76–0.92 across all models), far exceeding position bias (≤0.04), yet has received minimal research attention. All models show a conciseness preference on expansion pairs, but truncation controls confirm they correctly distinguish quality from length (0.92–1.00 accuracy), suggesting quality-sensitive evaluation rather than a simple length bias.

The paper also includes an open-source framework and controlled dataset, with code available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "74b2f40c-6e65-469c-9a5a-f2f9c849e8f1",
  "tool_use_result": {
    "query": "\"Judging the Judges Systematic Evaluation\" bias mitigation LLM-as-a-Judge Soumik 2026 published",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EtrBTcCT97CDc2jrPZJFah",
        "content": [
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/html/2604.23178"
          },
          {
            "title": "LLM Evaluators Recognize and Favor Their Own Generations",
            "url": "https://www.researchgate.net/publication/397200002_LLM_Evaluators_Recognize_and_Favor_Their_Own_Generations"
          },
          {
            "title": "GitHub - sksoumik/llm-as-judge: Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines · GitHub",
            "url": "https://github.com/sksoumik/llm-as-judge"
          },
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bi… - arXiv",
            "url": "https://arxiv-troller.com/paper/3154455/"
          },
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bias Miti- gation Strategies in LLM-as-a-Judge Pipelines | OpenReview",
            "url": "https://openreview.net/forum?id=QF4lAmG4zc"
          },
          {
            "title": "[2604.23178] Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/abs/2604.23178"
          },
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bias Miti-",
            "url": "https://arxiv.org/pdf/2604.23178"
          },
          {
            "title": "Mitigating the Bias of Large Language Model Evaluation",
            "url": "https://arxiv.org/pdf/2409.16788"
          }
        ]
      },
      "I found the paper! Here are the key details about \"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines\":\n\n**Publication Details:**\nThe paper was published on arXiv on April 25, 2026 (arXiv:2604.23178v1) by Sadman Kabir Soumik, an independent researcher.\n\n**Research Overview:**\nLLM-as-a-Judge has become the dominant paradigm for evaluating language model outputs, yet LLM judges exhibit systematic biases that compromise evaluation reliability.\n\n**Study Scope:**\nThe study compares nine debiasing strategies across five judge models from four provider families (Google, Anthropic, OpenAI, Meta), three benchmarks (MT-Bench n=400, LLMBar n=200, custom n=225), and four bias types.\n\n**Key Findings:**\nStyle bias is the dominant bias (0.76–0.92 across all models), far exceeding position bias (≤0.04), yet has received minimal research attention. All models show a conciseness preference on expansion pairs, but truncation controls confirm they correctly distinguish quality from length (0.92–1.00 accuracy), suggesting quality-sensitive evaluation rather than a simple length bias.\n\nThe paper also includes an open-source framework and controlled dataset, with code available on GitHub."
    ],
    "durationSeconds": 6.924110886000009
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-22T01:10:42.389Z_

<details><summary>↩ Tool result · `toolu_01MeAdqpBp1pu5x6kxchKyWf`</summary>

```text
Web search results for query: "FairJudge "Adaptive Debiased Consistent" LLM-as-a-Judge Yang Bo 2026 published"

Links: [{"title":"[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/abs/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/pdf/2602.06625"},{"title":"FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge","url":"https://arxiv.org/html/2602.06625"},{"title":"Paper page - Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training","url":"https://huggingface.co/papers/2603.12246"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"}]

Based on the search results, I found the paper you're looking for:

**FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge** is a paper by Bo Yang, Lanfei Feng, Yunkui Chen, Xiao Xu, Yu Zhang, and Shijian Li from the College of Computer Science at Zhejiang University that proposes FairJudge, an adaptive, debiased, and consistent LLM-as-a-Judge.

The paper was published on February 6, 2026, and is available on arXiv (paper ID: 2602.06625).

The research addresses three fundamental limitations in existing LLM-as-a-Judge systems: limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes.

The approach constructs a high-information-density judging dataset and adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "6b8e1610-1777-4533-bd2c-6bc626c70919",
  "tool_use_result": {
    "query": "FairJudge \"Adaptive Debiased Consistent\" LLM-as-a-Judge Yang Bo 2026 published",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fb7PmLSmiwEbW9zGoEwFYN",
        "content": [
          {
            "title": "[2602.06625] FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2602.06625"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2602.06625"
          },
          {
            "title": "FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2602.06625"
          },
          {
            "title": "Paper page - Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training",
            "url": "https://huggingface.co/papers/2603.12246"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge** is a paper by Bo Yang, Lanfei Feng, Yunkui Chen, Xiao Xu, Yu Zhang, and Shijian Li from the College of Computer Science at Zhejiang University that proposes FairJudge, an adaptive, debiased, and consistent LLM-as-a-Judge.\n\nThe paper was published on February 6, 2026, and is available on arXiv (paper ID: 2602.06625).\n\nThe research addresses three fundamental limitations in existing LLM-as-a-Judge systems: limited adaptivity to task- and domain-specific evaluation criteria, systematic biases driven by non-semantic cues such as position, length, format, and model provenance, and evaluation inconsistency that leads to contradictory judgments across different evaluation modes.\n\nThe approach constructs a high-information-density judging dataset and adopts a curriculum-style SFT-DPO-GRPO training paradigm that progressively aligns rubric adherence, bias mitigation, and cross-mode consistency."
    ],
    "durationSeconds": 20.457585234000014
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Great findings! Let me search for a few more arXiv papers to check if they have published versions.

Key findings so far:
1. tripathi2025pairwise - Published at "Second Conference on Language Modeling" 2025. Need to update.
2. wang2026fairjudge - Still arXiv only
3. casse2026concise - Still arXiv only
4. counterfactual2025rhetorical - Has OpenReview submission, checking if accepted. Still arXiv only for now.
5. soumik2026judging - Still arXiv only


6. wang2023faireval - Published at ACL 2024! Need to update.

Continuing to check the remaining papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "73e588a8-c457-407f-a691-f4eac30db7a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 52_

Good findings. `wang2023faireval` was published at ACL 2024 and `tripathi2025pairwise` at COLM 2025. Let me search for the remaining arXiv papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "5a818cfa-d0e7-460c-8009-c82eee7673f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014Yb4FHdA8Cz1e5ibtTrKJ2`</summary>

```json
{
  "query": "CalibraEval \"Calibrating Prediction Distribution\" LLM judges Li Haitao 2024 published venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "09e7f928-c9bf-4a91-a424-61e5015ff537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016HcqVE3W3mo4ursSUhUCbL`</summary>

```json
{
  "query": "\"Justice or Prejudice\" \"Quantifying Biases\" LLM-as-a-Judge Ye Jiayi 2024 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0e4f0342-37d2-4391-aa1a-a5fe4ae127a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F14DRKRYvr4jgKhjh9Vx2D`</summary>

```json
{
  "query": "\"Evaluation of Text Generation A Survey\" Celikyilmaz 2020 published journal venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "cdf751d3-6eac-463c-b410-a490269e2a81",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N5wP6TufgDXnB4SyQeNaSL`</summary>

```json
{
  "query": "\"Large Language Models are Inconsistent and Biased Evaluators\" Stureborg 2024 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "ac6f0cfb-2240-457a-8403-193325a2c4f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 57_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013GtU3upVHhsXSHm34ArCxK`</summary>

```json
{
  "query": "DeBERTaV3 \"Improving DeBERTa\" ELECTRA He Pengcheng 2021 published venue ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "5389ec29-aa83-4572-9258-a97458e941a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 58 · 2026-05-22T01:11:03.523Z_

<details><summary>↩ Tool result · `toolu_014Yb4FHdA8Cz1e5ibtTrKJ2`</summary>

```text
Web search results for query: "CalibraEval "Calibrating Prediction Distribution" LLM judges Li Haitao 2024 published venue conference"

Links: [{"title":"[2410.15393] CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges","url":"https://arxiv.org/abs/2410.15393"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection   Bias in LLMs-as-Judges","url":"https://arxiv.org/pdf/2410.15393"},{"title":"‪Calibraeval: Calibrating prediction distribution to mitigate selection bias in llms-as-judges‬","url":"https://scholar.google.com/citations?view_op=view_citation&hl=en&user=m88SZGgAAAAJ&citation_for_view=m88SZGgAAAAJ:f2IySw72cVMC"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges | alphaXiv","url":"https://www.alphaxiv.org/overview/2410.15393v1"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.808/"},{"title":"GitHub - CSHaitao/CalibraEval: The official repo for CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges","url":"https://github.com/CSHaitao/CalibraEval"},{"title":"Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction","url":"https://arxiv.org/html/2509.18658v1"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges | Request PDF","url":"https://www.researchgate.net/publication/394299911_CalibraEval_Calibrating_Prediction_Distribution_to_Mitigate_Selection_Bias_in_LLMs-as-Judges"},{"title":"CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges","url":"https://arxiv.org/html/2410.15393v1"}]

Based on the search results, here is the information about CalibraEval:

**Paper Title:** CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges

**Authors:** Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, Qian Dong, Yiqun Liu

**Published Venue:** ACL 2025

**Publication Date:** October 20, 2024

**Overview:** CalibraEval is a novel label-free method for mitigating selection bias during inference that reformulates debiasing as an optimization task aimed at adjusting observed prediction distributions to align with unbiased prediction distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "55cef9ba-5366-4666-83f7-434894ed0c9a",
  "tool_use_result": {
    "query": "CalibraEval \"Calibrating Prediction Distribution\" LLM judges Li Haitao 2024 published venue conference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01B55oWuFApXt7ozhTygeFnh",
        "content": [
          {
            "title": "[2410.15393] CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges",
            "url": "https://arxiv.org/abs/2410.15393"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection   Bias in LLMs-as-Judges",
            "url": "https://arxiv.org/pdf/2410.15393"
          },
          {
            "title": "‪Calibraeval: Calibrating prediction distribution to mitigate selection bias in llms-as-judges‬",
            "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=m88SZGgAAAAJ&citation_for_view=m88SZGgAAAAJ:f2IySw72cVMC"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2410.15393v1"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.808/"
          },
          {
            "title": "GitHub - CSHaitao/CalibraEval: The official repo for CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges",
            "url": "https://github.com/CSHaitao/CalibraEval"
          },
          {
            "title": "Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction",
            "url": "https://arxiv.org/html/2509.18658v1"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges | Request PDF",
            "url": "https://www.researchgate.net/publication/394299911_CalibraEval_Calibrating_Prediction_Distribution_to_Mitigate_Selection_Bias_in_LLMs-as-Judges"
          },
          {
            "title": "CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges",
            "url": "https://arxiv.org/html/2410.15393v1"
          }
        ]
      },
      "Based on the search results, here is the information about CalibraEval:\n\n**Paper Title:** CalibraEval: Calibrating Prediction Distribution to Mitigate Selection Bias in LLMs-as-Judges\n\n**Authors:** Haitao Li, Junjie Chen, Qingyao Ai, Zhumin Chu, Yujia Zhou, Qian Dong, Yiqun Liu\n\n**Published Venue:** ACL 2025\n\n**Publication Date:** October 20, 2024\n\n**Overview:** CalibraEval is a novel label-free method for mitigating selection bias during inference that reformulates debiasing as an optimization task aimed at adjusting observed prediction distributions to align with unbiased prediction distributions."
    ],
    "durationSeconds": 4.458076306000002
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RCy7dypSNf3zPyjtpkUKpn`</summary>

```json
{
  "query": "\"Judging the Judges Systematic Study Position Bias\" Shi Lin LLM 2024 published venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "ce7cc7d0-09b5-4ef0-8a31-8b70895f505d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HtiVAkSymHLqxmKBQwuYnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3098,
      "cache_creation_input_tokens": 1775,
      "cache_read_input_tokens": 63851,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1775
      },
      "output_tokens": 9,
      "service_tier": "standard",
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

_source line 60 · 2026-05-22T01:11:03.930Z_

<details><summary>↩ Tool result · `toolu_016HcqVE3W3mo4ursSUhUCbL`</summary>

```text
Web search results for query: ""Justice or Prejudice" "Quantifying Biases" LLM-as-a-Judge Ye Jiayi 2024 published venue"

Links: [{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://llm-judge-bias.github.io/"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge [Quick Review]","url":"https://liner.com/review/justice-or-prejudice-quantifying-biases-in-llmasajudge"},{"title":"[2410.02736v1] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.02736v1"},{"title":"[2410.02736] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/abs/2410.02736"},{"title":"[PDF] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge | Semantic Scholar","url":"https://www.semanticscholar.org/paper/e142887ab6516654f25e233a3e661eddac123630"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/pdf/2410.02736"},{"title":"NeurIPS Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://neurips.cc/virtual/2024/106162"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://arxiv.org/html/2410.02736v1"},{"title":"ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://iclr.cc/virtual/2025/poster/31088"}]

Based on the search results, I found the paper you're looking for. Here's the information about the published venue:

"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" by Jiayi Ye and co-authors was published at ICLR in October 2024. Additionally, the paper is also being presented at NeurIPS 2024, and it appears at ICLR 2025 as well.

The paper is also available as an arXiv preprint (arXiv:2410.02736).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "cf5947b9-b86a-433e-b47c-c5d203d4c6ce",
  "tool_use_result": {
    "query": "\"Justice or Prejudice\" \"Quantifying Biases\" LLM-as-a-Judge Ye Jiayi 2024 published venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PaAdfDwnRYqEEzNRKdRBsh",
        "content": [
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://llm-judge-bias.github.io/"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge [Quick Review]",
            "url": "https://liner.com/review/justice-or-prejudice-quantifying-biases-in-llmasajudge"
          },
          {
            "title": "[2410.02736v1] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2410.02736v1"
          },
          {
            "title": "[2410.02736] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2410.02736"
          },
          {
            "title": "[PDF] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/e142887ab6516654f25e233a3e661eddac123630"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2410.02736"
          },
          {
            "title": "NeurIPS Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://neurips.cc/virtual/2024/106162"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2410.02736v1"
          },
          {
            "title": "ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://iclr.cc/virtual/2025/poster/31088"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's the information about the published venue:\n\n\"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" by Jiayi Ye and co-authors was published at ICLR in October 2024. Additionally, the paper is also being presented at NeurIPS 2024, and it appears at ICLR 2025 as well.\n\nThe paper is also available as an arXiv preprint (arXiv:2410.02736)."
    ],
    "durationSeconds": 3.868179866999999
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-22T01:11:04.685Z_

<details><summary>↩ Tool result · `toolu_01F14DRKRYvr4jgKhjh9Vx2D`</summary>

```text
Web search results for query: ""Evaluation of Text Generation A Survey" Celikyilmaz 2020 published journal venue"

Links: [{"title":"[PDF] Evaluation of Text Generation: A Survey | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Evaluation-of-Text-Generation:-A-Survey-Celikyilmaz-Clark/e23cb51f50f749320b9122fb5f75113b4d192c0a"},{"title":"Reference-free Evaluation Metrics for Text Generation: A Survey","url":"https://arxiv.org/html/2501.12011v1"},{"title":"[2006.14799v2] Evaluation of Text Generation: A Survey","url":"https://arxiv.org/abs/2006.14799v2"},{"title":"[2006.14799] Evaluation of Text Generation: A Survey","url":"https://arxiv.org/abs/2006.14799"},{"title":"A Systematic survey on automated text generation tools and techniques: application, evaluation, and challenges | Multimedia Tools and Applications | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11042-023-15224-0"},{"title":"Evaluation of Text Generation: A Survey | Request PDF","url":"https://www.researchgate.net/publication/342520480_Evaluation_of_Text_Generation_A_Survey"},{"title":"Evaluation of Text Generation: A Survey","url":"https://arxiv.org/pdf/2006.14799"},{"title":"Evaluation of Text Generation: A Survey - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200614799C/abstract"},{"title":"Evaluation of Text Generation: A Survey | DeepAI","url":"https://deepai.org/publication/evaluation-of-text-generation-a-survey"},{"title":"Pre-Trained Language Models for Text Generation: A Survey | ACM Computing Surveys","url":"https://dl.acm.org/doi/abs/10.1145/3649449"}]

Based on the search results, the paper "Evaluation of Text Generation: A Survey" by Asli Celikyilmaz, Elizabeth Clark, and Jianfeng Gao was published on arXiv in 2020. Specifically, it was first posted on arXiv on June 26, 2020.

The paper was published as an arXiv preprint with ID abs/2006.14799, rather than in a traditional peer-reviewed journal venue. This is a preprint on arXiv, which is an open-access repository for research papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "f043fbb5-1552-49cd-976b-b441020d977c",
  "tool_use_result": {
    "query": "\"Evaluation of Text Generation A Survey\" Celikyilmaz 2020 published journal venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GBYLBAPZMAmc1kSxjPBbfM",
        "content": [
          {
            "title": "[PDF] Evaluation of Text Generation: A Survey | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Evaluation-of-Text-Generation:-A-Survey-Celikyilmaz-Clark/e23cb51f50f749320b9122fb5f75113b4d192c0a"
          },
          {
            "title": "Reference-free Evaluation Metrics for Text Generation: A Survey",
            "url": "https://arxiv.org/html/2501.12011v1"
          },
          {
            "title": "[2006.14799v2] Evaluation of Text Generation: A Survey",
            "url": "https://arxiv.org/abs/2006.14799v2"
          },
          {
            "title": "[2006.14799] Evaluation of Text Generation: A Survey",
            "url": "https://arxiv.org/abs/2006.14799"
          },
          {
            "title": "A Systematic survey on automated text generation tools and techniques: application, evaluation, and challenges | Multimedia Tools and Applications | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11042-023-15224-0"
          },
          {
            "title": "Evaluation of Text Generation: A Survey | Request PDF",
            "url": "https://www.researchgate.net/publication/342520480_Evaluation_of_Text_Generation_A_Survey"
          },
          {
            "title": "Evaluation of Text Generation: A Survey",
            "url": "https://arxiv.org/pdf/2006.14799"
          },
          {
            "title": "Evaluation of Text Generation: A Survey - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv200614799C/abstract"
          },
          {
            "title": "Evaluation of Text Generation: A Survey | DeepAI",
            "url": "https://deepai.org/publication/evaluation-of-text-generation-a-survey"
          },
          {
            "title": "Pre-Trained Language Models for Text Generation: A Survey | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/abs/10.1145/3649449"
          }
        ]
      },
      "Based on the search results, the paper \"Evaluation of Text Generation: A Survey\" by Asli Celikyilmaz, Elizabeth Clark, and Jianfeng Gao was published on arXiv in 2020. Specifically, it was first posted on arXiv on June 26, 2020.\n\nThe paper was published as an arXiv preprint with ID abs/2006.14799, rather than in a traditional peer-reviewed journal venue. This is a preprint on arXiv, which is an open-access repository for research papers."
    ],
    "durationSeconds": 3.582084792999987
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-22T01:11:05.669Z_

<details><summary>↩ Tool result · `toolu_01N5wP6TufgDXnB4SyQeNaSL`</summary>

```text
Web search results for query: ""Large Language Models are Inconsistent and Biased Evaluators" Stureborg 2024 published venue"

Links: [{"title":"Large Language Models are Inconsistent and Biased Evaluators | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/large-language-models-are-inconsistent-biased-evaluators"},{"title":"[2405.01724] Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/abs/2405.01724"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://www.catalyzex.com/paper/large-language-models-are-inconsistent-and"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://paperreading.club/page?id=225338"},{"title":"fly51fly on X: \"[CL] Large Language Models are Inconsistent and Biased Evaluators R Stureborg, D Alikaniotis, Y Suhara [Grammarly &amp; NVIDIA] (2024) https://t.co/hkfoLgU43Q - LLMs show familiarity bias, preferring texts with lower perplexity that they are more familiar with. - LLMs exhibit score https://t.co/EB7NZOh2nk\" / X","url":"https://x.com/fly51fly/status/1787369849922130004"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/pdf/2405.01724"},{"title":"Large Language Models are Inconsistent and Biased Evaluators | PromptLayer","url":"https://www.promptlayer.com/research-papers/large-language-models-are-inconsistent-and-biased-evaluators"},{"title":"Large Language Models are Inconsistent and Biased Evaluators - arXiv.gg","url":"https://arxiv.gg/abs/2405.01724"},{"title":"Large Language Models are Inconsistent a...","url":"https://axi.lims.ac.uk/paper/2405.01724"},{"title":"Large Language Models are Inconsistent and Biased Evaluators","url":"https://arxiv.org/html/2405.01724v1"}]

Based on the search results, the paper "Large Language Models are Inconsistent and Biased Evaluators" by Rickard Stureborg was published on May 2, 2024. However, the search results indicate this was posted to arXiv rather than a traditional conference or journal venue. The paper is classified under Computer Science categories (cs.CL and cs.AI), suggesting it was published as a preprint on arXiv (arxiv.org/abs/2405.01724).

The paper does not appear to have been published in a traditional peer-reviewed conference or journal venue based on the available search results. If you're looking for information about where this paper may have been subsequently published or presented at a conference, I'd be happy to search for more recent information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "b7eaaee0-f886-490c-a325-0466a5c2b715",
  "tool_use_result": {
    "query": "\"Large Language Models are Inconsistent and Biased Evaluators\" Stureborg 2024 published venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_016UTwWEQLKog1TQkGEQAVrs",
        "content": [
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/large-language-models-are-inconsistent-biased-evaluators"
          },
          {
            "title": "[2405.01724] Large Language Models are Inconsistent and Biased Evaluators",
            "url": "https://arxiv.org/abs/2405.01724"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators",
            "url": "https://www.catalyzex.com/paper/large-language-models-are-inconsistent-and"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators",
            "url": "https://paperreading.club/page?id=225338"
          },
          {
            "title": "fly51fly on X: \"[CL] Large Language Models are Inconsistent and Biased Evaluators R Stureborg, D Alikaniotis, Y Suhara [Grammarly &amp; NVIDIA] (2024) https://t.co/hkfoLgU43Q - LLMs show familiarity bias, preferring texts with lower perplexity that they are more familiar with. - LLMs exhibit score https://t.co/EB7NZOh2nk\" / X",
            "url": "https://x.com/fly51fly/status/1787369849922130004"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators",
            "url": "https://arxiv.org/pdf/2405.01724"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators | PromptLayer",
            "url": "https://www.promptlayer.com/research-papers/large-language-models-are-inconsistent-and-biased-evaluators"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators - arXiv.gg",
            "url": "https://arxiv.gg/abs/2405.01724"
          },
          {
            "title": "Large Language Models are Inconsistent a...",
            "url": "https://axi.lims.ac.uk/paper/2405.01724"
          },
          {
            "title": "Large Language Models are Inconsistent and Biased Evaluators",
            "url": "https://arxiv.org/html/2405.01724v1"
          }
        ]
      },
      "Based on the search results, the paper \"Large Language Models are Inconsistent and Biased Evaluators\" by Rickard Stureborg was published on May 2, 2024. However, the search results indicate this was posted to arXiv rather than a traditional conference or journal venue. The paper is classified under Computer Science categories (cs.CL and cs.AI), suggesting it was published as a preprint on arXiv (arxiv.org/abs/2405.01724).\n\nThe paper does not appear to have been published in a traditional peer-reviewed conference or journal venue based on the available search results. If you're looking for information about where this paper may have been subsequently published or presented at a conference, I'd be happy to search for more recent information."
    ],
    "durationSeconds": 4.18179685699998
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-22T01:11:07.772Z_

<details><summary>↩ Tool result · `toolu_013GtU3upVHhsXSHm34ArCxK`</summary>

```text
Web search results for query: "DeBERTaV3 "Improving DeBERTa" ELECTRA He Pengcheng 2021 published venue ICLR"

Links: [{"title":"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing [Quick Review]","url":"https://liner.com/review/debertav3-improving-deberta-using-electrastyle-pretraining-with-gradientdisentangled-embedding-sharing"},{"title":"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | DeepAI","url":"https://deepai.org/publication/debertav3-improving-deberta-using-electra-style-pre-training-with-gradient-disentangled-embedding-sharing"},{"title":"GitHub - microsoft/DeBERTa: The implementation of DeBERTa · GitHub","url":"https://github.com/microsoft/DeBERTa"},{"title":"[PDF] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DeBERTaV3:-Improving-DeBERTa-using-ELECTRA-Style-He-Gao/972706306f85b1bfb40c7d35c796ad5174eb0c9c"},{"title":"(PDF) DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://www.researchgate.net/publication/356375694_DeBERTaV3_Improving_DeBERTa_using_ELECTRA-Style_Pre-Training_with_Gradient-Disentangled_Embedding_Sharing"},{"title":"Published as a conference paper at ICLR 2023 DEBERTAV3: IMPROVING DEBERTA USING","url":"https://arxiv.org/pdf/2111.09543"},{"title":"microsoft/deberta-v3-base · Hugging Face","url":"https://huggingface.co/microsoft/deberta-v3-base"},{"title":"[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://arxiv.org/abs/2111.09543"},{"title":"DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | OpenReview","url":"https://openreview.net/forum?id=sE7-XhLxHA"},{"title":"ICLR Poster DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing","url":"https://iclr.cc/virtual/2023/poster/11295"}]

Based on the search results, here's what I found about the paper you're looking for:

**Title:** DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing

**Authors:** Pengcheng He, Jianfeng Gao, Weizhu Chen

**Published Venue:** The DeBERTaV3 paper is accepted by ICLR 2023

**Publication Date:** November 18, 2021 (note: the paper was preprinted in 2021 but formally published at ICLR in 2023)

**Key Contributions:** DeBERTaV3 integrates DeBERTa's disentangled attention with ELECTRA's RTD objective, replacing masked language modeling for improved pre-training sample efficiency. A novel Gradient-Disentangled Embedding Sharing (GDES) method is introduced to resolve the "tug-of-war" dynamics in RTD, allowing generators and discriminators to share embeddings without conflicting gradient updates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "f53797a0-77d5-4ea1-94d2-885522facc52",
  "tool_use_result": {
    "query": "DeBERTaV3 \"Improving DeBERTa\" ELECTRA He Pengcheng 2021 published venue ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_017RikiTL5eVmJmo9xaxNxeH",
        "content": [
          {
            "title": "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing [Quick Review]",
            "url": "https://liner.com/review/debertav3-improving-deberta-using-electrastyle-pretraining-with-gradientdisentangled-embedding-sharing"
          },
          {
            "title": "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | DeepAI",
            "url": "https://deepai.org/publication/debertav3-improving-deberta-using-electra-style-pre-training-with-gradient-disentangled-embedding-sharing"
          },
          {
            "title": "GitHub - microsoft/DeBERTa: The implementation of DeBERTa · GitHub",
            "url": "https://github.com/microsoft/DeBERTa"
          },
          {
            "title": "[PDF] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DeBERTaV3:-Improving-DeBERTa-using-ELECTRA-Style-He-Gao/972706306f85b1bfb40c7d35c796ad5174eb0c9c"
          },
          {
            "title": "(PDF) DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing",
            "url": "https://www.researchgate.net/publication/356375694_DeBERTaV3_Improving_DeBERTa_using_ELECTRA-Style_Pre-Training_with_Gradient-Disentangled_Embedding_Sharing"
          },
          {
            "title": "Published as a conference paper at ICLR 2023 DEBERTAV3: IMPROVING DEBERTA USING",
            "url": "https://arxiv.org/pdf/2111.09543"
          },
          {
            "title": "microsoft/deberta-v3-base · Hugging Face",
            "url": "https://huggingface.co/microsoft/deberta-v3-base"
          },
          {
            "title": "[2111.09543] DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing",
            "url": "https://arxiv.org/abs/2111.09543"
          },
          {
            "title": "DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing | OpenReview",
            "url": "https://openreview.net/forum?id=sE7-XhLxHA"
          },
          {
            "title": "ICLR Poster DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing",
            "url": "https://iclr.cc/virtual/2023/poster/11295"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper you're looking for:\n\n**Title:** DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing\n\n**Authors:** Pengcheng He, Jianfeng Gao, Weizhu Chen\n\n**Published Venue:** The DeBERTaV3 paper is accepted by ICLR 2023\n\n**Publication Date:** November 18, 2021 (note: the paper was preprinted in 2021 but formally published at ICLR in 2023)\n\n**Key Contributions:** DeBERTaV3 integrates DeBERTa's disentangled attention with ELECTRA's RTD objective, replacing masked language modeling for improved pre-training sample efficiency. A novel Gradient-Disentangled Embedding Sharing (GDES) method is introduced to resolve the \"tug-of-war\" dynamics in RTD, allowing generators and discriminators to share embeddings without conflicting gradient updates."
    ],
    "durationSeconds": 5.237294461000012
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-22T01:11:09.081Z_

<details><summary>↩ Tool result · `toolu_01RCy7dypSNf3zPyjtpkUKpn`</summary>

```text
Web search results for query: ""Judging the Judges Systematic Study Position Bias" Shi Lin LLM 2024 published venue conference"

Links: [{"title":"[2406.07791v7] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2406.07791v7"},{"title":"[2406.07791] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2406.07791"},{"title":"[2406.07791v8] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/abs/2406.07791v8"},{"title":"[2406.07791v6] Judging the Judges: A Systematic Investigation of Position Bias in Pairwise Comparative Assessments by LLMs","url":"https://web3.arxiv.org/abs/2406.07791v6"},{"title":"Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.18/"},{"title":"Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://arxiv.org/html/2406.07791v9"},{"title":"Judging the Judges: A Systematic Investigation of Position Bias in Pairwise Comparative Assessments by LLMs | OpenReview","url":"https://openreview.net/forum?id=y3jJmrKWQ4"},{"title":"A Systematic Study of Position Bias in LLM-as-a-Judge","url":"https://aclanthology.org/2025.ijcnlp-long.18.pdf"},{"title":"Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge | Request PDF","url":"https://www.researchgate.net/publication/402590616_Judging_the_Judges_A_Systematic_Study_of_Position_Bias_in_LLM-as-a-Judge"}]

Based on the search results, I found the information about this paper:

**Paper Details:**
- **Title:** Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge
- **Authors:** Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, and Soroush Vosoughi
- **Published Venue/Conference:** Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2025), Mumbai, India
- **Submission Date:** Submitted on 12 Jun 2024

**Overview:**
The study addresses position bias—a tendency to favor solutions based on their position in the prompt—in LLM-as-a-Judge evaluations. It introduces a systematic framework to examine position bias in pairwise comparisons, focusing on repetition stability, position consistency, and preference fairness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "17007c97-136c-4501-a356-f0c8431d01f8",
  "tool_use_result": {
    "query": "\"Judging the Judges Systematic Study Position Bias\" Shi Lin LLM 2024 published venue conference",
    "results": [
      {
        "tool_use_id": "srvtoolu_0154ywKcmtBTMnNWGhUwHCu3",
        "content": [
          {
            "title": "[2406.07791v7] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2406.07791v7"
          },
          {
            "title": "[2406.07791] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2406.07791"
          },
          {
            "title": "[2406.07791v8] Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2406.07791v8"
          },
          {
            "title": "[2406.07791v6] Judging the Judges: A Systematic Investigation of Position Bias in Pairwise Comparative Assessments by LLMs",
            "url": "https://web3.arxiv.org/abs/2406.07791v6"
          },
          {
            "title": "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge - ACL Anthology",
            "url": "https://aclanthology.org/2025.ijcnlp-long.18/"
          },
          {
            "title": "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2406.07791v9"
          },
          {
            "title": "Judging the Judges: A Systematic Investigation of Position Bias in Pairwise Comparative Assessments by LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=y3jJmrKWQ4"
          },
          {
            "title": "A Systematic Study of Position Bias in LLM-as-a-Judge",
            "url": "https://aclanthology.org/2025.ijcnlp-long.18.pdf"
          },
          {
            "title": "Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge | Request PDF",
            "url": "https://www.researchgate.net/publication/402590616_Judging_the_Judges_A_Systematic_Study_of_Position_Bias_in_LLM-as-a-Judge"
          }
        ]
      },
      "Based on the search results, I found the information about this paper:\n\n**Paper Details:**\n- **Title:** Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge\n- **Authors:** Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, and Soroush Vosoughi\n- **Published Venue/Conference:** Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2025), Mumbai, India\n- **Submission Date:** Submitted on 12 Jun 2024\n\n**Overview:**\nThe study addresses position bias—a tendency to favor solutions based on their position in the prompt—in LLM-as-a-Judge evaluations. It introduces a systematic framework to examine position bias in pairwise comparisons, focusing on repetition stability, position consistency, and preference fairness."
    ],
    "durationSeconds": 5.488320760000002
  }
}
```

</details>

---

### Assistant

_source line 65_

<details><summary>Logged reasoning block</summary>

```text
Excellent! More findings:

1. **li2024calibraeval** - Published at ACL 2025! Need to update from arXiv to @inproceedings with ACL 2025 venue.
2. **ye2024justice** - Published at ICLR 2025! Need to update from arXiv to @inproceedings with ICLR 2025 venue.
3. **celikyilmaz2020evaluation** - Still arXiv only.
4. **stureborg2024inconsistent** - Still arXiv only.
5. **he2021debertav3** - Published at ICLR 2023! Need to update from arXiv to @inproceedings with ICLR 2023 venue.


6. **shi2024judging** - Published at IJCNLP-AACL 2025! Need to update from arXiv to @inproceedings.

Now I need to verify the venue for `tripathi2025pairwise` more carefully, and check whether `counterfactual2025rhetorical` has been accepted anywhere beyond its OpenReview submission.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "52a31ed1-0ca2-4570-98bd-9d5cecab7049",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqnpnpT3QizKFxNTzUgsce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 65626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8757
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

_source line 66_

Several papers have published versions. Let me verify a few more details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "5915b147-f5dc-4292-b14d-794db098f984",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqnpnpT3QizKFxNTzUgsce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 65626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8757
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

_source line 67_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KmzUsXm2A8M7BVanYNiXcs`</summary>

```json
{
  "query": "Tripathi \"Pairwise or Pointwise\" COLM 2025 \"Conference on Language Modeling\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0e1fee89-b9a8-4eb4-8f37-db462dfbf583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqnpnpT3QizKFxNTzUgsce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 65626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8757
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

_source line 68_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HJCiht7VUUgMfjh8evSzSs`</summary>

```json
{
  "query": "site:openreview.net \"Counterfactual LLM-based Framework\" rhetorical style accepted ICLR ARR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "5862c15a-e0ae-4499-a0ec-eb1ca3658593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqnpnpT3QizKFxNTzUgsce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 65626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8757
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

_source line 69_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZmPJTDSJeEdqJKnw8zsoV`</summary>

```json
{
  "query": "\"Justice or Prejudice\" Ye Jiayi ICLR 2025 proceedings venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "82ae8afc-36b0-4aeb-8e1a-7770cdf20357",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqnpnpT3QizKFxNTzUgsce",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8757,
      "cache_read_input_tokens": 65626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8757
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

_source line 70 · 2026-05-22T01:11:26.324Z_

<details><summary>↩ Tool result · `toolu_01TZmPJTDSJeEdqJKnw8zsoV`</summary>

```text
Web search results for query: ""Justice or Prejudice" Ye Jiayi ICLR 2025 proceedings venue"

Links: [{"title":"JUSTICE OR PREJUDICE? QUANTIFYING BIASES IN LLM-AS-A-JUDGE for ICLR 2025 - IBM Research","url":"https://research.ibm.com/publications/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"},{"title":"Published as a conference paper at ICLR 2025 JUSTICE OR PREJUDICE?","url":"https://openreview.net/pdf/2086c02ae5ff0bf9a243a4841075ffe6de7630e1.pdf"},{"title":"dblp: Jiayi Ye","url":"https://dblp.org/pid/153/5814.html"},{"title":"dblp: Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge.","url":"https://dblp1.uni-trier.de/rec/conf/iclr/YeWHCZMGG0CC025.html"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge - Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang - ICLR, 2025 | Publications | News & Events | Ethics and the Common Good | University of Notre Dame","url":"https://ethics.nd.edu/news-and-events/publications/jiayi-ye-yanbo-wang-yue-huang-dongping-chen-qihui-zhang-nuno-moniz-tian-gao-werner-geyer-chao-huang-pin-yu-chen-nitesh-v-chawla-xiangliang-zhang-iclr-2025-justice-or-prejudice-quantifying-biases-in-llm-as-a-judge/"},{"title":"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://bibbase.org/network/publication/ye-wang-huang-chen-zhang-moniz-gao-geyer-etal-justiceorprejudicequantifyingbiasesinllmasajudge-2025"},{"title":"ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://iclr.cc/virtual/2025/poster/31088"},{"title":"[Literature Review] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge","url":"https://www.themoonlight.io/en/review/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"}]

Based on the search results, I can provide you with information about the venue for this paper:

"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" was published as a conference paper at ICLR 2025. The venue is The Thirteenth International Conference on Learning Representations, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "b73c350a-104a-45a0-9434-5a547c019d54",
  "tool_use_result": {
    "query": "\"Justice or Prejudice\" Ye Jiayi ICLR 2025 proceedings venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jv1hrjpUC94kgtdidV5Z2d",
        "content": [
          {
            "title": "JUSTICE OR PREJUDICE? QUANTIFYING BIASES IN LLM-AS-A-JUDGE for ICLR 2025 - IBM Research",
            "url": "https://research.ibm.com/publications/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 JUSTICE OR PREJUDICE?",
            "url": "https://openreview.net/pdf/2086c02ae5ff0bf9a243a4841075ffe6de7630e1.pdf"
          },
          {
            "title": "dblp: Jiayi Ye",
            "url": "https://dblp.org/pid/153/5814.html"
          },
          {
            "title": "dblp: Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge.",
            "url": "https://dblp1.uni-trier.de/rec/conf/iclr/YeWHCZMGG0CC025.html"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/hash/fdca08d371e4b6c031397909e20043bd-Abstract-Conference.html"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge - Jiayi Ye, Yanbo Wang, Yue Huang, Dongping Chen, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang - ICLR, 2025 | Publications | News & Events | Ethics and the Common Good | University of Notre Dame",
            "url": "https://ethics.nd.edu/news-and-events/publications/jiayi-ye-yanbo-wang-yue-huang-dongping-chen-qihui-zhang-nuno-moniz-tian-gao-werner-geyer-chao-huang-pin-yu-chen-nitesh-v-chawla-xiangliang-zhang-iclr-2025-justice-or-prejudice-quantifying-biases-in-llm-as-a-judge/"
          },
          {
            "title": "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://bibbase.org/network/publication/ye-wang-huang-chen-zhang-moniz-gao-geyer-etal-justiceorprejudicequantifyingbiasesinllmasajudge-2025"
          },
          {
            "title": "ICLR Poster Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://iclr.cc/virtual/2025/poster/31088"
          },
          {
            "title": "[Literature Review] Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge",
            "url": "https://www.themoonlight.io/en/review/justice-or-prejudice-quantifying-biases-in-llm-as-a-judge"
          }
        ]
      },
      "Based on the search results, I can provide you with information about the venue for this paper:\n\n\"Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge\" was published as a conference paper at ICLR 2025. The venue is The Thirteenth International Conference on Learning Representations, 2025."
    ],
    "durationSeconds": 3.1251094489999813
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-22T01:11:27.020Z_

<details><summary>↩ Tool result · `toolu_01HJCiht7VUUgMfjh8evSzSs`</summary>

```text
Web search results for query: "site:openreview.net "Counterfactual LLM-based Framework" rhetorical style accepted ICLR ARR"

Links: [{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview","url":"https://openreview.net/forum?id=fiohEI16sf"},{"title":"COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...","url":"https://openreview.net/pdf/e194fe1dda6ea2aff401bf0f16650a9c7d414fd9.pdf"},{"title":"Counterfactual LLM-based Framework for Measuring Rhetorical Style","url":"https://arxiv.org/pdf/2512.19908"},{"title":"Counterfactual Debating with Preset Stances for Hallucination   Elimination of LLMs","url":"https://arxiv.org/pdf/2406.11514"},{"title":"Executable Counterfactuals: Improving LLMs' Causal Reasoning Through Code","url":"https://arxiv.org/pdf/2510.01539"}]

I found the paper you're looking for! The "Counterfactual LLM-based Framework for Measuring Rhetorical Style" introduces a framework where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and outcomes are aggregated using a Bradley-Terry model.

The research applies this method to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings to provide a large-scale quantification of rhetorical style in ML papers.

The paper is available on OpenReview at: https://openreview.net/forum?id=fiohEI16sf


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "7122e549-5dce-440d-a495-b4f0068856ba",
  "tool_use_result": {
    "query": "site:openreview.net \"Counterfactual LLM-based Framework\" rhetorical style accepted ICLR ARR",
    "results": [
      {
        "tool_use_id": "srvtoolu_019WiZpt9LMJ8ZfspXUKPoF1",
        "content": [
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style | OpenReview",
            "url": "https://openreview.net/forum?id=fiohEI16sf"
          },
          {
            "title": "COUNTERFACTUAL LLM-BASED FRAMEWORK FOR ...",
            "url": "https://openreview.net/pdf/e194fe1dda6ea2aff401bf0f16650a9c7d414fd9.pdf"
          },
          {
            "title": "Counterfactual LLM-based Framework for Measuring Rhetorical Style",
            "url": "https://arxiv.org/pdf/2512.19908"
          },
          {
            "title": "Counterfactual Debating with Preset Stances for Hallucination   Elimination of LLMs",
            "url": "https://arxiv.org/pdf/2406.11514"
          },
          {
            "title": "Executable Counterfactuals: Improving LLMs' Causal Reasoning Through Code",
            "url": "https://arxiv.org/pdf/2510.01539"
          }
        ]
      },
      "I found the paper you're looking for! The \"Counterfactual LLM-based Framework for Measuring Rhetorical Style\" introduces a framework where multiple LLM rhetorical personas generate counterfactual writings from the same substantive content, an LLM judge compares them through pairwise evaluations, and outcomes are aggregated using a Bradley-Terry model.\n\nThe research applies this method to 8,485 ICLR submissions sampled from 2017 to 2025, generating more than 250,000 counterfactual writings to provide a large-scale quantification of rhetorical style in ML papers.\n\nThe paper is available on OpenReview at: https://openreview.net/forum?id=fiohEI16sf"
    ],
    "durationSeconds": 4.625893347000004
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-22T01:11:28.130Z_

<details><summary>↩ Tool result · `toolu_01KmzUsXm2A8M7BVanYNiXcs`</summary>

```text
Web search results for query: "Tripathi "Pairwise or Pointwise" COLM 2025 "Conference on Language Modeling""

Links: [{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for ...","url":"https://arxiv.org/pdf/2504.14716"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation | OpenReview","url":"https://openreview.net/forum?id=uyX5Vnow3U"},{"title":"LLM-AS-A-JUDGE: TOWARD WORLD MODELS FOR SLATE RECOMMENDATION SYSTEMS","url":"https://arxiv.org/pdf/2511.04541"},{"title":"[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://arxiv.org/abs/2504.14716"},{"title":"CodeRankEval: Benchmarking and Analyzing LLM Performance for Code Ranking","url":"https://www.researchgate.net/publication/397827093_CodeRankEval_Benchmarking_and_Analyzing_LLM_Performance_for_Code_Ranking"},{"title":"Published as a conference paper at COLM 2025","url":"https://arxiv.org/pdf/2508.06781"},{"title":"What Does Preference Learning Recover from Pairwise Comparison Data?","url":"https://arxiv.org/pdf/2602.10286"},{"title":"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation","url":"https://www.emergentmind.com/papers/2504.14716"}]

I found the paper you're looking for! The paper "Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation" by Tuhina Tripathi, Manya Wadhwa, Greg Durrett, and Scott Niekum was published as a conference paper at COLM 2025.

Here's a summary of the research:

The work examines how Large Language Models are used as proxies for human labelers in both training (Reinforcement Learning from AI Feedback) and large-scale response evaluation (LLM-as-a-judge). The research shows that the choice of feedback protocol for evaluation (absolute scores versus relative preferences) can significantly affect evaluation reliability and induce systematic biases.

Key findings include: Pairwise preferences are prone to distracted evaluation, whereas absolute scoring methods exhibit greater robustness against distortions caused by distractors. On average, pairwise preferences flip in 35% of cases when a distractor feature is introduced, compared to only 9% for absolute scores.

The paper is available on arXiv (2504.14716) and OpenReview as a published conference paper at COLM 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "39dd9943-07fc-4498-9a12-db9d83726508",
  "tool_use_result": {
    "query": "Tripathi \"Pairwise or Pointwise\" COLM 2025 \"Conference on Language Modeling\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_019cvnAJ2mTNjVJy3GSEp9ed",
        "content": [
          {
            "title": "Pairwise or Pointwise? Evaluating Feedback Protocols for ...",
            "url": "https://arxiv.org/pdf/2504.14716"
          },
          {
            "title": "Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation | OpenReview",
            "url": "https://openreview.net/forum?id=uyX5Vnow3U"
          },
          {
            "title": "LLM-AS-A-JUDGE: TOWARD WORLD MODELS FOR SLATE RECOMMENDATION SYSTEMS",
            "url": "https://arxiv.org/pdf/2511.04541"
          },
          {
            "title": "[2504.14716] Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation",
            "url": "https://arxiv.org/abs/2504.14716"
          },
          {
            "title": "CodeRankEval: Benchmarking and Analyzing LLM Performance for Code Ranking",
            "url": "https://www.researchgate.net/publication/397827093_CodeRankEval_Benchmarking_and_Analyzing_LLM_Performance_for_Code_Ranking"
          },
          {
            "title": "Published as a conference paper at COLM 2025",
            "url": "https://arxiv.org/pdf/2508.06781"
          },
          {
            "title": "What Does Preference Learning Recover from Pairwise Comparison Data?",
            "url": "https://arxiv.org/pdf/2602.10286"
          },
          {
            "title": "Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation",
            "url": "https://www.emergentmind.com/papers/2504.14716"
          }
        ]
      },
      "I found the paper you're looking for! The paper \"Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in LLM-Based Evaluation\" by Tuhina Tripathi, Manya Wadhwa, Greg Durrett, and Scott Niekum was published as a conference paper at COLM 2025.\n\nHere's a summary of the research:\n\nThe work examines how Large Language Models are used as proxies for human labelers in both training (Reinforcement Learning from AI Feedback) and large-scale response evaluation (LLM-as-a-judge). The research shows that the choice of feedback protocol for evaluation (absolute scores versus relative preferences) can significantly affect evaluation reliability and induce systematic biases.\n\nKey findings include: Pairwise preferences are prone to distracted evaluation, whereas absolute scoring methods exhibit greater robustness against distortions caused by distractors. On average, pairwise preferences flip in 35% of cases when a distractor feature is introduced, compared to only 9% for absolute scores.\n\nThe paper is available on arXiv (2504.14716) and OpenReview as a published conference paper at COLM 2025."
    ],
    "durationSeconds": 6.608153286999994
  }
}
```

</details>

---

### Assistant

_source line 73_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data. Let me also check the `counterfactual2025rhetorical` OpenReview status. It seems to be submitted to ICLR but I need to check if it was accepted. Let me check the OpenReview page.

Actually, from the search results, the OpenReview link just shows the paper page, not the acceptance status. Let me check if this was accepted or just submitted. Since there's no clear indication it was accepted at any venue, I'll treat it as arXiv only.

Now let me also check `wang2023faireval` - it was published at ACL 2024 per the search. I need the full details.


I'm also looking at the `casse2026concise` paper - the citation uses the method name CASSE as the bib key, which is unconventional but workable for identification purposes.

Similarly, `counterfactual2025rhetorical` derives its key from the content rather than the author, which is also unconventional. And `wang2026fairjudge` has a clear mismatch since the first author is Yang Bo, not Wang.

Now I'm compiling all the issues I've found: the critical ones that would break compilation, and the warnings where entries have incorrect or incomplete metadata - like papers that are arXiv preprints but were actually published at conferences like ACL 2024 or ICLR 2023, so their entry types need updating. The casse2026concise entry uses an unconventional key based on the method name rather than the author, which works in context since CASSE is referenced in the text. I'm also noticing several other key inconsistencies: counterfactual2025rhetorical doesn't follow author naming conventions, and boubdir2023elo, wu2023style, and zeng2023llmbar all have mismatched years between their keys and actual publication years. Additionally, some entries append venue abbreviations in parentheses after full names, and a couple of entries use "and others" instead of listing all authors.

Looking at the arXiv preprints, I'm seeing a pattern of papers that remain unpublished or in submission limbo—wang2026fairjudge, casse2026concise, counterfactual2025rhetorical, soumik2026judging, celikyilmaz2020evaluation, and stureborg2024inconsistent are all still arXiv-only or have unclear publication status.

The cross-reference validation checks out cleanly—all citations in the tex files match entries in the bibliography, there are no orphaned references, and I haven't found any duplicates. Now I'm identifying which bibliography entries can be automatically corrected: wang2023faireval needs to be converted to an inproceedings entry with ACL 2024, he2021debertav3 should be updated to ICLR 2023, and ye2024justice needs its venue information completed.

I'm also planning updates for li2024calibraeval (ACL 2025), shi2024judging (IJCNLP-AACL 2025), and tripathi2025pairwise (COLM 2025). I need to be careful not to change any bibliography keys themselves, since that would break the citations in the tex files. Before making these edits, I'm double-checking whether counterfactual2025rhetorical was actually accepted at ICLR or if it's still just a submission on OpenReview. Now I'm going through each entry to standardize the venue names and years—keeping the citation keys as-is even when they don't match the publication year, but updating the booktitle and year fields to reflect where each paper actually appeared. I need to update several bibliography entries from preprints to their published conference versions. For tripathi2025pairwise, wang2023faireval, li2024calibraeval, and ye2024justice, I'm converting them from @article entries with arXiv metadata to @inproceedings entries with the proper conference details. For ye2024justice at ICLR, I'll keep the arXiv URL since ICLR uses OpenReview for proceedings. Let me map out the specific line changes needed for each entry. I need to update the year fields for the published versions—wang2023faireval should be 2024, li2024calibraeval and ye2024justice should be 2025, he2021debertav3 should be 2023, and shi2024judging should be 2025. I also notice the ye2024justice entry is missing two authors from the full list, so I need to add Geyer and Chawla to complete it. I need to verify the author lists for these bibliography entries against the official sources and make corrections where needed. For wang2023faireval, the 11 authors in the current bib match the ACL version, so that's fine. For li2024calibraeval, the 7 authors also align with the arXiv listing. Now I'm ready to apply these edits, making sure to maintain consistent formatting with venue abbreviations in parentheses like the rest of the file. I'm seeing the pattern now—some entries use generic conference names while others include specific years and volume information. I'll standardize these by following the most consistent existing format, using the full conference names with years and volume details where applicable, and for COLM I need to determine the appropriate booktitle format.

Now I'm verifying the anthology IDs to confirm these are all long papers—wang2023faireval, li2024calibraeval, and shi2024judging all show the `-long.` designation, so they should all include the volume specification. Before making the edits, I also need to handle the "and others" citations in some entries.

Looking at the author fields with "and others," BibTeX will correctly render these as "et al." in the output, which is technically fine, but it would be more complete to have the full author lists. Since tracking down all the missing authors would be time-consuming, I'll note this as something to improve but won't change it now. Let me proceed with the main fixes to the bib file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "4dc5b950-8005-4c5e-b888-628e395d578c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 74_

Now I have all the data needed. Let me fix the bib file. Six arXiv preprints have published versions that need updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "6f61b89c-42fa-4fab-9d3d-591487f3d9ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

<details open><summary>🔧 Tool call — Edit · `toolu_0136usrKD2SKk9CkZk4hgBrc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  journal={arXiv preprint arXiv:2504.14716},\n  year={2025}\n}",
  "new_string": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "06375ead-e336-4e6c-a547-7148141bd476",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 76 · 2026-05-22T01:12:53.743Z_

<details><summary>↩ Tool result · `toolu_0136usrKD2SKk9CkZk4hgBrc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "da208358-0ddb-4283-9ce0-499b88ee2c71",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "oldString": "@article{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  journal={arXiv preprint arXiv:2504.14716},\n  year={2025}\n}",
    "newString": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}",
    "originalFile": "@article{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  journal={arXiv preprint arXiv:2504.14716},\n  year={2025}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@article{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  journal={arXiv preprint arXiv:2305.17926},\n  year={2023},\n  url={https://arxiv.org/abs/2305.17926}\n}\n\n@article{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  journal={arXiv preprint arXiv:2410.15393},\n  year={2024},\n  url={https://arxiv.org/abs/2410.15393}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 8,
        "newStart": 1,
        "newLines": 9,
        "lines": [
          "-@article{tripathi2025pairwise,",
          "+@inproceedings{tripathi2025pairwise,",
          "   title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},",
          "   author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},",
          "-  journal={arXiv preprint arXiv:2504.14716},",
          "-  year={2025}",
          "+  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},",
          "+  year={2025},",
          "+  url={https://arxiv.org/abs/2504.14716}",
          " }",
          " ",
          " @inproceedings{murugadoss2025sos,"
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

_source line 77_

<details open><summary>🔧 Tool call — Edit · `toolu_01GHjEDAg7piVs6xPy4cEbZ6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  journal={arXiv preprint arXiv:2305.17926},\n  year={2023},\n  url={https://arxiv.org/abs/2305.17926}\n}",
  "new_string": "@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "42f9d1c1-fd7d-459d-bd4e-33e580fafa17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 78 · 2026-05-22T01:12:57.660Z_

<details><summary>↩ Tool result · `toolu_01GHjEDAg7piVs6xPy4cEbZ6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "c7df7d9f-e56f-4ae3-9ac6-5973056a9e9a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "oldString": "@article{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  journal={arXiv preprint arXiv:2305.17926},\n  year={2023},\n  url={https://arxiv.org/abs/2305.17926}\n}",
    "newString": "@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}",
    "originalFile": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@article{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  journal={arXiv preprint arXiv:2305.17926},\n  year={2023},\n  url={https://arxiv.org/abs/2305.17926}\n}\n\n@article{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  journal={arXiv preprint arXiv:2410.15393},\n  year={2024},\n  url={https://arxiv.org/abs/2410.15393}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 156,
        "oldLines": 12,
        "newStart": 156,
        "newLines": 12,
        "lines": [
          " }",
          " ",
          " ",
          "-@article{wang2023faireval,",
          "+@inproceedings{wang2023faireval,",
          "   title={Large Language Models are not Fair Evaluators},",
          "-  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Liu, Qi and Liu, Tianyu and Sui, Zhifang},",
          "-  journal={arXiv preprint arXiv:2305.17926},",
          "-  year={2023},",
          "-  url={https://arxiv.org/abs/2305.17926}",
          "+  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},",
          "+  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},",
          "+  year={2024},",
          "+  url={https://aclanthology.org/2024.acl-long.511/}",
          " }",
          " ",
          " @article{li2024calibraeval,"
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

_source line 79_

<details open><summary>🔧 Tool call — Edit · `toolu_01Xx53FrhcRXDJTTirsJhba5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  journal={arXiv preprint arXiv:2410.15393},\n  year={2024},\n  url={https://arxiv.org/abs/2410.15393}\n}",
  "new_string": "@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "acc56324-6bc0-4c1b-8b19-a42890472bbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 80 · 2026-05-22T01:13:01.824Z_

<details><summary>↩ Tool result · `toolu_01Xx53FrhcRXDJTTirsJhba5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "d3199c1a-5eb1-43f0-9bb8-3b1b7f24c36a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "oldString": "@article{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  journal={arXiv preprint arXiv:2410.15393},\n  year={2024},\n  url={https://arxiv.org/abs/2410.15393}\n}",
    "newString": "@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}",
    "originalFile": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}\n\n@article{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  journal={arXiv preprint arXiv:2410.15393},\n  year={2024},\n  url={https://arxiv.org/abs/2410.15393}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 164,
        "oldLines": 12,
        "newStart": 164,
        "newLines": 12,
        "lines": [
          "   url={https://aclanthology.org/2024.acl-long.511/}",
          " }",
          " ",
          "-@article{li2024calibraeval,",
          "+@inproceedings{li2024calibraeval,",
          "   title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},",
          "   author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},",
          "-  journal={arXiv preprint arXiv:2410.15393},",
          "-  year={2024},",
          "-  url={https://arxiv.org/abs/2410.15393}",
          "+  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},",
          "+  year={2025},",
          "+  url={https://aclanthology.org/2025.acl-long.808/}",
          " }",
          " ",
          " @article{hoenig2001abuse,"
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

_source line 81_

<details open><summary>🔧 Tool call — Edit · `toolu_01Drbt6Kti8SQkSzhLPugszC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}",
  "new_string": "@inproceedings{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.02736}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "d6d33e8b-b0d5-4e45-a50e-b981d1ab997e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 82 · 2026-05-22T01:13:05.255Z_

<details><summary>↩ Tool result · `toolu_01Drbt6Kti8SQkSzhLPugszC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "cd3d8f65-8808-4539-91fe-568ea9e308e0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "oldString": "@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}",
    "newString": "@inproceedings{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.02736}\n}",
    "originalFile": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}\n\n@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@article{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},\n  journal={arXiv preprint arXiv:2410.02736},\n  year={2024},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 233,
        "oldLines": 11,
        "newStart": 233,
        "newLines": 11,
        "lines": [
          "   doi={10.1214/aos/1079120141}",
          " }",
          " ",
          "-@article{ye2024justice,",
          "+@inproceedings{ye2024justice,",
          "   title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},",
          "-  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu},",
          "-  journal={arXiv preprint arXiv:2410.02736},",
          "-  year={2024},",
          "+  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},",
          "+  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},",
          "+  year={2025},",
          "   url={https://arxiv.org/abs/2410.02736}",
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

_source line 83_

<details open><summary>🔧 Tool call — Edit · `toolu_01MoQa6cPZCPhqvNjCAqw4rc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}",
  "new_string": "@inproceedings{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2023},\n  url={https://arxiv.org/abs/2111.09543}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0259952c-ee8d-4a79-9e43-c10d8632e724",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 84 · 2026-05-22T01:13:09.013Z_

<details><summary>↩ Tool result · `toolu_01MoQa6cPZCPhqvNjCAqw4rc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "3eef52c5-63f8-4e2f-9489-27dfd2f07c5e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "oldString": "@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}",
    "newString": "@inproceedings{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2023},\n  url={https://arxiv.org/abs/2111.09543}\n}",
    "originalFile": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}\n\n@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@inproceedings{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@article{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  journal={arXiv preprint arXiv:2111.09543},\n  year={2021},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 434,
        "oldLines": 11,
        "newStart": 434,
        "newLines": 11,
        "lines": [
          "   url={https://aclanthology.org/2024.emnlp-main.474/}",
          " }",
          " ",
          "-@article{he2021debertav3,",
          "+@inproceedings{he2021debertav3,",
          "   title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},",
          "   author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},",
          "-  journal={arXiv preprint arXiv:2111.09543},",
          "-  year={2021},",
          "+  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},",
          "+  year={2023},",
          "   url={https://arxiv.org/abs/2111.09543}",
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

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_01A4ftJMWH3HEV3GGXaT3WdF`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
  "old_string": "@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}",
  "new_string": "@inproceedings{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.ijcnlp-long.18/}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "520094fe-7629-43c5-b61b-b2c6c100228c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D11UtT4Swp19uxX3UmXaHd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1434,
      "cache_creation_input_tokens": 1296,
      "cache_read_input_tokens": 74383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1296
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

_source line 86 · 2026-05-22T01:13:13.373Z_

<details><summary>↩ Tool result · `toolu_01A4ftJMWH3HEV3GGXaT3WdF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "85d948ac-5e78-4f38-a1ac-f9dc3dbb322e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
    "oldString": "@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}",
    "newString": "@inproceedings{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.ijcnlp-long.18/}\n}",
    "originalFile": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}\n\n@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@inproceedings{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@inproceedings{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2023},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@article{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  journal={arXiv preprint arXiv:2406.07791},\n  year={2024},\n  url={https://arxiv.org/abs/2406.07791}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
    "structuredPatch": [
      {
        "oldStart": 442,
        "oldLines": 12,
        "newStart": 442,
        "newLines": 12,
        "lines": [
          "   url={https://arxiv.org/abs/2111.09543}",
          " }",
          " ",
          "-@article{shi2024judging,",
          "+@inproceedings{shi2024judging,",
          "   title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},",
          "   author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},",
          "-  journal={arXiv preprint arXiv:2406.07791},",
          "-  year={2024},",
          "-  url={https://arxiv.org/abs/2406.07791}",
          "+  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},",
          "+  year={2025},",
          "+  url={https://aclanthology.org/2025.ijcnlp-long.18/}",
          " }",
          " ",
          " @inproceedings{bavaresco2025llms,"
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

_source line 87_

<details><summary>Logged reasoning block</summary>

```text
All edits done. Now let me save the audit report and verify the bib file looks correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "b5654370-b624-40d9-a7b1-e235f8aef04d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01At1bKWprhhSr31uPoirpkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8882,
      "cache_read_input_tokens": 75679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8882
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

_source line 88_

All bib fixes applied. Now let me save the audit report and verify the final bib.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "c97bd384-d653-4498-a17a-528a90104388",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01At1bKWprhhSr31uPoirpkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8882,
      "cache_read_input_tokens": 75679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8882
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

_source line 89_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01D1cWxXcPQT1whGdRAcQeoe`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "8b0b760b-8827-4d30-bf31-335f471ba563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01At1bKWprhhSr31uPoirpkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8882,
      "cache_read_input_tokens": 75679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8882
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

_source line 90 · 2026-05-22T01:13:18.989Z_

<details><summary>↩ Tool result · `toolu_01D1cWxXcPQT1whGdRAcQeoe`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "17337907-802e-4b49-8e77-af963dd2542f",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Read · `toolu_01BvzoVA4VUJDAkKsBzYmq5Q`</summary>

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
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "3747fe3f-3773-4013-aaa7-5c8a2b0a7d66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01At1bKWprhhSr31uPoirpkz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8882,
      "cache_read_input_tokens": 75679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8882
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

_source line 92 · 2026-05-22T01:13:19.124Z_

<details><summary>↩ Tool result · `toolu_01BvzoVA4VUJDAkKsBzYmq5Q`</summary>

```text
1	@inproceedings{tripathi2025pairwise,
2	  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},
3	  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},
4	  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},
5	  year={2025},
6	  url={https://arxiv.org/abs/2504.14716}
7	}
8	
9	@inproceedings{murugadoss2025sos,
10	  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},
11	  author={Murugadoss, Aakanksha and others},
12	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
13	  year={2025},
14	  url={https://arxiv.org/abs/2409.15268}
15	}
16	
17	@inproceedings{li2026preference,
18	  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},
19	  author={Li, Dawei and others},
20	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
21	  year={2026},
22	  url={https://arxiv.org/abs/2502.01534}
23	}
24	
25	@article{wang2026fairjudge,
26	  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},
27	  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},
28	  journal={arXiv preprint arXiv:2602.06625},
29	  year={2026},
30	  url={https://arxiv.org/abs/2602.06625}
31	}
32	
33	
34	@inproceedings{dubois2025lc,
35	  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},
36	  author={Dubois, Yann and others},
37	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
38	  year={2025},
39	  url={https://arxiv.org/abs/2404.04475}
40	}
41	
42	@article{casse2026concise,
43	  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},
44	  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},
45	  journal={arXiv preprint arXiv:2601.10809},
46	  year={2026},
47	  url={https://arxiv.org/abs/2601.10809}
48	}
49	
50	@article{counterfactual2025rhetorical,
51	  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},
52	  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},
53	  journal={arXiv preprint arXiv:2512.19908},
54	  year={2025},
55	  url={https://arxiv.org/abs/2512.19908}
56	}
57	
58	@article{soumik2026judging,
59	  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},
60	  author={Soumik, Mohammad and others},
61	  journal={arXiv preprint arXiv:2604.23178},
62	  year={2026},
63	  url={https://arxiv.org/abs/2604.23178}
64	}
65	
66	@inproceedings{reber2025rate,
67	  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},
68	  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},
69	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
70	  year={2025},
71	  url={https://arxiv.org/abs/2410.11348}
72	}
73	
74	@inproceedings{kiritchenko2017bws,
75	  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},
76	  author={Kiritchenko, Svetlana and Mohammad, Saif},
77	  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
78	  pages={465--470},
79	  year={2017},
80	  url={https://aclanthology.org/P17-2074/}
81	}
82	
83	@inproceedings{novikova2018rankme,
84	  title={{RankME}: Reliable Human Ratings for Natural Language Generation},
85	  author={Novikova, Jekaterina and Du{\v{s}}ek, Ond{\v{r}}ej and Rieser, Verena},
86	  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},
87	  year={2018},
88	  url={https://aclanthology.org/N18-2012/}
89	}
90	
91	@article{stevens1946theory,
92	  title={On the Theory of Scales of Measurement},
93	  author={Stevens, Stanley Smith},
94	  journal={Science},
95	  volume={103},
96	  number={2684},
97	  pages={677--680},
98	  year={1946}
99	}
100	
101	@article{thurstone1927law,
102	  title={A Law of Comparative Judgment},
103	  author={Thurstone, Louis Leon},
104	  journal={Psychological Review},
105	  volume={34},
106	  number={4},
107	  pages={273--286},
108	  year={1927}
109	}
110	
111	@article{decoster2011median,
112	  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},
113	  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},
114	  journal={Journal of Experimental Psychopathology},
115	  volume={2},
116	  number={2},
117	  pages={197--209},
118	  year={2011},
119	  doi={10.5127/jep.008310}
120	}
121	
122	@inproceedings{zheng2023judging,
123	  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},
124	  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},
125	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
126	  year={2023},
127	  url={https://arxiv.org/abs/2306.05685}
128	}
129	
130	@inproceedings{dubois2023alpacafarm,
131	  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},
132	  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},
133	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
134	  year={2023},
135	  url={https://arxiv.org/abs/2305.14387}
136	}
137	
138	@article{bradley1952rank,
139	  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},
140	  author={Bradley, Ralph Allan and Terry, Milton E.},
141	  journal={Biometrika},
142	  volume={39},
143	  number={3/4},
144	  pages={324--345},
145	  year={1952}
146	}
147	
148	@article{feinstein1990kappa,
149	  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},
150	  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},
151	  journal={Journal of Clinical Epidemiology},
152	  volume={43},
153	  number={6},
154	  pages={543--549},
155	  year={1990}
156	}
157	
158	
159	@inproceedings{wang2023faireval,
160	  title={Large Language Models are not Fair Evaluators},
161	  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},
162	  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
163	  year={2024},
164	  url={https://aclanthology.org/2024.acl-long.511/}
165	}
166	
167	@inproceedings{li2024calibraeval,
168	  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},
169	  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},
170	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
171	  year={2025},
172	  url={https://aclanthology.org/2025.acl-long.808/}
173	}
174	
175	@article{hoenig2001abuse,
176	  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},
177	  author={Hoenig, John M. and Heisey, Dennis M.},
178	  journal={The American Statistician},
179	  volume={55},
180	  number={1},
181	  pages={19--24},
182	  year={2001}
183	}
184	
185	@inproceedings{zeng2023llmbar,
186	  title={Evaluating Large Language Models at Evaluating Instruction Following},
187	  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},
188	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
189	  year={2024},
190	  url={https://arxiv.org/abs/2310.07641}
191	}
192	
193	@inproceedings{veitch2020adapting,
194	  title={Adapting Text Embeddings for Causal Inference},
195	  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},
196	  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},
197	  year={2020},
198	  url={https://arxiv.org/abs/1905.12741}
199	}
200	
201	@inproceedings{tan2025judgebench,
202	  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},
203	  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},
204	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
205	  year={2025},
206	  url={https://arxiv.org/abs/2410.12784}
207	}
208	
209	@book{louviere2015bws,
210	  title={Best-Worst Scaling: Theory, Methods and Applications},
211	  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},
212	  publisher={Cambridge University Press},
213	  year={2015},
214	  isbn={9781107043152}
215	}
216	
217	@inproceedings{chiang2024chatbot,
218	  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},
219	  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},
220	  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},
221	  year={2024},
222	  url={https://arxiv.org/abs/2403.04132}
223	}
224	
225	@article{hunter2004mm,
226	  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},
227	  author={Hunter, David R.},
228	  journal={The Annals of Statistics},
229	  volume={32},
230	  number={1},
231	  pages={384--406},
232	  year={2004},
233	  doi={10.1214/aos/1079120141}
234	}
235	
236	@inproceedings{ye2024justice,
237	  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},
238	  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},
239	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
240	  year={2025},
241	  url={https://arxiv.org/abs/2410.02736}
242	}
243	
244	@article{feder2021causalm,
245	  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},
246	  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},
247	  journal={Computational Linguistics},
248	  volume={47},
249	  number={2},
250	  pages={333--386},
251	  year={2021},
252	  url={https://aclanthology.org/2021.cl-2.13/}
253	}
254	
255	@inproceedings{wu2021polyjuice,
256	  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},
257	  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},
258	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
259	  year={2021},
260	  url={https://aclanthology.org/2021.acl-long.523/}
261	}
262	
263	@inproceedings{clark2021human,
264	  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},
265	  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},
266	  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},
267	  pages={7282--7296},
268	  year={2021},
269	  url={https://aclanthology.org/2021.acl-long.565/}
270	}
271	
272	@inproceedings{amidei2019likert,
273	  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},
274	  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},
275	  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},
276	  year={2019},
277	  url={https://aclanthology.org/W19-8648/}
278	}
279	
280	@inproceedings{boubdir2023elo,
281	  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},
282	  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},
283	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
284	  year={2024},
285	  url={https://arxiv.org/abs/2311.17295}
286	}
287	
288	@inproceedings{wu2023style,
289	  title={Style Over Substance: Evaluation Biases for Large Language Models},
290	  author={Wu, Minghao and Aji, Alham Fikri},
291	  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},
292	  year={2025},
293	  url={https://aclanthology.org/2025.coling-main.21/}
294	}
295	
296	@inproceedings{liusie2024comparative,
297	  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},
298	  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},
299	  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
300	  pages={139--151},
301	  year={2024},
302	  url={https://aclanthology.org/2024.eacl-long.8/}
303	}
304	
305	@article{feder2022causal,
306	  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},
307	  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},
308	  journal={Transactions of the Association for Computational Linguistics},
309	  volume={10},
310	  pages={1138--1158},
311	  year={2022},
312	  url={https://aclanthology.org/2022.tacl-1.66/}
313	}
314	
315	@inproceedings{koo2024cobbler,
316	  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},
317	  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},
318	  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},
319	  year={2024},
320	  url={https://aclanthology.org/2024.findings-acl.29/}
321	}
322	
323	@article{liang1986gee,
324	  title={Longitudinal Data Analysis Using Generalized Linear Models},
325	  author={Liang, Kung-Yee and Zeger, Scott L.},
326	  journal={Biometrika},
327	  volume={73},
328	  number={1},
329	  pages={13--22},
330	  year={1986},
331	  doi={10.1093/biomet/73.1.13}
332	}
333	
334	@article{krosnick1999survey,
335	  title={Survey Research},
336	  author={Krosnick, Jon A.},
337	  journal={Annual Review of Psychology},
338	  volume={50},
339	  number={1},
340	  pages={537--567},
341	  year={1999},
342	  doi={10.1146/annurev.psych.50.1.537}
343	}
344	
345	@article{lakens2017equivalence,
346	  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},
347	  author={Lakens, Dani{\"e}l},
348	  journal={Social Psychological and Personality Science},
349	  volume={8},
350	  number={4},
351	  pages={355--362},
352	  year={2017},
353	  doi={10.1177/1948550617697177}
354	}
355	
356	@article{preston2000scale,
357	  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},
358	  author={Preston, Carolyn C. and Colman, Andrew M.},
359	  journal={Acta Psychologica},
360	  volume={104},
361	  number={1},
362	  pages={1--15},
363	  year={2000},
364	  doi={10.1016/S0001-6918(99)00050-5}
365	}
366	
367	@inproceedings{vanderlee2019best,
368	  title={Best Practices for the Human Evaluation of Automatically Generated Text},
369	  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},
370	  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},
371	  pages={355--368},
372	  year={2019},
373	  url={https://aclanthology.org/W19-8643/}
374	}
375	
376	@article{vanderlee2021human,
377	  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},
378	  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},
379	  journal={Computer Speech \& Language},
380	  volume={67},
381	  pages={101151},
382	  year={2021},
383	  doi={10.1016/j.csl.2020.101151}
384	}
385	
386	@article{celikyilmaz2020evaluation,
387	  title={Evaluation of Text Generation: A Survey},
388	  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},
389	  journal={arXiv preprint arXiv:2006.14799},
390	  year={2020},
391	  url={https://arxiv.org/abs/2006.14799}
392	}
393	
394	@inproceedings{jeong2025comparative,
395	  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},
396	  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},
397	  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},
398	  pages={79--108},
399	  year={2025},
400	  url={https://aclanthology.org/2025.blackboxnlp-1.5}
401	}
402	
403	@article{stureborg2024inconsistent,
404	  title={Large Language Models are Inconsistent and Biased Evaluators},
405	  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},
406	  journal={arXiv preprint arXiv:2405.01724},
407	  year={2024},
408	  url={https://arxiv.org/abs/2405.01724}
409	}
410	
411	@inproceedings{park2024offsetbias,
412	  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},
413	  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},
414	  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},
415	  pages={1043--1067},
416	  year={2024},
417	  doi={10.18653/v1/2024.findings-emnlp.57},
418	  url={https://aclanthology.org/2024.findings-emnlp.57}
419	}
420	
421	@inproceedings{panickssery2024selfpreference,
422	  title={{LLM} Evaluators Recognize and Favor Their Own Generations},
423	  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},
424	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
425	  year={2024},
426	  url={https://arxiv.org/abs/2404.13076}
427	}
428	
429	@inproceedings{chen2024humans,
430	  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},
431	  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},
432	  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
433	  year={2024},
434	  url={https://aclanthology.org/2024.emnlp-main.474/}
435	}
436	
437	@inproceedings{he2021debertav3,
438	  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},
439	  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
440	  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
441	  year={2023},
442	  url={https://arxiv.org/abs/2111.09543}
443	}
444	
445	@inproceedings{shi2024judging,
446	  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},
447	  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},
448	  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},
449	  year={2025},
450	  url={https://aclanthology.org/2025.ijcnlp-long.18/}
451	}
452	
453	@inproceedings{bavaresco2025llms,
454	  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},
455	  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},
456	  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
457	  year={2025},
458	  url={https://aclanthology.org/2025.acl-short.20/}
459	}
460	
461	@inproceedings{saito2023verbosity,
462	  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},
463	  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},
464	  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
465	  year={2023},
466	  url={https://aclanthology.org/2023.emnlp-main.665/}
467	}
468	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "5dbf2260-42cf-4968-ba40-4cf8d38ff8f3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/docs/paper/references.bib",
      "content": "@inproceedings{tripathi2025pairwise,\n  title={Pairwise or Pointwise? Evaluating Feedback Protocols for Bias in {LLM}-Based Evaluation},\n  author={Tripathi, Tuhina and Wadhwa, Manya and Durrett, Greg and Niekum, Scott},\n  booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)},\n  year={2025},\n  url={https://arxiv.org/abs/2504.14716}\n}\n\n@inproceedings{murugadoss2025sos,\n  title={Style Over Substance: Failure Modes of {LLM} Judges in Alignment Benchmarking},\n  author={Murugadoss, Aakanksha and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2409.15268}\n}\n\n@inproceedings{li2026preference,\n  title={Preference Leakage: A Contamination Problem in {LLM}-as-a-Judge},\n  author={Li, Dawei and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2026},\n  url={https://arxiv.org/abs/2502.01534}\n}\n\n@article{wang2026fairjudge,\n  title={{FairJudge}: An Adaptive, Debiased, and Consistent {LLM}-as-a-Judge},\n  author={Yang, Bo and Feng, Lanfei and Chen, Yunkui and Zhang, Yu and Xu, Xiao and Li, Shijian},\n  journal={arXiv preprint arXiv:2602.06625},\n  year={2026},\n  url={https://arxiv.org/abs/2602.06625}\n}\n\n\n@inproceedings{dubois2025lc,\n  title={Length-Controlled {AlpacaEval}: A Simple Way to Debias Automatic Evaluators},\n  author={Dubois, Yann and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2404.04475}\n}\n\n@article{casse2026concise,\n  title={A Concise Agent is Less Expert: Revealing Side Effects of Using Style Features on Conversational Agents},\n  author={Cho, Young-Min and Yuan, Yuan and Guntuku, Sharath Chandra and Ungar, Lyle},\n  journal={arXiv preprint arXiv:2601.10809},\n  year={2026},\n  url={https://arxiv.org/abs/2601.10809}\n}\n\n@article{counterfactual2025rhetorical,\n  title={Counterfactual {LLM}-based Framework for Measuring Rhetorical Style},\n  author={Qiu, Jingyi and Chen, Hong and Li, Zongyi},\n  journal={arXiv preprint arXiv:2512.19908},\n  year={2025},\n  url={https://arxiv.org/abs/2512.19908}\n}\n\n@article{soumik2026judging,\n  title={Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in {LLM}-as-a-Judge Pipelines},\n  author={Soumik, Mohammad and others},\n  journal={arXiv preprint arXiv:2604.23178},\n  year={2026},\n  url={https://arxiv.org/abs/2604.23178}\n}\n\n@inproceedings{reber2025rate,\n  title={{RATE}: Causal Explainability of Reward Models with Imperfect Counterfactuals},\n  author={Reber, David and Richardson, Sean and Nief, Todd and Garbacea, Cristina and Veitch, Victor},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.11348}\n}\n\n@inproceedings{kiritchenko2017bws,\n  title={Best-Worst Scaling More Reliable than Rating Scales: A Case Study on Sentiment Intensity Annotation},\n  author={Kiritchenko, Svetlana and Mohammad, Saif},\n  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  pages={465--470},\n  year={2017},\n  url={https://aclanthology.org/P17-2074/}\n}\n\n@inproceedings{novikova2018rankme,\n  title={{RankME}: Reliable Human Ratings for Natural Language Generation},\n  author={Novikova, Jekaterina and Du{\\v{s}}ek, Ond{\\v{r}}ej and Rieser, Verena},\n  booktitle={Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers)},\n  year={2018},\n  url={https://aclanthology.org/N18-2012/}\n}\n\n@article{stevens1946theory,\n  title={On the Theory of Scales of Measurement},\n  author={Stevens, Stanley Smith},\n  journal={Science},\n  volume={103},\n  number={2684},\n  pages={677--680},\n  year={1946}\n}\n\n@article{thurstone1927law,\n  title={A Law of Comparative Judgment},\n  author={Thurstone, Louis Leon},\n  journal={Psychological Review},\n  volume={34},\n  number={4},\n  pages={273--286},\n  year={1927}\n}\n\n@article{decoster2011median,\n  title={Best Practices for Using Median Splits, Artificial Categorization, and Their Continuous Alternatives},\n  author={DeCoster, Jamie and Gallucci, Marcello and Iselin, Anne-Marie R.},\n  journal={Journal of Experimental Psychopathology},\n  volume={2},\n  number={2},\n  pages={197--209},\n  year={2011},\n  doi={10.5127/jep.008310}\n}\n\n@inproceedings{zheng2023judging,\n  title={Judging {LLM}-as-a-Judge with {MT-Bench} and {Chatbot Arena}},\n  author={Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{dubois2023alpacafarm,\n  title={{AlpacaFarm}: A Simulation Framework for Methods that Learn from Human Feedback},\n  author={Dubois, Yann and Li, Xuechen and Taori, Rohan and Zhang, Tianyi and Gulrajani, Ishaan and Ba, Jimmy and Guestrin, Carlos and Liang, Percy and Hashimoto, Tatsunori B.},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  url={https://arxiv.org/abs/2305.14387}\n}\n\n@article{bradley1952rank,\n  title={Rank Analysis of Incomplete Block Designs: {I}. {T}he Method of Paired Comparisons},\n  author={Bradley, Ralph Allan and Terry, Milton E.},\n  journal={Biometrika},\n  volume={39},\n  number={3/4},\n  pages={324--345},\n  year={1952}\n}\n\n@article{feinstein1990kappa,\n  title={High Agreement but Low Kappa: {I}. {T}he Problems of Two Paradoxes},\n  author={Feinstein, Alvan R. and Cicchetti, Domenic V.},\n  journal={Journal of Clinical Epidemiology},\n  volume={43},\n  number={6},\n  pages={543--549},\n  year={1990}\n}\n\n\n@inproceedings{wang2023faireval,\n  title={Large Language Models are not Fair Evaluators},\n  author={Wang, Peiyi and Li, Lei and Chen, Liang and Cai, Zefan and Zhu, Dawei and Lin, Binghuai and Cao, Yunbo and Kong, Lingpeng and Liu, Qi and Liu, Tianyu and Sui, Zhifang},\n  booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2024},\n  url={https://aclanthology.org/2024.acl-long.511/}\n}\n\n@inproceedings{li2024calibraeval,\n  title={{CalibraEval}: Calibrating Prediction Distribution to Mitigate Selection Bias in {LLMs}-as-Judges},\n  author={Li, Haitao and Chen, Junjie and Ai, Qingyao and Chu, Zhumin and Zhou, Yujia and Dong, Qian and Liu, Yiqun},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-long.808/}\n}\n\n@article{hoenig2001abuse,\n  title={The Abuse of Power: The Pervasive Fallacy of Power Calculations for Data Analysis},\n  author={Hoenig, John M. and Heisey, Dennis M.},\n  journal={The American Statistician},\n  volume={55},\n  number={1},\n  pages={19--24},\n  year={2001}\n}\n\n@inproceedings{zeng2023llmbar,\n  title={Evaluating Large Language Models at Evaluating Instruction Following},\n  author={Zeng, Zhiyuan and Yu, Jiatong and Gao, Tianyu and Meng, Yu and Goyal, Tanya and Chen, Danqi},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2024},\n  url={https://arxiv.org/abs/2310.07641}\n}\n\n@inproceedings{veitch2020adapting,\n  title={Adapting Text Embeddings for Causal Inference},\n  author={Veitch, Victor and Sridhar, Dhanya and Blei, David},\n  booktitle={Proceedings of the Conference on Uncertainty in Artificial Intelligence (UAI)},\n  year={2020},\n  url={https://arxiv.org/abs/1905.12741}\n}\n\n@inproceedings{tan2025judgebench,\n  title={{JudgeBench}: A Benchmark for Evaluating {LLM}-based Judges},\n  author={Tan, Sijun and Zhuang, Siyuan and Montgomery, Kyle and Tang, William and others},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.12784}\n}\n\n@book{louviere2015bws,\n  title={Best-Worst Scaling: Theory, Methods and Applications},\n  author={Louviere, Jordan J. and Flynn, Terry N. and Marley, A. A. J.},\n  publisher={Cambridge University Press},\n  year={2015},\n  isbn={9781107043152}\n}\n\n@inproceedings{chiang2024chatbot,\n  title={Chatbot Arena: An Open Platform for Evaluating {LLM}s by Human Preference},\n  author={Chiang, Wei-Lin and Zheng, Lianmin and Sheng, Ying and Angelopoulos, Anastasios Nikolas and Li, Tianle and Li, Dacheng and Zhu, Banghua and Zhang, Hao and Jordan, Michael I. and Gonzalez, Joseph E. and Stoica, Ion},\n  booktitle={Proceedings of the International Conference on Machine Learning (ICML)},\n  year={2024},\n  url={https://arxiv.org/abs/2403.04132}\n}\n\n@article{hunter2004mm,\n  title={{MM} Algorithms for Generalized {Bradley-Terry} Models},\n  author={Hunter, David R.},\n  journal={The Annals of Statistics},\n  volume={32},\n  number={1},\n  pages={384--406},\n  year={2004},\n  doi={10.1214/aos/1079120141}\n}\n\n@inproceedings{ye2024justice,\n  title={Justice or Prejudice? Quantifying Biases in {LLM}-as-a-Judge},\n  author={Ye, Jiayi and Wang, Yanbo and Huang, Yue and Chen, Dongping and Zhang, Qihui and Moniz, Nuno and Gao, Tian and Geyer, Werner and Huang, Chao and Chen, Pin-Yu and Chawla, Nitesh V. and Zhang, Xiangliang},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2025},\n  url={https://arxiv.org/abs/2410.02736}\n}\n\n@article{feder2021causalm,\n  title={{CausaLM}: Causal Model Explanation Through Counterfactual Language Models},\n  author={Feder, Amir and Oved, Nadav and Shalit, Uri and Reichart, Roi},\n  journal={Computational Linguistics},\n  volume={47},\n  number={2},\n  pages={333--386},\n  year={2021},\n  url={https://aclanthology.org/2021.cl-2.13/}\n}\n\n@inproceedings{wu2021polyjuice,\n  title={Polyjuice: Generating Counterfactuals for Explaining, Evaluating, and Improving Models},\n  author={Wu, Tongshuang and Ribeiro, Marco Tulio and Heer, Jeffrey and Weld, Daniel},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.523/}\n}\n\n@inproceedings{clark2021human,\n  title={All That's `Human' Is Not Gold: Evaluating Human Evaluation of Generated Text},\n  author={Clark, Elizabeth and August, Tal and Serrano, Sofia and Haduong, Nikita and Gururangan, Suchin and Smith, Noah A.},\n  booktitle={Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)},\n  pages={7282--7296},\n  year={2021},\n  url={https://aclanthology.org/2021.acl-long.565/}\n}\n\n@inproceedings{amidei2019likert,\n  title={The Use of Rating and {Likert} Scales in Natural Language Generation Human Evaluation Tasks: A Review and Some Recommendations},\n  author={Amidei, Jacopo and Piwek, Paul and Willis, Alistair},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  year={2019},\n  url={https://aclanthology.org/W19-8648/}\n}\n\n@inproceedings{boubdir2023elo,\n  title={Elo Uncovered: Robustness and Best Practices in Language Model Evaluation},\n  author={Boubdir, Meriem and Kim, Edward and Ermis, Beyza and Hooker, Sara and Fadaee, Marzieh},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2311.17295}\n}\n\n@inproceedings{wu2023style,\n  title={Style Over Substance: Evaluation Biases for Large Language Models},\n  author={Wu, Minghao and Aji, Alham Fikri},\n  booktitle={Proceedings of the 31st International Conference on Computational Linguistics (COLING)},\n  year={2025},\n  url={https://aclanthology.org/2025.coling-main.21/}\n}\n\n@inproceedings{liusie2024comparative,\n  title={{LLM} Comparative Assessment: Zero-shot {NLG} Evaluation through Pairwise Comparisons using Large Language Models},\n  author={Liusie, Adian and Manakul, Potsawee and Gales, Mark},\n  booktitle={Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  pages={139--151},\n  year={2024},\n  url={https://aclanthology.org/2024.eacl-long.8/}\n}\n\n@article{feder2022causal,\n  title={Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond},\n  author={Feder, Amir and Keith, Katherine A. and Manzoor, Emaad and Pryzant, Reid and Sridhar, Dhanya and Wood-Doughty, Zach and Eisenstein, Jacob and Grimmer, Justin and Reichart, Roi and Roberts, Margaret E. and Stewart, Brandon M. and Veitch, Victor and Yang, Diyi},\n  journal={Transactions of the Association for Computational Linguistics},\n  volume={10},\n  pages={1138--1158},\n  year={2022},\n  url={https://aclanthology.org/2022.tacl-1.66/}\n}\n\n@inproceedings{koo2024cobbler,\n  title={Benchmarking Cognitive Biases in Large Language Models as Evaluators},\n  author={Koo, Ryan and Lee, Minhwa and Raheja, Vipul and Park, Jong Inn and Kim, Zae Myung and Kang, Dongyeop},\n  booktitle={Findings of the Association for Computational Linguistics: ACL 2024},\n  year={2024},\n  url={https://aclanthology.org/2024.findings-acl.29/}\n}\n\n@article{liang1986gee,\n  title={Longitudinal Data Analysis Using Generalized Linear Models},\n  author={Liang, Kung-Yee and Zeger, Scott L.},\n  journal={Biometrika},\n  volume={73},\n  number={1},\n  pages={13--22},\n  year={1986},\n  doi={10.1093/biomet/73.1.13}\n}\n\n@article{krosnick1999survey,\n  title={Survey Research},\n  author={Krosnick, Jon A.},\n  journal={Annual Review of Psychology},\n  volume={50},\n  number={1},\n  pages={537--567},\n  year={1999},\n  doi={10.1146/annurev.psych.50.1.537}\n}\n\n@article{lakens2017equivalence,\n  title={Equivalence Tests: A Practical Primer for $t$ Tests, Correlations, and Meta-Analyses},\n  author={Lakens, Dani{\\\"e}l},\n  journal={Social Psychological and Personality Science},\n  volume={8},\n  number={4},\n  pages={355--362},\n  year={2017},\n  doi={10.1177/1948550617697177}\n}\n\n@article{preston2000scale,\n  title={Optimal Number of Response Categories in Rating Scales: Reliability, Validity, Discriminating Power, and Respondent Preferences},\n  author={Preston, Carolyn C. and Colman, Andrew M.},\n  journal={Acta Psychologica},\n  volume={104},\n  number={1},\n  pages={1--15},\n  year={2000},\n  doi={10.1016/S0001-6918(99)00050-5}\n}\n\n@inproceedings{vanderlee2019best,\n  title={Best Practices for the Human Evaluation of Automatically Generated Text},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Wubben, Sander and Krahmer, Emiel},\n  booktitle={Proceedings of the 12th International Conference on Natural Language Generation (INLG)},\n  pages={355--368},\n  year={2019},\n  url={https://aclanthology.org/W19-8643/}\n}\n\n@article{vanderlee2021human,\n  title={Human Evaluation of Automatically Generated Text: Current Trends and Best Practice Guidelines},\n  author={van der Lee, Chris and Gatt, Albert and van Miltenburg, Emiel and Krahmer, Emiel},\n  journal={Computer Speech \\& Language},\n  volume={67},\n  pages={101151},\n  year={2021},\n  doi={10.1016/j.csl.2020.101151}\n}\n\n@article{celikyilmaz2020evaluation,\n  title={Evaluation of Text Generation: A Survey},\n  author={Celikyilmaz, Asli and Clark, Elizabeth and Gao, Jianfeng},\n  journal={arXiv preprint arXiv:2006.14799},\n  year={2020},\n  url={https://arxiv.org/abs/2006.14799}\n}\n\n@inproceedings{jeong2025comparative,\n  title={The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators},\n  author={Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul},\n  booktitle={Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP},\n  pages={79--108},\n  year={2025},\n  url={https://aclanthology.org/2025.blackboxnlp-1.5}\n}\n\n@article{stureborg2024inconsistent,\n  title={Large Language Models are Inconsistent and Biased Evaluators},\n  author={Stureborg, Rickard and Alikaniotis, Dimitris and Suhara, Yoshi},\n  journal={arXiv preprint arXiv:2405.01724},\n  year={2024},\n  url={https://arxiv.org/abs/2405.01724}\n}\n\n@inproceedings{park2024offsetbias,\n  title={{OffsetBias}: Leveraging Debiased Data for Tuning Evaluators},\n  author={Park, Junsoo and Jwa, Seungyeon and Ren, Meiying and Kim, Daeyoung and Choi, Sanghyuk},\n  booktitle={Findings of the Association for Computational Linguistics: {EMNLP} 2024},\n  pages={1043--1067},\n  year={2024},\n  doi={10.18653/v1/2024.findings-emnlp.57},\n  url={https://aclanthology.org/2024.findings-emnlp.57}\n}\n\n@inproceedings{panickssery2024selfpreference,\n  title={{LLM} Evaluators Recognize and Favor Their Own Generations},\n  author={Panickssery, Arjun and Bowman, Samuel R. and Feng, Shi},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2024},\n  url={https://arxiv.org/abs/2404.13076}\n}\n\n@inproceedings{chen2024humans,\n  title={Humans or {LLMs} as the Judge? A Study on Judgement Biases},\n  author={Chen, Guiming Hardy and Chen, Shunian and Zhang, Ruifei and Chen, Junying and Xiong, Xiangbo and Yu, Zhouyu and Lin, Hongying and Wang, Benyou},\n  booktitle={Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2024},\n  url={https://aclanthology.org/2024.emnlp-main.474/}\n}\n\n@inproceedings{he2021debertav3,\n  title={{DeBERTaV3}: Improving {DeBERTa} using {ELECTRA}-Style Pre-Training with Gradient-Disentangled Embedding Sharing},\n  author={He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},\n  year={2023},\n  url={https://arxiv.org/abs/2111.09543}\n}\n\n@inproceedings{shi2024judging,\n  title={Judging the Judges: A Systematic Study of Position Bias in {LLM}-as-a-Judge},\n  author={Shi, Lin and Ma, Chiyu and Liang, Wenhua and Diao, Xingjian and Ma, Weicheng and Vosoughi, Soroush},\n  booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.ijcnlp-long.18/}\n}\n\n@inproceedings{bavaresco2025llms,\n  title={{LLMs} instead of Human Judges? A Large Scale Empirical Study across 20 {NLP} Evaluation Tasks},\n  author={Bavaresco, Anna and Bernardi, Raffaella and Bertolazzi, Leonardo and Bisazza, Arianna and Ceron, Davide and Ghahroodi, Omid and others},\n  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},\n  year={2025},\n  url={https://aclanthology.org/2025.acl-short.20/}\n}\n\n@inproceedings{saito2023verbosity,\n  title={Verbosity Bias in Multi-Turn Chatbot Evaluations},\n  author={Saito, Yuki and Nishida, Noriki and Okazaki, Naoaki},\n  booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year={2023},\n  url={https://aclanthology.org/2023.emnlp-main.665/}\n}\n",
      "numLines": 468,
      "startLine": 1,
      "totalLines": 468
    }
  }
}
```

</details>

---

### Assistant

_source line 93_

<details><summary>Logged reasoning block</summary>

```text
The bib file looks good with all fixes applied. Now let me save the audit report using the MCP tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "9b28ea98-110e-4ce0-96e2-1129c42b925c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sSnhWe8nSGf1wFSRxtwy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8511,
      "cache_read_input_tokens": 84561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8511
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

_source line 94_

Bib file verified. Now let me save the audit report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "450af8fa-ef81-4486-a82b-b5d7d52fff40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sSnhWe8nSGf1wFSRxtwy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8511,
      "cache_read_input_tokens": 84561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8511
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

_source line 95_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_011JRqEDydTb3XsmSa9tuuY4`</summary>

```json
{
  "project": "causal_style_decomp_judge",
  "file": "reference_audit_report.md",
  "content": "# Reference Audit Report\n\n**Date**: 2026-05-22\n**Bib file**: `docs/paper/references.bib`\n**Tex files**: `docs/paper/main.tex` + 7 section files\n\n**Total entries**: 53\n**Cited in tex**: 53 (all used)\n**Orphan bib entries** (bib exists, tex never cites): 0\n**Missing bib entries** (tex cites, bib missing): 0\n**Duplicate entries**: 0\n\n---\n\n## Auto-Fixed Issues\n\n### 1. [severity: warning] `tripathi2025pairwise` — arXiv → COLM 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2504.14716}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)}`, year=2025\n\n### 2. [severity: warning] `wang2023faireval` — arXiv → ACL 2024\n- Was: `@article` with `journal={arXiv preprint arXiv:2305.17926}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2024\n- Also added missing author \"Kong, Lingpeng\" and updated URL to ACL Anthology\n\n### 3. [severity: warning] `li2024calibraeval` — arXiv → ACL 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2410.15393}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology\n\n### 4. [severity: warning] `ye2024justice` — arXiv → ICLR 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2410.02736}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2025\n- Also added 2 missing authors: Chawla, Nitesh V. and Zhang, Xiangliang\n\n### 5. [severity: warning] `he2021debertav3` — arXiv → ICLR 2023\n- Was: `@article` with `journal={arXiv preprint arXiv:2111.09543}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2023\n\n### 6. [severity: warning] `shi2024judging` — arXiv → IJCNLP-AACL 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2406.07791}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology\n\n---\n\n## Remaining arXiv Preprints (No Published Version Found)\n\nThese were searched and no formal venue publication was found as of 2026-05-22:\n\n### 7. [severity: info] `wang2026fairjudge` — arXiv:2602.06625, still preprint\n### 8. [severity: info] `casse2026concise` — arXiv:2601.10809, still preprint\n### 9. [severity: info] `counterfactual2025rhetorical` — arXiv:2512.19908, still preprint (OpenReview submission exists but no acceptance confirmed)\n### 10. [severity: info] `soumik2026judging` — arXiv:2604.23178, still preprint\n### 11. [severity: info] `celikyilmaz2020evaluation` — arXiv:2006.14799, still preprint (6 years old, likely will remain preprint)\n### 12. [severity: info] `stureborg2024inconsistent` — arXiv:2405.01724, still preprint\n\n---\n\n## Key Name Mismatches (Not Fixed — Would Break Citations)\n\n### 13. [severity: info] `wang2026fairjudge` — first author is \"Yang, Bo\", not \"Wang\"\n- Key doesn't match first author convention. Not changed because renaming would require updating all tex files.\n\n### 14. [severity: info] `casse2026concise` — first author is \"Cho, Young-Min\", not \"Casse\"\n- Key derived from method name (CASSE), not author. Unconventional but functional. Tex cites it as `\\citep{casse2026concise}` where it refers to \"CASSE\" system.\n\n### 15. [severity: info] `counterfactual2025rhetorical` — first author is \"Qiu, Jingyi\"\n- Key derived from content descriptor, not author. Unconventional but functional.\n\n### 16. [severity: info] Key year mismatches (arXiv date vs. publication year):\n- `boubdir2023elo`: key=2023, year=2024 (NeurIPS 2024)\n- `wu2023style`: key=2023, year=2025 (COLING 2025)\n- `zeng2023llmbar`: key=2023, year=2024 (ICLR 2024)\n- Not changed — these are common when the arXiv preprint predates the venue year. Changing keys would require tex updates.\n\n---\n\n## Abbreviated Author Lists\n\n### 17. [severity: info] Six entries use `and others` instead of full author lists:\n- `murugadoss2025sos`, `li2026preference`, `dubois2025lc`, `soumik2026judging`, `tan2025judgebench`, `bavaresco2025llms`\n- BibTeX renders these correctly as \"et al.\" — functionally correct but bibliographically incomplete.\n\n---\n\n## Tripathi Citation Check (R7-REF1)\n\n- **Status**: ✅ Correctly included and cited\n- Bib entry `tripathi2025pairwise` present (lines 1-7)\n- Cited in `experiments.tex` line 135: `\\citet{tripathi2025pairwise}`\n- Context: \"independently confirm that pairwise and pointwise protocols exhibit distinct sensitivity profiles\"\n- **Updated**: from arXiv preprint to published COLM 2025 venue\n\n---\n\n## Items Requiring Human Confirmation\n\n1. **`wang2026fairjudge` key mismatch**: First author is Yang Bo, not Wang. Consider renaming to `yang2026fairjudge` if desired (requires updating tex files).\n2. **`casse2026concise` and `counterfactual2025rhetorical`**: Non-standard key naming. Consider standardizing if time permits.\n3. **Six `and others` entries**: Consider expanding to full author lists for bibliographic completeness.\n4. **`celikyilmaz2020evaluation`**: 6-year-old preprint with no published version. Consider whether a more recent survey could replace it, or accept as-is.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "e1087ff8-afc7-4dfa-aaa7-6dbe7b09b32c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014sSnhWe8nSGf1wFSRxtwy8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8511,
      "cache_read_input_tokens": 84561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8511
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

_source line 96 · 2026-05-22T01:14:00.712Z_

<details><summary>↩ Tool result · `toolu_011JRqEDydTb3XsmSa9tuuY4`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'reference_audit_report.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "0ac7b1e6-e7a0-4df0-b603-c2ce5e1a47e7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'reference_audit_report.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'reference_audit_report.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml'].\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 97_

<details><summary>Logged reasoning block</summary>

```text
The MCP tool can only write specific files. Let me write it directly to the project artifacts directory.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "013cfcb4-ccd9-41bb-9d0a-0d9b65edfcc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KB3dnJniGhwRRhpAHQkyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2076,
      "cache_read_input_tokens": 93072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2076
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

_source line 98_

MCP tool restricted to specific files. Let me write the report directly to the artifacts directory.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "8337da70-76ed-489e-97cf-c0aafcb80eb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KB3dnJniGhwRRhpAHQkyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2076,
      "cache_read_input_tokens": 93072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2076
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

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01Aq5hbJ73hzEW7SGYwR7Qv6`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "c8e8ee60-1324-40ed-9fe1-7bb0d900fc5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KB3dnJniGhwRRhpAHQkyt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2076,
      "cache_read_input_tokens": 93072,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2076
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

_source line 100 · 2026-05-22T01:14:13.123Z_

<details><summary>↩ Tool result · `toolu_01Aq5hbJ73hzEW7SGYwR7Qv6`</summary>

```text
_project
bootstrap_attenuation
bootstrap_attenuation.json
csd_pipeline
debiased_llama70b_summary.json
debiased_verbosity_gpt4o
debiased_verbosity_gpt4o_summary.json
double_rewrite_placebo.py
dream_reports
exp-002
exp-013
exp-015
exp-016
figure1_candidates.json
figures
finegrained_likert_100pt
finegrained_likert_100pt.json
gee_interaction_analysis.json
gpt4o_analysis.py
gpu_status_check.md
human_annotation
llama70b_analysis.py
llama70b_debiased
llama70b_register
llama70b_register_summary.json
llama70b_third_judge
llama70b_third_judge.json
manifest.yaml
nli_fn_bias
nli_threshold_sweep
nli_threshold_sweep.json
pairwise_results_debiased_llama70b_formality.jsonl
pairwise_results_debiased_llama70b_verbosity.jsonl
pairwise_results_llama70b_formality.jsonl
pairwise_results_llama70b_register.jsonl
pairwise_results_llama70b_verbosity.jsonl
power_analysis_formal.json
reanalysis_outputs
requirements.txt
response_letter_draft.md
review_issues.yaml
review_reports
run_mvp.sh
scored_llama70b_formality.jsonl
scored_llama70b_register.jsonl
scored_llama70b_verbosity.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "d929a9e2-5e4e-4458-869c-a31a27dfacd9",
  "tool_use_result": {
    "stdout": "_project\nbootstrap_attenuation\nbootstrap_attenuation.json\ncsd_pipeline\ndebiased_llama70b_summary.json\ndebiased_verbosity_gpt4o\ndebiased_verbosity_gpt4o_summary.json\ndouble_rewrite_placebo.py\ndream_reports\nexp-002\nexp-013\nexp-015\nexp-016\nfigure1_candidates.json\nfigures\nfinegrained_likert_100pt\nfinegrained_likert_100pt.json\ngee_interaction_analysis.json\ngpt4o_analysis.py\ngpu_status_check.md\nhuman_annotation\nllama70b_analysis.py\nllama70b_debiased\nllama70b_register\nllama70b_register_summary.json\nllama70b_third_judge\nllama70b_third_judge.json\nmanifest.yaml\nnli_fn_bias\nnli_threshold_sweep\nnli_threshold_sweep.json\npairwise_results_debiased_llama70b_formality.jsonl\npairwise_results_debiased_llama70b_verbosity.jsonl\npairwise_results_llama70b_formality.jsonl\npairwise_results_llama70b_register.jsonl\npairwise_results_llama70b_verbosity.jsonl\npower_analysis_formal.json\nreanalysis_outputs\nrequirements.txt\nresponse_letter_draft.md\nreview_issues.yaml\nreview_reports\nrun_mvp.sh\nscored_llama70b_formality.jsonl\nscored_llama70b_register.jsonl\nscored_llama70b_verbosity.jsonl",
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

_source line 101_

<details open><summary>🔧 Tool call — Write · `toolu_01TSVm6RXqfdZophyu7ErfAv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/reference_audit_report.md",
  "content": "# Reference Audit Report\n\n**Date**: 2026-05-22\n**Bib file**: `docs/paper/references.bib`\n**Tex files**: `docs/paper/main.tex` + 7 section files\n\n**Total entries**: 53\n**Cited in tex**: 53 (all used)\n**Orphan bib entries** (bib exists, tex never cites): 0\n**Missing bib entries** (tex cites, bib missing): 0\n**Duplicate entries**: 0\n\n---\n\n## Auto-Fixed Issues\n\n### 1. [severity: warning] `tripathi2025pairwise` — arXiv → COLM 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2504.14716}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)}`, year=2025\n\n### 2. [severity: warning] `wang2023faireval` — arXiv → ACL 2024\n- Was: `@article` with `journal={arXiv preprint arXiv:2305.17926}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2024\n- Also added missing author \"Kong, Lingpeng\" and updated URL to ACL Anthology\n\n### 3. [severity: warning] `li2024calibraeval` — arXiv → ACL 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2410.15393}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology\n\n### 4. [severity: warning] `ye2024justice` — arXiv → ICLR 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2410.02736}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2025\n- Also added 2 missing authors: Chawla, Nitesh V. and Zhang, Xiangliang\n\n### 5. [severity: warning] `he2021debertav3` — arXiv → ICLR 2023\n- Was: `@article` with `journal={arXiv preprint arXiv:2111.09543}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2023\n\n### 6. [severity: warning] `shi2024judging` — arXiv → IJCNLP-AACL 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2406.07791}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology\n\n---\n\n## Remaining arXiv Preprints (No Published Version Found)\n\nThese were searched and no formal venue publication was found as of 2026-05-22:\n\n### 7. [severity: info] `wang2026fairjudge` — arXiv:2602.06625, still preprint\n### 8. [severity: info] `casse2026concise` — arXiv:2601.10809, still preprint\n### 9. [severity: info] `counterfactual2025rhetorical` — arXiv:2512.19908, still preprint (OpenReview submission exists but no acceptance confirmed)\n### 10. [severity: info] `soumik2026judging` — arXiv:2604.23178, still preprint\n### 11. [severity: info] `celikyilmaz2020evaluation` — arXiv:2006.14799, still preprint (6 years old, likely will remain preprint)\n### 12. [severity: info] `stureborg2024inconsistent` — arXiv:2405.01724, still preprint\n\n---\n\n## Key Name Mismatches (Not Fixed — Would Break Citations)\n\n### 13. [severity: info] `wang2026fairjudge` — first author is \"Yang, Bo\", not \"Wang\"\n- Key doesn't match first author convention. Not changed because renaming would require updating all tex files.\n\n### 14. [severity: info] `casse2026concise` — first author is \"Cho, Young-Min\", not \"Casse\"\n- Key derived from method name (CASSE), not author. Unconventional but functional.\n\n### 15. [severity: info] `counterfactual2025rhetorical` — first author is \"Qiu, Jingyi\"\n- Key derived from content descriptor, not author. Unconventional but functional.\n\n### 16. [severity: info] Key year mismatches (arXiv date vs. publication year):\n- `boubdir2023elo`: key=2023, year=2024 (NeurIPS 2024)\n- `wu2023style`: key=2023, year=2025 (COLING 2025)\n- `zeng2023llmbar`: key=2023, year=2024 (ICLR 2024)\n- Not changed — common when arXiv preprint predates venue year. Changing keys would require tex updates.\n\n---\n\n## Abbreviated Author Lists\n\n### 17. [severity: info] Six entries use `and others` instead of full author lists:\n- `murugadoss2025sos`, `li2026preference`, `dubois2025lc`, `soumik2026judging`, `tan2025judgebench`, `bavaresco2025llms`\n- BibTeX renders these correctly as \"et al.\" — functionally correct but bibliographically incomplete.\n\n---\n\n## Tripathi Citation Check (R7-REF1)\n\n- **Status**: Correctly included and cited\n- Bib entry `tripathi2025pairwise` present (lines 1-7)\n- Cited in `experiments.tex` line 135: `\\citet{tripathi2025pairwise}`\n- Context: \"independently confirm that pairwise and pointwise protocols exhibit distinct sensitivity profiles\"\n- **Updated**: from arXiv preprint to published COLM 2025 venue\n\n---\n\n## Items Requiring Human Confirmation\n\n1. **`wang2026fairjudge` key mismatch**: First author is Yang Bo, not Wang. Consider renaming to `yang2026fairjudge` if desired (requires updating tex files).\n2. **`casse2026concise` and `counterfactual2025rhetorical`**: Non-standard key naming. Consider standardizing if time permits.\n3. **Six `and others` entries**: Consider expanding to full author lists for bibliographic completeness.\n4. **`celikyilmaz2020evaluation`**: 6-year-old preprint with no published version. Consider whether a more recent survey could replace it, or accept as-is.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "438aad82-ec32-4409-9315-560d159a47e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gAfTL1wVRqWrCeFduZgUg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 95148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 582
      },
      "output_tokens": 53,
      "service_tier": "standard",
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

_source line 102 · 2026-05-22T01:14:56.414Z_

<details><summary>↩ Tool result · `toolu_01TSVm6RXqfdZophyu7ErfAv`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/reference_audit_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "8654b223-4436-40d6-98f0-0b75ffd8443e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_5/projects/causal_style_decomp_judge/artifacts/reference_audit_report.md",
    "content": "# Reference Audit Report\n\n**Date**: 2026-05-22\n**Bib file**: `docs/paper/references.bib`\n**Tex files**: `docs/paper/main.tex` + 7 section files\n\n**Total entries**: 53\n**Cited in tex**: 53 (all used)\n**Orphan bib entries** (bib exists, tex never cites): 0\n**Missing bib entries** (tex cites, bib missing): 0\n**Duplicate entries**: 0\n\n---\n\n## Auto-Fixed Issues\n\n### 1. [severity: warning] `tripathi2025pairwise` — arXiv → COLM 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2504.14716}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)}`, year=2025\n\n### 2. [severity: warning] `wang2023faireval` — arXiv → ACL 2024\n- Was: `@article` with `journal={arXiv preprint arXiv:2305.17926}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2024\n- Also added missing author \"Kong, Lingpeng\" and updated URL to ACL Anthology\n\n### 3. [severity: warning] `li2024calibraeval` — arXiv → ACL 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2410.15393}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology\n\n### 4. [severity: warning] `ye2024justice` — arXiv → ICLR 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2410.02736}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2025\n- Also added 2 missing authors: Chawla, Nitesh V. and Zhang, Xiangliang\n\n### 5. [severity: warning] `he2021debertav3` — arXiv → ICLR 2023\n- Was: `@article` with `journal={arXiv preprint arXiv:2111.09543}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2023\n\n### 6. [severity: warning] `shi2024judging` — arXiv → IJCNLP-AACL 2025\n- Was: `@article` with `journal={arXiv preprint arXiv:2406.07791}`\n- Fixed: `@inproceedings` with `booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology\n\n---\n\n## Remaining arXiv Preprints (No Published Version Found)\n\nThese were searched and no formal venue publication was found as of 2026-05-22:\n\n### 7. [severity: info] `wang2026fairjudge` — arXiv:2602.06625, still preprint\n### 8. [severity: info] `casse2026concise` — arXiv:2601.10809, still preprint\n### 9. [severity: info] `counterfactual2025rhetorical` — arXiv:2512.19908, still preprint (OpenReview submission exists but no acceptance confirmed)\n### 10. [severity: info] `soumik2026judging` — arXiv:2604.23178, still preprint\n### 11. [severity: info] `celikyilmaz2020evaluation` — arXiv:2006.14799, still preprint (6 years old, likely will remain preprint)\n### 12. [severity: info] `stureborg2024inconsistent` — arXiv:2405.01724, still preprint\n\n---\n\n## Key Name Mismatches (Not Fixed — Would Break Citations)\n\n### 13. [severity: info] `wang2026fairjudge` — first author is \"Yang, Bo\", not \"Wang\"\n- Key doesn't match first author convention. Not changed because renaming would require updating all tex files.\n\n### 14. [severity: info] `casse2026concise` — first author is \"Cho, Young-Min\", not \"Casse\"\n- Key derived from method name (CASSE), not author. Unconventional but functional.\n\n### 15. [severity: info] `counterfactual2025rhetorical` — first author is \"Qiu, Jingyi\"\n- Key derived from content descriptor, not author. Unconventional but functional.\n\n### 16. [severity: info] Key year mismatches (arXiv date vs. publication year):\n- `boubdir2023elo`: key=2023, year=2024 (NeurIPS 2024)\n- `wu2023style`: key=2023, year=2025 (COLING 2025)\n- `zeng2023llmbar`: key=2023, year=2024 (ICLR 2024)\n- Not changed — common when arXiv preprint predates venue year. Changing keys would require tex updates.\n\n---\n\n## Abbreviated Author Lists\n\n### 17. [severity: info] Six entries use `and others` instead of full author lists:\n- `murugadoss2025sos`, `li2026preference`, `dubois2025lc`, `soumik2026judging`, `tan2025judgebench`, `bavaresco2025llms`\n- BibTeX renders these correctly as \"et al.\" — functionally correct but bibliographically incomplete.\n\n---\n\n## Tripathi Citation Check (R7-REF1)\n\n- **Status**: Correctly included and cited\n- Bib entry `tripathi2025pairwise` present (lines 1-7)\n- Cited in `experiments.tex` line 135: `\\citet{tripathi2025pairwise}`\n- Context: \"independently confirm that pairwise and pointwise protocols exhibit distinct sensitivity profiles\"\n- **Updated**: from arXiv preprint to published COLM 2025 venue\n\n---\n\n## Items Requiring Human Confirmation\n\n1. **`wang2026fairjudge` key mismatch**: First author is Yang Bo, not Wang. Consider renaming to `yang2026fairjudge` if desired (requires updating tex files).\n2. **`casse2026concise` and `counterfactual2025rhetorical`**: Non-standard key naming. Consider standardizing if time permits.\n3. **Six `and others` entries**: Consider expanding to full author lists for bibliographic completeness.\n4. **`celikyilmaz2020evaluation`**: 6-year-old preprint with no published version. Consider whether a more recent survey could replace it, or accept as-is.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 103_

审计完成。

**已自动修复 6 项**（arXiv → 正式发表版本）：
- `tripathi2025pairwise` → COLM 2025
- `wang2023faireval` → ACL 2024（补全作者 Kong, Lingpeng）
- `li2024calibraeval` → ACL 2025
- `ye2024justice` → ICLR 2025（补全 2 位缺失作者）
- `he2021debertav3` → ICLR 2023
- `shi2024judging` → IJCNLP-AACL 2025

**交叉引用**：53 条 bib 全部被 tex 引用，tex 中无缺失引用，无冗余条目，无重复。

**Tripathi (R7-REF1)**：已正确包含并引用于 `experiments.tex:135`，已从 arXiv 升级为 COLM 2025。

**6 条仍为 arXiv preprint**（未找到正式版本）：wang2026fairjudge、casse2026concise、counterfactual2025rhetorical、soumik2026judging、celikyilmaz2020evaluation、stureborg2024inconsistent。

**需人工确认 4 项**见报告末尾（key 命名不规范、`and others` 缩写、老 preprint 是否替换）。

报告路径：`artifacts/reference_audit_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "uuid": "152c8896-7061-47b5-a1dc-aa2f963bf9d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PE6kPn2fUrycnxd3ZgkwWp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1949,
      "cache_read_input_tokens": 95730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1949
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

_source line 104_

审计完成。

**已自动修复 6 项**（arXiv → 正式发表版本）：
- `tripathi2025pairwise` → COLM 2025
- `wang2023faireval` → ACL 2024（补全作者 Kong, Lingpeng）
- `li2024calibraeval` → ACL 2025
- `ye2024justice` → ICLR 2025（补全 2 位缺失作者）
- `he2021debertav3` → ICLR 2023
- `shi2024judging` → IJCNLP-AACL 2025

**交叉引用**：53 条 bib 全部被 tex 引用，tex 中无缺失引用，无冗余条目，无重复。

**Tripathi (R7-REF1)**：已正确包含并引用于 `experiments.tex:135`，已从 arXiv 升级为 COLM 2025。

**6 条仍为 arXiv preprint**（未找到正式版本）：wang2026fairjudge、casse2026concise、counterfactual2025rhetorical、soumik2026judging、celikyilmaz2020evaluation、stureborg2024inconsistent。

**需人工确认 4 项**见报告末尾（key 命名不规范、`and others` 缩写、老 preprint 是否替换）。

报告路径：`artifacts/reference_audit_report.md`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 387391,
  "duration_api_ms": 451761,
  "num_turns": 40,
  "stop_reason": "end_turn",
  "session_id": "da085466-b8d8-449b-a208-1385c230dba9",
  "total_cost_usd": 1.7719094999999998,
  "usage": {
    "input_tokens": 4549,
    "cache_creation_input_tokens": 86232,
    "cache_read_input_tokens": 812729,
    "output_tokens": 18747,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 86232,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 403,
        "cache_read_input_tokens": 95730,
        "cache_creation_input_tokens": 1949,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1949
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 159935,
      "outputTokens": 5048,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 15,
      "costUSD": 0.335175,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 4549,
      "outputTokens": 18747,
      "cacheReadInputTokens": 812729,
      "cacheCreationInputTokens": 86232,
      "webSearchRequests": 0,
      "costUSD": 1.4367345,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3afa43ad-0b71-410e-ba62-13b71863b30b"
}
```

</details>

---
