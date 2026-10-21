# paper research vit pruning gap

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_research_vit_pruning_gap_20260522T230243.log`
- **Structured JSON:** [`e9b364cac4667a5b7a61.json`](../../sessions/e9/e9b364cac4667a5b7a61.json)

## Before a recorded user message

29 recorded events

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
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
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
  "uuid": "5e2668a2-1cf4-438f-b8e4-79b8bab348ae",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/memory/"
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
    "resetsAt": 1779495000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b2f24234-c9e1-492a-a84b-026db0abf56b",
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845"
}
```

---

### Assistant

_source line 4_

I'll find a complementary paper for the ViT Token Pruning/Merging cluster. Let me start by reading the existing literature map and searching for candidates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "c4e9afa9-1585-4a28-8538-299b23ab574c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhmoEjgDkRK1Z5UiMXJbtG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12307
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

<details open><summary>🔧 Tool call — Read · `toolu_014GQvujzqU1QuoRkiCD8Zbd`</summary>

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
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "13474bac-e0ab-4403-b2c8-81a703d2d38e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhmoEjgDkRK1Z5UiMXJbtG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12307
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

_source line 6 · 2026-05-22T23:02:54.211Z_

<details><summary>↩ Tool result · `toolu_014GQvujzqU1QuoRkiCD8Zbd`</summary>

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
139	  - bibtex_key: yang2025efficientvla
140	    title: "EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models"
141	    authors: "Yang, Yantai and Wang, Yuhao and Wen, Zichen and others"
142	    year: 2025
143	    venue: "arXiv preprint"
144	    arxiv_id: "2506.10100"
145	    category: "VLM/LLM Token Efficiency"
146	    role: direct-competitor
147	    verified: true
148	    key_finding: "Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER."
149	    notes: "Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis."
150	
151	  - bibtex_key: liu2025vlapruner
152	    title: "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference"
153	    authors: "Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others"
154	    year: 2025
155	    venue: "arXiv preprint"
156	    arxiv_id: "2511.16449"
157	    category: "VLM/LLM Token Efficiency"
158	    role: direct-competitor
159	    verified: true
160	    key_finding: "Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning."
161	    notes: "VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance."
162	
163	  - bibtex_key: shang2024prumerge
164	    title: "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models"
165	    authors: "Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan"
166	    year: 2024
167	    venue: "ICCV 2025"
168	    arxiv_id: "2403.15388"
169	    category: "VLM/LLM Token Efficiency"
170	    role: direct-competitor
171	    verified: true
172	    key_finding: "Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks."
173	    notes: "VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs."
174	
175	  # ============================================================
176	  # Cluster: ViT Token Pruning/Merging (target: 7)
177	  # ============================================================
178	  - bibtex_key: rao2021dynamicvit
179	    title: "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification"
180	    authors: "Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui"
181	    year: 2021
182	    venue: "NeurIPS 2021"
183	    arxiv_id: "2106.02034"
184	    category: "ViT Token Pruning/Merging"
185	    role: foundation
186	    verified: true
187	    key_finding: "Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction."
188	    pruning_stats: "66% token removal, <0.5% accuracy drop, 40%+ throughput improvement."
189	
190	  - bibtex_key: bolya2023tome
191	    title: "Token Merging: Your ViT But Faster"
192	    authors: "Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy"
193	    year: 2023
194	    venue: "ICLR 2023 (Oral)"
195	    arxiv_id: "2210.09461"
196	    category: "ViT Token Pruning/Merging"
197	    role: foundation
198	    verified: true
199	    key_finding: "Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop."
200	    pruning_stats: "2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens."
201	
202	  - bibtex_key: liang2022evit
203	    title: "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations"
204	    authors: "Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao"
205	    year: 2022
206	    venue: "ICLR 2022"
207	    arxiv_id: "2202.07800"
208	    category: "ViT Token Pruning/Merging"
209	    role: foundation
210	    verified: true
211	    key_finding: "Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens."
212	    pruning_stats: "50% speedup, 0.3% accuracy drop on ImageNet."
213	
214	  # ============================================================
215	  # Cluster: Closed-Loop Evaluation (target: 5)
216	  # ============================================================
217	  - bibtex_key: liu2023libero
218	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
219	    authors: "Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter"
220	    year: 2023
221	    venue: "NeurIPS 2023"
222	    arxiv_id: "2306.03310"
223	    category: "Closed-Loop Evaluation"
224	    role: foundation
225	    verified: true
226	    key_finding: "130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations."
227	    notes: "Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task)."
228	
229	  - bibtex_key: mees2022calvin
230	    title: "CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks"
231	    authors: "Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram"
232	    year: 2022
233	    venue: "IEEE RA-L"
234	    arxiv_id: "2112.03227"
235	    category: "Closed-Loop Evaluation"
236	    role: background
237	    verified: true
238	    key_finding: "Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives."
239	
240	  - bibtex_key: chi2023diffusionpolicy
241	    title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
242	    authors: "Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran"
243	    year: 2023
244	    venue: "RSS 2023"
245	    arxiv_id: "2303.04137"
246	    category: "Closed-Loop Evaluation"
247	    role: background
248	    verified: true
249	    key_finding: "Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions."
250	
251	  # ============================================================
252	  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)
253	  # ============================================================
254	  - bibtex_key: zeng2023transformers_tsf
255	    title: "Are Transformers Effective for Time Series Forecasting?"
256	    authors: "Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang"
257	    year: 2023
258	    venue: "AAAI 2023"
259	    arxiv_id: "2205.13504"
260	    category: "Negative Results & Evaluation Pitfalls"
261	    role: foundation
262	    verified: true
263	    key_finding: "Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series."
264	
265	  - bibtex_key: bouthillier2024negative
266	    title: "Position: Embracing Negative Results in Machine Learning"
267	    authors: "Bouthillier, Xavier and others"
268	    year: 2024
269	    venue: "ICML 2024"
270	    arxiv_id: "2406.03980"
271	    category: "Negative Results & Evaluation Pitfalls"
272	    role: background
273	    verified: true
274	    key_finding: "Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions."
275	
276	  # ============================================================
277	  # Background / Architecture
278	  # ============================================================
279	  - bibtex_key: zhai2023siglip
280	    title: "Sigmoid Loss for Language Image Pre-Training"
281	    authors: "Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas"
282	    year: 2023
283	    venue: "ICCV 2023"
284	    arxiv_id: "2303.15343"
285	    category: "VLA Models"
286	    role: foundation
287	    verified: true
288	    key_finding: "Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips."
289	    notes: "Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token."
290	
291	  - bibtex_key: yang2024qwen2
292	    title: "Qwen2 Technical Report"
293	    authors: "Yang, An and others"
294	    year: 2024
295	    venue: "arXiv preprint"
296	    arxiv_id: "2407.10671"
297	    category: "VLA Models"
298	    role: background
299	    verified: true
300	    key_finding: "0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA."
301	
302	  - bibtex_key: lipman2023flow
303	    title: "Flow Matching for Generative Modeling"
304	    authors: "Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt"
305	    year: 2023
306	    venue: "ICLR 2023"
307	    arxiv_id: "2210.02747"
308	    category: "VLA Models"
309	    role: foundation
310	    verified: true
311	    key_finding: "Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling."
312	    notes: "Action generation mechanism in SmolVLA and pi0."
313	
314	  # ============================================================
315	  # Cluster: Vision Connectors & Token Compression (target: 6)
316	  # ============================================================
317	  - bibtex_key: li2023blip2
318	    title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
319	    authors: "Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven"
320	    year: 2023
321	    venue: "ICML 2023"
322	    arxiv_id: "2301.12597"
323	    category: "Vision Connectors & Token Compression"
324	    role: foundation
325	    verified: true
326	    key_finding: "Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters."
327	    notes: "Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle."
328	
329	  - bibtex_key: alayrac2022flamingo
330	    title: "Flamingo: a Visual Language Model for Few-Shot Learning"
331	    authors: "Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others"
332	    year: 2022
333	    venue: "NeurIPS 2022"
334	    arxiv_id: "2204.14198"
335	    category: "Vision Connectors & Token Compression"
336	    role: foundation
337	    verified: true
338	    key_finding: "Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries."
339	    notes: "Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches."
340	
341	  - bibtex_key: liu2023llava
342	    title: "Visual Instruction Tuning"
343	    authors: "Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae"
344	    year: 2023
345	    venue: "NeurIPS 2023"
346	    arxiv_id: "2304.08485"
347	    category: "Vision Connectors & Token Compression"
348	    role: foundation
349	    verified: true
350	    key_finding: "Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient."
351	    notes: "Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice."
352	
353	  - bibtex_key: shi2016subpixel
354	    title: "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network"
355	    authors: "Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan"
356	    year: 2016
357	    venue: "CVPR 2016"
358	    arxiv_id: "1609.05158"
359	    category: "Vision Connectors & Token Compression"
360	    role: background
361	    verified: true
362	    key_finding: "Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution."
363	    notes: "Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis."
364	
365	  - bibtex_key: chen2024internvl
366	    title: "How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites"
367	    authors: "Chen, Zhe and Wang, Weiyun and Tian, Hao and others"
368	    year: 2024
369	    venue: "arXiv preprint"
370	    arxiv_id: "2404.16821"
371	    category: "Vision Connectors & Token Compression"
372	    role: background
373	    verified: true
374	    key_finding: "InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles."
375	    notes: "Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding."
376	
377	  - bibtex_key: oquab2024dinov2
378	    title: "DINOv2: Learning Robust Visual Features without Supervision"
379	    authors: "Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others"
380	    year: 2024
381	    venue: "TMLR 2024"
382	    arxiv_id: "2304.07193"
383	    category: "Vision Connectors & Token Compression"
384	    role: foundation
385	    verified: true
386	    key_finding: "Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning."
387	    notes: "Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution."
388	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "b549c559-273a-47a6-be5b-f688c5ab465b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
      "content": "# Literature Map — importance_margin_vla_compress\n# Generated: 2026-05-17\n# Citation budget: 35\n\npapers:\n\n  # ============================================================\n  # Cluster: VLA Models (target: 6)\n  # ============================================================\n  - bibtex_key: shukor2025smolvla\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.01844\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64.\"\n    pruning_stats: null\n    notes: \"Our experimental platform. SigLIP encoder produces 128 vision tokens.\"\n\n  - bibtex_key: kim2024openvla\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    arxiv_id: \"2406.09246\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning.\"\n\n  - bibtex_key: zitkovich2023rt2\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others\"\n    year: 2023\n    venue: \"CoRL 2023\"\n    arxiv_id: \"2307.15818\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought.\"\n\n  - bibtex_key: ghosh2024octo\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2405.12213\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"Transformer-based generalist policy trained on 800K trajectories from Open X-Embodiment; effective fine-tuning across 9 robot platforms.\"\n\n  - bibtex_key: black2024pi0\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black, Kevin and Brown, Noah and Driess, Danny and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2410.24164\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"3.3B VLA using flow matching for 50Hz action generation; trained on 10K+ hours of robot data across 7 platforms and 68 tasks.\"\n\n  - bibtex_key: openxembodiment2024\n    title: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\"\n    authors: \"Open X-Embodiment Collaboration\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    arxiv_id: \"2310.08864\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"1M+ real robot trajectories spanning 22 embodiments; RT-1-X shows 50% improvement over single-embodiment baselines.\"\n\n  # ============================================================\n  # Cluster: VLM/LLM Token Efficiency (target: 8)\n  # ============================================================\n  - bibtex_key: chen2024fastv\n    title: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\"\n    authors: \"Chen, Liang and others\"\n    year: 2024\n    venue: \"ECCV 2024 (Oral)\"\n    arxiv_id: null\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Plug-and-play visual token pruning for VLMs; prunes tokens in deep layers based on attention patterns from early layers.\"\n    pruning_stats: \"Prunes ~50% visual tokens with minimal accuracy loss on VLM benchmarks.\"\n\n  - bibtex_key: zhang2023h2o\n    title: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\"\n    authors: \"Zhang, Zhenyu and others\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.14048\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"KV cache eviction retaining heavy-hitter tokens; 20% heavy hitters achieve up to 29x throughput improvement.\"\n\n  - bibtex_key: xiao2024streamingllm\n    title: \"Efficient Streaming Language Models with Attention Sinks\"\n    authors: \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2309.17453\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"Attention sink phenomenon: keeping KV of initial tokens recovers window attention performance; enables stable LLM inference over 4M+ tokens.\"\n\n  - bibtex_key: hsu2025vlacache\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: \"Hsu, Siyu and others\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2502.02175\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Training-free VLA acceleration via temporal KV caching of static visual tokens; 1.7x speedup with negligible SR loss.\"\n    notes: \"Exploits temporal continuity, not token removal. Key difference from our study: caches rather than removes tokens.\"\n\n  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\"\n\n  # ============================================================\n  # Cluster: ViT Token Pruning/Merging (target: 7)\n  # ============================================================\n  - bibtex_key: rao2021dynamicvit\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: \"Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    arxiv_id: \"2106.02034\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction.\"\n    pruning_stats: \"66% token removal, <0.5% accuracy drop, 40%+ throughput improvement.\"\n\n  - bibtex_key: bolya2023tome\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: \"Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy\"\n    year: 2023\n    venue: \"ICLR 2023 (Oral)\"\n    arxiv_id: \"2210.09461\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop.\"\n    pruning_stats: \"2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens.\"\n\n  - bibtex_key: liang2022evit\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: \"Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    arxiv_id: \"2202.07800\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"\n    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"\n    category: \"Closed-Loop Evaluation\"\n    role: foundation\n    verified: true\n    key_finding: \"130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations.\"\n    notes: \"Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task).\"\n\n  - bibtex_key: mees2022calvin\n    title: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\"\n    authors: \"Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram\"\n    year: 2022\n    venue: \"IEEE RA-L\"\n    arxiv_id: \"2112.03227\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives.\"\n\n  - bibtex_key: chi2023diffusionpolicy\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran\"\n    year: 2023\n    venue: \"RSS 2023\"\n    arxiv_id: \"2303.04137\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions.\"\n\n  # ============================================================\n  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)\n  # ============================================================\n  - bibtex_key: zeng2023transformers_tsf\n    title: \"Are Transformers Effective for Time Series Forecasting?\"\n    authors: \"Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang\"\n    year: 2023\n    venue: \"AAAI 2023\"\n    arxiv_id: \"2205.13504\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series.\"\n\n  - bibtex_key: bouthillier2024negative\n    title: \"Position: Embracing Negative Results in Machine Learning\"\n    authors: \"Bouthillier, Xavier and others\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2406.03980\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: background\n    verified: true\n    key_finding: \"Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions.\"\n\n  # ============================================================\n  # Background / Architecture\n  # ============================================================\n  - bibtex_key: zhai2023siglip\n    title: \"Sigmoid Loss for Language Image Pre-Training\"\n    authors: \"Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas\"\n    year: 2023\n    venue: \"ICCV 2023\"\n    arxiv_id: \"2303.15343\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips.\"\n    notes: \"Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token.\"\n\n  - bibtex_key: yang2024qwen2\n    title: \"Qwen2 Technical Report\"\n    authors: \"Yang, An and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2407.10671\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA.\"\n\n  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\"\n",
      "numLines": 388,
      "startLine": 1,
      "totalLines": 388
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01T9DVkkBLbycTRXAm7v5LYw`</summary>

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
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "a0411c01-85f0-438a-8b28-116e18787ddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhmoEjgDkRK1Z5UiMXJbtG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12307,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12307
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

_source line 8 · 2026-05-22T23:02:54.562Z_

<details><summary>↩ Tool result · `toolu_01T9DVkkBLbycTRXAm7v5LYw`</summary>

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
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "477a8ce2-11e1-4adc-aaf3-d0a12d8ffde3",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the existing papers in the ViT Token Pruning/Merging cluster:

1. **DynamicViT** (NeurIPS 2021) - Hierarchical token pruning with learned prediction modules (trained approach)
2. **ToMe** (ICLR 2023) - Training-free token merging via bipartite matching
3. **EViT** (ICLR 2022) - CLS attention-guided token reorganization (trained/finetuned approach)

What's missing? Let me think about complementarity:


- DynamicViT uses learned binary decisions to prune tokens
- ToMe applies similarity-based merging without any training
- EViT leverages CLS attention to identify and fuse less important tokens

A-ViT (Adaptive Tokens for Efficient Vision Transformer, CVPR 2022) would fill a gap nicely—it introduces a halting mechanism where tokens can exit at different layers based on adaptive computation, which is fundamentally different from the pruning and merging approaches already covered. Let me verify those details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "a27f26dd-8def-42d7-8ef2-345ea17823bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zFYYCkr84Ws49Ao1HtkRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 24148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7736
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

_source line 10_

Now let me search for the best complementary paper. The existing three cover: learned pruning (DynamicViT), training-free merging (ToMe), and CLS-attention reorganization (EViT). A paper with a different pruning paradigm would complement well.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "9554d50d-839a-44e1-9a12-273cb139f2b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zFYYCkr84Ws49Ao1HtkRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 24148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7736
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011zcwHFaXdfVajjk6qi2Prz`</summary>

```json
{
  "query": "A-ViT Adaptive Tokens Efficient Vision Transformer CVPR 2022 Yin Hongxu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "79447bb2-0edd-4475-a245-a116fa5068da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016zFYYCkr84Ws49Ao1HtkRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7736,
      "cache_read_input_tokens": 24148,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7736
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

_source line 12 · 2026-05-22T23:03:12.228Z_

<details><summary>↩ Tool result · `toolu_011zcwHFaXdfVajjk6qi2Prz`</summary>

```text
Web search results for query: "A-ViT Adaptive Tokens Efficient Vision Transformer CVPR 2022 Yin Hongxu"

Links: [{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://a-vit.github.io/"},{"title":"A-ViT - CVPR 2022 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2022/html/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.html"},{"title":"GitHub - NVlabs/A-ViT: Official PyTorch implementation of A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022) · GitHub","url":"https://github.com/NVlabs/A-ViT"},{"title":"AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/pdf/2112.07658"},{"title":"[PDF] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-ViT:-Adaptive-Tokens-for-Efficient-Vision-Yin-Vahdat/c2a0c18e810535db52e5ebaf180c64ce70356748"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/363908419_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"},{"title":"A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer | NVIDIA Learning and Perception Research","url":"https://research.nvidia.com/labs/lpr/publication/yin2022avit/"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer | Research","url":"https://research.nvidia.com/publication/2022-06_vit-adaptive-tokens-efficient-vision-transformer"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer | Fundamental Generative AI Research","url":"https://research.nvidia.com/labs/genair/publication/yin2022avit/"}]

Great! I found comprehensive information about A-ViT. Here are the search results:

## A-ViT: Adaptive Tokens for Efficient Vision Transformer

A-ViT was accepted to CVPR 2022 and authored by Hongxu Yin, Arash Vahdat, Jose M. Alvarez, Arun Mallya, Jan Kautz, and Pavlo Molchanov.

**Core Concept:**
A-ViT is a method to enable adaptive token computation for vision transformers, augmenting the vision transformer block with an adaptive halting module that computes a halting probability per token.

**Key Features:**
- The module reuses the parameters of existing blocks and borrows a single neuron from the last dense layer in each block to compute the halting probability, imposing no extra parameters or computations
- By adaptively halting tokens, dense compute is performed only on active tokens deemed informative for the task, resulting in successive blocks in vision transformers gradually receiving fewer tokens and leading to faster inference

**Implementation:**
The official PyTorch implementation was released by NVLabs, and the current version includes training, evaluation, and visualization of models on ImageNet-1K.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "99809ba8-bde5-4eab-b4d3-4a32df34a6a3",
  "tool_use_result": {
    "query": "A-ViT Adaptive Tokens Efficient Vision Transformer CVPR 2022 Yin Hongxu",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AcgtTpzmAGyBQX15CN4j8w",
        "content": [
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://a-vit.github.io/"
          },
          {
            "title": "A-ViT - CVPR 2022 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/html/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.html"
          },
          {
            "title": "GitHub - NVlabs/A-ViT: Official PyTorch implementation of A-ViT: Adaptive Tokens for Efficient Vision Transformer (CVPR 2022) · GitHub",
            "url": "https://github.com/NVlabs/A-ViT"
          },
          {
            "title": "AdaViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://arxiv.org/pdf/2112.07658"
          },
          {
            "title": "[PDF] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-ViT:-Adaptive-Tokens-for-Efficient-Vision-Yin-Vahdat/c2a0c18e810535db52e5ebaf180c64ce70356748"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF",
            "url": "https://www.researchgate.net/publication/363908419_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efﬁcient Vision Transformer Hongxu Yin Arash Vahdat",
            "url": "https://openaccess.thecvf.com/content/CVPR2022/papers/Yin_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer_CVPR_2022_paper.pdf"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer | NVIDIA Learning and Perception Research",
            "url": "https://research.nvidia.com/labs/lpr/publication/yin2022avit/"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer | Research",
            "url": "https://research.nvidia.com/publication/2022-06_vit-adaptive-tokens-efficient-vision-transformer"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer | Fundamental Generative AI Research",
            "url": "https://research.nvidia.com/labs/genair/publication/yin2022avit/"
          }
        ]
      },
      "Great! I found comprehensive information about A-ViT. Here are the search results:\n\n## A-ViT: Adaptive Tokens for Efficient Vision Transformer\n\nA-ViT was accepted to CVPR 2022 and authored by Hongxu Yin, Arash Vahdat, Jose M. Alvarez, Arun Mallya, Jan Kautz, and Pavlo Molchanov.\n\n**Core Concept:**\nA-ViT is a method to enable adaptive token computation for vision transformers, augmenting the vision transformer block with an adaptive halting module that computes a halting probability per token.\n\n**Key Features:**\n- The module reuses the parameters of existing blocks and borrows a single neuron from the last dense layer in each block to compute the halting probability, imposing no extra parameters or computations\n- By adaptively halting tokens, dense compute is performed only on active tokens deemed informative for the task, resulting in successive blocks in vision transformers gradually receiving fewer tokens and leading to faster inference\n\n**Implementation:**\nThe official PyTorch implementation was released by NVLabs, and the current version includes training, evaluation, and visualization of models on ImageNet-1K."
    ],
    "durationSeconds": 4.823464893000001
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
A-ViT is a great complement. Let me verify the arxiv ID and get more specific stats.

The existing papers:
1. DynamicViT - learned binary predictor for pruning (trained)
2. ToMe - training-free bipartite matching merging
3. EViT - CLS attention-based reorganization + token fusing

A-ViT brings:
- Adaptive computation time (ACT) / halting mechanism - tokens halt at different depths
- Per-token adaptive depth (different from all three which operate at fixed layers)
- No extra parameters (reuses existing block parameters)


- NVIDIA Research publication from CVPR 2022, arxiv 2112.07658
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "002ca31b-cf7c-44e3-9877-95019969b5c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M624bLg9VVtK3qpzDqHQXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 31884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1423
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

_source line 14_

A-ViT is a strong complement — it introduces per-token adaptive depth (halting mechanism), which is a fundamentally different paradigm from the fixed-layer pruning/merging in the other three. Let me verify the arxiv ID and citation stats.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "8a19ad85-5c4d-4f26-be23-d2526ec4645a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M624bLg9VVtK3qpzDqHQXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 31884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1423
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MPRyLfZB3hJyT3eSMmbmeo`</summary>

```json
{
  "query": "arxiv 2112.07658 A-ViT adaptive tokens vision transformer citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "0aa60db7-ed7d-41c2-930e-b6548fc46f4f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M624bLg9VVtK3qpzDqHQXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1423,
      "cache_read_input_tokens": 31884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1423
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

_source line 16 · 2026-05-22T23:03:31.428Z_

<details><summary>↩ Tool result · `toolu_01MPRyLfZB3hJyT3eSMmbmeo`</summary>

```text
Web search results for query: "arxiv 2112.07658 A-ViT adaptive tokens vision transformer citations"

Links: [{"title":"[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658"},{"title":"AdaViT: Adaptive Tokens for Efficient Vision Transformer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211207658Y/abstract"},{"title":"[2112.07658v3] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v3"},{"title":"[2112.07658] A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://ar5iv.labs.arxiv.org/html/2112.07658"},{"title":"[2112.07658v1] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v1"},{"title":"[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"}]

Based on the search results, here's information about arxiv 2112.07658:

## Paper Overview

The paper is titled "AdaViT: Adaptive Tokens for Efficient Vision Transformer" by authors Hongxu Yin, Arash Vahdat, Jose Alvarez, Arun Mallya, Jan Kautz, and Pavlo Molchanov.

## Main Contribution

A-ViT is a method that adaptively adjusts the inference cost of vision transformers for images of different complexity by automatically reducing the number of tokens that are processed in the network as inference proceeds.

## Technical Approach

The method reformulates Adaptive Computation Time (ACT) for this task, extending halting to discard redundant spatial tokens. A-ViT requires no extra parameters or sub-network for halting, as it bases the learning of adaptive halting on the original network parameters, and introduces distributional prior regularization that stabilizes training compared to prior ACT approaches.

## Paper Status

The paper was accepted as an oral presentation at CVPR'22 and was submitted on December 14, 2021, with the latest revision (v3) on October 5, 2022.

Regarding citations to this paper, the search results do not provide specific citation count information. You can check the arXiv page directly or use citation aggregators like Google Scholar for current citation metrics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "6efcf24d-7c33-47fe-b09b-66748fbddc86",
  "tool_use_result": {
    "query": "arxiv 2112.07658 A-ViT adaptive tokens vision transformer citations",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TksuARbLB8kTWRNQGabDeG",
        "content": [
          {
            "title": "[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://arxiv.org/abs/2112.07658"
          },
          {
            "title": "AdaViT: Adaptive Tokens for Efficient Vision Transformer - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2021arXiv211207658Y/abstract"
          },
          {
            "title": "[2112.07658v3] AdaViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://arxiv.org/abs/2112.07658v3"
          },
          {
            "title": "[2112.07658] A-ViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://ar5iv.labs.arxiv.org/html/2112.07658"
          },
          {
            "title": "[2112.07658v1] AdaViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://arxiv.org/abs/2112.07658v1"
          },
          {
            "title": "[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF",
            "url": "https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"
          }
        ]
      },
      "Based on the search results, here's information about arxiv 2112.07658:\n\n## Paper Overview\n\nThe paper is titled \"AdaViT: Adaptive Tokens for Efficient Vision Transformer\" by authors Hongxu Yin, Arash Vahdat, Jose Alvarez, Arun Mallya, Jan Kautz, and Pavlo Molchanov.\n\n## Main Contribution\n\nA-ViT is a method that adaptively adjusts the inference cost of vision transformers for images of different complexity by automatically reducing the number of tokens that are processed in the network as inference proceeds.\n\n## Technical Approach\n\nThe method reformulates Adaptive Computation Time (ACT) for this task, extending halting to discard redundant spatial tokens. A-ViT requires no extra parameters or sub-network for halting, as it bases the learning of adaptive halting on the original network parameters, and introduces distributional prior regularization that stabilizes training compared to prior ACT approaches.\n\n## Paper Status\n\nThe paper was accepted as an oral presentation at CVPR'22 and was submitted on December 14, 2021, with the latest revision (v3) on October 5, 2022.\n\nRegarding citations to this paper, the search results do not provide specific citation count information. You can check the arXiv page directly or use citation aggregators like Google Scholar for current citation metrics."
    ],
    "durationSeconds": 9.445811588999998
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
A-ViT (CVPR 2022 Oral) is an excellent complement. Key details:
- arxiv_id: 2112.07658
- Title: "A-ViT: Adaptive Tokens for Efficient Vision Transformer" (published name, originally "AdaViT" on arxiv)
- Authors: Hongxu Yin, Arash Vahdat, Jose Alvarez, Arun Mallya, Jan Kautz, Pavlo Molchanov


- Venue: CVPR 2022 (Oral)

The core innovation is Adaptive Computation Time halting, where individual tokens exit the network at different layers based on learned probabilities rather than following a fixed depth. This creates a fundamentally different efficiency axis compared to the other approaches: DynamicViT uses learned pruning at fixed layers, ToMe applies training-free merging throughout, and EViT reorganizes tokens based on CLS attention, but A-ViT uniquely enables per-token adaptive depth.

The key insight for our VLA work is that this reframes the question from "which tokens matter at this layer" to "how deep should this token go," revealing that token importance isn't uniform across the network's depth and directly informs how pruning decisions cascade through different pipeline stages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "43f36fa6-602a-49b3-be20-8dd74407730c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1stFy4Y1TnETN11FBx3sr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 33307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1013
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PAWBtFQGU3mRwEcf3VZGUR`</summary>

```json
{
  "query": "A-ViT CVPR 2022 oral ImageNet accuracy FLOPs reduction token halting results DeiT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "401f657c-1cbe-4bca-8ebd-44f4c5e2ce48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H1stFy4Y1TnETN11FBx3sr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1013,
      "cache_read_input_tokens": 33307,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1013
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

_source line 19 · 2026-05-22T23:03:53.506Z_

<details><summary>↩ Tool result · `toolu_01PAWBtFQGU3mRwEcf3VZGUR`</summary>

```text
Web search results for query: "A-ViT CVPR 2022 oral ImageNet accuracy FLOPs reduction token halting results DeiT"

Links: [{"title":"[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"},{"title":"AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/pdf/2112.07658"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://a-vit.github.io/"},{"title":"LookupViT: Compressing visual information to a limited number of tokens","url":"https://arxiv.org/pdf/2407.12753"},{"title":"Global Vision Transformer Pruning with Hessian-Aware Saliency","url":"https://arxiv.org/pdf/2110.04869"},{"title":"VTC-LFC: Vision Transformer Compression with Low-Frequency Components","url":"https://papers.neurips.cc/paper_files/paper/2022/file/5a8177df23bdcc15a02a6739f5b9dd4a-Paper-Conference.pdf"},{"title":"Vision Transformer with Attention Map Hallucination and FFN Compaction","url":"https://arxiv.org/pdf/2306.10875"}]

Based on the search results, here are the key findings about A-ViT from CVPR 2022:

## A-ViT: Adaptive Tokens for Efficient Vision Transformer

A-ViT is a method that adaptively adjusts the inference cost of vision transformer (ViT) for images of different complexity by automatically reducing the number of tokens in vision transformers that are processed in the network as inference proceeds.

### Technical Approach
A-ViT reformulates Adaptive Computation Time (ACT) for this task, extending halting to discard redundant spatial tokens. The method requires no extra parameters or sub-network for halting, as it bases the learning of adaptive halting on the original network parameters. A-ViT introduces distributional prior regularization that stabilizes training compared to prior ACT approaches.

### Results on ImageNet
The proposed method improves the throughput of DeiT-Tiny by 62% and DeiT-Small by 38% with only 0.3% accuracy drop, outperforming prior art by a large margin.

The paper demonstrates that learnt token halting varies across images, yet aligns surprisingly well with image semantics.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "a69515a6-e981-4439-bb4d-cc29ef83ace5",
  "tool_use_result": {
    "query": "A-ViT CVPR 2022 oral ImageNet accuracy FLOPs reduction token halting results DeiT",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MM7qkp2khiFD7hX3eUBe9U",
        "content": [
          {
            "title": "[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF",
            "url": "https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"
          },
          {
            "title": "AdaViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://arxiv.org/pdf/2112.07658"
          },
          {
            "title": "A-ViT: Adaptive Tokens for Efficient Vision Transformer",
            "url": "https://a-vit.github.io/"
          },
          {
            "title": "LookupViT: Compressing visual information to a limited number of tokens",
            "url": "https://arxiv.org/pdf/2407.12753"
          },
          {
            "title": "Global Vision Transformer Pruning with Hessian-Aware Saliency",
            "url": "https://arxiv.org/pdf/2110.04869"
          },
          {
            "title": "VTC-LFC: Vision Transformer Compression with Low-Frequency Components",
            "url": "https://papers.neurips.cc/paper_files/paper/2022/file/5a8177df23bdcc15a02a6739f5b9dd4a-Paper-Conference.pdf"
          },
          {
            "title": "Vision Transformer with Attention Map Hallucination and FFN Compaction",
            "url": "https://arxiv.org/pdf/2306.10875"
          }
        ]
      },
      "Based on the search results, here are the key findings about A-ViT from CVPR 2022:\n\n## A-ViT: Adaptive Tokens for Efficient Vision Transformer\n\nA-ViT is a method that adaptively adjusts the inference cost of vision transformer (ViT) for images of different complexity by automatically reducing the number of tokens in vision transformers that are processed in the network as inference proceeds.\n\n### Technical Approach\nA-ViT reformulates Adaptive Computation Time (ACT) for this task, extending halting to discard redundant spatial tokens. The method requires no extra parameters or sub-network for halting, as it bases the learning of adaptive halting on the original network parameters. A-ViT introduces distributional prior regularization that stabilizes training compared to prior ACT approaches.\n\n### Results on ImageNet\nThe proposed method improves the throughput of DeiT-Tiny by 62% and DeiT-Small by 38% with only 0.3% accuracy drop, outperforming prior art by a large margin.\n\nThe paper demonstrates that learnt token halting varies across images, yet aligns surprisingly well with image semantics."
    ],
    "durationSeconds": 9.393981263000002
  }
}
```

</details>

---

### Assistant

_source line 20_

Good — I have all the details. A-ViT achieves 62% throughput improvement on DeiT-T and 38% on DeiT-S with only 0.3% accuracy drop. Now let me add it to the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "1005558e-0f39-4108-8347-2baad0c7825a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tJ5T3S8ZcbFtVCKGAwXk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1110,
      "cache_read_input_tokens": 34320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1110
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01S2X9KxBKQ48m6mxAUydo78`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
  "offset": 208,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "753d5778-e6ea-4bc6-ac31-8549478b90ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tJ5T3S8ZcbFtVCKGAwXk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1110,
      "cache_read_input_tokens": 34320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1110
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

_source line 22 · 2026-05-22T23:03:59.005Z_

<details><summary>↩ Tool result · `toolu_01S2X9KxBKQ48m6mxAUydo78`</summary>

```text
208	    category: "ViT Token Pruning/Merging"
209	    role: foundation
210	    verified: true
211	    key_finding: "Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens."
212	    pruning_stats: "50% speedup, 0.3% accuracy drop on ImageNet."
213	
214	  # ============================================================
215	  # Cluster: Closed-Loop Evaluation (target: 5)
216	  # ============================================================
217	  - bibtex_key: liu2023libero
218	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
219	    authors: "Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter"
220	    year: 2023
221	    venue: "NeurIPS 2023"
222	    arxiv_id: "2306.03310"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "eb124b52-967c-4456-98ee-9a13d8e5268a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
      "content": "    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"\n    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"",
      "numLines": 15,
      "startLine": 208,
      "totalLines": 388
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01BjjuUNrZDegwrmKa5B2YEv`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
  "old_string": "    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================",
  "new_string": "    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  - bibtex_key: yin2022avit\n    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"\n    authors: \"Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo\"\n    year: 2022\n    venue: \"CVPR 2022 (Oral)\"\n    arxiv_id: \"2112.07658\"\n    category: \"ViT Token Pruning/Merging\"\n    role: background\n    verified: true\n    key_finding: \"Per-token adaptive depth via ACT halting — tokens exit at different layers based on learned halting probability. 62% throughput gain on DeiT-T, 38% on DeiT-S with 0.3% accuracy drop.\"\n    pruning_stats: \"62% throughput improvement (DeiT-T), 38% (DeiT-S), 0.3% accuracy drop. No extra parameters.\"\n    notes: \"Complements fixed-layer pruning (DynamicViT, EViT) and merging (ToMe) by introducing depth-adaptive token halting. Relevant to our analysis of how token importance varies across transformer depth.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "ee58b5c8-931a-4e1e-82b8-428d267be520",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N6XQeFvUYZZKh1tYFm9ndf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 35430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
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

_source line 24 · 2026-05-22T23:04:08.907Z_

<details><summary>↩ Tool result · `toolu_01BjjuUNrZDegwrmKa5B2YEv`</summary>

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
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "e34266a6-a62e-4e88-acaf-2ce0732ec678",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
    "oldString": "    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================",
    "newString": "    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  - bibtex_key: yin2022avit\n    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"\n    authors: \"Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo\"\n    year: 2022\n    venue: \"CVPR 2022 (Oral)\"\n    arxiv_id: \"2112.07658\"\n    category: \"ViT Token Pruning/Merging\"\n    role: background\n    verified: true\n    key_finding: \"Per-token adaptive depth via ACT halting — tokens exit at different layers based on learned halting probability. 62% throughput gain on DeiT-T, 38% on DeiT-S with 0.3% accuracy drop.\"\n    pruning_stats: \"62% throughput improvement (DeiT-T), 38% (DeiT-S), 0.3% accuracy drop. No extra parameters.\"\n    notes: \"Complements fixed-layer pruning (DynamicViT, EViT) and merging (ToMe) by introducing depth-adaptive token halting. Relevant to our analysis of how token importance varies across transformer depth.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================",
    "originalFile": "# Literature Map — importance_margin_vla_compress\n# Generated: 2026-05-17\n# Citation budget: 35\n\npapers:\n\n  # ============================================================\n  # Cluster: VLA Models (target: 6)\n  # ============================================================\n  - bibtex_key: shukor2025smolvla\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.01844\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64.\"\n    pruning_stats: null\n    notes: \"Our experimental platform. SigLIP encoder produces 128 vision tokens.\"\n\n  - bibtex_key: kim2024openvla\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    arxiv_id: \"2406.09246\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning.\"\n\n  - bibtex_key: zitkovich2023rt2\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others\"\n    year: 2023\n    venue: \"CoRL 2023\"\n    arxiv_id: \"2307.15818\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought.\"\n\n  - bibtex_key: ghosh2024octo\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2405.12213\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"Transformer-based generalist policy trained on 800K trajectories from Open X-Embodiment; effective fine-tuning across 9 robot platforms.\"\n\n  - bibtex_key: black2024pi0\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black, Kevin and Brown, Noah and Driess, Danny and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2410.24164\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"3.3B VLA using flow matching for 50Hz action generation; trained on 10K+ hours of robot data across 7 platforms and 68 tasks.\"\n\n  - bibtex_key: openxembodiment2024\n    title: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\"\n    authors: \"Open X-Embodiment Collaboration\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    arxiv_id: \"2310.08864\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"1M+ real robot trajectories spanning 22 embodiments; RT-1-X shows 50% improvement over single-embodiment baselines.\"\n\n  # ============================================================\n  # Cluster: VLM/LLM Token Efficiency (target: 8)\n  # ============================================================\n  - bibtex_key: chen2024fastv\n    title: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\"\n    authors: \"Chen, Liang and others\"\n    year: 2024\n    venue: \"ECCV 2024 (Oral)\"\n    arxiv_id: null\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Plug-and-play visual token pruning for VLMs; prunes tokens in deep layers based on attention patterns from early layers.\"\n    pruning_stats: \"Prunes ~50% visual tokens with minimal accuracy loss on VLM benchmarks.\"\n\n  - bibtex_key: zhang2023h2o\n    title: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\"\n    authors: \"Zhang, Zhenyu and others\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.14048\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"KV cache eviction retaining heavy-hitter tokens; 20% heavy hitters achieve up to 29x throughput improvement.\"\n\n  - bibtex_key: xiao2024streamingllm\n    title: \"Efficient Streaming Language Models with Attention Sinks\"\n    authors: \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2309.17453\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"Attention sink phenomenon: keeping KV of initial tokens recovers window attention performance; enables stable LLM inference over 4M+ tokens.\"\n\n  - bibtex_key: hsu2025vlacache\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: \"Hsu, Siyu and others\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2502.02175\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Training-free VLA acceleration via temporal KV caching of static visual tokens; 1.7x speedup with negligible SR loss.\"\n    notes: \"Exploits temporal continuity, not token removal. Key difference from our study: caches rather than removes tokens.\"\n\n  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\"\n\n  # ============================================================\n  # Cluster: ViT Token Pruning/Merging (target: 7)\n  # ============================================================\n  - bibtex_key: rao2021dynamicvit\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: \"Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    arxiv_id: \"2106.02034\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction.\"\n    pruning_stats: \"66% token removal, <0.5% accuracy drop, 40%+ throughput improvement.\"\n\n  - bibtex_key: bolya2023tome\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: \"Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy\"\n    year: 2023\n    venue: \"ICLR 2023 (Oral)\"\n    arxiv_id: \"2210.09461\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop.\"\n    pruning_stats: \"2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens.\"\n\n  - bibtex_key: liang2022evit\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: \"Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    arxiv_id: \"2202.07800\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"\n    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"\n    category: \"Closed-Loop Evaluation\"\n    role: foundation\n    verified: true\n    key_finding: \"130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations.\"\n    notes: \"Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task).\"\n\n  - bibtex_key: mees2022calvin\n    title: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\"\n    authors: \"Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram\"\n    year: 2022\n    venue: \"IEEE RA-L\"\n    arxiv_id: \"2112.03227\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives.\"\n\n  - bibtex_key: chi2023diffusionpolicy\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran\"\n    year: 2023\n    venue: \"RSS 2023\"\n    arxiv_id: \"2303.04137\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions.\"\n\n  # ============================================================\n  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)\n  # ============================================================\n  - bibtex_key: zeng2023transformers_tsf\n    title: \"Are Transformers Effective for Time Series Forecasting?\"\n    authors: \"Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang\"\n    year: 2023\n    venue: \"AAAI 2023\"\n    arxiv_id: \"2205.13504\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series.\"\n\n  - bibtex_key: bouthillier2024negative\n    title: \"Position: Embracing Negative Results in Machine Learning\"\n    authors: \"Bouthillier, Xavier and others\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2406.03980\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: background\n    verified: true\n    key_finding: \"Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions.\"\n\n  # ============================================================\n  # Background / Architecture\n  # ============================================================\n  - bibtex_key: zhai2023siglip\n    title: \"Sigmoid Loss for Language Image Pre-Training\"\n    authors: \"Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas\"\n    year: 2023\n    venue: \"ICCV 2023\"\n    arxiv_id: \"2303.15343\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips.\"\n    notes: \"Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token.\"\n\n  - bibtex_key: yang2024qwen2\n    title: \"Qwen2 Technical Report\"\n    authors: \"Yang, An and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2407.10671\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA.\"\n\n  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\"\n",
    "structuredPatch": [
      {
        "oldStart": 211,
        "oldLines": 6,
        "newStart": 211,
        "newLines": 19,
        "lines": [
          "     key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"",
          "     pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"",
          " ",
          "+  - bibtex_key: yin2022avit",
          "+    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"",
          "+    authors: \"Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo\"",
          "+    year: 2022",
          "+    venue: \"CVPR 2022 (Oral)\"",
          "+    arxiv_id: \"2112.07658\"",
          "+    category: \"ViT Token Pruning/Merging\"",
          "+    role: background",
          "+    verified: true",
          "+    key_finding: \"Per-token adaptive depth via ACT halting — tokens exit at different layers based on learned halting probability. 62% throughput gain on DeiT-T, 38% on DeiT-S with 0.3% accuracy drop.\"",
          "+    pruning_stats: \"62% throughput improvement (DeiT-T), 38% (DeiT-S), 0.3% accuracy drop. No extra parameters.\"",
          "+    notes: \"Complements fixed-layer pruning (DynamicViT, EViT) and merging (ToMe) by introducing depth-adaptive token halting. Relevant to our analysis of how token importance varies across transformer depth.\"",
          "+",
          "   # ============================================================",
          "   # Cluster: Closed-Loop Evaluation (target: 5)",
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

_source line 25_

Let me verify the entry was added correctly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "40d9d01d-c756-4215-9e6e-25a4c53c6c75",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsspnKpbLxuXnCgoF8jHJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 36006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
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

<details open><summary>🔧 Tool call — Read · `toolu_01Lbk7Wz7XyvxnMc4kkDUAc3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
  "offset": 213,
  "limit": 18
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "f337e4ce-0a06-4f18-a31d-d17db943ef95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EsspnKpbLxuXnCgoF8jHJ7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 36006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
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

_source line 27 · 2026-05-22T23:04:12.027Z_

<details><summary>↩ Tool result · `toolu_01Lbk7Wz7XyvxnMc4kkDUAc3`</summary>

```text
213	
214	  - bibtex_key: yin2022avit
215	    title: "A-ViT: Adaptive Tokens for Efficient Vision Transformer"
216	    authors: "Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo"
217	    year: 2022
218	    venue: "CVPR 2022 (Oral)"
219	    arxiv_id: "2112.07658"
220	    category: "ViT Token Pruning/Merging"
221	    role: background
222	    verified: true
223	    key_finding: "Per-token adaptive depth via ACT halting — tokens exit at different layers based on learned halting probability. 62% throughput gain on DeiT-T, 38% on DeiT-S with 0.3% accuracy drop."
224	    pruning_stats: "62% throughput improvement (DeiT-T), 38% (DeiT-S), 0.3% accuracy drop. No extra parameters."
225	    notes: "Complements fixed-layer pruning (DynamicViT, EViT) and merging (ToMe) by introducing depth-adaptive token halting. Relevant to our analysis of how token importance varies across transformer depth."
226	
227	  # ============================================================
228	  # Cluster: Closed-Loop Evaluation (target: 5)
229	  # ============================================================
230	  - bibtex_key: liu2023libero
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "2f775f41-a941-4272-8195-8cdd9400bd72",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
      "content": "\n  - bibtex_key: yin2022avit\n    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"\n    authors: \"Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo\"\n    year: 2022\n    venue: \"CVPR 2022 (Oral)\"\n    arxiv_id: \"2112.07658\"\n    category: \"ViT Token Pruning/Merging\"\n    role: background\n    verified: true\n    key_finding: \"Per-token adaptive depth via ACT halting — tokens exit at different layers based on learned halting probability. 62% throughput gain on DeiT-T, 38% on DeiT-S with 0.3% accuracy drop.\"\n    pruning_stats: \"62% throughput improvement (DeiT-T), 38% (DeiT-S), 0.3% accuracy drop. No extra parameters.\"\n    notes: \"Complements fixed-layer pruning (DynamicViT, EViT) and merging (ToMe) by introducing depth-adaptive token halting. Relevant to our analysis of how token importance varies across transformer depth.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero",
      "numLines": 18,
      "startLine": 213,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

Entry added and verified. Here's the summary:

**Added:** `yin2022avit` — *A-ViT: Adaptive Tokens for Efficient Vision Transformer*, CVPR 2022 (Oral)

**Why it complements the existing 3:**

| Paper | Mechanism |
|-------|-----------|
| DynamicViT | Learned binary pruning predictor at **fixed layers** |
| EViT | CLS-attention reorganization at **fixed layers** |
| ToMe | Training-free bipartite **merging** at every layer |
| **A-ViT** | Per-token **adaptive depth** via ACT halting — tokens exit at **different layers** |

A-ViT introduces a fundamentally different axis: instead of deciding *which tokens to remove at a given layer*, it asks *how deep should each token be processed*. This is directly relevant to our VLA token pruning analysis because it highlights that token importance varies across transformer depth — connecting to our investigation of how pruning at different stages of the VLA pipeline produces different failure modes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "uuid": "ecb6c48c-a4a6-41db-97bf-fe5a9b0f099d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0148iEfaCg6sSHj3LkTBF49i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 539,
      "cache_read_input_tokens": 36625,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 539
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

_source line 29_

Entry added and verified. Here's the summary:

**Added:** `yin2022avit` — *A-ViT: Adaptive Tokens for Efficient Vision Transformer*, CVPR 2022 (Oral)

**Why it complements the existing 3:**

| Paper | Mechanism |
|-------|-----------|
| DynamicViT | Learned binary pruning predictor at **fixed layers** |
| EViT | CLS-attention reorganization at **fixed layers** |
| ToMe | Training-free bipartite **merging** at every layer |
| **A-ViT** | Per-token **adaptive depth** via ACT halting — tokens exit at **different layers** |

A-ViT introduces a fundamentally different axis: instead of deciding *which tokens to remove at a given layer*, it asks *how deep should each token be processed*. This is directly relevant to our VLA token pruning analysis because it highlights that token importance varies across transformer depth — connecting to our investigation of how pruning at different stages of the VLA pipeline produces different failure modes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 92721,
  "duration_api_ms": 93872,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "3edbfaa2-e34b-4713-a1a6-f2b0de3b2845",
  "total_cost_usd": 0.4098442500000001,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 25323,
    "cache_read_input_tokens": 243561,
    "output_tokens": 2488,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25323,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 250,
        "cache_read_input_tokens": 36625,
        "cache_creation_input_tokens": 539,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 539
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 30760,
      "outputTokens": 1355,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.06753500000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 2488,
      "cacheReadInputTokens": 243561,
      "cacheCreationInputTokens": 25323,
      "webSearchRequests": 0,
      "costUSD": 0.34230925000000006,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "70378820-1686-43a3-9fc4-eecbd5bcaf34"
}
```

</details>

---
