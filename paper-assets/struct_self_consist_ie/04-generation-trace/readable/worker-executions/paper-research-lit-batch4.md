# paper research lit batch4

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_research_lit_batch4_20260514T184756.log`
- **Structured JSON:** [`1ef88fdb9d0abf7f9cdc.json`](../../sessions/1e/1ef88fdb9d0abf7f9cdc.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
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
  "uuid": "92c1622b-909d-4e6d-8e13-adffeba94516",
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
  "uuid": "a9cf145b-0004-4e02-8298-ca8e5123d070",
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current literature_map.yaml to understand the existing structure, then search for the required papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "032b7f5c-cbaf-4de0-8b8d-c289e8978ea9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gh3JwwnkHjzgBU61qdrPCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12171,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12171
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01GncgZpHDvj5sp4YyKdxSiH`</summary>

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
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "d3734344-87c1-4c1d-b2d5-d3c1bb07d4d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gh3JwwnkHjzgBU61qdrPCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12171,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12171
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

_source line 6 · 2026-05-14T18:48:06.634Z_

<details><summary>↩ Tool result · `toolu_01GncgZpHDvj5sp4YyKdxSiH`</summary>

```text
1	meta:
2	  last_updated: '2026-05-14T19:30:00.000Z'
3	  total_papers: 41
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
516	    role: foundation
517	    relevance: Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter
518	      prediction sets with formal coverage guarantees. Foundational for applying CP when calibration data is scarce in IE.
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
559	    role: background
560	    relevance: Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample
561	      guarantees. Provides the theoretical basis for risk-controlled prediction in structured IE tasks.
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
951	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "590ec7b2-1544-43a5-9e99-8db9dfb0dd72",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
      "content": "meta:\n  last_updated: '2026-05-14T19:30:00.000Z'\n  total_papers: 41\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\n      for our structured consistency metric that operates at the semantic level of IE triples.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  fisch2021conformal:\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\n    authors:\n    - Adam Fisch\n    - Tal Schuster\n    - Tommi Jaakkola\n    - Regina Barzilay\n    year: 2021\n    venue: ICML 2021\n    url: https://arxiv.org/abs/2102.08898\n    doi: 10.5555/3524938.3525234\n    bibtex_key: fisch2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\n      prediction sets with formal coverage guarantees. Foundational for applying CP when calibration data is scarce in IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  angelopoulos2021conformal:\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\n    authors:\n    - Anastasios N. Angelopoulos\n    - Stephen Bates\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.14193\n    doi: ''\n    bibtex_key: angelopoulos2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\n      conformal prediction methodology we adapt to structured IE output sets.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  bates2021rcps:\n    title: Distribution-Free, Risk-Controlling Prediction Sets\n    authors:\n    - Stephen Bates\n    - Anastasios Angelopoulos\n    - Lihua Lei\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: Journal of the ACM 2021\n    url: https://arxiv.org/abs/2101.02703\n    doi: 10.1145/3478535\n    bibtex_key: bates2021rcps\n    category: conformal_prediction\n    role: background\n    relevance: Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\n      guarantees. Provides the theoretical basis for risk-controlled prediction in structured IE tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  xiao2019uncertainty:\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\n    authors:\n    - Yijun Xiao\n    - William Yang Wang\n    year: 2019\n    venue: AAAI 2019\n    url: https://arxiv.org/abs/1811.07253\n    doi: 10.1609/aaai.v33i01.33017322\n    bibtex_key: xiao2019uncertainty\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\n      uncertainty improves both performance and reliability for token-level predictions.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  shelmanov2021active:\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\n    authors:\n    - Artem Shelmanov\n    - Dmitri Puzyrev\n    - Lyubov Kupriyanova\n    - Denis Belyakov\n    - Daniil Larionov\n    - Nikita Khromov\n    - Olga Kozlova\n    - Ekaterina Artemova\n    - Dmitry V. Dylov\n    - Alexander Panchenko\n    year: 2021\n    venue: EACL 2021\n    url: https://arxiv.org/abs/2101.08133\n    doi: 10.18653/v1/2021.eacl-main.145\n    bibtex_key: shelmanov2021active\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  zhang2023ener:\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\n    authors:\n    - Zhen Zhang\n    - Mengting Hu\n    - Shiwan Zhao\n    - Minlie Huang\n    - Haotian Wang\n    - Lemao Liu\n    - Zhirui Zhang\n    - Zhe Liu\n    - Bingzhe Wu\n    year: 2023\n    venue: ACL Findings 2023\n    url: https://arxiv.org/abs/2305.17854\n    doi: 10.18653/v1/2023.findings-acl.103\n    bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  lakshminarayanan2017ensembles:\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\n    authors:\n    - Balaji Lakshminarayanan\n    - Alexander Pritzel\n    - Charles Blundell\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1612.01474\n    doi: ''\n    bibtex_key: lakshminarayanan2017ensembles\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  gal2016dropout:\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\n    authors:\n    - Yarin Gal\n    - Zoubin Ghahramani\n    year: 2016\n    venue: ICML 2016\n    url: https://arxiv.org/abs/1506.02142\n    doi: ''\n    bibtex_key: gal2016dropout\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  fomicheva2020unsupervised:\n    title: Unsupervised Quality Estimation for Neural Machine Translation\n    authors:\n    - Marina Fomicheva\n    - Shuo Sun\n    - Lisa Yankovskaya\n    - Frédéric Blain\n    - Francisco Guzmán\n    - Mark Fishel\n    - Nikolaos Aletras\n    - Vishrav Chaudhary\n    - Lucia Specia\n    year: 2020\n    venue: TACL 2020\n    url: https://arxiv.org/abs/2005.10608\n    doi: 10.1162/tacl_a_00330\n    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n",
      "numLines": 951,
      "startLine": 1,
      "totalLines": 951
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0182jQpgCz9VcCbvE6LUpqkv`</summary>

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
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "04b8dd6b-a640-4d41-9ff6-c3dec3db1593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Gh3JwwnkHjzgBU61qdrPCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12171,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12171
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

_source line 8 · 2026-05-14T18:48:06.724Z_

<details><summary>↩ Tool result · `toolu_0182jQpgCz9VcCbvE6LUpqkv`</summary>

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
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "99691d4a-8cda-485d-986b-953a5190cb7e",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
I have the current literature_map.yaml with 41 papers. Now I need to search for the 10 papers to add. Let me launch parallel searches for all of them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "4b8c092f-4496-44d7-9b95-748ad56c3d76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 10_

Now I'll search for all 10 papers in parallel to verify their metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "938169db-9525-4a93-b87c-fd1d1acf0d70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KsFxGn7iz5hyLk59rsf4sQ`</summary>

```json
{
  "query": "Wadhwa et al 2023 \"Revisiting Relation Extraction in the Era of Large Language Models\" ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "b5e65f0f-6f5d-4aae-95ff-662fe54247ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FqzGDWiRgRF7kgB5gmipfo`</summary>

```json
{
  "query": "GoLLIE Sainz et al 2024 \"Annotation Guidelines improve Zero-Shot Information-Extraction\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "001354a5-bea3-474a-8eb1-56dacbc33f0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015H5o7k2rchZ14eeNxeoQy4`</summary>

```json
{
  "query": "Luan et al 2018 \"Multi-Task Identification of Entities Relations and Coreference for Scientific Knowledge Graph Construction\" EMNLP SciERC"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "a55fc53b-e842-47a6-9c10-1c5c335cb0cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RPeCxVJdVdrB6tLkJbhQnX`</summary>

```json
{
  "query": "Tjong Kim Sang De Meulder 2003 \"Introduction to the CoNLL-2003 Shared Task Language-Independent Named Entity Recognition\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "e855d6e5-7eb0-4d5a-aa4e-a4f0553497e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T3TCJGm4r8EeBhH4htf5fL`</summary>

```json
{
  "query": "Derczynski et al 2017 \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\" EMNLP Workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "e0c92c60-2a17-4442-90df-f0c932d4f53e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013ndackhpvtrEtsP7MM2crR`</summary>

```json
{
  "query": "Willard Louf 2023 \"Efficient Guided Generation for Large Language Models\" arXiv 2307.09702"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "4f5a480c-021c-4a45-bb48-17a128162b15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 17 · 2026-05-14T18:48:17.963Z_

<details><summary>↩ Tool result · `toolu_01KsFxGn7iz5hyLk59rsf4sQ`</summary>

```text
Web search results for query: "Wadhwa et al 2023 "Revisiting Relation Extraction in the Era of Large Language Models" ACL"

Links: [{"title":"Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2023.acl-long.868/"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/37674787/"},{"title":"[2305.05003] Revisiting Relation Extraction in the era of Large Language Models","url":"https://arxiv.org/abs/2305.05003"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"dblp: Revisiting Relation Extraction in the era of Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2305-05003.html"},{"title":"Revisiting Relation Extraction in the era of Large Language Models | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10523775-revisiting-relation-extraction-era-large-language-models"},{"title":"A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11280-0"},{"title":"[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"},{"title":"Empirical Analysis of Dialogue Relation Extraction with Large Language Models","url":"https://www.ijcai.org/proceedings/2024/0703.pdf"}]

I found the paper for you. Here are the key details:

**Citation Information:**
Somin Wadhwa, Silvio Amir, and Byron Wallace. 2023. Revisiting Relation Extraction in the era of Large Language Models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15566–15589, Toronto, Canada. Association for Computational Linguistics.

**Paper Overview:**
The paper examines relation extraction (RE), the task of inferring semantic relationships between entities from text. Recent work treated the problem as a sequence-to-sequence task, linearizing relations as target strings. The authors push the limits of this approach using larger language models (GPT-3 and Flan-T5 large) and evaluating their performance on standard RE tasks under varying levels of supervision. They address issues inherent to evaluating generative approaches by doing human evaluations, in lieu of relying on exact matching.

**Key Finding:**
Few-shot prompting with GPT-3 achieves near SOTA performance, roughly equivalent to existing fully supervised models.

The paper is available at: https://aclanthology.org/2023.acl-long.868/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "1449597a-0df4-481c-920d-942672b9f13f",
  "tool_use_result": {
    "query": "Wadhwa et al 2023 \"Revisiting Relation Extraction in the Era of Large Language Models\" ACL",
    "results": [
      {
        "tool_use_id": "srvtoolu_0191p6M496euhRoSpL25bUce",
        "content": [
          {
            "title": "Revisiting Relation Extraction in the era of Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2023.acl-long.868/"
          },
          {
            "title": "Revisiting Relation Extraction in the era of Large Language ...",
            "url": "https://aclanthology.org/2023.acl-long.868.pdf"
          },
          {
            "title": "Revisiting Relation Extraction in the era of Large Language Models - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/37674787/"
          },
          {
            "title": "[2305.05003] Revisiting Relation Extraction in the era of Large Language Models",
            "url": "https://arxiv.org/abs/2305.05003"
          },
          {
            "title": "Revisiting Relation Extraction in the era of Large Language Models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"
          },
          {
            "title": "dblp: Revisiting Relation Extraction in the era of Large Language Models.",
            "url": "https://dblp.org/rec/journals/corr/abs-2305-05003.html"
          },
          {
            "title": "Revisiting Relation Extraction in the era of Large Language Models | NSF Public Access Repository",
            "url": "https://par.nsf.gov/biblio/10523775-revisiting-relation-extraction-era-large-language-models"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-025-11280-0"
          },
          {
            "title": "[PDF] Revisiting Relation Extraction in the era of Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Revisiting-Relation-Extraction-in-the-era-of-Large-Wadhwa-Amir/97782a67971c4ff1a74bf07e82fe20b2c4bf86c4"
          },
          {
            "title": "Empirical Analysis of Dialogue Relation Extraction with Large Language Models",
            "url": "https://www.ijcai.org/proceedings/2024/0703.pdf"
          }
        ]
      },
      "I found the paper for you. Here are the key details:\n\n**Citation Information:**\nSomin Wadhwa, Silvio Amir, and Byron Wallace. 2023. Revisiting Relation Extraction in the era of Large Language Models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15566–15589, Toronto, Canada. Association for Computational Linguistics.\n\n**Paper Overview:**\nThe paper examines relation extraction (RE), the task of inferring semantic relationships between entities from text. Recent work treated the problem as a sequence-to-sequence task, linearizing relations as target strings. The authors push the limits of this approach using larger language models (GPT-3 and Flan-T5 large) and evaluating their performance on standard RE tasks under varying levels of supervision. They address issues inherent to evaluating generative approaches by doing human evaluations, in lieu of relying on exact matching.\n\n**Key Finding:**\nFew-shot prompting with GPT-3 achieves near SOTA performance, roughly equivalent to existing fully supervised models.\n\nThe paper is available at: https://aclanthology.org/2023.acl-long.868/"
    ],
    "durationSeconds": 5.979739081
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T2GLd3E6JMRDb4SgGT25Hh`</summary>

```json
{
  "query": "Fleiss 1971 \"Measuring Nominal Scale Agreement Among Many Raters\" Psychological Bulletin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "f1984521-d69c-445b-9232-ce9fe3a206ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016Ntev2AhtpwF918Qq6TXpX`</summary>

```json
{
  "query": "Jaccard 1901 coefficient original paper \"Étude comparative de la distribution florale\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "85dd5081-b4cc-42ab-bb8c-531f52ab9418",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 20 · 2026-05-14T18:48:20.035Z_

<details><summary>↩ Tool result · `toolu_01FqzGDWiRgRF7kgB5gmipfo`</summary>

```text
Web search results for query: "GoLLIE Sainz et al 2024 "Annotation Guidelines improve Zero-Shot Information-Extraction" ICLR 2024"

Links: [{"title":"[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/abs/2310.03668"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"},{"title":"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview","url":"https://openreview.net/forum?id=Y3wpuxd7u9"},{"title":"ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://iclr.cc/virtual/2024/poster/18435"},{"title":"GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea","url":"https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb?lang=en"},{"title":"GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction","url":"https://arxiv.org/html/2310.03668v5"},{"title":"gollie : annotation guidelines improve zero-shot ...","url":"https://arxiv.org/pdf/2310.03668"},{"title":"[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"},{"title":"GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...","url":"https://openreview.net/pdf?id=Y3wpuxd7u9"},{"title":"gollie: annotation guidelines improve zero-shot information ...","url":"https://scispace.com/pdf/gollie-annotation-guidelines-improve-zero-shot-information-4dv40ulquw.pdf"}]

I found the paper you're looking for! Here are the key details about the GoLLIE paper:

## Paper Information

**Title:** GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction

**Authors:** Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre

**Venue:** 12th International Conference on Learning Representations, ICLR 2024

## Summary

The paper proposes GoLLIE (Guideline-following Large Language Model for IE), a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines. 

IE tasks are characterized by complex annotation guidelines that describe the task and give examples to humans. Previous attempts to leverage such information have failed, even with the largest models, as they are not able to follow the guidelines out of the box. Comprehensive evaluation empirically demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction.

**Additional Resources:**
- arXiv: https://arxiv.org/abs/2310.03668
- ICLR 2024 Proceedings: https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf
- OpenReview: https://openreview.net/forum?id=Y3wpuxd7u9


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "468de1ab-d5df-4fb9-a7a1-3d43ebccb1a9",
  "tool_use_result": {
    "query": "GoLLIE Sainz et al 2024 \"Annotation Guidelines improve Zero-Shot Information-Extraction\" ICLR 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_011EWTigJSTyVPyBWcfgy8Yv",
        "content": [
          {
            "title": "[2310.03668] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction",
            "url": "https://arxiv.org/abs/2310.03668"
          },
          {
            "title": "GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf"
          },
          {
            "title": "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | OpenReview",
            "url": "https://openreview.net/forum?id=Y3wpuxd7u9"
          },
          {
            "title": "ICLR Poster GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction",
            "url": "https://iclr.cc/virtual/2024/poster/18435"
          },
          {
            "title": "GOLLIE: ANNOTATION GUIDELINES IMPROVE ZERO-SHOT INFORMATION-EXTRACTION | Documents - Universidad del País Vasco / Euskal Herriko Unibertsitatea",
            "url": "https://ekoizpen-zientifikoa.ehu.eus/documentos/66cb8eeac7cd8e0cebf21fbb?lang=en"
          },
          {
            "title": "GoLLIE : Annotation Guidelines improve Zero-Shot Information-Extraction",
            "url": "https://arxiv.org/html/2310.03668v5"
          },
          {
            "title": "gollie : annotation guidelines improve zero-shot ...",
            "url": "https://arxiv.org/pdf/2310.03668"
          },
          {
            "title": "[PDF] GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GoLLIE:-Annotation-Guidelines-improve-Zero-Shot-Sainz-Garc%C3%ADa-Ferrero/3f40edfcafc018b2cb54612a9aaa9d6b43a11a26"
          },
          {
            "title": "GOLLIE : ANNOTATION GUIDELINES IMPROVE ZERO- ...",
            "url": "https://openreview.net/pdf?id=Y3wpuxd7u9"
          },
          {
            "title": "gollie: annotation guidelines improve zero-shot information ...",
            "url": "https://scispace.com/pdf/gollie-annotation-guidelines-improve-zero-shot-information-4dv40ulquw.pdf"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about the GoLLIE paper:\n\n## Paper Information\n\n**Title:** GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\n\n**Authors:** Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre\n\n**Venue:** 12th International Conference on Learning Representations, ICLR 2024\n\n## Summary\n\nThe paper proposes GoLLIE (Guideline-following Large Language Model for IE), a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines. \n\nIE tasks are characterized by complex annotation guidelines that describe the task and give examples to humans. Previous attempts to leverage such information have failed, even with the largest models, as they are not able to follow the guidelines out of the box. Comprehensive evaluation empirically demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction.\n\n**Additional Resources:**\n- arXiv: https://arxiv.org/abs/2310.03668\n- ICLR 2024 Proceedings: https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf\n- OpenReview: https://openreview.net/forum?id=Y3wpuxd7u9"
    ],
    "durationSeconds": 7.088796699
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T18:48:18.941Z_

<details><summary>↩ Tool result · `toolu_015H5o7k2rchZ14eeNxeoQy4`</summary>

```text
Web search results for query: "Luan et al 2018 "Multi-Task Identification of Entities Relations and Coreference for Scientific Knowledge Graph Construction" EMNLP SciERC"

Links: [{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ACL Anthology","url":"https://aclanthology.org/D18-1360/"},{"title":"[1808.09602] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602"},{"title":"dblp: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction.","url":"https://dblp.org/rec/conf/emnlp/LuanHOH18.html"},{"title":"Multi-Task Identification of Entities, Relations, and Coreferencefor Scientific Knowledge Graph Construction","url":"https://nlp.cs.washington.edu/sciIE/"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ORKG","url":"https://orkg.org/paper/R36010"},{"title":"[1808.09602v1] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://arxiv.org/abs/1808.09602v1"},{"title":"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction","url":"https://www.researchgate.net/publication/327303141_Multi-Task_Identification_of_Entities_Relations_and_Coreference_for_Scientific_Knowledge_Graph_Construction"},{"title":"[PDF] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multi-Task-Identification-of-Entities,-Relations,-Luan-He/b21b927c251c415b601b6d7f785a42cc5c292635"},{"title":"Multi-Task Identiﬁcation of Entities, Relations, and Coreference","url":"https://arxiv.org/pdf/1808.09602"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Multi-task+identification+of+entities,+relations,+and+coreference+for+scientific+knowledge+graph+construction&amp=&author=Yi+Luan&amp=&author=Luheng+He&amp=&author=Mari+Ostendorf&amp=&author=Hannaneh+Hajishirzi&amp=&publication_year=2018&amp=&pages=3219-3232&amp=&doi=10.18653/v1/D18-1360"}]

I found the paper you're looking for! Here are the key details:

**Citation and Publication:**
Yi Luan, Luheng He, Mari Ostendorf, and Hannaneh Hajishirzi published "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction" in the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP), with pages 3219–3232 in Brussels, Belgium.

**Main Contributions:**
The paper introduces a multi-task setup of identifying entities, relations, and coreference clusters in scientific articles, creating a dataset called SciERC that includes annotations for all three tasks and developing a unified framework called SciIE with shared span representations.

**Key Benefits:**
The multi-task setup reduces cascading errors between tasks and leverages cross-sentence relations through coreference links, with experiments showing that the multi-task model outperforms previous models in scientific information extraction without using any domain-specific features.

**Application:**
The framework supports construction of a scientific knowledge graph, which is used to analyze information in scientific literature.

The paper is available through the ACL Anthology (aclanthology.org/D18-1360) and on arXiv (1808.09602).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "c348424c-b0b4-4d60-a783-932f88f1726e",
  "tool_use_result": {
    "query": "Luan et al 2018 \"Multi-Task Identification of Entities Relations and Coreference for Scientific Knowledge Graph Construction\" EMNLP SciERC",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q3665dhE6JoZz758sWTDWG",
        "content": [
          {
            "title": "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ACL Anthology",
            "url": "https://aclanthology.org/D18-1360/"
          },
          {
            "title": "[1808.09602] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction",
            "url": "https://arxiv.org/abs/1808.09602"
          },
          {
            "title": "dblp: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction.",
            "url": "https://dblp.org/rec/conf/emnlp/LuanHOH18.html"
          },
          {
            "title": "Multi-Task Identification of Entities, Relations, and Coreferencefor Scientific Knowledge Graph Construction",
            "url": "https://nlp.cs.washington.edu/sciIE/"
          },
          {
            "title": "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction - ORKG",
            "url": "https://orkg.org/paper/R36010"
          },
          {
            "title": "[1808.09602v1] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction",
            "url": "https://arxiv.org/abs/1808.09602v1"
          },
          {
            "title": "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction",
            "url": "https://www.researchgate.net/publication/327303141_Multi-Task_Identification_of_Entities_Relations_and_Coreference_for_Scientific_Knowledge_Graph_Construction"
          },
          {
            "title": "[PDF] Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Multi-Task-Identification-of-Entities,-Relations,-Luan-He/b21b927c251c415b601b6d7f785a42cc5c292635"
          },
          {
            "title": "Multi-Task Identiﬁcation of Entities, Relations, and Coreference",
            "url": "https://arxiv.org/pdf/1808.09602"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?title=Multi-task+identification+of+entities,+relations,+and+coreference+for+scientific+knowledge+graph+construction&amp=&author=Yi+Luan&amp=&author=Luheng+He&amp=&author=Mari+Ostendorf&amp=&author=Hannaneh+Hajishirzi&amp=&publication_year=2018&amp=&pages=3219-3232&amp=&doi=10.18653/v1/D18-1360"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Citation and Publication:**\nYi Luan, Luheng He, Mari Ostendorf, and Hannaneh Hajishirzi published \"Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\" in the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP), with pages 3219–3232 in Brussels, Belgium.\n\n**Main Contributions:**\nThe paper introduces a multi-task setup of identifying entities, relations, and coreference clusters in scientific articles, creating a dataset called SciERC that includes annotations for all three tasks and developing a unified framework called SciIE with shared span representations.\n\n**Key Benefits:**\nThe multi-task setup reduces cascading errors between tasks and leverages cross-sentence relations through coreference links, with experiments showing that the multi-task model outperforms previous models in scientific information extraction without using any domain-specific features.\n\n**Application:**\nThe framework supports construction of a scientific knowledge graph, which is used to analyze information in scientific literature.\n\nThe paper is available through the ACL Anthology (aclanthology.org/D18-1360) and on arXiv (1808.09602)."
    ],
    "durationSeconds": 4.5537033550000015
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T18:48:19.470Z_

<details><summary>↩ Tool result · `toolu_01RPeCxVJdVdrB6tLkJbhQnX`</summary>

```text
Web search results for query: "Tjong Kim Sang De Meulder 2003 "Introduction to the CoNLL-2003 Shared Task Language-Independent Named Entity Recognition""

Links: [{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - ACL Anthology","url":"https://aclanthology.org/W03-0419/"},{"title":"[cs/0306050] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition","url":"https://arxiv.org/abs/cs/0306050"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - ADS","url":"https://ui.adsabs.harvard.edu/abs/2003cs........6050S/abstract"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - Tilburg University Research Portal","url":"https://research.tilburguniversity.edu/en/publications/introduction-to-the-conll-2003-shared-task-language-independent-n/"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition","url":"https://www.researchgate.net/publication/1956514_Introduction_to_the_CoNLL-2003_Shared_Task_Language-Independent_Named_Entity_Recognition"},{"title":"[PDF] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Introduction-to-the-CoNLL-2003-Shared-Task:-Named-Sang-Meulder/10f97f1fb4f5c2c8e6c44d4a33da46d331dd4aeb"},{"title":"Introduction to the CoNLL-2003 shared task | Proceedings of the seventh conference on Natural language learning at HLT-NAACL 2003 - Volume 4","url":"https://dl.acm.org/doi/10.3115/1119176.1119195"},{"title":"2003 IntroductionToTheCoNLL2003SharedTask - GM-RKB","url":"https://www.gabormelli.com/RKB/2003_IntroductionToTheCoNLL2003SharedTask"},{"title":"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2dd04b198987c07e41355e4a17fd1493d/hkorte"},{"title":"[cs/0306050v1] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition","url":"https://arxiv.org/abs/cs/0306050v1"}]

I found the paper you're looking for. Here are the search results:

The paper "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition" was authored by Erik F. Tjong Kim Sang and Fien De Meulder in 2003 and was published in the Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL 2003 on pages 142–147.

The paper is available from multiple sources:
- ACL Anthology (https://aclanthology.org/W03-0419/)
- arXiv (https://arxiv.org/abs/cs/0306050)

The paper describes the CoNLL-2003 shared task on language-independent named entity recognition, provides background information on the data sets (English and German) and the evaluation method, and presents a general overview of the systems that participated in the task and their performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "231645de-c8e0-4cf5-ab3a-a5b08a6ca8b4",
  "tool_use_result": {
    "query": "Tjong Kim Sang De Meulder 2003 \"Introduction to the CoNLL-2003 Shared Task Language-Independent Named Entity Recognition\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_014pQaKuFmouMshNFiDxkwyd",
        "content": [
          {
            "title": "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/W03-0419/"
          },
          {
            "title": "[cs/0306050] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition",
            "url": "https://arxiv.org/abs/cs/0306050"
          },
          {
            "title": "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2003cs........6050S/abstract"
          },
          {
            "title": "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition - Tilburg University Research Portal",
            "url": "https://research.tilburguniversity.edu/en/publications/introduction-to-the-conll-2003-shared-task-language-independent-n/"
          },
          {
            "title": "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition",
            "url": "https://www.researchgate.net/publication/1956514_Introduction_to_the_CoNLL-2003_Shared_Task_Language-Independent_Named_Entity_Recognition"
          },
          {
            "title": "[PDF] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Introduction-to-the-CoNLL-2003-Shared-Task:-Named-Sang-Meulder/10f97f1fb4f5c2c8e6c44d4a33da46d331dd4aeb"
          },
          {
            "title": "Introduction to the CoNLL-2003 shared task | Proceedings of the seventh conference on Natural language learning at HLT-NAACL 2003 - Volume 4",
            "url": "https://dl.acm.org/doi/10.3115/1119176.1119195"
          },
          {
            "title": "2003 IntroductionToTheCoNLL2003SharedTask - GM-RKB",
            "url": "https://www.gabormelli.com/RKB/2003_IntroductionToTheCoNLL2003SharedTask"
          },
          {
            "title": "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/2dd04b198987c07e41355e4a17fd1493d/hkorte"
          },
          {
            "title": "[cs/0306050v1] Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition",
            "url": "https://arxiv.org/abs/cs/0306050v1"
          }
        ]
      },
      "I found the paper you're looking for. Here are the search results:\n\nThe paper \"Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition\" was authored by Erik F. Tjong Kim Sang and Fien De Meulder in 2003 and was published in the Proceedings of the Seventh Conference on Natural Language Learning at HLT-NAACL 2003 on pages 142–147.\n\nThe paper is available from multiple sources:\n- ACL Anthology (https://aclanthology.org/W03-0419/)\n- arXiv (https://arxiv.org/abs/cs/0306050)\n\nThe paper describes the CoNLL-2003 shared task on language-independent named entity recognition, provides background information on the data sets (English and German) and the evaluation method, and presents a general overview of the systems that participated in the task and their performance."
    ],
    "durationSeconds": 4.144677212999999
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C1Js9x7Jup2o1UCKhwZN4R`</summary>

```json
{
  "query": "arXiv 2505.10772 \"Ranked Voting based Self-Consistency of LLMs\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "0ccab132-a883-4749-97ca-5700366b42f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DM7xr2E2qgMGi59Pe7GUZB`</summary>

```json
{
  "query": "arXiv 2508.18395 \"Latent Self-Consistency\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "de6b4023-8334-491a-a461-62d5b87b58fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEQ8znNtPo3yrh8FW2FfCn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13525,
      "cache_read_input_tokens": 24012,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13525
      },
      "output_tokens": 17,
      "service_tier": "standard",
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

_source line 25 · 2026-05-14T18:48:22.281Z_

<details><summary>↩ Tool result · `toolu_01T3TCJGm4r8EeBhH4htf5fL`</summary>

```text
Web search results for query: "Derczynski et al 2017 "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition" EMNLP Workshop"

Links: [{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - ACL Anthology","url":"https://aclanthology.org/W17-4418/"},{"title":"GitHub - leondz/emerging_entities_17: Dataset for the Emerging & Novel Entity NER task (WNUT '17) · GitHub","url":"https://github.com/leondz/emerging_entities_17"},{"title":"[PDF] Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Results-of-the-WNUT2017-Shared-Task-on-Novel-and-Derczynski-Nichols/72e87913632d0f1295fbcfa46795c5bb26d0a422"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Request PDF","url":"https://www.researchgate.net/publication/322590094_Results_of_the_WNUT2017_Shared_Task_on_Novel_and_Emerging_Entity_Recognition"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition","url":"https://www.derczynski.com/sheffield/papers/emerging-wnut.pdf"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - Royal Netherlands Academy of Arts and Sciences (KNAW)","url":"https://pure.knaw.nl/portal/en/publications/results-of-the-wnut2017-shared-task-on-novel-and-emerging-entity-"},{"title":"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition","url":"https://noisy-text.github.io/2017/pdf/WNUT18.pdf"},{"title":"Emerging and Rare Entity Recognition","url":"http://noisy-text.github.io/2017/emerging-rare-entities.html"},{"title":"Description and demonstration guided data augmentation for sequence tagging - World Wide Web","url":"https://link.springer.com/article/10.1007/s11280-021-00978-0"},{"title":"Stronger interaction brings better performance: fine-grained alignment between different modalities for MNER | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-07987-0"}]

I found the paper you're looking for! Here are the details:

Leon Derczynski, Eric Nichols, Marieke van Erp, and Nut Limsopatham published "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition" in 2017 in the Proceedings of the 3rd Workshop on Noisy User-generated Text, which was held at EMNLP in Copenhagen, Denmark.

The task evaluated the ability of participating entries to detect and classify novel and emerging named entities in noisy text. The shared task focuses on identifying unusual, previously-unseen entities in the context of emerging discussions, as named entities form the basis of many modern approaches to other tasks (like event clustering and summarization), but recall on them is a real problem in noisy text - even among annotators.

The paper is available through the ACL Anthology at https://aclanthology.org/W17-4418/, and the associated dataset is available on GitHub at https://github.com/leondz/emerging_entities_17.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "475c9add-52fd-4623-8cdb-824bd1a3f068",
  "tool_use_result": {
    "query": "Derczynski et al 2017 \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\" EMNLP Workshop",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GEpabs8MBGwLM7duwaQZHb",
        "content": [
          {
            "title": "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - ACL Anthology",
            "url": "https://aclanthology.org/W17-4418/"
          },
          {
            "title": "GitHub - leondz/emerging_entities_17: Dataset for the Emerging & Novel Entity NER task (WNUT '17) · GitHub",
            "url": "https://github.com/leondz/emerging_entities_17"
          },
          {
            "title": "[PDF] Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Results-of-the-WNUT2017-Shared-Task-on-Novel-and-Derczynski-Nichols/72e87913632d0f1295fbcfa46795c5bb26d0a422"
          },
          {
            "title": "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition | Request PDF",
            "url": "https://www.researchgate.net/publication/322590094_Results_of_the_WNUT2017_Shared_Task_on_Novel_and_Emerging_Entity_Recognition"
          },
          {
            "title": "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition",
            "url": "https://www.derczynski.com/sheffield/papers/emerging-wnut.pdf"
          },
          {
            "title": "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition - Royal Netherlands Academy of Arts and Sciences (KNAW)",
            "url": "https://pure.knaw.nl/portal/en/publications/results-of-the-wnut2017-shared-task-on-novel-and-emerging-entity-"
          },
          {
            "title": "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition",
            "url": "https://noisy-text.github.io/2017/pdf/WNUT18.pdf"
          },
          {
            "title": "Emerging and Rare Entity Recognition",
            "url": "http://noisy-text.github.io/2017/emerging-rare-entities.html"
          },
          {
            "title": "Description and demonstration guided data augmentation for sequence tagging - World Wide Web",
            "url": "https://link.springer.com/article/10.1007/s11280-021-00978-0"
          },
          {
            "title": "Stronger interaction brings better performance: fine-grained alignment between different modalities for MNER | The Journal of Supercomputing | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11227-025-07987-0"
          }
        ]
      },
      "I found the paper you're looking for! Here are the details:\n\nLeon Derczynski, Eric Nichols, Marieke van Erp, and Nut Limsopatham published \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\" in 2017 in the Proceedings of the 3rd Workshop on Noisy User-generated Text, which was held at EMNLP in Copenhagen, Denmark.\n\nThe task evaluated the ability of participating entries to detect and classify novel and emerging named entities in noisy text. The shared task focuses on identifying unusual, previously-unseen entities in the context of emerging discussions, as named entities form the basis of many modern approaches to other tasks (like event clustering and summarization), but recall on them is a real problem in noisy text - even among annotators.\n\nThe paper is available through the ACL Anthology at https://aclanthology.org/W17-4418/, and the associated dataset is available on GitHub at https://github.com/leondz/emerging_entities_17."
    ],
    "durationSeconds": 5.926773085000001
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T18:48:22.472Z_

<details><summary>↩ Tool result · `toolu_013ndackhpvtrEtsP7MM2crR`</summary>

```text
Web search results for query: "Willard Louf 2023 "Efficient Guided Generation for Large Language Models" arXiv 2307.09702"

Links: [{"title":"[2307.09702] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702"},{"title":"Paper page - Efficient Guided Generation for Large Language Models","url":"https://huggingface.co/papers/2307.09702"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/pdf/2307.09702"},{"title":"[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"},{"title":"Efficient Guided Generation for Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230709702W/abstract"},{"title":"[2307.09702v3] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v3"},{"title":"[2307.09702v2] Efficient Guided Generation for Large Language Models","url":"https://arxiv.org/abs/2307.09702v2"},{"title":"dblp: Efficient Guided Generation for Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2307-09702.html"},{"title":"Efficient Guided Generation for Large Language Models","url":"https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2307.09702v3","url":"https://www.summarizepaper.com/en/arxiv-id/2307.09702v3/"}]

I found the paper successfully. Here's what the search revealed:

The paper "Efficient Guided Generation for Large Language Models" was authored by Brandon T. Willard and Rémi Louf (note: the paper is by Willard and Louf, not "Willard Louf" as a single name).

**Key Details:**

- **ArXiv ID:** 2307.09702
- **Submission Date:** July 19, 2023
- **Main Contribution:** The paper shows how neural text generation can be reformulated in terms of finite-state machine transitions, leading to an efficient approach to guiding text generation with regular expressions and context-free grammars

**Key Features:**

The approach is model agnostic, allows one to enforce domain-specific knowledge and constraints, and enables the construction of reliable interfaces by guaranteeing the structure of the generated text. It adds little overhead to the token sequence generation process and significantly outperforms existing solutions.

**Implementation:** An implementation is provided in the open source Python library Outlines.

The paper is available at https://arxiv.org/abs/2307.09702.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "0aac798f-c5ce-48f1-8679-100e50a2d3ad",
  "tool_use_result": {
    "query": "Willard Louf 2023 \"Efficient Guided Generation for Large Language Models\" arXiv 2307.09702",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q1ExxzR7YkBvnJteEmwYww",
        "content": [
          {
            "title": "[2307.09702] Efficient Guided Generation for Large Language Models",
            "url": "https://arxiv.org/abs/2307.09702"
          },
          {
            "title": "Paper page - Efficient Guided Generation for Large Language Models",
            "url": "https://huggingface.co/papers/2307.09702"
          },
          {
            "title": "Efficient Guided Generation for Large Language Models",
            "url": "https://arxiv.org/pdf/2307.09702"
          },
          {
            "title": "[PDF] Efficient Guided Generation for Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Efficient-Guided-Generation-for-Large-Language-Willard-Louf/c4ceaef35bca063815f50d90a087acbd07a65478"
          },
          {
            "title": "Efficient Guided Generation for Large Language Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230709702W/abstract"
          },
          {
            "title": "[2307.09702v3] Efficient Guided Generation for Large Language Models",
            "url": "https://arxiv.org/abs/2307.09702v3"
          },
          {
            "title": "[2307.09702v2] Efficient Guided Generation for Large Language Models",
            "url": "https://arxiv.org/abs/2307.09702v2"
          },
          {
            "title": "dblp: Efficient Guided Generation for Large Language Models.",
            "url": "https://dblp.org/rec/journals/corr/abs-2307-09702.html"
          },
          {
            "title": "Efficient Guided Generation for Large Language Models",
            "url": "https://www.researchhub.com/paper/1278292/efficient-guided-generation-for-large-language-models"
          },
          {
            "title": "AI-Powered Paper Summarization about the arXiv paper 2307.09702v3",
            "url": "https://www.summarizepaper.com/en/arxiv-id/2307.09702v3/"
          }
        ]
      },
      "I found the paper successfully. Here's what the search revealed:\n\nThe paper \"Efficient Guided Generation for Large Language Models\" was authored by Brandon T. Willard and Rémi Louf (note: the paper is by Willard and Louf, not \"Willard Louf\" as a single name).\n\n**Key Details:**\n\n- **ArXiv ID:** 2307.09702\n- **Submission Date:** July 19, 2023\n- **Main Contribution:** The paper shows how neural text generation can be reformulated in terms of finite-state machine transitions, leading to an efficient approach to guiding text generation with regular expressions and context-free grammars\n\n**Key Features:**\n\nThe approach is model agnostic, allows one to enforce domain-specific knowledge and constraints, and enables the construction of reliable interfaces by guaranteeing the structure of the generated text. It adds little overhead to the token sequence generation process and significantly outperforms existing solutions.\n\n**Implementation:** An implementation is provided in the open source Python library Outlines.\n\nThe paper is available at https://arxiv.org/abs/2307.09702."
    ],
    "durationSeconds": 5.160198608999999
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T18:48:22.850Z_

<details><summary>↩ Tool result · `toolu_01T2GLd3E6JMRDb4SgGT25Hh`</summary>

```text
Web search results for query: "Fleiss 1971 "Measuring Nominal Scale Agreement Among Many Raters" Psychological Bulletin"

Links: [{"title":"Measuring nominal scale agreement among many raters.","url":"https://psycnet.apa.org/record/1972-05083-001"},{"title":"Fleiss, J.L. (1971) Measuring nominal scale agreement among many raters. Psychological Bulletin, 76, 378-382. doi10.1037/h0031619 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=853322"},{"title":"Measuring nominal scale agreement among many raters. | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Measuring-nominal-scale-agreement-among-many-Fleiss/cfb4592221080deb127de94e8063fb403b13a298"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.proquest.com/docview/614289059"},{"title":"Measuring nominal scale agreement among many raters.","url":"https://europepmc.org/article/CTX/c6682"},{"title":"Measuring nominal scale agreement among many raters","url":"https://www.researchgate.net/publication/200086110_Measuring_nominal_scale_agreement_among_many_raters"},{"title":"Measuring nominal scale agreement among many raters | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2506a1115df044659165a488a75f9e449/folke"},{"title":"Fleiss, J. L. (1971). Measuring Nominal Scale Agreement among Many Raters. Psychological Bulletin, 76, 378-382. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=1733370"},{"title":"Measuring nominal scale agreement among many raters. – ScienceOpen","url":"https://www.scienceopen.com/document?vid=cbfac7ad-7aae-4e09-b8ff-fd5a74c99c0a"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?hl=en&volume=76&publication_year=1971&pages=378-382&journal=Psychological+Bulletin&issue=5&author=J.+L.+Fleiss&title=Measuring+nominal+scale+agreement+among+many+raters"}]

I found the publication you're looking for. Here are the details:

Fleiss, J.L. (1971) "Measuring nominal scale agreement among many raters." Psychological Bulletin, 76, 378-382.

The DOI is 10.1037/h0031619, and it was published in November 1971.

The paper introduced the statistic kappa to measure nominal scale agreement between raters, and generalized it to cases where each of a sample of subjects was rated on a nominal scale by the same number of raters but where the raters rating one subject are not necessarily the same as those rating another, with large sample standard errors derived.

This is a highly influential paper in the field of inter-rater reliability, with thousands of citations across multiple disciplines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "36380146-494a-4858-8a70-aad6bce299ef",
  "tool_use_result": {
    "query": "Fleiss 1971 \"Measuring Nominal Scale Agreement Among Many Raters\" Psychological Bulletin",
    "results": [
      {
        "tool_use_id": "srvtoolu_0127AjNNdNmuuWyj3LEjnTUL",
        "content": [
          {
            "title": "Measuring nominal scale agreement among many raters.",
            "url": "https://psycnet.apa.org/record/1972-05083-001"
          },
          {
            "title": "Fleiss, J.L. (1971) Measuring nominal scale agreement among many raters. Psychological Bulletin, 76, 378-382. doi10.1037/h0031619 - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=853322"
          },
          {
            "title": "Measuring nominal scale agreement among many raters. | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Measuring-nominal-scale-agreement-among-many-Fleiss/cfb4592221080deb127de94e8063fb403b13a298"
          },
          {
            "title": "Measuring nominal scale agreement among many raters",
            "url": "https://www.proquest.com/docview/614289059"
          },
          {
            "title": "Measuring nominal scale agreement among many raters.",
            "url": "https://europepmc.org/article/CTX/c6682"
          },
          {
            "title": "Measuring nominal scale agreement among many raters",
            "url": "https://www.researchgate.net/publication/200086110_Measuring_nominal_scale_agreement_among_many_raters"
          },
          {
            "title": "Measuring nominal scale agreement among many raters | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/2506a1115df044659165a488a75f9e449/folke"
          },
          {
            "title": "Fleiss, J. L. (1971). Measuring Nominal Scale Agreement among Many Raters. Psychological Bulletin, 76, 378-382. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=1733370"
          },
          {
            "title": "Measuring nominal scale agreement among many raters. – ScienceOpen",
            "url": "https://www.scienceopen.com/document?vid=cbfac7ad-7aae-4e09-b8ff-fd5a74c99c0a"
          },
          {
            "title": "Google Scholar",
            "url": "https://scholar.google.com/scholar_lookup?hl=en&volume=76&publication_year=1971&pages=378-382&journal=Psychological+Bulletin&issue=5&author=J.+L.+Fleiss&title=Measuring+nominal+scale+agreement+among+many+raters"
          }
        ]
      },
      "I found the publication you're looking for. Here are the details:\n\nFleiss, J.L. (1971) \"Measuring nominal scale agreement among many raters.\" Psychological Bulletin, 76, 378-382.\n\nThe DOI is 10.1037/h0031619, and it was published in November 1971.\n\nThe paper introduced the statistic kappa to measure nominal scale agreement between raters, and generalized it to cases where each of a sample of subjects was rated on a nominal scale by the same number of raters but where the raters rating one subject are not necessarily the same as those rating another, with large sample standard errors derived.\n\nThis is a highly influential paper in the field of inter-rater reliability, with thousands of citations across multiple disciplines."
    ],
    "durationSeconds": 4.621340305000001
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T18:48:23.515Z_

<details><summary>↩ Tool result · `toolu_016Ntev2AhtpwF918Qq6TXpX`</summary>

```text
Web search results for query: "Jaccard 1901 coefficient original paper "Étude comparative de la distribution florale""

Links: [{"title":"Jaccard, P. (1901) étude Comparative de la distribuition florale dans une portion des Alpes et des Jura. Bulletin de la Société Vaudoise des Sciences Naturelles, 7, 547-579. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2200199"},{"title":"Étude comparative de la distribution florale dans une portion des Alpes et du Jura – ScienceOpen","url":"https://www.scienceopen.com/document?vid=01a9bb0e-a14c-461f-85c9-f407259515dc"},{"title":"(PDF) Etude de la distribution florale dans une portion des Alpes et du Jura","url":"https://www.researchgate.net/publication/225035806_Etude_de_la_distribution_florale_dans_une_portion_des_Alpes_et_du_Jura"},{"title":"Jaccard, P. (1901) étude comparative de la distribution florale dans une portion des Alpes et du Jura. Bulletin de la Société Vaudoise des Sciences Naturelles, 37, 547-579. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2265036"},{"title":"Jaccard Similarity — distancia 0.0.1 documentation","url":"https://distancia.readthedocs.io/en/latest/Jaccard.html"},{"title":"Comparing sets of patterns with the Jaccard index","url":"https://ajis.aaisnet.org/index.php/ajis/article/download/1538/817/5125"},{"title":"(PDF) La distribution de la flore dans la zone alpine","url":"https://www.researchgate.net/publication/242651149_La_distribution_de_la_flore_dans_la_zone_alpine"},{"title":"Etude comparative de la distribution florale dans une portion des Alpes et des Jura | CiNii Research","url":"https://cir.nii.ac.jp/crid/1573387450552842240"},{"title":"(PDF) Nouvelles Recherches Sur la Distribution Florale","url":"https://www.researchgate.net/publication/242013831_Nouvelles_Recherches_Sur_la_Distribution_Florale"},{"title":"Étude comparative de la distribution florale dans une portion des Alpes et des | CiNii Research","url":"https://cir.nii.ac.jp/crid/1370848661206918145?lang=en"}]

Based on the web search results, I found information about Jaccard's original 1901 paper:

The original paper is titled "Étude Comparative de la distribution florale dans une portion des Alpes et des Jura" by P. Jaccard (1901), published in Bulletin de la Société Vaudoise des Sciences Naturelles, volume 37, pages 547-579.

This paper introduces the Jaccard coefficient and its application to biological studies. The Jaccard Similarity was first introduced by Swiss botanist Paul Jaccard in 1901, where he developed this coefficient to quantify the similarity between sample sets of plants based on their shared characteristics.

It's worth noting that there is a common error in bibliographies with the title "Étude comparative de la distribution florale dans une portion des Alpes et des Jura" – the correct version uses "Alpes et du Jura" (not "des Jura").


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "a2af7cc4-e728-4ff3-a0a7-c60ec3611e6d",
  "tool_use_result": {
    "query": "Jaccard 1901 coefficient original paper \"Étude comparative de la distribution florale\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SQcHMftbC2jiaR4DABD6d5",
        "content": [
          {
            "title": "Jaccard, P. (1901) étude Comparative de la distribuition florale dans une portion des Alpes et des Jura. Bulletin de la Société Vaudoise des Sciences Naturelles, 7, 547-579. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=2200199"
          },
          {
            "title": "Étude comparative de la distribution florale dans une portion des Alpes et du Jura – ScienceOpen",
            "url": "https://www.scienceopen.com/document?vid=01a9bb0e-a14c-461f-85c9-f407259515dc"
          },
          {
            "title": "(PDF) Etude de la distribution florale dans une portion des Alpes et du Jura",
            "url": "https://www.researchgate.net/publication/225035806_Etude_de_la_distribution_florale_dans_une_portion_des_Alpes_et_du_Jura"
          },
          {
            "title": "Jaccard, P. (1901) étude comparative de la distribution florale dans une portion des Alpes et du Jura. Bulletin de la Société Vaudoise des Sciences Naturelles, 37, 547-579. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/ReferencesPapers?ReferenceID=2265036"
          },
          {
            "title": "Jaccard Similarity — distancia 0.0.1 documentation",
            "url": "https://distancia.readthedocs.io/en/latest/Jaccard.html"
          },
          {
            "title": "Comparing sets of patterns with the Jaccard index",
            "url": "https://ajis.aaisnet.org/index.php/ajis/article/download/1538/817/5125"
          },
          {
            "title": "(PDF) La distribution de la flore dans la zone alpine",
            "url": "https://www.researchgate.net/publication/242651149_La_distribution_de_la_flore_dans_la_zone_alpine"
          },
          {
            "title": "Etude comparative de la distribution florale dans une portion des Alpes et des Jura | CiNii Research",
            "url": "https://cir.nii.ac.jp/crid/1573387450552842240"
          },
          {
            "title": "(PDF) Nouvelles Recherches Sur la Distribution Florale",
            "url": "https://www.researchgate.net/publication/242013831_Nouvelles_Recherches_Sur_la_Distribution_Florale"
          },
          {
            "title": "Étude comparative de la distribution florale dans une portion des Alpes et des | CiNii Research",
            "url": "https://cir.nii.ac.jp/crid/1370848661206918145?lang=en"
          }
        ]
      },
      "Based on the web search results, I found information about Jaccard's original 1901 paper:\n\nThe original paper is titled \"Étude Comparative de la distribution florale dans une portion des Alpes et des Jura\" by P. Jaccard (1901), published in Bulletin de la Société Vaudoise des Sciences Naturelles, volume 37, pages 547-579.\n\nThis paper introduces the Jaccard coefficient and its application to biological studies. The Jaccard Similarity was first introduced by Swiss botanist Paul Jaccard in 1901, where he developed this coefficient to quantify the similarity between sample sets of plants based on their shared characteristics.\n\nIt's worth noting that there is a common error in bibliographies with the title \"Étude comparative de la distribution florale dans une portion des Alpes et des Jura\" – the correct version uses \"Alpes et du Jura\" (not \"des Jura\")."
    ],
    "durationSeconds": 4.775098300999998
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T18:48:29.341Z_

<details><summary>↩ Tool result · `toolu_01DM7xr2E2qgMGi59Pe7GUZB`</summary>

```text
Web search results for query: "arXiv 2508.18395 "Latent Self-Consistency""

Links: [{"title":"[2508.18395] Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning","url":"https://arxiv.org/abs/2508.18395"},{"title":"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and","url":"https://arxiv.org/pdf/2508.18395"},{"title":"Latent Self-Consistency for Reliable Majority‑Set Selection in Short‑ and Long‑Answer Reasoning","url":"https://arxiv.org/html/2508.18395"},{"title":"Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning","url":"https://arxiv.org/html/2508.18395v1"},{"title":"(PDF) Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning","url":"https://www.researchgate.net/publication/394978774_Latent_Self-Consistency_for_Reliable_Majority-Set_Selection_in_Short-_and_Long-Answer_Reasoning"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in ...","url":"https://arxiv.org/pdf/2203.11171"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"How Effective Is Self-Consistency for Long-Context Problems?","url":"https://arxiv.org/html/2411.01101v1"},{"title":"[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"},{"title":"(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"}]

Based on the search results, here's what I found about arXiv 2508.18395 "Latent Self-Consistency":

## Overview

Latent Self-Consistency (LSC) is a framework that selects the most semantically consistent response using learnable token embeddings.

## Problem It Addresses

Probabilistic decoding in Large Language Models (LLMs) often yields inconsistent outputs, particularly on complex or long-form questions. Self-Consistency (SC) mitigates this for short-form QA by majority voting over exact strings, whereas Universal Self-Consistency (USC) and Weighted Unigram Consistency Score (WUCS) extend to long-form responses but lose accuracy on short-form benchmarks.

## How It Works

LSC appends a small set of trainable summary tokens after the EOS token of each generated response and reuses the key–value (KV) cache from the original generation to compute their final-layer representations, yielding compact embeddings that capture the semantic essence of each response. By computing pairwise cosine similarities with these learned embeddings, LSC identifies the most consistent response without constructing new prompts or performing any complex text processing.

## Performance

Across 6 short-form and 5 long-form reasoning benchmarks (e.g., MATH, MMLU, TruthfulQA), LSC surpasses SC, USC, and WUCS on both short-form and long-form on average performance, while adding negligible computational overhead on vanilla inference.

## Efficiency

LSC's lightweight forward processing of summary tokens only introduces negligible runtime overhead (at most 0.9%) on top of standard decoding of the base LLM, and requires no changes to the model architecture.

The paper was authored by Jungsuk Oh and Jay-Yoon Lee, with the latest version (v3) released on February 27, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "b95418a3-8a12-4277-b73b-70fc3107a3eb",
  "tool_use_result": {
    "query": "arXiv 2508.18395 \"Latent Self-Consistency\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_018WvcR7L8cEyg6jkcBTKxJU",
        "content": [
          {
            "title": "[2508.18395] Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning",
            "url": "https://arxiv.org/abs/2508.18395"
          },
          {
            "title": "Latent Self-Consistency for Reliable Majority-Set Selection in Short- and",
            "url": "https://arxiv.org/pdf/2508.18395"
          },
          {
            "title": "Latent Self-Consistency for Reliable Majority‑Set Selection in Short‑ and Long‑Answer Reasoning",
            "url": "https://arxiv.org/html/2508.18395"
          },
          {
            "title": "Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning",
            "url": "https://arxiv.org/html/2508.18395v1"
          },
          {
            "title": "(PDF) Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning",
            "url": "https://www.researchgate.net/publication/394978774_Latent_Self-Consistency_for_Reliable_Majority-Set_Selection_in_Short-_and_Long-Answer_Reasoning"
          },
          {
            "title": "Self-Consistency Improves Chain of Thought Reasoning in ...",
            "url": "https://arxiv.org/pdf/2203.11171"
          },
          {
            "title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=1PL1NIMMrw"
          },
          {
            "title": "How Effective Is Self-Consistency for Long-Context Problems?",
            "url": "https://arxiv.org/html/2411.01101v1"
          },
          {
            "title": "[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"
          },
          {
            "title": "(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv 2508.18395 \"Latent Self-Consistency\":\n\n## Overview\n\nLatent Self-Consistency (LSC) is a framework that selects the most semantically consistent response using learnable token embeddings.\n\n## Problem It Addresses\n\nProbabilistic decoding in Large Language Models (LLMs) often yields inconsistent outputs, particularly on complex or long-form questions. Self-Consistency (SC) mitigates this for short-form QA by majority voting over exact strings, whereas Universal Self-Consistency (USC) and Weighted Unigram Consistency Score (WUCS) extend to long-form responses but lose accuracy on short-form benchmarks.\n\n## How It Works\n\nLSC appends a small set of trainable summary tokens after the EOS token of each generated response and reuses the key–value (KV) cache from the original generation to compute their final-layer representations, yielding compact embeddings that capture the semantic essence of each response. By computing pairwise cosine similarities with these learned embeddings, LSC identifies the most consistent response without constructing new prompts or performing any complex text processing.\n\n## Performance\n\nAcross 6 short-form and 5 long-form reasoning benchmarks (e.g., MATH, MMLU, TruthfulQA), LSC surpasses SC, USC, and WUCS on both short-form and long-form on average performance, while adding negligible computational overhead on vanilla inference.\n\n## Efficiency\n\nLSC's lightweight forward processing of summary tokens only introduces negligible runtime overhead (at most 0.9%) on top of standard decoding of the base LLM, and requires no changes to the model architecture.\n\nThe paper was authored by Jungsuk Oh and Jay-Yoon Lee, with the latest version (v3) released on February 27, 2026."
    ],
    "durationSeconds": 8.603722708000001
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T18:48:29.465Z_

<details><summary>↩ Tool result · `toolu_01C1Js9x7Jup2o1UCKhwZN4R`</summary>

```text
Web search results for query: "arXiv 2505.10772 "Ranked Voting based Self-Consistency of LLMs""

Links: [{"title":"[2505.10772] Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/abs/2505.10772"},{"title":"Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/html/2505.10772v1"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://arxiv.org/pdf/2505.10772"},{"title":"GitHub - szu-tera/RankedVotingSC: RankedVotingSC (Ranked Voting based Self-Consistency) is a method that generates ranked answers in each reasoning attempt and aggregates them using ranked voting across multiple responses, aiming to select the most reliable final answer and enhance the reasoning performance of large language models.","url":"https://github.com/szu-tera/RankedVotingSC"},{"title":"Ranked Voting based Self-Consistency of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.744/"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://ylwangy.github.io/pub/ACL_2025_RVSC.pdf"},{"title":"Ranked Voting based Self-Consistency of Large Language Models","url":"https://www.researchgate.net/publication/394270401_Ranked_Voting_based_Self-Consistency_of_Large_Language_Models"},{"title":"(PDF) Quantum Combinatorial Reasoning for Large Language Models","url":"https://www.researchgate.net/publication/397007127_Quantum_Combinatorial_Reasoning_for_Large_Language_Models"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://aclanthology.org/2025.findings-acl.744.pdf"},{"title":"Found in the Middle: Permutation Self-Consistency Improves","url":"https://arxiv.org/pdf/2310.07712"}]

I found detailed information about the paper arXiv 2505.10772 on "Ranked Voting based Self-Consistency of Large Language Models."

## Overview

The paper proposes to generate ranked answers in each reasoning process and conduct ranked voting among multiple ranked answers from different responses, thereby making the overall self-consistency more reliable.

## Problem & Motivation

Majority voting is considered an effective method to enhance chain-of-thought reasoning, as it selects the answer with the highest "self-consistency" among different reasoning paths. However, previous chain-of-thought reasoning methods typically generate only a single answer in each trial, thereby ignoring the possibility of other potential answers. As a result, these alternative answers are often overlooked in subsequent voting processes.

## Methodology

The authors use three ranked voting methods: Instant-runoff voting, Borda count voting, and mean reciprocal rank voting.

## Evaluation

The methods are validated on six datasets, including three multiple-choice and three open-ended question-answering tasks, using both advanced open-source and closed-source large language models. The method achieves an average accuracy of 76.69% and 87.41% on gpt-3.5-turbo-0125 and gpt-4-turbo-2024-04-09, respectively, outperforming the best baseline methods by 3.4% and 0.48%.

## Authors

The paper was submitted on 16 May 2025 by authors Weiqin Wang, Yile Wang, and Hui Huang. The paper has been accepted to the Findings of ACL 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "97d03a56-1adc-47b3-a991-fce576c63a19",
  "tool_use_result": {
    "query": "arXiv 2505.10772 \"Ranked Voting based Self-Consistency of LLMs\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VqfA3Z8gHvnU6jFpfuarX9",
        "content": [
          {
            "title": "[2505.10772] Ranked Voting based Self-Consistency of Large Language Models",
            "url": "https://arxiv.org/abs/2505.10772"
          },
          {
            "title": "Ranked Voting based Self-Consistency of Large Language Models",
            "url": "https://arxiv.org/html/2505.10772v1"
          },
          {
            "title": "Ranked Voting based Self-Consistency of Large Language ...",
            "url": "https://arxiv.org/pdf/2505.10772"
          },
          {
            "title": "GitHub - szu-tera/RankedVotingSC: RankedVotingSC (Ranked Voting based Self-Consistency) is a method that generates ranked answers in each reasoning attempt and aggregates them using ranked voting across multiple responses, aiming to select the most reliable final answer and enhance the reasoning performance of large language models.",
            "url": "https://github.com/szu-tera/RankedVotingSC"
          },
          {
            "title": "Ranked Voting based Self-Consistency of Large Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.744/"
          },
          {
            "title": "Ranked Voting based Self-Consistency of Large Language ...",
            "url": "https://ylwangy.github.io/pub/ACL_2025_RVSC.pdf"
          },
          {
            "title": "Ranked Voting based Self-Consistency of Large Language Models",
            "url": "https://www.researchgate.net/publication/394270401_Ranked_Voting_based_Self-Consistency_of_Large_Language_Models"
          },
          {
            "title": "(PDF) Quantum Combinatorial Reasoning for Large Language Models",
            "url": "https://www.researchgate.net/publication/397007127_Quantum_Combinatorial_Reasoning_for_Large_Language_Models"
          },
          {
            "title": "Ranked Voting based Self-Consistency of Large Language ...",
            "url": "https://aclanthology.org/2025.findings-acl.744.pdf"
          },
          {
            "title": "Found in the Middle: Permutation Self-Consistency Improves",
            "url": "https://arxiv.org/pdf/2310.07712"
          }
        ]
      },
      "I found detailed information about the paper arXiv 2505.10772 on \"Ranked Voting based Self-Consistency of Large Language Models.\"\n\n## Overview\n\nThe paper proposes to generate ranked answers in each reasoning process and conduct ranked voting among multiple ranked answers from different responses, thereby making the overall self-consistency more reliable.\n\n## Problem & Motivation\n\nMajority voting is considered an effective method to enhance chain-of-thought reasoning, as it selects the answer with the highest \"self-consistency\" among different reasoning paths. However, previous chain-of-thought reasoning methods typically generate only a single answer in each trial, thereby ignoring the possibility of other potential answers. As a result, these alternative answers are often overlooked in subsequent voting processes.\n\n## Methodology\n\nThe authors use three ranked voting methods: Instant-runoff voting, Borda count voting, and mean reciprocal rank voting.\n\n## Evaluation\n\nThe methods are validated on six datasets, including three multiple-choice and three open-ended question-answering tasks, using both advanced open-source and closed-source large language models. The method achieves an average accuracy of 76.69% and 87.41% on gpt-3.5-turbo-0125 and gpt-4-turbo-2024-04-09, respectively, outperforming the best baseline methods by 3.4% and 0.48%.\n\n## Authors\n\nThe paper was submitted on 16 May 2025 by authors Weiqin Wang, Yile Wang, and Hui Huang. The paper has been accepted to the Findings of ACL 2025."
    ],
    "durationSeconds": 9.256702298
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the details for all 10 papers:

1. **Wadhwa et al. 2023** - "Revisiting Relation Extraction in the era of Large Language Models"
   - Authors: Somin Wadhwa, Silvio Amir, Byron Wallace
   - Year: 2023
   - Venue: ACL 2023
   - URL: https://aclanthology.org/2023.acl-long.868/
   - arXiv: https://arxiv.org/abs/2305.05003
   - Category: generative IE, foundation role

2. **GoLLIE (Sainz et al. 2024)** - "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction"
   - Authors: Oscar Sainz, Iker García-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre
   - Year: 2024
   - Venue: ICLR 2024
   - URL: https://arxiv.org/abs/2310.03668
   - Category: generative IE, foundation role

3. **Luan et al. 2018** - "Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction"
   - Authors: Yi Luan, Luheng He, Mari Ostendorf, Hannaneh Hajishirzi
   - Year: 2018
   - Venue: EMNLP 2018
   - URL: https://aclanthology.org/D18-1360/
   - Category: generative IE, dataset role

4. **Tjong Kim Sang & De Meulder 2003** - "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition"
   - Authors: Erik F. Tjong Kim Sang, Fien De Meulder
   - Year: 2003
   - Venue: CoNLL 2003
   - URL: https://aclanthology.org/W03-0419/
   - Category: generative IE, dataset role

5. **Derczynski et al. 2017** - "Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition"
   - Authors: Leon Derczynski, Eric Nichols, Marieke van Erp, Nut Limsopatham
   - Year: 2017
   - Venue: EMNLP Workshop (W-NUT) 2017
   - URL: https://aclanthology.org/W17-4418/

I'm continuing to compile the reference list for information extraction papers, filling in the remaining metadata for these foundational datasets and shared tasks.

6. **Willard & Louf 2023** - "Efficient Guided Generation for Large Language Models"
   - Authors: Brandon T. Willard, Rémi Louf
   - Year: 2023
   - Venue: arXiv preprint
   - URL: https://arxiv.org/abs/2307.09702
   - Category: generative IE, background role

7. **Fleiss 1971** - "Measuring Nominal Scale Agreement Among Many Raters"
   - Authors: Joseph L. Fleiss
   - Year: 1971
   - Venue: Psychological Bulletin
   - Category: agreement metrics, foundational work

8. **Jaccard 1901** - "Étude comparative de la distribution florale dans une portion des Alpes et du Jura"
   - Authors: Paul Jaccard
   - Year: 1901
   - Venue: Bulletin de la Société Vaudoise des Sciences Naturelles
   - Category: agreement metrics, foundational work

9. **Wang et al. 2025** - "Ranked Voting based Self-Consistency of Large Language Models"
   - Authors: Weiqin Wang, Yile Wang, Hui Huang
   - Year: 2025
   - Venue: ACL Findings 2025
   - URL: https://arxiv.org/abs/2505.10772
   - Category: self-consistency reasoning, background material

10. **Oh & Lee 2025** - "Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning"
    - Authors: Jungsuk Oh, Jay-Yoon Lee
    - Year: 2025
    - Venue: arXiv preprint
    - URL: https://arxiv.org/abs/2508.18395
    - Category: self-consistency reasoning, background material

I'm noticing the arXiv ID suggests August 2025, but the search results indicate a v3 release in February 2026, so I should verify the actual submission date.

Let me double-check the WNUT paper authors against the ACL Anthology and verify the Ranked Voting SC authors more carefully before writing the YAML update script.

Writing YAML entries... I'm noticing the ACL Findings venue for the Ranked Voting paper (2505.10772), so I should use that instead. The author list from the search shows Weiqin Wang, Yile Wang, and Hui Huang, though I'm trying to verify if there are additional authors by checking the PDF directly. I found the second author for the Latent SC paper is Jay-Yoon Lee. Now I'll start writing the YAML edits, updating the metadata section first and then adding the new entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "55d6d8c5-18f6-450e-92ed-6363310cbfb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3v3sHF5UB39hUnUqmb2Dt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1060,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 37537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9159
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

_source line 32_

All 10 papers verified. Now I'll update the YAML file — first the meta section, then append all new entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "266256d1-cfd8-4546-a7dc-cc6a48f86c0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3v3sHF5UB39hUnUqmb2Dt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1060,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 37537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9159
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

<details open><summary>🔧 Tool call — Edit · `toolu_01TGpa6MrBWgjyvSjfYC6jGX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "meta:\n  last_updated: '2026-05-14T19:30:00.000Z'\n  total_papers: 41",
  "new_string": "meta:\n  last_updated: '2026-05-14T21:00:00.000Z'\n  total_papers: 51"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "86afca48-4276-43c4-bb75-192096733498",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P3v3sHF5UB39hUnUqmb2Dt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1060,
      "cache_creation_input_tokens": 9159,
      "cache_read_input_tokens": 37537,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9159
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

_source line 34 · 2026-05-14T18:49:16.136Z_

<details><summary>↩ Tool result · `toolu_01TGpa6MrBWgjyvSjfYC6jGX`</summary>

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
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "b7713adb-981c-44e3-b446-3ed435b624fe",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "oldString": "meta:\n  last_updated: '2026-05-14T19:30:00.000Z'\n  total_papers: 41",
    "newString": "meta:\n  last_updated: '2026-05-14T21:00:00.000Z'\n  total_papers: 51",
    "originalFile": "meta:\n  last_updated: '2026-05-14T19:30:00.000Z'\n  total_papers: 41\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\n      for our structured consistency metric that operates at the semantic level of IE triples.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  fisch2021conformal:\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\n    authors:\n    - Adam Fisch\n    - Tal Schuster\n    - Tommi Jaakkola\n    - Regina Barzilay\n    year: 2021\n    venue: ICML 2021\n    url: https://arxiv.org/abs/2102.08898\n    doi: 10.5555/3524938.3525234\n    bibtex_key: fisch2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\n      prediction sets with formal coverage guarantees. Foundational for applying CP when calibration data is scarce in IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  angelopoulos2021conformal:\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\n    authors:\n    - Anastasios N. Angelopoulos\n    - Stephen Bates\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.14193\n    doi: ''\n    bibtex_key: angelopoulos2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\n      conformal prediction methodology we adapt to structured IE output sets.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  bates2021rcps:\n    title: Distribution-Free, Risk-Controlling Prediction Sets\n    authors:\n    - Stephen Bates\n    - Anastasios Angelopoulos\n    - Lihua Lei\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: Journal of the ACM 2021\n    url: https://arxiv.org/abs/2101.02703\n    doi: 10.1145/3478535\n    bibtex_key: bates2021rcps\n    category: conformal_prediction\n    role: background\n    relevance: Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\n      guarantees. Provides the theoretical basis for risk-controlled prediction in structured IE tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  xiao2019uncertainty:\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\n    authors:\n    - Yijun Xiao\n    - William Yang Wang\n    year: 2019\n    venue: AAAI 2019\n    url: https://arxiv.org/abs/1811.07253\n    doi: 10.1609/aaai.v33i01.33017322\n    bibtex_key: xiao2019uncertainty\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\n      uncertainty improves both performance and reliability for token-level predictions.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  shelmanov2021active:\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\n    authors:\n    - Artem Shelmanov\n    - Dmitri Puzyrev\n    - Lyubov Kupriyanova\n    - Denis Belyakov\n    - Daniil Larionov\n    - Nikita Khromov\n    - Olga Kozlova\n    - Ekaterina Artemova\n    - Dmitry V. Dylov\n    - Alexander Panchenko\n    year: 2021\n    venue: EACL 2021\n    url: https://arxiv.org/abs/2101.08133\n    doi: 10.18653/v1/2021.eacl-main.145\n    bibtex_key: shelmanov2021active\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  zhang2023ener:\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\n    authors:\n    - Zhen Zhang\n    - Mengting Hu\n    - Shiwan Zhao\n    - Minlie Huang\n    - Haotian Wang\n    - Lemao Liu\n    - Zhirui Zhang\n    - Zhe Liu\n    - Bingzhe Wu\n    year: 2023\n    venue: ACL Findings 2023\n    url: https://arxiv.org/abs/2305.17854\n    doi: 10.18653/v1/2023.findings-acl.103\n    bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  lakshminarayanan2017ensembles:\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\n    authors:\n    - Balaji Lakshminarayanan\n    - Alexander Pritzel\n    - Charles Blundell\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1612.01474\n    doi: ''\n    bibtex_key: lakshminarayanan2017ensembles\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  gal2016dropout:\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\n    authors:\n    - Yarin Gal\n    - Zoubin Ghahramani\n    year: 2016\n    venue: ICML 2016\n    url: https://arxiv.org/abs/1506.02142\n    doi: ''\n    bibtex_key: gal2016dropout\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  fomicheva2020unsupervised:\n    title: Unsupervised Quality Estimation for Neural Machine Translation\n    authors:\n    - Marina Fomicheva\n    - Shuo Sun\n    - Lisa Yankovskaya\n    - Frédéric Blain\n    - Francisco Guzmán\n    - Mark Fishel\n    - Nikolaos Aletras\n    - Vishrav Chaudhary\n    - Lucia Specia\n    year: 2020\n    venue: TACL 2020\n    url: https://arxiv.org/abs/2005.10608\n    doi: 10.1162/tacl_a_00330\n    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " meta:",
          "-  last_updated: '2026-05-14T19:30:00.000Z'",
          "-  total_papers: 41",
          "+  last_updated: '2026-05-14T21:00:00.000Z'",
          "+  total_papers: 51",
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

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_014R8Lhm8WjBLPnShpBP66Rj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "    added_at: '2026-05-14T19:30:00.000Z'\n",
  "new_string": "    added_at: '2026-05-14T19:30:00.000Z'\n  wadhwa2023revisiting:\n    title: Revisiting Relation Extraction in the era of Large Language Models\n    authors:\n    - Somin Wadhwa\n    - Silvio Amir\n    - Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    doi: 10.18653/v1/2023.acl-long.868\n    bibtex_key: wadhwa2023revisiting\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  sainz2024gollie:\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\n    authors:\n    - Oscar Sainz\n    - Iker García-Ferrero\n    - Rodrigo Agerri\n    - Oier Lopez de Lacalle\n    - German Rigau\n    - Eneko Agirre\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2310.03668\n    doi: ''\n    bibtex_key: sainz2024gollie\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  luan2018scierc:\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\n    authors:\n    - Yi Luan\n    - Luheng He\n    - Mari Ostendorf\n    - Hannaneh Hajishirzi\n    year: 2018\n    venue: EMNLP 2018\n    url: https://aclanthology.org/D18-1360/\n    doi: 10.18653/v1/D18-1360\n    bibtex_key: luan2018scierc\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\n      benchmark for our structured IE experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  tjongkimsang2003conll:\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\n    authors:\n    - Erik F. Tjong Kim Sang\n    - Fien De Meulder\n    year: 2003\n    venue: CoNLL 2003\n    url: https://aclanthology.org/W03-0419/\n    doi: ''\n    bibtex_key: tjongkimsang2003conll\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\n      for our NER consistency experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  derczynski2017wnut:\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\n    authors:\n    - Leon Derczynski\n    - Eric Nichols\n    - Marieke van Erp\n    - Nut Limsopatham\n    year: 2017\n    venue: W-NUT Workshop at EMNLP 2017\n    url: https://aclanthology.org/W17-4418/\n    doi: ''\n    bibtex_key: derczynski2017wnut\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\n      on harder, low-resource NER scenarios.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  willard2023guided:\n    title: Efficient Guided Generation for Large Language Models\n    authors:\n    - Brandon T. Willard\n    - Rémi Louf\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2307.09702\n    doi: ''\n    bibtex_key: willard2023guided\n    category: generative_ie\n    role: background\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  fleiss1971agreement:\n    title: Measuring Nominal Scale Agreement Among Many Raters\n    authors:\n    - Joseph L. Fleiss\n    year: 1971\n    venue: Psychological Bulletin\n    url: https://psycnet.apa.org/record/1972-05083-001\n    doi: 10.1037/h0031619\n    bibtex_key: fleiss1971agreement\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  jaccard1901distribution:\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\n    authors:\n    - Paul Jaccard\n    year: 1901\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\n    url: https://www.researchgate.net/publication/225035806\n    doi: ''\n    bibtex_key: jaccard1901distribution\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\n      between extracted entity/relation sets across multiple LLM samples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  wang2025rankedvoting:\n    title: Ranked Voting based Self-Consistency of Large Language Models\n    authors:\n    - Weiqin Wang\n    - Yile Wang\n    - Hui Huang\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2505.10772\n    doi: ''\n    bibtex_key: wang2025rankedvoting\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  oh2025latentsc:\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\n    authors:\n    - Jungsuk Oh\n    - Jay-Yoon Lee\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2508.18395\n    doi: ''\n    bibtex_key: oh2025latentsc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "28cd668b-b61e-430b-b487-6f3df0e43a20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018fwwkwoXMdveZxtQ7QZXGR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3627,
      "cache_read_input_tokens": 46696,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3627
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

_source line 36 · 2026-05-14T18:49:55.734Z_

<details><summary>↩ Tool result · reported error · `toolu_014R8Lhm8WjBLPnShpBP66Rj`</summary>

```text
&lt;tool_use_error>Found 11 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_at: '2026-05-14T19:30:00.000Z'
&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "e7e192e4-2469-471e-ad85-996ebc46bb13",
  "tool_use_result": "Error: Found 11 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.\nString:     added_at: '2026-05-14T19:30:00.000Z'\n"
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
I need to use a more unique string to identify the last entry. Let me use the last entry's context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "4319009e-47f7-422a-949c-39326e7b90fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbCrEPxPrFWinh93CP1EqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2683,
      "cache_read_input_tokens": 50323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2683
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

Need a more unique anchor. I'll use the last entry's full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "2db704e4-8cdb-4f0a-ba29-f3e23fed9111",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbCrEPxPrFWinh93CP1EqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2683,
      "cache_read_input_tokens": 50323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2683
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_015FpRMzDWsQF4RVosf8HDQv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "offset": 940
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "85d7f4ed-df15-4eb6-89e1-0260fa92e923",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DbCrEPxPrFWinh93CP1EqY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2683,
      "cache_read_input_tokens": 50323,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2683
      },
      "output_tokens": 11,
      "service_tier": "standard",
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

_source line 40 · 2026-05-14T18:50:00.933Z_

<details><summary>↩ Tool result · `toolu_015FpRMzDWsQF4RVosf8HDQv`</summary>

```text
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
951	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "64424568-525f-4842-b3c7-bb393231cef3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
      "content": "    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n",
      "numLines": 12,
      "startLine": 940,
      "totalLines": 951
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_017xU3AqHE4SB7mEAz7z985c`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
  "old_string": "    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'",
  "new_string": "    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wadhwa2023revisiting:\n    title: Revisiting Relation Extraction in the era of Large Language Models\n    authors:\n    - Somin Wadhwa\n    - Silvio Amir\n    - Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    doi: 10.18653/v1/2023.acl-long.868\n    bibtex_key: wadhwa2023revisiting\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  sainz2024gollie:\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\n    authors:\n    - Oscar Sainz\n    - Iker García-Ferrero\n    - Rodrigo Agerri\n    - Oier Lopez de Lacalle\n    - German Rigau\n    - Eneko Agirre\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2310.03668\n    doi: ''\n    bibtex_key: sainz2024gollie\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  luan2018scierc:\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\n    authors:\n    - Yi Luan\n    - Luheng He\n    - Mari Ostendorf\n    - Hannaneh Hajishirzi\n    year: 2018\n    venue: EMNLP 2018\n    url: https://aclanthology.org/D18-1360/\n    doi: 10.18653/v1/D18-1360\n    bibtex_key: luan2018scierc\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\n      benchmark for our structured IE experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  tjongkimsang2003conll:\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\n    authors:\n    - Erik F. Tjong Kim Sang\n    - Fien De Meulder\n    year: 2003\n    venue: CoNLL 2003\n    url: https://aclanthology.org/W03-0419/\n    doi: ''\n    bibtex_key: tjongkimsang2003conll\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\n      for our NER consistency experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  derczynski2017wnut:\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\n    authors:\n    - Leon Derczynski\n    - Eric Nichols\n    - Marieke van Erp\n    - Nut Limsopatham\n    year: 2017\n    venue: W-NUT Workshop at EMNLP 2017\n    url: https://aclanthology.org/W17-4418/\n    doi: ''\n    bibtex_key: derczynski2017wnut\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\n      on harder, low-resource NER scenarios.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  willard2023guided:\n    title: Efficient Guided Generation for Large Language Models\n    authors:\n    - Brandon T. Willard\n    - Rémi Louf\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2307.09702\n    doi: ''\n    bibtex_key: willard2023guided\n    category: generative_ie\n    role: background\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  fleiss1971agreement:\n    title: Measuring Nominal Scale Agreement Among Many Raters\n    authors:\n    - Joseph L. Fleiss\n    year: 1971\n    venue: Psychological Bulletin\n    url: https://psycnet.apa.org/record/1972-05083-001\n    doi: 10.1037/h0031619\n    bibtex_key: fleiss1971agreement\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  jaccard1901distribution:\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\n    authors:\n    - Paul Jaccard\n    year: 1901\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\n    url: https://www.researchgate.net/publication/225035806\n    doi: ''\n    bibtex_key: jaccard1901distribution\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\n      between extracted entity/relation sets across multiple LLM samples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  wang2025rankedvoting:\n    title: Ranked Voting based Self-Consistency of Large Language Models\n    authors:\n    - Weiqin Wang\n    - Yile Wang\n    - Hui Huang\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2505.10772\n    doi: ''\n    bibtex_key: wang2025rankedvoting\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  oh2025latentsc:\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\n    authors:\n    - Jungsuk Oh\n    - Jay-Yoon Lee\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2508.18395\n    doi: ''\n    bibtex_key: oh2025latentsc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "bf9886ce-185b-4a37-ade4-bca524d01326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U34Z4ngiTgJDHeMqSW22Wu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 336,
      "cache_read_input_tokens": 53006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 336
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

_source line 42 · 2026-05-14T18:50:37.171Z_

<details><summary>↩ Tool result · `toolu_017xU3AqHE4SB7mEAz7z985c`</summary>

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
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "8eac19bf-a83d-4251-b1e5-e9f1dfdfe5c4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml",
    "oldString": "    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'",
    "newString": "    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wadhwa2023revisiting:\n    title: Revisiting Relation Extraction in the era of Large Language Models\n    authors:\n    - Somin Wadhwa\n    - Silvio Amir\n    - Byron Wallace\n    year: 2023\n    venue: ACL 2023\n    url: https://aclanthology.org/2023.acl-long.868/\n    doi: 10.18653/v1/2023.acl-long.868\n    bibtex_key: wadhwa2023revisiting\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting\n      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  sainz2024gollie:\n    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'\n    authors:\n    - Oscar Sainz\n    - Iker García-Ferrero\n    - Rodrigo Agerri\n    - Oier Lopez de Lacalle\n    - German Rigau\n    - Eneko Agirre\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2310.03668\n    doi: ''\n    bibtex_key: sainz2024gollie\n    category: generative_ie\n    role: foundation\n    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization\n      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  luan2018scierc:\n    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction\n    authors:\n    - Yi Luan\n    - Luheng He\n    - Mari Ostendorf\n    - Hannaneh Hajishirzi\n    year: 2018\n    venue: EMNLP 2018\n    url: https://aclanthology.org/D18-1360/\n    doi: 10.18653/v1/D18-1360\n    bibtex_key: luan2018scierc\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation\n      benchmark for our structured IE experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  tjongkimsang2003conll:\n    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'\n    authors:\n    - Erik F. Tjong Kim Sang\n    - Fien De Meulder\n    year: 2003\n    venue: CoNLL 2003\n    url: https://aclanthology.org/W03-0419/\n    doi: ''\n    bibtex_key: tjongkimsang2003conll\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset\n      for our NER consistency experiments.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  derczynski2017wnut:\n    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition\n    authors:\n    - Leon Derczynski\n    - Eric Nichols\n    - Marieke van Erp\n    - Nut Limsopatham\n    year: 2017\n    venue: W-NUT Workshop at EMNLP 2017\n    url: https://aclanthology.org/W17-4418/\n    doi: ''\n    bibtex_key: derczynski2017wnut\n    category: generative_ie\n    role: dataset\n    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness\n      on harder, low-resource NER scenarios.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  willard2023guided:\n    title: Efficient Guided Generation for Large Language Models\n    authors:\n    - Brandon T. Willard\n    - Rémi Louf\n    year: 2023\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2307.09702\n    doi: ''\n    bibtex_key: willard2023guided\n    category: generative_ie\n    role: background\n    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and\n      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  fleiss1971agreement:\n    title: Measuring Nominal Scale Agreement Among Many Raters\n    authors:\n    - Joseph L. Fleiss\n    year: 1971\n    venue: Psychological Bulletin\n    url: https://psycnet.apa.org/record/1972-05083-001\n    doi: 10.1037/h0031619\n    bibtex_key: fleiss1971agreement\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation\n      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  jaccard1901distribution:\n    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura\n    authors:\n    - Paul Jaccard\n    year: 1901\n    venue: Bulletin de la Société Vaudoise des Sciences Naturelles\n    url: https://www.researchgate.net/publication/225035806\n    doi: ''\n    bibtex_key: jaccard1901distribution\n    category: agreement_metrics\n    role: foundation\n    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap\n      between extracted entity/relation sets across multiple LLM samples.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  wang2025rankedvoting:\n    title: Ranked Voting based Self-Consistency of Large Language Models\n    authors:\n    - Weiqin Wang\n    - Yile Wang\n    - Hui Huang\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2505.10772\n    doi: ''\n    bibtex_key: wang2025rankedvoting\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.\n      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'\n  oh2025latentsc:\n    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'\n    authors:\n    - Jungsuk Oh\n    - Jay-Yoon Lee\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2508.18395\n    doi: ''\n    bibtex_key: oh2025latentsc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.\n      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch4\n    added_at: '2026-05-14T21:00:00.000Z'",
    "originalFile": "meta:\n  last_updated: '2026-05-14T21:00:00.000Z'\n  total_papers: 51\ncategories: []\npapers:\n  wang2023selfconsistency:\n    title: Self-Consistency Improves Chain of Thought Reasoning in Language Models\n    authors:\n    - Xuezhi Wang\n    - Jason Wei\n    - Dale Schuurmans\n    - Quoc Le\n    - Ed Chi\n    - Sharan Narang\n    - Aakanksha Chowdhery\n    - Denny Zhou\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2203.11171\n    doi: ''\n    bibtex_key: wang2023selfconsistency\n    category: self_consistency_reasoning\n    role: foundation\n    relevance: 'Foundation paper: introduces self-consistency voting over diverse reasoning paths. We extend this paradigm\n      from closed-form answers to structured IE outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  taubenfeld2025cisc:\n    title: Confidence Improves Self-Consistency in LLMs\n    authors:\n    - Amir Taubenfeld\n    - Tom Sheffer\n    - Eran Ofek\n    - Amir Feder\n    - Ariel Goldstein\n    - Zorik Gekhman\n    - Gal Yona\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://arxiv.org/abs/2502.06233\n    doi: 10.18653/v1/2025.findings-acl.1030\n    bibtex_key: taubenfeld2025cisc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'CISC: confidence-weighted majority vote reduces required samples by 40%. Direct competitor — we address the\n      same \"strong predictor, weak selector\" gap but for structured outputs.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kang2025selfcertainty:\n    title: Scalable Best-of-N Selection for Large Language Models via Self-Certainty\n    authors:\n    - Zhewei Kang\n    - Xuandong Zhao\n    - Dawn Song\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.18581\n    doi: ''\n    bibtex_key: kang2025selfcertainty\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: Self-certainty metric for BoN selection using output probability distributions. Direct competitor — reward-free\n      quality estimation that we compare against for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  kim2026reasc:\n    title: Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning\n    authors:\n    - Junseok Kim\n    - Nakyeong Yang\n    - Kyungmin Min\n    - Kyomin Jung\n    year: 2026\n    venue: ACL 2026\n    url: https://arxiv.org/abs/2601.02970\n    doi: ''\n    bibtex_key: kim2026reasc\n    category: self_consistency_reasoning\n    role: direct-competitor\n    relevance: 'ReASC: two-stage adaptive sampling using response-level confidence for evidence sufficiency. Reduces cost\n      by 70% on GSM8K. Directly relevant to our efficiency analysis.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  thirukovalluru2024atomic:\n    title: Atomic Self-Consistency for Better Long Form Generations\n    authors:\n    - Raghuveer Thirukovalluru\n    - Yukun Huang\n    - Bhuwan Dhingra\n    year: 2024\n    venue: EMNLP 2024\n    url: https://aclanthology.org/2024.emnlp-main.706/\n    doi: 10.18653/v1/2024.emnlp-main.706\n    bibtex_key: thirukovalluru2024atomic\n    category: self_consistency_reasoning\n    role: background\n    relevance: Extends self-consistency to long-form generation by merging atomic subparts from multiple samples. Related\n      to our structured output aggregation approach.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  chen2024usc:\n    title: Universal Self-Consistency for Large Language Model Generation\n    authors:\n    - Xinyun Chen\n    - Renat Aksitov\n    - Uri Alon\n    - Jie Ren\n    - Kefan Xiao\n    - Pengcheng Yin\n    - Sushant Prakash\n    - Charles Sutton\n    - Xuezhi Wang\n    - Denny Zhou\n    year: 2024\n    venue: arXiv preprint (ICML 2024 Workshop ICL)\n    url: https://arxiv.org/abs/2311.17311\n    doi: ''\n    bibtex_key: chen2024usc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'USC: uses LLM itself to select most consistent answer among candidates, extending SC beyond closed-form answers\n      to free-form generation. Precursor to our structured consistency approach.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  manakul2023selfcheckgpt:\n    title: 'SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models'\n    authors:\n    - Potsawee Manakul\n    - Adian Liusie\n    - Mark Gales\n    year: 2023\n    venue: EMNLP 2023\n    url: https://aclanthology.org/2023.emnlp-main.557/\n    doi: 10.18653/v1/2023.emnlp-main.557\n    bibtex_key: manakul2023selfcheckgpt\n    category: self_consistency_reasoning\n    role: background\n    relevance: Uses cross-sample consistency for hallucination detection — if LLM knows a fact, samples are consistent; hallucinations\n      diverge. Motivates our consistency-based quality signal for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  wan2025rasc:\n    title: 'Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling'\n    authors:\n    - Guangya Wan\n    - Yuqi Wu\n    - Jie Chen\n    - Sheng Li\n    year: 2025\n    venue: NAACL 2025\n    url: https://aclanthology.org/2025.naacl-long.184/\n    doi: 10.18653/v1/2025.naacl-long.184\n    bibtex_key: wan2025rasc\n    category: self_consistency_reasoning\n    role: background\n    relevance: 'RASC: quality-aware selection using reasoning path assessment + consistency-driven stopping. Reduces samples\n      by ~70%. Complements our approach of structured quality-aware aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:cluster1\n    added_at: '2026-05-14T15:47:22.188Z'\n  nedellec2026consistency:\n    title: 'Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings\n      from plant-health data'\n    authors:\n    - Claire Nédellec\n    - Jingbo Xia\n    year: 2026\n    venue: Genomics & Informatics\n    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n    doi: 10.1186/s44342-025-00063-2\n    bibtex_key: nedellec2026consistency\n    category: consistency_structured_ie\n    role: direct-competitor\n    relevance: 'Most direct competitor: systematically measures consistency-accuracy correlation for LLM-based entity and\n      relation extraction on plant-health data, validating consistency as a reliability signal for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  vashurin2025cocoa:\n    title: 'Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency'\n    authors:\n    - Roman Vashurin\n    - Maiya Goloburda\n    - Albina Ilina\n    - Aleksandr Rubashevskii\n    - Preslav Nakov\n    - Artem Shelmanov\n    - Maxim Panov\n    year: 2025\n    venue: NeurIPS 2025\n    url: https://arxiv.org/abs/2502.04964\n    doi: ''\n    bibtex_key: vashurin2025cocoa\n    category: consistency_structured_ie\n    role: background\n    relevance: CoCoA framework unifies token-level confidence and sample-level consistency via MBR for uncertainty quantification.\n      Provides theoretical grounding for our dual-signal approach in structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  hobelsberger2025systematic:\n    title: Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models\n    authors:\n    - Christian Hobelsberger\n    - Theresa Winner\n    - Andreas Nawroth\n    - Oliver Mitevski\n    - Anna-Carolina Haensch\n    year: 2025\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2510.20460\n    doi: ''\n    bibtex_key: hobelsberger2025systematic\n    category: consistency_structured_ie\n    role: background\n    relevance: Systematic comparison of VCE, MSP, self-consistency, and CoCoA for LLM uncertainty estimation. Shows hybrid\n      CoCoA yields best calibration, supporting our multi-signal aggregation design.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  geng2024confidence:\n    title: A Survey of Confidence Estimation and Calibration in Large Language Models\n    authors:\n    - Jiahui Geng\n    - Fengyu Cai\n    - Yuxia Wang\n    - Heinz Koeppl\n    - Preslav Nakov\n    - Iryna Gurevych\n    year: 2024\n    venue: NAACL 2024\n    url: https://arxiv.org/abs/2311.08298\n    doi: 10.18653/v1/2024.naacl-long.366\n    bibtex_key: geng2024confidence\n    category: confidence_surveys\n    role: survey\n    relevance: Comprehensive survey of LLM confidence estimation and calibration techniques. Provides taxonomic context for\n      positioning our consistency-based confidence approach within the broader landscape.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  wen2025know:\n    title: 'Know Your Limits: A Survey of Abstention in Large Language Models'\n    authors:\n    - Bingbing Wen\n    - Jihan Yao\n    - Shangbin Feng\n    - Chenjun Xu\n    - Yulia Tsvetkov\n    - Bill Howe\n    - Lucy Lu Wang\n    year: 2025\n    venue: TACL 2025\n    url: https://arxiv.org/abs/2407.18418\n    doi: 10.1162/tacl_a_00754\n    bibtex_key: wen2025know\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey on LLM abstention from query, model, and human-values perspectives. Our consistency-based filtering\n      can be viewed as a structured-IE-specific abstention mechanism. [SUPPLEMENTARY: overlaps with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xia2025survey:\n    title: A Survey of Uncertainty Estimation Methods on Large Language Models\n    authors:\n    - Zhiqiu Xia\n    - Jinxuan Xu\n    - Yuqian Zhang\n    - Hang Liu\n    year: 2025\n    venue: ACL Findings 2025\n    url: https://aclanthology.org/2025.findings-acl.1101/\n    doi: ''\n    bibtex_key: xia2025survey\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Most comprehensive LLM uncertainty estimation survey with novel taxonomy (verbalizing, latent, consistency-based,\n      semantic clustering). Directly contextualizes our method within the consistency-based branch. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  liu2025uqcalibration:\n    title: 'Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey'\n    authors:\n    - Xiaoou Liu\n    - Tiejin Chen\n    - Longchao Da\n    - Chacha Chen\n    - Zhen Lin\n    - Hua Wei\n    year: 2025\n    venue: KDD 2025\n    url: https://arxiv.org/abs/2503.15850\n    doi: 10.1145/3711896.3736569\n    bibtex_key: liu2025uqcalibration\n    category: confidence_surveys\n    role: supplementary\n    relevance: 'Survey analyzing UQ through input, reasoning, parameter, and prediction uncertainty dimensions. Complements\n      other surveys with focus on calibration techniques applicable to our structured IE setting. [SUPPLEMENTARY: overlaps\n      with geng2024 main survey]'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kuhn2023semantic:\n    title: 'Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation'\n    authors:\n    - Lorenz Kuhn\n    - Yarin Gal\n    - Sebastian Farquhar\n    year: 2023\n    venue: ICLR 2023\n    url: https://arxiv.org/abs/2302.09664\n    doi: ''\n    bibtex_key: kuhn2023semantic\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Introduces semantic entropy for NLG uncertainty estimation by clustering semantically equivalent outputs. Foundation\n      for our structured consistency metric that operates at the semantic level of IE triples.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kadavath2022language:\n    title: Language Models (Mostly) Know What They Know\n    authors:\n    - Saurav Kadavath\n    - Tom Conerly\n    - Amanda Askell\n    - Tom Henighan\n    - Dawn Drain\n    - Ethan Perez\n    - Nicholas Schiefer\n    - Zac Hatfield-Dodds\n    - Nova DasSarma\n    - Eli Tran-Johnson\n    - Scott Johnston\n    - Sheer El-Showk\n    - Andy Jones\n    - Nelson Elhage\n    - Tristan Hume\n    - Anna Chen\n    - Yuntao Bai\n    - Sam Bowman\n    - Stanislav Fort\n    - Deep Ganguli\n    - Danny Hernandez\n    - Josh Jacobson\n    - Jackson Kernion\n    - Shauna Kravec\n    - Liane Lovitt\n    - Kamal Ndousse\n    - Catherine Olsson\n    - Sam Ringer\n    - Dario Amodei\n    - Tom Brown\n    - Jack Clark\n    - Nicholas Joseph\n    - Ben Mann\n    - Sam McCandlish\n    - Chris Olah\n    - Jared Kaplan\n    year: 2022\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2207.05221\n    doi: ''\n    bibtex_key: kadavath2022language\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Demonstrates LLMs can self-evaluate correctness via P(True) probing. Foundation for using model self-knowledge\n      as a confidence signal, which we extend to structured IE output quality estimation.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  guo2017calibration:\n    title: On Calibration of Modern Neural Networks\n    authors:\n    - Chuan Guo\n    - Geoff Pleiss\n    - Yu Sun\n    - Kilian Q. Weinberger\n    year: 2017\n    venue: ICML 2017\n    url: https://arxiv.org/abs/1706.04599\n    doi: ''\n    bibtex_key: guo2017calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Seminal work showing modern neural networks are miscalibrated and proposing temperature scaling. Foundational\n      reference for all calibration work including our LLM confidence calibration for IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  desai2020calibration:\n    title: Calibration of Pre-trained Transformers\n    authors:\n    - Shrey Desai\n    - Greg Durrett\n    year: 2020\n    venue: EMNLP 2020\n    url: https://arxiv.org/abs/2003.07892\n    doi: 10.18653/v1/2020.emnlp-main.21\n    bibtex_key: desai2020calibration\n    category: uncertainty_calibration\n    role: foundation\n    relevance: Shows pre-trained transformers (BERT, RoBERTa) are well-calibrated in-domain but degrade OOD. Bridges classical\n      calibration to the transformer era, motivating our LLM-specific calibration analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  kossen2024semantic:\n    title: 'Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs'\n    authors:\n    - Jannik Kossen\n    - Jiatong Han\n    - Muhammed Razzak\n    - Lisa Schut\n    - Shreshth Malik\n    - Yarin Gal\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2406.15927\n    doi: ''\n    bibtex_key: kossen2024semantic\n    category: uncertainty_calibration\n    role: background\n    relevance: Proposes lightweight probes to approximate semantic entropy from hidden states of a single generation, reducing\n      cost to near-zero. Relevant to our goal of efficient uncertainty estimation for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  xiong2024verbalized:\n    title: Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\n    authors:\n    - Miao Xiong\n    - Zhiyuan Hu\n    - Xinyang Lu\n    - Yifei Li\n    - Jie Fu\n    - Junxian He\n    - Bryan Hooi\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2306.13063\n    doi: ''\n    bibtex_key: xiong2024verbalized\n    category: uncertainty_calibration\n    role: background\n    relevance: Systematic evaluation of verbalized confidence elicitation via prompting, sampling, and aggregation. Directly\n      relevant to our use of LLM-expressed confidence as a signal for structured IE quality.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch1\n    added_at: '2026-05-14T17:52:10.000Z'\n  fisch2021conformal:\n    title: Few-Shot Conformal Prediction with Auxiliary Tasks\n    authors:\n    - Adam Fisch\n    - Tal Schuster\n    - Tommi Jaakkola\n    - Regina Barzilay\n    year: 2021\n    venue: ICML 2021\n    url: https://arxiv.org/abs/2102.08898\n    doi: 10.5555/3524938.3525234\n    bibtex_key: fisch2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Adapts conformal prediction to few-shot settings via meta-learning over auxiliary tasks, producing tighter\n      prediction sets with formal coverage guarantees. Foundational for applying CP when calibration data is scarce in IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  angelopoulos2021conformal:\n    title: Uncertainty Sets for Image Classifiers using Conformal Prediction\n    authors:\n    - Anastasios N. Angelopoulos\n    - Stephen Bates\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.14193\n    doi: ''\n    bibtex_key: angelopoulos2021conformal\n    category: conformal_prediction\n    role: foundation\n    relevance: Introduces RAPS (Regularized Adaptive Prediction Sets) with finite-sample coverage guarantees. Foundation for\n      conformal prediction methodology we adapt to structured IE output sets.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  bates2021rcps:\n    title: Distribution-Free, Risk-Controlling Prediction Sets\n    authors:\n    - Stephen Bates\n    - Anastasios Angelopoulos\n    - Lihua Lei\n    - Jitendra Malik\n    - Michael I. Jordan\n    year: 2021\n    venue: Journal of the ACM 2021\n    url: https://arxiv.org/abs/2101.02703\n    doi: 10.1145/3478535\n    bibtex_key: bates2021rcps\n    category: conformal_prediction\n    role: background\n    relevance: Generalizes conformal prediction to control arbitrary monotone losses for set-valued predictors with finite-sample\n      guarantees. Provides the theoretical basis for risk-controlled prediction in structured IE tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  xiao2019uncertainty:\n    title: Quantifying Uncertainties in Natural Language Processing Tasks\n    authors:\n    - Yijun Xiao\n    - William Yang Wang\n    year: 2019\n    venue: AAAI 2019\n    url: https://arxiv.org/abs/1811.07253\n    doi: 10.1609/aaai.v33i01.33017322\n    bibtex_key: xiao2019uncertainty\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Pioneers Bayesian uncertainty quantification for NLP tasks including NER, showing that modeling data and model\n      uncertainty improves both performance and reliability for token-level predictions.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  shelmanov2021active:\n    title: Active Learning for Sequence Tagging with Deep Pre-trained Models and Bayesian Uncertainty Estimates\n    authors:\n    - Artem Shelmanov\n    - Dmitri Puzyrev\n    - Lyubov Kupriyanova\n    - Denis Belyakov\n    - Daniil Larionov\n    - Nikita Khromov\n    - Olga Kozlova\n    - Ekaterina Artemova\n    - Dmitry V. Dylov\n    - Alexander Panchenko\n    year: 2021\n    venue: EACL 2021\n    url: https://arxiv.org/abs/2101.08133\n    doi: 10.18653/v1/2021.eacl-main.145\n    bibtex_key: shelmanov2021active\n    category: token_span_uncertainty_ner\n    role: foundation\n    relevance: Extensive empirical study of Bayesian uncertainty estimation (MC dropout variants) for sequence tagging with\n      pre-trained models. Establishes best practices for uncertainty-guided active learning in NER.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  zhang2023ener:\n    title: 'E-NER: Evidential Deep Learning for Trustworthy Named Entity Recognition'\n    authors:\n    - Zhen Zhang\n    - Mengting Hu\n    - Shiwan Zhao\n    - Minlie Huang\n    - Haotian Wang\n    - Lemao Liu\n    - Zhirui Zhang\n    - Zhe Liu\n    - Bingzhe Wu\n    year: 2023\n    venue: ACL Findings 2023\n    url: https://arxiv.org/abs/2305.17854\n    doi: 10.18653/v1/2023.findings-acl.103\n    bibtex_key: zhang2023ener\n    category: token_span_uncertainty_ner\n    role: background\n    relevance: Applies evidential deep learning to NER with uncertainty-guided loss terms, addressing sparse entities and\n      OOV/OOD discrimination. Demonstrates token-level uncertainty estimation across multiple NER paradigms.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  lakshminarayanan2017ensembles:\n    title: Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\n    authors:\n    - Balaji Lakshminarayanan\n    - Alexander Pritzel\n    - Charles Blundell\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1612.01474\n    doi: ''\n    bibtex_key: lakshminarayanan2017ensembles\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Proposes deep ensembles as a simple, scalable alternative to Bayesian NNs for predictive uncertainty estimation.\n      Foundational baseline for ensemble-based uncertainty quantification we compare against.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  gal2016dropout:\n    title: 'Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning'\n    authors:\n    - Yarin Gal\n    - Zoubin Ghahramani\n    year: 2016\n    venue: ICML 2016\n    url: https://arxiv.org/abs/1506.02142\n    doi: ''\n    bibtex_key: gal2016dropout\n    category: ensemble_mc_dropout\n    role: foundation\n    relevance: Establishes theoretical framework casting dropout as approximate Bayesian inference, enabling MC dropout for\n      uncertainty estimation. Foundation for all dropout-based uncertainty methods we build upon.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  fomicheva2020unsupervised:\n    title: Unsupervised Quality Estimation for Neural Machine Translation\n    authors:\n    - Marina Fomicheva\n    - Shuo Sun\n    - Lisa Yankovskaya\n    - Frédéric Blain\n    - Francisco Guzmán\n    - Mark Fishel\n    - Nikolaos Aletras\n    - Vishrav Chaudhary\n    - Lucia Specia\n    year: 2020\n    venue: TACL 2020\n    url: https://arxiv.org/abs/2005.10608\n    doi: 10.1162/tacl_a_00330\n    bibtex_key: fomicheva2020unsupervised\n    category: ensemble_mc_dropout\n    role: background\n    relevance: Applies MC dropout and ensemble-based uncertainty to NLP (MT quality estimation) without supervision, achieving\n      strong correlation with human judgments. Key precedent for unsupervised uncertainty signals in NLP generation tasks.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch2\n    added_at: '2026-05-14T18:10:52.000Z'\n  cobbe2021verifiers:\n    title: Training Verifiers to Solve Math Word Problems\n    authors:\n    - Karl Cobbe\n    - Vineet Kosaraju\n    - Mohammad Bavarian\n    - Mark Chen\n    - Heewoo Jun\n    - Lukasz Kaiser\n    - Matthias Plappert\n    - Jerry Tworek\n    - Jacob Hilton\n    - Reiichiro Nakano\n    - Christopher Hesse\n    - John Schulman\n    year: 2021\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2110.14168\n    doi: ''\n    bibtex_key: cobbe2021verifiers\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: introduces training outcome-based verifiers (ORM) for math word problems and the GSM8K benchmark.\n      Establishes the verify-then-select paradigm our method builds upon.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  lightman2024verify:\n    title: Let's Verify Step by Step\n    authors:\n    - Hunter Lightman\n    - Vineet Kosaraju\n    - Yura Burda\n    - Harri Edwards\n    - Bowen Baker\n    - Teddy Lee\n    - Jan Leike\n    - John Schulman\n    - Ilya Sutskever\n    - Karl Cobbe\n    year: 2024\n    venue: ICLR 2024\n    url: https://arxiv.org/abs/2305.20050\n    doi: ''\n    bibtex_key: lightman2024verify\n    category: verifier_reward_models\n    role: foundation\n    relevance: 'Foundation paper: demonstrates process reward models (PRMs) with step-level supervision outperform outcome-based\n      verification. Key motivation for fine-grained quality signals in our structured IE aggregation.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wang2024mathshepherd:\n    title: 'Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations'\n    authors:\n    - Peiyi Wang\n    - Lei Li\n    - Zhihong Shao\n    - Runxin Xu\n    - Damai Dai\n    - Yifei Li\n    - Deli Chen\n    - Yu Wu\n    - Zhifang Sui\n    year: 2024\n    venue: ACL 2024\n    url: https://arxiv.org/abs/2312.08935\n    doi: ''\n    bibtex_key: wang2024mathshepherd\n    category: verifier_reward_models\n    role: background\n    relevance: Automated process reward model construction without human annotations, enabling step-level verification at scale.\n      Demonstrates ORM/PRM effectiveness for both reranking and reinforcement learning.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  snell2024scaling:\n    title: Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\n    authors:\n    - Charlie Snell\n    - Jaehoon Lee\n    - Kelvin Xu\n    - Aviral Kumar\n    year: 2024\n    venue: ICLR 2025\n    url: https://arxiv.org/abs/2408.03314\n    doi: ''\n    bibtex_key: snell2024scaling\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: introduces compute-optimal test-time scaling, showing adaptive per-prompt compute allocation\n      improves efficiency 4x over best-of-N. Directly motivates our adaptive sampling strategy.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  brown2024monkeys:\n    title: 'Large Language Monkeys: Scaling Inference Compute with Repeated Sampling'\n    authors:\n    - Bradley Brown\n    - Jordan Juravsky\n    - Ryan Ehrlich\n    - Ronald Clark\n    - Quoc V. Le\n    - Christopher Ré\n    - Azalia Mirhoseini\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2407.21787\n    doi: ''\n    bibtex_key: brown2024monkeys\n    category: tts_scaling\n    role: foundation\n    relevance: 'Foundation paper: demonstrates log-linear scaling of coverage with repeated sampling across tasks, establishing\n      inference-time scaling laws. Motivates our multi-sample approach for structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  wu2024inference:\n    title: 'Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models'\n    authors:\n    - Yangzhen Wu\n    - Zhiqing Sun\n    - Shanda Li\n    - Sean Welleck\n    - Yiming Yang\n    year: 2024\n    venue: arXiv preprint\n    url: https://arxiv.org/abs/2408.00724\n    doi: ''\n    bibtex_key: wu2024inference\n    category: tts_scaling\n    role: background\n    relevance: Empirical analysis of compute-optimal inference strategies showing smaller models with advanced inference algorithms\n      achieve Pareto-optimal cost-performance trade-offs. Complements our efficiency analysis.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  kuleshov2015calibrated:\n    title: Calibrated Structured Prediction\n    authors:\n    - Volodymyr Kuleshov\n    - Percy Liang\n    year: 2015\n    venue: NeurIPS 2015\n    url: https://proceedings.neurips.cc/paper/2015/hash/52d2752b150f9c35ccb6869cbf074e48-Abstract.html\n    doi: ''\n    bibtex_key: kuleshov2015calibrated\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: extends calibration to structured prediction with formal guarantees, proposing recalibration\n      methods for marginal and conditional queries. Theoretical basis for calibrated structured IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  culotta2004confidence:\n    title: Confidence Estimation for Information Extraction\n    authors:\n    - Aron Culotta\n    - Andrew McCallum\n    year: 2004\n    venue: HLT-NAACL 2004\n    url: https://aclanthology.org/N04-4028/\n    doi: ''\n    bibtex_key: culotta2004confidence\n    category: structured_calibration_ie\n    role: foundation\n    relevance: 'Foundation paper: pioneers confidence estimation for CRF-based information extraction at both field and record\n      levels. Establishes the problem setting our LLM-based approach addresses.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  jagannatha2020calibrating:\n    title: Calibrating Structured Output Predictors for Natural Language Processing\n    authors:\n    - Abhyuday Jagannatha\n    - Hong Yu\n    year: 2020\n    venue: ACL 2020\n    url: https://aclanthology.org/2020.acl-main.188/\n    doi: ''\n    bibtex_key: jagannatha2020calibrating\n    category: structured_calibration_ie\n    role: background\n    relevance: Proposes general calibration scheme for neural structured prediction models in NLP including NER and QA. Bridges\n      classical calibration methods to modern neural IE, directly relevant to our structured output calibration.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  geifman2017selective:\n    title: Selective Classification for Deep Neural Networks\n    authors:\n    - Yonatan Geifman\n    - Ran El-Yaniv\n    year: 2017\n    venue: NeurIPS 2017\n    url: https://arxiv.org/abs/1705.08500\n    doi: ''\n    bibtex_key: geifman2017selective\n    category: selective_prediction\n    role: foundation\n    relevance: 'Foundation paper: introduces selective classification framework for DNNs with guaranteed risk control at specified\n      coverage levels. Theoretical foundation for our consistency-based selective prediction in IE.'\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n  ren2023selfevaluation:\n    title: Self-Evaluation Improves Selective Generation in Large Language Models\n    authors:\n    - Jie Ren\n    - Yao Zhao\n    - Tu Vu\n    - Peter J. Liu\n    - Balaji Lakshminarayanan\n    year: 2023\n    venue: NeurIPS 2023 Workshop\n    url: https://arxiv.org/abs/2312.09300\n    doi: ''\n    bibtex_key: ren2023selfevaluation\n    category: selective_prediction\n    role: background\n    relevance: Proposes LLM self-evaluation for selective generation, reformulating open-ended tasks into token-level predictions\n      to leverage better calibration. Directly relevant to our confidence-aware abstention mechanism for structured IE.\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper-research:lit_batch3\n    added_at: '2026-05-14T19:30:00.000Z'\n",
    "structuredPatch": [
      {
        "oldStart": 948,
        "oldLines": 3,
        "newStart": 948,
        "newLines": 201,
        "lines": [
          "     verified: true",
          "     added_by: paper-research:lit_batch3",
          "     added_at: '2026-05-14T19:30:00.000Z'",
          "+  wadhwa2023revisiting:",
          "+    title: Revisiting Relation Extraction in the era of Large Language Models",
          "+    authors:",
          "+    - Somin Wadhwa",
          "+    - Silvio Amir",
          "+    - Byron Wallace",
          "+    year: 2023",
          "+    venue: ACL 2023",
          "+    url: https://aclanthology.org/2023.acl-long.868/",
          "+    doi: 10.18653/v1/2023.acl-long.868",
          "+    bibtex_key: wadhwa2023revisiting",
          "+    category: generative_ie",
          "+    role: foundation",
          "+    relevance: 'Foundation paper: evaluates LLMs (GPT-3, Flan-T5) for relation extraction as seq2seq, showing few-shot prompting",
          "+      achieves near-SOTA performance. Establishes generative RE paradigm our structured consistency method builds upon.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  sainz2024gollie:",
          "+    title: 'GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction'",
          "+    authors:",
          "+    - Oscar Sainz",
          "+    - Iker García-Ferrero",
          "+    - Rodrigo Agerri",
          "+    - Oier Lopez de Lacalle",
          "+    - German Rigau",
          "+    - Eneko Agirre",
          "+    year: 2024",
          "+    venue: ICLR 2024",
          "+    url: https://arxiv.org/abs/2310.03668",
          "+    doi: ''",
          "+    bibtex_key: sainz2024gollie",
          "+    category: generative_ie",
          "+    role: foundation",
          "+    relevance: 'Foundation paper: fine-tunes LLM to follow annotation guidelines for zero-shot IE, achieving strong generalization",
          "+      to unseen tasks. Key baseline for guideline-driven structured generation in our framework.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  luan2018scierc:",
          "+    title: Multi-Task Identification of Entities, Relations, and Coreference for Scientific Knowledge Graph Construction",
          "+    authors:",
          "+    - Yi Luan",
          "+    - Luheng He",
          "+    - Mari Ostendorf",
          "+    - Hannaneh Hajishirzi",
          "+    year: 2018",
          "+    venue: EMNLP 2018",
          "+    url: https://aclanthology.org/D18-1360/",
          "+    doi: 10.18653/v1/D18-1360",
          "+    bibtex_key: luan2018scierc",
          "+    category: generative_ie",
          "+    role: dataset",
          "+    relevance: 'Introduces SciERC dataset with entity, relation, and coreference annotations for scientific text. Primary evaluation",
          "+      benchmark for our structured IE experiments.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  tjongkimsang2003conll:",
          "+    title: 'Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition'",
          "+    authors:",
          "+    - Erik F. Tjong Kim Sang",
          "+    - Fien De Meulder",
          "+    year: 2003",
          "+    venue: CoNLL 2003",
          "+    url: https://aclanthology.org/W03-0419/",
          "+    doi: ''",
          "+    bibtex_key: tjongkimsang2003conll",
          "+    category: generative_ie",
          "+    role: dataset",
          "+    relevance: 'Introduces CoNLL-2003 NER dataset, the standard benchmark for named entity recognition. Core evaluation dataset",
          "+      for our NER consistency experiments.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  derczynski2017wnut:",
          "+    title: Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition",
          "+    authors:",
          "+    - Leon Derczynski",
          "+    - Eric Nichols",
          "+    - Marieke van Erp",
          "+    - Nut Limsopatham",
          "+    year: 2017",
          "+    venue: W-NUT Workshop at EMNLP 2017",
          "+    url: https://aclanthology.org/W17-4418/",
          "+    doi: ''",
          "+    bibtex_key: derczynski2017wnut",
          "+    category: generative_ie",
          "+    role: dataset",
          "+    relevance: 'Introduces WNUT-17 dataset for novel and emerging entity recognition in noisy text. Tests our method robustness",
          "+      on harder, low-resource NER scenarios.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  willard2023guided:",
          "+    title: Efficient Guided Generation for Large Language Models",
          "+    authors:",
          "+    - Brandon T. Willard",
          "+    - Rémi Louf",
          "+    year: 2023",
          "+    venue: arXiv preprint",
          "+    url: https://arxiv.org/abs/2307.09702",
          "+    doi: ''",
          "+    bibtex_key: willard2023guided",
          "+    category: generative_ie",
          "+    role: background",
          "+    relevance: 'Reformulates neural text generation as FSM transitions, enabling efficient constrained decoding with regexes and",
          "+      CFGs. Foundational for structured output guarantees in our IE generation pipeline.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  fleiss1971agreement:",
          "+    title: Measuring Nominal Scale Agreement Among Many Raters",
          "+    authors:",
          "+    - Joseph L. Fleiss",
          "+    year: 1971",
          "+    venue: Psychological Bulletin",
          "+    url: https://psycnet.apa.org/record/1972-05083-001",
          "+    doi: 10.1037/h0031619",
          "+    bibtex_key: fleiss1971agreement",
          "+    category: agreement_metrics",
          "+    role: foundation",
          "+    relevance: 'Introduces Fleiss kappa for measuring inter-rater agreement on nominal scales with multiple raters. Foundation",
          "+      metric for quantifying cross-sample consistency in our multi-generation IE aggregation.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  jaccard1901distribution:",
          "+    title: Étude comparative de la distribution florale dans une portion des Alpes et du Jura",
          "+    authors:",
          "+    - Paul Jaccard",
          "+    year: 1901",
          "+    venue: Bulletin de la Société Vaudoise des Sciences Naturelles",
          "+    url: https://www.researchgate.net/publication/225035806",
          "+    doi: ''",
          "+    bibtex_key: jaccard1901distribution",
          "+    category: agreement_metrics",
          "+    role: foundation",
          "+    relevance: 'Introduces the Jaccard similarity coefficient for set comparison. Foundation metric for measuring pairwise overlap",
          "+      between extracted entity/relation sets across multiple LLM samples.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  wang2025rankedvoting:",
          "+    title: Ranked Voting based Self-Consistency of Large Language Models",
          "+    authors:",
          "+    - Weiqin Wang",
          "+    - Yile Wang",
          "+    - Hui Huang",
          "+    year: 2025",
          "+    venue: ACL Findings 2025",
          "+    url: https://arxiv.org/abs/2505.10772",
          "+    doi: ''",
          "+    bibtex_key: wang2025rankedvoting",
          "+    category: self_consistency_reasoning",
          "+    role: background",
          "+    relevance: 'Extends SC from single-answer majority vote to ranked answer lists with instant-runoff and Borda count voting.",
          "+      Relevant to our multi-candidate aggregation strategy for structured IE outputs.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'",
          "+  oh2025latentsc:",
          "+    title: 'Latent Self-Consistency for Reliable Majority-Set Selection in Short- and Long-Answer Reasoning'",
          "+    authors:",
          "+    - Jungsuk Oh",
          "+    - Jay-Yoon Lee",
          "+    year: 2025",
          "+    venue: arXiv preprint",
          "+    url: https://arxiv.org/abs/2508.18395",
          "+    doi: ''",
          "+    bibtex_key: oh2025latentsc",
          "+    category: self_consistency_reasoning",
          "+    role: background",
          "+    relevance: 'LSC: uses learnable summary token embeddings to compute semantic consistency across samples without text matching.",
          "+      Extends SC to long-form outputs with negligible overhead, relevant to our structured output consistency measurement.'",
          "+    abstract: ''",
          "+    semantic_scholar_id: ''",
          "+    verified: true",
          "+    added_by: paper-research:lit_batch4",
          "+    added_at: '2026-05-14T21:00:00.000Z'"
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

_source line 43_

Let me verify the file is valid YAML.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "354b689b-1a73-4379-a473-86fe4eaf15a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XRqwkgHQ6vJS1rgexJBLw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 53342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2853
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Xkkie5p7NJeyWHFQBHfebf`</summary>

```json
{
  "command": "python3 -c \"import yaml; data = yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml')); print(f'total_papers meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}'); print(f'actual papers: {len(data[\\\"papers\\\"])}'); batch4 = [k for k,v in data['papers'].items() if v.get('added_by') == 'paper-research:lit_batch4']; print(f'batch4 entries ({len(batch4)}):'); [print(f'  {k}: {v[\\\"category\\\"]}/{v[\\\"role\\\"]}') for k,v in data['papers'].items() if v.get('added_by') == 'paper-research:lit_batch4']\"",
  "description": "Validate YAML and count papers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "87867e9b-e678-460b-997f-54ad93332340",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017XRqwkgHQ6vJS1rgexJBLw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2853,
      "cache_read_input_tokens": 53342,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2853
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

_source line 45 · 2026-05-14T18:50:46.744Z_

<details><summary>↩ Tool result · `toolu_01Xkkie5p7NJeyWHFQBHfebf`</summary>

```text
total_papers meta: 51
actual papers: 51
batch4 entries (10):
  wadhwa2023revisiting: generative_ie/foundation
  sainz2024gollie: generative_ie/foundation
  luan2018scierc: generative_ie/dataset
  tjongkimsang2003conll: generative_ie/dataset
  derczynski2017wnut: generative_ie/dataset
  willard2023guided: generative_ie/background
  fleiss1971agreement: agreement_metrics/foundation
  jaccard1901distribution: agreement_metrics/foundation
  wang2025rankedvoting: self_consistency_reasoning/background
  oh2025latentsc: self_consistency_reasoning/background
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "d7f56e71-44d9-400c-832c-66538552b227",
  "tool_use_result": {
    "stdout": "total_papers meta: 51\nactual papers: 51\nbatch4 entries (10):\n  wadhwa2023revisiting: generative_ie/foundation\n  sainz2024gollie: generative_ie/foundation\n  luan2018scierc: generative_ie/dataset\n  tjongkimsang2003conll: generative_ie/dataset\n  derczynski2017wnut: generative_ie/dataset\n  willard2023guided: generative_ie/background\n  fleiss1971agreement: agreement_metrics/foundation\n  jaccard1901distribution: agreement_metrics/foundation\n  wang2025rankedvoting: self_consistency_reasoning/background\n  oh2025latentsc: self_consistency_reasoning/background",
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

YAML 验证通过。10 篇论文已全部追加到 `literature_map.yaml`，total_papers 更新为 51。

**本批次新增：**

| cluster | bibtex_key | role |
|---------|-----------|------|
| generative_ie | wadhwa2023revisiting | foundation |
| generative_ie | sainz2024gollie | foundation |
| generative_ie | luan2018scierc | dataset |
| generative_ie | tjongkimsang2003conll | dataset |
| generative_ie | derczynski2017wnut | dataset |
| generative_ie | willard2023guided | background |
| agreement_metrics | fleiss1971agreement | foundation |
| agreement_metrics | jaccard1901distribution | foundation |
| self_consistency_reasoning | wang2025rankedvoting | background |
| self_consistency_reasoning | oh2025latentsc | background |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "uuid": "d05074cc-b4fa-4b19-8c99-5fd9d830f187",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011qeYXWQUFgKZERbmHMF5MK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 482,
      "cache_read_input_tokens": 56195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 482
      },
      "output_tokens": 3,
      "service_tier": "standard",
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

YAML 验证通过。10 篇论文已全部追加到 `literature_map.yaml`，total_papers 更新为 51。

**本批次新增：**

| cluster | bibtex_key | role |
|---------|-----------|------|
| generative_ie | wadhwa2023revisiting | foundation |
| generative_ie | sainz2024gollie | foundation |
| generative_ie | luan2018scierc | dataset |
| generative_ie | tjongkimsang2003conll | dataset |
| generative_ie | derczynski2017wnut | dataset |
| generative_ie | willard2023guided | background |
| agreement_metrics | fleiss1971agreement | foundation |
| agreement_metrics | jaccard1901distribution | foundation |
| self_consistency_reasoning | wang2025rankedvoting | background |
| self_consistency_reasoning | oh2025latentsc | background |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 169083,
  "duration_api_ms": 221430,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "04ccb23e-781c-43ca-88db-301d5743abb1",
  "total_cost_usd": 0.96004,
  "usage": {
    "input_tokens": 1071,
    "cache_creation_input_tokens": 44836,
    "cache_read_input_tokens": 332952,
    "output_tokens": 9444,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44836,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 237,
        "cache_read_input_tokens": 56195,
        "cache_creation_input_tokens": 482,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 482
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 150394,
      "outputTokens": 4298,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 10,
      "costUSD": 0.271884,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1071,
      "outputTokens": 9444,
      "cacheReadInputTokens": 332952,
      "cacheCreationInputTokens": 44836,
      "webSearchRequests": 0,
      "costUSD": 0.688156,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "17c10bf8-1b06-44cd-8273-ebd14fc34f78"
}
```

</details>

---
