# paper research lit batch2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 57
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_paper_research_lit_batch2_20260514T180832.log`
- **Structured JSON:** [`54d6ab15a390e4dba521.json`](../../sessions/54/54d6ab15a390e4dba521.json)

## Before a recorded user message

57 recorded events

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
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
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
  "uuid": "0f19a18a-d528-4ead-8e57-9d5ceee87eb1",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778796000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "6fad4540-b797-4454-9b31-eb37820030fc",
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to add 9 papers across 3 clusters to a literature_map.yaml file. Let me start by:

1. Reading the existing literature_map.yaml
2. Searching for each paper's details
3. Appending the entries

Let me first read the existing file and search for papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "a6597989-2fe0-43e1-a89f-c155ff65de89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016nBiKKMV5wuBDtG6gipyeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12241,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12241
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

### Assistant

_source line 5_

先读取现有 YAML 文件，同时搜索论文信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "43b45877-b444-4d04-8df0-60e8af26e594",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016nBiKKMV5wuBDtG6gipyeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12241,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12241
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

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_014AvfG7wfX3EDNJLqx3YY9x`</summary>

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
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "49aceb0e-2265-42d7-b70a-8da57afd8c59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016nBiKKMV5wuBDtG6gipyeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12241,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12241
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

_source line 7 · 2026-05-14T18:08:46.752Z_

<details><summary>↩ Tool result · `toolu_014AvfG7wfX3EDNJLqx3YY9x`</summary>

```text
1	meta:
2	  last_updated: '2026-05-14T17:52:10.000Z'
3	  total_papers: 21
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
68	    relevance: 'Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free
69	      quality estimation that we compare against for structured IE.'
70	    abstract: ''
71	    semantic_scholar_id: ''
72	    verified: true
73	    added_by: paper-research:cluster1
74	    added_at: '2026-05-14T15:47:22.188Z'
75	  kim2026reasc:
76	    title: 'Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning'
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
109	    relevance: 'Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related
110	      to our structured output aggregation approach.'
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
156	    relevance: 'Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations
157	      diverge. Motivates our consistency-based quality signal for IE.'
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
221	    relevance: 'CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.
222	      Provides theoretical grounding for our dual-signal approach in structured IE.'
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
243	    relevance: 'Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid
244	      CoCoA yields best calibration, supporting our multi-signal aggregation design.'
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
266	    relevance: 'Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for
267	      positioning our consistency-based confidence approach within the broader landscape.'
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
312	      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps with geng2024 main survey]'
313	    abstract: ''
314	    semantic_scholar_id: ''
315	    verified: true
316	    added_by: paper-research:lit_batch1
317	    added_at: '2026-05-14T17:52:10.000Z'
318	  liu2025uqcalibration:
319	    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'
320	    authors:
321	    - Xiaoou Liu
322	    - Tiejin Chen
323	    - Longchao Da
324	    - Chacha Chen
325	    - Zhen Lin
326	    - Hua Wei
327	    year: 2025
328	    venue: KDD 2025
329	    url: https://arxiv.org/abs/2503.15850
330	    doi: 10.1145/3711896.3736569
331	    bibtex_key: liu2025uqcalibration
332	    category: confidence_surveys
333	    role: supplementary
334	    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements
335	      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps with geng2024 main survey]'
336	    abstract: ''
337	    semantic_scholar_id: ''
338	    verified: true
339	    added_by: paper-research:lit_batch1
340	    added_at: '2026-05-14T17:52:10.000Z'
341	  kuhn2023semantic:
342	    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'
343	    authors:
344	    - Lorenz Kuhn
345	    - Yarin Gal
346	    - Sebastian Farquhar
347	    year: 2023
348	    venue: ICLR 2023
349	    url: https://arxiv.org/abs/2302.09664
350	    doi: ''
351	    bibtex_key: kuhn2023semantic
352	    category: uncertainty_calibration
353	    role: foundation
354	    relevance: 'Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs.
355	      Foundation for our structured consistency metric that operates at the semantic level of IE triples.'
356	    abstract: ''
357	    semantic_scholar_id: ''
358	    verified: true
359	    added_by: paper-research:lit_batch1
360	    added_at: '2026-05-14T17:52:10.000Z'
361	  kadavath2022language:
362	    title: Language Models (Mostly) Know What They Know
363	    authors:
364	    - Saurav Kadavath
365	    - Tom Conerly
366	    - Amanda Askell
367	    - Tom Henighan
368	    - Dawn Drain
369	    - Ethan Perez
370	    - Nicholas Schiefer
371	    - Zac Hatfield-Dodds
372	    - Nova DasSarma
373	    - Eli Tran-Johnson
374	    - Scott Johnston
375	    - Sheer El-Showk
376	    - Andy Jones
377	    - Nelson Elhage
378	    - Tristan Hume
379	    - Anna Chen
380	    - Yuntao Bai
381	    - Sam Bowman
382	    - Stanislav Fort
383	    - Deep Ganguli
384	    - Danny Hernandez
385	    - Josh Jacobson
386	    - Jackson Kernion
387	    - Shauna Kravec
388	    - Liane Lovitt
389	    - Kamal Ndousse
390	    - Catherine Olsson
391	    - Sam Ringer
392	    - Dario Amodei
393	    - Tom Brown
394	    - Jack Clark
395	    - Nicholas Joseph
396	    - Ben Mann
397	    - Sam McCandlish
398	    - Chris Olah
399	    - Jared Kaplan
400	    year: 2022
401	    venue: arXiv preprint
402	    url: https://arxiv.org/abs/2207.05221
403	    doi: ''
404	    bibtex_key: kadavath2022language
405	    category: uncertainty_calibration
406	    role: foundation
407	    relevance: 'Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge
408	      as a confidence signal, which we extend to structured IE output quality estimation.'
409	    abstract: ''
410	    semantic_scholar_id: ''
411	    verified: true
412	    added_by: paper-research:lit_batch1
413	    added_at: '2026-05-14T17:52:10.000Z'
414	  guo2017calibration:
415	    title: On Calibration of Modern Neural Networks
416	    authors:
417	    - Chuan Guo
418	    - Geoff Pleiss
419	    - Yu Sun
420	    - Kilian Q. Weinberger
421	    year: 2017
422	    venue: ICML 2017
423	    url: https://arxiv.org/abs/1706.04599
424	    doi: ''
425	    bibtex_key: guo2017calibration
426	    category: uncertainty_calibration
427	    role: foundation
428	    relevance: 'Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational
429	      reference for all calibration work including our LLM confidence calibration for IE.'
430	    abstract: ''
431	    semantic_scholar_id: ''
432	    verified: true
433	    added_by: paper-research:lit_batch1
434	    added_at: '2026-05-14T17:52:10.000Z'
435	  desai2020calibration:
436	    title: Calibration of Pre-trained Transformers
437	    authors:
438	    - Shrey Desai
439	    - Greg Durrett
440	    year: 2020
441	    venue: EMNLP 2020
442	    url: https://arxiv.org/abs/2003.07892
443	    doi: 10.18653/v1/2020.emnlp-main.21
444	    bibtex_key: desai2020calibration
445	    category: uncertainty_calibration
446	    role: foundation
447	    relevance: 'Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical
448	      calibration to the transformer era, motivating our LLM-specific calibration analysis.'
449	    abstract: ''
450	    semantic_scholar_id: ''
451	    verified: true
452	    added_by: paper-research:lit_batch1
453	    added_at: '2026-05-14T17:52:10.000Z'
454	  kossen2024semantic:
455	    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'
456	    authors:
457	    - Jannik Kossen
458	    - Jiatong Han
459	    - Muhammed Razzak
460	    - Lisa Schut
461	    - Shreshth Malik
462	    - Yarin Gal
463	    year: 2024
464	    venue: arXiv preprint
465	    url: https://arxiv.org/abs/2406.15927
466	    doi: ''
467	    bibtex_key: kossen2024semantic
468	    category: uncertainty_calibration
469	    role: background
470	    relevance: 'Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing
471	      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.'
472	    abstract: ''
473	    semantic_scholar_id: ''
474	    verified: true
475	    added_by: paper-research:lit_batch1
476	    added_at: '2026-05-14T17:52:10.000Z'
477	  xiong2024verbalized:
478	    title: 'Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs'
479	    authors:
480	    - Miao Xiong
481	    - Zhiyuan Hu
482	    - Xinyang Lu
483	    - Yifei Li
484	    - Jie Fu
485	    - Junxian He
486	    - Bryan Hooi
487	    year: 2024
488	    venue: ICLR 2024
489	    url: https://arxiv.org/abs/2306.13063
490	    doi: ''
491	    bibtex_key: xiong2024verbalized
492	    category: uncertainty_calibration
493	    role: background
494	    relevance: 'Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly
495	      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.'
496	    abstract: ''
497	    semantic_scholar_id: ''
498	    verified: true
499	    added_by: paper-research:lit_batch1
500	    added_at: '2026-05-14T17:52:10.000Z'
501	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "1ec68d15-90cd-43c6-a9c3-f54cec3c3d31",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
      "content": "meta:\n  last_updated: '2026-05-14T17:52:10.000Z'\n  total_papers: 21\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: 'Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning'\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: 'CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: 'Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: 'Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: 'Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs.\n      Foundation for our structured consistency metric that operates at the semantic level of IE triples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: 'Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: 'Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: 'Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: 'Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: 'Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs'\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: 'Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n",
      "numLines": 501,
      "startLine": 1,
      "totalLines": 501
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HzrAwDE5gGE7DmV4X291uP`</summary>

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
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "5e415353-6011-42d2-a408-3c76de0e3ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016nBiKKMV5wuBDtG6gipyeG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12241,
      "cache_read_input_tokens": 11701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12241
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

_source line 9 · 2026-05-14T18:08:47.306Z_

<details><summary>↩ Tool result · `toolu_01HzrAwDE5gGE7DmV4X291uP`</summary>

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
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "d27fc2c0-01ea-469a-b91d-e16afb900fac",
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

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the existing YAML file with 21 papers. I need to search for 9 papers across 3 clusters. Let me search for all of them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "f18a23fb-2090-4989-8d83-035a0f92acb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 11_

现有 21 篇论文。开始搜索 9 篇论文的信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "05c839c4-6c05-421e-98a8-88369926645b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016cjaCWwrLSat8KJiSskhLL`</summary>

```json
{
  "query": "Fisch et al 2021 \"Few-Shot Conformal Prediction with Auxiliary Tasks\" NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "aba2dde2-fed4-45a6-805e-0750a7fc7984",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TjVZngVrwwimQCqpYmQp29`</summary>

```json
{
  "query": "Angelopoulos et al 2021 \"Uncertainty Sets for Image Classifiers using Conformal Prediction\" ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "40504591-59c2-45b0-bad4-373bf7cc140a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LcDncAJzuALDNkny5eX8Su`</summary>

```json
{
  "query": "conformal prediction NLP sequence labeling 2021 2022 2023 Bates structured prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "949c9a0f-07c8-4126-98b9-bcfb76482110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HA2RHVhd2JTVf5gBmEt34P`</summary>

```json
{
  "query": "Xiao Wang 2019 \"Quantifying Uncertainties in Natural Language Processing Tasks\" AAAI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "5a6e2e80-b62c-4490-8d40-d40530f5f3b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F27P5taqoJjJFA6Ew9L97g`</summary>

```json
{
  "query": "Shelmanov 2021 NER uncertainty active learning ACL EMNLP EACL structured prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "32dc1e38-035c-4f2f-8214-f69ad6ddba0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013VEaRDy1L1dNS8gRdCo2Wn`</summary>

```json
{
  "query": "He 2020 NER uncertainty estimation token-level ACL named entity recognition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "c09de7c0-cc5d-4391-8ec9-de3a1db7960b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DYMiR1k6WgnocbjVdU3ns9`</summary>

```json
{
  "query": "Lakshminarayanan 2017 \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\" NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "69fec406-aeae-4a3e-90c8-1d49516861be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015FLa77e7Ef9tiiLkbCYJgq`</summary>

```json
{
  "query": "Gal Ghahramani 2016 \"Dropout as a Bayesian Approximation\" ICML uncertainty deep learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "a18708b1-b678-41eb-bbce-5700b92856e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 20 · 2026-05-14T18:08:58.270Z_

<details><summary>↩ Tool result · `toolu_016cjaCWwrLSat8KJiSskhLL`</summary>

```text
Web search results for query: "Fisch et al 2021 "Few-Shot Conformal Prediction with Auxiliary Tasks" NeurIPS"

Links: [{"title":"Few-Shot Conformal Prediction with Auxiliary Tasks","url":"https://proceedings.mlr.press/v139/fisch21a.html"},{"title":"[2102.08898] Few-shot Conformal Prediction with Auxiliary Tasks","url":"https://arxiv.org/abs/2102.08898"},{"title":"Few-shot Conformal Prediction with Auxiliary Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210208898F/abstract"},{"title":"Few-shot Conformal Prediction with Auxiliary Tasks","url":"https://dspace.mit.edu/handle/1721.1/143522"},{"title":"Few-shot Conformal Prediction with Auxiliary Tasks","url":"https://icml.cc/media/icml-2021/Slides/8739.pdf"},{"title":"[PDF] Few-shot Conformal Prediction with Auxiliary Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Few-shot-Conformal-Prediction-with-Auxiliary-Tasks-Fisch-Schuster/36a2c27ffa72c05c2a17dc90b7c54e492b88ba01"},{"title":"Neural Conformal Control for Time Series Forecasting","url":"https://arxiv.org/html/2412.18144"},{"title":"GitHub - ajfisch/few-shot-cp: Few-Shot Conformal Prediction","url":"https://github.com/ajfisch/few-shot-cp"},{"title":"few-shot-cp/README.md at master · ajfisch/few-shot-cp","url":"https://github.com/ajfisch/few-shot-cp/blob/master/README.md"},{"title":"Few-shot Conformal Prediction with Auxiliary Tasks","url":"https://arxiv.org/pdf/2102.08898"}]

I found the paper! Here are the key details about "Few-Shot Conformal Prediction with Auxiliary Tasks" by Fisch et al. (2021):

**Publication Details:**
The paper was published in the Proceedings of the 38th International Conference on Machine Learning (ICML) in 2021, pages 3329-3339. Note: This was published at ICML, not NeurIPS.

**Authors:** Adam Fisch, Tal Schuster, Tommi Jaakkola, and Regina Barzilay

**Main Contribution:**
The paper develops a novel approach to conformal prediction when the target task has limited data available for training. Conformal prediction identifies a small set of promising output candidates in place of a single prediction, with guarantees that the set contains the correct answer with high probability.

The authors obtain substantially tighter prediction sets while maintaining desirable marginal guarantees by casting conformal prediction as a meta-learning paradigm over exchangeable collections of auxiliary tasks.

**Evaluation:**
The approach was demonstrated across a number of few-shot classification and regression tasks in natural language processing, computer vision, and computational chemistry for drug discovery.

**Availability:**
- Official paper: https://proceedings.mlr.press/v139/fisch21a.html
- arXiv version: https://arxiv.org/abs/2102.08898
- Code: https://github.com/ajfisch/few-shot-cp


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "da95183c-8b92-4305-95c6-ea7a75afc5a9",
  "tool_use_result": {
    "query": "Fisch et al 2021 \"Few-Shot Conformal Prediction with Auxiliary Tasks\" NeurIPS",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YQ9gQWmK4n1r7EYdoHC6kW",
        "content": [
          {
            "title": "Few-Shot Conformal Prediction with Auxiliary Tasks",
            "url": "https://proceedings.mlr.press/v139/fisch21a.html"
          },
          {
            "title": "[2102.08898] Few-shot Conformal Prediction with Auxiliary Tasks",
            "url": "https://arxiv.org/abs/2102.08898"
          },
          {
            "title": "Few-shot Conformal Prediction with Auxiliary Tasks - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210208898F/abstract"
          },
          {
            "title": "Few-shot Conformal Prediction with Auxiliary Tasks",
            "url": "https://dspace.mit.edu/handle/1721.1/143522"
          },
          {
            "title": "Few-shot Conformal Prediction with Auxiliary Tasks",
            "url": "https://icml.cc/media/icml-2021/Slides/8739.pdf"
          },
          {
            "title": "[PDF] Few-shot Conformal Prediction with Auxiliary Tasks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Few-shot-Conformal-Prediction-with-Auxiliary-Tasks-Fisch-Schuster/36a2c27ffa72c05c2a17dc90b7c54e492b88ba01"
          },
          {
            "title": "Neural Conformal Control for Time Series Forecasting",
            "url": "https://arxiv.org/html/2412.18144"
          },
          {
            "title": "GitHub - ajfisch/few-shot-cp: Few-Shot Conformal Prediction",
            "url": "https://github.com/ajfisch/few-shot-cp"
          },
          {
            "title": "few-shot-cp/README.md at master · ajfisch/few-shot-cp",
            "url": "https://github.com/ajfisch/few-shot-cp/blob/master/README.md"
          },
          {
            "title": "Few-shot Conformal Prediction with Auxiliary Tasks",
            "url": "https://arxiv.org/pdf/2102.08898"
          }
        ]
      },
      "I found the paper! Here are the key details about \"Few-Shot Conformal Prediction with Auxiliary Tasks\" by Fisch et al. (2021):\n\n**Publication Details:**\nThe paper was published in the Proceedings of the 38th International Conference on Machine Learning (ICML) in 2021, pages 3329-3339. Note: This was published at ICML, not NeurIPS.\n\n**Authors:** Adam Fisch, Tal Schuster, Tommi Jaakkola, and Regina Barzilay\n\n**Main Contribution:**\nThe paper develops a novel approach to conformal prediction when the target task has limited data available for training. Conformal prediction identifies a small set of promising output candidates in place of a single prediction, with guarantees that the set contains the correct answer with high probability.\n\nThe authors obtain substantially tighter prediction sets while maintaining desirable marginal guarantees by casting conformal prediction as a meta-learning paradigm over exchangeable collections of auxiliary tasks.\n\n**Evaluation:**\nThe approach was demonstrated across a number of few-shot classification and regression tasks in natural language processing, computer vision, and computational chemistry for drug discovery.\n\n**Availability:**\n- Official paper: https://proceedings.mlr.press/v139/fisch21a.html\n- arXiv version: https://arxiv.org/abs/2102.08898\n- Code: https://github.com/ajfisch/few-shot-cp"
    ],
    "durationSeconds": 5.893544445
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ba6F4ACnpA9ujD4RLtxN69`</summary>

```json
{
  "query": "Fomicheva 2020 \"Unsupervised Quality Estimation for Neural Machine Translation\" MC dropout ensemble uncertainty NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "af8f9c9c-8f80-4452-85c1-16acb0e53e3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVnDxcpYzxp4MN4TxkLNAd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7614,
      "cache_read_input_tokens": 23942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7614
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

_source line 22 · 2026-05-14T18:09:00.285Z_

<details><summary>↩ Tool result · `toolu_01TjVZngVrwwimQCqpYmQp29`</summary>

```text
Web search results for query: "Angelopoulos et al 2021 "Uncertainty Sets for Image Classifiers using Conformal Prediction" ICLR"

Links: [{"title":"Uncertainty Sets for Image Classifiers using Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200914193A/abstract"},{"title":"UNCERTAINTY SETS FOR IMAGE CLASSIFIERS USING CONFORMAL PREDICTION","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-classification.pdf"},{"title":"dblp: Uncertainty Sets for Image Classifiers using Conformal Prediction.","url":"https://dblp.org/rec/conf/iclr/AngelopoulosBJM21.html"},{"title":"GitHub - fahaddalwai/ImplementationConfClassification: Implementation of the experiments in 'Uncertainty Sets for Image Classifiers using Conformal Prediction. Angelopoulos, A. N., et al. (2021).ICLR'","url":"https://github.com/fahaddalwai/ImplementationConfClassification"},{"title":"ICLR 2021 Uncertainty Sets for Image Classifiers using Conformal Prediction Spotlight","url":"https://iclr.cc/virtual/2021/spotlight/3435"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2410.01767"},{"title":"Uncertainty Sets for Image Classifiers using Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=eNdiU_DbM9"},{"title":"[2009.14193] Uncertainty Sets for Image Classifiers using Conformal Prediction","url":"https://arxiv.org/abs/2009.14193"},{"title":"Improving uncertainty quantification of deep classifiers via neighborhood conformal prediction | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i6.25936"},{"title":"μ & σ - Conformal classification","url":"https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/conformal-classification/"}]

I found the paper! Here's a summary of the key information about the Angelopoulos et al. 2021 paper:

## Paper Overview

The paper presents an algorithm that modifies any classifier to output a predictive set containing the true label with a user-specified probability (such as 90%), while providing a formal finite-sample coverage guarantee for every model and dataset.

## Key Contributions

While convolutional image classifiers can achieve high predictive accuracy, quantifying their uncertainty remains an unresolved challenge. Existing uncertainty quantification techniques like Platt scaling attempt to calibrate probability estimates but lack formal guarantees.

The method modifies an existing conformal prediction algorithm to give more stable predictive sets by regularizing the small scores of unlikely classes after Platt scaling.

## Experimental Results

In experiments on both ImageNet and ImageNet-V2 with ResNet-152 and other classifiers, the scheme outperforms existing approaches, achieving coverage with sets that are often factors of 5 to 10 smaller than a stand-alone Platt scaling baseline.

## Publication Details

The paper was accepted as an ICLR 2021 Spotlight presentation, and the authors provide a project website at https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/conformal-classification/.

The method is known as **RAPS** (Regularized Adaptive Prediction Sets) and is designed to be simple, fast, and practical for deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "669eb47a-a8bc-443f-a525-7a1b25558ae5",
  "tool_use_result": {
    "query": "Angelopoulos et al 2021 \"Uncertainty Sets for Image Classifiers using Conformal Prediction\" ICLR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HFdMBNwEvN3DnmkCv8H59L",
        "content": [
          {
            "title": "Uncertainty Sets for Image Classifiers using Conformal Prediction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv200914193A/abstract"
          },
          {
            "title": "UNCERTAINTY SETS FOR IMAGE CLASSIFIERS USING CONFORMAL PREDICTION",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-classification.pdf"
          },
          {
            "title": "dblp: Uncertainty Sets for Image Classifiers using Conformal Prediction.",
            "url": "https://dblp.org/rec/conf/iclr/AngelopoulosBJM21.html"
          },
          {
            "title": "GitHub - fahaddalwai/ImplementationConfClassification: Implementation of the experiments in 'Uncertainty Sets for Image Classifiers using Conformal Prediction. Angelopoulos, A. N., et al. (2021).ICLR'",
            "url": "https://github.com/fahaddalwai/ImplementationConfClassification"
          },
          {
            "title": "ICLR 2021 Uncertainty Sets for Image Classifiers using Conformal Prediction Spotlight",
            "url": "https://iclr.cc/virtual/2021/spotlight/3435"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2410.01767"
          },
          {
            "title": "Uncertainty Sets for Image Classifiers using Conformal Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=eNdiU_DbM9"
          },
          {
            "title": "[2009.14193] Uncertainty Sets for Image Classifiers using Conformal Prediction",
            "url": "https://arxiv.org/abs/2009.14193"
          },
          {
            "title": "Improving uncertainty quantification of deep classifiers via neighborhood conformal prediction | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence",
            "url": "https://dl.acm.org/doi/10.1609/aaai.v37i6.25936"
          },
          {
            "title": "μ & σ - Conformal classification",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/conformal-classification/"
          }
        ]
      },
      "I found the paper! Here's a summary of the key information about the Angelopoulos et al. 2021 paper:\n\n## Paper Overview\n\nThe paper presents an algorithm that modifies any classifier to output a predictive set containing the true label with a user-specified probability (such as 90%), while providing a formal finite-sample coverage guarantee for every model and dataset.\n\n## Key Contributions\n\nWhile convolutional image classifiers can achieve high predictive accuracy, quantifying their uncertainty remains an unresolved challenge. Existing uncertainty quantification techniques like Platt scaling attempt to calibrate probability estimates but lack formal guarantees.\n\nThe method modifies an existing conformal prediction algorithm to give more stable predictive sets by regularizing the small scores of unlikely classes after Platt scaling.\n\n## Experimental Results\n\nIn experiments on both ImageNet and ImageNet-V2 with ResNet-152 and other classifiers, the scheme outperforms existing approaches, achieving coverage with sets that are often factors of 5 to 10 smaller than a stand-alone Platt scaling baseline.\n\n## Publication Details\n\nThe paper was accepted as an ICLR 2021 Spotlight presentation, and the authors provide a project website at https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/conformal-classification/.\n\nThe method is known as **RAPS** (Regularized Adaptive Prediction Sets) and is designed to be simple, fast, and practical for deployment."
    ],
    "durationSeconds": 6.898340780999999
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T18:09:00.940Z_

<details><summary>↩ Tool result · `toolu_01LcDncAJzuALDNkny5eX8Su`</summary>

```text
Web search results for query: "conformal prediction NLP sequence labeling 2021 2022 2023 Bates structured prediction"

Links: [{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://aclanthology.org/2024.tacl-1.82.pdf"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"Conformal Prediction and Verification of Large Language Model Extractions in","url":"https://ojs.aaai.org/index.php/AAAI-SS/article/download/36929/39067/41006"},{"title":"Conformal Prediction: A Data Perspective","url":"https://arxiv.org/html/2410.06494v2"},{"title":"Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains","url":"https://arxiv.org/html/2603.00924"},{"title":"Conformal Prediction for Text Infilling and Part-of-Speech Prediction","url":"https://nejsds.nestat.org/journal/NEJSDS/article/10/file/pdf"},{"title":"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/html/2601.16999"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"}]

Based on the search results, I found several relevant resources on conformal prediction applied to NLP sequence labeling tasks:

## Key Findings

**Survey Papers:**
A comprehensive survey on Conformal Prediction for Natural Language Processing was published in 2024, and Angelopoulos and Bates (2023) published a comprehensive survey on conformal prediction.

**Stephen Bates and Conformal Prediction Work:**
Angelopoulos and Bates authored "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification," which describes conformal prediction as a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for model predictions with distribution-free validity guarantees.

**Applications to Sequence Labeling:**
Research has introduced a framework for adapting sequence-labeling-based NER models to produce uncertainty-aware prediction sets that are guaranteed to contain the correct labeling with user-specified confidence, building on conformal prediction which offers finite-sample coverage guarantees.

Inductive conformal prediction algorithms have been proposed for text infilling and part-of-speech (POS) prediction, with ICP-enhanced algorithms for POS tagging based on BERT and BiLSTM.

**Recent Extensions:**
Recent work extends multi-label conformal prediction to identify confident components of long generations and demonstrates valid risk control on multiple diverse tasks.

These resources cover conformal prediction methods specifically designed for structured prediction tasks in NLP during the 2021-2024 period you specified.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "d9ace6f1-06c6-4192-b92d-6c8a743d524b",
  "tool_use_result": {
    "query": "conformal prediction NLP sequence labeling 2021 2022 2023 Bates structured prediction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BU3mLjy7BicBuSRHgry8df",
        "content": [
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://aclanthology.org/2024.tacl-1.82.pdf"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"
          },
          {
            "title": "[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
            "url": "https://arxiv.org/abs/2107.07511"
          },
          {
            "title": "Conformal Prediction and Verification of Large Language Model Extractions in",
            "url": "https://ojs.aaai.org/index.php/AAAI-SS/article/download/36929/39067/41006"
          },
          {
            "title": "Conformal Prediction: A Data Perspective",
            "url": "https://arxiv.org/html/2410.06494v2"
          },
          {
            "title": "Conformal Prediction for Risk-Controlled Medical Entity Extraction Across Clinical Domains",
            "url": "https://arxiv.org/html/2603.00924"
          },
          {
            "title": "Conformal Prediction for Text Infilling and Part-of-Speech Prediction",
            "url": "https://nejsds.nestat.org/journal/NEJSDS/article/10/file/pdf"
          },
          {
            "title": "Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction",
            "url": "https://arxiv.org/html/2601.16999"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          }
        ]
      },
      "Based on the search results, I found several relevant resources on conformal prediction applied to NLP sequence labeling tasks:\n\n## Key Findings\n\n**Survey Papers:**\nA comprehensive survey on Conformal Prediction for Natural Language Processing was published in 2024, and Angelopoulos and Bates (2023) published a comprehensive survey on conformal prediction.\n\n**Stephen Bates and Conformal Prediction Work:**\nAngelopoulos and Bates authored \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification,\" which describes conformal prediction as a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for model predictions with distribution-free validity guarantees.\n\n**Applications to Sequence Labeling:**\nResearch has introduced a framework for adapting sequence-labeling-based NER models to produce uncertainty-aware prediction sets that are guaranteed to contain the correct labeling with user-specified confidence, building on conformal prediction which offers finite-sample coverage guarantees.\n\nInductive conformal prediction algorithms have been proposed for text infilling and part-of-speech (POS) prediction, with ICP-enhanced algorithms for POS tagging based on BERT and BiLSTM.\n\n**Recent Extensions:**\nRecent work extends multi-label conformal prediction to identify confident components of long generations and demonstrates valid risk control on multiple diverse tasks.\n\nThese resources cover conformal prediction methods specifically designed for structured prediction tasks in NLP during the 2021-2024 period you specified."
    ],
    "durationSeconds": 7.1794667279999995
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T18:09:02.097Z_

<details><summary>↩ Tool result · `toolu_01HA2RHVhd2JTVf5gBmEt34P`</summary>

```text
Web search results for query: "Xiao Wang 2019 "Quantifying Uncertainties in Natural Language Processing Tasks" AAAI"

Links: [{"title":"Quantifying Uncertainties in Natural Language Processing Tasks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/4719"},{"title":"Quantifying uncertainties in natural language processing tasks | Proceedings of the Thirty-Third AAAI Conference on Artificial Intelligence and Thirty-First Innovative Applications of Artificial Intelligence Conference and Ninth AAAI Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v33i01.33017322"},{"title":"Quantifying Uncertainties in Natural Language Processing Tasks","url":"https://www.researchgate.net/publication/335380068_Quantifying_Uncertainties_in_Natural_Language_Processing_Tasks"},{"title":"Quantifying Uncertainties in Natural Language Processing ...","url":"https://ojs.aaai.org/index.php/AAAI/article/view/4719/4597"},{"title":"[1811.07253] Quantifying Uncertainties in Natural Language Processing Tasks","url":"https://arxiv.org/abs/1811.07253"},{"title":"Managing Uncertainty in NLP: Advanced Techniques and Approaches | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-88988-2_5"},{"title":"[1811.07253v1] Quantifying Uncertainties in Natural Language Processing Tasks","url":"https://arxiv.org/abs/1811.07253v1"},{"title":"CUE | Proceedings of the Thirty-Ninth Conference on Uncertainty in Artificial Intelligence","url":"https://dl.acm.org/doi/10.5555/3625834.3625952"},{"title":"Rethinking learning difficulty and uncertainty of samples with a target perturbation-aware bias-variance decomposition | International Journal of Machine Learning and Cybernetics | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s13042-025-02537-9"},{"title":"The Thirty-Third AAAI Conference on Artiﬁcial Intelligence (AAAI-19)","url":"https://www.aaai.org/ojs/index.php/AAAI/article/view/4719/4597"}]

I found the paper you're looking for. Here are the details:

**Paper Title:** Quantifying Uncertainties in Natural Language Processing Tasks, which proposes novel methods to study the benefits of characterizing model and data uncertainties for natural language processing (NLP) tasks

**Authors:** Yijun Xiao and Wangxuan Wang

**Conference:** Published in July 2019 in Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 33, No. 01, pp. 7322-7329)

**Abstract:** Reliable uncertainty quantification is a first step towards building explainable, transparent, and accountable artificial intelligent systems. Recent progress in Bayesian deep learning has made such quantification realizable.

**Key Findings:** With empirical experiments on sentiment analysis, named entity recognition, and language modeling using convolutional and recurrent neural network models, the paper shows that explicitly modeling uncertainties is not only necessary to measure output confidence levels, but also useful at enhancing model performances in various NLP tasks.

The paper is available at the AAAI proceedings website and also on arXiv (arXiv:1811.07253).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "0694d7c1-d1b8-4068-b17d-c5449969f897",
  "tool_use_result": {
    "query": "Xiao Wang 2019 \"Quantifying Uncertainties in Natural Language Processing Tasks\" AAAI",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VaWRpLCziwknVCNPMkucE1",
        "content": [
          {
            "title": "Quantifying Uncertainties in Natural Language Processing Tasks | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/4719"
          },
          {
            "title": "Quantifying uncertainties in natural language processing tasks | Proceedings of the Thirty-Third AAAI Conference on Artificial Intelligence and Thirty-First Innovative Applications of Artificial Intelligence Conference and Ninth AAAI Symposium on Educational Advances in Artificial Intelligence",
            "url": "https://dl.acm.org/doi/10.1609/aaai.v33i01.33017322"
          },
          {
            "title": "Quantifying Uncertainties in Natural Language Processing Tasks",
            "url": "https://www.researchgate.net/publication/335380068_Quantifying_Uncertainties_in_Natural_Language_Processing_Tasks"
          },
          {
            "title": "Quantifying Uncertainties in Natural Language Processing ...",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/4719/4597"
          },
          {
            "title": "[1811.07253] Quantifying Uncertainties in Natural Language Processing Tasks",
            "url": "https://arxiv.org/abs/1811.07253"
          },
          {
            "title": "Managing Uncertainty in NLP: Advanced Techniques and Approaches | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-88988-2_5"
          },
          {
            "title": "[1811.07253v1] Quantifying Uncertainties in Natural Language Processing Tasks",
            "url": "https://arxiv.org/abs/1811.07253v1"
          },
          {
            "title": "CUE | Proceedings of the Thirty-Ninth Conference on Uncertainty in Artificial Intelligence",
            "url": "https://dl.acm.org/doi/10.5555/3625834.3625952"
          },
          {
            "title": "Rethinking learning difficulty and uncertainty of samples with a target perturbation-aware bias-variance decomposition | International Journal of Machine Learning and Cybernetics | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s13042-025-02537-9"
          },
          {
            "title": "The Thirty-Third AAAI Conference on Artiﬁcial Intelligence (AAAI-19)",
            "url": "https://www.aaai.org/ojs/index.php/AAAI/article/view/4719/4597"
          }
        ]
      },
      "I found the paper you're looking for. Here are the details:\n\n**Paper Title:** Quantifying Uncertainties in Natural Language Processing Tasks, which proposes novel methods to study the benefits of characterizing model and data uncertainties for natural language processing (NLP) tasks\n\n**Authors:** Yijun Xiao and Wangxuan Wang\n\n**Conference:** Published in July 2019 in Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 33, No. 01, pp. 7322-7329)\n\n**Abstract:** Reliable uncertainty quantification is a first step towards building explainable, transparent, and accountable artificial intelligent systems. Recent progress in Bayesian deep learning has made such quantification realizable.\n\n**Key Findings:** With empirical experiments on sentiment analysis, named entity recognition, and language modeling using convolutional and recurrent neural network models, the paper shows that explicitly modeling uncertainties is not only necessary to measure output confidence levels, but also useful at enhancing model performances in various NLP tasks.\n\nThe paper is available at the AAAI proceedings website and also on arXiv (arXiv:1811.07253)."
    ],
    "durationSeconds": 7.265205067000003
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T18:09:02.262Z_

<details><summary>↩ Tool result · `toolu_01F27P5taqoJjJFA6Ew9L97g`</summary>

```text
Web search results for query: "Shelmanov 2021 NER uncertainty active learning ACL EMNLP EACL structured prediction"

Links: [{"title":"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.145/"},{"title":"Active Learning for Sequence Tagging with Deep Pre- ...","url":"https://aclanthology.org/2021.eacl-main.145.pdf"},{"title":"Re-weighting Tokens: A Simple and Effective Active ...","url":"https://aclanthology.org/2023.findings-emnlp.847.pdf"},{"title":"On the Calibration and Uncertainty of Neural Learning to ...","url":"https://aclanthology.org/2021.eacl-main.12.pdf"},{"title":"CUE | Proceedings of the Thirty-Ninth Conference on Uncertainty in Artificial Intelligence","url":"https://dl.acm.org/doi/10.5555/3625834.3625952"},{"title":"Second Workshop on Uncertainty-Aware NLP @EMNLP 2025","url":"https://uncertainlp.github.io/"},{"title":"Data-efficient Active Learning for Structured Prediction with ...","url":"https://aclanthology.org/2023.findings-emnlp.865.pdf"},{"title":"The Second Workshop on Uncertainty-Aware NLP @ EMNLP 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/second-workshop-uncertainty-aware-nlp-emnlp-2025-1"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2025/"},{"title":"ActiveEA: Active Learning for Neural Entity Alignment","url":"https://aclanthology.org/2021.emnlp-main.270.pdf"}]

I found the paper you're looking for! 

The paper is "Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates" by Shelmanov et al., published at EACL 2021 in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (pages 1698–1712).

The research conducts an extensive empirical study of various Bayesian uncertainty estimation methods and Monte Carlo dropout options for deep pre-trained models in the active learning framework and finds the best combinations for different types of models. The authors also demonstrate that a distilled version of a full-size Transformer can be substituted for instance acquisition during active learning, yielding better computational performance.

The paper appears to be available at: https://aclanthology.org/2021.eacl-main.145/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "85cd0ec1-5479-4828-bafe-7fbfc70d51d4",
  "tool_use_result": {
    "query": "Shelmanov 2021 NER uncertainty active learning ACL EMNLP EACL structured prediction",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EVg4WqDqfQ37utLzQz9zc6",
        "content": [
          {
            "title": "Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates - ACL Anthology",
            "url": "https://aclanthology.org/2021.eacl-main.145/"
          },
          {
            "title": "Active Learning for Sequence Tagging with Deep Pre- ...",
            "url": "https://aclanthology.org/2021.eacl-main.145.pdf"
          },
          {
            "title": "Re-weighting Tokens: A Simple and Effective Active ...",
            "url": "https://aclanthology.org/2023.findings-emnlp.847.pdf"
          },
          {
            "title": "On the Calibration and Uncertainty of Neural Learning to ...",
            "url": "https://aclanthology.org/2021.eacl-main.12.pdf"
          },
          {
            "title": "CUE | Proceedings of the Thirty-Ninth Conference on Uncertainty in Artificial Intelligence",
            "url": "https://dl.acm.org/doi/10.5555/3625834.3625952"
          },
          {
            "title": "Second Workshop on Uncertainty-Aware NLP @EMNLP 2025",
            "url": "https://uncertainlp.github.io/"
          },
          {
            "title": "Data-efficient Active Learning for Structured Prediction with ...",
            "url": "https://aclanthology.org/2023.findings-emnlp.865.pdf"
          },
          {
            "title": "The Second Workshop on Uncertainty-Aware NLP @ EMNLP 2025 | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/second-workshop-uncertainty-aware-nlp-emnlp-2025-1"
          },
          {
            "title": "The 2025 Conference on Empirical Methods in Natural Language Processing - ACL Anthology",
            "url": "https://aclanthology.org/events/emnlp-2025/"
          },
          {
            "title": "ActiveEA: Active Learning for Neural Entity Alignment",
            "url": "https://aclanthology.org/2021.emnlp-main.270.pdf"
          }
        ]
      },
      "I found the paper you're looking for! \n\nThe paper is \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\" by Shelmanov et al., published at EACL 2021 in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (pages 1698–1712).\n\nThe research conducts an extensive empirical study of various Bayesian uncertainty estimation methods and Monte Carlo dropout options for deep pre-trained models in the active learning framework and finds the best combinations for different types of models. The authors also demonstrate that a distilled version of a full-size Transformer can be substituted for instance acquisition during active learning, yielding better computational performance.\n\nThe paper appears to be available at: https://aclanthology.org/2021.eacl-main.145/"
    ],
    "durationSeconds": 5.890739579000001
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T18:09:03.173Z_

<details><summary>↩ Tool result · `toolu_013VEaRDy1L1dNS8gRdCo2Wn`</summary>

```text
Web search results for query: "He 2020 NER uncertainty estimation token-level ACL named entity recognition"

Links: [{"title":"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission - ACL Anthology","url":"https://aclanthology.org/2024.findings-naacl.180/"},{"title":"Uncertainty Estimation on Sequential Labeling via ... - People","url":"https://people.cs.vt.edu/~clu/Publication/2024/NAACL-Findings-2024-He.pdf"},{"title":"[2311.08726] Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission","url":"https://arxiv.org/abs/2311.08726"},{"title":"A Unified MRC Framework for Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.519/"},{"title":"Improving Low-Resource Named Entity Recognition using Joint Sentence and Token Labeling - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.523/"},{"title":"Are Data Augmentation Methods in Named Entity Recognition Applicable for Uncertainty Estimation?","url":"https://arxiv.org/html/2407.02062"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645414"},{"title":"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission","url":"https://arxiv.org/html/2311.08726"},{"title":"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.103/"},{"title":"Token-Level Metrics for Detecting Incorrect Gold Annotations in Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2025.findings-emnlp.827/"}]

Based on the search results, I found relevant information about uncertainty estimation in Named Entity Recognition at the token level. Here's what I discovered:

The most directly relevant work appears to be "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission" by He et al., published at NAACL 2024 (Findings). However, this is from 2024, not 2020 as mentioned in your query.

This work addresses how previous uncertainty estimation models often overlook two unique characteristics of NER: the connection between entities and wrong span cases in the entity extraction subtask, and proposes a Sequential Labeling Posterior Network (SLPN) to estimate uncertainty scores for extracted entities, considering uncertainty transmitted from other tokens.

The research centers on token-level sequential labeling in uncertainty estimation for NER, addressing the overlooked transmitted uncertainty from contextual tokens.

If you're looking for a specific 2020 ACL paper on NER with token-level uncertainty estimation, the search results don't show an exact match from that year with those specific characteristics. The results do include several ACL 2020 papers on NER (such as papers on unified MRC frameworks and low-resource NER), but they don't focus specifically on uncertainty estimation. 

Could you clarify if you're looking for a different author or paper, or would you like me to search for more specific information about uncertainty estimation in NER around 2020?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "ff0122ea-81b5-4ae9-a03a-3061f9499040",
  "tool_use_result": {
    "query": "He 2020 NER uncertainty estimation token-level ACL named entity recognition",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S6UhcovyNst6A8EyvWzywu",
        "content": [
          {
            "title": "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-naacl.180/"
          },
          {
            "title": "Uncertainty Estimation on Sequential Labeling via ... - People",
            "url": "https://people.cs.vt.edu/~clu/Publication/2024/NAACL-Findings-2024-He.pdf"
          },
          {
            "title": "[2311.08726] Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission",
            "url": "https://arxiv.org/abs/2311.08726"
          },
          {
            "title": "A Unified MRC Framework for Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.519/"
          },
          {
            "title": "Improving Low-Resource Named Entity Recognition using Joint Sentence and Token Labeling - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.523/"
          },
          {
            "title": "Are Data Augmentation Methods in Named Entity Recognition Applicable for Uncertainty Estimation?",
            "url": "https://arxiv.org/html/2407.02062"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024",
            "url": "https://dl.acm.org/doi/10.1145/3589334.3645414"
          },
          {
            "title": "Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission",
            "url": "https://arxiv.org/html/2311.08726"
          },
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2023.findings-acl.103/"
          },
          {
            "title": "Token-Level Metrics for Detecting Incorrect Gold Annotations in Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-emnlp.827/"
          }
        ]
      },
      "Based on the search results, I found relevant information about uncertainty estimation in Named Entity Recognition at the token level. Here's what I discovered:\n\nThe most directly relevant work appears to be \"Uncertainty Estimation on Sequential Labeling via Uncertainty Transmission\" by He et al., published at NAACL 2024 (Findings). However, this is from 2024, not 2020 as mentioned in your query.\n\nThis work addresses how previous uncertainty estimation models often overlook two unique characteristics of NER: the connection between entities and wrong span cases in the entity extraction subtask, and proposes a Sequential Labeling Posterior Network (SLPN) to estimate uncertainty scores for extracted entities, considering uncertainty transmitted from other tokens.\n\nThe research centers on token-level sequential labeling in uncertainty estimation for NER, addressing the overlooked transmitted uncertainty from contextual tokens.\n\nIf you're looking for a specific 2020 ACL paper on NER with token-level uncertainty estimation, the search results don't show an exact match from that year with those specific characteristics. The results do include several ACL 2020 papers on NER (such as papers on unified MRC frameworks and low-resource NER), but they don't focus specifically on uncertainty estimation. \n\nCould you clarify if you're looking for a different author or paper, or would you like me to search for more specific information about uncertainty estimation in NER around 2020?"
    ],
    "durationSeconds": 6.584053223999999
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T18:09:03.359Z_

<details><summary>↩ Tool result · `toolu_01DYMiR1k6WgnocbjVdU3ns9`</summary>

```text
Web search results for query: "Lakshminarayanan 2017 "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles" NeurIPS"

Links: [{"title":"[1612.01474] Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles","url":"https://arxiv.org/abs/1612.01474"},{"title":"Simple and scalable predictive uncertainty estimation using deep ensembles | Proceedings of the 31st International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3295222.3295387"},{"title":"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles","url":"https://arxiv.org/pdf/1612.01474"},{"title":"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Request PDF","url":"https://www.researchgate.net/publication/311430201_Simple_and_Scalable_Predictive_Uncertainty_Estimation_using_Deep_Ensembles"},{"title":"Simple and Scalable Predictive Uncertainty Estimation ...","url":"https://campusai.github.io/papers/uncertainty-estimation-deep-ensembles"},{"title":"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles","url":"https://papers.nips.cc/paper/7219-simple-and-scalable-predictive-uncertainty-estimation-using-deep-ensembles"},{"title":"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles","url":"https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html"},{"title":"Reviews: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles","url":"https://proceedings.neurips.cc/paper/2017/file/9ef2ed4b7fd2c810847ffa5fa85bce38-Reviews.html"},{"title":"[PDF] Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Simple-and-Scalable-Predictive-Uncertainty-using-Lakshminarayanan-Pritzel/802168a81571dde28f5ddb94d84677bc007afa7b"},{"title":"Paper review & code: Deep Ensembles (NIPS 2017) | by Alberto Arrigoni | Medium","url":"https://medium.com/@albertoarrigoni/paper-review-code-deep-ensembles-nips-2017-c5859070b8ce"}]

I found the paper you're looking for! Here are the search results:

The paper "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles" was authored by Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell in 2017, and it was published as part of Advances in Neural Information Processing Systems 30 (NIPS 2017).

**Key Details about the Paper:**

The paper addresses how deep neural networks are powerful black box predictors, but quantifying predictive uncertainty in them is a challenging problem. Bayesian neural networks, which learn a distribution over weights, are currently the state-of-the-art for estimating predictive uncertainty; however these require significant modifications to the training procedure and are computationally expensive.

**Main Contribution:**

The authors propose an alternative to Bayesian NNs that is simple to implement, readily parallelizable, requires very little hyperparameter tuning, and yields high quality predictive uncertainty estimates. Through a series of experiments on classification and regression benchmarks, they demonstrate that their method produces well-calibrated uncertainty estimates which are as good or better than approximate Bayesian NNs.

The paper is available through multiple sources including arXiv (arxiv.org/abs/1612.01474) and the official NeurIPS proceedings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "c3b7265d-eb79-46d0-8f10-7fc08f7647bc",
  "tool_use_result": {
    "query": "Lakshminarayanan 2017 \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\" NeurIPS",
    "results": [
      {
        "tool_use_id": "srvtoolu_018DgApMeCee8kTg3fg7P7Zy",
        "content": [
          {
            "title": "[1612.01474] Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles",
            "url": "https://arxiv.org/abs/1612.01474"
          },
          {
            "title": "Simple and scalable predictive uncertainty estimation using deep ensembles | Proceedings of the 31st International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3295222.3295387"
          },
          {
            "title": "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles",
            "url": "https://arxiv.org/pdf/1612.01474"
          },
          {
            "title": "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Request PDF",
            "url": "https://www.researchgate.net/publication/311430201_Simple_and_Scalable_Predictive_Uncertainty_Estimation_using_Deep_Ensembles"
          },
          {
            "title": "Simple and Scalable Predictive Uncertainty Estimation ...",
            "url": "https://campusai.github.io/papers/uncertainty-estimation-deep-ensembles"
          },
          {
            "title": "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles",
            "url": "https://papers.nips.cc/paper/7219-simple-and-scalable-predictive-uncertainty-estimation-using-deep-ensembles"
          },
          {
            "title": "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles",
            "url": "https://proceedings.neurips.cc/paper/2017/hash/9ef2ed4b7fd2c810847ffa5fa85bce38-Abstract.html"
          },
          {
            "title": "Reviews: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles",
            "url": "https://proceedings.neurips.cc/paper/2017/file/9ef2ed4b7fd2c810847ffa5fa85bce38-Reviews.html"
          },
          {
            "title": "[PDF] Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Simple-and-Scalable-Predictive-Uncertainty-using-Lakshminarayanan-Pritzel/802168a81571dde28f5ddb94d84677bc007afa7b"
          },
          {
            "title": "Paper review & code: Deep Ensembles (NIPS 2017) | by Alberto Arrigoni | Medium",
            "url": "https://medium.com/@albertoarrigoni/paper-review-code-deep-ensembles-nips-2017-c5859070b8ce"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\nThe paper \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\" was authored by Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell in 2017, and it was published as part of Advances in Neural Information Processing Systems 30 (NIPS 2017).\n\n**Key Details about the Paper:**\n\nThe paper addresses how deep neural networks are powerful black box predictors, but quantifying predictive uncertainty in them is a challenging problem. Bayesian neural networks, which learn a distribution over weights, are currently the state-of-the-art for estimating predictive uncertainty; however these require significant modifications to the training procedure and are computationally expensive.\n\n**Main Contribution:**\n\nThe authors propose an alternative to Bayesian NNs that is simple to implement, readily parallelizable, requires very little hyperparameter tuning, and yields high quality predictive uncertainty estimates. Through a series of experiments on classification and regression benchmarks, they demonstrate that their method produces well-calibrated uncertainty estimates which are as good or better than approximate Bayesian NNs.\n\nThe paper is available through multiple sources including arXiv (arxiv.org/abs/1612.01474) and the official NeurIPS proceedings."
    ],
    "durationSeconds": 6.2328610079999995
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:09:05.504Z_

<details><summary>↩ Tool result · `toolu_015FLa77e7Ef9tiiLkbCYJgq`</summary>

```text
Web search results for query: "Gal Ghahramani 2016 "Dropout as a Bayesian Approximation" ICML uncertainty deep learning"

Links: [{"title":"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning","url":"https://proceedings.mlr.press/v48/gal16.html"},{"title":"[1506.02142] Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning","url":"https://arxiv.org/abs/1506.02142"},{"title":"Dropout as a Bayesian approximation | Proceedings of the 33rd International Conference on International Conference on Machine Learning - Volume 48","url":"https://dl.acm.org/doi/10.5555/3045390.3045502"},{"title":"Dropout as a Bayesian Approximation: Insights and Applications Yarin Gal","url":"https://www.cs.ox.ac.uk/people/yarin.gal/website/PDFs/Dropout_as_a_Bayesian_approximation.pdf"},{"title":"[1506.02157] Dropout as a Bayesian Approximation: Appendix","url":"https://arxiv.org/abs/1506.02157"},{"title":"Dropout as a Bayesian Approximation: Representing Model","url":"https://abtinmu.com/assets/files/MCDropout-VIGP.pdf"},{"title":"Gal, Y. and Ghahramani, Z. (2016) Dropout as a Bayesian Approximation Representing Model Uncertainty in Deep Learning. Proceedings of the 33rd International Conference on Machine Learning, Vol. 48, 1050-1059. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3648830"},{"title":"Bayesian dropout - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S187705092200518X"},{"title":"BibSLEIGH — Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning","url":"https://bibtex.github.io/ICML-2016-GalG.html"},{"title":"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning","url":"https://www.researchgate.net/publication/277959098_Dropout_as_a_Bayesian_Approximation_Representing_Model_Uncertainty_in_Deep_Learning"}]

Based on the search results, here's information about the paper you're looking for:

Gal and Ghahramani published "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning" at the 33rd International Conference on Machine Learning (ICML) in 2016, pages 1050-1059.

**Paper Summary:**

The paper develops a new theoretical framework casting dropout training in deep neural networks as approximate Bayesian inference in deep Gaussian processes, providing tools to model uncertainty with dropout neural networks.

**Key Contributions:**

The work mitigates the problem of representing uncertainty in deep learning without sacrificing either computational complexity or test accuracy, and includes an extensive study of the properties of dropout's uncertainty.

The paper shows considerable improvement in predictive log-likelihood and RMSE compared to existing state-of-the-art methods, and includes applications to deep reinforcement learning.

**Availability:**

The paper is available through multiple sources:
- Official proceedings: https://proceedings.mlr.press/v48/gal16.html
- arXiv: https://arxiv.org/abs/1506.02142
- ACM Digital Library: https://dl.acm.org/doi/10.5555/3045390.3045502

This is a highly influential paper in the field of uncertainty quantification in deep learning, introducing the concept of Monte Carlo Dropout as a practical method for obtaining uncertainty estimates from neural networks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "a61dfd57-d7d6-41fd-9540-8928ced9e8a8",
  "tool_use_result": {
    "query": "Gal Ghahramani 2016 \"Dropout as a Bayesian Approximation\" ICML uncertainty deep learning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y6mGckGtwyQJpkEGXYoiUY",
        "content": [
          {
            "title": "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning",
            "url": "https://proceedings.mlr.press/v48/gal16.html"
          },
          {
            "title": "[1506.02142] Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning",
            "url": "https://arxiv.org/abs/1506.02142"
          },
          {
            "title": "Dropout as a Bayesian approximation | Proceedings of the 33rd International Conference on International Conference on Machine Learning - Volume 48",
            "url": "https://dl.acm.org/doi/10.5555/3045390.3045502"
          },
          {
            "title": "Dropout as a Bayesian Approximation: Insights and Applications Yarin Gal",
            "url": "https://www.cs.ox.ac.uk/people/yarin.gal/website/PDFs/Dropout_as_a_Bayesian_approximation.pdf"
          },
          {
            "title": "[1506.02157] Dropout as a Bayesian Approximation: Appendix",
            "url": "https://arxiv.org/abs/1506.02157"
          },
          {
            "title": "Dropout as a Bayesian Approximation: Representing Model",
            "url": "https://abtinmu.com/assets/files/MCDropout-VIGP.pdf"
          },
          {
            "title": "Gal, Y. and Ghahramani, Z. (2016) Dropout as a Bayesian Approximation Representing Model Uncertainty in Deep Learning. Proceedings of the 33rd International Conference on Machine Learning, Vol. 48, 1050-1059. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3648830"
          },
          {
            "title": "Bayesian dropout - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S187705092200518X"
          },
          {
            "title": "BibSLEIGH — Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning",
            "url": "https://bibtex.github.io/ICML-2016-GalG.html"
          },
          {
            "title": "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning",
            "url": "https://www.researchgate.net/publication/277959098_Dropout_as_a_Bayesian_Approximation_Representing_Model_Uncertainty_in_Deep_Learning"
          }
        ]
      },
      "Based on the search results, here's information about the paper you're looking for:\n\nGal and Ghahramani published \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\" at the 33rd International Conference on Machine Learning (ICML) in 2016, pages 1050-1059.\n\n**Paper Summary:**\n\nThe paper develops a new theoretical framework casting dropout training in deep neural networks as approximate Bayesian inference in deep Gaussian processes, providing tools to model uncertainty with dropout neural networks.\n\n**Key Contributions:**\n\nThe work mitigates the problem of representing uncertainty in deep learning without sacrificing either computational complexity or test accuracy, and includes an extensive study of the properties of dropout's uncertainty.\n\nThe paper shows considerable improvement in predictive log-likelihood and RMSE compared to existing state-of-the-art methods, and includes applications to deep reinforcement learning.\n\n**Availability:**\n\nThe paper is available through multiple sources:\n- Official proceedings: https://proceedings.mlr.press/v48/gal16.html\n- arXiv: https://arxiv.org/abs/1506.02142\n- ACM Digital Library: https://dl.acm.org/doi/10.5555/3045390.3045502\n\nThis is a highly influential paper in the field of uncertainty quantification in deep learning, introducing the concept of Monte Carlo Dropout as a practical method for obtaining uncertainty estimates from neural networks."
    ],
    "durationSeconds": 7.316898732999999
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T18:09:06.193Z_

<details><summary>↩ Tool result · `toolu_01Ba6F4ACnpA9ujD4RLtxN69`</summary>

```text
Web search results for query: "Fomicheva 2020 "Unsupervised Quality Estimation for Neural Machine Translation" MC dropout ensemble uncertainty NLP"

Links: [{"title":"Unsupervised Quality Estimation for Neural Machine Translation","url":"https://aclanthology.org/2020.tacl-1.35.pdf"},{"title":"[2005.10608] Unsupervised Quality Estimation for Neural Machine Translation","url":"https://arxiv.org/abs/2005.10608"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2020.tacl-1.35/"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00330/96475/Unsupervised-Quality-Estimation-for-Neural-Machine"},{"title":"[PDF] Unsupervised Quality Estimation for Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Unsupervised-Quality-Estimation-for-Neural-Machine-Fomicheva-Sun/8ae3421420ec57d551ef2f524b48dcc78f9337fc"},{"title":"fairseq/examples/unsupervised_quality_estimation/README.md at main · facebookresearch/fairseq","url":"https://github.com/facebookresearch/fairseq/blob/main/examples/unsupervised_quality_estimation/README.md"},{"title":"(PDF) Unsupervised Quality Estimation for Neural Machine Translation","url":"https://www.researchgate.net/publication/344763694_Unsupervised_Quality_Estimation_for_Neural_Machine_Translation"},{"title":"Unsupervised Quality Estimation for Neural Machine Translation - Tilburg University Research Portal","url":"https://research.tilburguniversity.edu/en/publications/unsupervised-quality-estimation-for-neural-machine-translation-2"},{"title":"Uncertainty Quantification Enhanced Quality Estimation for ...","url":"https://aclanthology.org/2021.findings-emnlp.401.pdf"},{"title":"Unsupervised quality estimation for neural machine translation - White Rose Research Online","url":"https://eprints.whiterose.ac.uk/161219/"}]

I found relevant information about the Fomicheva et al. 2020 paper. Here's what the search results show:

## Paper Overview

The paper "Unsupervised Quality Estimation for Neural Machine Translation" was published in 2020 in the Transactions of the Association for Computational Linguistics, volume 8, pages 539-555, with authors including Marina Fomicheva, Shuo Sun, Lisa Yankovskaya, Frédéric Blain, Francisco Guzmán, Mark Fishel, Nikolaos Aletras, Vishrav Chaudhary, and Lucia Specia.

## Main Contribution

The paper presents an unsupervised approach to Quality Estimation (QE) where no training or access to additional resources beyond the MT system itself is required, and it explores useful information that can be extracted from the MT system as a by-product of translation.

## Uncertainty Quantification Methods

The paper addresses uncertainty quantification in neural networks using a Bayesian framework, with various approximations developed to avoid high training costs, such as Monte Carlo Dropout (Gal and Ghahramani, 2016) or model ensembling.

## Results

By utilizing methods for uncertainty quantification, the approach achieves very good correlation with human judgments of quality, rivaling state-of-the-art supervised QE models.

The paper's code and implementation details are available in the fairseq toolkit, with dropout_n set to 30 in the experiments reported in the paper.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "95af6623-413a-49f0-b4b6-85203daf9eee",
  "tool_use_result": {
    "query": "Fomicheva 2020 \"Unsupervised Quality Estimation for Neural Machine Translation\" MC dropout ensemble uncertainty NLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_017B32CzFuEWYXuv8DqeB7Sg",
        "content": [
          {
            "title": "Unsupervised Quality Estimation for Neural Machine Translation",
            "url": "https://aclanthology.org/2020.tacl-1.35.pdf"
          },
          {
            "title": "[2005.10608] Unsupervised Quality Estimation for Neural Machine Translation",
            "url": "https://arxiv.org/abs/2005.10608"
          },
          {
            "title": "Unsupervised Quality Estimation for Neural Machine Translation - ACL Anthology",
            "url": "https://aclanthology.org/2020.tacl-1.35/"
          },
          {
            "title": "Unsupervised Quality Estimation for Neural Machine Translation | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00330/96475/Unsupervised-Quality-Estimation-for-Neural-Machine"
          },
          {
            "title": "[PDF] Unsupervised Quality Estimation for Neural Machine Translation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Unsupervised-Quality-Estimation-for-Neural-Machine-Fomicheva-Sun/8ae3421420ec57d551ef2f524b48dcc78f9337fc"
          },
          {
            "title": "fairseq/examples/unsupervised_quality_estimation/README.md at main · facebookresearch/fairseq",
            "url": "https://github.com/facebookresearch/fairseq/blob/main/examples/unsupervised_quality_estimation/README.md"
          },
          {
            "title": "(PDF) Unsupervised Quality Estimation for Neural Machine Translation",
            "url": "https://www.researchgate.net/publication/344763694_Unsupervised_Quality_Estimation_for_Neural_Machine_Translation"
          },
          {
            "title": "Unsupervised Quality Estimation for Neural Machine Translation - Tilburg University Research Portal",
            "url": "https://research.tilburguniversity.edu/en/publications/unsupervised-quality-estimation-for-neural-machine-translation-2"
          },
          {
            "title": "Uncertainty Quantification Enhanced Quality Estimation for ...",
            "url": "https://aclanthology.org/2021.findings-emnlp.401.pdf"
          },
          {
            "title": "Unsupervised quality estimation for neural machine translation - White Rose Research Online",
            "url": "https://eprints.whiterose.ac.uk/161219/"
          }
        ]
      },
      "I found relevant information about the Fomicheva et al. 2020 paper. Here's what the search results show:\n\n## Paper Overview\n\nThe paper \"Unsupervised Quality Estimation for Neural Machine Translation\" was published in 2020 in the Transactions of the Association for Computational Linguistics, volume 8, pages 539-555, with authors including Marina Fomicheva, Shuo Sun, Lisa Yankovskaya, Frédéric Blain, Francisco Guzmán, Mark Fishel, Nikolaos Aletras, Vishrav Chaudhary, and Lucia Specia.\n\n## Main Contribution\n\nThe paper presents an unsupervised approach to Quality Estimation (QE) where no training or access to additional resources beyond the MT system itself is required, and it explores useful information that can be extracted from the MT system as a by-product of translation.\n\n## Uncertainty Quantification Methods\n\nThe paper addresses uncertainty quantification in neural networks using a Bayesian framework, with various approximations developed to avoid high training costs, such as Monte Carlo Dropout (Gal and Ghahramani, 2016) or model ensembling.\n\n## Results\n\nBy utilizing methods for uncertainty quantification, the approach achieves very good correlation with human judgments of quality, rivaling state-of-the-art supervised QE models.\n\nThe paper's code and implementation details are available in the fairseq toolkit, with dropout_n set to 30 in the experiments reported in the paper."
    ],
    "durationSeconds": 7.3158409639999995
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have information for most papers. Let me get more details on some papers I need to clarify:

1. **Fisch et al. 2021** - ICML 2021 (not NeurIPS). Authors: Adam Fisch, Tal Schuster, Tommi Jaakkola, Regina Barzilay. URL: https://arxiv.org/abs/2102.08898

2. **Angelopoulos et al. 2021** - ICLR 2021. Authors: Anastasios N. Angelopoulos, Stephen Bates, Jitendra Malik, Michael I. 

Jordan. URL: https://arxiv.org/abs/2009.14193

3. **Conformal prediction for NLP** - I found a survey paper by Giovannotti 2024 in TACL, but I should look for a more specific conformal prediction paper focused on NLP applications.

4. **Xiao & Wang 2019** - AAAI 2019. Authors: Yijun Xiao, William Yang Wang. URL: https://arxiv.org/abs/1811.07253. DOI: 10.1609/aaai.v33i01.33017322

5. **Sh elmanov et al. 2021** - EACL 2021 paper on active learning for sequence tagging using deep pre-trained models with Bayesian uncertainty. URL: https://aclanthology.org/2021.eacl-main.145/

6. **He et al. for NER uncertainty** - I couldn't locate the 2020 paper directly, but found their 2024 NAACL Findings work on uncertainty estimation for sequential labeling. I should search for token-level uncertainty papers or E-NER instead.

7. **Lakshminarayanan et al. 2017** - NeurIPS 2017 paper by Balaji Lakshminarayanan, Alexander Pritzel, and Charles Blundell. URL: https://arxiv.org/

abs/1612.01474

8. **Gal & Ghahramani 2016** - ICML 2016 work by Yarin Gal and Zoubin Ghahramani. URL: https://arxiv.org/abs/1506.02142

9. **Fomicheva et al. 2020** - TACL 2020 paper with a large author team on quality estimation. URL: https://arxiv.org/abs/2005.10608. DOI: 10.1162/tacl_a_00330

Still looking for a conformal prediction paper for NLP.

I also need to track down a better token-level uncertainty approach for NER tasks, and I should grab the complete author lists for both the Angelopoulos and Shelmanov papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "8bce2030-0187-488a-bea4-04d0a26f8ad7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZhpW2gtYhhtAF7mXbQWTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8976,
      "cache_read_input_tokens": 31556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8976
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

需要补充搜索几篇论文的详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "ff04e1c2-7a4a-4697-9404-e4994dab5224",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZhpW2gtYhhtAF7mXbQWTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8976,
      "cache_read_input_tokens": 31556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8976
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XGZP34irAEW9ghZbQ8Gdnz`</summary>

```json
{
  "query": "Angelopoulos Bates Malik Jordan 2021 \"Uncertainty Sets for Image Classifiers\" ICLR authors full list RAPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "62251cdd-afeb-4266-b872-caea02c865c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZhpW2gtYhhtAF7mXbQWTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8976,
      "cache_read_input_tokens": 31556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8976
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NTTUq434Ut16UAba2fzjUy`</summary>

```json
{
  "query": "Shelmanov et al 2021 \"Active Learning for Sequence Tagging\" EACL authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "6bf1694b-21e4-4884-80fb-74ff3850a15f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZhpW2gtYhhtAF7mXbQWTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8976,
      "cache_read_input_tokens": 31556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8976
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011MEA8fbZvMKPkYUVhWjjcq`</summary>

```json
{
  "query": "Giovannotti 2024 \"Conformal Prediction for Natural Language Processing: A Survey\" TACL authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "6bb823b1-7944-4be6-abec-85874af5e284",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZhpW2gtYhhtAF7mXbQWTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8976,
      "cache_read_input_tokens": 31556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8976
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A6Yg69BHRi4AU5EjywUfKJ`</summary>

```json
{
  "query": "E-NER evidential deep learning named entity recognition 2023 uncertainty token-level NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "20888901-2869-4402-a16c-0e7a15334e49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ZhpW2gtYhhtAF7mXbQWTi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8976,
      "cache_read_input_tokens": 31556,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8976
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

_source line 36 · 2026-05-14T18:09:27.694Z_

<details><summary>↩ Tool result · `toolu_01NTTUq434Ut16UAba2fzjUy`</summary>

```text
Web search results for query: "Shelmanov et al 2021 "Active Learning for Sequence Tagging" EACL authors full list"

Links: [{"title":"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.145/"},{"title":"[2101.08133] Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates","url":"https://arxiv.org/abs/2101.08133"},{"title":"Active Learning for Sequence Tagging with Deep Pre- ...","url":"https://aclanthology.org/2021.eacl-main.145.pdf"},{"title":"Main Conference Accepted Papers - EACL 2021","url":"https://2021.eacl.org/program/accepted/"},{"title":"[2101.08133v2] Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates","url":"https://arxiv.org/abs/2101.08133v2"},{"title":"(PDF) Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates","url":"https://www.researchgate.net/publication/355430342_Active_Learning_for_Sequence_Tagging_with_Deep_Pre-trained_Models_and_Bayesian_Uncertainty_Estimates"},{"title":"Have LLMs Made Active Learning Obsolete? Surveying the NLP Community","url":"https://arxiv.org/html/2503.09701v1"},{"title":"Investigating Multi-source Active Learning for Natural ...","url":"https://aclanthology.org/2023.eacl-main.160.pdf"},{"title":"Aclanthology","url":"https://www.aclweb.org/anthology/2021.eacl-main.145.pdf"},{"title":"Paper page - Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates","url":"https://huggingface.co/papers/2101.08133"}]

Based on the search results, here is the complete list of authors for the paper "Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates" (Shelmanov et al., EACL 2021):

Artem Shelmanov, Dmitri Puzyrev, Lyubov Kupriyanova, Denis Belyakov, Daniil Larionov, Nikita Khromov, Olga Kozlova, Ekaterina Artemova, Dmitry V. Dylov, and Alexander Panchenko.

The paper was published in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume, pages 1698–1712, Online.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "1b79f6d6-8ba5-4aa2-b8cf-ac614dcc96d7",
  "tool_use_result": {
    "query": "Shelmanov et al 2021 \"Active Learning for Sequence Tagging\" EACL authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RWUUhJmRKqHyXbty8Ry5Z9",
        "content": [
          {
            "title": "Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates - ACL Anthology",
            "url": "https://aclanthology.org/2021.eacl-main.145/"
          },
          {
            "title": "[2101.08133] Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates",
            "url": "https://arxiv.org/abs/2101.08133"
          },
          {
            "title": "Active Learning for Sequence Tagging with Deep Pre- ...",
            "url": "https://aclanthology.org/2021.eacl-main.145.pdf"
          },
          {
            "title": "Main Conference Accepted Papers - EACL 2021",
            "url": "https://2021.eacl.org/program/accepted/"
          },
          {
            "title": "[2101.08133v2] Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates",
            "url": "https://arxiv.org/abs/2101.08133v2"
          },
          {
            "title": "(PDF) Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates",
            "url": "https://www.researchgate.net/publication/355430342_Active_Learning_for_Sequence_Tagging_with_Deep_Pre-trained_Models_and_Bayesian_Uncertainty_Estimates"
          },
          {
            "title": "Have LLMs Made Active Learning Obsolete? Surveying the NLP Community",
            "url": "https://arxiv.org/html/2503.09701v1"
          },
          {
            "title": "Investigating Multi-source Active Learning for Natural ...",
            "url": "https://aclanthology.org/2023.eacl-main.160.pdf"
          },
          {
            "title": "Aclanthology",
            "url": "https://www.aclweb.org/anthology/2021.eacl-main.145.pdf"
          },
          {
            "title": "Paper page - Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates",
            "url": "https://huggingface.co/papers/2101.08133"
          }
        ]
      },
      "Based on the search results, here is the complete list of authors for the paper \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\" (Shelmanov et al., EACL 2021):\n\nArtem Shelmanov, Dmitri Puzyrev, Lyubov Kupriyanova, Denis Belyakov, Daniil Larionov, Nikita Khromov, Olga Kozlova, Ekaterina Artemova, Dmitry V. Dylov, and Alexander Panchenko.\n\nThe paper was published in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume, pages 1698–1712, Online."
    ],
    "durationSeconds": 4.786514321999995
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T18:09:28.358Z_

<details><summary>↩ Tool result · `toolu_01XGZP34irAEW9ghZbQ8Gdnz`</summary>

```text
Web search results for query: "Angelopoulos Bates Malik Jordan 2021 "Uncertainty Sets for Image Classifiers" ICLR authors full list RAPS"

Links: [{"title":"UNCERTAINTY SETS FOR IMAGE CLASSIFIERS USING CONFORMAL PREDICTION","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-classification.pdf"},{"title":"μ & σ - Conformal classification","url":"https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/conformal-classification/"},{"title":"[2009.14193] Uncertainty Sets for Image Classifiers using Conformal Prediction","url":"https://arxiv.org/abs/2009.14193"},{"title":"Publications - Anastasios Angelopoulos","url":"https://people.eecs.berkeley.edu/~angelopoulos/publications/"},{"title":"Uncertainty Sets for Image Classifiers using Conformal Prediction | OpenReview","url":"https://openreview.net/forum?id=eNdiU_DbM9"},{"title":"UNCERTAINTY SETS FOR IMAGE CLASSIFIERS USING ...","url":"https://openreview.net/pdf?id=eNdiU_DbM9"},{"title":"Uncertainty Sets for Image Classifiers using Conformal Prediction - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200914193A/abstract"},{"title":"Theoretical Description Classification : contents — MAPIE 1.3.0 documentation","url":"https://mapie.readthedocs.io/en/latest/theoretical_description_classification.html"},{"title":"Distribution-free, Risk-controlling Prediction Sets | Journal of the ACM","url":"https://dl.acm.org/doi/abs/10.1145/3478535"},{"title":"GitHub - AlaaLab/deep-learning-uncertainty: Literature survey, paper reviews, experimental setups and a collection of implementations for baselines methods for predictive uncertainty estimation in deep learning models.","url":"https://github.com/AlaaLab/deep-learning-uncertainty"}]

Based on the search results, I found the information about the paper "Uncertainty Sets for Image Classifiers using Conformal Prediction":

## Full Author List

The authors are: Anastasios Angelopoulos, Stephen Bates, Jitendra Malik, and Michael I. Jordan.

## Publication Details

This was an ICLR 2021 Spotlight paper. The paper introduces an algorithm called RAPS, which modifies the classifier to output a predictive set containing the true label with a user-specified probability, such as 90%.

## Key Contribution

The algorithm is simple and fast like Platt scaling, but provides a formal finite-sample coverage guarantee for every model and dataset, and modifies an existing conformal prediction algorithm to give more stable predictive sets by regularizing the small scores of unlikely classes after Platt scaling.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "4f28a922-aad4-463a-bb4e-232b4362281c",
  "tool_use_result": {
    "query": "Angelopoulos Bates Malik Jordan 2021 \"Uncertainty Sets for Image Classifiers\" ICLR authors full list RAPS",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SJchVLzk7uFSFeEoJQRAmi",
        "content": [
          {
            "title": "UNCERTAINTY SETS FOR IMAGE CLASSIFIERS USING CONFORMAL PREDICTION",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/publications/downloads/conformal-classification.pdf"
          },
          {
            "title": "μ & σ - Conformal classification",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/conformal-classification/"
          },
          {
            "title": "[2009.14193] Uncertainty Sets for Image Classifiers using Conformal Prediction",
            "url": "https://arxiv.org/abs/2009.14193"
          },
          {
            "title": "Publications - Anastasios Angelopoulos",
            "url": "https://people.eecs.berkeley.edu/~angelopoulos/publications/"
          },
          {
            "title": "Uncertainty Sets for Image Classifiers using Conformal Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=eNdiU_DbM9"
          },
          {
            "title": "UNCERTAINTY SETS FOR IMAGE CLASSIFIERS USING ...",
            "url": "https://openreview.net/pdf?id=eNdiU_DbM9"
          },
          {
            "title": "Uncertainty Sets for Image Classifiers using Conformal Prediction - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv200914193A/abstract"
          },
          {
            "title": "Theoretical Description Classification : contents — MAPIE 1.3.0 documentation",
            "url": "https://mapie.readthedocs.io/en/latest/theoretical_description_classification.html"
          },
          {
            "title": "Distribution-free, Risk-controlling Prediction Sets | Journal of the ACM",
            "url": "https://dl.acm.org/doi/abs/10.1145/3478535"
          },
          {
            "title": "GitHub - AlaaLab/deep-learning-uncertainty: Literature survey, paper reviews, experimental setups and a collection of implementations for baselines methods for predictive uncertainty estimation in deep learning models.",
            "url": "https://github.com/AlaaLab/deep-learning-uncertainty"
          }
        ]
      },
      "Based on the search results, I found the information about the paper \"Uncertainty Sets for Image Classifiers using Conformal Prediction\":\n\n## Full Author List\n\nThe authors are: Anastasios Angelopoulos, Stephen Bates, Jitendra Malik, and Michael I. Jordan.\n\n## Publication Details\n\nThis was an ICLR 2021 Spotlight paper. The paper introduces an algorithm called RAPS, which modifies the classifier to output a predictive set containing the true label with a user-specified probability, such as 90%.\n\n## Key Contribution\n\nThe algorithm is simple and fast like Platt scaling, but provides a formal finite-sample coverage guarantee for every model and dataset, and modifies an existing conformal prediction algorithm to give more stable predictive sets by regularizing the small scores of unlikely classes after Platt scaling."
    ],
    "durationSeconds": 5.920751948999998
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T18:09:29.087Z_

<details><summary>↩ Tool result · `toolu_011MEA8fbZvMKPkYUVhWjjcq`</summary>

```text
Web search results for query: "Giovannotti 2024 "Conformal Prediction for Natural Language Processing: A Survey" TACL authors"

Links: [{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://aclanthology.org/2024.tacl-1.82.pdf"},{"title":"Conformal Prediction for Natural Language Processing: A Survey - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.82/"},{"title":"Conformalizing Machine Translation Evaluation | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00711/125277/Conformalizing-Machine-Translation-Evaluation"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/html/2405.01976v1"},{"title":"[2405.01976] Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/abs/2405.01976"},{"title":"Aclanthology","url":"https://aclanthology.org/2024.tacl-1.82.bib"},{"title":"[2405.01976v1] Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/abs/2405.01976v1"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Request PDF","url":"https://www.researchgate.net/publication/386030579_Conformal_Prediction_for_Natural_Language_Processing_A_Survey"},{"title":"Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"}]

Based on the search results, I found information about the paper "Conformal Prediction for Natural Language Processing: A Survey" published in TACL 2024.

The authors are Margarida Campos, António Farinhas, Chrysoula Zerva, Mário A. T. Figueiredo, and André F. T. Martins, published in Transactions of the Association for Computational Linguistics 2024, Volume 12, pages 1497–1516.

Regarding Giovannotti: The search results mention Giovannotti as a researcher who has applied conformal prediction to NLP tasks in prior work (2022-2023), but Giovannotti is not listed as one of the authors of this 2024 TACL survey paper. Giovannotti (2023) applied CP to referenceless MT evaluation (quality estimation), specifically using conformal predictive distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "4ac8478d-e302-46d5-a6f2-9b72d1e38f47",
  "tool_use_result": {
    "query": "Giovannotti 2024 \"Conformal Prediction for Natural Language Processing: A Survey\" TACL authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NuPzyKAiad1ymrhcoG7qZU",
        "content": [
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://aclanthology.org/2024.tacl-1.82.pdf"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey - ACL Anthology",
            "url": "https://aclanthology.org/2024.tacl-1.82/"
          },
          {
            "title": "Conformalizing Machine Translation Evaluation | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00711/125277/Conformalizing-Machine-Translation-Evaluation"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/html/2405.01976v1"
          },
          {
            "title": "[2405.01976] Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/abs/2405.01976"
          },
          {
            "title": "Aclanthology",
            "url": "https://aclanthology.org/2024.tacl-1.82.bib"
          },
          {
            "title": "[2405.01976v1] Conformal Prediction for Natural Language Processing: A Survey",
            "url": "https://arxiv.org/abs/2405.01976v1"
          },
          {
            "title": "Conformal Prediction for Natural Language Processing: A Survey | Request PDF",
            "url": "https://www.researchgate.net/publication/386030579_Conformal_Prediction_for_Natural_Language_Processing_A_Survey"
          },
          {
            "title": "Published as a conference paper at ICLR 2024 CONFORMAL LANGUAGE MODELING",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/31421b112e5f7faf4fc577b74e45dab2-Paper-Conference.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the paper \"Conformal Prediction for Natural Language Processing: A Survey\" published in TACL 2024.\n\nThe authors are Margarida Campos, António Farinhas, Chrysoula Zerva, Mário A. T. Figueiredo, and André F. T. Martins, published in Transactions of the Association for Computational Linguistics 2024, Volume 12, pages 1497–1516.\n\nRegarding Giovannotti: The search results mention Giovannotti as a researcher who has applied conformal prediction to NLP tasks in prior work (2022-2023), but Giovannotti is not listed as one of the authors of this 2024 TACL survey paper. Giovannotti (2023) applied CP to referenceless MT evaluation (quality estimation), specifically using conformal predictive distributions."
    ],
    "durationSeconds": 5.226207964999994
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T18:09:33.083Z_

<details><summary>↩ Tool result · `toolu_01A6Yg69BHRi4AU5EjywUfKJ`</summary>

```text
Web search results for query: "E-NER evidential deep learning named entity recognition 2023 uncertainty token-level NER"

Links: [{"title":"[2305.17854] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition","url":"https://arxiv.org/abs/2305.17854"},{"title":"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.103/"},{"title":"GitHub - zhzhengit/ENER: E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition","url":"https://github.com/zhzhengit/ENER"},{"title":"COMPREHENSIVE OVERVIEW OF NAMED ENTITY RECOGNITION:","url":"https://arxiv.org/pdf/2309.14084"},{"title":"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/372915667_E-NER_Evidential_Deep_Learning_for_Trustworthy_Named_Entity_Recognition"},{"title":"[Quick Review] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition","url":"https://liner.com/review/ener-evidential-deep-learning-for-trustworthy-named-entity-recognition"},{"title":"E-NER: Evidential Deep Learning for Trustworthy Named ...","url":"https://aclanthology.org/2023.findings-acl.103.pdf"},{"title":"Basic architecture of E-NER with different NER paradigms. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Basic-architecture-of-E-NER-with-different-NER-paradigms_fig1_371136201"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645414"},{"title":"Comprehensive Overview of Named Entity Recognition: Models, Domain-Specific Applications and Challenges","url":"https://arxiv.org/html/2309.14084"}]

I found comprehensive information about E-NER. Here are the search results:

## E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition

E-NER is a trustworthy NER framework that introduces two uncertainty-guided loss terms to conventional EDL, along with uncertainty-guided training strategies. The paper was published by Zhang et al. in 2023 in the Findings of the Association for Computational Linguistics: ACL 2023.

### Problem Statement

Most NER systems focus on improving model performance while ignoring the need to quantify model uncertainty, which is critical to the reliability of NER systems in open environments. Directly applying EDL to NER applications faces two challenges: the problems of sparse entities and OOV/OOD entities in NER tasks.

### Key Contributions

E-NER incorporates an uncertainty-guided importance weighted loss to mitigate sparse entities and an uncertainty mass optimization term to explicitly increase uncertainty for mispredicted and unknown entities, thereby improving OOV/OOD entity discrimination.

### Performance

E-NER can be applied to multiple NER paradigms to obtain accurate uncertainty estimation, and achieves better OOV/OOD detection performance and better generalization ability on OOV entities compared to state-of-the-art baselines.

The consistent improvement across different NER paradigms (sequence labeling, span-based, and Seq2Seq) demonstrates the generalizability and robustness of E-NER's approach, offering a broadly applicable solution for trustworthy NER in open environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "dadfc642-d9ce-4bdc-9d54-eed576222f84",
  "tool_use_result": {
    "query": "E-NER evidential deep learning named entity recognition 2023 uncertainty token-level NER",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EUzxAjASiqzFuobaCLiWnq",
        "content": [
          {
            "title": "[2305.17854] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition",
            "url": "https://arxiv.org/abs/2305.17854"
          },
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2023.findings-acl.103/"
          },
          {
            "title": "GitHub - zhzhengit/ENER: E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition",
            "url": "https://github.com/zhzhengit/ENER"
          },
          {
            "title": "COMPREHENSIVE OVERVIEW OF NAMED ENTITY RECOGNITION:",
            "url": "https://arxiv.org/pdf/2309.14084"
          },
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition | Request PDF",
            "url": "https://www.researchgate.net/publication/372915667_E-NER_Evidential_Deep_Learning_for_Trustworthy_Named_Entity_Recognition"
          },
          {
            "title": "[Quick Review] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition",
            "url": "https://liner.com/review/ener-evidential-deep-learning-for-trustworthy-named-entity-recognition"
          },
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named ...",
            "url": "https://aclanthology.org/2023.findings-acl.103.pdf"
          },
          {
            "title": "Basic architecture of E-NER with different NER paradigms. | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Basic-architecture-of-E-NER-with-different-NER-paradigms_fig1_371136201"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024",
            "url": "https://dl.acm.org/doi/10.1145/3589334.3645414"
          },
          {
            "title": "Comprehensive Overview of Named Entity Recognition: Models, Domain-Specific Applications and Challenges",
            "url": "https://arxiv.org/html/2309.14084"
          }
        ]
      },
      "I found comprehensive information about E-NER. Here are the search results:\n\n## E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\n\nE-NER is a trustworthy NER framework that introduces two uncertainty-guided loss terms to conventional EDL, along with uncertainty-guided training strategies. The paper was published by Zhang et al. in 2023 in the Findings of the Association for Computational Linguistics: ACL 2023.\n\n### Problem Statement\n\nMost NER systems focus on improving model performance while ignoring the need to quantify model uncertainty, which is critical to the reliability of NER systems in open environments. Directly applying EDL to NER applications faces two challenges: the problems of sparse entities and OOV/OOD entities in NER tasks.\n\n### Key Contributions\n\nE-NER incorporates an uncertainty-guided importance weighted loss to mitigate sparse entities and an uncertainty mass optimization term to explicitly increase uncertainty for mispredicted and unknown entities, thereby improving OOV/OOD entity discrimination.\n\n### Performance\n\nE-NER can be applied to multiple NER paradigms to obtain accurate uncertainty estimation, and achieves better OOV/OOD detection performance and better generalization ability on OOV entities compared to state-of-the-art baselines.\n\nThe consistent improvement across different NER paradigms (sequence labeling, span-based, and Seq2Seq) demonstrates the generalizability and robustness of E-NER's approach, offering a broadly applicable solution for trustworthy NER in open environments."
    ],
    "durationSeconds": 8.874780166000004
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I have most of the information. Let me also search for:
1. The Xiao & Wang 2019 paper authors - the search mentioned "Yijun Xiao and Wangxuan Wang" but I need to verify this. Let me check if it's "William Yang Wang" instead.
2. E-NER authors full list
3. For the conformal prediction NLP paper, I'll use the Campos et al. 2024 TACL survey as the third paper.

Wait, for the conformal prediction cluster, the user wants a NLP/序列标注 conformal prediction work. 

The TACL survey might be too broad for what the user needs. I should look for more specific conformal prediction work in NLP—either the Bates et al. 2021 paper or something more recent from 2022-2024. For the token span uncertainty NER cluster, I found E-NER from Zhang et al. 2023, but I still need to locate the third paper the user mentioned, possibly He et al. 2020 or another relevant work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "5ba97e0a-73cd-41b5-a1cf-695dffdd03fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tDk6ASE2kzZrfUYzDTApe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4310,
      "cache_read_input_tokens": 40532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4310
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

_source line 41_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MMEMTVFA68JJ8QKV94T9vk`</summary>

```json
{
  "query": "Xiao Wang 2019 AAAI \"Quantifying Uncertainties\" authors \"Yijun Xiao\" \"William Yang Wang\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "79a4db38-9c1d-4a1b-82ac-166a866919a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tDk6ASE2kzZrfUYzDTApe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4310,
      "cache_read_input_tokens": 40532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4310
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

_source line 42_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N9AY4st7jrjfg7sVTsvL6W`</summary>

```json
{
  "query": "Zhang et al 2023 E-NER evidential deep learning NER ACL Findings authors full list doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "30759b8d-b813-4088-8b1a-d8fe632291dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tDk6ASE2kzZrfUYzDTApe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4310,
      "cache_read_input_tokens": 40532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4310
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

_source line 43_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018pa83G5rzR9hnQVf8gRJ2U`</summary>

```json
{
  "query": "Bates et al 2021 \"Distribution-Free Risk-Controlling Prediction Sets\" conformal prediction structured"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "87081b66-15a4-4946-8e06-c236274670fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tDk6ASE2kzZrfUYzDTApe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4310,
      "cache_read_input_tokens": 40532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4310
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

_source line 44 · 2026-05-14T18:09:47.837Z_

<details><summary>↩ Tool result · `toolu_01MMEMTVFA68JJ8QKV94T9vk`</summary>

```text
Web search results for query: "Xiao Wang 2019 AAAI "Quantifying Uncertainties" authors "Yijun Xiao" "William Yang Wang""

Links: [{"title":"Quantifying Uncertainties in Natural Language Processing Tasks | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/4719"},{"title":"The Thirty-Third AAAI Conference on Artiﬁcial Intelligence (AAAI-19)","url":"https://ojs.aaai.org/index.php/AAAI/article/download/4719/4597"},{"title":"Quantifying Uncertainties in Natural Language Processing Tasks | ScienceGate","url":"https://www.sciencegate.app/document/10.1609/aaai.v33i01.33017322"},{"title":"dblp: Yijun Xiao","url":"https://dblp.org/pid/52/3925.html"},{"title":"Quantifying Uncertainties in Natural Language Processing ...","url":"https://ojs.aaai.org/index.php/AAAI/article/view/4719/4597"},{"title":"Quantifying Uncertainties in Natural Language Processing Tasks","url":"https://www.researchgate.net/publication/335380068_Quantifying_Uncertainties_in_Natural_Language_Processing_Tasks"},{"title":"[1811.07253v1] Quantifying Uncertainties in Natural Language Processing Tasks","url":"https://arxiv.org/abs/1811.07253v1"},{"title":"Quantifying Uncertainties in Natural Language Processing Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181107253X/abstract"},{"title":"[1811.07253] Quantifying Uncertainties in Natural Language Processing Tasks","url":"https://arxiv.org/abs/1811.07253"},{"title":"[PDF] Quantifying Uncertainties in Natural Language Processing Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Uncertainties-in-Natural-Language-Tasks-Xiao-Wang/0ca98cfa07e963932bd62e18189a25356d5355d2"}]

I found the paper you're looking for! Here are the search results:

The paper "Quantifying Uncertainties in Natural Language Processing Tasks" was authored by Yijun Xiao and William Yang Wang from University of California, Santa Barbara. 

The paper was published at AAAI 2019 with pages 7322-7329.

The paper proposes novel methods to study the benefits of characterizing model and data uncertainties for NLP tasks, with empirical experiments on sentiment analysis, named entity recognition, and language modeling using convolutional and recurrent neural network models, showing that explicitly modeling uncertainties is useful at enhancing model performances in various NLP tasks.

The paper is available at the official AAAI proceedings: https://ojs.aaai.org/index.php/AAAI/article/view/4719


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "d16a2da4-60db-4a8b-98c2-5056c2dd2d48",
  "tool_use_result": {
    "query": "Xiao Wang 2019 AAAI \"Quantifying Uncertainties\" authors \"Yijun Xiao\" \"William Yang Wang\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HYvP1ULtbj1cpHEP1cpeGC",
        "content": [
          {
            "title": "Quantifying Uncertainties in Natural Language Processing Tasks | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/4719"
          },
          {
            "title": "The Thirty-Third AAAI Conference on Artiﬁcial Intelligence (AAAI-19)",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/4719/4597"
          },
          {
            "title": "Quantifying Uncertainties in Natural Language Processing Tasks | ScienceGate",
            "url": "https://www.sciencegate.app/document/10.1609/aaai.v33i01.33017322"
          },
          {
            "title": "dblp: Yijun Xiao",
            "url": "https://dblp.org/pid/52/3925.html"
          },
          {
            "title": "Quantifying Uncertainties in Natural Language Processing ...",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/4719/4597"
          },
          {
            "title": "Quantifying Uncertainties in Natural Language Processing Tasks",
            "url": "https://www.researchgate.net/publication/335380068_Quantifying_Uncertainties_in_Natural_Language_Processing_Tasks"
          },
          {
            "title": "[1811.07253v1] Quantifying Uncertainties in Natural Language Processing Tasks",
            "url": "https://arxiv.org/abs/1811.07253v1"
          },
          {
            "title": "Quantifying Uncertainties in Natural Language Processing Tasks - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2018arXiv181107253X/abstract"
          },
          {
            "title": "[1811.07253] Quantifying Uncertainties in Natural Language Processing Tasks",
            "url": "https://arxiv.org/abs/1811.07253"
          },
          {
            "title": "[PDF] Quantifying Uncertainties in Natural Language Processing Tasks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Quantifying-Uncertainties-in-Natural-Language-Tasks-Xiao-Wang/0ca98cfa07e963932bd62e18189a25356d5355d2"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\nThe paper \"Quantifying Uncertainties in Natural Language Processing Tasks\" was authored by Yijun Xiao and William Yang Wang from University of California, Santa Barbara. \n\nThe paper was published at AAAI 2019 with pages 7322-7329.\n\nThe paper proposes novel methods to study the benefits of characterizing model and data uncertainties for NLP tasks, with empirical experiments on sentiment analysis, named entity recognition, and language modeling using convolutional and recurrent neural network models, showing that explicitly modeling uncertainties is useful at enhancing model performances in various NLP tasks.\n\nThe paper is available at the official AAAI proceedings: https://ojs.aaai.org/index.php/AAAI/article/view/4719"
    ],
    "durationSeconds": 4.346718645999994
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T18:09:49.409Z_

<details><summary>↩ Tool result · `toolu_01N9AY4st7jrjfg7sVTsvL6W`</summary>

```text
Web search results for query: "Zhang et al 2023 E-NER evidential deep learning NER ACL Findings authors full list doi"

Links: [{"title":"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/2023.findings-acl.103/"},{"title":"E-NER: Evidential Deep Learning for Trustworthy Named ...","url":"https://aclanthology.org/2023.findings-acl.103.pdf"},{"title":"GitHub - zhzhengit/ENER: E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition","url":"https://github.com/zhzhengit/ENER"},{"title":"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/372915667_E-NER_Evidential_Deep_Learning_for_Trustworthy_Named_Entity_Recognition"},{"title":"[Quick Review] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition","url":"https://liner.com/review/ener-evidential-deep-learning-for-trustworthy-named-entity-recognition"},{"title":"LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024","url":"https://dl.acm.org/doi/10.1145/3589334.3645414"},{"title":"[2305.17854] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition","url":"https://arxiv.org/abs/2305.17854"},{"title":"Evidence Retrieval is almost All You Need for Fact ...","url":"https://aclanthology.org/2024.findings-acl.551.pdf"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Adversarial Robustness for Large Language NER models ...","url":"https://aclanthology.org/2023.findings-emnlp.830.pdf"}]

Based on the search results, here is the information you requested for the Zhang et al. 2023 E-NER paper:

**Full Author List:**
Zhen Zhang, Mengting Hu, Shiwan Zhao, Minlie Huang, Haotian Wang, Lemao Liu, Zhirui Zhang, Zhe Liu, and Bingzhe Wu

**Publication Details:**
- **Title:** E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition
- **Venue:** Findings of the Association for Computational Linguistics: ACL 2023, pages 1619–1634, Toronto, Canada
- **Year:** 2023

**DOI:** 
10.18653/v1/2023.findings-acl.103

The paper addresses trustworthy NER by introducing two uncertainty-guided loss terms to the conventional EDL, along with a series of uncertainty-guided training strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "f21a6f42-d4d6-48a5-b983-3db4c36cc939",
  "tool_use_result": {
    "query": "Zhang et al 2023 E-NER evidential deep learning NER ACL Findings authors full list doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TL1reDTfriwni4tPnUX4ix",
        "content": [
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/2023.findings-acl.103/"
          },
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named ...",
            "url": "https://aclanthology.org/2023.findings-acl.103.pdf"
          },
          {
            "title": "GitHub - zhzhengit/ENER: E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition",
            "url": "https://github.com/zhzhengit/ENER"
          },
          {
            "title": "E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition | Request PDF",
            "url": "https://www.researchgate.net/publication/372915667_E-NER_Evidential_Deep_Learning_for_Trustworthy_Named_Entity_Recognition"
          },
          {
            "title": "[Quick Review] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition",
            "url": "https://liner.com/review/ener-evidential-deep-learning-for-trustworthy-named-entity-recognition"
          },
          {
            "title": "LinkNER: Linking Local Named Entity Recognition Models to Large Language Models using Uncertainty | Proceedings of the ACM Web Conference 2024",
            "url": "https://dl.acm.org/doi/10.1145/3589334.3645414"
          },
          {
            "title": "[2305.17854] E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition",
            "url": "https://arxiv.org/abs/2305.17854"
          },
          {
            "title": "Evidence Retrieval is almost All You Need for Fact ...",
            "url": "https://aclanthology.org/2024.findings-acl.551.pdf"
          },
          {
            "title": "A Survey of Generative Information Extraction",
            "url": "https://aclanthology.org/2025.coling-main.324.pdf"
          },
          {
            "title": "Adversarial Robustness for Large Language NER models ...",
            "url": "https://aclanthology.org/2023.findings-emnlp.830.pdf"
          }
        ]
      },
      "Based on the search results, here is the information you requested for the Zhang et al. 2023 E-NER paper:\n\n**Full Author List:**\nZhen Zhang, Mengting Hu, Shiwan Zhao, Minlie Huang, Haotian Wang, Lemao Liu, Zhirui Zhang, Zhe Liu, and Bingzhe Wu\n\n**Publication Details:**\n- **Title:** E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\n- **Venue:** Findings of the Association for Computational Linguistics: ACL 2023, pages 1619–1634, Toronto, Canada\n- **Year:** 2023\n\n**DOI:** \n10.18653/v1/2023.findings-acl.103\n\nThe paper addresses trustworthy NER by introducing two uncertainty-guided loss terms to the conventional EDL, along with a series of uncertainty-guided training strategies."
    ],
    "durationSeconds": 5.111883048000004
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T18:09:52.480Z_

<details><summary>↩ Tool result · `toolu_018pa83G5rzR9hnQVf8gRJ2U`</summary>

```text
Web search results for query: "Bates et al 2021 "Distribution-Free Risk-Controlling Prediction Sets" conformal prediction structured"

Links: [{"title":"Distribution-free, Risk-controlling Prediction Sets | Journal of the ACM","url":"https://dl.acm.org/doi/10.1145/3478535"},{"title":"Distribution-free, Risk-controlling Prediction Sets | Request PDF","url":"https://www.researchgate.net/publication/357462027_Distribution-free_Risk-controlling_Prediction_Sets"},{"title":"Distribution-free, Risk-controlling Prediction Sets","url":"https://dl.acm.org/doi/fullHtml/10.1145/3478535"},{"title":"Distribution-Free, Risk-Controlling Prediction Sets","url":"https://arxiv.org/pdf/2101.02703"},{"title":"[2101.02703] Distribution-Free, Risk-Controlling Prediction Sets","url":"https://arxiv.org/abs/2101.02703"},{"title":"Distribution-Free, Risk-Controlling Prediction Sets","url":"https://d3qi0qp55mx5f5.cloudfront.net/stat/docs/Statistics_Colloquium/2020-21/Bates__Stephen041221.pdf?mtime=1617641545"},{"title":"[PDF] Distribution-Free, Risk-Controlling Prediction Sets | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Distribution-Free,-Risk-Controlling-Prediction-Sets-Bates-Angelopoulos/e343f1517f038da090a78159363d14cdad5ddc35"},{"title":"Conformal Risk Control | OpenReview","url":"https://openreview.net/forum?id=33XGfHLtZg"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"Conformal Risk Control | Request PDF","url":"https://www.researchgate.net/publication/362489559_Conformal_Risk_Control"}]

I've successfully found information about the Bates et al. 2021 paper on "Distribution-Free Risk-Controlling Prediction Sets" and conformal prediction. Here are the key findings:

## Paper Details

The paper "Distribution-free, Risk-controlling Prediction Sets" was authored by Stephen Bates, Anastasios Angelopoulos, Lihua Lei, Jitendra Malik, and Michael Jordan, published in 2021 in J. ACM 68, 6, Article 43 (September 2021).

## Main Contribution

The work shows how to generate set-valued predictions from a black-box predictor that control the expected loss on future test points at a user-specified level. Their approach provides explicit finite-sample guarantees for any dataset by using a holdout set to calibrate the size of the prediction sets.

## Connection to Conformal Prediction

The work expands the notion of tolerance regions to apply to a wider class of losses for set-valued predictors, with development inspired by the nested set interpretation of conformal prediction, and the proposed algorithm is somewhat similar to split conformal prediction.

## Key Features

The central contribution of this work is a procedure to calibrate prediction sets to have finite-sample control of any loss satisfying a certain monotonicity requirement. The paper demonstrates applications across multiple domains including classification problems where some mistakes are more costly than others and multi-label classification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "76fef670-a76f-456a-ac9c-bcdb09da9eca",
  "tool_use_result": {
    "query": "Bates et al 2021 \"Distribution-Free Risk-Controlling Prediction Sets\" conformal prediction structured",
    "results": [
      {
        "tool_use_id": "srvtoolu_0169unqyLV7QjmwS7pNARGem",
        "content": [
          {
            "title": "Distribution-free, Risk-controlling Prediction Sets | Journal of the ACM",
            "url": "https://dl.acm.org/doi/10.1145/3478535"
          },
          {
            "title": "Distribution-free, Risk-controlling Prediction Sets | Request PDF",
            "url": "https://www.researchgate.net/publication/357462027_Distribution-free_Risk-controlling_Prediction_Sets"
          },
          {
            "title": "Distribution-free, Risk-controlling Prediction Sets",
            "url": "https://dl.acm.org/doi/fullHtml/10.1145/3478535"
          },
          {
            "title": "Distribution-Free, Risk-Controlling Prediction Sets",
            "url": "https://arxiv.org/pdf/2101.02703"
          },
          {
            "title": "[2101.02703] Distribution-Free, Risk-Controlling Prediction Sets",
            "url": "https://arxiv.org/abs/2101.02703"
          },
          {
            "title": "Distribution-Free, Risk-Controlling Prediction Sets",
            "url": "https://d3qi0qp55mx5f5.cloudfront.net/stat/docs/Statistics_Colloquium/2020-21/Bates__Stephen041221.pdf?mtime=1617641545"
          },
          {
            "title": "[PDF] Distribution-Free, Risk-Controlling Prediction Sets | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Distribution-Free,-Risk-Controlling-Prediction-Sets-Bates-Angelopoulos/e343f1517f038da090a78159363d14cdad5ddc35"
          },
          {
            "title": "Conformal Risk Control | OpenReview",
            "url": "https://openreview.net/forum?id=33XGfHLtZg"
          },
          {
            "title": "[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
            "url": "https://arxiv.org/abs/2107.07511"
          },
          {
            "title": "Conformal Risk Control | Request PDF",
            "url": "https://www.researchgate.net/publication/362489559_Conformal_Risk_Control"
          }
        ]
      },
      "I've successfully found information about the Bates et al. 2021 paper on \"Distribution-Free Risk-Controlling Prediction Sets\" and conformal prediction. Here are the key findings:\n\n## Paper Details\n\nThe paper \"Distribution-free, Risk-controlling Prediction Sets\" was authored by Stephen Bates, Anastasios Angelopoulos, Lihua Lei, Jitendra Malik, and Michael Jordan, published in 2021 in J. ACM 68, 6, Article 43 (September 2021).\n\n## Main Contribution\n\nThe work shows how to generate set-valued predictions from a black-box predictor that control the expected loss on future test points at a user-specified level. Their approach provides explicit finite-sample guarantees for any dataset by using a holdout set to calibrate the size of the prediction sets.\n\n## Connection to Conformal Prediction\n\nThe work expands the notion of tolerance regions to apply to a wider class of losses for set-valued predictors, with development inspired by the nested set interpretation of conformal prediction, and the proposed algorithm is somewhat similar to split conformal prediction.\n\n## Key Features\n\nThe central contribution of this work is a procedure to calibrate prediction sets to have finite-sample control of any loss satisfying a certain monotonicity requirement. The paper demonstrates applications across multiple domains including classification problems where some mistakes are more costly than others and multi-label classification."
    ],
    "durationSeconds": 7.830790666999994
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also get the DOI for the Angelopoulos et al. paper and verify a couple more details. But I think I have enough. Let me also search for the Fomicheva et al. authors list.

Actually wait, let me reconsider the third paper for each cluster:

1. **conformal_prediction cluster**: Bates et al. 2021 "Distribution-Free Risk-Controlling Prediction Sets" - this is a good choice as it extends conformal prediction to structured prediction with risk control. Published in JACM 2021.


2. **token_span_uncertainty_ner cluster**: E-NER (Zhang et al. 2023, ACL Findings) works well for token-level uncertainty in NER, even though the user mentioned a He et al. 2020 paper that doesn't seem to exist.
3. **ensemble_mc_dropout cluster**: Fomicheva et al. 2020 TACL is a solid fit for MC dropout and ensemble methods in NLP.

Let me gather the remaining details I need. I have the remaining papers to add: Xiao & Wang's 2019 AAAI work on quantifying uncertainties in NLP, Shelmanov et al.'s 2021 EACL paper on active learning with Bayesian estimates, Zhang et al.'s 2023 ACL Findings paper on evidential deep learning for NER, Lakshminarayanan et al.'s foundational 2017 NeurIPS work on deep ensembles, Gal & Ghahramani's influential 2016 ICML paper on dropout as Bayesian approximation, and Fomicheva et al.'s 2020 TACL paper on unsupervised quality estimation. Now I'll write all nine papers to the YAML file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "ad55c0d7-a011-4876-a233-eccc1f4138dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RQN7V2D1X4kMyLozT4cZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 44842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 48_

9 篇论文信息已确认。用 Python 脚本写入 YAML。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "0c31978e-7a54-4c12-a8ce-b200395543aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RQN7V2D1X4kMyLozT4cZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 44842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_01XfvUoaZc5S6NJuMbSKoFLt`</summary>

```json
{
  "command": "python3 -c \"import yaml; print('PyYAML available')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "525571ba-75c6-4647-8c2c-367ca3365e72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RQN7V2D1X4kMyLozT4cZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3021,
      "cache_read_input_tokens": 44842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3021
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

_source line 50 · 2026-05-14T18:10:12.496Z_

<details><summary>↩ Tool result · `toolu_01XfvUoaZc5S6NJuMbSKoFLt`</summary>

```text
PyYAML available
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "bce5936b-7c4e-4bec-9273-3fdfea60de4c",
  "tool_use_result": {
    "stdout": "PyYAML available",
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

_source line 51_

<details open><summary>🔧 Tool call — Bash · `toolu_01FeUjnqJbViMfjx1ecd1Ppr`</summary>

```json
{
  "command": "cat << 'PYEOF' > /tmp/update_lit_map.py\nimport yaml\nfrom datetime import datetime, timezone\n\nyaml_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml\"\n\nwith open(yaml_path, 'r') as f:\n    data = yaml.safe_load(f)\n\nnow = datetime.now(timezone.utc).strftime(\"%Y-%m-%dT%H:%M:%S.000Z\")\n\nnew_papers = {\n    # ====== Cluster: conformal_prediction ======\n    \"fisch2021conformal\": {\n        \"title\": \"Few-Shot Conformal Prediction with Auxiliary Tasks\",\n        \"authors\": [\"Adam Fisch\", \"Tal Schuster\", \"Tommi Jaakkola\", \"Regina Barzilay\"],\n        \"year\": 2021,\n        \"venue\": \"ICML 2021\",\n        \"url\": \"https://arxiv.org/abs/2102.08898\",\n        \"doi\": \"10.5555/3524938.3525234\",\n        \"bibtex_key\": \"fisch2021conformal\",\n        \"category\": \"conformal_prediction\",\n        \"role\": \"foundation\",\n        \"relevance\": \"Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter prediction sets with formal coverage guarantees. Foundational for applying CP when calibration data is scarce in IE.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    \"angelopoulos2021conformal\": {\n        \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\",\n        \"authors\": [\"Anastasios N. Angelopoulos\", \"Stephen Bates\", \"Jitendra Malik\", \"Michael I. Jordan\"],\n        \"year\": 2021,\n        \"venue\": \"ICLR 2021\",\n        \"url\": \"https://arxiv.org/abs/2009.14193\",\n        \"doi\": \"\",\n        \"bibtex_key\": \"angelopoulos2021conformal\",\n        \"category\": \"conformal_prediction\",\n        \"role\": \"foundation\",\n        \"relevance\": \"Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for conformal prediction methodology we adapt to structured IE output sets.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    \"bates2021rcps\": {\n        \"title\": \"Distribution-Free, Risk-Controlling Prediction Sets\",\n        \"authors\": [\"Stephen Bates\", \"Anastasios Angelopoulos\", \"Lihua Lei\", \"Jitendra Malik\", \"Michael I. Jordan\"],\n        \"year\": 2021,\n        \"venue\": \"Journal of the ACM 2021\",\n        \"url\": \"https://arxiv.org/abs/2101.02703\",\n        \"doi\": \"10.1145/3478535\",\n        \"bibtex_key\": \"bates2021rcps\",\n        \"category\": \"conformal_prediction\",\n        \"role\": \"background\",\n        \"relevance\": \"Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample guarantees. Provides the theoretical basis for risk-controlled prediction in structured IE tasks.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    # ====== Cluster: token_span_uncertainty_ner ======\n    \"xiao2019uncertainty\": {\n        \"title\": \"Quantifying Uncertainties in Natural Language Processing Tasks\",\n        \"authors\": [\"Yijun Xiao\", \"William Yang Wang\"],\n        \"year\": 2019,\n        \"venue\": \"AAAI 2019\",\n        \"url\": \"https://arxiv.org/abs/1811.07253\",\n        \"doi\": \"10.1609/aaai.v33i01.33017322\",\n        \"bibtex_key\": \"xiao2019uncertainty\",\n        \"category\": \"token_span_uncertainty_ner\",\n        \"role\": \"foundation\",\n        \"relevance\": \"Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model uncertainty improves both performance and reliability for token-level predictions.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    \"shelmanov2021active\": {\n        \"title\": \"Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\",\n        \"authors\": [\"Artem Shelmanov\", \"Dmitri Puzyrev\", \"Lyubov Kupriyanova\", \"Denis Belyakov\", \"Daniil Larionov\", \"Nikita Khromov\", \"Olga Kozlova\", \"Ekaterina Artemova\", \"Dmitry V. Dylov\", \"Alexander Panchenko\"],\n        \"year\": 2021,\n        \"venue\": \"EACL 2021\",\n        \"url\": \"https://arxiv.org/abs/2101.08133\",\n        \"doi\": \"10.18653/v1/2021.eacl-main.145\",\n        \"bibtex_key\": \"shelmanov2021active\",\n        \"category\": \"token_span_uncertainty_ner\",\n        \"role\": \"foundation\",\n        \"relevance\": \"Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    \"zhang2023ener\": {\n        \"title\": \"E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition\",\n        \"authors\": [\"Zhen Zhang\", \"Mengting Hu\", \"Shiwan Zhao\", \"Minlie Huang\", \"Haotian Wang\", \"Lemao Liu\", \"Zhirui Zhang\", \"Zhe Liu\", \"Bingzhe Wu\"],\n        \"year\": 2023,\n        \"venue\": \"ACL Findings 2023\",\n        \"url\": \"https://arxiv.org/abs/2305.17854\",\n        \"doi\": \"10.18653/v1/2023.findings-acl.103\",\n        \"bibtex_key\": \"zhang2023ener\",\n        \"category\": \"token_span_uncertainty_ner\",\n        \"role\": \"background\",\n        \"relevance\": \"Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    # ====== Cluster: ensemble_mc_dropout ======\n    \"lakshminarayanan2017ensembles\": {\n        \"title\": \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\",\n        \"authors\": [\"Balaji Lakshminarayanan\", \"Alexander Pritzel\", \"Charles Blundell\"],\n        \"year\": 2017,\n        \"venue\": \"NeurIPS 2017\",\n        \"url\": \"https://arxiv.org/abs/1612.01474\",\n        \"doi\": \"\",\n        \"bibtex_key\": \"lakshminarayanan2017ensembles\",\n        \"category\": \"ensemble_mc_dropout\",\n        \"role\": \"foundation\",\n        \"relevance\": \"Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation. Foundational baseline for ensemble-based uncertainty quantification we compare against.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    \"gal2016dropout\": {\n        \"title\": \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\",\n        \"authors\": [\"Yarin Gal\", \"Zoubin Ghahramani\"],\n        \"year\": 2016,\n        \"venue\": \"ICML 2016\",\n        \"url\": \"https://arxiv.org/abs/1506.02142\",\n        \"doi\": \"\",\n        \"bibtex_key\": \"gal2016dropout\",\n        \"category\": \"ensemble_mc_dropout\",\n        \"role\": \"foundation\",\n        \"relevance\": \"Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n    \"fomicheva2020unsupervised\": {\n        \"title\": \"Unsupervised Quality Estimation for Neural Machine Translation\",\n        \"authors\": [\"Marina Fomicheva\", \"Shuo Sun\", \"Lisa Yankovskaya\", \"Frédéric Blain\", \"Francisco Guzmán\", \"Mark Fishel\", \"Nikolaos Aletras\", \"Vishrav Chaudhary\", \"Lucia Specia\"],\n        \"year\": 2020,\n        \"venue\": \"TACL 2020\",\n        \"url\": \"https://arxiv.org/abs/2005.10608\",\n        \"doi\": \"10.1162/tacl_a_00330\",\n        \"bibtex_key\": \"fomicheva2020unsupervised\",\n        \"category\": \"ensemble_mc_dropout\",\n        \"role\": \"background\",\n        \"relevance\": \"Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\",\n        \"abstract\": \"\",\n        \"semantic_scholar_id\": \"\",\n        \"verified\": True,\n        \"added_by\": \"paper-research:lit_batch2\",\n        \"added_at\": now,\n    },\n}\n\n# Check for duplicates\nexisting_keys = set(data.get(\"papers\", {}).keys())\nfor key in new_papers:\n    if key in existing_keys:\n        print(f\"WARNING: {key} already exists, skipping\")\n        del new_papers[key]\n\ndata[\"papers\"].update(new_papers)\ndata[\"meta\"][\"total_papers\"] = len(data[\"papers\"])\ndata[\"meta\"][\"last_updated\"] = now\n\nclass LiteralStr(str):\n    pass\n\ndef literal_str_representer(dumper, data):\n    if '\\n' in data:\n        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')\n    return dumper.represent_scalar('tag:yaml.org,2002:str', data)\n\nyaml.add_representer(LiteralStr, literal_str_representer)\n\nwith open(yaml_path, 'w') as f:\n    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)\n\nprint(f\"Done. Total papers: {data['meta']['total_papers']}\")\nprint(f\"Added {len(new_papers)} new papers\")\nfor k in new_papers:\n    print(f\"  + {k} [{new_papers[k]['category']}]\")\nPYEOF\npython3 /tmp/update_lit_map.py",
  "description": "Append 9 new papers to literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "d082f838-cf5f-4de2-9335-c761be92e254",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QVgdFicPHw27zpLg7QDkZi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1123,
      "cache_read_input_tokens": 47863,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1123
      },
      "output_tokens": 46,
      "service_tier": "standard",
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

_source line 52 · 2026-05-14T18:10:52.333Z_

<details><summary>↩ Tool result · `toolu_01FeUjnqJbViMfjx1ecd1Ppr`</summary>

```text
Done. Total papers: 30
Added 9 new papers
  + fisch2021conformal [conformal_prediction]
  + angelopoulos2021conformal [conformal_prediction]
  + bates2021rcps [conformal_prediction]
  + xiao2019uncertainty [token_span_uncertainty_ner]
  + shelmanov2021active [token_span_uncertainty_ner]
  + zhang2023ener [token_span_uncertainty_ner]
  + lakshminarayanan2017ensembles [ensemble_mc_dropout]
  + gal2016dropout [ensemble_mc_dropout]
  + fomicheva2020unsupervised [ensemble_mc_dropout]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "6f3bfaf9-a18e-4aee-b72a-01685227546e",
  "tool_use_result": {
    "stdout": "Done. Total papers: 30\nAdded 9 new papers\n  + fisch2021conformal [conformal_prediction]\n  + angelopoulos2021conformal [conformal_prediction]\n  + bates2021rcps [conformal_prediction]\n  + xiao2019uncertainty [token_span_uncertainty_ner]\n  + shelmanov2021active [token_span_uncertainty_ner]\n  + zhang2023ener [token_span_uncertainty_ner]\n  + lakshminarayanan2017ensembles [ensemble_mc_dropout]\n  + gal2016dropout [ensemble_mc_dropout]\n  + fomicheva2020unsupervised [ensemble_mc_dropout]",
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

_source line 53_

验证写入结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "daef1fe0-a127-4908-9512-6fbee9be1c3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eLePov7KeDVcKMwC9V3VD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 48986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3302
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

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rok1DJs2JSwUTP9WUm14fy`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml') as f:\n    d = yaml.safe_load(f)\nprint(f'total_papers: {d[\\\"meta\\\"][\\\"total_papers\\\"]}')\nprint(f'last_updated: {d[\\\"meta\\\"][\\\"last_updated\\\"]}')\nprint()\nfor cluster in ['conformal_prediction', 'token_span_uncertainty_ner', 'ensemble_mc_dropout']:\n    papers = [(k,v) for k,v in d['papers'].items() if v['category'] == cluster]\n    print(f'=== {cluster} ({len(papers)} papers) ===')\n    for k,v in papers:\n        print(f'  {k}: {v[\\\"role\\\"]} | {v[\\\"venue\\\"]} | verified={v[\\\"verified\\\"]}')\n    print()\n\"",
  "description": "Verify YAML cluster counts and structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "f0538fa6-4542-49d0-95fe-9c5364bf1181",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eLePov7KeDVcKMwC9V3VD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3302,
      "cache_read_input_tokens": 48986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3302
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

_source line 55 · 2026-05-14T18:10:59.203Z_

<details><summary>↩ Tool result · `toolu_01Rok1DJs2JSwUTP9WUm14fy`</summary>

```text
total_papers: 30
last_updated: 2026-05-14T18:10:52.000Z

=== conformal_prediction (3 papers) ===
  fisch2021conformal: foundation | ICML 2021 | verified=True
  angelopoulos2021conformal: foundation | ICLR 2021 | verified=True
  bates2021rcps: background | Journal of the ACM 2021 | verified=True

=== token_span_uncertainty_ner (3 papers) ===
  xiao2019uncertainty: foundation | AAAI 2019 | verified=True
  shelmanov2021active: foundation | EACL 2021 | verified=True
  zhang2023ener: background | ACL Findings 2023 | verified=True

=== ensemble_mc_dropout (3 papers) ===
  lakshminarayanan2017ensembles: foundation | NeurIPS 2017 | verified=True
  gal2016dropout: foundation | ICML 2016 | verified=True
  fomicheva2020unsupervised: background | TACL 2020 | verified=True
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "cb620150-7455-4b8b-85f8-11bb73a073b8",
  "tool_use_result": {
    "stdout": "total_papers: 30\nlast_updated: 2026-05-14T18:10:52.000Z\n\n=== conformal_prediction (3 papers) ===\n  fisch2021conformal: foundation | ICML 2021 | verified=True\n  angelopoulos2021conformal: foundation | ICLR 2021 | verified=True\n  bates2021rcps: background | Journal of the ACM 2021 | verified=True\n\n=== token_span_uncertainty_ner (3 papers) ===\n  xiao2019uncertainty: foundation | AAAI 2019 | verified=True\n  shelmanov2021active: foundation | EACL 2021 | verified=True\n  zhang2023ener: background | ACL Findings 2023 | verified=True\n\n=== ensemble_mc_dropout (3 papers) ===\n  lakshminarayanan2017ensembles: foundation | NeurIPS 2017 | verified=True\n  gal2016dropout: foundation | ICML 2016 | verified=True\n  fomicheva2020unsupervised: background | TACL 2020 | verified=True",
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

_source line 56_

9 篇论文已写入，3 个 cluster 各 3 篇，total_papers 从 21 → 30。

| Cluster | Key | Venue | Role |
|---|---|---|---|
| **conformal_prediction** | `fisch2021conformal` | ICML 2021 | foundation |
| | `angelopoulos2021conformal` | ICLR 2021 | foundation |
| | `bates2021rcps` | JACM 2021 | background |
| **token_span_uncertainty_ner** | `xiao2019uncertainty` | AAAI 2019 | foundation |
| | `shelmanov2021active` | EACL 2021 | foundation |
| | `zhang2023ener` | ACL Findings 2023 | background |
| **ensemble_mc_dropout** | `lakshminarayanan2017ensembles` | NeurIPS 2017 | foundation |
| | `gal2016dropout` | ICML 2016 | foundation |
| | `fomicheva2020unsupervised` | TACL 2020 | background |

注意：Fisch et al. 2021 实际发表在 ICML（非 NeurIPS）；token_span_uncertainty_ner 的第三篇用 Zhang et al. 2023 E-NER 替代了未找到的 He et al. 2020。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "uuid": "55f2c355-642c-407e-a227-1de3cac35e02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018WYNcdTqdDNwjG75UNvLgi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 622,
      "cache_read_input_tokens": 52288,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 622
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

_source line 57_

9 篇论文已写入，3 个 cluster 各 3 篇，total_papers 从 21 → 30。

| Cluster | Key | Venue | Role |
|---|---|---|---|
| **conformal_prediction** | `fisch2021conformal` | ICML 2021 | foundation |
| | `angelopoulos2021conformal` | ICLR 2021 | foundation |
| | `bates2021rcps` | JACM 2021 | background |
| **token_span_uncertainty_ner** | `xiao2019uncertainty` | AAAI 2019 | foundation |
| | `shelmanov2021active` | EACL 2021 | foundation |
| | `zhang2023ener` | ACL Findings 2023 | background |
| **ensemble_mc_dropout** | `lakshminarayanan2017ensembles` | NeurIPS 2017 | foundation |
| | `gal2016dropout` | ICML 2016 | foundation |
| | `fomicheva2020unsupervised` | TACL 2020 | background |

注意：Fisch et al. 2021 实际发表在 ICML（非 NeurIPS）；token_span_uncertainty_ner 的第三篇用 Zhang et al. 2023 E-NER 替代了未找到的 He et al. 2020。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 145686,
  "duration_api_ms": 224982,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "0a426555-861f-4b0f-8c37-773cbab73c2b",
  "total_cost_usd": 1.0698772500000002,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 41209,
    "cache_read_input_tokens": 301710,
    "output_tokens": 7368,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 41209,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 367,
        "cache_read_input_tokens": 52288,
        "cache_creation_input_tokens": 622,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 622
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 284301,
      "outputTokens": 6581,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 16,
      "costUSD": 0.477206,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 7368,
      "cacheReadInputTokens": 301710,
      "cacheCreationInputTokens": 41209,
      "webSearchRequests": 0,
      "costUSD": 0.59267125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4bb59f12-e2c6-4333-b6c0-62f574946e19"
}
```

</details>

---
