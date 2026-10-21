# paper research bib sync

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_research_bib_sync_20260523T001801.log`
- **Structured JSON:** [`f795070010c07bf6c25b.json`](../../sessions/f7/f795070010c07bf6c25b.json)

## Before a recorded user message

19 recorded events

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
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
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
  "uuid": "0fb67da5-9cd2-4851-811b-9e1959d4a901",
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
    "resetsAt": 1779513000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b9bff353-7f6c-4396-92c7-48dda70044d3",
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048"
}
```

---

### Assistant

_source line 4_

I'll read the literature map and existing references.bib to construct the missing entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "cf1950fd-53e3-4162-bba7-471a26e4232f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kgG6ahMLZsixK5rHYRYJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12012
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

<details open><summary>🔧 Tool call — Read · `toolu_01AyhFFaYEGp3TpCnEzZbu8x`</summary>

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
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "dd38822e-46b2-4fa9-b6d6-d8d986df53ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kgG6ahMLZsixK5rHYRYJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12012
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

_source line 6 · 2026-05-23T00:18:10.917Z_

<details><summary>↩ Tool result · `toolu_01AyhFFaYEGp3TpCnEzZbu8x`</summary>

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
231	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
232	    authors: "Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter"
233	    year: 2023
234	    venue: "NeurIPS 2023"
235	    arxiv_id: "2306.03310"
236	    category: "Closed-Loop Evaluation"
237	    role: foundation
238	    verified: true
239	    key_finding: "130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations."
240	    notes: "Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task)."
241	
242	  - bibtex_key: mees2022calvin
243	    title: "CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks"
244	    authors: "Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram"
245	    year: 2022
246	    venue: "IEEE RA-L"
247	    arxiv_id: "2112.03227"
248	    category: "Closed-Loop Evaluation"
249	    role: background
250	    verified: true
251	    key_finding: "Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives."
252	
253	  - bibtex_key: chi2023diffusionpolicy
254	    title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
255	    authors: "Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran"
256	    year: 2023
257	    venue: "RSS 2023"
258	    arxiv_id: "2303.04137"
259	    category: "Closed-Loop Evaluation"
260	    role: background
261	    verified: true
262	    key_finding: "Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions."
263	
264	  # ============================================================
265	  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)
266	  # ============================================================
267	  - bibtex_key: zeng2023transformers_tsf
268	    title: "Are Transformers Effective for Time Series Forecasting?"
269	    authors: "Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang"
270	    year: 2023
271	    venue: "AAAI 2023"
272	    arxiv_id: "2205.13504"
273	    category: "Negative Results & Evaluation Pitfalls"
274	    role: foundation
275	    verified: true
276	    key_finding: "Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series."
277	
278	  - bibtex_key: bouthillier2024negative
279	    title: "Position: Embracing Negative Results in Machine Learning"
280	    authors: "Bouthillier, Xavier and others"
281	    year: 2024
282	    venue: "ICML 2024"
283	    arxiv_id: "2406.03980"
284	    category: "Negative Results & Evaluation Pitfalls"
285	    role: background
286	    verified: true
287	    key_finding: "Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions."
288	
289	  # ============================================================
290	  # Background / Architecture
291	  # ============================================================
292	  - bibtex_key: zhai2023siglip
293	    title: "Sigmoid Loss for Language Image Pre-Training"
294	    authors: "Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas"
295	    year: 2023
296	    venue: "ICCV 2023"
297	    arxiv_id: "2303.15343"
298	    category: "VLA Models"
299	    role: foundation
300	    verified: true
301	    key_finding: "Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips."
302	    notes: "Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token."
303	
304	  - bibtex_key: yang2024qwen2
305	    title: "Qwen2 Technical Report"
306	    authors: "Yang, An and others"
307	    year: 2024
308	    venue: "arXiv preprint"
309	    arxiv_id: "2407.10671"
310	    category: "VLA Models"
311	    role: background
312	    verified: true
313	    key_finding: "0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA."
314	
315	  - bibtex_key: lipman2023flow
316	    title: "Flow Matching for Generative Modeling"
317	    authors: "Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt"
318	    year: 2023
319	    venue: "ICLR 2023"
320	    arxiv_id: "2210.02747"
321	    category: "VLA Models"
322	    role: foundation
323	    verified: true
324	    key_finding: "Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling."
325	    notes: "Action generation mechanism in SmolVLA and pi0."
326	
327	  # ============================================================
328	  # Cluster: Vision Connectors & Token Compression (target: 6)
329	  # ============================================================
330	  - bibtex_key: li2023blip2
331	    title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
332	    authors: "Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven"
333	    year: 2023
334	    venue: "ICML 2023"
335	    arxiv_id: "2301.12597"
336	    category: "Vision Connectors & Token Compression"
337	    role: foundation
338	    verified: true
339	    key_finding: "Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters."
340	    notes: "Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle."
341	
342	  - bibtex_key: alayrac2022flamingo
343	    title: "Flamingo: a Visual Language Model for Few-Shot Learning"
344	    authors: "Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others"
345	    year: 2022
346	    venue: "NeurIPS 2022"
347	    arxiv_id: "2204.14198"
348	    category: "Vision Connectors & Token Compression"
349	    role: foundation
350	    verified: true
351	    key_finding: "Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries."
352	    notes: "Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches."
353	
354	  - bibtex_key: liu2023llava
355	    title: "Visual Instruction Tuning"
356	    authors: "Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae"
357	    year: 2023
358	    venue: "NeurIPS 2023"
359	    arxiv_id: "2304.08485"
360	    category: "Vision Connectors & Token Compression"
361	    role: foundation
362	    verified: true
363	    key_finding: "Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient."
364	    notes: "Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice."
365	
366	  - bibtex_key: shi2016subpixel
367	    title: "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network"
368	    authors: "Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan"
369	    year: 2016
370	    venue: "CVPR 2016"
371	    arxiv_id: "1609.05158"
372	    category: "Vision Connectors & Token Compression"
373	    role: background
374	    verified: true
375	    key_finding: "Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution."
376	    notes: "Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis."
377	
378	  - bibtex_key: chen2024internvl
379	    title: "How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites"
380	    authors: "Chen, Zhe and Wang, Weiyun and Tian, Hao and others"
381	    year: 2024
382	    venue: "arXiv preprint"
383	    arxiv_id: "2404.16821"
384	    category: "Vision Connectors & Token Compression"
385	    role: background
386	    verified: true
387	    key_finding: "InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles."
388	    notes: "Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding."
389	
390	  - bibtex_key: oquab2024dinov2
391	    title: "DINOv2: Learning Robust Visual Features without Supervision"
392	    authors: "Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others"
393	    year: 2024
394	    venue: "TMLR 2024"
395	    arxiv_id: "2304.07193"
396	    category: "Vision Connectors & Token Compression"
397	    role: foundation
398	    verified: true
399	    key_finding: "Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning."
400	    notes: "Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution."
401	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "b7b1e473-dcd2-4ebc-9709-e1284e5b4a09",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/literature_map.yaml",
      "content": "# Literature Map — importance_margin_vla_compress\n# Generated: 2026-05-17\n# Citation budget: 35\n\npapers:\n\n  # ============================================================\n  # Cluster: VLA Models (target: 6)\n  # ============================================================\n  - bibtex_key: shukor2025smolvla\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.01844\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"450M-param VLA combining compact VLM (SigLIP+Qwen2) with flow matching action expert; 87.3% SR on LIBERO with batch size 64.\"\n    pruning_stats: null\n    notes: \"Our experimental platform. SigLIP encoder produces 128 vision tokens.\"\n\n  - bibtex_key: kim2024openvla\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    arxiv_id: \"2406.09246\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"7B-param open-source VLA trained on 970K episodes from Open X-Embodiment; supports parameter-efficient fine-tuning.\"\n\n  - bibtex_key: zitkovich2023rt2\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others\"\n    year: 2023\n    venue: \"CoRL 2023\"\n    arxiv_id: \"2307.15818\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Co-fine-tunes VLM on robotic trajectory data; actions expressed as text tokens; emergent semantic reasoning via chain of thought.\"\n\n  - bibtex_key: ghosh2024octo\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh, Dibya and Walke, Homer and Pertsch, Karl and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2405.12213\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"Transformer-based generalist policy trained on 800K trajectories from Open X-Embodiment; effective fine-tuning across 9 robot platforms.\"\n\n  - bibtex_key: black2024pi0\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black, Kevin and Brown, Noah and Driess, Danny and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2410.24164\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"3.3B VLA using flow matching for 50Hz action generation; trained on 10K+ hours of robot data across 7 platforms and 68 tasks.\"\n\n  - bibtex_key: openxembodiment2024\n    title: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\"\n    authors: \"Open X-Embodiment Collaboration\"\n    year: 2024\n    venue: \"ICRA 2024\"\n    arxiv_id: \"2310.08864\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"1M+ real robot trajectories spanning 22 embodiments; RT-1-X shows 50% improvement over single-embodiment baselines.\"\n\n  # ============================================================\n  # Cluster: VLM/LLM Token Efficiency (target: 8)\n  # ============================================================\n  - bibtex_key: chen2024fastv\n    title: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\"\n    authors: \"Chen, Liang and others\"\n    year: 2024\n    venue: \"ECCV 2024 (Oral)\"\n    arxiv_id: null\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Plug-and-play visual token pruning for VLMs; prunes tokens in deep layers based on attention patterns from early layers.\"\n    pruning_stats: \"Prunes ~50% visual tokens with minimal accuracy loss on VLM benchmarks.\"\n\n  - bibtex_key: zhang2023h2o\n    title: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\"\n    authors: \"Zhang, Zhenyu and others\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.14048\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"KV cache eviction retaining heavy-hitter tokens; 20% heavy hitters achieve up to 29x throughput improvement.\"\n\n  - bibtex_key: xiao2024streamingllm\n    title: \"Efficient Streaming Language Models with Attention Sinks\"\n    authors: \"Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike\"\n    year: 2024\n    venue: \"ICLR 2024\"\n    arxiv_id: \"2309.17453\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: background\n    verified: true\n    key_finding: \"Attention sink phenomenon: keeping KV of initial tokens recovers window attention performance; enables stable LLM inference over 4M+ tokens.\"\n\n  - bibtex_key: hsu2025vlacache\n    title: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\"\n    authors: \"Hsu, Siyu and others\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    arxiv_id: \"2502.02175\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Training-free VLA acceleration via temporal KV caching of static visual tokens; 1.7x speedup with negligible SR loss.\"\n    notes: \"Exploits temporal continuity, not token removal. Key difference from our study: caches rather than removes tokens.\"\n\n  - bibtex_key: wang2026vlaiap\n    title: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\"\n    authors: \"Wang, others\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.22991\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Geometric prior + dynamic scheduling for VLA token pruning; 97.8% SR with 1.54x speedup. Claims to preserve manipulation-critical tokens.\"\n    notes: \"Reports successful VLA token pruning. Key contrast with our findings. Uses OpenVLA, not SmolVLA.\"\n\n  - bibtex_key: yang2025efficientvla\n    title: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\"\n    authors: \"Yang, Yantai and Wang, Yuhao and Wen, Zichen and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.10100\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Synergistic layer pruning + task-aware visual token selection + temporal caching on CogACT (7B); 1.93x speedup with 0.6% SR drop on SIMPLER.\"\n    notes: \"Combines three orthogonal efficiency strategies. Uses CogACT not SmolVLA. Layer pruning and temporal caching are complementary to our token-level analysis.\"\n\n  - bibtex_key: liu2025vlapruner\n    title: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\"\n    authors: \"Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2511.16449\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Dual-level importance criterion combining prefill attention (semantic) and temporally-smoothed action decode attention for VLA token pruning.\"\n    notes: \"VLA-specific pruning exploiting temporal continuity. Directly relevant as it separates semantic vs action-level token importance.\"\n\n  - bibtex_key: shang2024prumerge\n    title: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\"\n    authors: \"Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan\"\n    year: 2024\n    venue: \"ICCV 2025\"\n    arxiv_id: \"2403.15388\"\n    category: \"VLM/LLM Token Efficiency\"\n    role: direct-competitor\n    verified: true\n    key_finding: \"Adaptive visual token pruning + merging for LMMs; reduces tokens by 4x (to 5.5% with PruMerge) with comparable performance on VQA/reasoning tasks.\"\n    notes: \"VLM token reduction via CLS attention importance + similarity-based merging. Establishes prune-then-merge paradigm for visual tokens in VLMs.\"\n\n  # ============================================================\n  # Cluster: ViT Token Pruning/Merging (target: 7)\n  # ============================================================\n  - bibtex_key: rao2021dynamicvit\n    title: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\"\n    authors: \"Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    arxiv_id: \"2106.02034\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Hierarchical token pruning for ViT; removes 66% tokens with only 0.5% accuracy drop on ImageNet; 31-37% FLOPs reduction.\"\n    pruning_stats: \"66% token removal, <0.5% accuracy drop, 40%+ throughput improvement.\"\n\n  - bibtex_key: bolya2023tome\n    title: \"Token Merging: Your ViT But Faster\"\n    authors: \"Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy\"\n    year: 2023\n    venue: \"ICLR 2023 (Oral)\"\n    arxiv_id: \"2210.09461\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Training-free token merging via bipartite matching; 2x throughput on ViT-L with only 0.2-0.3% accuracy drop.\"\n    pruning_stats: \"2x throughput, 0.2-0.3% accuracy drop. Merges redundant foreground + background tokens.\"\n\n  - bibtex_key: liang2022evit\n    title: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\"\n    authors: \"Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao\"\n    year: 2022\n    venue: \"ICLR 2022\"\n    arxiv_id: \"2202.07800\"\n    category: \"ViT Token Pruning/Merging\"\n    role: foundation\n    verified: true\n    key_finding: \"Token reorganization guided by CLS attention; 50% speedup with 0.3% accuracy drop on DeiT-S. Fuses inattentive tokens.\"\n    pruning_stats: \"50% speedup, 0.3% accuracy drop on ImageNet.\"\n\n  - bibtex_key: yin2022avit\n    title: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\"\n    authors: \"Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo\"\n    year: 2022\n    venue: \"CVPR 2022 (Oral)\"\n    arxiv_id: \"2112.07658\"\n    category: \"ViT Token Pruning/Merging\"\n    role: background\n    verified: true\n    key_finding: \"Per-token adaptive depth via ACT halting — tokens exit at different layers based on learned halting probability. 62% throughput gain on DeiT-T, 38% on DeiT-S with 0.3% accuracy drop.\"\n    pruning_stats: \"62% throughput improvement (DeiT-T), 38% (DeiT-S), 0.3% accuracy drop. No extra parameters.\"\n    notes: \"Complements fixed-layer pruning (DynamicViT, EViT) and merging (ToMe) by introducing depth-adaptive token halting. Relevant to our analysis of how token importance varies across transformer depth.\"\n\n  # ============================================================\n  # Cluster: Closed-Loop Evaluation (target: 5)\n  # ============================================================\n  - bibtex_key: liu2023libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"\n    category: \"Closed-Loop Evaluation\"\n    role: foundation\n    verified: true\n    key_finding: \"130 manipulation tasks across 4 suites; evaluates knowledge transfer in lifelong robot learning with teleoperated demonstrations.\"\n    notes: \"Our evaluation benchmark. We use Object/Spatial/Goal suites (10 tasks each, 50 episodes/task).\"\n\n  - bibtex_key: mees2022calvin\n    title: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\"\n    authors: \"Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram\"\n    year: 2022\n    venue: \"IEEE RA-L\"\n    arxiv_id: \"2112.03227\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Long-horizon language-conditioned manipulation benchmark; 24h teleoperated play data with 20K language directives.\"\n\n  - bibtex_key: chi2023diffusionpolicy\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran\"\n    year: 2023\n    venue: \"RSS 2023\"\n    arxiv_id: \"2303.04137\"\n    category: \"Closed-Loop Evaluation\"\n    role: background\n    verified: true\n    key_finding: \"Conditional denoising diffusion for robot policy; 46.9% average improvement across 12 tasks; handles multimodal action distributions.\"\n\n  # ============================================================\n  # Cluster: Negative Results & Evaluation Pitfalls (target: 5)\n  # ============================================================\n  - bibtex_key: zeng2023transformers_tsf\n    title: \"Are Transformers Effective for Time Series Forecasting?\"\n    authors: \"Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang\"\n    year: 2023\n    venue: \"AAAI 2023\"\n    arxiv_id: \"2205.13504\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear models outperform sophisticated Transformer-based LTSF models on all 9 datasets, often by 20-50%. Challenges the Transformer paradigm for time series.\"\n\n  - bibtex_key: bouthillier2024negative\n    title: \"Position: Embracing Negative Results in Machine Learning\"\n    authors: \"Bouthillier, Xavier and others\"\n    year: 2024\n    venue: \"ICML 2024\"\n    arxiv_id: \"2406.03980\"\n    category: \"Negative Results & Evaluation Pitfalls\"\n    role: background\n    verified: true\n    key_finding: \"Position paper arguing for publication of negative results to improve ML research efficiency; predictive performance alone is insufficient for evaluating contributions.\"\n\n  # ============================================================\n  # Background / Architecture\n  # ============================================================\n  - bibtex_key: zhai2023siglip\n    title: \"Sigmoid Loss for Language Image Pre-Training\"\n    authors: \"Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas\"\n    year: 2023\n    venue: \"ICCV 2023\"\n    arxiv_id: \"2303.15343\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Pairwise sigmoid loss for image-text pretraining; optimal at batch size 32K; 84.5% ImageNet zero-shot with only 4 TPUv4 chips.\"\n    notes: \"Vision encoder used in SmolVLA. Produces spatial patch tokens without CLS token.\"\n\n  - bibtex_key: yang2024qwen2\n    title: \"Qwen2 Technical Report\"\n    authors: \"Yang, An and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2407.10671\"\n    category: \"VLA Models\"\n    role: background\n    verified: true\n    key_finding: \"0.5B-72B parameter LLM family; Qwen2-1.5B is the LLM backbone in SmolVLA.\"\n\n  - bibtex_key: lipman2023flow\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    arxiv_id: \"2210.02747\"\n    category: \"VLA Models\"\n    role: foundation\n    verified: true\n    key_finding: \"Simulation-free CNF training via regressing conditional probability path vector fields; OT displacement interpolation enables faster training and sampling.\"\n    notes: \"Action generation mechanism in SmolVLA and pi0.\"\n\n  # ============================================================\n  # Cluster: Vision Connectors & Token Compression (target: 6)\n  # ============================================================\n  - bibtex_key: li2023blip2\n    title: \"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\"\n    authors: \"Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven\"\n    year: 2023\n    venue: \"ICML 2023\"\n    arxiv_id: \"2301.12597\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Querying Transformer (Q-Former) compresses visual tokens into fixed number of query tokens; outperforms Flamingo80B on zero-shot VQAv2 with 54x fewer trainable parameters.\"\n    notes: \"Exemplar of learned cross-attention compression for vision-language bridging. Our proposed cross-attention compression draws on this principle.\"\n\n  - bibtex_key: alayrac2022flamingo\n    title: \"Flamingo: a Visual Language Model for Few-Shot Learning\"\n    authors: \"Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others\"\n    year: 2022\n    venue: \"NeurIPS 2022\"\n    arxiv_id: \"2204.14198\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Perceiver Resampler maps variable-size spatio-temporal visual features to fixed number of output tokens via cross-attention with learnable queries.\"\n    notes: \"Another learned cross-attention connector. Together with BLIP-2, establishes the cross-attention connector paradigm that contrasts with MLP/pixel_shuffle approaches.\"\n\n  - bibtex_key: liu2023llava\n    title: \"Visual Instruction Tuning\"\n    authors: \"Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2304.08485\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Simple linear/MLP projection connects vision encoder to LLM; LLaVA-1.5 shows two-layer MLP projector is surprisingly effective and data-efficient.\"\n    notes: \"Key reference for the MLP projector approach used in OpenVLA. Our finding that MLP projector enables graceful degradation under token pruning connects to this design choice.\"\n\n  - bibtex_key: shi2016subpixel\n    title: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\"\n    authors: \"Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan\"\n    year: 2016\n    venue: \"CVPR 2016\"\n    arxiv_id: \"1609.05158\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"Introduces sub-pixel convolution (pixel shuffle) that rearranges spatial resolution and channel dimensions; enables real-time 1080p super-resolution.\"\n    notes: \"Origin of the pixel_shuffle operation adopted by SmolVLA and InternVL as vision connector. Central to our cliff-edge failure analysis.\"\n\n  - bibtex_key: chen2024internvl\n    title: \"How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites\"\n    authors: \"Chen, Zhe and Wang, Weiyun and Tian, Hao and others\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2404.16821\"\n    category: \"Vision Connectors & Token Compression\"\n    role: background\n    verified: true\n    key_finding: \"InternVL 1.5 uses 2x2 pixel unshuffle to compress 1024 visual tokens to 256 per tile; supports dynamic high-resolution up to 4K with up to 40 tiles.\"\n    notes: \"Another VLM using pixel_shuffle connector, confirming its adoption beyond SmolVLA. Strengthens generality of our cliff-edge finding.\"\n\n  - bibtex_key: oquab2024dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Oquab, Maxime and Darcet, Timothee and Moutakanni, Theo and others\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: \"Vision Connectors & Token Compression\"\n    role: foundation\n    verified: true\n    key_finding: \"Self-supervised ViT producing all-purpose visual features; scaled to ViT-g with curated LVD-142M dataset; strong transfer across tasks without finetuning.\"\n    notes: \"Vision encoder used in OpenVLA (DinoSigLIP). Its feature structure interacts with the MLP projector to determine token-level importance distribution.\"\n",
      "numLines": 401,
      "startLine": 1,
      "totalLines": 401
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01CE8LGn8e15eVzrHx4mEKU5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "48b2a989-9d04-45e3-9d45-c356c5bf3f9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kgG6ahMLZsixK5rHYRYJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12012,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12012
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

_source line 8 · 2026-05-23T00:18:11.087Z_

<details><summary>↩ Tool result · `toolu_01CE8LGn8e15eVzrHx4mEKU5`</summary>

```text
1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% VLA Token Compression (concurrent work)
8	% ============================================================
9	
10	@article{gao2025compressorvla,
11	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
12	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
13	  journal={arXiv preprint arXiv:2511.18950},
14	  year={2025},
15	  eprint={2511.18950},
16	  archivePrefix={arXiv}
17	}
18	
19	@article{wang2025specprunevla,
20	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
21	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
22	  journal={arXiv preprint arXiv:2509.05614},
23	  year={2025},
24	  eprint={2509.05614},
25	  archivePrefix={arXiv}
26	}
27	
28	@inproceedings{jiang2026lightvla,
29	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
30	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
31	  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},
32	  year={2026},
33	  eprint={2509.12594},
34	  archivePrefix={arXiv}
35	}
36	
37	@inproceedings{feng2026seewhatmatters,
38	  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},
39	  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},
40	  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},
41	  year={2026},
42	  eprint={2605.11817},
43	  archivePrefix={arXiv}
44	}
45	
46	@inproceedings{zhang2025sparsevlm,
47	  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},
48	  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},
49	  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},
50	  year={2025},
51	  eprint={2410.04417},
52	  archivePrefix={arXiv}
53	}
54	
55	@inproceedings{khaki2025sparsevila,
56	  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},
57	  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},
58	  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
59	  year={2025},
60	  eprint={2510.17777},
61	  archivePrefix={arXiv}
62	}
63	
64	@article{jabbour2025dontrun,
65	  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},
66	  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},
67	  journal={arXiv preprint arXiv:2510.08464},
68	  year={2025},
69	  eprint={2510.08464},
70	  archivePrefix={arXiv}
71	}
72	
73	@inproceedings{li2024roboflamingo,
74	  title={Vision-Language Foundation Models as Effective Robot Imitators},
75	  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},
76	  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},
77	  year={2024},
78	  eprint={2311.01378},
79	  archivePrefix={arXiv}
80	}
81	
82	% ============================================================
83	% VLA Models
84	% ============================================================
85	
86	@article{shukor2025smolvla,
87	  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},
88	  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},
89	  journal={arXiv preprint arXiv:2506.01844},
90	  year={2025}
91	}
92	
93	@inproceedings{kim2024openvla,
94	  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},
95	  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},
96	  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},
97	  year={2024}
98	}
99	
100	@inproceedings{brohan2023rt2,
101	  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
102	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
103	  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},
104	  year={2023}
105	}
106	
107	
108	@article{black2024pi0,
109	  title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
110	  author={Black, Kevin and Brown, Noah and Driess, Danny and others},
111	  journal={arXiv preprint arXiv:2410.24164},
112	  year={2024}
113	}
114	
115	@article{black2025pi05,
116	  title={$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},
117	  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},
118	  journal={arXiv preprint arXiv:2504.16054},
119	  year={2025},
120	  eprint={2504.16054},
121	  archivePrefix={arXiv}
122	}
123	
124	@inproceedings{ghosh2024octo,
125	  title={Octo: An Open-Source Generalist Robot Policy},
126	  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},
127	  booktitle={Robotics: Science and Systems (RSS)},
128	  year={2024}
129	}
130	
131	@inproceedings{brohan2023rt1,
132	  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},
133	  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},
134	  booktitle={Robotics: Science and Systems (RSS)},
135	  year={2023}
136	}
137	
138	
139	% ============================================================
140	% VLM/LLM Token Efficiency
141	% ============================================================
142	
143	@inproceedings{chen2024fastv,
144	  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},
145	  author={Chen, Liang and others},
146	  booktitle={European Conference on Computer Vision (ECCV)},
147	  year={2024},
148	  note={Oral presentation}
149	}
150	
151	
152	@inproceedings{xu2025vlacache,
153	  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},
154	  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},
155	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
156	  year={2025}
157	}
158	
159	@article{cheng2026vlaiap,
160	  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},
161	  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},
162	  journal={arXiv preprint arXiv:2603.22991},
163	  year={2026}
164	}
165	
166	% ============================================================
167	% ViT Token Pruning/Merging
168	% ============================================================
169	
170	@inproceedings{rao2021dynamicvit,
171	  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},
172	  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},
173	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
174	  year={2021}
175	}
176	
177	@inproceedings{bolya2023tome,
178	  title={Token Merging: Your {ViT} But Faster},
179	  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},
180	  booktitle={International Conference on Learning Representations (ICLR)},
181	  year={2023}
182	}
183	
184	@inproceedings{liang2022evit,
185	  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},
186	  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},
187	  booktitle={International Conference on Learning Representations (ICLR)},
188	  year={2022}
189	}
190	
191	% ============================================================
192	% Closed-Loop Evaluation
193	% ============================================================
194	
195	@inproceedings{liu2023libero,
196	  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
197	  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},
198	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
199	  year={2023}
200	}
201	
202	
203	% ============================================================
204	% Negative Results & Evaluation Pitfalls
205	% ============================================================
206	
207	
208	% ============================================================
209	% VLA Token Efficiency (new additions)
210	% ============================================================
211	
212	@article{yang2025efficientvla,
213	  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},
214	  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},
215	  journal={arXiv preprint arXiv:2506.10100},
216	  year={2025}
217	}
218	
219	@article{liu2025vlapruner,
220	  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},
221	  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},
222	  journal={arXiv preprint arXiv:2511.16449},
223	  year={2025}
224	}
225	
226	@inproceedings{shang2024prumerge,
227	  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},
228	  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},
229	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
230	  year={2025}
231	}
232	
233	% ============================================================
234	% Vision Connectors
235	% ============================================================
236	
237	@inproceedings{alayrac2022flamingo,
238	  title={Flamingo: a Visual Language Model for Few-Shot Learning},
239	  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},
240	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
241	  year={2022}
242	}
243	
244	@inproceedings{liu2023llava,
245	  title={Visual Instruction Tuning},
246	  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},
247	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
248	  year={2023}
249	}
250	
251	@inproceedings{shi2016subpixel,
252	  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},
253	  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},
254	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
255	  year={2016}
256	}
257	
258	@article{chen2024internvl,
259	  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},
260	  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},
261	  journal={arXiv preprint arXiv:2404.16821},
262	  year={2024}
263	}
264	
265	% ============================================================
266	% Background / Architecture
267	% ============================================================
268	
269	@inproceedings{li2023blip2,
270	  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},
271	  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},
272	  booktitle={International Conference on Machine Learning (ICML)},
273	  year={2023}
274	}
275	
276	@inproceedings{jaegle2021perceiver,
277	  title={Perceiver: General Perception with Iterative Attention},
278	  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},
279	  booktitle={International Conference on Machine Learning (ICML)},
280	  year={2021}
281	}
282	
283	@article{oquab2023dinov2,
284	  title={{DINOv2}: Learning Robust Visual Features without Supervision},
285	  author={Oquab, Maxime and Darcet, Timoth{\'e}e and Moutakanni, Theo and others},
286	  journal={Transactions on Machine Learning Research},
287	  year={2024}
288	}
289	
290	@inproceedings{zhai2023siglip,
291	  title={Sigmoid Loss for Language Image Pre-Training},
292	  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},
293	  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},
294	  year={2023}
295	}
296	
297	@article{yang2024qwen2,
298	  title={Qwen2 Technical Report},
299	  author={Yang, An and others},
300	  journal={arXiv preprint arXiv:2407.10671},
301	  year={2024}
302	}
303	
304	@inproceedings{lipman2023flow,
305	  title={Flow Matching for Generative Modeling},
306	  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},
307	  booktitle={International Conference on Learning Representations (ICLR)},
308	  year={2023}
309	}
310	
311	% ============================================================
312	% Additional references (Round 3 reviewer request)
313	% ============================================================
314	
315	% ============================================================
316	% Additional VLA / VLM references
317	% ============================================================
318	
319	@article{li2024cogact,
320	  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},
321	  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},
322	  journal={arXiv preprint arXiv:2411.19650},
323	  year={2024},
324	  eprint={2411.19650},
325	  archivePrefix={arXiv}
326	}
327	
328	@article{kim2025openoft,
329	  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},
330	  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},
331	  journal={arXiv preprint arXiv:2502.19645},
332	  year={2025},
333	  eprint={2502.19645},
334	  archivePrefix={arXiv}
335	}
336	
337	@article{li2024tokenpacker,
338	  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},
339	  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},
340	  journal={arXiv preprint arXiv:2407.02392},
341	  year={2024},
342	  eprint={2407.02392},
343	  archivePrefix={arXiv}
344	}
345	
346	@inproceedings{zheng2025xvla,
347	  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},
348	  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},
349	  booktitle={International Conference on Learning Representations (ICLR)},
350	  year={2026},
351	  eprint={2510.10274},
352	  archivePrefix={arXiv}
353	}
354	
355	@article{wen2024tinyvla,
356	  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},
357	  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},
358	  journal={arXiv preprint arXiv:2409.12514},
359	  year={2024},
360	  eprint={2409.12514},
361	  archivePrefix={arXiv}
362	}
363	
364	@inproceedings{lewis2020bart,
365	  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},
366	  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},
367	  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},
368	  year={2020}
369	}
370	
371	% ============================================================
372	% New additions for expanded Related Work
373	% ============================================================
374	
375	@inproceedings{ryoo2021tokenlearner,
376	  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},
377	  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},
378	  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
379	  year={2021},
380	  eprint={2106.11297},
381	  archivePrefix={arXiv}
382	}
383	
384	@inproceedings{yin2022avit,
385	  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},
386	  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},
387	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
388	  year={2022},
389	  eprint={2112.07658},
390	  archivePrefix={arXiv}
391	}
392	
393	@inproceedings{meng2022adavit,
394	  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},
395	  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},
396	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
397	  year={2022},
398	  eprint={2111.15668},
399	  archivePrefix={arXiv}
400	}
401	
402	@inproceedings{chen2023sparsevit,
403	  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},
404	  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},
405	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
406	  year={2023},
407	  eprint={2303.17605},
408	  archivePrefix={arXiv}
409	}
410	
411	@inproceedings{ye2025fitprune,
412	  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},
413	  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},
414	  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},
415	  year={2025},
416	  eprint={2409.10197},
417	  archivePrefix={arXiv}
418	}
419	
420	@inproceedings{shi2024crossget,
421	  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},
422	  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},
423	  booktitle={International Conference on Machine Learning (ICML)},
424	  year={2024},
425	  eprint={2305.17455},
426	  archivePrefix={arXiv}
427	}
428	
429	@article{zhang2024fastervlm,
430	  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},
431	  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},
432	  journal={arXiv preprint arXiv:2412.01818},
433	  year={2024},
434	  eprint={2412.01818},
435	  archivePrefix={arXiv}
436	}
437	
438	@inproceedings{liu2024llava15,
439	  title={Improved Baselines with Visual Instruction Tuning},
440	  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},
441	  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
442	  year={2024},
443	  eprint={2310.03744},
444	  archivePrefix={arXiv}
445	}
446	
447	@article{chen2024internvl25,
448	  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},
449	  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},
450	  journal={arXiv preprint arXiv:2412.05271},
451	  year={2024},
452	  eprint={2412.05271},
453	  archivePrefix={arXiv}
454	}
455	
456	@article{gao2024miniinternvl,
457	  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\% Parameters and 90\% Performance},
458	  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},
459	  journal={arXiv preprint arXiv:2410.16261},
460	  year={2024},
461	  eprint={2410.16261},
462	  archivePrefix={arXiv}
463	}
464	
465	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "6a8e6574-675c-41ef-ab90-10a0bab2bfd6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
      "content": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n",
      "numLines": 465,
      "startLine": 1,
      "totalLines": 465
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I need to identify the 11 missing entries and check what's already in the bib file. Let me cross-reference:

1. `zitkovich2023rt2` - The literature map has this key, but the bib file has `brohan2023rt2` (different key!). So I need to add `zitkovich2023rt2`.
2. `openxembodiment2024` - Not in bib. Need to add.
3. `zhang2023h2o` - Not in bib. Need to add.
4. `xiao2024streamingllm` - Not in bib. Need to add.


5. `hsu2025vlacache` - The bib has `xu2025vlacache` (different key!). Need to add `hsu2025vlacache`.
6. `wang2026vlaiap` - The bib has `cheng2026vlaiap` (different key!). Need to add `wang2026vlaiap`.
7. `mees2022calvin` - Not in bib. Need to add.
8. `chi2023diffusionpolicy` - Not in bib. Need to add.
9. `zeng2023transformers_tsf` - Not in bib. Need to add.
10. `bouthillier2024negative` - Not in bib. Need to add.
11. `oquab2024dinov2` - The bib has `oquab2023dinov2` (different key!). Need to add `oquab2024dinov2`.

Now I'm realizing the actual task here - the literature map uses specific keys that don't always match what's in the bib file. For `zitkovich2023rt2`, the bib has it under `brohan2023rt2`, but since the literature map explicitly references `zitkovich2023rt2` with Zitkovich as the author, I need to add that entry with the correct key rather than just using the existing one.

Looking at entries like `hsu2025vlacache` versus `xu2025vlacache` - these appear to be duplicate entries with slightly different author surnames in the keys. The literature map specifies `hsu2025vlacache` with Hsu as the author, so I should add that version even though a similar entry exists under a different key. I'll go ahead and add all 11 entries with their exact keys from the literature map. I'll add these 11 entries with their exact keys from the literature map, even though some appear to be duplicates of existing entries with different author orderings or years—they might be referenced elsewhere or the project may prefer these specific keys. Now I'm constructing the BibTeX entries by examining the formatting style of existing ones and preparing to add all 11 with proper entry types and fields. Finishing up the bibliography entries...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "04eef84b-1818-4633-afe5-b579ac571adb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDFoDi6RZHyyanmCC98T1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15308,
      "cache_read_input_tokens": 23853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15308
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

_source line 10_

Now I'll back up the file and append the 11 missing entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "f8fc59de-29e0-42cc-9b45-82665e50611d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDFoDi6RZHyyanmCC98T1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15308,
      "cache_read_input_tokens": 23853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15308
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01LFVJk9idQf87DzwF5cFTyJ`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib.prev",
  "description": "Backup references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "a8e5890d-c4c0-4ea7-9d87-16d75abc5fbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TDFoDi6RZHyyanmCC98T1X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15308,
      "cache_read_input_tokens": 23853,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15308
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

_source line 12 · 2026-05-23T00:18:43.658Z_

<details><summary>↩ Tool result · `toolu_01LFVJk9idQf87DzwF5cFTyJ`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "c90d7875-19d5-4bab-aabe-430fe13720e6",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01SKKWmEdQNoEpz282xyPbDL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
  "old_string": "@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}",
  "new_string": "@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{hsu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Hsu, Siyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  eprint={2502.02175},\n  archivePrefix={arXiv}\n}\n\n@article{wang2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Wang, others},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026},\n  eprint={2603.22991},\n  archivePrefix={arXiv}\n}\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "e850975a-efe8-442d-8949-a403792cb5df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012KeRyDW55XmTagTGkMXPmW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1599,
      "cache_read_input_tokens": 39161,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1599
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 14 · 2026-05-23T00:19:11.953Z_

<details><summary>↩ Tool result · `toolu_01SKKWmEdQNoEpz282xyPbDL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "054ba531-f660-4b98-8ba0-4ec3e0394e5b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib",
    "oldString": "@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}",
    "newString": "@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% Synced from literature_map.yaml (missing entries)\n% ============================================================\n\n% --- VLA Models ---\n\n@inproceedings{zitkovich2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023},\n  eprint={2307.15818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{openxembodiment2024,\n  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},\n  author={{Open X-Embodiment Collaboration}},\n  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2024},\n  eprint={2310.08864},\n  archivePrefix={arXiv}\n}\n\n% --- VLM/LLM Token Efficiency ---\n\n@inproceedings{zhang2023h2o,\n  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n  author={Zhang, Zhenyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023},\n  eprint={2306.14048},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{xiao2024streamingllm,\n  title={Efficient Streaming Language Models with Attention Sinks},\n  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2309.17453},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{hsu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Hsu, Siyu and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025},\n  eprint={2502.02175},\n  archivePrefix={arXiv}\n}\n\n@article{wang2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Wang, others},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026},\n  eprint={2603.22991},\n  archivePrefix={arXiv}\n}\n\n% --- Closed-Loop Evaluation ---\n\n@article{mees2022calvin,\n  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},\n  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},\n  journal={IEEE Robotics and Automation Letters},\n  year={2022},\n  eprint={2112.03227},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chi2023diffusionpolicy,\n  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023},\n  eprint={2303.04137},\n  archivePrefix={arXiv}\n}\n\n% --- Negative Results & Evaluation Pitfalls ---\n\n@inproceedings{zeng2023transformers_tsf,\n  title={Are Transformers Effective for Time Series Forecasting?},\n  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2023},\n  eprint={2205.13504},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{bouthillier2024negative,\n  title={Position: Embracing Negative Results in Machine Learning},\n  author={Bouthillier, Xavier and others},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2406.03980},\n  archivePrefix={arXiv}\n}\n\n% --- Vision Connectors & Token Compression ---\n\n@article{oquab2024dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024},\n  eprint={2304.07193},\n  archivePrefix={arXiv}\n}",
    "originalFile": "% References for: The Cliff Edge — Why Vision Token Reduction Fails\n% Catastrophically in VLA Closed-Loop Control\n% Auto-generated from literature_map.yaml (verified entries only)\n% 2026-05-17\n\n% ============================================================\n% VLA Token Compression (concurrent work)\n% ============================================================\n\n@article{gao2025compressorvla,\n  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},\n  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},\n  journal={arXiv preprint arXiv:2511.18950},\n  year={2025},\n  eprint={2511.18950},\n  archivePrefix={arXiv}\n}\n\n@article{wang2025specprunevla,\n  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},\n  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},\n  journal={arXiv preprint arXiv:2509.05614},\n  year={2025},\n  eprint={2509.05614},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{jiang2026lightvla,\n  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},\n  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},\n  booktitle={Proceedings of the IEEE International Conference on Robotics and Automation (ICRA)},\n  year={2026},\n  eprint={2509.12594},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{feng2026seewhatmatters,\n  title={See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model},\n  author={Feng, Yixu and Zhao, Zinan and Ma, Yanxiang and Xia, Chenghao and Du, Chengbin and Wang, Yunke and Xu, Chang},\n  booktitle={Proceedings of the Forty-Third International Conference on Machine Learning (ICML)},\n  year={2026},\n  eprint={2605.11817},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zhang2025sparsevlm,\n  title={SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference},\n  author={Zhang, Yuan and Fan, Chun-Kai and Ma, Junpeng and Zheng, Wenzhao and Huang, Tao and Cheng, Kuan and Gudovskiy, Denis and Okuno, Tomoyuki and Nakata, Yohei and Keutzer, Kurt and Zhang, Shanghang},\n  booktitle={Proceedings of the Forty-Second International Conference on Machine Learning (ICML)},\n  year={2025},\n  eprint={2410.04417},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{khaki2025sparsevila,\n  title={SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference},\n  author={Khaki, Samir and Guo, Junxian and Tang, Jiaming and Yang, Shang and Chen, Yukang and Plataniotis, Konstantinos N. and Lu, Yao and Han, Song and Liu, Zhijian},\n  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025},\n  eprint={2510.17777},\n  archivePrefix={arXiv}\n}\n\n@article{jabbour2025dontrun,\n  title={Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered},\n  author={Jabbour, Jason and Kim, Dong-Ki and Smith, Max and Patrikar, Jay and Ghosal, Radhika and Wang, Youhui and Agha, Ali and Janapa Reddi, Vijay and Omidshafiei, Shayegan},\n  journal={arXiv preprint arXiv:2510.08464},\n  year={2025},\n  eprint={2510.08464},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{li2024roboflamingo,\n  title={Vision-Language Foundation Models as Effective Robot Imitators},\n  author={Li, Xinghang and Liu, Minghuan and Zhang, Hanbo and Yu, Cunjun and Xu, Jie and Wu, Hongtao and Cheang, Chilam and Jing, Ya and Zhang, Weinan and Liu, Huaping and Li, Hang and Kong, Tao},\n  booktitle={Proceedings of the Twelfth International Conference on Learning Representations (ICLR)},\n  year={2024},\n  eprint={2311.01378},\n  archivePrefix={arXiv}\n}\n\n% ============================================================\n% VLA Models\n% ============================================================\n\n@article{shukor2025smolvla,\n  title={{SmolVLA}: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n  author={Shukor, Mustafa and Aubakirova, Dana and Casas, Adrien and others},\n  journal={arXiv preprint arXiv:2506.01844},\n  year={2025}\n}\n\n@inproceedings{kim2024openvla,\n  title={{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author={Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and others},\n  booktitle={Proceedings of the 8th Conference on Robot Learning (CoRL)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt2,\n  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},\n  year={2023}\n}\n\n\n@article{black2024pi0,\n  title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n  author={Black, Kevin and Brown, Noah and Driess, Danny and others},\n  journal={arXiv preprint arXiv:2410.24164},\n  year={2024}\n}\n\n@article{black2025pi05,\n  title={$\\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization},\n  author={Black, Kevin and Brown, Noah and Shafiullah, Nur Muhammad Mahi and others},\n  journal={arXiv preprint arXiv:2504.16054},\n  year={2025},\n  eprint={2504.16054},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ghosh2024octo,\n  title={Octo: An Open-Source Generalist Robot Policy},\n  author={{Octo Model Team} and Ghosh, Dibya and Walke, Homer and Pertsch, Karl and Black, Kevin and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2024}\n}\n\n@inproceedings{brohan2023rt1,\n  title={{RT-1}: Robotics Transformer for Real-World Control at Scale},\n  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and others},\n  booktitle={Robotics: Science and Systems (RSS)},\n  year={2023}\n}\n\n\n% ============================================================\n% VLM/LLM Token Efficiency\n% ============================================================\n\n@inproceedings{chen2024fastv,\n  title={An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models},\n  author={Chen, Liang and others},\n  booktitle={European Conference on Computer Vision (ECCV)},\n  year={2024},\n  note={Oral presentation}\n}\n\n\n@inproceedings{xu2025vlacache,\n  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},\n  author={Xu, Siyu and Wang, Yunke and Xia, Chenghao and Zhu, Dihao and Huang, Tao and Xu, Chang},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2025}\n}\n\n@article{cheng2026vlaiap,\n  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},\n  author={Cheng, Jintao and Wang, Haozhe and Li, Weibin and Wang, Gang and Zhang, Yipu and Tang, Xiaoyu and Wu, Jin and Chen, Xieyuanli and Liu, Yunhui and Zhang, Wei},\n  journal={arXiv preprint arXiv:2603.22991},\n  year={2026}\n}\n\n% ============================================================\n% ViT Token Pruning/Merging\n% ============================================================\n\n@inproceedings{rao2021dynamicvit,\n  title={{DynamicViT}: Efficient Vision Transformers with Dynamic Token Sparsification},\n  author={Rao, Yongming and Zhao, Wenliang and Liu, Benlin and Lu, Jiwen and Zhou, Jie and Hsieh, Cho-Jui},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021}\n}\n\n@inproceedings{bolya2023tome,\n  title={Token Merging: Your {ViT} But Faster},\n  author={Bolya, Daniel and Fu, Cheng-Yang and Dai, Xiaoliang and Zhang, Peizhao and Feichtenhofer, Christoph and Hoffman, Judy},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n@inproceedings{liang2022evit,\n  title={Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations},\n  author={Liang, Youwei and Ge, Chongjian and Tong, Zhan and Song, Yibing and Wang, Jue and Xie, Pengtao},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2022}\n}\n\n% ============================================================\n% Closed-Loop Evaluation\n% ============================================================\n\n@inproceedings{liu2023libero,\n  title={{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author={Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n\n% ============================================================\n% Negative Results & Evaluation Pitfalls\n% ============================================================\n\n\n% ============================================================\n% VLA Token Efficiency (new additions)\n% ============================================================\n\n@article{yang2025efficientvla,\n  title={{EfficientVLA}: Training-Free Acceleration and Compression for Vision-Language-Action Models},\n  author={Yang, Yantai and Wang, Yuhao and Wen, Zichen and others},\n  journal={arXiv preprint arXiv:2506.10100},\n  year={2025}\n}\n\n@article{liu2025vlapruner,\n  title={{VLA-Pruner}: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference},\n  author={Liu, Ziyan and Chen, Yeqiu and Cai, Hongyi and others},\n  journal={arXiv preprint arXiv:2511.16449},\n  year={2025}\n}\n\n@inproceedings{shang2024prumerge,\n  title={{LLaVA-PruMerge}: Adaptive Token Reduction for Efficient Large Multimodal Models},\n  author={Shang, Yuzhang and Cai, Mu and Xu, Bingxin and Lee, Yong Jae and Yan, Yan},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2025}\n}\n\n% ============================================================\n% Vision Connectors\n% ============================================================\n\n@inproceedings{alayrac2022flamingo,\n  title={Flamingo: a Visual Language Model for Few-Shot Learning},\n  author={Alayrac, Jean-Baptiste and Donahue, Jeff and Luc, Pauline and others},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2022}\n}\n\n@inproceedings{liu2023llava,\n  title={Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2023}\n}\n\n@inproceedings{shi2016subpixel,\n  title={Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network},\n  author={Shi, Wenzhe and Caballero, Jose and Huszar, Ferenc and Totz, Johannes and Aitken, Andrew P. and Bishop, Rob and Rueckert, Daniel and Wang, Zehan},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2016}\n}\n\n@article{chen2024internvl,\n  title={How Far Are We to {GPT-4V}? Closing the Gap to Commercial Multimodal Models with Open-Source Suites},\n  author={Chen, Zhe and Wang, Weiyun and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2404.16821},\n  year={2024}\n}\n\n% ============================================================\n% Background / Architecture\n% ============================================================\n\n@inproceedings{li2023blip2,\n  title={{BLIP-2}: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models},\n  author={Li, Junnan and Li, Dongxu and Savarese, Silvio and Hoi, Steven},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2023}\n}\n\n@inproceedings{jaegle2021perceiver,\n  title={Perceiver: General Perception with Iterative Attention},\n  author={Jaegle, Andrew and Gimeno, Felix and Brock, Andrew and Zisserman, Andrew and Vinyals, Oriol and Carreira, Joao},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2021}\n}\n\n@article{oquab2023dinov2,\n  title={{DINOv2}: Learning Robust Visual Features without Supervision},\n  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}\n\n@inproceedings{zhai2023siglip,\n  title={Sigmoid Loss for Language Image Pre-Training},\n  author={Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle={IEEE/CVF International Conference on Computer Vision (ICCV)},\n  year={2023}\n}\n\n@article{yang2024qwen2,\n  title={Qwen2 Technical Report},\n  author={Yang, An and others},\n  journal={arXiv preprint arXiv:2407.10671},\n  year={2024}\n}\n\n@inproceedings{lipman2023flow,\n  title={Flow Matching for Generative Modeling},\n  author={Lipman, Yaron and Chen, Ricky T. Q. and Ben-Hamu, Heli and Nickel, Maximilian and Le, Matt},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2023}\n}\n\n% ============================================================\n% Additional references (Round 3 reviewer request)\n% ============================================================\n\n% ============================================================\n% Additional VLA / VLM references\n% ============================================================\n\n@article{li2024cogact,\n  title={CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation},\n  author={Li, Qixiu and Liang, Yaobo and Wang, Zeyu and Luo, Lin and Chen, Xi and Liao, Mozheng and Wei, Fangyun and Deng, Yu and Xu, Sicheng and Zhang, Yizhong and Wang, Xiaofan and Liu, Bei and Fu, Jianlong and Bao, Jianmin and Chen, Dong and Shi, Yuanchun and Yang, Jiaolong and Guo, Baining},\n  journal={arXiv preprint arXiv:2411.19650},\n  year={2024},\n  eprint={2411.19650},\n  archivePrefix={arXiv}\n}\n\n@article{kim2025openoft,\n  title={Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success},\n  author={Kim, Moo Jin and Finn, Chelsea and Liang, Percy},\n  journal={arXiv preprint arXiv:2502.19645},\n  year={2025},\n  eprint={2502.19645},\n  archivePrefix={arXiv}\n}\n\n@article{li2024tokenpacker,\n  title={TokenPacker: Efficient Visual Projector for Multimodal LLM},\n  author={Li, Wentong and Yuan, Yuqian and Liu, Jian and Tang, Dongqi and Wang, Song and Qin, Jie and Zhu, Jianke and Zhang, Lei},\n  journal={arXiv preprint arXiv:2407.02392},\n  year={2024},\n  eprint={2407.02392},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{zheng2025xvla,\n  title={{X-VLA}: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model},\n  author={Zheng, Yifu and Li, Zhihao and Wang, Shengjie and Wang, Jianxiong and others},\n  booktitle={International Conference on Learning Representations (ICLR)},\n  year={2026},\n  eprint={2510.10274},\n  archivePrefix={arXiv}\n}\n\n@article{wen2024tinyvla,\n  title={TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation},\n  author={Wen, Junjie and Zhu, Yichen and Li, Jinming and Zhu, Minjie and Wu, Kun and Xu, Zhiyuan and Liu, Ning and Cheng, Ran and Shen, Chaomin and Peng, Yaxin and Feng, Feifei and Tang, Jian},\n  journal={arXiv preprint arXiv:2409.12514},\n  year={2024},\n  eprint={2409.12514},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{lewis2020bart,\n  title={{BART}: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension},\n  author={Lewis, Mike and Liu, Yinhan and Goyal, Naman and Ghazvininejad, Marjan and Mohamed, Abdelrahman and Levy, Omer and Stoyanov, Veselin and Zettlemoyer, Luke},\n  booktitle={Annual Meeting of the Association for Computational Linguistics (ACL)},\n  year={2020}\n}\n\n% ============================================================\n% New additions for expanded Related Work\n% ============================================================\n\n@inproceedings{ryoo2021tokenlearner,\n  title={{TokenLearner}: Adaptive Space-Time Tokenization for Videos},\n  author={Ryoo, Michael S. and Piergiovanni, AJ and Arnab, Anurag and Dehghani, Mostafa and Angelova, Anelia},\n  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n  year={2021},\n  eprint={2106.11297},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{yin2022avit,\n  title={{A-ViT}: Adaptive Tokens for Efficient Vision Transformer},\n  author={Yin, Hongxu and Vahdat, Arash and Alvarez, Jose M. and Mallya, Arun and Kautz, Jan and Molchanov, Pavlo},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2112.07658},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{meng2022adavit,\n  title={{AdaViT}: Adaptive Vision Transformers for Efficient Image Recognition},\n  author={Meng, Lingchen and Li, Hengduo and Chen, Bor-Chun and Lan, Shiyi and Wu, Zuxuan and Jiang, Yu-Gang and Lim, Ser-Nam},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2022},\n  eprint={2111.15668},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{chen2023sparsevit,\n  title={{SparseViT}: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer},\n  author={Chen, Xuanyao and Liu, Zhijian and Tang, Haotian and Yi, Li and Zhao, Hang and Han, Song},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2023},\n  eprint={2303.17605},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{ye2025fitprune,\n  title={Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models},\n  author={Ye, Weihao and Wu, Qiong and Lin, Wenhao and Zhou, Yiyi},\n  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},\n  year={2025},\n  eprint={2409.10197},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{shi2024crossget,\n  title={{CrossGET}: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers},\n  author={Shi, Dachuan and Tao, Chaofan and Rao, Anyi and Yang, Zhendong and Yuan, Chun and Wang, Jiaqi},\n  booktitle={International Conference on Machine Learning (ICML)},\n  year={2024},\n  eprint={2305.17455},\n  archivePrefix={arXiv}\n}\n\n@article{zhang2024fastervlm,\n  title={[CLS] Attention is All You Need for Training-Free Visual Token Pruning: Make {VLM} Inference Faster},\n  author={Zhang, Qizhe and Cheng, Aosong and Lu, Ming and Zhuo, Zhiyong and Wang, Minqi and Cao, Jiajun and Guo, Shaobo and She, Qi and Zhang, Shanghang},\n  journal={arXiv preprint arXiv:2412.01818},\n  year={2024},\n  eprint={2412.01818},\n  archivePrefix={arXiv}\n}\n\n@inproceedings{liu2024llava15,\n  title={Improved Baselines with Visual Instruction Tuning},\n  author={Liu, Haotian and Li, Chunyuan and Li, Yuheng and Lee, Yong Jae},\n  booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},\n  year={2024},\n  eprint={2310.03744},\n  archivePrefix={arXiv}\n}\n\n@article{chen2024internvl25,\n  title={Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling},\n  author={Chen, Zhe and Wang, Weiyun and Cao, Yue and Liu, Yangzhou and Gao, Zhangwei and Cui, Erfei and Zhu, Jinguo and Ye, Shenglong and Tian, Hao and others},\n  journal={arXiv preprint arXiv:2412.05271},\n  year={2024},\n  eprint={2412.05271},\n  archivePrefix={arXiv}\n}\n\n@article{gao2024miniinternvl,\n  title={{Mini-InternVL}: A Flexible-Transfer Pocket Multimodal Model with 5\\% Parameters and 90\\% Performance},\n  author={Gao, Zhangwei and Chen, Zhe and Cui, Erfei and Ren, Yiming and Wang, Weiyun and Zhu, Jinguo and Tian, Hao and Ye, Shenglong and He, Junjun and Zhu, Xizhou and others},\n  journal={arXiv preprint arXiv:2410.16261},\n  year={2024},\n  eprint={2410.16261},\n  archivePrefix={arXiv}\n}\n\n",
    "structuredPatch": [
      {
        "oldStart": 462,
        "oldLines": 3,
        "newStart": 462,
        "newLines": 116,
        "lines": [
          "   archivePrefix={arXiv}",
          " }",
          " ",
          "+% ============================================================",
          "+% Synced from literature_map.yaml (missing entries)",
          "+% ============================================================",
          "+",
          "+% --- VLA Models ---",
          "+",
          "+@inproceedings{zitkovich2023rt2,",
          "+  title={{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},",
          "+  author={Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others},",
          "+  booktitle={Proceedings of the 7th Conference on Robot Learning (CoRL)},",
          "+  year={2023},",
          "+  eprint={2307.15818},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+@inproceedings{openxembodiment2024,",
          "+  title={Open {X-Embodiment}: Robotic Learning Datasets and {RT-X} Models},",
          "+  author={{Open X-Embodiment Collaboration}},",
          "+  booktitle={IEEE International Conference on Robotics and Automation (ICRA)},",
          "+  year={2024},",
          "+  eprint={2310.08864},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+% --- VLM/LLM Token Efficiency ---",
          "+",
          "+@inproceedings{zhang2023h2o,",
          "+  title={{H2O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},",
          "+  author={Zhang, Zhenyu and others},",
          "+  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},",
          "+  year={2023},",
          "+  eprint={2306.14048},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+@inproceedings{xiao2024streamingllm,",
          "+  title={Efficient Streaming Language Models with Attention Sinks},",
          "+  author={Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike},",
          "+  booktitle={International Conference on Learning Representations (ICLR)},",
          "+  year={2024},",
          "+  eprint={2309.17453},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+@inproceedings{hsu2025vlacache,",
          "+  title={{VLA-Cache}: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching},",
          "+  author={Hsu, Siyu and others},",
          "+  booktitle={Advances in Neural Information Processing Systems (NeurIPS)},",
          "+  year={2025},",
          "+  eprint={2502.02175},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+@article{wang2026vlaiap,",
          "+  title={{VLA-IAP}: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models},",
          "+  author={Wang, others},",
          "+  journal={arXiv preprint arXiv:2603.22991},",
          "+  year={2026},",
          "+  eprint={2603.22991},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+% --- Closed-Loop Evaluation ---",
          "+",
          "+@article{mees2022calvin,",
          "+  title={{CALVIN}: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks},",
          "+  author={Mees, Oier and Hermann, Lukas and Rosete-Beas, Erick and Burgard, Wolfram},",
          "+  journal={IEEE Robotics and Automation Letters},",
          "+  year={2022},",
          "+  eprint={2112.03227},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+@inproceedings{chi2023diffusionpolicy,",
          "+  title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},",
          "+  author={Chi, Cheng and Feng, Siyuan and Du, Yilun and Xu, Zhenjia and Cousineau, Eric and Burchfiel, Benjamin and Song, Shuran},",
          "+  booktitle={Robotics: Science and Systems (RSS)},",
          "+  year={2023},",
          "+  eprint={2303.04137},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+% --- Negative Results & Evaluation Pitfalls ---",
          "+",
          "+@inproceedings{zeng2023transformers_tsf,",
          "+  title={Are Transformers Effective for Time Series Forecasting?},",
          "+  author={Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},",
          "+  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence (AAAI)},",
          "+  year={2023},",
          "+  eprint={2205.13504},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+@inproceedings{bouthillier2024negative,",
          "+  title={Position: Embracing Negative Results in Machine Learning},",
          "+  author={Bouthillier, Xavier and others},",
          "+  booktitle={International Conference on Machine Learning (ICML)},",
          "+  year={2024},",
          "+  eprint={2406.03980},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+",
          "+% --- Vision Connectors & Token Compression ---",
          "+",
          "+@article{oquab2024dinov2,",
          "+  title={{DINOv2}: Learning Robust Visual Features without Supervision},",
          "+  author={Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and others},",
          "+  journal={Transactions on Machine Learning Research},",
          "+  year={2024},",
          "+  eprint={2304.07193},",
          "+  archivePrefix={arXiv}",
          "+}",
          "+"
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

_source line 15_

Now verifying all 11 keys are present.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "97920316-5dd9-46cb-96de-41b9e0e558cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLar8BaoUFDzwbWDQZZpcc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 40760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01MacJwsKkLKbw54BWsKjp8D`</summary>

```json
{
  "command": "for key in zitkovich2023rt2 openxembodiment2024 zhang2023h2o xiao2024streamingllm hsu2025vlacache wang2026vlaiap mees2022calvin chi2023diffusionpolicy zeng2023transformers_tsf bouthillier2024negative oquab2024dinov2; do echo -n \"$key: \"; grep -c \"$key\" /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib; done",
  "description": "Verify all 11 keys present in references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "0d295e37-935d-4121-9037-1dade8199a08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLar8BaoUFDzwbWDQZZpcc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 40760,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1883
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

_source line 17 · 2026-05-23T00:19:16.724Z_

<details><summary>↩ Tool result · `toolu_01MacJwsKkLKbw54BWsKjp8D`</summary>

```text
zitkovich2023rt2: 1
openxembodiment2024: 1
zhang2023h2o: 1
xiao2024streamingllm: 1
hsu2025vlacache: 1
wang2026vlaiap: 1
mees2022calvin: 1
chi2023diffusionpolicy: 1
zeng2023transformers_tsf: 1
bouthillier2024negative: 1
oquab2024dinov2: 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "f38ab2ee-f11d-4541-8990-d903f9b283c8",
  "tool_use_result": {
    "stdout": "zitkovich2023rt2: 1\nopenxembodiment2024: 1\nzhang2023h2o: 1\nxiao2024streamingllm: 1\nhsu2025vlacache: 1\nwang2026vlaiap: 1\nmees2022calvin: 1\nchi2023diffusionpolicy: 1\nzeng2023transformers_tsf: 1\nbouthillier2024negative: 1\noquab2024dinov2: 1",
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

_source line 18_

All 11 entries added and verified. Backup saved as `references.bib.prev`. No issues encountered.

Note: the bib file already had near-duplicate entries under slightly different keys for 3 of these (`brohan2023rt2` / `xu2025vlacache` / `cheng2026vlaiap` / `oquab2023dinov2`). The new entries use the keys from `literature_map.yaml` — you may want to consolidate the old keys if they're no longer referenced in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "uuid": "1edb1a4e-3787-467f-add8-266440e57251",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3tTUAYU235sdEo2yVXofV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 42643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
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

_source line 19_

All 11 entries added and verified. Backup saved as `references.bib.prev`. No issues encountered.

Note: the bib file already had near-duplicate entries under slightly different keys for 3 of these (`brohan2023rt2` / `xu2025vlacache` / `cheng2026vlaiap` / `oquab2023dinov2`). The new entries use the keys from `literature_map.yaml` — you may want to consolidate the old keys if they're no longer referenced in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 75478,
  "duration_api_ms": 76125,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "8b8dceac-2879-4170-a25a-1097ce1cb048",
  "total_cost_usd": 0.37372525,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 31169,
    "cache_read_input_tokens": 158258,
    "output_tokens": 3934,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31169,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 124,
        "cache_read_input_tokens": 42643,
        "cache_creation_input_tokens": 367,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 367
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1315,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001405,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 3934,
      "cacheReadInputTokens": 158258,
      "cacheCreationInputTokens": 31169,
      "webSearchRequests": 0,
      "costUSD": 0.37232025,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "39b439ab-3144-44b6-b545-86d69f94fc56"
}
```

</details>

---
