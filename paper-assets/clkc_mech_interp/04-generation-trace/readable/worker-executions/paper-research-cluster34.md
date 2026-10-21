# paper research cluster34

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_research_cluster34_20260522T134427.log`
- **Structured JSON:** [`57137af2dd553a7c52e5.json`](../../sessions/57/57137af2dd553a7c52e5.json)

## Before a recorded user message

60 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
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
    "mcp__agent-ml-research__check_figures_and_layout",
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
  "uuid": "5891511f-3996-4ba1-858e-9699ae630597",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
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
    "resetsAt": 1779475200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d08105f9-4b9d-45e6-8f46-dfde6dea6ea0",
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to search for academic papers in two clusters (Cross-lingual Representations and Probing Methodology) and add them to their literature_map.yaml. Let me start by reading the existing literature_map.yaml and then searching for papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "d4929f52-c671-4ee3-88da-15ef5966ef55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz19cX4HH1ipWZN6t8C5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

先读现有 literature_map.yaml，同时并行搜索论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "3ae0110a-c090-4d16-a63f-7596c8ec8299",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz19cX4HH1ipWZN6t8C5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_014PA1zYTDZ8eXBLjo9LWWTU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "e37d49f9-bdc7-496a-8b15-a6e191fc2e0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz19cX4HH1ipWZN6t8C5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 7 · 2026-05-22T13:44:43.932Z_

<details><summary>↩ Tool result · `toolu_014PA1zYTDZ8eXBLjo9LWWTU`</summary>

```text
1	categories: []
2	meta:
3	  last_updated: '2026-05-22T14:00:00Z'
4	  total_papers: 15
5	papers:
6	  basu2026interpretability:
7	    abstract: ''
8	    added_at: '2026-05-21T12:04:50.273Z'
9	    added_by: director-bootstrap
10	    authors:
11	    - Basu, S.
12	    - et al.
13	    bibtex_key: basu2026interpretability
14	    category: sae-steering
15	    doi: ''
16	    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.
17	      Critical negative result: defines boundary conditions for when SAE steering
18	      works. Our Track 3 design addresses their methodological gaps.'
19	    role: direct-competitor
20	    semantic_scholar_id: ''
21	    title: 'Interpretability without actionability: mechanistic methods cannot correct
22	      language model errors despite near-perfect internal representations'
23	    url: https://arxiv.org/abs/2603.18353
24	    venue: arXiv
25	    verified: true
26	    year: 2026
27	  boer2026probing:
28	    abstract: ''
29	    added_at: '2026-05-21T12:04:50.273Z'
30	    added_by: director-bootstrap
31	    authors:
32	    - Boer, A.
33	    - Brink, I.
34	    - Ulmer, D.
35	    bibtex_key: boer2026probing
36	    category: probing
37	    doi: ''
38	    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.
39	      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99
40	      F1.
41	    role: direct-competitor
42	    semantic_scholar_id: ''
43	    title: Probing for Knowledge Attribution in Large Language Models
44	    url: https://arxiv.org/abs/2602.22787
45	    venue: arXiv
46	    verified: true
47	    year: 2026
48	  ifergan2024beneath:
49	    added_at: '2026-05-22T14:00:00Z'
50	    added_by: paper-agent-lit-search
51	    authors:
52	    - Ifergan, M.
53	    - Choshen, L.
54	    - Aharoni, R.
55	    - Szpektor, I.
56	    - Abend, O.
57	    bibtex_key: ifergan2024beneath
58	    category: cross-lingual-conflict
59	    doi: ''
60	    relevance: Shows cross-lingual answer consistency does not imply shared representation;
61	      script similarity dominates sharing. Directly motivates our probing approach
62	      to test whether conflict signals share representations across languages.
63	    role: foundation
64	    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge
65	      Representation Sharing in LLMs'
66	    url: https://arxiv.org/abs/2408.10646
67	    venue: Findings of NAACL 2025
68	    verified: true
69	    year: 2024
70	  kialy2026universal:
71	    abstract: ''
72	    added_at: '2026-05-21T12:04:50.273Z'
73	    added_by: director-bootstrap
74	    authors:
75	    - Kialy, U.Z.
76	    - Shtarkberg, A.
77	    - Klein, A.
78	    bibtex_key: kialy2026universal
79	    category: cross-lingual-sae
80	    doi: ''
81	    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core
82	      for register features + zero-shot steering transfer. We test whether this extends
83	      to knowledge conflict features.
84	    role: direct-competitor
85	    semantic_scholar_id: ''
86	    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register
87	      with SAEs
88	    url: https://arxiv.org/abs/2603.26236
89	    venue: arXiv
90	    verified: true
91	    year: 2026
92	  li2025taming:
93	    added_at: '2026-05-22T14:00:00Z'
94	    added_by: paper-agent-lit-search
95	    authors:
96	    - Li, G.
97	    - Chen, Y.
98	    - Tong, H.
99	    bibtex_key: li2025taming
100	    category: knowledge-conflict
101	    doi: ''
102	    relevance: Proposes conflict resolution framework for LLMs. Provides resolution
103	      baselines our mechanistic approach complements.
104	    role: direct-competitor
105	    title: Taming Knowledge Conflicts in Language Models
106	    url: https://arxiv.org/abs/2503.10996
107	    venue: ICML 2025 (Spotlight)
108	    verified: true
109	    year: 2025
110	  pham2026where:
111	    abstract: ''
112	    added_at: '2026-05-21T12:04:50.273Z'
113	    added_by: director-bootstrap
114	    authors:
115	    - Pham, M.V.
116	    - Borkakoty, H.
117	    - Hou, Y.
118	    bibtex_key: pham2026where
119	    category: conflict-mechanism
120	    doi: ''
121	    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers
122	      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel
123	      for within-parametric conflicts.
124	    role: direct-competitor
125	    semantic_scholar_id: ''
126	    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge
127	      Conflict in Language Models'
128	    url: https://arxiv.org/abs/2601.09445
129	    venue: arXiv
130	    verified: true
131	    year: 2026
132	  team2026qwen:
133	    abstract: ''
134	    added_at: '2026-05-21T12:04:50.273Z'
135	    added_by: director-bootstrap
136	    authors:
137	    - Qwen Team
138	    bibtex_key: team2026qwen
139	    category: sae-tools
140	    doi: ''
141	    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs
142	      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section
143	      5.2).
144	    role: foundation
145	    semantic_scholar_id: ''
146	    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language
147	      Models'
148	    url: https://arxiv.org/abs/2605.11887
149	    venue: arXiv
150	    verified: true
151	    year: 2026
152	  wang2025lost:
153	    abstract: ''
154	    added_at: '2026-05-21T12:04:50.273Z'
155	    added_by: director-bootstrap
156	    authors:
157	    - Wang, M.
158	    - Adel, H.
159	    - Lange, L.
160	    - et al.
161	    bibtex_key: wang2025lost
162	    category: cross-lingual-mechanism
163	    doi: ''
164	    relevance: Language-independent concept space through most layers, language-specific
165	      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.
166	    role: foundation
167	    semantic_scholar_id: ''
168	    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency
169	      in Transformer Language Models'
170	    url: https://arxiv.org/abs/2504.04264
171	    venue: ACL 2025 (SAC Highlights)
172	    verified: true
173	    year: 2025
174	  wong2026langfir:
175	    abstract: ''
176	    added_at: '2026-05-21T12:04:50.273Z'
177	    added_by: director-bootstrap
178	    authors:
179	    - Wong, S.H.
180	    - Siddique, A.B.
181	    - Sajjad, H.
182	    bibtex_key: wong2026langfir
183	    category: cross-lingual-sae
184	    doi: ''
185	    relevance: Random-token filtering isolates <5 language-specific SAE features/language.
186	      Our Track 2 uses this as control to disentangle language-identity from conflict
187	      features.
188	    role: direct-competitor
189	    semantic_scholar_id: ''
190	    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual
191	      Data for Language Steering'
192	    url: https://arxiv.org/abs/2604.03532
193	    venue: arXiv
194	    verified: true
195	    year: 2026
196	  xie2024adaptive:
197	    added_at: '2026-05-22T14:00:00Z'
198	    added_by: paper-agent-lit-search
199	    authors:
200	    - Xie, J.
201	    - Zhang, K.
202	    - Chen, J.
203	    - Lou, R.
204	    - Su, Y.
205	    bibtex_key: xie2024adaptive
206	    category: knowledge-conflict
207	    doi: ''
208	    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying
209	      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation
210	      dataset.
211	    role: foundation
212	    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large
213	      Language Models in Knowledge Conflicts'
214	    url: https://arxiv.org/abs/2305.13300
215	    venue: ICLR 2024
216	    verified: true
217	    year: 2024
218	  xing2024evaluating:
219	    added_at: '2026-05-22T14:00:00Z'
220	    added_by: paper-agent-lit-search
221	    authors:
222	    - Xing, X.
223	    - He, Z.
224	    - Xu, H.
225	    - Wang, X.
226	    - Wang, R.
227	    - Hong, Y.
228	    bibtex_key: xing2024evaluating
229	    category: cross-lingual-conflict
230	    doi: ''
231	    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics
232	      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation
233	      methodology relevant to our cross-lingual conflict measurement.
234	    role: peripheral
235	    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language
236	      Models
237	    url: https://arxiv.org/abs/2407.01358
238	    venue: arXiv
239	    verified: true
240	    year: 2024
241	  xu2024knowledge:
242	    added_at: '2026-05-22T14:00:00Z'
243	    added_by: paper-agent-lit-search
244	    authors:
245	    - Xu, R.
246	    - Qi, Z.
247	    - Guo, Z.
248	    - Wang, C.
249	    - Wang, H.
250	    - Zhang, Y.
251	    - Xu, W.
252	    bibtex_key: xu2024knowledge
253	    category: knowledge-conflict
254	    doi: ''
255	    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory
256	      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.
257	    role: foundation
258	    title: 'Knowledge Conflicts for LLMs: A Survey'
259	    url: https://arxiv.org/abs/2403.08319
260	    venue: EMNLP 2024
261	    verified: true
262	    year: 2024
263	  zhao2024analysing:
264	    abstract: ''
265	    added_at: '2026-05-21T12:04:50.273Z'
266	    added_by: director-bootstrap
267	    authors:
268	    - Zhao, Y.
269	    - Du, X.
270	    - Hong, G.
271	    - et al.
272	    bibtex_key: zhao2024analysing
273	    category: probing
274	    doi: ''
275	    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts
276	      in residual stream. Foundation for our Track 1 cross-lingual extension.'
277	    role: foundation
278	    semantic_scholar_id: ''
279	    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts
280	    url: https://arxiv.org/abs/2410.16090
281	    venue: NeurIPS 2024 FMI Workshop
282	    verified: true
283	    year: 2024
284	  zhao2025steering:
285	    abstract: ''
286	    added_at: '2026-05-21T12:04:50.273Z'
287	    added_by: director-bootstrap
288	    authors:
289	    - Zhao, Y.
290	    - Devoto, A.
291	    - Hong, G.
292	    - et al.
293	    bibtex_key: zhao2025steering
294	    category: sae-steering
295	    doi: ''
296	    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology
297	      we extend to cross-lingual setting. MI-based feature selection, constraint-aware
298	      activation editing.'
299	    role: direct-competitor
300	    semantic_scholar_id: ''
301	    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation
302	      Engineering
303	    url: https://arxiv.org/abs/2410.15999
304	    venue: NAACL 2025 Oral
305	    verified: true
306	    year: 2025
307	  zhao2026when:
308	    abstract: ''
309	    added_at: '2026-05-21T12:04:50.273Z'
310	    added_by: director-bootstrap
311	    authors:
312	    - Zhao, J.
313	    - et al.
314	    bibtex_key: zhao2026when
315	    category: cross-lingual-conflict
316	    doi: ''
317	    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral
318	      finding that linguistic similarity governs entity-centric conflict resolution.
319	      Our work provides mechanistic explanation.'
320	    role: direct-competitor
321	    semantic_scholar_id: ''
322	    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'
323	    url: https://arxiv.org/abs/2601.07041
324	    venue: arXiv
325	    verified: true
326	    year: 2026
327	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "f2d473a7-5a97-43ea-824f-da5f23172a0b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
      "content": "categories: []\nmeta:\n  last_updated: '2026-05-22T14:00:00Z'\n  total_papers: 15\npapers:\n  basu2026interpretability:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Basu, S.\n    - et al.\n    bibtex_key: basu2026interpretability\n    category: sae-steering\n    doi: ''\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\n      Critical negative result: defines boundary conditions for when SAE steering\n      works. Our Track 3 design addresses their methodological gaps.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\n      language model errors despite near-perfect internal representations'\n    url: https://arxiv.org/abs/2603.18353\n    venue: arXiv\n    verified: true\n    year: 2026\n  boer2026probing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Boer, A.\n    - Brink, I.\n    - Ulmer, D.\n    bibtex_key: boer2026probing\n    category: probing\n    doi: ''\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\n      F1.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Probing for Knowledge Attribution in Large Language Models\n    url: https://arxiv.org/abs/2602.22787\n    venue: arXiv\n    verified: true\n    year: 2026\n  ifergan2024beneath:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ifergan, M.\n    - Choshen, L.\n    - Aharoni, R.\n    - Szpektor, I.\n    - Abend, O.\n    bibtex_key: ifergan2024beneath\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Shows cross-lingual answer consistency does not imply shared representation;\n      script similarity dominates sharing. Directly motivates our probing approach\n      to test whether conflict signals share representations across languages.\n    role: foundation\n    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge\n      Representation Sharing in LLMs'\n    url: https://arxiv.org/abs/2408.10646\n    venue: Findings of NAACL 2025\n    verified: true\n    year: 2024\n  kialy2026universal:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Kialy, U.Z.\n    - Shtarkberg, A.\n    - Klein, A.\n    bibtex_key: kialy2026universal\n    category: cross-lingual-sae\n    doi: ''\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\n      for register features + zero-shot steering transfer. We test whether this extends\n      to knowledge conflict features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\n      with SAEs\n    url: https://arxiv.org/abs/2603.26236\n    venue: arXiv\n    verified: true\n    year: 2026\n  li2025taming:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, G.\n    - Chen, Y.\n    - Tong, H.\n    bibtex_key: li2025taming\n    category: knowledge-conflict\n    doi: ''\n    relevance: Proposes conflict resolution framework for LLMs. Provides resolution\n      baselines our mechanistic approach complements.\n    role: direct-competitor\n    title: Taming Knowledge Conflicts in Language Models\n    url: https://arxiv.org/abs/2503.10996\n    venue: ICML 2025 (Spotlight)\n    verified: true\n    year: 2025\n  pham2026where:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Pham, M.V.\n    - Borkakoty, H.\n    - Hou, Y.\n    bibtex_key: pham2026where\n    category: conflict-mechanism\n    doi: ''\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\n      for within-parametric conflicts.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\n      Conflict in Language Models'\n    url: https://arxiv.org/abs/2601.09445\n    venue: arXiv\n    verified: true\n    year: 2026\n  team2026qwen:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Qwen Team\n    bibtex_key: team2026qwen\n    category: sae-tools\n    doi: ''\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\n      5.2).\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\n      Models'\n    url: https://arxiv.org/abs/2605.11887\n    venue: arXiv\n    verified: true\n    year: 2026\n  wang2025lost:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wang, M.\n    - Adel, H.\n    - Lange, L.\n    - et al.\n    bibtex_key: wang2025lost\n    category: cross-lingual-mechanism\n    doi: ''\n    relevance: Language-independent concept space through most layers, language-specific\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\n      in Transformer Language Models'\n    url: https://arxiv.org/abs/2504.04264\n    venue: ACL 2025 (SAC Highlights)\n    verified: true\n    year: 2025\n  wong2026langfir:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wong, S.H.\n    - Siddique, A.B.\n    - Sajjad, H.\n    bibtex_key: wong2026langfir\n    category: cross-lingual-sae\n    doi: ''\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\n      Our Track 2 uses this as control to disentangle language-identity from conflict\n      features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\n      Data for Language Steering'\n    url: https://arxiv.org/abs/2604.03532\n    venue: arXiv\n    verified: true\n    year: 2026\n  xie2024adaptive:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xie, J.\n    - Zhang, K.\n    - Chen, J.\n    - Lou, R.\n    - Su, Y.\n    bibtex_key: xie2024adaptive\n    category: knowledge-conflict\n    doi: ''\n    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying\n      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation\n      dataset.\n    role: foundation\n    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large\n      Language Models in Knowledge Conflicts'\n    url: https://arxiv.org/abs/2305.13300\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  xing2024evaluating:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xing, X.\n    - He, Z.\n    - Xu, H.\n    - Wang, X.\n    - Wang, R.\n    - Hong, Y.\n    bibtex_key: xing2024evaluating\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics\n      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation\n      methodology relevant to our cross-lingual conflict measurement.\n    role: peripheral\n    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language\n      Models\n    url: https://arxiv.org/abs/2407.01358\n    venue: arXiv\n    verified: true\n    year: 2024\n  xu2024knowledge:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xu, R.\n    - Qi, Z.\n    - Guo, Z.\n    - Wang, C.\n    - Wang, H.\n    - Zhang, Y.\n    - Xu, W.\n    bibtex_key: xu2024knowledge\n    category: knowledge-conflict\n    doi: ''\n    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory\n      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.\n    role: foundation\n    title: 'Knowledge Conflicts for LLMs: A Survey'\n    url: https://arxiv.org/abs/2403.08319\n    venue: EMNLP 2024\n    verified: true\n    year: 2024\n  zhao2024analysing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Du, X.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2024analysing\n    category: probing\n    doi: ''\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\n    role: foundation\n    semantic_scholar_id: ''\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\n    url: https://arxiv.org/abs/2410.16090\n    venue: NeurIPS 2024 FMI Workshop\n    verified: true\n    year: 2024\n  zhao2025steering:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Devoto, A.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2025steering\n    category: sae-steering\n    doi: ''\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\n      activation editing.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\n      Engineering\n    url: https://arxiv.org/abs/2410.15999\n    venue: NAACL 2025 Oral\n    verified: true\n    year: 2025\n  zhao2026when:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, J.\n    - et al.\n    bibtex_key: zhao2026when\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\n      finding that linguistic similarity governs entity-centric conflict resolution.\n      Our work provides mechanistic explanation.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n",
      "numLines": 327,
      "startLine": 1,
      "totalLines": 327
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L5sne1zHeUU1thSh1uqRN8`</summary>

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
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "7461dbb6-2c44-4428-aa9c-b09e1a81cfcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qz19cX4HH1ipWZN6t8C5GS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12532
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 9 · 2026-05-22T13:44:44.551Z_

<details><summary>↩ Tool result · `toolu_01L5sne1zHeUU1thSh1uqRN8`</summary>

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
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "4943c8b2-c167-4c76-9720-552aaa9dd30a",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the current literature_map.yaml and the WebSearch tool. Let me now search for the papers in parallel. I'll search for the key papers across both clusters.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "8d864433-7ac6-49df-ba49-8ea8982bd57c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 11_

开始并行搜索两个 cluster 的论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "26c33bf5-4289-4e1f-8aee-c731a2680d73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WXxjzqMBHEEJ399mhLNu7Z`</summary>

```json
{
  "query": "Conneau et al 2020 \"Emerging Cross-lingual Structure in Pretrained Language Models\" ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "667cda1a-52d2-4d66-b94b-739f5332caa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UeLPezkX88GLBZqkzCGGGo`</summary>

```json
{
  "query": "Belinkov 2022 probing classifiers survey \"Probing Classifiers\" computational linguistics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "fe5c90b1-6031-4bc8-8427-ebed20a319fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019r4ESSWbx2oxY4itd54hWB`</summary>

```json
{
  "query": "cross-lingual representation alignment multilingual transformer CKA layer-wise analysis 2022 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "4660b6fc-c1f1-4042-8fa3-d5760113a754",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VsPuuUiYcFech495cfNCLi`</summary>

```json
{
  "query": "English-centric bias multilingual language models representations 2023 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "ba0f24cf-3791-4b17-958c-87bc3c5faa83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ryE2refDKWsBRznmjn7aZ`</summary>

```json
{
  "query": "linear probe expressiveness limitations selectivity probing NLP 2020 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "2c3c13e3-98f5-4e30-940a-bee89ff89dee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BNhWh3tVyhdYwS2WXw3kMe`</summary>

```json
{
  "query": "bootstrap confidence interval probing NLP statistical significance 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "0c4fa67c-4275-4dc0-b828-3521ee304ecd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016o4xoKa5ZvhFxrTCpQu3EN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4978,
      "cache_read_input_tokens": 24373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4978
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

_source line 18 · 2026-05-22T13:44:53.895Z_

<details><summary>↩ Tool result · `toolu_01UeLPezkX88GLBZqkzCGGGo`</summary>

```text
Web search results for query: "Belinkov 2022 probing classifiers survey "Probing Classifiers" computational linguistics"

Links: [{"title":"Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"},{"title":"@article{belinkov-2022-probing,","url":"https://aclanthology.org/2022.cl-1.7.bib"},{"title":"[PDF] Probing Classifiers: Promises, Shortcomings, and Advances | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Probing-Classifiers:-Promises,-Shortcomings,-and-Belinkov/3dcfa05a1c162e6cab927c5b08d0444f7b6691f4"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology","url":"https://aclanthology.org/2022.cl-1.7/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal","url":"https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"},{"title":"Yonatan Belinkov | publications","url":"https://belinkov.com/publications/publicationstype/"},{"title":"[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/abs/2102.12452"}]

I've found the paper you're looking for. Here are the key details:

**Title:** "Probing Classifiers: Promises, Shortcomings, and Advances"

**Author:** Yonatan Belinkov

**Publication:** Computational Linguistics, 48(1):207–219, 2022

**Overview:** Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple—a classifier is trained to predict some linguistic property from a model's representations—and has been used to examine a wide variety of models and properties.

**Content:** Recent studies have demonstrated various methodological limitations of this approach. The paper critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances.

The paper is available on multiple platforms including MIT Press, ACL Anthology, and arXiv (arXiv:2102.12452).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "8bd6554e-64fc-46ff-866e-f7f8699a0f57",
  "tool_use_result": {
    "query": "Belinkov 2022 probing classifiers survey \"Probing Classifiers\" computational linguistics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MF7RnWjALMwkfhHbxsmMZk",
        "content": [
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and"
          },
          {
            "title": "@article{belinkov-2022-probing,",
            "url": "https://aclanthology.org/2022.cl-1.7.bib"
          },
          {
            "title": "[PDF] Probing Classifiers: Promises, Shortcomings, and Advances | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Probing-Classifiers:-Promises,-Shortcomings,-and-Belinkov/3dcfa05a1c162e6cab927c5b08d0444f7b6691f4"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances - ACL Anthology",
            "url": "https://aclanthology.org/2022.cl-1.7/"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances - Technion - Israel Institute of Technology",
            "url": "https://cris.technion.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances - Israeli Research Community Portal",
            "url": "https://cris.iucc.ac.il/en/publications/probing-classifiers-promises-shortcomings-and-advances/"
          },
          {
            "title": "Yonatan Belinkov | publications",
            "url": "https://belinkov.com/publications/publicationstype/"
          },
          {
            "title": "[2102.12452] Probing Classifiers: Promises, Shortcomings, and Advances",
            "url": "https://arxiv.org/abs/2102.12452"
          }
        ]
      },
      "I've found the paper you're looking for. Here are the key details:\n\n**Title:** \"Probing Classifiers: Promises, Shortcomings, and Advances\"\n\n**Author:** Yonatan Belinkov\n\n**Publication:** Computational Linguistics, 48(1):207–219, 2022\n\n**Overview:** Probing classifiers have emerged as one of the prominent methodologies for interpreting and analyzing deep neural network models of natural language processing. The basic idea is simple—a classifier is trained to predict some linguistic property from a model's representations—and has been used to examine a wide variety of models and properties.\n\n**Content:** Recent studies have demonstrated various methodological limitations of this approach. The paper critically reviews the probing classifiers framework, highlighting their promises, shortcomings, and advances.\n\nThe paper is available on multiple platforms including MIT Press, ACL Anthology, and arXiv (arXiv:2102.12452)."
    ],
    "durationSeconds": 4.092943711
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T13:44:55.461Z_

<details><summary>↩ Tool result · `toolu_01WXxjzqMBHEEJ399mhLNu7Z`</summary>

```text
Web search results for query: "Conneau et al 2020 "Emerging Cross-lingual Structure in Pretrained Language Models" ACL"

Links: [{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.536/"},{"title":"Exploring the Data Efficiency of Cross-Lingual Post-Training in Pretrained Language Models","url":"https://www.mdpi.com/2076-3417/11/5/1974"},{"title":"GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub","url":"https://github.com/shijie-wu/crosslingual-nlp"},{"title":"crosslingual-nlp/README.md at master · shijie-wu/crosslingual-nlp","url":"https://github.com/shijie-wu/crosslingual-nlp/blob/master/README.md"},{"title":"(PDF) Cross-lingual Language Model Pretraining for Retrieval","url":"https://www.researchgate.net/publication/352111504_Cross-lingual_Language_Model_Pretraining_for_Retrieval"},{"title":"Cross-lingual Language Model Pretraining for Retrieval | Proceedings of the Web Conference 2021","url":"https://dl.acm.org/doi/10.1145/3442381.3449830"},{"title":"ACL2020: Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://virtual.acl2020.org/paper_main.536.html"},{"title":"[PDF] Emerging Cross-lingual Structure in Pretrained Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Emerging-Cross-lingual-Structure-in-Pretrained-Wu-Conneau/cfe8ec7a183ed548db1a862e38908343cefb94c7"},{"title":"[1911.01464] Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://arxiv.org/abs/1911.01464"},{"title":"(PDF) Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://www.researchgate.net/publication/337048070_Emerging_Cross-lingual_Structure_in_Pretrained_Language_Models"}]

Based on the search results, I found the paper you're looking for:

"Emerging Cross-lingual Structure in Pretrained Language Models" by Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov, published in 2020, was presented at ACL (Association for Computational Linguistics).

The paper studies multilingual masked language modeling—training a single model on concatenated text from multiple languages—and presents a detailed study of factors that influence why these models are effective for cross-lingual transfer.

Key findings include: Transfer is possible even without shared vocabulary across monolingual corpora or when text comes from different domains, requiring only shared parameters in the top layers of the multilingual encoder. Additionally, representations from monolingual BERT models in different languages can be aligned post-hoc effectively, suggesting universal latent symmetries in learned embedding spaces.

The paper is available on the ACL Anthology at https://aclanthology.org/2020.acl-main.536/ (DOI: 10.18653/v1/2020.acl-main.536) and was also preprinted on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "784acffe-b1b8-40e9-ac8e-91170792e98c",
  "tool_use_result": {
    "query": "Conneau et al 2020 \"Emerging Cross-lingual Structure in Pretrained Language Models\" ACL",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XnM5GzkpQMpC6fYACFYfzd",
        "content": [
          {
            "title": "Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.536/"
          },
          {
            "title": "Exploring the Data Efficiency of Cross-Lingual Post-Training in Pretrained Language Models",
            "url": "https://www.mdpi.com/2076-3417/11/5/1974"
          },
          {
            "title": "GitHub - shijie-wu/crosslingual-nlp: This repo supports various cross-lingual transfer learning & multilingual NLP models. · GitHub",
            "url": "https://github.com/shijie-wu/crosslingual-nlp"
          },
          {
            "title": "crosslingual-nlp/README.md at master · shijie-wu/crosslingual-nlp",
            "url": "https://github.com/shijie-wu/crosslingual-nlp/blob/master/README.md"
          },
          {
            "title": "(PDF) Cross-lingual Language Model Pretraining for Retrieval",
            "url": "https://www.researchgate.net/publication/352111504_Cross-lingual_Language_Model_Pretraining_for_Retrieval"
          },
          {
            "title": "Cross-lingual Language Model Pretraining for Retrieval | Proceedings of the Web Conference 2021",
            "url": "https://dl.acm.org/doi/10.1145/3442381.3449830"
          },
          {
            "title": "ACL2020: Emerging Cross-lingual Structure in Pretrained Language Models",
            "url": "https://virtual.acl2020.org/paper_main.536.html"
          },
          {
            "title": "[PDF] Emerging Cross-lingual Structure in Pretrained Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Emerging-Cross-lingual-Structure-in-Pretrained-Wu-Conneau/cfe8ec7a183ed548db1a862e38908343cefb94c7"
          },
          {
            "title": "[1911.01464] Emerging Cross-lingual Structure in Pretrained Language Models",
            "url": "https://arxiv.org/abs/1911.01464"
          },
          {
            "title": "(PDF) Emerging Cross-lingual Structure in Pretrained Language Models",
            "url": "https://www.researchgate.net/publication/337048070_Emerging_Cross-lingual_Structure_in_Pretrained_Language_Models"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Emerging Cross-lingual Structure in Pretrained Language Models\" by Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov, published in 2020, was presented at ACL (Association for Computational Linguistics).\n\nThe paper studies multilingual masked language modeling—training a single model on concatenated text from multiple languages—and presents a detailed study of factors that influence why these models are effective for cross-lingual transfer.\n\nKey findings include: Transfer is possible even without shared vocabulary across monolingual corpora or when text comes from different domains, requiring only shared parameters in the top layers of the multilingual encoder. Additionally, representations from monolingual BERT models in different languages can be aligned post-hoc effectively, suggesting universal latent symmetries in learned embedding spaces.\n\nThe paper is available on the ACL Anthology at https://aclanthology.org/2020.acl-main.536/ (DOI: 10.18653/v1/2020.acl-main.536) and was also preprinted on arXiv."
    ],
    "durationSeconds": 6.0514312169999975
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T13:44:58.519Z_

<details><summary>↩ Tool result · `toolu_019r4ESSWbx2oxY4itd54hWB`</summary>

```text
Web search results for query: "cross-lingual representation alignment multilingual transformer CKA layer-wise analysis 2022 2023 2024"

Links: [{"title":"Neither Here Nor There: Cross-Lingual Representation Dynamics of Code-Mixed Text in Multilingual Encoders","url":"https://arxiv.org/html/2603.19771"},{"title":"TRepLiNa: Layer-wise CKA+REPINA Alignment Improves Low-Resource Machine Translation in Aya-23 8B","url":"https://arxiv.org/pdf/2510.06249"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF","url":"https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs","url":"https://arxiv.org/html/2502.14830v1"},{"title":"Cross-Lingual Continuous Pretraining","url":"https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"},{"title":"Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://arxiv.org/pdf/2212.01924"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/pdf/2504.09378"}]

I've successfully performed a web search for your query about cross-lingual representation alignment in multilingual transformers with CKA layer-wise analysis. Here's a summary of the relevant findings:

## Key Research Areas and Findings

**CKA for Cross-Lingual Analysis:**
CKA (Centered Kernel Alignment) and SVCCA are employed as complementary representation similarity measures to quantify layer-wise alignment between sentence representations across languages. CKA is invariant to isotropic scaling and orthogonal transformations, making it well-suited for comparing representations across layers, languages, and model architectures.

**Recent Applications (2024-2025):**
Recent work combines CKA with Representation Projection Invariance (REPINA), a regularization method that constrains parameter updates to remain close to the pretrained model, into a joint method called TRepLiNa. Aligning mid-level layers with TRepLiNa is a low-cost and practical way to improve low-resource language translation in data-scarce settings.

**Layer-Wise Patterns:**
Recent findings indicate that optimal cross-lingual alignment is not necessarily achieved at the final Transformer layer for low-resource languages. Multilingual LLMs tend to turn language-specific inputs into more language-agnostic representations in their middle layers.

**Methodological Discussions:**
CKA and variants of CCA are commonly used indexes to measure cross-lingual representation similarity, though their assumptions align poorly with explaining zero-shot cross-lingual transfer.

The search results include recent papers from 2024-2026 addressing these topics in detail.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "042515bd-ceca-4e3f-999f-e64338382751",
  "tool_use_result": {
    "query": "cross-lingual representation alignment multilingual transformer CKA layer-wise analysis 2022 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_0173PY27DA3WZnep4jDQVTkF",
        "content": [
          {
            "title": "Neither Here Nor There: Cross-Lingual Representation Dynamics of Code-Mixed Text in Multilingual Encoders",
            "url": "https://arxiv.org/html/2603.19771"
          },
          {
            "title": "TRepLiNa: Layer-wise CKA+REPINA Alignment Improves Low-Resource Machine Translation in Aya-23 8B",
            "url": "https://arxiv.org/pdf/2510.06249"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"
          },
          {
            "title": "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs",
            "url": "https://arxiv.org/html/2502.14830v1"
          },
          {
            "title": "Cross-Lingual Continuous Pretraining",
            "url": "https://www.emergentmind.com/topics/cross-lingual-continuous-pretraining"
          },
          {
            "title": "Cross-lingual Similarity of Multilingual Representations Revisited",
            "url": "https://arxiv.org/pdf/2212.01924"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/pdf/2504.09378"
          }
        ]
      },
      "I've successfully performed a web search for your query about cross-lingual representation alignment in multilingual transformers with CKA layer-wise analysis. Here's a summary of the relevant findings:\n\n## Key Research Areas and Findings\n\n**CKA for Cross-Lingual Analysis:**\nCKA (Centered Kernel Alignment) and SVCCA are employed as complementary representation similarity measures to quantify layer-wise alignment between sentence representations across languages. CKA is invariant to isotropic scaling and orthogonal transformations, making it well-suited for comparing representations across layers, languages, and model architectures.\n\n**Recent Applications (2024-2025):**\nRecent work combines CKA with Representation Projection Invariance (REPINA), a regularization method that constrains parameter updates to remain close to the pretrained model, into a joint method called TRepLiNa. Aligning mid-level layers with TRepLiNa is a low-cost and practical way to improve low-resource language translation in data-scarce settings.\n\n**Layer-Wise Patterns:**\nRecent findings indicate that optimal cross-lingual alignment is not necessarily achieved at the final Transformer layer for low-resource languages. Multilingual LLMs tend to turn language-specific inputs into more language-agnostic representations in their middle layers.\n\n**Methodological Discussions:**\nCKA and variants of CCA are commonly used indexes to measure cross-lingual representation similarity, though their assumptions align poorly with explaining zero-shot cross-lingual transfer.\n\nThe search results include recent papers from 2024-2026 addressing these topics in detail."
    ],
    "durationSeconds": 7.300306474000001
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-22T13:44:58.632Z_

<details><summary>↩ Tool result · `toolu_01BNhWh3tVyhdYwS2WXw3kMe`</summary>

```text
Web search results for query: "bootstrap confidence interval probing NLP statistical significance 2022 2023"

Links: [{"title":"[2205.11134] Please, Don't Forget the Difference and the Confidence Interval when Seeking for the State-of-the-Art Status","url":"https://arxiv.org/abs/2205.11134"},{"title":"Please, Don't Forget the Difference and the Confidence Interval when   Seeking for the State-of-the-Art Status","url":"https://arxiv.org/pdf/2205.11134"},{"title":"(PDF) Confidence Intervals by Bootstrapping Approach: A Significance Review","url":"https://www.researchgate.net/publication/368809659_Confidence_Intervals_by_Bootstrapping_Approach_A_Significance_Review"},{"title":"Please, Don't Forget the Difference and the Confidence ...","url":"https://aclanthology.org/2022.lrec-1.640.pdf"},{"title":"Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation","url":"https://arxiv.org/pdf/2509.22612"},{"title":"Appendix - Recommended Statistical Significance Tests for NLP Tasks","url":"https://arxiv.org/pdf/1809.01448"},{"title":"Using the bootstrap to establish statistical significance for relative validity comparisons among patient-reported outcome measures","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3681626/"}]

Based on the search results, I found several relevant resources on bootstrap confidence intervals, statistical significance, and NLP evaluation from 2022-2023:

**Key Finding:**

A 2022 paper argues for the widest possible use of bootstrap confidence intervals for comparing NLP system performances instead of the state-of-the-art status (SOTA) and statistical significance testing. The main benefits are to draw attention to the difference in performance between two systems and to help assess the degree of superiority of one system over another.

**Supporting Resources:**

- A python module for obtaining these confidence intervals as well as a function implementing the Fisher-Pitman test for paired samples are freely available on PyPi.

- Additional recent work addresses statistical significance and uncertainty quantification in NLP evaluation more broadly, examining alternative approaches to assessing model performance variation beyond traditional resampling methods.

The search results include academic papers from 2022-2023 focused on bootstrap approaches for statistical significance testing in NLP, with practical implementations and critiques of traditional SOTA rankings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "fa4da7f1-f303-4b9f-b263-7999af0d2965",
  "tool_use_result": {
    "query": "bootstrap confidence interval probing NLP statistical significance 2022 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_0182KL5ApFfyhVN38rR4erew",
        "content": [
          {
            "title": "[2205.11134] Please, Don't Forget the Difference and the Confidence Interval when Seeking for the State-of-the-Art Status",
            "url": "https://arxiv.org/abs/2205.11134"
          },
          {
            "title": "Please, Don't Forget the Difference and the Confidence Interval when   Seeking for the State-of-the-Art Status",
            "url": "https://arxiv.org/pdf/2205.11134"
          },
          {
            "title": "(PDF) Confidence Intervals by Bootstrapping Approach: A Significance Review",
            "url": "https://www.researchgate.net/publication/368809659_Confidence_Intervals_by_Bootstrapping_Approach_A_Significance_Review"
          },
          {
            "title": "Please, Don't Forget the Difference and the Confidence ...",
            "url": "https://aclanthology.org/2022.lrec-1.640.pdf"
          },
          {
            "title": "Beyond statistical significance: Quantifying uncertainty and statistical variability in multilingual and multitask NLP evaluation",
            "url": "https://arxiv.org/pdf/2509.22612"
          },
          {
            "title": "Appendix - Recommended Statistical Significance Tests for NLP Tasks",
            "url": "https://arxiv.org/pdf/1809.01448"
          },
          {
            "title": "Using the bootstrap to establish statistical significance for relative validity comparisons among patient-reported outcome measures",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3681626/"
          }
        ]
      },
      "Based on the search results, I found several relevant resources on bootstrap confidence intervals, statistical significance, and NLP evaluation from 2022-2023:\n\n**Key Finding:**\n\nA 2022 paper argues for the widest possible use of bootstrap confidence intervals for comparing NLP system performances instead of the state-of-the-art status (SOTA) and statistical significance testing. The main benefits are to draw attention to the difference in performance between two systems and to help assess the degree of superiority of one system over another.\n\n**Supporting Resources:**\n\n- A python module for obtaining these confidence intervals as well as a function implementing the Fisher-Pitman test for paired samples are freely available on PyPi.\n\n- Additional recent work addresses statistical significance and uncertainty quantification in NLP evaluation more broadly, examining alternative approaches to assessing model performance variation beyond traditional resampling methods.\n\nThe search results include academic papers from 2022-2023 focused on bootstrap approaches for statistical significance testing in NLP, with practical implementations and critiques of traditional SOTA rankings."
    ],
    "durationSeconds": 5.572860367999998
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T13:44:59.767Z_

<details><summary>↩ Tool result · `toolu_01VsPuuUiYcFech495cfNCLi`</summary>

```text
Web search results for query: "English-centric bias multilingual language models representations 2023 2024"

Links: [{"title":"Do Multilingual LLMs Think In English?","url":"https://arxiv.org/pdf/2502.15603"},{"title":"Cross-Language Bias Examination in Large Language Models Yuxuan Liang","url":"https://arxiv.org/pdf/2512.16029"},{"title":"PANGEA:AFULLY OPEN MULTILINGUAL MULTI","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf"},{"title":"Beyond English-Centric LLMs: What Language Do Multilingual Language Models Think in?","url":"https://arxiv.org/html/2408.10811v1"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"},{"title":"Tokenization and Representation Biases in Multilingual ...","url":"https://aclanthology.org/2025.emnlp-main.1224.pdf"},{"title":"What Language Do Non-English-Centric Large ...","url":"https://aclanthology.org/2025.findings-acl.1350.pdf"}]

I've found relevant research on English-centric bias in multilingual language models. Here are the key findings from recent 2023-2024 research:

## Performance and Fairness Issues

English-centric behavior of LLMs causes them to perform worse in other languages in downstream tasks and in fluency. Additionally, this impacts the fairness of these models—which currently exhibit cultural biases—and their robustness and reliability in diverse linguistic settings.

## Training Data Imbalances

Models suffer from English- and western-centric training and evaluation datasets, resulting in a lack of representation for the vast majority of the world's languages and diverse cultural contexts. Models predominately trained on such data exhibit diminished performance in multilingual settings with poor tokenization further leading to higher inference costs, generate outputs misaligned with the socio-cultural norms of underrepresented languages, and lack the ability to recognize objects from geographically diverse regions.

## Internal Language Representations

Recent research explores how multilingual models represent language internally. The internal latent language phenomenon raises the question of what internal latent language non-English-centric models 'think' in, and whether these models utilize the dominant language from their training corpora in their intermediate layers when processing tasks. These models semantically use English as a pivot language in their middle layers.

## Bias Evaluation

Much research on explicit bias in LLMs focuses on English-centric bias detection, indicating that evaluation frameworks themselves are often skewed toward English.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "6cd9a708-50ca-4c8d-a46c-d0e21b729a7f",
  "tool_use_result": {
    "query": "English-centric bias multilingual language models representations 2023 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KjQs9oLj4WvFeDoi4W5ahw",
        "content": [
          {
            "title": "Do Multilingual LLMs Think In English?",
            "url": "https://arxiv.org/pdf/2502.15603"
          },
          {
            "title": "Cross-Language Bias Examination in Large Language Models Yuxuan Liang",
            "url": "https://arxiv.org/pdf/2512.16029"
          },
          {
            "title": "PANGEA:AFULLY OPEN MULTILINGUAL MULTI",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/770b8cf7ef10b4aa7170d09b36b6bb6f-Paper-Conference.pdf"
          },
          {
            "title": "Beyond English-Centric LLMs: What Language Do Multilingual Language Models Think in?",
            "url": "https://arxiv.org/html/2408.10811v1"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via ...",
            "url": "https://arxiv.org/pdf/2410.05873"
          },
          {
            "title": "Tokenization and Representation Biases in Multilingual ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1224.pdf"
          },
          {
            "title": "What Language Do Non-English-Centric Large ...",
            "url": "https://aclanthology.org/2025.findings-acl.1350.pdf"
          }
        ]
      },
      "I've found relevant research on English-centric bias in multilingual language models. Here are the key findings from recent 2023-2024 research:\n\n## Performance and Fairness Issues\n\nEnglish-centric behavior of LLMs causes them to perform worse in other languages in downstream tasks and in fluency. Additionally, this impacts the fairness of these models—which currently exhibit cultural biases—and their robustness and reliability in diverse linguistic settings.\n\n## Training Data Imbalances\n\nModels suffer from English- and western-centric training and evaluation datasets, resulting in a lack of representation for the vast majority of the world's languages and diverse cultural contexts. Models predominately trained on such data exhibit diminished performance in multilingual settings with poor tokenization further leading to higher inference costs, generate outputs misaligned with the socio-cultural norms of underrepresented languages, and lack the ability to recognize objects from geographically diverse regions.\n\n## Internal Language Representations\n\nRecent research explores how multilingual models represent language internally. The internal latent language phenomenon raises the question of what internal latent language non-English-centric models 'think' in, and whether these models utilize the dominant language from their training corpora in their intermediate layers when processing tasks. These models semantically use English as a pivot language in their middle layers.\n\n## Bias Evaluation\n\nMuch research on explicit bias in LLMs focuses on English-centric bias detection, indicating that evaluation frameworks themselves are often skewed toward English."
    ],
    "durationSeconds": 8.058835758
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-22T13:45:01.704Z_

<details><summary>↩ Tool result · `toolu_015ryE2refDKWsBRznmjn7aZ`</summary>

```text
Web search results for query: "linear probe expressiveness limitations selectivity probing NLP 2020 2021 2022"

Links: [{"title":"Linear Probes: Neural Network Diagnostics","url":"https://www.emergentmind.com/topics/linear-probes"},{"title":"Trustworthy AI: Validity, Fairness, Explainability, and Uncertainty Assessments: Explainability methods: Linear Probes","url":"https://carpentries-incubator.github.io/fair-explainable-ml/5c-probes.html"},{"title":"Probing for Labeled Dependency Trees","url":"https://arxiv.org/pdf/2203.12971"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"},{"title":"Probing Classifiers: Promises, Shortcomings, and Advances","url":"https://arxiv.org/pdf/2102.12452"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://aclanthology.org/D19-1275.pdf"},{"title":"Probing Classifiers: Decoding What Language Models Learn - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/probing-classifiers"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"Linguistics Wisdom of NLP Models | Towards Data Science","url":"https://towardsdatascience.com/linguistics-wisdom-of-nlp-models-8c8554bc8c66/"},{"title":"Interventional Probing in High Dimensions: An NLI Case Study","url":"https://arxiv.org/pdf/2304.10346"}]

Based on the search results, here's what I found regarding linear probe expressiveness limitations and selectivity probing in NLP:

## Key Findings on Linear Probes and Selectivity

Linear probes tend to have high selectivity, while non-linear probes tend to have low selectivity. This is a crucial distinction in probing methodology. Linear probes reveal only linearly accessible structure; non-linear phenomena remain invisible unless more expressive probes are used, though these introduce interpretability trade-offs.

## The Expressiveness-Selectivity Tradeoff

An important paper in this area is "Designing and Interpreting Probes with Control Tasks" (2019). A linear probe on part-of-speech tagging achieves similar 97.2 accuracy and 71.2 control task accuracy, for 26.0 selectivity, suggesting that the small accuracy gain of the MLP may be explained by increased probe expressivity. 

With popular hyperparameter settings, MLP probes achieve very low selectivity, suggesting caution in interpreting how their results reflect properties of representations.

## Selectivity as a Diagnostic Tool

Selectivity is proposed to be used for building intuition about the expressivity of probes and the properties of models, putting probing accuracies into richer context. High selectivity from a linear probe indicates features are truly encoded in representation, rather than artifacts of the probe.

## Design Challenges

One large challenge in using probes is identifying the correct architectural design of the probe - too simple, and it may not be able to learn the downstream task at all; too complex, and it may be able to learn the task even if the model does not contain the information required to make the prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "73188b93-9d9b-47d3-b267-f2faee62bb49",
  "tool_use_result": {
    "query": "linear probe expressiveness limitations selectivity probing NLP 2020 2021 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QMb5wKGx4sGTWJwmhGaur3",
        "content": [
          {
            "title": "Linear Probes: Neural Network Diagnostics",
            "url": "https://www.emergentmind.com/topics/linear-probes"
          },
          {
            "title": "Trustworthy AI: Validity, Fairness, Explainability, and Uncertainty Assessments: Explainability methods: Linear Probes",
            "url": "https://carpentries-incubator.github.io/fair-explainable-ml/5c-probes.html"
          },
          {
            "title": "Probing for Labeled Dependency Trees",
            "url": "https://arxiv.org/pdf/2203.12971"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks John Hewitt",
            "url": "https://nlp.stanford.edu/pubs/hewitt2019control.pdf"
          },
          {
            "title": "Probing Classifiers: Promises, Shortcomings, and Advances",
            "url": "https://arxiv.org/pdf/2102.12452"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://aclanthology.org/D19-1275.pdf"
          },
          {
            "title": "Probing Classifiers: Decoding What Language Models Learn - Interactive | Michael Brenndoerfer | Michael Brenndoerfer",
            "url": "https://mbrenndoerfer.com/writing/probing-classifiers"
          },
          {
            "title": "Designing and Interpreting Probes · John Hewitt",
            "url": "https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"
          },
          {
            "title": "Linguistics Wisdom of NLP Models | Towards Data Science",
            "url": "https://towardsdatascience.com/linguistics-wisdom-of-nlp-models-8c8554bc8c66/"
          },
          {
            "title": "Interventional Probing in High Dimensions: An NLI Case Study",
            "url": "https://arxiv.org/pdf/2304.10346"
          }
        ]
      },
      "Based on the search results, here's what I found regarding linear probe expressiveness limitations and selectivity probing in NLP:\n\n## Key Findings on Linear Probes and Selectivity\n\nLinear probes tend to have high selectivity, while non-linear probes tend to have low selectivity. This is a crucial distinction in probing methodology. Linear probes reveal only linearly accessible structure; non-linear phenomena remain invisible unless more expressive probes are used, though these introduce interpretability trade-offs.\n\n## The Expressiveness-Selectivity Tradeoff\n\nAn important paper in this area is \"Designing and Interpreting Probes with Control Tasks\" (2019). A linear probe on part-of-speech tagging achieves similar 97.2 accuracy and 71.2 control task accuracy, for 26.0 selectivity, suggesting that the small accuracy gain of the MLP may be explained by increased probe expressivity. \n\nWith popular hyperparameter settings, MLP probes achieve very low selectivity, suggesting caution in interpreting how their results reflect properties of representations.\n\n## Selectivity as a Diagnostic Tool\n\nSelectivity is proposed to be used for building intuition about the expressivity of probes and the properties of models, putting probing accuracies into richer context. High selectivity from a linear probe indicates features are truly encoded in representation, rather than artifacts of the probe.\n\n## Design Challenges\n\nOne large challenge in using probes is identifying the correct architectural design of the probe - too simple, and it may not be able to learn the downstream task at all; too complex, and it may be able to learn the task even if the model does not contain the information required to make the prediction."
    ],
    "durationSeconds": 9.051177838
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the two MUST CITE papers. Now let me search for more specific papers to fill the gaps. I need:

For Cluster 3 (Cross-lingual Representations):
1. ✅ Conneau et al. 2020 - Found (ACL 2020)
2. Need more on multilingual model internal representation analysis - let me look at specific papers
3. Need English-centric bias paper - "Beyond English-Centric LLMs: What Language Do Multilingual Language Models Think in?" looks relevant


4. Looking for another cross-lingual alignment paper to round out this cluster

For Cluster 4 (Probing Methodology):
1. ✅ Belinkov 2022 - Found (Computational Linguistics)
2. ✅ Hewitt & Liang 2019 on probe selectivity and control tasks - that's the critical limitations paper
3. Still need to track down the bootstrap confidence interval paper
4. Might add one more methodology paper if I find something particularly relevant

Let me dig deeper into the literature for these remaining gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "68255aa1-67fe-4fbc-9b35-61a6d71d5913",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqHTiqEJH7nDQ4kNDwNT7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 29351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4587
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

_source line 25_

找到两篇 MUST CITE。继续搜索补充论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "5ba49bae-7f3e-44b8-b801-163e831898ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqHTiqEJH7nDQ4kNDwNT7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 29351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4587
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BL7HSU42H1QoCQSNYR96xV`</summary>

```json
{
  "query": "Wendler et al 2024 \"Do Multilingual LLMs Think in English\" arxiv multilingual internal representations pivot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "87d3c7b3-2a85-4bc1-9c56-03070942ce55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqHTiqEJH7nDQ4kNDwNT7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 29351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4587
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NAej2afWDZUysENMeqNHoW`</summary>

```json
{
  "query": "Hewitt Liang 2019 \"Designing and Interpreting Probes with Control Tasks\" EMNLP selectivity"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "18864f74-8b22-4149-a306-fef7f85a1e2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqHTiqEJH7nDQ4kNDwNT7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 29351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4587
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PpC1PMWD4H8iwySBGvwd2X`</summary>

```json
{
  "query": "MEXA \"Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment\" 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "7d75517b-6598-47c2-a026-0c4cf55a3201",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqHTiqEJH7nDQ4kNDwNT7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 29351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4587
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EVibNvFhLDx1w5Pv3iecH9`</summary>

```json
{
  "query": "Muller et al \"cross-lingual alignment multilingual BERT representations\" 2021 2022 layer CKA probing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "f13e9cf2-1722-48c7-a40e-24f20f3e7fa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GqHTiqEJH7nDQ4kNDwNT7T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 643,
      "cache_creation_input_tokens": 4587,
      "cache_read_input_tokens": 29351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4587
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

_source line 30 · 2026-05-22T13:45:18.182Z_

<details><summary>↩ Tool result · `toolu_01NAej2afWDZUysENMeqNHoW`</summary>

```text
Web search results for query: "Hewitt Liang 2019 "Designing and Interpreting Probes with Control Tasks" EMNLP selectivity"

Links: [{"title":"Designing and Interpreting Probes with Control Tasks - ACL Anthology","url":"https://aclanthology.org/D19-1275/"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"},{"title":"Designing and Interpreting Probes with Control Tasks | papers_we_read","url":"https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"},{"title":"Designing and Interpreting Probes · John Hewitt","url":"https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"},{"title":"[1909.03368] Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/abs/1909.03368"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://www.researchgate.net/publication/335713697_Designing_and_Interpreting_Probes_with_Control_Tasks"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://arxiv.org/pdf/1909.03368"},{"title":"[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"},{"title":"Designing and Interpreting Probes with Control Tasks","url":"https://aclanthology.org/D19-1275.pdf"},{"title":"Designing and Interpreting Probes with Control Tasks John Hewitt","url":"https://nlp.stanford.edu/pubs/hewitt2019control.pdf"}]

I found the paper! Here's what the search results show:

"Designing and Interpreting Probes with Control Tasks" was published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) by John Hewitt and Percy Liang, with pages 2733–2743.

The paper received the Best Paper Runner Up Award at EMNLP 2019.

Regarding selectivity, the paper's key contribution is defining this metric: "selectivity = linguistic task accuracy - control task accuracy". A good probe (one that reflects the representation) should be selective, achieving high linguistic task accuracy and low control task accuracy, which puts linguistic task accuracy in context with the probe's capacity to memorize from word types.

The authors constructed control tasks for English part-of-speech tagging and dependency edge prediction, and showed that popular probes on ELMo representations are not selective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "22d1bdc5-7115-4d7a-87c1-962bfa3a1a4a",
  "tool_use_result": {
    "query": "Hewitt Liang 2019 \"Designing and Interpreting Probes with Control Tasks\" EMNLP selectivity",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KqCgmsMqMUiVkgQV4nRTbm",
        "content": [
          {
            "title": "Designing and Interpreting Probes with Control Tasks - ACL Anthology",
            "url": "https://aclanthology.org/D19-1275/"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://bibbase.org/network/publication/hewitt-liang-designingandinterpretingprobeswithcontroltasks-2019"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks | papers_we_read",
            "url": "https://vlgiitr.github.io/papers_we_read/summaries/control_tasks.html"
          },
          {
            "title": "Designing and Interpreting Probes · John Hewitt",
            "url": "https://www.cs.columbia.edu/~johnhew/interpreting-probes.html"
          },
          {
            "title": "[1909.03368] Designing and Interpreting Probes with Control Tasks",
            "url": "https://arxiv.org/abs/1909.03368"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://www.researchgate.net/publication/335713697_Designing_and_Interpreting_Probes_with_Control_Tasks"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://arxiv.org/pdf/1909.03368"
          },
          {
            "title": "[PDF] Designing and Interpreting Probes with Control Tasks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Designing-and-Interpreting-Probes-with-Control-Hewitt-Liang/199ff73d2f728e997f860b62a2322823d3e3d9e8"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks",
            "url": "https://aclanthology.org/D19-1275.pdf"
          },
          {
            "title": "Designing and Interpreting Probes with Control Tasks John Hewitt",
            "url": "https://nlp.stanford.edu/pubs/hewitt2019control.pdf"
          }
        ]
      },
      "I found the paper! Here's what the search results show:\n\n\"Designing and Interpreting Probes with Control Tasks\" was published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) by John Hewitt and Percy Liang, with pages 2733–2743.\n\nThe paper received the Best Paper Runner Up Award at EMNLP 2019.\n\nRegarding selectivity, the paper's key contribution is defining this metric: \"selectivity = linguistic task accuracy - control task accuracy\". A good probe (one that reflects the representation) should be selective, achieving high linguistic task accuracy and low control task accuracy, which puts linguistic task accuracy in context with the probe's capacity to memorize from word types.\n\nThe authors constructed control tasks for English part-of-speech tagging and dependency edge prediction, and showed that popular probes on ELMo representations are not selective."
    ],
    "durationSeconds": 5.484130169000004
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T13:45:19.155Z_

<details><summary>↩ Tool result · `toolu_01BL7HSU42H1QoCQSNYR96xV`</summary>

```text
Web search results for query: "Wendler et al 2024 "Do Multilingual LLMs Think in English" arxiv multilingual internal representations pivot"

Links: [{"title":"Improving Multilingual Language Models by Aligning Representations through Steering","url":"https://arxiv.org/html/2505.12584v1"},{"title":"arXiv:2506.09890v1 [cs.CL] 11 Jun 2025","url":"https://www.arxiv.org/pdf/2506.09890"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"},{"title":"Quantifying Multilingual Performance of Large Language Models Across Languages","url":"https://arxiv.org/html/2404.11553v2"},{"title":"Do Multilingual LLMs Think In English?","url":"https://arxiv.org/html/2502.15603v1"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/html/2504.09378v1"},{"title":"Do Large Language Models Have an English “Accent”? Evaluating and Improving the Naturalness of Multilingual LLMs","url":"https://arxiv.org/html/2410.15956"},{"title":"Lens: Rethinking Multilingual Enhancement for Large Language Models","url":"https://arxiv.org/html/2410.04407v1"},{"title":"Continually Adding New Languages to Multilingual Language Models","url":"https://arxiv.org/html/2509.11414v1"},{"title":"GitHub - tjunlp-lab/Awesome-Multilingual-LLMs-Papers: Awesome-Multilingual-LLMs-Papers · GitHub","url":"https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers"}]

Based on the search results, I found the paper you're looking for:

The paper by Wendler et al. (2024) is titled "Do llamas work in English? On the latent language of multilingual transformers" and was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics in August 2024.

The key findings of this research include:

1. **English as an internal pivot language**: Wendler et al. (2024) found that for Llama 2, an English-centric LLM, English could be seen as a kind of "pivot" language, enabling to solve complex semantic tasks in a foreign language through a detour into English.

2. **Implicit pivoting through English representations**: Wendler et al. (2024) extended earlier work by using early decoding of intermediate layer residuals to reveal that Anglocentric LLMs implicitly pivot through English representations when processing non-English text.

3. **Contrast with other research perspectives**: This work studies single token context, contrasting with later work that found evidence for language-specific spaces in open-ended multi-token language generation.

The research demonstrates how multilingual LLMs maintain an English-centric internal representation space, supporting the hypothesis that these models use English as an internal language for processing non-English inputs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "f70785cc-b5ae-4e35-bb22-d290711841b9",
  "tool_use_result": {
    "query": "Wendler et al 2024 \"Do Multilingual LLMs Think in English\" arxiv multilingual internal representations pivot",
    "results": [
      {
        "tool_use_id": "srvtoolu_01L8ddHRf1qBEwvdzo5jMBrg",
        "content": [
          {
            "title": "Improving Multilingual Language Models by Aligning Representations through Steering",
            "url": "https://arxiv.org/html/2505.12584v1"
          },
          {
            "title": "arXiv:2506.09890v1 [cs.CL] 11 Jun 2025",
            "url": "https://www.arxiv.org/pdf/2506.09890"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via ...",
            "url": "https://arxiv.org/pdf/2410.05873"
          },
          {
            "title": "Quantifying Multilingual Performance of Large Language Models Across Languages",
            "url": "https://arxiv.org/html/2404.11553v2"
          },
          {
            "title": "Do Multilingual LLMs Think In English?",
            "url": "https://arxiv.org/html/2502.15603v1"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/html/2504.09378v1"
          },
          {
            "title": "Do Large Language Models Have an English “Accent”? Evaluating and Improving the Naturalness of Multilingual LLMs",
            "url": "https://arxiv.org/html/2410.15956"
          },
          {
            "title": "Lens: Rethinking Multilingual Enhancement for Large Language Models",
            "url": "https://arxiv.org/html/2410.04407v1"
          },
          {
            "title": "Continually Adding New Languages to Multilingual Language Models",
            "url": "https://arxiv.org/html/2509.11414v1"
          },
          {
            "title": "GitHub - tjunlp-lab/Awesome-Multilingual-LLMs-Papers: Awesome-Multilingual-LLMs-Papers · GitHub",
            "url": "https://github.com/tjunlp-lab/Awesome-Multilingual-LLMs-Papers"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper by Wendler et al. (2024) is titled \"Do llamas work in English? On the latent language of multilingual transformers\" and was published in the Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics in August 2024.\n\nThe key findings of this research include:\n\n1. **English as an internal pivot language**: Wendler et al. (2024) found that for Llama 2, an English-centric LLM, English could be seen as a kind of \"pivot\" language, enabling to solve complex semantic tasks in a foreign language through a detour into English.\n\n2. **Implicit pivoting through English representations**: Wendler et al. (2024) extended earlier work by using early decoding of intermediate layer residuals to reveal that Anglocentric LLMs implicitly pivot through English representations when processing non-English text.\n\n3. **Contrast with other research perspectives**: This work studies single token context, contrasting with later work that found evidence for language-specific spaces in open-ended multi-token language generation.\n\nThe research demonstrates how multilingual LLMs maintain an English-centric internal representation space, supporting the hypothesis that these models use English as an internal language for processing non-English inputs."
    ],
    "durationSeconds": 6.4643416
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-22T13:45:21.092Z_

<details><summary>↩ Tool result · `toolu_01PpC1PMWD4H8iwySBGvwd2X`</summary>

```text
Web search results for query: "MEXA "Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment" 2024 arxiv"

Links: [{"title":"[Literature Review] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.themoonlight.io/en/review/mexa-multilingual-evaluation-of-english-centric-llms-via-cross-lingual-alignment"},{"title":"Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | OpenReview","url":"https://openreview.net/forum?id=hsMkpzr9Oy"},{"title":"GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://github.com/cisnlp/MEXA"},{"title":"Paper page - MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://huggingface.co/papers/2410.05873"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment_国家预印本平台","url":"https://sinoxiv.napstic.cn/article/10967125"},{"title":"[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/abs/2410.05873"},{"title":"(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/html/2410.05873v1"},{"title":"Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs","url":"https://arxiv.org/html/2504.09378v1"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"}]

Based on the search results, here's information about the MEXA paper:

## Overview

MEXA is a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, which are available for more languages than existing downstream tasks.

## Key Innovation

MEXA leverages that English-centric LLMs use English as a pivot language in their intermediate layers, and computes the alignment between English and non-English languages using parallel sentences to evaluate the transfer of language understanding from English to other languages.

## Publication Details

The paper is authored by Amir Hossein Kargaran, Ali Modarressi, Nafiseh Nikeghbal, Jana Diesner, François Yvon, and Hinrich Schütze, published on arXiv as preprint arXiv:2410.05873 in 2024.

## Results

MEXA achieves a statistically significant average Pearson correlation of 0.90 with three established downstream tasks across nine models and two parallel datasets.

## Resources

A leaderboard and code are available at https://huggingface.co/spaces/cis-lmu/Mexa and https://github.com/cisnlp/Mexa respectively.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "a93f03d4-2b5e-4f51-8688-a8011deeaae8",
  "tool_use_result": {
    "query": "MEXA \"Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment\" 2024 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bz9qGDewPJTQAjwBF2Br7G",
        "content": [
          {
            "title": "[Literature Review] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://www.themoonlight.io/en/review/mexa-multilingual-evaluation-of-english-centric-llms-via-cross-lingual-alignment"
          },
          {
            "title": "Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | OpenReview",
            "url": "https://openreview.net/forum?id=hsMkpzr9Oy"
          },
          {
            "title": "GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://github.com/cisnlp/MEXA"
          },
          {
            "title": "Paper page - MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://huggingface.co/papers/2410.05873"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment_国家预印本平台",
            "url": "https://sinoxiv.napstic.cn/article/10967125"
          },
          {
            "title": "[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://arxiv.org/abs/2410.05873"
          },
          {
            "title": "(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"
          },
          {
            "title": "Mexa: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://arxiv.org/html/2410.05873v1"
          },
          {
            "title": "Can you map it to English? The Role of Cross-Lingual Alignment in Multilingual Performance of LLMs",
            "url": "https://arxiv.org/html/2504.09378v1"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via ...",
            "url": "https://arxiv.org/pdf/2410.05873"
          }
        ]
      },
      "Based on the search results, here's information about the MEXA paper:\n\n## Overview\n\nMEXA is a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, which are available for more languages than existing downstream tasks.\n\n## Key Innovation\n\nMEXA leverages that English-centric LLMs use English as a pivot language in their intermediate layers, and computes the alignment between English and non-English languages using parallel sentences to evaluate the transfer of language understanding from English to other languages.\n\n## Publication Details\n\nThe paper is authored by Amir Hossein Kargaran, Ali Modarressi, Nafiseh Nikeghbal, Jana Diesner, François Yvon, and Hinrich Schütze, published on arXiv as preprint arXiv:2410.05873 in 2024.\n\n## Results\n\nMEXA achieves a statistically significant average Pearson correlation of 0.90 with three established downstream tasks across nine models and two parallel datasets.\n\n## Resources\n\nA leaderboard and code are available at https://huggingface.co/spaces/cis-lmu/Mexa and https://github.com/cisnlp/Mexa respectively."
    ],
    "durationSeconds": 7.143266121000001
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-22T13:45:22.337Z_

<details><summary>↩ Tool result · `toolu_01EVibNvFhLDx1w5Pv3iecH9`</summary>

```text
Web search results for query: "Muller et al "cross-lingual alignment multilingual BERT representations" 2021 2022 layer CKA probing"

Links: [{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF","url":"https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"},{"title":"(PDF) Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://www.researchgate.net/publication/366027168_Cross-lingual_Similarity_of_Multilingual_Representations_Revisited"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Paper to HTML | Allen Institute for AI","url":"https://a11y2.apps.allenai.org/paper?id=1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"},{"title":"Probing the Emergence of Cross-lingual Alignment during LLM Training","url":"https://arxiv.org/html/2406.13229v1"},{"title":"[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://arxiv.org/abs/2101.11109"},{"title":"Cross-lingual Similarity of Multilingual Representations Revisited","url":"https://arxiv.org/pdf/2212.01924"},{"title":"Probing Multilingual Sentence Representations With X-Probe","url":"https://arxiv.org/pdf/1906.05061"}]

The search has returned results related to the Muller et al. work on cross-lingual alignment in multilingual BERT. Here's what I found:

The key paper is "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT" by Benjamin Muller, Yanai Elazar, Benoît Sagot, and Djamé Seddah (2021).

The research focuses on understanding how multilingual BERT achieves zero-shot cross-lingual transfer. Using CKA and behavior analysis, Muller et al. (2021) demonstrated that language representations align with network depth, and representations first converge towards language neutrality and then recover some language-specificity.

The study used the Central Kernel Alignment (CKA) metric, which was introduced by Kornblith et al. (2019), to measure the similarities of representations across languages in pretrained and fine-tuned multilingual models.

Additionally, a follow-up study (2022) on "Cross-lingual Similarity of Multilingual Representations Revisited" captures the "first align, then translate" pattern presented in Muller et al. (2021), though it also critiques some limitations of the CKA approach for cross-lingual analysis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "118e1e62-012e-4f38-a710-5f0aeb121836",
  "tool_use_result": {
    "query": "Muller et al \"cross-lingual alignment multilingual BERT representations\" 2021 2022 layer CKA probing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VAvWP8XoW3eCYVdiZngYaW",
        "content": [
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF",
            "url": "https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"
          },
          {
            "title": "(PDF) Cross-lingual Similarity of Multilingual Representations Revisited",
            "url": "https://www.researchgate.net/publication/366027168_Cross-lingual_Similarity_of_Multilingual_Representations_Revisited"
          },
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Paper to HTML | Allen Institute for AI",
            "url": "https://a11y2.apps.allenai.org/paper?id=1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"
          },
          {
            "title": "Probing the Emergence of Cross-lingual Alignment during LLM Training",
            "url": "https://arxiv.org/html/2406.13229v1"
          },
          {
            "title": "[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT",
            "url": "https://arxiv.org/abs/2101.11109"
          },
          {
            "title": "Cross-lingual Similarity of Multilingual Representations Revisited",
            "url": "https://arxiv.org/pdf/2212.01924"
          },
          {
            "title": "Probing Multilingual Sentence Representations With X-Probe",
            "url": "https://arxiv.org/pdf/1906.05061"
          }
        ]
      },
      "The search has returned results related to the Muller et al. work on cross-lingual alignment in multilingual BERT. Here's what I found:\n\nThe key paper is \"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT\" by Benjamin Muller, Yanai Elazar, Benoît Sagot, and Djamé Seddah (2021).\n\nThe research focuses on understanding how multilingual BERT achieves zero-shot cross-lingual transfer. Using CKA and behavior analysis, Muller et al. (2021) demonstrated that language representations align with network depth, and representations first converge towards language neutrality and then recover some language-specificity.\n\nThe study used the Central Kernel Alignment (CKA) metric, which was introduced by Kornblith et al. (2019), to measure the similarities of representations across languages in pretrained and fine-tuned multilingual models.\n\nAdditionally, a follow-up study (2022) on \"Cross-lingual Similarity of Multilingual Representations Revisited\" captures the \"first align, then translate\" pattern presented in Muller et al. (2021), though it also critiques some limitations of the CKA approach for cross-lingual analysis."
    ],
    "durationSeconds": 7.701244304
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for more specific papers. I need:

For Cluster 3:
1. ✅ Conneau et al. 2020 - "Emerging Cross-lingual Structure in Pretrained Language Models" (ACL 2020) - wu2020emerging
2. Wendler et al. 2024 - "Do Llamas Work in English?" - about English as pivot language, need to get exact details
3. MEXA - Kargaran et al. 2024 - about cross-lingual alignment evaluation
4. Muller et al. 2021 - "First Align, then Predict" - about CKA alignment in mBERT


5. Belinkov 2022 - "Probing Classifiers: Promises, Shortcomings, and Advances" (CL 2022)
6. Hewitt & Liang 2019 - "Designing and Interpreting Probes with Control Tasks" (EMNLP 2019)

I need to track down the exact details for Wendler et al. and find a paper on bootstrap confidence intervals or statistical testing methods for probing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "6829e32a-15ab-497b-8141-59fc4b6df2b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtoZuxuf5LoqXDcnjJyoUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4539,
      "cache_read_input_tokens": 33938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4539
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

继续搜索 Wendler et al. 2024 的准确信息和 bootstrap probing 相关论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "93e7ccb6-5cff-42e8-bdd6-7bded6436cbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtoZuxuf5LoqXDcnjJyoUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4539,
      "cache_read_input_tokens": 33938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4539
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015f8guLvxZesDFrkUUgjLC6`</summary>

```json
{
  "query": "Wendler Veselovsky Flagg Alam West 2024 \"Do Llamas Work in English\" latent language multilingual transformers ACL arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "66a07589-ede7-470b-95d6-44d495a435f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtoZuxuf5LoqXDcnjJyoUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4539,
      "cache_read_input_tokens": 33938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4539
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R2Jt1UjKXuNxXSeBL47JDU`</summary>

```json
{
  "query": "Ulmer et al 2022 \"deep-significance\" bootstrap statistical testing NLP probing confidence interval arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "a872c7ce-7232-4c05-8e9a-05d9cf5071d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RtoZuxuf5LoqXDcnjJyoUE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4539,
      "cache_read_input_tokens": 33938,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4539
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

_source line 38 · 2026-05-22T13:45:49.223Z_

<details><summary>↩ Tool result · `toolu_01R2Jt1UjKXuNxXSeBL47JDU`</summary>

```text
Web search results for query: "Ulmer et al 2022 "deep-significance" bootstrap statistical testing NLP probing confidence interval arxiv"

Links: [{"title":"deep-significance: Easy and Better Significance Testing for Deep Neural Networks — deep-significance 1.2.5 documentation","url":"https://deep-significance.readthedocs.io/"},{"title":"[PDF] deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/deep-significance-Easy-and-Meaningful-Statistical-Ulmer-Hardmeier/bcef143c672029431c316fe40235671879827aa7"},{"title":"(PDF) deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks","url":"https://www.researchgate.net/publication/359971291_deep-significance_-_Easy_and_Meaningful_Statistical_Significance_Testing_in_the_Age_of_Neural_Networks"},{"title":"GitHub - Kaleidophon/deep-significance: Enabling easy statistical significance testing for deep neural networks. · GitHub","url":"https://github.com/Kaleidophon/deep-significance"},{"title":"[2204.06815v1] deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks","url":"https://arxiv.org/abs/2204.06815v1"},{"title":"Predicting Fine-Tuning Performance with Probing","url":"https://arxiv.org/pdf/2210.07352"},{"title":"Statistical Significance Tests in NLP | by Sudhanva Savyasachi S | Medium","url":"https://sudhanvaiitr.medium.com/statistical-significance-tests-in-nlp-313ad69cc57a"},{"title":"Please, Don't Forget the Difference and the Confidence Interval when   Seeking for the State-of-the-Art Status","url":"https://arxiv.org/pdf/2205.11134"}]

Based on the search results, I found the relevant paper:

The paper "deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks" was authored by Dennis Ulmer, Christian Hardmeier, and Jes Frellsen and published on arXiv in 2022 (arxiv:2204.06815). The paper provides an easy-to-use package containing different significance tests and utility functions specifically tailored towards research needs and usability.

The research addresses statistical significance testing methodologies for neural networks. The paper discusses approaches like Almost Stochastic Order (ASO), which uses cumulative distribution functions to express bounds on model superiority, with smaller values indicating greater certainty in model superiority.

You can access the paper directly at: https://arxiv.org/abs/2204.06815v1


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "6fe6bcdc-9376-414a-a7df-eb637cd8e282",
  "tool_use_result": {
    "query": "Ulmer et al 2022 \"deep-significance\" bootstrap statistical testing NLP probing confidence interval arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_015SZma98tHQmUrrnFatD8z4",
        "content": [
          {
            "title": "deep-significance: Easy and Better Significance Testing for Deep Neural Networks — deep-significance 1.2.5 documentation",
            "url": "https://deep-significance.readthedocs.io/"
          },
          {
            "title": "[PDF] deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/deep-significance-Easy-and-Meaningful-Statistical-Ulmer-Hardmeier/bcef143c672029431c316fe40235671879827aa7"
          },
          {
            "title": "(PDF) deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks",
            "url": "https://www.researchgate.net/publication/359971291_deep-significance_-_Easy_and_Meaningful_Statistical_Significance_Testing_in_the_Age_of_Neural_Networks"
          },
          {
            "title": "GitHub - Kaleidophon/deep-significance: Enabling easy statistical significance testing for deep neural networks. · GitHub",
            "url": "https://github.com/Kaleidophon/deep-significance"
          },
          {
            "title": "[2204.06815v1] deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks",
            "url": "https://arxiv.org/abs/2204.06815v1"
          },
          {
            "title": "Predicting Fine-Tuning Performance with Probing",
            "url": "https://arxiv.org/pdf/2210.07352"
          },
          {
            "title": "Statistical Significance Tests in NLP | by Sudhanva Savyasachi S | Medium",
            "url": "https://sudhanvaiitr.medium.com/statistical-significance-tests-in-nlp-313ad69cc57a"
          },
          {
            "title": "Please, Don't Forget the Difference and the Confidence Interval when   Seeking for the State-of-the-Art Status",
            "url": "https://arxiv.org/pdf/2205.11134"
          }
        ]
      },
      "Based on the search results, I found the relevant paper:\n\nThe paper \"deep-significance - Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks\" was authored by Dennis Ulmer, Christian Hardmeier, and Jes Frellsen and published on arXiv in 2022 (arxiv:2204.06815). The paper provides an easy-to-use package containing different significance tests and utility functions specifically tailored towards research needs and usability.\n\nThe research addresses statistical significance testing methodologies for neural networks. The paper discusses approaches like Almost Stochastic Order (ASO), which uses cumulative distribution functions to express bounds on model superiority, with smaller values indicating greater certainty in model superiority.\n\nYou can access the paper directly at: https://arxiv.org/abs/2204.06815v1"
    ],
    "durationSeconds": 5.566512422999993
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T13:45:51.737Z_

<details><summary>↩ Tool result · `toolu_015f8guLvxZesDFrkUUgjLC6`</summary>

```text
Web search results for query: "Wendler Veselovsky Flagg Alam West 2024 "Do Llamas Work in English" latent language multilingual transformers ACL arxiv"

Links: [{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.820/"},{"title":"[PDF] Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Do-Llamas-Work-in-English-On-the-Latent-Language-of-Wendler-Veselovsky/e88efdfc05d0d8832b2ded7af9c8ececdd03e58d"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Artificial Intelligence Hub","url":"https://aicitta.com/posts/do-llamas-work-in-english/"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Consensus","url":"https://consensus.app/papers/details/b8aa720cd459550191960afe5413d726/"},{"title":"[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers","url":"https://arxiv.org/abs/2402.10588"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual   Transformers","url":"https://arxiv.org/pdf/2402.10588"},{"title":"Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Paper Detail","url":"https://deeplearn.org/arxiv/459055/do-llamas-work-in-english"},{"title":"[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers","url":"https://ar5iv.labs.arxiv.org/html/2402.10588"},{"title":"dblp: Do Llamas Work in English? On the Latent Language of Multilingual Transformers.","url":"https://dblp.org/rec/journals/corr/abs-2402-10588.html"}]

I found the paper you're looking for! Here's the information:

"Do Llamas Work in English? On the Latent Language of Multilingual Transformers" was published by Wendler, Veselovsky, Giovanni Monea, and Robert West at ACL 2024. The paper is available as arXiv preprint arXiv:2402.10588.

The research investigates whether multilingual language models trained on unbalanced, English-dominated corpora use English as an internal pivot language—a question important for understanding how language models function and the origins of linguistic bias. Focusing on the Llama-2 family of transformer models, the study is based on carefully constructed non-English prompts with a unique correct single-token continuation.

The findings reveal three distinct phases in intermediate embeddings: they start far away from output token embeddings; already allow for decoding a semantically correct next token in middle layers but give higher probability to its version in English than in the input language; and finally move into an input-language-specific region of the embedding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "4176457b-f3fb-4a00-90a5-aaf1b28d5a0d",
  "tool_use_result": {
    "query": "Wendler Veselovsky Flagg Alam West 2024 \"Do Llamas Work in English\" latent language multilingual transformers ACL arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Mc9zxPiDxsgA7fPqeVnRF9",
        "content": [
          {
            "title": "Do Llamas Work in English? On the Latent Language of Multilingual Transformers - ACL Anthology",
            "url": "https://aclanthology.org/2024.acl-long.820/"
          },
          {
            "title": "[PDF] Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Do-Llamas-Work-in-English-On-the-Latent-Language-of-Wendler-Veselovsky/e88efdfc05d0d8832b2ded7af9c8ececdd03e58d"
          },
          {
            "title": "Do Llamas Work in English? On the Latent Language of Multilingual Transformers | Artificial Intelligence Hub",
            "url": "https://aicitta.com/posts/do-llamas-work-in-english/"
          },
          {
            "title": "Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Consensus",
            "url": "https://consensus.app/papers/details/b8aa720cd459550191960afe5413d726/"
          },
          {
            "title": "[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers",
            "url": "https://arxiv.org/abs/2402.10588"
          },
          {
            "title": "Do Llamas Work in English? On the Latent Language of Multilingual   Transformers",
            "url": "https://arxiv.org/pdf/2402.10588"
          },
          {
            "title": "Do Llamas Work in English? On the Latent Language of Multilingual Transformers - Paper Detail",
            "url": "https://deeplearn.org/arxiv/459055/do-llamas-work-in-english"
          },
          {
            "title": "[2402.10588] Do Llamas Work in English? On the Latent Language of Multilingual Transformers",
            "url": "https://ar5iv.labs.arxiv.org/html/2402.10588"
          },
          {
            "title": "dblp: Do Llamas Work in English? On the Latent Language of Multilingual Transformers.",
            "url": "https://dblp.org/rec/journals/corr/abs-2402-10588.html"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information:\n\n\"Do Llamas Work in English? On the Latent Language of Multilingual Transformers\" was published by Wendler, Veselovsky, Giovanni Monea, and Robert West at ACL 2024. The paper is available as arXiv preprint arXiv:2402.10588.\n\nThe research investigates whether multilingual language models trained on unbalanced, English-dominated corpora use English as an internal pivot language—a question important for understanding how language models function and the origins of linguistic bias. Focusing on the Llama-2 family of transformer models, the study is based on carefully constructed non-English prompts with a unique correct single-token continuation.\n\nThe findings reveal three distinct phases in intermediate embeddings: they start far away from output token embeddings; already allow for decoding a semantically correct next token in middle layers but give higher probability to its version in English than in the input language; and finally move into an input-language-specific region of the embedding."
    ],
    "durationSeconds": 8.255300919000002
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough papers for both clusters. Let me also search for one more paper on language-independent representation / cross-lingual alignment to strengthen Cluster 3. Let me also verify Conneau 2020 author list more carefully.

Let me compile the papers:

**Cluster 3: Cross-lingual Representations (need 4)**

1. **Conneau / Wu et al. 2020** - "Emerging Cross-lingual Structure in Pretrained Language Models" (ACL 2020)
   - Authors: Shijie Wu, Alexis Conneau (wait, need to check - the paper on ACL Anthology says authors are... let me check)
   - Actually, I'm finding this paper on ACL Anthology at https://aclanthology.org/2020.acl-main.536/ with Shijie Wu and Alexis Conneau as authors, published at ACL 2020. This looks like the right paper the user was referring to.
   - I should use Wu as the first author for the bibtex key since that's the convention, though the user cited it as "Conneau et al. 2020" — both are key authors on this work about cross-lingual structure in pretrained models.

Now I'm moving on to the second paper, which is the Wendler et al. 2024 ACL paper about the latent language properties of multilingual transformers.

For the third paper, I'm looking at the MEXA paper from 2024 that evaluates English-centric LLMs across languages. I need to verify whether this was published at a conference or is still on arXiv, since the venue information isn't immediately clear to me.

Now I'm thinking through which papers would best address the user's specific needs around mid-layer cross-lingual alignment, layer-wise analysis techniques like CKA, and English-centric bias. Wu & Conneau's 2020 work on cross-lingual structure is essential, and Wendler et al. 2024 on English as a pivot language fits well. For the methodology side, Muller et al. 2021 provides the CKA analysis framework, and Kargaran et al. 2024 directly tackles English-centric alignment evaluation. I should also include Belinkov's 2022 work on probing methodology to round out the methodological foundations.

For the probing cluster, I'm pulling together key papers on how to properly design and evaluate probing classifiers. Hewitt & Liang 2019 is crucial for understanding control tasks and avoiding spurious correlations, and Ulmer et al. 2022 addresses statistical significance testing which is often overlooked in this type of analysis. I've got 7 papers total across the clusters, which hits my target. Now I'm double-checking the venue for Muller et al. 2021 — the search results show it's from arXiv, but I want to confirm whether it was also published at a conference like EACL.

Before I finalize everything in the YAML, I should run through a quick verification of the authorship and publication venues for all the papers to make sure I have the details right.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "2497b32b-1dc6-4bc1-9c8e-b21750f0c335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KMqiSCXFSQtgiVUef7oRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 38477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

_source line 41_

确认 Muller et al. 2021 和 MEXA 的 venue 信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "5916298f-4095-4bfa-8a95-fb9ad5fb5623",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KMqiSCXFSQtgiVUef7oRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 38477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_014A3mgRDaK1Mo6vMh2fFiHx`</summary>

```json
{
  "query": "Muller Elazar Sagot Seddah 2021 \"First Align then Predict\" EACL arxiv:2101.11109 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "8d01f8a6-4b04-400c-8ff9-49ddc80955ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KMqiSCXFSQtgiVUef7oRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 38477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KLipUo8eAFgJ2UVk3YZ12T`</summary>

```json
{
  "query": "Kargaran Modarressi \"MEXA\" 2024 2025 venue EMNLP NAACL accepted conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "1418d8bd-8068-4e9c-999f-264507149f7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KMqiSCXFSQtgiVUef7oRV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 718,
      "cache_creation_input_tokens": 1342,
      "cache_read_input_tokens": 38477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1342
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

_source line 44 · 2026-05-22T13:46:38.276Z_

<details><summary>↩ Tool result · `toolu_014A3mgRDaK1Mo6vMh2fFiHx`</summary>

```text
Web search results for query: "Muller Elazar Sagot Seddah 2021 "First Align then Predict" EACL arxiv:2101.11109 venue"

Links: [{"title":"Main Conference Accepted Papers - EACL 2021","url":"https://2021.eacl.org/program/accepted/"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.189/"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-03239087"},{"title":"GitHub - benjamin-mlr/first-align-then-predict · GitHub","url":"https://github.com/benjamin-mlr/first-align-then-predict"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF","url":"https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"},{"title":"[PDF] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"},{"title":"Figure 5 from First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f/figure/9"},{"title":"[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT","url":"https://arxiv.org/abs/2101.11109"},{"title":"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210111109M/abstract"}]

Based on the search results, I found comprehensive information about this paper:

**Paper Details:**

The paper "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT" was written by Benjamin Muller, Yanai Elazar, Benoît Sagot, and Djamé Seddah, and was published in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume (2021).

**Venue:** EACL 2021 - The 16th Conference of the European Chapter of the Association for Computational Linguistics, held in April 2021 in Kyiv/Virtual, Ukraine.

**ArXiv ID:** The paper has the ArXiv identifier 2101.11109.

**Research Focus:** Using a novel layer ablation technique and analyses of the model's internal representations, the paper shows that multilingual BERT can be viewed as the stacking of two sub-networks: a multilingual encoder followed by a task-specific language-agnostic predictor.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "9498fb4e-2d06-4fa5-aabd-259a4041765b",
  "tool_use_result": {
    "query": "Muller Elazar Sagot Seddah 2021 \"First Align then Predict\" EACL arxiv:2101.11109 venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HTRwomPUeRaNxtXULvZQhP",
        "content": [
          {
            "title": "Main Conference Accepted Papers - EACL 2021",
            "url": "https://2021.eacl.org/program/accepted/"
          },
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ACL Anthology",
            "url": "https://aclanthology.org/2021.eacl-main.189/"
          },
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - Inria - Institut national de recherche en sciences et technologies du numérique",
            "url": "https://inria.hal.science/hal-03239087"
          },
          {
            "title": "GitHub - benjamin-mlr/first-align-then-predict · GitHub",
            "url": "https://github.com/benjamin-mlr/first-align-then-predict"
          },
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Request PDF",
            "url": "https://www.researchgate.net/publication/355434439_First_Align_then_Predict_Understanding_the_Cross-Lingual_Ability_of_Multilingual_BERT"
          },
          {
            "title": "[PDF] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f"
          },
          {
            "title": "Figure 5 from First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/First-Align,-then-Predict:-Understanding-the-of-Muller-Elazar/1cfd0f08bb7ab449bbccc3d69a62ffbf43a7eb7f/figure/9"
          },
          {
            "title": "[2101.11109] First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT",
            "url": "https://arxiv.org/abs/2101.11109"
          },
          {
            "title": "First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv210111109M/abstract"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about this paper:\n\n**Paper Details:**\n\nThe paper \"First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT\" was written by Benjamin Muller, Yanai Elazar, Benoît Sagot, and Djamé Seddah, and was published in the Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics: Main Volume (2021).\n\n**Venue:** EACL 2021 - The 16th Conference of the European Chapter of the Association for Computational Linguistics, held in April 2021 in Kyiv/Virtual, Ukraine.\n\n**ArXiv ID:** The paper has the ArXiv identifier 2101.11109.\n\n**Research Focus:** Using a novel layer ablation technique and analyses of the model's internal representations, the paper shows that multilingual BERT can be viewed as the stacking of two sub-networks: a multilingual encoder followed by a task-specific language-agnostic predictor."
    ],
    "durationSeconds": 4.596285200999992
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-22T13:46:40.660Z_

<details><summary>↩ Tool result · `toolu_01KLipUo8eAFgJ2UVk3YZ12T`</summary>

```text
Web search results for query: "Kargaran Modarressi "MEXA" 2024 2025 venue EMNLP NAACL accepted conference"

Links: [{"title":"[Quick Review] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://liner.com/review/mexa-multilingual-evaluation-englishcentric-llms-via-crosslingual-alignment"},{"title":"GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://github.com/cisnlp/MEXA"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1385/"},{"title":"publications | Amir Hossein Kargaran","url":"https://kargaranamir.github.io/publications/"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF","url":"https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"},{"title":"MEXA: Multilingual Evaluation of English-Centric LLMs via ...","url":"https://arxiv.org/pdf/2410.05873"},{"title":"[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://arxiv.org/abs/2410.05873"},{"title":"(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment","url":"https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"}]

Based on the search results, here's what I found about the MEXA paper by Kargaran and Modarressi:

The MEXA paper by Kargaran et al. (including Ali Modarressi) was accepted to the Findings of the Association for Computational Linguistics: ACL 2025, with the conference held in Vienna, Austria.

The paper is titled "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment."

The paper introduces MEXA, a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, which are available for more languages than existing downstream tasks.

The paper was initially available on arXiv in 2024 (arXiv:2410.05873) before its acceptance to ACL 2025 Findings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "3f66ec5e-c231-472a-ae63-e44c1ffe72b0",
  "tool_use_result": {
    "query": "Kargaran Modarressi \"MEXA\" 2024 2025 venue EMNLP NAACL accepted conference",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HbtBtXLwYHcmUkyenidKTV",
        "content": [
          {
            "title": "[Quick Review] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://liner.com/review/mexa-multilingual-evaluation-englishcentric-llms-via-crosslingual-alignment"
          },
          {
            "title": "GitHub - cisnlp/MEXA: 🔍 Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://github.com/cisnlp/MEXA"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1385/"
          },
          {
            "title": "publications | Amir Hossein Kargaran",
            "url": "https://kargaranamir.github.io/publications/"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/394303914_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"
          },
          {
            "title": "MEXA: Multilingual Evaluation of English-Centric LLMs via ...",
            "url": "https://arxiv.org/pdf/2410.05873"
          },
          {
            "title": "[2410.05873] MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://arxiv.org/abs/2410.05873"
          },
          {
            "title": "(PDF) MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment",
            "url": "https://www.researchgate.net/publication/384771337_MEXA_Multilingual_Evaluation_of_English-Centric_LLMs_via_Cross-Lingual_Alignment"
          }
        ]
      },
      "Based on the search results, here's what I found about the MEXA paper by Kargaran and Modarressi:\n\nThe MEXA paper by Kargaran et al. (including Ali Modarressi) was accepted to the Findings of the Association for Computational Linguistics: ACL 2025, with the conference held in Vienna, Austria.\n\nThe paper is titled \"MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment.\"\n\nThe paper introduces MEXA, a method for assessing the multilingual capabilities of pre-trained English-centric LLMs using parallel sentences, which are available for more languages than existing downstream tasks.\n\nThe paper was initially available on arXiv in 2024 (arXiv:2410.05873) before its acceptance to ACL 2025 Findings."
    ],
    "durationSeconds": 6.168514058
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also verify the Wu & Conneau 2020 paper authors more carefully.

From the search results:
- ACL Anthology: https://aclanthology.org/2020.acl-main.536/
- The paper: "Emerging Cross-lingual Structure in Pretrained Language Models" - Shijie Wu and Mark Dredze, ACL 2020

Wait, actually, looking at the Semantic Scholar result more carefully: "Emerging Cross-lingual Structure in Pretrained Language Models" by Wu and Conneau. 

But I need to double-check the ACL Anthology page directly. The search description lists the authors as Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov, which is different from what I initially thought. I'm trying to pin down whether this is one paper with multiple author orderings or actually two separate papers—the Conneau et al. work on "Emerging Cross-lingual Structure" seems to be the same paper I found on arXiv, but I want to verify the exact author list and publication details before moving forward. I'm checking the author order more carefully—the Semantic Scholar URL shows "Wu-Conneau" but the actual paper lists Conneau first, so I'll use Conneau as the primary author for the citation. I'm seeing conflicting information about the author order—the search result lists Conneau first, but the Semantic Scholar URL suggests Wu is the first author based on the naming convention. Let me verify this against the ACL Anthology page directly since that's the authoritative source. I'm noticing the arxiv ID points to a 2019 preprint that was published at ACL 2020, and the URL structure suggests Wu is the first author with Conneau as second. I should double-check against the ACL Anthology to confirm the exact author order and make sure I'm not mixing up two different papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "5073b12e-92b5-4949-9e35-1073eaa4d97e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYWZva4XPjkRAaDgRQEHfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4633,
      "cache_read_input_tokens": 39819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4633
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

_source line 47_

验证 Wu/Conneau 2020 的作者顺序。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "d24b436b-602f-4298-a19a-1e1d5ba85cd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYWZva4XPjkRAaDgRQEHfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4633,
      "cache_read_input_tokens": 39819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4633
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mxdu2du6nk88EuceZ3AL7R`</summary>

```json
{
  "query": "site:aclanthology.org \"2020.acl-main.536\" \"Emerging Cross-lingual Structure\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "41c35669-043e-440a-ab17-24971cd2b93e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TYWZva4XPjkRAaDgRQEHfG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4633,
      "cache_read_input_tokens": 39819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4633
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

_source line 49 · 2026-05-22T13:47:30.448Z_

<details><summary>↩ Tool result · `toolu_01Mxdu2du6nk88EuceZ3AL7R`</summary>

```text
Web search results for query: "site:aclanthology.org "2020.acl-main.536" "Emerging Cross-lingual Structure" authors"

Links: [{"title":"Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.536/"},{"title":"Emerging Cross-lingual Structure in Pretrained Language Models","url":"https://arxiv.org/pdf/1911.01464"},{"title":"Addressing Issues of Cross-Linguality in Open-Retrieval Question   Answering Systems For Emergent Domains","url":"https://arxiv.org/pdf/2201.11153"},{"title":"Cross-Lingual Ability of Multilingual Masked Language Models: A Study of   Language Structure","url":"https://arxiv.org/pdf/2203.08430"},{"title":"Crosslingual Structural Priming and the Pre-Training Dynamics of   Bilingual Language Models","url":"https://arxiv.org/pdf/2310.07929"}]

Based on the search results, I found the paper you're looking for. The authors of "Emerging Cross-lingual Structure in Pretrained Language Models" are Shijie Wu, Alexis Conneau, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov. 

Shijie Wu is from the Department of Computer Science at Johns Hopkins University, while Alexis Conneau, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov are from Facebook AI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "e8ae3feb-a60e-4147-a8bc-3f37b8292a1c",
  "tool_use_result": {
    "query": "site:aclanthology.org \"2020.acl-main.536\" \"Emerging Cross-lingual Structure\" authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RXKGYjcNqXRhwEpqWABXUn",
        "content": [
          {
            "title": "Emerging Cross-lingual Structure in Pretrained Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2020.acl-main.536/"
          },
          {
            "title": "Emerging Cross-lingual Structure in Pretrained Language Models",
            "url": "https://arxiv.org/pdf/1911.01464"
          },
          {
            "title": "Addressing Issues of Cross-Linguality in Open-Retrieval Question   Answering Systems For Emergent Domains",
            "url": "https://arxiv.org/pdf/2201.11153"
          },
          {
            "title": "Cross-Lingual Ability of Multilingual Masked Language Models: A Study of   Language Structure",
            "url": "https://arxiv.org/pdf/2203.08430"
          },
          {
            "title": "Crosslingual Structural Priming and the Pre-Training Dynamics of   Bilingual Language Models",
            "url": "https://arxiv.org/pdf/2310.07929"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. The authors of \"Emerging Cross-lingual Structure in Pretrained Language Models\" are Shijie Wu, Alexis Conneau, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov. \n\nShijie Wu is from the Department of Computer Science at Johns Hopkins University, while Alexis Conneau, Haoran Li, Luke Zettlemoyer, and Veselin Stoyanov are from Facebook AI."
    ],
    "durationSeconds": 8.559434546000004
  }
}
```

</details>

---

### Assistant

_source line 50_

<details><summary>Logged reasoning block</summary>

```text
OK, so the correct authors are:
- Shijie Wu (first author, Johns Hopkins)
- Alexis Conneau (Facebook AI)
- Haoran Li (Facebook AI)
- Luke Zettlemoyer (Facebook AI)
- Veselin Stoyanov (Facebook AI)

The bibtex key should be wu2020emerging (following first-author convention), but the user referenced it as "Conneau et al. 2020". I'll use the bibtex key `conneau2020emerging` to match the user's citation convention since Conneau is the well-known author associated with this work.


I need to stick with the first-author convention for the bibtex key, so that's `wu2020emerging`. Now I'm checking on the Ulmer et al. 2022 paper venue—the search results show it's on arXiv (2204.06815), and I'm not finding clear evidence of a conference publication, so I'll go with arXiv as the venue.

Looking at the existing YAML structure, using arXiv as a venue is consistent with what's already there. Let me now write out all the papers for this cluster with their full metadata.

For the cross-lingual representations papers, I'm documenting how these works establish foundational understanding of how multilingual models develop shared representational spaces. The Wu et al. paper shows that cross-lingual alignment emerges naturally in the middle layers of pretrained models, which is crucial for understanding the language-agnostic concept spaces I'm investigating. The Wendler et al. work reveals that even English-centric LLMs route information through English representations in their intermediate layers, providing key insights into how these models handle multilingual input.

Now looking at the Muller et al. paper, which uses CKA-based analysis to decompose mBERT into distinct functional components—a multilingual encoder and a language-agnostic predictor. This methodological approach directly informs how I should analyze the conflict signals and their routing through different representational subspaces.

The Kargaran et al. work from 2024 proposes a cross-lingual alignment metric that directly tests the English pivot hypothesis, achieving strong correlation with downstream tasks and providing a concrete evaluation framework for measuring how well English-centric models align across languages.

Now I'm moving into the probing methodology cluster, starting with Belinkov's comprehensive survey that establishes the foundational framework and best practices for probing classifiers—this is essential for justifying our linear probe approach. The next paper by Hewitt introduces control tasks as a methodological refinement to strengthen probing validity. Finishing the URL for that paper, then reconsidering whether deep-significance is the right fit since the user specifically asked for bootstrap CI in NLP probing work. There are other candidates like the LREC 2022 paper on confidence intervals, though deep-significance does get cited frequently in probing studies. I'm sticking with these three papers since they map directly to the user's search targets. Now I need to pull up the existing YAML file to ensure I'm using the correct formatting and structure before adding these entries.

Writing YAML entries...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "257c0c81-8a21-40c2-8c45-1bab7949d869",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oW3UfgVZGeyQGbk3Y9yBF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 44452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2430
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

_source line 51_

所有论文信息已确认。7 篇论文（Cluster 3: 4篇，Cluster 4: 3篇）。现在更新 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "44f67450-2e7c-49b0-b6f6-69934248a1f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oW3UfgVZGeyQGbk3Y9yBF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 44452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2430
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

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01H3FcxNFNqZCcdj1HnJ48g6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "meta:\n  last_updated: '2026-05-22T14:00:00Z'\n  total_papers: 15",
  "new_string": "meta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "f684b378-01c2-4a40-a6f7-6e2c303ffb78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oW3UfgVZGeyQGbk3Y9yBF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2430,
      "cache_read_input_tokens": 44452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2430
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

_source line 53 · 2026-05-22T13:48:28.858Z_

<details><summary>↩ Tool result · `toolu_01H3FcxNFNqZCcdj1HnJ48g6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "b895193c-f4f7-46b6-bb6f-25ee5083aeae",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
    "oldString": "meta:\n  last_updated: '2026-05-22T14:00:00Z'\n  total_papers: 15",
    "newString": "meta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22",
    "originalFile": "categories: []\nmeta:\n  last_updated: '2026-05-22T14:00:00Z'\n  total_papers: 15\npapers:\n  basu2026interpretability:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Basu, S.\n    - et al.\n    bibtex_key: basu2026interpretability\n    category: sae-steering\n    doi: ''\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\n      Critical negative result: defines boundary conditions for when SAE steering\n      works. Our Track 3 design addresses their methodological gaps.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\n      language model errors despite near-perfect internal representations'\n    url: https://arxiv.org/abs/2603.18353\n    venue: arXiv\n    verified: true\n    year: 2026\n  boer2026probing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Boer, A.\n    - Brink, I.\n    - Ulmer, D.\n    bibtex_key: boer2026probing\n    category: probing\n    doi: ''\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\n      F1.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Probing for Knowledge Attribution in Large Language Models\n    url: https://arxiv.org/abs/2602.22787\n    venue: arXiv\n    verified: true\n    year: 2026\n  ifergan2024beneath:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ifergan, M.\n    - Choshen, L.\n    - Aharoni, R.\n    - Szpektor, I.\n    - Abend, O.\n    bibtex_key: ifergan2024beneath\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Shows cross-lingual answer consistency does not imply shared representation;\n      script similarity dominates sharing. Directly motivates our probing approach\n      to test whether conflict signals share representations across languages.\n    role: foundation\n    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge\n      Representation Sharing in LLMs'\n    url: https://arxiv.org/abs/2408.10646\n    venue: Findings of NAACL 2025\n    verified: true\n    year: 2024\n  kialy2026universal:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Kialy, U.Z.\n    - Shtarkberg, A.\n    - Klein, A.\n    bibtex_key: kialy2026universal\n    category: cross-lingual-sae\n    doi: ''\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\n      for register features + zero-shot steering transfer. We test whether this extends\n      to knowledge conflict features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\n      with SAEs\n    url: https://arxiv.org/abs/2603.26236\n    venue: arXiv\n    verified: true\n    year: 2026\n  li2025taming:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, G.\n    - Chen, Y.\n    - Tong, H.\n    bibtex_key: li2025taming\n    category: knowledge-conflict\n    doi: ''\n    relevance: Proposes conflict resolution framework for LLMs. Provides resolution\n      baselines our mechanistic approach complements.\n    role: direct-competitor\n    title: Taming Knowledge Conflicts in Language Models\n    url: https://arxiv.org/abs/2503.10996\n    venue: ICML 2025 (Spotlight)\n    verified: true\n    year: 2025\n  pham2026where:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Pham, M.V.\n    - Borkakoty, H.\n    - Hou, Y.\n    bibtex_key: pham2026where\n    category: conflict-mechanism\n    doi: ''\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\n      for within-parametric conflicts.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\n      Conflict in Language Models'\n    url: https://arxiv.org/abs/2601.09445\n    venue: arXiv\n    verified: true\n    year: 2026\n  team2026qwen:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Qwen Team\n    bibtex_key: team2026qwen\n    category: sae-tools\n    doi: ''\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\n      5.2).\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\n      Models'\n    url: https://arxiv.org/abs/2605.11887\n    venue: arXiv\n    verified: true\n    year: 2026\n  wang2025lost:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wang, M.\n    - Adel, H.\n    - Lange, L.\n    - et al.\n    bibtex_key: wang2025lost\n    category: cross-lingual-mechanism\n    doi: ''\n    relevance: Language-independent concept space through most layers, language-specific\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\n      in Transformer Language Models'\n    url: https://arxiv.org/abs/2504.04264\n    venue: ACL 2025 (SAC Highlights)\n    verified: true\n    year: 2025\n  wong2026langfir:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wong, S.H.\n    - Siddique, A.B.\n    - Sajjad, H.\n    bibtex_key: wong2026langfir\n    category: cross-lingual-sae\n    doi: ''\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\n      Our Track 2 uses this as control to disentangle language-identity from conflict\n      features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\n      Data for Language Steering'\n    url: https://arxiv.org/abs/2604.03532\n    venue: arXiv\n    verified: true\n    year: 2026\n  xie2024adaptive:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xie, J.\n    - Zhang, K.\n    - Chen, J.\n    - Lou, R.\n    - Su, Y.\n    bibtex_key: xie2024adaptive\n    category: knowledge-conflict\n    doi: ''\n    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying\n      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation\n      dataset.\n    role: foundation\n    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large\n      Language Models in Knowledge Conflicts'\n    url: https://arxiv.org/abs/2305.13300\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  xing2024evaluating:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xing, X.\n    - He, Z.\n    - Xu, H.\n    - Wang, X.\n    - Wang, R.\n    - Hong, Y.\n    bibtex_key: xing2024evaluating\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics\n      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation\n      methodology relevant to our cross-lingual conflict measurement.\n    role: peripheral\n    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language\n      Models\n    url: https://arxiv.org/abs/2407.01358\n    venue: arXiv\n    verified: true\n    year: 2024\n  xu2024knowledge:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xu, R.\n    - Qi, Z.\n    - Guo, Z.\n    - Wang, C.\n    - Wang, H.\n    - Zhang, Y.\n    - Xu, W.\n    bibtex_key: xu2024knowledge\n    category: knowledge-conflict\n    doi: ''\n    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory\n      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.\n    role: foundation\n    title: 'Knowledge Conflicts for LLMs: A Survey'\n    url: https://arxiv.org/abs/2403.08319\n    venue: EMNLP 2024\n    verified: true\n    year: 2024\n  zhao2024analysing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Du, X.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2024analysing\n    category: probing\n    doi: ''\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\n    role: foundation\n    semantic_scholar_id: ''\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\n    url: https://arxiv.org/abs/2410.16090\n    venue: NeurIPS 2024 FMI Workshop\n    verified: true\n    year: 2024\n  zhao2025steering:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Devoto, A.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2025steering\n    category: sae-steering\n    doi: ''\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\n      activation editing.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\n      Engineering\n    url: https://arxiv.org/abs/2410.15999\n    venue: NAACL 2025 Oral\n    verified: true\n    year: 2025\n  zhao2026when:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, J.\n    - et al.\n    bibtex_key: zhao2026when\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\n      finding that linguistic similarity governs entity-centric conflict resolution.\n      Our work provides mechanistic explanation.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 7,
        "newStart": 1,
        "newLines": 7,
        "lines": [
          " categories: []",
          " meta:",
          "-  last_updated: '2026-05-22T14:00:00Z'",
          "-  total_papers: 15",
          "+  last_updated: '2026-05-22T14:30:00Z'",
          "+  total_papers: 22",
          " papers:",
          "   basu2026interpretability:",
          "     abstract: ''"
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

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01YDqi7u5xyMdRzk9x3SEZBq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
  "old_string": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026",
  "new_string": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "d10e5014-5ba7-4b21-9347-b5ad6ce8ecc5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SexWV4DSoRq77QS9ACSgJK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2616,
      "cache_read_input_tokens": 46882,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2616
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

_source line 55 · 2026-05-22T13:49:03.387Z_

<details><summary>↩ Tool result · `toolu_01YDqi7u5xyMdRzk9x3SEZBq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "06f7ed7f-7493-4740-bd17-984fa7150df2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml",
    "oldString": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026",
    "newString": "    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n  wu2020emerging:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wu, S.\n    - Conneau, A.\n    - Li, H.\n    - Zettlemoyer, L.\n    - Stoyanov, V.\n    bibtex_key: wu2020emerging\n    category: cross-lingual-repr\n    doi: 10.18653/v1/2020.acl-main.536\n    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters\n      alone; monolingual representations can be aligned post-hoc. Foundation for understanding\n      language-agnostic concept space our probing hypotheses build on. MUST CITE.\n    role: foundation\n    title: Emerging Cross-lingual Structure in Pretrained Language Models\n    url: https://aclanthology.org/2020.acl-main.536/\n    venue: ACL 2020\n    verified: true\n    year: 2020\n  wendler2024llamas:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Wendler, C.\n    - Veselovsky, V.\n    - Monea, G.\n    - West, R.\n    bibtex_key: wendler2024llamas\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations\n      in middle layers. Three-phase pattern (input language -> English pivot -> output\n      language) supports hypothesis that conflict signals may route through English-aligned\n      subspace.\n    role: foundation\n    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'\n    url: https://arxiv.org/abs/2402.10588\n    venue: ACL 2024\n    verified: true\n    year: 2024\n  muller2021first:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Muller, B.\n    - Elazar, Y.\n    - Sagot, B.\n    - Seddah, D.\n    bibtex_key: muller2021first\n    category: cross-lingual-repr\n    doi: ''\n    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual\n      encoder + language-agnostic predictor. Representations first converge to language\n      neutrality then recover language specificity. Methodological precedent for our\n      layer-wise analysis.\n    role: methodology\n    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual\n      BERT'\n    url: https://aclanthology.org/2021.eacl-main.189/\n    venue: EACL 2021\n    verified: true\n    year: 2021\n  kargaran2024mexa:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Kargaran, A.H.\n    - Modarressi, A.\n    - Nikeghbal, N.\n    - Diesner, J.\n    - Yvon, F.\n    - \"Sch\\xFCtze, H.\"\n    bibtex_key: kargaran2024mexa\n    category: cross-lingual-repr\n    doi: ''\n    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90\n      Pearson correlation with downstream tasks. Provides evaluation methodology for\n      measuring English-centric alignment relevant to our cross-lingual transfer analysis.\n    role: methodology\n    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual\n      Alignment'\n    url: https://arxiv.org/abs/2410.05873\n    venue: Findings of ACL 2025\n    verified: true\n    year: 2024\n  belinkov2022probing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Belinkov, Y.\n    bibtex_key: belinkov2022probing\n    category: probing-methodology\n    doi: ''\n    relevance: Comprehensive survey of probing classifier promises, shortcomings, and\n      advances. Defines the methodological framework our linear probes follow. MUST\n      CITE for probing methodology justification.\n    role: foundation\n    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'\n    url: https://arxiv.org/abs/2102.12452\n    venue: Computational Linguistics 48(1)\n    verified: true\n    year: 2022\n  hewitt2019designing:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Hewitt, J.\n    - Liang, P.\n    bibtex_key: hewitt2019designing\n    category: probing-methodology\n    doi: ''\n    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)\n      to distinguish genuine representation encoding from probe memorization. Our probing\n      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner\n      Up.\n    role: methodology\n    title: Designing and Interpreting Probes with Control Tasks\n    url: https://aclanthology.org/D19-1275/\n    venue: EMNLP 2019\n    verified: true\n    year: 2019\n  ulmer2022deep:\n    added_at: '2026-05-22T14:30:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ulmer, D.\n    - Hardmeier, C.\n    - Frellsen, J.\n    bibtex_key: ulmer2022deep\n    category: probing-methodology\n    doi: ''\n    relevance: Bootstrap-based statistical testing framework for neural network comparisons,\n      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology\n      we use for probing accuracy significance testing.\n    role: methodology\n    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing\n      in the Age of Neural Networks'\n    url: https://arxiv.org/abs/2204.06815\n    venue: arXiv\n    verified: true\n    year: 2022",
    "originalFile": "categories: []\nmeta:\n  last_updated: '2026-05-22T14:30:00Z'\n  total_papers: 22\npapers:\n  basu2026interpretability:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Basu, S.\n    - et al.\n    bibtex_key: basu2026interpretability\n    category: sae-steering\n    doi: ''\n    relevance: 'SAE steering failure in clinical triage despite 98.2% AUROC probes.\n      Critical negative result: defines boundary conditions for when SAE steering\n      works. Our Track 3 design addresses their methodological gaps.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Interpretability without actionability: mechanistic methods cannot correct\n      language model errors despite near-perfect internal representations'\n    url: https://arxiv.org/abs/2603.18353\n    venue: arXiv\n    verified: true\n    year: 2026\n  boer2026probing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Boer, A.\n    - Brink, I.\n    - Ulmer, D.\n    bibtex_key: boer2026probing\n    category: probing\n    doi: ''\n    relevance: 0.96 Macro-F1 parametric-vs-contextual attribution probe on Llama/Mistral/Qwen.\n      Monolingual performance ceiling for our Track 1. Cross-domain transfer 0.94-0.99\n      F1.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Probing for Knowledge Attribution in Large Language Models\n    url: https://arxiv.org/abs/2602.22787\n    venue: arXiv\n    verified: true\n    year: 2026\n  ifergan2024beneath:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Ifergan, M.\n    - Choshen, L.\n    - Aharoni, R.\n    - Szpektor, I.\n    - Abend, O.\n    bibtex_key: ifergan2024beneath\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Shows cross-lingual answer consistency does not imply shared representation;\n      script similarity dominates sharing. Directly motivates our probing approach\n      to test whether conflict signals share representations across languages.\n    role: foundation\n    title: 'Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge\n      Representation Sharing in LLMs'\n    url: https://arxiv.org/abs/2408.10646\n    venue: Findings of NAACL 2025\n    verified: true\n    year: 2024\n  kialy2026universal:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Kialy, U.Z.\n    - Shtarkberg, A.\n    - Klein, A.\n    bibtex_key: kialy2026universal\n    category: cross-lingual-sae\n    doi: ''\n    relevance: First cross-lingual SAE feature discovery. Shows cross-linguistic core\n      for register features + zero-shot steering transfer. We test whether this extends\n      to knowledge conflict features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register\n      with SAEs\n    url: https://arxiv.org/abs/2603.26236\n    venue: arXiv\n    verified: true\n    year: 2026\n  li2025taming:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Li, G.\n    - Chen, Y.\n    - Tong, H.\n    bibtex_key: li2025taming\n    category: knowledge-conflict\n    doi: ''\n    relevance: Proposes conflict resolution framework for LLMs. Provides resolution\n      baselines our mechanistic approach complements.\n    role: direct-competitor\n    title: Taming Knowledge Conflicts in Language Models\n    url: https://arxiv.org/abs/2503.10996\n    venue: ICML 2025 (Spotlight)\n    verified: true\n    year: 2025\n  pham2026where:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Pham, M.V.\n    - Borkakoty, H.\n    - Hou, Y.\n    bibtex_key: pham2026where\n    category: conflict-mechanism\n    doi: ''\n    relevance: Activation patching + CMAP for intra-memory conflicts. Attention layers\n      21-47 dominate conflict resolution in Qwen3-4B. Closest methodological parallel\n      for within-parametric conflicts.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge\n      Conflict in Language Models'\n    url: https://arxiv.org/abs/2601.09445\n    venue: arXiv\n    verified: true\n    year: 2026\n  team2026qwen:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Qwen Team\n    bibtex_key: team2026qwen\n    category: sae-tools\n    doi: ''\n    relevance: Pretrained SAEs for Qwen3 family. Our Track 2 uses Qwen-Scope SAEs\n      on Qwen3-8B-Base. Documents cross-lingual transfer for toxicity features (Section\n      5.2).\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Qwen-Scope: Turning Sparse Features into Development Tools for Large Language\n      Models'\n    url: https://arxiv.org/abs/2605.11887\n    venue: arXiv\n    verified: true\n    year: 2026\n  wang2025lost:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wang, M.\n    - Adel, H.\n    - Lange, L.\n    - et al.\n    bibtex_key: wang2025lost\n    category: cross-lingual-mechanism\n    doi: ''\n    relevance: Language-independent concept space through most layers, language-specific\n      only in final layers. Key mechanistic finding our H1/H2 hypotheses build on.\n    role: foundation\n    semantic_scholar_id: ''\n    title: 'Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency\n      in Transformer Language Models'\n    url: https://arxiv.org/abs/2504.04264\n    venue: ACL 2025 (SAC Highlights)\n    verified: true\n    year: 2025\n  wong2026langfir:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Wong, S.H.\n    - Siddique, A.B.\n    - Sajjad, H.\n    bibtex_key: wong2026langfir\n    category: cross-lingual-sae\n    doi: ''\n    relevance: Random-token filtering isolates <5 language-specific SAE features/language.\n      Our Track 2 uses this as control to disentangle language-identity from conflict\n      features.\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'LangFIR: Discovering Sparse Language-Specific Features from Monolingual\n      Data for Language Steering'\n    url: https://arxiv.org/abs/2604.03532\n    venue: arXiv\n    verified: true\n    year: 2026\n  xie2024adaptive:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xie, J.\n    - Zhang, K.\n    - Chen, J.\n    - Lou, R.\n    - Su, Y.\n    bibtex_key: xie2024adaptive\n    category: knowledge-conflict\n    doi: ''\n    relevance: Introduces ConflictQA benchmark (PopQA + StrategyQA based) for studying\n      LLM behavior under context-parametric knowledge conflicts. Our primary evaluation\n      dataset.\n    role: foundation\n    title: 'Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large\n      Language Models in Knowledge Conflicts'\n    url: https://arxiv.org/abs/2305.13300\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  xing2024evaluating:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xing, X.\n    - He, Z.\n    - Xu, H.\n    - Wang, X.\n    - Wang, R.\n    - Hong, Y.\n    bibtex_key: xing2024evaluating\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: Proposes cross-lingual semantic/accuracy/timeliness consistency metrics\n      (xSC, xAC, xTC) for evaluating multilingual LLM inconsistency. Provides evaluation\n      methodology relevant to our cross-lingual conflict measurement.\n    role: peripheral\n    title: Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language\n      Models\n    url: https://arxiv.org/abs/2407.01358\n    venue: arXiv\n    verified: true\n    year: 2024\n  xu2024knowledge:\n    added_at: '2026-05-22T14:00:00Z'\n    added_by: paper-agent-lit-search\n    authors:\n    - Xu, R.\n    - Qi, Z.\n    - Guo, Z.\n    - Wang, C.\n    - Wang, H.\n    - Zhang, Y.\n    - Xu, W.\n    bibtex_key: xu2024knowledge\n    category: knowledge-conflict\n    doi: ''\n    relevance: Comprehensive survey of context-memory, inter-context, and intra-memory\n      knowledge conflicts in LLMs. Defines the taxonomy our work builds on.\n    role: foundation\n    title: 'Knowledge Conflicts for LLMs: A Survey'\n    url: https://arxiv.org/abs/2403.08319\n    venue: EMNLP 2024\n    verified: true\n    year: 2024\n  zhao2024analysing:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Du, X.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2024analysing\n    category: probing\n    doi: ''\n    relevance: 'Original conflict probing work: ~90% accuracy detecting conflicts\n      in residual stream. Foundation for our Track 1 cross-lingual extension.'\n    role: foundation\n    semantic_scholar_id: ''\n    title: Analysing the Residual Stream of Language Models Under Knowledge Conflicts\n    url: https://arxiv.org/abs/2410.16090\n    venue: NeurIPS 2024 FMI Workshop\n    verified: true\n    year: 2024\n  zhao2025steering:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, Y.\n    - Devoto, A.\n    - Hong, G.\n    - et al.\n    bibtex_key: zhao2025steering\n    category: sae-steering\n    doi: ''\n    relevance: 'SpARE: SAE-based conflict feature selection + steering. Core methodology\n      we extend to cross-lingual setting. MI-based feature selection, constraint-aware\n      activation editing.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Steering Knowledge Selection Behaviours in LLMs via SAE-Based Representation\n      Engineering\n    url: https://arxiv.org/abs/2410.15999\n    venue: NAACL 2025 Oral\n    verified: true\n    year: 2025\n  zhao2026when:\n    abstract: ''\n    added_at: '2026-05-21T12:04:50.273Z'\n    added_by: director-bootstrap\n    authors:\n    - Zhao, J.\n    - et al.\n    bibtex_key: zhao2026when\n    category: cross-lingual-conflict\n    doi: ''\n    relevance: 'CLEAR benchmark: 10-language cross-lingual conflict evaluation. Behavioral\n      finding that linguistic similarity governs entity-centric conflict resolution.\n      Our work provides mechanistic explanation.'\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models'\n    url: https://arxiv.org/abs/2601.07041\n    venue: arXiv\n    verified: true\n    year: 2026\n",
    "structuredPatch": [
      {
        "oldStart": 324,
        "oldLines": 3,
        "newStart": 324,
        "newLines": 146,
        "lines": [
          "     venue: arXiv",
          "     verified: true",
          "     year: 2026",
          "+  wu2020emerging:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Wu, S.",
          "+    - Conneau, A.",
          "+    - Li, H.",
          "+    - Zettlemoyer, L.",
          "+    - Stoyanov, V.",
          "+    bibtex_key: wu2020emerging",
          "+    category: cross-lingual-repr",
          "+    doi: 10.18653/v1/2020.acl-main.536",
          "+    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters",
          "+      alone; monolingual representations can be aligned post-hoc. Foundation for understanding",
          "+      language-agnostic concept space our probing hypotheses build on. MUST CITE.",
          "+    role: foundation",
          "+    title: Emerging Cross-lingual Structure in Pretrained Language Models",
          "+    url: https://aclanthology.org/2020.acl-main.536/",
          "+    venue: ACL 2020",
          "+    verified: true",
          "+    year: 2020",
          "+  wendler2024llamas:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Wendler, C.",
          "+    - Veselovsky, V.",
          "+    - Monea, G.",
          "+    - West, R.",
          "+    bibtex_key: wendler2024llamas",
          "+    category: cross-lingual-repr",
          "+    doi: ''",
          "+    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations",
          "+      in middle layers. Three-phase pattern (input language -> English pivot -> output",
          "+      language) supports hypothesis that conflict signals may route through English-aligned",
          "+      subspace.",
          "+    role: foundation",
          "+    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'",
          "+    url: https://arxiv.org/abs/2402.10588",
          "+    venue: ACL 2024",
          "+    verified: true",
          "+    year: 2024",
          "+  muller2021first:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Muller, B.",
          "+    - Elazar, Y.",
          "+    - Sagot, B.",
          "+    - Seddah, D.",
          "+    bibtex_key: muller2021first",
          "+    category: cross-lingual-repr",
          "+    doi: ''",
          "+    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual",
          "+      encoder + language-agnostic predictor. Representations first converge to language",
          "+      neutrality then recover language specificity. Methodological precedent for our",
          "+      layer-wise analysis.",
          "+    role: methodology",
          "+    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual",
          "+      BERT'",
          "+    url: https://aclanthology.org/2021.eacl-main.189/",
          "+    venue: EACL 2021",
          "+    verified: true",
          "+    year: 2021",
          "+  kargaran2024mexa:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Kargaran, A.H.",
          "+    - Modarressi, A.",
          "+    - Nikeghbal, N.",
          "+    - Diesner, J.",
          "+    - Yvon, F.",
          "+    - \"Sch\\xFCtze, H.\"",
          "+    bibtex_key: kargaran2024mexa",
          "+    category: cross-lingual-repr",
          "+    doi: ''",
          "+    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90",
          "+      Pearson correlation with downstream tasks. Provides evaluation methodology for",
          "+      measuring English-centric alignment relevant to our cross-lingual transfer analysis.",
          "+    role: methodology",
          "+    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual",
          "+      Alignment'",
          "+    url: https://arxiv.org/abs/2410.05873",
          "+    venue: Findings of ACL 2025",
          "+    verified: true",
          "+    year: 2024",
          "+  belinkov2022probing:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Belinkov, Y.",
          "+    bibtex_key: belinkov2022probing",
          "+    category: probing-methodology",
          "+    doi: ''",
          "+    relevance: Comprehensive survey of probing classifier promises, shortcomings, and",
          "+      advances. Defines the methodological framework our linear probes follow. MUST",
          "+      CITE for probing methodology justification.",
          "+    role: foundation",
          "+    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'",
          "+    url: https://arxiv.org/abs/2102.12452",
          "+    venue: Computational Linguistics 48(1)",
          "+    verified: true",
          "+    year: 2022",
          "+  hewitt2019designing:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Hewitt, J.",
          "+    - Liang, P.",
          "+    bibtex_key: hewitt2019designing",
          "+    category: probing-methodology",
          "+    doi: ''",
          "+    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)",
          "+      to distinguish genuine representation encoding from probe memorization. Our probing",
          "+      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner",
          "+      Up.",
          "+    role: methodology",
          "+    title: Designing and Interpreting Probes with Control Tasks",
          "+    url: https://aclanthology.org/D19-1275/",
          "+    venue: EMNLP 2019",
          "+    verified: true",
          "+    year: 2019",
          "+  ulmer2022deep:",
          "+    added_at: '2026-05-22T14:30:00Z'",
          "+    added_by: paper-agent-lit-search",
          "+    authors:",
          "+    - Ulmer, D.",
          "+    - Hardmeier, C.",
          "+    - Frellsen, J.",
          "+    bibtex_key: ulmer2022deep",
          "+    category: probing-methodology",
          "+    doi: ''",
          "+    relevance: Bootstrap-based statistical testing framework for neural network comparisons,",
          "+      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology",
          "+      we use for probing accuracy significance testing.",
          "+    role: methodology",
          "+    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing",
          "+      in the Age of Neural Networks'",
          "+    url: https://arxiv.org/abs/2204.06815",
          "+    venue: arXiv",
          "+    verified: true",
          "+    year: 2022"
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

_source line 56_

验证写入结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "f12a8114-4e68-427e-a16c-850cd41b17b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEGP5cpnbcZJH4XqN4nFYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1989,
      "cache_read_input_tokens": 49498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1989
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

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_017KonvcXQoFGDESBrG3HQUf`</summary>

```json
{
  "command": "python3 -c \"\nimport yaml\nwith open('literature_map.yaml') as f:\n    data = yaml.safe_load(f)\nprint(f'Total papers in meta: {data[\\\"meta\\\"][\\\"total_papers\\\"]}')\nprint(f'Actual paper count: {len(data[\\\"papers\\\"])}')\nprint()\nnew_keys = ['wu2020emerging','wendler2024llamas','muller2021first','kargaran2024mexa','belinkov2022probing','hewitt2019designing','ulmer2022deep']\nfor k in new_keys:\n    p = data['papers'][k]\n    print(f'{k}: {p[\\\"title\\\"][:60]}... | {p[\\\"venue\\\"]} | {p[\\\"year\\\"]} | verified={p[\\\"verified\\\"]}')\n\"\n",
  "description": "Verify YAML integrity and new paper entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "2ded8e56-d2c4-4c56-a404-98af3144b225",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GEGP5cpnbcZJH4XqN4nFYs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1989,
      "cache_read_input_tokens": 49498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1989
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

_source line 58 · 2026-05-22T13:49:10.944Z_

<details><summary>↩ Tool result · `toolu_017KonvcXQoFGDESBrG3HQUf`</summary>

```text
Total papers in meta: 22
Actual paper count: 22

wu2020emerging: Emerging Cross-lingual Structure in Pretrained Language Mode... | ACL 2020 | 2020 | verified=True
wendler2024llamas: Do Llamas Work in English? On the Latent Language of Multili... | ACL 2024 | 2024 | verified=True
muller2021first: First Align, then Predict: Understanding the Cross-Lingual A... | EACL 2021 | 2021 | verified=True
kargaran2024mexa: MEXA: Multilingual Evaluation of English-Centric LLMs via Cr... | Findings of ACL 2025 | 2024 | verified=True
belinkov2022probing: Probing Classifiers: Promises, Shortcomings, and Advances... | Computational Linguistics 48(1) | 2022 | verified=True
hewitt2019designing: Designing and Interpreting Probes with Control Tasks... | EMNLP 2019 | 2019 | verified=True
ulmer2022deep: deep-significance: Easy and Meaningful Statistical Significa... | arXiv | 2022 | verified=True
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "b0176f49-c017-4782-b093-4f07c7b58cda",
  "tool_use_result": {
    "stdout": "Total papers in meta: 22\nActual paper count: 22\n\nwu2020emerging: Emerging Cross-lingual Structure in Pretrained Language Mode... | ACL 2020 | 2020 | verified=True\nwendler2024llamas: Do Llamas Work in English? On the Latent Language of Multili... | ACL 2024 | 2024 | verified=True\nmuller2021first: First Align, then Predict: Understanding the Cross-Lingual A... | EACL 2021 | 2021 | verified=True\nkargaran2024mexa: MEXA: Multilingual Evaluation of English-Centric LLMs via Cr... | Findings of ACL 2025 | 2024 | verified=True\nbelinkov2022probing: Probing Classifiers: Promises, Shortcomings, and Advances... | Computational Linguistics 48(1) | 2022 | verified=True\nhewitt2019designing: Designing and Interpreting Probes with Control Tasks... | EMNLP 2019 | 2019 | verified=True\nulmer2022deep: deep-significance: Easy and Meaningful Statistical Significa... | arXiv | 2022 | verified=True",
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

_source line 59_

22 篇，YAML 完整。汇总：

**Cluster 3: Cross-lingual Representations (+4)**
| Key | Title | Venue |
|-----|-------|-------|
| `wu2020emerging` | Emerging Cross-lingual Structure in Pretrained Language Models | ACL 2020 **(MUST CITE)** |
| `wendler2024llamas` | Do Llamas Work in English? On the Latent Language of Multilingual Transformers | ACL 2024 |
| `muller2021first` | First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | EACL 2021 |
| `kargaran2024mexa` | MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Findings of ACL 2025 |

**Cluster 4: Probing Methodology (+3)**
| Key | Title | Venue |
|-----|-------|-------|
| `belinkov2022probing` | Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics 48(1) **(MUST CITE)** |
| `hewitt2019designing` | Designing and Interpreting Probes with Control Tasks | EMNLP 2019 |
| `ulmer2022deep` | deep-significance: Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks | arXiv 2022 |

所有 URL 已通过 WebSearch 确认指向真实论文。literature_map.yaml 已从 15 篇更新至 22 篇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "uuid": "e269754c-10df-43bc-bbdb-303563b51bbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E4hRStGdPh8AXyVYsyuuKn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 600,
      "cache_read_input_tokens": 51487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 600
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

_source line 60_

22 篇，YAML 完整。汇总：

**Cluster 3: Cross-lingual Representations (+4)**
| Key | Title | Venue |
|-----|-------|-------|
| `wu2020emerging` | Emerging Cross-lingual Structure in Pretrained Language Models | ACL 2020 **(MUST CITE)** |
| `wendler2024llamas` | Do Llamas Work in English? On the Latent Language of Multilingual Transformers | ACL 2024 |
| `muller2021first` | First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual BERT | EACL 2021 |
| `kargaran2024mexa` | MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual Alignment | Findings of ACL 2025 |

**Cluster 4: Probing Methodology (+3)**
| Key | Title | Venue |
|-----|-------|-------|
| `belinkov2022probing` | Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics 48(1) **(MUST CITE)** |
| `hewitt2019designing` | Designing and Interpreting Probes with Control Tasks | EMNLP 2019 |
| `ulmer2022deep` | deep-significance: Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks | arXiv 2022 |

所有 URL 已通过 WebSearch 确认指向真实论文。literature_map.yaml 已从 15 篇更新至 22 篇。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 281899,
  "duration_api_ms": 343867,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "74944a45-8e5c-4732-a5c6-a2e003be4fe9",
  "total_cost_usd": 1.0652215,
  "usage": {
    "input_tokens": 1372,
    "cache_creation_input_tokens": 40246,
    "cache_read_input_tokens": 370118,
    "output_tokens": 10998,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40246,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 416,
        "cache_read_input_tokens": 51487,
        "cache_creation_input_tokens": 600,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 600
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 167180,
      "outputTokens": 5927,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 15,
      "costUSD": 0.34681500000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1372,
      "outputTokens": 10998,
      "cacheReadInputTokens": 370118,
      "cacheCreationInputTokens": 40246,
      "webSearchRequests": 0,
      "costUSD": 0.7184065000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6ff9fe75-47fb-42fb-9299-4f5a858c7a88"
}
```

</details>

---
