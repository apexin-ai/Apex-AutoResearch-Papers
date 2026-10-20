# Research conversation: Read the literature_map.yaml at `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml` a

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-acd089d1966135c41.jsonl`
- **Structured JSON:** [`cbecbda481691944db6e.json`](../../sessions/cb/cbecbda481691944db6e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-22T14:24:37.919Z_

Read the literature_map.yaml at `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/literature_map.yaml` and generate a complete BibTeX file at `/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib`.

Rules:
1. Only include papers with `verified: true`
2. For venue mapping:
   - Venues containing "arXiv" → `@article` with `journal = {arXiv preprint arXiv:XXXX.XXXXX}` (extract ID from url)
   - "ACL", "EMNLP", "NAACL", "EACL", "NeurIPS", "ICML", "ICLR" → `@inproceedings` with `booktitle = {Proceedings of ...}`
   - "Findings of ACL/NAACL/EMNLP" → `@inproceedings` with `booktitle = {Findings of ...}`
   - "Computational Linguistics" → `@article` with `journal = {Computational Linguistics}`
3. Every entry must have: author, title, year, and either booktitle or journal
4. Use proper BibTeX author formatting: `{Last1, First1 and Last2, First2}`
5. Include `url` field when available
6. Include `doi` field when non-empty
7. For "et al." in authors list, try to expand if the full author list is in the data, otherwise use the available names

The existing references.bib file has only placeholder comments — overwrite it completely.

Important: Read the file first, then Write the complete BibTeX output.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "9ba93c69-17bf-4ffd-b2fc-6339c47e699d",
  "agentId": "acd089d1966135c41",
  "type": "user",
  "uuid": "a7e9cf2b-be48-400a-9499-c305e6d42e86",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-22T14:24:37.923Z_

```json
{
  "parentUuid": "a7e9cf2b-be48-400a-9499-c305e6d42e86",
  "isSidechain": true,
  "agentId": "acd089d1966135c41",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
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
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "c901124b-e340-43a7-b0ae-aa0282b30534",
  "timestamp": "2026-05-22T14:24:37.923Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

---

### Tool call

_source line 3 · 2026-05-22T14:24:41.086Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GLAsCE5wQvaFnfiwGFBymk`</summary>

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
  "parentUuid": "c901124b-e340-43a7-b0ae-aa0282b30534",
  "isSidechain": true,
  "agentId": "acd089d1966135c41",
  "requestId": "req_011CbHm3QizXaoMzH2dEtXMB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "578de6a7-afc4-408d-ae80-21b5974ea75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QY4ScHVG9b1hWL7G3fxQmw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24617,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 24617,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T14:24:41.099Z_

<details><summary>↩ Tool result · `toolu_01GLAsCE5wQvaFnfiwGFBymk`</summary>

```text
1	categories: []
2	meta:
3	  last_updated: '2026-05-22T14:30:00Z'
4	  total_papers: 29
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
327	  wu2020emerging:
328	    added_at: '2026-05-22T14:30:00Z'
329	    added_by: paper-agent-lit-search
330	    authors:
331	    - Wu, S.
332	    - Conneau, A.
333	    - Li, H.
334	    - Zettlemoyer, L.
335	    - Stoyanov, V.
336	    bibtex_key: wu2020emerging
337	    category: cross-lingual-repr
338	    doi: 10.18653/v1/2020.acl-main.536
339	    relevance: Shows mid-layer cross-lingual alignment emerges from shared parameters
340	      alone; monolingual representations can be aligned post-hoc. Foundation for understanding
341	      language-agnostic concept space our probing hypotheses build on. MUST CITE.
342	    role: foundation
343	    title: Emerging Cross-lingual Structure in Pretrained Language Models
344	    url: https://aclanthology.org/2020.acl-main.536/
345	    venue: ACL 2020
346	    verified: true
347	    year: 2020
348	  wendler2024llamas:
349	    added_at: '2026-05-22T14:30:00Z'
350	    added_by: paper-agent-lit-search
351	    authors:
352	    - Wendler, C.
353	    - Veselovsky, V.
354	    - Monea, G.
355	    - West, R.
356	    bibtex_key: wendler2024llamas
357	    category: cross-lingual-repr
358	    doi: ''
359	    relevance: Demonstrates English-centric LLMs implicitly pivot through English representations
360	      in middle layers. Three-phase pattern (input language -> English pivot -> output
361	      language) supports hypothesis that conflict signals may route through English-aligned
362	      subspace.
363	    role: foundation
364	    title: 'Do Llamas Work in English? On the Latent Language of Multilingual Transformers'
365	    url: https://arxiv.org/abs/2402.10588
366	    venue: ACL 2024
367	    verified: true
368	    year: 2024
369	  muller2021first:
370	    added_at: '2026-05-22T14:30:00Z'
371	    added_by: paper-agent-lit-search
372	    authors:
373	    - Muller, B.
374	    - Elazar, Y.
375	    - Sagot, B.
376	    - Seddah, D.
377	    bibtex_key: muller2021first
378	    category: cross-lingual-repr
379	    doi: ''
380	    relevance: CKA-based layer-wise analysis showing mBERT decomposes into multilingual
381	      encoder + language-agnostic predictor. Representations first converge to language
382	      neutrality then recover language specificity. Methodological precedent for our
383	      layer-wise analysis.
384	    role: methodology
385	    title: 'First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual
386	      BERT'
387	    url: https://aclanthology.org/2021.eacl-main.189/
388	    venue: EACL 2021
389	    verified: true
390	    year: 2021
391	  kargaran2024mexa:
392	    added_at: '2026-05-22T14:30:00Z'
393	    added_by: paper-agent-lit-search
394	    authors:
395	    - Kargaran, A.H.
396	    - Modarressi, A.
397	    - Nikeghbal, N.
398	    - Diesner, J.
399	    - Yvon, F.
400	    - "Sch\xFCtze, H."
401	    bibtex_key: kargaran2024mexa
402	    category: cross-lingual-repr
403	    doi: ''
404	    relevance: Cross-lingual alignment metric leveraging English pivot hypothesis, 0.90
405	      Pearson correlation with downstream tasks. Provides evaluation methodology for
406	      measuring English-centric alignment relevant to our cross-lingual transfer analysis.
407	    role: methodology
408	    title: 'MEXA: Multilingual Evaluation of English-Centric LLMs via Cross-Lingual
409	      Alignment'
410	    url: https://arxiv.org/abs/2410.05873
411	    venue: Findings of ACL 2025
412	    verified: true
413	    year: 2024
414	  belinkov2022probing:
415	    added_at: '2026-05-22T14:30:00Z'
416	    added_by: paper-agent-lit-search
417	    authors:
418	    - Belinkov, Y.
419	    bibtex_key: belinkov2022probing
420	    category: probing-methodology
421	    doi: ''
422	    relevance: Comprehensive survey of probing classifier promises, shortcomings, and
423	      advances. Defines the methodological framework our linear probes follow. MUST
424	      CITE for probing methodology justification.
425	    role: foundation
426	    title: 'Probing Classifiers: Promises, Shortcomings, and Advances'
427	    url: https://arxiv.org/abs/2102.12452
428	    venue: Computational Linguistics 48(1)
429	    verified: true
430	    year: 2022
431	  hewitt2019designing:
432	    added_at: '2026-05-22T14:30:00Z'
433	    added_by: paper-agent-lit-search
434	    authors:
435	    - Hewitt, J.
436	    - Liang, P.
437	    bibtex_key: hewitt2019designing
438	    category: probing-methodology
439	    doi: ''
440	    relevance: Introduces selectivity metric (linguistic accuracy - control accuracy)
441	      to distinguish genuine representation encoding from probe memorization. Our probing
442	      design uses control tasks following this framework. EMNLP 2019 Best Paper Runner
443	      Up.
444	    role: methodology
445	    title: Designing and Interpreting Probes with Control Tasks
446	    url: https://aclanthology.org/D19-1275/
447	    venue: EMNLP 2019
448	    verified: true
449	    year: 2019
450	  ulmer2022deep:
451	    added_at: '2026-05-22T14:30:00Z'
452	    added_by: paper-agent-lit-search
453	    authors:
454	    - Ulmer, D.
455	    - Hardmeier, C.
456	    - Frellsen, J.
457	    bibtex_key: ulmer2022deep
458	    category: probing-methodology
459	    doi: ''
460	    relevance: Bootstrap-based statistical testing framework for neural network comparisons,
461	      including Almost Stochastic Order (ASO). Provides the bootstrap CI methodology
462	      we use for probing accuracy significance testing.
463	    role: methodology
464	    title: 'deep-significance: Easy and Meaningful Statistical Significance Testing
465	      in the Age of Neural Networks'
466	    url: https://arxiv.org/abs/2204.06815
467	    venue: arXiv
468	    verified: true
469	    year: 2022
470	  li2023iti:
471	    added_at: '2026-05-22T16:00:00Z'
472	    added_by: paper-agent-lit-search
473	    authors:
474	    - Li, K.
475	    - Patel, O.
476	    - "Vi\xE9gas, F."
477	    - Pfister, H.
478	    - Wattenberg, M.
479	    bibtex_key: li2023iti
480	    category: steering
481	    doi: ''
482	    relevance: Inference-Time Intervention shifts activations along truthful directions
483	      in attention heads to improve truthfulness. Foundational activation steering method
484	      our causal intervention approach builds on.
485	    role: foundation
486	    title: 'Inference-Time Intervention: Eliciting Truthful Answers from a Language
487	      Model'
488	    url: https://arxiv.org/abs/2306.03341
489	    venue: NeurIPS 2023
490	    verified: true
491	    year: 2023
492	  zou2023representation:
493	    added_at: '2026-05-22T16:00:00Z'
494	    added_by: paper-agent-lit-search
495	    authors:
496	    - Zou, A.
497	    - Phan, L.
498	    - Chen, S.
499	    - Campbell, J.
500	    - Guo, P.
501	    - Ren, R.
502	    - Pan, A.
503	    - et al.
504	    bibtex_key: zou2023representation
505	    category: steering
506	    doi: ''
507	    relevance: Introduces Representation Engineering (RepE) framework using population-level
508	      representations for monitoring and manipulating high-level cognitive phenomena.
509	      Foundational paradigm for our steering methodology.
510	    role: foundation
511	    title: 'Representation Engineering: A Top-Down Approach to AI Transparency'
512	    url: https://arxiv.org/abs/2310.01405
513	    venue: arXiv
514	    verified: true
515	    year: 2023
516	  feng2026finegrained:
517	    added_at: '2026-05-22T16:00:00Z'
518	    added_by: paper-agent-lit-search
519	    authors:
520	    - Feng, Z.
521	    - Li, T.
522	    - Zhu, Z.
523	    - Zhou, H.
524	    - Qian, J.
525	    - Zhang, L.
526	    - Mao, K.
527	    bibtex_key: feng2026finegrained
528	    category: steering
529	    doi: ''
530	    relevance: Decomposes block activations into atomic-unit-level activations for
531	      fine-grained steering. Shows block-level steering entangles beneficial and harmful
532	      features. Methodological advance relevant to our per-feature steering design.
533	    role: methodology
534	    title: 'Fine-Grained Activation Steering: Steering Less, Achieving More'
535	    url: https://arxiv.org/abs/2602.04428
536	    venue: ICLR 2026
537	    verified: true
538	    year: 2026
539	  conneau2018xnli:
540	    added_at: '2026-05-22T16:00:00Z'
541	    added_by: paper-agent-lit-search
542	    authors:
543	    - Conneau, A.
544	    - Rinott, R.
545	    - Lample, G.
546	    - Williams, A.
547	    - Bowman, S.
548	    - Schwenk, H.
549	    - Stoyanov, V.
550	    bibtex_key: conneau2018xnli
551	    category: dataset-tool
552	    doi: ''
553	    relevance: Cross-lingual NLI benchmark spanning 15 languages. Used for evaluating
554	      cross-lingual transfer and multilingual understanding in our experiments.
555	    role: foundation
556	    title: 'XNLI: Evaluating Cross-lingual Sentence Representations'
557	    url: https://aclanthology.org/D18-1269/
558	    venue: EMNLP 2018
559	    verified: true
560	    year: 2018
561	  rei2020comet:
562	    added_at: '2026-05-22T16:00:00Z'
563	    added_by: paper-agent-lit-search
564	    authors:
565	    - Rei, R.
566	    - Stewart, C.
567	    - Farinha, A.C.
568	    - Lavie, A.
569	    bibtex_key: rei2020comet
570	    category: dataset-tool
571	    doi: ''
572	    relevance: Neural MT evaluation metric using cross-lingual pretrained encoders.
573	      Provides translation quality evaluation for our cross-lingual dataset construction
574	      pipeline.
575	    role: methodology
576	    title: 'COMET: A Neural Framework for MT Evaluation'
577	    url: https://aclanthology.org/2020.emnlp-main.213/
578	    venue: EMNLP 2020
579	    verified: true
580	    year: 2020
581	  grattafiori2024llama:
582	    added_at: '2026-05-22T16:00:00Z'
583	    added_by: paper-agent-lit-search
584	    authors:
585	    - Grattafiori, A.
586	    - et al. (Llama Team, AI @ Meta)
587	    bibtex_key: grattafiori2024llama
588	    category: dataset-tool
589	    doi: ''
590	    relevance: Technical report for Llama 3.1 models (8B/70B/405B). One of our primary
591	      experimental models. Documents multilingual capabilities and 128K context window.
592	    role: foundation
593	    title: The Llama 3 Herd of Models
594	    url: https://arxiv.org/abs/2407.21783
595	    venue: arXiv
596	    verified: true
597	    year: 2024
598	  yang2024qwen25:
599	    added_at: '2026-05-22T16:00:00Z'
600	    added_by: paper-agent-lit-search
601	    authors:
602	    - Yang, A.
603	    - Yang, B.
604	    - et al. (Qwen Team)
605	    bibtex_key: yang2024qwen25
606	    category: dataset-tool
607	    doi: ''
608	    relevance: Technical report for Qwen2.5 model series. One of our primary experimental
609	      models. Documents multilingual pretraining on 18T tokens.
610	    role: foundation
611	    title: Qwen2.5 Technical Report
612	    url: https://arxiv.org/abs/2412.15115
613	    venue: arXiv
614	    verified: true
615	    year: 2024
616	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "578de6a7-afc4-408d-ae80-21b5974ea75b",
  "isSidechain": true,
  "promptId": "9ba93c69-17bf-4ffd-b2fc-6339c47e699d",
  "agentId": "acd089d1966135c41",
  "type": "user",
  "uuid": "be545eb2-77b3-43e5-b5c1-91f9ac2d731e",
  "sourceToolAssistantUUID": "578de6a7-afc4-408d-ae80-21b5974ea75b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T14:24:41.259Z_

<details open><summary>🔧 Tool call — Read · `toolu_01G9UdNwrWDUjRaxdaWT5943`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be545eb2-77b3-43e5-b5c1-91f9ac2d731e",
  "isSidechain": true,
  "agentId": "acd089d1966135c41",
  "requestId": "req_011CbHm3QizXaoMzH2dEtXMB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "91b77ab7-adcf-495a-8cb2-3431439ae087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QY4ScHVG9b1hWL7G3fxQmw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 24617,
      "cache_read_input_tokens": 0,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 24617
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 153,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 24617,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 24617,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T14:24:41.266Z_

<details><summary>↩ Tool result · `toolu_01G9UdNwrWDUjRaxdaWT5943`</summary>

```text
1	% References for Cross-Lingual Knowledge Conflict paper
2	% Auto-generated from literature_map.yaml — will be populated in Step 3 bib_sync
3	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "91b77ab7-adcf-495a-8cb2-3431439ae087",
  "isSidechain": true,
  "promptId": "9ba93c69-17bf-4ffd-b2fc-6339c47e699d",
  "agentId": "acd089d1966135c41",
  "type": "user",
  "uuid": "4fb682ae-113f-44d1-b5f9-6727cf2cd4ae",
  "sourceToolAssistantUUID": "91b77ab7-adcf-495a-8cb2-3431439ae087",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-22T14:24:44.806Z_

All 29 papers have `verified: true`. Now I'll generate the complete BibTeX file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fb682ae-113f-44d1-b5f9-6727cf2cd4ae",
  "isSidechain": true,
  "agentId": "acd089d1966135c41",
  "requestId": "req_011CbHm3fevFE5mNC7n79QLY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9a040801-422a-4196-b05c-23f9a45d769e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Riyz1x35zwyeCQq6V1H8sG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9123,
      "cache_read_input_tokens": 24617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9123,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-22T14:25:35.524Z_

<details open><summary>🔧 Tool call — Write · `toolu_01MX8jsRyLbtkqGEFhV85SaT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib",
  "content": "% References for Cross-Lingual Knowledge Conflict paper\n% Auto-generated from literature_map.yaml\n\n@article{basu2026interpretability,\n  author    = {Basu, S. and others},\n  title     = {Interpretability without Actionability: Mechanistic Methods Cannot Correct Language Model Errors Despite Near-Perfect Internal Representations},\n  journal   = {arXiv preprint arXiv:2603.18353},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2603.18353}\n}\n\n@article{boer2026probing,\n  author    = {Boer, A. and Brink, I. and Ulmer, D.},\n  title     = {Probing for Knowledge Attribution in Large Language Models},\n  journal   = {arXiv preprint arXiv:2602.22787},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.22787}\n}\n\n@inproceedings{ifergan2024beneath,\n  author    = {Ifergan, M. and Choshen, L. and Aharoni, R. and Szpektor, I. and Abend, O.},\n  title     = {Beneath the Surface of Consistency: Exploring Cross-lingual Knowledge Representation Sharing in {LLMs}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL 2025},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2408.10646}\n}\n\n@article{kialy2026universal,\n  author    = {Kialy, U.Z. and Shtarkberg, A. and Klein, A.},\n  title     = {A Universal Vibe? Finding and Controlling Language-Agnostic Informal Register with {SAEs}},\n  journal   = {arXiv preprint arXiv:2603.26236},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2603.26236}\n}\n\n@inproceedings{li2025taming,\n  author    = {Li, G. and Chen, Y. and Tong, H.},\n  title     = {Taming Knowledge Conflicts in Language Models},\n  booktitle = {Proceedings of the 42nd International Conference on Machine Learning (ICML)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.10996}\n}\n\n@article{pham2026where,\n  author    = {Pham, M.V. and Borkakoty, H. and Hou, Y.},\n  title     = {Where Knowledge Collides: A Mechanistic Study of Intra-Memory Knowledge Conflict in Language Models},\n  journal   = {arXiv preprint arXiv:2601.09445},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.09445}\n}\n\n@article{team2026qwen,\n  author    = {{Qwen Team}},\n  title     = {Qwen-Scope: Turning Sparse Features into Development Tools for Large Language Models},\n  journal   = {arXiv preprint arXiv:2605.11887},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2605.11887}\n}\n\n@inproceedings{wang2025lost,\n  author    = {Wang, M. and Adel, H. and Lange, L. and others},\n  title     = {Lost in Multilinguality: Dissecting Cross-lingual Factual Inconsistency in Transformer Language Models},\n  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2504.04264}\n}\n\n@article{wong2026langfir,\n  author    = {Wong, S.H. and Siddique, A.B. and Sajjad, H.},\n  title     = {{LangFIR}: Discovering Sparse Language-Specific Features from Monolingual Data for Language Steering},\n  journal   = {arXiv preprint arXiv:2604.03532},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2604.03532}\n}\n\n@inproceedings{xie2024adaptive,\n  author    = {Xie, J. and Zhang, K. and Chen, J. and Lou, R. and Su, Y.},\n  title     = {Adaptive Chameleon or Stubborn Sloth: Revealing the Behavior of Large Language Models in Knowledge Conflicts},\n  booktitle = {Proceedings of the 12th International Conference on Learning Representations (ICLR)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2305.13300}\n}\n\n@article{xing2024evaluating,\n  author    = {Xing, X. and He, Z. and Xu, H. and Wang, X. and Wang, R. and Hong, Y.},\n  title     = {Evaluating Knowledge-based Cross-lingual Inconsistency in Large Language Models},\n  journal   = {arXiv preprint arXiv:2407.01358},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2407.01358}\n}\n\n@inproceedings{xu2024knowledge,\n  author    = {Xu, R. and Qi, Z. and Guo, Z. and Wang, C. and Wang, H. and Zhang, Y. and Xu, W.},\n  title     = {Knowledge Conflicts for {LLMs}: A Survey},\n  booktitle = {Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.08319}\n}\n\n@inproceedings{zhao2024analysing,\n  author    = {Zhao, Y. and Du, X. and Hong, G. and others},\n  title     = {Analysing the Residual Stream of Language Models Under Knowledge Conflicts},\n  booktitle = {NeurIPS 2024 Workshop on Foundation Model Interventions},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.16090}\n}\n\n@inproceedings{zhao2025steering,\n  author    = {Zhao, Y. and Devoto, A. and Hong, G. and others},\n  title     = {Steering Knowledge Selection Behaviours in {LLMs} via {SAE}-Based Representation Engineering},\n  booktitle = {Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL)},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2410.15999}\n}\n\n@article{zhao2026when,\n  author    = {Zhao, J. and others},\n  title     = {When Abundance Conceals Weakness: Knowledge Conflict in Multilingual Models},\n  journal   = {arXiv preprint arXiv:2601.07041},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2601.07041}\n}\n\n@inproceedings{wu2020emerging,\n  author    = {Wu, S. and Conneau, A. and Li, H. and Zettlemoyer, L. and Stoyanov, V.},\n  title     = {Emerging Cross-lingual Structure in Pretrained Language Models},\n  booktitle = {Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2020},\n  url       = {https://aclanthology.org/2020.acl-main.536/},\n  doi       = {10.18653/v1/2020.acl-main.536}\n}\n\n@inproceedings{wendler2024llamas,\n  author    = {Wendler, C. and Veselovsky, V. and Monea, G. and West, R.},\n  title     = {Do Llamas Work in {English}? On the Latent Language of Multilingual Transformers},\n  booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.10588}\n}\n\n@inproceedings{muller2021first,\n  author    = {Muller, B. and Elazar, Y. and Sagot, B. and Seddah, D.},\n  title     = {First Align, then Predict: Understanding the Cross-Lingual Ability of Multilingual {BERT}},\n  booktitle = {Proceedings of the 16th Conference of the European Chapter of the Association for Computational Linguistics (EACL)},\n  year      = {2021},\n  url       = {https://aclanthology.org/2021.eacl-main.189/}\n}\n\n@inproceedings{kargaran2024mexa,\n  author    = {Kargaran, A.H. and Modarressi, A. and Nikeghbal, N. and Diesner, J. and Yvon, F. and Sch{\\\"u}tze, H.},\n  title     = {{MEXA}: Multilingual Evaluation of {English}-Centric {LLMs} via Cross-Lingual Alignment},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2410.05873}\n}\n\n@article{belinkov2022probing,\n  author    = {Belinkov, Y.},\n  title     = {Probing Classifiers: Promises, Shortcomings, and Advances},\n  journal   = {Computational Linguistics},\n  volume    = {48},\n  number    = {1},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2102.12452}\n}\n\n@inproceedings{hewitt2019designing,\n  author    = {Hewitt, J. and Liang, P.},\n  title     = {Designing and Interpreting Probes with Control Tasks},\n  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2019},\n  url       = {https://aclanthology.org/D19-1275/}\n}\n\n@article{ulmer2022deep,\n  author    = {Ulmer, D. and Hardmeier, C. and Frellsen, J.},\n  title     = {deep-significance: Easy and Meaningful Statistical Significance Testing in the Age of Neural Networks},\n  journal   = {arXiv preprint arXiv:2204.06815},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2204.06815}\n}\n\n@inproceedings{li2023iti,\n  author    = {Li, K. and Patel, O. and Vi{\\'e}gas, F. and Pfister, H. and Wattenberg, M.},\n  title     = {Inference-Time Intervention: Eliciting Truthful Answers from a Language Model},\n  booktitle = {Advances in Neural Information Processing Systems 36 (NeurIPS)},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.03341}\n}\n\n@article{zou2023representation,\n  author    = {Zou, A. and Phan, L. and Chen, S. and Campbell, J. and Guo, P. and Ren, R. and Pan, A. and others},\n  title     = {Representation Engineering: A Top-Down Approach to {AI} Transparency},\n  journal   = {arXiv preprint arXiv:2310.01405},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2310.01405}\n}\n\n@inproceedings{feng2026finegrained,\n  author    = {Feng, Z. and Li, T. and Zhu, Z. and Zhou, H. and Qian, J. and Zhang, L. and Mao, K.},\n  title     = {Fine-Grained Activation Steering: Steering Less, Achieving More},\n  booktitle = {Proceedings of the 14th International Conference on Learning Representations (ICLR)},\n  year      = {2026},\n  url       = {https://arxiv.org/abs/2602.04428}\n}\n\n@inproceedings{conneau2018xnli,\n  author    = {Conneau, A. and Rinott, R. and Lample, G. and Williams, A. and Bowman, S. and Schwenk, H. and Stoyanov, V.},\n  title     = {{XNLI}: Evaluating Cross-lingual Sentence Representations},\n  booktitle = {Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2018},\n  url       = {https://aclanthology.org/D18-1269/}\n}\n\n@inproceedings{rei2020comet,\n  author    = {Rei, R. and Stewart, C. and Farinha, A.C. and Lavie, A.},\n  title     = {{COMET}: A Neural Framework for {MT} Evaluation},\n  booktitle = {Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year      = {2020},\n  url       = {https://aclanthology.org/2020.emnlp-main.213/}\n}\n\n@article{grattafiori2024llama,\n  author    = {Grattafiori, A. and others},\n  title     = {The {Llama} 3 Herd of Models},\n  journal   = {arXiv preprint arXiv:2407.21783},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2407.21783}\n}\n\n@article{yang2024qwen25,\n  author    = {Yang, A. and Yang, B. and others},\n  title     = {Qwen2.5 Technical Report},\n  journal   = {arXiv preprint arXiv:2412.15115},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2412.15115}\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a040801-422a-4196-b05c-23f9a45d769e",
  "isSidechain": true,
  "agentId": "acd089d1966135c41",
  "requestId": "req_011CbHm3fevFE5mNC7n79QLY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "044cd859-cf22-4e8d-b0ea-5f40da88148f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Riyz1x35zwyeCQq6V1H8sG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9123,
      "cache_read_input_tokens": 24617,
      "output_tokens": 3878,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9123
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3878,
          "cache_read_input_tokens": 24617,
          "cache_creation_input_tokens": 9123,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9123,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T14:25:35.560Z_

<details><summary>↩ Tool result · `toolu_01MX8jsRyLbtkqGEFhV85SaT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "044cd859-cf22-4e8d-b0ea-5f40da88148f",
  "isSidechain": true,
  "promptId": "9ba93c69-17bf-4ffd-b2fc-6339c47e699d",
  "agentId": "acd089d1966135c41",
  "type": "user",
  "uuid": "414dd743-80cc-4692-bb67-be05f1deebb3",
  "sourceToolAssistantUUID": "044cd859-cf22-4e8d-b0ea-5f40da88148f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-22T14:25:44.853Z_

已生成完整 BibTeX 文件，包含全部 29 篇 verified 论文。

文件路径：`/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/references.bib`

处理细节：
- **`@article`**（13篇）：所有 arXiv 论文 + `belinkov2022probing`（Computational Linguistics）+ `ulmer2022deep`（arXiv）
- **`@inproceedings`**（16篇）：ACL/EMNLP/NAACL/EACL/NeurIPS/ICML/ICLR 会议论文 + Findings 论文
- `wu2020emerging` 是唯一带 `doi` 字段的条目（`10.18653/v1/2020.acl-main.536`）
- 特殊字符处理：`Schütze` → `Sch{\"u}tze`，`Viégas` → `Vi{\'e}gas`
- 团队作者用 `{{Qwen Team}}` 双括弧防止 BibTeX 拆分
- "et al." 保留为 `and others`（原始数据未提供完整作者列表）
- 缩写词（LLMs, SAEs, BERT, XNLI, COMET, LangFIR, MEXA, Llama, MT, AI）用 `{}` 保护大小写

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "414dd743-80cc-4692-bb67-be05f1deebb3",
  "isSidechain": true,
  "agentId": "acd089d1966135c41",
  "requestId": "req_011CbHm7fCkPrNMLZduZoLod",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2da93301-844d-420e-bb53-973fa43f3eb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/.claude/sessions/paper_agent_d627ec85",
  "sessionId": "33306ce6-bc65-47b8-8276-72d7d617436c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "enchanted-petting-dahl",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mnsyUsbsGPyNAZLodG4hB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3930,
      "cache_read_input_tokens": 33740,
      "output_tokens": 401,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3930
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 401,
          "cache_read_input_tokens": 33740,
          "cache_creation_input_tokens": 3930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3930,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
