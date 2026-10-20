# paper research cluster2 infra

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 0
- **Tool calls:** 30
- **Original source:** `logs/workers/worker_paper_research_cluster2_infra_20260521T181537.log`
- **Structured JSON:** [`a79680fec01641a2a54b.json`](../../sessions/a7/a79680fec01641a2a54b.json)

## Before a recorded user message

83 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
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
  "uuid": "b88c6efb-a231-44ed-a164-603e8f70163b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-projects-nlp-variance-gtheory/memory/"
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
    "resetsAt": 1779388200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8af9590d-8b88-48f8-ade1-de60fb401f5c",
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current literature_map.yaml and searching for the 3 existing papers plus 2 new ones in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "0bf95967-9ba7-46f3-8e3c-1388b202a8c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192eUueL8DvrnsQa6Kfnrx7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12755,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12755
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

<details open><summary>🔧 Tool call — Read · `toolu_01MXNkxRaxUzxyPSHEBMxYtA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "683a6e8e-a2bb-45b0-86fb-87c9fdffbdcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0192eUueL8DvrnsQa6Kfnrx7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12755,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12755
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

_source line 6 · 2026-05-21T18:15:49.060Z_

<details><summary>↩ Tool result · `toolu_01MXNkxRaxUzxyPSHEBMxYtA`</summary>

```text
1	meta:
2	  last_updated: "2026-05-20T14:00:00Z"
3	  total_papers: 16
4	
5	categories:
6	  - key: "gtheory_evaluation"
7	    name: "G-Theory & Evaluation Variance"
8	    narrative: "Applying Generalizability Theory and variance decomposition to LLM evaluation reliability"
9	  - key: "infrastructure_variance"
10	    name: "Infrastructure-Induced Variance"
11	    narrative: "Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference"
12	  - key: "prompt_sensitivity"
13	    name: "Prompt Sensitivity & Methodological Variance"
14	    narrative: "Prompt phrasing, seed, temperature, and ordering as variance sources"
15	  - key: "evaluation_methodology"
16	    name: "Evaluation Methodology"
17	    narrative: "Scoring artifacts, benchmark design, and evaluation protocol considerations"
18	
19	papers:
20	  mesting2026hidden:
21	    title: "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking"
22	    authors:
23	      - "Messing, S."
24	    year: 2026
25	    venue: "arXiv"
26	    url: "https://arxiv.org/abs/2604.11581"
27	    category: "gtheory_evaluation"
28	    role: "direct-competitor"
29	    relevance: "Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology."
30	    verified: true
31	    added_by: "director"
32	    added_at: "2026-05-20T14:00:00Z"
33	
34	  brittlebench2026:
35	    title: "Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity"
36	    authors: []
37	    year: 2026
38	    venue: "arXiv"
39	    url: "https://arxiv.org/abs/2603.13285"
40	    category: "prompt_sensitivity"
41	    role: "direct-competitor"
42	    relevance: "Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors."
43	    verified: false
44	    added_by: "director"
45	    added_at: "2026-05-20T14:00:00Z"
46	
47	  yuan2025layercast:
48	    title: "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference"
49	    authors:
50	      - "Yuan, Z."
51	    year: 2025
52	    venue: "arXiv"
53	    url: "https://arxiv.org/abs/2506.09501"
54	    category: "infrastructure_variance"
55	    role: "direct-competitor"
56	    relevance: "Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources."
57	    verified: false
58	    added_by: "director"
59	    added_at: "2026-05-20T14:00:00Z"
60	
61	  messina2026background:
62	    title: "Introducing Background Temperature to Characterise Hidden Randomness in LLMs"
63	    authors:
64	      - "Messina, P."
65	      - "Scotta, A."
66	    year: 2026
67	    venue: "arXiv"
68	    url: "https://arxiv.org/abs/2604.22411"
69	    category: "infrastructure_variance"
70	    role: "method-component"
71	    relevance: "Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure."
72	    verified: false
73	    added_by: "director"
74	    added_at: "2026-05-20T14:00:00Z"
75	
76	  generalizit2024:
77	    title: "GeneralizIT: A Python Solution for Generalizability Theory Computations"
78	    authors:
79	      - "Smith, T.J."
80	      - "Kline, T."
81	      - "Kline, A."
82	    year: 2024
83	    venue: "arXiv"
84	    url: "https://arxiv.org/abs/2411.17880"
85	    category: "gtheory_evaluation"
86	    role: "method-component"
87	    relevance: "Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline."
88	    verified: true
89	    added_by: "director"
90	    added_at: "2026-05-20T14:00:00Z"
91	
92	  hua2025flaw:
93	    title: "Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs"
94	    authors:
95	      - "Hua, W."
96	    year: 2025
97	    venue: "EMNLP"
98	    category: "evaluation_methodology"
99	    role: "evaluation"
100	    relevance: "Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring."
101	    verified: false
102	    added_by: "director"
103	    added_at: "2026-05-20T14:00:00Z"
104	
105	  thinkingmachines2025batch:
106	    title: "Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference"
107	    authors: []
108	    year: 2025
109	    venue: "Technical Report"
110	    category: "infrastructure_variance"
111	    role: "method-component"
112	    relevance: "Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions."
113	    verified: false
114	    added_by: "director"
115	    added_at: "2026-05-20T14:00:00Z"
116	
117	  kunievsky2025intent:
118	    title: "Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework"
119	    authors:
120	      - "Kunievsky, N."
121	      - "Evans, J.A."
122	    year: 2025
123	    venue: "arXiv"
124	    url: "https://arxiv.org/abs/2506.16584"
125	    category: "gtheory_evaluation"
126	    role: "direct-competitor"
127	    relevance: "Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against."
128	    verified: true
129	    added_by: "director"
130	    added_at: "2026-05-20T14:00:00Z"
131	
132	  bui2025seeds:
133	    title: "Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models"
134	    authors:
135	      - "Bui, T."
136	    year: 2025
137	    venue: "arXiv"
138	    category: "prompt_sensitivity"
139	    role: "background"
140	    relevance: "Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing."
141	    verified: false
142	    added_by: "director"
143	    added_at: "2026-05-20T14:00:00Z"
144	
145	  sameprompt2026:
146	    title: "Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs"
147	    authors: []
148	    year: 2026
149	    venue: "arXiv"
150	    url: "https://arxiv.org/abs/2602.14349"
151	    category: "prompt_sensitivity"
152	    role: "background"
153	    relevance: "Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing."
154	    verified: false
155	    added_by: "director"
156	    added_at: "2026-05-20T14:00:00Z"
157	
158	  bouthillier2021accounting:
159	    title: "Accounting for Variance in Machine Learning Benchmarks"
160	    authors:
161	      - "Bouthillier, X."
162	      - "Delaunay, P."
163	      - "Bronzi, M."
164	      - "Trofimov, A."
165	      - "Nichyporuk, B."
166	      - "Szeto, J."
167	      - "Sepahvand, N.M."
168	      - "Raff, E."
169	      - "Madan, K."
170	      - "Voleti, V."
171	      - "Kahou, S.E."
172	      - "Michalski, V."
173	      - "Arbel, T."
174	      - "Pal, C."
175	      - "Varoquaux, G."
176	      - "Vincent, P."
177	    year: 2021
178	    venue: "MLSys"
179	    url: "https://arxiv.org/abs/2103.03098"
180	    category: "gtheory_evaluation"
181	    role: "method-component"
182	    relevance: "Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation."
183	    verified: true
184	    added_by: "worker"
185	    added_at: "2026-05-21T00:00:00Z"
186	
187	  shavelson1991generalizability:
188	    title: "Generalizability Theory: A Primer"
189	    authors:
190	      - "Shavelson, R.J."
191	      - "Webb, N.M."
192	    year: 1991
193	    venue: "SAGE Publications"
194	    isbn: "978-0-8039-3744-4"
195	    category: "gtheory_evaluation"
196	    role: "foundational"
197	    relevance: "Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt."
198	    verified: true
199	    added_by: "worker"
200	    added_at: "2026-05-21T00:00:00Z"
201	
202	  brennan2001generalizability:
203	    title: "Generalizability Theory"
204	    authors:
205	      - "Brennan, R.L."
206	    year: 2001
207	    venue: "Springer"
208	    isbn: "978-0-387-95282-6"
209	    category: "gtheory_evaluation"
210	    role: "foundational"
211	    relevance: "Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition."
212	    verified: true
213	    added_by: "worker"
214	    added_at: "2026-05-21T00:00:00Z"
215	
216	  madaan2024quantifying:
217	    title: "Quantifying Variance in Evaluation Benchmarks"
218	    authors:
219	      - "Madaan, L."
220	      - "Singh, A.K."
221	      - "Schaeffer, R."
222	      - "Poulton, A."
223	      - "Koyejo, S."
224	      - "Stenetorp, P."
225	      - "Narang, S."
226	      - "Hupkes, D."
227	    year: 2024
228	    venue: "arXiv"
229	    url: "https://arxiv.org/abs/2406.10229"
230	    category: "gtheory_evaluation"
231	    role: "background"
232	    relevance: "Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon."
233	    verified: true
234	    added_by: "worker"
235	    added_at: "2026-05-21T00:00:00Z"
236	
237	  saleva2025beyond:
238	    title: "Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation"
239	    authors:
240	      - "Sälevä, J."
241	      - "Ataman, D."
242	      - "Lignos, C."
243	    year: 2025
244	    venue: "IJCNLP-AACL"
245	    url: "https://arxiv.org/abs/2509.22612"
246	    category: "gtheory_evaluation"
247	    role: "background"
248	    relevance: "Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error."
249	    verified: true
250	    added_by: "worker"
251	    added_at: "2026-05-21T00:00:00Z"
252	
253	  song2025exploring:
254	    title: "Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory"
255	    authors:
256	      - "Song, D."
257	      - "Lee, W.-C."
258	      - "Jiao, H."
259	    year: 2025
260	    venue: "arXiv"
261	    url: "https://arxiv.org/abs/2507.19980"
262	    category: "gtheory_evaluation"
263	    role: "background"
264	    relevance: "Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation."
265	    verified: true
266	    added_by: "worker"
267	    added_at: "2026-05-21T00:00:00Z"
268	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "df86811f-8038-499c-b782-2182e81182c5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
      "content": "meta:\n  last_updated: \"2026-05-20T14:00:00Z\"\n  total_papers: 16\n\ncategories:\n  - key: \"gtheory_evaluation\"\n    name: \"G-Theory & Evaluation Variance\"\n    narrative: \"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\"\n  - key: \"infrastructure_variance\"\n    name: \"Infrastructure-Induced Variance\"\n    narrative: \"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\"\n  - key: \"prompt_sensitivity\"\n    name: \"Prompt Sensitivity & Methodological Variance\"\n    narrative: \"Prompt phrasing, seed, temperature, and ordering as variance sources\"\n  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n\npapers:\n  mesting2026hidden:\n    title: \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"\n    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
      "numLines": 268,
      "startLine": 1,
      "totalLines": 268
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I'll search for all 5 papers in parallel — verifying the 3 existing ones and finding 2 new ones.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "c17b557d-f15f-4cd9-8345-de53919e6349",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCgQvjwfxYLodUrEzosrid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 24596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4155
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

_source line 8_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CdKait2W6yqFuxPxrpCFiQ`</summary>

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
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "690e4c92-062d-44ff-851d-ae10e6a8614a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCgQvjwfxYLodUrEzosrid",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 24596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4155
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

_source line 9 · 2026-05-21T18:15:52.207Z_

<details><summary>↩ Tool result · `toolu_01CdKait2W6yqFuxPxrpCFiQ`</summary>

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
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "b5f69b4d-b2bd-402d-8b95-784568fced34",
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
Now I'll search for all the papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "8186176b-9f78-47d0-bd04-197630ccd35d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 11_

Searching for all papers in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "f2436301-af47-482a-9b1b-3ff8ba3757f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TN43XDZPdsS5sxVESfAjkq`</summary>

```json
{
  "query": "Yuan LayerCast \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\" arXiv 2506.09501"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "3ed2a951-f81b-4ca4-9351-ca33a3c77672",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Aj8ACiPh4vkLUrYqxRFnw2`</summary>

```json
{
  "query": "Messina Scotta \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\" arXiv 2604.22411"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "0f0b8866-b6df-4417-acda-1585dd05e538",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A3GYguEpKg9ehdBHdVB5pA`</summary>

```json
{
  "query": "\"Batch Invariance Seed Locking\" \"Countering Nondeterminism in LLM Inference\" ThinkingMachines 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "9dc78565-2eb7-4a48-a1cd-8f22c61716bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KzisgvCXZT9edKG16ne1F6`</summary>

```json
{
  "query": "numerical precision GPU nondeterminism LLM inference floating point reproducibility 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "5b936b91-80d7-41c9-a592-fdfdb076bd3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lx7cfPJZYBNiAsapGxN7GM`</summary>

```json
{
  "query": "CUDA nondeterminism deep learning inference hardware variance reproducibility neural network"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "8998d3af-14c1-48ce-9986-64587d3dbf58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BRyM74cHjRNp8AcTr44vd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 632,
      "cache_read_input_tokens": 28751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 632
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

_source line 17 · 2026-05-21T18:16:05.586Z_

<details><summary>↩ Tool result · `toolu_01TN43XDZPdsS5sxVESfAjkq`</summary>

```text
Web search results for query: "Yuan LayerCast "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference" arXiv 2506.09501"

Links: [{"title":"[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/abs/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=Q3qAsZAEZw"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250609501Y/abstract"},{"title":"NeurIPS Poster Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/118169"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | alphaXiv","url":"https://www.alphaxiv.org/overview/2506.09501"},{"title":"NeurIPS 2025 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference Oral","url":"https://neurips.cc/virtual/2025/oral/130305"},{"title":"GitHub - nanomaoli/llm_reproducibility · GitHub","url":"https://github.com/nanomaoli/llm_reproducibility"}]

I found the paper! Here's what I found about it:

This work presents the first systematic investigation into how numerical precision affects reproducibility in LLM inference, quantifying when and how model outputs diverge through carefully controlled experiments across various hardware, software, and precision settings.

The paper demonstrates that LLM reproducibility is fragile—changing system configuration such as evaluation batch size, GPU count, and GPU version can introduce significant differences in generated responses, with this issue being especially pronounced in reasoning models where minor rounding differences in early tokens can cascade into divergent chains of thought.

For instance, under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size.

The root cause of this variability is traced to the non-associative nature of floating-point arithmetic under limited numerical precision.

To address this, the authors develop a lightweight inference pipeline dubbed LayerCast, that stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability.

The paper appears to have been accepted as an oral presentation at NeurIPS 2025, and the code is available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2987115e-c063-476d-8a5f-b1c8707a0a9d",
  "tool_use_result": {
    "query": "Yuan LayerCast \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\" arXiv 2506.09501",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Roke6bXwohx7X23VrKkcoX",
        "content": [
          {
            "title": "[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/abs/2506.09501"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | OpenReview",
            "url": "https://openreview.net/forum?id=Q3qAsZAEZw"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/html/2506.09501v2"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250609501Y/abstract"
          },
          {
            "title": "NeurIPS Poster Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://neurips.cc/virtual/2025/poster/118169"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2506.09501"
          },
          {
            "title": "NeurIPS 2025 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference Oral",
            "url": "https://neurips.cc/virtual/2025/oral/130305"
          },
          {
            "title": "GitHub - nanomaoli/llm_reproducibility · GitHub",
            "url": "https://github.com/nanomaoli/llm_reproducibility"
          }
        ]
      },
      "I found the paper! Here's what I found about it:\n\nThis work presents the first systematic investigation into how numerical precision affects reproducibility in LLM inference, quantifying when and how model outputs diverge through carefully controlled experiments across various hardware, software, and precision settings.\n\nThe paper demonstrates that LLM reproducibility is fragile—changing system configuration such as evaluation batch size, GPU count, and GPU version can introduce significant differences in generated responses, with this issue being especially pronounced in reasoning models where minor rounding differences in early tokens can cascade into divergent chains of thought.\n\nFor instance, under bfloat16 precision with greedy decoding, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size.\n\nThe root cause of this variability is traced to the non-associative nature of floating-point arithmetic under limited numerical precision.\n\nTo address this, the authors develop a lightweight inference pipeline dubbed LayerCast, that stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability.\n\nThe paper appears to have been accepted as an oral presentation at NeurIPS 2025, and the code is available on GitHub."
    ],
    "durationSeconds": 5.582379312000001
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T18:16:07.872Z_

<details><summary>↩ Tool result · `toolu_01Aj8ACiPh4vkLUrYqxRFnw2`</summary>

```text
Web search results for query: "Messina Scotta "Introducing Background Temperature to Characterise Hidden Randomness in LLMs" arXiv 2604.22411"

Links: [{"title":"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models","url":"https://arxiv.org/html/2604.22411"},{"title":"[2604.22411] Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models","url":"https://arxiv.org/abs/2604.22411"},{"title":"The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior","url":"https://arxiv.org/pdf/2512.12066"},{"title":"[2604.22771] The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model Token Distributions","url":"https://arxiv.org/abs/2604.22771"},{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12375657/"}]

I found the paper! Here's what the search reveals:

The paper "Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models" is by Alberto Messina and Stefano Scotta from RAI (Radiotelevisione Italiana), Centre for Research, Technological Innovation and Experimentation (CRITS), published on arXiv as 2604.22411 on April 24, 2026.

The paper addresses how large language models can produce divergent outputs for identical inputs even when decoding with temperature T=0. Recent work has highlighted implementation-level sources of nondeterminism, including batch-size variation, kernel non-invariance, and floating-point non-associativity.

The authors formalize this behavior by introducing the notion of "background temperature" (T_bg), the effective temperature induced by an implementation-dependent perturbation process observed even when nominal T=0. They provide clean definitions, show how T_bg relates to a stochastic perturbation governed by the inference environment, and propose an empirical protocol to estimate T_bg via the equivalent temperature T_n(I) of an ideal reference system.

You can access the full paper at https://arxiv.org/html/2604.22411 or https://arxiv.org/abs/2604.22411.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "e18ba5e3-8cc6-4156-85be-049b44ab5c42",
  "tool_use_result": {
    "query": "Messina Scotta \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\" arXiv 2604.22411",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N1Ern1wKFqsnMmzaTUVH38",
        "content": [
          {
            "title": "Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models",
            "url": "https://arxiv.org/html/2604.22411"
          },
          {
            "title": "[2604.22411] Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models",
            "url": "https://arxiv.org/abs/2604.22411"
          },
          {
            "title": "The Instability of Safety: How Random Seeds and Temperature Expose Inconsistent LLM Refusal Behavior",
            "url": "https://arxiv.org/pdf/2512.12066"
          },
          {
            "title": "[2604.22771] The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model Token Distributions",
            "url": "https://arxiv.org/abs/2604.22771"
          },
          {
            "title": "An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12375657/"
          }
        ]
      },
      "I found the paper! Here's what the search reveals:\n\nThe paper \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\" is by Alberto Messina and Stefano Scotta from RAI (Radiotelevisione Italiana), Centre for Research, Technological Innovation and Experimentation (CRITS), published on arXiv as 2604.22411 on April 24, 2026.\n\nThe paper addresses how large language models can produce divergent outputs for identical inputs even when decoding with temperature T=0. Recent work has highlighted implementation-level sources of nondeterminism, including batch-size variation, kernel non-invariance, and floating-point non-associativity.\n\nThe authors formalize this behavior by introducing the notion of \"background temperature\" (T_bg), the effective temperature induced by an implementation-dependent perturbation process observed even when nominal T=0. They provide clean definitions, show how T_bg relates to a stochastic perturbation governed by the inference environment, and propose an empirical protocol to estimate T_bg via the equivalent temperature T_n(I) of an ideal reference system.\n\nYou can access the full paper at https://arxiv.org/html/2604.22411 or https://arxiv.org/abs/2604.22411."
    ],
    "durationSeconds": 6.507464074
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T18:16:10.772Z_

<details><summary>↩ Tool result · `toolu_01KzisgvCXZT9edKG16ne1F6`</summary>

```text
Web search results for query: "numerical precision GPU nondeterminism LLM inference floating point reproducibility 2024 2025"

Links: [{"title":"[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/abs/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | OpenReview","url":"https://openreview.net/forum?id=Q3qAsZAEZw"},{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"NeurIPS Poster Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://neurips.cc/virtual/2025/poster/118169"},{"title":"NeurIPS 2025 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference Oral","url":"https://neurips.cc/virtual/2025/loc/mexico-city/oral/130305"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250609501Y/abstract"},{"title":"GitHub - nanomaoli/llm_reproducibility · GitHub","url":"https://github.com/nanomaoli/llm_reproducibility"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.17826"}]

Here are the search results for your query on numerical precision, GPU nondeterminism, LLM inference, floating point, and reproducibility from 2024-2025:

## Key Findings

The first systematic investigation into how numerical precision affects reproducibility in LLM inference was recently published. Changing system configuration, such as evaluation batch size, GPU count, and GPU version, can introduce significant differences in the generated responses.

This issue is especially pronounced in reasoning models, where minor rounding differences in early tokens can cascade into divergent chains of thought, ultimately affecting accuracy. Notably, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size under bfloat16 precision.

## Root Causes

The root cause of this variability is traced to the non-associative nature of floating-point arithmetic under limited numerical precision. The fundamental cause of nondeterministic outputs is the small gap between competing logits, which makes token selection vulnerable to minute numerical fluctuations.

## Solutions

LayerCast is a lightweight inference pipeline that stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability. Additionally, TBIK is a framework for achieving deterministic LLM inference across different TP sizes that eliminates nondeterminism caused by floating-point non-associativity and delivers bit-wise identical outputs across batch sizes, TP configurations, and frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "5c05d461-fc2c-43dc-97f8-a2193611989e",
  "tool_use_result": {
    "query": "numerical precision GPU nondeterminism LLM inference floating point reproducibility 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_019QzomsxKjmqyBAeJco1LVd",
        "content": [
          {
            "title": "[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/abs/2506.09501"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference | OpenReview",
            "url": "https://openreview.net/forum?id=Q3qAsZAEZw"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of ...",
            "url": "https://arxiv.org/pdf/2506.09501"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab",
            "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/html/2506.09501v2"
          },
          {
            "title": "NeurIPS Poster Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://neurips.cc/virtual/2025/poster/118169"
          },
          {
            "title": "NeurIPS 2025 Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference Oral",
            "url": "https://neurips.cc/virtual/2025/loc/mexico-city/oral/130305"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250609501Y/abstract"
          },
          {
            "title": "GitHub - nanomaoli/llm_reproducibility · GitHub",
            "url": "https://github.com/nanomaoli/llm_reproducibility"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.17826"
          }
        ]
      },
      "Here are the search results for your query on numerical precision, GPU nondeterminism, LLM inference, floating point, and reproducibility from 2024-2025:\n\n## Key Findings\n\nThe first systematic investigation into how numerical precision affects reproducibility in LLM inference was recently published. Changing system configuration, such as evaluation batch size, GPU count, and GPU version, can introduce significant differences in the generated responses.\n\nThis issue is especially pronounced in reasoning models, where minor rounding differences in early tokens can cascade into divergent chains of thought, ultimately affecting accuracy. Notably, a reasoning model like DeepSeek-R1-Distill-Qwen-7B can exhibit up to 9% variation in accuracy and 9,000 tokens difference in response length due to differences in GPU count, type, and evaluation batch size under bfloat16 precision.\n\n## Root Causes\n\nThe root cause of this variability is traced to the non-associative nature of floating-point arithmetic under limited numerical precision. The fundamental cause of nondeterministic outputs is the small gap between competing logits, which makes token selection vulnerable to minute numerical fluctuations.\n\n## Solutions\n\nLayerCast is a lightweight inference pipeline that stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability. Additionally, TBIK is a framework for achieving deterministic LLM inference across different TP sizes that eliminates nondeterminism caused by floating-point non-associativity and delivers bit-wise identical outputs across batch sizes, TP configurations, and frameworks."
    ],
    "durationSeconds": 7.412739878999997
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T18:16:10.834Z_

<details><summary>↩ Tool result · `toolu_01A3GYguEpKg9ehdBHdVB5pA`</summary>

```text
Web search results for query: ""Batch Invariance Seed Locking" "Countering Nondeterminism in LLM Inference" ThinkingMachines 2025"

Links: [{"title":"Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"},{"title":"(PDF) BATCH INVARIANCE, SEED LOCKING, AND BEYOND: COUNTERING NONDETERMINISM IN LLM INFERENCE","url":"https://www.researchgate.net/publication/395667341_BATCH_INVARIANCE_SEED_LOCKING_AND_BEYOND_COUNTERING_NONDETERMINISM_IN_LLM_INFERENCE"},{"title":"Defeating Nondeterminism in LLM Inference: Theory to Deterministic Code Edits | Morph","url":"https://www.morphllm.com/defeating-nondeterminism-llm-inference"},{"title":"Defeating Nondeterminism in LLM Inference","url":"https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Musing 137: Defeating Nondeterminism in LLM Inference","url":"https://aiscientist.substack.com/p/musing-137-defeating-nondeterminism"},{"title":"Defeating nondeterminism in LLM inference, in practice | by Siddhant Gupta | Medium","url":"https://medium.com/@siddhantg314/defeating-nondeterminism-in-llm-inference-in-practice-38a7dd1e4112"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Explained: Defeating Nondeterminism in LLM Inference","url":"https://www.llmwatch.com/p/eli5-defeating-nondeterminism-in"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury","url":"https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"}]

I found relevant results for your search. Here's what the research shows:

## Overview

Thinking Machines Lab argue that user-visible nondeterminism primarily arises from batch-size variation: non-batch-invariant kernels change reduction orders as load fluctuates, altering logits even at T = 0; they supply batch-invariant RMSNorm/GEMM/attention kernels that restore determinism with modest overheads.

## Key Findings

In September 2025, Thinking Machines Lab demonstrated that the primary source of LLM inference nondeterminism is batch variance, not floating-point non-associativity from concurrent GPU threads. Despite determinism within individual kernels, LLM inference is system-level nondeterministic because output depends on batch size — a property known as batch invariance. Many kernels (matmul, RMSNorm, attention) change numerical output for a sample, depending on the overall batch size of the operation.

## Practical Results

Empirically, under default vLLM with Qwen-3-8B at T =0 they observed 80/1000 unique completions; enabling batch-invariant RMSNorm/GEMM/attention restored 1000/1000 identical outputs with a 1.6-2.1× latency trade-off. The thinking-machines-lab/batch_invariant_ops code that accompanies this paper addresses this by providing a PyTorch implementation of invariant kernels and demonstrates them running Qwen3-8B deterministically under vLLM.

## Significance

The paper reframes LLM nondeterminism as an engineering bug (batch-sensitive kernels) rather than an inevitable hardware limitation, and provides a practical, open-source fix that achieves mathematically perfect reproducibility without sacrificing the benefits of batching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "f8870588-aebf-4e41-bbdc-e8ec53eb18ba",
  "tool_use_result": {
    "query": "\"Batch Invariance Seed Locking\" \"Countering Nondeterminism in LLM Inference\" ThinkingMachines 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FJo8LoBgKpFF6aJ1CwgVLK",
        "content": [
          {
            "title": "Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium",
            "url": "https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"
          },
          {
            "title": "(PDF) BATCH INVARIANCE, SEED LOCKING, AND BEYOND: COUNTERING NONDETERMINISM IN LLM INFERENCE",
            "url": "https://www.researchgate.net/publication/395667341_BATCH_INVARIANCE_SEED_LOCKING_AND_BEYOND_COUNTERING_NONDETERMINISM_IN_LLM_INFERENCE"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference: Theory to Deterministic Code Edits | Morph",
            "url": "https://www.morphllm.com/defeating-nondeterminism-llm-inference"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference",
            "url": "https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com",
            "url": "https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"
          },
          {
            "title": "Musing 137: Defeating Nondeterminism in LLM Inference",
            "url": "https://aiscientist.substack.com/p/musing-137-defeating-nondeterminism"
          },
          {
            "title": "Defeating nondeterminism in LLM inference, in practice | by Siddhant Gupta | Medium",
            "url": "https://medium.com/@siddhantg314/defeating-nondeterminism-in-llm-inference-in-practice-38a7dd1e4112"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab",
            "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"
          },
          {
            "title": "Explained: Defeating Nondeterminism in LLM Inference",
            "url": "https://www.llmwatch.com/p/eli5-defeating-nondeterminism-in"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury",
            "url": "https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"
          }
        ]
      },
      "I found relevant results for your search. Here's what the research shows:\n\n## Overview\n\nThinking Machines Lab argue that user-visible nondeterminism primarily arises from batch-size variation: non-batch-invariant kernels change reduction orders as load fluctuates, altering logits even at T = 0; they supply batch-invariant RMSNorm/GEMM/attention kernels that restore determinism with modest overheads.\n\n## Key Findings\n\nIn September 2025, Thinking Machines Lab demonstrated that the primary source of LLM inference nondeterminism is batch variance, not floating-point non-associativity from concurrent GPU threads. Despite determinism within individual kernels, LLM inference is system-level nondeterministic because output depends on batch size — a property known as batch invariance. Many kernels (matmul, RMSNorm, attention) change numerical output for a sample, depending on the overall batch size of the operation.\n\n## Practical Results\n\nEmpirically, under default vLLM with Qwen-3-8B at T =0 they observed 80/1000 unique completions; enabling batch-invariant RMSNorm/GEMM/attention restored 1000/1000 identical outputs with a 1.6-2.1× latency trade-off. The thinking-machines-lab/batch_invariant_ops code that accompanies this paper addresses this by providing a PyTorch implementation of invariant kernels and demonstrates them running Qwen3-8B deterministically under vLLM.\n\n## Significance\n\nThe paper reframes LLM nondeterminism as an engineering bug (batch-sensitive kernels) rather than an inevitable hardware limitation, and provides a practical, open-source fix that achieves mathematically perfect reproducibility without sacrificing the benefits of batching."
    ],
    "durationSeconds": 8.504446368
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T18:16:11.472Z_

<details><summary>↩ Tool result · `toolu_01Lx7cfPJZYBNiAsapGxN7GM`</summary>

```text
Web search results for query: "CUDA nondeterminism deep learning inference hardware variance reproducibility neural network"

Links: [{"title":"Solving Reproducibility Challenges in Deep Learning and LLMs: Our Journey","url":"https://www.ingonyama.com/post/solving-reproducibility-challenges-in-deep-learning-and-llms-our-journey"},{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"IMPLEMENTATIONS OF THE PARALLEL SUM IN CUDA. NON-DETERMINISTIC... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/IMPLEMENTATIONS-OF-THE-PARALLEL-SUM-IN-CUDA-NON-DETERMINISTIC-IMPLEMENTATIONS-SHOWN-IN_tbl2_387848485"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"Issues in the Reproducibility of Deep Learning Results","url":"https://par.nsf.gov/servlets/purl/10199663"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC   and deep learning applications","url":"https://arxiv.org/pdf/2408.05148"},{"title":"Defeating Nondeterminism: Achieving Predictable LLM Inference for AI Reliability","url":"https://nishadil.com/news/unlocking-predictability-conquering-nondeterminism-in-llm-inference-for-a-reliable-ai-future/3fcac37c348c0f9edcbac001a1d206c7"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow","url":"https://arxiv.org/html/2408.05148v3"}]

I've found comprehensive information on CUDA nondeterminism in deep learning inference. Here are the key findings:

## Nondeterminism Sources

The source of nondeterminism can be traced to CUDA machine code (PTX files), with some kernels generating different instructions depending on the target architecture.

Floating-point operations maintain their inherent non-determinism even when weights are quantized, as unquantized layers and dequantization during inference are part of the computation pipeline.

## Hardware Variance

Different GPU architectures exhibit different levels of probability variance, with A100s generally showing slightly higher probability variance than L40S under identical configurations, likely due to differences in hardware-level floating-point implementations and memory hierarchies.

These effects are most pronounced under BF16 precision due to its limited mantissa bits making it especially susceptible to rounding effects.

## Batch Size Impact

Smaller batch sizes produce higher variance in token probabilities because they require more sequential processing steps that accumulate rounding errors, while larger batches benefit from parallel computation within optimized CUDA kernels that limit error accumulation.

## Reproducibility Solutions

Solutions include pinning specific versions of software dependencies from the operating system and CUDA drivers to deep learning frameworks, and employing deterministic algorithms that ensure parallel operations are performed in a strictly ordered fashion or aggregated deterministically.

Deterministic implementations can perform as fast or only slightly slower than non-deterministic counterparts, suggesting that determinism doesn't necessarily require performance trade-offs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "d1d06957-2ae9-4485-b249-d53559bb373c",
  "tool_use_result": {
    "query": "CUDA nondeterminism deep learning inference hardware variance reproducibility neural network",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WbEQwCZkHpweuuKSG8EL46",
        "content": [
          {
            "title": "Solving Reproducibility Challenges in Deep Learning and LLMs: Our Journey",
            "url": "https://www.ingonyama.com/post/solving-reproducibility-challenges-in-deep-learning-and-llms-our-journey"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of ...",
            "url": "https://arxiv.org/pdf/2506.09501"
          },
          {
            "title": "IMPLEMENTATIONS OF THE PARALLEL SUM IN CUDA. NON-DETERMINISTIC... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/IMPLEMENTATIONS-OF-THE-PARALLEL-SUM-IN-CUDA-NON-DETERMINISTIC-IMPLEMENTATIONS-SHOWN-IN_tbl2_387848485"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/html/2506.09501v2"
          },
          {
            "title": "Issues in the Reproducibility of Deep Learning Results",
            "url": "https://par.nsf.gov/servlets/purl/10199663"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC   and deep learning applications",
            "url": "https://arxiv.org/pdf/2408.05148"
          },
          {
            "title": "Defeating Nondeterminism: Achieving Predictable LLM Inference for AI Reliability",
            "url": "https://nishadil.com/news/unlocking-predictability-conquering-nondeterminism-in-llm-inference-for-a-reliable-ai-future/3fcac37c348c0f9edcbac001a1d206c7"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow",
            "url": "https://arxiv.org/html/2408.05148v3"
          }
        ]
      },
      "I've found comprehensive information on CUDA nondeterminism in deep learning inference. Here are the key findings:\n\n## Nondeterminism Sources\n\nThe source of nondeterminism can be traced to CUDA machine code (PTX files), with some kernels generating different instructions depending on the target architecture.\n\nFloating-point operations maintain their inherent non-determinism even when weights are quantized, as unquantized layers and dequantization during inference are part of the computation pipeline.\n\n## Hardware Variance\n\nDifferent GPU architectures exhibit different levels of probability variance, with A100s generally showing slightly higher probability variance than L40S under identical configurations, likely due to differences in hardware-level floating-point implementations and memory hierarchies.\n\nThese effects are most pronounced under BF16 precision due to its limited mantissa bits making it especially susceptible to rounding effects.\n\n## Batch Size Impact\n\nSmaller batch sizes produce higher variance in token probabilities because they require more sequential processing steps that accumulate rounding errors, while larger batches benefit from parallel computation within optimized CUDA kernels that limit error accumulation.\n\n## Reproducibility Solutions\n\nSolutions include pinning specific versions of software dependencies from the operating system and CUDA drivers to deep learning frameworks, and employing deterministic algorithms that ensure parallel operations are performed in a strictly ordered fashion or aggregated deterministically.\n\nDeterministic implementations can perform as fast or only slightly slower than non-deterministic counterparts, suggesting that determinism doesn't necessarily require performance trade-offs."
    ],
    "durationSeconds": 7.555049843000001
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Good, I've verified the three existing papers and found some leads. Let me now search more specifically for:

1. The exact authors and venue for Yuan et al. 2025 (I see it was accepted at NeurIPS 2025 as an oral)
2. The exact authors for Messina & Scotta 2026
3. The ThinkingMachines paper details - it's a blog post from Thinking Machines Lab
4. Two new papers for infrastructure variance

From the search results:
- Yuan et al. 2025: NeurIPS 2025 (oral). Need full author list.


- Messina & Scotta 2026: arXiv 2604.22411, with Alberto Messina and Stefano Scotta from RAI
- ThinkingMachines 2025: Blog post at thinkingmachines.ai, also on ResearchGate, but still need to track down the authors

I'm also spotting some promising new papers on infrastructure variance—particularly one on floating-point non-associativity and its effects on reproducibility in HPC and deep learning (arXiv 2408.05148), plus the Ingonyama blog post and possibly a TBIK paper. Let me dig deeper into these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "1617d0a3-c391-447d-88c4-d79f38c9462d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnqWx8ta89Vpqc4XEBCYNY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 29383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4897
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

_source line 23_

Found all 3 existing papers. Now searching for more details and new papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "a481b419-811e-4593-b718-7b66dd5c3d15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnqWx8ta89Vpqc4XEBCYNY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 29383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4897
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018RE4ni3KKpdagKwwodBkxZ`</summary>

```json
{
  "query": "arXiv 2506.09501 Yuan LayerCast authors full list NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "3279cfec-2ebc-408f-9a54-e6a3afc48d9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnqWx8ta89Vpqc4XEBCYNY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 29383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4897
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SoXNCPPcSxQxEhCrJn16gb`</summary>

```json
{
  "query": "\"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications\" arXiv 2408.05148 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "5341d838-8e4b-42b7-a47d-bf03af9e15e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnqWx8ta89Vpqc4XEBCYNY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 29383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4897
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_016HJ3baoRVbikieLBvjZgkT`</summary>

```json
{
  "query": "Thinking Machines Lab \"batch invariance\" nondeterminism LLM authors blog 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "30949ad5-f3c1-4f55-835d-fd489d6594bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnqWx8ta89Vpqc4XEBCYNY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 29383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4897
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015CWYUBsHaJow9WeSADS9w7`</summary>

```json
{
  "query": "GPU hardware type LLM inference accuracy variation empirical study A100 H100 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "fa8b23d6-564a-43cd-9dd5-9c3d76e26a76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KnqWx8ta89Vpqc4XEBCYNY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4897,
      "cache_read_input_tokens": 29383,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4897
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

_source line 28 · 2026-05-21T18:16:36.791Z_

<details><summary>↩ Tool result · `toolu_01SoXNCPPcSxQxEhCrJn16gb`</summary>

```text
Web search results for query: ""Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications" arXiv 2408.05148 authors"

Links: [{"title":"[Literature Review] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://www.themoonlight.io/en/review/impacts-of-floating-point-non-associativity-on-reproducibility-for-hpc-and-deep-learning-applications"},{"title":"[2408.05148] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://arxiv.org/abs/2408.05148"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | ORNL","url":"https://www.ornl.gov/publication/impacts-floating-point-non-associativity-reproducibility-hpc-and-deep-learning"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/iel8/10820557/10820558/10820674.pdf"},{"title":"(PDF) Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://www.researchgate.net/publication/387848485_Impacts_of_floating-point_non-associativity_on_reproducibility_for_HPC_and_deep_learning_applications"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow","url":"https://arxiv.org/html/2408.05148v1"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis","url":"https://dl.acm.org/doi/10.1109/SCW63240.2024.00028"},{"title":"au:Shanmugavelu_S in:cs - SciRate Search","url":"https://scirate.com/search?q=au:Shanmugavelu_S+in:cs"},{"title":"Impacts of floating-point non-associativity on reproducibility ...","url":"https://arxiv.org/pdf/2408.05148"},{"title":"dblp: Ada Sedova","url":"https://dblp.org/pid/234/2258.html"}]

Based on the search results, here is the information about the arXiv paper 2408.05148:

**Paper Title:** Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications

**Authors:** Sanjif Shanmugavelu, Mathieu Taillefumier, Christopher Culver, Oscar Hernandez, Mark Coletti, Ada Sedova

**Overview:** The paper investigates the statistical properties of floating-point non-associativity within modern parallel programming models. Run to run variability in parallel programs caused by floating-point non-associativity has been known to significantly affect reproducibility in iterative algorithms, due to accumulating errors, and the sensitivity of deep learning training and inference pipelines to floating-point non-associativity has been found to sometimes be extreme.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "ae22c669-eb25-4ac6-84f0-19468ea239a4",
  "tool_use_result": {
    "query": "\"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications\" arXiv 2408.05148 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gos81BZWFheit4o6StC29L",
        "content": [
          {
            "title": "[Literature Review] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications",
            "url": "https://www.themoonlight.io/en/review/impacts-of-floating-point-non-associativity-on-reproducibility-for-hpc-and-deep-learning-applications"
          },
          {
            "title": "[2408.05148] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications",
            "url": "https://arxiv.org/abs/2408.05148"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | ORNL",
            "url": "https://www.ornl.gov/publication/impacts-floating-point-non-associativity-reproducibility-hpc-and-deep-learning"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | IEEE Conference Publication | IEEE Xplore",
            "url": "https://ieeexplore.ieee.org/iel8/10820557/10820558/10820674.pdf"
          },
          {
            "title": "(PDF) Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications",
            "url": "https://www.researchgate.net/publication/387848485_Impacts_of_floating-point_non-associativity_on_reproducibility_for_HPC_and_deep_learning_applications"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications This manuscript has been authored by UT-Battelle, LLC under Contract No. DE-AC05-00OR22725 with the U.S. Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a non-exclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow",
            "url": "https://arxiv.org/html/2408.05148v1"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis",
            "url": "https://dl.acm.org/doi/10.1109/SCW63240.2024.00028"
          },
          {
            "title": "au:Shanmugavelu_S in:cs - SciRate Search",
            "url": "https://scirate.com/search?q=au:Shanmugavelu_S+in:cs"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility ...",
            "url": "https://arxiv.org/pdf/2408.05148"
          },
          {
            "title": "dblp: Ada Sedova",
            "url": "https://dblp.org/pid/234/2258.html"
          }
        ]
      },
      "Based on the search results, here is the information about the arXiv paper 2408.05148:\n\n**Paper Title:** Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications\n\n**Authors:** Sanjif Shanmugavelu, Mathieu Taillefumier, Christopher Culver, Oscar Hernandez, Mark Coletti, Ada Sedova\n\n**Overview:** The paper investigates the statistical properties of floating-point non-associativity within modern parallel programming models. Run to run variability in parallel programs caused by floating-point non-associativity has been known to significantly affect reproducibility in iterative algorithms, due to accumulating errors, and the sensitivity of deep learning training and inference pipelines to floating-point non-associativity has been found to sometimes be extreme."
    ],
    "durationSeconds": 4.910937491999997
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-21T18:16:38.854Z_

<details><summary>↩ Tool result · `toolu_015CWYUBsHaJow9WeSADS9w7`</summary>

```text
Web search results for query: "GPU hardware type LLM inference accuracy variation empirical study A100 H100 2024 2025"

Links: [{"title":"Private LLM Inference on Consumer Blackwell GPUs:","url":"https://arxiv.org/pdf/2601.09527"},{"title":"Best GPUs for LLM inference in 2025 | WhiteFiber","url":"https://www.whitefiber.com/compare/best-gpus-for-llm-inference-in-2025"},{"title":"Which GPUs Are Best Optimized for LLM Inference Workloads?","url":"https://www.gmicloud.ai/en/blog/which-gpus-are-best-optimized-for-llm-inference-workloads"},{"title":"LLM-Inference-Bench: Inference Benchmarking of","url":"https://arxiv.org/pdf/2411.00136"},{"title":"Understanding Performance Implications of LLM Inference on CPUs","url":"https://par.nsf.gov/servlets/purl/10576248"},{"title":"Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective","url":"https://arxiv.org/html/2410.04466v3"}]

I've completed the web search for your query. Here's what I found:

## Key Research Findings

The search results reveal several relevant studies on GPU hardware performance for LLM inference, particularly comparing A100 and H100 GPUs:

**Performance Comparisons:**
For a batch size of 64, LLaMA-3-70B on H100 is 7.8x faster than A100. Additionally, H100 GPU scales efficiently with an increase in batch size due to large DRAM and tensor core utilization compared to A100.

**Empirical Studies:**
- One benchmark study (LLM-Inference-Bench) evaluated LLaMA-3-8B and Mistral-7B on A100 and H100 GPUs, examining various inference optimization techniques.

- Another comprehensive hardware perspective study achieved 113.7-121.7 tokens/s on NVIDIA A100 GPUs for Llama3-8B with 4-bit quantization.

**Recent 2025 Research:**
A recent systematic evaluation of consumer GPUs benchmarked four open-weight models across 79 configurations spanning quantization formats (BF16, W4A16, NVFP4, MXFP4), context lengths (8k–64k), and three workloads: RAG, multi-LoRA agentic serving, and high-concurrency APIs.

The search results indicate growing research interest in GPU hardware variations for LLM inference, though most studies focus on performance/throughput rather than accuracy variations across different hardware types.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "74d01549-e709-474e-8af1-97af8eed72a9",
  "tool_use_result": {
    "query": "GPU hardware type LLM inference accuracy variation empirical study A100 H100 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KaG2TJQx6G6EPVkrMANcLh",
        "content": [
          {
            "title": "Private LLM Inference on Consumer Blackwell GPUs:",
            "url": "https://arxiv.org/pdf/2601.09527"
          },
          {
            "title": "Best GPUs for LLM inference in 2025 | WhiteFiber",
            "url": "https://www.whitefiber.com/compare/best-gpus-for-llm-inference-in-2025"
          },
          {
            "title": "Which GPUs Are Best Optimized for LLM Inference Workloads?",
            "url": "https://www.gmicloud.ai/en/blog/which-gpus-are-best-optimized-for-llm-inference-workloads"
          },
          {
            "title": "LLM-Inference-Bench: Inference Benchmarking of",
            "url": "https://arxiv.org/pdf/2411.00136"
          },
          {
            "title": "Understanding Performance Implications of LLM Inference on CPUs",
            "url": "https://par.nsf.gov/servlets/purl/10576248"
          },
          {
            "title": "Large Language Model Inference Acceleration: A Comprehensive Hardware Perspective",
            "url": "https://arxiv.org/html/2410.04466v3"
          }
        ]
      },
      "I've completed the web search for your query. Here's what I found:\n\n## Key Research Findings\n\nThe search results reveal several relevant studies on GPU hardware performance for LLM inference, particularly comparing A100 and H100 GPUs:\n\n**Performance Comparisons:**\nFor a batch size of 64, LLaMA-3-70B on H100 is 7.8x faster than A100. Additionally, H100 GPU scales efficiently with an increase in batch size due to large DRAM and tensor core utilization compared to A100.\n\n**Empirical Studies:**\n- One benchmark study (LLM-Inference-Bench) evaluated LLaMA-3-8B and Mistral-7B on A100 and H100 GPUs, examining various inference optimization techniques.\n\n- Another comprehensive hardware perspective study achieved 113.7-121.7 tokens/s on NVIDIA A100 GPUs for Llama3-8B with 4-bit quantization.\n\n**Recent 2025 Research:**\nA recent systematic evaluation of consumer GPUs benchmarked four open-weight models across 79 configurations spanning quantization formats (BF16, W4A16, NVFP4, MXFP4), context lengths (8k–64k), and three workloads: RAG, multi-LoRA agentic serving, and high-concurrency APIs.\n\nThe search results indicate growing research interest in GPU hardware variations for LLM inference, though most studies focus on performance/throughput rather than accuracy variations across different hardware types."
    ],
    "durationSeconds": 6.946539667999998
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T18:16:39.505Z_

<details><summary>↩ Tool result · `toolu_016HJ3baoRVbikieLBvjZgkT`</summary>

```text
Web search results for query: "Thinking Machines Lab "batch invariance" nondeterminism LLM authors blog 2025"

Links: [{"title":"Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"},{"title":"Defeating Nondeterminism in LLM Inference","url":"https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/"},{"title":"Defeating nondeterminism in LLM inference, in practice | by Siddhant Gupta | Medium","url":"https://medium.com/@siddhantg314/defeating-nondeterminism-in-llm-inference-in-practice-38a7dd1e4112"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Towards Deterministic Inference in SGLang and Reproducible RL Training - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-09-22-sglang-deterministic/"},{"title":"The Deterministic LLM: Engineering Batch Invariance to Restore Data Integrity in Inference Pipelines","url":"https://blog.singlr.ai/non_deterministic_llm/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury","url":"https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines ...","url":"https://www.mbgsec.com/_archive/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"},{"title":"Billion-Dollar Unicorn Releases Long Article Solving LLM Inference Non - Deterministic Problem in First Public Statement After 7 - Month Establishment","url":"https://eu.36kr.com/en/p/3461963944908162"}]

Based on the search results, here's what I found about the Thinking Machines Lab work on batch invariance and nondeterminism in LLMs:

## Overview

This paper is the first public output from Thinking Machines, the AI Lab founded in February 2025 by Mira Murati, OpenAI's former CTO (and interim CEO for a few days). The work is titled "Defeating Nondeterminism in LLM Inference" by Horace He and Thinking Machines Lab, published in September 2025.

## The Core Problem

Despite determinism within individual kernels, LLM inference is system-level nondeterministic because output depends on batch size — a property known as batch invariance. When serving requests in production, batch size can fluctuate unpredictably due to system load, causing outputs to change even for identical requests.

## The Solution

To ensure reproducible inference, kernels must be batch-invariant — the computation for each element should not depend on the batch size or position within the batch. The thinking-machines-lab/batch_invariant_ops code that accompanies this paper addresses this by providing a PyTorch implementation of invariant kernels and demonstrates them running Qwen3-8B deterministically under vLLM.

## Broader Impact

The paper reframes LLM nondeterminism as an engineering bug (batch-sensitive kernels) rather than an inevitable hardware limitation, and provides a practical, open-source fix that achieves mathematically perfect reproducibility without sacrificing the benefits of batching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "fb12a516-9eae-4143-a28e-5e90344dc7e4",
  "tool_use_result": {
    "query": "Thinking Machines Lab \"batch invariance\" nondeterminism LLM authors blog 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M15x9V4jRrdUPrSQF71b72",
        "content": [
          {
            "title": "Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium",
            "url": "https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference",
            "url": "https://simonwillison.net/2025/Sep/11/defeating-nondeterminism/"
          },
          {
            "title": "Defeating nondeterminism in LLM inference, in practice | by Siddhant Gupta | Medium",
            "url": "https://medium.com/@siddhantg314/defeating-nondeterminism-in-llm-inference-in-practice-38a7dd1e4112"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab",
            "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"
          },
          {
            "title": "Towards Deterministic Inference in SGLang and Reproducible RL Training - LMSYS Blog | LMSYS Org",
            "url": "https://www.lmsys.org/blog/2025-09-22-sglang-deterministic/"
          },
          {
            "title": "The Deterministic LLM: Engineering Batch Invariance to Restore Data Integrity in Inference Pipelines",
            "url": "https://blog.singlr.ai/non_deterministic_llm/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com",
            "url": "https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury",
            "url": "https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines ...",
            "url": "https://www.mbgsec.com/_archive/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"
          },
          {
            "title": "Billion-Dollar Unicorn Releases Long Article Solving LLM Inference Non - Deterministic Problem in First Public Statement After 7 - Month Establishment",
            "url": "https://eu.36kr.com/en/p/3461963944908162"
          }
        ]
      },
      "Based on the search results, here's what I found about the Thinking Machines Lab work on batch invariance and nondeterminism in LLMs:\n\n## Overview\n\nThis paper is the first public output from Thinking Machines, the AI Lab founded in February 2025 by Mira Murati, OpenAI's former CTO (and interim CEO for a few days). The work is titled \"Defeating Nondeterminism in LLM Inference\" by Horace He and Thinking Machines Lab, published in September 2025.\n\n## The Core Problem\n\nDespite determinism within individual kernels, LLM inference is system-level nondeterministic because output depends on batch size — a property known as batch invariance. When serving requests in production, batch size can fluctuate unpredictably due to system load, causing outputs to change even for identical requests.\n\n## The Solution\n\nTo ensure reproducible inference, kernels must be batch-invariant — the computation for each element should not depend on the batch size or position within the batch. The thinking-machines-lab/batch_invariant_ops code that accompanies this paper addresses this by providing a PyTorch implementation of invariant kernels and demonstrates them running Qwen3-8B deterministically under vLLM.\n\n## Broader Impact\n\nThe paper reframes LLM nondeterminism as an engineering bug (batch-sensitive kernels) rather than an inevitable hardware limitation, and provides a practical, open-source fix that achieves mathematically perfect reproducibility without sacrificing the benefits of batching."
    ],
    "durationSeconds": 7.614490578000004
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T18:16:39.802Z_

<details><summary>↩ Tool result · `toolu_018RE4ni3KKpdagKwwodBkxZ`</summary>

```text
Web search results for query: "arXiv 2506.09501 Yuan LayerCast authors full list NeurIPS 2025"

Links: [{"title":"[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/abs/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501"},{"title":"Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning","url":"https://arxiv.org/html/2506.09501v1"},{"title":"Performance of reasoning large language models on nephrology multiple-choice questions","url":"https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"},{"title":"Anchor-controlled generative adversarial network for high-fidelity electromagnetic and structurally diverse metasurface design","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12397733/"},{"title":"Layer-wise Instance Binding for Regional and Occlusion Control in Text-to-Image Diffusion Transformers","url":"https://arxiv.org/pdf/2603.05769"}]

Based on the search results, I found the paper arXiv 2506.09501. Here are the full author details:

The authors are: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, and Zirui Liu.

The paper is titled "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference" and was accepted to the 39th Conference on Neural Information Processing Systems (NeurIPS 2025). The paper develops a lightweight inference pipeline called LayerCast, which stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "f21a0ee3-ba1e-4afc-97c8-b4194002730a",
  "tool_use_result": {
    "query": "arXiv 2506.09501 Yuan LayerCast authors full list NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WA7n6tvxc5S4pmndr5k1PP",
        "content": [
          {
            "title": "[2506.09501] Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/abs/2506.09501"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of ...",
            "url": "https://arxiv.org/pdf/2506.09501"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/html/2506.09501"
          },
          {
            "title": "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning",
            "url": "https://arxiv.org/html/2506.09501v1"
          },
          {
            "title": "Performance of reasoning large language models on nephrology multiple-choice questions",
            "url": "https://www.medrxiv.org/content/10.64898/2025.12.03.25341427.full.pdf"
          },
          {
            "title": "Anchor-controlled generative adversarial network for high-fidelity electromagnetic and structurally diverse metasurface design",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12397733/"
          },
          {
            "title": "Layer-wise Instance Binding for Regional and Occlusion Control in Text-to-Image Diffusion Transformers",
            "url": "https://arxiv.org/pdf/2603.05769"
          }
        ]
      },
      "Based on the search results, I found the paper arXiv 2506.09501. Here are the full author details:\n\nThe authors are: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, and Zirui Liu.\n\nThe paper is titled \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\" and was accepted to the 39th Conference on Neural Information Processing Systems (NeurIPS 2025). The paper develops a lightweight inference pipeline called LayerCast, which stores weights in 16-bit precision but performs all computations in FP32, balancing memory efficiency with numerical stability."
    ],
    "durationSeconds": 8.050536996999996
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have:

1. **Yuan et al. 2025** - Verified. Authors: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, Zirui Liu. Venue: NeurIPS 2025 (oral). arXiv 2506.09501.

2. **Messina & Scotta 2026** - Verified. 

Authors: Alberto Messina, Stefano Scotta. arXiv 2604.22411. April 2026.

3. **ThinkingMachines 2025** - A blog post by Thinking Machines Lab (Horace He) from September 2025 at https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/, with supporting materials on ResearchGate.

I'm also tracking down some additional papers, including one by Shanmugavelu et al. from 2024 on floating-point nondeterminism impacts. I'm looking for more papers on infrastructure variance and determinism in LLM inference systems to round out the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "499ce431-5ab9-42a6-9bc1-e89020f7e75d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GneBW1R4Ap7PkrQLfubM7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2726,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 34280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1197
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

_source line 33_

Good progress. I need one more paper. Let me search for additional candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "43401a17-9d4a-4f48-83e3-9628ef57817e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GneBW1R4Ap7PkrQLfubM7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2726,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 34280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1197
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HyRgZwNMpC7LkGsi5PnYSZ`</summary>

```json
{
  "query": "arXiv 2408.05148 Shanmugavelu floating-point non-associativity SC24 venue DOI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "e1733925-c508-4fbb-bcf8-cc6f924824a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GneBW1R4Ap7PkrQLfubM7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2726,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 34280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1197
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RmyBVvzJKhhyUSr7NkxdwZ`</summary>

```json
{
  "query": "SGLang deterministic inference reproducible RL training LMSYS 2025 arXiv paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "c4c56d76-f202-4601-88fd-cf31765ca19e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GneBW1R4Ap7PkrQLfubM7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2726,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 34280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1197
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FhM8QCAjuhUovYKCBzBE3G`</summary>

```json
{
  "query": "vLLM nondeterminism reproducibility inference framework benchmark 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "264d997a-41e1-479e-a98e-f730f1e35383",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GneBW1R4Ap7PkrQLfubM7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2726,
      "cache_creation_input_tokens": 1197,
      "cache_read_input_tokens": 34280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1197
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

_source line 37 · 2026-05-21T18:17:03.297Z_

<details><summary>↩ Tool result · `toolu_01HyRgZwNMpC7LkGsi5PnYSZ`</summary>

```text
Web search results for query: "arXiv 2408.05148 Shanmugavelu floating-point non-associativity SC24 venue DOI"

Links: [{"title":"(PDF) Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://www.researchgate.net/publication/387848485_Impacts_of_floating-point_non-associativity_on_reproducibility_for_HPC_and_deep_learning_applications"},{"title":"[2408.05148] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications","url":"https://arxiv.org/abs/2408.05148"},{"title":"SC24 Proceedings","url":"https://sc24.supercomputing.org/proceedings/workshops/workshop_pages/ws_corr108.html"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | ORNL","url":"https://www.ornl.gov/publication/impacts-floating-point-non-associativity-reproducibility-hpc-and-deep-learning"},{"title":"au:Shanmugavelu_S in:cs - SciRate Search","url":"https://scirate.com/search?q=au:Shanmugavelu_S+in:cs"},{"title":"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis","url":"https://dl.acm.org/doi/10.1109/SCW63240.2024.00028"},{"title":"Presentation – SC24 Schedule","url":"https://sc24.conference-program.com/presentation/?id=ws_corr108&sess=sess759"},{"title":"Impacts of Floating-Point non-Associativity on ...","url":"https://conferences.computer.org/sc-wpub/pdfs/SC-W2024-6oZmigAQfgJ1GhPL0yE3pS/555400a170/555400a170.pdf"},{"title":"Impacts of floating-point non-associativity on reproducibility ...","url":"https://arxiv.org/pdf/2408.05148"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Paper Details

The paper is titled "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications" by Sanjif Shanmugavelu, Mathieu Taillefumier, Christopher Culver, Oscar Hernandez, Mark Coletti, and Ada Sedova.

## arXiv Information

The arXiv identifier is 2408.05148, and the paper addresses how run to run variability in parallel programs caused by floating-point non-associativity significantly affects reproducibility in iterative algorithms due to accumulating errors.

## SC24 Venue

The paper was presented at SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis. It was presented by the workshop session with authors from Groq Inc/Maxeler, Swiss National Supercomputing Centre (CSCS) at ETH Zürich, and Oak Ridge National Laboratory (ORNL).

## DOI

The DOI for the published proceedings paper is associated with SC-W '24: Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, with the specific DOI being **10.1109/SCW63240.2024.00028** based on the ACM Digital Library citation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "f6e793a8-d080-438c-945c-78597ad56c78",
  "tool_use_result": {
    "query": "arXiv 2408.05148 Shanmugavelu floating-point non-associativity SC24 venue DOI",
    "results": [
      {
        "tool_use_id": "srvtoolu_013VY7tbJZ34WkdCTaiyHBQR",
        "content": [
          {
            "title": "(PDF) Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications",
            "url": "https://www.researchgate.net/publication/387848485_Impacts_of_floating-point_non-associativity_on_reproducibility_for_HPC_and_deep_learning_applications"
          },
          {
            "title": "[2408.05148] Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications",
            "url": "https://arxiv.org/abs/2408.05148"
          },
          {
            "title": "SC24 Proceedings",
            "url": "https://sc24.supercomputing.org/proceedings/workshops/workshop_pages/ws_corr108.html"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | ORNL",
            "url": "https://www.ornl.gov/publication/impacts-floating-point-non-associativity-reproducibility-hpc-and-deep-learning"
          },
          {
            "title": "au:Shanmugavelu_S in:cs - SciRate Search",
            "url": "https://scirate.com/search?q=au:Shanmugavelu_S+in:cs"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications | Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis",
            "url": "https://dl.acm.org/doi/10.1109/SCW63240.2024.00028"
          },
          {
            "title": "Presentation – SC24 Schedule",
            "url": "https://sc24.conference-program.com/presentation/?id=ws_corr108&sess=sess759"
          },
          {
            "title": "Impacts of Floating-Point non-Associativity on ...",
            "url": "https://conferences.computer.org/sc-wpub/pdfs/SC-W2024-6oZmigAQfgJ1GhPL0yE3pS/555400a170/555400a170.pdf"
          },
          {
            "title": "Impacts of floating-point non-associativity on reproducibility ...",
            "url": "https://arxiv.org/pdf/2408.05148"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the paper you're looking for:\n\n## Paper Details\n\nThe paper is titled \"Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications\" by Sanjif Shanmugavelu, Mathieu Taillefumier, Christopher Culver, Oscar Hernandez, Mark Coletti, and Ada Sedova.\n\n## arXiv Information\n\nThe arXiv identifier is 2408.05148, and the paper addresses how run to run variability in parallel programs caused by floating-point non-associativity significantly affects reproducibility in iterative algorithms due to accumulating errors.\n\n## SC24 Venue\n\nThe paper was presented at SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis. It was presented by the workshop session with authors from Groq Inc/Maxeler, Swiss National Supercomputing Centre (CSCS) at ETH Zürich, and Oak Ridge National Laboratory (ORNL).\n\n## DOI\n\nThe DOI for the published proceedings paper is associated with SC-W '24: Proceedings of the SC '24 Workshops of the International Conference on High Performance Computing, Network, Storage, and Analysis, with the specific DOI being **10.1109/SCW63240.2024.00028** based on the ACM Digital Library citation."
    ],
    "durationSeconds": 5.876541750999997
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T18:17:05.277Z_

<details><summary>↩ Tool result · `toolu_01RmyBVvzJKhhyUSr7NkxdwZ`</summary>

```text
Web search results for query: "SGLang deterministic inference reproducible RL training LMSYS 2025 arXiv paper"

Links: [{"title":"Towards Deterministic Inference in SGLang and Reproducible RL Training - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-09-22-sglang-deterministic/"},{"title":"LMSYS Org on X: \"SGLang now supports deterministic LLM inference! Building on @thinkymachines batch-invariant kernels, we integrated deterministic attention &amp; sampling ops into a high-throughput engine - fully compatible with chunked prefill, CUDA graphs, radix cache, and non-greedy sampling. ✅ https://t.co/drH8Z0eKag\" / X","url":"https://x.com/lmsysorg/status/1970240927429206161"},{"title":"Deterministic Inference — SGLang","url":"https://sgl-project.github.io/advanced_features/deterministic_inference.html"},{"title":"sglang/docs/advanced_features/deterministic_inference.md at main · sgl-project/sglang","url":"https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/deterministic_inference.md"},{"title":"GitHub - aerlabsAI/ai-inference-resources: Curated collection of AI inference engineering resources — LLM serving, GPU kernels, quantization, distributed inference, and production deployment. Compiled from the AER Labs community.","url":"https://github.com/aerlabsAI/ai-inference-resources"},{"title":"DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2026-04-25-deepseek-v4/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/pdf/2511.17826"},{"title":"LLM-42: Enabling Determinism in LLM Inference with Verified Speculation","url":"https://arxiv.org/html/2601.17768v1"},{"title":"Mini-SGLang: Efficient Inference Engine in a Nutshell - LMSYS Blog | LMSYS Org","url":"https://www.lmsys.org/blog/2025-12-17-minisgl/"}]

Based on my web search, I found relevant information about SGLang's deterministic inference and reproducible RL training work from LMSYS:

## Key Findings

SGLang achieves fully deterministic inference while maintaining compatibility with chunked prefill, CUDA graphs, radix cache, and non-greedy sampling, building on Thinking Machines Lab's batch-invariant operators.

### Problem Addressed

Even with temperature set to 0 in SGLang, sampling is not deterministic due to the use of dynamic batching and radix cache. Different batch sizes cause GPU kernels to split reduction operations differently, leading to different addition orders, and due to floating-point non-associativity, this produces different results even for identical inputs.

### Technical Implementation

SGLang supports deterministic inference even with non-greedy sampling by using sampling seeds, which is particularly useful for reinforcement learning scenarios like GRPO (Group Relative Policy Optimization) where multiple diverse but reproducible responses are needed.

### Performance and Results

With CUDA graphs, SGLang delivers 2.8x acceleration and reduces performance overhead to just 34.35% (compared to TML's 61.5%). Validation experiments on Qwen3-8B demonstrate perfect reproducibility: two independent training runs produce identical curves.

The LMSYS blog post on this topic was published on September 22, 2025. However, I did not find a specific arXiv paper with that exact title in the search results—the work appears to be primarily documented in the LMSYS blog post and related technical documentation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "05771ee6-c7e7-4f0a-b810-e1f52905000e",
  "tool_use_result": {
    "query": "SGLang deterministic inference reproducible RL training LMSYS 2025 arXiv paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_011gKwbdUW8qNArfks16bP5G",
        "content": [
          {
            "title": "Towards Deterministic Inference in SGLang and Reproducible RL Training - LMSYS Blog | LMSYS Org",
            "url": "https://www.lmsys.org/blog/2025-09-22-sglang-deterministic/"
          },
          {
            "title": "LMSYS Org on X: \"SGLang now supports deterministic LLM inference! Building on @thinkymachines batch-invariant kernels, we integrated deterministic attention &amp; sampling ops into a high-throughput engine - fully compatible with chunked prefill, CUDA graphs, radix cache, and non-greedy sampling. ✅ https://t.co/drH8Z0eKag\" / X",
            "url": "https://x.com/lmsysorg/status/1970240927429206161"
          },
          {
            "title": "Deterministic Inference — SGLang",
            "url": "https://sgl-project.github.io/advanced_features/deterministic_inference.html"
          },
          {
            "title": "sglang/docs/advanced_features/deterministic_inference.md at main · sgl-project/sglang",
            "url": "https://github.com/sgl-project/sglang/blob/main/docs/advanced_features/deterministic_inference.md"
          },
          {
            "title": "GitHub - aerlabsAI/ai-inference-resources: Curated collection of AI inference engineering resources — LLM serving, GPU kernels, quantization, distributed inference, and production deployment. Compiled from the AER Labs community.",
            "url": "https://github.com/aerlabsAI/ai-inference-resources"
          },
          {
            "title": "DeepSeek-V4 on Day 0: From Fast Inference to Verified RL with SGLang and Miles - LMSYS Blog | LMSYS Org",
            "url": "https://www.lmsys.org/blog/2026-04-25-deepseek-v4/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com",
            "url": "https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"
          },
          {
            "title": "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch",
            "url": "https://arxiv.org/pdf/2511.17826"
          },
          {
            "title": "LLM-42: Enabling Determinism in LLM Inference with Verified Speculation",
            "url": "https://arxiv.org/html/2601.17768v1"
          },
          {
            "title": "Mini-SGLang: Efficient Inference Engine in a Nutshell - LMSYS Blog | LMSYS Org",
            "url": "https://www.lmsys.org/blog/2025-12-17-minisgl/"
          }
        ]
      },
      "Based on my web search, I found relevant information about SGLang's deterministic inference and reproducible RL training work from LMSYS:\n\n## Key Findings\n\nSGLang achieves fully deterministic inference while maintaining compatibility with chunked prefill, CUDA graphs, radix cache, and non-greedy sampling, building on Thinking Machines Lab's batch-invariant operators.\n\n### Problem Addressed\n\nEven with temperature set to 0 in SGLang, sampling is not deterministic due to the use of dynamic batching and radix cache. Different batch sizes cause GPU kernels to split reduction operations differently, leading to different addition orders, and due to floating-point non-associativity, this produces different results even for identical inputs.\n\n### Technical Implementation\n\nSGLang supports deterministic inference even with non-greedy sampling by using sampling seeds, which is particularly useful for reinforcement learning scenarios like GRPO (Group Relative Policy Optimization) where multiple diverse but reproducible responses are needed.\n\n### Performance and Results\n\nWith CUDA graphs, SGLang delivers 2.8x acceleration and reduces performance overhead to just 34.35% (compared to TML's 61.5%). Validation experiments on Qwen3-8B demonstrate perfect reproducibility: two independent training runs produce identical curves.\n\nThe LMSYS blog post on this topic was published on September 22, 2025. However, I did not find a specific arXiv paper with that exact title in the search results—the work appears to be primarily documented in the LMSYS blog post and related technical documentation."
    ],
    "durationSeconds": 7.343521798999995
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-21T18:17:07.981Z_

<details><summary>↩ Tool result · `toolu_01FhM8QCAjuhUovYKCBzBE3G`</summary>

```text
Web search results for query: "vLLM nondeterminism reproducibility inference framework benchmark 2024 2025 arXiv"

Links: [{"title":"Understanding and Mitigating Numerical Sources of ...","url":"https://arxiv.org/pdf/2506.09501"},{"title":"Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning","url":"https://arxiv.org/html/2506.09501v1"},{"title":"GitHub - nanomaoli/llm_reproducibility · GitHub","url":"https://github.com/nanomaoli/llm_reproducibility"},{"title":"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference","url":"https://arxiv.org/html/2506.09501v2"},{"title":"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/pdf/2511.17826"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.17826v1"},{"title":"Quantifying non‑deterministic drift in large language models","url":"https://arxiv.org/html/2601.19934v1"},{"title":"DiFR: Inference Verification Despite Nondeterminism","url":"https://arxiv.org/html/2511.20621"}]

Based on the web search results, I found several recent arXiv papers addressing vLLM nondeterminism, reproducibility, and inference frameworks in 2024-2025:

## Key Papers Found:

**1. "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning" (2025)**
This paper by Jiayi Yuan et al. (arXiv:2506.09501) addresses challenges and solutions for reproducible reasoning. The authors primarily use vLLM as the inference backend and conduct experiments on four recent LLMs across five commonly used LLM evaluation benchmarks including AIME'24, MATH500, and LiveCodeBench. They propose LayerCast, an optimized FP32 inference pipeline that performs computations in FP32 while retaining model weights in BF16 precision, balancing memory efficiency and reproducibility, released as a patch to vLLM.

**2. "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch" (2025)**
A new paper on arXiv proposes TBIK (Tree Based Invariant Kernels), which enables deterministic inference across TP sizes. The experiments confirm zero probability divergence and bit-wise reproducibility for deterministic inference across different TP sizes, achieving bit-wise identical results between vLLM and FSDP in RL training pipelines.

**3. "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference" (2025)**
This NeurIPS 2025 Oral paper addresses numerical sources of nondeterminism in LLM inference.

**4. "DiFR: Inference Verification Despite Nondeterminism" (2025)**
This paper uses vLLM with various quantization configurations (bf16 baseline, fp8-quantized, fp8 KV-cache quantized, and 4-bit-quantized) to evaluate inference consistency across different model configurations.

These papers collectively address nondeterminism issues in vLLM and propose various solutions for achieving reproducible inference across different hardware configurations and parallelization strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "3eaa0e98-50cb-4134-b81a-e9a2fd215dff",
  "tool_use_result": {
    "query": "vLLM nondeterminism reproducibility inference framework benchmark 2024 2025 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PX9TVY82z6tBDzYMfDhGGy",
        "content": [
          {
            "title": "Understanding and Mitigating Numerical Sources of ...",
            "url": "https://arxiv.org/pdf/2506.09501"
          },
          {
            "title": "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning",
            "url": "https://arxiv.org/html/2506.09501v1"
          },
          {
            "title": "GitHub - nanomaoli/llm_reproducibility · GitHub",
            "url": "https://github.com/nanomaoli/llm_reproducibility"
          },
          {
            "title": "Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference",
            "url": "https://arxiv.org/html/2506.09501v2"
          },
          {
            "title": "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch",
            "url": "https://arxiv.org/pdf/2511.17826"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.17826v1"
          },
          {
            "title": "Quantifying non‑deterministic drift in large language models",
            "url": "https://arxiv.org/html/2601.19934v1"
          },
          {
            "title": "DiFR: Inference Verification Despite Nondeterminism",
            "url": "https://arxiv.org/html/2511.20621"
          }
        ]
      },
      "Based on the web search results, I found several recent arXiv papers addressing vLLM nondeterminism, reproducibility, and inference frameworks in 2024-2025:\n\n## Key Papers Found:\n\n**1. \"Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning\" (2025)**\nThis paper by Jiayi Yuan et al. (arXiv:2506.09501) addresses challenges and solutions for reproducible reasoning. The authors primarily use vLLM as the inference backend and conduct experiments on four recent LLMs across five commonly used LLM evaluation benchmarks including AIME'24, MATH500, and LiveCodeBench. They propose LayerCast, an optimized FP32 inference pipeline that performs computations in FP32 while retaining model weights in BF16 precision, balancing memory efficiency and reproducibility, released as a patch to vLLM.\n\n**2. \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\" (2025)**\nA new paper on arXiv proposes TBIK (Tree Based Invariant Kernels), which enables deterministic inference across TP sizes. The experiments confirm zero probability divergence and bit-wise reproducibility for deterministic inference across different TP sizes, achieving bit-wise identical results between vLLM and FSDP in RL training pipelines.\n\n**3. \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\" (2025)**\nThis NeurIPS 2025 Oral paper addresses numerical sources of nondeterminism in LLM inference.\n\n**4. \"DiFR: Inference Verification Despite Nondeterminism\" (2025)**\nThis paper uses vLLM with various quantization configurations (bf16 baseline, fp8-quantized, fp8 KV-cache quantized, and 4-bit-quantized) to evaluate inference consistency across different model configurations.\n\nThese papers collectively address nondeterminism issues in vLLM and propose various solutions for achieving reproducible inference across different hardware configurations and parallelization strategies."
    ],
    "durationSeconds": 9.053598872999995
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
I now have enough information. Let me look at two more candidate papers for the additional 2:

1. **Shanmugavelu et al. 2024** - "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications" - SC'24 Workshop. DOI: 10.1109/SCW63240.2024.00028. Very relevant as foundational theory for infrastructure variance.

2. For the second new paper, I have several candidates:
   - "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch" (arXiv 2511.17826) - TBIK paper
   - "Quantifying non-deterministic drift in large language models" (arXiv 2601.19934)
   - "DiFR: Inference Verification Despite Nondeterminism" (arXiv 2511.20621)

I'm comparing the TBIK paper on deterministic inference with the one on quantifying non-deterministic drift to see which better complements the existing selection.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "e987811d-c0ed-489a-908c-760ad59555cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzZXUhKNWT6cNpfDD3sMRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 35477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6376
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

Let me get details on two strong candidates for the 5th paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "e929849c-05ef-4e7c-b98f-d76f48efbb8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzZXUhKNWT6cNpfDD3sMRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 35477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6376
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NFP7waZ7ETayDz3D7muxLJ`</summary>

```json
{
  "query": "\"Deterministic Inference across Tensor Parallel Sizes\" TBIK arXiv 2511.17826 authors venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "d9ba808b-546d-4dfb-9d41-d005029e0611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzZXUhKNWT6cNpfDD3sMRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 35477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6376
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QFdofnxvY9p36x93irFctf`</summary>

```json
{
  "query": "\"Quantifying non-deterministic drift in large language models\" arXiv 2601.19934 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "ddcd64b6-78a8-4758-bff5-d617be0fcfa5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XzZXUhKNWT6cNpfDD3sMRB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6376,
      "cache_read_input_tokens": 35477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6376
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

_source line 44 · 2026-05-21T18:17:28.170Z_

<details><summary>↩ Tool result · `toolu_01QFdofnxvY9p36x93irFctf`</summary>

```text
Web search results for query: ""Quantifying non-deterministic drift in large language models" arXiv 2601.19934 authors"

Links: [{"title":"[2601.19934] Quantifying non deterministic drift in large language models","url":"https://arxiv.org/abs/2601.19934"},{"title":"Quantifying non deterministic drift in large language models","url":"https://arxiv.org/pdf/2601.19934"},{"title":"Quantifying non‑deterministic drift in large language models","url":"https://arxiv.org/html/2601.19934v1"},{"title":"Quantifying Non‑Deterministic Drift in Large Language Models","url":"https://ubos.tech/quantifying-non%E2%80%91deterministic-drift-in-large-language-models-research-summary/"},{"title":"Entropy-Based Measurement of Value Drift and Alignment Work in Large Language Models","url":"https://arxiv.org/pdf/2512.03047"},{"title":"Non-Determinism of \"Deterministic\" LLM Settings","url":"https://arxiv.org/pdf/2408.04667"},{"title":"Benchmarking Large Language Model Volatility","url":"https://arxiv.org/pdf/2311.15180"},{"title":"LLM Output Drift: Cross-Provider Validation & Mitigation for Financial Workflows","url":"https://arxiv.org/pdf/2511.07585"}]

Based on the search results, I found the paper you're looking for:

**Title:** Quantifying non deterministic drift in large language models

**ArXiv ID:** 2601.19934

**Author:** Claire Nicholson

**Submitted:** January 12, 2026

**Summary:** The paper conducts repeated-run experiments to empirically quantify baseline behavioural drift, evaluating two publicly accessible models, gpt-4o-mini and llama3.1-8b, across five prompt categories using exact repeats, perturbed inputs, and reuse modes at temperatures of 0.0 and 0.7. The results show that nondeterminism persists even at temperature 0.0, with distinct variability patterns by model size, deployment, and prompt type.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "03e37b74-ea76-4a28-a6b2-778fc2fc8dd6",
  "tool_use_result": {
    "query": "\"Quantifying non-deterministic drift in large language models\" arXiv 2601.19934 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_017EoBKHpdbz5zBQe9YpXozS",
        "content": [
          {
            "title": "[2601.19934] Quantifying non deterministic drift in large language models",
            "url": "https://arxiv.org/abs/2601.19934"
          },
          {
            "title": "Quantifying non deterministic drift in large language models",
            "url": "https://arxiv.org/pdf/2601.19934"
          },
          {
            "title": "Quantifying non‑deterministic drift in large language models",
            "url": "https://arxiv.org/html/2601.19934v1"
          },
          {
            "title": "Quantifying Non‑Deterministic Drift in Large Language Models",
            "url": "https://ubos.tech/quantifying-non%E2%80%91deterministic-drift-in-large-language-models-research-summary/"
          },
          {
            "title": "Entropy-Based Measurement of Value Drift and Alignment Work in Large Language Models",
            "url": "https://arxiv.org/pdf/2512.03047"
          },
          {
            "title": "Non-Determinism of \"Deterministic\" LLM Settings",
            "url": "https://arxiv.org/pdf/2408.04667"
          },
          {
            "title": "Benchmarking Large Language Model Volatility",
            "url": "https://arxiv.org/pdf/2311.15180"
          },
          {
            "title": "LLM Output Drift: Cross-Provider Validation & Mitigation for Financial Workflows",
            "url": "https://arxiv.org/pdf/2511.07585"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Quantifying non deterministic drift in large language models\n\n**ArXiv ID:** 2601.19934\n\n**Author:** Claire Nicholson\n\n**Submitted:** January 12, 2026\n\n**Summary:** The paper conducts repeated-run experiments to empirically quantify baseline behavioural drift, evaluating two publicly accessible models, gpt-4o-mini and llama3.1-8b, across five prompt categories using exact repeats, perturbed inputs, and reuse modes at temperatures of 0.0 and 0.7. The results show that nondeterminism persists even at temperature 0.0, with distinct variability patterns by model size, deployment, and prompt type."
    ],
    "durationSeconds": 5.615771648999988
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T18:17:29.010Z_

<details><summary>↩ Tool result · `toolu_01NFP7waZ7ETayDz3D7muxLJ`</summary>

```text
Web search results for query: ""Deterministic Inference across Tensor Parallel Sizes" TBIK arXiv 2511.17826 authors venue"

Links: [{"title":"[2511.17826] Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/abs/2511.17826"},{"title":"Deterministic Inference across Tensor Parallel Sizes That ...","url":"https://arxiv.org/pdf/2511.17826"},{"title":"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch | Request PDF","url":"https://www.researchgate.net/publication/397932505_Deterministic_Inference_across_Tensor_Parallel_Sizes_That_Eliminates_Training-Inference_Mismatch"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.17826"},{"title":"Tensor Parallel LLM Inferencing. As models increase in size, it becomes… | by Sneha Ghantasala | Thomson Reuters Labs | Medium","url":"https://medium.com/tr-labs-ml-engineering-blog/tensor-parallel-llm-inferencing-09138daf0ba7"},{"title":"Flash Communication: Reducing Tensor Parallelization Bottleneck for Fast   Large Language Model Inference","url":"https://arxiv.org/pdf/2412.04964"},{"title":"TPI-LLM: Serving 70B-scale LLMs Efficiently on Low-resource Edge Devices","url":"https://arxiv.org/pdf/2410.00531"}]

Based on the search results, here is the information about the paper:

**Title:** Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch

**ArXiv ID:** 2511.17826

**Authors:** Ziyang Zhang and 6 other authors. Additional author names visible in the search results include Xinheng Ding, Jiayi Yuan, and Rixin Liu.

**Main Contribution:** The paper proposes Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size.

**Venue:** The paper appears to be a preprint submitted to arXiv (cs.LG category - Computer Science: Machine Learning) on November 21, 2025. It is a preprint and early-stage research that may not have been peer reviewed yet.

**Implementation:** The kernels were implemented in Triton and integrated into vLLM and FSDP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "0cfb9130-cdba-4266-b7de-42b41e9cbde7",
  "tool_use_result": {
    "query": "\"Deterministic Inference across Tensor Parallel Sizes\" TBIK arXiv 2511.17826 authors venue",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CEZnpSUJLvnnpZxdL134vJ",
        "content": [
          {
            "title": "[2511.17826] Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch",
            "url": "https://arxiv.org/abs/2511.17826"
          },
          {
            "title": "Deterministic Inference across Tensor Parallel Sizes That ...",
            "url": "https://arxiv.org/pdf/2511.17826"
          },
          {
            "title": "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch | Request PDF",
            "url": "https://www.researchgate.net/publication/397932505_Deterministic_Inference_across_Tensor_Parallel_Sizes_That_Eliminates_Training-Inference_Mismatch"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2511.17826"
          },
          {
            "title": "Tensor Parallel LLM Inferencing. As models increase in size, it becomes… | by Sneha Ghantasala | Thomson Reuters Labs | Medium",
            "url": "https://medium.com/tr-labs-ml-engineering-blog/tensor-parallel-llm-inferencing-09138daf0ba7"
          },
          {
            "title": "Flash Communication: Reducing Tensor Parallelization Bottleneck for Fast   Large Language Model Inference",
            "url": "https://arxiv.org/pdf/2412.04964"
          },
          {
            "title": "TPI-LLM: Serving 70B-scale LLMs Efficiently on Low-resource Edge Devices",
            "url": "https://arxiv.org/pdf/2410.00531"
          }
        ]
      },
      "Based on the search results, here is the information about the paper:\n\n**Title:** Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\n\n**ArXiv ID:** 2511.17826\n\n**Authors:** Ziyang Zhang and 6 other authors. Additional author names visible in the search results include Xinheng Ding, Jiayi Yuan, and Rixin Liu.\n\n**Main Contribution:** The paper proposes Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size.\n\n**Venue:** The paper appears to be a preprint submitted to arXiv (cs.LG category - Computer Science: Machine Learning) on November 21, 2025. It is a preprint and early-stage research that may not have been peer reviewed yet.\n\n**Implementation:** The kernels were implemented in Triton and integrated into vLLM and FSDP."
    ],
    "durationSeconds": 6.543408150000003
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Let me get the full author lists for the TBIK paper. Let me also check the Shanmugavelu paper more carefully.

Now let me decide which 2 papers to add:

1. **Shanmugavelu et al. 2024** - "Impacts of floating-point non-associativity on reproducibility for HPC and deep learning applications" - SC'24 Workshop. Very relevant as it provides the theoretical foundation for why floating-point non-associativity causes nondeterminism in deep learning.

2. For the second paper, I have:
   - **Zhang et al. 2025** (TBIK) - "Deterministic Inference across Tensor Parallel Sizes..." - arXiv 2511.17826. This is about TP-invariant kernels for deterministic inference.
   - **Nicholson 2026** - "Quantifying non-deterministic drift in large language models" - arXiv 2601.19934. Empirical study of nondeterminism persistence.

The TBIK paper seems like the stronger choice since it directly addresses deterministic inference across different tensor parallelism configurations, which is more aligned with infrastructure variance concerns. The Nicholson paper covers similar ground but takes a more empirical approach to measuring nondeterminism drift.

I'm leaning toward pairing Shanmugavelu et al. 2024 on floating-point non-associativity with the TBIK paper, since one provides the foundational theory and the other applies it specifically to LLM inference. Though I should verify the author overlap between TBIK and the Yuan/LayerCast work to make sure I'm not double-citing the same group.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "8367eb81-a307-467d-9152-90dcf60b2f48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5ofTXhMXnAVDSPiWdpgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 578,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 41853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1205
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

Let me get the full author lists for these papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2b5a4d0b-0c36-4341-bd1a-9d985cc943b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5ofTXhMXnAVDSPiWdpgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 578,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 41853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1205
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JXRHQHGPjuViPh1XW1pNW9`</summary>

```json
{
  "query": "arXiv 2511.17826 \"Ziyang Zhang\" TBIK full author list deterministic inference tensor parallel"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "ba839ae4-0cda-46dc-a8ec-4e7404503e60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5ofTXhMXnAVDSPiWdpgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 578,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 41853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1205
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MzN6LKWJwnUm2c4eGdJkRW`</summary>

```json
{
  "query": "Thinking Machines Lab \"Horace He\" \"defeating nondeterminism\" paper ResearchGate authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "421fcfdc-fbdf-4d6a-828e-49b98592dd93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017d5ofTXhMXnAVDSPiWdpgP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 578,
      "cache_creation_input_tokens": 1205,
      "cache_read_input_tokens": 41853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1205
      },
      "output_tokens": 10,
      "service_tier": "standard",
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

_source line 50 · 2026-05-21T18:17:46.847Z_

<details><summary>↩ Tool result · `toolu_01JXRHQHGPjuViPh1XW1pNW9`</summary>

```text
Web search results for query: "arXiv 2511.17826 "Ziyang Zhang" TBIK full author list deterministic inference tensor parallel"

Links: [{"title":"[2511.17826] Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch","url":"https://arxiv.org/abs/2511.17826"},{"title":"System and methods for upsampling of decompressed genomic data after lossy compression using a neural network","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12417386"},{"title":"Identification of bioactive constituents for colitis from traditional Chinese medicine prescription via deep neural network","url":"https://www.biorxiv.org/content/10.1101/2023.05.31.542690.full.pdf"},{"title":"Scintillator ageing of the T2K near detectors from 2010 to 2021","url":"https://arxiv.org/pdf/2207.12982"},{"title":"Testing T2K's Bayesian constraints with priors in alternate parameterisations","url":"https://arxiv.org/pdf/2507.02101"}]

Perfect! I found the arXiv paper. According to the search results, the paper "Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch" is by Ziyang Zhang and 6 other authors.

However, the search results only mention that there are 6 additional authors beyond Ziyang Zhang, but don't provide the complete list of all author names. To get the full author list, you would need to visit the arXiv page directly at https://arxiv.org/abs/2511.17826 or view the PDF.

The paper's main contribution is proposing Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size, which addresses the issue of non-deterministic behavior in LLM serving frameworks where identical inputs can yield different outputs when system configurations vary.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "a774b946-4f69-4714-8fa9-c286cc112f5e",
  "tool_use_result": {
    "query": "arXiv 2511.17826 \"Ziyang Zhang\" TBIK full author list deterministic inference tensor parallel",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Tq581vB3XjnfeovRc89i95",
        "content": [
          {
            "title": "[2511.17826] Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch",
            "url": "https://arxiv.org/abs/2511.17826"
          },
          {
            "title": "System and methods for upsampling of decompressed genomic data after lossy compression using a neural network",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12417386"
          },
          {
            "title": "Identification of bioactive constituents for colitis from traditional Chinese medicine prescription via deep neural network",
            "url": "https://www.biorxiv.org/content/10.1101/2023.05.31.542690.full.pdf"
          },
          {
            "title": "Scintillator ageing of the T2K near detectors from 2010 to 2021",
            "url": "https://arxiv.org/pdf/2207.12982"
          },
          {
            "title": "Testing T2K's Bayesian constraints with priors in alternate parameterisations",
            "url": "https://arxiv.org/pdf/2507.02101"
          }
        ]
      },
      "Perfect! I found the arXiv paper. According to the search results, the paper \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\" is by Ziyang Zhang and 6 other authors.\n\nHowever, the search results only mention that there are 6 additional authors beyond Ziyang Zhang, but don't provide the complete list of all author names. To get the full author list, you would need to visit the arXiv page directly at https://arxiv.org/abs/2511.17826 or view the PDF.\n\nThe paper's main contribution is proposing Tree-Based Invariant Kernels (TBIK), a set of TP-invariant matrix multiplication and reduction primitives that guarantee bit-wise identical results regardless of TP size, which addresses the issue of non-deterministic behavior in LLM serving frameworks where identical inputs can yield different outputs when system configurations vary."
    ],
    "durationSeconds": 5.431862156999996
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T18:17:46.912Z_

<details><summary>↩ Tool result · `toolu_01MzN6LKWJwnUm2c4eGdJkRW`</summary>

```text
Web search results for query: "Thinking Machines Lab "Horace He" "defeating nondeterminism" paper ResearchGate authors full list"

Links: [{"title":"Connectionism - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/"},{"title":"Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com","url":"https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"},{"title":"Mira Murati’s New AI Lab Wants to Fix a Hidden Problem in LLMs | by Luna | Machine Learning Reviews | Medium","url":"https://medium.com/lunas-orbit/mira-muratis-new-ai-lab-wants-to-fix-a-hidden-problem-in-llms-6ab72dffd6fe"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab","url":"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"},{"title":"Thinking Machines Lab wants to make AI models more consistent | TechCrunch","url":"https://techcrunch.com/2025/09/10/thinking-machines-lab-wants-to-make-ai-models-more-consistent/"},{"title":"Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury","url":"https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"},{"title":"Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium","url":"https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"},{"title":"Inside Thinking Machines Lab: Murati’s $12 billion AI startup tackles reproducibility","url":"https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/"}]

Based on the search results, I found information about the "Defeating Nondeterminism in LLM Inference" paper by Horace He in collaboration with others at Thinking Machines Lab, published September 10, 2025.

However, the search results show this is a **blog post** published on the Thinking Machines Lab research blog "Connectionism," not a ResearchGate paper. The sources consistently refer to it as a technical blog post rather than a formal research paper with a full author list on ResearchGate.

The author is Horace He, a respected systems and kernels engineer known for deep dives on PyTorch numerics and performance, though he collaborated with others at Thinking Machines Lab. However, the search results don't provide the full list of collaborators' names.

If you're looking for the complete author list, I'd recommend checking the official blog post directly at thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ or looking for any formal paper publication that may have been released, as the search results indicate this was primarily published as a blog post rather than as an academic paper on ResearchGate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "aada5c00-5005-48a0-8ec3-78fe53ecbd23",
  "tool_use_result": {
    "query": "Thinking Machines Lab \"Horace He\" \"defeating nondeterminism\" paper ResearchGate authors full list",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QALt3oubeFkcd2rRuJ5HpT",
        "content": [
          {
            "title": "Connectionism - Thinking Machines Lab",
            "url": "https://thinkingmachines.ai/blog/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference by Thinking Machines | NextBigFuture.com",
            "url": "https://www.nextbigfuture.com/2025/11/defeating-nondeterminism-in-llm-inference-by-thinking-machines.html"
          },
          {
            "title": "Mira Murati’s New AI Lab Wants to Fix a Hidden Problem in LLMs | by Luna | Machine Learning Reviews | Medium",
            "url": "https://medium.com/lunas-orbit/mira-muratis-new-ai-lab-wants-to-fix-a-hidden-problem-in-llms-6ab72dffd6fe"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab",
            "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"
          },
          {
            "title": "Thinking Machines Lab wants to make AI models more consistent | TechCrunch",
            "url": "https://techcrunch.com/2025/09/10/thinking-machines-lab-wants-to-make-ai-models-more-consistent/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference - Thinking Machines Lab - Michael Bargury",
            "url": "https://www.mbgsec.com/weblog/2025-09-11-defeating-nondeterminism-in-llm-inference-thinking-machines-lab/"
          },
          {
            "title": "Defeating Nondeterminism in LLM Inference — Thinking Machines | by Sulbha Jain | Medium",
            "url": "https://medium.com/@sulbha.jindal/defeating-nondeterminism-in-llm-inference-thinking-machines-2339599e4156"
          },
          {
            "title": "Inside Thinking Machines Lab: Murati’s $12 billion AI startup tackles reproducibility",
            "url": "https://americanbazaaronline.com/2025/09/11/inside-thinking-machines-lab-muratis-12-billion-ai-startup-tackles-reproducibility-467536/"
          }
        ]
      },
      "Based on the search results, I found information about the \"Defeating Nondeterminism in LLM Inference\" paper by Horace He in collaboration with others at Thinking Machines Lab, published September 10, 2025.\n\nHowever, the search results show this is a **blog post** published on the Thinking Machines Lab research blog \"Connectionism,\" not a ResearchGate paper. The sources consistently refer to it as a technical blog post rather than a formal research paper with a full author list on ResearchGate.\n\nThe author is Horace He, a respected systems and kernels engineer known for deep dives on PyTorch numerics and performance, though he collaborated with others at Thinking Machines Lab. However, the search results don't provide the full list of collaborators' names.\n\nIf you're looking for the complete author list, I'd recommend checking the official blog post directly at thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ or looking for any formal paper publication that may have been released, as the search results indicate this was primarily published as a blog post rather than as an academic paper on ResearchGate."
    ],
    "durationSeconds": 5.182458117000002
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
OK let me now gather the remaining details I need. For the ThinkingMachines paper, the author is Horace He, and it's a blog post at thinkingmachines.ai. The ResearchGate entry earlier seemed to have a PDF version with the full title "BATCH INVARIANCE, SEED LOCKING, AND BEYOND: COUNTERING NONDETERMINISM IN LLM INFERENCE", so there may be a technical report version too.

Let me also try to get the full author list for the TBIK paper (arXiv 2511.17826).

Actually, let me use WebFetch to get the arXiv page directly.


I need to refine my search approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "b14a41a8-fc58-4076-a581-07f491a95494",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LJp2sudhTiXMBN4udSNrL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 43058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2620
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

_source line 53_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TRpvWfCozZLqmmX6ve6YVk`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "665f770f-757b-49da-9565-93897aaa8d9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017LJp2sudhTiXMBN4udSNrL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 43058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2620
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

_source line 54 · 2026-05-21T18:17:54.539Z_

<details><summary>↩ Tool result · `toolu_01TRpvWfCozZLqmmX6ve6YVk`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "6b5998e9-928a-4810-9ee4-fc65ad5eb628",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GEU8864yFUBm4Eva8murNj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.17826",
  "prompt": "Extract the complete list of all authors and the submission date for this paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2c5f4312-3cce-423e-b244-4f0b2217f53c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EbSfcK8CSP4LGk43gZMiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 45678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 770
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

_source line 56_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CkcNXBwDBxq6GvX1XN1rtY`</summary>

```json
{
  "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/",
  "prompt": "Extract the author name(s), publication date, and any formal citation information (e.g. technical report number, DOI) for this blog post."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "3de4ef53-09d2-4641-aebf-67e40fd765cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EbSfcK8CSP4LGk43gZMiH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 770,
      "cache_read_input_tokens": 45678,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 770
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

_source line 57 · 2026-05-21T18:18:01.301Z_

<details><summary>↩ Tool result · `toolu_01GEU8864yFUBm4Eva8murNj`</summary>

```text
# Paper Authors and Submission Date

**Authors:**
1. Ziyang Zhang
2. Xinheng Ding
3. Jiayi Yuan
4. Rixin Liu
5. Huizi Mao
6. Jiarong Xing
7. Zirui Liu

**Submission Date:** November 21, 2025

The paper was "Submitted on 21 Nov 2025" according to the arXiv metadata displayed on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2df52d91-c7b0-4fa6-88b1-ead0d047f2be",
  "tool_use_result": {
    "bytes": 49532,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Authors and Submission Date\n\n**Authors:**\n1. Ziyang Zhang\n2. Xinheng Ding\n3. Jiayi Yuan\n4. Rixin Liu\n5. Huizi Mao\n6. Jiarong Xing\n7. Zirui Liu\n\n**Submission Date:** November 21, 2025\n\nThe paper was \"Submitted on 21 Nov 2025\" according to the arXiv metadata displayed on the page.",
    "durationMs": 2788,
    "url": "https://arxiv.org/abs/2511.17826"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T18:18:02.517Z_

<details><summary>↩ Tool result · `toolu_01CkcNXBwDBxq6GvX1XN1rtY`</summary>

````text
# Citation Information for "Defeating Nondeterminism in LLM Inference"

**Author(s):** Horace He in collaboration with others at Thinking Machines Lab

**Publication Date:** September 10, 2025

**Formal Citation Information:**

The post provides its own suggested citations:

Chicago-style format: "He, Horace and Thinking Machines Lab, 'Defeating Nondeterminism in LLM Inference', Thinking Machines Lab: Connectionism, Sep 2025."

BibTeX format:
```
@article{he2025nondeterminism,
  author = {Horace He and Thinking Machines Lab},
  title = {Defeating Nondeterminism in LLM Inference},
  journal = {Thinking Machines Lab: Connectionism},
  year = {2025},
  note = {https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/},
  doi = {10.64434/tml.20250910}
}
```

**DOI:** 10.64434/tml.20250910
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "fe220594-dad9-4202-b91e-c39772c1af24",
  "tool_use_result": {
    "bytes": 82338,
    "code": 200,
    "codeText": "OK",
    "result": "# Citation Information for \"Defeating Nondeterminism in LLM Inference\"\n\n**Author(s):** Horace He in collaboration with others at Thinking Machines Lab\n\n**Publication Date:** September 10, 2025\n\n**Formal Citation Information:**\n\nThe post provides its own suggested citations:\n\nChicago-style format: \"He, Horace and Thinking Machines Lab, 'Defeating Nondeterminism in LLM Inference', Thinking Machines Lab: Connectionism, Sep 2025.\"\n\nBibTeX format:\n```\n@article{he2025nondeterminism,\n  author = {Horace He and Thinking Machines Lab},\n  title = {Defeating Nondeterminism in LLM Inference},\n  journal = {Thinking Machines Lab: Connectionism},\n  year = {2025},\n  note = {https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/},\n  doi = {10.64434/tml.20250910}\n}\n```\n\n**DOI:** 10.64434/tml.20250910",
    "durationMs": 2781,
    "url": "https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/"
  }
}
````

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also verify the Yuan et al. full author list.

From the search results, the authors for Yuan et al. are: Jiayi Yuan, Hao Li, Xinheng Ding, Wenya Xie, Yu-Jhe Li, Wentian Zhao, Kun Wan, Jing Shi, Xia Hu, and Zirui Liu.

Let me verify by fetching the arXiv page.

Actually, I already have enough information. Let me now compile everything and update the literature_map.yaml.


Now I'm checking the three existing papers to make sure all the details are correct—verifying titles, author lists, years, and venues. For the Yuan et al. paper on LayerCast, I have the full author list and can confirm it's from 2025, though I need to verify the NeurIPS venue designation. I'm noticing the title discrepancy — the blog post uses "Defeating Nondeterminism in LLM Inference" while ResearchGate shows a longer version with "Batch Invariance, Seed Locking, and Beyond." I'll go with the official blog citation since that's the primary source, and I need to add Horace He as the author, update the venue to "Thinking Machines Lab: Connectionism," and include the DOI. The official citation uses the shorter title "Defeating Nondeterminism in LLM Inference," so I'll go with that. I need to keep the existing bibtex_key `thinkingmachines2025batch` since it might be referenced elsewhere, even though it doesn't quite match the standard format they mentioned.

Now I'm adding a second paper about floating-point non-associativity and its effects on reproducibility in HPC and deep learning, authored by Shanmugavelu and colleagues from 2024.

For the metadata, I'm noting the DOI, categorizing it under infrastructure variance, and marking it as background material since it provides the theoretical foundation for understanding how floating-point operations in parallel systems like CUDA kernels produce bitwise-different results depending on reduction order.

I'm also starting to add a third entry on deterministic inference across tensor parallel sizes by Zhang and team from 2025, which addresses training-inference mismatch in distributed models.

Now I need to update the YAML file with these new papers and make several corrections to existing entries, then increment the total paper count from 16 to 18 and refresh the timestamp.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "34878f23-9af7-4ca2-842e-87b59d7d1bdd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uhCSBqmYbE9jEwh7hcGiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 46448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 60_

Now I have all verified information. Let me update the literature_map.yaml with all changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2cbea52b-0b39-44ac-8b10-58ae92161a24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uhCSBqmYbE9jEwh7hcGiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 46448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 61_

<details open><summary>🔧 Tool call — Edit · `toolu_01Av6B1CPjyeDgLHR9UFRKnM`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "meta:\n  last_updated: \"2026-05-20T14:00:00Z\"\n  total_papers: 16",
  "new_string": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "6235f9b4-cd71-482b-8af7-6e52737ab495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016uhCSBqmYbE9jEwh7hcGiv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 652,
      "cache_read_input_tokens": 46448,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 652
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

_source line 62 · 2026-05-21T18:18:46.187Z_

<details><summary>↩ Tool result · `toolu_01Av6B1CPjyeDgLHR9UFRKnM`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2b17a7cf-442a-44f5-8de4-8645b4f46c88",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "oldString": "meta:\n  last_updated: \"2026-05-20T14:00:00Z\"\n  total_papers: 16",
    "newString": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18",
    "originalFile": "meta:\n  last_updated: \"2026-05-20T14:00:00Z\"\n  total_papers: 16\n\ncategories:\n  - key: \"gtheory_evaluation\"\n    name: \"G-Theory & Evaluation Variance\"\n    narrative: \"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\"\n  - key: \"infrastructure_variance\"\n    name: \"Infrastructure-Induced Variance\"\n    narrative: \"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\"\n  - key: \"prompt_sensitivity\"\n    name: \"Prompt Sensitivity & Methodological Variance\"\n    narrative: \"Prompt phrasing, seed, temperature, and ordering as variance sources\"\n  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n\npapers:\n  mesting2026hidden:\n    title: \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"\n    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " meta:",
          "-  last_updated: \"2026-05-20T14:00:00Z\"",
          "-  total_papers: 16",
          "+  last_updated: \"2026-05-21T12:00:00Z\"",
          "+  total_papers: 18",
          " ",
          " categories:",
          "   - key: \"gtheory_evaluation\""
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

<details open><summary>🔧 Tool call — Edit · `toolu_01B67nZSvLniQ3DYTJqjkTQB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "74ef116a-7cf2-4fc9-9f6a-a52452408ef1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VD2BaRC16p9jS3rdg1M9Kw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2064,
      "cache_read_input_tokens": 47100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2064
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

_source line 64 · 2026-05-21T18:18:59.346Z_

<details><summary>↩ Tool result · `toolu_01B67nZSvLniQ3DYTJqjkTQB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "c97711ff-d34a-4cac-b3b9-94500841de77",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "oldString": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "newString": "  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "originalFile": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18\n\ncategories:\n  - key: \"gtheory_evaluation\"\n    name: \"G-Theory & Evaluation Variance\"\n    narrative: \"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\"\n  - key: \"infrastructure_variance\"\n    name: \"Infrastructure-Induced Variance\"\n    narrative: \"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\"\n  - key: \"prompt_sensitivity\"\n    name: \"Prompt Sensitivity & Methodological Variance\"\n    narrative: \"Prompt phrasing, seed, temperature, and ordering as variance sources\"\n  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n\npapers:\n  mesting2026hidden:\n    title: \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"\n    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
    "structuredPatch": [
      {
        "oldStart": 47,
        "oldLines": 14,
        "newStart": 47,
        "newLines": 23,
        "lines": [
          "   yuan2025layercast:",
          "     title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"",
          "     authors:",
          "-      - \"Yuan, Z.\"",
          "+      - \"Yuan, J.\"",
          "+      - \"Li, H.\"",
          "+      - \"Ding, X.\"",
          "+      - \"Xie, W.\"",
          "+      - \"Li, Y.-J.\"",
          "+      - \"Zhao, W.\"",
          "+      - \"Wan, K.\"",
          "+      - \"Shi, J.\"",
          "+      - \"Hu, X.\"",
          "+      - \"Liu, Z.\"",
          "     year: 2025",
          "-    venue: \"arXiv\"",
          "+    venue: \"NeurIPS 2025 (Oral)\"",
          "     url: \"https://arxiv.org/abs/2506.09501\"",
          "     category: \"infrastructure_variance\"",
          "     role: \"direct-competitor\"",
          "     relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"",
          "-    verified: false",
          "+    verified: true",
          "     added_by: \"director\"",
          "     added_at: \"2026-05-20T14:00:00Z\"",
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

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_01WjL28n1QXR2XqWxtS4qPM8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"\n    authors:\n      - \"Messina, A.\"\n      - \"Scotta, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "d8345a8f-6707-4f26-a7ab-26e2841daaa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013fHuJ7R95a17wBXbbTpxYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 49164,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 72,
      "service_tier": "standard",
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

_source line 66 · 2026-05-21T18:19:07.313Z_

<details><summary>↩ Tool result · `toolu_01WjL28n1QXR2XqWxtS4qPM8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "bc08aebf-2709-4c6b-830f-8c73939ada01",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "oldString": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "newString": "  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"\n    authors:\n      - \"Messina, A.\"\n      - \"Scotta, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "originalFile": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18\n\ncategories:\n  - key: \"gtheory_evaluation\"\n    name: \"G-Theory & Evaluation Variance\"\n    narrative: \"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\"\n  - key: \"infrastructure_variance\"\n    name: \"Infrastructure-Induced Variance\"\n    narrative: \"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\"\n  - key: \"prompt_sensitivity\"\n    name: \"Prompt Sensitivity & Methodological Variance\"\n    narrative: \"Prompt phrasing, seed, temperature, and ordering as variance sources\"\n  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n\npapers:\n  mesting2026hidden:\n    title: \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"\n    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"\n    authors:\n      - \"Messina, P.\"\n      - \"Scotta, A.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
    "structuredPatch": [
      {
        "oldStart": 68,
        "oldLines": 17,
        "newStart": 68,
        "newLines": 17,
        "lines": [
          "     added_at: \"2026-05-20T14:00:00Z\"",
          " ",
          "   messina2026background:",
          "-    title: \"Introducing Background Temperature to Characterise Hidden Randomness in LLMs\"",
          "+    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"",
          "     authors:",
          "-      - \"Messina, P.\"",
          "-      - \"Scotta, A.\"",
          "+      - \"Messina, A.\"",
          "+      - \"Scotta, S.\"",
          "     year: 2026",
          "     venue: \"arXiv\"",
          "     url: \"https://arxiv.org/abs/2604.22411\"",
          "     category: \"infrastructure_variance\"",
          "     role: \"method-component\"",
          "     relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"",
          "-    verified: false",
          "+    verified: true",
          "     added_by: \"director\"",
          "     added_at: \"2026-05-20T14:00:00Z\"",
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

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_01FkCr2ybejTa2pE2fTmt4Hp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
  "new_string": "  thinkingmachines2025batch:\n    title: \"Defeating Nondeterminism in LLM Inference\"\n    authors:\n      - \"He, H.\"\n      - \"Thinking Machines Lab\"\n    year: 2025\n    venue: \"Thinking Machines Lab: Connectionism\"\n    url: \"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/\"\n    doi: \"10.64434/tml.20250910\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "c3d5c79c-5a34-4fb5-b1ad-82a717e210a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015EM6qGyvGK2svmt4VBdfqz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 715,
      "cache_read_input_tokens": 49857,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 715
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 68 · 2026-05-21T18:19:17.151Z_

<details><summary>↩ Tool result · `toolu_01FkCr2ybejTa2pE2fTmt4Hp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "e1e2c3e2-4c52-4523-9db0-a1ca21b458f2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "oldString": "  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "newString": "  thinkingmachines2025batch:\n    title: \"Defeating Nondeterminism in LLM Inference\"\n    authors:\n      - \"He, H.\"\n      - \"Thinking Machines Lab\"\n    year: 2025\n    venue: \"Thinking Machines Lab: Connectionism\"\n    url: \"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/\"\n    doi: \"10.64434/tml.20250910\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"",
    "originalFile": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18\n\ncategories:\n  - key: \"gtheory_evaluation\"\n    name: \"G-Theory & Evaluation Variance\"\n    narrative: \"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\"\n  - key: \"infrastructure_variance\"\n    name: \"Infrastructure-Induced Variance\"\n    narrative: \"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\"\n  - key: \"prompt_sensitivity\"\n    name: \"Prompt Sensitivity & Methodological Variance\"\n    narrative: \"Prompt phrasing, seed, temperature, and ordering as variance sources\"\n  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n\npapers:\n  mesting2026hidden:\n    title: \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"\n    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"\n    authors:\n      - \"Messina, A.\"\n      - \"Scotta, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  thinkingmachines2025batch:\n    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"\n    authors: []\n    year: 2025\n    venue: \"Technical Report\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
    "structuredPatch": [
      {
        "oldStart": 112,
        "oldLines": 14,
        "newStart": 112,
        "newLines": 18,
        "lines": [
          "     added_at: \"2026-05-20T14:00:00Z\"",
          " ",
          "   thinkingmachines2025batch:",
          "-    title: \"Batch Invariance, Seed Locking, and Beyond: Countering Nondeterminism in LLM Inference\"",
          "-    authors: []",
          "+    title: \"Defeating Nondeterminism in LLM Inference\"",
          "+    authors:",
          "+      - \"He, H.\"",
          "+      - \"Thinking Machines Lab\"",
          "     year: 2025",
          "-    venue: \"Technical Report\"",
          "+    venue: \"Thinking Machines Lab: Connectionism\"",
          "+    url: \"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/\"",
          "+    doi: \"10.64434/tml.20250910\"",
          "     category: \"infrastructure_variance\"",
          "     role: \"method-component\"",
          "     relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"",
          "-    verified: false",
          "+    verified: true",
          "     added_by: \"director\"",
          "     added_at: \"2026-05-20T14:00:00Z\"",
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

### Assistant

_source line 69_

Now adding the 2 new papers at the end of the papers section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "9abfff1e-d8b9-43b2-bb22-81db52c9fce2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5yiaUYw2Re9wvwptrYcHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 50572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 675
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

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01LWrEeKGnEyMtVmdxHo2XfZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "offset": 255
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "856fcba0-c1ea-4849-9a4a-5fbe82d8bf07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P5yiaUYw2Re9wvwptrYcHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 50572,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 675
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

_source line 71 · 2026-05-21T18:19:19.964Z_

<details><summary>↩ Tool result · `toolu_01LWrEeKGnEyMtVmdxHo2XfZ`</summary>

```text
255	      - "Lignos, C."
256	    year: 2025
257	    venue: "IJCNLP-AACL"
258	    url: "https://arxiv.org/abs/2509.22612"
259	    category: "gtheory_evaluation"
260	    role: "background"
261	    relevance: "Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error."
262	    verified: true
263	    added_by: "worker"
264	    added_at: "2026-05-21T00:00:00Z"
265	
266	  song2025exploring:
267	    title: "Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory"
268	    authors:
269	      - "Song, D."
270	      - "Lee, W.-C."
271	      - "Jiao, H."
272	    year: 2025
273	    venue: "arXiv"
274	    url: "https://arxiv.org/abs/2507.19980"
275	    category: "gtheory_evaluation"
276	    role: "background"
277	    relevance: "Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation."
278	    verified: true
279	    added_by: "worker"
280	    added_at: "2026-05-21T00:00:00Z"
281	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "6978af22-2d44-41ba-820d-869e33459d89",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
      "content": "      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
      "numLines": 27,
      "startLine": 255,
      "totalLines": 281
    }
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_01UzsbVZS8GFxG67hBVtSszY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "    added_at: \"2026-05-21T00:00:00Z\"\n",
  "new_string": "    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "faa72d4c-10de-437c-8f01-2752e7120fc1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RWdRkfCsSS5cWm9JUzu62X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 533,
      "cache_read_input_tokens": 51247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 533
      },
      "output_tokens": 37,
      "service_tier": "standard",
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

_source line 73 · 2026-05-21T18:19:33.313Z_

<details><summary>↩ Tool result · reported error · `toolu_01UzsbVZS8GFxG67hBVtSszY`</summary>

```text
&lt;tool_use_error>Found 6 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.
String:     added_at: "2026-05-21T00:00:00Z"
&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "8e26a8f6-a443-41b2-9482-d695f049b7be",
  "tool_use_result": "Error: Found 6 matches of the string to replace, but replace_all is false. To replace all occurrences, set replace_all to true. To replace only one occurrence, please provide more context to uniquely identify the instance.\nString:     added_at: \"2026-05-21T00:00:00Z\"\n"
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_011toa5qfYcmBCkLAdFXZf76`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "old_string": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"",
  "new_string": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "6e5ce642-bc6f-45e0-ad88-1185d2d013d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeWh9xRiN3i5C9JqKzbVQV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 830,
      "cache_read_input_tokens": 51780,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 830
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

_source line 75 · 2026-05-21T18:19:43.774Z_

<details><summary>↩ Tool result · `toolu_011toa5qfYcmBCkLAdFXZf76`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "d571bc4b-f1d4-4188-bc64-efd0559fda3c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
    "oldString": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"",
    "newString": "  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shanmugavelu2024floating:\n    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"\n    authors:\n      - \"Shanmugavelu, S.\"\n      - \"Taillefumier, M.\"\n      - \"Culver, C.\"\n      - \"Hernandez, O.\"\n      - \"Coletti, M.\"\n      - \"Sedova, A.\"\n    year: 2024\n    venue: \"SC'24 Workshops (IEEE)\"\n    url: \"https://arxiv.org/abs/2408.05148\"\n    doi: \"10.1109/SCW63240.2024.00028\"\n    category: \"infrastructure_variance\"\n    role: \"background\"\n    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"\n\n  zhang2025tbik:\n    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"\n    authors:\n      - \"Zhang, Z.\"\n      - \"Ding, X.\"\n      - \"Yuan, J.\"\n      - \"Liu, R.\"\n      - \"Mao, H.\"\n      - \"Xing, J.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2511.17826\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T12:00:00Z\"",
    "originalFile": "meta:\n  last_updated: \"2026-05-21T12:00:00Z\"\n  total_papers: 18\n\ncategories:\n  - key: \"gtheory_evaluation\"\n    name: \"G-Theory & Evaluation Variance\"\n    narrative: \"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\"\n  - key: \"infrastructure_variance\"\n    name: \"Infrastructure-Induced Variance\"\n    narrative: \"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\"\n  - key: \"prompt_sensitivity\"\n    name: \"Prompt Sensitivity & Methodological Variance\"\n    narrative: \"Prompt phrasing, seed, temperature, and ordering as variance sources\"\n  - key: \"evaluation_methodology\"\n    name: \"Evaluation Methodology\"\n    narrative: \"Scoring artifacts, benchmark design, and evaluation protocol considerations\"\n\npapers:\n  mesting2026hidden:\n    title: \"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\"\n    authors:\n      - \"Messing, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.11581\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  brittlebench2026:\n    title: \"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2603.13285\"\n    category: \"prompt_sensitivity\"\n    role: \"direct-competitor\"\n    relevance: \"Up to 50% performance variance from prompt perturbations, 63% of cases show ranking reversals from single perturbations. Provides perturbation protocol we follow for prompt paraphrase generation. Does not cross with infrastructure factors.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  yuan2025layercast:\n    title: \"Understanding and Mitigating Numerical Sources of Nondeterminism in LLM Inference\"\n    authors:\n      - \"Yuan, J.\"\n      - \"Li, H.\"\n      - \"Ding, X.\"\n      - \"Xie, W.\"\n      - \"Li, Y.-J.\"\n      - \"Zhao, W.\"\n      - \"Wan, K.\"\n      - \"Shi, J.\"\n      - \"Hu, X.\"\n      - \"Liu, Z.\"\n    year: 2025\n    venue: \"NeurIPS 2025 (Oral)\"\n    url: \"https://arxiv.org/abs/2506.09501\"\n    category: \"infrastructure_variance\"\n    role: \"direct-competitor\"\n    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  messina2026background:\n    title: \"Introducing Background Temperature to Characterise Hidden Randomness in Large Language Models\"\n    authors:\n      - \"Messina, A.\"\n      - \"Scotta, S.\"\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2604.22411\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  generalizit2024:\n    title: \"GeneralizIT: A Python Solution for Generalizability Theory Computations\"\n    authors:\n      - \"Smith, T.J.\"\n      - \"Kline, T.\"\n      - \"Kline, A.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2411.17880\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Python implementation of G-theory computations including D-study projections. Core analysis tool for our variance decomposition pipeline.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  hua2025flaw:\n    title: \"Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs\"\n    authors:\n      - \"Hua, W.\"\n    year: 2025\n    venue: \"EMNLP\"\n    category: \"evaluation_methodology\"\n    role: \"evaluation\"\n    relevance: \"Demonstrates log-likelihood-based evaluation inflates apparent prompt sensitivity — a confounder our generation-based evaluation protocol controls for. Motivates our choice of generation-based scoring.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  thinkingmachines2025batch:\n    title: \"Defeating Nondeterminism in LLM Inference\"\n    authors:\n      - \"He, H.\"\n      - \"Thinking Machines Lab\"\n    year: 2025\n    venue: \"Thinking Machines Lab: Connectionism\"\n    url: \"https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/\"\n    doi: \"10.64434/tml.20250910\"\n    category: \"infrastructure_variance\"\n    role: \"method-component\"\n    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  kunievsky2025intent:\n    title: \"Measuring Intent Comprehension in LLMs: A Variance Decomposition Framework\"\n    authors:\n      - \"Kunievsky, N.\"\n      - \"Evans, J.A.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2506.16584\"\n    category: \"gtheory_evaluation\"\n    role: \"direct-competitor\"\n    relevance: \"Decomposes variance into intent, articulation, and model uncertainty facets. Does not include infrastructure factors. Provides alternative facet structure we compare against.\"\n    verified: true\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bui2025seeds:\n    title: \"Assessing the Macro and Micro Effects of Random Seeds on Fine-Tuning Large Language Models\"\n    authors:\n      - \"Bui, T.\"\n    year: 2025\n    venue: \"arXiv\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Documents extreme seed sensitivity (RTES variance=18.22) in fine-tuning. Motivates our fine-tuning G-study extension. Isolated factor study without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  sameprompt2026:\n    title: \"Same Prompt, Different Outcomes: Evaluating the Reproducibility of Data Analysis by LLMs\"\n    authors: []\n    year: 2026\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2602.14349\"\n    category: \"prompt_sensitivity\"\n    role: \"background\"\n    relevance: \"Evaluated 2 strategies x 6 models x 4 temperatures with 10 repeats but excluded hardware/precision. Confirms methodology-layer variance without infrastructure crossing.\"\n    verified: false\n    added_by: \"director\"\n    added_at: \"2026-05-20T14:00:00Z\"\n\n  bouthillier2021accounting:\n    title: \"Accounting for Variance in Machine Learning Benchmarks\"\n    authors:\n      - \"Bouthillier, X.\"\n      - \"Delaunay, P.\"\n      - \"Bronzi, M.\"\n      - \"Trofimov, A.\"\n      - \"Nichyporuk, B.\"\n      - \"Szeto, J.\"\n      - \"Sepahvand, N.M.\"\n      - \"Raff, E.\"\n      - \"Madan, K.\"\n      - \"Voleti, V.\"\n      - \"Kahou, S.E.\"\n      - \"Michalski, V.\"\n      - \"Arbel, T.\"\n      - \"Pal, C.\"\n      - \"Varoquaux, G.\"\n      - \"Vincent, P.\"\n    year: 2021\n    venue: \"MLSys\"\n    url: \"https://arxiv.org/abs/2103.03098\"\n    category: \"gtheory_evaluation\"\n    role: \"method-component\"\n    relevance: \"Models the full ML benchmarking process, decomposing variance from data sampling, initialization, and hyperparameters via ANOVA. Foundational work on variance attribution in ML evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  shavelson1991generalizability:\n    title: \"Generalizability Theory: A Primer\"\n    authors:\n      - \"Shavelson, R.J.\"\n      - \"Webb, N.M.\"\n    year: 1991\n    venue: \"SAGE Publications\"\n    isbn: \"978-0-8039-3744-4\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Canonical introductory textbook on G-theory. Defines the G-study/D-study framework and variance component estimation we adopt.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  brennan2001generalizability:\n    title: \"Generalizability Theory\"\n    authors:\n      - \"Brennan, R.L.\"\n    year: 2001\n    venue: \"Springer\"\n    isbn: \"978-0-387-95282-6\"\n    category: \"gtheory_evaluation\"\n    role: \"foundational\"\n    relevance: \"Definitive G-theory reference. Ch.12 on binary/polytomous data directly supports our accuracy-based variance decomposition.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  madaan2024quantifying:\n    title: \"Quantifying Variance in Evaluation Benchmarks\"\n    authors:\n      - \"Madaan, L.\"\n      - \"Singh, A.K.\"\n      - \"Schaeffer, R.\"\n      - \"Poulton, A.\"\n      - \"Koyejo, S.\"\n      - \"Stenetorp, P.\"\n      - \"Narang, S.\"\n      - \"Hupkes, D.\"\n    year: 2024\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2406.10229\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Empirical study of seed variance and monotonicity across 13 NLP benchmarks and 280+ models. Provides metrics for quantifying evaluation variance we build upon.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  saleva2025beyond:\n    title: \"Beyond Statistical Significance: Quantifying Uncertainty and Statistical Variability in Multilingual and Multitask NLP Evaluation\"\n    authors:\n      - \"Sälevä, J.\"\n      - \"Ataman, D.\"\n      - \"Lignos, C.\"\n    year: 2025\n    venue: \"IJCNLP-AACL\"\n    url: \"https://arxiv.org/abs/2509.22612\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Introduces resampling-based variance component analysis for multilingual/multitask NLP benchmarks, showing multiple non-negligible variance sources beyond sampling error.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n\n  song2025exploring:\n    title: \"Exploring LLM Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory\"\n    authors:\n      - \"Song, D.\"\n      - \"Lee, W.-C.\"\n      - \"Jiao, H.\"\n    year: 2025\n    venue: \"arXiv\"\n    url: \"https://arxiv.org/abs/2507.19980\"\n    category: \"gtheory_evaluation\"\n    role: \"background\"\n    relevance: \"Applies G-theory to compare human vs. LLM rater reliability in educational writing assessment. Directly bridges G-theory methodology and LLM evaluation.\"\n    verified: true\n    added_by: \"worker\"\n    added_at: \"2026-05-21T00:00:00Z\"\n",
    "structuredPatch": [
      {
        "oldStart": 278,
        "oldLines": 3,
        "newStart": 278,
        "newLines": 43,
        "lines": [
          "     verified: true",
          "     added_by: \"worker\"",
          "     added_at: \"2026-05-21T00:00:00Z\"",
          "+",
          "+  shanmugavelu2024floating:",
          "+    title: \"Impacts of Floating-Point Non-Associativity on Reproducibility for HPC and Deep Learning Applications\"",
          "+    authors:",
          "+      - \"Shanmugavelu, S.\"",
          "+      - \"Taillefumier, M.\"",
          "+      - \"Culver, C.\"",
          "+      - \"Hernandez, O.\"",
          "+      - \"Coletti, M.\"",
          "+      - \"Sedova, A.\"",
          "+    year: 2024",
          "+    venue: \"SC'24 Workshops (IEEE)\"",
          "+    url: \"https://arxiv.org/abs/2408.05148\"",
          "+    doi: \"10.1109/SCW63240.2024.00028\"",
          "+    category: \"infrastructure_variance\"",
          "+    role: \"background\"",
          "+    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"",
          "+    verified: true",
          "+    added_by: \"worker\"",
          "+    added_at: \"2026-05-21T12:00:00Z\"",
          "+",
          "+  zhang2025tbik:",
          "+    title: \"Deterministic Inference across Tensor Parallel Sizes That Eliminates Training-Inference Mismatch\"",
          "+    authors:",
          "+      - \"Zhang, Z.\"",
          "+      - \"Ding, X.\"",
          "+      - \"Yuan, J.\"",
          "+      - \"Liu, R.\"",
          "+      - \"Mao, H.\"",
          "+      - \"Xing, J.\"",
          "+      - \"Liu, Z.\"",
          "+    year: 2025",
          "+    venue: \"arXiv\"",
          "+    url: \"https://arxiv.org/abs/2511.17826\"",
          "+    category: \"infrastructure_variance\"",
          "+    role: \"method-component\"",
          "+    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"",
          "+    verified: true",
          "+    added_by: \"worker\"",
          "+    added_at: \"2026-05-21T12:00:00Z\""
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

_source line 76_

Let me verify the final state of the infrastructure_variance entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2d0e127d-e00d-4b5e-96a4-39932b046688",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEAyTRFNpLEKgBMFihiX5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 52610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1131
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

_source line 77_

<details open><summary>🔧 Tool call — Grep · `toolu_01SPQ3U3WrLGmEy9L18ct3Kh`</summary>

```json
{
  "pattern": "infrastructure_variance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "output_mode": "count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "8aa22b52-31d0-4bb7-9ef3-272e391224b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BEAyTRFNpLEKgBMFihiX5i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1131,
      "cache_read_input_tokens": 52610,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1131
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

_source line 78 · 2026-05-21T18:19:47.757Z_

<details><summary>↩ Tool result · `toolu_01SPQ3U3WrLGmEy9L18ct3Kh`</summary>

```text
6

Found 0 total occurrences across 0 files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "3b3e5663-80ad-490e-a804-bbd2ad346d73",
  "tool_use_result": {
    "mode": "count",
    "numFiles": 0,
    "filenames": [],
    "content": "6",
    "numMatches": 0
  }
}
```

</details>

---

### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
6 matches: 1 in categories definition + 5 papers. That's correct: yuan2025layercast, messina2026background, thinkingmachines2025batch, shanmugavelu2024floating, zhang2025tbik.

Let me also verify the verified status of all infrastructure_variance papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "70a2cba6-aec6-49a9-8c48-93109feb25a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaqyUimJYwuL8Hp8hQaGvi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 53741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
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

_source line 80_

<details open><summary>🔧 Tool call — Grep · `toolu_01CPhD9ytxbKHHL2t4KkqNbn`</summary>

```json
{
  "pattern": "category: \"infrastructure_variance\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml",
  "output_mode": "content",
  "-A": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "2f60db86-b744-48d3-86e9-a7899efda6bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BaqyUimJYwuL8Hp8hQaGvi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 164,
      "cache_read_input_tokens": 53741,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 164
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

_source line 81 · 2026-05-21T18:19:52.774Z_

<details><summary>↩ Tool result · `toolu_01CPhD9ytxbKHHL2t4KkqNbn`</summary>

```text
63:    category: "infrastructure_variance"
64-    role: "direct-competitor"
65-    relevance: "Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources."
--
78:    category: "infrastructure_variance"
79-    role: "method-component"
80-    relevance: "Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure."
--
123:    category: "infrastructure_variance"
124-    role: "method-component"
125-    relevance: "Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions."
--
295:    category: "infrastructure_variance"
296-    role: "background"
297-    relevance: "Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference."
--
315:    category: "infrastructure_variance"
316-    role: "method-component"
317-    relevance: "Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "e40d6296-3f76-42e8-9201-6a076719ba01",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "63:    category: \"infrastructure_variance\"\n64-    role: \"direct-competitor\"\n65-    relevance: \"Documents up to 9% accuracy variation and 9,000-token response-length shifts from GPU count, type, and precision changes. Proposes LayerCast (FP16 storage + FP32 compute) mitigation. Does not conduct factorial attribution across multiple variance sources.\"\n--\n78:    category: \"infrastructure_variance\"\n79-    role: \"method-component\"\n80-    relevance: \"Formalizes hidden nondeterminism as effective background temperature T_bg persisting even at nominal T=0 due to floating-point non-associativity in BF16/FP16. Provides theoretical framework for understanding infrastructure-level stochasticity we measure.\"\n--\n123:    category: \"infrastructure_variance\"\n124-    role: \"method-component\"\n125-    relevance: \"Shows 80/1000 unique completions for Qwen3-8B at T=0 under default vLLM settings. Demonstrates batch-invariant GEMM/RMSNorm/attention kernels eliminate nondeterminism with 1.6-2.1x latency overhead. We use DEFAULT settings (without these kernels) to reflect practitioner conditions.\"\n--\n295:    category: \"infrastructure_variance\"\n296-    role: \"background\"\n297-    relevance: \"Theoretical and empirical analysis of floating-point non-associativity in CUDA parallel reductions. Documents how reduction order changes produce bitwise-different results across GPUs, providing the mathematical foundation for infrastructure-induced variance we observe in LLM inference.\"\n--\n315:    category: \"infrastructure_variance\"\n316-    role: \"method-component\"\n317-    relevance: \"Proposes Tree-Based Invariant Kernels (TBIK) achieving bit-wise identical LLM outputs regardless of tensor-parallel configuration. Demonstrates TP size as an infrastructure variance source producing divergent outputs from identical inputs, directly supporting our infrastructure facet design.\"",
    "numLines": 19
  }
}
```

</details>

---

### Assistant

_source line 82_

5 infrastructure_variance papers, all verified. Here's the summary:

## Infrastructure Variance Cluster — 5 papers verified

| # | Key | Paper | Venue | Status |
|---|-----|-------|-------|--------|
| 1 | `yuan2025layercast` | Yuan et al. — LayerCast, up to 9% accuracy variation from precision/GPU | NeurIPS 2025 (Oral) | verified, authors+venue updated |
| 2 | `messina2026background` | Messina & Scotta — background temperature T_bg formalization | arXiv 2604.22411 | verified, title+authors corrected |
| 3 | `thinkingmachines2025batch` | He & Thinking Machines Lab — batch-invariant kernels, 80/1000 unique at T=0 | Connectionism blog, DOI: 10.64434/tml.20250910 | verified, title+authors+URL+DOI added |
| 4 | `shanmugavelu2024floating` | Shanmugavelu et al. — FP non-associativity in CUDA reductions | SC'24 Workshops (IEEE) | **NEW**, verified |
| 5 | `zhang2025tbik` | Zhang et al. — TBIK for TP-invariant deterministic inference | arXiv 2511.17826 | **NEW**, verified |

Key corrections made:
- Yuan et al. venue upgraded from "arXiv" to "NeurIPS 2025 (Oral)", full 10-author list added
- Messina authors corrected: Alberto Messina → `Messina, A.`, Stefano Scotta → `Scotta, S.`
- ThinkingMachines title updated to official citation "Defeating Nondeterminism in LLM Inference", author Horace He added, DOI added
- `total_papers` updated 16 → 18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "uuid": "cebc8496-bb83-4a50-a699-c928a0f7f3e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DD4bFwB9FuDUhAHaBH4jKX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 722,
      "cache_read_input_tokens": 53905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 722
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

_source line 83_

5 infrastructure_variance papers, all verified. Here's the summary:

## Infrastructure Variance Cluster — 5 papers verified

| # | Key | Paper | Venue | Status |
|---|-----|-------|-------|--------|
| 1 | `yuan2025layercast` | Yuan et al. — LayerCast, up to 9% accuracy variation from precision/GPU | NeurIPS 2025 (Oral) | verified, authors+venue updated |
| 2 | `messina2026background` | Messina & Scotta — background temperature T_bg formalization | arXiv 2604.22411 | verified, title+authors corrected |
| 3 | `thinkingmachines2025batch` | He & Thinking Machines Lab — batch-invariant kernels, 80/1000 unique at T=0 | Connectionism blog, DOI: 10.64434/tml.20250910 | verified, title+authors+URL+DOI added |
| 4 | `shanmugavelu2024floating` | Shanmugavelu et al. — FP non-associativity in CUDA reductions | SC'24 Workshops (IEEE) | **NEW**, verified |
| 5 | `zhang2025tbik` | Zhang et al. — TBIK for TP-invariant deterministic inference | arXiv 2511.17826 | **NEW**, verified |

Key corrections made:
- Yuan et al. venue upgraded from "arXiv" to "NeurIPS 2025 (Oral)", full 10-author list added
- Messina authors corrected: Alberto Messina → `Messina, A.`, Stefano Scotta → `Scotta, S.`
- ThinkingMachines title updated to official citation "Defeating Nondeterminism in LLM Inference", author Horace He added, DOI added
- `total_papers` updated 16 → 18

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 260919,
  "duration_api_ms": 336390,
  "num_turns": 31,
  "stop_reason": "end_turn",
  "session_id": "d3f168ca-13ff-4c8d-b1ea-6a42f1b4685a",
  "total_cost_usd": 1.3126720000000003,
  "usage": {
    "input_tokens": 3326,
    "cache_creation_input_tokens": 42786,
    "cache_read_input_tokens": 801341,
    "output_tokens": 10001,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42786,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 474,
        "cache_read_input_tokens": 53905,
        "cache_creation_input_tokens": 722,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 722
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 179954,
      "outputTokens": 7596,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 16,
      "costUSD": 0.37793400000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3326,
      "outputTokens": 10001,
      "cacheReadInputTokens": 801341,
      "cacheCreationInputTokens": 42786,
      "webSearchRequests": 0,
      "costUSD": 0.934738,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ce3bb79c-7673-43eb-baaf-796a65aa414a"
}
```

</details>

---
