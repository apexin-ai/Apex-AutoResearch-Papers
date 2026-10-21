# paper research lit vla efficiency

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_research_lit_vla_efficiency_20260518T015546.log`
- **Structured JSON:** [`95f4d543305cf450b243.json`](../../sessions/95/95f4d543305cf450b243.json)

## Before a recorded user message

37 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress",
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
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
  "uuid": "878e4e06-99d0-4fed-bc61-73dbbb861069",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779085200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "be257686-074f-45a4-b27b-c1ead689a5ab",
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the existing literature_map.yaml to understand its structure and find where to append new entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "edfc8440-95df-4bf1-923e-1950a72dcf34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4hMgDaCRvwqiJUxA8pbs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13614,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13614
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01WwWmjf9RMWTRUFLjUD81FA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "a4e4f1cf-eb4c-40ca-ad9f-c1b01f788915",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J4hMgDaCRvwqiJUxA8pbs8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13614,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13614
      },
      "output_tokens": 38,
      "service_tier": "standard",
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

_source line 6 · 2026-05-18T01:55:57.720Z_

<details><summary>↩ Tool result · `toolu_01WwWmjf9RMWTRUFLjUD81FA`</summary>

```text
1	# Literature Map — importance_margin_vla_compress
2	# Generated: 2026-05-17
3	# Citation budget: 35
4	
5	papers:
6	
7	  # ============================================================
8	  # Cluster: VLA Models (target: 6)
9	  # ============================================================
10	  - bibtex_key: shukor2025smolvla
11	    title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
12	    authors: "Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others"
13	    year: 2025
14	    venue: "arXiv preprint"
15	    arxiv_id: "2506.01844"
16	    category: "VLA Models"
17	    role: foundation
18	    verified: true
19	    key_finding: "450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64."
20	    pruning_stats: null
21	    notes: "Our experimental platform. SigLIP encoder produces 128 vision tokens."
22	
23	  - bibtex_key: kim2024openvla
24	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
25	    authors: "Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others"
26	    year: 2024
27	    venue: "CoRL 2024"
28	    arxiv_id: "2406.09246"
29	    category: "VLA Models"
30	    role: foundation
31	    verified: true
32	    key_finding: "7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning."
33	
34	  - bibtex_key: zitkovich2023rt2
35	    title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
36	    authors: "Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others"
37	    year: 2023
38	    venue: "CoRL 2023"
39	    arxiv_id: "2307.15818"
40	    category: "VLA Models"
41	    role: foundation
42	    verified: true
43	    key_finding: "Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought."
44	
45	  - bibtex_key: ghosh2024octo
46	    title: "Octo: An Open-Source Generalist Robot Policy"
47	    authors: "Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others"
48	    year: 2024
49	    venue: "arXiv preprint"
50	    arxiv_id: "2405.12213"
51	    category: "VLA Models"
52	    role: background
53	    verified: true
54	    key_finding: "Transformer-based generalist policy trained on 800K trajectories from Open X-Embodiment; effective fine-tuning across 9 robot platforms."
55	
56	  - bibtex_key: black2024pi0
57	    title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
58	    authors: "Black, Kevin and Brown, Noah and Driess, Danny and others"
59	    year: 2024
60	    venue: "arXiv preprint"
61	    arxiv_id: "2410.24164"
62	    category: "VLA Models"
63	    role: foundation
64	    verified: true
65	    key_finding: "3.3B VLA using flow matching for 50Hz action generation; trained on 10K+ hours of robot data across 7 platforms and 68 tasks."
66	
67	  - bibtex_key: openxembodiment2024
68	    title: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models"
69	    authors: "Open X-Embodiment Collaboration"
70	    year: 2024
71	    venue: "ICRA 2024"
72	    arxiv_id: "2310.08864"
73	    category: "VLA Models"
74	    role: background
75	    verified: true
76	    key_finding: "1M+ real robot trajectories spanning 22 embodiments; RT-1-X shows 50% improvement over single-embodiment baselines."
77	
78	  # ============================================================
79	  # Cluster: VLM/LLM Token Efficiency (target: 8)
80	  # ============================================================
81	  - bibtex_key: chen2024fastv
82	    title: "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models"
83	    authors: "Chen, Liang and others"
84	    year: 2024
85	    venue: "ECCV 2024 (Oral)"
86	    arxiv_id: null
87	    category: "VLM/LLM Token Efficiency"
88	    role: direct-competitor
89	    verified: true
90	    key_finding: "Plug-and-play visual token pruning for VLMs; prunes tokens in deep layers based on attention patterns from early layers."
91	    pruning_stats: "Prunes ~50% visual tokens with minimal accuracy loss on VLM benchmarks."
92	
93	  - bibtex_key: zhang2023h2o
94	    title: "H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models"
95	    authors: "Zhang, Zhenyu and others"
96	    year: 2023
97	    venue: "NeurIPS 2023"
98	    arxiv_id: "2306.14048"
99	    category: "VLM/LLM Token Efficiency"
100	    role: background
101	    verified: true
102	    key_finding: "KV cache eviction retaining heavy-hitter tokens; 20% heavy hitters achieve up to 29x throughput improvement."
103	
104	  - bibtex_key: xiao2024streamingllm
105	    title: "Efficient Streaming Language Models with Attention Sinks"
106	    authors: "Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike"
107	    year: 2024
108	    venue: "ICLR 2024"
109	    arxiv_id: "2309.17453"
110	    category: "VLM/LLM Token Efficiency"
111	    role: background
112	    verified: true
113	    key_finding: "Attention sink phenomenon: keeping KV of initial tokens recovers window attention performance; enables stable LLM inference over 4M+ tokens."
114	
115	  - bibtex_key: hsu2025vlacache
116	    title: "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching"
117	    authors: "Hsu, Siyu and others"
118	    year: 2025
119	    venue: "NeurIPS 2025"
120	    arxiv_id: "2502.02175"
121	    category: "VLM/LLM Token Efficiency"
122	    role: direct-competitor
123	    verified: true
124	    key_finding: "Training-free VLA acceleration via temporal KV caching of static visual tokens; 1.7x speedup with negligible SR loss."
125	    notes: "Exploits temporal continuity, not token removal. Key difference from our study: caches rather than removes tokens."
126	
127	  - bibtex_key: wang2026vlaiap
128	    title: "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models"
129	    authors: "Wang, others"
130	    year: 2026
131	    venue: "arXiv preprint"
132	    arxiv_id: "2603.22991"
133	    category: "VLM/LLM Token Efficiency"
134	    role: direct-competitor
135	    verified: true
136	    key_finding: "Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens."
137	    notes: "Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA."
138	
139	  # ============================================================
140	  # Cluster: ViT Token Pruning/Merging (target: 7)
141	  # ============================================================
142	  - bibtex_key: rao2021dynamicvit
143	    title: "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification"
144	    authors: "Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui"
145	    year: 2021
146	    venue: "NeurIPS 2021"
147	    arxiv_id: "2106.02034"
148	    category: "ViT Token Pruning/Merging"
149	    role: foundation
150	    verified: true
151	    key_finding: "Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction."
152	    pruning_stats: "66% token removal, <0.5% accuracy drop, 40%+ throughput improvement."
153	
154	  - bibtex_key: bolya2023tome
155	    title: "Token Merging: Your ViT But Faster"
156	    authors: "Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy"
157	    year: 2023
158	    venue: "ICLR 2023 (Oral)"
159	    arxiv_id: "2210.09461"
160	    category: "ViT Token Pruning/Merging"
161	    role: foundation
162	    verified: true
163	    key_finding: "Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop."
164	    pruning_stats: "2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens."
165	
166	  - bibtex_key: liang2022evit
167	    title: "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations"
168	    authors: "Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao"
169	    year: 2022
170	    venue: "ICLR 2022"
171	    arxiv_id: "2202.07800"
172	    category: "ViT Token Pruning/Merging"
173	    role: foundation
174	    verified: true
175	    key_finding: "Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens."
176	    pruning_stats: "50% speedup, 0.3% accuracy drop on ImageNet."
177	
178	  # ============================================================
179	  # Cluster: Closed-Loop Evaluation (target: 5)
180	  # ============================================================
181	  - bibtex_key: liu2023libero
182	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
183	    authors: "Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter"
184	    year: 2023
185	    venue: "NeurIPS 2023"
186	    arxiv_id: "2306.03310"
187	    category: "Closed-Loop Evaluation"
188	    role: foundation
189	    verified: true
190	    key_finding: "130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations."
191	    notes: "Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task)."
192	
193	  - bibtex_key: mees2022calvin
194	    title: "CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks"
195	    authors: "Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram"
196	    year: 2022
197	    venue: "IEEE RA-L"
198	    arxiv_id: "2112.03227"
199	    category: "Closed-Loop Evaluation"
200	    role: background
201	    verified: true
202	    key_finding: "Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives."
203	
204	  - bibtex_key: chi2023diffusionpolicy
205	    title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
206	    authors: "Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran"
207	    year: 2023
208	    venue: "RSS 2023"
209	    arxiv_id: "2303.04137"
210	    category: "Closed-Loop Evaluation"
211	    role: background
212	    verified: true
213	    key_finding: "Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions."
214	
215	  # ============================================================
216	  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)
217	  # ============================================================
218	  - bibtex_key: zeng2023transformers_tsf
219	    title: "Are Transformers Effective for Time Series Forecasting?"
220	    authors: "Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang"
221	    year: 2023
222	    venue: "AAAI 2023"
223	    arxiv_id: "2205.13504"
224	    category: "Negative Results & Evaluation Pitfalls"
225	    role: foundation
226	    verified: true
227	    key_finding: "Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series."
228	
229	  - bibtex_key: bouthillier2024negative
230	    title: "Position: Embracing Negative Results in Machine Learning"
231	    authors: "Bouthillier, Xavier and others"
232	    year: 2024
233	    venue: "ICML 2024"
234	    arxiv_id: "2406.03980"
235	    category: "Negative Results & Evaluation Pitfalls"
236	    role: background
237	    verified: true
238	    key_finding: "Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions."
239	
240	  # ============================================================
241	  # Background / Architecture
242	  # ============================================================
243	  - bibtex_key: zhai2023siglip
244	    title: "Sigmoid Loss for Language Image Pre-Training"
245	    authors: "Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas"
246	    year: 2023
247	    venue: "ICCV 2023"
248	    arxiv_id: "2303.15343"
249	    category: "VLA Models"
250	    role: foundation
251	    verified: true
252	    key_finding: "Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips."
253	    notes: "Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token."
254	
255	  - bibtex_key: yang2024qwen2
256	    title: "Qwen2 Technical Report"
257	    authors: "Yang, An and others"
258	    year: 2024
259	    venue: "arXiv preprint"
260	    arxiv_id: "2407.10671"
261	    category: "VLA Models"
262	    role: background
263	    verified: true
264	    key_finding: "0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA."
265	
266	  - bibtex_key: lipman2023flow
267	    title: "Flow Matching for Generative Modeling"
268	    authors: "Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt"
269	    year: 2023
270	    venue: "ICLR 2023"
271	    arxiv_id: "2210.02747"
272	    category: "VLA Models"
273	    role: foundation
274	    verified: true
275	    key_finding: "Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling."
276	    notes: "Action generation mechanism in SmolVLA and pi0."
277	
278	  # ============================================================
279	  # Cluster: Vision Connectors & Token Compression (target: 6)
280	  # ============================================================
281	  - bibtex_key: li2023blip2
282	    title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
283	    authors: "Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven"
284	    year: 2023
285	    venue: "ICML 2023"
286	    arxiv_id: "2301.12597"
287	    category: "Vision Connectors & Token Compression"
288	    role: foundation
289	    verified: true
290	    key_finding: "Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters."
291	    notes: "Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle."
292	
293	  - bibtex_key: alayrac2022flamingo
294	    title: "Flamingo: a Visual Language Model for Few-Shot Learning"
295	    authors: "Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others"
296	    year: 2022
297	    venue: "NeurIPS 2022"
298	    arxiv_id: "2204.14198"
299	    category: "Vision Connectors & Token Compression"
300	    role: foundation
301	    verified: true
302	    key_finding: "Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries."
303	    notes: "Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches."
304	
305	  - bibtex_key: liu2023llava
306	    title: "Visual Instruction Tuning"
307	    authors: "Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae"
308	    year: 2023
309	    venue: "NeurIPS 2023"
310	    arxiv_id: "2304.08485"
311	    category: "Vision Connectors & Token Compression"
312	    role: foundation
313	    verified: true
314	    key_finding: "Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient."
315	    notes: "Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice."
316	
317	  - bibtex_key: shi2016subpixel
318	    title: "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network"
319	    authors: "Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan"
320	    year: 2016
321	    venue: "CVPR 2016"
322	    arxiv_id: "1609.05158"
323	    category: "Vision Connectors & Token Compression"
324	    role: background
325	    verified: true
326	    key_finding: "Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution."
327	    notes: "Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis."
328	
329	  - bibtex_key: chen2024internvl
330	    title: "How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites"
331	    authors: "Chen, Zhe and Wang, Weiyun and Tian, Hao and others"
332	    year: 2024
333	    venue: "arXiv preprint"
334	    arxiv_id: "2404.16821"
335	    category: "Vision Connectors & Token Compression"
336	    role: background
337	    verified: true
338	    key_finding: "InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles."
339	    notes: "Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding."
340	
341	  - bibtex_key: oquab2024dinov2
342	    title: "DINOv2: Learning Robust Visual Features without Supervision"
343	    authors: "Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others"
344	    year: 2024
345	    venue: "TMLR 2024"
346	    arxiv_id: "2304.07193"
347	    category: "Vision Connectors & Token Compression"
348	    role: foundation
349	    verified: true
350	    key_finding: "Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning."
351	    notes: "Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution."
352	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "a66cb00a-3bb1-4d87-ac8c-8c4b35eb3ed2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
      "content": "# Literature Map — importance_margin_vla_compress\n# Generated: 2026-05-17\n# Citation budget: 35\n\npapers:\n\n  # ============================================================\n  # Cluster: VLA Models (target: 6)\n  # ============================================================\n  - bibtex_key: shukor2025smolvla\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.01844\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64.\"\n    pruning_stats: null\n    notes: \"Our experimental platform. SigLIP encoder produces 128 vision tokens.\"\n\n  - bibtex_key: kim2024openvla\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    arxiv_id: \"2406.09246\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning.\"\n\n  - bibtex_key: zitkovich2023rt2\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others\"\n    year: 2023\n    venue: \"CoRL 2023\"\n    arxiv_id: \"2307.15818\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought.\"\n\n  - bibtex_key: ghosh2024octo\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2405.12213\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"Transformer-based generalist policy trained on 800K trajectories from Open X-Embodiment; effective fine-tuning across 9 robot platforms.\"\n\n  - bibtex_key: black2024pi0\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black, Kevin and Brown, Noah and Driess, Danny and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2410.24164\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"3.3B VLA using flow matching for 50Hz action generation; trained on 10K+ hours of robot data across 7 platforms and 68 tasks.\"\n\n  - bibtex_key: openxembodiment2024\n    title: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\"\n    authors: \"Open X-Embodiment Collaboration\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    arxiv_id: \"2310.08864\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"1M+ real robot trajectories spanning 22 embodiments; RT-1-X shows 50% improvement over single-embodiment baselines.\"\n\n  # ============================================================\n  # Cluster: VLM/LLM Token Efficiency (target: 8)\n  # ============================================================\n  - bibtex_key: chen2024fastv\n    title: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\"\n    authors: \"Chen, Liang and others\"\n    year: 2024\n    venue: \"ECCV 2024 (Oral)\"\n    arxiv_id: null\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Plug-and-play visual token pruning for VLMs; prunes tokens in deep layers based on attention patterns from early layers.\"\n    pruning_stats: \"Prunes ~50% visual tokens with minimal accuracy loss on VLM benchmarks.\"\n\n  - bibtex_key: zhang2023h2o\n    title: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\"\n    authors: \"Zhang, Zhenyu and others\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.14048\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"KV cache eviction retaining heavy-hitter tokens; 20% heavy hitters achieve up to 29x throughput improvement.\"\n\n  - bibtex_key: xiao2024streamingllm\n    title: \"Efficient Streaming Language Models with Attention Sinks\"\n    authors: \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2309.17453\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"Attention sink phenomenon: keeping KV of initial tokens recovers window attention performance; enables stable LLM inference over 4M+ tokens.\"\n\n  - bibtex_key: hsu2025vlacache\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: \"Hsu, Siyu and others\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2502.02175\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Training-free VLA acceleration via temporal KV caching of static visual tokens; 1.7x speedup with negligible SR loss.\"\n    notes: \"Exploits temporal continuity, not token removal. Key difference from our study: caches rather than removes tokens.\"\n\n  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  # ============================================================\n  # Cluster: ViT Token Pruning/Merging (target: 7)\n  # ============================================================\n  - bibtex_key: rao2021dynamicvit\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: \"Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    arxiv_id: \"2106.02034\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction.\"\n    pruning_stats: \"66% token removal, <0.5% accuracy drop, 40%+ throughput improvement.\"\n\n  - bibtex_key: bolya2023tome\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: \"Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy\"\n    year: 2023\n    venue: \"ICLR 2023 (Oral)\"\n    arxiv_id: \"2210.09461\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop.\"\n    pruning_stats: \"2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens.\"\n\n  - bibtex_key: liang2022evit\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: \"Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    arxiv_id: \"2202.07800\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"\n    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"\n    category: \"Closed-Loop Evaluation\"\n    role: foundation\n    verified: true\n    key_finding: \"130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations.\"\n    notes: \"Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task).\"\n\n  - bibtex_key: mees2022calvin\n    title: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\"\n    authors: \"Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram\"\n    year: 2022\n    venue: \"IEEE RA-L\"\n    arxiv_id: \"2112.03227\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives.\"\n\n  - bibtex_key: chi2023diffusionpolicy\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran\"\n    year: 2023\n    venue: \"RSS 2023\"\n    arxiv_id: \"2303.04137\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions.\"\n\n  # ============================================================\n  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)\n  # ============================================================\n  - bibtex_key: zeng2023transformers_tsf\n    title: \"Are Transformers Effective for Time Series Forecasting?\"\n    authors: \"Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang\"\n    year: 2023\n    venue: \"AAAI 2023\"\n    arxiv_id: \"2205.13504\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series.\"\n\n  - bibtex_key: bouthillier2024negative\n    title: \"Position: Embracing Negative Results in Machine Learning\"\n    authors: \"Bouthillier, Xavier and others\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2406.03980\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: background\n    verified: true\n    key_finding: \"Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions.\"\n\n  # ============================================================\n  # Background / Architecture\n  # ============================================================\n  - bibtex_key: zhai2023siglip\n    title: \"Sigmoid Loss for Language Image Pre-Training\"\n    authors: \"Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas\"\n    year: 2023\n    venue: \"ICCV 2023\"\n    arxiv_id: \"2303.15343\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips.\"\n    notes: \"Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token.\"\n\n  - bibtex_key: yang2024qwen2\n    title: \"Qwen2 Technical Report\"\n    authors: \"Yang, An and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2407.10671\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA.\"\n\n  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\"\n",
      "numLines": 352,
      "startLine": 1,
      "totalLines": 352
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I'll search for the three papers using Semantic Scholar API.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "89363181-f549-4c25-ab66-4a172038eae3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbsjL5cWSyjGcRXRfRubSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 25455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6363
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

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01BfNztNJWovWGEQN6VWYjjM`</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 1: EfficientVLA\nresults = search_s2('EfficientVLA efficient vision language action model', 5)\nprint('=== EfficientVLA ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
  "description": "Search Semantic Scholar for EfficientVLA",
  "timeout": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "19056412-6cb4-4faa-b338-6ba57e9c3d6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbsjL5cWSyjGcRXRfRubSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 25455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6363
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

_source line 9 · 2026-05-18T01:56:08.605Z_

<details><summary>↩ Tool result · reported error · `toolu_01BfNztNJWovWGEQN6VWYjjM`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 11, in &lt;module>
    results = search_s2('EfficientVLA efficient vision language action model', 5)
  File "&lt;string>", line 7, in search_s2
    with urllib.request.urlopen(req, timeout=15) as resp:
         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
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
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "6b042726-5209-4686-ac68-2f4da9a0dffe",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 11, in &lt;module>\n    results = search_s2('EfficientVLA efficient vision language action model', 5)\n  File \"&lt;string>\", line 7, in search_s2\n    with urllib.request.urlopen(req, timeout=15) as resp:\n         ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/urllib/request.py\", line 187, in urlopen\n    return opener.open(url, data, timeout)\n           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/urllib/request.py\", line 493, in open\n    response = meth(req, response)\n  File \"/usr/lib/python3.14/urllib/request.py\", line 602, in http_response\n    response = self.parent.error(\n        'http', request, response, code, msg, hdrs)\n  File \"/usr/lib/python3.14/urllib/request.py\", line 531, in error\n    return self._call_chain(*args)\n           ~~~~~~~~~~~~~~~~^^^^^^^\n  File \"/usr/lib/python3.14/urllib/request.py\", line 464, in _call_chain\n    result = func(*args)\n  File \"/usr/lib/python3.14/urllib/request.py\", line 611, in http_error_default\n    raise HTTPError(req.full_url, code, msg, hdrs, fp)\nurllib.error.HTTPError: HTTP Error 429:"
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Bash · `toolu_01UpguGiYtXeNrTRVYNBjdpB`</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 2: VLA-Pruner\nresults = search_s2('VLA-Pruner temporal aware pruning vision language action', 5)\nprint('=== VLA-Pruner ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
  "description": "Search Semantic Scholar for VLA-Pruner",
  "timeout": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "3185e97e-35bb-495a-92e9-b7017f28b50e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbsjL5cWSyjGcRXRfRubSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 25455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6363
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

_source line 11 · 2026-05-18T01:56:11.402Z_

<details><summary>↩ Tool result · reported error · `toolu_01UpguGiYtXeNrTRVYNBjdpB`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import urllib.request, urll…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "5e716d17-deca-4cbb-89d2-92da1731f970",
  "tool_use_result": "Cancelled: parallel tool call Bash(python3 -c \"\nimport urllib.request, urll…) errored"
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01K23ikR8aKMyUs5J2BGE5Ur`</summary>

```json
{
  "command": "python3 -c \"\nimport urllib.request, urllib.parse, json\n\ndef search_s2(query, limit=5):\n    url = f'https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(query)}&limit={limit}&fields=title,authors,year,venue,externalIds,abstract'\n    req = urllib.request.Request(url)\n    with urllib.request.urlopen(req, timeout=15) as resp:\n        return json.loads(resp.read())\n\n# Search 3: LLaVA-PruMerge or VLM token pruning merging\nresults = search_s2('LLaVA-PruMerge visual token pruning merging', 5)\nprint('=== LLaVA-PruMerge ===')\nfor p in results.get('data', []):\n    print(json.dumps({'title': p['title'], 'year': p.get('year'), 'venue': p.get('venue'), 'arxiv': p.get('externalIds', {}).get('ArXiv'), 'authors': [a['name'] for a in p.get('authors', [])[:3]]}, indent=2))\n    print()\n\"\n",
  "description": "Search Semantic Scholar for LLaVA-PruMerge",
  "timeout": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "925af2ac-00da-4301-8426-cbc3685829db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HbsjL5cWSyjGcRXRfRubSe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6363,
      "cache_read_input_tokens": 25455,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6363
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

_source line 13 · 2026-05-18T01:56:14.307Z_

<details><summary>↩ Tool result · reported error · `toolu_01K23ikR8aKMyUs5J2BGE5Ur`</summary>

```text
&lt;tool_use_error>Cancelled: parallel tool call Bash(python3 -c "
import urllib.request, urll…) errored&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "74f913d4-8462-4185-a2e3-736a4b2e1d9a",
  "tool_use_result": "Cancelled: parallel tool call Bash(python3 -c \"\nimport urllib.request, urll…) errored"
}
```

</details>

---

### Assistant

_source line 14_

S2 API rate-limited. Let me use WebSearch instead.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "76055be8-d72b-44b9-bce9-fc4bcab1c02c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHRD3JfUr7xQH88xN7cfC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1671,
      "cache_read_input_tokens": 31818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1671
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

_source line 15_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01F3PFQqzfAjVzUcaTxYCxa8`</summary>

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
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "c6a717c6-c2e9-49c0-93f3-e44ddb641a56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UHRD3JfUr7xQH88xN7cfC1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1671,
      "cache_read_input_tokens": 31818,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1671
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

_source line 16 · 2026-05-18T01:56:20.504Z_

<details><summary>↩ Tool result · `toolu_01F3PFQqzfAjVzUcaTxYCxa8`</summary>

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
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "3722b3d0-2840-43ae-bd8e-afe2e24cd4ea",
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

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Let me search for these papers using WebSearch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "52af4b68-4b74-4c30-bf74-aba979a925b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMNUepdHaZhGHdH7s3sTXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 33489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wn19HZWZzXbbh58KEZ539q`</summary>

```json
{
  "query": "EfficientVLA vision language action model pruning caching 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "47b2b310-ca9a-4d87-ad22-b13cc16545d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMNUepdHaZhGHdH7s3sTXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 33489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011juZs4zVEDnhKN2RdDqpJ5`</summary>

```json
{
  "query": "VLA-Pruner temporal aware dual level pruning vision language action 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "d437d001-c373-4450-b0c9-5400def9c044",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMNUepdHaZhGHdH7s3sTXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 33489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
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

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UrCACASDqR9UFr6WaLNBVH`</summary>

```json
{
  "query": "LLaVA-PruMerge adaptive token reduction large multimodal models arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "c17150b4-477f-41a3-8973-563f2cb4a17b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMNUepdHaZhGHdH7s3sTXZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 618,
      "cache_read_input_tokens": 33489,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 618
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

_source line 21 · 2026-05-18T01:56:33.284Z_

<details><summary>↩ Tool result · `toolu_011juZs4zVEDnhKN2RdDqpJ5`</summary>

```text
Web search results for query: "VLA-Pruner temporal aware dual level pruning vision language action 2025 arxiv"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v1"},{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation","url":"https://arxiv.org/html/2509.22093v1"},{"title":"SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration","url":"https://arxiv.org/html/2506.12723v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"}]

Based on the search results, I found the paper you're looking for. Here's the information about VLA-Pruner:

## VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning

VLA-Pruner is a paper titled "Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference", published on arXiv with ID 2511.16449.

### Key Aspects:

**Problem:** Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment.

**Approach:** VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.

**Technical Method:** VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.

**Results:** Experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks.

The paper addresses a limitation in existing VLM-specific token pruning methods that overlook the dual-system nature of VLA models, which require both semantic understanding and action execution capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "7906bd84-8237-4d99-ae61-42e7f4a25185",
  "tool_use_result": {
    "query": "VLA-Pruner temporal aware dual level pruning vision language action 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FtmVfy2hQbPB4Qyyei3SSY",
        "content": [
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449v1"
          },
          {
            "title": "[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/abs/2509.05614"
          },
          {
            "title": "Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2602.00780"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware",
            "url": "https://arxiv.org/pdf/2509.05614"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/html/2509.05614v1"
          },
          {
            "title": "Action-aware Dynamic Pruning for Efficient Vision-Language-Action Manipulation",
            "url": "https://arxiv.org/html/2509.22093v1"
          },
          {
            "title": "SP-VLA: A Joint Model Scheduling and Token Pruning Approach for VLA Model Acceleration",
            "url": "https://arxiv.org/html/2506.12723v2"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2603.22991v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's the information about VLA-Pruner:\n\n## VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning\n\nVLA-Pruner is a paper titled \"Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\", published on arXiv with ID 2511.16449.\n\n### Key Aspects:\n\n**Problem:** Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment.\n\n**Approach:** VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.\n\n**Technical Method:** VLA-Pruner adopts a dual-level importance criterion for visual token retention: vision-language prefill attention for semantic-level relevance and action decode attention, estimated via temporal smoothing, for action-level importance.\n\n**Results:** Experiments show that VLA-Pruner achieves state-of-the-art performance across multiple VLA architectures and diverse robotic tasks.\n\nThe paper addresses a limitation in existing VLM-specific token pruning methods that overlook the dual-system nature of VLA models, which require both semantic understanding and action execution capabilities."
    ],
    "durationSeconds": 5.868775503000005
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-18T01:56:33.615Z_

<details><summary>↩ Tool result · `toolu_01UrCACASDqR9UFr6WaLNBVH`</summary>

```text
Web search results for query: "LLaVA-PruMerge adaptive token reduction large multimodal models arxiv"

Links: [{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v5"},{"title":"[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v4"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"Rethinking Token Reduction in MLLMs: Towards a Unified Paradigm for Training-Free Acceleration","url":"https://arxiv.org/html/2411.17686v1"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models - Paper Detail","url":"https://deeplearn.org/arxiv/472288/llava-prumerge:-adaptive-token-reduction-for-efficient-large-multimodal-models"},{"title":"PAR: Prompt-Aware Token Reduction Method for Efficient Large Multimodal Models","url":"https://arxiv.org/html/2410.07278v2"},{"title":"Towards Adaptive Visual Token Pruning for Large Multimodal Models","url":"https://arxiv.org/html/2509.00320v1"},{"title":"AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning","url":"https://arxiv.org/html/2412.03248v1"}]

I found the research paper you're looking for. Here's a summary of the search results:

## LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models

Large Multimodal Models (LMMs) have shown significant visual reasoning capabilities by connecting a visual encoder and a large language model, and typically take in a fixed and large amount of visual tokens, such as the penultimate layer features in the CLIP visual encoder, as the prefix content.

Due to the inherent design of the Transformer architecture, the computational costs of these models tend to increase quadratically with the number of input tokens. PruMerge is a novel adaptive visual token reduction strategy that significantly reduces the number of visual tokens without compromising the performance of LMMs.

**Key Results:**
PruMerge and PruMerge+ can adaptively reduce visual tokens, which use only (respectively) 5.5% and 25.0% visual tokens on average (on 6 tasks) and achieves competitive performance to the original LLaVA-1.5.

The paper (arXiv:2403.15388) was authored by Yuzhang Shang and collaborators, and additional resources including code and checkpoints are available at the paper's official website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "2ee9c7a7-8aa1-4d2c-a92b-60b5200b5652",
  "tool_use_result": {
    "query": "LLaVA-PruMerge adaptive token reduction large multimodal models arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_015AKh8Ku3eoBtDiSXJf5FwN",
        "content": [
          {
            "title": "[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/abs/2403.15388"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/pdf/2403.15388"
          },
          {
            "title": "[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/abs/2403.15388v5"
          },
          {
            "title": "[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/abs/2403.15388v4"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"
          },
          {
            "title": "Rethinking Token Reduction in MLLMs: Towards a Unified Paradigm for Training-Free Acceleration",
            "url": "https://arxiv.org/html/2411.17686v1"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models - Paper Detail",
            "url": "https://deeplearn.org/arxiv/472288/llava-prumerge:-adaptive-token-reduction-for-efficient-large-multimodal-models"
          },
          {
            "title": "PAR: Prompt-Aware Token Reduction Method for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/html/2410.07278v2"
          },
          {
            "title": "Towards Adaptive Visual Token Pruning for Large Multimodal Models",
            "url": "https://arxiv.org/html/2509.00320v1"
          },
          {
            "title": "AIM: Adaptive Inference of Multi-Modal LLMs via Token Merging and Pruning",
            "url": "https://arxiv.org/html/2412.03248v1"
          }
        ]
      },
      "I found the research paper you're looking for. Here's a summary of the search results:\n\n## LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\n\nLarge Multimodal Models (LMMs) have shown significant visual reasoning capabilities by connecting a visual encoder and a large language model, and typically take in a fixed and large amount of visual tokens, such as the penultimate layer features in the CLIP visual encoder, as the prefix content.\n\nDue to the inherent design of the Transformer architecture, the computational costs of these models tend to increase quadratically with the number of input tokens. PruMerge is a novel adaptive visual token reduction strategy that significantly reduces the number of visual tokens without compromising the performance of LMMs.\n\n**Key Results:**\nPruMerge and PruMerge+ can adaptively reduce visual tokens, which use only (respectively) 5.5% and 25.0% visual tokens on average (on 6 tasks) and achieves competitive performance to the original LLaVA-1.5.\n\nThe paper (arXiv:2403.15388) was authored by Yuzhang Shang and collaborators, and additional resources including code and checkpoints are available at the paper's official website."
    ],
    "durationSeconds": 6.022234461
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-18T01:56:35.751Z_

<details><summary>↩ Tool result · `toolu_01Wn19HZWZzXbbh58KEZ539q`</summary>

```text
Web search results for query: "EfficientVLA vision language action model pruning caching 2025 arxiv"

Links: [{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://arxiv.org/html/2511.18960v1"}]

I found comprehensive information about EfficientVLA and related research on Vision-Language-Action (VLA) model optimization. Here are the key findings:

## EfficientVLA Overview

EfficientVLA is a novel training-free, structured inference acceleration framework that synergistically prunes redundant layers from the language module based on their informational impact and strategically selects a compact, task-focused subset of visual tokens by considering both VLA task relevance and inherent image feature diversity.

## Key Components

The framework addresses three main efficiency challenges:

1. **Layer Pruning**: Using a similarity-derived importance metric to target the primary memory bottleneck of the language module and its observed depth-wise redundancy, EfficientVLA employs a similarity-derived importance metric to prune functionally inconsequential layers, thus reducing the depth of the model and the demands for memory without retraining.

2. **Visual Token Pruning**: To manage the initial computational load from visual inputs before the memory of LLM limit is reached, the visual token pruning strategy tackles both task-relevant and inherent image redundancies by first selecting critical task-aligned tokens, then augmenting this set to ensure representational diversity while maintaining high task relevance.

3. **Temporal Caching**: EfficientVLA addresses temporal redundancy in the compute-intensive action generator (highlighted by high feature similarity across timesteps) by caching and reusing intermediate attention and MLP outputs, thus curtailing redundant computations.

## Performance

EfficientVLA demonstrates efficacy through extensive experiments on the CogACT in the SIMPLER environment. The framework achieves significant efficiency improvements while maintaining task performance, making it practical for deployment on resource-constrained robotics platforms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "a68f3a60-ff43-4fa2-b831-19149ae1ee0d",
  "tool_use_result": {
    "query": "EfficientVLA vision language action model pruning caching 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PETMnq5vYLAtCBcbM1t8W9",
        "content": [
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.10100v1"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning",
            "url": "https://arxiv.org/html/2509.05614v1"
          },
          {
            "title": "VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation",
            "url": "https://arxiv.org/html/2502.02175v1"
          },
          {
            "title": "The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning",
            "url": "https://arxiv.org/html/2509.12594v1"
          },
          {
            "title": "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware",
            "url": "https://arxiv.org/pdf/2509.05614"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v2"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching",
            "url": "https://arxiv.org/html/2502.02175"
          },
          {
            "title": "AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention",
            "url": "https://arxiv.org/html/2511.18960v1"
          }
        ]
      },
      "I found comprehensive information about EfficientVLA and related research on Vision-Language-Action (VLA) model optimization. Here are the key findings:\n\n## EfficientVLA Overview\n\nEfficientVLA is a novel training-free, structured inference acceleration framework that synergistically prunes redundant layers from the language module based on their informational impact and strategically selects a compact, task-focused subset of visual tokens by considering both VLA task relevance and inherent image feature diversity.\n\n## Key Components\n\nThe framework addresses three main efficiency challenges:\n\n1. **Layer Pruning**: Using a similarity-derived importance metric to target the primary memory bottleneck of the language module and its observed depth-wise redundancy, EfficientVLA employs a similarity-derived importance metric to prune functionally inconsequential layers, thus reducing the depth of the model and the demands for memory without retraining.\n\n2. **Visual Token Pruning**: To manage the initial computational load from visual inputs before the memory of LLM limit is reached, the visual token pruning strategy tackles both task-relevant and inherent image redundancies by first selecting critical task-aligned tokens, then augmenting this set to ensure representational diversity while maintaining high task relevance.\n\n3. **Temporal Caching**: EfficientVLA addresses temporal redundancy in the compute-intensive action generator (highlighted by high feature similarity across timesteps) by caching and reusing intermediate attention and MLP outputs, thus curtailing redundant computations.\n\n## Performance\n\nEfficientVLA demonstrates efficacy through extensive experiments on the CogACT in the SIMPLER environment. The framework achieves significant efficiency improvements while maintaining task performance, making it practical for deployment on resource-constrained robotics platforms."
    ],
    "durationSeconds": 9.167621006000001
  }
}
```

</details>

---

### Assistant

_source line 24_

Found all three papers. Let me get more details on EfficientVLA (arxiv ID and authors).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "1b92739f-847e-4290-ad1a-30510d38abd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqPbhP7kk4NsdD1VYLWX8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1816,
      "cache_creation_input_tokens": 1238,
      "cache_read_input_tokens": 34107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1238
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TmkSLmNq3uHopRarzRchoE`</summary>

```json
{
  "query": "arxiv 2506.10100 EfficientVLA authors CogACT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "2aab191f-481a-4797-a690-4eb301da855c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqPbhP7kk4NsdD1VYLWX8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1816,
      "cache_creation_input_tokens": 1238,
      "cache_read_input_tokens": 34107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1238
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MvGsUvHtUnHzdv7iaEHtH`</summary>

```json
{
  "query": "arxiv 2403.15388 LLaVA-PruMerge authors Yuzhang Shang venue 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "558e69a4-9c2d-4c83-b1cc-7773477e321b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FqPbhP7kk4NsdD1VYLWX8W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1816,
      "cache_creation_input_tokens": 1238,
      "cache_read_input_tokens": 34107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1238
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

_source line 27 · 2026-05-18T01:56:48.549Z_

<details><summary>↩ Tool result · `toolu_01TmkSLmNq3uHopRarzRchoE`</summary>

```text
Web search results for query: "arxiv 2506.10100 EfficientVLA authors CogACT"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"},{"title":"README.md · CogACT/CogACT-Small at 8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d","url":"https://huggingface.co/CogACT/CogACT-Small/blob/8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d/README.md"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.17811"}]

Based on the search results, I found the paper arxiv 2506.10100 with information about EfficientVLA and CogACT:

## Paper: EfficientVLA (arxiv 2506.10100)

The authors are: Yantai Yang, Yuhao Wang, Zichen Wen, Luo Zhongwei, Chang Zou, Zhipeng Zhang, Chuan Wen, and Linfeng Zhang.

### Overview
EfficientVLA is a structured and training-free inference acceleration framework that systematically eliminates barriers by cohesively exploiting multifaceted redundancies.

### Key Strategies
EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features.

### Results on CogACT
When applied to the CogACT model, EfficientVLA yields a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "63b2841d-1cbc-4d57-a057-ccc37a3010eb",
  "tool_use_result": {
    "query": "arxiv 2506.10100 EfficientVLA authors CogACT",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XqxUMJBzywV3X2atm9ZLPK",
        "content": [
          {
            "title": "[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2506.10100"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.10100"
          },
          {
            "title": "Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2506.10100"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation",
            "url": "https://arxiv.org/html/2411.19650v1"
          },
          {
            "title": "[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"
          },
          {
            "title": "README.md · CogACT/CogACT-Small at 8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d",
            "url": "https://huggingface.co/CogACT/CogACT-Small/blob/8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d/README.md"
          },
          {
            "title": "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching",
            "url": "https://vla-cache.github.io/"
          },
          {
            "title": "[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation",
            "url": "https://arxiv.org/abs/2411.19650"
          },
          {
            "title": "RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.17811"
          }
        ]
      },
      "Based on the search results, I found the paper arxiv 2506.10100 with information about EfficientVLA and CogACT:\n\n## Paper: EfficientVLA (arxiv 2506.10100)\n\nThe authors are: Yantai Yang, Yuhao Wang, Zichen Wen, Luo Zhongwei, Chang Zou, Zhipeng Zhang, Chuan Wen, and Linfeng Zhang.\n\n### Overview\nEfficientVLA is a structured and training-free inference acceleration framework that systematically eliminates barriers by cohesively exploiting multifaceted redundancies.\n\n### Key Strategies\nEfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features.\n\n### Results on CogACT\nWhen applied to the CogACT model, EfficientVLA yields a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark."
    ],
    "durationSeconds": 7.257372445000001
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-18T01:56:48.605Z_

<details><summary>↩ Tool result · `toolu_018MvGsUvHtUnHzdv7iaEHtH`</summary>

```text
Web search results for query: "arxiv 2403.15388 LLaVA-PruMerge authors Yuzhang Shang venue 2024"

Links: [{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"[Paper Review] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://velog.io/@euisuk-chung/LLaVA-PruMerge-Adaptive-Token-Reduction-for-Efficient-Large-Multimodal-Models"},{"title":"Figure 2 from LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLaVA-PruMerge:-Adaptive-Token-Reduction-for-Large-Shang-Cai/c0ef72d02b93065e77c506e23ce9acbbcd945893/figure/2"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2403.15388"},{"title":"dblp: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models.","url":"https://dblp.org/rec/journals/corr/abs-2403-15388.html"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.html"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...","url":"https://arxiv.org/pdf/2403.15388v4"},{"title":"arXiv:2409.10994v3 [cs.CL] 17 Dec 2024","url":"https://arxiv.org/pdf/2409.10994"}]

Based on the search results, here's the information about arxiv paper 2403.15388:

**Paper Title:** LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models

**Authors:** Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan

**Submission Date:** The paper was first submitted on March 22, 2024

**Venue:** The paper was published in the Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) in October 2025

**Summary:** PruMerge is a novel adaptive visual token reduction strategy that significantly reduces the number of visual tokens without compromising the performance of LMMs. When applied to LLaVA-1.5 and Video-LLaVA, the approach can reduce the number of visual tokens by 4 times, and achieve comparable or better performance across diverse visual question-answering and reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "6f737321-fa5a-46bb-b22a-99595b633a9d",
  "tool_use_result": {
    "query": "arxiv 2403.15388 LLaVA-PruMerge authors Yuzhang Shang venue 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GgzKnLAidj38KLZHBYHCu1",
        "content": [
          {
            "title": "[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/abs/2403.15388"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://arxiv.org/pdf/2403.15388"
          },
          {
            "title": "[Paper Review] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models",
            "url": "https://velog.io/@euisuk-chung/LLaVA-PruMerge-Adaptive-Token-Reduction-for-Efficient-Large-Multimodal-Models"
          },
          {
            "title": "Figure 2 from LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/LLaVA-PruMerge:-Adaptive-Token-Reduction-for-Large-Shang-Cai/c0ef72d02b93065e77c506e23ce9acbbcd945893/figure/2"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...",
            "url": "https://ui.adsabs.harvard.edu/abs/arXiv:2403.15388"
          },
          {
            "title": "dblp: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models.",
            "url": "https://dblp.org/rec/journals/corr/abs-2403-15388.html"
          },
          {
            "title": "ICCV 2025 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/html/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.html"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"
          },
          {
            "title": "LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...",
            "url": "https://arxiv.org/pdf/2403.15388v4"
          },
          {
            "title": "arXiv:2409.10994v3 [cs.CL] 17 Dec 2024",
            "url": "https://arxiv.org/pdf/2409.10994"
          }
        ]
      },
      "Based on the search results, here's the information about arxiv paper 2403.15388:\n\n**Paper Title:** LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\n\n**Authors:** Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan\n\n**Submission Date:** The paper was first submitted on March 22, 2024\n\n**Venue:** The paper was published in the Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) in October 2025\n\n**Summary:** PruMerge is a novel adaptive visual token reduction strategy that significantly reduces the number of visual tokens without compromising the performance of LMMs. When applied to LLaVA-1.5 and Video-LLaVA, the approach can reduce the number of visual tokens by 4 times, and achieve comparable or better performance across diverse visual question-answering and reasoning tasks."
    ],
    "durationSeconds": 6.428325581000005
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information for all three papers. Let me also get the VLA-Pruner authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "c97e7d00-0b7d-44af-91b7-b4c22015d0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQfe4x3rj6YThFBPv7FtEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 35345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3975
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

_source line 30_

Now let me get VLA-Pruner authors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "b140166e-a90f-434b-b8a1-ee7620508177",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQfe4x3rj6YThFBPv7FtEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 35345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3975
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QUGtZrvWik169pebDRcFsy`</summary>

```json
{
  "query": "arxiv 2511.16449 VLA-Pruner authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "c9a2ef9c-a0e7-4674-864a-2368281fdd99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQfe4x3rj6YThFBPv7FtEr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3975,
      "cache_read_input_tokens": 35345,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3975
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

_source line 32 · 2026-05-18T01:56:56.661Z_

<details><summary>↩ Tool result · `toolu_01QUGtZrvWik169pebDRcFsy`</summary>

```text
Web search results for query: "arxiv 2511.16449 VLA-Pruner authors"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://www.arxiv.org/list/cs.CV/2025?skip=24300&show=50"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=7900"},{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2511.09516] MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation","url":"https://arxiv.org/abs/2511.09516"},{"title":"[2511.10518] SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.10518"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"[2512.02700] VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm","url":"https://arxiv.org/abs/2512.02700"},{"title":"[2511.05397v1] EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation","url":"https://arxiv.org/abs/2511.05397v1"}]

Based on the search results, the authors of arXiv paper 2511.16449 "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference" are: Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, and Bo Zhao.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "0d7c8cfa-9192-4800-8e46-d855a8420619",
  "tool_use_result": {
    "query": "arxiv 2511.16449 VLA-Pruner authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_012DH9HUrQe1ABd38nJrj4zU",
        "content": [
          {
            "title": "[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/abs/2511.16449"
          },
          {
            "title": "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference",
            "url": "https://arxiv.org/html/2511.16449"
          },
          {
            "title": "Computer Vision and Pattern Recognition 2025",
            "url": "https://www.arxiv.org/list/cs.CV/2025?skip=24300&show=50"
          },
          {
            "title": "Computer Science Nov 2025",
            "url": "https://arxiv.org/list/cs/2025-11?skip=7900"
          },
          {
            "title": "[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22991v1"
          },
          {
            "title": "[2511.09516] MAP-VLA: Memory-Augmented Prompting for Vision-Language-Action Model in Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.09516"
          },
          {
            "title": "[2511.10518] SemanticVLA: Semantic-Aligned Sparsification and Enhancement for Efficient Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.10518"
          },
          {
            "title": "AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2511.14148v1"
          },
          {
            "title": "[2512.02700] VLM-Pruner: Buffering for Spatial Sparsity in an Efficient VLM Centrifugal Token Pruning Paradigm",
            "url": "https://arxiv.org/abs/2512.02700"
          },
          {
            "title": "[2511.05397v1] EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation",
            "url": "https://arxiv.org/abs/2511.05397v1"
          }
        ]
      },
      "Based on the search results, the authors of arXiv paper 2511.16449 \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" are: Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, and Bo Zhao."
    ],
    "durationSeconds": 3.403387764999992
  }
}
```

</details>

---

### Assistant

_source line 33_

I have all three papers verified. Now I'll append them to the literature_map.yaml.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "54f8a36b-4c78-4e7b-a7ff-42bae3cdfcd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbLQkot8DFb1KT8NjixX39",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 39320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 34_

<details open><summary>🔧 Tool call — Edit · `toolu_01LDXA31dBjRm1z1a84A3rGo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
  "old_string": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"",
  "new_string": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "ff9ee127-0d13-49d3-a034-e8a6545edd3d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BbLQkot8DFb1KT8NjixX39",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 785,
      "cache_read_input_tokens": 39320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 785
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

_source line 35 · 2026-05-18T01:57:22.208Z_

<details><summary>↩ Tool result · `toolu_01LDXA31dBjRm1z1a84A3rGo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "1e72f29e-9c47-4ac4-9bd9-7e5a329fc5f0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
    "oldString": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"",
    "newString": "  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\"",
    "originalFile": "# Literature Map — importance_margin_vla_compress\n# Generated: 2026-05-17\n# Citation budget: 35\n\npapers:\n\n  # ============================================================\n  # Cluster: VLA Models (target: 6)\n  # ============================================================\n  - bibtex_key: shukor2025smolvla\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.01844\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64.\"\n    pruning_stats: null\n    notes: \"Our experimental platform. SigLIP encoder produces 128 vision tokens.\"\n\n  - bibtex_key: kim2024openvla\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    arxiv_id: \"2406.09246\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning.\"\n\n  - bibtex_key: zitkovich2023rt2\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others\"\n    year: 2023\n    venue: \"CoRL 2023\"\n    arxiv_id: \"2307.15818\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought.\"\n\n  - bibtex_key: ghosh2024octo\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2405.12213\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"Transformer-based generalist policy trained on 800K trajectories from Open X-Embodiment; effective fine-tuning across 9 robot platforms.\"\n\n  - bibtex_key: black2024pi0\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black, Kevin and Brown, Noah and Driess, Danny and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2410.24164\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"3.3B VLA using flow matching for 50Hz action generation; trained on 10K+ hours of robot data across 7 platforms and 68 tasks.\"\n\n  - bibtex_key: openxembodiment2024\n    title: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\"\n    authors: \"Open X-Embodiment Collaboration\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    arxiv_id: \"2310.08864\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"1M+ real robot trajectories spanning 22 embodiments; RT-1-X shows 50% improvement over single-embodiment baselines.\"\n\n  # ============================================================\n  # Cluster: VLM/LLM Token Efficiency (target: 8)\n  # ============================================================\n  - bibtex_key: chen2024fastv\n    title: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\"\n    authors: \"Chen, Liang and others\"\n    year: 2024\n    venue: \"ECCV 2024 (Oral)\"\n    arxiv_id: null\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Plug-and-play visual token pruning for VLMs; prunes tokens in deep layers based on attention patterns from early layers.\"\n    pruning_stats: \"Prunes ~50% visual tokens with minimal accuracy loss on VLM benchmarks.\"\n\n  - bibtex_key: zhang2023h2o\n    title: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\"\n    authors: \"Zhang, Zhenyu and others\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.14048\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"KV cache eviction retaining heavy-hitter tokens; 20% heavy hitters achieve up to 29x throughput improvement.\"\n\n  - bibtex_key: xiao2024streamingllm\n    title: \"Efficient Streaming Language Models with Attention Sinks\"\n    authors: \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2309.17453\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"Attention sink phenomenon: keeping KV of initial tokens recovers window attention performance; enables stable LLM inference over 4M+ tokens.\"\n\n  - bibtex_key: hsu2025vlacache\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: \"Hsu, Siyu and others\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2502.02175\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Training-free VLA acceleration via temporal KV caching of static visual tokens; 1.7x speedup with negligible SR loss.\"\n    notes: \"Exploits temporal continuity, not token removal. Key difference from our study: caches rather than removes tokens.\"\n\n  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  # ============================================================\n  # Cluster: ViT Token Pruning/Merging (target: 7)\n  # ============================================================\n  - bibtex_key: rao2021dynamicvit\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: \"Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    arxiv_id: \"2106.02034\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction.\"\n    pruning_stats: \"66% token removal, <0.5% accuracy drop, 40%+ throughput improvement.\"\n\n  - bibtex_key: bolya2023tome\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: \"Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy\"\n    year: 2023\n    venue: \"ICLR 2023 (Oral)\"\n    arxiv_id: \"2210.09461\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop.\"\n    pruning_stats: \"2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens.\"\n\n  - bibtex_key: liang2022evit\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: \"Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    arxiv_id: \"2202.07800\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"\n    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"\n    category: \"Closed-Loop Evaluation\"\n    role: foundation\n    verified: true\n    key_finding: \"130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations.\"\n    notes: \"Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task).\"\n\n  - bibtex_key: mees2022calvin\n    title: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\"\n    authors: \"Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram\"\n    year: 2022\n    venue: \"IEEE RA-L\"\n    arxiv_id: \"2112.03227\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives.\"\n\n  - bibtex_key: chi2023diffusionpolicy\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran\"\n    year: 2023\n    venue: \"RSS 2023\"\n    arxiv_id: \"2303.04137\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions.\"\n\n  # ============================================================\n  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)\n  # ============================================================\n  - bibtex_key: zeng2023transformers_tsf\n    title: \"Are Transformers Effective for Time Series Forecasting?\"\n    authors: \"Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang\"\n    year: 2023\n    venue: \"AAAI 2023\"\n    arxiv_id: \"2205.13504\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series.\"\n\n  - bibtex_key: bouthillier2024negative\n    title: \"Position: Embracing Negative Results in Machine Learning\"\n    authors: \"Bouthillier, Xavier and others\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2406.03980\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: background\n    verified: true\n    key_finding: \"Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions.\"\n\n  # ============================================================\n  # Background / Architecture\n  # ============================================================\n  - bibtex_key: zhai2023siglip\n    title: \"Sigmoid Loss for Language Image Pre-Training\"\n    authors: \"Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas\"\n    year: 2023\n    venue: \"ICCV 2023\"\n    arxiv_id: \"2303.15343\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips.\"\n    notes: \"Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token.\"\n\n  - bibtex_key: yang2024qwen2\n    title: \"Qwen2 Technical Report\"\n    authors: \"Yang, An and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2407.10671\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA.\"\n\n  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\"\n",
    "structuredPatch": [
      {
        "oldStart": 136,
        "oldLines": 6,
        "newStart": 136,
        "newLines": 42,
        "lines": [
          "     key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"",
          "     notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"",
          " ",
          "+  - bibtex_key: yang2025efficientvla",
          "+    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"",
          "+    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"",
          "+    year: 2025",
          "+    venue: \"arXiv preprint\"",
          "+    arxiv_id: \"2506.10100\"",
          "+    category: \"VLM/LLM Token Efficiency\"",
          "+    role: direct-competitor",
          "+    verified: true",
          "+    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"",
          "+    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"",
          "+",
          "+  - bibtex_key: liu2025vlapruner",
          "+    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"",
          "+    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"",
          "+    year: 2025",
          "+    venue: \"arXiv preprint\"",
          "+    arxiv_id: \"2511.16449\"",
          "+    category: \"VLM/LLM Token Efficiency\"",
          "+    role: direct-competitor",
          "+    verified: true",
          "+    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"",
          "+    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"",
          "+",
          "+  - bibtex_key: shang2024prumerge",
          "+    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"",
          "+    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"",
          "+    year: 2024",
          "+    venue: \"ICCV 2025\"",
          "+    arxiv_id: \"2403.15388\"",
          "+    category: \"VLM/LLM Token Efficiency\"",
          "+    role: direct-competitor",
          "+    verified: true",
          "+    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"",
          "+    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\"",
          "+",
          "   # ============================================================",
          "   # Cluster: ViT Token Pruning/Merging (target: 7)",
          "   # ============================================================"
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

_source line 36_

已完成。在 `wang2026vlaiap` 后追加了 3 篇论文：

1. **yang2025efficientvla** — EfficientVLA (arXiv 2506.10100): 层剪枝 + token 选择 + 时序缓存，CogACT 上 1.93x 加速
2. **liu2025vlapruner** — VLA-Pruner (arXiv 2511.16449): 双层级 (语义 + 动作注意力) 时序感知 token 剪枝
3. **shang2024prumerge** — LLaVA-PruMerge (arXiv 2403.15388, ICCV 2025): 自适应视觉 token 剪枝 + 合并，4x token 压缩

"VLM/LLM Token Efficiency" cluster 现有 8 篇 (原 5 + 新增 3)，达到 target。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "uuid": "c2579644-8bf0-4450-b61c-6bb66ef8c0be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ky2JzU9CJivnzzh51otvjw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1283,
      "cache_read_input_tokens": 40105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1283
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

_source line 37_

已完成。在 `wang2026vlaiap` 后追加了 3 篇论文：

1. **yang2025efficientvla** — EfficientVLA (arXiv 2506.10100): 层剪枝 + token 选择 + 时序缓存，CogACT 上 1.93x 加速
2. **liu2025vlapruner** — VLA-Pruner (arXiv 2511.16449): 双层级 (语义 + 动作注意力) 时序感知 token 剪枝
3. **shang2024prumerge** — LLaVA-PruMerge (arXiv 2403.15388, ICCV 2025): 自适应视觉 token 剪枝 + 合并，4x token 压缩

"VLM/LLM Token Efficiency" cluster 现有 8 篇 (原 5 + 新增 3)，达到 target。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 99584,
  "duration_api_ms": 120942,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "27d43230-28d0-4486-a217-fb2a388db1d5",
  "total_cost_usd": 0.58579375,
  "usage": {
    "input_tokens": 1826,
    "cache_creation_input_tokens": 29547,
    "cache_read_input_tokens": 251480,
    "output_tokens": 3313,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29547,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 264,
        "cache_read_input_tokens": 40105,
        "cache_creation_input_tokens": 1283,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1283
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 111340,
      "outputTokens": 2418,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 6,
      "costUSD": 0.18342999999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1826,
      "outputTokens": 3313,
      "cacheReadInputTokens": 251480,
      "cacheCreationInputTokens": 29547,
      "webSearchRequests": 0,
      "costUSD": 0.40236375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d7dad785-a05a-4f29-916a-09137dae4275"
}
```

</details>

---
