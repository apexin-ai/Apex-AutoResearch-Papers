# paper research inference time compute

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_paper_research_inference_time_compute_20260518T092521.log`
- **Structured JSON:** [`d3c0cb282d1ebd9590f3.json`](../../sessions/d3/d3c0cb282d1ebd9590f3.json)

## Before a recorded user message

55 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
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
  "uuid": "65de624e-0907-45e0-89c3-9396cdfd8fea",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779113400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e12cf77a-4acd-4957-817b-218def65becf",
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b"
}
```

---

### Assistant

_source line 4_

I'll search for the 3 papers on inference-time compute scaling and verify the existing entry. Let me start by reading the current literature map and searching in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "dc0ca813-b596-4836-a3d9-4abf6badcb9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnakyDqFbo4LpxkNECiDT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13495
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

<details open><summary>🔧 Tool call — Read · `toolu_01UjNmTk6VWDjnRuQRCEcJrf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "bb475f3c-ba53-4b18-9343-3c687312b910",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnakyDqFbo4LpxkNECiDT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13495
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

_source line 6 · 2026-05-18T09:25:33.131Z_

<details><summary>↩ Tool result · `toolu_01UjNmTk6VWDjnRuQRCEcJrf`</summary>

```text
1	papers:
2	  - bibtex_key: "a2c2_2025"
3	    title: "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"
4	    authors: "Sendai et al."
5	    year: 2025
6	    venue: "arXiv:2509.23224"
7	    url: "https://arxiv.org/abs/2509.23224"
8	    category: "inference_correction"
9	    verified: true
10	    relevance: "Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA."
11	    must_cite: true
12	
13	  - bibtex_key: "angelopoulos2023gentle"
14	    title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
15	    authors: "Angelopoulos & Bates"
16	    year: 2023
17	    venue: "Foundations and Trends in Machine Learning"
18	    url: "https://arxiv.org/abs/2107.07511"
19	    category: "cp_foundation"
20	    verified: true
21	    relevance: "Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA."
22	    must_cite: true
23	
24	  - bibtex_key: "barber2023conformal"
25	    title: "Conformal Prediction Beyond Exchangeability"
26	    authors: "Barber et al."
27	    year: 2023
28	    venue: "Annals of Statistics, 51(2):816-845"
29	    url: "https://arxiv.org/abs/2202.13415"
30	    category: "cp_foundation"
31	    verified: true
32	    relevance: "Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment."
33	    must_cite: false
34	
35	  - bibtex_key: "black2024pi0"
36	    title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
37	    authors: "Black et al."
38	    year: 2024
39	    venue: "arXiv:2410.24164"
40	    url: "https://arxiv.org/abs/2410.24164"
41	    category: "vla_foundation"
42	    verified: true
43	    relevance: "Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0."
44	    must_cite: false
45	
46	  - bibtex_key: "braun2025cgs"
47	    title: "Multivariate Conformal Prediction via Conformalized Gaussian Scoring"
48	    authors: "Braun et al."
49	    year: 2025
50	    venue: "arXiv:2507.20941"
51	    url: "https://arxiv.org/abs/2507.20941"
52	    category: "cp_foundation"
53	    verified: true
54	    relevance: "Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component."
55	    must_cite: true
56	
57	  - bibtex_key: "brohan2023rt2"
58	    title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
59	    authors: "Brohan et al."
60	    year: 2023
61	    venue: "arXiv:2307.15818"
62	    url: "https://arxiv.org/abs/2307.15818"
63	    category: "vla_foundation"
64	    verified: true
65	    relevance: "Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon."
66	    must_cite: false
67	
68	  - bibtex_key: "chen2026reconvla"
69	    title: "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control"
70	    authors: "Chen et al."
71	    year: 2026
72	    venue: "arXiv:2604.16677"
73	    url: "https://arxiv.org/abs/2604.16677"
74	    category: "inference_correction"
75	    verified: true
76	    relevance: "Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach."
77	    must_cite: true
78	
79	  - bibtex_key: "digflow2025"
80	    title: "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models"
81	    authors: "Zhang et al."
82	    year: 2025
83	    venue: "arXiv:2512.01715"
84	    url: "https://arxiv.org/abs/2512.01715"
85	    category: "vla_robustness_training"
86	    verified: true
87	    relevance: "Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction."
88	    must_cite: true
89	
90	  - bibtex_key: "fei2025liberoplus"
91	    title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
92	    authors: "Fei et al."
93	    year: 2025
94	    venue: "arXiv:2510.13626"
95	    url: "https://arxiv.org/abs/2510.13626"
96	    category: "other"
97	    verified: true
98	    relevance: "Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments."
99	    must_cite: true
100	
101	  - bibtex_key: "ghosh2024octo"
102	    title: "Octo: An Open-Source Generalist Robot Policy"
103	    authors: "Ghosh et al."
104	    year: 2024
105	    venue: "arXiv:2405.12213"
106	    url: "https://arxiv.org/abs/2405.12213"
107	    category: "vla_foundation"
108	    verified: true
109	    relevance: "Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution."
110	    must_cite: false
111	
112	  - bibtex_key: "gibbs2021aci"
113	    title: "Adaptive Conformal Inference Under Distribution Shift"
114	    authors: "Gibbs & Candès"
115	    year: 2021
116	    venue: "NeurIPS 2021"
117	    url: "https://arxiv.org/abs/2106.00170"
118	    category: "cp_foundation"
119	    verified: true
120	    relevance: "Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment."
121	    must_cite: true
122	
123	  - bibtex_key: "gu2025safe"
124	    title: "SAFE: Multitask Failure Detection for Vision-Language-Action Models"
125	    authors: "Gu et al."
126	    year: 2025
127	    venue: "NeurIPS 2025"
128	    url: "https://arxiv.org/abs/2506.09937"
129	    category: "inference_correction"
130	    verified: true
131	    relevance: "VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach."
132	    must_cite: true
133	
134	  - bibtex_key: "kim2024openvla"
135	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
136	    authors: "Kim et al."
137	    year: 2024
138	    venue: "arXiv:2406.09246"
139	    url: "https://arxiv.org/abs/2406.09246"
140	    category: "vla_foundation"
141	    verified: true
142	    relevance: "Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration."
143	    must_cite: false
144	
145	  - bibtex_key: "ledoit2004well"
146	    title: "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices"
147	    authors: "Ledoit & Wolf"
148	    year: 2004
149	    venue: "Journal of Multivariate Analysis, 88(2):365-411"
150	    url: "https://www.sciencedirect.com/science/article/pii/S0047259X03000964"
151	    category: "other"
152	    verified: true
153	    relevance: "Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples."
154	    must_cite: false
155	
156	  - bibtex_key: "lipman2023flow"
157	    title: "Flow Matching for Generative Modeling"
158	    authors: "Lipman et al."
159	    year: 2023
160	    venue: "ICLR 2023"
161	    url: "https://arxiv.org/abs/2210.02747"
162	    category: "other"
163	    verified: true
164	    relevance: "Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects."
165	    must_cite: false
166	
167	  - bibtex_key: "liu2023libero"
168	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
169	    authors: "Liu et al."
170	    year: 2023
171	    venue: "NeurIPS 2023"
172	    url: "https://arxiv.org/abs/2306.03310"
173	    category: "other"
174	    verified: true
175	    relevance: "Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation."
176	    must_cite: false
177	
178	  - bibtex_key: "liu2026ttvla"
179	    title: "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning"
180	    authors: "Liu et al."
181	    year: 2026
182	    venue: "arXiv:2601.06748"
183	    url: "https://arxiv.org/abs/2601.06748"
184	    category: "vla_robustness_training"
185	    verified: true
186	    relevance: "Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction."
187	    must_cite: true
188	
189	  - bibtex_key: "luan2026snapflow"
190	    title: "SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation"
191	    authors: "Luan et al."
192	    year: 2026
193	    venue: "arXiv:2604.05656"
194	    url: "https://arxiv.org/abs/2604.05656"
195	    category: "vla_robustness_training"
196	    verified: true
197	    relevance: "Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness."
198	    must_cite: true
199	
200	  - bibtex_key: "robustvla2025"
201	    title: "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"
202	    authors: "Zhang et al."
203	    year: 2025
204	    venue: "arXiv:2511.01331"
205	    url: "https://arxiv.org/abs/2511.01331"
206	    category: "vla_robustness_training"
207	    verified: true
208	    relevance: "RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach."
209	    must_cite: true
210	
211	  - bibtex_key: "romano2019cqr"
212	    title: "Conformalized Quantile Regression"
213	    authors: "Romano et al."
214	    year: 2019
215	    venue: "NeurIPS 2019"
216	    url: "https://arxiv.org/abs/1905.03222"
217	    category: "cp_foundation"
218	    verified: true
219	    relevance: "Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction."
220	    must_cite: false
221	
222	  - bibtex_key: "shafer2008tutorial"
223	    title: "A Tutorial on Conformal Prediction"
224	    authors: "Shafer & Vovk"
225	    year: 2008
226	    venue: "Journal of Machine Learning Research, 9:371-421"
227	    url: "https://jmlr.org/papers/v9/shafer08a.html"
228	    category: "cp_foundation"
229	    verified: true
230	    relevance: "Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA."
231	    must_cite: false
232	
233	  - bibtex_key: "shukor2025smolvla"
234	    title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
235	    authors: "Shukor et al."
236	    year: 2025
237	    venue: "arXiv:2506.01844"
238	    url: "https://arxiv.org/abs/2506.01844"
239	    category: "vla_foundation"
240	    verified: true
241	    relevance: "450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments."
242	    must_cite: true
243	
244	  - bibtex_key: "srpo2025"
245	    title: "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models"
246	    authors: "Fei et al."
247	    year: 2025
248	    venue: "arXiv:2511.15605"
249	    url: "https://arxiv.org/abs/2511.15605"
250	    category: "vla_robustness_training"
251	    verified: true
252	    relevance: "Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time."
253	    must_cite: true
254	
255	  - bibtex_key: "wang2025cploop"
256	    title: "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization"
257	    authors: "Wang & Ning"
258	    year: 2025
259	    venue: "arXiv:2510.16376"
260	    url: "https://arxiv.org/abs/2510.16376"
261	    category: "cp_robotics"
262	    verified: true
263	    relevance: "Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning."
264	    must_cite: true
265	
266	  - bibtex_key: "xing2026diu"
267	    title: "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching"
268	    authors: "Xing et al."
269	    year: 2026
270	    venue: "arXiv:2605.00941"
271	    url: "https://arxiv.org/abs/2605.00941"
272	    category: "uq_flow_matching"
273	    verified: true
274	    relevance: "Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage."
275	    must_cite: true
276	
277	  - bibtex_key: "yuan2026ups"
278	    title: "When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering"
279	    authors: "Yuan et al."
280	    year: 2026
281	    venue: "arXiv:2602.22474"
282	    url: "https://arxiv.org/abs/2602.22474"
283	    category: "inference_correction"
284	    verified: true
285	    relevance: "Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach."
286	    must_cite: true
287	
288	  - bibtex_key: "zhao2024conformalized"
289	    title: "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions"
290	    authors: "Zhao et al."
291	    year: 2024
292	    venue: "RSS 2024"
293	    url: "https://arxiv.org/abs/2406.07767"
294	    category: "cp_robotics"
295	    verified: true
296	    relevance: "Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach."
297	    must_cite: true
298	
299	  - bibtex_key: "cosmos_policy_2026"
300	    title: "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning"
301	    authors: "Kim et al."
302	    year: 2026
303	    venue: "arXiv:2601.16163"
304	    url: "https://arxiv.org/abs/2601.16163"
305	    category: "vla_foundation"
306	    verified: true
307	    relevance: "NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic."
308	    must_cite: false
309	
310	  - bibtex_key: "vla_gse_2026"
311	    title: "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts"
312	    authors: "Jiang et al."
313	    year: 2026
314	    venue: "arXiv:2605.06175"
315	    url: "https://arxiv.org/abs/2605.06175"
316	    category: "vla_robustness_training"
317	    verified: true
318	    relevance: "Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach."
319	    must_cite: false
320	
321	  - bibtex_key: "lakshminarayanan2017ensembles"
322	    title: "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
323	    authors: "Lakshminarayanan et al."
324	    year: 2017
325	    venue: "NeurIPS 2017"
326	    url: "https://arxiv.org/abs/1612.01474"
327	    category: "uq_foundation"
328	    verified: true
329	    relevance: "Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches."
330	    must_cite: false
331	
332	  - bibtex_key: "gal2016dropout"
333	    title: "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning"
334	    authors: "Gal & Ghahramani"
335	    year: 2016
336	    venue: "ICML 2016"
337	    url: "https://arxiv.org/abs/1506.02142"
338	    category: "uq_foundation"
339	    verified: true
340	    relevance: "Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces."
341	    must_cite: false
342	
343	  - bibtex_key: "chi2023diffusion_policy"
344	    title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
345	    authors: "Chi et al."
346	    year: 2023
347	    venue: "RSS 2023 / IJRR 2024"
348	    url: "https://arxiv.org/abs/2303.04137"
349	    category: "vla_foundation"
350	    verified: false
351	    verification_note: "Well-known paper, needs URL reachability confirmation"
352	    relevance: "Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits."
353	    must_cite: true
354	
355	  # ===== New entries added 2026-05-14 =====
356	
357	  - bibtex_key: "fan2025interpretable_mcp"
358	    title: "Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization"
359	    authors: "Fan & Sesia"
360	    year: 2025
361	    venue: "arXiv:2512.15383"
362	    url: "https://arxiv.org/abs/2512.15383"
363	    category: "cp_foundation"
364	    verified: true
365	    relevance: "Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations."
366	    must_cite: false
367	    relation: "complementary"
368	
369	  - bibtex_key: "klein2025otcp"
370	    title: "Multivariate Conformal Prediction using Optimal Transport"
371	    authors: "Klein, Bethune, Ndiaye & Cuturi"
372	    year: 2025
373	    venue: "arXiv:2502.03609"
374	    url: "https://arxiv.org/abs/2502.03609"
375	    category: "cp_foundation"
376	    verified: true
377	    relevance: "Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces."
378	    must_cite: false
379	    relation: "complementary"
380	
381	  - bibtex_key: "zollo2025vla_calibration"
382	    title: "Confidence Calibration in Vision-Language-Action Models"
383	    authors: "Zollo & Zemel"
384	    year: 2025
385	    venue: "arXiv:2507.17383"
386	    url: "https://arxiv.org/abs/2507.17383"
387	    category: "uq_vla"
388	    verified: true
389	    relevance: "First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against."
390	    must_cite: true
391	    relation: "complementary"
392	
393	  - bibtex_key: "tang2026shifting_uncertainty"
394	    title: "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model"
395	    authors: "Tang et al."
396	    year: 2026
397	    venue: "arXiv:2603.18342"
398	    url: "https://arxiv.org/abs/2603.18342"
399	    category: "uq_vla"
400	    verified: true
401	    relevance: "Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring."
402	    must_cite: false
403	    relation: "complementary"
404	
405	  - bibtex_key: "lcp2025"
406	    title: "Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception"
407	    authors: "Not specified"
408	    year: 2025
409	    venue: "arXiv:2509.21955"
410	    url: "https://arxiv.org/abs/2509.21955"
411	    category: "cp_robotics"
412	    verified: true
413	    relevance: "Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics."
414	    must_cite: false
415	    relation: "complementary"
416	
417	  - bibtex_key: "claps2025"
418	    title: "Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups"
419	    authors: "Not specified"
420	    year: 2025
421	    venue: "arXiv:2512.10294"
422	    url: "https://arxiv.org/abs/2512.10294"
423	    category: "cp_robotics"
424	    verified: true
425	    relevance: "Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones."
426	    must_cite: false
427	    relation: "complementary"
428	
429	  - bibtex_key: "lucca2024"
430	    title: "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration"
431	    authors: "Marques et al."
432	    year: 2024
433	    venue: "arXiv:2409.08249"
434	    url: "https://arxiv.org/abs/2409.08249"
435	    category: "cp_robotics"
436	    verified: true
437	    relevance: "Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty."
438	    must_cite: false
439	    relation: "complementary"
440	
441	  - bibtex_key: "sc_vla_2026"
442	    title: "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination"
443	    authors: "Li et al."
444	    year: 2026
445	    venue: "arXiv:2602.21633"
446	    url: "https://arxiv.org/abs/2602.21633"
447	    category: "inference_correction"
448	    verified: true
449	    relevance: "Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction."
450	    must_cite: true
451	    relation: "competitor"
452	
453	  - bibtex_key: "vla_pilot_2025"
454	    title: "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion"
455	    authors: "Not specified"
456	    year: 2025
457	    venue: "arXiv:2511.14178"
458	    url: "https://arxiv.org/abs/2511.14178"
459	    category: "inference_correction"
460	    verified: true
461	    relevance: "VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees."
462	    must_cite: true
463	    relation: "competitor"
464	
465	  - bibtex_key: "acot_vla_2026"
466	    title: "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models"
467	    authors: "AgibotTech"
468	    year: 2026
469	    venue: "CVPR 2026, arXiv:2601.11404"
470	    url: "https://arxiv.org/abs/2601.11404"
471	    category: "vla_robustness_training"
472	    verified: true
473	    relevance: "Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning."
474	    must_cite: false
475	    relation: "complementary"
476	
477	  - bibtex_key: "gonzales2026crc_cbf"
478	    title: "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control"
479	    authors: "Gonzales et al."
480	    year: 2026
481	    venue: "IROS 2025, arXiv:2603.10392"
482	    url: "https://arxiv.org/abs/2603.10392"
483	    category: "cp_robotics"
484	    verified: true
485	    relevance: "Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control."
486	    must_cite: false
487	    relation: "background"
488	
489	  - bibtex_key: "safediffcon2025"
490	    title: "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control"
491	    authors: "Not specified"
492	    year: 2025
493	    venue: "ICML 2025, arXiv:2502.02205"
494	    url: "https://arxiv.org/abs/2502.02205"
495	    category: "cp_foundation"
496	    verified: true
497	    relevance: "SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach."
498	    must_cite: false
499	    relation: "background"
500	
501	  - bibtex_key: "afil2026"
502	    title: "Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models"
503	    authors: "Not specified"
504	    year: 2026
505	    venue: "arXiv:2605.08434"
506	    url: "https://arxiv.org/abs/2605.08434"
507	    category: "vla_robustness_training"
508	    verified: true
509	    relevance: "AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction."
510	    must_cite: false
511	    relation: "complementary"
512	
513	  - bibtex_key: "valle2025vla_uq_metrics"
514	    title: "Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots"
515	    authors: "Valle et al."
516	    year: 2025
517	    venue: "arXiv:2507.17049"
518	    url: "https://arxiv.org/abs/2507.17049"
519	    category: "uq_vla"
520	    verified: true
521	    relevance: "Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against."
522	    must_cite: false
523	    relation: "complementary"
524	
525	  - bibtex_key: "diffusionvla2024"
526	    title: "Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning"
527	    authors: "Wen et al."
528	    year: 2024
529	    venue: "ICML 2025, arXiv:2412.03293"
530	    url: "https://arxiv.org/abs/2412.03293"
531	    category: "vla_foundation"
532	    verified: true
533	    relevance: "Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around."
534	    must_cite: false
535	    relation: "background"
536	
537	  # ===== Correction Magnitude Control literature (added 2026-05-14) =====
538	
539	  - bibtex_key: "silver2018residual"
540	    title: "Residual Policy Learning"
541	    authors: "Silver et al."
542	    year: 2018
543	    venue: "RSS 2018"
544	    url: "https://arxiv.org/abs/1812.06298"
545	    category: "residual_policy"
546	    verified: true
547	    relevance: "First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon."
548	    must_cite: true
549	    relation: "background"
550	
551	  - bibtex_key: "johannink2019residual"
552	    title: "Residual Reinforcement Learning for Robot Manipulator Control"
553	    authors: "Johannink et al."
554	    year: 2019
555	    venue: "ICRA 2019"
556	    url: "https://arxiv.org/abs/1812.03201"
557	    category: "residual_policy"
558	    verified: true
559	    relevance: "Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability."
560	    must_cite: false
561	    relation: "method-component"
562	
563	  - bibtex_key: "jiang2024transic"
564	    title: "TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning"
565	    authors: "Jiang et al."
566	    year: 2024
567	    venue: "CoRL 2024"
568	    url: "https://arxiv.org/abs/2405.10315"
569	    category: "residual_policy"
570	    verified: true
571	    relevance: "Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism."
572	    must_cite: true
573	    relation: "direct-competitor"
574	
575	  - bibtex_key: "ankile2024resip"
576	    title: "ResiP: Residual Reinforcement Learning for Precise Assembly"
577	    authors: "Ankile et al."
578	    year: 2024
579	    venue: "CoRL Workshop 2024"
580	    url: ""
581	    category: "residual_policy"
582	    verified: false
583	    verification_note: "Workshop paper, no arXiv ID provided"
584	    relevance: "Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design."
585	    must_cite: false
586	    relation: "method-component"
587	
588	  - bibtex_key: "xiao2026pld"
589	    title: "PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning"
590	    authors: "Xiao et al."
591	    year: 2026
592	    venue: "ICLR 2026"
593	    url: "https://arxiv.org/abs/2511.00091"
594	    category: "residual_policy"
595	    verified: true
596	    relevance: "Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA."
597	    must_cite: true
598	    relation: "direct-competitor"
599	
600	  - bibtex_key: "pan2025drc"
601	    title: "DRC: Decaying Relative Correction for Policy Refinement"
602	    authors: "Pan et al."
603	    year: 2025
604	    venue: "arXiv:2503.15368"
605	    url: "https://arxiv.org/abs/2503.15368"
606	    category: "residual_policy"
607	    verified: true
608	    relevance: "Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds."
609	    must_cite: false
610	    relation: "method-component"
611	
612	  - bibtex_key: "ma2026dawn"
613	    title: "DAWN: Value Learning in Residual Reinforcement Learning"
614	    authors: "Ma et al."
615	    year: 2026
616	    venue: "arXiv:2602.10539"
617	    url: "https://arxiv.org/abs/2602.10539"
618	    category: "residual_policy"
619	    verified: true
620	    relevance: "Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design."
621	    must_cite: false
622	    relation: "background"
623	
624	  - bibtex_key: "vla_in_the_loop_2025"
625	    title: "VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models"
626	    authors: "Not specified"
627	    year: 2025
628	    venue: "arXiv 2025"
629	    url: ""
630	    category: "inference_correction"
631	    verified: false
632	    verification_note: "No arXiv ID provided, needs verification"
633	    relevance: "Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger."
634	    must_cite: false
635	    relation: "method-component"
636	
637	  - bibtex_key: "zhou2025acp_cbf"
638	    title: "Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning"
639	    authors: "Zhou et al."
640	    year: 2025
641	    venue: "ICRA 2025"
642	    url: "https://arxiv.org/abs/2503.17678"
643	    category: "cp_robotics"
644	    verified: true
645	    relevance: "Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism."
646	    must_cite: true
647	    relation: "method-component"
648	
649	  # ===== Literature gap papers (added 2026-05-15) =====
650	
651	  # --- Gap 1: Supervised (non-RL) residual correction ---
652	
653	  - bibtex_key: "cai2025cr_dagger"
654	    title: "Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections"
655	    authors: "Cai et al."
656	    year: 2025
657	    venue: "NeurIPS 2025"
658	    url: "https://arxiv.org/abs/2506.16685"
659	    category: "supervised_residual"
660	    verified: true
661	    relevance: "Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction."
662	    must_cite: false
663	    relation: "background"
664	
665	  - bibtex_key: "rac2025"
666	    title: "RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction"
667	    authors: "Not specified"
668	    year: 2025
669	    venue: "arXiv:2509.07953"
670	    url: "https://arxiv.org/abs/2509.07953"
671	    category: "supervised_residual"
672	    verified: true
673	    relevance: "Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices."
674	    must_cite: false
675	    relation: "background"
676	
677	  - bibtex_key: "xue2025reactive_diffusion"
678	    title: "Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation"
679	    authors: "Xue et al."
680	    year: 2025
681	    venue: "RSS 2025"
682	    url: "https://arxiv.org/abs/2503.02881"
683	    category: "supervised_residual"
684	    verified: true
685	    relevance: "Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction."
686	    must_cite: false
687	    relation: "background"
688	
689	  - bibtex_key: "ross2011dagger"
690	    title: "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning"
691	    authors: "Ross, Gordon & Bagnell"
692	    year: 2011
693	    venue: "AISTATS 2011"
694	    url: "https://arxiv.org/abs/1011.0686"
695	    category: "imitation_learning"
696	    verified: true
697	    relevance: "Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger."
698	    must_cite: true
699	    relation: "background"
700	
701	  # --- Gap 2: Uncertainty-conditioned negative results ---
702	
703	  - bibtex_key: "ovadia2019trust_uncertainty"
704	    title: "Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift"
705	    authors: "Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek"
706	    year: 2019
707	    venue: "NeurIPS 2019"
708	    url: "https://arxiv.org/abs/1906.02530"
709	    category: "uq_foundation"
710	    verified: true
711	    relevance: "Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal."
712	    must_cite: false
713	    relation: "background"
714	
715	  # --- Gap 3: Object vs spatial robustness taxonomy ---
716	
717	  - bibtex_key: "xu2025libero_pro"
718	    title: "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization"
719	    authors: "Xu et al."
720	    year: 2025
721	    venue: "arXiv:2510.03827"
722	    url: "https://arxiv.org/abs/2510.03827"
723	    category: "benchmark"
724	    verified: true
725	    relevance: "Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks."
726	    must_cite: false
727	    relation: "background"
728	
729	  - bibtex_key: "wang2024gendp"
730	    title: "GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy"
731	    authors: "Wang et al."
732	    year: 2024
733	    venue: "CoRL 2024"
734	    url: "https://arxiv.org/abs/2410.17488"
735	    category: "manipulation_generalization"
736	    verified: true
737	    relevance: "Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage."
738	    must_cite: false
739	    relation: "background"
740	
741	  - bibtex_key: "s2_diffusion_2025"
742	    title: "S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation"
743	    authors: "Not specified"
744	    year: 2025
745	    venue: "arXiv:2502.09389"
746	    url: "https://arxiv.org/abs/2502.09389"
747	    category: "manipulation_generalization"
748	    verified: true
749	    relevance: "Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning."
750	    must_cite: false
751	    relation: "background"
752	
753	  # --- Gap 4: Compounding error in action prediction ---
754	
755	  - bibtex_key: "laskey2017dart"
756	    title: "DART: Noise Injection for Robust Imitation Learning"
757	    authors: "Laskey, Lee, Fox, Dragan & Goldberg"
758	    year: 2017
759	    venue: "CoRL 2017"
760	    url: "https://arxiv.org/abs/1703.09327"
761	    category: "imitation_learning"
762	    verified: true
763	    relevance: "Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach."
764	    must_cite: false
765	    relation: "background"
766	
767	  - bibtex_key: "somalwar2025imperfect_models"
768	    title: "Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error"
769	    authors: "Somalwar et al."
770	    year: 2025
771	    venue: "arXiv:2504.01766"
772	    url: "https://arxiv.org/abs/2504.01766"
773	    category: "imitation_learning"
774	    verified: true
775	    relevance: "Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification)."
776	    must_cite: false
777	    relation: "background"
778	
779	  # --- Gap 5: Conformal prediction as feature extractor ---
780	
781	  - bibtex_key: "huang2023feature_cp"
782	    title: "Predictive Inference with Feature Conformal Prediction"
783	    authors: "Huang et al."
784	    year: 2023
785	    venue: "ICLR 2023"
786	    url: "https://openreview.net/forum?id=0uRm1YmFTu"
787	    category: "cp_foundation"
788	    verified: true
789	    relevance: "Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning."
790	    must_cite: false
791	    relation: "background"
792	
793	  - bibtex_key: "lekeufack2024conformal_decision"
794	    title: "Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions"
795	    authors: "Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik"
796	    year: 2024
797	    venue: "ICRA 2024"
798	    url: "https://arxiv.org/abs/2310.05921"
799	    category: "cp_foundation"
800	    verified: true
801	    relevance: "Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning."
802	    must_cite: false
803	    relation: "background"
804	
805	  - bibtex_key: "jin2023selection_prediction"
806	    title: "Selection by Prediction with Conformal p-values"
807	    authors: "Jin & Candes"
808	    year: 2023
809	    venue: "JMLR 2023"
810	    url: "https://arxiv.org/abs/2210.01408"
811	    category: "cp_foundation"
812	    verified: true
813	    relevance: "Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach."
814	    must_cite: false
815	    relation: "background"
816	
817	  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====
818	
819	  - bibtex_key: "sampson2024conformal_hyperrect"
820	    title: "Conformal Multi-Target Hyperrectangles"
821	    authors: "Sampson et al."
822	    year: 2024
823	    venue: "Statistical Analysis and Data Mining, arXiv:2406.04498"
824	    url: "https://arxiv.org/abs/2406.04498"
825	    category: "cp_foundation"
826	    verified: true
827	    relevance: "Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency."
828	    must_cite: false
829	    relation: "method-component"
830	
831	  - bibtex_key: "fang2026trace"
832	    title: "TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models"
833	    authors: "Fang et al."
834	    year: 2026
835	    venue: "arXiv:2605.07100"
836	    url: "https://arxiv.org/abs/2605.07100"
837	    category: "cp_foundation"
838	    verified: true
839	    relevance: "Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition."
840	    must_cite: false
841	    relation: "method-component"
842	
843	  - bibtex_key: "dodeja2025accel_residual_uq"
844	    title: "Accelerating Residual Reinforcement Learning with Uncertainty Estimation"
845	    authors: "Dodeja & Schmeckpeper"
846	    year: 2025
847	    venue: "IEEE RA-L, arXiv:2506.17564"
848	    url: "https://arxiv.org/abs/2506.17564"
849	    category: "residual_policy"
850	    verified: true
851	    relevance: "Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections."
852	    must_cite: false
853	    relation: "method-component"
854	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "4291daa2-ccdd-4643-b3e8-c75122bccbd2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
      "content": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\n\n  - bibtex_key: \"silver2018residual\"\n    title: \"Residual Policy Learning\"\n    authors: \"Silver et al.\"\n    year: 2018\n    venue: \"RSS 2018\"\n    url: \"https://arxiv.org/abs/1812.06298\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"johannink2019residual\"\n    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"\n    authors: \"Johannink et al.\"\n    year: 2019\n    venue: \"ICRA 2019\"\n    url: \"https://arxiv.org/abs/1812.03201\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"jiang2024transic\"\n    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"\n    authors: \"Jiang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2405.10315\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"ankile2024resip\"\n    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"\n    authors: \"Ankile et al.\"\n    year: 2024\n    venue: \"CoRL Workshop 2024\"\n    url: \"\"\n    category: \"residual_policy\"\n    verified: false\n    verification_note: \"Workshop paper, no arXiv ID provided\"\n    relevance: \"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"xiao2026pld\"\n    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"\n    authors: \"Xiao et al.\"\n    year: 2026\n    venue: \"ICLR 2026\"\n    url: \"https://arxiv.org/abs/2511.00091\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"pan2025drc\"\n    title: \"DRC: Decaying Relative Correction for Policy Refinement\"\n    authors: \"Pan et al.\"\n    year: 2025\n    venue: \"arXiv:2503.15368\"\n    url: \"https://arxiv.org/abs/2503.15368\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"ma2026dawn\"\n    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"\n    authors: \"Ma et al.\"\n    year: 2026\n    venue: \"arXiv:2602.10539\"\n    url: \"https://arxiv.org/abs/2602.10539\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"vla_in_the_loop_2025\"\n    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv 2025\"\n    url: \"\"\n    category: \"inference_correction\"\n    verified: false\n    verification_note: \"No arXiv ID provided, needs verification\"\n    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"zhou2025acp_cbf\"\n    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    year: 2025\n    venue: \"ICRA 2025\"\n    url: \"https://arxiv.org/abs/2503.17678\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"\n    must_cite: true\n    relation: \"method-component\"\n\n  # ===== Literature gap papers (added 2026-05-15) =====\n\n  # --- Gap 1: Supervised (non-RL) residual correction ---\n\n  - bibtex_key: \"cai2025cr_dagger\"\n    title: \"Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections\"\n    authors: \"Cai et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.16685\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"rac2025\"\n    title: \"RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.07953\"\n    url: \"https://arxiv.org/abs/2509.07953\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"xue2025reactive_diffusion\"\n    title: \"Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation\"\n    authors: \"Xue et al.\"\n    year: 2025\n    venue: \"RSS 2025\"\n    url: \"https://arxiv.org/abs/2503.02881\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"ross2011dagger\"\n    title: \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\"\n    authors: \"Ross, Gordon & Bagnell\"\n    year: 2011\n    venue: \"AISTATS 2011\"\n    url: \"https://arxiv.org/abs/1011.0686\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger.\"\n    must_cite: true\n    relation: \"background\"\n\n  # --- Gap 2: Uncertainty-conditioned negative results ---\n\n  - bibtex_key: \"ovadia2019trust_uncertainty\"\n    title: \"Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift\"\n    authors: \"Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1906.02530\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal.\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 3: Object vs spatial robustness taxonomy ---\n\n  - bibtex_key: \"xu2025libero_pro\"\n    title: \"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\"\n    authors: \"Xu et al.\"\n    year: 2025\n    venue: \"arXiv:2510.03827\"\n    url: \"https://arxiv.org/abs/2510.03827\"\n    category: \"benchmark\"\n    verified: true\n    relevance: \"Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"wang2024gendp\"\n    title: \"GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy\"\n    authors: \"Wang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2410.17488\"\n    category: \"manipulation_generalization\"\n    verified: true\n    relevance: \"Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"s2_diffusion_2025\"\n    title: \"S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2502.09389\"\n    url: \"https://arxiv.org/abs/2502.09389\"\n    category: \"manipulation_generalization\"\n    verified: true\n    relevance: \"Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning.\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 4: Compounding error in action prediction ---\n\n  - bibtex_key: \"laskey2017dart\"\n    title: \"DART: Noise Injection for Robust Imitation Learning\"\n    authors: \"Laskey, Lee, Fox, Dragan & Goldberg\"\n    year: 2017\n    venue: \"CoRL 2017\"\n    url: \"https://arxiv.org/abs/1703.09327\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"somalwar2025imperfect_models\"\n    title: \"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\"\n    authors: \"Somalwar et al.\"\n    year: 2025\n    venue: \"arXiv:2504.01766\"\n    url: \"https://arxiv.org/abs/2504.01766\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification).\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 5: Conformal prediction as feature extractor ---\n\n  - bibtex_key: \"huang2023feature_cp\"\n    title: \"Predictive Inference with Feature Conformal Prediction\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://openreview.net/forum?id=0uRm1YmFTu\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"lekeufack2024conformal_decision\"\n    title: \"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions\"\n    authors: \"Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    url: \"https://arxiv.org/abs/2310.05921\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"jin2023selection_prediction\"\n    title: \"Selection by Prediction with Conformal p-values\"\n    authors: \"Jin & Candes\"\n    year: 2023\n    venue: \"JMLR 2023\"\n    url: \"https://arxiv.org/abs/2210.01408\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====\n\n  - bibtex_key: \"sampson2024conformal_hyperrect\"\n    title: \"Conformal Multi-Target Hyperrectangles\"\n    authors: \"Sampson et al.\"\n    year: 2024\n    venue: \"Statistical Analysis and Data Mining, arXiv:2406.04498\"\n    url: \"https://arxiv.org/abs/2406.04498\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"fang2026trace\"\n    title: \"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models\"\n    authors: \"Fang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.07100\"\n    url: \"https://arxiv.org/abs/2605.07100\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"dodeja2025accel_residual_uq\"\n    title: \"Accelerating Residual Reinforcement Learning with Uncertainty Estimation\"\n    authors: \"Dodeja & Schmeckpeper\"\n    year: 2025\n    venue: \"IEEE RA-L, arXiv:2506.17564\"\n    url: \"https://arxiv.org/abs/2506.17564\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"\n",
      "numLines": 854,
      "startLine": 1,
      "totalLines": 854
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_018e5L8rpYWaHLC36h7D9xNU`</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('scaling test-time compute LLM best-of-N sampling 2024')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=10&fields=title,authors,year,venue,externalIds,url,abstract'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {', '.join(a['name'] for a in (p.get('authors') or [])[:5])}\\\")\n    print(f\\\"Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n    ids = p.get('externalIds', {})\n    print(f\\\"ArXiv: {ids.get('ArXiv', 'N/A')}\\\")\n    abs_text = (p.get('abstract') or '')[:200]\n    print(f\\\"Abstract: {abs_text}\\\")\n    print('---')\n\" 2>&1",
  "description": "Search Semantic Scholar for test-time compute scaling papers",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "56f2eb22-324e-4a22-9107-104eac5d4bfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnakyDqFbo4LpxkNECiDT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13495
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

_source line 8 · 2026-05-18T09:25:36.778Z_

<details><summary>↩ Tool result · reported error · `toolu_018e5L8rpYWaHLC36h7D9xNU`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    data = json.loads(urlopen(req).read())
                      ~~~~~~~^^^^^
  File "/usr/lib/python3.14/urllib/request.py", line 187, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/urllib/request.py", line 493, in open
    response = meth(req, response)
  File "/usr/lib/python3.14/urllib/request.py", line 602, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/usr/lib/python3.14/urllib/request.py", line 531, in error
    return self._call_chain(*args)
           ~~~~~~~~~~~~~~~~^^^^^^^
  File "/usr/lib/python3.14/urllib/request.py", line 464, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.14/urllib/request.py", line 611, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 429:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "50124475-1b9a-40ae-b629-31539c747185",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    data = json.loads(urlopen(req).read())\n                      ~~~~~~~^^^^^\n  File \"/usr/lib/python3.14/urllib/request.py\", line 187, in urlopen\n    return opener.open(url, data, timeout)\n           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/urllib/request.py\", line 493, in open\n    response = meth(req, response)\n  File \"/usr/lib/python3.14/urllib/request.py\", line 602, in http_response\n    response = self.parent.error(\n        'http', request, response, code, msg, hdrs)\n  File \"/usr/lib/python3.14/urllib/request.py\", line 531, in error\n    return self._call_chain(*args)\n           ~~~~~~~~~~~~~~~~^^^^^^^\n  File \"/usr/lib/python3.14/urllib/request.py\", line 464, in _call_chain\n    result = func(*args)\n  File \"/usr/lib/python3.14/urllib/request.py\", line 611, in http_error_default\n    raise HTTPError(req.full_url, code, msg, hdrs, fp)\nurllib.error.HTTPError: HTTP Error 429:"
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_01UpJboRJwvzyZFW3yjSBtP9`</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('Scaling LLM Test-Time Compute Optimally Snell 2024')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5&fields=title,authors,year,venue,externalIds,url,abstract'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {', '.join(a['name'] for a in (p.get('authors') or [])[:6])}\\\")\n    print(f\\\"Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n    ids = p.get('externalIds', {})\n    print(f\\\"ArXiv: {ids.get('ArXiv', 'N/A')}\\\")\n    abs_text = (p.get('abstract') or '')[:300]\n    print(f\\\"Abstract: {abs_text}\\\")\n    print('---')\n\" 2>&1",
  "description": "Search Semantic Scholar specifically for Snell et al. 2024",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "6bde52a4-99ba-4e68-aba3-97825ad344c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnakyDqFbo4LpxkNECiDT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13495
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

_source line 10 · 2026-05-18T09:25:39.290Z_

<details><summary>↩ Tool result · reported error · `toolu_01UpJboRJwvzyZFW3yjSBtP9`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "ddbcd81f-8f35-4af4-8179-5f18c733b621",
  "tool_use_result": "Cancelled: parallel tool call Bash(python3 -c \"\nfrom urllib.request import …) errored"
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_018EWzydiYyPwkbtC9B1BCtr`</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('best-of-N sampling reward model language model generation 2023 2024')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=10&fields=title,authors,year,venue,externalIds,url,abstract'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {', '.join(a['name'] for a in (p.get('authors') or [])[:5])}\\\")\n    print(f\\\"Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n    ids = p.get('externalIds', {})\n    print(f\\\"ArXiv: {ids.get('ArXiv', 'N/A')}\\\")\n    abs_text = (p.get('abstract') or '')[:200]\n    print(f\\\"Abstract: {abs_text}\\\")\n    print('---')\n\" 2>&1",
  "description": "Search for best-of-N sampling papers",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "927ebcd3-a1b6-4f0d-984b-aafe21dcc6ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnakyDqFbo4LpxkNECiDT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13495
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

_source line 12 · 2026-05-18T09:25:42.172Z_

<details><summary>↩ Tool result · reported error · `toolu_018EWzydiYyPwkbtC9B1BCtr`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "2553b0a2-d412-472a-8cda-2f11a2b1ce02",
  "tool_use_result": "Cancelled: parallel tool call Bash(python3 -c \"\nfrom urllib.request import …) errored"
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01NgXHncB8xK3DR9GZCE8Jtv`</summary>

```json
{
  "command": "python3 -c \"\nfrom urllib.request import urlopen, Request\nfrom urllib.parse import quote\nimport json\n\nquery = quote('inference-time compute scaling robotics embodied AI policy 2024')\nurl = f'https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=10&fields=title,authors,year,venue,externalIds,url,abstract'\nreq = Request(url, headers={'User-Agent': 'Mozilla/5.0'})\ndata = json.loads(urlopen(req).read())\nfor p in data.get('data', []):\n    print(f\\\"Title: {p['title']}\\\")\n    print(f\\\"Authors: {', '.join(a['name'] for a in (p.get('authors') or [])[:5])}\\\")\n    print(f\\\"Year: {p.get('year')}, Venue: {p.get('venue')}\\\")\n    ids = p.get('externalIds', {})\n    print(f\\\"ArXiv: {ids.get('ArXiv', 'N/A')}\\\")\n    abs_text = (p.get('abstract') or '')[:200]\n    print(f\\\"Abstract: {abs_text}\\\")\n    print('---')\n\" 2>&1",
  "description": "Search for inference-time compute in robotics/embodied AI",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "f0892697-e50a-4a1e-908b-0f5185e1f1a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AnakyDqFbo4LpxkNECiDT3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13495
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

_source line 14 · 2026-05-18T09:25:44.949Z_

<details><summary>↩ Tool result · reported error · `toolu_01NgXHncB8xK3DR9GZCE8Jtv`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
from urllib.request import …) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "ff770743-cce8-49aa-ae97-ebae4748f3aa",
  "tool_use_result": "Cancelled: parallel tool call Bash(python3 -c \"\nfrom urllib.request import …) errored"
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
S2 API hit rate limit (429). Let me fall back to WebSearch for all three searches, and also verify the chi2023diffusion_policy URL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "5876a5fd-20dd-4304-8a8e-b5ec4253c2bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014iGTncYct1KbNjyJAwvmC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16394,
      "cache_read_input_tokens": 25336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16394
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

_source line 16_

S2 API rate-limited. Falling back to WebSearch for all three targets.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "feeb29ff-279f-4878-8ff3-141f99af87d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014iGTncYct1KbNjyJAwvmC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16394,
      "cache_read_input_tokens": 25336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16394
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

_source line 17_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015PjBHoMSJnDxcR5t5TAoxY`</summary>

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
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "e3047ede-9d2b-4ba7-8ae1-3d59dc237c90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014iGTncYct1KbNjyJAwvmC6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16394,
      "cache_read_input_tokens": 25336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16394
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

_source line 18 · 2026-05-18T09:25:50.922Z_

<details><summary>↩ Tool result · `toolu_015PjBHoMSJnDxcR5t5TAoxY`</summary>

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
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "8faba202-5913-4155-83c3-61a4044eb29b",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Let me use WebSearch to find the papers, and WebFetch to verify the chi2023diffusion_policy URL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "b38a7481-55dd-4da1-982a-9e88cf2c16e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01298hb39J5ftcbH4CF66TcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 41730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VUoRUBy3cQPCShQpGTKh1a`</summary>

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
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "53a56794-d5d9-4776-ae61-866fbc0e518e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01298hb39J5ftcbH4CF66TcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 665,
      "cache_read_input_tokens": 41730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 665
      },
      "output_tokens": 26,
      "service_tier": "standard",
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

_source line 21 · 2026-05-18T09:25:54.320Z_

<details><summary>↩ Tool result · `toolu_01VUoRUBy3cQPCShQpGTKh1a`</summary>

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
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "24edd752-dcad-4830-8267-e305e296eea0",
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

_source line 22_

Running all searches and the URL verification in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "3189c15c-9cc3-41a4-8c56-bcdb235e32d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVzqmgqCPbxRMuLdduSufk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 42395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018wNZB9xDE7Asi86Ar2AGXc`</summary>

```json
{
  "query": "Snell \"Scaling LLM Test-Time Compute Optimally\" 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "cb913f0e-0c81-4e5b-aecd-9754c39dc138",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVzqmgqCPbxRMuLdduSufk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 42395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NEsSAxd2bxyQQcCCvRf7MM`</summary>

```json
{
  "query": "best-of-N sampling reward model LLM generation 2024 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "0a26447c-4a09-405c-adff-bbdad44ac066",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVzqmgqCPbxRMuLdduSufk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 42395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5ZTwuq5yjekFCJmaNmXpZ`</summary>

```json
{
  "query": "inference-time compute scaling robotics embodied AI policy 2024 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "f54b695e-fa40-4f24-9796-f0c1d58a79fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVzqmgqCPbxRMuLdduSufk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 42395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 26_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WCZdGqhuM4HzpGZpQjKsBG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2303.04137",
  "prompt": "Confirm this is the paper \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi et al. Return the title, authors, and year."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "bd710ef8-d401-49d6-b971-8ac4ce763430",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVzqmgqCPbxRMuLdduSufk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 42395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 27 · 2026-05-18T09:26:04.520Z_

<details><summary>↩ Tool result · `toolu_01WCZdGqhuM4HzpGZpQjKsBG`</summary>

```text
# Paper Confirmation

**Title:** "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"

**Authors:** Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song

**Year:** 2023 (submitted March 7, 2023; extended journal version last revised March 14, 2024)

This is confirmed to be the correct paper. The work presents a novel approach where "a robot's visuomotor policy" is represented "as a conditional denoising diffusion process," achieving significant performance improvements across multiple robot manipulation benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "b2e0554b-b627-40eb-9601-11d709ec181e",
  "tool_use_result": {
    "bytes": 47730,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Confirmation\n\n**Title:** \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n\n**Authors:** Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song\n\n**Year:** 2023 (submitted March 7, 2023; extended journal version last revised March 14, 2024)\n\nThis is confirmed to be the correct paper. The work presents a novel approach where \"a robot's visuomotor policy\" is represented \"as a conditional denoising diffusion process,\" achieving significant performance improvements across multiple robot manipulation benchmarks.",
    "durationMs": 3267,
    "url": "https://arxiv.org/abs/2303.04137"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T09:26:04.787Z_

<details><summary>↩ Tool result · `toolu_018wNZB9xDE7Asi86Ar2AGXc`</summary>

```text
Web search results for query: "Snell "Scaling LLM Test-Time Compute Optimally" 2024 arXiv"

Links: [{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/scaling-llm-test-time-compute-optimally-can-be-more-effective-than-scaling-model-parameters-19a0c9fb7c44"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"[2408.03314v1] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314v1"},{"title":"2024-8-7 Scaling LLM Test-Time Compute Optimally can","url":"https://arxiv.org/pdf/2408.03314"},{"title":"What is Test Time Compute? | CSA","url":"https://cloudsecurityalliance.org/blog/2024/12/13/test-time-compute"},{"title":"SCALING LLM TEST-TIME COMPUTE OPTIMALLY CAN ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf"},{"title":"Scaling Test-time Compute for LLM Agents","url":"https://arxiv.org/html/2506.12928v1"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, Charlie Snell+, arXiv'24 · Issue #1501 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1501"}]

I found the paper! Here are the search results for the Snell et al. 2024 paper on arXiv:

## Paper Details

The paper is titled "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" by Charlie Snell and 3 other authors, with arXiv paper number 2408.03314.

## Key Findings

The paper studies the scaling of inference-time computation in LLMs, focusing on how much an LLM can improve its performance on a challenging prompt when allowed to use a fixed amount of inference-time compute.

The authors find that the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt, which motivates applying a "compute-optimal" scaling strategy that allocates test-time compute adaptively per prompt.

Using this compute-optimal strategy, they can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, they find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.

The paper was submitted on August 6, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "be2a1901-7b30-431b-b020-4c0fdb0271e9",
  "tool_use_result": {
    "query": "Snell \"Scaling LLM Test-Time Compute Optimally\" 2024 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_0132Ftznq1QV2iCtVAUd9YH4",
        "content": [
          {
            "title": "[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
            "url": "https://arxiv.org/abs/2408.03314"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
            "url": "https://arxiv.org/html/2408.03314v1"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | by Eleventh Hour Enthusiast | Medium",
            "url": "https://medium.com/@EleventhHourEnthusiast/scaling-llm-test-time-compute-optimally-can-be-more-effective-than-scaling-model-parameters-19a0c9fb7c44"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4FWAwZtd2n"
          },
          {
            "title": "[2408.03314v1] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
            "url": "https://arxiv.org/abs/2408.03314v1"
          },
          {
            "title": "2024-8-7 Scaling LLM Test-Time Compute Optimally can",
            "url": "https://arxiv.org/pdf/2408.03314"
          },
          {
            "title": "What is Test Time Compute? | CSA",
            "url": "https://cloudsecurityalliance.org/blog/2024/12/13/test-time-compute"
          },
          {
            "title": "SCALING LLM TEST-TIME COMPUTE OPTIMALLY CAN ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf"
          },
          {
            "title": "Scaling Test-time Compute for LLM Agents",
            "url": "https://arxiv.org/html/2506.12928v1"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters, Charlie Snell+, arXiv'24 · Issue #1501 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/1501"
          }
        ]
      },
      "I found the paper! Here are the search results for the Snell et al. 2024 paper on arXiv:\n\n## Paper Details\n\nThe paper is titled \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\" by Charlie Snell and 3 other authors, with arXiv paper number 2408.03314.\n\n## Key Findings\n\nThe paper studies the scaling of inference-time computation in LLMs, focusing on how much an LLM can improve its performance on a challenging prompt when allowed to use a fixed amount of inference-time compute.\n\nThe authors find that the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt, which motivates applying a \"compute-optimal\" scaling strategy that allocates test-time compute adaptively per prompt.\n\nUsing this compute-optimal strategy, they can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, they find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.\n\nThe paper was submitted on August 6, 2024."
    ],
    "durationSeconds": 6.089320667
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-18T09:26:08.063Z_

<details><summary>↩ Tool result · `toolu_01NEsSAxd2bxyQQcCCvRf7MM`</summary>

```text
Web search results for query: "best-of-N sampling reward model LLM generation 2024 arXiv"

Links: [{"title":"[2502.12668] Evaluation of Best-of-N Sampling Strategies for Language Model Alignment","url":"https://arxiv.org/abs/2502.12668"},{"title":"Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better,","url":"https://arxiv.org/pdf/2410.02725"},{"title":"[2404.01054] Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment","url":"https://arxiv.org/abs/2404.01054"},{"title":"Reward Inside the Model: A Lightweight Hidden-State Reward Model for LLM’s Best-of-N sampling","url":"https://arxiv.org/html/2505.12225v1"},{"title":"Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling","url":"https://arxiv.org/html/2505.12225v3"},{"title":"Inference-Aware Fine-Tuning for Best-of-N Sampling in ...","url":"https://arxiv.org/pdf/2412.15287"},{"title":"Evaluation of Best-of-N Sampling Strategies for Language Model Alignment | OpenReview","url":"https://openreview.net/forum?id=H4S4ETc8c9"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/pdf/2502.18581"},{"title":"Published in Transactions on Machine Learning Research (11/2024)","url":"https://arxiv.org/pdf/2406.16838"},{"title":"[2505.12225] Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling","url":"https://arxiv.org/abs/2505.12225"}]

I found several relevant arXiv papers on best-of-N sampling with reward models for LLM generation from 2024 and recent 2025 papers. Here are the key findings:

## Key Papers on Best-of-N Sampling with Reward Models

### Recent Papers (2024-2025)

1. **Evaluation of Best-of-N Sampling Strategies for Language Model Alignment** (February 2025)
   - Best-of-N (BoN) sampling with a reward model has been shown to be an effective strategy for aligning Large Language Models (LLMs) with human preferences at the time of decoding.
   - BoN sampling is susceptible to a problem known as reward hacking.
   - The paper proposes Stochastic RBoN sampling (SRBoN) as a theoretically guaranteed approach to worst-case reward hacking problems.

2. **Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better** (October 2024)
   - Best-of-N (Snell et al., 2024) is a widely used test-time compute approach to improve the performance of LLMs. Specifically, given a prompt, N candidate responses from an LLM are scored using a reward model, and the highest-scoring response is filtered as the final response.

3. **Regularized Best-of-N Sampling with Minimum Bayes Risk Objective** (April 2024)
   - MBR-BoN, a variant of BoN that aims to mitigate reward hacking at inference time by incorporating the Minimum Bayes Risk (MBR) objective as a proximity regularization term.

4. **Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling** (January 2026)
   - Best-of-N sampling is a powerful method for improving Large Language Model (LLM) performance, but it is often limited by its dependence on massive, text-based reward models.
   - During generation, an LLM naturally emits internal signals that reflect its confidence of its answer and the quality of its reasoning. This "internal knowledge" is often captured in a linearly separable representations within the model's hidden states.

5. **Inference-Aware Fine-Tuning for Best-of-N Sampling** (December 2024)
   - To address the gap between how LLMs are trained and how they are used at inference time, inference-aware fine-tuning was developed. For example, I can be the BoN strategy, which samples multiple candidate responses, and selects the best using the score function of some verifier.

These papers collectively address key challenges in best-of-N sampling including reward hacking, computational efficiency, and the development of more robust selection strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "cb3887c5-7d18-48c9-86cb-e24335491a0c",
  "tool_use_result": {
    "query": "best-of-N sampling reward model LLM generation 2024 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LyoV7aahfsF1LB4rgqpASm",
        "content": [
          {
            "title": "[2502.12668] Evaluation of Best-of-N Sampling Strategies for Language Model Alignment",
            "url": "https://arxiv.org/abs/2502.12668"
          },
          {
            "title": "Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better,",
            "url": "https://arxiv.org/pdf/2410.02725"
          },
          {
            "title": "[2404.01054] Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for Language Model Alignment",
            "url": "https://arxiv.org/abs/2404.01054"
          },
          {
            "title": "Reward Inside the Model: A Lightweight Hidden-State Reward Model for LLM’s Best-of-N sampling",
            "url": "https://arxiv.org/html/2505.12225v1"
          },
          {
            "title": "Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling",
            "url": "https://arxiv.org/html/2505.12225v3"
          },
          {
            "title": "Inference-Aware Fine-Tuning for Best-of-N Sampling in ...",
            "url": "https://arxiv.org/pdf/2412.15287"
          },
          {
            "title": "Evaluation of Best-of-N Sampling Strategies for Language Model Alignment | OpenReview",
            "url": "https://openreview.net/forum?id=H4S4ETc8c9"
          },
          {
            "title": "Scalable Best-of-N Selection for Large Language Models via Self-Certainty",
            "url": "https://arxiv.org/pdf/2502.18581"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (11/2024)",
            "url": "https://arxiv.org/pdf/2406.16838"
          },
          {
            "title": "[2505.12225] Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling",
            "url": "https://arxiv.org/abs/2505.12225"
          }
        ]
      },
      "I found several relevant arXiv papers on best-of-N sampling with reward models for LLM generation from 2024 and recent 2025 papers. Here are the key findings:\n\n## Key Papers on Best-of-N Sampling with Reward Models\n\n### Recent Papers (2024-2025)\n\n1. **Evaluation of Best-of-N Sampling Strategies for Language Model Alignment** (February 2025)\n   - Best-of-N (BoN) sampling with a reward model has been shown to be an effective strategy for aligning Large Language Models (LLMs) with human preferences at the time of decoding.\n   - BoN sampling is susceptible to a problem known as reward hacking.\n   - The paper proposes Stochastic RBoN sampling (SRBoN) as a theoretically guaranteed approach to worst-case reward hacking problems.\n\n2. **Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better** (October 2024)\n   - Best-of-N (Snell et al., 2024) is a widely used test-time compute approach to improve the performance of LLMs. Specifically, given a prompt, N candidate responses from an LLM are scored using a reward model, and the highest-scoring response is filtered as the final response.\n\n3. **Regularized Best-of-N Sampling with Minimum Bayes Risk Objective** (April 2024)\n   - MBR-BoN, a variant of BoN that aims to mitigate reward hacking at inference time by incorporating the Minimum Bayes Risk (MBR) objective as a proximity regularization term.\n\n4. **Mining Intrinsic Rewards from LLM Hidden States for Efficient Best-of-N Sampling** (January 2026)\n   - Best-of-N sampling is a powerful method for improving Large Language Model (LLM) performance, but it is often limited by its dependence on massive, text-based reward models.\n   - During generation, an LLM naturally emits internal signals that reflect its confidence of its answer and the quality of its reasoning. This \"internal knowledge\" is often captured in a linearly separable representations within the model's hidden states.\n\n5. **Inference-Aware Fine-Tuning for Best-of-N Sampling** (December 2024)\n   - To address the gap between how LLMs are trained and how they are used at inference time, inference-aware fine-tuning was developed. For example, I can be the BoN strategy, which samples multiple candidate responses, and selects the best using the score function of some verifier.\n\nThese papers collectively address key challenges in best-of-N sampling including reward hacking, computational efficiency, and the development of more robust selection strategies."
    ],
    "durationSeconds": 8.889989634999997
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T09:26:10.751Z_

<details><summary>↩ Tool result · `toolu_01B5ZTwuq5yjekFCJmaNmXpZ`</summary>

```text
Web search results for query: "inference-time compute scaling robotics embodied AI policy 2024 2025 arXiv"

Links: [{"title":"arXiv:2507.02076v1 [cs.AI] 2 Jul 2025","url":"https://arxiv.org/pdf/2507.02076"},{"title":"Embodied AI: Emerging Risks and Opportunities for Policy Action","url":"https://arxiv.org/html/2509.00117"},{"title":"Robotic computing system and embodied AI evolution: an algorithm-hardware co-design perspective","url":"https://www.jos.ac.cn/en/article/doi/10.1088/1674-4926/25020034"},{"title":"Inference-Time Scaling | Introl Blog","url":"https://introl.com/blog/inference-time-scaling-research-reasoning-models-december-2025"},{"title":"Embodied AI: From LLMs to World Models","url":"https://arxiv.org/html/2509.20021v1"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"},{"title":"Inference-Time Scaling for Complex Tasks: Where We Stand and What Lies Ahead","url":"https://arxiv.org/html/2504.00294v1"},{"title":"A SURVEY OF EMBODIED ARTIFICIAL INTELLIGENCE DATA ENGINEERING","url":"https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf"},{"title":"Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction","url":"https://arxiv.org/html/2508.05294v4"},{"title":"DATA SCALING LAWS IN IMITATION LEARNING FOR ...","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/88b7b2c896506daabc8d3fd587055167-Paper-Conference.pdf"}]

I've completed the web search for your query on inference-time compute scaling in robotics and embodied AI. Here are the key findings:

## Recent Research on Inference-Time Compute Scaling in Embodied AI (2024-2025)

**Test-Time Compute Methods:**
A growing body of research has focused on test-time compute (TTC) methods, which aim to improve LLM reasoning by allocating additional computation at inference time. Inference-time scaling improves performance but varies by domain and task complexity.

**Embodied AI Progress:**
Recent breakthroughs in AI capabilities—particularly those related to Large Language Models (LLMs) and Large Multimodal Models (LMMs)—have catalyzed unprecedented progress in EAI systems' ability to navigate and act in the physical world. The rise of Vision-Language-Action Models (VLAs)—which cast control as next-token prediction over interleaved visual and linguistic tokens—opens the possibility for a "ChatGPT moment" for robotics.

**Computational Efficiency Challenges:**
Embodied AI tasks encounter significant challenges in computational efficiency, particularly in real-time applications. Although models such as Transformers and Diffusion networks exhibit strong performance, their high inference costs conflict with the real-time control demands of robotic systems.

**Algorithm-Hardware Co-Design:**
Algorithm-hardware co-design has emerged as the primary methodology, which analyzes algorithm behaviors on hardware to identify common computational properties. These properties can motivate algorithm optimization to reduce computational complexity and hardware innovation from architecture to circuit for high performance and high energy efficiency.

**Latency in Embodied AI Inference:**
The challenges of joint MLLM-WM-driven embodied AI architecture include 1) real-time synchronization between MLLMs' high-latency semantic processing and WMs' physics-based representation, often leading to delayed responses in dynamic environments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "81af39a2-5f9b-4998-a1d8-42ab342a0010",
  "tool_use_result": {
    "query": "inference-time compute scaling robotics embodied AI policy 2024 2025 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_012ZmNpJixSai5jQzkHKjU5t",
        "content": [
          {
            "title": "arXiv:2507.02076v1 [cs.AI] 2 Jul 2025",
            "url": "https://arxiv.org/pdf/2507.02076"
          },
          {
            "title": "Embodied AI: Emerging Risks and Opportunities for Policy Action",
            "url": "https://arxiv.org/html/2509.00117"
          },
          {
            "title": "Robotic computing system and embodied AI evolution: an algorithm-hardware co-design perspective",
            "url": "https://www.jos.ac.cn/en/article/doi/10.1088/1674-4926/25020034"
          },
          {
            "title": "Inference-Time Scaling | Introl Blog",
            "url": "https://introl.com/blog/inference-time-scaling-research-reasoning-models-december-2025"
          },
          {
            "title": "Embodied AI: From LLMs to World Models",
            "url": "https://arxiv.org/html/2509.20021v1"
          },
          {
            "title": "A Comprehensive Survey on World Models for Embodied AI",
            "url": "https://arxiv.org/html/2510.16732v1"
          },
          {
            "title": "Inference-Time Scaling for Complex Tasks: Where We Stand and What Lies Ahead",
            "url": "https://arxiv.org/html/2504.00294v1"
          },
          {
            "title": "A SURVEY OF EMBODIED ARTIFICIAL INTELLIGENCE DATA ENGINEERING",
            "url": "https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf"
          },
          {
            "title": "Towards Embodied Agentic AI: Review and Classification of LLM- and VLM-Driven Robot Autonomy and Interaction",
            "url": "https://arxiv.org/html/2508.05294v4"
          },
          {
            "title": "DATA SCALING LAWS IN IMITATION LEARNING FOR ...",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/88b7b2c896506daabc8d3fd587055167-Paper-Conference.pdf"
          }
        ]
      },
      "I've completed the web search for your query on inference-time compute scaling in robotics and embodied AI. Here are the key findings:\n\n## Recent Research on Inference-Time Compute Scaling in Embodied AI (2024-2025)\n\n**Test-Time Compute Methods:**\nA growing body of research has focused on test-time compute (TTC) methods, which aim to improve LLM reasoning by allocating additional computation at inference time. Inference-time scaling improves performance but varies by domain and task complexity.\n\n**Embodied AI Progress:**\nRecent breakthroughs in AI capabilities—particularly those related to Large Language Models (LLMs) and Large Multimodal Models (LMMs)—have catalyzed unprecedented progress in EAI systems' ability to navigate and act in the physical world. The rise of Vision-Language-Action Models (VLAs)—which cast control as next-token prediction over interleaved visual and linguistic tokens—opens the possibility for a \"ChatGPT moment\" for robotics.\n\n**Computational Efficiency Challenges:**\nEmbodied AI tasks encounter significant challenges in computational efficiency, particularly in real-time applications. Although models such as Transformers and Diffusion networks exhibit strong performance, their high inference costs conflict with the real-time control demands of robotic systems.\n\n**Algorithm-Hardware Co-Design:**\nAlgorithm-hardware co-design has emerged as the primary methodology, which analyzes algorithm behaviors on hardware to identify common computational properties. These properties can motivate algorithm optimization to reduce computational complexity and hardware innovation from architecture to circuit for high performance and high energy efficiency.\n\n**Latency in Embodied AI Inference:**\nThe challenges of joint MLLM-WM-driven embodied AI architecture include 1) real-time synchronization between MLLMs' high-latency semantic processing and WMs' physics-based representation, often leading to delayed responses in dynamic environments."
    ],
    "durationSeconds": 10.608645425000002
  }
}
```

</details>

---

### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Good. I found:

1. **Snell et al. 2024** — "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" — arXiv:2408.03314. Authors: Charlie Snell et al. Let me get the full author list.

2. **Best-of-N sampling** — Several papers found. The most relevant foundational one seems to be "Evaluation of Best-of-N Sampling Strategies for Language Model Alignment" (2502.12668) or I could look for the more canonical best-of-N paper. 

Now I'm thinking about which papers best illustrate the K-value scaling pattern the user mentioned. Since Snell et al. already covers best-of-N as a baseline, I should look for something that specifically examines the monotonic improvement curve or adaptive compute allocation. I'm seeing "Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better" which discusses when best-of-N sampling becomes worthwhile.

For the robotics side, I notice the user already has several inference-time compute papers mapped—test-time RL for VLAs, inference-time policy steering, and self-correcting VLAs. What's missing is a paper that specifically studies the scaling behavior of generating multiple samples and selecting among them in the robotics domain. Let me search for something more targeted there. For best-of-N, I'm thinking Stiennon et al. 2020 on summarization with reward models or Nakano et al. 2021's WebGPT would be solid foundational references, though I need to find something more directly addressing the scaling laws of best-of-N sampling. The key is connecting Snell et al.'s test-time compute framework to how best-of-N behaves across different K values, and then finding a robotics paper that applies this inference-time scaling to manipulation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "1da09d04-f7ed-43c1-b113-536a9f0fe651",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvMDZXDgZFv79XkBECQBNH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3491,
      "cache_read_input_tokens": 43040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3491
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

Found Snell et al. and confirmed `chi2023diffusion_policy` URL is valid. Now searching for more specific papers on best-of-N scaling and robotics test-time compute.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "5df407c2-a66d-4af1-889c-6dddc7e29fc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvMDZXDgZFv79XkBECQBNH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3491,
      "cache_read_input_tokens": 43040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3491
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BQmHURJ9GXF9D5AgqA1xNZ`</summary>

```json
{
  "url": "https://arxiv.org/abs/2408.03314",
  "prompt": "Extract the full author list for this paper. Return all author names."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "cb68379b-9763-43c2-a91a-7990408cbe9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvMDZXDgZFv79XkBECQBNH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3491,
      "cache_read_input_tokens": 43040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3491
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013vNiuWj78wTNq8EQsGaB8U`</summary>

```json
{
  "query": "\"test-time compute\" scaling robot manipulation policy best-of-N sampling 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "903023bf-13ab-46f5-9785-44736cf14502",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvMDZXDgZFv79XkBECQBNH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3491,
      "cache_read_input_tokens": 43040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3491
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WAabrwWBDSxHoeVctuDDFP`</summary>

```json
{
  "query": "Gui Zhong \"inference time scaling\" robot embodied 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "af90dd12-0774-460c-a6fa-d4bc0f774fb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KvMDZXDgZFv79XkBECQBNH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 195,
      "cache_creation_input_tokens": 3491,
      "cache_read_input_tokens": 43040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3491
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

_source line 36 · 2026-05-18T09:26:37.577Z_

<details><summary>↩ Tool result · `toolu_01BQmHURJ9GXF9D5AgqA1xNZ`</summary>

```text
# Full Author List

Based on the paper header, the complete author list is:

1. Charlie Snell
2. Jaehoon Lee
3. Kelvin Xu
4. Aviral Kumar

These four researchers authored the paper "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters," submitted to arXiv on August 6, 2024.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "76e04edf-a23b-45a8-b680-a53cfd162b48",
  "tool_use_result": {
    "bytes": 48991,
    "code": 200,
    "codeText": "OK",
    "result": "# Full Author List\n\nBased on the paper header, the complete author list is:\n\n1. Charlie Snell\n2. Jaehoon Lee\n3. Kelvin Xu\n4. Aviral Kumar\n\nThese four researchers authored the paper \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters,\" submitted to arXiv on August 6, 2024.",
    "durationMs": 1917,
    "url": "https://arxiv.org/abs/2408.03314"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-18T09:26:43.737Z_

<details><summary>↩ Tool result · `toolu_01WAabrwWBDSxHoeVctuDDFP`</summary>

```text
Web search results for query: "Gui Zhong "inference time scaling" robot embodied 2025 arXiv"

Links: [{"title":"Learning Primitive Embodied World Models: Towards Scalable Robotic Learning","url":"https://arxiv.org/html/2508.20840v2"},{"title":"A SURVEY OF EMBODIED ARTIFICIAL INTELLIGENCE DATA ENGINEERING","url":"https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf"},{"title":"Towards Embodiment Scaling Laws in Robot Locomotion","url":"https://arxiv.org/html/2505.05753v1"},{"title":"A Comprehensive Survey on World Models for Embodied AI","url":"https://arxiv.org/html/2510.16732v1"},{"title":"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10975"},{"title":"A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗","url":"https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"},{"title":"GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).","url":"https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"},{"title":"MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment","url":"https://arxiv.org/html/2512.06628v2"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=1500&show=2000"},{"title":"GitHub - HCPLab-SYSU/Embodied_AI_Paper_List: [Embodied-AI-Survey-2025] Paper List and Resource Repository for Embodied AI · GitHub","url":"https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"}]

Based on the search results, I found relevant information about inference time scaling and embodied robotics research from 2025 arXiv papers, though I didn't find a specific paper by "Gui Zhong" with that exact title combination.

However, the search did reveal several highly relevant 2025 arXiv papers on related topics:

1. **Inference Time Scaling in Embodied AI**: Test-time scaling has shown potential in LLMs and VLMs, and some embodied approaches adopt a fast-slow-thinking design that separates a deliberative high-level 'brain' from a low-latency 'cerebellum' controller, enabling planning-execution decoupling for more challenging tasks.

2. **Inference Optimization for Robotics**: One approach performs only 4 denoising steps per chunk (with 4 frames), enabling low-latency inference, and achieves real-time on-the-fly prediction at 12 FPS on standard hardware, making it suitable for closed-loop robotic control.

3. **Robot Learning Framework**: MIND-V is described as a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation.

If you're looking for a specific paper by Gui Zhong on inference time scaling for embodied robots, you might want to check the arXiv directly or provide additional details about the paper's abstract or content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "370428d7-2603-4d55-9ed1-8a6caf93171f",
  "tool_use_result": {
    "query": "Gui Zhong \"inference time scaling\" robot embodied 2025 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TuNcB6Zb4hRsYyDKTEPUiS",
        "content": [
          {
            "title": "Learning Primitive Embodied World Models: Towards Scalable Robotic Learning",
            "url": "https://arxiv.org/html/2508.20840v2"
          },
          {
            "title": "A SURVEY OF EMBODIED ARTIFICIAL INTELLIGENCE DATA ENGINEERING",
            "url": "https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf"
          },
          {
            "title": "Towards Embodiment Scaling Laws in Robot Locomotion",
            "url": "https://arxiv.org/html/2505.05753v1"
          },
          {
            "title": "A Comprehensive Survey on World Models for Embodied AI",
            "url": "https://arxiv.org/html/2510.16732v1"
          },
          {
            "title": "RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2510.10975"
          },
          {
            "title": "A Survey of Embodied World Models Yu Shang1 Yinzhou Tang1∗ Xin Zhang1∗",
            "url": "https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf"
          },
          {
            "title": "GitHub - Songwxuan/Embodied-AI-Paper-TopConf: [Actively Maintained🔥] A list of Embodied AI papers accepted by top conferences (ICLR, NeurIPS, ICML, RSS, CoRL, ICRA, IROS, CVPR, ICCV, ECCV).",
            "url": "https://github.com/Songwxuan/Embodied-AI-Paper-TopConf"
          },
          {
            "title": "MIND-V: Hierarchical World Model for Long-Horizon Robotic Manipulation with RL-based Physical Alignment",
            "url": "https://arxiv.org/html/2512.06628v2"
          },
          {
            "title": "Artificial Intelligence Jun 2025",
            "url": "https://www.arxiv.org/list/cs.AI/2025-06?skip=1500&show=2000"
          },
          {
            "title": "GitHub - HCPLab-SYSU/Embodied_AI_Paper_List: [Embodied-AI-Survey-2025] Paper List and Resource Repository for Embodied AI · GitHub",
            "url": "https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"
          }
        ]
      },
      "Based on the search results, I found relevant information about inference time scaling and embodied robotics research from 2025 arXiv papers, though I didn't find a specific paper by \"Gui Zhong\" with that exact title combination.\n\nHowever, the search did reveal several highly relevant 2025 arXiv papers on related topics:\n\n1. **Inference Time Scaling in Embodied AI**: Test-time scaling has shown potential in LLMs and VLMs, and some embodied approaches adopt a fast-slow-thinking design that separates a deliberative high-level 'brain' from a low-latency 'cerebellum' controller, enabling planning-execution decoupling for more challenging tasks.\n\n2. **Inference Optimization for Robotics**: One approach performs only 4 denoising steps per chunk (with 4 frames), enabling low-latency inference, and achieves real-time on-the-fly prediction at 12 FPS on standard hardware, making it suitable for closed-loop robotic control.\n\n3. **Robot Learning Framework**: MIND-V is described as a cognitive hierarchical world model designed to synthesize physically plausible and logically coherent videos of long-horizon robotic manipulation.\n\nIf you're looking for a specific paper by Gui Zhong on inference time scaling for embodied robots, you might want to check the arXiv directly or provide additional details about the paper's abstract or content."
    ],
    "durationSeconds": 6.951963078
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-18T09:26:43.747Z_

<details><summary>↩ Tool result · `toolu_013vNiuWj78wTNq8EQsGaB8U`</summary>

```text
Web search results for query: ""test-time compute" scaling robot manipulation policy best-of-N sampling 2024 2025"

Links: [{"title":"Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy | OpenReview","url":"https://openreview.net/forum?id=oDoPiR8wZJ"},{"title":"NeurIPS Poster Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy","url":"https://neurips.cc/virtual/2025/poster/116060"},{"title":"[2511.20906] Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy","url":"https://arxiv.org/abs/2511.20906"},{"title":"Scaling LLM Reasoning via Test-time Policy Evolution","url":"https://arxiv.org/pdf/2601.20379"},{"title":"Test-Time Scaling Law","url":"https://www.emergentmind.com/topics/test-time-scaling-law"},{"title":"(PDF) Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy","url":"https://www.researchgate.net/publication/398025928_Dynamic_Test-Time_Compute_Scaling_in_Control_Policy_Difficulty-Aware_Stochastic_Interpolant_Policy"},{"title":"Revisiting the Test-Time Scaling of o1-like Models","url":"https://aclanthology.org/2025.acl-long.232.pdf"},{"title":"(PDF) Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning","url":"https://www.researchgate.net/publication/392466011_Revisiting_Test-Time_Scaling_A_Survey_and_a_Diversity-Aware_Method_for_Efficient_Reasoning"},{"title":"Scaling LLM Test Time Compute","url":"https://www.jonvet.com/blog/llm-test-time-compute"},{"title":"A brief history of LLM Scaling Laws and what to expect in 2025","url":"https://www.jonvet.com/blog/llm-scaling-in-2025"}]

Here are the search results for your query about test-time compute scaling in robot manipulation policies with best-of-N sampling in 2024-2025:

## Key Findings:

**Test-Time Compute Scaling in Robot Manipulation:**

Diffusion- and flow-based policies deliver state-of-the-art performance on long-horizon robotic manipulation tasks, but these controllers employ a fixed inference budget at every control step regardless of task complexity, leading to computational inefficiency for simple subtasks while potentially underperforming on challenging ones.

**Difficulty-Aware Stochastic Interpolant Policy (DA-SIP):**

A recent framework called DA-SIP enables robotic controllers to adaptively adjust their integration horizon in real-time based on task difficulty, employing a difficulty classifier that analyzes RGB-D observations to dynamically select the step budget, the optimal solver variant, and ODE/SDE integration at each control cycle. This approach was presented at NeurIPS 2025 and reduces computation time by 2.6-4.4× while maintaining success rates.

**Test-Time Scaling in Robotics More Broadly:**

Test-time scaling laws apply across domains like large language models and robotics, showing that performance can be enhanced post-training through methods like best-of-N sampling or iterative refinement. In robotics and Vision Language Models, action error decreases exponentially with more sampled and verified actions, enabling robust out-of-distribution performance and efficient adaptation to new environments.

For robotics, action sampling and verification involves proposing N candidate actions at each decision step, optionally perturbing them, and then verifying using a learned model, with the best output selected.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "9eff810e-44c3-4495-b844-9f8a52ef98ff",
  "tool_use_result": {
    "query": "\"test-time compute\" scaling robot manipulation policy best-of-N sampling 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013qevQRYEfQ4xdhjbmhmjV9",
        "content": [
          {
            "title": "Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy | OpenReview",
            "url": "https://openreview.net/forum?id=oDoPiR8wZJ"
          },
          {
            "title": "NeurIPS Poster Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy",
            "url": "https://neurips.cc/virtual/2025/poster/116060"
          },
          {
            "title": "[2511.20906] Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy",
            "url": "https://arxiv.org/abs/2511.20906"
          },
          {
            "title": "Scaling LLM Reasoning via Test-time Policy Evolution",
            "url": "https://arxiv.org/pdf/2601.20379"
          },
          {
            "title": "Test-Time Scaling Law",
            "url": "https://www.emergentmind.com/topics/test-time-scaling-law"
          },
          {
            "title": "(PDF) Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy",
            "url": "https://www.researchgate.net/publication/398025928_Dynamic_Test-Time_Compute_Scaling_in_Control_Policy_Difficulty-Aware_Stochastic_Interpolant_Policy"
          },
          {
            "title": "Revisiting the Test-Time Scaling of o1-like Models",
            "url": "https://aclanthology.org/2025.acl-long.232.pdf"
          },
          {
            "title": "(PDF) Revisiting Test-Time Scaling: A Survey and a Diversity-Aware Method for Efficient Reasoning",
            "url": "https://www.researchgate.net/publication/392466011_Revisiting_Test-Time_Scaling_A_Survey_and_a_Diversity-Aware_Method_for_Efficient_Reasoning"
          },
          {
            "title": "Scaling LLM Test Time Compute",
            "url": "https://www.jonvet.com/blog/llm-test-time-compute"
          },
          {
            "title": "A brief history of LLM Scaling Laws and what to expect in 2025",
            "url": "https://www.jonvet.com/blog/llm-scaling-in-2025"
          }
        ]
      },
      "Here are the search results for your query about test-time compute scaling in robot manipulation policies with best-of-N sampling in 2024-2025:\n\n## Key Findings:\n\n**Test-Time Compute Scaling in Robot Manipulation:**\n\nDiffusion- and flow-based policies deliver state-of-the-art performance on long-horizon robotic manipulation tasks, but these controllers employ a fixed inference budget at every control step regardless of task complexity, leading to computational inefficiency for simple subtasks while potentially underperforming on challenging ones.\n\n**Difficulty-Aware Stochastic Interpolant Policy (DA-SIP):**\n\nA recent framework called DA-SIP enables robotic controllers to adaptively adjust their integration horizon in real-time based on task difficulty, employing a difficulty classifier that analyzes RGB-D observations to dynamically select the step budget, the optimal solver variant, and ODE/SDE integration at each control cycle. This approach was presented at NeurIPS 2025 and reduces computation time by 2.6-4.4× while maintaining success rates.\n\n**Test-Time Scaling in Robotics More Broadly:**\n\nTest-time scaling laws apply across domains like large language models and robotics, showing that performance can be enhanced post-training through methods like best-of-N sampling or iterative refinement. In robotics and Vision Language Models, action error decreases exponentially with more sampled and verified actions, enabling robust out-of-distribution performance and efficient adaptation to new environments.\n\nFor robotics, action sampling and verification involves proposing N candidate actions at each decision step, optionally perturbing them, and then verifying using a learned model, with the best output selected."
    ],
    "durationSeconds": 7.6150313610000016
  }
}
```

</details>

---

### Assistant

_source line 39_

<details><summary>Logged reasoning block</summary>

```text
I found a great paper: **DA-SIP: "Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy"** (arXiv:2511.20906, NeurIPS 2025). This is exactly what the user needs for inference-time compute scaling in robotics!

And I also found **RoVer: "Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model"** (arXiv:2510.10975) which uses a test-time verifier (reward model) for VLA, basically best-of-N for robotics.


Now I'm looking for the foundational best-of-N papers to give the user context. The key candidates are Stiennon et al. 2020 on learning from human feedback with reward models, Cobbe et al. 2021 on verifiers for math problems, and Lightman et al. 2024 on process reward models—I should pick whichever best matches what the user is actually looking for.

For showing the scaling behavior of best-of-N with monotonic improvement as K increases, Snell et al. 2024 already covers this as a baseline, and there's a specific evaluation paper on best-of-N strategies that might be more targeted. I'm leaning toward Snell et al. 2024 as the main test-time compute paper, DA-SIP for inference-time compute in robotics, and then finding the right canonical best-of-N paper to round out the three.

Actually, RoVer stands out because it's essentially best-of-N sampling with a reward model applied to vision-language models—which is almost exactly what ACR-VLA's K-sample approach does. Let me pull up the details on both DA-SIP and RoVer to see which fits better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "311987ed-c67e-4ec9-af08-39a5357cf19b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGqRQqYHj86x4JvsAEUAfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 46531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2482
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

_source line 40_

Found two excellent candidates: DA-SIP (test-time compute scaling in control policy) and RoVer (robot reward model as test-time verifier for VLA). Let me get details on both.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "bd4401b4-5dc5-442b-8f83-71f161778b0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGqRQqYHj86x4JvsAEUAfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 46531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2482
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VqiHSKBSnZfLrG1Sgqv3nj`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.20906",
  "prompt": "Extract: title, full author list, year, venue, and abstract. This paper is about dynamic test-time compute scaling in control policy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "36f93d52-4a61-4ae3-8792-595893dfa9bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGqRQqYHj86x4JvsAEUAfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 46531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2482
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HZd85UeakLKKxKKRnUprVb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.10975",
  "prompt": "Extract: title, full author list, year, venue, and abstract. This paper is about robot reward model as test-time verifier for VLA."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "c401fa9a-3c73-4b27-857a-ecb25aa979c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GGqRQqYHj86x4JvsAEUAfD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 976,
      "cache_creation_input_tokens": 2482,
      "cache_read_input_tokens": 46531,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2482
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

_source line 43 · 2026-05-18T09:27:02.452Z_

<details><summary>↩ Tool result · `toolu_01VqiHSKBSnZfLrG1Sgqv3nj`</summary>

```text
# Paper Details

**Title:** Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy

**Authors:** Inkook Chun, Seungjae Lee, Michael S. Albergo, Saining Xie, Eric Vanden-Eijnden

**Year:** 2025

**Venue:** arXiv (cs.RO - Robotics)

**Abstract:**

The paper presents DA-SIP, a framework enabling robotic controllers to dynamically modify their computational budgets during inference based on task difficulty. The method employs "a difficulty classifier that analyzes observations to dynamically select the step budget" and optimal solver configurations. Built on stochastic interpolant theory, the approach adapts both diffusion and flow-based policies. Experimental results across manipulation tasks demonstrate "2.6-4.4x reduction in total computation time while maintaining task success rates" comparable to fixed-budget approaches, enabling more efficient resource allocation for robotic control.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "f15d5e6a-7bca-4f18-8418-be633dc68dee",
  "tool_use_result": {
    "bytes": 47122,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Details\n\n**Title:** Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy\n\n**Authors:** Inkook Chun, Seungjae Lee, Michael S. Albergo, Saining Xie, Eric Vanden-Eijnden\n\n**Year:** 2025\n\n**Venue:** arXiv (cs.RO - Robotics)\n\n**Abstract:**\n\nThe paper presents DA-SIP, a framework enabling robotic controllers to dynamically modify their computational budgets during inference based on task difficulty. The method employs \"a difficulty classifier that analyzes observations to dynamically select the step budget\" and optimal solver configurations. Built on stochastic interpolant theory, the approach adapts both diffusion and flow-based policies. Experimental results across manipulation tasks demonstrate \"2.6-4.4x reduction in total computation time while maintaining task success rates\" comparable to fixed-budget approaches, enabling more efficient resource allocation for robotic control.",
    "durationMs": 3660,
    "url": "https://arxiv.org/abs/2511.20906"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-18T09:27:03.529Z_

<details><summary>↩ Tool result · `toolu_01HZd85UeakLKKxKKRnUprVb`</summary>

```text
# RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model

**Title:** RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model

**Authors:** Mingtong Dai, Lingbo Liu, Yongjie Bai, Yang Liu, Zhouxia Wang, Rui Su, Chunjie Chen, Liang Lin, Xinyu Wu

**Year:** 2025

**Venue:** arXiv (cs.RO - Robotics)

**Abstract:**

This research introduces an embodied test-time scaling framework that enhances Vision-Language-Action models without architectural modifications. The system uses a Robot Process Reward Model functioning as a verification mechanism. During inference, the framework generates multiple candidate actions, expands them through PRM-guided directions, and evaluates all candidates to select optimal actions for execution.

Key contributions include: a plug-and-play test-time scaling framework for VLAs; a process reward model providing "scalar process rewards and an action-space direction to guide exploration"; and an efficient sampling strategy leveraging shared perception caching. The approach essentially converts additional computational resources into improved decision-making, achieving test-time scaling benefits without extra training requirements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "b86f284d-31a3-4e0f-83dd-bd0ec930d7c3",
  "tool_use_result": {
    "bytes": 48371,
    "code": 200,
    "codeText": "OK",
    "result": "# RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model\n\n**Title:** RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model\n\n**Authors:** Mingtong Dai, Lingbo Liu, Yongjie Bai, Yang Liu, Zhouxia Wang, Rui Su, Chunjie Chen, Liang Lin, Xinyu Wu\n\n**Year:** 2025\n\n**Venue:** arXiv (cs.RO - Robotics)\n\n**Abstract:**\n\nThis research introduces an embodied test-time scaling framework that enhances Vision-Language-Action models without architectural modifications. The system uses a Robot Process Reward Model functioning as a verification mechanism. During inference, the framework generates multiple candidate actions, expands them through PRM-guided directions, and evaluates all candidates to select optimal actions for execution.\n\nKey contributions include: a plug-and-play test-time scaling framework for VLAs; a process reward model providing \"scalar process rewards and an action-space direction to guide exploration\"; and an efficient sampling strategy leveraging shared perception caching. The approach essentially converts additional computational resources into improved decision-making, achieving test-time scaling benefits without extra training requirements.",
    "durationMs": 4450,
    "url": "https://arxiv.org/abs/2510.10975"
  }
}
```

</details>

---

### Assistant

_source line 45_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Both papers are highly relevant:

1. **Snell et al. 2024** — "Scaling LLM Test-Time Compute Optimally..." — arXiv:2408.03314 — foundational test-time compute scaling paper
2. **RoVer (Dai et al. 2025)** — "RoVer: Robot Reward Model as Test-Time Verifier for VLA" — arXiv:2510.10975 — best-of-N sampling with reward model for VLAs in robotics! This is perfect because it's literally test-time compute scaling for VLAs.


3. **DA-SIP (Chun et al. 2025)** — "Dynamic Test-Time Compute Scaling in Control Policy" — arXiv:2511.20906 — inference-time compute scaling in robotics

Now I'm updating the literature map by adding these three papers, marking the diffusion policy entry as verified, and then checking the final count.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "6e5a1601-c0ba-4d9f-abd9-693c3082c364",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsvHnBSxx6zdksZKaPnXpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 49013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 46_

All three papers found. Now updating the literature map: adding 3 new entries and verifying `chi2023diffusion_policy`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "3ad40cae-7088-455d-868f-32b4ab219b83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsvHnBSxx6zdksZKaPnXpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 49013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_016AyXfVEHb9fgEUjhwAT3xk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
  "old_string": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true",
  "new_string": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "e8c8f561-cc61-4b18-81e2-0bac66e90a87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CsvHnBSxx6zdksZKaPnXpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 49013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
      },
      "output_tokens": 48,
      "service_tier": "standard",
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

_source line 48 · 2026-05-18T09:27:18.453Z_

<details><summary>↩ Tool result · `toolu_016AyXfVEHb9fgEUjhwAT3xk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "a39f78ce-3707-45e4-8609-fba53a1a5429",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
    "oldString": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true",
    "newString": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true",
    "originalFile": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\n\n  - bibtex_key: \"silver2018residual\"\n    title: \"Residual Policy Learning\"\n    authors: \"Silver et al.\"\n    year: 2018\n    venue: \"RSS 2018\"\n    url: \"https://arxiv.org/abs/1812.06298\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"johannink2019residual\"\n    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"\n    authors: \"Johannink et al.\"\n    year: 2019\n    venue: \"ICRA 2019\"\n    url: \"https://arxiv.org/abs/1812.03201\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"jiang2024transic\"\n    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"\n    authors: \"Jiang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2405.10315\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"ankile2024resip\"\n    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"\n    authors: \"Ankile et al.\"\n    year: 2024\n    venue: \"CoRL Workshop 2024\"\n    url: \"\"\n    category: \"residual_policy\"\n    verified: false\n    verification_note: \"Workshop paper, no arXiv ID provided\"\n    relevance: \"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"xiao2026pld\"\n    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"\n    authors: \"Xiao et al.\"\n    year: 2026\n    venue: \"ICLR 2026\"\n    url: \"https://arxiv.org/abs/2511.00091\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"pan2025drc\"\n    title: \"DRC: Decaying Relative Correction for Policy Refinement\"\n    authors: \"Pan et al.\"\n    year: 2025\n    venue: \"arXiv:2503.15368\"\n    url: \"https://arxiv.org/abs/2503.15368\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"ma2026dawn\"\n    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"\n    authors: \"Ma et al.\"\n    year: 2026\n    venue: \"arXiv:2602.10539\"\n    url: \"https://arxiv.org/abs/2602.10539\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"vla_in_the_loop_2025\"\n    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv 2025\"\n    url: \"\"\n    category: \"inference_correction\"\n    verified: false\n    verification_note: \"No arXiv ID provided, needs verification\"\n    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"zhou2025acp_cbf\"\n    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    year: 2025\n    venue: \"ICRA 2025\"\n    url: \"https://arxiv.org/abs/2503.17678\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"\n    must_cite: true\n    relation: \"method-component\"\n\n  # ===== Literature gap papers (added 2026-05-15) =====\n\n  # --- Gap 1: Supervised (non-RL) residual correction ---\n\n  - bibtex_key: \"cai2025cr_dagger\"\n    title: \"Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections\"\n    authors: \"Cai et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.16685\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"rac2025\"\n    title: \"RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.07953\"\n    url: \"https://arxiv.org/abs/2509.07953\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"xue2025reactive_diffusion\"\n    title: \"Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation\"\n    authors: \"Xue et al.\"\n    year: 2025\n    venue: \"RSS 2025\"\n    url: \"https://arxiv.org/abs/2503.02881\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"ross2011dagger\"\n    title: \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\"\n    authors: \"Ross, Gordon & Bagnell\"\n    year: 2011\n    venue: \"AISTATS 2011\"\n    url: \"https://arxiv.org/abs/1011.0686\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger.\"\n    must_cite: true\n    relation: \"background\"\n\n  # --- Gap 2: Uncertainty-conditioned negative results ---\n\n  - bibtex_key: \"ovadia2019trust_uncertainty\"\n    title: \"Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift\"\n    authors: \"Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1906.02530\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal.\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 3: Object vs spatial robustness taxonomy ---\n\n  - bibtex_key: \"xu2025libero_pro\"\n    title: \"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\"\n    authors: \"Xu et al.\"\n    year: 2025\n    venue: \"arXiv:2510.03827\"\n    url: \"https://arxiv.org/abs/2510.03827\"\n    category: \"benchmark\"\n    verified: true\n    relevance: \"Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"wang2024gendp\"\n    title: \"GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy\"\n    authors: \"Wang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2410.17488\"\n    category: \"manipulation_generalization\"\n    verified: true\n    relevance: \"Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"s2_diffusion_2025\"\n    title: \"S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2502.09389\"\n    url: \"https://arxiv.org/abs/2502.09389\"\n    category: \"manipulation_generalization\"\n    verified: true\n    relevance: \"Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning.\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 4: Compounding error in action prediction ---\n\n  - bibtex_key: \"laskey2017dart\"\n    title: \"DART: Noise Injection for Robust Imitation Learning\"\n    authors: \"Laskey, Lee, Fox, Dragan & Goldberg\"\n    year: 2017\n    venue: \"CoRL 2017\"\n    url: \"https://arxiv.org/abs/1703.09327\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"somalwar2025imperfect_models\"\n    title: \"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\"\n    authors: \"Somalwar et al.\"\n    year: 2025\n    venue: \"arXiv:2504.01766\"\n    url: \"https://arxiv.org/abs/2504.01766\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification).\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 5: Conformal prediction as feature extractor ---\n\n  - bibtex_key: \"huang2023feature_cp\"\n    title: \"Predictive Inference with Feature Conformal Prediction\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://openreview.net/forum?id=0uRm1YmFTu\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"lekeufack2024conformal_decision\"\n    title: \"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions\"\n    authors: \"Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    url: \"https://arxiv.org/abs/2310.05921\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"jin2023selection_prediction\"\n    title: \"Selection by Prediction with Conformal p-values\"\n    authors: \"Jin & Candes\"\n    year: 2023\n    venue: \"JMLR 2023\"\n    url: \"https://arxiv.org/abs/2210.01408\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====\n\n  - bibtex_key: \"sampson2024conformal_hyperrect\"\n    title: \"Conformal Multi-Target Hyperrectangles\"\n    authors: \"Sampson et al.\"\n    year: 2024\n    venue: \"Statistical Analysis and Data Mining, arXiv:2406.04498\"\n    url: \"https://arxiv.org/abs/2406.04498\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"fang2026trace\"\n    title: \"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models\"\n    authors: \"Fang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.07100\"\n    url: \"https://arxiv.org/abs/2605.07100\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"dodeja2025accel_residual_uq\"\n    title: \"Accelerating Residual Reinforcement Learning with Uncertainty Estimation\"\n    authors: \"Dodeja & Schmeckpeper\"\n    year: 2025\n    venue: \"IEEE RA-L, arXiv:2506.17564\"\n    url: \"https://arxiv.org/abs/2506.17564\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"\n",
    "structuredPatch": [
      {
        "oldStart": 347,
        "oldLines": 8,
        "newStart": 347,
        "newLines": 7,
        "lines": [
          "     venue: \"RSS 2023 / IJRR 2024\"",
          "     url: \"https://arxiv.org/abs/2303.04137\"",
          "     category: \"vla_foundation\"",
          "-    verified: false",
          "-    verification_note: \"Well-known paper, needs URL reachability confirmation\"",
          "+    verified: true",
          "     relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"",
          "     must_cite: true",
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

_source line 49_

<details open><summary>🔧 Tool call — Edit · `toolu_01LM5FVrS6MwxPTazSKgMSeZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
  "old_string": "    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"",
  "new_string": "    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  # ===== Inference-time compute scaling literature (added 2026-05-18) =====\n\n  - bibtex_key: \"snell2024scaling_ttc\"\n    title: \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\"\n    authors: \"Snell, Lee, Xu & Kumar\"\n    year: 2024\n    venue: \"ICLR 2025, arXiv:2408.03314\"\n    url: \"https://arxiv.org/abs/2408.03314\"\n    category: \"inference_time_compute\"\n    verified: true\n    relevance: \"Foundational test-time compute scaling paper showing adaptive compute allocation per prompt outperforms best-of-N by 4x. Establishes the paradigm that ACR-VLA's K-value scaling (K=1->5->10 monotonic improvement) instantiates for robot action generation.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"dai2025rover\"\n    title: \"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model\"\n    authors: \"Dai, Liu, Bai, Liu, Wang, Su, Chen, Lin & Wu\"\n    year: 2025\n    venue: \"arXiv:2510.10975\"\n    url: \"https://arxiv.org/abs/2510.10975\"\n    category: \"inference_time_compute\"\n    verified: true\n    relevance: \"Embodied test-time scaling framework for VLAs using a Process Reward Model to score and select among multiple candidate actions. Directly instantiates best-of-N sampling with reward-model verification for robot manipulation, closely related to ACR-VLA's multi-sample generation and conformal selection.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"chun2025dasip\"\n    title: \"Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy\"\n    authors: \"Chun, Lee, Albergo, Xie & Vanden-Eijnden\"\n    year: 2025\n    venue: \"NeurIPS 2025, arXiv:2511.20906\"\n    url: \"https://arxiv.org/abs/2511.20906\"\n    category: \"inference_time_compute\"\n    verified: true\n    relevance: \"Adaptive inference compute budget for diffusion/flow robot policies based on task difficulty. Demonstrates 2.6-4.4x compute reduction while maintaining success rates. Complementary perspective on test-time compute allocation: DA-SIP reduces compute for easy steps, while ACR-VLA increases samples for uncertain steps.\"\n    must_cite: false\n    relation: \"complementary\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "38362cbf-8072-4fb0-ba3d-f81ba367dda3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A4S1GtETv5w2u2GZBk417F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 897,
      "cache_read_input_tokens": 51415,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 897
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

_source line 50 · 2026-05-18T09:27:34.458Z_

<details><summary>↩ Tool result · `toolu_01LM5FVrS6MwxPTazSKgMSeZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "a5aa0bfd-aba8-47e1-adc1-8b9cae03c272",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
    "oldString": "    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"",
    "newString": "    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  # ===== Inference-time compute scaling literature (added 2026-05-18) =====\n\n  - bibtex_key: \"snell2024scaling_ttc\"\n    title: \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\"\n    authors: \"Snell, Lee, Xu & Kumar\"\n    year: 2024\n    venue: \"ICLR 2025, arXiv:2408.03314\"\n    url: \"https://arxiv.org/abs/2408.03314\"\n    category: \"inference_time_compute\"\n    verified: true\n    relevance: \"Foundational test-time compute scaling paper showing adaptive compute allocation per prompt outperforms best-of-N by 4x. Establishes the paradigm that ACR-VLA's K-value scaling (K=1->5->10 monotonic improvement) instantiates for robot action generation.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"dai2025rover\"\n    title: \"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model\"\n    authors: \"Dai, Liu, Bai, Liu, Wang, Su, Chen, Lin & Wu\"\n    year: 2025\n    venue: \"arXiv:2510.10975\"\n    url: \"https://arxiv.org/abs/2510.10975\"\n    category: \"inference_time_compute\"\n    verified: true\n    relevance: \"Embodied test-time scaling framework for VLAs using a Process Reward Model to score and select among multiple candidate actions. Directly instantiates best-of-N sampling with reward-model verification for robot manipulation, closely related to ACR-VLA's multi-sample generation and conformal selection.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"chun2025dasip\"\n    title: \"Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy\"\n    authors: \"Chun, Lee, Albergo, Xie & Vanden-Eijnden\"\n    year: 2025\n    venue: \"NeurIPS 2025, arXiv:2511.20906\"\n    url: \"https://arxiv.org/abs/2511.20906\"\n    category: \"inference_time_compute\"\n    verified: true\n    relevance: \"Adaptive inference compute budget for diffusion/flow robot policies based on task difficulty. Demonstrates 2.6-4.4x compute reduction while maintaining success rates. Complementary perspective on test-time compute allocation: DA-SIP reduces compute for easy steps, while ACR-VLA increases samples for uncertain steps.\"\n    must_cite: false\n    relation: \"complementary\"",
    "originalFile": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\n\n  - bibtex_key: \"silver2018residual\"\n    title: \"Residual Policy Learning\"\n    authors: \"Silver et al.\"\n    year: 2018\n    venue: \"RSS 2018\"\n    url: \"https://arxiv.org/abs/1812.06298\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"johannink2019residual\"\n    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"\n    authors: \"Johannink et al.\"\n    year: 2019\n    venue: \"ICRA 2019\"\n    url: \"https://arxiv.org/abs/1812.03201\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"jiang2024transic\"\n    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"\n    authors: \"Jiang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2405.10315\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"ankile2024resip\"\n    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"\n    authors: \"Ankile et al.\"\n    year: 2024\n    venue: \"CoRL Workshop 2024\"\n    url: \"\"\n    category: \"residual_policy\"\n    verified: false\n    verification_note: \"Workshop paper, no arXiv ID provided\"\n    relevance: \"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"xiao2026pld\"\n    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"\n    authors: \"Xiao et al.\"\n    year: 2026\n    venue: \"ICLR 2026\"\n    url: \"https://arxiv.org/abs/2511.00091\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"pan2025drc\"\n    title: \"DRC: Decaying Relative Correction for Policy Refinement\"\n    authors: \"Pan et al.\"\n    year: 2025\n    venue: \"arXiv:2503.15368\"\n    url: \"https://arxiv.org/abs/2503.15368\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"ma2026dawn\"\n    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"\n    authors: \"Ma et al.\"\n    year: 2026\n    venue: \"arXiv:2602.10539\"\n    url: \"https://arxiv.org/abs/2602.10539\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"vla_in_the_loop_2025\"\n    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv 2025\"\n    url: \"\"\n    category: \"inference_correction\"\n    verified: false\n    verification_note: \"No arXiv ID provided, needs verification\"\n    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"zhou2025acp_cbf\"\n    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    year: 2025\n    venue: \"ICRA 2025\"\n    url: \"https://arxiv.org/abs/2503.17678\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"\n    must_cite: true\n    relation: \"method-component\"\n\n  # ===== Literature gap papers (added 2026-05-15) =====\n\n  # --- Gap 1: Supervised (non-RL) residual correction ---\n\n  - bibtex_key: \"cai2025cr_dagger\"\n    title: \"Compliant Residual DAgger: Improving Real-World Contact-Rich Manipulation with Human Corrections\"\n    authors: \"Cai et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.16685\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Learns supervised residual corrections from human delta corrections via compliance control; no RL. Closest supervised residual paradigm to CRM's offline L2-trained correction.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"rac2025\"\n    title: \"RaC: Robot Learning for Long-Horizon Tasks by Scaling Recovery and Correction\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.07953\"\n    url: \"https://arxiv.org/abs/2509.07953\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Supervised fine-tuning on human intervention trajectories (recovery + correction). DAgger-style supervised correction without RL. Demonstrates supervised correction data suffices.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"xue2025reactive_diffusion\"\n    title: \"Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation\"\n    authors: \"Xue et al.\"\n    year: 2025\n    venue: \"RSS 2025\"\n    url: \"https://arxiv.org/abs/2503.02881\"\n    category: \"supervised_residual\"\n    verified: true\n    relevance: \"Two-level slow-fast architecture: slow diffusion policy + fast supervised correction module. Structural precedent for generate-then-correct pipeline with supervised (non-RL) correction.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"ross2011dagger\"\n    title: \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\"\n    authors: \"Ross, Gordon & Bagnell\"\n    year: 2011\n    venue: \"AISTATS 2011\"\n    url: \"https://arxiv.org/abs/1011.0686\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Classic DAgger algorithm proving O(T^2) compounding error for BC, reduced to O(T) via iterative expert corrections. Foundational supervised correction framework; CRM as single-round offline DAgger.\"\n    must_cite: true\n    relation: \"background\"\n\n  # --- Gap 2: Uncertainty-conditioned negative results ---\n\n  - bibtex_key: \"ovadia2019trust_uncertainty\"\n    title: \"Can You Trust Your Model's Uncertainty? Evaluating Predictive Uncertainty Under Dataset Shift\"\n    authors: \"Ovadia, Fertig, Ren, Nado, Sculley, Nowozin, Dillon, Lakshminarayanan & Snoek\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1906.02530\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Systematic evaluation showing UQ methods degrade under distribution shift; post-hoc calibration can make things worse. Supports our finding that CP features under OOD shift may carry corrupted signal.\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 3: Object vs spatial robustness taxonomy ---\n\n  - bibtex_key: \"xu2025libero_pro\"\n    title: \"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\"\n    authors: \"Xu et al.\"\n    year: 2025\n    venue: \"arXiv:2510.03827\"\n    url: \"https://arxiv.org/abs/2510.03827\"\n    category: \"benchmark\"\n    verified: true\n    relevance: \"Robustness evaluation across 4 perturbation dimensions. VLAs collapse to 0% under spatial perturbation due to spatial memorization. Explains why CRM helps object but not spatial tasks.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"wang2024gendp\"\n    title: \"GenDP: 3D Semantic Fields for Category-Level Generalizable Diffusion Policy\"\n    authors: \"Wang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2410.17488\"\n    category: \"manipulation_generalization\"\n    verified: true\n    relevance: \"Uses 3D semantic fields for category-level object generalization (20%->93%). Shows object generalization relies on semantic features available in observation embeddings, supporting CRM's obs_only advantage.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"s2_diffusion_2025\"\n    title: \"S^2-Diffusion: Generalizing from Instance-level to Category-level Skills in Robot Manipulation\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2502.09389\"\n    url: \"https://arxiv.org/abs/2502.09389\"\n    category: \"manipulation_generalization\"\n    verified: true\n    relevance: \"Spatial-Semantic Diffusion policy for instance-to-category transfer. Object category generalization via semantic abstraction (correctable at inference) vs spatial requiring re-planning.\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 4: Compounding error in action prediction ---\n\n  - bibtex_key: \"laskey2017dart\"\n    title: \"DART: Noise Injection for Robust Imitation Learning\"\n    authors: \"Laskey, Lee, Fox, Dragan & Goldberg\"\n    year: 2017\n    venue: \"CoRL 2017\"\n    url: \"https://arxiv.org/abs/1703.09327\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Injects optimized noise into demonstrations for compounding error robustness without online interaction. 3x faster than DAgger. Analogous to CRM's offline training approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"somalwar2025imperfect_models\"\n    title: \"Learning with Imperfect Models: When Multi-step Prediction Mitigates Compounding Error\"\n    authors: \"Somalwar et al.\"\n    year: 2025\n    venue: \"arXiv:2504.01766\"\n    url: \"https://arxiv.org/abs/2504.01766\"\n    category: \"imitation_learning\"\n    verified: true\n    relevance: \"Proves multi-step predictors reduce bias under model misspecification. Provides theoretical framework for when correction helps (correctable misspecification) vs hurts (new misspecification).\"\n    must_cite: false\n    relation: \"background\"\n\n  # --- Gap 5: Conformal prediction as feature extractor ---\n\n  - bibtex_key: \"huang2023feature_cp\"\n    title: \"Predictive Inference with Feature Conformal Prediction\"\n    authors: \"Huang et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://openreview.net/forum?id=0uRm1YmFTu\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Deploys CP in learned feature space (reverse direction from ACR-VLA). Uses surrogate features for nonconformity scores. Establishes conceptual bridge between CP and representation learning.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"lekeufack2024conformal_decision\"\n    title: \"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions\"\n    authors: \"Lekeufack, Angelopoulos, Bajcsy, Jordan & Malik\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    url: \"https://arxiv.org/abs/2310.05921\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses CP scores to calibrate decisions directly, not just prediction sets. Closest precedent for using CP beyond calibration; CP scores inform decision-making in robot planning.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"jin2023selection_prediction\"\n    title: \"Selection by Prediction with Conformal p-values\"\n    authors: \"Jin & Candes\"\n    year: 2023\n    venue: \"JMLR 2023\"\n    url: \"https://arxiv.org/abs/2210.01408\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses conformal p-values for downstream screening/selection with FDR control. CP scores as informative signals for downstream task, paralleling CRM's CP-as-features approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Robustness scan (added 2026-05-15) =====\n\n  - bibtex_key: \"sampson2024conformal_hyperrect\"\n    title: \"Conformal Multi-Target Hyperrectangles\"\n    authors: \"Sampson et al.\"\n    year: 2024\n    venue: \"Statistical Analysis and Data Mining, arXiv:2406.04498\"\n    url: \"https://arxiv.org/abs/2406.04498\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Studies per-dimension marginal coverage vs joint coverage in multi-target CP. Shows Bonferroni correction is overconservative and can produce imbalanced marginal coverage across dimensions. Directly explains perdof's failure mode: independently constructed per-DOF intervals lose inter-DOF coherence at high norm bounds, while balanced joint approaches maintain consistency.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"fang2026trace\"\n    title: \"TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching Models\"\n    authors: \"Fang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.07100\"\n    url: \"https://arxiv.org/abs/2605.07100\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Defines scalar nonconformity scores via transport alignment in flow matching models — measuring velocity-matching errors along generative trajectories. Avoids per-dimension decomposition entirely. Supports the obs_only thesis: a scalar score derived from generative dynamics (analogous to obs_only's observation-conditioned scalar correction) naturally preserves directional coherence, unlike per-DOF decomposition.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"dodeja2025accel_residual_uq\"\n    title: \"Accelerating Residual Reinforcement Learning with Uncertainty Estimation\"\n    authors: \"Dodeja & Schmeckpeper\"\n    year: 2025\n    venue: \"IEEE RA-L, arXiv:2506.17564\"\n    url: \"https://arxiv.org/abs/2506.17564\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"\n    must_cite: false\n    relation: \"method-component\"\n",
    "structuredPatch": [
      {
        "oldStart": 850,
        "oldLines": 3,
        "newStart": 850,
        "newLines": 41,
        "lines": [
          "     relevance: \"Uses base policy uncertainty estimates to focus residual RL exploration on low-confidence regions. Handles stochastic (diffusion-based) base policies. Connects uncertainty estimation to correction effectiveness — corrections guided by uncertainty outperform uniform-magnitude corrections.\"",
          "     must_cite: false",
          "     relation: \"method-component\"",
          "+",
          "+  # ===== Inference-time compute scaling literature (added 2026-05-18) =====",
          "+",
          "+  - bibtex_key: \"snell2024scaling_ttc\"",
          "+    title: \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\"",
          "+    authors: \"Snell, Lee, Xu & Kumar\"",
          "+    year: 2024",
          "+    venue: \"ICLR 2025, arXiv:2408.03314\"",
          "+    url: \"https://arxiv.org/abs/2408.03314\"",
          "+    category: \"inference_time_compute\"",
          "+    verified: true",
          "+    relevance: \"Foundational test-time compute scaling paper showing adaptive compute allocation per prompt outperforms best-of-N by 4x. Establishes the paradigm that ACR-VLA's K-value scaling (K=1->5->10 monotonic improvement) instantiates for robot action generation.\"",
          "+    must_cite: true",
          "+    relation: \"background\"",
          "+",
          "+  - bibtex_key: \"dai2025rover\"",
          "+    title: \"RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model\"",
          "+    authors: \"Dai, Liu, Bai, Liu, Wang, Su, Chen, Lin & Wu\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2510.10975\"",
          "+    url: \"https://arxiv.org/abs/2510.10975\"",
          "+    category: \"inference_time_compute\"",
          "+    verified: true",
          "+    relevance: \"Embodied test-time scaling framework for VLAs using a Process Reward Model to score and select among multiple candidate actions. Directly instantiates best-of-N sampling with reward-model verification for robot manipulation, closely related to ACR-VLA's multi-sample generation and conformal selection.\"",
          "+    must_cite: true",
          "+    relation: \"direct-competitor\"",
          "+",
          "+  - bibtex_key: \"chun2025dasip\"",
          "+    title: \"Dynamic Test-Time Compute Scaling in Control Policy: Difficulty-Aware Stochastic Interpolant Policy\"",
          "+    authors: \"Chun, Lee, Albergo, Xie & Vanden-Eijnden\"",
          "+    year: 2025",
          "+    venue: \"NeurIPS 2025, arXiv:2511.20906\"",
          "+    url: \"https://arxiv.org/abs/2511.20906\"",
          "+    category: \"inference_time_compute\"",
          "+    verified: true",
          "+    relevance: \"Adaptive inference compute budget for diffusion/flow robot policies based on task difficulty. Demonstrates 2.6-4.4x compute reduction while maintaining success rates. Complementary perspective on test-time compute allocation: DA-SIP reduces compute for easy steps, while ACR-VLA increases samples for uncertain steps.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\""
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

_source line 51_

Now verifying the count of `inference_time_compute` entries with `verified: true`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "085e1414-2a26-4c9e-9ec4-76cd162691bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01623iEyQAcC5x2J6ZK8ENQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 52312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 52_

<details open><summary>🔧 Tool call — Grep · `toolu_01Ub9qGB9oSEAie88EXDza4j`</summary>

```json
{
  "pattern": "category: \"inference_time_compute\"",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
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
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "5cb66903-8bb6-4c25-b253-9882b3427c7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01623iEyQAcC5x2J6ZK8ENQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 52312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1141
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

_source line 53 · 2026-05-18T09:27:40.229Z_

<details><summary>↩ Tool result · `toolu_01Ub9qGB9oSEAie88EXDza4j`</summary>

```text
862:    category: "inference_time_compute"
863-    verified: true
864-    relevance: "Foundational test-time compute scaling paper showing adaptive compute allocation per prompt outperforms best-of-N by 4x. Establishes the paradigm that ACR-VLA's K-value scaling (K=1->5->10 monotonic improvement) instantiates for robot action generation."
--
874:    category: "inference_time_compute"
875-    verified: true
876-    relevance: "Embodied test-time scaling framework for VLAs using a Process Reward Model to score and select among multiple candidate actions. Directly instantiates best-of-N sampling with reward-model verification for robot manipulation, closely related to ACR-VLA's multi-sample generation and conformal selection."
--
886:    category: "inference_time_compute"
887-    verified: true
888-    relevance: "Adaptive inference compute budget for diffusion/flow robot policies based on task difficulty. Demonstrates 2.6-4.4x compute reduction while maintaining success rates. Complementary perspective on test-time compute allocation: DA-SIP reduces compute for easy steps, while ACR-VLA increases samples for uncertain steps."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "e8bb7602-68a3-4604-a6dc-f9f4a0ad6aab",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "862:    category: \"inference_time_compute\"\n863-    verified: true\n864-    relevance: \"Foundational test-time compute scaling paper showing adaptive compute allocation per prompt outperforms best-of-N by 4x. Establishes the paradigm that ACR-VLA's K-value scaling (K=1->5->10 monotonic improvement) instantiates for robot action generation.\"\n--\n874:    category: \"inference_time_compute\"\n875-    verified: true\n876-    relevance: \"Embodied test-time scaling framework for VLAs using a Process Reward Model to score and select among multiple candidate actions. Directly instantiates best-of-N sampling with reward-model verification for robot manipulation, closely related to ACR-VLA's multi-sample generation and conformal selection.\"\n--\n886:    category: \"inference_time_compute\"\n887-    verified: true\n888-    relevance: \"Adaptive inference compute budget for diffusion/flow robot policies based on task difficulty. Demonstrates 2.6-4.4x compute reduction while maintaining success rates. Complementary perspective on test-time compute allocation: DA-SIP reduces compute for easy steps, while ACR-VLA increases samples for uncertain steps.\"",
    "numLines": 11
  }
}
```

</details>

---

### Assistant

_source line 54_

3 entries with `category: "inference_time_compute"` and `verified: true`. All tasks complete:

| # | Paper | arXiv | Category |
|---|-------|-------|----------|
| 1 | Snell et al. 2024 — "Scaling LLM Test-Time Compute Optimally..." | 2408.03314 | LLM test-time compute scaling (foundational) |
| 2 | Dai et al. 2025 — "RoVer: Robot Reward Model as Test-Time Verifier for VLA" | 2510.10975 | Best-of-N + reward model for VLAs |
| 3 | Chun et al. 2025 — "DA-SIP: Dynamic Test-Time Compute Scaling in Control Policy" | 2511.20906 | Adaptive inference compute in robot control |

Additionally: `chi2023diffusion_policy` verified — URL `https://arxiv.org/abs/2303.04137` confirmed accessible, `verified` set to `true`, `verification_note` removed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "uuid": "6293f4a8-e8e6-4d2a-bac0-bca65eeddb6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JLLsxBENZWebVQruRk9wBQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 53453,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 55_

3 entries with `category: "inference_time_compute"` and `verified: true`. All tasks complete:

| # | Paper | arXiv | Category |
|---|-------|-------|----------|
| 1 | Snell et al. 2024 — "Scaling LLM Test-Time Compute Optimally..." | 2408.03314 | LLM test-time compute scaling (foundational) |
| 2 | Dai et al. 2025 — "RoVer: Robot Reward Model as Test-Time Verifier for VLA" | 2510.10975 | Best-of-N + reward model for VLAs |
| 3 | Chun et al. 2025 — "DA-SIP: Dynamic Test-Time Compute Scaling in Control Policy" | 2511.20906 | Adaptive inference compute in robot control |

Additionally: `chi2023diffusion_policy` verified — URL `https://arxiv.org/abs/2303.04137` confirmed accessible, `verified` set to `true`, `verification_note` removed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 139860,
  "duration_api_ms": 172735,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "905784d4-78cc-44ea-ad4c-b8d41a8e5c0b",
  "total_cost_usd": 0.8275857500000002,
  "usage": {
    "input_tokens": 1185,
    "cache_creation_input_tokens": 42083,
    "cache_read_input_tokens": 417066,
    "output_tokens": 6546,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 42083,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 263,
        "cache_read_input_tokens": 53453,
        "cache_creation_input_tokens": 471,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 471
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 118194,
      "outputTokens": 3653,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.18645899999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1185,
      "outputTokens": 6546,
      "cacheReadInputTokens": 417066,
      "cacheCreationInputTokens": 42083,
      "webSearchRequests": 0,
      "costUSD": 0.6411267500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "088b9d75-937a-48fa-bba6-f0419f284204"
}
```

</details>

---
